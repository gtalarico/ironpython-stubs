class Ray3d(object,ISerializable,IEquatable[Ray3d],IEpsilonComparable[Ray3d]):
 """ Ray3d(position: Point3d,direction: Vector3d) """
 def EpsilonEquals(self,other,epsilon):
  """ EpsilonEquals(self: Ray3d,other: Ray3d,epsilon: float) -> bool """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Ray3d,ray: Ray3d) -> bool
  Equals(self: Ray3d,obj: object) -> bool
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: Ray3d) -> int """
  pass
 def PointAt(self,t):
  """ PointAt(self: Ray3d,t: float) -> Point3d """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,position,direction):
  """
  __new__[Ray3d]() -> Ray3d
  
  __new__(cls: type,position: Point3d,direction: Vector3d)
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
 Direction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Direction(self: Ray3d) -> Vector3d

"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Position(self: Ray3d) -> Point3d

"""


