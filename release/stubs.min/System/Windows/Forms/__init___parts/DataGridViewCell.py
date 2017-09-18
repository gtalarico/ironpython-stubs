class DataGridViewCell(DataGridViewElement,ICloneable,IDisposable):
 """ Represents an individual cell in a System.Windows.Forms.DataGridView control. """
 def AdjustCellBorderStyle(self,dataGridViewAdvancedBorderStyleInput,dataGridViewAdvancedBorderStylePlaceholder,singleVerticalBorderAdded,singleHorizontalBorderAdded,isFirstDisplayedColumn,isFirstDisplayedRow):
  """
  AdjustCellBorderStyle(self: DataGridViewCell,dataGridViewAdvancedBorderStyleInput: DataGridViewAdvancedBorderStyle,dataGridViewAdvancedBorderStylePlaceholder: DataGridViewAdvancedBorderStyle,singleVerticalBorderAdded: bool,singleHorizontalBorderAdded: bool,isFirstDisplayedColumn: bool,isFirstDisplayedRow: bool) -> DataGridViewAdvancedBorderStyle

  

   Modifies the input cell border style according to the specified criteria.

  

   dataGridViewAdvancedBorderStyleInput: A System.Windows.Forms.DataGridViewAdvancedBorderStyle that represents the cell border style to 

    modify.

  

   dataGridViewAdvancedBorderStylePlaceholder: A System.Windows.Forms.DataGridViewAdvancedBorderStyle that is used to store intermediate 

    changes to the cell border style.

  

   singleVerticalBorderAdded: true to add a vertical border to the cell; otherwise,false.

   singleHorizontalBorderAdded: true to add a horizontal border to the cell; otherwise,false.

   isFirstDisplayedColumn: true if the hosting cell is in the first visible column; otherwise,false.

   isFirstDisplayedRow: true if the hosting cell is in the first visible row; otherwise,false.

   Returns: The modified System.Windows.Forms.DataGridViewAdvancedBorderStyle.
  """
  pass
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
  Clone(self: DataGridViewCell) -> object

  

   Creates an exact copy of this cell.

   Returns: An System.Object that represents the cloned System.Windows.Forms.DataGridViewCell.
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
  """
  DetachEditingControl(self: DataGridViewCell)

   Removes the cell's editing control from the System.Windows.Forms.DataGridView.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: DataGridViewCell)

   Releases all resources used by the System.Windows.Forms.DataGridViewCell.
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
  GetContentBounds(self: DataGridViewCell,rowIndex: int) -> Rectangle

  

   Returns the bounding rectangle that encloses the cell's content area using a default 

    System.Drawing.Graphics and cell style currently in effect for the cell.

  

  

   rowIndex: The index of the cell's parent row.

   Returns: The System.Drawing.Rectangle that bounds the cell's contents.
  """
  pass
 def GetEditedFormattedValue(self,rowIndex,context):
  """
  GetEditedFormattedValue(self: DataGridViewCell,rowIndex: int,context: DataGridViewDataErrorContexts) -> object

  

   Returns the current,formatted value of the cell,regardless of whether the cell is in edit mode 

    and the value has not been committed.

  

  

   rowIndex: The row index of the cell.

   context: A bitwise combination of System.Windows.Forms.DataGridViewDataErrorContexts values that 

    specifies the data error context.

  

   Returns: The current,formatted value of the System.Windows.Forms.DataGridViewCell.
  """
  pass
 def GetErrorIconBounds(self,*args):
  """
  GetErrorIconBounds(self: DataGridViewCell,graphics: Graphics,cellStyle: DataGridViewCellStyle,rowIndex: int) -> Rectangle

  

   Returns the bounding rectangle that encloses the cell's error icon,if one is displayed.

  

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
 def GetInheritedContextMenuStrip(self,rowIndex):
  """
  GetInheritedContextMenuStrip(self: DataGridViewCell,rowIndex: int) -> ContextMenuStrip

  

   Gets the inherited shortcut menu for the current cell.

  

   rowIndex: The row index of the current cell.

   Returns: A System.Windows.Forms.ContextMenuStrip if the parent System.Windows.Forms.DataGridView,

    System.Windows.Forms.DataGridViewRow,or System.Windows.Forms.DataGridViewColumn has a 

    System.Windows.Forms.ContextMenuStrip assigned; otherwise,null.
  """
  pass
 def GetInheritedState(self,rowIndex):
  """
  GetInheritedState(self: DataGridViewCell,rowIndex: int) -> DataGridViewElementStates

  

   Returns a value indicating the current state of the cell as inherited from the state of its row 

    and column.

  

  

   rowIndex: The index of the row containing the cell.

   Returns: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values representing the 

    current state of the cell.
  """
  pass
 def GetInheritedStyle(self,inheritedCellStyle,rowIndex,includeColors):
  """
  GetInheritedStyle(self: DataGridViewCell,inheritedCellStyle: DataGridViewCellStyle,rowIndex: int,includeColors: bool) -> DataGridViewCellStyle

  

   Gets the style applied to the cell.

  

   inheritedCellStyle: A System.Windows.Forms.DataGridViewCellStyle to be populated with the inherited cell style.

   rowIndex: The index of the cell's parent row.

   includeColors: true to include inherited colors in the returned cell style; otherwise,false.

   Returns: A System.Windows.Forms.DataGridViewCellStyle that includes the style settings of the cell 

    inherited from the cell's parent row,column,and System.Windows.Forms.DataGridView.
  """
  pass
 def GetPreferredSize(self,*args):
  """
  GetPreferredSize(self: DataGridViewCell,graphics: Graphics,cellStyle: DataGridViewCellStyle,rowIndex: int,constraintSize: Size) -> Size

  

   Calculates the preferred size,in pixels,of the cell.

  

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
  InitializeEditingControl(self: DataGridViewCell,rowIndex: int,initialFormattedValue: object,dataGridViewCellStyle: DataGridViewCellStyle)

   Initializes the control used to edit the cell.

  

   rowIndex: The zero-based row index of the cell's location.

   initialFormattedValue: An System.Object that represents the value displayed by the cell when editing is started.

   dataGridViewCellStyle: A System.Windows.Forms.DataGridViewCellStyle that represents the style of the cell.
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
  KeyEntersEditMode(self: DataGridViewCell,e: KeyEventArgs) -> bool

  

   Determines if edit mode should be started based on the given key.

  

   e: A System.Windows.Forms.KeyEventArgs that represents the key that was pressed.

   Returns: true if edit mode should be started; otherwise,false. The default is false.
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
 @staticmethod
 def MeasureTextHeight(graphics,text,font,maxWidth,flags,widthTruncated=None):
  """
  MeasureTextHeight(graphics: Graphics,text: str,font: Font,maxWidth: int,flags: TextFormatFlags) -> (int,bool)

  

   Gets the height,in pixels,of the specified text,given the specified characteristics. Also 

    indicates whether the required width is greater than the specified maximum width.

  

  

   graphics: The System.Drawing.Graphics used to render the text.

   text: The text to measure.

   font: The System.Drawing.Font applied to the text.

   maxWidth: The maximum width of the text.

   flags: A bitwise combination of System.Windows.Forms.TextFormatFlags  values to apply to the text.

   Returns: The height,in pixels,of the text.

  MeasureTextHeight(graphics: Graphics,text: str,font: Font,maxWidth: int,flags: TextFormatFlags) -> int

  

   Gets the height,in pixels,of the specified text,given the specified characteristics.

  

   graphics: The System.Drawing.Graphics used to render the text.

   text: The text to measure.

   font: The System.Drawing.Font applied to the text.

   maxWidth: The maximum width of the text.

   flags: A bitwise combination of System.Windows.Forms.TextFormatFlags  values to apply to the text.

   Returns: The height,in pixels,of the text.
  """
  pass
 @staticmethod
 def MeasureTextPreferredSize(graphics,text,font,maxRatio,flags):
  """
  MeasureTextPreferredSize(graphics: Graphics,text: str,font: Font,maxRatio: Single,flags: TextFormatFlags) -> Size

  

   Gets the ideal height and width of the specified text given the specified characteristics.

  

   graphics: The System.Drawing.Graphics used to render the text.

   text: The text to measure.

   font: The System.Drawing.Font applied to the text.

   maxRatio: The maximum width-to-height ratio of the block of text.

   flags: A bitwise combination of System.Windows.Forms.TextFormatFlags  values to apply to the text.

   Returns: A System.Drawing.Size representing the preferred height and width of the text.
  """
  pass
 @staticmethod
 def MeasureTextSize(graphics,text,font,flags):
  """
  MeasureTextSize(graphics: Graphics,text: str,font: Font,flags: TextFormatFlags) -> Size

  

   Gets the height and width of the specified text given the specified characteristics.

  

   graphics: The System.Drawing.Graphics used to render the text.

   text: The text to measure.

   font: The System.Drawing.Font applied to the text.

   flags: A bitwise combination of System.Windows.Forms.TextFormatFlags  values to apply to the text.

   Returns: A System.Drawing.Size representing the height and width of the text.
  """
  pass
 @staticmethod
 def MeasureTextWidth(graphics,text,font,maxHeight,flags):
  """
  MeasureTextWidth(graphics: Graphics,text: str,font: Font,maxHeight: int,flags: TextFormatFlags) -> int

  

   Gets the width,in pixels,of the specified text given the specified characteristics.

  

   graphics: The System.Drawing.Graphics used to render the text.

   text: The text to measure.

   font: The System.Drawing.Font applied to the text.

   maxHeight: The maximum height of the text.

   flags: A bitwise combination of System.Windows.Forms.TextFormatFlags  values to apply to the text.

   Returns: The width,in pixels,of the text.
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
  Paint(self: DataGridViewCell,graphics: Graphics,clipBounds: Rectangle,cellBounds: Rectangle,rowIndex: int,cellState: DataGridViewElementStates,value: object,formattedValue: object,errorText: str,cellStyle: DataGridViewCellStyle,advancedBorderStyle: DataGridViewAdvancedBorderStyle,paintParts: DataGridViewPaintParts)

   Paints the current System.Windows.Forms.DataGridViewCell.

  

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
 def ParseFormattedValue(self,formattedValue,cellStyle,formattedValueTypeConverter,valueTypeConverter):
  """
  ParseFormattedValue(self: DataGridViewCell,formattedValue: object,cellStyle: DataGridViewCellStyle,formattedValueTypeConverter: TypeConverter,valueTypeConverter: TypeConverter) -> object

  

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
 def PositionEditingControl(self,setLocation,setSize,cellBounds,cellClip,cellStyle,singleVerticalBorderAdded,singleHorizontalBorderAdded,isFirstDisplayedColumn,isFirstDisplayedRow):
  """
  PositionEditingControl(self: DataGridViewCell,setLocation: bool,setSize: bool,cellBounds: Rectangle,cellClip: Rectangle,cellStyle: DataGridViewCellStyle,singleVerticalBorderAdded: bool,singleHorizontalBorderAdded: bool,isFirstDisplayedColumn: bool,isFirstDisplayedRow: bool)

   Sets the location and size of the editing control hosted by a cell in the 

    System.Windows.Forms.DataGridView control.

  

  

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
 def PositionEditingPanel(self,cellBounds,cellClip,cellStyle,singleVerticalBorderAdded,singleHorizontalBorderAdded,isFirstDisplayedColumn,isFirstDisplayedRow):
  """
  PositionEditingPanel(self: DataGridViewCell,cellBounds: Rectangle,cellClip: Rectangle,cellStyle: DataGridViewCellStyle,singleVerticalBorderAdded: bool,singleHorizontalBorderAdded: bool,isFirstDisplayedColumn: bool,isFirstDisplayedRow: bool) -> Rectangle

  

   Sets the location and size of the editing panel hosted by the cell,and returns the normal 

    bounds of the editing control within the editing panel.

  

  

   cellBounds: A System.Drawing.Rectangle that defines the cell bounds.

   cellClip: The area that will be used to paint the editing panel.

   cellStyle: A System.Windows.Forms.DataGridViewCellStyle that represents the style of the cell being edited.

   singleVerticalBorderAdded: true to add a vertical border to the cell; otherwise,false.

   singleHorizontalBorderAdded: true to add a horizontal border to the cell; otherwise,false.

   isFirstDisplayedColumn: true if the cell is in the first column currently displayed in the control; otherwise,false.

   isFirstDisplayedRow: true if the cell is in the first row currently displayed in the control; otherwise,false.

   Returns: A System.Drawing.Rectangle that represents the normal bounds of the editing control within the 

    editing panel.
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
  ToString(self: DataGridViewCell) -> str

  

   Returns a string that describes the current object.

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
 AccessibilityObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.DataGridViewCell.DataGridViewCellAccessibleObject assigned to the System.Windows.Forms.DataGridViewCell.



