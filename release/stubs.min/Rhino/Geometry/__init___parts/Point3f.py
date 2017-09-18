class Point3f(object,IEquatable[Point3f],IComparable[Point3f],IComparable,IEpsilonFComparable[Point3f]):
 """
 Represents the three coordinates of a point in three-dimensional space,

    using System.Single-precision floating point numbers.

 

 Point3f(x: Single,y: Single,z: Single)
 """
 def CompareTo(self,other):
  """
  CompareTo(self: Point3f,other: Point3f) -> int

  

   Compares this Rhino.Geometry.Point3f with another Rhino.Geometry.Point3f.

     Component 

    evaluation priority is first X,then Y,then Z.

  

  

   other: The other Rhino.Geometry.Point3d to use in comparison.

   Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 

    other.Y-1: if this.X == other.X and this.Y == other.Y and this.Z < other.Z+1: otherwise.
  """
  pass
 def DistanceTo(self,other):
  """
  DistanceTo(self: Point3f,other: Point3f) -> float

  

   Computes the distance between two points.

  

   other: Other point for distance measurement.

   Returns: The length of the line between this and the other point; or 0 if any of the points is not valid.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Point3f,other: Point3f,epsilon: Single) -> bool

  

   Check that all values in other are withing epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Point3f,point: Point3f) -> bool

  

   Determines whether the specified Point3f has the same values as the present point.

  

   point: The specified point.

   Returns: true if point has the same coordinates as this; otherwise false.

  Equals(self: Point3f,obj: object) -> bool

  

   Determines whether the specified System.Object is a Point3f and has the same values as the 

    present point.

  

  

   obj: The specified object.

   Returns: true if obj is Point3f and has the same coordinates as this; otherwise false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Point3f) -> int

  

   Computes a hash code for the present point.

   Returns: A non-unique integer that represents this point.
  """
  pass
 @staticmethod
 def Subtract(point1,point2):
  """
  Subtract(point1: Point3f,point2: Point3f) -> Vector3f

  

   Subtracts a point from another point.

     (Provided for languages that do not support 

    operator overloading. You can use the - operator otherwise)

  

  

   point1: A point.

   point2: Another point.

   Returns: A new vector that is the difference of point minus vector.
  """
  pass
 def ToString(self):
  """
  ToString(self: Point3f) -> str

  

   Constructs the string representation for the current point.

   Returns: The point representation in the form X,Y,Z.
  """
  pass
 def Transform(self,xform):
  """
  Transform(self: Point3f,xform: Transform)

   Transforms the present point in place. The transformation matrix acts on the left of the point. 

    i.e.,

     result=transformation*point

  

  

   xform: Transformation to apply.
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
 def __new__(self,x,y,z):
  """
  __new__[Point3f]() -> Point3f

  

  __new__(cls: type,x: Single,y: Single,z: Single)
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(point1: Point3f,point2: Point3f) -> Vector3f

  

   Subtracts a point from another point.

  

   point1: A point.

   point2: Another point.

   Returns: A new vector that is the difference of point minus vector.
  """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Each coordinate of the point must pass the Rhino.RhinoMath.IsValidSingle(System.Single) test.



Get: IsValid(self: Point3f) -> bool



"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X (first) component of the vector.



Get: X(self: Point3f) -> Single



Set: X(self: Point3f)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y (second) component of the vector.



Get: Y(self: Point3f) -> Single



Set: Y(self: Point3f)=value

"""

 Z=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Z (third) component of the vector.



Get: Z(self: Point3f) -> Single



Set: Z(self: Point3f)=value

"""


 Origin=None
 Unset=None

