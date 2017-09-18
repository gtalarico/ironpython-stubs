class Point(object):
 """
 Represents an ordered pair of integer x- and y-coordinates that defines a point in a two-dimensional plane.

 

 Point(x: int,y: int)

 Point(sz: Size)

 Point(dw: int)
 """
 @staticmethod
 def Add(pt,sz):
  """
  Add(pt: Point,sz: Size) -> Point

  

   Adds the specified System.Drawing.Size to the specified System.Drawing.Point.

  

   pt: The System.Drawing.Point to add.

   sz: The System.Drawing.Size to add

   Returns: The System.Drawing.Point that is the result of the addition operation.
  """
  pass
 @staticmethod
 def Ceiling(value):
  """
  Ceiling(value: PointF) -> Point

  

   Converts the specified System.Drawing.PointF to a System.Drawing.Point by rounding the values of 

    the System.Drawing.PointF to the next higher integer values.

  

  

   value: The System.Drawing.PointF to convert.

   Returns: The System.Drawing.Point this method converts to.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: Point,obj: object) -> bool

  

   Specifies whether this System.Drawing.Point contains the same coordinates as the specified 

    System.Object.

  

  

   obj: The System.Object to test.

   Returns: true if obj is a System.Drawing.Point and has the same coordinates as this System.Drawing.Point.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Point) -> int

  

   Returns a hash code for this System.Drawing.Point.

   Returns: An integer value that specifies a hash value for this System.Drawing.Point.
  """
  pass
 def Offset(self,*__args):
  """
  Offset(self: Point,p: Point)

   Translates this System.Drawing.Point by the specified System.Drawing.Point.

  

   p: The System.Drawing.Point used offset this System.Drawing.Point.

  Offset(self: Point,dx: int,dy: int)

   Translates this System.Drawing.Point by the specified amount.

  

   dx: The amount to offset the x-coordinate.

   dy: The amount to offset the y-coordinate.
  """
  pass
 @staticmethod
 def Round(value):
  """
  Round(value: PointF) -> Point

  

   Converts the specified System.Drawing.PointF to a System.Drawing.Point object by rounding the 

    System.Drawing.Point values to the nearest integer.

  

  

   value: The System.Drawing.PointF to convert.

   Returns: The System.Drawing.Point this method converts to.
  """
  pass
 @staticmethod
 def Subtract(pt,sz):
  """
  Subtract(pt: Point,sz: Size) -> Point

  

   Returns the result of subtracting specified System.Drawing.Size from the specified 

    System.Drawing.Point.

  

  

   pt: The System.Drawing.Point to be subtracted from.

   sz: The System.Drawing.Size to subtract from the System.Drawing.Point.

   Returns: The System.Drawing.Point that is the result of the subtraction operation.
  """
  pass
 def ToString(self):
  """
  ToString(self: Point) -> str

  

   Converts this System.Drawing.Point to a human-readable string.

   Returns: A string that represents this System.Drawing.Point.
  """
  pass
 @staticmethod
 def Truncate(value):
  """
  Truncate(value: PointF) -> Point

  

   Converts the specified System.Drawing.PointF to a System.Drawing.Point by truncating the values 

    of the System.Drawing.Point.

  

  

   value: The System.Drawing.PointF to convert.

   Returns: The System.Drawing.Point this method converts to.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Point]() -> Point

  

  __new__(cls: type,x: int,y: int)

  __new__(cls: type,sz: Size)

  __new__(cls: type,dw: int)
  """
  pass
 def __ne__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this System.Drawing.Point is empty.



Get: IsEmpty(self: Point) -> bool



"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the x-coordinate of this System.Drawing.Point.



Get: X(self: Point) -> int



Set: X(self: Point)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the y-coordinate of this System.Drawing.Point.



Get: Y(self: Point) -> int



Set: Y(self: Point)=value

"""


 Empty=None

