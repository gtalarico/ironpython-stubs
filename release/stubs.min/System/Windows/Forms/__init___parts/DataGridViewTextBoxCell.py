class DataGridViewTextBoxCell(DataGridViewCell,ICloneable,IDisposable):
 """
 Displays editable text information in a System.Windows.Forms.DataGridView control.

 

 DataGridViewTextBoxCell()
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
  Clone(self: DataGridViewTextBoxCell) -> object

  

   Creates an exact copy of this cell.

   Returns: An System.Object that represents the cloned System.Windows.Forms.DataGridViewTextBoxCell.
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
  CreateAccessibilityInstance(self: DataGridViewCell) -> AccessibleObject

  

   Creates a new accessible object for the System.Windows.Forms.DataGridViewCell.

   Returns: A new System.Windows.Forms.DataGridViewCell.DataGridViewCellAccessibleObject for the 

    System.Windows.Forms.DataGridViewCell.
  """
  pass
 def DetachEditingControl(self):
  """ DetachEditingControl(self: DataGridViewTextBoxCell) """
  pass
 def Dispose(self):
  """
  Dispose(self: DataGridViewCell,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.DataGridViewCell and 

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
  GetClipboardContent(self: DataGridViewCell,rowIndex: int,firstCell: bool,lastCell: bool,inFirstRow: bool,inLastRow: bool,format: str) -> object

  

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

   Returns: An System.Object that represents the value of the cell to copy to the 

    System.Windows.Forms.Clipboard.
  """
  pass
 def GetContentBounds(self,rowIndex):
  """
  GetContentBounds(self: DataGridViewTextBoxCell,graphics: Graphics,cellStyle: DataGridViewCellStyle,rowIndex: int) -> Rectangle

  

   graphics: The graphics context for the cell.

   cellStyle: The System.Windows.Forms.DataGridViewCellStyle to be applied to the cell.

   rowIndex: The index of the cell's parent row.

   Returns: The System.Drawing.Rectangle that bounds the cell's contents.
  """
  pass
 def GetErrorIconBounds(self,*args):
  """
  GetErrorIconBounds(self: DataGridViewTextBoxCell,graphics: Graphics,cellStyle: DataGridViewCellStyle,rowIndex: int) -> Rectangle

  

   graphics: The graphics context for the cell.

   cellStyle: The System.Windows.Forms.DataGridViewCellStyle to be applied to the cell.

   rowIndex: The index of the cell's parent row.

   Returns: The System.Drawing.Rectangle that bounds the cell's error icon,if one is displayed; otherwise,

    System.Drawing.Rectangle.Empty.
  """
  pass
 def GetErrorText(self,*args):
  """
  GetErrorText(self: DataGridViewCell,rowIndex: int) -> str

  

   Returns a string that represents the error for the cell.

  

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
 def GetPreferredSize(self,*args):
  """
  GetPreferredSize(self: DataGridViewTextBoxCell,graphics: Graphics,cellStyle: DataGridViewCellStyle,rowIndex: int,constraintSize: Size) -> Size

  

   graphics: The System.Drawing.Graphics used to draw the cell.

   cellStyle: A System.Windows.Forms.DataGridViewCellStyle that represents the style of the cell.

   rowIndex: The zero-based row index of the cell.

   constraintSize: The cell's maximum allowable size.

   Returns: A System.Drawing.Size that represents the preferred size,in pixels,of the cell.
  """
  pass
 def GetSize(self,*args):
  """
  GetSize(self: DataGridViewCell,rowIndex: int) -> Size

  

   Gets the size of the cell.

  

   rowIndex: The index of the cell's parent row.

   Returns: A System.Drawing.Size representing the cell's dimensions.
  """
  pass
 def GetValue(self,*args):
  """
  GetValue(self: DataGridViewCell,rowIndex: int) -> object

  

   Gets the value of the cell.

  

   rowIndex: The index of the cell's parent row.

   Returns: The value contained in the System.Windows.Forms.DataGridViewCell.
  """
  pass
 def InitializeEditingControl(self,rowIndex,initialFormattedValue,dataGridViewCellStyle):
  """
  InitializeEditingControl(self: DataGridViewTextBoxCell,rowIndex: int,initialFormattedValue: object,dataGridViewCellStyle: DataGridViewCellStyle)

   Attaches and initializes the hosted editing control.

  

   rowIndex: The index of the row being edited.

   initialFormattedValue: The initial value to be displayed in the control.

   dataGridViewCellStyle: A cell style that is used to determine the appearance of the hosted control.
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
 def KeyEntersEditMode(self,e):
  """
  KeyEntersEditMode(self: DataGridViewTextBoxCell,e: KeyEventArgs) -> bool

  

   Determines if edit mode should be started based on the given key.

  

   e: A System.Windows.Forms.KeyEventArgs that represents the key that was pressed.

   Returns: true if edit mode should be started; otherwise,false.
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
  MouseDownUnsharesRow(self: DataGridViewCell,e: DataGridViewCellMouseEventArgs) -> bool

  

   Indicates whether a row will be unshared when the user holds down a mouse button while the 

    pointer is on a cell in the row.

  

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
  """
  pass
 def MouseEnterUnsharesRow(self,*args):
  """
  MouseEnterUnsharesRow(self: DataGridViewCell,rowIndex: int) -> bool

  

   Indicates whether a row will be unshared when the mouse pointer moves over a cell in the row.

  

   rowIndex: The index of the cell's parent row.

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
  """
  pass
 def MouseLeaveUnsharesRow(self,*args):
  """
  MouseLeaveUnsharesRow(self: DataGridViewCell,rowIndex: int) -> bool

  

   Indicates whether a row will be unshared when the mouse pointer leaves the row.

  

   rowIndex: The index of the cell's parent row.

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
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
  MouseUpUnsharesRow(self: DataGridViewCell,e: DataGridViewCellMouseEventArgs) -> bool

  

   Indicates whether a row will be unshared when the user releases a mouse button while the pointer 

    is on a cell in the row.

  

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.

   Returns: true if the row will be unshared,otherwise,false. The base 

    System.Windows.Forms.DataGridViewCell class always returns false.
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
  OnEnter(self: DataGridViewTextBoxCell,rowIndex: int,throughMouseClick: bool)

   Called by System.Windows.Forms.DataGridView when the selection cursor moves onto a cell.

  

   rowIndex: The index of the row entered by the mouse.

   throughMouseClick: true if the cell was entered as a result of a mouse click; otherwise,false.
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
  OnLeave(self: DataGridViewTextBoxCell,rowIndex: int,throughMouseClick: bool)

   Called by the System.Windows.Forms.DataGridView when the mouse leaves a cell.

  

   rowIndex: The index of the row the mouse has left.

   throughMouseClick: true if the cell was left as a result of a mouse click; otherwise,false.
  """
  pass
 def OnMouseClick(self,*args):
  """
  OnMouseClick(self: DataGridViewTextBoxCell,e: DataGridViewCellMouseEventArgs)

   Called by System.Windows.Forms.DataGridView when the mouse leaves a cell.

  

   e: An System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
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
  OnMouseDown(self: DataGridViewCell,e: DataGridViewCellMouseEventArgs)

   Called when the user holds down a mouse button while the pointer is on a cell.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
  """
  pass
 def OnMouseEnter(self,*args):
  """
  OnMouseEnter(self: DataGridViewCell,rowIndex: int)

   Called when the mouse pointer moves over a cell.

  

   rowIndex: The index of the cell's parent row.
  """
  pass
 def OnMouseLeave(self,*args):
  """
  OnMouseLeave(self: DataGridViewCell,rowIndex: int)

   Called when the mouse pointer leaves the cell.

  

   rowIndex: The index of the cell's parent row.
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
  OnMouseUp(self: DataGridViewCell,e: DataGridViewCellMouseEventArgs)

   Called when the user releases a mouse button while the pointer is on a cell.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
  """
  pass
 def Paint(self,*args):
  """
  Paint(self: DataGridViewTextBoxCell,graphics: Graphics,clipBounds: Rectangle,cellBounds: Rectangle,rowIndex: int,cellState: DataGridViewElementStates,value: object,formattedValue: object,errorText: str,cellStyle: DataGridViewCellStyle,advancedBorderStyle: DataGridViewAdvancedBorderStyle,paintParts: DataGridViewPaintParts)

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
 def PositionEditingControl(self,setLocation,setSize,cellBounds,cellClip,cellStyle,singleVerticalBorderAdded,singleHorizontalBorderAdded,isFirstDisplayedColumn,isFirstDisplayedRow):
  """
  PositionEditingControl(self: DataGridViewTextBoxCell,setLocation: bool,setSize: bool,cellBounds: Rectangle,cellClip: Rectangle,cellStyle: DataGridViewCellStyle,singleVerticalBorderAdded: bool,singleHorizontalBorderAdded: bool,isFirstDisplayedColumn: bool,isFirstDisplayedRow: bool)

   setLocation: true to have the control placed as specified by the other arguments; false to allow the control 

    to place itself.

  

   setSize: true to specify the size; false to allow the control to size itself.

   cellBounds: A System.Drawing.Rectangle that defines the cell bounds.

   cellClip: The area that will be used to paint the editing control.

   cellStyle: A System.Windows.Forms.DataGridViewCellStyle that represents the style of the cell being edited.

   singleVerticalBorderAdded: true to add a vertical border to the cell; otherwise,false.

   singleHorizontalBorderAdded: true to add a horizontal border to the cell; otherwise,false.

   isFirstDisplayedColumn: true if the hosting cell is in the first visible column; otherwise,false.

   isFirstDisplayedRow: true if the hosting cell is in the first visible row; otherwise,false.
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
  SetValue(self: DataGridViewCell,rowIndex: int,value: object) -> bool

  

   Sets the value of the cell.

  

   rowIndex: The index of the cell's parent row.

   value: The cell value to set.

   Returns: true if the value has been set; otherwise,false.
  """
  pass
 def ToString(self):
  """
  ToString(self: DataGridViewTextBoxCell) -> str

   Returns: A string that represents the current object.
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
 FormattedValueType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of the formatted value associated with the cell.



Get: FormattedValueType(self: DataGridViewTextBoxCell) -> Type



"""

 MaxInputLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum number of characters that can be entered into the text box.



Get: MaxInputLength(self: DataGridViewTextBoxCell) -> int



Set: MaxInputLength(self: DataGridViewTextBoxCell)=value

"""

 ValueType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ValueType(self: DataGridViewTextBoxCell) -> Type



"""


