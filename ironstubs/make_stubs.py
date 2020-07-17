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

scriptOverrideables = {}

import re
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


def load_assemblies(assembly_name):
    """ Load Assemblies using clr.AddReference """
    try:
        logger.info('Adding Assembly [{}]'.format(assembly_name))
        clr.AddReference(assembly_name)
    except Exception as errmsg:
        logger.error('Could not load assembly: {}'.format(assembly_name))
        logger.error(errmsg)
    else:
        logger.info('Loaded [{}]'.format(assembly_name))


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


def crawl_loaded_references(target_assembly_name):
    """ Crawl Loaded assemblies to get Namespaces. """
    namespaces_dict = {}
    for assembly in clr.References:
        assembly_name = assembly.GetName().Name
        assembly_path = assembly.CodeBase
        types = assembly.GetTypes()
        methods = []
        for typ in types:
            methods.append(typ.GetMethods())
        for method in methods:
            for sub in method:
                custom = sub.GetCustomAttributes(True)
                for i in custom:
                    try:
                        if "scriptoverridableattribute" in i.ToString().lower():
                            print "true"
                            regex = "[\s\S]*] ([\s\S]*)\("
                            override = re.findall(regex, sub.ToString())[0]
                            scriptOverrideables[override] = True
                    except Exception as e:
                        print "boo"
                        print e
                # if len(custom) > 0:
                #     print sub.GetCustomAttributes(type(ScriptOverridableAttribute()), True).Length > 0
                # if sub.GetCustomAttributes(type("ScriptOverridableAttribute"), True).Length > 0:
                #     print sub.GetCustomAttributes(True)
        assembly_filename = os.path.basename(assembly_path)
        if assembly_name == target_assembly_name:
            logger.info('Parsing Assembly: {}'.format(assembly_name))
            namespaces_dict[assembly_filename] = iter_module(assembly_name, assembly)
        else:
            logger.debug('Assembly Skipped. Not in target list: {}'.format(assembly_name))
    return namespaces_dict


def stub_exists(output_dir, module_path):
    """ Check if Stub exists """
    path = os.path.join(output_dir, *module_path.split('.'))
    exists = os.path.exists(path) or os.path.exists(path + '.py')
    return exists

def create_stubs(output_dir, module_path):
    """ Actually Make Stubs """
    try:
        logger.info('='*30)
        logger.info('Processing [{}]'.format(module_path))
        process_one(module_path, None, True, output_dir)
    except Exception as errmsg:
        logger.error('Could not process module_path: {}'.format(module_path))
        logger.error(errmsg)
    else:
        logger.info('Done')

def delete_module(module_path):
    """ Delete Module after it has been processed """
    try:
        del sys.modules[module_path]
    except Exception as exc:
        logger.debug('Could not delete: {}'.format(module_path))
    else:
        logger.debug('Deleted Module: {}'.format(module_path))

def dump_json_log(namespaces_dict):
    json_dir = os.path.join(os.getcwd(), 'logs')
    # now = str(time.time()).split('.')[0]
    name = '-'.join(namespaces_dict.keys())
    filepath = os.path.join(json_dir, '{}.json'.format(name))
    with open(filepath, 'w') as fp:
        json.dump(namespaces_dict, fp, indent=2)

def make(output_dir, assembly_or_builtin, overwrite=False, quiet=False):
    """ Main Processing Function """
    assembly_dict = {}
    print('='*80)
    logger.info('Making [{}]'.format(assembly_or_builtin))
    try:
        clr.AddReference(assembly_or_builtin)
    except:
        # clr did not work Worked, Try as BuiltIn
        importlib.import_module(assembly_or_builtin)
        builtin_name = assembly_or_builtin
        builtin_dict = {builtin_name: str(sys.modules[builtin_name])}
        assembly_dict = {'__builtins__': builtin_dict}
    else:
        # Clr Worked Parse as Assembly Name
        assembly_name = assembly_or_builtin
        load_assemblies(assembly_name)
        namespaces_dict = crawl_loaded_references(assembly_name)
        assembly_dict = namespaces_dict

    if not assembly_dict:
        raise Exception('No namespaces to process')

    modules = [d.keys() for d in assembly_dict.values()]
    logger.info('Modules and Assemblies Loaded: {}'.format(modules))
    logger.debug( json.dumps(assembly_dict, indent=2, sort_keys=True))

    if not quiet and raw_input('>>> Write Stubs ({}) [y/n] [n]:\n>>> '.format(output_dir)) != 'y':
        logger.info('No Stubs Created')
    else:
        for assembly, modules in assembly_dict.items():
            for module_path in modules.keys():
                if not stub_exists(output_dir, module_path) or overwrite:
                    create_stubs(output_dir, module_path)
                else:
                    logger.info('Skipping [{}] Already Exists'.format(module_path))
            for module_path in modules.keys():
                delete_module(module_path)

        logger.info('Stubs Created')
    return assembly_dict








