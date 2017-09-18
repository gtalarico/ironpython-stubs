class DataGridViewCellCancelEventArgs(CancelEventArgs):
 """
 Provides data for System.Windows.Forms.DataGridView.CellBeginEdit and System.Windows.Forms.DataGridView.RowValidating events.

 

 DataGridViewCellCancelEventArgs(columnIndex: int,rowIndex: int)
 """
 @staticmethod
 def __new__(self,columnIndex,rowIndex):
  """ __new__(cls: type,columnIndex: int,rowIndex: int) """
  pass
 ColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column index of the cell that the event occurs for.



Get: ColumnIndex(self: DataGridViewCellCancelEventArgs) -> int



"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row index of the cell that the event occurs for.



Get: RowIndex(self: DataGridViewCellCancelEventArgs) -> int



"""


