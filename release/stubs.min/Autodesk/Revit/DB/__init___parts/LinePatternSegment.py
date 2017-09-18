class LinePatternSegment(object,IDisposable):
 """
 Represents a segment in a line pattern.

 

 LinePatternSegment(type: LinePatternSegmentType,length: float)

 LinePatternSegment()
 """
 def Dispose(self):
  """ Dispose(self: LinePatternSegment) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: LinePatternSegment,disposing: bool) """
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
 def __new__(self,type=None,length=None):
  """
  __new__(cls: type,type: LinePatternSegmentType,length: float)

  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: LinePatternSegment) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the length of the segment.



Get: Length(self: LinePatternSegment) -> float



Set: Length(self: LinePatternSegment)=value

"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the type of the segment.



Get: Type(self: LinePatternSegment) -> LinePatternSegmentType



Set: Type(self: LinePatternSegment)=value

"""


