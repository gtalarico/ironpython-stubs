class ColorSelectionDialog(object,IDisposable):
 """
 Allows display of the Revit Color dialog.
 
 ColorSelectionDialog()
 """
 def Dispose(self):
  """ Dispose(self: ColorSelectionDialog) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ColorSelectionDialog,disposing: bool) """
  pass
 def Show(self):
  """
  Show(self: ColorSelectionDialog) -> ItemSelectionDialogResult
  
   Shows the Revit Color dialog as a modal dialog.
   Returns: A status indicating whether the user selected a color or cancelled the dialog 
    without making a selection.
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

Get: IsValidObject(self: ColorSelectionDialog) -> bool

"""

 OriginalColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The original color.

Get: OriginalColor(self: ColorSelectionDialog) -> Color

Set: OriginalColor(self: ColorSelectionDialog)=value
"""

 SelectedColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The new color selected by the user.

Get: SelectedColor(self: ColorSelectionDialog) -> Color

"""


