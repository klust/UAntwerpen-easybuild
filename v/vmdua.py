##
# Copyright 2009-2019 Ghent University
# Copyright 2015-2016 Stanford University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
EasyBuild support for VMD, implemented as an easyblock

@author: Stephane Thiell (Stanford University)
@author: Kenneth Hoste (HPC-UGent)
@author: Kurt Lust (UAntwerp)
"""
import os
import shutil

from distutils.version import LooseVersion
from easybuild.easyblocks.generic.configuremake import ConfigureMake
from easybuild.easyblocks.generic.pythonpackage import det_pylibdir
from easybuild.framework.easyconfig import CUSTOM
from easybuild.tools.build_log import EasyBuildError
from easybuild.tools.filetools import change_dir, copy_file, extract_file
from easybuild.tools.run import run_cmd
from easybuild.tools.modules import get_software_root, get_software_version
import easybuild.tools.environment as env
import easybuild.tools.toolchain as toolchain


class EB_VMDUA(ConfigureMake):
    """Easyblock for building and installing VMD (UAntwerp modifications)"""

    def __init__(self, *args, **kwargs):
        """Initialize VMD-specific variables."""
        super(EB_VMDUA, self).__init__(*args, **kwargs)
        # source tarballs contains a 'plugins' and 'vmd-<version>' directory
        self.vmddir = os.path.join(self.builddir, '%s-%s' % (self.name.lower(), self.version))
        self.surf_dir = os.path.join(self.vmddir, 'lib', 'surf')
        self.stride_dir = os.path.join(self.vmddir, 'lib', 'stride')

    @staticmethod
    def extra_options(extra_vars=None):
        """Define custom easyconfig parameters for VMD."""
        extra_vars = ConfigureMake.extra_options(extra_vars)
        extra_vars.update({
            'vmd_arch':       ['LINUXAMD64', "VMD architecture string to use, default is LINUXAMD64", CUSTOM],
            'vmd_extra_opts': [ '',          "Extra options to pass to the VMD configure process",    CUSTOM],
        })
        return extra_vars

    def extract_step(self):
        """Custom extract step for VMD."""
        super(EB_VMDUA, self).extract_step()

        if LooseVersion(self.version) >= LooseVersion("1.9.3"):
            change_dir(self.surf_dir)
            extract_file('surf.tar.Z', os.getcwd())

    def configure_step(self):
        """
        Configure VMD for building.
        """
        # make sure required dependencies are available
        deps = {}
        for dep in ['FLTK', 'Mesa', 'Tcl', 'Tk']:
            deps[dep] = get_software_root(dep)
            if deps[dep] is None:
                raise EasyBuildError("Required dependency %s is missing", dep)

        # optional dependencies
        for dep in ['ACTC', 'CUDA', 'OptiX', 'Python', 'netCDF']:
            deps[dep] = get_software_root(dep)

        # specify Tcl/Tk locations & libraries
        tclinc = os.path.join(deps['Tcl'], 'include')
        tcllib = os.path.join(deps['Tcl'], 'lib')
        env.setvar('TCL_INCLUDE_DIR', tclinc)
        env.setvar('TCL_LIBRARY_DIR', tcllib)

        env.setvar('TK_INCLUDE_DIR', os.path.join(deps['Tk'], 'include'))
        env.setvar('TK_LIBRARY_DIR', os.path.join(deps['Tk'], 'lib'))

        tclshortver = '.'.join(get_software_version('Tcl').split('.')[:2])
        self.cfg.update('buildopts', 'TCLLDFLAGS="-ltcl%s"' % tclshortver)

        # Netcdf locations, in theory an optional component, however some of the plugins require it.
        if deps['netCDF']:
            netcdfinc = os.path.join(deps['netCDF'], 'include')
            netcdflib = os.path.join(deps['netCDF'], 'lib')
            netcdfopt = ' '.join([
                "NETCDFINC='-I%s'" % netcdfinc,
                "NETCDFLIB='-L%s'" % netcdflib,
                ])
        else:
            netcdfopt = ''
            # Change the following code once we find how to build without netCDF.
            raise EasyBuildError("Even though the VMD manual mentions netCDF as an optional component, it is currently required for building the plugins which this VMD EasyBlock always does.")

        # Python locations
        if deps['Python']:
            pyshortver = '.'.join(get_software_version('Python').split('.')[:2])
            pyvermajor = get_software_version('Python').split('.')[0]
            if pyvermajor == '2':
                env.setvar('PYTHON_INCLUDE_DIR', os.path.join(deps['Python'], 'include/python%s' % pyshortver))
            else:
                env.setvar('PYTHON_INCLUDE_DIR', os.path.join(deps['Python'], 'include/python%sm' % pyshortver))
            pylibdir = det_pylibdir()
            python_libdir = os.path.join(deps['Python'], os.path.dirname(pylibdir))
            env.setvar('PYTHON_LIBRARY_DIR', python_libdir)

            # numpy include location, easiest way to determine it is via numpy.get_include()
            out, ec = run_cmd("python -c 'import numpy; print( numpy.get_include() )'", simple=False)
            if ec:
                raise EasyBuildError("NumPy support expected when using Python, but failed to determine NumPy include directory: %s", out)
            else:
                env.setvar('NUMPY_INCLUDE_DIR', out.strip())

        # compiler commands
        self.cfg.update('buildopts', 'CC="%s"' % os.getenv('CC'))
        self.cfg.update('buildopts', 'CCPP="%s"' % os.getenv('CXX'))

        # plugins need to be built first (see http://www.ks.uiuc.edu/Research/vmd/doxygen/compiling.html)
        change_dir(os.path.join(self.builddir, 'plugins'))
        cmd = ' '.join([
            'make',
            self.cfg.get('vmd_arch'),
            "TCLINC='-I%s'" % tclinc,
            "TCLLIB='-L%s'" % tcllib,
            "TCLLDFLAGS='-ltcl%s'" % tclshortver,
            netcdfopt,
            self.cfg['buildopts'],
        ])
        run_cmd(cmd, log_all=True, simple=False)

        # create plugins distribution
        plugindir = os.path.join(self.vmddir, 'plugins')
        env.setvar('PLUGINDIR', plugindir)
        self.log.info("Generating VMD plugins in %s", plugindir)
        run_cmd("make distrib %s" % self.cfg['buildopts'], log_all=True, simple=False)

        # explicitely mention whether or not we're building with CUDA/OptiX support
        if deps['CUDA']:
            self.log.info("Building with CUDA %s support", get_software_version('CUDA'))
            if deps['OptiX']:
                self.log.info("Building with Nvidia OptiX %s support", get_software_version('OptiX'))
            else:
                self.log.warn("Not building with Nvidia OptiX support!")
        else:
            self.log.warn("Not building with CUDA nor OptiX support!")

        # see http://www.ks.uiuc.edu/Research/vmd/doxygen/configure.html
        # LINUXAMD64: Linux 64-bit
        # LP64: build VMD as 64-bit binary
        # IMD: enable support for Interactive Molecular Dynamics (e.g. to connect to NAMD for remote simulations)
        # PTHREADS: enable support for POSIX threads
        # COLVARS: enable support for collective variables (related to NAMD/LAMMPS)
        # NOSILENT: verbose build command
        self.cfg.update('configopts', self.cfg.get('vmd_arch') + " LP64 IMD PTHREADS COLVARS NOSILENT " + self.cfg.get('vmd_extra_opts'), allow_duplicate=False)

        # add additional configopts based on available dependencies
        for key in deps:
            if deps[key]:
                if key == 'Mesa':
                    self.cfg.update('configopts', "OPENGL MESA", allow_duplicate=False)
                elif key == 'OptiX':
                    self.cfg.update('configopts', "LIBOPTIX", allow_duplicate=False)
                elif key == 'Python':
                    self.cfg.update('configopts', "PYTHON NUMPY", allow_duplicate=False)
                else:
                    self.cfg.update('configopts', key.upper(), allow_duplicate=False)

        # configure for building with Intel compilers specifically
        if self.toolchain.comp_family() == toolchain.INTELCOMP:
            self.cfg.update('configopts', 'ICC', allow_duplicate=False)

        # specify install location using environment variables
        env.setvar('VMDINSTALLBINDIR', os.path.join(self.installdir, 'bin'))
        env.setvar('VMDINSTALLLIBRARYDIR', os.path.join(self.installdir, 'lib'))

        # configure in vmd-<version> directory
        change_dir(self.vmddir)
        run_cmd("%s ./configure %s" % (self.cfg['preconfigopts'], self.cfg['configopts']))

        # change to 'src' subdirectory, ready for building
        change_dir(os.path.join(self.vmddir, 'src'))

    def build_step(self):
        """Custom build step for VMD."""
        super(EB_VMDUA, self).build_step()

        self.have_stride = False
        # Build Surf, which is part of VMD as of VMD version 1.9.3
        if LooseVersion(self.version) >= LooseVersion("1.9.3"):
            change_dir(self.surf_dir)
            surf_build_cmd = 'make CC="%s" OPT="%s"' % (os.environ['CC'], os.environ['CFLAGS'])
            run_cmd(surf_build_cmd)
            # Build Stride if it was downloaded
            if os.path.exists(os.path.join(self.stride_dir, 'Makefile')):
                change_dir(self.stride_dir)
                self.have_stride = True
                stride_build_cmd = 'make CC="%s" CFLAGS="%s"' % (os.environ['CC'], os.environ['CFLAGS'])
                run_cmd(stride_build_cmd)
            else:
                self.log.info("Stride has not been downloaded and/or unpacked.")

    def install_step(self):
        """Custom build step for VMD."""

        # Install must also be done in 'src' subdir
        change_dir(os.path.join(self.vmddir, 'src'))
        super(EB_VMDUA, self).install_step()

        if LooseVersion(self.version) >= LooseVersion("1.9.3"):
            surf_bin = os.path.join(self.surf_dir, 'surf')
            copy_file(surf_bin, os.path.join(self.installdir, 'lib', 'surf_LINUXAMD64'))
            if self.have_stride:
                stride_bin = os.path.join(self.stride_dir, 'stride')
                copy_file(stride_bin, os.path.join(self.installdir, 'lib', 'stride_LINUXAMD64'))

    def sanity_check_step(self):
        """Custom sanity check for VMD."""
        custom_paths = {
            'files': ['bin/vmd'],
            'dirs': ['lib'],
        }
        super(EB_VMDUA, self).sanity_check_step(custom_paths=custom_paths)
