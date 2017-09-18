class DataGridRowDetailsEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Controls.DataGrid.LoadingRowDetails,System.Windows.Controls.DataGrid.UnloadingRowDetails,and System.Windows.Controls.DataGrid.RowDetailsVisibilityChanged events.

 

 DataGridRowDetailsEventArgs(row: DataGridRow,detailsElement: FrameworkElement)
 """
 @staticmethod
 def __new__(self,row,detailsElement):
  """ __new__(cls: type,row: DataGridRow,detailsElement: FrameworkElement) """
  pass
 DetailsElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row details section as a framework element.



Get: DetailsElement(self: DataGridRowDetailsEventArgs) -> FrameworkElement



"""

 Row=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row for which the event occurred.



Get: Row(self: DataGridRowDetailsEventArgs) -> DataGridRow



"""


