class ExportFontKey(object,IDisposable):
 """
 A key used to represent an item stored in an Autodesk.Revit.DB.ExportFontTable.
 
 ExportFontKey(originalFontName: str)
 ExportFontKey()
 ExportFontKey(other: ExportFontKey)
 """
 def Dispose(self):
  """ Dispose(self: ExportFontKey) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExportFontKey,disposing: bool) """
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
 def __new__(self,*__args):
  """
  __new__(cls: type,originalFontName: str)
  __new__(cls: type)
  __new__(cls: type,other: ExportFontKey)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExportFontKey) -> bool

"""

 OriginalFontName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The original font name.

Get: OriginalFontName(self: ExportFontKey) -> str

Set: OriginalFontName(self: ExportFontKey)=value
"""


