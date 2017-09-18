class Arc(object,IEquatable[Arc],IEpsilonComparable[Arc]):
 """
 Represents the value of a plane,two angles and a radius in

    a subcurve of a three-dimensional circle.

    

    The curve is parameterized by an angle expressed in radians. For an IsValid arc

    the total subtended angle AngleRadians()=Domain()(1) - Domain()(0) must satisfy

    0 < AngleRadians() < 2*PiThe parameterization of the Arc is inherited from the Circle it is derived from.

    In particulart -> center + cos(t)*radius*xaxis + sin(t)*radius*yaxiswhere xaxis and yaxis,(part of Circle.Plane) form an othonormal frame of the plane

    containing the circle.

 

 Arc(circle: Circle,angleRadians: float)

 Arc(circle: Circle,angleIntervalRadians: Interval)

 Arc(plane: Plane,radius: float,angleRadians: float)

 Arc(center: Point3d,radius: float,angleRadians: float)

 Arc(plane: Plane,center: Point3d,radius: float,angleRadians: float)

 Arc(startPoint: Point3d,pointOnInterior: Point3d,endPoint: Point3d)

 Arc(pointA: Point3d,tangentA: Vector3d,pointB: Point3d)
 """
 def BoundingBox(self):
  """
  BoundingBox(self: Arc) -> BoundingBox

  

   Computes the 3D axis aligned bounding box for this arc.

   Returns: Bounding box of arc.
  """
  pass
 def ClosestParameter(self,testPoint):
  """
  ClosestParameter(self: Arc,testPoint: Point3d) -> float

  

   Gets parameter on the arc closest to a test point.

  

   testPoint: Point to get close to.

   Returns: Parameter (in radians) of the point on the arc that

     is closest to the test point. 

    If testPoint is the center

     of the arc,then the starting point of the arc is

     

       (arc.Domain()[0]) returned. If no parameter could be found,

     

    RhinoMath.UnsetValue is returned.
  """
  pass
 def ClosestPoint(self,testPoint):
  """
  ClosestPoint(self: Arc,testPoint: Point3d) -> Point3d

  

   Computes the point on an arc that is closest to a test point.

  

   testPoint: Point to get close to.

   Returns: The point on the arc that is closest to testPoint. If testPoint is

     the center of 

    the arc,then the starting point of the arc is returned.

     UnsetPoint on failure.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Arc,other: Arc,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Arc,other: Arc) -> bool

  

   Determines whether another arc has the same value as this arc.

  

   other: An arc.

   Returns: true if obj is equal to this arc; otherwise false.

  Equals(self: Arc,obj: object) -> bool

  

   Determines whether another object is an arc and has the same value as this arc.

  

   obj: An object.

   Returns: true if obj is an arc and is exactly equal to this arc; otherwise false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Arc) -> int

  

   Computes a hash code for the present arc.

   Returns: A non-unique integer that represents this arc.
  """
  pass
 def PointAt(self,t):
  """
  PointAt(self: Arc,t: float) -> Point3d

  

   Gets the point at the given arc parameter.

  

   t: Arc parameter to evaluate.

   Returns: The point at the given parameter.
  """
  pass
 def Reverse(self):
  """
  Reverse(self: Arc)

   Reverses the orientation of the arc. Changes the domain from [a,b]

     to [-b,-a].
  """
  pass
 def TangentAt(self,t):
  """
  TangentAt(self: Arc,t: float) -> Vector3d

  

   Gets the tangent at the given parameter.

  

   t: Parameter of tangent to evaluate.

   Returns: The tangent at the arc at the given parameter.
  """
  pass
 def ToNurbsCurve(self):
  """
  ToNurbsCurve(self: Arc) -> NurbsCurve

  

   Initializes a nurbs curve representation of this arc. 

     This amounts to the same as 

    calling NurbsCurve.CreateFromArc().

  

   Returns: A nurbs curve representation of this arc or null if no such representation could be made.
  """
  pass
 def Transform(self,xform):
  """
  Transform(self: Arc,xform: Transform) -> bool

  

   Transforms the arc using a Transformation matrix.

  

   xform: Transformations to apply. 

     Note that arcs cannot handle non-euclidian 

    transformations.

  

   Returns: true on success,false on failure.
  """
  pass
 def Trim(self,domain):
  """
  Trim(self: Arc,domain: Interval) -> bool

  

   Sets arc's angle domain (in radians) as a subdomain of the circle.

  

   domain: 0 < domain[1] - domain[0] <= 2.0 * RhinoMath.Pi.

   Returns: true on success,false on failure.
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
  __new__[Arc]() -> Arc

  

  __new__(cls: type,circle: Circle,angleRadians: float)

  __new__(cls: type,circle: Circle,angleIntervalRadians: Interval)

  __new__(cls: type,plane: Plane,radius: float,angleRadians: float)

  __new__(cls: type,center: Point3d,radius: float,angleRadians: float)

  __new__(cls: type,plane: Plane,center: Point3d,radius: float,angleRadians: float)

  __new__(cls: type,startPoint: Point3d,pointOnInterior: Point3d,endPoint: Point3d)

  __new__(cls: type,pointA: Point3d,tangentA: Vector3d,pointB: Point3d)
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
 Angle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the sweep -or subtended- angle (in Radians) for this arc segment.



Get: Angle(self: Arc) -> float



Set: Angle(self: Arc)=value

"""

 AngleDegrees=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the sweep -or subtended- angle (in Radians) for this arc segment.



