class PrintSetup(APIObject,IDisposable):
 """ Represents the Print Setup (Application Menu->Print->Print Setup) within Autodesk Revit. """
 def Delete(self):
  """
  Delete(self: PrintSetup) -> bool
  
   Delete the current print setting,and make the In-Session setting as the 
    current one.
  
   Returns: False if Delete operation fails,otherwise true.
  """
  pass
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
  pass
 def Rename(self,newName):
  """
  Rename(self: PrintSetup,newName: str) -> bool
  
   Rename the current print setting with the specified name.
  
   newName: print setting name to be renamed as.
   Returns: False if Rename operation fails,otherwise true.
  """
  pass
 def Revert(self):
  """
  Revert(self: PrintSetup)
   Revert the current print setting.
  """
  pass
 def Save(self):
  """
  Save(self: PrintSetup) -> bool
  
   Save the changes for the current print setting.
   Returns: False if save operation fails,otherwise True.
  """
  pass
 def SaveAs(self,newName):
  """
  SaveAs(self: PrintSetup,newName: str) -> bool
  
   Save the current print setting to another print setting with the specified name.
  
   newName: print setting name to be saved as.
   Returns: False if Save As operation fails,otherwise true.
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
 CurrentPrintSetting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The current Print Setting of Print Setup.

Get: CurrentPrintSetting(self: PrintSetup) -> IPrintSetting

Set: CurrentPrintSetting(self: PrintSetup)=value
"""

 InSession=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The in-session Print Setting of Print Setup.

Get: InSession(self: PrintSetup) -> InSessionPrintSetting

"""


