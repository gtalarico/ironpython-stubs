class FileOpenDialog(FileDialog,IDisposable):
 """
 This class allows an add-in to prompt the user with the Revit dialog used to navigate to and select an existing
    file path.  This dialog is typically used to select a file for opening or importing.
 
 FileOpenDialog(filter: str)
 """
 def Dispose(self):
  """ Dispose(self: FileDialog,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FileDialog,disposing: bool) """
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
 @staticmethod
 def __new__(self,filter):
  """ __new__(cls: type,filter: str) """
  pass
 ShowPreview=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the dialog should include a region showing a preview of the selected file.

Get: ShowPreview(self: FileOpenDialog) -> bool

Set: ShowPreview(self: FileOpenDialog)=value
"""


