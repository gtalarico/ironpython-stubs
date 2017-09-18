class DataGridViewEditingControlShowingEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.EditingControlShowing event.

 

 DataGridViewEditingControlShowingEventArgs(control: Control,cellStyle: DataGridViewCellStyle)
 """
 @staticmethod
 def __new__(self,control,cellStyle):
  """ __new__(cls: type,control: Control,cellStyle: DataGridViewCellStyle) """
  pass
 CellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the cell style of the edited cell.



Get: CellStyle(self: DataGridViewEditingControlShowingEventArgs) -> DataGridViewCellStyle



Set: CellStyle(self: DataGridViewEditingControlShowingEventArgs)=value

"""

 Control=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The control shown to the user for editing the selected cell's value.



Get: Control(self: DataGridViewEditingControlShowingEventArgs) -> Control



"""


