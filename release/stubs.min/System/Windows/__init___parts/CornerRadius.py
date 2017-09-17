class CornerRadius(object,IEquatable[CornerRadius]):
 """
 Represents the radii of a rectangle's corners.
 
 CornerRadius(uniformRadius: float)
 CornerRadius(topLeft: float,topRight: float,bottomRight: float,bottomLeft: float)
 """
 def Equals(self,*__args):
  """
  Equals(self: CornerRadius,cornerRadius: CornerRadius) -> bool
  
   Compares two System.Windows.CornerRadius structures for equality.
  
   cornerRadius: The System.Windows.CornerRadius to compare to this System.Windows.CornerRadius.
   Returns: true if cornerRadius contains the same corner radius values as this 
    System.Windows.CornerRadius; otherwise,false.
  
  Equals(self: CornerRadius,obj: object) -> bool
  
   Determines whether the specified System.Object is a System.Windows.CornerRadius 
    and whether it contains the same corner radius values as this 
    System.Windows.CornerRadius.
  
  
   obj: The System.Object to compare.
   Returns: true if obj is a System.Windows.CornerRadius and contains the same corner 
    radius values as this System.Windows.CornerRadius; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CornerRadius) -> int
  
   Returns the hash code for this System.Windows.CornerRadius.
   Returns: The hash code for this System.Windows.CornerRadius structure.
  """
  pass
 def ToString(self):
  """
  ToString(self: CornerRadius) -> str
  
   Returns the string representation of the System.Windows.CornerRadius.
   Returns: A string representation of the System.Windows.CornerRadius.
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
  __new__[CornerRadius]() -> CornerRadius
  
  __new__(cls: type,uniformRadius: float)
  __new__(cls: type,topLeft: float,topRight: float,bottomRight: float,bottomLeft: float)
  """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 BottomLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the radius of the bottom-left corner.

Get: BottomLeft(self: CornerRadius) -> float

Set: BottomLeft(self: CornerRadius)=value
"""

 BottomRight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the radius of the bottom-right corner.

Get: BottomRight(self: CornerRadius) -> float

Set: BottomRight(self: CornerRadius)=value
"""

 TopLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the radius of the top-left corner.

Get: TopLeft(self: CornerRadius) -> float

Set: TopLeft(self: CornerRadius)=value
"""

 TopRight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the radius of the top-right corner.

Get: TopRight(self: CornerRadius) -> float

Set: TopRight(self: CornerRadius)=value
"""


