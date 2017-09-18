class RectangleF(object):
 """
 Stores a set of four floating-point numbers that represent the location and size of a rectangle. For more advanced region functions,use a System.Drawing.Region object.

 

 RectangleF(x: Single,y: Single,width: Single,height: Single)

 RectangleF(location: PointF,size: SizeF)
 """
 def Contains(self,*__args):
  """
  Contains(self: RectangleF,rect: RectangleF) -> bool

  

   Determines if the rectangular region represented by rect is entirely contained within this 

    System.Drawing.RectangleF structure.

  

  

   rect: The System.Drawing.RectangleF to test.

   Returns: This method returns true if the rectangular region represented by rect is entirely contained 

    within the rectangular region represented by this System.Drawing.RectangleF; otherwise false.

  

  Contains(self: RectangleF,pt: PointF) -> bool

  

   Determines if the specified point is contained within this System.Drawing.RectangleF structure.

  

   pt: The System.Drawing.PointF to test.

   Returns: This method returns true if the point represented by the pt parameter is contained within this 

    System.Drawing.RectangleF structure; otherwise false.

  

  Contains(self: RectangleF,x: Single,y: Single) -> bool

  

   Determines if the specified point is contained within this System.Drawing.RectangleF structure.

  

   x: The x-coordinate of the point to test.

   y: The y-coordinate of the point to test.

   Returns: This method returns true if the point defined by x and y is contained within this 

    System.Drawing.RectangleF structure; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: RectangleF,obj: object) -> bool

  

   Tests whether obj is a System.Drawing.RectangleF with the same location and size of this 

    System.Drawing.RectangleF.

  

  

   obj: The System.Object to test.

   Returns: This method returns true if obj is a System.Drawing.RectangleF and its X,Y,Width,and Height 

    properties are equal to the corresponding properties of this System.Drawing.RectangleF; 

    otherwise,false.
  """
  pass
 @staticmethod
 def FromLTRB(left,top,right,bottom):
  """
  FromLTRB(left: Single,top: Single,right: Single,bottom: Single) -> RectangleF

  

   Creates a System.Drawing.RectangleF structure with upper-left corner and lower-right corner at 

    the specified locations.

  

  

   left: The x-coordinate of the upper-left corner of the rectangular region.

   top: The y-coordinate of the upper-left corner of the rectangular region.

   right: The x-coordinate of the lower-right corner of the rectangular region.

   bottom: The y-coordinate of the lower-right corner of the rectangular region.

   Returns: The new System.Drawing.RectangleF that this method creates.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: RectangleF) -> int

  

   Gets the hash code for this System.Drawing.RectangleF structure. For information about the use 

    of hash codes,see Object.GetHashCode.

  

   Returns: The hash code for this System.Drawing.RectangleF.
  """
  pass
 def Inflate(self,*__args):
  """
  Inflate(rect: RectangleF,x: Single,y: Single) -> RectangleF

  

   Creates and returns an enlarged copy of the specified System.Drawing.RectangleF structure. The 

    copy is enlarged by the specified amount and the original rectangle remains unmodified.

  

  

   rect: The System.Drawing.RectangleF to be copied. This rectangle is not modified.

   x: The amount to enlarge the copy of the rectangle horizontally.

   y: The amount to enlarge the copy of the rectangle vertically.

   Returns: The enlarged System.Drawing.RectangleF.

  Inflate(self: RectangleF,size: SizeF)

   Enlarges this System.Drawing.RectangleF by the specified amount.

  

   size: The amount to inflate this rectangle.

  Inflate(self: RectangleF,x: Single,y: Single)

   Enlarges this System.Drawing.RectangleF structure by the specified amount.

  

   x: The amount to inflate this System.Drawing.RectangleF structure horizontally.

   y: The amount to inflate this System.Drawing.RectangleF structure vertically.
  """
  pass
 def Intersect(self,*__args):
  """
  Intersect(a: RectangleF,b: RectangleF) -> RectangleF

  

   Returns a System.Drawing.RectangleF structure that represents the intersection of two 

    rectangles. If there is no intersection,and empty System.Drawing.RectangleF is returned.

  

  

   a: A rectangle to intersect.

   b: A rectangle to intersect.

   Returns: A third System.Drawing.RectangleF structure the size of which represents the overlapped area of 

    the two specified rectangles.

  

  Intersect(self: RectangleF,rect: RectangleF)

   Replaces this System.Drawing.RectangleF structure with the intersection of itself and the 

    specified System.Drawing.RectangleF structure.

  

  

   rect: The rectangle to intersect.
  """
  pass
 def IntersectsWith(self,rect):
  """
  IntersectsWith(self: RectangleF,rect: RectangleF) -> bool

  

   Determines if this rectangle intersects with rect.

  

   rect: The rectangle to test.

   Returns: This method returns true if there is any intersection.
  """
  pass
 def Offset(self,*__args):
  """
  Offset(self: RectangleF,x: Single,y: Single)

   Adjusts the location of this rectangle by the specified amount.

  

   x: The amount to offset the location horizontally.

   y: The amount to offset the location vertically.

  Offset(self: RectangleF,pos: PointF)

   Adjusts the location of this rectangle by the specified amount.

  

   pos: The amount to offset the location.
  """
  pass
 def ToString(self):
  """
  ToString(self: RectangleF) -> str

  

   Converts the Location and System.Drawing.Size of this System.Drawing.RectangleF to a 

    human-readable string.

  

   Returns: A string that contains the position,width,and height of this System.Drawing.RectangleF 

    structure. For example,"{X=20,Y=20,Width=100,Height=50}".
  """
  pass
 @staticmethod
 def Union(a,b):
  """
  Union(a: RectangleF,b: RectangleF) -> RectangleF

  

   Creates the smallest possible third rectangle that can contain both of two rectangles that form 

    a union.

  

  

   a: A rectangle to union.

   b: A rectangle to union.

   Returns: A third System.Drawing.RectangleF structure that contains both of the two rectangles that form 

    the union.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[RectangleF]() -> RectangleF

  

  __new__(cls: type,x: Single,y: Single,width: Single,height: Single)

  __new__(cls: type,location: PointF,size: SizeF)
  """
  pass
 def __ne__(self,*args):
  pass
 Bottom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the y-coordinate that is the sum of System.Drawing.RectangleF.Y and System.Drawing.RectangleF.Height of this System.Drawing.RectangleF structure.



