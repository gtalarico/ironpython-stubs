class Point3d(object,ISerializable,IEquatable[Point3d],IComparable[Point3d],IComparable,IEpsilonComparable[Point3d]):
 """
 Represents the three coordinates of a point in three-dimensional space,

    using System.Double-precision floating point values.

 

 Point3d(x: float,y: float,z: float)

 Point3d(vector: Vector3d)

 Point3d(point: Point3f)

 Point3d(point: Point3d)

 Point3d(point: Point4d)
 """
 @staticmethod
 def Add(*__args):
  """
  Add(point: Point3d,vector: Vector3f) -> Point3d

  

   Sums up a point and a vector,and returns a new point.

     (Provided for languages that 

    do not support operator overloading. You can use the + operator otherwise)

  

  

   point: A point.

   vector: A vector.

   Returns: A new point that results from the addition of point and vector.

  Add(vector: Vector3d,point: Point3d) -> Point3d

  

   Sums up a point and a vector,and returns a new point.

     (Provided for languages that 

    do not support operator overloading. You can use the + operator otherwise)

  

  

   vector: A vector.

   point: A point.

   Returns: A new point that results from the addition of point and vector.

  Add(point1: Point3d,point2: Point3d) -> Point3d

  

   Sums two Rhino.Geometry.Point3d instances.

     (Provided for languages that do not 

    support operator overloading. You can use the + operator otherwise)

  

  

   point1: A point.

   point2: A point.

   Returns: A new point that results from the addition of point1 and point2.

  Add(point: Point3d,vector: Vector3d) -> Point3d

  

   Sums up a point and a vector,and returns a new point.

     (Provided for languages that 

    do not support operator overloading. You can use the + operator otherwise)

  

  

   point: A point.

   vector: A vector.

   Returns: A new point that results from the addition of point and vector.
  """
  pass
 @staticmethod
 def ArePointsCoplanar(points,tolerance):
  """ ArePointsCoplanar(points: IEnumerable[Point3d],tolerance: float) -> bool """
  pass
 def CompareTo(self,other):
  """
  CompareTo(self: Point3d,other: Point3d) -> int

  

   Compares this Rhino.Geometry.Point3d with another Rhino.Geometry.Point3d.

     Component 

    evaluation priority is first X,then Y,then Z.

  

  

   other: The other Rhino.Geometry.Point3d to use in comparison.

   Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 

    other.Y-1: if this.X == other.X and this.Y == other.Y and this.Z < other.Z+1: otherwise.
  """
  pass
 @staticmethod
 def CullDuplicates(points,tolerance):
  """ CullDuplicates(points: IEnumerable[Point3d],tolerance: float) -> Array[Point3d] """
  pass
 def DistanceTo(self,other):
  """
  DistanceTo(self: Point3d,other: Point3d) -> float

  

   Computes the distance between two points.

  

   other: Other point for distance measurement.

   Returns: The length of the line between this and the other point; or 0 if any of the points is not valid.
  """
  pass
 @staticmethod
 def Divide(point,t):
  """
  Divide(point: Point3d,t: float) -> Point3d

  

   Divides a Rhino.Geometry.Point3d by a number.

     (Provided for languages that do not 

    support operator overloading. You can use the / operator otherwise)

  

  

   point: A point.

   t: A number.

   Returns: A new point that is coordinatewise divided by t.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Point3d,other: Point3d,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Point3d,point: Point3d) -> bool

  

   Determines whether the specified Rhino.Geometry.Point3d has the same values as the present point.

  

   point: The specified point.

   Returns: true if point has the same coordinates as this; otherwise false.

  Equals(self: Point3d,obj: object) -> bool

  

   Determines whether the specified System.Object is a Rhino.Geometry.Point3d and has the same 

    values as the present point.

  

  

   obj: The specified object.

   Returns: true if obj is a Point3d and has the same coordinates as this; otherwise false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Point3d) -> int

  

   Computes a hash code for the present point.

   Returns: A non-unique integer that represents this point.
  """
  pass
 def Interpolate(self,pA,pB,t):
  """
  Interpolate(self: Point3d,pA: Point3d,pB: Point3d,t: float)

   Interpolate between two points.

  

   pA: First point.

   pB: Second point.

   t: Interpolation parameter. 

     If t=0 then this point is set to pA. 

     If t=1 

    then this point is set to pB. 

     Values of t in between 0.0 and 1.0 result in points 

    between pA and pB.
  """
  pass
 @staticmethod
 def Multiply(*__args):
  """
  Multiply(t: float,point: Point3d) -> Point3d

  

   Multiplies a Rhino.Geometry.Point3d by a number.

     (Provided for languages that do 

    not support operator overloading. You can use the * operator otherwise)

  

  

   t: A number.

   point: A point.

   Returns: A new point that is coordinatewise multiplied by t.

  Multiply(point: Point3d,t: float) -> Point3d

  

   Multiplies a Rhino.Geometry.Point3d by a number.

     (Provided for languages that do 

    not support operator overloading. You can use the * operator otherwise)

  

  

   point: A point.

   t: A number.

   Returns: A new point that is coordinatewise multiplied by t.
  """
  pass
 @staticmethod
 def SortAndCullPointList(points,minimumDistance):
  """ SortAndCullPointList(points: IEnumerable[Point3d],minimumDistance: float) -> Array[Point3d] """
  pass
 @staticmethod
 def Subtract(*__args):
  """
  Subtract(point1: Point3d,point2: Point3d) -> Vector3d

  

   Subtracts a point from another point.

     (Provided for languages that do not support 

    operator overloading. You can use the - operator otherwise)

  

  

   point1: A point.

   point2: Another point.

   Returns: A new vector that is the difference of point minus vector.

  Subtract(point: Point3d,vector: Vector3d) -> Point3d

  

   Subtracts a vector from a point.

     (Provided for languages that do not support 

    operator overloading. You can use the - operator otherwise)

  

  

   point: A point.

   vector: A vector.

   Returns: A new point that is the difference of point minus vector.
  """
  pass
 def ToString(self):
  """
  ToString(self: Point3d) -> str

  

   Constructs the string representation for the current point.

   Returns: The point representation in the form X,Y,Z.
  """
  pass
 def Transform(self,xform):
  """
  Transform(self: Point3d,xform: Transform)

   Transforms the present point in place. The transformation matrix acts on the left of the point. 

    i.e.,

     result=transformation*point

  

  

   xform: Transformation to apply.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
 def __neg__(self,*args):
  """ x.__neg__() <==> -x """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Point3d]() -> Point3d

  

  __new__(cls: type,x: float,y: float,z: float)

  __new__(cls: type,vector: Vector3d)

  __new__(cls: type,point: Point3f)

  __new__(cls: type,point: Point3d)

  __new__(cls: type,point: Point4d)
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """
  __radd__(vector: Vector3d,point: Point3d) -> Point3d

  

   Sums up a point and a vector,and returns a new point.

  

   vector: A vector.

   point: A point.

   Returns: A new point that results from the addition of point and vector.

  __radd__(point1: Point3d,point2: Point3d) -> Point3d

  

   Sums two Rhino.Geometry.Point3d instances.

  

   point1: A point.

   point2: A point.

   Returns: A new point that results from the addition of point1 and point2.
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rmul__(self,*args):
  """
  __rmul__(t: float,point: Point3d) -> Point3d

  

   Multiplies a Rhino.Geometry.Point3d by a number.

  

   t: A number.

   point: A point.

   Returns: A new point that is coordinatewise multiplied by t.
  """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(point1: Point3d,point2: Point3d) -> Vector3d

  

   Subtracts a point from another point.

  

   point1: A point.

   point2: Another point.

   Returns: A new vector that is the difference of point minus vector.
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
 """Each coordinate of the point must pass the Rhino.RhinoMath.IsValidDouble(System.Double) test.



Get: IsValid(self: Point3d) -> bool



"""

 MaximumCoordinate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the largest (both positive and negative) valid coordinate in this point,

   or RhinoMath.UnsetValue if no coordinate is valid.



Get: MaximumCoordinate(self: Point3d) -> float



"""

 MinimumCoordinate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the smallest (both positive and negative) coordinate value in this point.



Get: MinimumCoordinate(self: Point3d) -> float



"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X (first) coordinate of this point.



Get: X(self: Point3d) -> float



Set: X(self: Point3d)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y (second) coordinate of this point.



Get: Y(self: Point3d) -> float



Set: Y(self: Point3d)=value

"""

 Z=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Z (third) coordinate of this point.



Get: Z(self: Point3d) -> float



Set: Z(self: Point3d)=value

"""


 Origin=None
 Unset=None

