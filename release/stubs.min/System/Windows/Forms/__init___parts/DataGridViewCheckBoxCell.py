class DataGridViewCheckBoxCell(DataGridViewCell,ICloneable,IDisposable,IDataGridViewEditingCell):
 """
 Displays a check box user interface (UI) to use in a System.Windows.Forms.DataGridView control.

 

 DataGridViewCheckBoxCell()

 DataGridViewCheckBoxCell(threeState: bool)
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
  Clone(self: DataGridViewCheckBoxCell) -> object

  

   Creates an exact copy of this cell.

   Returns: An System.Object that represents the cloned System.Windows.Forms.DataGridViewCheckBoxCell.
  """
  pass
 def ContentClickUnsharesRow(self,*args):
  """
  ContentClickUnsharesRow(self: DataGridViewCheckBoxCell,e: DataGridViewCellEventArgs) -> bool

  

   Indicates whether the row containing the cell will be unshared when the cell content is clicked.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains data about the mouse click.

   Returns: true if the cell is in edit mode; otherwise,false.
  """
  pass
 def ContentDoubleClickUnsharesRow(self,*args):
  """
  ContentDoubleClickUnsharesRow(self: DataGridViewCheckBoxCell,e: DataGridViewCellEventArgs) -> bool

  

   Indicates whether the row containing the cell will be unshared when the cell content is 

    double-clicked.

  

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains data about the double-click.

   Returns: true if the cell is in edit mode; otherwise,false.
  """
  pass
 def CreateAccessibilityInstance(self,*args):
  """
  CreateAccessibilityInstance(self: DataGridViewCheckBoxCell) -> AccessibleObject

  

   Creates a new accessible object for the System.Windows.Forms.DataGridViewCheckBoxCell.

   Returns: A new System.Windows.Forms.DataGridViewCheckBoxCell.DataGridViewCheckBoxCellAccessibleObject for 

    the System.Windows.Forms.DataGridViewCheckBoxCell.
  """
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
  GetContentBounds(self: DataGridViewCheckBoxCell,graphics: Graphics,cellStyle: DataGridViewCellStyle,rowIndex: int) -> Rectangle

  

   graphics: The graphics context for the cell.

   cellStyle: The System.Windows.Forms.DataGridViewCellStyle to be applied to the cell.

   rowIndex: The index of the cell's parent row.

   Returns: The System.Drawing.Rectangle that bounds the cell's contents.
  """
  pass
 def GetEditingCellFormattedValue(self,context):
  """
  GetEditingCellFormattedValue(self: DataGridViewCheckBoxCell,context: DataGridViewDataErrorContexts) -> object

  

   Gets the formatted value of the cell while it is in edit mode.

  

   context: A bitwise combination of System.Windows.Forms.DataGridViewDataErrorContexts values that 

    describes the context in which any formatting error occurs.

  

   Returns: An System.Object representing the formatted value of the editing cell.
  """
  pass
 def GetErrorIconBounds(self,*args):
  """
  GetErrorIconBounds(self: DataGridViewCheckBoxCell,graphics: Graphics,cellStyle: DataGridViewCellStyle,rowIndex: int) -> Rectangle

  

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
  GetFormattedValue(self: DataGridViewCheckBoxCell,value: object,rowIndex: int,cellStyle: DataGridViewCellStyle,valueTypeConverter: TypeConverter,formattedValueTypeConverter: TypeConverter,context: DataGridViewDataErrorContexts) -> (object,DataGridViewCellStyle)

  

   Gets the formatted value of the cell's data.

  

   value: The value to be formatted.

   rowIndex: The index of the cell's parent row.

   cellStyle: The System.Windows.Forms.DataGridViewCellStyle in effect for the cell.

   valueTypeConverter: A System.ComponentModel.TypeConverter associated with the value type that provides custom 

    conversion to the formatted value type,or null if no such custom conversion is needed.

  

   formattedValueTypeConverter: A System.ComponentModel.TypeConverter associated with the formatted value type that provides 

    custom conversion from the value type,or null if no such custom conversion is needed.

  

   context: A bitwise combination of System.Windows.Forms.DataGridViewDataErrorContexts values describing 

    the context in which the formatted value is needed.

  

   Returns: The value of the cell's data after formatting has been applied or null if the cell is not part 

    of a System.Windows.Forms.DataGridView control.
  """
  pass
 def GetPreferredSize(self,*args):
  """
  GetPreferredSize(self: DataGridViewCheckBoxCell,graphics: Graphics,cellStyle: DataGridViewCellStyle,rowIndex: int,constraintSize: Size) -> Size

  

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
 def KeyDownUnsharesRow(self,*args):
  """
  KeyDownUnsharesRow(self: DataGridViewCheckBoxCell,e: KeyEventArgs,rowIndex: int) -> bool

  

   Indicates whether the row containing the cell is unshared when a key is pressed while the cell 

    has focus.

  

  

   e: A System.Windows.Forms.KeyEventArgs that contains data about the key press.

   rowIndex: The index of the row containing the cell.

   Returns: true if the SPACE key is pressed and the CTRL,ALT,and SHIFT keys are all not pressed; 

    otherwise,false.
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
  KeyUpUnsharesRow(self: DataGridViewCheckBoxCell,e: KeyEventArgs,rowIndex: int) -> bool

  

   Indicates whether the row containing the cell is unshared when a key is released while the cell 

    has focus.

  

  

   e: A System.Windows.Forms.KeyEventArgs that contains data about the key press.

   rowIndex: The index of the row containing the cell.

   Returns: true if the SPACE key is released; otherwise,false.
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
  MouseDownUnsharesRow(self: DataGridViewCheckBoxCell,e: DataGridViewCellMouseEventArgs) -> bool

  

   Indicates whether the row containing the cell will be unshared when the mouse button is pressed 

    while the pointer is over the cell.

  

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains data about the mouse click.

   Returns: Always true.
  """
  pass
 def MouseEnterUnsharesRow(self,*args):
  """
  MouseEnterUnsharesRow(self: DataGridViewCheckBoxCell,rowIndex: int) -> bool

  

   Indicates whether the row containing the cell will be unshared when the mouse pointer moves over 

    the cell.

  

  

   rowIndex: The index of the row containing the cell.

   Returns: true if the cell was the last cell receiving a mouse click; otherwise,false.
  """
  pass
 def MouseLeaveUnsharesRow(self,*args):
  """
  MouseLeaveUnsharesRow(self: DataGridViewCheckBoxCell,rowIndex: int) -> bool

  

   Indicates whether the row containing the cell will be unshared when the mouse pointer leaves the 

    cell.

  

  

   rowIndex: The index of the row containing the cell.

   Returns: true if the button is not in the normal state; false if the button is in the pressed state.
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
  MouseUpUnsharesRow(self: DataGridViewCheckBoxCell,e: DataGridViewCellMouseEventArgs) -> bool

  

   Indicates whether the row containing the cell will be unshared when the mouse button is released 

    while the pointer is over the cell.

  

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains data about the mouse click.

   Returns: Always true.
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
  OnContentClick(self: DataGridViewCheckBoxCell,e: DataGridViewCellEventArgs)

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnContentDoubleClick(self,*args):
  """
  OnContentDoubleClick(self: DataGridViewCheckBoxCell,e: DataGridViewCellEventArgs)

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
  OnKeyDown(self: DataGridViewCheckBoxCell,e: KeyEventArgs,rowIndex: int)

   Called when a character key is pressed while the focus is on a cell.

  

   e: A System.Windows.Forms.KeyEventArgs that contains the event data

   rowIndex: The row index of the current cell,or -1 if the cell is not owned by a row.
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
  OnKeyUp(self: DataGridViewCheckBoxCell,e: KeyEventArgs,rowIndex: int)

   Called when a character key is released while the focus is on a cell.

  

   e: A System.Windows.Forms.KeyEventArgs that contains the event data

   rowIndex: The row index of the current cell,or -1 if the cell is not owned by a row.
  """
  pass
 def OnLeave(self,*args):
  """
  OnLeave(self: DataGridViewCheckBoxCell,rowIndex: int,throughMouseClick: bool)

   Called when the focus moves from a cell.

  

   rowIndex: The row index of the current cell,or -1 if the cell is not owned by a row.

   throughMouseClick: true if the cell was left as a result of user mouse click rather than a programmatic cell 

    change; otherwise,false.
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
  OnMouseDown(self: DataGridViewCheckBoxCell,e: DataGridViewCellMouseEventArgs)

   Called when the mouse button is held down while the pointer is on a cell.

  

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
  OnMouseLeave(self: DataGridViewCheckBoxCell,rowIndex: int)

   Called when the mouse pointer moves from a cell.

  

   rowIndex: The row index of the current cell or -1 if the cell is not owned by a row.
  """
  pass
 def OnMouseMove(self,*args):
  """
  OnMouseMove(self: DataGridViewCheckBoxCell,e: DataGridViewCellMouseEventArgs)

   Called when the mouse pointer moves within a cell.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
  """
  pass
 def OnMouseUp(self,*args):
  """
  OnMouseUp(self: DataGridViewCheckBoxCell,e: DataGridViewCellMouseEventArgs)

   Called when the mouse button is released while the pointer is on a cell.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
  """
  pass
 def Paint(self,*args):
  """
  Paint(self: DataGridViewCheckBoxCell,graphics: Graphics,clipBounds: Rectangle,cellBounds: Rectangle,rowIndex: int,elementState: DataGridViewElementStates,value: object,formattedValue: object,errorText: str,cellStyle: DataGridViewCellStyle,advancedBorderStyle: DataGridViewAdvancedBorderStyle,paintParts: DataGridViewPaintParts)

   Paints the current System.Windows.Forms.DataGridViewCheckBoxCell.

  

   graphics: The System.Drawing.Graphics used to paint the cell.

   clipBounds: A System.Drawing.Rectangle that represents the area of the System.Windows.Forms.DataGridView 

    that needs to be repainted.

  

   cellBounds: A System.Drawing.Rectangle that contains the bounds of the cell that is being painted.

   rowIndex: The row index of the cell that is being painted.

   elementState: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values that specifies 

    the state of the cell.

  

   value: The data of the cell that is being painted.

   formattedValue: The formatted data of the cell that is being painted.

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
 def ParseFormattedValue(self,formattedValue,cellStyle,formattedValueTypeConverter,valueTypeConverter):
  """
  ParseFormattedValue(self: DataGridViewCheckBoxCell,formattedValue: object,cellStyle: DataGridViewCellStyle,formattedValueTypeConverter: TypeConverter,valueTypeConverter: TypeConverter) -> object

  

   Converts a value formatted for display to an actual cell value.

  

   formattedValue: The display value of the cell.

   cellStyle: The System.Windows.Forms.DataGridViewCellStyle in effect for the cell.

   formattedValueTypeConverter: A System.ComponentModel.TypeConverter for the display value type,or null to use the default 

    converter.

  

   valueTypeConverter: A System.ComponentModel.TypeConverter for the cell value type,or null to use the default 

    converter.

  

   Returns: The cell value.
  """
  pass
 def PrepareEditingCellForEdit(self,selectAll):
  """
  PrepareEditingCellForEdit(self: DataGridViewCheckBoxCell,selectAll: bool)

   This method is not meaningful for this type.

  

   selectAll: This parameter is ignored.
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
  ToString(self: DataGridViewCheckBoxCell) -> str

  

   Returns the string representation of the cell.

   Returns: A System.String that represents the current cell.
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
 def __new__(self,threeState=None):
  """
  __new__(cls: type)

  __new__(cls: type,threeState: bool)
  """
  pass
 def __str__(self,*args):
  pass
 EditingCellFormattedValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the formatted value of the control hosted by the cell when it is in edit mode.



Get: EditingCellFormattedValue(self: DataGridViewCheckBoxCell) -> object



Set: EditingCellFormattedValue(self: DataGridViewCheckBoxCell)=value

"""

 EditingCellValueChanged=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a flag indicating that the value has been changed for this cell.



