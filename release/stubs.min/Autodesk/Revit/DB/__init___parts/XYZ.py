class XYZ(object):
 """
 Object representing coordinates in 3-dimensional space.
 
 XYZ(x: float,y: float,z: float)
 XYZ()
 """
 def Add(self,source):
  """
  Add(self: XYZ,source: XYZ) -> XYZ
  
   Adds the specified vector to this vector and returns the result.
  
   source: The vector to add to this vector.
   Returns: The vector equal to the sum of the two vectors.
  """
  pass
 def AngleOnPlaneTo(self,right,normal):
  """
  AngleOnPlaneTo(self: XYZ,right: XYZ,normal: XYZ) -> float
  
   Returns the angle between this vector and the specified vector projected to the 
    specified plane.
  
  
   right: The specified vector.
   normal: The normal vector that defines the plane.
   Returns: The real number between 0 and 2*PI equal to the projected angle between the two 
    vectors.
  """
  pass
 def AngleTo(self,source):
  """
  AngleTo(self: XYZ,source: XYZ) -> float
  
   Returns the angle between this vector and the specified vector.
  
   source: The specified vector.
   Returns: The real number between 0 and PI equal to the angle between the two vectors in 
    radians..
  """
  pass
 def CrossProduct(self,source):
  """
  CrossProduct(self: XYZ,source: XYZ) -> XYZ
  
   The cross product of this vector and the specified vector.
  
   source: The vector to multiply with this vector.
   Returns: The vector equal to the cross product.
  """
  pass
 def DistanceTo(self,source):
  """
  DistanceTo(self: XYZ,source: XYZ) -> float
  
   Returns the distance from this point to the specified point.
  
   source: The specified point.
   Returns: The real number equal to the distance between the two points.
  """
  pass
 def Divide(self,value):
  """
  Divide(self: XYZ,value: float) -> XYZ
  
   Divides this vector by the specified value and returns the result.
  
   value: The value to divide this vector by.
   Returns: The divided vector.
  """
  pass
 def DotProduct(self,source):
  """
  DotProduct(self: XYZ,source: XYZ) -> float
  
   The dot product of this vector and the specified vector.
  
   source: The vector to multiply with this vector.
   Returns: The real number equal to the dot product.
  """
  pass
 def GetLength(self):
  """
  GetLength(self: XYZ) -> float
  
   Gets the length of this vector.
  """
  pass
 def IsAlmostEqualTo(self,source,tolerance=None):
  """
  IsAlmostEqualTo(self: XYZ,source: XYZ) -> bool
  
   Determines whether this vector and the specified vector are the same within the 
    tolerance (1.0e-09).
  
  
   source: The vector to compare with this vector.
   Returns: True if the vectors are the same; otherwise,false.
  IsAlmostEqualTo(self: XYZ,source: XYZ,tolerance: float) -> bool
  
   Determines whether 2 vectors are the same within the given tolerance.
  
   source: The vector to compare with this vector.
   tolerance: The tolerance for equality check.
   Returns: True if the vectors are the same; otherwise,false.
  """
  pass
 def IsUnitLength(self):
  """
  IsUnitLength(self: XYZ) -> bool
  
   The boolean value that indicates whether this vector is of unit length.
  """
  pass
 @staticmethod
 def IsWithinLengthLimits(point):
  """
  IsWithinLengthLimits(point: XYZ) -> bool
  
   Validates that the input point is within Revit design limits.
  
   point: The point to test.
   Returns: True if the input point is within Revit design limits,false otherwise.
  """
  pass
 def IsZeroLength(self):
  """
  IsZeroLength(self: XYZ) -> bool
  
   The boolean value that indicates whether this vector is a zero vector.
  """
  pass
 def Multiply(self,value):
  """
  Multiply(self: XYZ,value: float) -> XYZ
  
   Multiplies this vector by the specified value and returns the result.
  
   value: The value to multiply with this vector.
   Returns: The multiplied vector.
  """
  pass
 def Negate(self):
  """
  Negate(self: XYZ) -> XYZ
  
   Negates this vector.
   Returns: The vector opposite to this vector.
  """
  pass
 def Normalize(self):
  """
  Normalize(self: XYZ) -> XYZ
  
   Returns a new XYZ whose coordinates are the normalized values from this vector.
   Returns: The normalized XYZ or zero if the vector is almost Zero.
  """
  pass
 def Subtract(self,source):
  """
  Subtract(self: XYZ,source: XYZ) -> XYZ
  
   Subtracts the specified vector from this vector and returns the result.
  
   source: The vector to subtract from this vector.
   Returns: The vector equal to the difference between the two vectors.
  """
  pass
 def ToString(self):
  """
  ToString(self: XYZ) -> str
  
   Gets formatted string showing (X,Y,Z) with values formatted to 9 decimal 
    places.
  """
  pass
 def TripleProduct(self,middle,right):
  """
  TripleProduct(self: XYZ,middle: XYZ,right: XYZ) -> float
  
   The triple product of this vector and the two specified vectors.
  
   middle: The second vector.
   right: The third vector.
   Returns: The real number equal to the triple product.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __div__(self,*args):
  """ x.__div__(y) <==> x/y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __mul__(self,*args):
  """ x.__mul__(y) <==> x*y """
  pass
 def __neg__(self,*args):
  """ x.__neg__() <==> -x """
  pass
 @staticmethod
 def __new__(self,x=None,y=None,z=None):
  """
  __new__(cls: type,x: float,y: float,z: float)
  __new__(cls: type)
  """
  pass
 def __radd__(self,*args):
  """
  __radd__(left: XYZ,right: XYZ) -> XYZ
  
   Adds the two specified vectors and returns the result.
  
   left: The first vector.
   right: The second vector.
   Returns: The vector equal to the sum of the two source vectors.
  """
  pass
 def __rmul__(self,*args):
  """
  __rmul__(value: float,right: XYZ) -> XYZ
  
   Multiplies the specified number and the specified vector.
  
   value: The value to multiply with the specified vector.
   right: The vector to multiply with the value.
   Returns: The multiplied vector.
  """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(left: XYZ,right: XYZ) -> XYZ
  
   Subtracts the two specified vectors and returns the result.
  
   left: The first vector.
   right: The second vector.
   Returns: The vector equal to the difference between the two source vectors.
  """
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the first coordinate.

Get: X(self: XYZ) -> float

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the second coordinate.

Get: Y(self: XYZ) -> float

"""

 Z=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the third coordinate.

Get: Z(self: XYZ) -> float

"""


 BasisX=None
 BasisY=None
 BasisZ=None
 Zero=None

