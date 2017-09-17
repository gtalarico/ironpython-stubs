class AnalysisDisplayColorEntry(object,IDisposable):
 """
 Contains one entry of intermediate colors in color settings for analysis display style.
 
 AnalysisDisplayColorEntry(color: Color)
 AnalysisDisplayColorEntry(color: Color,value: float)
 AnalysisDisplayColorEntry()
 """
 def Dispose(self):
  """ Dispose(self: AnalysisDisplayColorEntry) """
  pass
 def HasValue(self):
  """
  HasValue(self: AnalysisDisplayColorEntry) -> bool
  
   Check if color entry has associated value.
   Returns: True if entry has a value associated with it,false otherwise.
  """
  pass
 def IsEqual(self,other):
  """
  IsEqual(self: AnalysisDisplayColorEntry,other: AnalysisDisplayColorEntry) -> bool
  
   Compare color entries.
  
   other: Color entry to compare to.
   Returns: True if color entries are equal,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: AnalysisDisplayColorEntry,disposing: bool) """
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
 def __new__(self,color=None,value=None):
  """
  __new__(cls: type,color: Color)
  __new__(cls: type,color: Color,value: float)
  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Color associated with color entry.

Get: Color(self: AnalysisDisplayColorEntry) -> Color

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AnalysisDisplayColorEntry) -> bool

"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Value associated with color entry.

Get: Value(self: AnalysisDisplayColorEntry) -> float

"""


