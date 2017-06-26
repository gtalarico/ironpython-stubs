class Vector3f(object,IEquatable[Vector3f],IComparable[Vector3f],IComparable,IEpsilonFComparable[Vector3f]):
 """ Vector3f(x: Single,y: Single,z: Single) """
 @staticmethod
 def Add(point,vector):
  """ Add(point: Point3f,vector: Vector3f) -> Point3f """
  pass
 def CompareTo(self,other):
  """ CompareTo(self: Vector3f,other: Vector3f) -> int """
  pass
 @staticmethod
 def CrossProduct(a,b):
  """ CrossProduct(a: Vector3f,b: Vector3f) -> Vector3f """
  pass
 def EpsilonEquals(self,other,epsilon):
  """ EpsilonEquals(self: Vector3f,other: Vector3f,epsilon: Single) -> bool """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Vector3f,vector: Vector3f) -> bool
  Equals(self: Vector3f,obj: object) -> bool
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: Vector3f) -> int """
  pass
 @staticmethod
 def Multiply(*__args):
  """
  Multiply(t: Single,vector: Vector3f) -> Vector3f
  Multiply(vector: Vector3f,t: Single) -> Vector3f
  """
  pass
 def PerpendicularTo(self,other):
  """ PerpendicularTo(self: Vector3f,other: Vector3f) -> bool """
  pass
 def Reverse(self):
  """ Reverse(self: Vector3f) -> bool """
  pass
 def Rotate(self,angleRadians,rotationAxis):
  """ Rotate(self: Vector3f,angleRadians: float,rotationAxis: Vector3f) -> bool """
  pass
 def ToString(self):
  """ ToString(self: Vector3f) -> str """
  pass
 def Transform(self,transformation):
  """ Transform(self: Vector3f,transformation: Transform) """
  pass
 def Unitize(self):
  """ Unitize(self: Vector3f) -> bool """
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
 def __mul__(self,*args):
  """ x.__mul__(y) <==> x*y """
  pass
 @staticmethod
 def __new__(self,x,y,z):
  """
  __new__[Vector3f]() -> Vector3f
  
  __new__(cls: type,x: Single,y: Single,z: Single)
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """ __radd__(point: Point3f,vector: Vector3f) -> Point3f """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rmul__(self,*args):
  """ __rmul__(t: Single,vector: Vector3f) -> Vector3f """
  pass
 def __str__(self,*args):
  pass
 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Length(self: Vector3f) -> Single

"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: X(self: Vector3f) -> Single

Set: X(self: Vector3f)=value
"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Y(self: Vector3f) -> Single

Set: Y(self: Vector3f)=value
"""

 Z=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Z(self: Vector3f) -> Single

Set: Z(self: Vector3f)=value
"""


 Unset=None
 XAxis=None
 YAxis=None
 ZAxis=None
 Zero=None


# variables with complex values

