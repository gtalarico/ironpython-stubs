class Vector2d(object,ISerializable,IEquatable[Vector2d],IComparable[Vector2d],IComparable,IEpsilonComparable[Vector2d]):
 """ Vector2d(x: float,y: float) """
 def CompareTo(self,other):
  """ CompareTo(self: Vector2d,other: Vector2d) -> int """
  pass
 def EpsilonEquals(self,other,epsilon):
  """ EpsilonEquals(self: Vector2d,other: Vector2d,epsilon: float) -> bool """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Vector2d,vector: Vector2d) -> bool
  Equals(self: Vector2d,obj: object) -> bool
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: Vector2d) -> int """
  pass
 def ToString(self):
  """ ToString(self: Vector2d) -> str """
  pass
 def Unitize(self):
  """ Unitize(self: Vector2d) -> bool """
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
 def __new__(self,x,y):
  """
  __new__[Vector2d]() -> Vector2d
  
  __new__(cls: type,x: float,y: float)
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValid(self: Vector2d) -> bool

"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Length(self: Vector2d) -> float

"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: X(self: Vector2d) -> float

Set: X(self: Vector2d)=value
"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Y(self: Vector2d) -> float

Set: Y(self: Vector2d)=value
"""


 Unset=None
 Zero=None