Get: AccessibilityObject(self: DataGridViewCell) -> AccessibleObject



"""

 ColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column index for this cell.



Get: ColumnIndex(self: DataGridViewCell) -> int



"""

 ContentBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bounding rectangle that encloses the cell's content area.



Get: ContentBounds(self: DataGridViewCell) -> Rectangle



"""

 ContextMenuStrip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the shortcut menu associated with the cell.



Get: ContextMenuStrip(self: DataGridViewCell) -> ContextMenuStrip



Set: ContextMenuStrip(self: DataGridViewCell)=value

"""

 DefaultNewRowValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default value for a cell in the row for new records.



Get: DefaultNewRowValue(self: DataGridViewCell) -> object



"""

 Displayed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the cell is currently displayed on-screen.



Get: Displayed(self: DataGridViewCell) -> bool



"""

 EditedFormattedValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current,formatted value of the cell,regardless of whether the cell is in edit mode and the value has not been committed.



Get: EditedFormattedValue(self: DataGridViewCell) -> object



"""

 EditType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of the cell's hosted editing control.



Get: EditType(self: DataGridViewCell) -> Type



"""

 ErrorIconBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bounds of the error icon for the cell.



Get: ErrorIconBounds(self: DataGridViewCell) -> Rectangle



"""

 ErrorText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text describing an error condition associated with the cell.



Get: ErrorText(self: DataGridViewCell) -> str



Set: ErrorText(self: DataGridViewCell)=value

"""

 FormattedValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the cell as formatted for display.



