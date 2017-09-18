class DataGridRowClipboardEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Controls.DataGrid.CopyingRowClipboardContent event.

 

 DataGridRowClipboardEventArgs(item: object,startColumnDisplayIndex: int,endColumnDisplayIndex: int,isColumnHeadersRow: bool)
 """
 def FormatClipboardCellValues(self,format):
  """
  FormatClipboardCellValues(self: DataGridRowClipboardEventArgs,format: str) -> str

  

   Returns the System.Windows.Controls.DataGridRowClipboardEventArgs.ClipboardRowContent values as 

    a string in the specified format.

  

  

   format: The data format in which to serialize the cell values.

   Returns: The formatted string.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,item,startColumnDisplayIndex,endColumnDisplayIndex,isColumnHeadersRow):
  """ __new__(cls: type,item: object,startColumnDisplayIndex: int,endColumnDisplayIndex: int,isColumnHeadersRow: bool) """
  pass
 ClipboardRowContent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a list of System.Windows.Controls.DataGridClipboardCellContent values that represent the text values of the cells being copied.



Get: ClipboardRowContent(self: DataGridRowClipboardEventArgs) -> List[DataGridClipboardCellContent]



"""

 EndColumnDisplayIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Controls.DataGridColumn.DisplayIndex value of the column that contains the last selected cell in the row.



Get: EndColumnDisplayIndex(self: DataGridRowClipboardEventArgs) -> int



"""

 IsColumnHeadersRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the row for which the event occurred represents the column headers.



Get: IsColumnHeadersRow(self: DataGridRowClipboardEventArgs) -> bool



"""

 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the data item for the row for which the event occurred.



Get: Item(self: DataGridRowClipboardEventArgs) -> object



"""

 StartColumnDisplayIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Controls.DataGridColumn.DisplayIndex value of the column that contains the first selected cell in the row.



Get: StartColumnDisplayIndex(self: DataGridRowClipboardEventArgs) -> int



"""


