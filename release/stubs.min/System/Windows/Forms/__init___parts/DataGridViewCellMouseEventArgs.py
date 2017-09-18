class DataGridViewCellMouseEventArgs(MouseEventArgs):
 """
 Provides data for mouse events raised by a System.Windows.Forms.DataGridView whenever the mouse is moved within a System.Windows.Forms.DataGridViewCell.

 

 DataGridViewCellMouseEventArgs(columnIndex: int,rowIndex: int,localX: int,localY: int,e: MouseEventArgs)
 """
 @staticmethod
 def __new__(self,columnIndex,rowIndex,localX,localY,e):
  """ __new__(cls: type,columnIndex: int,rowIndex: int,localX: int,localY: int,e: MouseEventArgs) """
  pass
 ColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the zero-based column index of the cell.



Get: ColumnIndex(self: DataGridViewCellMouseEventArgs) -> int



"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the zero-based row index of the cell.



Get: RowIndex(self: DataGridViewCellMouseEventArgs) -> int



"""


