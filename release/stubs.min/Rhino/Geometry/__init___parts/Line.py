class Line(object,IEquatable[Line],IEpsilonComparable[Line]):
 """
 Represents the value of start and end points in a single line segment.

 

 Line(from: Point3d,to: Point3d)

 Line(start: Point3d,span: Vector3d)

 Line(start: Point3d,direction: Vector3d,length: float)

 Line(x0: float,y0: float,z0: float,x1: float,y1: float,z1: float)
 """
 def ClosestParameter(self,testPoint):
  """
  ClosestParameter(self: Line,testPoint: Point3d) -> float

  

   Finds the parameter on the infinite line segment that is closest to a test point.

  

   testPoint: Point to project onto the line.

   Returns: The parameter on the line that is closest to testPoint.
  """
  pass
 def ClosestPoint(self,testPoint,limitToFiniteSegment):
  """
  ClosestPoint(self: Line,testPoint: Point3d,limitToFiniteSegment: bool) -> Point3d

  

   Finds the point on the (in)finite line segment that is closest to a test point.

  

   testPoint: Point to project onto the line.

   limitToFiniteSegment: If true,the projection is limited to the finite line segment.

   Returns: The point on the (in)finite line that is closest to testPoint.
  """
  pass
 def DistanceTo(self,testPoint,limitToFiniteSegment):
  """
  DistanceTo(self: Line,testPoint: Point3d,limitToFiniteSegment: bool) -> float

  

   Compute the shortest distance between this line segment and a test point.

  

   testPoint: Point for distance computation.

   limitToFiniteSegment: If true,the distance is limited to the finite line segment.

   Returns: The shortest distance between this line segment and testPoint.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Line,other: Line,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Line,other: Line) -> bool

  

   Determines whether a line has the same value as this line.

  

   other: A line.

   Returns: true if other has the same coordinates as this; otherwise false.

  Equals(self: Line,obj: object) -> bool

  

   Determines whether an object is a line that has the same value as this line.

  

   obj: An object.

   Returns: true if obj is a Line and has the same coordinates as this; otherwise false.
  """
  pass
 def Extend(self,startLength,endLength):
  """
  Extend(self: Line,startLength: float,endLength: float) -> bool

  

   Extend the line by custom distances on both sides.

  

   startLength: Distance to extend the line at the start point. 

     Positive distance result in longer 

    lines.

  

   endLength: Distance to extend the line at the end point. 

     Positive distance result in longer 

    lines.

  

   Returns: true on success,false on failure.
  """
  pass
 def ExtendThroughBox(self,box,additionalLength=None):
  """
  ExtendThroughBox(self: Line,box: Box) -> bool

  

   Ensure the line extends all the way through a box. 

     Note,this does not result in 

    the shortest possible line that overlaps the box.

  

  

   box: Box to extend through.

   Returns: true on success,false on failure.

  ExtendThroughBox(self: Line,box: Box,additionalLength: float) -> bool

  

   Ensure the line extends all the way through a box. 

     Note,this does not result in 

    the shortest possible line that overlaps the box.

  

  

   box: Box to extend through.

   additionalLength: Additional length to append at both sides of the line.

   Returns: true on success,false on failure.

  ExtendThroughBox(self: Line,box: BoundingBox) -> bool

  

   Ensure the line extends all the way through a box. 

     Note,this does not result in 

    the shortest possible line 

     that overlaps the box.

  

  

   box: Box to extend through.

   Returns: true on success,false on failure.

  ExtendThroughBox(self: Line,box: BoundingBox,additionalLength: float) -> bool

  

   Ensure the line extends all the way through a box. 

     Note,this does not result in 

    the shortest possible line that overlaps the box.

  

  

   box: Box to extend through.

   additionalLength: Additional length to append at both sides of the line.

   Returns: true on success,false on failure.
  """
  pass
 def Flip(self):
  """
  Flip(self: Line)

   Flip the endpoints of the line segment.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Line) -> int

  

   Computes a hash number that represents this line.

   Returns: A number that is not unique to the value of this line.
  """
  pass
 def MaximumDistanceTo(self,*__args):
  """
  MaximumDistanceTo(self: Line,testLine: Line) -> float

  

   Finds the largest distance between this line as a finite segment

     and another finite 

    segment.

  

  

   testLine: A line to test.

   Returns: The maximum distance.

  MaximumDistanceTo(self: Line,testPoint: Point3d) -> float

  

   Finds the largest distance between this line as a finite segment

     and a test point.

  

   testPoint: A point to test.

   Returns: The maximum distance.
  """
  pass
 def MinimumDistanceTo(self,*__args):
  """
  MinimumDistanceTo(self: Line,testLine: Line) -> float

  

   Finds the shortest distance between this line as a finite segment

     and another 

    finite segment.

  

  

   testLine: A line to test.

   Returns: The minimum distance.

  MinimumDistanceTo(self: Line,testPoint: Point3d) -> float

  

   Finds the shortest distance between this line as a finite segment

     and a test point.

  

   testPoint: A point to test.

   Returns: The minimum distance.
  """
  pass
 def PointAt(self,t):
  """
  PointAt(self: Line,t: float) -> Point3d

  

   Evaluates the line at the specified parameter.

  

   t: Parameter to evaluate line segment at. Line parameters are normalised parameters.

   Returns: The point at the specified parameter.
  """
  pass
 def ToNurbsCurve(self):
  """
  ToNurbsCurve(self: Line) -> NurbsCurve

  

   Constructs a nurbs curve representation of this line. 

     This amounts to the same as 

    calling NurbsCurve.CreateFromLine().

  

   Returns: A nurbs curve representation of this line or null if no such representation could be made.
  """
  pass
 def ToString(self):
  """
  ToString(self: Line) -> str

  

   Contructs the string representation of this line,in the form "From,To".

   Returns: A text string.
  """
  pass
 def Transform(self,xform):
  """
  Transform(self: Line,xform: Transform) -> bool

  

   Transform the line using a Transformation matrix.

  

   xform: Transform to apply to this line.

   Returns: true on success,false on failure.
  """
  pass
 @staticmethod
 def TryCreateBetweenCurves(curve0,curve1,t0,t1,perpendicular0,perpendicular1,line):
  """
  TryCreateBetweenCurves(curve0: Curve,curve1: Curve,t0: float,t1: float,perpendicular0: bool,perpendicular1: bool) -> (bool,float,float,Line)

  

   Creates a line segment between a pair of curves such that the line segment is either tangent or 

    perpendicular to each of the curves.

  

  

   curve0: The first curve.

   curve1: The second curve.

   t0: Parameter value of point on curve0. Seed value at input and solution at output.

   t1: Parameter value of point on curve 0.  Seed value at input and solution at output.

   perpendicular0: Find line Perpendicuar to (true) or tangent to (false) curve0.

   perpendicular1: Find line Perpendicuar to (true) or tangent to (false) curve1.

   Returns: true on success,false on failure.
  """
  pass
 @staticmethod
 def TryFitLineToPoints(points,fitLine):
  """ TryFitLineToPoints(points: IEnumerable[Point3d]) -> (bool,Line) """
  pass
 def TryGetPlane(self,plane):
  """
  TryGetPlane(self: Line) -> (bool,Plane)

  

   Gets a plane that contains the line. The origin of the plane is at the start of the line.

     

       If possible,a plane parallel to the world xy,yz,or zx plane is returned.

  

   Returns: true on success.
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
  __new__[Line]() -> Line

  

  __new__(cls: type,from: Point3d,to: Point3d)

  __new__(cls: type,start: Point3d,span: Vector3d)

  __new__(cls: type,start: Point3d,direction: Vector3d,length: float)

  __new__(cls: type,x0: float,y0: float,z0: float,x1: float,y1: float,z1: float)
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
 BoundingBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the line's 3d axis aligned bounding box.



Get: BoundingBox(self: Line) -> BoundingBox



"""

 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the direction of this line segment. 

   The length of the direction vector equals the length of 

   the line segment.



