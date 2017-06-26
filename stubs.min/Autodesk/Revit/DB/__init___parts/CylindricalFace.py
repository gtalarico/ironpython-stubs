class CylindricalFace(Face,IDisposable):
 """ A cylindrical face of a 3d solid or open shell. """
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
 Axis=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Axis of the surface.

Get: Axis(self: CylindricalFace) -> XYZ

"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Origin of the surface.

Get: Origin(self: CylindricalFace) -> XYZ

"""


