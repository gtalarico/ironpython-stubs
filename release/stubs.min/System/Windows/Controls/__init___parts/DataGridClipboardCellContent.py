class DataGridClipboardCellContent(object):
 """
 Encapsulates the value and location of a System.Windows.Controls.DataGrid cell for use when copying content to the Clipboard.

 

 DataGridClipboardCellContent(item: object,column: DataGridColumn,content: object)
 """
 def Equals(self,data):
  """
  Equals(self: DataGridClipboardCellContent,data: object) -> bool

  

   Indicates whether the current and specified System.Windows.Controls.DataGridClipboardCellContent 

    instances are equivalent.

  

  

   data: The System.Windows.Controls.DataGridClipboardCellContent instance to compare with the current 

    System.Windows.Controls.DataGridClipboardCellContent instance.

  

   Returns: true if the current and specified System.Windows.Controls.DataGridClipboardCellContent instances 

    have the same System.Windows.Controls.DataGridClipboardCellContent.Item,

    System.Windows.Controls.DataGridClipboardCellContent.Column,and 

    System.Windows.Controls.DataGridClipboardCellContent.Content property values; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DataGridClipboardCellContent) -> int

  

   Returns the hash code for this System.Windows.Controls.DataGridClipboardCellContent instance.

   Returns: The hash code for this System.Windows.Controls.DataGridClipboardCellContent instance.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,item,column,content):
  """
  __new__(cls: type,item: object,column: DataGridColumn,content: object)

  __new__[DataGridClipboardCellContent]() -> DataGridClipboardCellContent
  """
  pass
 def __ne__(self,*args):
  pass
 Column=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column that contains the cell being copied.



Get: Column(self: DataGridClipboardCellContent) -> DataGridColumn



"""

 Content=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the text value of the cell being copied.



Get: Content(self: DataGridClipboardCellContent) -> object



"""

 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the data item for the row that contains the cell being copied.



Get: Item(self: DataGridClipboardCellContent) -> object



"""


