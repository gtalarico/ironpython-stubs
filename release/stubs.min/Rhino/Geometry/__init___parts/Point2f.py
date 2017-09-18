class Point2f(object,IEquatable[Point2f],IComparable[Point2f],IComparable,IEpsilonFComparable[Point2f]):
 """
 Represents the two coordinates of a point in two-dimensional space,

    using System.Single-precision floating point numbers.

 

 Point2f(x: Single,y: Single)

 Point2f(x: float,y: float)
 """
 def CompareTo(self,other):
  """
  CompareTo(self: Point2f,other: Point2f) -> int

  

   Compares this Rhino.Geometry.Point2f with another Rhino.Geometry.Point2f.

     

    Coordinates evaluation priority is first X,then Y.

  

  

   other: The other Rhino.Geometry.Point2f to use in comparison.

   Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 

    other.Y+1: otherwise.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Point2f,other: Point2f,epsilon: Single) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Point2f,point: Point2f) -> bool

  

   Determines whether the specified Rhino.Geometry.Point2f has the same values as the present point.

  

   point: The specified point.

   Returns: true if point has the same coordinates as this; otherwise false.

  Equals(self: Point2f,obj: object) -> bool

  

   Determines whether the specified System.Object is a Rhino.Geometry.Point2f and has the same 

    values as the present point.

  

  

   obj: The specified object.

   Returns: true if obj is Point2f and has the same coordinates as this; otherwise false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Point2f) -> int

  

   Computes a hash number that represents the current point.

   Returns: A hash code that is not unique for each point.
  """
  pass
 def ToString(self):
  """
  ToString(self: Point2f) -> str

  

   Constructs the string representation for the current point.

   Returns: The point representation in the form X,Y.
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
 """Gets a value indicating whether this point is considered valid.



Get: IsValid(self: Point2f) -> bool



"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X (first) component of the vector.



Get: X(self: Point2f) -> Single



Set: X(self: Point2f)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y (second) component of the vector.



Get: Y(self: Point2f) -> Single



Set: Y(self: Point2f)=value

"""


 Unset=None

