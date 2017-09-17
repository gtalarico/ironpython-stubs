class Point4d(object,ISerializable,IEquatable[Point4d],IEpsilonComparable[Point4d]):
 """
 Point4d(x: float,y: float,z: float,w: float)
 Point4d(point: Point3d)
 """
 @staticmethod
 def Add(point1,point2):
  """ Add(point1: Point4d,point2: Point4d) -> Point4d """
  pass
 def EpsilonEquals(self,other,epsilon):
  """ EpsilonEquals(self: Point4d,other: Point4d,epsilon: float) -> bool """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Point4d,point: Point4d) -> bool
  Equals(self: Point4d,obj: object) -> bool
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: Point4d) -> int """
  pass
 @staticmethod
 def Multiply(point,d):
  """ Multiply(point: Point4d,d: float) -> Point4d """
  pass
 @staticmethod
 def Subtract(point1,point2):
  """ Subtract(point1: Point4d,point2: Point4d) -> Point4d """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __mul__(self,*args):
  """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Point4d]() -> Point4d
  
  __new__(cls: type,x: float,y: float,z: float,w: float)
  __new__(cls: type,point: Point3d)
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """ __radd__(point1: Point4d,point2: Point4d) -> Point4d """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rmul__(self,*args):
  """ __rmul__(point1: Point4d,point2: Point4d) -> float """
  pass
 def __rsub__(self,*args):
  """ __rsub__(point1: Point4d,point2: Point4d) -> Point4d """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 W=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: W(self: Point4d) -> float

Set: W(self: Point4d)=value
"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: X(self: Point4d) -> float

Set: X(self: Point4d)=value
"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Y(self: Point4d) -> float

Set: Y(self: Point4d)=value
"""

 Z=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Z(self: Point4d) -> float

Set: Z(self: Point4d)=value
"""


 Unset=None

