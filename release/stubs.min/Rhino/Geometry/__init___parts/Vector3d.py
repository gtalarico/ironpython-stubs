class Vector3d(object,ISerializable,IEquatable[Vector3d],IComparable[Vector3d],IComparable,IEpsilonComparable[Vector3d]):
 """
 Vector3d(x: float,y: float,z: float)
 Vector3d(point: Point3d)
 Vector3d(vector: Vector3f)
 Vector3d(vector: Vector3d)
 """
 @staticmethod
 def Add(vector1,vector2):
  """ Add(vector1: Vector3d,vector2: Vector3d) -> Vector3d """
  pass
 def CompareTo(self,other):
  """ CompareTo(self: Vector3d,other: Vector3d) -> int """
  pass
 @staticmethod
 def CrossProduct(a,b):
  """ CrossProduct(a: Vector3d,b: Vector3d) -> Vector3d """
  pass
 @staticmethod
 def Divide(vector,t):
  """ Divide(vector: Vector3d,t: float) -> Vector3d """
  pass
 def EpsilonEquals(self,other,epsilon):
  """ EpsilonEquals(self: Vector3d,other: Vector3d,epsilon: float) -> bool """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Vector3d,vector: Vector3d) -> bool
  Equals(self: Vector3d,obj: object) -> bool
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: Vector3d) -> int """
  pass
 def IsParallelTo(self,other,angleTolerance=None):
  """
  IsParallelTo(self: Vector3d,other: Vector3d,angleTolerance: float) -> int
  IsParallelTo(self: Vector3d,other: Vector3d) -> int
  """
  pass
 def IsPerpendicularTo(self,other,angleTolerance=None):
  """
  IsPerpendicularTo(self: Vector3d,other: Vector3d,angleTolerance: float) -> bool
  IsPerpendicularTo(self: Vector3d,other: Vector3d) -> bool
  """
  pass
 def IsTiny(self,tolerance=None):
  """
  IsTiny(self: Vector3d) -> bool
  IsTiny(self: Vector3d,tolerance: float) -> bool
  """
  pass
 @staticmethod
 def Multiply(*__args):
  """
  Multiply(vector1: Vector3d,vector2: Vector3d) -> float
  Multiply(t: float,vector: Vector3d) -> Vector3d
  Multiply(vector: Vector3d,t: float) -> Vector3d
  """
  pass
 @staticmethod
 def Negate(vector):
  """ Negate(vector: Vector3d) -> Vector3d """
  pass
 def PerpendicularTo(self,other):
  """ PerpendicularTo(self: Vector3d,other: Vector3d) -> bool """
  pass
 def Reverse(self):
  """ Reverse(self: Vector3d) -> bool """
  pass
 def Rotate(self,angleRadians,rotationAxis):
  """ Rotate(self: Vector3d,angleRadians: float,rotationAxis: Vector3d) -> bool """
  pass
 @staticmethod
 def Subtract(vector1,vector2):
  """ Subtract(vector1: Vector3d,vector2: Vector3d) -> Vector3d """
  pass
 def ToString(self):
  """ ToString(self: Vector3d) -> str """
  pass
 def Transform(self,transformation):
  """ Transform(self: Vector3d,transformation: Transform) """
  pass
 def Unitize(self):
  """ Unitize(self: Vector3d) -> bool """
  pass
 @staticmethod
 def VectorAngle(a,b,plane=None):
  """
  VectorAngle(a: Vector3d,b: Vector3d,plane: Plane) -> float
  VectorAngle(a: Vector3d,b: Vector3d) -> float
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
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
  """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
  pass
 def __neg__(self,*args):
  """ x.__neg__() <==> -x """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Vector3d]() -> Vector3d
  
  __new__(cls: type,x: float,y: float,z: float)
  __new__(cls: type,point: Point3d)
  __new__(cls: type,vector: Vector3f)
  __new__(cls: type,vector: Vector3d)
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """ __radd__(vector1: Vector3d,vector2: Vector3d) -> Vector3d """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rmul__(self,*args):
  """
  __rmul__(vector1: Vector3d,vector2: Vector3d) -> float
  __rmul__(t: float,vector: Vector3d) -> Vector3d
  """
  pass
 def __rsub__(self,*args):
  """ __rsub__(vector1: Vector3d,vector2: Vector3d) -> Vector3d """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 IsUnitVector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsUnitVector(self: Vector3d) -> bool

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValid(self: Vector3d) -> bool

"""

 IsZero=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsZero(self: Vector3d) -> bool

"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Length(self: Vector3d) -> float

"""

 MaximumCoordinate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaximumCoordinate(self: Vector3d) -> float

"""

 MinimumCoordinate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MinimumCoordinate(self: Vector3d) -> float

"""

 SquareLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SquareLength(self: Vector3d) -> float

"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: X(self: Vector3d) -> float

Set: X(self: Vector3d)=value
"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Y(self: Vector3d) -> float

Set: Y(self: Vector3d)=value
"""

 Z=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Z(self: Vector3d) -> float

Set: Z(self: Vector3d)=value
"""


 Unset=None
 XAxis=None
 YAxis=None
 ZAxis=None
 Zero=None

