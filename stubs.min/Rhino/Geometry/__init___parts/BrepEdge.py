class BrepEdge(CurveProxy,IDisposable,ISerializable):
 # no doc
 def AdjacentFaces(self):
  """ AdjacentFaces(self: BrepEdge) -> Array[int] """
  pass
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Dispose(self):
  """ Dispose(self: Curve,disposing: bool) """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: Curve) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: GeometryBase) """
  pass
 def SetEdgeCurve(self,curve3dIndex,subDomain=None):
  """
  SetEdgeCurve(self: BrepEdge,curve3dIndex: int,subDomain: Interval) -> bool
  SetEdgeCurve(self: BrepEdge,curve3dIndex: int) -> bool
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
 Brep=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Brep(self: BrepEdge) -> Brep

"""

 EdgeIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EdgeIndex(self: BrepEdge) -> int

"""

 EndVertex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EndVertex(self: BrepEdge) -> BrepVertex

"""

 StartVertex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: StartVertex(self: BrepEdge) -> BrepVertex

"""

 Tolerance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Tolerance(self: BrepEdge) -> float

Set: Tolerance(self: BrepEdge)=value
"""

 TrimCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TrimCount(self: BrepEdge) -> int

"""

 Valence=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Valence(self: BrepEdge) -> EdgeAdjacency

"""


