class DataGridViewButtonCell(DataGridViewCell, ICloneable, IDisposable):
    """
    Displays a button-like user interface (UI) for use in a System.Windows.Forms.DataGridView control.
    
    DataGridViewButtonCell()
    """
    def BorderWidths(self, *args): #cannot find CLR method
        """
        BorderWidths(self: DataGridViewCell, advancedBorderStyle: DataGridViewAdvancedBorderStyle) -> Rectangle
        
            Returns a System.Drawing.Rectangle that represents the widths of all the cell margins.
        
            advancedBorderStyle: A System.Windows.Forms.DataGridViewAdvancedBorderStyle that the margins are to be calculated for.
            Returns: A System.Drawing.Rectangle that represents the widths of all the cell margins.
        """
        pass

    def ClickUnsharesRow(self, *args): #cannot find CLR method
        """
        ClickUnsharesRow(self: DataGridViewCell, e: DataGridViewCellEventArgs) -> bool
        
            Indicates whether the cell's row will be unshared when the cell is clicked.
        
            e: The System.Windows.Forms.DataGridViewCellEventArgs containing the data passed to the System.Windows.Forms.DataGridViewCell.OnClick(System.Windows.Forms.DataGridViewCellEventArgs) method.
            Returns: true if the row will be unshared, otherwise, false. The base System.Windows.Forms.DataGridViewCell class always returns false.
        """
        pass

    def Clone(self):
        """
        Clone(self: DataGridViewButtonCell) -> object
        
            Creates an exact copy of this cell.
            Returns: An System.Object that represents the cloned System.Windows.Forms.DataGridViewButtonCell.
        """
        pass

    def ContentClickUnsharesRow(self, *args): #cannot find CLR method
        """
        ContentClickUnsharesRow(self: DataGridViewCell, e: DataGridViewCellEventArgs) -> bool
        
            Indicates whether the cell's row will be unshared when the cell's content is clicked.
        
            e: The System.Windows.Forms.DataGridViewCellEventArgs containing the data passed to the System.Windows.Forms.DataGridViewCell.OnContentClick(System.Windows.Forms.DataGridViewCellEventArgs) method.
            Returns: true if the row will be unshared, otherwise, false. The base System.Windows.Forms.DataGridViewCell class always returns false.
        """
        pass

    def ContentDoubleClickUnsharesRow(self, *args): #cannot find CLR method
        """
        ContentDoubleClickUnsharesRow(self: DataGridViewCell, e: DataGridViewCellEventArgs) -> bool
        
            Indicates whether the cell's row will be unshared when the cell's content is double-clicked.
        
            e: The System.Windows.Forms.DataGridViewCellEventArgs containing the data passed to the System.Windows.Forms.DataGridViewCell.OnContentDoubleClick(System.Windows.Forms.DataGridViewCellEventArgs) method.
            Returns: true if the row will be unshared, otherwise, false. The base System.Windows.Forms.DataGridViewCell class always returns false.
        """
        pass

    def CreateAccessibilityInstance(self, *args): #cannot find CLR method
        """
        CreateAccessibilityInstance(self: DataGridViewButtonCell) -> AccessibleObject
        
            Creates a new accessible object for the System.Windows.Forms.DataGridViewButtonCell.
            Returns: A new System.Windows.Forms.DataGridViewButtonCell.DataGridViewButtonCellAccessibleObject for the System.Windows.Forms.DataGridViewButtonCell.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: DataGridViewCell, disposing: bool)
            Releases the unmanaged resources used by the System.Windows.Forms.DataGridViewCell and optionally releases the managed resources.
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def DoubleClickUnsharesRow(self, *args): #cannot find CLR method
        """
        DoubleClickUnsharesRow(self: DataGridViewCell, e: DataGridViewCellEventArgs) -> bool
        
            Indicates whether the cell's row will be unshared when the cell is double-clicked.
        
            e: The System.Windows.Forms.DataGridViewCellEventArgs containing the data passed to the System.Windows.Forms.DataGridViewCell.OnDoubleClick(System.Windows.Forms.DataGridViewCellEventArgs) method.
            Returns: true if the row will be unshared, otherwise, false. The base System.Windows.Forms.DataGridViewCell class always returns false.
        """
        pass

    def EnterUnsharesRow(self, *args): #cannot find CLR method
        """
        EnterUnsharesRow(self: DataGridViewCell, rowIndex: int, throughMouseClick: bool) -> bool
        
            Indicates whether the parent row will be unshared when the focus moves to the cell.
        
            rowIndex: The index of the cell's parent row.
            throughMouseClick: true if a user action moved focus to the cell; false if a programmatic operation moved focus to the cell.
            Returns: true if the row will be unshared; otherwise, false. The base System.Windows.Forms.DataGridViewCell class always returns false.
        """
        pass

    def GetClipboardContent(self, *args): #cannot find CLR method
        """
        GetClipboardContent(self: DataGridViewCell, rowIndex: int, firstCell: bool, lastCell: bool, inFirstRow: bool, inLastRow: bool, format: str) -> object
        
            Retrieves the formatted value of the cell to copy to the System.Windows.Forms.Clipboard.
        
            rowIndex: The zero-based index of the row containing the cell.
            firstCell: true to indicate that the cell is in the first column of the region defined by the selected cells; otherwise, false.
            lastCell: true to indicate that the cell is the last column of the region defined by the selected cells; otherwise, false.
            inFirstRow: true to indicate that the cell is in the first row of the region defined by the selected cells; otherwise, false.
            inLastRow: true to indicate that the cell is in the last row of the region defined by the selected cells; otherwise, false.
            format: The current format string of the cell.
            Returns: An System.Object that represents the value of the cell to copy to the System.Windows.Forms.Clipboard.
        """
        pass

    def GetContentBounds(self, rowIndex):
        """
        GetContentBounds(self: DataGridViewButtonCell, graphics: Graphics, cellStyle: DataGridViewCellStyle, rowIndex: int) -> Rectangle
        
            graphics: The graphics context for the cell.
            cellStyle: The System.Windows.Forms.DataGridViewCellStyle to be applied to the cell.
            rowIndex: The index of the cell's parent row.
            Returns: The System.Drawing.Rectangle that bounds the cell's contents.
        """
        pass

    def GetErrorIconBounds(self, *args): #cannot find CLR method
        """
        GetErrorIconBounds(self: DataGridViewButtonCell, graphics: Graphics, cellStyle: DataGridViewCellStyle, rowIndex: int) -> Rectangle
        
            graphics: The graphics context for the cell.
            cellStyle: The System.Windows.Forms.DataGridViewCellStyle to be applied to the cell.
            rowIndex: The index of the cell's parent row.
            Returns: The System.Drawing.Rectangle that bounds the cell's error icon, if one is displayed; otherwise, System.Drawing.Rectangle.Empty.
        """
        pass

    def GetErrorText(self, *args): #cannot find CLR method
        """
        GetErrorText(self: DataGridViewCell, rowIndex: int) -> str
        
            Returns a string that represents the error for the cell.
        
            rowIndex: The row index of the cell.
            Returns: A string that describes the error for the current System.Windows.Forms.DataGridViewCell.
        """
        pass

    def GetFormattedValue(self, *args): #cannot find CLR method
        """
        GetFormattedValue(self: DataGridViewCell, value: object, rowIndex: int, cellStyle: DataGridViewCellStyle, valueTypeConverter: TypeConverter, formattedValueTypeConverter: TypeConverter, context: DataGridViewDataErrorContexts) -> (object, DataGridViewCellStyle)
        
            Gets the value of the cell as formatted for display.
        
            value: The value to be formatted.
            rowIndex: The index of the cell's parent row.
            cellStyle: The System.Windows.Forms.DataGridViewCellStyle in effect for the cell.
            valueTypeConverter: A System.ComponentModel.TypeConverter associated with the value type that provides custom conversion to the formatted value type, or null if no such custom conversion is needed.
            formattedValueTypeConverter: A System.ComponentModel.TypeConverter associated with the formatted value type that provides custom conversion from the value type, or null if no such custom conversion is needed.
            context: A bitwise combination of System.Windows.Forms.DataGridViewDataErrorContexts values describing the context in which the formatted value is needed.
            Returns: The formatted value of the cell or null if the cell does not belong to a System.Windows.Forms.DataGridView control.
        """
        pass

    def GetPreferredSize(self, *args): #cannot find CLR method
        """
        GetPreferredSize(self: DataGridViewButtonCell, graphics: Graphics, cellStyle: DataGridViewCellStyle, rowIndex: int, constraintSize: Size) -> Size
        
            graphics: The System.Drawing.Graphics used to draw the cell.
            cellStyle: A System.Windows.Forms.DataGridViewCellStyle that represents the style of the cell.
            rowIndex: The zero-based row index of the cell.
            constraintSize: The cell's maximum allowable size.
            Returns: A System.Drawing.Size that represents the preferred size, in pixels, of the cell.
        """
        pass

    def GetSize(self, *args): #cannot find CLR method
        """
        GetSize(self: DataGridViewCell, rowIndex: int) -> Size
        
            Gets the size of the cell.
        
            rowIndex: The index of the cell's parent row.
            Returns: A System.Drawing.Size representing the cell's dimensions.
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: DataGridViewButtonCell, rowIndex: int) -> object
        
            Retrieves the text associated with the button.
        
            rowIndex: The index of the cell's parent row.
            Returns: The value of the System.Windows.Forms.DataGridViewButtonCell or the System.Windows.Forms.DataGridViewButtonColumn.Text value of the owning column if 
             System.Windows.Forms.DataGridViewButtonCell.UseColumnTextForButtonValue is true.
        """
        pass

    def KeyDownUnsharesRow(self, *args): #cannot find CLR method
        """
        KeyDownUnsharesRow(self: DataGridViewButtonCell, e: KeyEventArgs, rowIndex: int) -> bool
        
            Indicates whether a row is unshared if a key is pressed while the focus is on a cell in the row.
        
            e: A System.Windows.Forms.KeyEventArgs that contains the event data.
            rowIndex: The index of the cell's parent row.
            Returns: true if the user pressed the SPACE key without modifier keys; otherwise, false.
        """
        pass

    def KeyPressUnsharesRow(self, *args): #cannot find CLR method
        """
        KeyPressUnsharesRow(self: DataGridViewCell, e: KeyPressEventArgs, rowIndex: int) -> bool
        
            Indicates whether a row will be unshared if a key is pressed while a cell in the row has focus.
        
            e: A System.Windows.Forms.KeyPressEventArgs that contains the event data.
            rowIndex: The index of the cell's parent row.
            Returns: true if the row will be unshared, otherwise, false. The base System.Windows.Forms.DataGridViewCell class always returns false.
        """
        pass

    def KeyUpUnsharesRow(self, *args): #cannot find CLR method
        """
        KeyUpUnsharesRow(self: DataGridViewButtonCell, e: KeyEventArgs, rowIndex: int) -> bool
        
            Indicates whether a row is unshared when a key is released while the focus is on a cell in the row.
        
            e: A System.Windows.Forms.KeyEventArgs that contains the event data.
            rowIndex: The index of the cell's parent row.
            Returns: true if the user released the SPACE key; otherwise, false.
        """
        pass

    def LeaveUnsharesRow(self, *args): #cannot find CLR method
        """
        LeaveUnsharesRow(self: DataGridViewCell, rowIndex: int, throughMouseClick: bool) -> bool
        
            Indicates whether a row will be unshared when the focus leaves a cell in the row.
        
            rowIndex: The index of the cell's parent row.
            throughMouseClick: true if a user action moved focus to the cell; false if a programmatic operation moved focus to the cell.
            Returns: true if the row will be unshared, otherwise, false. The base System.Windows.Forms.DataGridViewCell class always returns false.
        """
        pass

    def MouseClickUnsharesRow(self, *args): #cannot find CLR method
        """
        MouseClickUnsharesRow(self: DataGridViewCell, e: DataGridViewCellMouseEventArgs) -> bool
        
            Indicates whether a row will be unshared if the user clicks a mouse button while the pointer is on a cell in the row.
        
            e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
            Returns: true if the row will be unshared, otherwise, false. The base System.Windows.Forms.DataGridViewCell class always returns false.
        """
        pass

    def MouseDoubleClickUnsharesRow(self, *args): #cannot find CLR method
        """
        MouseDoubleClickUnsharesRow(self: DataGridViewCell, e: DataGridViewCellMouseEventArgs) -> bool
        
            Indicates whether a row will be unshared if the user double-clicks a cell in the row.
        
            e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
            Returns: true if the row will be unshared, otherwise, false. The base System.Windows.Forms.DataGridViewCell class always returns false.
        """
        pass

    def MouseDownUnsharesRow(self, *args): #cannot find CLR method
        """
        MouseDownUnsharesRow(self: DataGridViewButtonCell, e: DataGridViewCellMouseEventArgs) -> bool
        
            Indicates whether a row will be unshared when the mouse button is held down while the pointer is on a cell in the row.
        
            e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
            Returns: true if the user pressed the left mouse button; otherwise, false.
        """
        pass

    def MouseEnterUnsharesRow(self, *args): #cannot find CLR method
        """
        MouseEnterUnsharesRow(self: DataGridViewButtonCell, rowIndex: int) -> bool
        
            Indicates whether a row will be unshared when the mouse pointer moves over a cell in the row.
        
            rowIndex: The row index of the current cell, or -1 if the cell is not owned by a row.
            Returns: true if the cell was the last cell receiving a mouse click; otherwise, false.
        """
        pass

    def MouseLeaveUnsharesRow(self, *args): #cannot find CLR method
        """
        MouseLeaveUnsharesRow(self: DataGridViewButtonCell, rowIndex: int) -> bool
        
            Indicates whether a row will be unshared when the mouse pointer leaves the row.
        
            rowIndex: The row index of the current cell, or -1 if the cell is not owned by a row.
            Returns: true if the button displayed by the cell is in the pressed state; otherwise, false.
        """
        pass

    def MouseMoveUnsharesRow(self, *args): #cannot find CLR method
        """
        MouseMoveUnsharesRow(self: DataGridViewCell, e: DataGridViewCellMouseEventArgs) -> bool
        
            Indicates whether a row will be unshared when the mouse pointer moves over a cell in the row.
        
            e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
            Returns: true if the row will be unshared, otherwise, false. The base System.Windows.Forms.DataGridViewCell class always returns false.
        """
        pass

    def MouseUpUnsharesRow(self, *args): #cannot find CLR method
        """
        MouseUpUnsharesRow(self: DataGridViewButtonCell, e: DataGridViewCellMouseEventArgs) -> bool
        
            Indicates whether a row will be unshared when the mouse button is released while the pointer is on a cell in the row.
        
            e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
            Returns: true if the left mouse button was released; otherwise, false.
        """
        pass

    def OnClick(self, *args): #cannot find CLR method
        """
        OnClick(self: DataGridViewCell, e: DataGridViewCellEventArgs)
            Called when the cell is clicked.
        
            e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
        """
        pass

    def OnContentClick(self, *args): #cannot find CLR method
        """
        OnContentClick(self: DataGridViewCell, e: DataGridViewCellEventArgs)
            Called when the cell's contents are clicked.
        
            e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
        """
        pass

    def OnContentDoubleClick(self, *args): #cannot find CLR method
        """
        OnContentDoubleClick(self: DataGridViewCell, e: DataGridViewCellEventArgs)
            Called when the cell's contents are double-clicked.
        
            e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
        """
        pass

    def OnDataGridViewChanged(self, *args): #cannot find CLR method
        """
        OnDataGridViewChanged(self: DataGridViewCell)
            Called when the System.Windows.Forms.DataGridViewElement.DataGridView property of the cell changes.
        """
        pass

    def OnDoubleClick(self, *args): #cannot find CLR method
        """
        OnDoubleClick(self: DataGridViewCell, e: DataGridViewCellEventArgs)
            Called when the cell is double-clicked.
        
            e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
        """
        pass

    def OnEnter(self, *args): #cannot find CLR method
        """
        OnEnter(self: DataGridViewCell, rowIndex: int, throughMouseClick: bool)
            Called when the focus moves to a cell.
        
            rowIndex: The index of the cell's parent row.
            throughMouseClick: true if a user action moved focus to the cell; false if a programmatic operation moved focus to the cell.
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: DataGridViewButtonCell, e: KeyEventArgs, rowIndex: int)
            Called when a character key is pressed while the focus is on the cell.
        
            e: A System.Windows.Forms.KeyEventArgs that contains the event data.
            rowIndex: The row index of the current cell, or -1 if the cell is not owned by a row.
        """
        pass

    def OnKeyPress(self, *args): #cannot find CLR method
        """
        OnKeyPress(self: DataGridViewCell, e: KeyPressEventArgs, rowIndex: int)
            Called when a key is pressed while the focus is on a cell.
        
            e: A System.Windows.Forms.KeyPressEventArgs that contains the event data.
            rowIndex: The index of the cell's parent row.
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: DataGridViewButtonCell, e: KeyEventArgs, rowIndex: int)
            Called when a character key is released while the focus is on the cell.
        
            e: A System.Windows.Forms.KeyEventArgs that contains the event data
            rowIndex: The row index of the current cell, or -1 if the cell is not owned by a row.
        """
        pass

    def OnLeave(self, *args): #cannot find CLR method
        """
        OnLeave(self: DataGridViewButtonCell, rowIndex: int, throughMouseClick: bool)
            Called when the focus moves from the cell.
        
            rowIndex: The row index of the current cell, or -1 if the cell is not owned by a row.
            throughMouseClick: true if focus left the cell as a result of user mouse click; false if focus left due to a programmatic cell change.
        """
        pass

    def OnMouseClick(self, *args): #cannot find CLR method
        """
        OnMouseClick(self: DataGridViewCell, e: DataGridViewCellMouseEventArgs)
            Called when the user clicks a mouse button while the pointer is on a cell.
        
            e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
        """
        pass

    def OnMouseDoubleClick(self, *args): #cannot find CLR method
        """
        OnMouseDoubleClick(self: DataGridViewCell, e: DataGridViewCellMouseEventArgs)
            Called when the user double-clicks a mouse button while the pointer is on a cell.
        
            e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: DataGridViewButtonCell, e: DataGridViewCellMouseEventArgs)
            Called when the mouse button is held down while the pointer is on the cell.
        
            e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: DataGridViewCell, rowIndex: int)
            Called when the mouse pointer moves over a cell.
        
            rowIndex: The index of the cell's parent row.
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: DataGridViewButtonCell, rowIndex: int)
            Called when the mouse pointer moves out of the cell.
        
            rowIndex: The row index of the current cell, or -1 if the cell is not owned by a row.
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: DataGridViewButtonCell, e: DataGridViewCellMouseEventArgs)
            Called when the mouse pointer moves while it is over the cell.
        
            e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: DataGridViewButtonCell, e: DataGridViewCellMouseEventArgs)
            Called when the mouse button is released while the pointer is on the cell.
        
            e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
        """
        pass

    def Paint(self, *args): #cannot find CLR method
        """
        Paint(self: DataGridViewButtonCell, graphics: Graphics, clipBounds: Rectangle, cellBounds: Rectangle, rowIndex: int, elementState: DataGridViewElementStates, value: object, formattedValue: object, errorText: str, cellStyle: DataGridViewCellStyle, advancedBorderStyle: DataGridViewAdvancedBorderStyle, paintParts: DataGridViewPaintParts)
            Paints the current System.Windows.Forms.DataGridViewButtonCell.
        
            graphics: The System.Drawing.Graphics used to paint the cell.
            clipBounds: A System.Drawing.Rectangle that represents the area of the System.Windows.Forms.DataGridView that needs to be repainted.
            cellBounds: A System.Drawing.Rectangle that contains the bounds of the cell that is being painted.
            rowIndex: The row index of the cell that is being painted.
            elementState: A bitwise combination of System.Windows.Forms.DataGridViewElementStates values that specifies the state of the cell.
            value: The data of the cell that is being painted.
            formattedValue: The formatted data of the cell that is being painted.
            errorText: An error message that is associated with the cell.
            cellStyle: A System.Windows.Forms.DataGridViewCellStyle that contains formatting and style information about the cell.
            advancedBorderStyle: A System.Windows.Forms.DataGridViewAdvancedBorderStyle that contains border styles for the cell that is being painted.
            paintParts: A bitwise combination of the System.Windows.Forms.DataGridViewPaintParts values that specifies which parts of the cell need to be painted.
        """
        pass

    def PaintBorder(self, *args): #cannot find CLR method
        """
        PaintBorder(self: DataGridViewCell, graphics: Graphics, clipBounds: Rectangle, bounds: Rectangle, cellStyle: DataGridViewCellStyle, advancedBorderStyle: DataGridViewAdvancedBorderStyle)
            Paints the border of the current System.Windows.Forms.DataGridViewCell.
        
            graphics: The System.Drawing.Graphics used to paint the border.
            clipBounds: A System.Drawing.Rectangle that represents the area of the System.Windows.Forms.DataGridView that needs to be repainted.
            bounds: A System.Drawing.Rectangle that contains the area of the border that is being painted.
            cellStyle: A System.Windows.Forms.DataGridViewCellStyle that contains formatting and style information about the current cell.
            advancedBorderStyle: A System.Windows.Forms.DataGridViewAdvancedBorderStyle that contains border styles of the border that is being painted.
        """
        pass

    def PaintErrorIcon(self, *args): #cannot find CLR method
        """
        PaintErrorIcon(self: DataGridViewCell, graphics: Graphics, clipBounds: Rectangle, cellValueBounds: Rectangle, errorText: str)
            Paints the error icon of the current System.Windows.Forms.DataGridViewCell.
        
            graphics: The System.Drawing.Graphics used to paint the border.
            clipBounds: A System.Drawing.Rectangle that represents the area of the System.Windows.Forms.DataGridView that needs to be repainted.
            cellValueBounds: The bounding System.Drawing.Rectangle that encloses the cell's content area.
            errorText: An error message that is associated with the cell.
        """
        pass

    def RaiseCellClick(self, *args): #cannot find CLR method
        """
        RaiseCellClick(self: DataGridViewElement, e: DataGridViewCellEventArgs)
            Raises the System.Windows.Forms.DataGridView.CellClick event.
        
            e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
        """
        pass

    def RaiseCellContentClick(self, *args): #cannot find CLR method
        """
        RaiseCellContentClick(self: DataGridViewElement, e: DataGridViewCellEventArgs)
            Raises the System.Windows.Forms.DataGridView.CellContentClick event.
        
            e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
        """
        pass

    def RaiseCellContentDoubleClick(self, *args): #cannot find CLR method
        """
        RaiseCellContentDoubleClick(self: DataGridViewElement, e: DataGridViewCellEventArgs)
            Raises the System.Windows.Forms.DataGridView.CellContentDoubleClick event.
        
            e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
        """
        pass

    def RaiseCellValueChanged(self, *args): #cannot find CLR method
        """
        RaiseCellValueChanged(self: DataGridViewElement, e: DataGridViewCellEventArgs)
            Raises the System.Windows.Forms.DataGridView.CellValueChanged event.
        
            e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
        """
        pass

    def RaiseDataError(self, *args): #cannot find CLR method
        """
        RaiseDataError(self: DataGridViewElement, e: DataGridViewDataErrorEventArgs)
            Raises the System.Windows.Forms.DataGridView.DataError event.
        
            e: A System.Windows.Forms.DataGridViewDataErrorEventArgs that contains the event data.
        """
        pass

    def RaiseMouseWheel(self, *args): #cannot find CLR method
        """
        RaiseMouseWheel(self: DataGridViewElement, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseWheel event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def SetValue(self, *args): #cannot find CLR method
        """
        SetValue(self: DataGridViewCell, rowIndex: int, value: object) -> bool
        
            Sets the value of the cell.
        
            rowIndex: The index of the cell's parent row.
            value: The cell value to set.
            Returns: true if the value has been set; otherwise, false.
        """
        pass

    def ToString(self):
        """
        ToString(self: DataGridViewButtonCell) -> str
        
            Returns the string representation of the cell.
            Returns: A System.String that represents the current cell.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    EditType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the cell's hosted editing control.

Get: EditType(self: DataGridViewButtonCell) -> Type

"""

    FlatStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the style determining the button's appearance.

Get: FlatStyle(self: DataGridViewButtonCell) -> FlatStyle

Set: FlatStyle(self: DataGridViewButtonCell) = value
"""

    FormattedValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FormattedValueType(self: DataGridViewButtonCell) -> Type

"""

    UseColumnTextForButtonValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the owning column's text will appear on the button displayed by the cell.

Get: UseColumnTextForButtonValue(self: DataGridViewButtonCell) -> bool

Set: UseColumnTextForButtonValue(self: DataGridViewButtonCell) = value
"""

    ValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueType(self: DataGridViewButtonCell) -> Type

"""


    DataGridViewButtonCellAccessibleObject = None

