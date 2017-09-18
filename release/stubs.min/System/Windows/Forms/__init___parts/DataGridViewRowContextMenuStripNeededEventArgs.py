class DataGridViewRowContextMenuStripNeededEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.RowContextMenuStripNeeded event.

 

 DataGridViewRowContextMenuStripNeededEventArgs(rowIndex: int)
 """
 @staticmethod
 def __new__(self,rowIndex):
  """ __new__(cls: type,rowIndex: int) """
  pass
 ContextMenuStrip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the shortcut menu for the row that raised the System.Windows.Forms.DataGridView.RowContextMenuStripNeeded event.



Get: ContextMenuStrip(self: DataGridViewRowContextMenuStripNeededEventArgs) -> ContextMenuStrip



Set: ContextMenuStrip(self: DataGridViewRowContextMenuStripNeededEventArgs)=value

"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the row that is requesting a shortcut menu.



Get: RowIndex(self: DataGridViewRowContextMenuStripNeededEventArgs) -> int



"""


