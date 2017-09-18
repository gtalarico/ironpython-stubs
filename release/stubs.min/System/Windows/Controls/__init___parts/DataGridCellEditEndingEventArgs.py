class DataGridCellEditEndingEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Controls.DataGrid.CellEditEnding event.

 

 DataGridCellEditEndingEventArgs(column: DataGridColumn,row: DataGridRow,editingElement: FrameworkElement,editAction: DataGridEditAction)
 """
 @staticmethod
 def __new__(self,column,row,editingElement,editAction):
  """ __new__(cls: type,column: DataGridColumn,row: DataGridRow,editingElement: FrameworkElement,editAction: DataGridEditAction) """
  pass
 Cancel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the event should be canceled.



Get: Cancel(self: DataGridCellEditEndingEventArgs) -> bool



Set: Cancel(self: DataGridCellEditEndingEventArgs)=value

"""

 Column=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column that contains the cell for which the event occurred.



Get: Column(self: DataGridCellEditEndingEventArgs) -> DataGridColumn



"""

 EditAction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the edit was canceled or committed.



Get: EditAction(self: DataGridCellEditEndingEventArgs) -> DataGridEditAction



"""

 EditingElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the element that the cell displays in editing mode.



Get: EditingElement(self: DataGridCellEditEndingEventArgs) -> FrameworkElement



"""

 Row=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row that contains the cell for which the event occurred.



Get: Row(self: DataGridCellEditEndingEventArgs) -> DataGridRow



"""


