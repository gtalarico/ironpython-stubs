class Vector3f(object,IEquatable[Vector3f],IComparable[Vector3f],IComparable,IEpsilonFComparable[Vector3f]):
 """
 Represents the three components of a vector in three-dimensional space,

    using System.Single-precision floating point numbers.

 

 Vector3f(x: Single,y: Single,z: Single)
 """
 @staticmethod
 def Add(point,vector):
  """
  Add(point: Point3f,vector: Vector3f) -> Point3f

  

   Sums up a point and a vector,and returns a new point.

     (Provided for languages that 

    do not support operator overloading. You can use the + operator otherwise)

  

  

   point: A point.

   vector: A vector.

   Returns: A new point that results from the addition of point and vector.
  """
  pass
 def CompareTo(self,other):
  """
  CompareTo(self: Vector3f,other: Vector3f) -> int

  

   Compares this Rhino.Geometry.Vector3f with another Rhino.Geometry.Vector3f.

     

    Component evaluation priority is first X,then Y,then Z.

  

  

   other: The other Rhino.Geometry.Vector3f to use in comparison.

   Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 

    other.Y-1: if this.X == other.X and this.Y == other.Y and this.Z < other.Z+1: otherwise.
  """
  pass
 @staticmethod
 def CrossProduct(a,b):
  """
  CrossProduct(a: Vector3f,b: Vector3f) -> Vector3f

  

   Computes the cross product (or vector product,or exterior product) of two vectors.

     

    This operation is not commutative.

  

  

   a: First vector.

   b: Second vector.

   Returns: A new vector that is perpendicular to both a and b,

     has Length == a.Length * 

    b.Length andwith a result that is oriented following the right hand rule.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Vector3f,other: Vector3f,epsilon: Single) -> bool

  

   Check that all values in other are withing epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Vector3f,vector: Vector3f) -> bool

  

   Determines whether the specified vector has the same values as the present vector.

  

   vector: The specified vector.

   Returns: true if vector has the same components as this; otherwise false.

  Equals(self: Vector3f,obj: object) -> bool

  

   Determines whether the specified System.Object is a Vector3f and has the same values as the 

    present vector.

  

  

   obj: The specified object.

   Returns: true if obj is Vector3f and has the same components as this; otherwise false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Vector3f) -> int

  

   Computes a hash number that represents the current vector.

   Returns: A hash code that is not unique for each vector.
  """
  pass
 @staticmethod
 def Multiply(*__args):
  """
  Multiply(t: Single,vector: Vector3f) -> Vector3f

  

   Multiplies a vector by a number,having the effect of scaling it.

     (Provided for 

    languages that do not support operator overloading. You can use the * operator otherwise)

  

  

   t: A number.

   vector: A vector.

   Returns: A new vector that is the original vector coordinatewise multiplied by t.

  Multiply(vector: Vector3f,t: Single) -> Vector3f

  

   Multiplies a vector by a number,having the effect of scaling it.

     (Provided for 

    languages that do not support operator overloading. You can use the * operator otherwise)

  

  

   vector: A vector.

   t: A number.

   Returns: A new vector that is the original vector coordinatewise multiplied by t.
  """
  pass
 def PerpendicularTo(self,other):
  """
  PerpendicularTo(self: Vector3f,other: Vector3f) -> bool

  

   Sets this vector to be perpendicular to another vector. 

      Result is not unitized.

  

   other: Vector to use as guide.

   Returns: true on success,false if input vector is zero or invalid.
  """
  pass
 def Reverse(self):
  """
  Reverse(self: Vector3f) -> bool

  

   Reverses (inverts) this vector in place.

      If this vector contains 

    RhinoMath.UnsetValue,the 

      reverse will also be invalid and false will be 

    returned.

  

   Returns: true on success or false if the vector is invalid.
  """
  pass
 def Rotate(self,angleRadians,rotationAxis):
  """
  Rotate(self: Vector3f,angleRadians: float,rotationAxis: Vector3f) -> bool

  

   Rotates this vector around a given axis.

  

   angleRadians: Angle of rotation (in radians).

   rotationAxis: Axis of rotation.

   Returns: true on success,false on failure.
  """
  pass
 def ToString(self):
  """
  ToString(self: Vector3f) -> str

  

   Constructs the string representation of the current vector.

   Returns: The vector representation in the form X,Y,Z.
  """
  pass
 def Transform(self,transformation):
  """
  Transform(self: Vector3f,transformation: Transform)

   Transforms the vector in place.

     The transformation matrix acts on the left of the 

    vector; i.e.,result=transformation*vector

  

  

   transformation: Transformation matrix to apply.
  """
  pass
 def Unitize(self):
  """
  Unitize(self: Vector3f) -> bool

  

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
 def __mul__(self,*args):
  """ x.__mul__(y) <==> x*y """
  pass
 @staticmethod
 def __new__(self,x,y,z):
  """
  __new__[Vector3f]() -> Vector3f

  

  __new__(cls: type,x: Single,y: Single,z: Single)
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """
  __radd__(point: Point3f,vector: Vector3f) -> Point3f

  

   Sums up a point and a vector,and returns a new point.

  

   point: A point.

   vector: A vector.

   Returns: A new point that results from the addition of point and vector.
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rmul__(self,*args):
  """
  __rmul__(t: Single,vector: Vector3f) -> Vector3f

  

   Multiplies a vector by a number,having the effect of scaling it.

  

   t: A number.

   vector: A vector.

   Returns: A new vector that is the original vector coordinatewise multiplied by t.
  """
  pass
 def __str__(self,*args):
  pass
 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Computes the length (or magnitude,or size) of this vector.

   This is an application of Pythagoras' theorem.

   If this vector is invalid,its length is considered 0.



Get: Length(self: Vector3f) -> Single



"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X (first) component of this vector.



Get: X(self: Vector3f) -> Single



Set: X(self: Vector3f)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y (second) component of this vector.



Get: Y(self: Vector3f) -> Single



Set: Y(self: Vector3f)=value

"""

 Z=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Z (third) component of this vector.



Get: Z(self: Vector3f) -> Single



Set: Z(self: Vector3f)=value

"""


 Unset=None
 XAxis=None
 YAxis=None
 ZAxis=None
 Zero=None

