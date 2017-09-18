class TriangulatedShellComponent(object,IDisposable):
 """
 This class represents a triangulated boundary component of a solid or a

    triangulated connected component of a shell.
 """
 def Clear(self):
  """
  Clear(self: TriangulatedShellComponent)

   Empties the contents of this TriangulatedShellComponent.
  """
  pass
 def Dispose(self):
  """ Dispose(self: TriangulatedShellComponent) """
  pass
 def GetTriangle(self,triangleIndex):
  """
  GetTriangle(self: TriangulatedShellComponent,triangleIndex: int) -> TriangleInShellComponent

  

   Returns the triangle corresponding to the given index.

  

   triangleIndex: The index of the triangle (between 0 and TriangleCount-1,inclusive).

   Returns: The triangle.
  """
  pass
 def GetVertex(self,vertexIndex):
  """
  GetVertex(self: TriangulatedShellComponent,vertexIndex: int) -> XYZ

  

   Returns the vertex with a given index.

  

   vertexIndex: The index of the vertex (between 0 and getVertexCount()-1,inclusive).

   Returns: A copy of the requested vertex.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: TriangulatedShellComponent,disposing: bool) """
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
 IsClosed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if and only if the triangulation represents a topologically closed shell

   (i.e.,each edge is shared by two triangles).



Get: IsClosed(self: TriangulatedShellComponent) -> bool



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: TriangulatedShellComponent) -> bool



"""

 TriangleCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of triangles in the triangulation.



Get: TriangleCount(self: TriangulatedShellComponent) -> int



"""

 VertexCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of vertices in the triangulation.



Get: VertexCount(self: TriangulatedShellComponent) -> int



"""


