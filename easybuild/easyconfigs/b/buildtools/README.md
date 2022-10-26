# buildtools module

Buildtools is a collection of various build tools installed in a single module and 
directory tree. We update it once with every toolchain and give it a version number 
based on the toolchain.

The original setup was to only include executables and not libraries. However, that 
created a build dependency on sufficiently recent versions of Bison 3.0 and flex, so 
we decided to include them also even though they provide libraries that we may want 
to compile with a more recent GCC when used in applications (though I expect that 
even then those libraries will only be used on a non-performance-critical part of 
the code, I would expect in I/O. And by specifying other flex and/or Bison modules 
in the right order when building those applications, we may even totally avoid 
these problems.


## Contents

The contents of the module evolved over time. It does contain a subset of:

* [byacc (Berkeley Yacc)](https://invisible-island.net/byacc/byacc.html) 
    * [version check download location](https://invisible-mirror.net/archives/byacc/)
    * [byacc in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/b/byacc)
* [flex (Fast LEXical analyzer generator](https://sourceforge.net/projects/flex/) 
    * [version check GitHub](https://github.com/westes/flex/releases)
    * [flex in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/f/flex)
* [git](https://git-scm.com/)  
    * [version check GitHub](https://github.com/git/git/tags)
    * [git in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/g/git)
* [GNU Autoconf](https://www.gnu.org/software/autoconf/) 
    * [version check download location](http://ftp.gnu.org/gnu/autoconf/)
    * [Autoconf in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/a/Autoconf)
* [GNU Automake](https://www.gnu.org/software/automake/automake.html)
    * [version check download location](http://ftp.gnu.org/gnu/automake/)
    * [Automake in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/a/Automake)
* [GNU Autoconf-archive](https://www.gnu.org/software/autoconf-archive)
    * [version check download location](https://ftp.gnu.org/gnu/autoconf-archive/)
    * [Autoconf-archive in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/a/Autoconf-archive)
* [GNU Bison](https://www.gnu.org/software/bison) 
    * [version check on download location](https://ftp.gnu.org/gnu/bison/)
    * [Bison in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/b/Bison)
* [GNU libtool](https://www.gnu.org/software/libtool)
    * [version check on the download location](https://www.gnu.org/software/libtool/)
    * [libtool in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/l/libtool)
* [GNU M4](https://www.gnu.org/software/m4/m4.html) 
    * [version check on the download loacation](https://ftp.gnu.org/gnu/m4/)\
    * [M4 in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/m/M4)
* [GNU make](https://www.gnu.org/software/make/make.html) 
    * [version check on the download location](http://ftp.gnu.org/gnu/make/)
    * [make in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/m/make)
* [GNU sed](https://www.gnu.org/software/sed/) 
    * [version check on the download location](http://ftp.gnu.org/gnu/sed/)
    * No support for sed in the EasyBuilders repository
* [CMake](https://cmake.org/) 
    * [version check on the CMake web site](http://www.cmake.org/)
    * [Releases on the GitHub mirror of the development repository](https://github.com/Kitware/CMake/releases)
    * [CMake in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/c/CMake)
* [Ninja](https://ninja-build.org/) 
    * [version check on the Ninja web site](https://ninja-build.org/)
    * [Releases on the Ninja GitHub](https://github.com/ninja-build/ninja/releases)
    * [Ninja in the EAsyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs//n/Ninja)
* [NASM](https://www.nasm.us/) 
    * [version check on the NASM web site](http://www.nasm.us/)
    * [Releases on the NASM GitHub](https://github.com/netwide-assembler/nasm/tags)
* [Yasm](http://yasm.tortall.net/) 
    * [version check on the Yasm web site](http://yasm.tortall.net/)
    * [Releases on the Yasm GitHub](https://github.com/yasm/yasm/releases)
    * [Yasm in th EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs//y/Yasm)
* [patchelf](https://github.com/NixOS/patchelf) 
    * [version check on the download location](https://github.com/NixOS/patchelf/releases)
    * [patchelf in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs//p/patchelf)
* [pkg-config](http://www.freedesktop.org/wiki/Software/pkg-config/)
    * [version check on the download location](https://pkgconfig.freedesktop.org/releases/)
    * [pkg-config in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs//p/pkg-config)
* [GNU perf](https://www.gnu.org/software/gperf/)
    * [version check on the gperf web site](https://www.gnu.org/software/gperf/)
    * [version check on the download location](https://ftp.gnu.org/gnu/gperf/)
    * [gperf in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs//g/gperf)
* [GNU help2man](https://www.gnu.org/software/help2man/) 
    * [version check on the download location](http://ftpmirror.gnu.org/help2man/)
    * [help2man in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs//h/help2man)
* [Doxygen](https://doxygen.nl/index.html) 
    * [version check on the doxygen web site](http://www.doxygen.nl/download.html)
    * [version check on the doxugen GitHub](https://github.com/doxygen/doxygen/tags)
    * [Doxygen on the EasyBuilders web site](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/d/Doxygen)
* [re2c](https://re2c.org/)
    * [version check on the re2c GitHub](https://github.com/skvadrik/re2c/releases)
    * [re2c in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/r/re2c)
* [Meson](https://mesonbuild.com) 
    * [version check on PyPi](https://pypi.org/project/meson/#history)
    * [Meson in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/m/Meson)
* [SCons](https://www.scons.org/)
    * [Version check on PyPi](https://pypi.org/project/SCons/#history)
    * [SCons in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/s/SCons)


## EasyConfigs

### Notes

* This documentation was started when developing the 2020a version of the module.
* CMake still requires an ncurses and OpenSSL library from the system.
* There are dependencies between those packages, so sometimes the order in the 
  EasyConfig file does matter and is chosen to use the newly installed tools
  for the installation of some of the other tools in the bundle.


### 2020a

* We did notice that some GNU tools are no longer available in the tar.bz2 format and 
  instead in .tar.lz. However, since there lzip was not yet installed on our systems 
  and since there is no easy-to-recognize SOURCE_TAR_LZ or SOURCELOWER_TAR_LZ constant
  defined in EasyBuild, we do not yet use that format.
* We did add EBROOT and EBVERSION variables for all components for increased compatibility
  with standard EasysBuild-generated modules (in case those variables would, e.g., 
  be used in EasyBlocks for certain software packages).
* Added re2c and SCons to the bundle.

Versions used:

* Byacc 20191125
* Flex 2.6.4
* re2c 1.3
* git 2.26.0 
* GNU Autoconf 2.69
* GNU Automake 1.16.2
* GNU Bison 3.5.3
* GNU libtool 2.4.6
* GNU M4 1.4.18
* GNU make 4.3. Switched back to .tar.gz as there was no .tar.bz2 file anymore
* GNU sed 4.8
* CMake 3.17.0
* Ninja 1.10.0
* Meson 0.53.2
* SCons 3.1.2
* NASM 2.14.02
* Yasm 1.3.0
* patchelf 0.10
* pkg-config 0.29.2
* GNU gperf 3.1
* GNU help2man 1.47.13
* Doxygen 1.8.18


### 2022a

* Removed those packages that use the system Python and require PYTHONPATH to be
  set as they don't provide shell script wrappers: Meson and SCons. These will
  appear in `buildtools-systempython` and `buildtools-python`.
  
* Made sure that only static libraries are generated, and those are removed at the
  end of the build process to ensure that programs that use buildtools will not try
  to use those libraries when configuring.
  
Versions used:

* Byacc 20220128
* Flex 2.6.4
* git 2.36.0 (2022a uses 2.36, but upgraded to 2.36.3)
* GNU Autoconf 2.71
* GNU Automake 1.16.2
* GNU Autoconf-archive 2022.09.03
* GNU Bison 3.8.2
* GNU libtool 2.4.7
* GNU M4 1.4.19
* GNU make 4.3. Switched back to .tar.gz as there was no .tar.bz2 file anymore
* GNU sed 4.8
* CMake 3.23.4 (2022a still uses 3.23.1 but we went for the latest bugfix release at 
  the time of development)
* Ninja 1.10.2 (version used in 2022a, not the newest at time of development)
* NASM 2.15.05
* Yasm 1.3.0
* patchelf 0.15.0
* pkg-config 0.29.2
* GNU gperf 3.1
* GNU help2man 1.49.2
* Doxygen 1.9.5 (2022a uses 1.9.4, but we went for the latest bugfix release at the 
  time of development)
* re2c 2.2 (Version used in 2022a, not clear why the community did not upgrade to 3.0 
  which was out before the development of 2022a even started)






