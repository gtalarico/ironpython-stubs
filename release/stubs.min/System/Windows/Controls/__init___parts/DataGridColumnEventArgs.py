class DataGridColumnEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Controls.DataGrid.ColumnDisplayIndexChanged and System.Windows.Controls.DataGrid.ColumnReordered events.

 

 DataGridColumnEventArgs(column: DataGridColumn)
 """
 @staticmethod
 def __new__(self,column):
  """ __new__(cls: type,column: DataGridColumn) """
  pass
 Column=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column related to the event.



Get: Column(self: DataGridColumnEventArgs) -> DataGridColumn



"""