Get: Direction(self: Line) -> Vector3d



"""

 From=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Start point of line segment.



Get: From(self: Line) -> Point3d



Set: From(self: Line)=value

"""

 FromX=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X coordinate of the line From point.



Get: FromX(self: Line) -> float



Set: FromX(self: Line)=value

"""

 FromY=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y coordinate of the line From point.



Get: FromY(self: Line) -> float



Set: FromY(self: Line)=value

"""

 FromZ=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Z coordinate of the line From point.



Get: FromZ(self: Line) -> float



Set: FromZ(self: Line)=value

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not this line is valid. 

   Valid lines must have valid start and end points.



Get: IsValid(self: Line) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the length of this line segment. 

   Note that a negative length will invert the line segment without 

   making the actual length negative. The line From point will remain fixed 

   when a new Length is set.



Get: Length(self: Line) -> float



Set: Length(self: Line)=value

"""

 To=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """End point of line segment.



Get: To(self: Line) -> Point3d



Set: To(self: Line)=value

"""

 ToX=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X coordinate of the line To point.



Get: ToX(self: Line) -> float



Set: ToX(self: Line)=value

"""

 ToY=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y coordinate of the line To point.



Get: ToY(self: Line) -> float



Set: ToY(self: Line)=value

"""

 ToZ=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Z coordinate of the line To point.



Get: ToZ(self: Line) -> float



Set: ToZ(self: Line)=value

"""

 UnitTangent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the tangent of the line segment. 

   Note that tangent vectors are always unit vectors.



Get: UnitTangent(self: Line) -> Vector3d



"""


 Unset=None

