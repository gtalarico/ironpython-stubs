class DataGridViewRow(DataGridViewBand,ICloneable,IDisposable):
 """
 Represents a row in a System.Windows.Forms.DataGridView control.

 

 DataGridViewRow()
 """
 def AdjustRowHeaderBorderStyle(self,dataGridViewAdvancedBorderStyleInput,dataGridViewAdvancedBorderStylePlaceholder,singleVerticalBorderAdded,singleHorizontalBorderAdded,isFirstDisplayedRow,isLastVisibleRow):
  """
  AdjustRowHeaderBorderStyle(self: DataGridViewRow,dataGridViewAdvancedBorderStyleInput: DataGridViewAdvancedBorderStyle,dataGridViewAdvancedBorderStylePlaceholder: DataGridViewAdvancedBorderStyle,singleVerticalBorderAdded: bool,singleHorizontalBorderAdded: bool,isFirstDisplayedRow: bool,isLastVisibleRow: bool) -> DataGridViewAdvancedBorderStyle

  

   Modifies an input row header border style according to the specified criteria.

  

   dataGridViewAdvancedBorderStyleInput: A System.Windows.Forms.DataGridViewAdvancedBorderStyle that represents the row header border 

    style to modify.

  

   dataGridViewAdvancedBorderStylePlaceholder: A System.Windows.Forms.DataGridViewAdvancedBorderStyle that is used to store intermediate 

    changes to the row header border style.

  

   singleVerticalBorderAdded: true to add a single vertical border to the result; otherwise,false.

   singleHorizontalBorderAdded: true to add a single horizontal border to the result; otherwise,false.

   isFirstDisplayedRow: true if the row is the first row displayed in the System.Windows.Forms.DataGridView; otherwise,

    false.

  

   isLastVisibleRow: true if the row is the last row in the System.Windows.Forms.DataGridView that has its 

    System.Windows.Forms.DataGridViewRow.Visible property set to true; otherwise,false.

  

   Returns: A System.Windows.Forms.DataGridViewAdvancedBorderStyle that represents the new border style used.
  """
  pass
 def Clone(self):
  """
  Clone(self: DataGridViewRow) -> object

  

   Creates an exact copy of this row.

   Returns: An System.Object that represents the cloned System.Windows.Forms.DataGridViewRow.
  """
  pass
 def CreateAccessibilityInstance(self,*args):
  """
  CreateAccessibilityInstance(self: DataGridViewRow) -> AccessibleObject

  

   Creates a new accessible object for the System.Windows.Forms.DataGridViewRow.

   Returns: A new System.Windows.Forms.DataGridViewRow.DataGridViewRowAccessibleObject for the 

    System.Windows.Forms.DataGridViewRow.
  """
  pass
 def CreateCells(self,dataGridView,values=None):
  """
  CreateCells(self: DataGridViewRow,dataGridView: DataGridView,*values: Array[object])

   Clears the existing cells and sets their template and values.

  

   dataGridView: A System.Windows.Forms.DataGridView that acts as a template for cell styles.

   values: An array of objects that initialize the reset cells.

  CreateCells(self: DataGridViewRow,dataGridView: DataGridView)

   Clears the existing cells and sets their template according to the supplied 

    System.Windows.Forms.DataGridView template.

  

  

   dataGridView: A System.Windows.Forms.DataGridView that acts as a template for cell styles.
  """
  pass
 def CreateCellsInstance(self,*args):
  """
  CreateCellsInstance(self: DataGridViewRow) -> DataGridViewCellCollection

  

   Constructs a new collection of cells based on this row.

   Returns: The newly created System.Windows.Forms.DataGridViewCellCollection.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: DataGridViewBand,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.DataGridViewBand and 

    optionally releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def DrawFocus(self,*args):
  """
  DrawFocus(self: DataGridViewRow,graphics: Graphics,clipBounds: Rectangle,bounds: Rectangle,rowIndex: int,rowState: DataGridViewElementStates,cellStyle: DataGridViewCellStyle,cellsPaintSelectionBackground: bool)

   Draws a focus rectangle around the specified bounds.

  

   graphics: The System.Drawing.Graphics used to paint the System.Windows.Forms.DataGridViewRow.

   clipBounds: A System.Drawing.Rectangle that represents the area of the System.Windows.Forms.DataGridView 

    that needs to be painted.

  

   bounds: A System.Drawing.Rectangle that contains the bounds of the System.Windows.Forms.DataGridViewRow 

    that is being painted.

  

   rowIndex: The row index of the cell that is being painted.

   rowState: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values that specifies 

    the state of the row.

  

   cellStyle: The System.Windows.Forms.DataGridViewCellStyle used to paint the focus rectangle.

   cellsPaintSelectionBackground: true to use the System.Windows.Forms.DataGridViewCellStyle.SelectionBackColor property of 

    cellStyle as the color of the focus rectangle; false to use the 

    System.Windows.Forms.DataGridViewCellStyle.BackColor property of cellStyle as the color of the 

    focus rectangle.
  """
  pass
 def GetContextMenuStrip(self,rowIndex):
  """
  GetContextMenuStrip(self: DataGridViewRow,rowIndex: int) -> ContextMenuStrip

  

   Gets the shortcut menu for the row.

  

   rowIndex: The index of the current row.

   Returns: A System.Windows.Forms.ContextMenuStrip that belongs to the System.Windows.Forms.DataGridViewRow 

    at the specified index.
  """
  pass
 def GetErrorText(self,rowIndex):
  """
  GetErrorText(self: DataGridViewRow,rowIndex: int) -> str

  

   Gets the error text for the row at the specified index.

  

   rowIndex: The index of the row that contains the error.

   Returns: A string that describes the error of the row at the specified index.
  """
  pass
 def GetPreferredHeight(self,rowIndex,autoSizeRowMode,fixedWidth):
  """
  GetPreferredHeight(self: DataGridViewRow,rowIndex: int,autoSizeRowMode: DataGridViewAutoSizeRowMode,fixedWidth: bool) -> int

  

   Calculates the ideal height of the specified row based on the specified criteria.

  

   rowIndex: The index of the row whose preferred height is calculated.

   autoSizeRowMode: A System.Windows.Forms.DataGridViewAutoSizeRowMode that specifies an automatic sizing mode.

   fixedWidth: true to calculate the preferred height for a fixed cell width; otherwise,false.

   Returns: The ideal height of the row,in pixels.
  """
  pass
 def GetState(self,rowIndex):
  """
  GetState(self: DataGridViewRow,rowIndex: int) -> DataGridViewElementStates

  

   Returns a value indicating the current state of the row.

  

   rowIndex: The index of the row.

   Returns: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values indicating the 

    row state.
  """
  pass
 def OnDataGridViewChanged(self,*args):
  """
  OnDataGridViewChanged(self: DataGridViewBand)

   Called when the band is associated with a different System.Windows.Forms.DataGridView.
  """
  pass
 def Paint(self,*args):
  """
  Paint(self: DataGridViewRow,graphics: Graphics,clipBounds: Rectangle,rowBounds: Rectangle,rowIndex: int,rowState: DataGridViewElementStates,isFirstDisplayedRow: bool,isLastVisibleRow: bool)

   Paints the current row.

  

   graphics: The System.Drawing.Graphics used to paint the System.Windows.Forms.DataGridViewRow.

   clipBounds: A System.Drawing.Rectangle that represents the area of the System.Windows.Forms.DataGridView 

    that needs to be painted.

  

   rowBounds: A System.Drawing.Rectangle that contains the bounds of the System.Windows.Forms.DataGridViewRow 

    that is being painted.

  

   rowIndex: The row index of the cell that is being painted.

   rowState: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values that specifies 

    the state of the row.

  

   isFirstDisplayedRow: true to indicate whether the current row is the first row displayed in the 

    System.Windows.Forms.DataGridView; otherwise,false.

  

   isLastVisibleRow: true to indicate whether the current row is the last row in the 

    System.Windows.Forms.DataGridView that has the System.Windows.Forms.DataGridViewRow.Visible 

    property set to true; otherwise,false.
  """
  pass
 def PaintCells(self,*args):
  """
  PaintCells(self: DataGridViewRow,graphics: Graphics,clipBounds: Rectangle,rowBounds: Rectangle,rowIndex: int,rowState: DataGridViewElementStates,isFirstDisplayedRow: bool,isLastVisibleRow: bool,paintParts: DataGridViewPaintParts)

   Paints the cells in the current row.

  

   graphics: The System.Drawing.Graphics used to paint the System.Windows.Forms.DataGridViewRow.

   clipBounds: A System.Drawing.Rectangle that represents the area of the System.Windows.Forms.DataGridView 

    that needs to be painted.

  

   rowBounds: A System.Drawing.Rectangle that contains the bounds of the System.Windows.Forms.DataGridViewRow 

    that is being painted.

  

   rowIndex: The row index of the cell that is being painted.

   rowState: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values that specifies 

    the state of the row.

  

   isFirstDisplayedRow: true to indicate whether the current row is the first row displayed in the 

    System.Windows.Forms.DataGridView; otherwise,false.

  

   isLastVisibleRow: true to indicate whether the current row is the last row in the 

    System.Windows.Forms.DataGridView that has the System.Windows.Forms.DataGridViewRow.Visible 

    property set to true; otherwise,false.

  

   paintParts: A bitwise combination of System.Windows.Forms.DataGridViewPaintParts values indicating the parts 

    of the cells to paint.
  """
  pass
 def PaintHeader(self,*args):
  """
  PaintHeader(self: DataGridViewRow,graphics: Graphics,clipBounds: Rectangle,rowBounds: Rectangle,rowIndex: int,rowState: DataGridViewElementStates,isFirstDisplayedRow: bool,isLastVisibleRow: bool,paintParts: DataGridViewPaintParts)

   Paints the header cell of the current row.

  

   graphics: The System.Drawing.Graphics used to paint the System.Windows.Forms.DataGridViewRow.

   clipBounds: A System.Drawing.Rectangle that represents the area of the System.Windows.Forms.DataGridView 

    that needs to be painted.

  

   rowBounds: A System.Drawing.Rectangle that contains the bounds of the System.Windows.Forms.DataGridViewRow 

    that is being painted.

  

   rowIndex: The row index of the cell that is being painted.

   rowState: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values that specifies 

    the state of the row.

  

   isFirstDisplayedRow: true to indicate that the current row is the first row displayed in the 

    System.Windows.Forms.DataGridView; otherwise,false.

  

   isLastVisibleRow: true to indicate that the current row is the last row in the System.Windows.Forms.DataGridView 

    that has the System.Windows.Forms.DataGridViewRow.Visible property set to true; otherwise,

    false.

  

   paintParts: A bitwise combination of System.Windows.Forms.DataGridViewPaintParts values indicating the parts 

    of the cells to paint.
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
 def SetValues(self,values):
  """
  SetValues(self: DataGridViewRow,*values: Array[object]) -> bool

  

   Sets the values of the row's cells.

  

   values: One or more objects that represent the cell values in the row.-or-An System.Array of 

    System.Object values.

  

   Returns: true if all values have been set; otherwise,false.
  """
  pass
 def ToString(self):
  """
  ToString(self: DataGridViewRow) -> str

  

   Gets a human-readable string that describes the row.

   Returns: A System.String that describes this row.
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
 def __str__(self,*args):
  pass
 AccessibilityObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.DataGridViewRow.DataGridViewRowAccessibleObject assigned to the System.Windows.Forms.DataGridViewRow.



Get: AccessibilityObject(self: DataGridViewRow) -> AccessibleObject



"""

 Cells=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of cells that populate the row.



