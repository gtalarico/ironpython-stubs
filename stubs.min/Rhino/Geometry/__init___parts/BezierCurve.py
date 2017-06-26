class BezierCurve(object,IDisposable):
 """
 BezierCurve(controlPoints: IEnumerable[Point2d])
 BezierCurve(controlPoints: IEnumerable[Point3d])
 BezierCurve(controlPoints: IEnumerable[Point4d])
 """
 def ChangeDimension(self,desiredDimension):
  """ ChangeDimension(self: BezierCurve,desiredDimension: int) -> bool """
  pass
 @staticmethod
 def CreateLoftedBezier(points):
  """
  CreateLoftedBezier(points: IEnumerable[Point2d]) -> BezierCurve
  CreateLoftedBezier(points: IEnumerable[Point3d]) -> BezierCurve
  """
  pass
 def CurvatureAt(self,t):
  """ CurvatureAt(self: BezierCurve,t: float) -> Vector3d """
  pass
 def Dispose(self):
  """ Dispose(self: BezierCurve) """
  pass
 def GetBoundingBox(self,accurate):
  """ GetBoundingBox(self: BezierCurve,accurate: bool) -> BoundingBox """
  pass
 def GetControlVertex2d(self,index):
  """ GetControlVertex2d(self: BezierCurve,index: int) -> Point2d """
  pass
 def GetControlVertex3d(self,index):
  """ GetControlVertex3d(self: BezierCurve,index: int) -> Point3d """
  pass
 def GetControlVertex4d(self,index):
  """ GetControlVertex4d(self: BezierCurve,index: int) -> Point4d """
  pass
 def IncreaseDegree(self,desiredDegree):
  """ IncreaseDegree(self: BezierCurve,desiredDegree: int) -> bool """
  pass
 def MakeNonRational(self):
  """ MakeNonRational(self: BezierCurve) -> bool """
  pass
 def MakeRational(self):
  """ MakeRational(self: BezierCurve) -> bool """
  pass
 def PointAt(self,t):
  """ PointAt(self: BezierCurve,t: float) -> Point3d """
  pass
 def TangentAt(self,t):
  """ TangentAt(self: BezierCurve,t: float) -> Vector3d """
  pass
 def ToNurbsCurve(self):
  """ ToNurbsCurve(self: BezierCurve) -> NurbsCurve """
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
 """Get: ControlVertexCount(self: BezierCurve) -> int

"""

 IsRational=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsRational(self: BezierCurve) -> bool

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValid(self: BezierCurve) -> bool

"""


