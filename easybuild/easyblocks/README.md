# Custom UAntwerpen EasyBlocks

*This list is still very incomplete.*

## rmpi.py - Rmpi R package

  * This is an empty EasyBlock to overwrite the default one from EasyBuild
    as we prefer to set the `--configure-args` flag by hand. (The value generated
    by the default EasyBlock is wrong on our system.)

## xml.py - XML R package

  * This is an empty EasyBlock as the default one does not work on our system
    (since we include zlib in baselibs and don't set EBROOTZLIB since some of
    these variables in baselibs cause trouble with EasyBuild).

