class Rectangle3d(object,IEpsilonComparable[Rectangle3d]):
 """
 Represents the values of a plane and two intervals

    that form an oriented rectangle in three dimensions.

 

 Rectangle3d(plane: Plane,width: float,height: float)

 Rectangle3d(plane: Plane,width: Interval,height: Interval)

 Rectangle3d(plane: Plane,cornerA: Point3d,cornerB: Point3d)
 """
 def ClosestPoint(self,point,includeInterior=None):
  """
  ClosestPoint(self: Rectangle3d,point: Point3d,includeInterior: bool) -> Point3d

  

   Gets the point on the rectangle that is closest to a test-point.

  

   point: Point to project.

   includeInterior: If false,the point is projected onto the boundary edge only,

     otherwise the 

    interior of the rectangle is also taken into consideration.

  

   Returns: The point on the rectangle closest to the test point or Point3d.Unset on failure.

  ClosestPoint(self: Rectangle3d,point: Point3d) -> Point3d

  

   Gets the point on the rectangle that is closest to a test-point.

  

   point: Point to project.

   Returns: The point on or in the rectangle closest to the test point or Point3d.Unset on failure.
  """
  pass
 def Contains(self,*__args):
  """
  Contains(self: Rectangle3d,x: float,y: float) -> PointContainment

  

   Determines if two plane parameters are included in this rectangle.

  

   x: Parameter along base plane X direction.

   y: Parameter along base plane Y direction.

   Returns: Parameter Rectangle relationship.

  Contains(self: Rectangle3d,pt: Point3d) -> PointContainment

  

   Determines if a point is included in this rectangle.

  

   pt: Point to test. The point will be projected onto the Rectangle plane before inclusion is 

    determined.

  

   Returns: Point Rectangle relationship.
  """
  pass
 def Corner(self,index):
  """
  Corner(self: Rectangle3d,index: int) -> Point3d

  

   Gets the corner at the given index.

  

   index: Index of corner,valid values are:

     0=lower left (min-x,min-y)1=lower right 

    (max-x,min-y)2=upper right (max-x,max-y)3=upper left (min-x,max-y)

  

   Returns: The point at the given corner index.
  """
  pass
 @staticmethod
 def CreateFromPolyline(polyline,deviation=None,angleDeviation=None):
  """
  CreateFromPolyline(polyline: IEnumerable[Point3d]) -> (Rectangle3d,float,float)

  CreateFromPolyline(polyline: IEnumerable[Point3d]) -> Rectangle3d
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Rectangle3d,other: Rectangle3d,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def MakeIncreasing(self):
  """
  MakeIncreasing(self: Rectangle3d)

   Ensures the X and Y dimensions are increasing or singleton intervals.
  """
  pass
 def PointAt(self,*__args):
  """
  PointAt(self: Rectangle3d,t: float) -> Point3d

  

   Gets a point along the rectangle boundary.

  

   t: Parameter along rectangle boundary. Valid values range from 0.0 to 4.0,

     where each 

    integer domain represents a single boundary edge.

  

   Returns: The point at the given boundary parameter.

  PointAt(self: Rectangle3d,x: float,y: float) -> Point3d

  

   Gets a point in Rectangle space.

  

   x: Normalized parameter along Rectangle width.

   y: Normalized parameter along Rectangle height.

   Returns: The point at the given x,y parameter.
  """
  pass
 def RecenterPlane(self,*__args):
  """
  RecenterPlane(self: Rectangle3d,origin: Point3d)

   Recenters the base plane on a new origin.

  

   origin: New origin for plane.

  RecenterPlane(self: Rectangle3d,index: int)

   Recenters the base plane on one of the corners.

  

   index: Index of corner,valid values are:

     0=lower left (min-x,min-y)1=lower right 

    (max-x,min-y)2=upper right (max-x,max-y)3=upper left (min-x,max-y)
  """
  pass
 def ToNurbsCurve(self):
  """
  ToNurbsCurve(self: Rectangle3d) -> NurbsCurve

  

   Constructs a nurbs curve representation of this rectangle.

   Returns: A nurbs curve with the same shape as this rectangle.
  """
  pass
 def ToPolyline(self):
  """
  ToPolyline(self: Rectangle3d) -> Polyline

  

   Constructs a polyline from this rectangle.

   Returns: A polyline with the same shape as this rectangle.
  """
  pass
 def Transform(self,xform):
  """
  Transform(self: Rectangle3d,xform: Transform) -> bool

  

   Transforms this rectangle. Note that rectangles cannot be skewed or tapered.

  

   xform: Transformation to apply.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,plane,*__args):
  """
  __new__[Rectangle3d]() -> Rectangle3d

  

  __new__(cls: type,plane: Plane,width: float,height: float)

  __new__(cls: type,plane: Plane,width: Interval,height: Interval)

  __new__(cls: type,plane: Plane,cornerA: Point3d,cornerB: Point3d)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Area=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unsigned Area of the rectangle.



Get: Area(self: Rectangle3d) -> float



"""

 BoundingBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the world aligned boundingbox for this rectangle.



Get: BoundingBox(self: Rectangle3d) -> BoundingBox



"""

 Center=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the point in the center of the rectangle.



Get: Center(self: Rectangle3d) -> Point3d



"""

 Circumference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the circumference of the rectangle.



Get: Circumference(self: Rectangle3d) -> float



"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the signed height of the rectangle. If the Y dimension is decreasing,the height will be negative.



Get: Height(self: Rectangle3d) -> float



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not this is a valid rectangle. 

   A rectangle is considered to be valid when the base plane and both dimensions are valid.



Get: IsValid(self: Rectangle3d) -> bool



"""

 Plane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the base plane of the rectangle.



Get: Plane(self: Rectangle3d) -> Plane



Set: Plane(self: Rectangle3d)=value

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the signed width of the rectangle. If the X dimension is decreasing,the width will be negative.



Get: Width(self: Rectangle3d) -> float



"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the dimensions of the rectangle along the base plane X-Axis (i.e. the width).



Get: X(self: Rectangle3d) -> Interval



Set: X(self: Rectangle3d)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the dimensions of the rectangle along the base plane Y-Axis (i.e. the height).



Get: Y(self: Rectangle3d) -> Interval



Set: Y(self: Rectangle3d)=value

"""


 Unset=None

