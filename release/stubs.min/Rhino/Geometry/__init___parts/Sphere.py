class Sphere(object,IEpsilonComparable[Sphere]):
 """
 Represents the plane and radius values of a sphere.

 

 Sphere(center: Point3d,radius: float)

 Sphere(equatorialPlane: Plane,radius: float)
 """
 def ClosestParameter(self,testPoint,longitudeRadians,latitudeRadians):
  """
  ClosestParameter(self: Sphere,testPoint: Point3d) -> (bool,float,float)

  

   Finds the angle parameters on this sphere that are closest to a test point.

  

   testPoint: Point to project onto the sphere.

   Returns: true on success,false on failure. This function will fail if the point it coincident with the 

    sphere center.
  """
  pass
 def ClosestPoint(self,testPoint):
  """
  ClosestPoint(self: Sphere,testPoint: Point3d) -> Point3d

  

   Returns point on sphere that is closest to given point.

  

   testPoint: Point to project onto Sphere.

   Returns: Point on sphere surface closest to testPoint.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Sphere,other: Sphere,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 @staticmethod
 def FitSphereToPoints(points):
  """ FitSphereToPoints(points: IEnumerable[Point3d]) -> Sphere """
  pass
 def LatitudeDegrees(self,degrees):
  """
  LatitudeDegrees(self: Sphere,degrees: float) -> Circle

  

   Computes the parallel at a specific latitude angle.

     The angle is specified in 

    degrees.

  

  

   degrees: An angle in degrees for the meridian.

   Returns: A circle.
  """
  pass
 def LatitudeRadians(self,radians):
  """
  LatitudeRadians(self: Sphere,radians: float) -> Circle

  

   Computes the parallel at a specific latitude angle.

     The angle is specified in 

    radians.

  

  

   radians: An angle in radians for the parallel.

   Returns: A circle.
  """
  pass
 def LongitudeDegrees(self,degrees):
  """
  LongitudeDegrees(self: Sphere,degrees: float) -> Circle

  

   Computes the meridian at a specific longitude angle.

     The angle is specified in 

    degrees.

  

  

   degrees: An angle in degrees.

   Returns: A circle.
  """
  pass
 def LongitudeRadians(self,radians):
  """
  LongitudeRadians(self: Sphere,radians: float) -> Circle

  

   Computes the meridian at a specific longitude angle.

     The angle is specified in 

    radians.

  

  

   radians: An angle in radians.

   Returns: A circle.
  """
  pass
 def NormalAt(self,longitudeRadians,latitudeRadians):
  """
  NormalAt(self: Sphere,longitudeRadians: float,latitudeRadians: float) -> Vector3d

  

   Computes the normal at a specific angular location on the sphere.

  

   longitudeRadians: A number within the interval [0,2pi].

   latitudeRadians: A number within the interval [-pi/2,pi/2].

   Returns: A vector.
  """
  pass
 def PointAt(self,longitudeRadians,latitudeRadians):
  """
  PointAt(self: Sphere,longitudeRadians: float,latitudeRadians: float) -> Point3d

  

   Evaluates the sphere at specific longitude and latitude angles.

  

   longitudeRadians: A number within the interval [0,2pi].

   latitudeRadians: A number within the interval [-pi/2,pi/2].

   Returns: A point value.
  """
  pass
 def Rotate(self,*__args):
  """
  Rotate(self: Sphere,sinAngle: float,cosAngle: float,axisOfRotation: Vector3d,centerOfRotation: Point3d) -> bool

  

   Rotates this sphere about a point and an axis.

  

   sinAngle: sin(angle)

   cosAngle: cod(angle)

   axisOfRotation: Axis of rotation.

   centerOfRotation: Center of rotation.

   Returns: true on success; false on failure.

  Rotate(self: Sphere,angleRadians: float,axisOfRotation: Vector3d,centerOfRotation: Point3d) -> bool

  

   Rotates this sphere about a point and an axis.

  

   angleRadians: Rotation angle (in Radians)

   axisOfRotation: Axis of rotation.

   centerOfRotation: Center of rotation.

   Returns: true on success; false on failure.

  Rotate(self: Sphere,sinAngle: float,cosAngle: float,axisOfRotation: Vector3d) -> bool

  

   Rotates this sphere about the center point.

  

   sinAngle: sin(angle)

   cosAngle: cos(angle)

   axisOfRotation: The direction of the axis of rotation.

   Returns: true on success; false on failure.

  Rotate(self: Sphere,angleRadians: float,axisOfRotation: Vector3d) -> bool

  

   Rotates the sphere about the center point.

  

   angleRadians: Angle of rotation (in radians)

   axisOfRotation: Rotation axis.

   Returns: true on success; false on failure.
  """
  pass
 def ToBrep(self):
  """
  ToBrep(self: Sphere) -> Brep

  

   Converts this sphere is it Brep representation
  """
  pass
 def ToNurbsSurface(self):
  """
  ToNurbsSurface(self: Sphere) -> NurbsSurface

  

   Converts this sphere to its NurbsSurface representation. 

     This is synonymous with 

    calling NurbsSurface.CreateFromSphere().

  

   Returns: A nurbs surface representation of this sphere or null.
  """
  pass
 def ToRevSurface(self):
  """
  ToRevSurface(self: Sphere) -> RevSurface

  

   Converts this Sphere to a RevSurface representation. 

     This is synonymous with 

    calling RevSurface.CreateFromSphere().

  

   Returns: A surface of revolution representation of this sphere or null.
  """
  pass
 def Transform(self,xform):
  """
  Transform(self: Sphere,xform: Transform) -> bool

  

   Transforms this sphere. Note that non-similarity preserving transformations 

     cannot 

    be applied to a sphere as that would result in an ellipsoid.

  

  

   xform: Transformation matrix to apply.

   Returns: true on success,false on failure.
  """
  pass
 def Translate(self,delta):
  """
  Translate(self: Sphere,delta: Vector3d) -> bool

  

   Moves this sphere along a motion vector.

  

   delta: Motion vector.

   Returns: true on success; false on failure.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Sphere]() -> Sphere

  

  __new__(cls: type,center: Point3d,radius: float)

  __new__(cls: type,equatorialPlane: Plane,radius: float)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 BoundingBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the world aligned boundingbox for this Sphere. 

   If the Sphere is Invalid,an empty box is returned.



Get: BoundingBox(self: Sphere) -> BoundingBox



"""

 Center=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the center point of the sphere.



Get: Center(self: Sphere) -> Point3d



Set: Center(self: Sphere)=value

"""

 Diameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the diameter for this sphere.



Get: Diameter(self: Sphere) -> float



Set: Diameter(self: Sphere)=value

"""

 EquitorialPlane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Equatorial plane for this sphere.



Get: EquitorialPlane(self: Sphere) -> Plane



Set: EquitorialPlane(self: Sphere)=value

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the sphere is valid.



Get: IsValid(self: Sphere) -> bool



"""

 NorthPole=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the point at the North Pole of the sphere.

   This is the parameterization singularity that can be obtained,

   at V value +Math.Pi/2.



Get: NorthPole(self: Sphere) -> Point3d



"""

 Radius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Radius for this sphere.



Get: Radius(self: Sphere) -> float



Set: Radius(self: Sphere)=value

"""

 SouthPole=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the point at the South Pole of the sphere.

   This is the parameterization singularity that can be obtained,

   at V value -Math.Pi/2.



Get: SouthPole(self: Sphere) -> Point3d



"""


 Unset=None

