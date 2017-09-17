class ExportPatternInfo(object,IDisposable):
 """
 A value used to represent the info stored in the Autodesk.Revit.DB.ExportPatternTable.
 
 ExportPatternInfo(destinationPatternName: str)
 ExportPatternInfo()
 ExportPatternInfo(other: ExportPatternInfo)
 """
 def Dispose(self):
  """ Dispose(self: ExportPatternInfo) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExportPatternInfo,disposing: bool) """
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
  __new__(cls: type,destinationPatternName: str)
  __new__(cls: type)
  __new__(cls: type,other: ExportPatternInfo)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 DestinationPatternName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The destination pattern name (the name of the pattern in the exported format).

Get: DestinationPatternName(self: ExportPatternInfo) -> str

Set: DestinationPatternName(self: ExportPatternInfo)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExportPatternInfo) -> bool

"""


