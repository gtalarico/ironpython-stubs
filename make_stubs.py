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
from config import PROJECT_DIR, SYS_PATHS, SAVE_PATH
from config import LOADABLE_ASSEMBLIES, BUILTIN_MODULES
from generator3.generator3 import process_one

# Add Paths
[sys.path.append(p) for p in SYS_PATHS]

def is_namespace(something):
    """ Returns True if object is Namespace: Module """
    if isinstance(something, type(System)):
        return True

def iter_module(module_name, module, module_path=None, namespaces=None, ):
    """ Recursively iterate through all namespaces in assembly """
    if not namespaces:
        namespaces = defaultdict(dict)

    for submodule_name, submodule in vars(module).iteritems():
        if not is_namespace(submodule):
            continue
        if module_path:
            submodule_path = '.'.join([module_path, submodule_name])
        else:
            submodule_path = submodule_name
        flat_namespaces[submodule_path] = repr(submodule_name)

        namespaces[module_name].update({submodule_name: repr(submodule)})
        iter_module(submodule_name, submodule, submodule_path, namespaces=namespaces)
    return namespaces

###################
# LOAD ASSEMBLIES #
###################
for assembly_name in LOADABLE_ASSEMBLIES:
    print('='*30)
    try:
        print('Adding Assembly [{}]'.format(assembly_name))
        clr.AddReference(assembly_name)
    except Exception as errmsg:
        print('Could not load assembly: {}'.format(assembly_name))
        print(errmsg)
    else:
        print('Loaded [{}]'.format(assembly_name))

print('#'*30)

##########################################
# CRAWL ASSEMBLIES TO GET ALL NAMESPACES #
##########################################
master_namespaces = {}
flat_namespaces = {}

for assembly in clr.References:
    assembly_name = assembly.GetName().Name
    assembly_path = assembly.CodeBase
    assembly_filename = os.path.basename(assembly_path)
    if assembly_name in LOADABLE_ASSEMBLIES:
        print('Parsing Assembly: {}'.format(assembly_name))
        namespaces = iter_module(assembly_name, assembly)
        print('Total: {}'.format(len(flat_namespaces)))
        master_namespaces[assembly_filename] = namespaces
    else:
        print('*** Assembly Skiped. Not in target list: {}'.format(assembly_name))

# print( json.dumps(master_namespaces, indent=4))
print( json.dumps(flat_namespaces, indent=4, sort_keys=True))
print('#'*30)

###############################
# MAKE STUBS USING GENERATOR3 #
###############################

def make_stubs():
    for namespace in sorted(flat_namespaces.keys()):
        try:
            print('Processing [{}]'.format(namespace))
            print('='*30)
            process_one(namespace, None, True, SAVE_PATH)
        except Exception as errmsg:
            print('Could not process namespace: {}'.format(module))
            print(errmsg)
        else:
            print('Done')
        print('='*30)

    for other in BUILTIN_MODULES:
        process_one(other, None, True, SAVE_PATH)

    with open('stubs.json', 'w') as fp:
        json.dump(master_namespaces, fp, indent=4)

# Uncomment to re-create stubs
# make_stubs()
