class DataGridViewRowsRemovedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.RowsRemoved event.
 
 DataGridViewRowsRemovedEventArgs(rowIndex: int,rowCount: int)
 """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return DataGridViewRowsRemovedEventArgs()

 @staticmethod
 def __new__(self,rowIndex,rowCount):
  """ __new__(cls: type,rowIndex: int,rowCount: int) """
  pass
 RowCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of rows that were deleted.

Get: RowCount(self: DataGridViewRowsRemovedEventArgs) -> int

"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the zero-based index of the row deleted,or the first deleted row if multiple rows were deleted.

Get: RowIndex(self: DataGridViewRowsRemovedEventArgs) -> int

"""


