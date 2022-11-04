# EasyBuild instructions

-   [EasyBuild website](https://easybuild.io/)
    
    
## EasyBuild

-   [EasyBuild in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/e/EasyBuild)
    
    
### 4.5.3 used for 2020a rebuild

The EasyConfig is based on the EasyBuilders one but with several modifications:

-   Adapted the documentation to our needs.
    
-   Use our own EasyBlock as we needed to disable an old part of the code that did not
    work for us, but we should revisit that as the EasyBlock is also evolving.
    
-   Used the extensions mechanism to install a bunch of additional packages to
    enable the archspec support and the progress bar.
    
    
### 4.6.2 used for system and 2022a

-   Straightforward port of the 4.5.3 EasyConfig.
    
