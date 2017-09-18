class FilledRegionType(LineAndTextAttrSymbol,IDisposable):
 """ A filled region attributes element. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def IsValidLineWeight(lineWeight):
  """
  IsValidLineWeight(lineWeight: int) -> bool

  

   Indicates whether the given line weight value is valid.

  

   lineWeight: The line weight.

   Returns: True if it is a valid line weight value,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
 Background=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The background.



Get: Background(self: FilledRegionType) -> FilledRegionBackground



Set: Background(self: FilledRegionType)=value

"""

 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The color of the fill pattern.



Get: Color(self: FilledRegionType) -> Color



Set: Color(self: FilledRegionType)=value

"""

 FillPatternId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The fill pattern Id.



Get: FillPatternId(self: FilledRegionType) -> ElementId



Set: FillPatternId(self: FilledRegionType)=value

"""

 LineWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The line weight of the fill pattern.



Get: LineWeight(self: FilledRegionType) -> int



Set: LineWeight(self: FilledRegionType)=value

"""


