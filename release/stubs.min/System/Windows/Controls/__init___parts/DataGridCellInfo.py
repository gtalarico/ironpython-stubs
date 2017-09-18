class DataGridCellInfo(object):
 """
 Represents information about a specific cell in a System.Windows.Controls.DataGrid.

 

 DataGridCellInfo(item: object,column: DataGridColumn)

 DataGridCellInfo(cell: DataGridCell)
 """
 def Equals(self,obj):
  """
  Equals(self: DataGridCellInfo,obj: object) -> bool

  

   Indicates whether the specified object is equal to the current instance.

  

   obj: The object to compare to the current instance.

   Returns: true if the comparison object represents the same cell; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DataGridCellInfo) -> int

  

   Returns a hash code for the current System.Windows.Controls.DataGridCellInfo structure.

   Returns: A hash code for the structure.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,item: object,column: DataGridColumn)

  __new__(cls: type,cell: DataGridCell)

  __new__[DataGridCellInfo]() -> DataGridCellInfo
  """
  pass
 def __ne__(self,*args):
  pass
 Column=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column that contains the cell.



Get: Column(self: DataGridCellInfo) -> DataGridColumn



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the structure holds valid information.



Get: IsValid(self: DataGridCellInfo) -> bool



"""

 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the data item for the row that contains the cell.



Get: Item(self: DataGridCellInfo) -> object



"""


