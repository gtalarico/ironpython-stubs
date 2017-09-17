class TextEditorOptions(object,IDisposable):
 """ Provides access to settings that control Revit's Text Editor appearance and functionality. """
 def Dispose(self):
  """ Dispose(self: TextEditorOptions) """
  pass
 @staticmethod
 def GetTextEditorOptions():
  """
  GetTextEditorOptions() -> TextEditorOptions
  
   Returns the current Revit instance's TextEditorOptions.
   Returns: The TextEditorOptions for the current Revit instance.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: TextEditorOptions,disposing: bool) """
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

Get: IsValidObject(self: TextEditorOptions) -> bool

"""

 ShowBorder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Show the border box around the text during editing.

Get: ShowBorder(self: TextEditorOptions) -> bool

Set: ShowBorder(self: TextEditorOptions)=value
"""

 ShowOpaqueBackground=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Show opaque background behind the text during editing.

Get: ShowOpaqueBackground(self: TextEditorOptions) -> bool

Set: ShowOpaqueBackground(self: TextEditorOptions)=value
"""


