class Vector3d(object,ISerializable,IEquatable[Vector3d],IComparable[Vector3d],IComparable,IEpsilonComparable[Vector3d]):
 """
 Represents the three components of a vector in three-dimensional space,

    using System.Double-precision floating point numbers.

 

 Vector3d(x: float,y: float,z: float)

 Vector3d(point: Point3d)

 Vector3d(vector: Vector3f)

 Vector3d(vector: Vector3d)
 """
 @staticmethod
 def Add(vector1,vector2):
  """
  Add(vector1: Vector3d,vector2: Vector3d) -> Vector3d

  

   Sums up two vectors.

     (Provided for languages that do not support operator 

    overloading. You can use the + operator otherwise)

  

  

   vector1: A vector.

   vector2: A second vector.

   Returns: A new vector that results from the componentwise addition of the two vectors.
  """
  pass
 def CompareTo(self,other):
  """
  CompareTo(self: Vector3d,other: Vector3d) -> int

  

   Compares this Rhino.Geometry.Vector3d with another Rhino.Geometry.Vector3d.

     

    Component evaluation priority is first X,then Y,then Z.

  

  

   other: The other Rhino.Geometry.Vector3d to use in comparison.

   Returns: 0: if this is identical to other-1: if this.X < other.X-1: if this.X == other.X and this.Y < 

    other.Y-1: if this.X == other.X and this.Y == other.Y and this.Z < other.Z+1: otherwise.
  """
  pass
 @staticmethod
 def CrossProduct(a,b):
  """
  CrossProduct(a: Vector3d,b: Vector3d) -> Vector3d

  

   Computes the cross product (or vector product,or exterior product) of two vectors.

     

    This operation is not commutative.

  

  

   a: First vector.

   b: Second vector.

   Returns: A new vector that is perpendicular to both a and b,

     has Length == a.Length * 

    b.Length andwith a result that is oriented following the right hand rule.
  """
  pass
 @staticmethod
 def Divide(vector,t):
  """
  Divide(vector: Vector3d,t: float) -> Vector3d

  

   Divides a Rhino.Geometry.Vector3d by a number,having the effect of shrinking it.

     

    (Provided for languages that do not support operator overloading. You can use the / operator 

    otherwise)

  

  

   vector: A vector.

   t: A number.

   Returns: A new vector that is componentwise divided by t.
  """
  pass
 def EpsilonEquals(self,other,epsilon):
  """
  EpsilonEquals(self: Vector3d,other: Vector3d,epsilon: float) -> bool

  

   Check that all values in other are within epsilon of the values in this
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: Vector3d,vector: Vector3d) -> bool

  

   Determines whether the specified vector has the same value as the present vector.

  

   vector: The specified vector.

   Returns: true if vector has the same coordinates as this; otherwise false.

  Equals(self: Vector3d,obj: object) -> bool

  

   Determines whether the specified System.Object is a Vector3d and has the same values as the 

    present vector.

  

  

   obj: The specified object.

   Returns: true if obj is a Vector3d and has the same coordinates as this; otherwise false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Vector3d) -> int

  

   Computes the hash code for the current vector.

   Returns: A non-unique number that represents the components of this vector.
  """
  pass
 def IsParallelTo(self,other,angleTolerance=None):
  """
  IsParallelTo(self: Vector3d,other: Vector3d,angleTolerance: float) -> int

  

   Determines whether this vector is parallel to another vector,within a provided tolerance.

  

   other: Vector to use for comparison.

   angleTolerance: Angle tolerance (in radians).

   Returns: Parallel indicator:

     +1=both vectors are parallel.0=vectors are not parallel or 

    at least one of the vectors is zero.-1=vectors are anti-parallel.

  

  IsParallelTo(self: Vector3d,other: Vector3d) -> int

  

   Determines whether this vector is parallel to another vector,within one degree (within Pi / 

    180).

  

  

   other: Vector to use for comparison.

   Returns: Parallel indicator:

     +1=both vectors are parallel 0=vectors are not parallel,or 

    at least one of the vectors is zero-1=vectors are anti-parallel.
  """
  pass
 def IsPerpendicularTo(self,other,angleTolerance=None):
  """
  IsPerpendicularTo(self: Vector3d,other: Vector3d,angleTolerance: float) -> bool

  

   Determines whether this vector is perpendicular to another vector,within a provided angle 

    tolerance.

  

  

   other: Vector to use for comparison.

   angleTolerance: Angle tolerance (in radians).

   Returns: true if vectors form Pi-radians (90-degree) angles with each other; otherwise false.

  IsPerpendicularTo(self: Vector3d,other: Vector3d) -> bool

  

   Test to see whether this vector is perpendicular to within one degree of another one.

  

   other: Vector to compare to.

   Returns: true if both vectors are perpendicular,false if otherwise.
  """
  pass
 def IsTiny(self,tolerance=None):
  """
  IsTiny(self: Vector3d) -> bool

  

   Uses RhinoMath.ZeroTolerance for IsTiny calculation.

   Returns: true if vector is very small,otherwise false.

  IsTiny(self: Vector3d,tolerance: float) -> bool

  

   Determines whether a vector is very short.

  

   tolerance: A nonzero value used as the coordinate zero tolerance.

     .

   Returns: (Math.Abs(X) <= tiny_tol) AND (Math.Abs(Y) <= tiny_tol) AND (Math.Abs(Z) <= tiny_tol).
  """
  pass
 @staticmethod
 def Multiply(*__args):
  """
  Multiply(vector1: Vector3d,vector2: Vector3d) -> float

  

   Multiplies two vectors together,returning the dot product (or inner product).

     This 

    differs from the cross product.

     (Provided for languages that do not support 

    operator overloading. You can use the * operator otherwise)

  

  

   vector1: A vector.

   vector2: A second vector.

   Returns: A value that results from the evaluation of v1.X*v2.X + v1.Y*v2.Y + v1.Z*v2.Z.

     This 

    value equals v1.Length * v2.Length * cos(alpha),where alpha is the angle between vectors.

  

  Multiply(t: float,vector: Vector3d) -> Vector3d

  

   Multiplies a vector by a number,having the effect of scaling it.

     (Provided for 

    languages that do not support operator overloading. You can use the * operator otherwise)

  

  

   t: A number.

   vector: A vector.

   Returns: A new vector that is the original vector coordinatewise multiplied by t.

  Multiply(vector: Vector3d,t: float) -> Vector3d

  

   Multiplies a vector by a number,having the effect of scaling it.

     (Provided for 

    languages that do not support operator overloading. You can use the * operator otherwise)

  

  

   vector: A vector.

   t: A number.

   Returns: A new vector that is the original vector coordinatewise multiplied by t.
  """
  pass
 @staticmethod
 def Negate(vector):
  """
  Negate(vector: Vector3d) -> Vector3d

  

   Computes the opposite vector.

     (Provided for languages that do not support operator 

    overloading. You can use the - unary operator otherwise)

  

  

   vector: A vector to negate.

   Returns: A new vector where all components were multiplied by -1.
  """
  pass
 def PerpendicularTo(self,other):
  """
  PerpendicularTo(self: Vector3d,other: Vector3d) -> bool

  

   Sets this vector to be perpendicular to another vector. 

      Result is not unitized.

  

   other: Vector to use as guide.

   Returns: true on success,false if input vector is zero or invalid.
  """
  pass
 def Reverse(self):
  """
  Reverse(self: Vector3d) -> bool

  

   Reverses (inverts) this vector in place.

      If this vector is Invalid,no changes 

    will occur and false will be returned.

  

   Returns: true on success or false if the vector is invalid.
  """
  pass
 def Rotate(self,angleRadians,rotationAxis):
  """
  Rotate(self: Vector3d,angleRadians: float,rotationAxis: Vector3d) -> bool

  

   Rotates this vector around a given axis.

  

   angleRadians: Angle of rotation (in radians).

   rotationAxis: Axis of rotation.

   Returns: true on success,false on failure.
  """
  pass
 @staticmethod
 def Subtract(vector1,vector2):
  """
  Subtract(vector1: Vector3d,vector2: Vector3d) -> Vector3d

  

   Subtracts the second vector from the first one.

     (Provided for languages that do not 

    support operator overloading. You can use the - operator otherwise)

  

  

   vector1: A vector.

   vector2: A second vector.

   Returns: A new vector that results from the componentwise difference of vector1 - vector2.
  """
  pass
 def ToString(self):
  """
  ToString(self: Vector3d) -> str

  

   Returns the string representation of the current vector,in the form X,Y,Z.

   Returns: A string with the current location of the point.
  """
  pass
 def Transform(self,transformation):
  """
  Transform(self: Vector3d,transformation: Transform)

   Transforms the vector in place.

     The transformation matrix acts on the left of the 

    vector; i.e.,result=transformation*vector

  

  

   transformation: Transformation matrix to apply.
  """
  pass
 def Unitize(self):
  """
  Unitize(self: Vector3d) -> bool

  

   Unitizes the vector in place. A unit vector has length 1 unit. 

     An invalid or zero 

    length vector cannot be unitized.

  

   Returns: true on success or false on failure.
  """
  pass
 @staticmethod
 def VectorAngle(a,b,plane=None):
  """
  VectorAngle(a: Vector3d,b: Vector3d,plane: Plane) -> float

  

   Computes the angle on a plane between two vectors.

  

   a: First vector.

   b: Second vector.

   plane: Two-dimensional plane on which to perform the angle measurement.

   Returns: On success,the angle (in radians) between a and b as projected onto the plane; 

    RhinoMath.UnsetValue on failure.

  

  VectorAngle(a: Vector3d,b: Vector3d) -> float

  

   Compute the angle between two vectors.

     This operation is commutative.

  

   a: First vector for angle.

   b: Second vector for angle.

   Returns: If the input is valid,the angle (in radians) between a and b; RhinoMath.UnsetValue otherwise.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
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
  """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
  pass
 def __neg__(self,*args):
  """ x.__neg__() <==> -x """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Vector3d]() -> Vector3d

  

  __new__(cls: type,x: float,y: float,z: float)

  __new__(cls: type,point: Point3d)

  __new__(cls: type,vector: Vector3f)

  __new__(cls: type,vector: Vector3d)
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """
  __radd__(vector1: Vector3d,vector2: Vector3d) -> Vector3d

  

   Sums up two vectors.

  

   vector1: A vector.

   vector2: A second vector.

   Returns: A new vector that results from the componentwise addition of the two vectors.
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rmul__(self,*args):
  """
  __rmul__(vector1: Vector3d,vector2: Vector3d) -> float

  

   Multiplies two vectors together,returning the dot product (or inner product).

     This 

    differs from the cross product.

  

  

   vector1: A vector.

   vector2: A second vector.

   Returns: A value that results from the evaluation of v1.X*v2.X + v1.Y*v2.Y + v1.Z*v2.Z.

     This 

    value equals v1.Length * v2.Length * cos(alpha),where alpha is the angle between vectors.

  

  __rmul__(t: float,vector: Vector3d) -> Vector3d

  

   Multiplies a vector by a number,having the effect of scaling it.

  

   t: A number.

   vector: A vector.

   Returns: A new vector that is the original vector coordinatewise multiplied by t.
  """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(vector1: Vector3d,vector2: Vector3d) -> Vector3d

  

   Subtracts the second vector from the first one.

  

   vector1: A vector.

   vector2: A second vector.

   Returns: A new vector that results from the componentwise difference of vector1 - vector2.
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 IsUnitVector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not this is a unit vector. 

   A unit vector has length 1.



Get: IsUnitVector(self: Vector3d) -> bool



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this vector is valid. 

   A valid vector must be formed of valid component values for x,y and z.



Get: IsValid(self: Vector3d) -> bool



"""

 IsZero=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the X,Y,and Z values are all equal to 0.0.



Get: IsZero(self: Vector3d) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Computes the length (or magnitude,or size) of this vector.

   This is an application of Pythagoras' theorem.

   If this vector is invalid,its length is considered 0.



Get: Length(self: Vector3d) -> float



"""

 MaximumCoordinate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the largest (both positive and negative) component value in this vector.



Get: MaximumCoordinate(self: Vector3d) -> float



"""

 MinimumCoordinate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the smallest (both positive and negative) component value in this vector.



Get: MinimumCoordinate(self: Vector3d) -> float



"""

 SquareLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Computes the squared length (or magnitude,or size) of this vector.

   This is an application of Pythagoras' theorem.

   While the Length property checks for input validity,

   this property does not. You should check validity in advance,

   if this vector can be invalid.



Get: SquareLength(self: Vector3d) -> float



"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X (first) component of the vector.



Get: X(self: Vector3d) -> float



Set: X(self: Vector3d)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y (second) component of the vector.



Get: Y(self: Vector3d) -> float



Set: Y(self: Vector3d)=value

"""

 Z=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Z (third) component of the vector.



Get: Z(self: Vector3d) -> float



Set: Z(self: Vector3d)=value

"""


 Unset=None
 XAxis=None
 YAxis=None
 ZAxis=None
 Zero=None

