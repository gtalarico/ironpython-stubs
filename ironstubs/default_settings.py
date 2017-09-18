import os

PATHS = [
    # | Local Binaries
    # | Revit
    'C:\\Program Files\\Autodesk\\Revit 2017',
    'C:\\Program Files\\Autodesk\\Revit 2017\\en-US',
    # | Dynamo
    'C:\\Program Files\\Dynamo\Dynamo Core\\1.2',
    'C:\\Program Files\\Dynamo\Dynamo Revit\\1.2\\Revit_2017',
    # | Rhino
    'C:\\Program Files\\Rhinoceros 5 (64-bit)\\System',
    # Grasshopper
    'C:\\Users\\gtalarico\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\Plug-ins\\Grasshopper (b45a29b1-4343-4035-989e-044e8580d9cf)\\0.9.76.0'
    ]

ASSEMBLIES = [
    # | Ironpython
    'IronPython.Wpf',
    # | Windows
    'PresentationCore',
    'PresentationFramework',
    'WindowsBase',
    # | System
    'System',
    'System.Drawing',
    'System.Windows.Forms',
    # | Dynamo
    'ProtoGeometry',
    'DSCoreNodes',
    'DSOffice',
    'Tessellation',
    # | Rhino
    'Rhino3dmIO',
    'RhinoCommon',
    # | Grasshopper
    'Grasshopper',
    # 'GH_IO',
    # 'GH_Util',
    ]

BUILTINS = [
    'clr',
    'wpf'
    ]

ASSEMBLIES.extend(BUILTINS)
ASSEMBLIES.sort()

REVIT_ASSEMBLIES = [
    # | Revit
    'RevitAPI',
    'RevitAPIUI',
    'RevitServices',
    'RevitNodes',
    ]

# | If running inside Revit, Process Revit Assemblies Only
try:
    __revit__
except NameError:
    pass
else:
    ASSEMBLIES = REVIT_ASSEMBLIES
