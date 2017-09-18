class SweptBlend(GenericForm,IDisposable):
 """ A swept blend solid or void form. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetVertexConnectionMap(self):
  """
  GetVertexConnectionMap(self: SweptBlend) -> VertexIndexPairArray

  

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
  SetVertexConnectionMap(self: SweptBlend,vertexMap: VertexIndexPairArray)

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
 BottomProfile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The curves which make up the bottom profile of the sketch.



Get: BottomProfile(self: SweptBlend) -> CurveArrArray



"""

 BottomProfileSymbol=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The bottom family symbol profile of the swept blend.



Get: BottomProfileSymbol(self: SweptBlend) -> FamilySymbolProfile



"""

 BottomSketch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The bottom profile sketch of the swept blend.



Get: BottomSketch(self: SweptBlend) -> Sketch



"""

 PathSketch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sketched path for the swept blend.



Get: PathSketch(self: SweptBlend) -> Sketch



"""

 SelectedPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The selected curve used for the swept blend path.



Get: SelectedPath(self: SweptBlend) -> Curve



"""

 TopProfile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The curves which make up the top profile of the sketch.



Get: TopProfile(self: SweptBlend) -> CurveArrArray



"""

 TopProfileSymbol=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The top family symbol profile of the swept blend.



Get: TopProfileSymbol(self: SweptBlend) -> FamilySymbolProfile



"""

 TopSketch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The top profile sketch of the swept blend.



Get: TopSketch(self: SweptBlend) -> Sketch



"""


