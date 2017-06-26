class PlanarFace(Face,IDisposable):
 """ A bounded face of a 3d solid or open shell. """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
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
 FaceNormal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Normal of the planar face.

Get: FaceNormal(self: PlanarFace) -> XYZ

"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Origin of the surface.

Get: Origin(self: PlanarFace) -> XYZ

"""

 XVector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The X-vector of the planar face.

Get: XVector(self: PlanarFace) -> XYZ

"""

 YVector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Y-vector of the planar face.

Get: YVector(self: PlanarFace) -> XYZ

"""


