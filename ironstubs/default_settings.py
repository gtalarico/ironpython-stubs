import os

PATHS = [
    # Local Binaries
    os.path.join(os.getcwd(), 'bin'),
    # Revit
    'C:\\Program Files\\Autodesk\\Revit 2017',
    'C:\\Program Files\\Autodesk\\Revit 2017\\en-US',
    # Dynamo
    'C:\\Program Files\\Dynamo\Dynamo Core\\1.2',
    'C:\\Program Files\\Dynamo\Dynamo Revit\\1.2\\Revit_2017',
    # Rhino
    'C:\\Program Files\\Rhinoceros 5 (64-bit)\\System',
    ]

ASSEMBLIES = [
    # Ironpython
    'IronPython.Wpf',
    # Windows
    'PresentationCore',
    'PresentationFramework',
    'WindowsBase',
    # System
    'System',
    'System.Drawing',
    'System.Windows.Forms',
    # Dynamo
    'ProtoGeometry',
    'DSCoreNodes',
    'DSOffice',
    'Tessellation',
    # Rhino
    'Rhino3dmIO',
    'RhinoCommon',
    # Grasshopper
    'GH_IO',
    'Grasshopper',
    'GH_Util',
    ]

BUILTINS = [
    'clr'
    'wpf'
    ]

ASSEMBLIES.extend(BUILTINS)
ASSEMBLIES.sort()

REVIT_ASSEMBLIES = [
    # Revit
    'RevitAPI',
    'RevitAPIU',
    'RevitServices',
    'RevitNodes',
    ]

# If running inside Revit, Process Revit Assemblies Only
try:
    __revit__
except NameError:
    pass
else:
    ASSEMBLIES = REVIT_ASSEMBLIES
