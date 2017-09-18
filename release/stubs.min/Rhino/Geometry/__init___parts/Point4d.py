class Point4d(object,ISerializable,IEquatable[Point4d],IEpsilonComparable[Point4d]):
 """
 Represents the four coordinates of a point in four-dimensional space.

    The W (fourth) dimension is often considered the weight of the point as seen in 3D space.

 

 Point4d(x: float,y: float,z: float,w: float)

 Point4d(point: Point3d)
 """
 @staticmethod
 def Add(point1,point2):
  """
  Add(point1: Point4d,point2: Point4d) -> Point4d

  

   Sums two Rhino.Geometry.Point4d together.

     (Provided for languages that do not 

    support operator overloading. You can use the + operator otherwise)

  

  

   point1: First point.

   point2: Second point.

   Returns: A new point that results from the weighted addition of point1 and point2.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Point4d,other: Point4d,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Point4d,point: Point4d) -> bool

  

   Determines whether the specified point has same value as the present point.

  

   point: The specified point.

   Returns: true if point has the same value as this; otherwise false.

  Equals(self: Point4d,obj: object) -> bool

  

   Determines whether the specified System.Object is Point4d and has same coordinates as the 

    present point.

  

  

   obj: The specified object.

   Returns: true if obj is Point4d and has the same coordinates as this; otherwise false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Point4d) -> int

  

   Computes the hash code for the present point.

   Returns: A non-unique hash code,which uses all coordiantes of this object.
  """
  pass
 @staticmethod
 def Multiply(point,d):
  """
  Multiply(point: Point4d,d: float) -> Point4d

  

   Multiplies a point by a number.

     (Provided for languages that do not support 

    operator overloading. You can use the * operator otherwise)

  

  

   point: A point.

   d: A number.

   Returns: A new point that results from the coordinatewise multiplication of point with d.
  """
  pass
 @staticmethod
 def Subtract(point1,point2):
  """
  Subtract(point1: Point4d,point2: Point4d) -> Point4d

  

   Subtracts the second point from the first point.

     (Provided for languages that do 

    not support operator overloading. You can use the - operator otherwise)

  

  

   point1: First point.

   point2: Second point.

   Returns: A new point that results from the weighted subtraction of point2 from point1.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __mul__(self,*args):
  """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Point4d]() -> Point4d

  

  __new__(cls: type,x: float,y: float,z: float,w: float)

  __new__(cls: type,point: Point3d)
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """
  __radd__(point1: Point4d,point2: Point4d) -> Point4d

  

   Sums two Rhino.Geometry.Point4d together.

  

   point1: First point.

   point2: Second point.

   Returns: A new point that results from the weighted addition of point1 and point2.
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rmul__(self,*args):
  """
  __rmul__(point1: Point4d,point2: Point4d) -> float

  

   Multiplies two Rhino.Geometry.Point4d together,returning the dot (internal) product of the two.


    
     This is not the cross product.

  

  

   point1: The first point.

   point2: The second point.

   Returns: A value that results from the coordinatewise multiplication of point1 and point2.
  """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(point1: Point4d,point2: Point4d) -> Point4d

  

   Subtracts the second point from the first point.

  

   point1: First point.

   point2: Second point.

   Returns: A new point that results from the weighted subtraction of point2 from point1.
  """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 W=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the W (fourth) coordinate -or weight- of this point.



Get: W(self: Point4d) -> float



Set: W(self: Point4d)=value

"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X (first) coordinate of this point.



Get: X(self: Point4d) -> float



Set: X(self: Point4d)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y (second) coordinate of this point.



Get: Y(self: Point4d) -> float



Set: Y(self: Point4d)=value

"""

 Z=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Z (third) coordinate of this point.



Get: Z(self: Point4d) -> float



Set: Z(self: Point4d)=value

"""


 Unset=None