Get: Bottom(self: RectangleF) -> Single



"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of this System.Drawing.RectangleF structure.



Get: Height(self: RectangleF) -> Single



Set: Height(self: RectangleF)=value

"""

 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Tests whether the System.Drawing.RectangleF.Width or System.Drawing.RectangleF.Height property of this System.Drawing.RectangleF has a value of zero.



Get: IsEmpty(self: RectangleF) -> bool



"""

 Left=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the x-coordinate of the left edge of this System.Drawing.RectangleF structure.



Get: Left(self: RectangleF) -> Single



"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the coordinates of the upper-left corner of this System.Drawing.RectangleF structure.



Get: Location(self: RectangleF) -> PointF



Set: Location(self: RectangleF)=value

"""

 Right=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the x-coordinate that is the sum of System.Drawing.RectangleF.X and System.Drawing.RectangleF.Width of this System.Drawing.RectangleF structure.



Get: Right(self: RectangleF) -> Single



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size of this System.Drawing.RectangleF.



Get: Size(self: RectangleF) -> SizeF



Set: Size(self: RectangleF)=value

"""

 Top=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the y-coordinate of the top edge of this System.Drawing.RectangleF structure.



Get: Top(self: RectangleF) -> Single



"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of this System.Drawing.RectangleF structure.



Get: Width(self: RectangleF) -> Single



Set: Width(self: RectangleF)=value

"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the x-coordinate of the upper-left corner of this System.Drawing.RectangleF structure.



Get: X(self: RectangleF) -> Single



Set: X(self: RectangleF)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the y-coordinate of the upper-left corner of this System.Drawing.RectangleF structure.



Get: Y(self: RectangleF) -> Single



Set: Y(self: RectangleF)=value

"""


 Empty=None

