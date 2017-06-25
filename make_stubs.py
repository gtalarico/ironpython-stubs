""" Dll Stub Generator.
Based on script developed by:
URL

"""

import os
import sys
import clr

join = os.path.join
project_dir = os.getcwd()  # Must execute from project dir

# sys.path.append(join(project_dir, 'bin')) # Dlls
sys.path.append(join(project_dir, 'lib')) # Generator
# print('Path: {}'.format(sys.path))

# Other Dlls
sys.path.append('C:\\Program Files\\Autodesk\\Revit 2017')                                               # RevitAPI
sys.path.append('C:\\Program Files\\Autodesk\\Revit 2017\\en-US')                                      # RevitAPIUI - Revit Req.
# sys.path.append('C:\\Program Files\\Dynamo\\Dynamo Core\\1.2')                                           # ProtoGeometry
# sys.path.append('C:\\Program Files\\Dynamo\\Dynamo Revit\\1.2\\Revit_2017')                              # RevitServices

class Module():

    def __init__(self, name, module, parent):
        self.name = name
        self.module = module
        self.parent = parent


from generator3 import process_one

target_assemblies = [
              'RevitAPI.dll',
            #   'RevitServices.dll',
            #   'RevitAPIUI.dll',
            #   'RevitNodes.dll',
            #   'ProtoGeometry.dll',
            #   'Rhino3dmIO.dll',
            #   'Ironpython.Wpf.dll',

            #   'PresentationFramework.dll',
            #   'WindowsBase.dll',
            #   'System',
            #   'System.Drawings',
            #   'System.Collections',
            #   'System.Windows.Forms',
              ]

for assembly_name in target_assemblies:
    print('='*30)
    try:
        print('Adding Assembly [{}]'.format(assembly_name))
        clr.AddReferenceToFile(assembly_name)
    except Exception as errmsg:
        print('Could not load assembly: {}'.format(assembly_name))
        # print('-'*30)
        print(errmsg)
        # print('='*30)
    else:
        print('Loaded [{}]'.format(assembly_name))

def iter_assembly(assembly, namespaces=None):
    if not namespaces:
        namespaces = []
    for name, module in vars(assembly).iteritems():
        # print('='*30)
        # print(name)
        # print(module)
        # print(type(module))
        if 'namespace' in str(type(module)):
            print('Iterating: {}'.format(module))
            namespaces += iter_assembly(module, namespaces=namespaces)
    return namespaces

namespaces = []

for assembly in clr.References:
    # print(assembly)
    assembly_name = assembly.GetName().Name
    assembly_path = assembly.CodeBase
    assembly_filename = os.path.basename(assembly_path)
    print(assembly_filename)
    if assembly_filename in target_assemblies:
        rv = iter_assembly(assembly, assembly_name)
# print('+++++++++++++++++')
# print(rv)

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

# if REVIT_LOADED:
#     namespaces.extend(revit_namespaces)
#
# # namespaces.extend(rhino_namespaces)
#
# SAVE_PATH = os.path.join(project_dir, 'stubs3')
#
# for module in namespaces:
#     try:
#         print('Processing [{}]'.format(module))
#         process_one(module, None, True, SAVE_PATH)
#     except Exception as errmsg:
#         print('Could not process module: {}'.format(module))
#         print(errmsg)
#     else:
#         print('Done')
