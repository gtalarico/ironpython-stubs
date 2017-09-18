class DataGridViewCellEventArgs(EventArgs):
 """
 Provides data for System.Windows.Forms.DataGridView events related to cell and row operations.

 

 DataGridViewCellEventArgs(columnIndex: int,rowIndex: int)
 """
 @staticmethod
 def __new__(self,columnIndex,rowIndex):
  """ __new__(cls: type,columnIndex: int,rowIndex: int) """
  pass
 ColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the column index of the cell that the event occurs for.



Get: ColumnIndex(self: DataGridViewCellEventArgs) -> int



"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the row index of the cell that the event occurs for.



Get: RowIndex(self: DataGridViewCellEventArgs) -> int



"""


