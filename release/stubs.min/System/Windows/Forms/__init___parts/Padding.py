class Padding(object):
 """
 Represents padding or margin information associated with a user interface (UI) element.

 

 Padding(all: int)

 Padding(left: int,top: int,right: int,bottom: int)
 """
 @staticmethod
 def Add(p1,p2):
  """
  Add(p1: Padding,p2: Padding) -> Padding

  

   Computes the sum of the two specified System.Windows.Forms.Padding values.

  

   p1: A System.Windows.Forms.Padding.

   p2: A System.Windows.Forms.Padding.

   Returns: A System.Windows.Forms.Padding that contains the sum of the two specified 

    System.Windows.Forms.Padding values.
  """
  pass
 def Equals(self,other):
  """
  Equals(self: Padding,other: object) -> bool

  

   Determines whether the value of the specified object is equivalent to the current 

    System.Windows.Forms.Padding.

  

  

   other: The object to compare to the current System.Windows.Forms.Padding.

   Returns: true if the System.Windows.Forms.Padding objects are equivalent; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Padding) -> int

  

   Generates a hash code for the current System.Windows.Forms.Padding.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 @staticmethod
 def Subtract(p1,p2):
  """
  Subtract(p1: Padding,p2: Padding) -> Padding

  

   Subtracts one specified System.Windows.Forms.Padding value from another.

  

   p1: A System.Windows.Forms.Padding.

   p2: A System.Windows.Forms.Padding.

   Returns: A System.Windows.Forms.Padding that contains the result of the subtraction of one specified 

    System.Windows.Forms.Padding value from another.
  """
  pass
 def ToString(self):
  """
  ToString(self: Padding) -> str

  

   Returns a string that represents the current System.Windows.Forms.Padding.

   Returns: A System.String that represents the current System.Windows.Forms.Padding.
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
  __new__(cls: type,all: int)

  __new__(cls: type,left: int,top: int,right: int,bottom: int)

  __new__[Padding]() -> Padding
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """
  __radd__(p1: Padding,p2: Padding) -> Padding

  

   Performs vector addition on the two specified System.Windows.Forms.Padding objects,resulting in 

    a new System.Windows.Forms.Padding.

  

  

   p1: The first System.Windows.Forms.Padding to add.

   p2: The second System.Windows.Forms.Padding to add.

   Returns: A new System.Windows.Forms.Padding that results from adding p1 and p2.
  """
  pass
 def __rsub__(self,*args):
  """
  __rsub__(p1: Padding,p2: Padding) -> Padding

  

   Performs vector subtraction on the two specified System.Windows.Forms.Padding objects,resulting 

    in a new System.Windows.Forms.Padding.

  

  

   p1: The System.Windows.Forms.Padding to subtract from (the minuend).

   p2: The System.Windows.Forms.Padding to subtract from (the subtrahend).

   Returns: The System.Windows.Forms.Padding result of subtracting p2 from p1.
  """
  pass
 def __sub__(self,*args):
  """ x.__sub__(y) <==> x-y """
  pass
 All=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the padding value for all the edges.



Get: All(self: Padding) -> int



Set: All(self: Padding)=value

"""

 Bottom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the padding value for the bottom edge.



Get: Bottom(self: Padding) -> int



Set: Bottom(self: Padding)=value

"""

 Horizontal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the combined padding for the right and left edges.



Get: Horizontal(self: Padding) -> int



"""

 Left=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the padding value for the left edge.



Get: Left(self: Padding) -> int



Set: Left(self: Padding)=value

"""

 Right=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the padding value for the right edge.



Get: Right(self: Padding) -> int



Set: Right(self: Padding)=value

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the padding information in the form of a System.Drawing.Size.



Get: Size(self: Padding) -> Size



"""

 Top=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the padding value for the top edge.



Get: Top(self: Padding) -> int



Set: Top(self: Padding)=value

"""

 Vertical=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the combined padding for the top and bottom edges.



Get: Vertical(self: Padding) -> int



"""


 Empty=None

