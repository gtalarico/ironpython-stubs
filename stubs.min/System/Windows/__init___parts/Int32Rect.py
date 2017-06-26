class Int32Rect(object,IFormattable):
 """
 Describes the width,height,and location of an integer rectangle.
 
 Int32Rect(x: int,y: int,width: int,height: int)
 """
 @staticmethod
 def Equals(*__args):
  """
  Equals(self: Int32Rect,value: Int32Rect) -> bool
  
   Determines whether the specified rectangle is equal to this rectangle.
  
   value: The rectangle to compare to the current rectangle.
   Returns: true if both rectangles have the same System.Windows.Int32Rect.X,
    System.Windows.Int32Rect.Y,System.Windows.Int32Rect.Width,and 
    System.Windows.Int32Rect.Height as this rectangle; otherwise,false.
  
  Equals(self: Int32Rect,o: object) -> bool
  
   Determines whether the specified rectangle is equal to this rectangle.
  
   o: The object to compare to the current rectangle.
   Returns: true if o is an System.Windows.Int32Rect and the same 
    System.Windows.Int32Rect.X,System.Windows.Int32Rect.Y,
    System.Windows.Int32Rect.Width,and System.Windows.Int32Rect.Height as this 
    rectangle; otherwise,false.
  
  Equals(int32Rect1: Int32Rect,int32Rect2: Int32Rect) -> bool
  
   Determines whether the specified rectangles are equal.
  
   int32Rect1: The first rectangle to compare.
   int32Rect2: The second rectangle to compare.
   Returns: true if int32Rect1 and int32Rect2 have the same System.Windows.Int32Rect.X,
    System.Windows.Int32Rect.Y,System.Windows.Int32Rect.Width,and 
    System.Windows.Int32Rect.Height; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Int32Rect) -> int
  
   Creates a hash code from this rectangle's System.Windows.Int32Rect.X,
    System.Windows.Int32Rect.Y,System.Windows.Int32Rect.Width,and 
    System.Windows.Int32Rect.Height values.
  
   Returns: This rectangle's hash code.
  """
  pass
 @staticmethod
 def Parse(source):
  """
  Parse(source: str) -> Int32Rect
  
   Creates an System.Windows.Int32Rect structure from the specified System.String 
    representation.
  
  
   source: A string representation of an System.Windows.Int32Rect.
   Returns: The equivalent System.Windows.Int32Rect structure.
  """
  pass
 def ToString(self,provider=None):
  """
  ToString(self: Int32Rect,provider: IFormatProvider) -> str
  
   Creates a string representation of this System.Windows.Int32Rect based on the 
    supplied System.IFormatProvider.
  
  
   provider: The format provider to use. If provider is null,the current culture is used.
   Returns: A string representation of this instance of System.Windows.Int32Rect.
  ToString(self: Int32Rect) -> str
  
   Creates a string representation of this System.Windows.Int32Rect.
   Returns: A string containing the same System.Windows.Int32Rect.X,
    System.Windows.Int32Rect.Y,System.Windows.Int32Rect.Width,and 
    System.Windows.Int32Rect.Height values of this System.Windows.Int32Rect 
    structure.
  """
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
 @staticmethod
 def __new__(self,x,y,width,height):
  """
  __new__(cls: type,x: int,y: int,width: int,height: int)
  __new__[Int32Rect]() -> Int32Rect
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 HasArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasArea(self: Int32Rect) -> bool

"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the rectangle.

Get: Height(self: Int32Rect) -> int

Set: Height(self: Int32Rect)=value
"""

 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the rectangle is empty.

Get: IsEmpty(self: Int32Rect) -> bool

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of the rectangle.

Get: Width(self: Int32Rect) -> int

Set: Width(self: Int32Rect)=value
"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the x-coordinate of the top-left corner of the rectangle.

Get: X(self: Int32Rect) -> int

Set: X(self: Int32Rect)=value
"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the y-coordinate of the top-left corner of the rectangle.

Get: Y(self: Int32Rect) -> int

Set: Y(self: Int32Rect)=value
"""


 Empty=None

