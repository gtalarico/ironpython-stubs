class Vector2f(object,IEquatable[Vector2f],IComparable[Vector2f],IComparable,IEpsilonFComparable[Vector2f]):
 """
 Represents the two components of a vector in two-dimensional space,

    using System.Single-precision floating point numbers.
 """
 def CompareTo(self,other):
  """
  CompareTo(self: Vector2f,other: Vector2f) -> int

  

   Compares this Rhino.Geometry.Vector2f with another Rhino.Geometry.Vector2f.

     

    Components evaluation priority is first X,then Y.

  

  

   other: The other Rhino.Geometry.Vector2f to use in comparison.

   Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 

    other.Y+1: otherwise.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Vector2f,other: Vector2f,epsilon: Single) -> bool

  

   Check that all values in other are withing epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Vector2f,vector: Vector2f) -> bool

  

   Determines whether the specified vector has the same values as the present vector.

  

   vector: The specified vector.

   Returns: true if obj is Vector2f and has the same coordinates as this; otherwise false.

  Equals(self: Vector2f,obj: object) -> bool

  

   Determines whether the specified System.Object is a Vector2f and has the same values as the 

    present vector.

  

  

   obj: The specified object.

   Returns: true if obj is Vector2f and has the same coordinates as this; otherwise false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Vector2f) -> int

  

   Computes a hash number that represents the current vector.

   Returns: A hash code that is not unique for each vector.
  """
  pass
 def ToString(self):
  """
  ToString(self: Vector2f) -> str

  

   Constructs the string representation of the current vector.

   Returns: The vector representation in the form X,Y,Z.
  """
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
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X (first) component of this vector.



Get: X(self: Vector2f) -> Single



Set: X(self: Vector2f)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y (second) component of this vector.



Get: Y(self: Vector2f) -> Single



Set: Y(self: Vector2f)=value

"""


