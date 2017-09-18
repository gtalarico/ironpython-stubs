class Rectangle(object):
 """
 Stores a set of four integers that represent the location and size of a rectangle

 

 Rectangle(x: int,y: int,width: int,height: int)

 Rectangle(location: Point,size: Size)
 """
 @staticmethod
 def Ceiling(value):
  """
  Ceiling(value: RectangleF) -> Rectangle

  

   Converts the specified System.Drawing.RectangleF structure to a System.Drawing.Rectangle 

    structure by rounding the System.Drawing.RectangleF values to the next higher integer values.

  

  

   value: The System.Drawing.RectangleF structure to be converted.

   Returns: Returns a System.Drawing.Rectangle.
  """
  pass
 def Contains(self,*__args):
  """
  Contains(self: Rectangle,rect: Rectangle) -> bool

  

   Determines if the rectangular region represented by rect is entirely contained within this 

    System.Drawing.Rectangle structure.

  

  

   rect: The System.Drawing.Rectangle to test.

   Returns: This method returns true if the rectangular region represented by rect is entirely contained 

    within this System.Drawing.Rectangle structure; otherwise false.

  

  Contains(self: Rectangle,pt: Point) -> bool

  

   Determines if the specified point is contained within this System.Drawing.Rectangle structure.

  

   pt: The System.Drawing.Point to test.

   Returns: This method returns true if the point represented by pt is contained within this 

    System.Drawing.Rectangle structure; otherwise false.

  

  Contains(self: Rectangle,x: int,y: int) -> bool

  

   Determines if the specified point is contained within this System.Drawing.Rectangle structure.

  

   x: The x-coordinate of the point to test.

   y: The y-coordinate of the point to test.

   Returns: This method returns true if the point defined by x and y is contained within this 

    System.Drawing.Rectangle structure; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: Rectangle,obj: object) -> bool

  

   Tests whether obj is a System.Drawing.Rectangle structure with the same location and size of 

    this System.Drawing.Rectangle structure.

  

  

   obj: The System.Object to test.

   Returns: This method returns true if obj is a System.Drawing.Rectangle structure and its 

    System.Drawing.Rectangle.X,System.Drawing.Rectangle.Y,System.Drawing.Rectangle.Width,and 

    System.Drawing.Rectangle.Height properties are equal to the corresponding properties of this 

    System.Drawing.Rectangle structure; otherwise,false.
  """
  pass
 @staticmethod
 def FromLTRB(left,top,right,bottom):
  """
  FromLTRB(left: int,top: int,right: int,bottom: int) -> Rectangle

  

   Creates a System.Drawing.Rectangle structure with the specified edge locations.

  

   left: The x-coordinate of the upper-left corner of this System.Drawing.Rectangle structure.

   top: The y-coordinate of the upper-left corner of this System.Drawing.Rectangle structure.

   right: The x-coordinate of the lower-right corner of this System.Drawing.Rectangle structure.

   bottom: The y-coordinate of the lower-right corner of this System.Drawing.Rectangle structure.

   Returns: The new System.Drawing.Rectangle that this method creates.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Rectangle) -> int

  

   Returns the hash code for this System.Drawing.Rectangle structure. For information about the use 

    of hash codes,see System.Object.GetHashCode .

  

   Returns: An integer that represents the hash code for this rectangle.
  """
  pass
 def Inflate(self,*__args):
  """
  Inflate(rect: Rectangle,x: int,y: int) -> Rectangle

  

   Creates and returns an enlarged copy of the specified System.Drawing.Rectangle structure. The 

    copy is enlarged by the specified amount. The original System.Drawing.Rectangle structure 

    remains unmodified.

  

  

   rect: The System.Drawing.Rectangle with which to start. This rectangle is not modified.

   x: The amount to inflate this System.Drawing.Rectangle horizontally.

   y: The amount to inflate this System.Drawing.Rectangle vertically.

   Returns: The enlarged System.Drawing.Rectangle.

  Inflate(self: Rectangle,size: Size)

   Enlarges this System.Drawing.Rectangle by the specified amount.

  

   size: The amount to inflate this rectangle.

  Inflate(self: Rectangle,width: int,height: int)

   Enlarges this System.Drawing.Rectangle by the specified amount.

  

   width: The amount to inflate this System.Drawing.Rectangle horizontally.

   height: The amount to inflate this System.Drawing.Rectangle vertically.
  """
  pass
 def Intersect(self,*__args):
  """
  Intersect(a: Rectangle,b: Rectangle) -> Rectangle

  

   Returns a third System.Drawing.Rectangle structure that represents the intersection of two other 

    System.Drawing.Rectangle structures. If there is no intersection,an empty 

    System.Drawing.Rectangle is returned.

  

  

   a: A rectangle to intersect.

   b: A rectangle to intersect.

   Returns: A System.Drawing.Rectangle that represents the intersection of a and b.

  Intersect(self: Rectangle,rect: Rectangle)

   Replaces this System.Drawing.Rectangle with the intersection of itself and the specified 

    System.Drawing.Rectangle.

  

  

   rect: The System.Drawing.Rectangle with which to intersect.
  """
  pass
 def IntersectsWith(self,rect):
  """
  IntersectsWith(self: Rectangle,rect: Rectangle) -> bool

  

   Determines if this rectangle intersects with rect.

  

   rect: The rectangle to test.

   Returns: This method returns true if there is any intersection,otherwise false.
  """
  pass
 def Offset(self,*__args):
  """
  Offset(self: Rectangle,x: int,y: int)

   Adjusts the location of this rectangle by the specified amount.

  

   x: The horizontal offset.

   y: The vertical offset.

  Offset(self: Rectangle,pos: Point)

   Adjusts the location of this rectangle by the specified amount.

  

   pos: Amount to offset the location.
  """
  pass
 @staticmethod
 def Round(value):
  """
  Round(value: RectangleF) -> Rectangle

  

   Converts the specified System.Drawing.RectangleF to a System.Drawing.Rectangle by rounding the 

    System.Drawing.RectangleF values to the nearest integer values.

  

  

   value: The System.Drawing.RectangleF to be converted.

   Returns: A System.Drawing.Rectangle.
  """
  pass
 def ToString(self):
  """
  ToString(self: Rectangle) -> str

  

   Converts the attributes of this System.Drawing.Rectangle to a human-readable string.

   Returns: A string that contains the position,width,and height of this System.Drawing.Rectangle 

    structure � for example,{X=20,Y=20,Width=100,Height=50}
  """
  pass
 @staticmethod
 def Truncate(value):
  """
  Truncate(value: RectangleF) -> Rectangle

  

   Converts the specified System.Drawing.RectangleF to a System.Drawing.Rectangle by truncating the 

    System.Drawing.RectangleF values.

  

  

   value: The System.Drawing.RectangleF to be converted.

   Returns: A System.Drawing.Rectangle.
  """
  pass
 @staticmethod
 def Union(a,b):
  """
  Union(a: Rectangle,b: Rectangle) -> Rectangle

  

   Gets a System.Drawing.Rectangle structure that contains the union of two 

    System.Drawing.Rectangle structures.

  

  

   a: A rectangle to union.

   b: A rectangle to union.

   Returns: A System.Drawing.Rectangle structure that bounds the union of the two System.Drawing.Rectangle 

    structures.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Rectangle]() -> Rectangle

  

  __new__(cls: type,x: int,y: int,width: int,height: int)

  __new__(cls: type,location: Point,size: Size)
  """
  pass
 def __ne__(self,*args):
  pass
 Bottom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the y-coordinate that is the sum of the System.Drawing.Rectangle.Y and System.Drawing.Rectangle.Height property values of this System.Drawing.Rectangle structure.



