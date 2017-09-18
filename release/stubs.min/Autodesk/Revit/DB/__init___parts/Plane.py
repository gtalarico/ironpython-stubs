class Plane(Surface,IDisposable):
 """
 A Planar surface.

 

 Plane(norm: XYZ,origin: XYZ)

 Plane(xVec: XYZ,yVec: XYZ,origin: XYZ)

 Plane()
 """
 @staticmethod
 def Create(frameOfReference):
  """
  Create(frameOfReference: Frame) -> Plane

  

   Creates a Plane object defined by a local frame of reference.

  

   frameOfReference: frameOfReference is an orthonormal frame that defines a local coordinate system 

    for the plane being constructed.

     Frame.Origin is a point on plane. 

    Frame.BasisZ defines the plane's normal,while Frame.BasisX and Frame.BasisY 

    are orthogonal to the normal. The frame may be either left-handed or 

    right-handed (see Frame.IsRightHanded).
  """
  pass
 @staticmethod
 def CreateByNormalAndOrigin(normal,origin):
  """
  CreateByNormalAndOrigin(normal: XYZ,origin: XYZ) -> Plane

  

   Constructs a Plane object from a normal and an origin represented as XYZ 

    objects. Follows the standard conventions for a planar surface.

     The 

    constructed Plane object will pass through origin and be perpendicular to 

    normal. The X and Y axes of the plane will be defined arbitrarily.

  

  

   normal: Plane normal. Expected to be a valid non-zero length vector. Doesn't need to be 

    a unit vector.

  

   origin: Plane origin.  Expected to lie within the Revit design limits 

    Autodesk.Revit.DB.XYZ.IsWithinLengthLimits(Autodesk.Revit.DB.XYZ).
  """
  pass
 @staticmethod
 def CreateByOriginAndBasis(origin,basisX,basisY):
  """
  CreateByOriginAndBasis(origin: XYZ,basisX: XYZ,basisY: XYZ) -> Plane

  

   Creates a Plane object defined by the two orthogonal unit vectors and passing 

    through the origin point supplied as arguments.

  

  

   origin: Plane origin. Expected to lie within the Revit design limits 

    Autodesk.Revit.DB.XYZ.IsWithinLengthLimits(Autodesk.Revit.DB.XYZ).

  

   basisX: First of the two unit vectors that define the plane. Must be orthogonal to the 

    second one.

  

   basisY: Second of the two unit vectors that define the plane. Must be orthogonal to the 

    first one.
  """
  pass
 @staticmethod
 def CreateByThreePoints(point1,point2,point3):
  """
  CreateByThreePoints(point1: XYZ,point2: XYZ,point3: XYZ) -> Plane

  

   Creates a Plane object passing through three points supplied as arguments.

  

   point1: First of the three points that define a unique plane. The created Plane object 

    will pass through these points.

  

   point2: Second of the three points that define a unique plane.

   point3: Third of the three points that define a unique plane.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Surface,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Surface,disposing: bool) """
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
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,norm: XYZ,origin: XYZ)

  __new__(cls: type,xVec: XYZ,yVec: XYZ,origin: XYZ)

  __new__(cls: type)
  """
  pass
 Normal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Plane normal.



Get: Normal(self: Plane) -> XYZ



"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Plane origin.



Get: Origin(self: Plane) -> XYZ



"""

 XVec=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Axis defining the first parametric direction of the plane.



Get: XVec(self: Plane) -> XYZ



"""

 YVec=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Axis defining the second parametric direction of the plane.



Get: YVec(self: Plane) -> XYZ



"""


