class Rectangle3d(object,IEpsilonComparable[Rectangle3d]):
 """
 Rectangle3d(plane: Plane,width: float,height: float)
 Rectangle3d(plane: Plane,width: Interval,height: Interval)
 Rectangle3d(plane: Plane,cornerA: Point3d,cornerB: Point3d)
 """
 def ClosestPoint(self,point,includeInterior=None):
  """
  ClosestPoint(self: Rectangle3d,point: Point3d,includeInterior: bool) -> Point3d
  ClosestPoint(self: Rectangle3d,point: Point3d) -> Point3d
  """
  pass
 def Contains(self,*__args):
  """
  Contains(self: Rectangle3d,x: float,y: float) -> PointContainment
  Contains(self: Rectangle3d,pt: Point3d) -> PointContainment
  """
  pass
 def Corner(self,index):
  """ Corner(self: Rectangle3d,index: int) -> Point3d """
  pass
 @staticmethod
 def CreateFromPolyline(polyline,deviation=None,angleDeviation=None):
  """
  CreateFromPolyline(polyline: IEnumerable[Point3d]) -> (Rectangle3d,float,float)
  CreateFromPolyline(polyline: IEnumerable[Point3d]) -> Rectangle3d
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """ EpsilonEquals(self: Rectangle3d,other: Rectangle3d,epsilon: float) -> bool """
  pass
 def MakeIncreasing(self):
  """ MakeIncreasing(self: Rectangle3d) """
  pass
 def PointAt(self,*__args):
  """
  PointAt(self: Rectangle3d,t: float) -> Point3d
  PointAt(self: Rectangle3d,x: float,y: float) -> Point3d
  """
  pass
 def RecenterPlane(self,*__args):
  """ RecenterPlane(self: Rectangle3d,origin: Point3d)RecenterPlane(self: Rectangle3d,index: int) """
  pass
 def ToNurbsCurve(self):
  """ ToNurbsCurve(self: Rectangle3d) -> NurbsCurve """
  pass
 def ToPolyline(self):
  """ ToPolyline(self: Rectangle3d) -> Polyline """
  pass
 def Transform(self,xform):
  """ Transform(self: Rectangle3d,xform: Transform) -> bool """
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
 """Get: Area(self: Rectangle3d) -> float

"""

 BoundingBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BoundingBox(self: Rectangle3d) -> BoundingBox

"""

 Center=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Center(self: Rectangle3d) -> Point3d

"""

 Circumference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Circumference(self: Rectangle3d) -> float

"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Height(self: Rectangle3d) -> float

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValid(self: Rectangle3d) -> bool

"""

 Plane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Plane(self: Rectangle3d) -> Plane

Set: Plane(self: Rectangle3d)=value
"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Width(self: Rectangle3d) -> float

"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: X(self: Rectangle3d) -> Interval

Set: X(self: Rectangle3d)=value
"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Y(self: Rectangle3d) -> Interval

Set: Y(self: Rectangle3d)=value
"""


 Unset=None

