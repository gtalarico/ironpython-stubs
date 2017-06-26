class TriOrQuadFacet(object,IDisposable):
 """ This class represents a triangle or quadrilateral in a faceted structure. """
 def Dispose(self):
  """ Dispose(self: TriOrQuadFacet) """
  pass
 def GetVertexIndex(self,index):
  """
  GetVertexIndex(self: TriOrQuadFacet,index: int) -> int
  
   Returns the index of the specified vertex of this facet (as an index into the 
    external array
     of vertices in the TriangulationInterface that was used to 
    create the list of TriOrQuadFacets).
  
  
   index: Index of the desired vertex in this TriOrQuadFacet (between 0 and 
    NumberOfVertices-1,inclusive).
  
   Returns: The index of the specified vertex in the external array of vertices (only valid 
    if NumberOfVertices >= 3).
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: TriOrQuadFacet,disposing: bool) """
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

Get: IsValidObject(self: TriOrQuadFacet) -> bool

"""

 Normal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A unit normal vector for this facet.

Get: Normal(self: TriOrQuadFacet) -> XYZ

"""

 NumberOfVertices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of vertices (3 for a triangle,4 for a quadrilateral,0 for an unset TriOrQuadFacet).

Get: NumberOfVertices(self: TriOrQuadFacet) -> int

"""


