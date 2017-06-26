class Segment(Element,IDisposable):
 """ This element represents a segment of an MEP curve object. """
 def AddSize(self,size):
  """
  AddSize(self: Segment,size: MEPSize)
   Adds a new MEPSize to the segment.
  
   size: The new MEPSize to be added.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetSizes(self):
  """
  GetSizes(self: Segment) -> ICollection[MEPSize]
  
   Gets the defined sizes of the segment.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveSize(self,nominalDiameter):
  """
  RemoveSize(self: Segment,nominalDiameter: float)
   Remove the existing MEPSize with this nominal diameter from the segment.
  
   nominalDiameter: The nominal diameter of the size.
  """
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
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The description of the segment.

Get: Description(self: Segment) -> str

Set: Description(self: Segment)=value
"""

 MaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ElementId of the MaterialElem.

Get: MaterialId(self: Segment) -> ElementId

"""

 Roughness=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The roughness value for given material.

Get: Roughness(self: Segment) -> float

Set: Roughness(self: Segment)=value
"""

 SizeCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of size objects in the segment.

Get: SizeCount(self: Segment) -> int

"""