Get: AngleDegrees(self: Arc) -> float



Set: AngleDegrees(self: Arc)=value

"""

 AngleDomain=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the angle domain (in Radians) of this arc.



Get: AngleDomain(self: Arc) -> Interval



Set: AngleDomain(self: Arc)=value

"""

 Center=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the center point for this arc.



Get: Center(self: Arc) -> Point3d



Set: Center(self: Arc)=value

"""

 Circumference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the circumference of the circle that is coincident with this arc.



Get: Circumference(self: Arc) -> float



"""

 Diameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Diameter of this arc.



Get: Diameter(self: Arc) -> float



Set: Diameter(self: Arc)=value

"""

 EndAngle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the end angle (in Radians) for this arc segment.



Get: EndAngle(self: Arc) -> float



Set: EndAngle(self: Arc)=value

"""

 EndAngleDegrees=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the end angle (in Radians) for this arc segment.



Get: EndAngleDegrees(self: Arc) -> float



Set: EndAngleDegrees(self: Arc)=value

"""

 EndPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the end point of the arc.



Get: EndPoint(self: Arc) -> Point3d



"""

 IsCircle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not this arc is a complete circle.



Get: IsCircle(self: Arc) -> bool



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not this arc is valid.

   Detail:

    Radius>0 and 0<AngleRadians()<=2*Math.Pi.



Get: IsValid(self: Arc) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length of the arc. (Length=Radius * (subtended angle in radians)).



Get: Length(self: Arc) -> float



"""

 MidPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the mid-point of the arc.



Get: MidPoint(self: Arc) -> Point3d



"""

 Plane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the plane in which this arc lies.



Get: Plane(self: Arc) -> Plane



Set: Plane(self: Arc)=value

"""

 Radius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the radius of this arc.



Get: Radius(self: Arc) -> float



Set: Radius(self: Arc)=value

"""

 StartAngle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the start angle (in Radians) for this arc segment.



Get: StartAngle(self: Arc) -> float



Set: StartAngle(self: Arc)=value

"""

 StartAngleDegrees=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the start angle (in Radians) for this arc segment.



Get: StartAngleDegrees(self: Arc) -> float



Set: StartAngleDegrees(self: Arc)=value

"""

 StartPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the start point of the arc.



Get: StartPoint(self: Arc) -> Point3d



"""


