class DataGridRowEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Controls.DataGrid.LoadingRow and System.Windows.Controls.DataGrid.UnloadingRow events.

 

 DataGridRowEventArgs(row: DataGridRow)
 """
 @staticmethod
 def __new__(self,row):
  """ __new__(cls: type,row: DataGridRow) """
  pass
 Row=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row for which the event occurred.



Get: Row(self: DataGridRowEventArgs) -> DataGridRow



"""


