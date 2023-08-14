import os
import re

from easybuild.tools.module_naming_scheme.mns import ModuleNamingScheme

from easybuild.tools.module_naming_scheme.hierarchical_mns import HierarchicalMNS, COMP_NAME_VERSION_TEMPLATES
from easybuild.tools.module_naming_scheme.hierarchical_mns import CORE, COMPILER, MPI
from easybuild.tools.module_naming_scheme.hierarchical_mns import MODULECLASS_COMPILER, MODULECLASS_MPI

class ExampleMNS(ModuleNamingScheme):
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

class LowerHierarchicalMNS(HierarchicalMNS):
    """ HierarchicalMNS but with lowercase module names. """

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
        """
        Determine whether the specified (short) module name is a module for software with the specified name.
        Default implementation checks via a strict regex pattern, and assumes short module names are of the form:
            <name>/<version>[-<toolchain>]
        """

        modname_regex = re.compile('^%s/\S+$' % re.escape(name.lower()))
        res = bool(modname_regex.match(short_modname.lower()))

        self.log.debug("Checking whether '%s' is a module name for software with name '%s' via regex %s: %s",
                       short_modname, name, modname_regex.pattern, res)

        return res


    pass
