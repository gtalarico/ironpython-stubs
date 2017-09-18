class DataGridLength(object,IEquatable[DataGridLength]):
 """
 Represents the lengths of elements within the System.Windows.Controls.DataGrid control.

 

 DataGridLength(pixels: float)

 DataGridLength(value: float,type: DataGridLengthUnitType)

 DataGridLength(value: float,type: DataGridLengthUnitType,desiredValue: float,displayValue: float)
 """
 def Equals(self,*__args):
  """
  Equals(self: DataGridLength,other: DataGridLength) -> bool

  

   Determines whether the specified System.Windows.Controls.DataGridLength is equal to the current 

    System.Windows.Controls.DataGridLength.

  

  

   other: The System.Windows.Controls.DataGridLength to compare to the current instance.

   Returns: true if the specified object is a System.Windows.Controls.DataGridLength with the same value or 

    sizing mode as the current System.Windows.Controls.DataGridLength; otherwise,false.

  

  Equals(self: DataGridLength,obj: object) -> bool

  

   Determines whether the specified object is equal to the current 

    System.Windows.Controls.DataGridLength.

  

  

   obj: The object to compare to the current instance.

   Returns: true if the specified object is a System.Windows.Controls.DataGridLength with the same value or 

    sizing mode as the current System.Windows.Controls.DataGridLength; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DataGridLength) -> int

  

   Gets a hash code for the System.Windows.Controls.DataGridLength.

   Returns: A hash code for the current System.Windows.Controls.DataGridLength.
  """
  pass
 def ToString(self):
  """
  ToString(self: DataGridLength) -> str

  

   Returns a string that represents the current object.

   Returns: A string that represent the current object.
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
  __new__(cls: type,pixels: float)

  __new__(cls: type,value: float,type: DataGridLengthUnitType)

  __new__(cls: type,value: float,type: DataGridLengthUnitType,desiredValue: float,displayValue: float)

  __new__[DataGridLength]() -> DataGridLength
  """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 DesiredValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the calculated pixel value needed for the element.



Get: DesiredValue(self: DataGridLength) -> float



"""

 DisplayValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the pixel value allocated for the size of the element.



Get: DisplayValue(self: DataGridLength) -> float



"""

 IsAbsolute=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this instance sizes elements based on a fixed pixel value.



Get: IsAbsolute(self: DataGridLength) -> bool



"""

 IsAuto=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this instance automatically sizes elements based on both the content of cells and the column headers.



Get: IsAuto(self: DataGridLength) -> bool



"""

 IsSizeToCells=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this instance automatically sizes elements based on the content of the cells.



Get: IsSizeToCells(self: DataGridLength) -> bool



"""

 IsSizeToHeader=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this instance automatically sizes elements based on the header.



Get: IsSizeToHeader(self: DataGridLength) -> bool



"""

 IsStar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this instance automatically sizes elements based on a weighted proportion of available space.



Get: IsStar(self: DataGridLength) -> bool



"""

 UnitType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type that is used to determine how the size of the element is calculated.



Get: UnitType(self: DataGridLength) -> DataGridLengthUnitType



"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the absolute value of the System.Windows.Controls.DataGridLength in pixels.



Get: Value(self: DataGridLength) -> float



"""


 Auto=None
 SizeToCells=None
 SizeToHeader=None

