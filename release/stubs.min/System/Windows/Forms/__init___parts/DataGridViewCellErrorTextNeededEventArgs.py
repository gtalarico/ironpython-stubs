class DataGridViewCellErrorTextNeededEventArgs(DataGridViewCellEventArgs):
 """ Provides data for the System.Windows.Forms.DataGridView.CellErrorTextNeeded event of a System.Windows.Forms.DataGridView control. """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return DataGridViewCellErrorTextNeededEventArgs()

 ErrorText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the message that is displayed when the cell is selected.

Get: ErrorText(self: DataGridViewCellErrorTextNeededEventArgs) -> str

Set: ErrorText(self: DataGridViewCellErrorTextNeededEventArgs)=value
"""


