class TableLayoutSettings(LayoutSettings,ISerializable):
 """ Collects the characteristics associated with table layouts. """
 def GetCellPosition(self,control):
  """
  GetCellPosition(self: TableLayoutSettings,control: object) -> TableLayoutPanelCellPosition

  

   Gets the System.Windows.Forms.TableLayoutPanelCellPosition that represents the row and the 

    column of the cell.

  

  

   control: A control contained within a cell.

   Returns: A System.Windows.Forms.TableLayoutPanelCellPosition that represents the cell position.
  """
  pass
 def GetColumn(self,control):
  """
  GetColumn(self: TableLayoutSettings,control: object) -> int

  

   Gets the column position of the specified child control.

  

   control: A control contained within a cell.

   Returns: The column position of the specified child control.
  """
  pass
 def GetColumnSpan(self,control):
  """
  GetColumnSpan(self: TableLayoutSettings,control: object) -> int

  

   Gets the number of columns that the cell containing the child control spans.

  

   control: A control contained within a cell.

   Returns: The number of columns that the cell containing the child control spans.
  """
  pass
 def GetRow(self,control):
  """
  GetRow(self: TableLayoutSettings,control: object) -> int

  

   Gets the row position of the specified child control.

  

   control: A control contained within a cell.

   Returns: The row position of the specified child control.
  """
  pass
 def GetRowSpan(self,control):
  """
  GetRowSpan(self: TableLayoutSettings,control: object) -> int

  

   Gets the number of rows that the cell containing the child control spans.

  

   control: A control contained within a cell.

   Returns: The number of rows that the cell containing the child control spans.
  """
  pass
 def SetCellPosition(self,control,cellPosition):
  """
  SetCellPosition(self: TableLayoutSettings,control: object,cellPosition: TableLayoutPanelCellPosition)

   Sets the System.Windows.Forms.TableLayoutPanelCellPosition that represents the row and the 

    column of the cell.

  

  

   control: A control contained within a cell.

   cellPosition: A System.Windows.Forms.TableLayoutPanelCellPosition  that represents the cell position.
  """
  pass
 def SetColumn(self,control,column):
  """
  SetColumn(self: TableLayoutSettings,control: object,column: int)

   Sets the column position for the specified child control.

  

   control: A control contained within a cell.

   column: The column position for the specified child control.
  """
  pass
 def SetColumnSpan(self,control,value):
  """
  SetColumnSpan(self: TableLayoutSettings,control: object,value: int)

   Sets the number of columns that the cell containing the child control spans.

  

   control: A control contained within a cell.

   value: The number of columns that the cell containing the child control spans.
  """
  pass
 def SetRow(self,control,row):
  """
  SetRow(self: TableLayoutSettings,control: object,row: int)

   Sets the row position of the specified child control.

  

   control: A control contained within a cell.

   row: The row position of the specified child control.
  """
  pass
 def SetRowSpan(self,control,value):
  """
  SetRowSpan(self: TableLayoutSettings,control: object,value: int)

   Sets the number of rows that the cell containing the child control spans.

  

   control: A control contained within a cell.

   value: The number of rows that the cell containing the child control spans.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 ColumnCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum number of columns allowed in the table layout.



Get: ColumnCount(self: TableLayoutSettings) -> int



Set: ColumnCount(self: TableLayoutSettings)=value

"""

 ColumnStyles=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of styles used to determine the look and feel of the table layout columns.



Get: ColumnStyles(self: TableLayoutSettings) -> TableLayoutColumnStyleCollection



"""

 GrowStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating how the table layout should expand to accommodate new cells when all existing cells are occupied.



Get: GrowStyle(self: TableLayoutSettings) -> TableLayoutPanelGrowStyle



Set: GrowStyle(self: TableLayoutSettings)=value

"""

 LayoutEngine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current table layout engine.



Get: LayoutEngine(self: TableLayoutSettings) -> LayoutEngine



"""

 RowCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum number of rows allowed in the table layout.



Get: RowCount(self: TableLayoutSettings) -> int



Set: RowCount(self: TableLayoutSettings)=value

"""

 RowStyles=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of styles used to determine the look and feel of the table layout rows.



Get: RowStyles(self: TableLayoutSettings) -> TableLayoutRowStyleCollection



"""


