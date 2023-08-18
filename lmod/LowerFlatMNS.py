import os
import re

from easybuild.tools.module_naming_scheme.mns import ModuleNamingScheme

class LowerFlatMNS(ModuleNamingScheme):
    """ Example from tutorial http://tutorial.easybuild.io/2023-eb-eessi-uk-workshop/easybuild-module-naming-schemes/ """

    REQUIRED_KEYS = ['name', 'version', 'versionsuffix', 'toolchain']

    def det_full_module_name(self, ec):
        """
        Determine full module name:
        - all lowercase
        - replace all dashes with underscores
        """
        parts = [ec['version']]

        # versionsuffix directly after version (but only if it's not empty)
        if ec['versionsuffix']:
            parts.append(ec['versionsuffix'])

        # only add toolchain name/version for non-system toolchain
        tc = ec['toolchain']
        if tc['name'].lower() != 'system':
            parts.extend([tc['name'], tc['version']])

        modname = ec['name'] + '/' + '_'.join(parts)

        modname = modname.replace('-', '_').replace('__', '_')

        return modname.lower()

    def is_short_modname_for(self, short_modname, name):
        """Determine whether short module name is a module for the software with specified name."""
        return short_modname.startswith(name.lower().replace('-', '_') + '/')
    pass # end class