Get: Cells(self: DataGridViewRow) -> DataGridViewCellCollection



"""

 ContextMenuStrip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the shortcut menu for the row.



Get: ContextMenuStrip(self: DataGridViewRow) -> ContextMenuStrip



Set: ContextMenuStrip(self: DataGridViewRow)=value

"""

 DataBoundItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the data-bound object that populated the row.



Get: DataBoundItem(self: DataGridViewRow) -> object



"""

 DefaultCellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default styles for the row,which are used to render cells in the row unless the styles are overridden.



Get: DefaultCellStyle(self: DataGridViewRow) -> DataGridViewCellStyle



Set: DefaultCellStyle(self: DataGridViewRow)=value

"""

 Displayed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this row is displayed on the screen.



Get: Displayed(self: DataGridViewRow) -> bool



"""

 DividerHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height,in pixels,of the row divider.



Get: DividerHeight(self: DataGridViewRow) -> int



Set: DividerHeight(self: DataGridViewRow)=value

"""

 ErrorText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the error message text for row-level errors.



Get: ErrorText(self: DataGridViewRow) -> str



Set: ErrorText(self: DataGridViewRow)=value

"""

 Frozen=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the row is frozen.



Get: Frozen(self: DataGridViewRow) -> bool



Set: Frozen(self: DataGridViewRow)=value

"""

 HeaderCell=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the row's header cell.



