class DataGridViewRowsAddedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.RowsAdded event.

 

 DataGridViewRowsAddedEventArgs(rowIndex: int,rowCount: int)
 """
 @staticmethod
 def __new__(self,rowIndex,rowCount):
  """ __new__(cls: type,rowIndex: int,rowCount: int) """
  pass
 RowCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of rows that have been added.



Get: RowCount(self: DataGridViewRowsAddedEventArgs) -> int



"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the first added row.



Get: RowIndex(self: DataGridViewRowsAddedEventArgs) -> int



"""


