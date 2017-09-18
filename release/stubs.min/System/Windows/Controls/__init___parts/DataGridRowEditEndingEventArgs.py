class DataGridRowEditEndingEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Controls.DataGrid.RowEditEnding event.

 

 DataGridRowEditEndingEventArgs(row: DataGridRow,editAction: DataGridEditAction)
 """
 @staticmethod
 def __new__(self,row,editAction):
  """ __new__(cls: type,row: DataGridRow,editAction: DataGridEditAction) """
  pass
 Cancel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the event should be canceled.



Get: Cancel(self: DataGridRowEditEndingEventArgs) -> bool



Set: Cancel(self: DataGridRowEditEndingEventArgs)=value

"""

 EditAction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the edit was canceled or committed.



Get: EditAction(self: DataGridRowEditEndingEventArgs) -> DataGridEditAction



"""

 Row=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row for which the event occurred.



Get: Row(self: DataGridRowEditEndingEventArgs) -> DataGridRow



"""