Get: HeaderCell(self: DataGridViewRow) -> DataGridViewRowHeaderCell



Set: HeaderCell(self: DataGridViewRow)=value

"""

 HeaderCellCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the header cell of the System.Windows.Forms.DataGridViewBand.



"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current height of the row.



Get: Height(self: DataGridViewRow) -> int



Set: Height(self: DataGridViewRow)=value

"""

 InheritedStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the cell style in effect for the row.



Get: InheritedStyle(self: DataGridViewRow) -> DataGridViewCellStyle



"""

 IsNewRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the row is the row for new records.



Get: IsNewRow(self: DataGridViewRow) -> bool



"""

 IsRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the band represents a row.



"""

 MinimumHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum height of the row.



Get: MinimumHeight(self: DataGridViewRow) -> int



Set: MinimumHeight(self: DataGridViewRow)=value

"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the row is read-only.



Get: ReadOnly(self: DataGridViewRow) -> bool



Set: ReadOnly(self: DataGridViewRow)=value

"""

 Resizable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether users can resize the row or indicating that the behavior is inherited from the System.Windows.Forms.DataGridView.AllowUserToResizeRows property.



Get: Resizable(self: DataGridViewRow) -> DataGridViewTriState



Set: Resizable(self: DataGridViewRow)=value

"""

 Selected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the row is selected.



Get: Selected(self: DataGridViewRow) -> bool



Set: Selected(self: DataGridViewRow)=value

"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current state of the row.



Get: State(self: DataGridViewRow) -> DataGridViewElementStates



"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the row is visible.



Get: Visible(self: DataGridViewRow) -> bool



Set: Visible(self: DataGridViewRow)=value

"""


 DataGridViewRowAccessibleObject=None

