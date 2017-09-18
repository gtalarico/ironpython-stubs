class BezierCurve(object,IDisposable):
 """
 Represents a Bezier curve.

    Note: as an exception,the bezier curve is not derived from Rhino.Geometry.Curve.

 

 BezierCurve(controlPoints: IEnumerable[Point2d])

 BezierCurve(controlPoints: IEnumerable[Point3d])

 BezierCurve(controlPoints: IEnumerable[Point4d])
 """
 def ChangeDimension(self,desiredDimension):
  """
  ChangeDimension(self: BezierCurve,desiredDimension: int) -> bool

  

   Change dimension of bezier.

   Returns: true if successful.  false if desired_dimension < 1
  """
  pass
 @staticmethod
 def CreateCubicBeziers(sourceCurve,distanceTolerance,kinkTolerance):
  """
  CreateCubicBeziers(sourceCurve: Curve,distanceTolerance: float,kinkTolerance: float) -> Array[BezierCurve]

  

   Constructs an array of cubic,non-rational beziers that fit a curve to a tolerance.

  

   sourceCurve: A curve to approximate.

   distanceTolerance: The max fitting error. Use RhinoMath.SqrtEpsilon as a minimum.

   kinkTolerance: If the input curve has a g1-discontinuity with angle radian measure

     greater than 

    kinkTolerance at some point P,the list of beziers will

     also have a kink at P.

  

   Returns: A new array of bezier curves. The array can be empty and might contain null items.
  """
  pass
 @staticmethod
 def CreateLoftedBezier(points):
  """
  CreateLoftedBezier(points: IEnumerable[Point2d]) -> BezierCurve

  CreateLoftedBezier(points: IEnumerable[Point3d]) -> BezierCurve
  """
  pass
 def CurvatureAt(self,t):
  """
  CurvatureAt(self: BezierCurve,t: float) -> Vector3d

  

   Evaluate the curvature vector at a curve parameter.

  

   t: Evaluation parameter.

   Returns: Curvature vector of the curve at the parameter t.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: BezierCurve)

   Actively reclaims unmanaged resources that this instance uses.
  """
  pass
 def GetBoundingBox(self,accurate):
  """
  GetBoundingBox(self: BezierCurve,accurate: bool) -> BoundingBox

  

   Boundingbox solver. Gets the world axis aligned boundingbox for the curve.

  

   accurate: If true,a physically accurate boundingbox will be computed. 

     If not,a boundingbox 

    estimate will be computed. For some geometry types there is no 

     difference between 

    the estimate and the accurate boundingbox. Estimated boundingboxes 

     can be computed 

    much (much) faster than accurate (or "tight") bounding boxes. 

     Estimated bounding 

    boxes are always similar to or larger than accurate bounding boxes.

  

   Returns: The boundingbox of the geometry in world coordinates or BoundingBox.Empty 

     if not 

    bounding box could be found.
  """
  pass
 def GetControlVertex2d(self,index):
  """
  GetControlVertex2d(self: BezierCurve,index: int) -> Point2d

  

   Get location of a control vertex.

  

   index: Control vertex index (0 <= index < ControlVertexCount)

   Returns: If the bezier is rational,the euclidean location is returned.
  """
  pass
 def GetControlVertex3d(self,index):
  """
  GetControlVertex3d(self: BezierCurve,index: int) -> Point3d

  

   Get location of a control vertex.

  

   index: Control vertex index (0 <= index < ControlVertexCount)

   Returns: If the bezier is rational,the euclidean location is returned.
  """
  pass
 def GetControlVertex4d(self,index):
  """
  GetControlVertex4d(self: BezierCurve,index: int) -> Point4d

  

   Get location of a control vertex.

  

   index: Control vertex index (0 <= index < ControlVertexCount)

   Returns: Homogenous value of control vertex. If the bezier is not

     rational,the weight is 1.
  """
  pass
 def IncreaseDegree(self,desiredDegree):
  """
  IncreaseDegree(self: BezierCurve,desiredDegree: int) -> bool

  

   Increase degree of bezier

   Returns: true if successful.  false if desiredDegree < current degree.
  """
  pass
 def MakeNonRational(self):
  """
  MakeNonRational(self: BezierCurve) -> bool

  

   Make bezier non-rational

   Returns: treu if successful
  """
  pass
 def MakeRational(self):
  """
  MakeRational(self: BezierCurve) -> bool

  

   Make bezier rational

   Returns: true if successful
  """
  pass
 def PointAt(self,t):
  """
  PointAt(self: BezierCurve,t: float) -> Point3d

  

   Evaluates point at a curve parameter.

  

   t: Evaluation parameter.

   Returns: Point (location of curve at the parameter t).
  """
  pass
 def TangentAt(self,t):
  """
  TangentAt(self: BezierCurve,t: float) -> Vector3d

  

   Evaluates the unit tangent vector at a curve parameter.

  

   t: Evaluation parameter.

   Returns: Unit tangent vector of the curve at the parameter t.
  """
  pass
 def ToNurbsCurve(self):
  """
  ToNurbsCurve(self: BezierCurve) -> NurbsCurve

  

   Constructs a NURBS curve representation of this curve.

   Returns: NURBS representation of the curve on success,null on failure.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,controlPoints):
  """
  __new__(cls: type,controlPoints: IEnumerable[Point2d])

  __new__(cls: type,controlPoints: IEnumerable[Point3d])

  __new__(cls: type,controlPoints: IEnumerable[Point4d])
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ControlVertexCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of control vertices in this curve



Get: ControlVertexCount(self: BezierCurve) -> int



"""

 IsRational=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not the curve is rational. 

   Rational curves have control-points with custom weights.



Get: IsRational(self: BezierCurve) -> bool



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Tests an object to see if it is valid.



Get: IsValid(self: BezierCurve) -> bool



"""


