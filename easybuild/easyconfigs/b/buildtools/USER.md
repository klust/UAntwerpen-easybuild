# Usage of buildtools

Buildtools is a module meant to replace several separate build tools.
It is designed to make it easy to create a more reproducible build environment
by including it in the `builddependencies` of an EasyConfig. The binaries do 
depend on some system libraries, but the module does try to minimise the surface
of interaction with the system and the software being installed to minimise the
chance that the build tools influence the configuration process of the software
installation process.

In the 2022a version, all tools depending on Python have been removed as they 
turn out to interfer with packages being installed with newer Python versions. 
These tools now come in a separate module, `buildtoold-python`, that can be
rebuild for each Python implementation.

The version number refers to the calcua software stack for which it is meant.

Tools included:

-   [byacc (Berkeley Yacc)](https://invisible-island.net/byacc/byacc.html)

-   [flex (Fast LEXical analyzer generator](https://sourceforge.net/projects/flex/)

-   [git](https://git-scm.com/) 

-   [GNU Autoconf](https://www.gnu.org/software/autoconf/)

-   [GNU Automake](https://www.gnu.org/software/automake/automake.html)

-   [GNU Autoconf-archive](https://www.gnu.org/software/autoconf-archive)

-   [GNU Bison](https://www.gnu.org/software/bison)

-   [GNU libtool](https://www.gnu.org/software/libtool)

-   [GNU M4](https://www.gnu.org/software/m4/m4.html)

-   [GNU make](https://www.gnu.org/software/make/make.html)

-   [GNU sed](https://www.gnu.org/software/sed/)

-   [CMake](https://cmake.org/)

-   [Ninja](https://ninja-build.org/)

-   [NASM](https://www.nasm.us/)

-   [Yasm](http://yasm.tortall.net/)

-   [patchelf](https://github.com/NixOS/patchelf)

-   [pkg-config](http://www.freedesktop.org/wiki/Software/pkg-config/)

-   [GNU perf](https://www.gnu.org/software/gperf/)

-   [GNU help2man](https://www.gnu.org/software/help2man/)

-   [Doxygen](https://doxygen.nl/index.html)

-   [re2c](https://re2c.org/)

-   [Meson](https://mesonbuild.com) (2020a only)

-   [SCons](https://www.scons.org/) (2020a only)

