class Circle(object,IEpsilonComparable[Circle]):
 """
 Represents a circle in 3D.

    The values used are a radius and an orthonormal frame	of the plane containing the circle,

    with origin at the center.The circle is parameterized by radians from 0 to 2 Pi given byt -> center + cos(t)*radius*xaxis + sin(t)*radius*yaxiswhere center,xaxis and yaxis define the orthonormal frame of the circle plane.

 

 Circle(radius: float)

 Circle(plane: Plane,radius: float)

 Circle(center: Point3d,radius: float)

 Circle(arc: Arc)

 Circle(point1: Point3d,point2: Point3d,point3: Point3d)

 Circle(plane: Plane,center: Point3d,radius: float)

 Circle(startPoint: Point3d,tangentAtP: Vector3d,pointOnCircle: Point3d)
 """
 def ClosestParameter(self,testPoint,t):
  """
  ClosestParameter(self: Circle,testPoint: Point3d) -> (bool,float)

  

   Gets the parameter on the circle which is closest to a test point.

  

   testPoint: Point to project onto the circle.

   Returns: true on success,false on failure.
  """
  pass
 def ClosestPoint(self,testPoint):
  """
  ClosestPoint(self: Circle,testPoint: Point3d) -> Point3d

  

   Gets the point on the circle which is closest to a test point.

  

   testPoint: Point to project onto the circle.

   Returns: The point on the circle that is closest to testPoint or

     Point3d.Unset on failure.
  """
  pass
 def DerivativeAt(self,derivative,t):
  """
  DerivativeAt(self: Circle,derivative: int,t: float) -> Vector3d

  

   Determines the value of the Nth derivative at a parameter.

  

   derivative: Which order of derivative is wanted.

   t: Parameter to evaluate derivative. Valid values are 0,1,2 and 3.

   Returns: The derivative of the circle at the given parameter.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Circle,other: Circle,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def IsInPlane(self,plane,tolerance):
  """
  IsInPlane(self: Circle,plane: Plane,tolerance: float) -> bool

  

   Evaluates whether or not this circle is co-planar with a given plane.

  

   plane: Plane.

   tolerance: Tolerance to use.

   Returns: true if the circle plane is co-planar with the given plane within tolerance.
  """
  pass
 def PointAt(self,t):
  """
  PointAt(self: Circle,t: float) -> Point3d

  

   Circles use trigonometric parameterization: 

     t -> center + cos(t)*radius*xaxis + 

    sin(t)*radius*yaxis.

  

  

   t: Parameter of point to evaluate.

   Returns: The point on the circle at the given parameter.
  """
  pass
 def Reverse(self):
  """
  Reverse(self: Circle)

   Reverse the orientation of the circle. Changes the domain from [a,b]

     to [-b,-a].
  """
  pass
 def Rotate(self,*__args):
  """
  Rotate(self: Circle,angle: float,axis: Vector3d) -> bool

  

   Rotates the circle through a given angle.

  

   angle: Angle (in radians) of the rotation.

   axis: Rotation axis.

   Returns: true on success,false on failure.

  Rotate(self: Circle,angle: float,axis: Vector3d,point: Point3d) -> bool

  

   Rotates the circle through a given angle.

  

   angle: Angle (in radians) of the rotation.

   axis: Rotation axis.

   point: Rotation anchor point.

   Returns: true on success,false on failure.

  Rotate(self: Circle,sinAngle: float,cosAngle: float,axis: Vector3d) -> bool

  

   Rotates the circle around an axis that starts at the base plane origin.

  

   sinAngle: The value returned by Math.Sin(angle) to compose the rotation.

   cosAngle: The value returned by Math.Cos(angle) to compose the rotation.

   axis: A rotation axis.

   Returns: true on success,false on failure.

  Rotate(self: Circle,sinAngle: float,cosAngle: float,axis: Vector3d,point: Point3d) -> bool

  

   Rotates the circle around an axis that starts at the provided point.

  

   sinAngle: The value returned by Math.Sin(angle) to compose the rotation.

   cosAngle: The value returned by Math.Cos(angle) to compose the rotation.

   axis: A rotation direction.

   point: A rotation base point.

   Returns: true on success,false on failure.
  """
  pass
 def TangentAt(self,t):
  """
  TangentAt(self: Circle,t: float) -> Vector3d

  

   Circles use trigonometric parameterization: 

     t -> center + cos(t)*radius*xaxis + 

    sin(t)*radius*yaxis.

  

  

   t: Parameter of tangent to evaluate.

   Returns: The tangent at the circle at the given parameter.
  """
  pass
 def ToNurbsCurve(self):
  """
  ToNurbsCurve(self: Circle) -> NurbsCurve

  

   Constructs a nurbs curve representation of this circle. 

     This amounts to the same 

    as calling NurbsCurve.CreateFromCircle().

  

   Returns: A nurbs curve representation of this circle or null if no such representation could be made.
  """
  pass
 def Transform(self,xform):
  """
  Transform(self: Circle,xform: Transform) -> bool

  

   Transforms this circle using an xform matrix.

  

   xform: Transformation to apply.

   Returns: true on success,false on failure.
  """
  pass
 def Translate(self,delta):
  """
  Translate(self: Circle,delta: Vector3d) -> bool

  

   Moves the circle.

  

   delta: Translation vector.

   Returns: true on success,false on failure.
  """
  pass
 @staticmethod
 def TryFitCircleTT(c1,c2,t1,t2):
  """
  TryFitCircleTT(c1: Curve,c2: Curve,t1: float,t2: float) -> Circle

  

   Try to fit a circle to two curves using tangent relationships.

  

   c1: First curve to touch.

   c2: Second curve to touch.

   t1: Parameter on first curve close to desired solution.

   t2: Parameter on second curve closet to desired solution.

   Returns: Valid circle on success,Circle.Unset on failure.
  """
  pass
 @staticmethod
 def TryFitCircleTTT(c1,c2,c3,t1,t2,t3):
  """
  TryFitCircleTTT(c1: Curve,c2: Curve,c3: Curve,t1: float,t2: float,t3: float) -> Circle

  

   Try to fit a circle to three curves using tangent relationships.

  

   c1: First curve to touch.

   c2: Second curve to touch.

   c3: Third curve to touch.

   t1: Parameter on first curve close to desired solution.

   t2: Parameter on second curve closet to desired solution.

   t3: Parameter on third curve close to desired solution.

   Returns: Valid circle on success,Circle.Unset on failure.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Circle]() -> Circle

  

  __new__(cls: type,radius: float)

  __new__(cls: type,plane: Plane,radius: float)

  __new__(cls: type,center: Point3d,radius: float)

  __new__(cls: type,arc: Arc)

  __new__(cls: type,point1: Point3d,point2: Point3d,point3: Point3d)

  __new__(cls: type,plane: Plane,center: Point3d,radius: float)

  __new__(cls: type,startPoint: Point3d,tangentAtP: Vector3d,pointOnCircle: Point3d)
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
 """Gets the circle's 3d axis aligned bounding box.



Get: BoundingBox(self: Circle) -> BoundingBox



"""

 Center=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the center point of this circle.



Get: Center(self: Circle) -> Point3d



Set: Center(self: Circle)=value

"""

 Circumference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the circumference of this circle.



Get: Circumference(self: Circle) -> float



Set: Circumference(self: Circle)=value

"""

 Diameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the diameter (radius * 2.0) of this circle. 

   Diameters should be positive values.



Get: Diameter(self: Circle) -> float



Set: Diameter(self: Circle)=value

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A valid circle has radius larger than 0.0 and a base plane which is must also be valid.



Get: IsValid(self: Circle) -> bool



"""

 Normal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the normal vector for this circle.



Get: Normal(self: Circle) -> Vector3d



"""

 Plane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the plane of the circle.



Get: Plane(self: Circle) -> Plane



Set: Plane(self: Circle)=value

"""

 Radius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the radius of this circle. 

   Radii should be positive values.



Get: Radius(self: Circle) -> float



Set: Radius(self: Circle)=value

"""


 Unset=None

