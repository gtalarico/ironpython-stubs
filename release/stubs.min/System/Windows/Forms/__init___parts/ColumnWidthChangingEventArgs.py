class ColumnWidthChangingEventArgs(CancelEventArgs):
 """
 Provides data for the System.Windows.Forms.ListView.ColumnWidthChanging event.

 

 ColumnWidthChangingEventArgs(columnIndex: int,newWidth: int,cancel: bool)

 ColumnWidthChangingEventArgs(columnIndex: int,newWidth: int)
 """
 @staticmethod
 def __new__(self,columnIndex,newWidth,cancel=None):
  """
  __new__(cls: type,columnIndex: int,newWidth: int,cancel: bool)

  __new__(cls: type,columnIndex: int,newWidth: int)
  """
  pass
 ColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the column whose width is changing.



Get: ColumnIndex(self: ColumnWidthChangingEventArgs) -> int



"""

 NewWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the new width for the column.



Get: NewWidth(self: ColumnWidthChangingEventArgs) -> int



Set: NewWidth(self: ColumnWidthChangingEventArgs)=value

"""


