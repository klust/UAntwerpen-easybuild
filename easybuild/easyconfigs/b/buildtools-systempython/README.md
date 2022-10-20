# buildtools-python instructions

This module augments buildtools with Python-based buildtools. In this module,
they use the system-installed Python 3. Since the packages need PYTHONPATH
to be set, they can conflict with software that uses EasyBuild-installed
more recent Python versions which is why they have been separated in
a separate module.


## Contents

The contents of the module evolved over time. It does contain a subset of:
* Meson 
    * [version check on PyPi](https://pypi.org/project/meson/#history)
    * [Meson in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/m/Meson)
* SCons
    * [Version check on PyPi](https://pypi.org/project/SCons/#history)
    * [SCons in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/s/SCons)


## EasyBuild

This module is a UAntwerpen development.


### Version 2022a

-   New EasyConfig, UAntwerpen-design, derived from the older buildtools
    versions that contained support for Meson and SCons.

Versions used:
-   Meson: 0.61.5 as that is the last version supporting Python 3.6.
-   SCons: 4.0.1 as later versions gave problems, likely with the distutils
    package on the system.

  