class Circle(object,IEpsilonComparable[Circle]):
 """
 Circle(radius: float)
 Circle(plane: Plane,radius: float)
 Circle(center: Point3d,radius: float)
 Circle(arc: Arc)
 Circle(point1: Point3d,point2: Point3d,point3: Point3d)
 Circle(plane: Plane,center: Point3d,radius: float)
 Circle(startPoint: Point3d,tangentAtP: Vector3d,pointOnCircle: Point3d)
 """
 def ClosestParameter(self,testPoint,t):
  """ ClosestParameter(self: Circle,testPoint: Point3d) -> (bool,float) """
  pass
 def ClosestPoint(self,testPoint):
  """ ClosestPoint(self: Circle,testPoint: Point3d) -> Point3d """
  pass
 def DerivativeAt(self,derivative,t):
  """ DerivativeAt(self: Circle,derivative: int,t: float) -> Vector3d """
  pass
 def EpsilonEquals(self,other,epsilon):
  """ EpsilonEquals(self: Circle,other: Circle,epsilon: float) -> bool """
  pass
 def IsInPlane(self,plane,tolerance):
  """ IsInPlane(self: Circle,plane: Plane,tolerance: float) -> bool """
  pass
 def PointAt(self,t):
  """ PointAt(self: Circle,t: float) -> Point3d """
  pass
 def Reverse(self):
  """ Reverse(self: Circle) """
  pass
 def Rotate(self,*__args):
  """
  Rotate(self: Circle,angle: float,axis: Vector3d) -> bool
  Rotate(self: Circle,angle: float,axis: Vector3d,point: Point3d) -> bool
  Rotate(self: Circle,sinAngle: float,cosAngle: float,axis: Vector3d) -> bool
  Rotate(self: Circle,sinAngle: float,cosAngle: float,axis: Vector3d,point: Point3d) -> bool
  """
  pass
 def TangentAt(self,t):
  """ TangentAt(self: Circle,t: float) -> Vector3d """
  pass
 def ToNurbsCurve(self):
  """ ToNurbsCurve(self: Circle) -> NurbsCurve """
  pass
 def Transform(self,xform):
  """ Transform(self: Circle,xform: Transform) -> bool """
  pass
 def Translate(self,delta):
  """ Translate(self: Circle,delta: Vector3d) -> bool """
  pass
 @staticmethod
 def TryFitCircleTT(c1,c2,t1,t2):
  """ TryFitCircleTT(c1: Curve,c2: Curve,t1: float,t2: float) -> Circle """
  pass
 @staticmethod
 def TryFitCircleTTT(c1,c2,c3,t1,t2,t3):
  """ TryFitCircleTTT(c1: Curve,c2: Curve,c3: Curve,t1: float,t2: float,t3: float) -> Circle """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Circle]() -> Circle
  
  __new__(cls: type,radius: float)
  __new__(cls: type,plane: Plane,radius: float)
  __new__(cls: type,center: Point3d,radius: float)
  __new__(cls: type,arc: Arc)
  __new__(cls: type,point1: Point3d,point2: Point3d,point3: Point3d)
  __new__(cls: type,plane: Plane,center: Point3d,radius: float)
  __new__(cls: type,startPoint: Point3d,tangentAtP: Vector3d,pointOnCircle: Point3d)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 BoundingBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BoundingBox(self: Circle) -> BoundingBox

"""

 Center=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Center(self: Circle) -> Point3d

Set: Center(self: Circle)=value
"""

 Circumference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Circumference(self: Circle) -> float

Set: Circumference(self: Circle)=value
"""

 Diameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Diameter(self: Circle) -> float

Set: Diameter(self: Circle)=value
"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValid(self: Circle) -> bool

"""

 Normal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Normal(self: Circle) -> Vector3d

"""

 Plane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Plane(self: Circle) -> Plane

Set: Plane(self: Circle)=value
"""

 Radius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Radius(self: Circle) -> float

Set: Radius(self: Circle)=value
"""


 Unset=None

