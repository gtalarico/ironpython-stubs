class Vector(object,IFormattable):
 """
 Represents a displacement in 2-D space.
 
 Vector(x: float,y: float)
 """
 @staticmethod
 def Add(*__args):
  """
  Add(vector: Vector,point: Point) -> Point
  
   Translates the specified point by the specified vector and returns the 
    resulting point.
  
  
   vector: The amount to translate the specified point.
   point: The point to translate.
   Returns: The result of translating point by vector.
  Add(vector1: Vector,vector2: Vector) -> Vector
  
   Adds two vectors and returns the result as a System.Windows.Vector structure.
  
   vector1: The first vector to add.
   vector2: The second vector to add.
   Returns: The sum of vector1 and vector2.
  """
  pass
 @staticmethod
 def AngleBetween(vector1,vector2):
  """
  AngleBetween(vector1: Vector,vector2: Vector) -> float
  
   Retrieves the angle,expressed in degrees,between the two specified vectors.
  
   vector1: The first vector to evaluate.
   vector2: The second vector to evaluate.
   Returns: The angle,in degrees,between vector1 and vector2.
  """
  pass
 @staticmethod
 def CrossProduct(vector1,vector2):
  """
  CrossProduct(vector1: Vector,vector2: Vector) -> float
  
   Calculates the cross product of two vectors.
  
   vector1: The first vector to evaluate.
   vector2: The second vector to evaluate.
   Returns: The cross product of vector1 and vector2. The following formula is used to 
    calculate the cross product: (Vector1.X * Vector2.Y) - (Vector1.Y * Vector2.X)
  """
  pass
 @staticmethod
 def Determinant(vector1,vector2):
  """
  Determinant(vector1: Vector,vector2: Vector) -> float
  
   Calculates the determinant of two vectors.
  
   vector1: The first vector to evaluate.
   vector2: The second vector to evaluate.
   Returns: The determinant of vector1 and vector2.
  """
  pass
 @staticmethod
 def Divide(vector,scalar):
  """
  Divide(vector: Vector,scalar: float) -> Vector
  
   Divides the specified vector by the specified scalar and returns the result as 
    a System.Windows.Vector.
  
  
   vector: The vector structure to divide.
   scalar: The amount by which vector is divided.
   Returns: The result of dividing vector by scalar.
  """
  pass
 @staticmethod
 def Equals(*__args):
  """
  Equals(self: Vector,value: Vector) -> bool
  
   Compares two vectors for equality.
  
   value: The vector to compare with this vector.
   Returns: true if value has the same System.Windows.Vector.X and System.Windows.Vector.Y 
    values as this vector; otherwise,false.
  
  Equals(self: Vector,o: object) -> bool
  
   Determines whether the specified System.Object is a System.Windows.Vector 
    structure and,if it is,whether it has the same System.Windows.Vector.X and 
    System.Windows.Vector.Y values as this vector.
  
  
   o: The vector to compare.
   Returns: true if o is a System.Windows.Vector and has the same System.Windows.Vector.X 
    and System.Windows.Vector.Y values as this vector; otherwise,false.
  
  Equals(vector1: Vector,vector2: Vector) -> bool
  
   Compares the two specified vectors for equality.
  
   vector1: The first vector to compare.
   vector2: The second vector to compare.
   Returns: true if t he System.Windows.Vector.X and System.Windows.Vector.Y components of 
    vector1 and vector2 are equal; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Vector) -> int
  
   Returns the hash code for this vector.
   Returns: The hash code for this instance.
  """
  pass
 @staticmethod
 def Multiply(*__args):
  """
  Multiply(vector: Vector,matrix: Matrix) -> Vector
  
   Transforms the coordinate space of the specified vector using the specified 
    System.Windows.Media.Matrix.
  
  
   vector: The vector structure to transform.
   matrix: The transformation to apply to vector.
   Returns: The result of transforming vector by matrix.
  Multiply(vector1: Vector,vector2: Vector) -> float
  
   Calculates the dot product of the two specified vectors and returns the result 
    as a System.Double.
  
  
   vector1: The first vector to multiply.
   vector2: The second vector structure to multiply.
   Returns: A System.Double containing the scalar dot product of vector1 and vector2,which 
    is calculated using the following formula: (vector1.X * vector2.X) + (vector1.Y 
    * vector2.Y)
  
  Multiply(vector: Vector,scalar: float) -> Vector
  
   Multiplies the specified vector by the specified scalar and returns the 
    resulting System.Windows.Vector.
  
  
   vector: The vector to multiply.
   scalar: The scalar to multiply.
   Returns: The result of multiplying vector and scalar.
  Multiply(scalar: float,vector: Vector) -> Vector
  
   Multiplies the specified scalar by the specified vector and returns the 
    resulting System.Windows.Vector.
  
  
   scalar: The scalar to multiply.
   vector: The vector to multiply.
   Returns: The result of multiplying scalar and vector.
  """
  pass
 def Negate(self):
  """
  Negate(self: Vector)
   Negates this vector. The vector has the same magnitude as before,but its 
    direction is now opposite.
  """
  pass
 def Normalize(self):
  """
  Normalize(self: Vector)
   Normalizes this vector.
  """
  pass
 @staticmethod
 def Parse(source):
  """
  Parse(source: str) -> Vector
  
   Converts a string representation of a vector into the equivalent 
    System.Windows.Vector structure.
  
  
   source: The string representation of the vector.
   Returns: The equivalent System.Windows.Vector structure.
  """
  pass
 @staticmethod
 def Subtract(vector1,vector2):
  """
  Subtract(vector1: Vector,vector2: Vector) -> Vector
  
   Subtracts the specified vector from another specified vector.
  
   vector1: The vector from which vector2 is subtracted.
   vector2: The vector to subtract from vector1.
   Returns: The difference between vector1 and vector2.
  """
  pass
 def ToString(self,provider=None):
  """
  ToString(self: Vector,provider: IFormatProvider) -> str
  
   Returns the string representation of this System.Windows.Vector structure with 
    the specified formatting information.
  
  
   provider: The culture-specific formatting information.
   Returns: A string that represents the System.Windows.Vector.X and 
    System.Windows.Vector.Y values of this System.Windows.Vector.
  
  ToString(self: Vector) -> str
  
   Returns the string representation of this System.Windows.Vector structure.
   Returns: A string that represents the System.Windows.Vector.X and 
    System.Windows.Vector.Y values of this System.Windows.Vector.
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
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __mul__(self,*args):
  """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
  pass
 def __neg__(self,*args):
  """ x.__neg__() <==> -x """
  pass
 @staticmethod
 def __new__(self,x,y):
  """
  __new__(cls: type,x: float,y: float)
  __new__[Vector]() -> Vector
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """
  __radd__(vector1: Vector,vector2: Vector) -> Vector
  
   Adds two vectors and returns the result as a vector.
  
   vector1: The first vector to add.
   vector2: The second vector to add.
   Returns: The sum of vector1 and vector2.
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rmul__(self,*args):
  """
  __rmul__(vector1: Vector,vector2: Vector) -> float
  
   Calculates the dot product of the two specified vector structures and returns 
    the result as a System.Double.
  
  
   vector1: The first vector to multiply.
   vector2: The second vector to multiply.
   Returns: Returns a System.Double containing the scalar dot product of vector1 and 
    vector2,which is calculated using the following formula:vector1.X * vector2.X 
    + vector1.Y * vector2.Y
  
  __rmul__(scalar: float,vector: Vector) -> Vector
  
   Multiplies the specified scalar by the specified vector and returns the 
    resulting vector.
  
  
   scalar: The scalar to multiply.
   vector: The vector to multiply.
   Returns: The result of multiplying scalar and vector.
  """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(vector1: Vector,vector2: Vector) -> Vector
  
   Subtracts one specified vector from another.
  
   vector1: The vector from which vector2 is subtracted.
   vector2: The vector to subtract from vector1.
   Returns: The difference between vector1 and vector2.
  """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length of this vector.

Get: Length(self: Vector) -> float

"""

 LengthSquared=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the square of the length of this vector.

Get: LengthSquared(self: Vector) -> float

"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Vector.X component of this vector.

Get: X(self: Vector) -> float

Set: X(self: Vector)=value
"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Vector.Y component of this vector.

Get: Y(self: Vector) -> float

Set: Y(self: Vector)=value
"""


