# Java instructions

-   [Java home page](https://java.com/)

-   [OpenJDK home page](http://openjdk.java.net)

-   [Adoptium project](https://github.com/adoptium/)

The current Java modules at UAntwerpen are taken from the OpenJDK distribution 
[Adoptium](https://github.com/adoptium/) managed by the Eclipse community.
The Adoptium Temurin builds are recommended by [whichjdk.com](https://whichjdk.com/).

We use the standard EasyBuild recipes with enhanced documentation. The purpose of this
setup is to make it easy to install new subversions that fix security problems without
having to change any of the EasyConfigs of packages that use Java, yet have a fully
automated installation procedure. So EasyConfigs should refer to, e.g., Java/11 as
a dependency and not, e.g., Java/11.0.16, and users should also simply use Java/11
to load whatever Jave 11 version is considered to be the safer one by system staff.

Note that Java distinguishes between long tem support versions and feature versions.
We prefer to only offer long term support versions in the central software stack,
but users are free to install other versions via the EasyBuild-user module.

As of October 2022, the LTS versions are:

-   8: Official unpaid support ended, though some distributions still provide new
    patches. Not recommended anymore.
    
-   11: Launched in September 2018

-   17: Launched in September 2021


## EasyBuild

-    [Java support in the EasyBuilders repository](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/j/Java)


### Java/8 (currently 8.345) for 2020a

-   Standard EasyConfigs with some improvements to the documentation.


### Java/11 (currently 11.0.16) for 2020a and 2022a

-   Standard EasyConfigs with some improvements to the documentation.


### Java/17 (currently 17.0.4) for 2022a

-   Standard EasyConfigs with some improvements to the documentation.


