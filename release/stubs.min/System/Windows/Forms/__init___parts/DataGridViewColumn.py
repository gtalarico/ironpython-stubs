class DataGridViewColumn(DataGridViewBand,ICloneable,IDisposable,IComponent):
 """
 Represents a column in a System.Windows.Forms.DataGridView control.

 

 DataGridViewColumn()

 DataGridViewColumn(cellTemplate: DataGridViewCell)
 """
 def Clone(self):
  """
  Clone(self: DataGridViewColumn) -> object

   Returns: An System.Object that represents the cloned System.Windows.Forms.DataGridViewBand.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: DataGridViewColumn,disposing: bool)

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def GetPreferredWidth(self,autoSizeColumnMode,fixedHeight):
  """
  GetPreferredWidth(self: DataGridViewColumn,autoSizeColumnMode: DataGridViewAutoSizeColumnMode,fixedHeight: bool) -> int

  

   Calculates the ideal width of the column based on the specified criteria.

  

   autoSizeColumnMode: A System.Windows.Forms.DataGridViewAutoSizeColumnMode value that specifies an automatic sizing 

    mode.

  

   fixedHeight: true to calculate the width of the column based on the current row heights; false to calculate 

    the width with the expectation that the row heights will be adjusted.

  

   Returns: The ideal width,in pixels,of the column.
  """
  pass
 def OnDataGridViewChanged(self,*args):
  """
  OnDataGridViewChanged(self: DataGridViewBand)

   Called when the band is associated with a different System.Windows.Forms.DataGridView.
  """
  pass
 def RaiseCellClick(self,*args):
  """
  RaiseCellClick(self: DataGridViewElement,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellClick event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def RaiseCellContentClick(self,*args):
  """
  RaiseCellContentClick(self: DataGridViewElement,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellContentClick event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def RaiseCellContentDoubleClick(self,*args):
  """
  RaiseCellContentDoubleClick(self: DataGridViewElement,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellContentDoubleClick event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def RaiseCellValueChanged(self,*args):
  """
  RaiseCellValueChanged(self: DataGridViewElement,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellValueChanged event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def RaiseDataError(self,*args):
  """
  RaiseDataError(self: DataGridViewElement,e: DataGridViewDataErrorEventArgs)

   Raises the System.Windows.Forms.DataGridView.DataError event.

  

   e: A System.Windows.Forms.DataGridViewDataErrorEventArgs that contains the event data.
  """
  pass
 def RaiseMouseWheel(self,*args):
  """
  RaiseMouseWheel(self: DataGridViewElement,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseWheel event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def ToString(self):
  """
  ToString(self: DataGridViewColumn) -> str

  

   Gets a string that describes the column.

   Returns: A System.String that describes the column.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,cellTemplate=None):
  """
  __new__(cls: type)

  __new__(cls: type,cellTemplate: DataGridViewCell)
  """
  pass
 def __str__(self,*args):
  pass
 AutoSizeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the mode by which the column automatically adjusts its width.



Get: AutoSizeMode(self: DataGridViewColumn) -> DataGridViewAutoSizeColumnMode



Set: AutoSizeMode(self: DataGridViewColumn)=value

"""

 CellTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template used to create new cells.



Get: CellTemplate(self: DataGridViewColumn) -> DataGridViewCell



Set: CellTemplate(self: DataGridViewColumn)=value

"""

 CellType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the run-time type of the cell template.



Get: CellType(self: DataGridViewColumn) -> Type



"""

 ContextMenuStrip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the shortcut menu for the column.



Get: ContextMenuStrip(self: DataGridViewColumn) -> ContextMenuStrip



Set: ContextMenuStrip(self: DataGridViewColumn)=value

"""

 DataPropertyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the data source property or database column to which the System.Windows.Forms.DataGridViewColumn is bound.



Get: DataPropertyName(self: DataGridViewColumn) -> str



Set: DataPropertyName(self: DataGridViewColumn)=value

"""

 DefaultCellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the column's default cell style.



Get: DefaultCellStyle(self: DataGridViewColumn) -> DataGridViewCellStyle



Set: DefaultCellStyle(self: DataGridViewColumn)=value

"""

 DisplayIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the display order of the column relative to the currently displayed columns.



Get: DisplayIndex(self: DataGridViewColumn) -> int



Set: DisplayIndex(self: DataGridViewColumn)=value

"""

 DividerWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width,in pixels,of the column divider.



Get: DividerWidth(self: DataGridViewColumn) -> int



Set: DividerWidth(self: DataGridViewColumn)=value

"""

 FillWeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that represents the width of the column when it is in fill mode relative to the widths of other fill-mode columns in the control.



Get: FillWeight(self: DataGridViewColumn) -> Single



Set: FillWeight(self: DataGridViewColumn)=value

"""

 Frozen=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a column will move when a user scrolls the System.Windows.Forms.DataGridView control horizontally.



Get: Frozen(self: DataGridViewColumn) -> bool



Set: Frozen(self: DataGridViewColumn)=value

"""

 HeaderCell=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Forms.DataGridViewColumnHeaderCell that represents the column header.



Get: HeaderCell(self: DataGridViewColumn) -> DataGridViewColumnHeaderCell



Set: HeaderCell(self: DataGridViewColumn)=value

"""

 HeaderCellCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the header cell of the System.Windows.Forms.DataGridViewBand.



"""

 HeaderText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the caption text on the column's header cell.



Get: HeaderText(self: DataGridViewColumn) -> str



Set: HeaderText(self: DataGridViewColumn)=value

"""

 InheritedAutoSizeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the sizing mode in effect for the column.



Get: InheritedAutoSizeMode(self: DataGridViewColumn) -> DataGridViewAutoSizeColumnMode



"""

 InheritedStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the cell style currently applied to the column.



Get: InheritedStyle(self: DataGridViewColumn) -> DataGridViewCellStyle



"""

 IsDataBound=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the column is bound to a data source.



Get: IsDataBound(self: DataGridViewColumn) -> bool



"""

 IsRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the band represents a row.



"""

 MinimumWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum width,in pixels,of the column.



Get: MinimumWidth(self: DataGridViewColumn) -> int



Set: MinimumWidth(self: DataGridViewColumn)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the column.



Get: Name(self: DataGridViewColumn) -> str



Set: Name(self: DataGridViewColumn)=value

"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the user can edit the column's cells.



Get: ReadOnly(self: DataGridViewColumn) -> bool



Set: ReadOnly(self: DataGridViewColumn)=value

"""

 Resizable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the column is resizable.



Get: Resizable(self: DataGridViewColumn) -> DataGridViewTriState



Set: Resizable(self: DataGridViewColumn)=value

"""

 Site=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the site of the column.



Get: Site(self: DataGridViewColumn) -> ISite



Set: Site(self: DataGridViewColumn)=value

"""

 SortMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the sort mode for the column.



Get: SortMode(self: DataGridViewColumn) -> DataGridViewColumnSortMode



Set: SortMode(self: DataGridViewColumn)=value

"""

 ToolTipText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text used for ToolTips.



Get: ToolTipText(self: DataGridViewColumn) -> str



Set: ToolTipText(self: DataGridViewColumn)=value

"""

 ValueType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the data type of the values in the column's cells.



Get: ValueType(self: DataGridViewColumn) -> Type



Set: ValueType(self: DataGridViewColumn)=value

"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the column is visible.



Get: Visible(self: DataGridViewColumn) -> bool



Set: Visible(self: DataGridViewColumn)=value

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current width of the column.



Get: Width(self: DataGridViewColumn) -> int



Set: Width(self: DataGridViewColumn)=value

"""


 Disposed=None

