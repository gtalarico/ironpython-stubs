class SetupEnergySimulationDialog(object,IDisposable):
 """
 The Revit dialog which typically precedes invocation of an Energy Simulation run on the Green Building Studio server.
 
 SetupEnergySimulationDialog()
 """
 def Dispose(self):
  """ Dispose(self: SetupEnergySimulationDialog) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: SetupEnergySimulationDialog,disposing: bool) """
  pass
 def Show(self):
  """
  Show(self: SetupEnergySimulationDialog) -> SetupEnergySimulationDialogResult
  
   Shows the SetupEnergySimulationDialog to the user as a modal dialog.
   Returns: One of the Autodesk.Revit.UI.SetupEnergySimulationDialogResult values.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: SetupEnergySimulationDialog) -> bool

"""

 ProjectId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The identifier of the project (on the Green Building Studio server) that was selected by the user.

Get: ProjectId(self: SetupEnergySimulationDialog) -> int

"""

 ProjectName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The project name (representing a project on the Green Building Studio server) selected or supplied by the user.

Get: ProjectName(self: SetupEnergySimulationDialog) -> str

"""

 RunName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the analysis run that was supplied by the user.

Get: RunName(self: SetupEnergySimulationDialog) -> str

"""


