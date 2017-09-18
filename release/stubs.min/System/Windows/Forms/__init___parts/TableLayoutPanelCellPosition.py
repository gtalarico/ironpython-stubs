class TableLayoutPanelCellPosition(object):
 """
 Represents a cell in a System.Windows.Forms.TableLayoutPanel.

 

 TableLayoutPanelCellPosition(column: int,row: int)
 """
 def Equals(self,other):
  """
  Equals(self: TableLayoutPanelCellPosition,other: object) -> bool

  

   Specifies whether this System.Windows.Forms.TableLayoutPanelCellPosition contains the same row 

    and column as the specified System.Windows.Forms.TableLayoutPanelCellPosition.

  

  

   other: The System.Windows.Forms.TableLayoutPanelCellPosition to test.

   Returns: true if other is a System.Windows.Forms.TableLayoutPanelCellPosition and has the same row and 

    column as the specified System.Windows.Forms.TableLayoutPanelCellPosition; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TableLayoutPanelCellPosition) -> int

  

   Returns a hash code for this System.Windows.Forms.TableLayoutPanelCellPosition.

   Returns: An integer value that specifies a hash value for this 

    System.Windows.Forms.TableLayoutPanelCellPosition.
  """
  pass
 def ToString(self):
  """
  ToString(self: TableLayoutPanelCellPosition) -> str

  

   Converts this System.Windows.Forms.TableLayoutPanelCellPosition to a human readable string.

   Returns: A string that represents this System.Windows.Forms.TableLayoutPanelCellPosition.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,column,row):
  """
  __new__(cls: type,column: int,row: int)

  __new__[TableLayoutPanelCellPosition]() -> TableLayoutPanelCellPosition
  """
  pass
 def __ne__(self,*args):
  pass
 Column=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the column number of the current System.Windows.Forms.TableLayoutPanelCellPosition.



Get: Column(self: TableLayoutPanelCellPosition) -> int



Set: Column(self: TableLayoutPanelCellPosition)=value

"""

 Row=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the row number of the current System.Windows.Forms.TableLayoutPanelCellPosition.



Get: Row(self: TableLayoutPanelCellPosition) -> int



Set: Row(self: TableLayoutPanelCellPosition)=value

"""