Get: Bottom(self: Rectangle) -> int



"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of this System.Drawing.Rectangle structure.



Get: Height(self: Rectangle) -> int



Set: Height(self: Rectangle)=value

"""

 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Tests whether all numeric properties of this System.Drawing.Rectangle have values of zero.



Get: IsEmpty(self: Rectangle) -> bool



"""

 Left=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the x-coordinate of the left edge of this System.Drawing.Rectangle structure.



Get: Left(self: Rectangle) -> int



"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the coordinates of the upper-left corner of this System.Drawing.Rectangle structure.



Get: Location(self: Rectangle) -> Point



Set: Location(self: Rectangle)=value

"""

 Right=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the x-coordinate that is the sum of System.Drawing.Rectangle.X and System.Drawing.Rectangle.Width property values of this System.Drawing.Rectangle structure.



Get: Right(self: Rectangle) -> int



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size of this System.Drawing.Rectangle.



Get: Size(self: Rectangle) -> Size



Set: Size(self: Rectangle)=value

"""

 Top=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the y-coordinate of the top edge of this System.Drawing.Rectangle structure.



Get: Top(self: Rectangle) -> int



"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of this System.Drawing.Rectangle structure.



Get: Width(self: Rectangle) -> int



Set: Width(self: Rectangle)=value

"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the x-coordinate of the upper-left corner of this System.Drawing.Rectangle structure.



Get: X(self: Rectangle) -> int



Set: X(self: Rectangle)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the y-coordinate of the upper-left corner of this System.Drawing.Rectangle structure.



Get: Y(self: Rectangle) -> int



Set: Y(self: Rectangle)=value

"""


 Empty=None

