##
# Modified by Kurt Lust to use the standard ParMETIS installation procedure using
# make config rather than calling cmake ourselves.
#
# Current deficiencies:
# * Only tested with the Intel toolchain
# * Almost certainly not yet correct for versions before version 4.
# * Building a shared library is not yet supported.
# * Somewhere in the ParMETIS code,a -O3 gets added to the compiler options so the
#   compiler options set by EasyBuild are partially overwritten.
# 
# Further extensions:
# * Define configuration parameters to set the integer and floatin point data types
#   and do this in the easyblock rather than in the easyconfig.
# * Support creating both static and shared libraries by configuring/compiling/installing
#   twice?
##
##
# Copyright 2009-2017 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://www.vscentrum.be),
# Flemish Research Foundation (FWO) (http://www.fwo.be/en)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# https://github.com/easybuilders/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
EasyBuild support for ParMETIS, implemented as an easyblock

@author: Stijn De Weirdt (Ghent University)
@author: Dries Verdegem (Ghent University)
@author: Kenneth Hoste (Ghent University)
@author: Pieter De Baets (Ghent University)
@author: Jens Timmerman (Ghent University)
"""
import os
import shutil
from distutils.version import LooseVersion

from easybuild.framework.easyblock import EasyBlock
from easybuild.tools.build_log import EasyBuildError
from easybuild.tools.filetools import mkdir
from easybuild.tools.run import run_cmd


class EB_ParMETISMOD(EasyBlock):
	"""Support for building and installing ParMETIS."""

	def configure_step(self):
		"""Configure ParMETIS build.
		For versions of ParMETIS < 4 , METIS is a seperate build
		New versions of ParMETIS include METIS
		"""
		if LooseVersion(self.version) >= LooseVersion("4"):
			# tested with 4.0.2, now actually requires cmake to be run first
			# for both parmetis and metis

			if self.toolchain.options['openmp']:
				self.cfg.update('configopts', 'openmp=1')
			else:
				self.cfg.update('configopts', 'openmp=0')

			if self.toolchain.options.get('usempi', None):
				self.cfg.update('configopts', 'cc=%s' % (os.getenv('MPICC')) )
				self.cfg.update('configopts', 'cxx=%s' % (os.getenv('MPICXX')) )

			self.parmetis_builddir = 'build'
			try:
				cmd = "%s make config %s prefix=%s BUILDDIR=build" % (self.cfg['preconfigopts'], self.cfg['configopts'], self.installdir)
				run_cmd(cmd, log_all=True, simple=True)
				os.chdir(self.cfg['start_dir'])
			except OSError as err:
				raise EasyBuildError("Running make config in %s failed: %s", self.parmetis_builddir, err)
		else:
			raise EasyBuildError("ParMETIS versions before version 4 not fully supported by this EasyBlock.")

	def build_step(self, verbose=False):
		"""Build ParMETIS (and METIS) using build_step."""

		if self.cfg['parallel']:
			paracmd = "-j %s" % self.cfg['parallel']
		else:
			paracmd = ''

		cmd = "%s make %s %s BUILDDIR=build" % (self.cfg['prebuildopts'], paracmd, self.cfg['buildopts'])

		try:
			run_cmd(cmd, log_all=True, simple=True, log_output=verbose)
		except OSError as err:
			raise EasyBuildError("Running cmd '%s' failed: %s", cmd, err)

	def install_step(self):
		"""
		Install by copying files over to the right places.

		Also create symlinks where expected by other software (Lib directory).
		"""
		includedir = os.path.join(self.installdir, 'include')
		libdir = os.path.join(self.installdir, 'lib')

		if LooseVersion(self.version) >= LooseVersion("4"):
			# includedir etc changed in v4, use a normal make install
			cmd = "make install %s BUILDDIR=build" % self.cfg['installopts']
			try:
				run_cmd(cmd, log_all=True, simple=True)
				os.chdir(self.cfg['start_dir'])
			except OSError as err:
				raise EasyBuildError("Running '%s' in %s failed: %s", cmd, self.parmetis_builddir, err)

			# libraries: make install does not install libmetis.a
			try:
				src = os.path.join(self.cfg['start_dir'], 'build' ,'libmetis' ,'libmetis.a')
				dst = os.path.join(libdir, 'libmetis.a')
				shutil.copy2(src, dst)
			except OSError as err:
				raise EasyBuildError("Copying files to installation dir failed: %s", err)

			# include files: make install does not copy metis.h though this is read by
            # parmetis.h, and the accuracy of the data types is defined in metis.h.
			try:
				src = os.path.join(self.cfg['start_dir'], 'build', 'metis', 'include', 'metis.h')
				dst = os.path.join(includedir, 'metis.h')
				shutil.copy2(src, dst)
			except OSError as err:
				raise EasyBuildError("Copying files to installation dir failed: %s", err)

		else:
			mkdir(libdir)
			mkdir(includedir)

			# libraries
			try:
				for fil in ['libmetis.a', 'libparmetis.a']:
					src = os.path.join(self.cfg['start_dir'], fil)
					dst = os.path.join(libdir, fil)
					shutil.copy2(src, dst)
			except OSError as err:
				raise EasyBuildError("Copying files to installation dir failed: %s", err)

			# include files
			try:
				src = os.path.join(self.cfg['start_dir'], 'parmetis.h')
				dst = os.path.join(includedir, 'parmetis.h')
				shutil.copy2(src, dst)
				# some applications (SuiteSparse) can only use METIS (not ParMETIS), but header files are the same
				dst = os.path.join(includedir, 'metis.h')
				shutil.copy2(src, dst)
			except OSError as err:
				raise EasyBuildError("Copying files to installation dir failed: %s", err)

		# other applications depending on ParMETIS (SuiteSparse for one) look for both ParMETIS libraries
		# and header files in the Lib directory (capital L). The following symlink are hence created.
		try:
			llibdir = os.path.join(self.installdir, 'Lib')
			os.symlink(libdir, llibdir)
			for f in ['metis.h', 'parmetis.h']:
				os.symlink(os.path.join(includedir, f), os.path.join(libdir, f))
		except OSError as err:
			raise EasyBuildError("Something went wrong during symlink creation: %s", err)

		# Copy the manual
		try:
			manualdir = os.path.join(self.installdir, 'manual')
			mkdir(manualdir)
			src = os.path.join(self.cfg['start_dir'], 'manual/manual.pdf')
			dst = os.path.join(manualdir, 'manual.pdf')
			shutil.copy2(src, dst)
		except OSError as err:
			raise EasyBuildError("Copying the manual (manual/manual.pdf) failed: %s", err)

		# Copy the LICENSE.txt file
		try:
			src = os.path.join(self.cfg['start_dir'], 'LICENSE.txt')
			dst = os.path.join(self.installdir, 'LICENSE.txt')
			shutil.copy2(src, dst)
		except OSError as err:
			raise EasyBuildError("Copying LICENSE.txt failed: %s", err)

	def sanity_check_step(self):
		"""Custom sanity check for ParMETIS."""

		custom_paths = {
						'files': ['include/%smetis.h' % x for x in ["", "par"]] +
								 ['lib/lib%smetis.a' % x for x in ["", "par"]],
						'dirs':['Lib']
					   }

		super(EB_ParMETISMOD, self).sanity_check_step(custom_paths=custom_paths)