Get: FormattedValue(self: DataGridViewCell) -> object



"""

 FormattedValueType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of the formatted value associated with the cell.



Get: FormattedValueType(self: DataGridViewCell) -> Type



"""

 Frozen=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the cell is frozen.



Get: Frozen(self: DataGridViewCell) -> bool



"""

 HasStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.DataGridViewCell.Style property has been set.



Get: HasStyle(self: DataGridViewCell) -> bool



"""

 InheritedState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current state of the cell as inherited from the state of its row and column.



Get: InheritedState(self: DataGridViewCell) -> DataGridViewElementStates



"""

 InheritedStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the style currently applied to the cell.



Get: InheritedStyle(self: DataGridViewCell) -> DataGridViewCellStyle



"""

 IsInEditMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this cell is currently being edited.



Get: IsInEditMode(self: DataGridViewCell) -> bool



"""

 OwningColumn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column that contains this cell.



Get: OwningColumn(self: DataGridViewCell) -> DataGridViewColumn



"""

 OwningRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row that contains this cell.



Get: OwningRow(self: DataGridViewCell) -> DataGridViewRow



"""

 PreferredSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size,in pixels,of a rectangular area into which the cell can fit.



Get: PreferredSize(self: DataGridViewCell) -> Size



"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the cell's data can be edited.



Get: ReadOnly(self: DataGridViewCell) -> bool



Set: ReadOnly(self: DataGridViewCell)=value

"""

 Resizable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the cell can be resized.



