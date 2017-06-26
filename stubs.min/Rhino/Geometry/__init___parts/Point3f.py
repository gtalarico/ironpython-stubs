class Point3f(object,IEquatable[Point3f],IComparable[Point3f],IComparable,IEpsilonFComparable[Point3f]):
 """ Point3f(x: Single,y: Single,z: Single) """
 def CompareTo(self,other):
  """ CompareTo(self: Point3f,other: Point3f) -> int """
  pass
 def DistanceTo(self,other):
  """ DistanceTo(self: Point3f,other: Point3f) -> float """
  pass
 def EpsilonEquals(self,other,epsilon):
  """ EpsilonEquals(self: Point3f,other: Point3f,epsilon: Single) -> bool """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Point3f,point: Point3f) -> bool
  Equals(self: Point3f,obj: object) -> bool
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: Point3f) -> int """
  pass
 @staticmethod
 def Subtract(point1,point2):
  """ Subtract(point1: Point3f,point2: Point3f) -> Vector3f """
  pass
 def ToString(self):
  """ ToString(self: Point3f) -> str """
  pass
 def Transform(self,xform):
  """ Transform(self: Point3f,xform: Transform) """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
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
 @staticmethod
 def __new__(self,x,y,z):
  """
  __new__[Point3f]() -> Point3f
  
  __new__(cls: type,x: Single,y: Single,z: Single)
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rsub__(self,*args):
  """ __rsub__(point1: Point3f,point2: Point3f) -> Vector3f """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValid(self: Point3f) -> bool

"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: X(self: Point3f) -> Single

Set: X(self: Point3f)=value
"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Y(self: Point3f) -> Single

Set: Y(self: Point3f)=value
"""

 Z=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Z(self: Point3f) -> Single

Set: Z(self: Point3f)=value
"""


 Origin=None
 Unset=None

