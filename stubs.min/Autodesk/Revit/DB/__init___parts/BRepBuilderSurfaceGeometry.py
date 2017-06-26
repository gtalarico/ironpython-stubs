class BRepBuilderSurfaceGeometry(object,IDisposable):
 """ An abstract class used by BRepBuilder to represent the geometry of a surface. Specific surface-geometry representations are represented by subclasses. """
 @staticmethod
 def Create(surface,surfaceEnvelope):
  """
  Create(surface: Surface,surfaceEnvelope: BoundingBoxUV) -> BRepBuilderSurfaceGeometry
  
   Construct BRepBuilderSurfaceGeometry based on a permitted Revit Surface,
    including Plane and CylSurf.
  
  
   surface: The Revit surface defining the geometry.
     This BRepBuilderSurfaceGeometry 
    stores a copy of the input surface.
  
   surfaceEnvelope: Envelope of the surface in the uv parametric domain. Defines the domain of 
    interest for the created surface.
     This is typically used to identify the 
    domain of the face that references the surface in question.
     Expected to 
    either be null or define a valid domain.
  """
  pass
 @staticmethod
 def CreateNURBSSurface(degreeU,degreeV,knotsU,knotsV,controlPoints,*__args):
  """
  CreateNURBSSurface(degreeU: int,degreeV: int,knotsU: IList[float],knotsV: IList[float],controlPoints: IList[XYZ],weights: IList[float],bReverseOrientation: bool,surfaceEnvelope: BoundingBoxUV) -> BRepBuilderSurfaceGeometry
  CreateNURBSSurface(degreeU: int,degreeV: int,knotsU: IList[float],knotsV: IList[float],controlPoints: IList[XYZ],bReverseOrientation: bool,surfaceEnvelope: BoundingBoxUV) -> BRepBuilderSurfaceGeometry
  """
  pass
 def Dispose(self):
  """ Dispose(self: BRepBuilderSurfaceGeometry) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: BRepBuilderSurfaceGeometry,disposing: bool) """
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

Get: IsValidObject(self: BRepBuilderSurfaceGeometry) -> bool

"""


