class Point(object,IFormattable):
 """
 Represents an x- and y-coordinate pair in two-dimensional space.
 
 Point(x: float,y: float)
 """
 @staticmethod
 def Add(point,vector):
  """
  Add(point: Point,vector: Vector) -> Point
  
   Adds a System.Windows.Vector to a System.Windows.Point and returns the result 
    as a System.Windows.Point structure.
  
  
   point: The System.Windows.Point structure to add.
   vector: The System.Windows.Vector structure to add.
   Returns: Returns the sum of point and vector.
  """
  pass
 @staticmethod
 def Equals(*__args):
  """
  Equals(self: Point,value: Point) -> bool
  
   Compares two System.Windows.Point structures for equality.
  
   value: The point to compare to this instance.
   Returns: true if both System.Windows.Point structures contain the same 
    System.Windows.Point.X and System.Windows.Point.Y values; otherwise,false.
  
  Equals(self: Point,o: object) -> bool
  
   Determines whether the specified System.Object is a System.Windows.Point and 
    whether it contains the same coordinates as this System.Windows.Point.
  
  
   o: The System.Object to compare.
   Returns: true if o is a System.Windows.Point and contains the same 
    System.Windows.Point.X and System.Windows.Point.Y values as this 
    System.Windows.Point; otherwise,false.
  
  Equals(point1: Point,point2: Point) -> bool
  
   Compares two System.Windows.Point structures for equality.
  
   point1: The first point to compare.
   point2: The second point to compare.
   Returns: true if point1 and point2 contain the same System.Windows.Point.X and 
    System.Windows.Point.Y values; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Point) -> int
  
   Returns the hash code for this System.Windows.Point.
   Returns: The hash code for this System.Windows.Point structure.
  """
  pass
 @staticmethod
 def Multiply(point,matrix):
  """
  Multiply(point: Point,matrix: Matrix) -> Point
  
   Transforms the specified System.Windows.Point structure by the specified 
    System.Windows.Media.Matrix structure.
  
  
   point: The point to transform.
   matrix: The transformation matrix.
   Returns: The transformed point.
  """
  pass
 def Offset(self,offsetX,offsetY):
  """
  Offset(self: Point,offsetX: float,offsetY: float)
   Offsets a point's System.Windows.Point.X and System.Windows.Point.Y coordinates 
    by the specified amounts.
  
  
   offsetX: The amount to offset the point'sSystem.Windows.Point.X coordinate.
   offsetY: The amount to offset thepoint's System.Windows.Point.Y coordinate.
  """
  pass
 @staticmethod
 def Parse(source):
  """
  Parse(source: str) -> Point
  
   Constructs a System.Windows.Point from the specified System.String.
  
   source: A string representation of a point.
   Returns: The equivalent System.Windows.Point structure.
  """
  pass
 @staticmethod
 def Subtract(*__args):
  """
  Subtract(point1: Point,point2: Point) -> Vector
  
   Subtracts the specified System.Windows.Point from another specified 
    System.Windows.Point and returns the difference as a System.Windows.Vector.
  
  
   point1: The point from which point2 is subtracted.
   point2: The point to subtract from point1.
   Returns: The difference between point1 and point2.
  Subtract(point: Point,vector: Vector) -> Point
  
   Subtracts the specified System.Windows.Vector from the specified 
    System.Windows.Point and returns the resulting System.Windows.Point.
  
  
   point: The point from which vector is subtracted.
   vector: The vector to subtract from point.
   Returns: The difference between point and vector.
  """
  pass
 def ToString(self,provider=None):
  """
  ToString(self: Point,provider: IFormatProvider) -> str
  
   Creates a System.String representation of this System.Windows.Point.
  
   provider: Culture-specific formatting information.
   Returns: A System.String containing the System.Windows.Point.X and 
    System.Windows.Point.Y values of this System.Windows.Point structure.
  
  ToString(self: Point) -> str
  
   Creates a System.String representation of this System.Windows.Point.
   Returns: A System.String containing the System.Windows.Point.X and 
    System.Windows.Point.Y values of this System.Windows.Point structure.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
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
  """ x.__mul__(y) <==> x*y """
  pass
 @staticmethod
 def __new__(self,x,y):
  """
  __new__(cls: type,x: float,y: float)
  __new__[Point]() -> Point
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
  __rsub__(point1: Point,point2: Point) -> Vector
  
   Subtracts the specified System.Windows.Point from another specified 
    System.Windows.Point and returns the difference as a System.Windows.Vector.
  
  
   point1: The point from which point2 is subtracted.
   point2: The point to subtract from point1.
   Returns: The difference between point1 and point2.
  """
  pass
 def __str__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
  pass
 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Point.X-coordinate value of this System.Windows.Point structure.

Get: X(self: Point) -> float

Set: X(self: Point)=value
"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Point.Y-coordinate value of this System.Windows.Point.

Get: Y(self: Point) -> float

Set: Y(self: Point)=value
"""


