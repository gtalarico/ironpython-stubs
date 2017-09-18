class DataGridViewColumnDividerDoubleClickEventArgs(HandledMouseEventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.ColumnDividerDoubleClick event of a System.Windows.Forms.DataGridView.

 

 DataGridViewColumnDividerDoubleClickEventArgs(columnIndex: int,e: HandledMouseEventArgs)
 """
 @staticmethod
 def __new__(self,columnIndex,e):
  """ __new__(cls: type,columnIndex: int,e: HandledMouseEventArgs) """
  pass
 ColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The index of the column next to the column divider that was double-clicked.



Get: ColumnIndex(self: DataGridViewColumnDividerDoubleClickEventArgs) -> int



"""


