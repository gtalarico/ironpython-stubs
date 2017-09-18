class Face(GeometryObject,IDisposable):
 """ A bounded face of a 3d solid or open shell. """
 def ComputeDerivatives(self,point):
  """
  ComputeDerivatives(self: Face,point: UV) -> Transform

  

   Returns the first partial derivatives of the underlying surface at the 

    specified point.

  

  

   point: The parameters to be evaluated,in natural parameterization of the face.

   Returns: A transformation containing tangent vectors and a normal vector.
  """
  pass
 def ComputeNormal(self,point):
  """
  ComputeNormal(self: Face,point: UV) -> XYZ

  

   Returns the normal vector for the face at the given point.

  

   point: The parameters to be evaluated,in natural parameterization of the face.

   Returns: The normal vector. This vector will be normalized.
  """
  pass
 def ComputeSecondDerivatives(self,point):
  """
  ComputeSecondDerivatives(self: Face,point: UV) -> FaceSecondDerivatives

  

   Returns the second partial derivatives of the face at the specified point.

  

   point: The parameters to be evaluated,in natural parameterization of the face.

   Returns: The second partial derivatives of the face at the specified point.
  """
  pass
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def Evaluate(self,params):
  """
  Evaluate(self: Face,params: UV) -> XYZ

  

   Evaluates and returns the XYZ coordinates of a point at the indicated UV 

    parameterization of the face.

  

  

   params: The parameters to be evaluated,in natural parameterization of the face.

   Returns: The XYZ coordinates.
  """
  pass
 def GetBoundingBox(self):
  """
  GetBoundingBox(self: Face) -> BoundingBoxUV

  

   Returns the UV bounding box of the face.

   Returns: A BoundingBoxUV with the extents of the parameterization of the face.
  """
  pass
 def GetEdgesAsCurveLoops(self):
  """
  GetEdgesAsCurveLoops(self: Face) -> IList[CurveLoop]

  

   Returns a list of closed curve loops that correspond to the edge loops of the 

    face. 

  Curves in each curve loop correspond to individual edges.

  

   Returns: A list of closed curve loops,that correspond edges of face.
  """
  pass
 def GetRegions(self):
  """
  GetRegions(self: Face) -> IList[Face]

  

   Gets the face regions (created,for example,by the Split Face command) of the 

    face.

  

   Returns: A list of faces,one for the main face of the object hosting the Split Face 

    (such as wall or floor) 

  and one face for each Split Face regions.
  """
  pass
 def Intersect(self,*__args):
  """
  Intersect(self: Face,curve: Curve) -> (SetComparisonResult,IntersectionResultArray)

  

   Calculates the intersection of the specified curve with this face and returns 

    the intersection results.

  

  

   curve: The specified curve to intersect with this face.

   Returns: SetComparisonResult.Overlap - One or more intersections were encountered.  The 

    output argument has the results. SetComparisonResult.Subset - The curve is 

    coincident with the surface.SetComparisonResult.Disjoint - There is no 

    intersection found.

  

  Intersect(self: Face,curve: Curve) -> SetComparisonResult

  

   Calculates the intersection of the specified curve with this face.

  

   curve: The specified curve to intersect with this face.

   Returns: SetComparisonResult.Overlap - One or more intersections were encountered. 

    SetComparisonResult.Subset - The curve is coincident with the 

    surface.SetComparisonResult.Disjoint - There is no intersection found.

  

  Intersect(self: Face,face: Face) -> (FaceIntersectionFaceResult,Curve)

  

   Calculates the intersection of the specified face with this face and returns 

    the intersection results.

  

  

   face: The specified face to intersect with this face.

   Returns: FaceIntersectionFaceResult.Intersecting - One or more intersections were 

    encountered.SetComparisonResult.NonIntersecting - There is no intersection 

    found.

  

  Intersect(self: Face,face: Face) -> FaceIntersectionFaceResult

  

   Calculates the intersection of the specified face with this face and returns 

    the intersection results.

  

  

   face: The specified face to intersect with this face.

   Returns: FaceIntersectionFaceResult.Intersecting - One or more intersections were 

    encountered.SetComparisonResult.NonIntersecting - There is no intersection 

    found.
  """
  pass
 def IsInside(self,point,result=None):
  """
  IsInside(self: Face,point: UV) -> bool

  

   Indicates whether the specified point is within this face.

  

   point: The parameters to be evaluated,in natural parameterization of the face.

   Returns: True if point is within this face or on its boundary,otherwise false.

  IsInside(self: Face,point: UV) -> (bool,IntersectionResult)

  

   Indicates whether the specified point is within this face and outputs 

    additional information about the point location.

  

  

   point: The parameters to be evaluated,in natural parameterization of the face.

   Returns: True if within this face or on its boundary,otherwise False.
  """
  pass
 def Project(self,point):
  """
  Project(self: Face,point: XYZ) -> IntersectionResult

  

   Projects the specified point on the face.

  

   point: The point to be projected.

   Returns: Geometric information if projection is successful;

  if projection fails or the 

    nearest point is outside of this face,returns ll.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: GeometryObject) """
  pass
 def Triangulate(self,levelOfDetail=None):
  """
  Triangulate(self: Face) -> Mesh

  

   Returns a triangular mesh approximation to the face.

  Triangulate(self: Face,levelOfDetail: float) -> Mesh

  

   Returns a triangular mesh approximation to the face.

  

   levelOfDetail: The level of detail. Its range is from 0 to 1. 0 is the lowest level of detail 

    and 1 is the highest.
  """
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
 Area=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The area of this face.



Get: Area(self: Face) -> float



"""

 EdgeLoops=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A collection of edge loops.  Each edge loop represents one of the closed boundaries of the face.



Get: EdgeLoops(self: Face) -> EdgeArrayArray



"""

 HasRegions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the face contains regions (which can be created,for example,by the Split Face command).



Get: HasRegions(self: Face) -> bool



"""

 IsTwoSided=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if a face is two-sided (degenerate).



Get: IsTwoSided(self: Face) -> bool



"""

 MaterialElementId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The element ID of the material from which this face is composed.



Get: MaterialElementId(self: Face) -> ElementId



"""

 Reference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns a stable reference to the face.



Get: Reference(self: Face) -> Reference



"""


