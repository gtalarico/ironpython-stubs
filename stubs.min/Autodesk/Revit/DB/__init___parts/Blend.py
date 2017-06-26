class Blend(GenericForm,IDisposable):
 """ A blend solid or void form. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetVertexConnectionMap(self):
  """
  GetVertexConnectionMap(self: Blend) -> VertexIndexPairArray
  
   Gets the mapping between the vertices in the top and bottom profiles.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetVertexConnectionMap(self,vertexMap):
  """
  SetVertexConnectionMap(self: Blend,vertexMap: VertexIndexPairArray)
   Sets the mapping between the vertices in the top and bottom profiles.
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
 BottomOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The offset of the bottom end of the blend relative to the sketch plane.

Get: BottomOffset(self: Blend) -> float

Set: BottomOffset(self: Blend)=value
"""

 BottomProfile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The curves which make up the bottom profile of the sketch.

Get: BottomProfile(self: Blend) -> CurveArrArray

"""

 BottomSketch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Bottom Sketch of the Blend.

Get: BottomSketch(self: Blend) -> Sketch

"""

 TopOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The offset of the top end of the blend relative to the sketch plane.

Get: TopOffset(self: Blend) -> float

Set: TopOffset(self: Blend)=value
"""

 TopProfile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The curves which make up the top profile of the sketch.

Get: TopProfile(self: Blend) -> CurveArrArray

"""

 TopSketch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Top Sketch of the Blend.

Get: TopSketch(self: Blend) -> Sketch

"""


