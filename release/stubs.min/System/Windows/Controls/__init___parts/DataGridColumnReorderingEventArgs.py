class DataGridColumnReorderingEventArgs(DataGridColumnEventArgs):
 """
 Provides data for the System.Windows.Controls.DataGrid.ColumnReordering event.

 

 DataGridColumnReorderingEventArgs(dataGridColumn: DataGridColumn)
 """
 @staticmethod
 def __new__(self,dataGridColumn):
  """ __new__(cls: type,dataGridColumn: DataGridColumn) """
  pass
 Cancel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the reordering operation is stopped before completion.



Get: Cancel(self: DataGridColumnReorderingEventArgs) -> bool



Set: Cancel(self: DataGridColumnReorderingEventArgs)=value

"""

 DragIndicator=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the control that is used to display the visual indicator of the header for the column that is being dragged.



Get: DragIndicator(self: DataGridColumnReorderingEventArgs) -> Control



Set: DragIndicator(self: DataGridColumnReorderingEventArgs)=value

"""

 DropLocationIndicator=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the control that is used to display the visual indicator of the current drop location during a column drag operation.



Get: DropLocationIndicator(self: DataGridColumnReorderingEventArgs) -> Control



Set: DropLocationIndicator(self: DataGridColumnReorderingEventArgs)=value

"""


