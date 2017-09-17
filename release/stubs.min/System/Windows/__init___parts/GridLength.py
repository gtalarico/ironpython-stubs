class GridLength(object,IEquatable[GridLength]):
 """
 Represents the length of elements that explicitly support System.Windows.GridUnitType.Star unit types.
 
 GridLength(pixels: float)
 GridLength(value: float,type: GridUnitType)
 """
 def Equals(self,*__args):
  """
  Equals(self: GridLength,gridLength: GridLength) -> bool
  
   Determines whether the specified System.Windows.GridLength is equal to the 
    current System.Windows.GridLength.
  
  
   gridLength: The System.Windows.GridLength structure to compare with the current instance.
   Returns: true if the specified System.Windows.GridLength has the same value and 
    System.Windows.GridLength.GridUnitType as the current instance; otherwise,
    false.
  
  Equals(self: GridLength,oCompare: object) -> bool
  
   Determines whether the specified object is equal to the current 
    System.Windows.GridLength instance.
  
  
   oCompare: The object to compare with the current instance.
   Returns: true if the specified object has the same value and System.Windows.GridUnitType 
    as the current instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: GridLength) -> int
  
   Gets a hash code for the System.Windows.GridLength.
   Returns: A hash code for the current System.Windows.GridLength structure.
  """
  pass
 def ToString(self):
  """
  ToString(self: GridLength) -> str
  
   Returns a System.String representation of the System.Windows.GridLength.
   Returns: A System.String representation of the current System.Windows.GridLength 
    structure.
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
  __new__[GridLength]() -> GridLength
  
  __new__(cls: type,pixels: float)
  __new__(cls: type,value: float,type: GridUnitType)
  """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 GridUnitType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the associated System.Windows.GridUnitType for the System.Windows.GridLength.

Get: GridUnitType(self: GridLength) -> GridUnitType

"""

 IsAbsolute=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.Windows.GridLength holds a value that is expressed in pixels.

Get: IsAbsolute(self: GridLength) -> bool

"""

 IsAuto=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.Windows.GridLength holds a value whose size is determined by the size properties of the content object.

Get: IsAuto(self: GridLength) -> bool

"""

 IsStar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.Windows.GridLength holds a value that is expressed as a weighted proportion of available space.

Get: IsStar(self: GridLength) -> bool

"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Double that represents the value of the System.Windows.GridLength.

Get: Value(self: GridLength) -> float

"""


 Auto=None

