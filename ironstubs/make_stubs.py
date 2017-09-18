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

import os
import sys
import json
import time
from collections import defaultdict
from pprint import pprint
import importlib

import clr
import System

# Ensure Proper CWD is set. This ensure proper running from within Revit
# os.chdir(os.path.dirname(__file__))
from utils.logger import logger
from generator3.generator3 import process_one


def is_namespace(something):
    """ Returns True if object is Namespace: Module """
    if isinstance(something, type(System)):
        return True

def iter_module(module_name, module, module_path=None, namespaces=None):
    """
    Recursively iterate through all namespaces in assembly
    """
    if not namespaces:
        namespaces = {}

    for submodule_name, submodule in vars(module).iteritems():
        if not is_namespace(submodule):
            continue
        if module_path:
            submodule_path = '.'.join([module_path, submodule_name])
        else:
            submodule_path = submodule_name
        namespaces[submodule_path] = repr(submodule)
        iter_module(submodule_name, submodule, submodule_path,
                    namespaces=namespaces)
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

def crawl_loaded_references(assemblies):
    """ Crawl Loaded assemblies to get Namespaces. """
    namespaces_dict = {}
    for assembly in clr.References:
        assembly_name = assembly.GetName().Name
        assembly_path = assembly.CodeBase
        assembly_filename = os.path.basename(assembly_path)
        if assembly_name in assemblies:
            logger.info('Parsing Assembly: {}'.format(assembly_name))
            namespaces_dict[assembly_filename] = iter_module(assembly_name, assembly)
        else:
            logger.warning('Assembly Skiped. Not in target list: {}'.format(assembly_name))
    return namespaces_dict

def crawl_builtin_modules(builtin_modules):
    """ Crawl Built in  Modules """
    builtin_dict = {}
    for module_name in builtin_modules:
        importlib.import_module(module_name)
        builtin_dict[module_name] = str(sys.modules[module_name])
    return builtin_dict

def stub_exists(output_dir, module_path):
    """ Check if Stub exists """
    path = os.path.join(output_dir, *module_path.split('.'))
    exists = os.path.exists(path) or os.path.exists(path + '.py')
    return exists

def create_stubs(output_dir, module_path):
    """ Actually Make Stubs """
    try:
        logger.info('Processing [{}]'.format(module_path))
        logger.info('='*30)
        process_one(module_path, None, True, output_dir)
    except Exception as errmsg:
        logger.error('Could not process module_path: {}'.format(module))
        logger.error(errmsg)
    else:
        logger.info('Done')
    logger.info('='*30)

def delete_module(module_path):
    try:
        del sys.modules[module_path]
    except:
        logger.info('Could not delete: {}'.format(module_path))
    else:
        logger.info('Deleted Module: {}'.format(module_path))

def create_json(output_dir, namespaces_dict):
    now = str(time.time()).split('.')[0]
    filepath = os.path.join(output_dir, '{}-{}.json'.format(output_dir, now))
    with open(filepath, 'w') as fp:
        json.dump(namespaces_dict, fp, indent=2)

def make(output_dir, assemblies=None, builtins=None, overwrite=False):
    # TODO: Handle assemblies or builtins automatically

    namespaces_to_process = {}
    if assemblies:
        load_assemblies(assemblies)
        namespaces_dict = crawl_loaded_references(assemblies)
        namespaces_to_process.update(namespaces_dict)
    if builtins:
        builtins_dict = crawl_builtin_modules(builtins)
        namespaces_to_process.update({'__builtins__': builtins_dict})

    if not namespaces_to_process:
        raise Exception('No namspaces to process')

    logger.info('#'*30)
    logger.info('Modules and Assemblies Loaded: ')
    logger.info([v.keys() for v in namespaces_to_process.values()])
    logger.debug( json.dumps(namespaces_dict, indent=2, sort_keys=True))

    if raw_input('>>> Write Stubs ({}) [y/n] [n]:\n>>> '.format(output_dir)) != 'y':
        logger.info('No Stubs Created')
    else:
        for assembly, modules in namespaces_dict.items():
            for module_path in modules.keys():
                if not stub_exists(output_dir, module_path) or overwrite:
                    create_stubs(output_dir, module_path)
                    delete_module(module_path)
                else:
                    logger.info('Skipping [{}]'.format(module_path))
        logger.info('Stubs Created')
        create_json(output_dir, namespaces_dict)








