class Ray3d(object,ISerializable,IEquatable[Ray3d],IEpsilonComparable[Ray3d]):
 """
 Represents an immutable ray in three dimensions,using position and direction.

 

 Ray3d(position: Point3d,direction: Vector3d)
 """
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Ray3d,other: Ray3d,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Ray3d,ray: Ray3d) -> bool

  

   Determines whether the specified Ray3d has the same value as the present ray.

  

   ray: The specified ray.

   Returns: true if ray has the same position and direction as this; otherwise false.

  Equals(self: Ray3d,obj: object) -> bool

  

   Determines whether the specified System.Object is a Ray3d and has the same values as the present 

    ray.

  

  

   obj: The specified object.

   Returns: true if obj is a Ray3d and has the same position and direction as this; otherwise false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Ray3d) -> int

  

   Computes a hashing number that represents the current ray.

   Returns: A signed integer that represents both postion and direction,but is not unique.
  """
  pass
 def PointAt(self,t):
  """
  PointAt(self: Ray3d,t: float) -> Point3d

  

   Evaluates a point along the ray.

  

   t: The t parameter.

   Returns: A point at (Direction*t + Position).
  """
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
 """Gets the direction vector of this ray.



Get: Direction(self: Ray3d) -> Vector3d



"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the starting position of this ray.



Get: Position(self: Ray3d) -> Point3d



"""


