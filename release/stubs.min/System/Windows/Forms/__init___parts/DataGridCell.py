class DataGridCell(object):
 """
 Identifies a cell in the grid.

 

 DataGridCell(r: int,c: int)
 """
 def Equals(self,o):
  """
  Equals(self: DataGridCell,o: object) -> bool

  

   Gets a value indicating whether the System.Windows.Forms.DataGridCell is identical to a second 

    System.Windows.Forms.DataGridCell.

  

  

   o: An object you are to comparing.

   Returns: true if the second object is identical to the first; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DataGridCell) -> int

  

   Gets a hash value that can be added to a System.Collections.Hashtable.

   Returns: A number that uniquely identifies the System.Windows.Forms.DataGridCell in a 

    System.Collections.Hashtable.
  """
  pass
 def ToString(self):
  """
  ToString(self: DataGridCell) -> str

  

   Gets the row number and column number of the cell.

   Returns: A string containing the row number and column number.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,r,c):
  """
  __new__(cls: type,r: int,c: int)

  __new__[DataGridCell]() -> DataGridCell
  """
  pass
 def __ne__(self,*args):
  pass
 ColumnNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of a column in the System.Windows.Forms.DataGrid control.



Get: ColumnNumber(self: DataGridCell) -> int



Set: ColumnNumber(self: DataGridCell)=value

"""

 RowNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of a row in the System.Windows.Forms.DataGrid control.



Get: RowNumber(self: DataGridCell) -> int



Set: RowNumber(self: DataGridCell)=value

"""


