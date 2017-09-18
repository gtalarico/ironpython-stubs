class DataGridViewAdvancedBorderStyle(object,ICloneable):
 """
 Contains border styles for the cells in a System.Windows.Forms.DataGridView control.

 

 DataGridViewAdvancedBorderStyle()
 """
 def Equals(self,other):
  """
  Equals(self: DataGridViewAdvancedBorderStyle,other: object) -> bool

  

   Determines whether the specified object is equal to the current 

    System.Windows.Forms.DataGridViewAdvancedBorderStyle.

  

  

   other: An System.Object to be compared.

   Returns: true if other is a System.Windows.Forms.DataGridViewAdvancedBorderStyle and the values for the 

    System.Windows.Forms.DataGridViewAdvancedBorderStyle.Top,

    System.Windows.Forms.DataGridViewAdvancedBorderStyle.Bottom,

    System.Windows.Forms.DataGridViewAdvancedBorderStyle.Left,and 

    System.Windows.Forms.DataGridViewAdvancedBorderStyle.Right properties are equal to their 

    counterpart in the current System.Windows.Forms.DataGridViewAdvancedBorderStyle; otherwise,

    false.
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: DataGridViewAdvancedBorderStyle) -> int """
  pass
 def ToString(self):
  """
  ToString(self: DataGridViewAdvancedBorderStyle) -> str

  

   Returns a string that represents the System.Windows.Forms.DataGridViewAdvancedBorderStyle.

   Returns: A string that represents the System.Windows.Forms.DataGridViewAdvancedBorderStyle.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 All=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the border style for all of the borders of a cell.



Get: All(self: DataGridViewAdvancedBorderStyle) -> DataGridViewAdvancedCellBorderStyle



Set: All(self: DataGridViewAdvancedBorderStyle)=value

"""

 Bottom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style for the bottom border of a cell.



Get: Bottom(self: DataGridViewAdvancedBorderStyle) -> DataGridViewAdvancedCellBorderStyle



Set: Bottom(self: DataGridViewAdvancedBorderStyle)=value

"""

 Left=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the style for the left border of a cell.



Get: Left(self: DataGridViewAdvancedBorderStyle) -> DataGridViewAdvancedCellBorderStyle



Set: Left(self: DataGridViewAdvancedBorderStyle)=value

"""

 Right=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the style for the right border of a cell.



Get: Right(self: DataGridViewAdvancedBorderStyle) -> DataGridViewAdvancedCellBorderStyle



Set: Right(self: DataGridViewAdvancedBorderStyle)=value

"""

 Top=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the style for the top border of a cell.



Get: Top(self: DataGridViewAdvancedBorderStyle) -> DataGridViewAdvancedCellBorderStyle



Set: Top(self: DataGridViewAdvancedBorderStyle)=value

"""


