class FileDialog(object,IDisposable):
 """ Base class supporting display of the dialog used to navigate to and select a file from Autodesk Revit. """
 def Dispose(self):
  """ Dispose(self: FileDialog) """
  pass
 def GetSelectedModelPath(self):
  """
  GetSelectedModelPath(self: FileDialog) -> ModelPath

  

   Returns the selected file path chosen by the user.

   Returns: The selected file path,or ll if the dialog has not been shown or selection was 

    cancelled.
  """
  pass
 @staticmethod
 def IsValidFilterString(filterString):
  """
  IsValidFilterString(filterString: str) -> bool

  

   Determines if the input string is acceptable as input for a FileDialog filter 

    string.

  

  

   filterString: The filter string.

   Returns: True of the filter string meets the minimal requirements to be a valid filter 

    string.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FileDialog,disposing: bool) """
  pass
 def Show(self):
  """
  Show(self: FileDialog) -> ItemSelectionDialogResult

  

   Shows the dialog using the stored settings.

   Returns: A status indicating whether the user selected a file name or cancelled the 

    dialog without making a selection.
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
 DefaultFilterEntry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The default entry (from the filter) to be selected in the dialog.



Get: DefaultFilterEntry(self: FileDialog) -> str



Set: DefaultFilterEntry(self: FileDialog)=value

"""

 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The filter string representing a collection of extensions allowed by the dialog.



Get: Filter(self: FileDialog) -> str



Set: Filter(self: FileDialog)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: FileDialog) -> bool



"""

 Title=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The title to show on the dialog.



Get: Title(self: FileDialog) -> str



Set: Title(self: FileDialog)=value

"""


