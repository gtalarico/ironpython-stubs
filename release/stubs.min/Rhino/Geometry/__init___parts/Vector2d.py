class Vector2d(object,ISerializable,IEquatable[Vector2d],IComparable[Vector2d],IComparable,IEpsilonComparable[Vector2d]):
 """
 Represents the two components of a vector in two-dimensional space,

    using System.Double-precision floating point numbers.

 

 Vector2d(x: float,y: float)
 """
 def CompareTo(self,other):
  """
  CompareTo(self: Vector2d,other: Vector2d) -> int

  

   Compares this Rhino.Geometry.Vector2d with another Rhino.Geometry.Vector2d.

     

    Components evaluation priority is first X,then Y.

  

  

   other: The other Rhino.Geometry.Vector2d to use in comparison.

   Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 

    other.Y+1: otherwise.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Vector2d,other: Vector2d,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Vector2d,vector: Vector2d) -> bool

  

   Determines whether the specified vector has the same value as the present vector.

  

   vector: The specified vector.

   Returns: true if vector has the same components as this; otherwise false.

  Equals(self: Vector2d,obj: object) -> bool

  

   Determines whether the specified System.Object is a Vector2d and has the same value as the 

    present vector.

  

  

   obj: The specified object.

   Returns: true if obj is Vector2d and has the same components as this; otherwise false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Vector2d) -> int

  

   Provides a hashing value for the present vector.

   Returns: A non-unique number based on vector components.
  """
  pass
 def ToString(self):
  """
  ToString(self: Vector2d) -> str

  

   Constructs a string representation of the current vector.

   Returns: A string in the form X,Y.
  """
  pass
 def Unitize(self):
  """
  Unitize(self: Vector2d) -> bool

  

   Unitizes the vector in place. A unit vector has length 1 unit. 

     An invalid or zero 

    length vector cannot be unitized.

  

   Returns: true on success or false on failure.
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
 """Gets a value indicating whether this vector is valid. 

   A valid vector must be formed of valid component values for x,y and z.



Get: IsValid(self: Vector2d) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Computes the length (or magnitude,or size) of this vector.

   This is an application of Pythagoras' theorem.



Get: Length(self: Vector2d) -> float



"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X (first) component of this vector.



Get: X(self: Vector2d) -> float



Set: X(self: Vector2d)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y (second) component of this vector.



Get: Y(self: Vector2d) -> float



Set: Y(self: Vector2d)=value

"""


 Unset=None
 Zero=None

