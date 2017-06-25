""" Dll Stub Generator.
Based on script developed by:
URL

"""

import os
import sys
import clr
from collections import defaultdict
import json
from pprint import pprint

from generator3.generator3 import process_one

join = os.path.join
project_dir = os.getcwd()  # Must execute from project dir

# Revit + Dynamo
sys.path.append('C:\\Program Files\\Autodesk\\Revit 2017')                                               # RevitAPI
sys.path.append('C:\\Program Files\\Autodesk\\Revit 2017\\en-US')                                      # RevitAPIUI - Revit Req.
sys.path.append('C:\\Program Files\\Dynamo\\Dynamo Core\\1.2')                                           # ProtoGeometry
sys.path.append('C:\\Program Files\\Dynamo\\Dynamo Revit\\1.2\\Revit_2017')                              # RevitServices
sys.path.append(join(project_dir, 'bin'))


def is_namespace(something):
    """ Returns True if object is Module """
    if 'namespace' in str(type(something)):
        return True

def iter_module(module_name, module, module_path=None, namespaces=None, ):
    """ Recursively iterate through all namespaces in assembly """
    # print('>>> {}'.format(module_name))
    if not namespaces:
        namespaces = defaultdict(dict)
    # module_path = module_path or module_name

    for submodule_name, submodule in vars(module).iteritems():
        if not is_namespace(submodule):
            continue
        if module_path:
            submodule_path = '.'.join([module_path, submodule_name])
        else:
            submodule_path = submodule_name
        flat_namespaces[submodule_path] = repr(submodule_name)

        namespaces[module_name].update({submodule_name: submodule})
        iter_module(submodule_name, submodule, submodule_path, namespaces=namespaces)
    return namespaces

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

# IN REVIT ONLY
loadable_assemblies = [ 'RevitAPI', 'RevitAPIUI',]
loadable_assemblies = [ ]

other_namespaces = ['clr']
# try:
#     import wpf
#     other_modules.append(wpf)
# except:
#     loadable_assemblies.append('IronPython.Wpf')

for assembly_name in loadable_assemblies:
    print('='*30)
    try:
        print('Adding Assembly [{}]'.format(assembly_name))
        clr.AddReference(assembly_name)
    except Exception as errmsg:
        print('Could not load assembly: {}'.format(assembly_name))
        # print('-'*30)
        print(errmsg)
        # print('='*30)
    else:
        print('Loaded [{}]'.format(assembly_name))


print('='*30)
print('='*30)

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
        master_namespaces[assembly_filename] = flat_namespaces
        # pprint(dict(flat_namespaces))
    else:
        print('*** Assembly Skiped. Not in target list: {}'.format(assembly_name))


print('='*30)
print('='*30)
# print( json.dumps(master_namespaces, indent=4))
print( json.dumps(flat_namespaces, indent=4, sort_keys=True))


SAVE_PATH = os.path.join(project_dir, 'stubs2')
print('='*30)
print('='*30)

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

for other in other_namespaces:
    process_one(other, None, True, SAVE_PATH)

# modules = {
#             {
#             'loader': None,
#             'path': None
#             'namespaces': ['clr']
#             },
#             {
#             'loader': clr.AddReferenceToFile('RevitAPI.dll'),
#             'path': bin
#             'namespaces': ['clr']
#             }
# }
#                 # IronPython Core/System
#                 'clr',
#                 'System',
#                 'System.Boolean',
#                 'System.Collections',
#                 'System.Collections.Generic',
#                 'System.IO',
#                 'System.String',
#                 'System.Treading'
#
#                 # System + Wpf + Misc
#                 'wpf',
#                 'System.Drawing',
#                 'System.Collections',
#                 'System.Collections.Generic',
#                 'System.Windows',
#                 'System.Windows',
#                 'System.Windows.Window',
#                 'System.Windows.Controls',
#                 'System.Environment',
#                 'System.Windows.Input',
#                 ]
#
# rhino_namespaces = [
#                 # Rhino
#                 'Rhino',
#                 'Rhino.ApplicationSettings',
#                 'Rhino.Collections',
#                 'Rhino.Commands',
#                 'Rhino.Display',
#                 'Rhino.DocObjects',
#                 'Rhino.DocObjects.Custom',
#                 'Rhino.DocObjects.Tables',
#                 'Rhino.FileIO',
#                 'Rhino.Geometry',
#                 'Rhino.Geometry.Collections',
#                 'Rhino.Geometry.Intersect',
#                 'Rhino.Geometry.Morphs',
#                 'Rhino.Input',
#                 'Rhino.Input.Custom',
#                 'Rhino.PlugIns',
#                 'Rhino.Render',
#                 'Rhino.Render.Fields',
#                 'Rhino.Render.UI',
#                 'Rhino.Runtime',
#                 'Rhino.Runtime.InteropWrappers',
#                 'Rhino.UI',
#                 'Rhino.UI.Gumball',
#                 ]
#
# revit_namespaces = [
#                 # Revit API
#                 'Autodesk.Revit.ApplicationServices',
#                 'Autodesk.Revit.Attributes',
#                 'Autodesk.Revit.Creation',
#                 'Autodesk.Revit.Exceptions',
#                 'Autodesk.Revit.Utility',
#
#                 'Autodesk.Revit.DB',
#                 'Autodesk.Revit.DB.Analysis',
#                 'Autodesk.Revit.DB.Architecture',
#                 'Autodesk.Revit.DB.Electrical',
#                 'Autodesk.Revit.DB.Events',
#                 'Autodesk.Revit.DB.ExtensibleStorage',
#                 'Autodesk.Revit.DB.ExternalService',
#                 'Autodesk.Revit.DB.Fabrication',
#                 'Autodesk.Revit.DB.IFC',
#                 'Autodesk.Revit.DB.Lighting',
#                 'Autodesk.Revit.DB.Macros',
#                 'Autodesk.Revit.DB.Mechanical',
#                 'Autodesk.Revit.DB.Plumbing',
#                 'Autodesk.Revit.DB.PointClouds',
#                 'Autodesk.Revit.DB.Structure',
#                 'Autodesk.Revit.DB.Structure.StructuralSections',
#
#                 'Autodesk.Revit.UI',
#                 'Autodesk.Revit.UI.Events',
#                 'Autodesk.Revit.UI.Macros',
#                 'Autodesk.Revit.UI.Mechanical',
#                 'Autodesk.Revit.UI.Plumbing',
#                 'Autodesk.Revit.UI.Selection',
#
#                 # DesignScript
#                 'Autodesk.DesignScript.Geometry',
#                 'Autodesk.DesignScript.Geometry.TSpline',
#
#                 # Dynamo-Revit
#                 'RevitServices.Persistence',
#                 'RevitServices.Transactions',
#                 'Revit.Application',
#                 'Revit.Elements',
#                 'Revit.Elements.Views',
#                 'Revit.Filter',
#                 'Revit.GeometryConversion',
#                 'Revit.GeometryObjects',
#                 'Revit.Transaction',
#                 'Revit.References',
                # 'Revit.AnalysisDisplay',
                # ]
