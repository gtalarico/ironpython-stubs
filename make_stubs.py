""" Stub Generator for IronPython

Extended script based on script developed by Gary Edwards at:
gitlab.com/reje/revit-python-stubs

This is uses a slightly modify version of generator3,
github.com/JetBrains/intellij-community/blob/master/python/helpers/generator3.py

Iterates through a list of targeted assemblies and generates stub directories
for the namespaces using pycharm's generator3.

Note:
    Some files ended up too large for Jedi to handle and would cause
    memory errors and crashes - 1mb+ in a single files was enough to
    cause problems. To fix this, there is a separate module that creates
    a compressed version of the stubs, but it also split large file
    into separate files to deal with jedi.
    These directories will show up in the stubs as (X_parts)


MIT LICENSE
https://github.com/gtalarico/ironpython-stubs
Gui Talarico
"""

__version__ = '0.2.0'

import os
import sys
import json
from collections import defaultdict
from pprint import pprint

import clr
import System

# Ensure Proper CWD is set. This ensure proper running from within Revit
# os.chdir(os.path.dirname(__file__))
from config import PROJECT_DIR, SYS_PATHS, STUBS_DIR, STUBS_JSON_DIR
from config import LOADABLE_ASSEMBLIES, BUILTIN_MODULES
from config import OVERWRITE_EXISTING
from logger import logger
from generator3.generator3 import process_one

# Add Paths
[sys.path.append(p) for p in SYS_PATHS]

def is_namespace(something):
    """ Returns True if object is Namespace: Module """
    if isinstance(something, type(System)):
        return True


def run():

    def iter_module(module_name, module, module_path=None, namespaces=None):
        """
        Recursively iterate through all namespaces in assembly
        Returns namespaces dictionary
        namespaces[module_name] = {}
        """
        if not namespaces:
            namespaces = defaultdict(dict)

        for submodule_name, submodule in vars(module).iteritems():
            if not is_namespace(submodule):
                continue
            if module_path:
                submodule_path = '.'.join([module_path, submodule_name])
            else:
                submodule_path = submodule_name
            flat_namespaces[submodule_path] = repr(module)
            namespaces[module_name].update({submodule_name: repr(submodule)})
            iter_module(submodule_name, submodule, submodule_path, namespaces=namespaces)
        return namespaces

    def load_assemblies(assemblies):
        """ Load Assemblies using clr.AddReference """
        for assembly_name in assemblies:
            logger.info('='*30)
            try:
                logger.info('Adding Assembly [{}]'.format(assembly_name))
                clr.AddReference(assembly_name)
            except Exception as errmsg:
                logger.error('Could not load assembly: {}'.format(assembly_name))
                logger.error(errmsg)
            else:
                logger.info('Loaded [{}]'.format(assembly_name))

    def crawl_loaded_references():
        """ CRAWL ASSEMBLIES TO GET ALL NAMESPACES """
        for assembly in clr.References:
            assembly_name = assembly.GetName().Name
            assembly_path = assembly.CodeBase
            assembly_filename = os.path.basename(assembly_path)
            if assembly_name in LOADABLE_ASSEMBLIES:
                logger.info('Parsing Assembly: {}'.format(assembly_name))
                namespaces = iter_module(assembly_name, assembly)
                master_namespaces[assembly_filename] = namespaces
            else:
                logger.warning('*** Assembly Skiped. Not in target list: {}'.format(assembly_name))

    def make_stubs():
        """ Actually Make Stubs """

        for namespace in sorted(flat_namespaces.keys()):

            # Skip if exists and
            path = os.path.join(STUBS_DIR, *namespace.split('.'))
            exists = os.path.exists(path) or os.path.exists(path + '.py')
            if exists and not OVERWRITE_EXISTING:
                logger.info('Skipping [{}]'.format(namespace))
                continue
            try:
                logger.info('Processing [{}]'.format(namespace))
                logger.info('='*30)
                process_one(namespace, None, True, STUBS_DIR)
            except Exception as errmsg:
                logger.error('Could not process namespace: {}'.format(module))
                logger.error(errmsg)
            else:
                logger.info('Done')
            logger.info('='*30)

        for module in BUILTIN_MODULES:
            process_one(module, None, True, STUBS_DIR)

    master_namespaces = {}
    flat_namespaces = {}
    load_assemblies(LOADABLE_ASSEMBLIES)
    logger.info('>>> Assemblies Loaded. Crawling Modules')
    crawl_loaded_references()

    print( json.dumps(master_namespaces, indent=4))
    print( json.dumps(flat_namespaces, indent=4))
    # logger.info( json.dumps(flat_namespaces, indent=4, sort_keys=True))
    # print( json.dumps(flat_namespaces, indent=4, sort_keys=True))
    with open('stubs2.json', 'w') as fp:
        json.dump(master_namespaces, fp, indent=4)

    if raw_input('Write Stubs ({}) [y] ?'.format(STUBS_DIR)) == 'y':
        make_stubs()
        print('Stubs Created')
    else:
        print('No Stubs Created')

run()








