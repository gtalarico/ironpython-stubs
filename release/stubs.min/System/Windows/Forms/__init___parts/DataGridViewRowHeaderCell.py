class DataGridViewRowHeaderCell(DataGridViewHeaderCell,ICloneable,IDisposable):
 """
 Represents a row header of a System.Windows.Forms.DataGridView control.

 

 DataGridViewRowHeaderCell()
 """
 def BorderWidths(self,*args):
  """
  BorderWidths(self: DataGridViewCell,advancedBorderStyle: DataGridViewAdvancedBorderStyle) -> Rectangle

  

   Returns a System.Drawing.Rectangle that represents the widths of all the cell margins.

  

   advancedBorderStyle: A System.Windows.Forms.DataGridViewAdvancedBorderStyle that the margins are to be calculated for.

   Returns: A System.Drawing.Rectangle that represents the widths of all the cell margins.
  """
  pass
 def ClickUnsharesRow(self,*args):
  """
  ClickUnsharesRow(self: DataGridViewCell,e: DataGridViewCellEventArgs) -> bool

  

   Indicates whether the cell's row will be unshared when the cell is clicked.

  

   e: The System.Windows.Forms.DataGridViewCellEventArgs containing the data passed to the 

    System.Windows.Forms.DataGridViewCell.OnClick(System.Windows.Forms.DataGridViewCellEventArgs) 

    method.

  

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
  """
  pass
 def Clone(self):
  """
  Clone(self: DataGridViewRowHeaderCell) -> object

   Returns: An System.Object that represents the cloned System.Windows.Forms.DataGridViewHeaderCell.
  """
  pass
 def ContentClickUnsharesRow(self,*args):
  """
  ContentClickUnsharesRow(self: DataGridViewCell,e: DataGridViewCellEventArgs) -> bool

  

   Indicates whether the cell's row will be unshared when the cell's content is clicked.

  

   e: The System.Windows.Forms.DataGridViewCellEventArgs containing the data passed to the 

    System.Windows.Forms.DataGridViewCell.OnContentClick(System.Windows.Forms.DataGridViewCellEventAr

    gs) method.

  

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
  """
  pass
 def ContentDoubleClickUnsharesRow(self,*args):
  """
  ContentDoubleClickUnsharesRow(self: DataGridViewCell,e: DataGridViewCellEventArgs) -> bool

  

   Indicates whether the cell's row will be unshared when the cell's content is double-clicked.

  

   e: The System.Windows.Forms.DataGridViewCellEventArgs containing the data passed to the 

    System.Windows.Forms.DataGridViewCell.OnContentDoubleClick(System.Windows.Forms.DataGridViewCellE

    ventArgs) method.

  

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
  """
  pass
 def CreateAccessibilityInstance(self,*args):
  """
  CreateAccessibilityInstance(self: DataGridViewRowHeaderCell) -> AccessibleObject

  

   Creates a new accessible object for the System.Windows.Forms.DataGridViewRowHeaderCell.

   Returns: A new System.Windows.Forms.DataGridViewRowHeaderCell.DataGridViewRowHeaderCellAccessibleObject 

    for the System.Windows.Forms.DataGridViewRowHeaderCell.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: DataGridViewHeaderCell,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.DataGridViewHeaderCell and 

    optionally releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def DoubleClickUnsharesRow(self,*args):
  """
  DoubleClickUnsharesRow(self: DataGridViewCell,e: DataGridViewCellEventArgs) -> bool

  

   Indicates whether the cell's row will be unshared when the cell is double-clicked.

  

   e: The System.Windows.Forms.DataGridViewCellEventArgs containing the data passed to the 

    System.Windows.Forms.DataGridViewCell.OnDoubleClick(System.Windows.Forms.DataGridViewCellEventArg

    s) method.

  

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
  """
  pass
 def EnterUnsharesRow(self,*args):
  """
  EnterUnsharesRow(self: DataGridViewCell,rowIndex: int,throughMouseClick: bool) -> bool

  

   Indicates whether the parent row will be unshared when the focus moves to the cell.

  

   rowIndex: The index of the cell's parent row.

   throughMouseClick: true if a user action moved focus to the cell; false if a programmatic operation moved focus to 

    the cell.

  

   Returns: true if the row will be unshared; otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
  """
  pass
 def GetClipboardContent(self,*args):
  """
  GetClipboardContent(self: DataGridViewRowHeaderCell,rowIndex: int,firstCell: bool,lastCell: bool,inFirstRow: bool,inLastRow: bool,format: str) -> object

  

   Retrieves the formatted value of the cell to copy to the System.Windows.Forms.Clipboard.

  

   rowIndex: The zero-based index of the row containing the cell.

   firstCell: true to indicate that the cell is in the first column of the region defined by the selected 

    cells; otherwise,false.

  

   lastCell: true to indicate that the cell is the last column of the region defined by the selected cells; 

    otherwise,false.

  

   inFirstRow: true to indicate that the cell is in the first row of the region defined by the selected cells; 

    otherwise,false.

  

   inLastRow: true to indicate that the cell is in the last row of the region defined by the selected cells; 

    otherwise,false.

  

   format: The current format string of the cell.

   Returns: A System.Object that represents the value of the cell to copy to the 

    System.Windows.Forms.Clipboard.
  """
  pass
 def GetContentBounds(self,rowIndex):
  """
  GetContentBounds(self: DataGridViewRowHeaderCell,graphics: Graphics,cellStyle: DataGridViewCellStyle,rowIndex: int) -> Rectangle

  

   graphics: The graphics context for the cell.

   cellStyle: The System.Windows.Forms.DataGridViewCellStyle to be applied to the cell.

   rowIndex: The index of the cell's parent row.

   Returns: The System.Drawing.Rectangle that bounds the cell's contents.
  """
  pass
 def GetErrorIconBounds(self,*args):
  """
  GetErrorIconBounds(self: DataGridViewRowHeaderCell,graphics: Graphics,cellStyle: DataGridViewCellStyle,rowIndex: int) -> Rectangle

  

   graphics: The graphics context for the cell.

   cellStyle: The System.Windows.Forms.DataGridViewCellStyle to be applied to the cell.

   rowIndex: The index of the cell's parent row.

   Returns: The System.Drawing.Rectangle that bounds the cell's error icon,if one is displayed; otherwise,

    System.Drawing.Rectangle.Empty.
  """
  pass
 def GetErrorText(self,*args):
  """
  GetErrorText(self: DataGridViewRowHeaderCell,rowIndex: int) -> str

  

   rowIndex: The row index of the cell.

   Returns: A string that describes the error for the current System.Windows.Forms.DataGridViewCell.
  """
  pass
 def GetFormattedValue(self,*args):
  """
  GetFormattedValue(self: DataGridViewCell,value: object,rowIndex: int,cellStyle: DataGridViewCellStyle,valueTypeConverter: TypeConverter,formattedValueTypeConverter: TypeConverter,context: DataGridViewDataErrorContexts) -> (object,DataGridViewCellStyle)

  

   Gets the value of the cell as formatted for display.

  

   value: The value to be formatted.

   rowIndex: The index of the cell's parent row.

   cellStyle: The System.Windows.Forms.DataGridViewCellStyle in effect for the cell.

   valueTypeConverter: A System.ComponentModel.TypeConverter associated with the value type that provides custom 

    conversion to the formatted value type,or null if no such custom conversion is needed.

  

   formattedValueTypeConverter: A System.ComponentModel.TypeConverter associated with the formatted value type that provides 

    custom conversion from the value type,or null if no such custom conversion is needed.

  

   context: A bitwise combination of System.Windows.Forms.DataGridViewDataErrorContexts values describing 

    the context in which the formatted value is needed.

  

   Returns: The formatted value of the cell or null if the cell does not belong to a 

    System.Windows.Forms.DataGridView control.
  """
  pass
 def GetInheritedContextMenuStrip(self,rowIndex):
  """
  GetInheritedContextMenuStrip(self: DataGridViewRowHeaderCell,rowIndex: int) -> ContextMenuStrip

  

   Retrieves the inherited shortcut menu for the specified row.

  

   rowIndex: The index of the row to get the System.Windows.Forms.ContextMenuStrip of. The index must be -1 

    to indicate the row of column headers.

  

   Returns: The System.Windows.Forms.ContextMenuStrip of the row if one exists; otherwise,the 

    System.Windows.Forms.ContextMenuStrip inherited from System.Windows.Forms.DataGridView.
  """
  pass
 def GetInheritedStyle(self,inheritedCellStyle,rowIndex,includeColors):
  """
  GetInheritedStyle(self: DataGridViewRowHeaderCell,inheritedCellStyle: DataGridViewCellStyle,rowIndex: int,includeColors: bool) -> DataGridViewCellStyle

  

   inheritedCellStyle: A System.Windows.Forms.DataGridViewCellStyle to be populated with the inherited cell style.

   rowIndex: The index of the cell's parent row.

   includeColors: true to include inherited colors in the returned cell style; otherwise,false.

   Returns: A System.Windows.Forms.DataGridViewCellStyle that includes the style settings of the cell 

    inherited from the cell's parent row,column,and System.Windows.Forms.DataGridView.
  """
  pass
 def GetPreferredSize(self,*args):
  """
  GetPreferredSize(self: DataGridViewRowHeaderCell,graphics: Graphics,cellStyle: DataGridViewCellStyle,rowIndex: int,constraintSize: Size) -> Size

  

   graphics: The System.Drawing.Graphics used to draw the cell.

   cellStyle: A System.Windows.Forms.DataGridViewCellStyle that represents the style of the cell.

   rowIndex: The zero-based row index of the cell.

   constraintSize: The cell's maximum allowable size.

   Returns: A System.Drawing.Size that represents the preferred size,in pixels,of the cell.
  """
  pass
 def GetSize(self,*args):
  """
  GetSize(self: DataGridViewHeaderCell,rowIndex: int) -> Size

  

   Gets the size of the cell.

  

   rowIndex: The row index of the header cell.

   Returns: A System.Drawing.Size that represents the size of the header cell.
  """
  pass
 def GetValue(self,*args):
  """
  GetValue(self: DataGridViewRowHeaderCell,rowIndex: int) -> object

  

   Gets the value of the cell.

  

   rowIndex: The index of the cell's parent row.

   Returns: The value contained in the System.Windows.Forms.DataGridViewRowHeaderCell.
  """
  pass
 def KeyDownUnsharesRow(self,*args):
  """
  KeyDownUnsharesRow(self: DataGridViewCell,e: KeyEventArgs,rowIndex: int) -> bool

  

   Indicates whether the parent row is unshared if the user presses a key while the focus is on the 

    cell.

  

  

   e: A System.Windows.Forms.KeyEventArgs that contains the event data.

   rowIndex: The index of the cell's parent row.

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
  """
  pass
 def KeyPressUnsharesRow(self,*args):
  """
  KeyPressUnsharesRow(self: DataGridViewCell,e: KeyPressEventArgs,rowIndex: int) -> bool

  

   Indicates whether a row will be unshared if a key is pressed while a cell in the row has focus.

  

   e: A System.Windows.Forms.KeyPressEventArgs that contains the event data.

   rowIndex: The index of the cell's parent row.

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
  """
  pass
 def KeyUpUnsharesRow(self,*args):
  """
  KeyUpUnsharesRow(self: DataGridViewCell,e: KeyEventArgs,rowIndex: int) -> bool

  

   Indicates whether the parent row is unshared when the user releases a key while the focus is on 

    the cell.

  

  

   e: A System.Windows.Forms.KeyEventArgs that contains the event data.

   rowIndex: The index of the cell's parent row.

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
  """
  pass
 def LeaveUnsharesRow(self,*args):
  """
  LeaveUnsharesRow(self: DataGridViewCell,rowIndex: int,throughMouseClick: bool) -> bool

  

   Indicates whether a row will be unshared when the focus leaves a cell in the row.

  

   rowIndex: The index of the cell's parent row.

   throughMouseClick: true if a user action moved focus to the cell; false if a programmatic operation moved focus to 

    the cell.

  

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
  """
  pass
 def MouseClickUnsharesRow(self,*args):
  """
  MouseClickUnsharesRow(self: DataGridViewCell,e: DataGridViewCellMouseEventArgs) -> bool

  

   Indicates whether a row will be unshared if the user clicks a mouse button while the pointer is 

    on a cell in the row.

  

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
  """
  pass
 def MouseDoubleClickUnsharesRow(self,*args):
  """
  MouseDoubleClickUnsharesRow(self: DataGridViewCell,e: DataGridViewCellMouseEventArgs) -> bool

  

   Indicates whether a row will be unshared if the user double-clicks a cell in the row.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
  """
  pass
 def MouseDownUnsharesRow(self,*args):
  """
  MouseDownUnsharesRow(self: DataGridViewHeaderCell,e: DataGridViewCellMouseEventArgs) -> bool

  

   Indicates whether a row will be unshared when the mouse button is held down while the pointer is 

    on a cell in the row.

  

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains information about the mouse 

    position.

  

   Returns: true if the user clicks with the left mouse button,visual styles are enabled,and the 

    System.Windows.Forms.DataGridView.EnableHeadersVisualStyles property is true; otherwise,false.
  """
  pass
 def MouseEnterUnsharesRow(self,*args):
  """
  MouseEnterUnsharesRow(self: DataGridViewHeaderCell,rowIndex: int) -> bool

  

   Indicates whether a row will be unshared when the mouse pointer moves over a cell in the row.

  

   rowIndex: The index of the row that the mouse pointer entered.

   Returns: true if visual styles are enabled,and the 

    System.Windows.Forms.DataGridView.EnableHeadersVisualStyles property is true; otherwise,false.
  """
  pass
 def MouseLeaveUnsharesRow(self,*args):
  """
  MouseLeaveUnsharesRow(self: DataGridViewHeaderCell,rowIndex: int) -> bool

  

   Indicates whether a row will be unshared when the mouse pointer leaves the row.

  

   rowIndex: The index of the row that the mouse pointer left.

   Returns: true if the System.Windows.Forms.DataGridViewHeaderCell.ButtonState property value is not 

    System.Windows.Forms.ButtonState.Normal,visual styles are enabled,and the 

    System.Windows.Forms.DataGridView.EnableHeadersVisualStyles property is true; otherwise,false.
  """
  pass
 def MouseMoveUnsharesRow(self,*args):
  """
  MouseMoveUnsharesRow(self: DataGridViewCell,e: DataGridViewCellMouseEventArgs) -> bool

  

   Indicates whether a row will be unshared when the mouse pointer moves over a cell in the row.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
  """
  pass
 def MouseUpUnsharesRow(self,*args):
  """
  MouseUpUnsharesRow(self: DataGridViewHeaderCell,e: DataGridViewCellMouseEventArgs) -> bool

  

   Indicates whether a row will be unshared when the mouse button is released while the pointer is 

    on a cell in the row.

  

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains information about the mouse 

    position.

  

   Returns: true if the left mouse button was released,visual styles are enabled,and the 

    System.Windows.Forms.DataGridView.EnableHeadersVisualStyles property is true; otherwise,false.
  """
  pass
 def OnClick(self,*args):
  """
  OnClick(self: DataGridViewCell,e: DataGridViewCellEventArgs)

   Called when the cell is clicked.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnContentClick(self,*args):
  """
  OnContentClick(self: DataGridViewCell,e: DataGridViewCellEventArgs)

   Called when the cell's contents are clicked.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnContentDoubleClick(self,*args):
  """
  OnContentDoubleClick(self: DataGridViewCell,e: DataGridViewCellEventArgs)

   Called when the cell's contents are double-clicked.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnDataGridViewChanged(self,*args):
  """
  OnDataGridViewChanged(self: DataGridViewCell)

   Called when the System.Windows.Forms.DataGridViewElement.DataGridView property of the cell 

    changes.
  """
  pass
 def OnDoubleClick(self,*args):
  """
  OnDoubleClick(self: DataGridViewCell,e: DataGridViewCellEventArgs)

   Called when the cell is double-clicked.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnEnter(self,*args):
  """
  OnEnter(self: DataGridViewCell,rowIndex: int,throughMouseClick: bool)

   Called when the focus moves to a cell.

  

   rowIndex: The index of the cell's parent row.

   throughMouseClick: true if a user action moved focus to the cell; false if a programmatic operation moved focus to 

    the cell.
  """
  pass
 def OnKeyDown(self,*args):
  """
  OnKeyDown(self: DataGridViewCell,e: KeyEventArgs,rowIndex: int)

   Called when a character key is pressed while the focus is on a cell.

  

   e: A System.Windows.Forms.KeyEventArgs that contains the event data.

   rowIndex: The index of the cell's parent row.
  """
  pass
 def OnKeyPress(self,*args):
  """
  OnKeyPress(self: DataGridViewCell,e: KeyPressEventArgs,rowIndex: int)

   Called when a key is pressed while the focus is on a cell.

  

   e: A System.Windows.Forms.KeyPressEventArgs that contains the event data.

   rowIndex: The index of the cell's parent row.
  """
  pass
 def OnKeyUp(self,*args):
  """
  OnKeyUp(self: DataGridViewCell,e: KeyEventArgs,rowIndex: int)

   Called when a character key is released while the focus is on a cell.

  

   e: A System.Windows.Forms.KeyEventArgs that contains the event data.

   rowIndex: The index of the cell's parent row.
  """
  pass
 def OnLeave(self,*args):
  """
  OnLeave(self: DataGridViewCell,rowIndex: int,throughMouseClick: bool)

   Called when the focus moves from a cell.

  

   rowIndex: The index of the cell's parent row.

   throughMouseClick: true if a user action moved focus from the cell; false if a programmatic operation moved focus 

    from the cell.
  """
  pass
 def OnMouseClick(self,*args):
  """
  OnMouseClick(self: DataGridViewCell,e: DataGridViewCellMouseEventArgs)

   Called when the user clicks a mouse button while the pointer is on a cell.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
  """
  pass
 def OnMouseDoubleClick(self,*args):
  """
  OnMouseDoubleClick(self: DataGridViewCell,e: DataGridViewCellMouseEventArgs)

   Called when the user double-clicks a mouse button while the pointer is on a cell.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
  """
  pass
 def OnMouseDown(self,*args):
  """
  OnMouseDown(self: DataGridViewHeaderCell,e: DataGridViewCellMouseEventArgs)

   Called when the mouse button is held down while the pointer is on a cell.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains information about the mouse 

    position.
  """
  pass
 def OnMouseEnter(self,*args):
  """
  OnMouseEnter(self: DataGridViewHeaderCell,rowIndex: int)

   Called when the mouse pointer enters the cell.

  

   rowIndex: The index of the row containing the cell.
  """
  pass
 def OnMouseLeave(self,*args):
  """
  OnMouseLeave(self: DataGridViewHeaderCell,rowIndex: int)

   Called when the mouse pointer leaves the cell.

  

   rowIndex: The index of the row containing the cell.
  """
  pass
 def OnMouseMove(self,*args):
  """
  OnMouseMove(self: DataGridViewCell,e: DataGridViewCellMouseEventArgs)

   Called when the mouse pointer moves within a cell.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
  """
  pass
 def OnMouseUp(self,*args):
  """
  OnMouseUp(self: DataGridViewHeaderCell,e: DataGridViewCellMouseEventArgs)

   Called when the mouse button is released while the pointer is over the cell.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains information about the mouse 

    position.
  """
  pass
 def Paint(self,*args):
  """
  Paint(self: DataGridViewRowHeaderCell,graphics: Graphics,clipBounds: Rectangle,cellBounds: Rectangle,rowIndex: int,cellState: DataGridViewElementStates,value: object,formattedValue: object,errorText: str,cellStyle: DataGridViewCellStyle,advancedBorderStyle: DataGridViewAdvancedBorderStyle,paintParts: DataGridViewPaintParts)

   Paints the current System.Windows.Forms.DataGridViewRowHeaderCell.

  

   graphics: The System.Drawing.Graphics used to paint the System.Windows.Forms.DataGridViewCell.

   clipBounds: A System.Drawing.Rectangle that represents the area of the System.Windows.Forms.DataGridView 

    that needs to be repainted.

  

   cellBounds: A System.Drawing.Rectangle that contains the bounds of the System.Windows.Forms.DataGridViewCell 

    that is being painted.

  

   rowIndex: The row index of the cell that is being painted.

   cellState: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values that specifies 

    the state of the cell.

  

   value: The data of the System.Windows.Forms.DataGridViewCell that is being painted.

   formattedValue: The formatted data of the System.Windows.Forms.DataGridViewCell that is being painted.

   errorText: An error message that is associated with the cell.

   cellStyle: A System.Windows.Forms.DataGridViewCellStyle that contains formatting and style information 

    about the cell.

  

   advancedBorderStyle: A System.Windows.Forms.DataGridViewAdvancedBorderStyle that contains border styles for the cell 

    that is being painted.

  

   paintParts: A bitwise combination of the System.Windows.Forms.DataGridViewPaintParts values that specifies 

    which parts of the cell need to be painted.
  """
  pass
 def PaintBorder(self,*args):
  """
  PaintBorder(self: DataGridViewCell,graphics: Graphics,clipBounds: Rectangle,bounds: Rectangle,cellStyle: DataGridViewCellStyle,advancedBorderStyle: DataGridViewAdvancedBorderStyle)

   Paints the border of the current System.Windows.Forms.DataGridViewCell.

  

   graphics: The System.Drawing.Graphics used to paint the border.

   clipBounds: A System.Drawing.Rectangle that represents the area of the System.Windows.Forms.DataGridView 

    that needs to be repainted.

  

   bounds: A System.Drawing.Rectangle that contains the area of the border that is being painted.

   cellStyle: A System.Windows.Forms.DataGridViewCellStyle that contains formatting and style information 

    about the current cell.

  

   advancedBorderStyle: A System.Windows.Forms.DataGridViewAdvancedBorderStyle that contains border styles of the border 

    that is being painted.
  """
  pass
 def PaintErrorIcon(self,*args):
  """
  PaintErrorIcon(self: DataGridViewCell,graphics: Graphics,clipBounds: Rectangle,cellValueBounds: Rectangle,errorText: str)

   Paints the error icon of the current System.Windows.Forms.DataGridViewCell.

  

   graphics: The System.Drawing.Graphics used to paint the border.

   clipBounds: A System.Drawing.Rectangle that represents the area of the System.Windows.Forms.DataGridView 

    that needs to be repainted.

  

   cellValueBounds: The bounding System.Drawing.Rectangle that encloses the cell's content area.

   errorText: An error message that is associated with the cell.
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
 def SetValue(self,*args):
  """
  SetValue(self: DataGridViewRowHeaderCell,rowIndex: int,value: object) -> bool

  

   rowIndex: The index of the cell's parent row.

   value: The cell value to set.

   Returns: true if the value has been set; otherwise,false.
  """
  pass
 def ToString(self):
  """
  ToString(self: DataGridViewRowHeaderCell) -> str

  

   Returns the string representation of the cell.

   Returns: A string that represents the current cell.
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
 ButtonState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the buttonlike visual state of the header cell.



"""


 DataGridViewRowHeaderCellAccessibleObject=None

