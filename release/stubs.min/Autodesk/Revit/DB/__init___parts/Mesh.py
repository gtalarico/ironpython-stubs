class Mesh(GeometryObject,IDisposable):
 """ A triangular mesh. """
 def Dispose(self):
  """ Dispose(self: Mesh,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: GeometryObject) """
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
 MaterialElementId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Element ID of the material from which this mesh is composed.

Get: MaterialElementId(self: Mesh) -> ElementId

"""

 NumTriangles=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of triangles that the mesh contains.

Get: NumTriangles(self: Mesh) -> int

"""

 Vertices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves all vertices used to define this mesh. Intended for indexed access.

Get: Vertices(self: Mesh) -> IList[XYZ]

"""


