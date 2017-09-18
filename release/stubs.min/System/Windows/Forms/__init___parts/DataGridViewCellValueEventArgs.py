class DataGridViewCellValueEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.CellValueNeeded and System.Windows.Forms.DataGridView.CellValuePushed events of the System.Windows.Forms.DataGridView control.

 

 DataGridViewCellValueEventArgs(columnIndex: int,rowIndex: int)
 """
 @staticmethod
 def __new__(self,columnIndex,rowIndex):
  """ __new__(cls: type,columnIndex: int,rowIndex: int) """
  pass
 ColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the column index of the cell that the event occurs for.



Get: ColumnIndex(self: DataGridViewCellValueEventArgs) -> int



"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the row index of the cell that the event occurs for.



Get: RowIndex(self: DataGridViewCellValueEventArgs) -> int



"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the cell that the event occurs for.



Get: Value(self: DataGridViewCellValueEventArgs) -> object



Set: Value(self: DataGridViewCellValueEventArgs)=value

"""


