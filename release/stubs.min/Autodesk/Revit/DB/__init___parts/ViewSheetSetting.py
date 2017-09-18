class ViewSheetSetting(APIObject,IDisposable):
 """ Represents the View/Sheet Set (Application Menu->Print) within Autodesk Revit. """
 def Delete(self):
  """
  Delete(self: ViewSheetSetting) -> bool

  

   Delete the current view sheet set,and make the In-Session set as the current 

    one.

  

   Returns: False if Delete operation fails,otherwise True.
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
  Rename(self: ViewSheetSetting,newName: str) -> bool

  

   Rename the current view sheet set.

  

   newName: View sheet set name to be renamed as.

   Returns: False if Rename operation fails,otherwise True.
  """
  pass
 def Revert(self):
  """
  Revert(self: ViewSheetSetting)

   Revert the current view sheet set.
  """
  pass
 def Save(self):
  """
  Save(self: ViewSheetSetting) -> bool

  

   Save the changes for the current view sheet set.

   Returns: False if save operation fails,otherwise True.
  """
  pass
 def SaveAs(self,newName):
  """
  SaveAs(self: ViewSheetSetting,newName: str) -> bool

  

   Save the current view sheet set to another view sheet set with the specified 

    name.

  

  

   newName: View sheet set name to be saved as.

   Returns: False if Save As operation fails,otherwise True.
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
 AvailableViews=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """All views that can be printed.



Get: AvailableViews(self: ViewSheetSetting) -> ViewSet



"""

 CurrentViewSheetSet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The current view sheet set of PrintSetup.



Get: CurrentViewSheetSet(self: ViewSheetSetting) -> IViewSheetSet



Set: CurrentViewSheetSet(self: ViewSheetSetting)=value

"""

 InSession=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The in-session view sheet set of Print Setup.



Get: InSession(self: ViewSheetSetting) -> InSessionViewSheetSet



"""


