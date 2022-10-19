# NAMD instructions

-   [NAMD web site](https://www.ks.uiuc.edu/Research/namd/)
    
Building NAMD can be tricky as it first builds Charm++ and then compiles
NAMD with it.

## EasyBuild

-   [NAMD in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/n/NAMD)
    

### Versions 2.12 and 2.14 from binaries

-   UAntwerpen EasyConfig where for now we simply download from binaries after
    problems trying to build NAMD ourselves.

-   When we tried 2.12 with the version of EasyBuild from 2017, it turned out
    that it was slower than the downloaded binaries and than our manual builds.