Get: EditingCellValueChanged(self: DataGridViewCheckBoxCell) -> bool



Set: EditingCellValueChanged(self: DataGridViewCheckBoxCell)=value

"""

 EditType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of the cell's hosted editing control.



Get: EditType(self: DataGridViewCheckBoxCell) -> Type



"""

 FalseValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the underlying value corresponding to a cell value of false.



Get: FalseValue(self: DataGridViewCheckBoxCell) -> object



Set: FalseValue(self: DataGridViewCheckBoxCell)=value

"""

 FlatStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the flat style appearance of the check box user interface (UI).



Get: FlatStyle(self: DataGridViewCheckBoxCell) -> FlatStyle



Set: FlatStyle(self: DataGridViewCheckBoxCell)=value

"""

 FormattedValueType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of the cell display value.



Get: FormattedValueType(self: DataGridViewCheckBoxCell) -> Type



"""

 IndeterminateValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the underlying value corresponding to an indeterminate or null cell value.



Get: IndeterminateValue(self: DataGridViewCheckBoxCell) -> object



Set: IndeterminateValue(self: DataGridViewCheckBoxCell)=value

"""

 ThreeState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether ternary mode has been enabled for the hosted check box control.



Get: ThreeState(self: DataGridViewCheckBoxCell) -> bool



Set: ThreeState(self: DataGridViewCheckBoxCell)=value

"""

 TrueValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the underlying value corresponding to a cell value of true.



Get: TrueValue(self: DataGridViewCheckBoxCell) -> object



Set: TrueValue(self: DataGridViewCheckBoxCell)=value

"""

 ValueType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the data type of the values in the cell.



Get: ValueType(self: DataGridViewCheckBoxCell) -> Type



Set: ValueType(self: DataGridViewCheckBoxCell)=value

"""


 DataGridViewCheckBoxCellAccessibleObject=None

