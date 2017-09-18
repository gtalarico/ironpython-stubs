class HermiteSpline(Curve,IDisposable):
 """ A Hermite spline. """
 @staticmethod
 def Create(controlPoints,periodic,tangents=None):
  """
  Create(controlPoints: IList[XYZ],periodic: bool) -> HermiteSpline
  Create(controlPoints: IList[XYZ],periodic: bool,tangents: HermiteSplineTangents) -> HermiteSpline
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
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 ControlPoints=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The control points of the Hermite spline.

Get: ControlPoints(self: HermiteSpline) -> IList[XYZ]

Set: ControlPoints(self: HermiteSpline)=value
"""

 IsPeriodic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns whether the Hermite spline is periodic or not.

Get: IsPeriodic(self: HermiteSpline) -> bool

"""

 Parameters=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the params of the Hermite spline.

Get: Parameters(self: HermiteSpline) -> DoubleArray

"""

 Tangents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the tangents of the Hermite spline.

Get: Tangents(self: HermiteSpline) -> IList[XYZ]

"""


