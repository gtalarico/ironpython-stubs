class Point2f(object,IEquatable[Point2f],IComparable[Point2f],IComparable,IEpsilonFComparable[Point2f]):
 """
 Point2f(x: Single,y: Single)
 Point2f(x: float,y: float)
 """
 def CompareTo(self,other):
  """ CompareTo(self: Point2f,other: Point2f) -> int """
  pass
 def EpsilonEquals(self,other,epsilon):
  """ EpsilonEquals(self: Point2f,other: Point2f,epsilon: Single) -> bool """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Point2f,point: Point2f) -> bool
  Equals(self: Point2f,obj: object) -> bool
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: Point2f) -> int """
  pass
 def ToString(self):
  """ ToString(self: Point2f) -> str """
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
  __new__[Point2f]() -> Point2f
  
  __new__(cls: type,x: Single,y: Single)
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
 """Get: IsValid(self: Point2f) -> bool

"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: X(self: Point2f) -> Single

Set: X(self: Point2f)=value
"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Y(self: Point2f) -> Single

Set: Y(self: Point2f)=value
"""


 Unset=None

