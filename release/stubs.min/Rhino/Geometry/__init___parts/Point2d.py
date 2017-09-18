class Point2d(object,ISerializable,IEquatable[Point2d],IComparable[Point2d],IComparable,IEpsilonComparable[Point2d]):
 """
 Represents the two coordinates of a point in two-dimensional space,

    using System.Double-precision floating point numbers.

 

 Point2d(x: float,y: float)

 Point2d(vector: Vector2d)

 Point2d(point: Point2d)

 Point2d(point: Point3d)
 """
 @staticmethod
 def Add(*__args):
  """
  Add(point1: Point2d,point2: Point2d) -> Point2d

  

   Adds a point with a point.

     (Provided for languages that do not support operator 

    overloading. You can use the + operator otherwise)

  

  

   point1: A point.

   point2: A point.

   Returns: A new point that is coordinatewise summed with the other point.

  Add(vector: Vector2d,point: Point2d) -> Point2d

  

   Adds a vector with a point.

     (Provided for languages that do not support operator 

    overloading. You can use the + operator otherwise)

  

  

   vector: A vector.

   point: A point.

   Returns: A new point that is coordinatewise summed with the vector.

  Add(point: Point2d,vector: Vector2d) -> Point2d

  

   Adds a point with a vector.

     (Provided for languages that do not support operator 

    overloading. You can use the + operator otherwise)

  

  

   point: A point.

   vector: A vector.

   Returns: A new point that is coordinatewise summed with the vector.
  """
  pass
 def CompareTo(self,other):
  """
  CompareTo(self: Point2d,other: Point2d) -> int

  

   Compares this Rhino.Geometry.Point2d with another Rhino.Geometry.Point2d.

     

    Coordinates evaluation priority is first X,then Y.

  

  

   other: The other Rhino.Geometry.Point2d to use in comparison.

   Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 

    other.Y+1: otherwise.
  """
  pass
 def DistanceTo(self,other):
  """
  DistanceTo(self: Point2d,other: Point2d) -> float

  

   Computes the distance between two points.

  

   other: Another point.

   Returns: The length of the line between the two points,or 0 if either point is invalid.
  """
  pass
 @staticmethod
 def Divide(point,t):
  """
  Divide(point: Point2d,t: float) -> Point2d

  

   Divides a Rhino.Geometry.Point2d by a number.

     (Provided for languages that do not 

    support operator overloading. You can use the / operator otherwise)

  

  

   point: A point.

   t: A number.

   Returns: A new point that is coordinatewise divided by t.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Point2d,other: Point2d,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Point2d,point: Point2d) -> bool

  

   Determines whether the specified Point2d has the same values as the present point.

  

   point: The specified point.

   Returns: true if point has the same coordinates as this; otherwise false.

  Equals(self: Point2d,obj: object) -> bool

  

   Determines whether the specified System.Object is a Point2d and has the same values as the 

    present point.

  

  

   obj: The specified object.

   Returns: true if obj is a Point2d and has the same coordinates as this; otherwise false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Point2d) -> int

  

   Computes a hash number that represents the current point.

   Returns: A hash code that is not unique for each point.
  """
  pass
 @staticmethod
 def Multiply(*__args):
  """
  Multiply(t: float,point: Point2d) -> Point2d

  

   Multiplies a Rhino.Geometry.Point2d by a number.

     (Provided for languages that do 

    not support operator overloading. You can use the * operator otherwise)

  

  

   t: A number.

   point: A point.

   Returns: A new point that is coordinatewise multiplied by t.

  Multiply(point: Point2d,t: float) -> Point2d

  

   Multiplies a Rhino.Geometry.Point2d by a number.

     (Provided for languages that do 

    not support operator overloading. You can use the * operator otherwise)

  

  

   point: A point.

   t: A number.

   Returns: A new point that is coordinatewise multiplied by t.
  """
  pass
 @staticmethod
 def Subtract(*__args):
  """
  Subtract(point1: Point2d,point2: Point2d) -> Vector2d

  

   Subtracts the second point from the first point.

     (Provided for languages that do 

    not support operator overloading. You can use the - operator otherwise)

  

  

   point1: A point (minuend).

   point2: A point (subtrahend).

   Returns: A new vector that is point1 coordinatewise subtracted by point2.

  Subtract(point: Point2d,vector: Vector2d) -> Point2d

  

   Subtracts a vector from a point.

     (Provided for languages that do not support 

    operator overloading. You can use the - operator otherwise)

  

  

   point: A point.

   vector: A vector.

   Returns: A new point that is coordinatewise subtracted by vector.
  """
  pass
 def ToString(self):
  """
  ToString(self: Point2d) -> str

  

   Constructs the string representation for the current point.

   Returns: The point representation in the form X,Y.
  """
  pass
 def Transform(self,xform):
  """
  Transform(self: Point2d,xform: Transform)

   Transforms the present point in place. The transformation matrix acts on the left of the point. 

    i.e.,

     result=transformation*point

  

  

   xform: Transformation to apply.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
  """ x.__mul__(y) <==> x*y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Point2d]() -> Point2d

  

  __new__(cls: type,x: float,y: float)

  __new__(cls: type,vector: Vector2d)

  __new__(cls: type,point: Point2d)

  __new__(cls: type,point: Point3d)
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """
  __radd__(point1: Point2d,point2: Point2d) -> Point2d

  

   Adds a point with a point.

  

   point1: A point.

   point2: A point.

   Returns: A new point that is coordinatewise summed with the other point.

  __radd__(vector: Vector2d,point: Point2d) -> Point2d

  

   Adds a vector with a point.

  

   vector: A vector.

   point: A point.

   Returns: A new point that is coordinatewise summed with the vector.
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rmul__(self,*args):
  """
  __rmul__(t: float,point: Point2d) -> Point2d

  

   Multiplies a Rhino.Geometry.Point2d by a number.

  

   t: A number.

   point: A point.

   Returns: A new point that is coordinatewise multiplied by t.
  """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(point1: Point2d,point2: Point2d) -> Vector2d

  

   Subtracts point2 from point1.

  

   point1: A point (minuend).

   point2: A point (subtrahend).

   Returns: A new vector that is point1 coordinatewise subtracted by point2.
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
  pass
 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If any coordinate of a point is UnsetValue,then the point is not valid.



Get: IsValid(self: Point2d) -> bool



"""

 MaximumCoordinate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the largest valid coordinate,or RhinoMath.UnsetValue if no coordinate is valid.



Get: MaximumCoordinate(self: Point2d) -> float



"""

 MinimumCoordinate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the smallest (both positive and negative) valid coordinate,or RhinoMath.UnsetValue if no coordinate is valid.



Get: MinimumCoordinate(self: Point2d) -> float



"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X (first) coordinate of the point.



Get: X(self: Point2d) -> float



Set: X(self: Point2d)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y (second) coordinate of the point.



Get: Y(self: Point2d) -> float



Set: Y(self: Point2d)=value

"""


 Origin=None
 Unset=None

