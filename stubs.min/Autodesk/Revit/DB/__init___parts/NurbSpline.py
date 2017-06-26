class NurbSpline(Curve,IDisposable):
 """ A nurb spline. """
 @staticmethod
 def Create(*__args):
  """
  Create(controlPoints: IList[XYZ],weights: IList[float],knots: IList[float],degree: int,closed: bool,rational: bool) -> NurbSpline
  Create(controlPoints: IList[XYZ],weights: IList[float]) -> NurbSpline
  Create(hermiteSpline: HermiteSpline) -> NurbSpline
  
   Creates a new geometric NurbSpline object from a HermiteSpline.
  
   hermiteSpline: The hermite spline that will be converted to NurbSpline.
   Returns: The new NurbSpline object.
  """
  pass
 @staticmethod
 def CreateCurve(*__args):
  """
  CreateCurve(degree: int,knots: IList[float],controlPoints: IList[XYZ],weights: IList[float]) -> Curve
  CreateCurve(degree: int,knots: IList[float],controlPoints: IList[XYZ]) -> Curve
  CreateCurve(hermiteSpline: HermiteSpline) -> Curve
  
   Creates a new geometric Curve object by converting the given HermiteSpline.
     
    The created curve may be a NURBSpline or a simpler curve such as line or arc.
  
  
   hermiteSpline: The HermiteSpline that will be converted.
   Returns: The new Curve object.
  CreateCurve(controlPoints: IList[XYZ],weights: IList[float]) -> Curve
  """
  pass
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: GeometryObject) """
  pass
 def SetControlPointsAndWeights(self,ctrlPoints,weights):
  """ SetControlPointsAndWeights(self: NurbSpline,ctrlPoints: IList[XYZ],weights: DoubleArray) """
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
 CtrlPoints=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the control points of the nurb spline.

Get: CtrlPoints(self: NurbSpline) -> IList[XYZ]

"""

 Degree=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the degree of the nurb spline.

Get: Degree(self: NurbSpline) -> int

"""

 isClosed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Return/set the nurb spline's isClosed property.

Get: isClosed(self: NurbSpline) -> bool

Set: isClosed(self: NurbSpline)=value
"""

 isRational=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns whether the nurb spline is rational or not.

Get: isRational(self: NurbSpline) -> bool

"""

 Knots=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Return/set the knots of the nurb spline.

Get: Knots(self: NurbSpline) -> DoubleArray

Set: Knots(self: NurbSpline)=value
"""

 Weights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the weights of the nurb spline.

Get: Weights(self: NurbSpline) -> DoubleArray

"""


