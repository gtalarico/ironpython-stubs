class ColumnWidthChangedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ListView.ColumnWidthChanged event.

 

 ColumnWidthChangedEventArgs(columnIndex: int)
 """
 @staticmethod
 def __new__(self,columnIndex):
  """ __new__(cls: type,columnIndex: int) """
  pass
 ColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column index for the column whose width is being changed.



Get: ColumnIndex(self: ColumnWidthChangedEventArgs) -> int



"""


