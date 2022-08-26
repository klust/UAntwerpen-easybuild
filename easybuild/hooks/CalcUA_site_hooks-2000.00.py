#
# Hooks for CalcUA.
#
# This version: Used from LUMI/21.04 and EasyBuild 4.4.0 onwards
#
# Authors:
#   Kurt Lust, University of Antwerp
#

import os

CALCUA_SUPPORT = 'CalcUA User Support @ hpc@uantwerpen.be'

def parse_hook(ec, *args, **kwargs):
    """CalcUA parse hooks
         - Add support contact to modules installed via EasyBuild-production or EasyBuild-infrastructure.
    """

    easybuild_mode = os.environ['CALCUA_EASYBUILD_MODE']

    if easybuild_mode in ['production', 'infrastructure'] and ec['site_contacts'] == None:
        ec['site_contacts'] = CALCUA_SUPPORT


    #
    # END of parse_hook
    #
