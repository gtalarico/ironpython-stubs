class Thickness(object,IEquatable[Thickness]):
 """
 Describes the thickness of a frame around a rectangle. Four System.Double values describe the System.Windows.Thickness.Left,System.Windows.Thickness.Top,System.Windows.Thickness.Right,and System.Windows.Thickness.Bottom sides of the rectangle,respectively.
 
 Thickness(uniformLength: float)
 Thickness(left: float,top: float,right: float,bottom: float)
 """
 def Equals(self,*__args):
  """
  Equals(self: Thickness,thickness: Thickness) -> bool
  
   Compares this System.Windows.Thickness structure to another 
    System.Windows.Thickness structure for equality.
  
  
   thickness: An instance of System.Windows.Thickness to compare for equality.
   Returns: true if the two instances of System.Windows.Thickness are equal; otherwise,
    false.
  
  Equals(self: Thickness,obj: object) -> bool
  
   Compares this System.Windows.Thickness structure to another System.Object for 
    equality.
  
  
   obj: The object to compare.
   Returns: true if the two objects are equal; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Thickness) -> int
  
   Returns the hash code of the structure.
   Returns: A hash code for this instance of System.Windows.Thickness.
  """
  pass
 def ToString(self):
  """
  ToString(self: Thickness) -> str
  
   Returns the string representation of the System.Windows.Thickness structure.
   Returns: A System.String that represents the System.Windows.Thickness value.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__[Thickness]() -> Thickness
  
  __new__(cls: type,uniformLength: float)
  __new__(cls: type,left: float,top: float,right: float,bottom: float)
  """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Bottom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width,in pixels,of the lower side of the bounding rectangle.

Get: Bottom(self: Thickness) -> float

Set: Bottom(self: Thickness)=value
"""

 Left=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width,in pixels,of the left side of the bounding rectangle.

Get: Left(self: Thickness) -> float

Set: Left(self: Thickness)=value
"""

 Right=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width,in pixels,of the right side of the bounding rectangle.

Get: Right(self: Thickness) -> float

Set: Right(self: Thickness)=value
"""

 Top=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width,in pixels,of the upper side of the bounding rectangle.

Get: Top(self: Thickness) -> float

Set: Top(self: Thickness)=value
"""


