class PointF(object):
 """
 Represents an ordered pair of floating-point x- and y-coordinates that defines a point in a two-dimensional plane.

 

 PointF(x: Single,y: Single)
 """
 @staticmethod
 def Add(pt,sz):
  """
  Add(pt: PointF,sz: SizeF) -> PointF

  

   Translates a given System.Drawing.PointF by a specified System.Drawing.SizeF.

  

   pt: The System.Drawing.PointF to translate.

   sz: The System.Drawing.SizeF that specifies the numbers to add to the coordinates of pt.

   Returns: The translated System.Drawing.PointF.

  Add(pt: PointF,sz: Size) -> PointF

  

   Translates a given System.Drawing.PointF by the specified System.Drawing.Size.

  

   pt: The System.Drawing.PointF to translate.

   sz: The System.Drawing.Size that specifies the numbers to add to the coordinates of pt.

   Returns: The translated System.Drawing.PointF.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PointF,obj: object) -> bool

  

   Specifies whether this System.Drawing.PointF contains the same coordinates as the specified 

    System.Object.

  

  

   obj: The System.Object to test.

   Returns: This method returns true if obj is a System.Drawing.PointF and has the same coordinates as this 

    System.Drawing.Point.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PointF) -> int

  

   Returns a hash code for this System.Drawing.PointF structure.

   Returns: An integer value that specifies a hash value for this System.Drawing.PointF structure.
  """
  pass
 @staticmethod
 def Subtract(pt,sz):
  """
  Subtract(pt: PointF,sz: SizeF) -> PointF

  

   Translates a System.Drawing.PointF by the negative of a specified size.

  

   pt: The System.Drawing.PointF to translate.

   sz: The System.Drawing.SizeF that specifies the numbers to subtract from the coordinates of pt.

   Returns: The translated System.Drawing.PointF.

  Subtract(pt: PointF,sz: Size) -> PointF

  

   Translates a System.Drawing.PointF by the negative of a specified size.

  

   pt: The System.Drawing.PointF to translate.

   sz: The System.Drawing.Size that specifies the numbers to subtract from the coordinates of pt.

   Returns: The translated System.Drawing.PointF.
  """
  pass
 def ToString(self):
  """
  ToString(self: PointF) -> str

  

   Converts this System.Drawing.PointF to a human readable string.

   Returns: A string that represents this System.Drawing.PointF.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,x,y):
  """
  __new__[PointF]() -> PointF

  

  __new__(cls: type,x: Single,y: Single)
  """
  pass
 def __ne__(self,*args):
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
  pass
 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this System.Drawing.PointF is empty.



Get: IsEmpty(self: PointF) -> bool



"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the x-coordinate of this System.Drawing.PointF.



Get: X(self: PointF) -> Single



Set: X(self: PointF)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the y-coordinate of this System.Drawing.PointF.



Get: Y(self: PointF) -> Single



Set: Y(self: PointF)=value

"""


 Empty=None

