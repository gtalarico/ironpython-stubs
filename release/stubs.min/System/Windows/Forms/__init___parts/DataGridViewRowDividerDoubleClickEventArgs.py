class DataGridViewRowDividerDoubleClickEventArgs(HandledMouseEventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.RowDividerDoubleClick event of a System.Windows.Forms.DataGridView.

 

 DataGridViewRowDividerDoubleClickEventArgs(rowIndex: int,e: HandledMouseEventArgs)
 """
 @staticmethod
 def __new__(self,rowIndex,e):
  """ __new__(cls: type,rowIndex: int,e: HandledMouseEventArgs) """
  pass
 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The index of the row above the row divider that was double-clicked.



Get: RowIndex(self: DataGridViewRowDividerDoubleClickEventArgs) -> int



"""