Get: Resizable(self: DataGridViewCell) -> bool



"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the cell's parent row.



Get: RowIndex(self: DataGridViewCell) -> int



"""

 Selected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the cell has been selected.



Get: Selected(self: DataGridViewCell) -> bool



Set: Selected(self: DataGridViewCell)=value

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size of the cell.



Get: Size(self: DataGridViewCell) -> Size



"""

 Style=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style for the cell.



Get: Style(self: DataGridViewCell) -> DataGridViewCellStyle



Set: Style(self: DataGridViewCell)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object that contains supplemental data about the cell.



Get: Tag(self: DataGridViewCell) -> object



Set: Tag(self: DataGridViewCell)=value

"""

 ToolTipText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the ToolTip text associated with this cell.



Get: ToolTipText(self: DataGridViewCell) -> str



Set: ToolTipText(self: DataGridViewCell)=value

"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value associated with this cell.



Get: Value(self: DataGridViewCell) -> object



Set: Value(self: DataGridViewCell)=value

"""

 ValueType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the data type of the values in the cell.



Get: ValueType(self: DataGridViewCell) -> Type



Set: ValueType(self: DataGridViewCell)=value

"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the cell is in a row or column that has been hidden.



Get: Visible(self: DataGridViewCell) -> bool



"""


 DataGridViewCellAccessibleObject=None

