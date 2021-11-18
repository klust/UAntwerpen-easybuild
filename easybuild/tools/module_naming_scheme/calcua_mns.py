import os

from easybuild.tools.module_naming_scheme.easybuild_mns import EasyBuildMNS


class CalcUAMNS(EasyBuildMNS):

    def det_module_symlink_paths(self, ec):
        """
        Determine list of paths in which symlinks to module files must be created.
        """
        # no longer make symlinks from moduleclass sudirectory of $MODULEPATH
        return []
