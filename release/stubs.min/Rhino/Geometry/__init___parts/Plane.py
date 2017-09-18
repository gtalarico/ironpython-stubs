class Plane(object,IEquatable[Plane],IEpsilonComparable[Plane]):
 """
 Represents the value of a center point and two axes in a plane in three dimensions.

 

 Plane(other: Plane)

 Plane(origin: Point3d,normal: Vector3d)

 Plane(origin: Point3d,xDirection: Vector3d,yDirection: Vector3d)

 Plane(origin: Point3d,xPoint: Point3d,yPoint: Point3d)

 Plane(a: float,b: float,c: float,d: float)
 """
 def ClosestParameter(self,testPoint,s,t):
  """
  ClosestParameter(self: Plane,testPoint: Point3d) -> (bool,float,float)

  

   Gets the parameters of the point on the plane closest to a test point.

  

   testPoint: Point to get close to.

   Returns: true if a parameter could be found,

     false if the point could not be projected 

    successfully.
  """
  pass
 def ClosestPoint(self,testPoint):
  """
  ClosestPoint(self: Plane,testPoint: Point3d) -> Point3d

  

   Gets the point on the plane closest to a test point.

  

   testPoint: Point to get close to.

   Returns: The point on the plane that is closest to testPoint,

     or Point3d.Unset on failure.
  """
  pass
 def DistanceTo(self,testPoint):
  """
  DistanceTo(self: Plane,testPoint: Point3d) -> float

  

   Returns the signed distance from testPoint to its projection onto this plane. 

     If 

    the point is below the plane,a negative distance is returned.

  

  

   testPoint: Point to test.

   Returns: Signed distance from this plane to testPoint.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Plane,other: Plane,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Plane,plane: Plane) -> bool

  

   Determines if another plane has the same components as this plane.

  

   plane: A plane.

   Returns: true if plane has the same components as this plane; false otherwise.

  Equals(self: Plane,obj: object) -> bool

  

   Determines if an object is a plane and has the same components as this plane.

  

   obj: An object.

   Returns: true if obj is a plane and has the same components as this plane; false otherwise.
  """
  pass
 def ExtendThroughBox(self,box,s,t):
  """
  ExtendThroughBox(self: Plane,box: Box) -> (bool,Interval,Interval)

  

   Extend this plane through a Box.

  

   box: A box to use for extension.

   Returns: true on success,false on failure.

  ExtendThroughBox(self: Plane,box: BoundingBox) -> (bool,Interval,Interval)

  

   Extends this plane through a bounding box.

  

   box: A box to use as minimal extension boundary.

   Returns: true on success,false on failure.
  """
  pass
 @staticmethod
 def FitPlaneToPoints(points,plane,maximumDeviation=None):
  """
  FitPlaneToPoints(points: IEnumerable[Point3d]) -> (PlaneFitResult,Plane,float)

  FitPlaneToPoints(points: IEnumerable[Point3d]) -> (PlaneFitResult,Plane)
  """
  pass
 def Flip(self):
  """
  Flip(self: Plane)

   Flip this plane by swapping out the X and Y axes and inverting the Z axis.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Plane) -> int

  

   Gets a non-unique hashing code for this entity.

   Returns: A particular number for a specific instance of plane.
  """
  pass
 def GetPlaneEquation(self):
  """
  GetPlaneEquation(self: Plane) -> Array[float]

  

   Gets the plane equation for this plane in the format of Ax+By+Cz+D=0.

   Returns: Array of four values.
  """
  pass
 def PointAt(self,u,v,w=None):
  """
  PointAt(self: Plane,u: float,v: float,w: float) -> Point3d

  

   Evaluate a point on the plane.

  

   u: evaulation parameter.

   v: evaulation parameter.

   w: evaulation parameter.

   Returns: plane.origin + u*plane.xaxis + v*plane.yaxis + z*plane.zaxis.

  PointAt(self: Plane,u: float,v: float) -> Point3d

  

   Evaluate a point on the plane.

  

   u: evaulation parameter.

   v: evaulation parameter.

   Returns: plane.origin + u*plane.xaxis + v*plane.yaxis.
  """
  pass
 def RemapToPlaneSpace(self,ptSample,ptPlane):
  """
  RemapToPlaneSpace(self: Plane,ptSample: Point3d) -> (bool,Point3d)

  

   Convert a point from World space coordinates into Plane space coordinates.

  

   ptSample: World point to remap.

   Returns: true on success,false on failure.
  """
  pass
 def Rotate(self,*__args):
  """
  Rotate(self: Plane,angle: float,axis: Vector3d,centerOfRotation: Point3d) -> bool

  

   Rotate the plane about a custom anchor point.

  

   angle: Angle in radians.

   axis: Axis of rotation.

   centerOfRotation: Center of rotation.

   Returns: true on success,false on failure.

  Rotate(self: Plane,sinAngle: float,cosAngle: float,axis: Vector3d,centerOfRotation: Point3d) -> bool

  

   Rotate the plane about a custom anchor point.

  

   sinAngle: Sin(angle)

   cosAngle: Cos(angle)

   axis: Axis of rotation.

   centerOfRotation: Center of rotation.

   Returns: true on success,false on failure.

  Rotate(self: Plane,sinAngle: float,cosAngle: float,axis: Vector3d) -> bool

  

   Rotate the plane about its origin point.

  

   sinAngle: Sin(angle).

   cosAngle: Cos(angle).

   axis: Axis of rotation.

   Returns: true on success,false on failure.

  Rotate(self: Plane,angle: float,axis: Vector3d) -> bool

  

   Rotate the plane about its origin point.

  

   angle: Angle in radians.

   axis: Axis of rotation.

   Returns: true on success,false on failure.
  """
  pass
 def ToString(self):
  """
  ToString(self: Plane) -> str

  

   Constructs the string representation of this plane.

   Returns: Text.
  """
  pass
 def Transform(self,xform):
  """
  Transform(self: Plane,xform: Transform) -> bool

  

   Transform the plane with a Transformation matrix.

  

   xform: Transformation to apply to plane.

   Returns: true on success,false on failure.
  """
  pass
 def Translate(self,delta):
  """
  Translate(self: Plane,delta: Vector3d) -> bool

  

   Translate (move) the plane along a vector.

  

   delta: Translation (motion) vector.

   Returns: true on success,false on failure.
  """
  pass
 def ValueAt(self,p):
  """
  ValueAt(self: Plane,p: Point3d) -> float

  

   Get the value of the plane equation at the point.

  

   p: evaulation point.

   Returns: returns pe[0]*p.X + pe[1]*p.Y + pe[2]*p.Z + pe[3] where

     pe[0],pe[1],pe[2] and 

    pe[3] are the coeeficients of the plane equation.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Plane]() -> Plane

  

  __new__(cls: type,other: Plane)

  __new__(cls: type,origin: Point3d,normal: Vector3d)

  __new__(cls: type,origin: Point3d,xDirection: Vector3d,yDirection: Vector3d)

  __new__(cls: type,origin: Point3d,xPoint: Point3d,yPoint: Point3d)

  __new__(cls: type,a: float,b: float,c: float,d: float)
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not this is a valid plane. 

   A plane is considered to be valid when all fields contain reasonable 

   information and the equation jibes with point and zaxis.



Get: IsValid(self: Plane) -> bool



"""

 Normal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the normal of this plane. This is essentially the ZAxis of the plane.



Get: Normal(self: Plane) -> Vector3d



"""

 Origin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the origin point of this plane.



Get: Origin(self: Plane) -> Point3d



Set: Origin(self: Plane)=value

"""

 OriginX=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X coordinate of the origin of this plane.



Get: OriginX(self: Plane) -> float



Set: OriginX(self: Plane)=value

"""

 OriginY=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y coordinate of the origin of this plane.



Get: OriginY(self: Plane) -> float



Set: OriginY(self: Plane)=value

"""

 OriginZ=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Z coordinate of the origin of this plane.



Get: OriginZ(self: Plane) -> float



Set: OriginZ(self: Plane)=value

"""

 XAxis=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X axis vector of this plane.



Get: XAxis(self: Plane) -> Vector3d



Set: XAxis(self: Plane)=value

"""

 YAxis=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y axis vector of this plane.



Get: YAxis(self: Plane) -> Vector3d



Set: YAxis(self: Plane)=value

"""

 ZAxis=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Z axis vector of this plane.



Get: ZAxis(self: Plane) -> Vector3d



Set: ZAxis(self: Plane)=value

"""


 Unset=None
 WorldXY=None
 WorldYZ=None
 WorldZX=None

