class Point2d(object,ISerializable,IEquatable[Point2d],IComparable[Point2d],IComparable,IEpsilonComparable[Point2d]):
 """
 Point2d(x: float,y: float)
 Point2d(vector: Vector2d)
 Point2d(point: Point2d)
 Point2d(point: Point3d)
 """
 @staticmethod
 def Add(*__args):
  """
  Add(point1: Point2d,point2: Point2d) -> Point2d
  Add(vector: Vector2d,point: Point2d) -> Point2d
  Add(point: Point2d,vector: Vector2d) -> Point2d
  """
  pass
 def CompareTo(self,other):
  """ CompareTo(self: Point2d,other: Point2d) -> int """
  pass
 def DistanceTo(self,other):
  """ DistanceTo(self: Point2d,other: Point2d) -> float """
  pass
 @staticmethod
 def Divide(point,t):
  """ Divide(point: Point2d,t: float) -> Point2d """
  pass
 def EpsilonEquals(self,other,epsilon):
  """ EpsilonEquals(self: Point2d,other: Point2d,epsilon: float) -> bool """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Point2d,point: Point2d) -> bool
  Equals(self: Point2d,obj: object) -> bool
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: Point2d) -> int """
  pass
 @staticmethod
 def Multiply(*__args):
  """
  Multiply(t: float,point: Point2d) -> Point2d
  Multiply(point: Point2d,t: float) -> Point2d
  """
  pass
 @staticmethod
 def Subtract(*__args):
  """
  Subtract(point1: Point2d,point2: Point2d) -> Vector2d
  Subtract(point: Point2d,vector: Vector2d) -> Point2d
  """
  pass
 def ToString(self):
  """ ToString(self: Point2d) -> str """
  pass
 def Transform(self,xform):
  """ Transform(self: Point2d,xform: Transform) """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __div__(self,*args):
  """ x.__div__(y) <==> x/y """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __mul__(self,*args):
  """ x.__mul__(y) <==> x*y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Point2d]() -> Point2d
  
  __new__(cls: type,x: float,y: float)
  __new__(cls: type,vector: Vector2d)
  __new__(cls: type,point: Point2d)
  __new__(cls: type,point: Point3d)
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """
  __radd__(point1: Point2d,point2: Point2d) -> Point2d
  __radd__(vector: Vector2d,point: Point2d) -> Point2d
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rmul__(self,*args):
  """ __rmul__(t: float,point: Point2d) -> Point2d """
  pass
 def __rsub__(self,*args):
  """ __rsub__(point1: Point2d,point2: Point2d) -> Vector2d """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
  pass
 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValid(self: Point2d) -> bool

"""

 MaximumCoordinate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaximumCoordinate(self: Point2d) -> float

"""

 MinimumCoordinate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MinimumCoordinate(self: Point2d) -> float

"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: X(self: Point2d) -> float

Set: X(self: Point2d)=value
"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Y(self: Point2d) -> float

Set: Y(self: Point2d)=value
"""


 Origin=None
 Unset=None

