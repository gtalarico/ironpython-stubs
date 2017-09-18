class NurbsCurve(Curve,IDisposable,ISerializable,IEpsilonComparable[NurbsCurve]):
 """
 Represents a Non Uniform Rational B-Splines (NURBS) curve.

 

 NurbsCurve(other: NurbsCurve)

 NurbsCurve(degree: int,pointCount: int)

 NurbsCurve(dimension: int,rational: bool,order: int,pointCount: int)
 """
 def ConstructConstObject(self,*args):
  """
  ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int)

   Assigns a parent object and a subobject index to this.

  

   parentObject: The parent object.

   subobject_index: The subobject index.
  """
  pass
 @staticmethod
 def Create(periodic,degree,points):
  """ Create(periodic: bool,degree: int,points: IEnumerable[Point3d]) -> NurbsCurve """
  pass
 @staticmethod
 def CreateFromArc(arc):
  """
  CreateFromArc(arc: Arc) -> NurbsCurve

  

   Gets a rational degree 2 NURBS curve representation

     of the arc. Note that the 

    parameterization of NURBS curve

     does not match arc's transcendental 

    paramaterization.

  

   Returns: Curve on success,null on failure.
  """
  pass
 @staticmethod
 def CreateFromCircle(circle):
  """
  CreateFromCircle(circle: Circle) -> NurbsCurve

  

   Gets a rational degree 2 NURBS curve representation

     of the circle. Note that the 

    parameterization of NURBS curve

     does not match circle's transcendental 

    paramaterization.  

     Use GetRadianFromNurbFormParameter() and

     

    GetParameterFromRadian() to convert between the NURBS curve 

     parameter and the 

    transcendental parameter.

  

   Returns: Curve on success,null on failure.
  """
  pass
 @staticmethod
 def CreateFromEllipse(ellipse):
  """
  CreateFromEllipse(ellipse: Ellipse) -> NurbsCurve

  

   Gets a rational degree 2 NURBS curve representation of the ellipse.

     Note that the 

    parameterization of the NURBS curve does not match

     with the transcendental 

    paramaterization of the ellipsis.

  

   Returns: A nurbs curve representation of this ellipse or null if no such representation could be made.
  """
  pass
 @staticmethod
 def CreateFromLine(line):
  """
  CreateFromLine(line: Line) -> NurbsCurve

  

   Gets a non-rational,degree 1 Nurbs curve representation of the line.

   Returns: Curve on success,null on failure.
  """
  pass
 @staticmethod
 def CreateSpiral(*__args):
  """
  CreateSpiral(railCurve: Curve,t0: float,t1: float,radiusPoint: Point3d,pitch: float,turnCount: float,radius0: float,radius1: float,pointsPerTurn: int) -> NurbsCurve

  

   Create a C2 non-rational uniform cubic NURBS approximation of a swept helix or spiral.

  

   railCurve: The rail curve.

   t0: Starting portion of rail curve's domain to sweep along.

   t1: Ending portion of rail curve's domain to sweep along.

   radiusPoint: Point used only to get a vector that is perpedicular to the axis. In

     particular,

    this vector must not be (anti)parallel to the axis vector.

  

   pitch: The pitch. Positive values produce counter-clockwise orientation,

     negative values 

    produce clockwise orientation.

  

   turnCount: The turn count. If != 0,then the resulting helix will have this many

     turns. If=

    0,then pitch must be != 0 and the approximate distance

     between turns will be set 

    to pitch. Positive values produce counter-clockwise

     orientation,negitive values 

    produce clockwise orientation.

  

   radius0: The starting radius. At least one radii must benonzero. Negative values

     are allowed.

   radius1: The ending radius. At least ont radii must be nonzero. Negative values

     are allowed.

   pointsPerTurn: Number of points to intepolate per turn. Must be greater than 4.

     When in doubt,use 

    12.

  

   Returns: NurbsCurve on success,null on failure.

  CreateSpiral(axisStart: Point3d,axisDir: Vector3d,radiusPoint: Point3d,pitch: float,turnCount: float,radius0: float,radius1: float) -> NurbsCurve

  

   Creates a C1 cubic NURBS approximation of a helix or spiral. For a helix,

     you may 

    have radius0 == radius1. For a spiral radius0 == radius0 produces

     a circle. Zero 

    and negative radii are permissible.

  

  

   axisStart: Helix's axis starting point or center of spiral.

   axisDir: Helix's axis vector or normal to spiral's plane.

   radiusPoint: Point used only to get a vector that is perpedicular to the axis. In

     particular,

    this vector must not be (anti)parallel to the axis vector.

  

   pitch: The pitch,where a spiral has a pitch=0,and pitch > 0 is the distance

     between 

    the helix's "threads".

  

   turnCount: The number of turns in spiral or helix. Positive

     values produce counter-clockwise 

    orientation,negitive values produce

     clockwise orientation. Note,for a helix,

    turnCount * pitch=length of

     the helix's axis.

  

   radius0: The starting radius.

   radius1: The ending radius.

   Returns: NurbsCurve on success,null on failure.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Curve,disposing: bool)

   For derived class implementers.

     This method is called with argument true when class 

    user calls Dispose(),while with argument false when

     the Garbage Collector invokes 

    the finalizer,or Finalize() method.You must reclaim all used unmanaged resources in both cases,

    and can use this chance to call Dispose on disposable fields if the argument is true.Also,you 

    must call the base virtual method within your overriding method.

  

  

   disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 

    finalizer.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: NurbsCurve,other: NurbsCurve,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def GrevilleParameter(self,index):
  """
  GrevilleParameter(self: NurbsCurve,index: int) -> float

  

   Gets the greville (edit point) parameter that belongs 

     to the control point at the 

    specified index.

  

  

   index: Index of Greville (Edit) point.
  """
  pass
 def GrevilleParameters(self):
  """
  GrevilleParameters(self: NurbsCurve) -> Array[float]

  

   Gets all Greville (Edit point) parameters for this curve.
  """
  pass
 def GrevillePoint(self,index):
  """
  GrevillePoint(self: NurbsCurve,index: int) -> Point3d

  

   Gets the greville (edit point) parameter that belongs 

     to the control point at the 

    specified index.

  

  

   index: Index of Greville (Edit) point.
  """
  pass
 def GrevillePoints(self):
  """
  GrevillePoints(self: NurbsCurve) -> Point3dList

  

   Gets all Greville (Edit) points for this curve.
  """
  pass
 def IncreaseDegree(self,desiredDegree):
  """
  IncreaseDegree(self: NurbsCurve,desiredDegree: int) -> bool

  

   Increase the degree of this curve.

  

   desiredDegree: The desired degree. 

     Degrees should be number between and including 1 and 11.

   Returns: true on success,false on failure.
  """
  pass
 @staticmethod
 def IsDuplicate(curveA,curveB,ignoreParameterization,tolerance):
  """
  IsDuplicate(curveA: NurbsCurve,curveB: NurbsCurve,ignoreParameterization: bool,tolerance: float) -> bool

  

   Determines if two curves are similar.

  

   curveA: First curve used in comparison.

   curveB: Second curve used in comparison.

   ignoreParameterization: if true,parameterization and orientaion are ignored.

   tolerance: tolerance to use when comparing control points.

   Returns: true if curves are similar within tolerance.
  """
  pass
 def MakePiecewiseBezier(self,setEndWeightsToOne):
  """
  MakePiecewiseBezier(self: NurbsCurve,setEndWeightsToOne: bool) -> bool

  

   Clamps ends and adds knots so the NURBS curve has bezier spans 

     (all distinct knots 

    have multiplitity=degree).

  

  

   setEndWeightsToOne: If true and the first or last weight is not one,then the first and

     last spans are 

    reparameterized so that the end weights are one.

  

   Returns: true on success,false on failure.
  """
  pass
 def NonConstOperation(self,*args):
  """
  NonConstOperation(self: Curve)

   For derived classes implementers.

     Defines the necessary implementation to free the 

    instance from being const.
  """
  pass
 def OnSwitchToNonConst(self,*args):
  """
  OnSwitchToNonConst(self: GeometryBase)

   Is called when a non-const operation occurs.
  """
  pass
 def Reparameterize(self,c):
  """
  Reparameterize(self: NurbsCurve,c: float) -> bool

  

   Use a linear fractional transformation to reparameterize the NURBS curve.

     This does 

    not change the curve's domain.

  

  

   c: reparameterization constant (generally speaking,c should be > 0). The

     control 

    points and knots are adjusted so that

     output_nurbs(t)=input_nurbs(lambda(t)),

    where lambda(t)=c*t/( (c-1)*t + 1 ).

     Note that lambda(0)=0,lambda(1)=1,

    lambda'(t) > 0,

     lambda'(0)=c and lambda'(1)=1/c.

  

   Returns: true if successful.
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
 def __new__(self,*__args):
  """
  __new__(cls: type,other: NurbsCurve)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)

  __new__(cls: type,degree: int,pointCount: int)

  __new__(cls: type,dimension: int,rational: bool,order: int,pointCount: int)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 HasBezierSpans=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns true if the NURBS curve has bezier spans (all distinct knots have multiplitity=degree)



Get: HasBezierSpans(self: NurbsCurve) -> bool



"""

 IsRational=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not the curve is rational. 

   Rational curves have control-points with custom weights.



Get: IsRational(self: NurbsCurve) -> bool



"""

 Knots=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets access to the knots (or "knot vector") of this nurbs curve.



Get: Knots(self: NurbsCurve) -> NurbsCurveKnotList



"""

 Order=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the order of the curve. Order=Degree + 1.



Get: Order(self: NurbsCurve) -> int



"""

 Points=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets access to the control points of this nurbs curve.



Get: Points(self: NurbsCurve) -> NurbsCurvePointList



"""


