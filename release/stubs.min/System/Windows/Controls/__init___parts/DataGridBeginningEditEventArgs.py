class DataGridBeginningEditEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Controls.DataGrid.BeginningEdit event.

 

 DataGridBeginningEditEventArgs(column: DataGridColumn,row: DataGridRow,editingEventArgs: RoutedEventArgs)
 """
 @staticmethod
 def __new__(self,column,row,editingEventArgs):
  """ __new__(cls: type,column: DataGridColumn,row: DataGridRow,editingEventArgs: RoutedEventArgs) """
  pass
 Cancel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the event should be canceled.



Get: Cancel(self: DataGridBeginningEditEventArgs) -> bool



Set: Cancel(self: DataGridBeginningEditEventArgs)=value

"""

 Column=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column that contains the cell to be edited.



Get: Column(self: DataGridBeginningEditEventArgs) -> DataGridColumn



"""

 EditingEventArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets information about the user gesture that caused the cell to enter edit mode.



Get: EditingEventArgs(self: DataGridBeginningEditEventArgs) -> RoutedEventArgs



"""

 Row=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row that contains the cell to be edited.



Get: Row(self: DataGridBeginningEditEventArgs) -> DataGridRow



"""


