class Polyline(Point3dList,IList[Point3d],ICollection[Point3d],IEnumerable[Point3d],IEnumerable,IList,ICollection):
 """
 Represents an ordered set of points connected by linear segments.

    Polylines are closed if start and end points coincide.

 

 Polyline()

 Polyline(initialCapacity: int)

 Polyline(collection: IEnumerable[Point3d])
 """
 def BreakAtAngles(self,angle):
  """
  BreakAtAngles(self: Polyline,angle: float) -> Array[Polyline]

  

   Breaks this polyline into sections at sharp kinks. 

     Closed polylines will also be 

    broken at the first and last vertex.

  

  

   angle: Angle (in radians) between adjacent segments for a break to occur.

   Returns: An array of polyline segments,or null on error.
  """
  pass
 def CenterPoint(self):
  """
  CenterPoint(self: Polyline) -> Point3d

  

   Compute the center point of the polyline as the weighted average of all segments.

   Returns: The weighted average of all segments.
  """
  pass
 def ClosestParameter(self,testPoint):
  """
  ClosestParameter(self: Polyline,testPoint: Point3d) -> float

  

   Gets the parameter along the polyline which is closest to a test-point.

  

   testPoint: Point to approximate.

   Returns: The parameter along the polyline closest to testPoint.
  """
  pass
 def ClosestPoint(self,testPoint):
  """
  ClosestPoint(self: Polyline,testPoint: Point3d) -> Point3d

  

   Gets the point on the polyline which is closest to a test-point.

  

   testPoint: Point to approximate.

   Returns: The point on the polyline closest to testPoint.
  """
  pass
 def CollapseShortSegments(self,tolerance):
  """
  CollapseShortSegments(self: Polyline,tolerance: float) -> int

  

   Collapses all segments until none are shorter than tolerance. 

     This function is 

    significantly slower than DeleteShortSegments,

     since it recursively operates on 

    the shortest segment. 

     When a segment is collapsed the end-points are placed in the 

    center of the segment.

  

  

   tolerance: Tolerance to use during collapsing.

   Returns: The number of segments that were collapsed.
  """
  pass
 def DeleteShortSegments(self,tolerance):
  """
  DeleteShortSegments(self: Polyline,tolerance: float) -> int

  

   Removes all points that are closer than tolerance to the previous point. 

     Start and 

    end points are left intact.

  

  

   tolerance: Vertices closer together than tolerance will be removed.

   Returns: Number of points (and segments) removed.
  """
  pass
 def GetSegments(self):
  """
  GetSegments(self: Polyline) -> Array[Line]

  

   Constructs an array of line segments that make up the entire polyline.

   Returns: An array of line segments or null if the polyline contains fewer than 2 points.
  """
  pass
 def IsClosedWithinTolerance(self,tolerance):
  """
  IsClosedWithinTolerance(self: Polyline,tolerance: float) -> bool

  

   Determines whether the polyline is closed,provided a tolerance value.

  

   tolerance: If the distance between the start and end point of the polyline 

     is less than 

    tolerance,the polyline is considered to be closed.

  

   Returns: true if the polyline is closed to within tolerance,false otherwise.
  """
  pass
 def PointAt(self,t):
  """
  PointAt(self: Polyline,t: float) -> Point3d

  

   Gets the point on the polyline at the given parameter. 

     The integer part of the 

    parameter indicates the index of the segment.

  

  

   t: Polyline parameter.

   Returns: The point on the polyline at t.
  """
  pass
 def ReduceSegments(self,tolerance):
  """
  ReduceSegments(self: Polyline,tolerance: float) -> int

  

   Constructs a reduction of this polyline by recursively removing the least significant segments.

  

   tolerance: Tolerance for reduction. Whenever a vertex of the polyline is more 

     significant 

    than tolerance,it will be included in the reduction.

  

   Returns: The number of vertices that disappeared due to reduction.
  """
  pass
 def SegmentAt(self,index):
  """
  SegmentAt(self: Polyline,index: int) -> Line

  

   Gets the line segment at the given index.

  

   index: Index of segment to retrieve.

   Returns: Line segment at index or Line.Unset on failure.
  """
  pass
 def Smooth(self,amount):
  """
  Smooth(self: Polyline,amount: float) -> bool

  

   Smoothens the polyline segments by averaging adjacent vertices. 

     Smoothing requires 

    a polyline with exclusively valid vertices.

  

  

   amount: Amount to smooth. Zero equals no smoothing,one equals complete smoothing.

   Returns: true on success,false on failure.
  """
  pass
 def TangentAt(self,t):
  """
  TangentAt(self: Polyline,t: float) -> Vector3d

  

   Gets the unit tangent vector along the polyline at the given parameter. 

     The 

    integer part of the parameter indicates the index of the segment.

  

  

   t: Polyline parameter.

   Returns: The tangent along the polyline at t.
  """
  pass
 def ToNurbsCurve(self):
  """
  ToNurbsCurve(self: Polyline) -> NurbsCurve

  

   Constructs a nurbs curve representation of this polyline.

   Returns: A Nurbs curve shaped like this polyline or null on failure.
  """
  pass
 def TriangulateClosedPolyline(self):
  """
  TriangulateClosedPolyline(self: Polyline) -> Array[MeshFace]

  

   Attempts to create a list of triangles which represent a

     triangulation of a closed 

    polyline
  """
  pass
 def Trim(self,domain):
  """
  Trim(self: Polyline,domain: Interval) -> Polyline

  

   Constructs a polyline out of a parameter subdomain in this curve.

  

   domain: The subdomain of the polyline. 

     The integer part of the domain parameters indicate 

    the index of the segment.

  

   Returns: The polyline as defined by the subdomain,or null on failure.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,initialCapacity: int)

  __new__(cls: type,collection: IEnumerable[Point3d])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsClosed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this polyline is closed. 

   The polyline is considered to be closed if its start is 

   identical to its endpoint.



Get: IsClosed(self: Polyline) -> bool



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this polyline is valid. 

   Valid polylines have at least one segment,no Invalid points and no zero length segments.Closed polylines with only two segments are also not considered valid.



Get: IsValid(self: Polyline) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total length of the polyline.



Get: Length(self: Polyline) -> float



"""

 SegmentCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of segments for this polyline.



Get: SegmentCount(self: Polyline) -> int



"""


