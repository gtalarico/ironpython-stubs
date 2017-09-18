class DataGridCellClipboardEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Controls.DataGridColumn.CopyingCellClipboardContent and System.Windows.Controls.DataGridColumn.PastingCellClipboardContent events.

 

 DataGridCellClipboardEventArgs(item: object,column: DataGridColumn,content: object)
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,item,column,content):
  """ __new__(cls: type,item: object,column: DataGridColumn,content: object) """
  pass
 Column=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column that contains the cell for which the event occurred.



Get: Column(self: DataGridCellClipboardEventArgs) -> DataGridColumn



"""

 Content=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text value of the cell for which the event occurred.



Get: Content(self: DataGridCellClipboardEventArgs) -> object



Set: Content(self: DataGridCellClipboardEventArgs)=value

"""

 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the data item for the row that contains the cell for which the event occurred.



Get: Item(self: DataGridCellClipboardEventArgs) -> object



"""


