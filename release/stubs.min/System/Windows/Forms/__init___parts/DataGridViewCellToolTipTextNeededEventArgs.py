class DataGridViewCellToolTipTextNeededEventArgs(DataGridViewCellEventArgs):
 """ Provides data for the System.Windows.Forms.DataGridView.CellToolTipTextNeeded event. """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return DataGridViewCellToolTipTextNeededEventArgs()

 ToolTipText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the ToolTip text.

Get: ToolTipText(self: DataGridViewCellToolTipTextNeededEventArgs) -> str

Set: ToolTipText(self: DataGridViewCellToolTipTextNeededEventArgs)=value
"""


