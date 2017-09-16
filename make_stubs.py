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
import clr
from collections import defaultdict
import json
from pprint import pprint

join = os.path.join
project_dir = os.getcwd()  # Must execute from project dir

from generator3.generator3 import process_one

##################
# Revit + Dynamo #
##################
# RevitAPI
sys.path.append('C:\\Program Files\\Autodesk\\Revit 2017')
# RevitAPIUI + Other  Revit Requirements
sys.path.append('C:\\Program Files\\Autodesk\\Revit 2017\\en-US')
# ProtoGeometry
sys.path.append('C:\\Program Files\\Dynamo\\Dynamo Core\\1.2')
# RevitServices
sys.path.append('C:\\Program Files\\Dynamo\\Dynamo Revit\\1.2\\Revit_2017')

# Repository Dlls
sys.path.append(join(project_dir, 'bin'))

def is_namespace(something):
    """ Returns True if object is Module """
    if 'namespace' in str(type(something)):
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

loaded_modules = ['clr', 'wpf']
loadable_assemblies = [
                       'IronPython.Wpf',
                       'System',
                       'PresentationFramework',
                       'PresentationCore',
                       'WindowsBase',
                       'System.Drawing',
                       'System.Windows.Forms',

                       'RevitServices',
                       'RevitNodes',
                       'ProtoGeometry',
                       'Rhino3dmIO',
                      ]

# If running inside Revit, process these only
try:
    __revit__
    loadable_assemblies.extend([ 'RevitAPI', 'RevitAPIUI'])
    # loadable_assemblies = [ 'RevitAPI', 'RevitAPIUI',] # ONLY REVIT
except NameError:
    pass

###################
# LOAD ASSEMBLIES #
###################
for assembly_name in loadable_assemblies:
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
    if assembly_name in loadable_assemblies:
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

    for other in loaded_modules:
        process_one(other, None, True, SAVE_PATH)

    with open('stubs.json', 'w') as fp:
        json.dump(master_namespaces, fp, indent=4)

SAVE_PATH = os.path.join(project_dir, 'stubs')
# Uncomment to re-create stubs
make_stubs()
