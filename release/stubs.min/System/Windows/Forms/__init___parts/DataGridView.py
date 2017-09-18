class DataGridView(Control,IComponent,IDisposable,IOleControl,IOleObject,IOleInPlaceObject,IOleInPlaceActiveObject,IOleWindow,IViewObject,IViewObject2,IPersist,IPersistStreamInit,IPersistPropertyBag,IPersistStorage,IQuickActivate,ISupportOleDropSource,IDropTarget,ISynchronizeInvoke,IWin32Window,IArrangedElement,IBindableComponent,ISupportInitialize):
 """
 Displays data in a customizable grid.

 

 DataGridView()
 """
 def AccessibilityNotifyClients(self,*args):
  """
  AccessibilityNotifyClients(self: Control,accEvent: AccessibleEvents,objectID: int,childID: int)

   Notifies the accessibility client applications of the specified 

    System.Windows.Forms.AccessibleEvents for the specified child control .

  

  

   accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications of.

   objectID: The identifier of the System.Windows.Forms.AccessibleObject.

   childID: The child System.Windows.Forms.Control to notify of the accessible event.

  AccessibilityNotifyClients(self: Control,accEvent: AccessibleEvents,childID: int)

   Notifies the accessibility client applications of the specified 

    System.Windows.Forms.AccessibleEvents for the specified child control.

  

  

   accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications of.

   childID: The child System.Windows.Forms.Control to notify of the accessible event.
  """
  pass
 def AccessibilityNotifyCurrentCellChanged(self,*args):
  """
  AccessibilityNotifyCurrentCellChanged(self: DataGridView,cellAddress: Point)

   Notifies the accessible client applications when a new cell becomes the current cell.

  

   cellAddress: A System.Drawing.Point indicating the row and column indexes of the new current cell.
  """
  pass
 def AdjustColumnHeaderBorderStyle(self,dataGridViewAdvancedBorderStyleInput,dataGridViewAdvancedBorderStylePlaceholder,isFirstDisplayedColumn,isLastVisibleColumn):
  """
  AdjustColumnHeaderBorderStyle(self: DataGridView,dataGridViewAdvancedBorderStyleInput: DataGridViewAdvancedBorderStyle,dataGridViewAdvancedBorderStylePlaceholder: DataGridViewAdvancedBorderStyle,isFirstDisplayedColumn: bool,isLastVisibleColumn: bool) -> DataGridViewAdvancedBorderStyle

  

   Adjusts the System.Windows.Forms.DataGridViewAdvancedBorderStyle for a column header cell of a 

    System.Windows.Forms.DataGridView that is currently being painted.

  

  

   dataGridViewAdvancedBorderStyleInput: A System.Windows.Forms.DataGridViewAdvancedBorderStyle that that represents the column header 

    border style to modify.

  

   dataGridViewAdvancedBorderStylePlaceholder: A System.Windows.Forms.DataGridViewAdvancedBorderStyle that is used to store intermediate 

    changes to the column header border style.

  

   isFirstDisplayedColumn: true to indicate that the System.Windows.Forms.DataGridViewCell that is currently being painted 

    is in the first column displayed on the System.Windows.Forms.DataGridView; otherwise,false.

  

   isLastVisibleColumn: true to indicate that the System.Windows.Forms.DataGridViewCell that is currently being painted 

    is in the last column in the System.Windows.Forms.DataGridView that has the 

    System.Windows.Forms.DataGridViewColumn.Visible property set to true; otherwise,false.

  

   Returns: A System.Windows.Forms.DataGridViewAdvancedBorderStyle that represents the border style for the 

    current column header.
  """
  pass
 def AreAllCellsSelected(self,includeInvisibleCells):
  """
  AreAllCellsSelected(self: DataGridView,includeInvisibleCells: bool) -> bool

  

   Returns a value indicating whether all the System.Windows.Forms.DataGridView cells are currently 

    selected.

  

  

   includeInvisibleCells: true to include the rows and columns with System.Windows.Forms.DataGridViewBand.Visible property 

    values of false; otherwise,false.

  

   Returns: true if all cells (or all visible cells) are selected or if there are no cells (or no visible 

    cells); otherwise,false.
  """
  pass
 def AutoResizeColumn(self,columnIndex,autoSizeColumnMode=None):
  """
  AutoResizeColumn(self: DataGridView,columnIndex: int,autoSizeColumnMode: DataGridViewAutoSizeColumnMode)

   Adjusts the width of the specified column using the specified size mode.

  

   columnIndex: The index of the column to resize.

   autoSizeColumnMode: One of the System.Windows.Forms.DataGridViewAutoSizeColumnMode values.

  AutoResizeColumn(self: DataGridView,columnIndex: int)

   Adjusts the width of the specified column to fit the contents of all its cells,including the 

    header cell.

  

  

   columnIndex: The index of the column to resize.
  """
  pass
 def AutoResizeColumnHeadersHeight(self,columnIndex=None):
  """
  AutoResizeColumnHeadersHeight(self: DataGridView,columnIndex: int)

   Adjusts the height of the column headers based on changes to the contents of the header in the 

    specified column.

  

  

   columnIndex: The index of the column containing the header with the changed content.

  AutoResizeColumnHeadersHeight(self: DataGridView)

   Adjusts the height of the column headers to fit the contents of the largest column header.
  """
  pass
 def AutoResizeColumns(self,autoSizeColumnsMode=None):
  """
  AutoResizeColumns(self: DataGridView,autoSizeColumnsMode: DataGridViewAutoSizeColumnsMode)

   Adjusts the width of all columns using the specified size mode.

  

   autoSizeColumnsMode: One of the System.Windows.Forms.DataGridViewAutoSizeColumnsMode values.

  AutoResizeColumns(self: DataGridView)

   Adjusts the width of all columns to fit the contents of all their cells,including the header 

    cells.
  """
  pass
 def AutoResizeRow(self,rowIndex,autoSizeRowMode=None):
  """
  AutoResizeRow(self: DataGridView,rowIndex: int,autoSizeRowMode: DataGridViewAutoSizeRowMode)

   Adjusts the height of the specified row using the specified size mode.

  

   rowIndex: The index of the row to resize.

   autoSizeRowMode: One of the System.Windows.Forms.DataGridViewAutoSizeRowMode values.

  AutoResizeRow(self: DataGridView,rowIndex: int)

   Adjusts the height of the specified row to fit the contents of all its cells including the 

    header cell.

  

  

   rowIndex: The index of the row to resize.
  """
  pass
 def AutoResizeRowHeadersWidth(self,*__args):
  """
  AutoResizeRowHeadersWidth(self: DataGridView,rowIndex: int,rowHeadersWidthSizeMode: DataGridViewRowHeadersWidthSizeMode)

   Adjusts the width of the row headers based on changes to the contents of the header in the 

    specified row and using the specified size mode.

  

  

   rowIndex: The index of the row header with the changed content.

   rowHeadersWidthSizeMode: One of the System.Windows.Forms.DataGridViewRowHeadersWidthSizeMode values.

  AutoResizeRowHeadersWidth(self: DataGridView,rowHeadersWidthSizeMode: DataGridViewRowHeadersWidthSizeMode)

   Adjusts the width of the row headers using the specified size mode.

  

   rowHeadersWidthSizeMode: One of the System.Windows.Forms.DataGridViewRowHeadersWidthSizeMode values.
  """
  pass
 def AutoResizeRows(self,autoSizeRowsMode=None):
  """
  AutoResizeRows(self: DataGridView,autoSizeRowsMode: DataGridViewAutoSizeRowsMode)

   Adjusts the heights of the rows using the specified size mode value.

  

   autoSizeRowsMode: One of the System.Windows.Forms.DataGridViewAutoSizeRowsMode values.

  AutoResizeRows(self: DataGridView)

   Adjusts the heights of all rows to fit the contents of all their cells,including the header 

    cells.
  """
  pass
 def BeginEdit(self,selectAll):
  """
  BeginEdit(self: DataGridView,selectAll: bool) -> bool

  

   Puts the current cell in edit mode.

  

   selectAll: true to select all the cell's contents; false to not select any contents.

   Returns: true if the current cell is already in edit mode or successfully enters edit mode; otherwise,

    false.
  """
  pass
 def CancelEdit(self):
  """
  CancelEdit(self: DataGridView) -> bool

  

   Cancels edit mode for the currently selected cell and discards any changes.

   Returns: true if the cancel was successful; otherwise,false.
  """
  pass
 def ClearSelection(self):
  """
  ClearSelection(self: DataGridView)

   Clears the current selection by unselecting all selected cells.
  """
  pass
 def CommitEdit(self,context):
  """
  CommitEdit(self: DataGridView,context: DataGridViewDataErrorContexts) -> bool

  

   Commits changes in the current cell to the data cache without ending edit mode.

  

   context: A bitwise combination of System.Windows.Forms.DataGridViewDataErrorContexts values that 

    specifies the context in which an error can occur.

  

   Returns: true if the changes were committed; otherwise false.
  """
  pass
 def CreateAccessibilityInstance(self,*args):
  """
  CreateAccessibilityInstance(self: DataGridView) -> AccessibleObject

  

   Creates a new accessible object for the System.Windows.Forms.DataGridView.

   Returns: A new System.Windows.Forms.DataGridView.DataGridViewAccessibleObject for the 

    System.Windows.Forms.DataGridView.
  """
  pass
 def CreateColumnsInstance(self,*args):
  """
  CreateColumnsInstance(self: DataGridView) -> DataGridViewColumnCollection

  

   Creates and returns a new System.Windows.Forms.DataGridViewColumnCollection.

   Returns: An empty System.Windows.Forms.DataGridViewColumnCollection.
  """
  pass
 def CreateControlsInstance(self,*args):
  """
  CreateControlsInstance(self: DataGridView) -> ControlCollection

  

   Creates and returns a new System.Windows.Forms.Control.ControlCollection that can be cast to 

    type System.Windows.Forms.DataGridView.DataGridViewControlCollection.

  

   Returns: An empty System.Windows.Forms.Control.ControlCollection.
  """
  pass
 def CreateHandle(self,*args):
  """
  CreateHandle(self: Control)

   Creates a handle for the control.
  """
  pass
 def CreateRowsInstance(self,*args):
  """
  CreateRowsInstance(self: DataGridView) -> DataGridViewRowCollection

  

   Creates and returns a new System.Windows.Forms.DataGridViewRowCollection.

   Returns: An empty System.Windows.Forms.DataGridViewRowCollection.
  """
  pass
 def DefWndProc(self,*args):
  """
  DefWndProc(self: Control,m: Message) -> Message

  

   Sends the specified message to the default window procedure.

  

   m: The Windows System.Windows.Forms.Message to process.
  """
  pass
 def DestroyHandle(self,*args):
  """
  DestroyHandle(self: Control)

   Destroys the handle associated with the control.
  """
  pass
 def DisplayedColumnCount(self,includePartialColumns):
  """
  DisplayedColumnCount(self: DataGridView,includePartialColumns: bool) -> int

  

   Returns the number of columns displayed to the user.

  

   includePartialColumns: true to include partial columns in the displayed column count; otherwise,false.

   Returns: The number of columns displayed to the user.
  """
  pass
 def DisplayedRowCount(self,includePartialRow):
  """
  DisplayedRowCount(self: DataGridView,includePartialRow: bool) -> int

  

   Returns the number of rows displayed to the user.

  

   includePartialRow: true to include partial rows in the displayed row count; otherwise,false.

   Returns: The number of rows displayed to the user.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: DataGridView,disposing: bool)

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def EndEdit(self,context=None):
  """
  EndEdit(self: DataGridView,context: DataGridViewDataErrorContexts) -> bool

  

   Commits and ends the edit operation on the current cell using the specified error context.

  

   context: A bitwise combination of System.Windows.Forms.DataGridViewDataErrorContexts values that 

    specifies the context in which an error can occur.

  

   Returns: true if the edit operation is committed and ended; otherwise,false.

  EndEdit(self: DataGridView) -> bool

  

   Commits and ends the edit operation on the current cell using the default error context.

   Returns: true if the edit operation is committed and ended; otherwise,false.
  """
  pass
 def GetAccessibilityObjectById(self,*args):
  """
  GetAccessibilityObjectById(self: DataGridView,objectId: int) -> AccessibleObject

  

   objectId: An Int32 that identifies the System.Windows.Forms.AccessibleObject to retrieve.

   Returns: An System.Windows.Forms.AccessibleObject.
  """
  pass
 def GetAutoSizeMode(self,*args):
  """
  GetAutoSizeMode(self: Control) -> AutoSizeMode

  

   Retrieves a value indicating how a control will behave when its 

    System.Windows.Forms.Control.AutoSize property is enabled.

  

   Returns: One of the System.Windows.Forms.AutoSizeMode values.
  """
  pass
 def GetCellCount(self,includeFilter):
  """
  GetCellCount(self: DataGridView,includeFilter: DataGridViewElementStates) -> int

  

   Gets the number of cells that satisfy the provided filter.

  

   includeFilter: A bitwise combination of the System.Windows.Forms.DataGridViewElementStates values specifying 

    the cells to count.

  

   Returns: The number of cells that match the includeFilter parameter.
  """
  pass
 def GetCellDisplayRectangle(self,columnIndex,rowIndex,cutOverflow):
  """
  GetCellDisplayRectangle(self: DataGridView,columnIndex: int,rowIndex: int,cutOverflow: bool) -> Rectangle

  

   Returns the rectangle that represents the display area for a cell.

  

   columnIndex: The column index for the desired cell.

   rowIndex: The row index for the desired cell.

   cutOverflow: true to return the displayed portion of the cell only; false to return the entire cell bounds.

   Returns: The System.Drawing.Rectangle that represents the display rectangle of the cell.
  """
  pass
 def GetClipboardContent(self):
  """
  GetClipboardContent(self: DataGridView) -> DataObject

  

   Retrieves the formatted values that represent the contents of the selected cells for copying to 

    the System.Windows.Forms.Clipboard.

  

   Returns: A System.Windows.Forms.DataObject that represents the contents of the selected cells.
  """
  pass
 def GetColumnDisplayRectangle(self,columnIndex,cutOverflow):
  """
  GetColumnDisplayRectangle(self: DataGridView,columnIndex: int,cutOverflow: bool) -> Rectangle

  

   Returns the rectangle that represents the display area for a column,as determined by the column 

    index.

  

  

   columnIndex: The column index for the desired cell.

   cutOverflow: true to return the column rectangle visible in the System.Windows.Forms.DataGridView bounds; 

    false to return the entire column rectangle.

  

   Returns: The System.Drawing.Rectangle that represents the display rectangle of the column.
  """
  pass
 def GetRowDisplayRectangle(self,rowIndex,cutOverflow):
  """
  GetRowDisplayRectangle(self: DataGridView,rowIndex: int,cutOverflow: bool) -> Rectangle

  

   Returns the rectangle that represents the display area for a row,as determined by the row index.

  

   rowIndex: The row index for the desired cell.

   cutOverflow: true to return the row rectangle visible in the System.Windows.Forms.DataGridView bounds; false 

    to return the entire row rectangle.

  

   Returns: The System.Drawing.Rectangle that represents the display rectangle of the row.
  """
  pass
 def GetScaledBounds(self,*args):
  """
  GetScaledBounds(self: Control,bounds: Rectangle,factor: SizeF,specified: BoundsSpecified) -> Rectangle

  

   Retrieves the bounds within which the control is scaled.

  

   bounds: A System.Drawing.Rectangle that specifies the area for which to retrieve the display bounds.

   factor: The height and width of the control's bounds.

   specified: One of the values of System.Windows.Forms.BoundsSpecified that specifies the bounds of the 

    control to use when defining its size and position.

  

   Returns: A System.Drawing.Rectangle representing the bounds within which the control is scaled.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Component,service: Type) -> object

  

   Returns an object that represents a service provided by the System.ComponentModel.Component or 

    by its System.ComponentModel.Container.

  

  

   service: A service provided by the System.ComponentModel.Component.

   Returns: An System.Object that represents a service provided by the System.ComponentModel.Component,or 

    null if the System.ComponentModel.Component does not provide the specified service.
  """
  pass
 def GetStyle(self,*args):
  """
  GetStyle(self: Control,flag: ControlStyles) -> bool

  

   Retrieves the value of the specified control style bit for the control.

  

   flag: The System.Windows.Forms.ControlStyles bit to return the value from.

   Returns: true if the specified control style bit is set to true; otherwise,false.
  """
  pass
 def GetTopLevel(self,*args):
  """
  GetTopLevel(self: Control) -> bool

  

   Determines if the control is a top-level control.

   Returns: true if the control is a top-level control; otherwise,false.
  """
  pass
 def HitTest(self,x,y):
  """
  HitTest(self: DataGridView,x: int,y: int) -> HitTestInfo

  

   Returns location information,such as row and column indices,given x- and y-coordinates.

  

   x: The x-coordinate.

   y: The y-coordinate.

   Returns: A System.Windows.Forms.DataGridView.HitTestInfo that contains the location information.
  """
  pass
 def InitLayout(self,*args):
  """
  InitLayout(self: Control)

   Called after the control has been added to another container.
  """
  pass
 def InvalidateCell(self,*__args):
  """
  InvalidateCell(self: DataGridView,columnIndex: int,rowIndex: int)

   Invalidates the cell with the specified row and column indexes,forcing it to be repainted.

  

   columnIndex: The column index of the cell to invalidate.

   rowIndex: The row index of the cell to invalidate.

  InvalidateCell(self: DataGridView,dataGridViewCell: DataGridViewCell)

   Invalidates the specified cell of the System.Windows.Forms.DataGridView,forcing it to be 

    repainted.

  

  

   dataGridViewCell: The System.Windows.Forms.DataGridViewCell to invalidate.
  """
  pass
 def InvalidateColumn(self,columnIndex):
  """
  InvalidateColumn(self: DataGridView,columnIndex: int)

   Invalidates the specified column of the System.Windows.Forms.DataGridView,forcing it to be 

    repainted.

  

  

   columnIndex: The index of the column to invalidate.
  """
  pass
 def InvalidateRow(self,rowIndex):
  """
  InvalidateRow(self: DataGridView,rowIndex: int)

   Invalidates the specified row of the System.Windows.Forms.DataGridView,forcing it to be 

    repainted.

  

  

   rowIndex: The index of the row to invalidate.
  """
  pass
 def InvokeGotFocus(self,*args):
  """
  InvokeGotFocus(self: Control,toInvoke: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.GotFocus event for the specified control.

  

   toInvoke: The System.Windows.Forms.Control to assign the event to.

   e: An System.EventArgs that contains the event data.
  """
  pass
 def InvokeLostFocus(self,*args):
  """
  InvokeLostFocus(self: Control,toInvoke: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.LostFocus event for the specified control.

  

   toInvoke: The System.Windows.Forms.Control to assign the event to.

   e: An System.EventArgs that contains the event data.
  """
  pass
 def InvokeOnClick(self,*args):
  """
  InvokeOnClick(self: Control,toInvoke: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.Click event for the specified control.

  

   toInvoke: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Click event to.

   e: An System.EventArgs that contains the event data.
  """
  pass
 def InvokePaint(self,*args):
  """
  InvokePaint(self: Control,c: Control,e: PaintEventArgs)

   Raises the System.Windows.Forms.Control.Paint event for the specified control.

  

   c: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Paint event to.

   e: An System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def InvokePaintBackground(self,*args):
  """
  InvokePaintBackground(self: Control,c: Control,e: PaintEventArgs)

   Raises the PaintBackground event for the specified control.

  

   c: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Paint event to.

   e: An System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def IsInputChar(self,*args):
  """
  IsInputChar(self: DataGridView,charCode: Char) -> bool

  

   Determines whether a character is an input character that the System.Windows.Forms.DataGridView 

    recognizes.

  

  

   charCode: The character to test.

   Returns: true if the character is recognized as an input character; otherwise,false.
  """
  pass
 def IsInputKey(self,*args):
  """
  IsInputKey(self: DataGridView,keyData: Keys) -> bool

  

   keyData: One of the System.Windows.Forms.Keys values.

   Returns: true if the specified key is a regular input key; otherwise,false.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def NotifyCurrentCellDirty(self,dirty):
  """
  NotifyCurrentCellDirty(self: DataGridView,dirty: bool)

   Notifies the System.Windows.Forms.DataGridView that the current cell has uncommitted changes.

  

   dirty: true to indicate the cell has uncommitted changes; otherwise,false.
  """
  pass
 def NotifyInvalidate(self,*args):
  """
  NotifyInvalidate(self: Control,invalidatedArea: Rectangle)

   Raises the System.Windows.Forms.Control.Invalidated event with a specified region of the control 

    to invalidate.

  

  

   invalidatedArea: A System.Drawing.Rectangle representing the area to invalidate.
  """
  pass
 def OnAllowUserToAddRowsChanged(self,*args):
  """
  OnAllowUserToAddRowsChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.AllowUserToAddRowsChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnAllowUserToDeleteRowsChanged(self,*args):
  """
  OnAllowUserToDeleteRowsChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.AllowUserToDeleteRowsChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnAllowUserToOrderColumnsChanged(self,*args):
  """
  OnAllowUserToOrderColumnsChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.AllowUserToOrderColumnsChanged event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnAllowUserToResizeColumnsChanged(self,*args):
  """
  OnAllowUserToResizeColumnsChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.AllowUserToResizeColumnsChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnAllowUserToResizeRowsChanged(self,*args):
  """
  OnAllowUserToResizeRowsChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.AllowUserToResizeRowsChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnAlternatingRowsDefaultCellStyleChanged(self,*args):
  """
  OnAlternatingRowsDefaultCellStyleChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.AlternatingRowsDefaultCellStyleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnAutoGenerateColumnsChanged(self,*args):
  """
  OnAutoGenerateColumnsChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.AutoGenerateColumnsChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnAutoSizeChanged(self,*args):
  """
  OnAutoSizeChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.AutoSizeChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnAutoSizeColumnModeChanged(self,*args):
  """
  OnAutoSizeColumnModeChanged(self: DataGridView,e: DataGridViewAutoSizeColumnModeEventArgs)

   Raises the System.Windows.Forms.DataGridView.AutoSizeColumnModeChanged event.

  

   e: A System.Windows.Forms.DataGridViewAutoSizeColumnModeEventArgs that contains the event data.
  """
  pass
 def OnAutoSizeColumnsModeChanged(self,*args):
  """
  OnAutoSizeColumnsModeChanged(self: DataGridView,e: DataGridViewAutoSizeColumnsModeEventArgs)

   Raises the System.Windows.Forms.DataGridView.AutoSizeColumnsModeChanged event.

  

   e: A System.Windows.Forms.DataGridViewAutoSizeColumnsModeEventArgs that contains the event data.
  """
  pass
 def OnAutoSizeRowsModeChanged(self,*args):
  """
  OnAutoSizeRowsModeChanged(self: DataGridView,e: DataGridViewAutoSizeModeEventArgs)

   Raises the System.Windows.Forms.DataGridView.AutoSizeRowsModeChanged event.

  

   e: A System.Windows.Forms.DataGridViewAutoSizeModeEventArgs that contains the event data.
  """
  pass
 def OnBackColorChanged(self,*args):
  """
  OnBackColorChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.BackColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBackgroundColorChanged(self,*args):
  """
  OnBackgroundColorChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.BackgroundColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBackgroundImageChanged(self,*args):
  """
  OnBackgroundImageChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.BackgroundImageChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBackgroundImageLayoutChanged(self,*args):
  """
  OnBackgroundImageLayoutChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.BackgroundImageLayoutChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBindingContextChanged(self,*args):
  """
  OnBindingContextChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.Control.BindingContextChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBorderStyleChanged(self,*args):
  """
  OnBorderStyleChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.BorderStyleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnCancelRowEdit(self,*args):
  """
  OnCancelRowEdit(self: DataGridView,e: QuestionEventArgs)

   Raises the System.Windows.Forms.DataGridView.CancelRowEdit event.

  

   e: A System.Windows.Forms.QuestionEventArgs that contains the event data.
  """
  pass
 def OnCausesValidationChanged(self,*args):
  """
  OnCausesValidationChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.CausesValidationChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnCellBeginEdit(self,*args):
  """
  OnCellBeginEdit(self: DataGridView,e: DataGridViewCellCancelEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellBeginEdit event.

  

   e: A System.Windows.Forms.DataGridViewCellCancelEventArgs that contains the event data.
  """
  pass
 def OnCellBorderStyleChanged(self,*args):
  """
  OnCellBorderStyleChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.CellBorderStyleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnCellClick(self,*args):
  """
  OnCellClick(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellClick event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnCellContentClick(self,*args):
  """
  OnCellContentClick(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellContentClick event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains information regarding the cell 

    whose content was clicked.
  """
  pass
 def OnCellContentDoubleClick(self,*args):
  """
  OnCellContentDoubleClick(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellContentDoubleClick event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnCellContextMenuStripChanged(self,*args):
  """
  OnCellContextMenuStripChanged(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellContextMenuStripChanged event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnCellContextMenuStripNeeded(self,*args):
  """
  OnCellContextMenuStripNeeded(self: DataGridView,e: DataGridViewCellContextMenuStripNeededEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellContextMenuStripNeeded event.

  

   e: A System.Windows.Forms.DataGridViewCellContextMenuStripNeededEventArgs that contains the event 

    data.
  """
  pass
 def OnCellDoubleClick(self,*args):
  """
  OnCellDoubleClick(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellDoubleClick event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnCellEndEdit(self,*args):
  """
  OnCellEndEdit(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellEndEdit event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnCellEnter(self,*args):
  """
  OnCellEnter(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellEnter event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnCellErrorTextChanged(self,*args):
  """
  OnCellErrorTextChanged(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellErrorTextChanged event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnCellErrorTextNeeded(self,*args):
  """
  OnCellErrorTextNeeded(self: DataGridView,e: DataGridViewCellErrorTextNeededEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellErrorTextNeeded event.

  

   e: A System.Windows.Forms.DataGridViewCellErrorTextNeededEventArgs that contains the event data.
  """
  pass
 def OnCellFormatting(self,*args):
  """
  OnCellFormatting(self: DataGridView,e: DataGridViewCellFormattingEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellFormatting event.

  

   e: A System.Windows.Forms.DataGridViewCellFormattingEventArgs that contains the event data.
  """
  pass
 def OnCellLeave(self,*args):
  """
  OnCellLeave(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellLeave event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnCellMouseClick(self,*args):
  """
  OnCellMouseClick(self: DataGridView,e: DataGridViewCellMouseEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellMouseClick event.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
  """
  pass
 def OnCellMouseDoubleClick(self,*args):
  """
  OnCellMouseDoubleClick(self: DataGridView,e: DataGridViewCellMouseEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellMouseDoubleClick event.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
  """
  pass
 def OnCellMouseDown(self,*args):
  """
  OnCellMouseDown(self: DataGridView,e: DataGridViewCellMouseEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellMouseDown event.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
  """
  pass
 def OnCellMouseEnter(self,*args):
  """
  OnCellMouseEnter(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellMouseEnter event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnCellMouseLeave(self,*args):
  """
  OnCellMouseLeave(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellMouseLeave event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnCellMouseMove(self,*args):
  """
  OnCellMouseMove(self: DataGridView,e: DataGridViewCellMouseEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellMouseMove event.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
  """
  pass
 def OnCellMouseUp(self,*args):
  """
  OnCellMouseUp(self: DataGridView,e: DataGridViewCellMouseEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellMouseUp event.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
  """
  pass
 def OnCellPainting(self,*args):
  """
  OnCellPainting(self: DataGridView,e: DataGridViewCellPaintingEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellPainting event.

  

   e: A System.Windows.Forms.DataGridViewCellPaintingEventArgs that contains the event data.
  """
  pass
 def OnCellParsing(self,*args):
  """
  OnCellParsing(self: DataGridView,e: DataGridViewCellParsingEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellParsing event.

  

   e: A System.Windows.Forms.DataGridViewCellParsingEventArgs that contains the event data.
  """
  pass
 def OnCellStateChanged(self,*args):
  """
  OnCellStateChanged(self: DataGridView,e: DataGridViewCellStateChangedEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellStateChanged event.

  

   e: A System.Windows.Forms.DataGridViewCellStateChangedEventArgs that contains the event data.
  """
  pass
 def OnCellStyleChanged(self,*args):
  """
  OnCellStyleChanged(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellStyleChanged event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnCellStyleContentChanged(self,*args):
  """
  OnCellStyleContentChanged(self: DataGridView,e: DataGridViewCellStyleContentChangedEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellStyleContentChanged event.

  

   e: A System.Windows.Forms.DataGridViewCellStyleContentChangedEventArgs that contains the event data.
  """
  pass
 def OnCellToolTipTextChanged(self,*args):
  """
  OnCellToolTipTextChanged(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellToolTipTextChanged event.

  

   e: An System.Windows.Forms.DataGridViewCellEventArgs that contains information about the cell.
  """
  pass
 def OnCellToolTipTextNeeded(self,*args):
  """
  OnCellToolTipTextNeeded(self: DataGridView,e: DataGridViewCellToolTipTextNeededEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellToolTipTextNeeded event.

  

   e: A System.Windows.Forms.DataGridViewCellToolTipTextNeededEventArgs that contains the event data.
  """
  pass
 def OnCellValidated(self,*args):
  """
  OnCellValidated(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellValidated event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnCellValidating(self,*args):
  """
  OnCellValidating(self: DataGridView,e: DataGridViewCellValidatingEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellValidating event.

  

   e: A System.Windows.Forms.DataGridViewCellValidatingEventArgs that contains the event data.
  """
  pass
 def OnCellValueChanged(self,*args):
  """
  OnCellValueChanged(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellValueChanged event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnCellValueNeeded(self,*args):
  """
  OnCellValueNeeded(self: DataGridView,e: DataGridViewCellValueEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellValueNeeded event.

  

   e: A System.Windows.Forms.DataGridViewCellValueEventArgs that contains the event data.
  """
  pass
 def OnCellValuePushed(self,*args):
  """
  OnCellValuePushed(self: DataGridView,e: DataGridViewCellValueEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellValuePushed event.

  

   e: A System.Windows.Forms.DataGridViewCellValueEventArgs that contains the event data.
  """
  pass
 def OnChangeUICues(self,*args):
  """
  OnChangeUICues(self: Control,e: UICuesEventArgs)

   Raises the System.Windows.Forms.Control.ChangeUICues event.

  

   e: A System.Windows.Forms.UICuesEventArgs that contains the event data.
  """
  pass
 def OnClick(self,*args):
  """
  OnClick(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.Click event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnClientSizeChanged(self,*args):
  """
  OnClientSizeChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.ClientSizeChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnColumnAdded(self,*args):
  """
  OnColumnAdded(self: DataGridView,e: DataGridViewColumnEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnAdded event.

  

   e: A System.Windows.Forms.DataGridViewColumnEventArgs that contains the event data.
  """
  pass
 def OnColumnContextMenuStripChanged(self,*args):
  """
  OnColumnContextMenuStripChanged(self: DataGridView,e: DataGridViewColumnEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnContextMenuStripChanged event.

  

   e: A System.Windows.Forms.DataGridViewColumnEventArgs that contains the event data.
  """
  pass
 def OnColumnDataPropertyNameChanged(self,*args):
  """
  OnColumnDataPropertyNameChanged(self: DataGridView,e: DataGridViewColumnEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnDataPropertyNameChanged event.

  

   e: A System.Windows.Forms.DataGridViewColumnEventArgs that contains the event data.
  """
  pass
 def OnColumnDefaultCellStyleChanged(self,*args):
  """
  OnColumnDefaultCellStyleChanged(self: DataGridView,e: DataGridViewColumnEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnDefaultCellStyleChanged event.

  

   e: A System.Windows.Forms.DataGridViewColumnEventArgs that contains the event data.
  """
  pass
 def OnColumnDisplayIndexChanged(self,*args):
  """
  OnColumnDisplayIndexChanged(self: DataGridView,e: DataGridViewColumnEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnDisplayIndexChanged event.

  

   e: A System.Windows.Forms.DataGridViewColumnEventArgs that contains the event data.
  """
  pass
 def OnColumnDividerDoubleClick(self,*args):
  """
  OnColumnDividerDoubleClick(self: DataGridView,e: DataGridViewColumnDividerDoubleClickEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnDividerDoubleClick event.

  

   e: A System.Windows.Forms.DataGridViewColumnDividerDoubleClickEventArgs that contains the event 

    data.
  """
  pass
 def OnColumnDividerWidthChanged(self,*args):
  """
  OnColumnDividerWidthChanged(self: DataGridView,e: DataGridViewColumnEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnDividerWidthChanged event.

  

   e: A System.Windows.Forms.DataGridViewColumnEventArgs that contains the event data.
  """
  pass
 def OnColumnHeaderCellChanged(self,*args):
  """
  OnColumnHeaderCellChanged(self: DataGridView,e: DataGridViewColumnEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnHeaderCellChanged event.

  

   e: A System.Windows.Forms.DataGridViewColumnEventArgs that contains the event data.
  """
  pass
 def OnColumnHeaderMouseClick(self,*args):
  """
  OnColumnHeaderMouseClick(self: DataGridView,e: DataGridViewCellMouseEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnHeaderMouseClick event.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains the event data.
  """
  pass
 def OnColumnHeaderMouseDoubleClick(self,*args):
  """
  OnColumnHeaderMouseDoubleClick(self: DataGridView,e: DataGridViewCellMouseEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnHeaderMouseDoubleClick event.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains information about the cell 

    and the position of the mouse pointer.
  """
  pass
 def OnColumnHeadersBorderStyleChanged(self,*args):
  """
  OnColumnHeadersBorderStyleChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnHeadersBorderStyleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnColumnHeadersDefaultCellStyleChanged(self,*args):
  """
  OnColumnHeadersDefaultCellStyleChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnHeadersDefaultCellStyleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnColumnHeadersHeightChanged(self,*args):
  """
  OnColumnHeadersHeightChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnHeadersHeightChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnColumnHeadersHeightSizeModeChanged(self,*args):
  """
  OnColumnHeadersHeightSizeModeChanged(self: DataGridView,e: DataGridViewAutoSizeModeEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnHeadersHeightSizeModeChanged event.

  

   e: A System.Windows.Forms.DataGridViewAutoSizeModeEventArgs that contains the event data.
  """
  pass
 def OnColumnMinimumWidthChanged(self,*args):
  """
  OnColumnMinimumWidthChanged(self: DataGridView,e: DataGridViewColumnEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnMinimumWidthChanged event.

  

   e: A System.Windows.Forms.DataGridViewColumnEventArgs that contains the event data.
  """
  pass
 def OnColumnNameChanged(self,*args):
  """
  OnColumnNameChanged(self: DataGridView,e: DataGridViewColumnEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnNameChanged event.

  

   e: A System.Windows.Forms.DataGridViewColumnEventArgs that contains the event data.
  """
  pass
 def OnColumnRemoved(self,*args):
  """
  OnColumnRemoved(self: DataGridView,e: DataGridViewColumnEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnRemoved event.

  

   e: A System.Windows.Forms.DataGridViewColumnEventArgs that contains the event data.
  """
  pass
 def OnColumnSortModeChanged(self,*args):
  """
  OnColumnSortModeChanged(self: DataGridView,e: DataGridViewColumnEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnSortModeChanged event.

  

   e: A System.Windows.Forms.DataGridViewColumnEventArgs that contains the event data.
  """
  pass
 def OnColumnStateChanged(self,*args):
  """
  OnColumnStateChanged(self: DataGridView,e: DataGridViewColumnStateChangedEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnStateChanged event.

  

   e: A System.Windows.Forms.DataGridViewColumnStateChangedEventArgs that contains the event data.
  """
  pass
 def OnColumnToolTipTextChanged(self,*args):
  """
  OnColumnToolTipTextChanged(self: DataGridView,e: DataGridViewColumnEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnToolTipTextChanged event.

  

   e: A System.Windows.Forms.DataGridViewColumnEventArgs that contains information about the column.
  """
  pass
 def OnColumnWidthChanged(self,*args):
  """
  OnColumnWidthChanged(self: DataGridView,e: DataGridViewColumnEventArgs)

   Raises the System.Windows.Forms.DataGridView.ColumnWidthChanged event.

  

   e: A System.Windows.Forms.DataGridViewColumnEventArgs that contains the event data.
  """
  pass
 def OnContextMenuChanged(self,*args):
  """
  OnContextMenuChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.ContextMenuChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnContextMenuStripChanged(self,*args):
  """
  OnContextMenuStripChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.ContextMenuStripChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnControlAdded(self,*args):
  """
  OnControlAdded(self: Control,e: ControlEventArgs)

   Raises the System.Windows.Forms.Control.ControlAdded event.

  

   e: A System.Windows.Forms.ControlEventArgs that contains the event data.
  """
  pass
 def OnControlRemoved(self,*args):
  """
  OnControlRemoved(self: Control,e: ControlEventArgs)

   Raises the System.Windows.Forms.Control.ControlRemoved event.

  

   e: A System.Windows.Forms.ControlEventArgs that contains the event data.
  """
  pass
 def OnCreateControl(self,*args):
  """
  OnCreateControl(self: Control)

   Raises the System.Windows.Forms.Control.CreateControl method.
  """
  pass
 def OnCurrentCellChanged(self,*args):
  """
  OnCurrentCellChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.CurrentCellChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnCurrentCellDirtyStateChanged(self,*args):
  """
  OnCurrentCellDirtyStateChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.CurrentCellDirtyStateChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnCursorChanged(self,*args):
  """
  OnCursorChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.Control.CursorChanged event and updates the 

    System.Windows.Forms.DataGridView.UserSetCursor property if the cursor was changed in user code.

  

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDataBindingComplete(self,*args):
  """
  OnDataBindingComplete(self: DataGridView,e: DataGridViewBindingCompleteEventArgs)

   Raises the System.Windows.Forms.DataGridView.DataBindingComplete event.

  

   e: A System.Windows.Forms.DataGridViewBindingCompleteEventArgs that contains the event data.
  """
  pass
 def OnDataError(self,*args):
  """
  OnDataError(self: DataGridView,displayErrorDialogIfNoHandler: bool,e: DataGridViewDataErrorEventArgs)

   Raises the System.Windows.Forms.DataGridView.DataError event.

  

   displayErrorDialogIfNoHandler: true to display an error dialog box if there is no handler for the 

    System.Windows.Forms.DataGridView.DataError event.

  

   e: A System.Windows.Forms.DataGridViewDataErrorEventArgs that contains the event data.
  """
  pass
 def OnDataMemberChanged(self,*args):
  """
  OnDataMemberChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.DataMemberChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDataSourceChanged(self,*args):
  """
  OnDataSourceChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.DataSourceChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDefaultCellStyleChanged(self,*args):
  """
  OnDefaultCellStyleChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.DefaultCellStyleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDefaultValuesNeeded(self,*args):
  """
  OnDefaultValuesNeeded(self: DataGridView,e: DataGridViewRowEventArgs)

   Raises the System.Windows.Forms.DataGridView.DefaultValuesNeeded event.

  

   e: A System.Windows.Forms.DataGridViewRowEventArgs that contains the event data.
  """
  pass
 def OnDockChanged(self,*args):
  """
  OnDockChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.DockChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDoubleClick(self,*args):
  """
  OnDoubleClick(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.Control.DoubleClick event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDpiChangedAfterParent(self,*args):
  """ OnDpiChangedAfterParent(self: Control,e: EventArgs) """
  pass
 def OnDpiChangedBeforeParent(self,*args):
  """ OnDpiChangedBeforeParent(self: Control,e: EventArgs) """
  pass
 def OnDragDrop(self,*args):
  """
  OnDragDrop(self: Control,drgevent: DragEventArgs)

   Raises the System.Windows.Forms.Control.DragDrop event.

  

   drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
  """
  pass
 def OnDragEnter(self,*args):
  """
  OnDragEnter(self: Control,drgevent: DragEventArgs)

   Raises the System.Windows.Forms.Control.DragEnter event.

  

   drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
  """
  pass
 def OnDragLeave(self,*args):
  """
  OnDragLeave(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.DragLeave event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDragOver(self,*args):
  """
  OnDragOver(self: Control,drgevent: DragEventArgs)

   Raises the System.Windows.Forms.Control.DragOver event.

  

   drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
  """
  pass
 def OnEditingControlShowing(self,*args):
  """
  OnEditingControlShowing(self: DataGridView,e: DataGridViewEditingControlShowingEventArgs)

   Raises the System.Windows.Forms.DataGridView.EditingControlShowing event.

  

   e: A System.Windows.Forms.DataGridViewEditingControlShowingEventArgs that contains information 

    about the editing control.
  """
  pass
 def OnEditModeChanged(self,*args):
  """
  OnEditModeChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.EditModeChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnEnabledChanged(self,*args):
  """
  OnEnabledChanged(self: DataGridView,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnEnter(self,*args):
  """
  OnEnter(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.Control.Enter event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnFontChanged(self,*args):
  """
  OnFontChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.FontChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnForeColorChanged(self,*args):
  """
  OnForeColorChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.ForeColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnGiveFeedback(self,*args):
  """
  OnGiveFeedback(self: Control,gfbevent: GiveFeedbackEventArgs)

   Raises the System.Windows.Forms.Control.GiveFeedback event.

  

   gfbevent: A System.Windows.Forms.GiveFeedbackEventArgs that contains the event data.
  """
  pass
 def OnGotFocus(self,*args):
  """
  OnGotFocus(self: DataGridView,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnGridColorChanged(self,*args):
  """
  OnGridColorChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.GridColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleCreated(self,*args):
  """
  OnHandleCreated(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.Control.HandleCreated event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleDestroyed(self,*args):
  """
  OnHandleDestroyed(self: DataGridView,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHelpRequested(self,*args):
  """
  OnHelpRequested(self: Control,hevent: HelpEventArgs)

   Raises the System.Windows.Forms.Control.HelpRequested event.

  

   hevent: A System.Windows.Forms.HelpEventArgs that contains the event data.
  """
  pass
 def OnImeModeChanged(self,*args):
  """
  OnImeModeChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.ImeModeChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnInvalidated(self,*args):
  """
  OnInvalidated(self: Control,e: InvalidateEventArgs)

   Raises the System.Windows.Forms.Control.Invalidated event.

  

   e: An System.Windows.Forms.InvalidateEventArgs that contains the event data.
  """
  pass
 def OnKeyDown(self,*args):
  """
  OnKeyDown(self: DataGridView,e: KeyEventArgs)

   Raises the System.Windows.Forms.Control.KeyDown event.

  

   e: A System.Windows.Forms.KeyEventArgs that contains the event data.
  """
  pass
 def OnKeyPress(self,*args):
  """
  OnKeyPress(self: DataGridView,e: KeyPressEventArgs)

   Raises the System.Windows.Forms.Control.KeyPress event.

  

   e: A System.Windows.Forms.KeyPressEventArgs that contains the event data.
  """
  pass
 def OnKeyUp(self,*args):
  """
  OnKeyUp(self: DataGridView,e: KeyEventArgs)

   Raises the System.Windows.Forms.Control.KeyUp event.

  

   e: A System.Windows.Forms.KeyEventArgs that contains the event data.
  """
  pass
 def OnLayout(self,*args):
  """
  OnLayout(self: DataGridView,e: LayoutEventArgs)

   Raises the System.Windows.Forms.Control.Layout event.

  

   e: A System.Windows.Forms.LayoutEventArgs that contains the event data.
  """
  pass
 def OnLeave(self,*args):
  """
  OnLeave(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.Control.Leave event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnLocationChanged(self,*args):
  """
  OnLocationChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.LocationChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnLostFocus(self,*args):
  """
  OnLostFocus(self: DataGridView,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMarginChanged(self,*args):
  """
  OnMarginChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.MarginChanged event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnMouseCaptureChanged(self,*args):
  """
  OnMouseCaptureChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.MouseCaptureChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseClick(self,*args):
  """
  OnMouseClick(self: DataGridView,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseClick event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseDoubleClick(self,*args):
  """
  OnMouseDoubleClick(self: DataGridView,e: MouseEventArgs)

   e: An System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseDown(self,*args):
  """
  OnMouseDown(self: DataGridView,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseDown event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseEnter(self,*args):
  """
  OnMouseEnter(self: DataGridView,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseHover(self,*args):
  """
  OnMouseHover(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.MouseHover event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseLeave(self,*args):
  """
  OnMouseLeave(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.Control.MouseLeave event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseMove(self,*args):
  """
  OnMouseMove(self: DataGridView,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseMove event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseUp(self,*args):
  """
  OnMouseUp(self: DataGridView,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseUp event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseWheel(self,*args):
  """
  OnMouseWheel(self: DataGridView,e: MouseEventArgs)

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMove(self,*args):
  """
  OnMove(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.Move event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMultiSelectChanged(self,*args):
  """
  OnMultiSelectChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.MultiSelectChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnNewRowNeeded(self,*args):
  """
  OnNewRowNeeded(self: DataGridView,e: DataGridViewRowEventArgs)

   Raises the System.Windows.Forms.DataGridView.NewRowNeeded event.

  

   e: A System.Windows.Forms.DataGridViewRowEventArgs that contains the event data.
  """
  pass
 def OnNotifyMessage(self,*args):
  """
  OnNotifyMessage(self: Control,m: Message)

   Notifies the control of Windows messages.

  

   m: A System.Windows.Forms.Message that represents the Windows message.
  """
  pass
 def OnPaddingChanged(self,*args):
  """
  OnPaddingChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.PaddingChanged event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnPaint(self,*args):
  """
  OnPaint(self: DataGridView,e: PaintEventArgs)

   Raises the System.Windows.Forms.Control.Paint event.

  

   e: A System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def OnPaintBackground(self,*args):
  """
  OnPaintBackground(self: Control,pevent: PaintEventArgs)

   Paints the background of the control.

  

   pevent: A System.Windows.Forms.PaintEventArgs that contains information about the control to paint.
  """
  pass
 def OnParentBackColorChanged(self,*args):
  """
  OnParentBackColorChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.BackColorChanged event when the 

    System.Windows.Forms.Control.BackColor property value of the control's container changes.

  

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentBackgroundImageChanged(self,*args):
  """
  OnParentBackgroundImageChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.BackgroundImageChanged event when the 

    System.Windows.Forms.Control.BackgroundImage property value of the control's container changes.

  

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentBindingContextChanged(self,*args):
  """
  OnParentBindingContextChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.BindingContextChanged event when the 

    System.Windows.Forms.Control.BindingContext property value of the control's container changes.

  

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentChanged(self,*args):
  """
  OnParentChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.ParentChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentCursorChanged(self,*args):
  """
  OnParentCursorChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.CursorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentEnabledChanged(self,*args):
  """
  OnParentEnabledChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.EnabledChanged event when the 

    System.Windows.Forms.Control.Enabled property value of the control's container changes.

  

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentFontChanged(self,*args):
  """
  OnParentFontChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.FontChanged event when the 

    System.Windows.Forms.Control.Font property value of the control's container changes.

  

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentForeColorChanged(self,*args):
  """
  OnParentForeColorChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.ForeColorChanged event when the 

    System.Windows.Forms.Control.ForeColor property value of the control's container changes.

  

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentRightToLeftChanged(self,*args):
  """
  OnParentRightToLeftChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.RightToLeftChanged event when the 

    System.Windows.Forms.Control.RightToLeft property value of the control's container changes.

  

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentVisibleChanged(self,*args):
  """
  OnParentVisibleChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.VisibleChanged event when the 

    System.Windows.Forms.Control.Visible property value of the control's container changes.

  

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnPreviewKeyDown(self,*args):
  """
  OnPreviewKeyDown(self: Control,e: PreviewKeyDownEventArgs)

   Raises the System.Windows.Forms.Control.PreviewKeyDown event.

  

   e: A System.Windows.Forms.PreviewKeyDownEventArgs that contains the event data.
  """
  pass
 def OnPrint(self,*args):
  """
  OnPrint(self: Control,e: PaintEventArgs)

   Raises the System.Windows.Forms.Control.Paint event.

  

   e: A System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def OnQueryContinueDrag(self,*args):
  """
  OnQueryContinueDrag(self: Control,qcdevent: QueryContinueDragEventArgs)

   Raises the System.Windows.Forms.Control.QueryContinueDrag event.

  

   qcdevent: A System.Windows.Forms.QueryContinueDragEventArgs that contains the event data.
  """
  pass
 def OnReadOnlyChanged(self,*args):
  """
  OnReadOnlyChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.ReadOnlyChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRegionChanged(self,*args):
  """
  OnRegionChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.RegionChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnResize(self,*args):
  """
  OnResize(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.Control.Resize event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRightToLeftChanged(self,*args):
  """
  OnRightToLeftChanged(self: DataGridView,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRowContextMenuStripChanged(self,*args):
  """
  OnRowContextMenuStripChanged(self: DataGridView,e: DataGridViewRowEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowContextMenuStripChanged event.

  

   e: A System.Windows.Forms.DataGridViewRowEventArgs that contains the event data.
  """
  pass
 def OnRowContextMenuStripNeeded(self,*args):
  """
  OnRowContextMenuStripNeeded(self: DataGridView,e: DataGridViewRowContextMenuStripNeededEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowContextMenuStripNeeded event.

  

   e: A System.Windows.Forms.DataGridViewRowContextMenuStripNeededEventArgs that contains the event 

    data.
  """
  pass
 def OnRowDefaultCellStyleChanged(self,*args):
  """
  OnRowDefaultCellStyleChanged(self: DataGridView,e: DataGridViewRowEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowDefaultCellStyleChanged event.

  

   e: A System.Windows.Forms.DataGridViewRowEventArgs that contains the event data.
  """
  pass
 def OnRowDirtyStateNeeded(self,*args):
  """
  OnRowDirtyStateNeeded(self: DataGridView,e: QuestionEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowDirtyStateNeeded event.

  

   e: A System.Windows.Forms.QuestionEventArgs that contains the event data.
  """
  pass
 def OnRowDividerDoubleClick(self,*args):
  """
  OnRowDividerDoubleClick(self: DataGridView,e: DataGridViewRowDividerDoubleClickEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowDividerDoubleClick event.

  

   e: A System.Windows.Forms.DataGridViewRowDividerDoubleClickEventArgs that contains the event data.
  """
  pass
 def OnRowDividerHeightChanged(self,*args):
  """
  OnRowDividerHeightChanged(self: DataGridView,e: DataGridViewRowEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowDividerHeightChanged event.

  

   e: A System.Windows.Forms.DataGridViewRowEventArgs that contains the event data.
  """
  pass
 def OnRowEnter(self,*args):
  """
  OnRowEnter(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowEnter event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnRowErrorTextChanged(self,*args):
  """
  OnRowErrorTextChanged(self: DataGridView,e: DataGridViewRowEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowErrorTextChanged event.

  

   e: A System.Windows.Forms.DataGridViewRowEventArgs that contains the event data.
  """
  pass
 def OnRowErrorTextNeeded(self,*args):
  """
  OnRowErrorTextNeeded(self: DataGridView,e: DataGridViewRowErrorTextNeededEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowErrorTextNeeded event.

  

   e: A System.Windows.Forms.DataGridViewRowErrorTextNeededEventArgs that contains the event data.
  """
  pass
 def OnRowHeaderCellChanged(self,*args):
  """
  OnRowHeaderCellChanged(self: DataGridView,e: DataGridViewRowEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowHeaderCellChanged event.

  

   e: A System.Windows.Forms.DataGridViewRowEventArgs that contains the event data.
  """
  pass
 def OnRowHeaderMouseClick(self,*args):
  """
  OnRowHeaderMouseClick(self: DataGridView,e: DataGridViewCellMouseEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowHeaderMouseClick event.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains information about the mouse 

    and the header cell that was clicked.
  """
  pass
 def OnRowHeaderMouseDoubleClick(self,*args):
  """
  OnRowHeaderMouseDoubleClick(self: DataGridView,e: DataGridViewCellMouseEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowHeaderMouseDoubleClick event.

  

   e: A System.Windows.Forms.DataGridViewCellMouseEventArgs that contains information about the mouse 

    and the header cell that was double-clicked.
  """
  pass
 def OnRowHeadersBorderStyleChanged(self,*args):
  """
  OnRowHeadersBorderStyleChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.RowHeadersBorderStyleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRowHeadersDefaultCellStyleChanged(self,*args):
  """
  OnRowHeadersDefaultCellStyleChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.RowHeadersDefaultCellStyleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRowHeadersWidthChanged(self,*args):
  """
  OnRowHeadersWidthChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.RowHeadersWidthChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRowHeadersWidthSizeModeChanged(self,*args):
  """
  OnRowHeadersWidthSizeModeChanged(self: DataGridView,e: DataGridViewAutoSizeModeEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowHeadersWidthSizeModeChanged event.

  

   e: A System.Windows.Forms.DataGridViewAutoSizeModeEventArgs that contains the event data.
  """
  pass
 def OnRowHeightChanged(self,*args):
  """
  OnRowHeightChanged(self: DataGridView,e: DataGridViewRowEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowHeightChanged event.

  

   e: A System.Windows.Forms.DataGridViewRowEventArgs that contains the event data.
  """
  pass
 def OnRowHeightInfoNeeded(self,*args):
  """
  OnRowHeightInfoNeeded(self: DataGridView,e: DataGridViewRowHeightInfoNeededEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowHeightInfoNeeded event.

  

   e: A System.Windows.Forms.DataGridViewRowHeightInfoNeededEventArgs that contains the event data.
  """
  pass
 def OnRowHeightInfoPushed(self,*args):
  """
  OnRowHeightInfoPushed(self: DataGridView,e: DataGridViewRowHeightInfoPushedEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowHeightInfoPushed event.

  

   e: A System.Windows.Forms.DataGridViewRowHeightInfoPushedEventArgs that contains the event data.
  """
  pass
 def OnRowLeave(self,*args):
  """
  OnRowLeave(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowLeave event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnRowMinimumHeightChanged(self,*args):
  """
  OnRowMinimumHeightChanged(self: DataGridView,e: DataGridViewRowEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowMinimumHeightChanged event.

  

   e: A System.Windows.Forms.DataGridViewRowEventArgs that contains the event data.
  """
  pass
 def OnRowPostPaint(self,*args):
  """
  OnRowPostPaint(self: DataGridView,e: DataGridViewRowPostPaintEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowPostPaint event.

  

   e: A System.Windows.Forms.DataGridViewRowPostPaintEventArgs that contains the event data.
  """
  pass
 def OnRowPrePaint(self,*args):
  """
  OnRowPrePaint(self: DataGridView,e: DataGridViewRowPrePaintEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowPrePaint event.

  

   e: A System.Windows.Forms.DataGridViewRowPrePaintEventArgs that contains the event data.
  """
  pass
 def OnRowsAdded(self,*args):
  """
  OnRowsAdded(self: DataGridView,e: DataGridViewRowsAddedEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowsAdded event.

  

   e: A System.Windows.Forms.DataGridViewRowsAddedEventArgs that contains information about the added 

    rows.
  """
  pass
 def OnRowsDefaultCellStyleChanged(self,*args):
  """
  OnRowsDefaultCellStyleChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.RowsDefaultCellStyleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRowsRemoved(self,*args):
  """
  OnRowsRemoved(self: DataGridView,e: DataGridViewRowsRemovedEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowsRemoved event.

  

   e: A System.Windows.Forms.DataGridViewRowsRemovedEventArgs that contains information about the 

    deleted rows.
  """
  pass
 def OnRowStateChanged(self,*args):
  """
  OnRowStateChanged(self: DataGridView,rowIndex: int,e: DataGridViewRowStateChangedEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowStateChanged event.

  

   rowIndex: The index of the row that is changing state.

   e: A System.Windows.Forms.DataGridViewRowStateChangedEventArgs that contains the event data.
  """
  pass
 def OnRowUnshared(self,*args):
  """
  OnRowUnshared(self: DataGridView,e: DataGridViewRowEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowUnshared event.

  

   e: A System.Windows.Forms.DataGridViewRowEventArgs that contains the event data.
  """
  pass
 def OnRowValidated(self,*args):
  """
  OnRowValidated(self: DataGridView,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowValidated event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def OnRowValidating(self,*args):
  """
  OnRowValidating(self: DataGridView,e: DataGridViewCellCancelEventArgs)

   Raises the System.Windows.Forms.DataGridView.RowValidating event.

  

   e: A System.Windows.Forms.DataGridViewCellCancelEventArgs that contains the event data.
  """
  pass
 def OnScroll(self,*args):
  """
  OnScroll(self: DataGridView,e: ScrollEventArgs)

   Raises the System.Windows.Forms.DataGridView.Scroll event.

  

   e: A System.Windows.Forms.ScrollEventArgs that contains the event data.
  """
  pass
 def OnSelectionChanged(self,*args):
  """
  OnSelectionChanged(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.SelectionChanged event.

  

   e: An System.EventArgs that contains information about the event.
  """
  pass
 def OnSizeChanged(self,*args):
  """
  OnSizeChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.SizeChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnSortCompare(self,*args):
  """
  OnSortCompare(self: DataGridView,e: DataGridViewSortCompareEventArgs)

   Raises the System.Windows.Forms.DataGridView.SortCompare event.

  

   e: A System.Windows.Forms.DataGridViewSortCompareEventArgs that contains the event data.
  """
  pass
 def OnSorted(self,*args):
  """
  OnSorted(self: DataGridView,e: EventArgs)

   Raises the System.Windows.Forms.DataGridView.Sorted event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnStyleChanged(self,*args):
  """
  OnStyleChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.StyleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnSystemColorsChanged(self,*args):
  """
  OnSystemColorsChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.SystemColorsChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnTabIndexChanged(self,*args):
  """
  OnTabIndexChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.TabIndexChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnTabStopChanged(self,*args):
  """
  OnTabStopChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.TabStopChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnTextChanged(self,*args):
  """
  OnTextChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.TextChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnUserAddedRow(self,*args):
  """
  OnUserAddedRow(self: DataGridView,e: DataGridViewRowEventArgs)

   Raises the System.Windows.Forms.DataGridView.UserAddedRow event.

  

   e: A System.Windows.Forms.DataGridViewRowEventArgs that contains the event data.
  """
  pass
 def OnUserDeletedRow(self,*args):
  """
  OnUserDeletedRow(self: DataGridView,e: DataGridViewRowEventArgs)

   Raises the System.Windows.Forms.DataGridView.UserDeletedRow event.

  

   e: A System.Windows.Forms.DataGridViewRowEventArgs that contains the event data.
  """
  pass
 def OnUserDeletingRow(self,*args):
  """
  OnUserDeletingRow(self: DataGridView,e: DataGridViewRowCancelEventArgs)

   Raises the System.Windows.Forms.DataGridView.UserDeletingRow event.

  

   e: A System.Windows.Forms.DataGridViewRowCancelEventArgs that contains the event data.
  """
  pass
 def OnValidated(self,*args):
  """
  OnValidated(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.Validated event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnValidating(self,*args):
  """
  OnValidating(self: DataGridView,e: CancelEventArgs)

   Raises the System.Windows.Forms.Control.Validating event.

  

   e: A System.ComponentModel.CancelEventArgs that contains the event data.
  """
  pass
 def OnVisibleChanged(self,*args):
  """
  OnVisibleChanged(self: DataGridView,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def PaintBackground(self,*args):
  """
  PaintBackground(self: DataGridView,graphics: Graphics,clipBounds: Rectangle,gridBounds: Rectangle)

   Paints the background of the System.Windows.Forms.DataGridView.

  

   graphics: The System.Drawing.Graphics used to paint the background.

   clipBounds: A System.Drawing.Rectangle that represents the area of the System.Windows.Forms.DataGridView 

    that needs to be painted.

  

   gridBounds: A System.Drawing.Rectangle that represents the area in which cells are drawn.
  """
  pass
 def ProcessAKey(self,*args):
  """
  ProcessAKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the A key.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessCmdKey(self,*args):
  """
  ProcessCmdKey(self: Control,msg: Message,keyData: Keys) -> (bool,Message)

  

   Processes a command key.

  

   msg: A System.Windows.Forms.Message,passed by reference,that represents the window message to 

    process.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   Returns: true if the character was processed by the control; otherwise,false.
  """
  pass
 def ProcessDataGridViewKey(self,*args):
  """
  ProcessDataGridViewKey(self: DataGridView,e: KeyEventArgs) -> bool

  

   Processes keys used for navigating in the System.Windows.Forms.DataGridView.

  

   e: Contains information about the key that was pressed.

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessDeleteKey(self,*args):
  """
  ProcessDeleteKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the DELETE key.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessDialogChar(self,*args):
  """
  ProcessDialogChar(self: Control,charCode: Char) -> bool

  

   Processes a dialog character.

  

   charCode: The character to process.

   Returns: true if the character was processed by the control; otherwise,false.
  """
  pass
 def ProcessDialogKey(self,*args):
  """
  ProcessDialogKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes keys,such as the TAB,ESCAPE,ENTER,and ARROW keys,used to control dialog boxes.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessDownKey(self,*args):
  """
  ProcessDownKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the DOWN ARROW key.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessEndKey(self,*args):
  """
  ProcessEndKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the END key.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessEnterKey(self,*args):
  """
  ProcessEnterKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the ENTER key.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessEscapeKey(self,*args):
  """
  ProcessEscapeKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the ESC key.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessF2Key(self,*args):
  """
  ProcessF2Key(self: DataGridView,keyData: Keys) -> bool

  

   Processes the F2 key.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessHomeKey(self,*args):
  """
  ProcessHomeKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the HOME key.

  

   keyData: The key that was pressed.

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessInsertKey(self,*args):
  """
  ProcessInsertKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the INSERT key.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessKeyEventArgs(self,*args):
  """
  ProcessKeyEventArgs(self: DataGridView,m: Message) -> (bool,Message)

  

   Processes a key message and generates the appropriate control events.

  

   m: A System.Windows.Forms.Message,passed by reference,that represents the window message to 

    process.

  

   Returns: true if the message was processed; otherwise,false.
  """
  pass
 def ProcessKeyMessage(self,*args):
  """
  ProcessKeyMessage(self: Control,m: Message) -> (bool,Message)

  

   Processes a keyboard message.

  

   m: A System.Windows.Forms.Message,passed by reference,that represents the window message to 

    process.

  

   Returns: true if the message was processed by the control; otherwise,false.
  """
  pass
 def ProcessKeyPreview(self,*args):
  """
  ProcessKeyPreview(self: DataGridView,m: Message) -> (bool,Message)

  

   Previews a keyboard message.

  

   m: A System.Windows.Forms.Message,passed by reference,that represents the window message to 

    process.

  

   Returns: true if the message was processed; otherwise,false.
  """
  pass
 def ProcessLeftKey(self,*args):
  """
  ProcessLeftKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the LEFT ARROW key.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessMnemonic(self,*args):
  """
  ProcessMnemonic(self: Control,charCode: Char) -> bool

  

   Processes a mnemonic character.

  

   charCode: The character to process.

   Returns: true if the character was processed as a mnemonic by the control; otherwise,false.
  """
  pass
 def ProcessNextKey(self,*args):
  """
  ProcessNextKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the PAGE DOWN key.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessPriorKey(self,*args):
  """
  ProcessPriorKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the PAGE UP key.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessRightKey(self,*args):
  """
  ProcessRightKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the RIGHT ARROW key.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessSpaceKey(self,*args):
  """
  ProcessSpaceKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the SPACEBAR.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessTabKey(self,*args):
  """
  ProcessTabKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the TAB key.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessUpKey(self,*args):
  """
  ProcessUpKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the UP ARROW key.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def ProcessZeroKey(self,*args):
  """
  ProcessZeroKey(self: DataGridView,keyData: Keys) -> bool

  

   Processes the 0 key.

  

   keyData: A bitwise combination of System.Windows.Forms.Keys values that represents the key or keys to 

    process.

  

   Returns: true if the key was processed; otherwise,false.
  """
  pass
 def RaiseDragEvent(self,*args):
  """
  RaiseDragEvent(self: Control,key: object,e: DragEventArgs)

   Raises the appropriate drag event.

  

   key: The event to raise.

   e: A System.Windows.Forms.DragEventArgs that contains the event data.
  """
  pass
 def RaiseKeyEvent(self,*args):
  """
  RaiseKeyEvent(self: Control,key: object,e: KeyEventArgs)

   Raises the appropriate key event.

  

   key: The event to raise.

   e: A System.Windows.Forms.KeyEventArgs that contains the event data.
  """
  pass
 def RaiseMouseEvent(self,*args):
  """
  RaiseMouseEvent(self: Control,key: object,e: MouseEventArgs)

   Raises the appropriate mouse event.

  

   key: The event to raise.

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def RaisePaintEvent(self,*args):
  """
  RaisePaintEvent(self: Control,key: object,e: PaintEventArgs)

   Raises the appropriate paint event.

  

   key: The event to raise.

   e: A System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def RecreateHandle(self,*args):
  """
  RecreateHandle(self: Control)

   Forces the re-creation of the handle for the control.
  """
  pass
 def RefreshEdit(self):
  """
  RefreshEdit(self: DataGridView) -> bool

  

   Refreshes the value of the current cell with the underlying cell value when the cell is in edit 

    mode,discarding any previous value.

  

   Returns: true if successful; false if a System.Windows.Forms.DataGridView.DataError event occurred.
  """
  pass
 def RescaleConstantsForDpi(self,*args):
  """ RescaleConstantsForDpi(self: Control,deviceDpiOld: int,deviceDpiNew: int) """
  pass
 def ResetMouseEventArgs(self,*args):
  """
  ResetMouseEventArgs(self: Control)

   Resets the control to handle the System.Windows.Forms.Control.MouseLeave event.
  """
  pass
 def ResetText(self):
  """
  ResetText(self: DataGridView)

   Resets the System.Windows.Forms.DataGridView.Text property to its default value.
  """
  pass
 def RtlTranslateAlignment(self,*args):
  """
  RtlTranslateAlignment(self: Control,align: ContentAlignment) -> ContentAlignment

  

   Converts the specified System.Drawing.ContentAlignment to the appropriate 

    System.Drawing.ContentAlignment to support right-to-left text.

  

  

   align: One of the System.Drawing.ContentAlignment values.

   Returns: One of the System.Drawing.ContentAlignment values.

  RtlTranslateAlignment(self: Control,align: LeftRightAlignment) -> LeftRightAlignment

  

   Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate 

    System.Windows.Forms.LeftRightAlignment to support right-to-left text.

  

  

   align: One of the System.Windows.Forms.LeftRightAlignment values.

   Returns: One of the System.Windows.Forms.LeftRightAlignment values.

  RtlTranslateAlignment(self: Control,align: HorizontalAlignment) -> HorizontalAlignment

  

   Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate 

    System.Windows.Forms.HorizontalAlignment to support right-to-left text.

  

  

   align: One of the System.Windows.Forms.HorizontalAlignment values.

   Returns: One of the System.Windows.Forms.HorizontalAlignment values.
  """
  pass
 def RtlTranslateContent(self,*args):
  """
  RtlTranslateContent(self: Control,align: ContentAlignment) -> ContentAlignment

  

   Converts the specified System.Drawing.ContentAlignment to the appropriate 

    System.Drawing.ContentAlignment to support right-to-left text.

  

  

   align: One of the System.Drawing.ContentAlignment values.

   Returns: One of the System.Drawing.ContentAlignment values.
  """
  pass
 def RtlTranslateHorizontal(self,*args):
  """
  RtlTranslateHorizontal(self: Control,align: HorizontalAlignment) -> HorizontalAlignment

  

   Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate 

    System.Windows.Forms.HorizontalAlignment to support right-to-left text.

  

  

   align: One of the System.Windows.Forms.HorizontalAlignment values.

   Returns: One of the System.Windows.Forms.HorizontalAlignment values.
  """
  pass
 def RtlTranslateLeftRight(self,*args):
  """
  RtlTranslateLeftRight(self: Control,align: LeftRightAlignment) -> LeftRightAlignment

  

   Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate 

    System.Windows.Forms.LeftRightAlignment to support right-to-left text.

  

  

   align: One of the System.Windows.Forms.LeftRightAlignment values.

   Returns: One of the System.Windows.Forms.LeftRightAlignment values.
  """
  pass
 def ScaleControl(self,*args):
  """
  ScaleControl(self: Control,factor: SizeF,specified: BoundsSpecified)

   Scales a control's location,size,padding and margin.

  

   factor: The factor by which the height and width of the control will be scaled.

   specified: A System.Windows.Forms.BoundsSpecified value that specifies the bounds of the control to use 

    when defining its size and position.
  """
  pass
 def ScaleCore(self,*args):
  """
  ScaleCore(self: Control,dx: Single,dy: Single)

   This method is not relevant for this class.

  

   dx: The horizontal scaling factor.

   dy: The vertical scaling factor.
  """
  pass
 def Select(self):
  """
  Select(self: Control,directed: bool,forward: bool)

   Activates a child control. Optionally specifies the direction in the tab order to select the 

    control from.

  

  

   directed: true to specify the direction of the control to select; otherwise,false.

   forward: true to move forward in the tab order; false to move backward in the tab order.
  """
  pass
 def SelectAll(self):
  """
  SelectAll(self: DataGridView)

   Selects all the cells in the System.Windows.Forms.DataGridView.
  """
  pass
 def SetAutoSizeMode(self,*args):
  """
  SetAutoSizeMode(self: Control,mode: AutoSizeMode)

   Sets a value indicating how a control will behave when its System.Windows.Forms.Control.AutoSize 

    property is enabled.

  

  

   mode: One of the System.Windows.Forms.AutoSizeMode values.
  """
  pass
 def SetBoundsCore(self,*args):
  """
  SetBoundsCore(self: DataGridView,x: int,y: int,width: int,height: int,specified: BoundsSpecified)

   This member overrides 

    System.Windows.Forms.Control.SetBoundsCore(System.Int32,System.Int32,System.Int32,System.Int32,Sy

    stem.Windows.Forms.BoundsSpecified).

  

  

   x: The new System.Windows.Forms.Control.Left property value of the control.

   y: The new System.Windows.Forms.Control.Top property value of the control.

   width: The new System.Windows.Forms.Control.Width property value of the control.

   height: The new System.Windows.Forms.Control.Height property value of the control.

   specified: A bitwise combination of the System.Windows.Forms.BoundsSpecified values.
  """
  pass
 def SetClientSizeCore(self,*args):
  """
  SetClientSizeCore(self: Control,x: int,y: int)

   Sets the size of the client area of the control.

  

   x: The client area width,in pixels.

   y: The client area height,in pixels.
  """
  pass
 def SetCurrentCellAddressCore(self,*args):
  """
  SetCurrentCellAddressCore(self: DataGridView,columnIndex: int,rowIndex: int,setAnchorCellAddress: bool,validateCurrentCell: bool,throughMouseClick: bool) -> bool

  

   Sets the currently active cell.

  

   columnIndex: The index of the column containing the cell.

   rowIndex: The index of the row containing the cell.

   setAnchorCellAddress: true to make the new current cell the anchor cell for a subsequent multicell selection using the 

    SHIFT key; otherwise,false.

  

   validateCurrentCell: true to validate the value in the old current cell and cancel the change if validation fails; 

    otherwise,false.

  

   throughMouseClick: true if the current cell is being set as a result of a mouse click; otherwise,false.

   Returns: true if the current cell was successfully set; otherwise,false.
  """
  pass
 def SetSelectedCellCore(self,*args):
  """
  SetSelectedCellCore(self: DataGridView,columnIndex: int,rowIndex: int,selected: bool)

   Changes the selection state of the cell with the specified row and column indexes.

  

   columnIndex: The index of the column containing the cell.

   rowIndex: The index of the row containing the cell.

   selected: true to select the cell; false to cancel the selection of the cell.
  """
  pass
 def SetSelectedColumnCore(self,*args):
  """
  SetSelectedColumnCore(self: DataGridView,columnIndex: int,selected: bool)

   Changes the selection state of the column with the specified index.

  

   columnIndex: The index of the column.

   selected: true to select the column; false to cancel the selection of the column.
  """
  pass
 def SetSelectedRowCore(self,*args):
  """
  SetSelectedRowCore(self: DataGridView,rowIndex: int,selected: bool)

   Changes the selection state of the row with the specified index.

  

   rowIndex: The index of the row.

   selected: true to select the row; false to cancel the selection of the row.
  """
  pass
 def SetStyle(self,*args):
  """
  SetStyle(self: Control,flag: ControlStyles,value: bool)

   Sets a specified System.Windows.Forms.ControlStyles flag to either true or false.

  

   flag: The System.Windows.Forms.ControlStyles bit to set.

   value: true to apply the specified style to the control; otherwise,false.
  """
  pass
 def SetTopLevel(self,*args):
  """
  SetTopLevel(self: Control,value: bool)

   Sets the control as the top-level control.

  

   value: true to set the control as the top-level control; otherwise,false.
  """
  pass
 def SetVisibleCore(self,*args):
  """
  SetVisibleCore(self: Control,value: bool)

   Sets the control to the specified visible state.

  

   value: true to make the control visible; otherwise,false.
  """
  pass
 def SizeFromClientSize(self,*args):
  """
  SizeFromClientSize(self: Control,clientSize: Size) -> Size

  

   Determines the size of the entire control from the height and width of its client area.

  

   clientSize: A System.Drawing.Size value representing the height and width of the control's client area.

   Returns: A System.Drawing.Size value representing the height and width of the entire control.
  """
  pass
 def Sort(self,*__args):
  """
  Sort(self: DataGridView,comparer: IComparer)

   Sorts the contents of the System.Windows.Forms.DataGridView control using an implementation of 

    the System.Collections.IComparer interface.

  

  

   comparer: An implementation of System.Collections.IComparer that performs the custom sorting operation.

  Sort(self: DataGridView,dataGridViewColumn: DataGridViewColumn,direction: ListSortDirection)

   Sorts the contents of the System.Windows.Forms.DataGridView control in ascending or descending 

    order based on the contents of the specified column.

  

  

   dataGridViewColumn: The column by which to sort the contents of the System.Windows.Forms.DataGridView.

   direction: One of the System.ComponentModel.ListSortDirection values.
  """
  pass
 def UpdateBounds(self,*args):
  """
  UpdateBounds(self: Control,x: int,y: int,width: int,height: int,clientWidth: int,clientHeight: int)

   Updates the bounds of the control with the specified size,location,and client size.

  

   x: The System.Drawing.Point.X coordinate of the control.

   y: The System.Drawing.Point.Y coordinate of the control.

   width: The System.Drawing.Size.Width of the control.

   height: The System.Drawing.Size.Height of the control.

   clientWidth: The client System.Drawing.Size.Width of the control.

   clientHeight: The client System.Drawing.Size.Height of the control.

  UpdateBounds(self: Control,x: int,y: int,width: int,height: int)

   Updates the bounds of the control with the specified size and location.

  

   x: The System.Drawing.Point.X coordinate of the control.

   y: The System.Drawing.Point.Y coordinate of the control.

   width: The System.Drawing.Size.Width of the control.

   height: The System.Drawing.Size.Height of the control.

  UpdateBounds(self: Control)

   Updates the bounds of the control with the current size and location.
  """
  pass
 def UpdateCellErrorText(self,columnIndex,rowIndex):
  """
  UpdateCellErrorText(self: DataGridView,columnIndex: int,rowIndex: int)

   Forces the cell at the specified location to update its error text.

  

   columnIndex: The column index of the cell to update,or -1 to indicate a row header cell.

   rowIndex: The row index of the cell to update,or -1 to indicate a column header cell.
  """
  pass
 def UpdateCellValue(self,columnIndex,rowIndex):
  """
  UpdateCellValue(self: DataGridView,columnIndex: int,rowIndex: int)

   Forces the control to update its display of the cell at the specified location based on its new 

    value,applying any automatic sizing modes currently in effect.

  

  

   columnIndex: The zero-based column index of the cell with the new value.

   rowIndex: The zero-based row index of the cell with the new value.
  """
  pass
 def UpdateRowErrorText(self,*__args):
  """
  UpdateRowErrorText(self: DataGridView,rowIndexStart: int,rowIndexEnd: int)

   Forces the rows in the given range to update their error text.

  

   rowIndexStart: The zero-based index of the first row in the set of rows to update.

   rowIndexEnd: The zero-based index of the last row in the set of rows to update.

  UpdateRowErrorText(self: DataGridView,rowIndex: int)

   Forces the row at the given row index to update its error text.

  

   rowIndex: The zero-based index of the row to update.
  """
  pass
 def UpdateRowHeightInfo(self,rowIndex,updateToEnd):
  """
  UpdateRowHeightInfo(self: DataGridView,rowIndex: int,updateToEnd: bool)

   Forces the specified row or rows to update their height information.

  

   rowIndex: The zero-based index of the first row to update.

   updateToEnd: true to update the specified row and all subsequent rows.
  """
  pass
 def UpdateStyles(self,*args):
  """
  UpdateStyles(self: Control)

   Forces the assigned styles to be reapplied to the control.
  """
  pass
 def UpdateZOrder(self,*args):
  """
  UpdateZOrder(self: Control)

   Updates the control in its parent's z-order.
  """
  pass
 def WndProc(self,*args):
  """
  WndProc(self: DataGridView,m: Message) -> Message

  

   Processes window messages.

  

   m: A System.Windows.Forms.Message,passed by reference,that represents the window message to 

    process.
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
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]=x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass
 AdjustedTopLeftHeaderBorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the border style for the upper-left cell in the System.Windows.Forms.DataGridView.



Get: AdjustedTopLeftHeaderBorderStyle(self: DataGridView) -> DataGridViewAdvancedBorderStyle



"""

 AdvancedCellBorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the border style of the cells in the System.Windows.Forms.DataGridView.



Get: AdvancedCellBorderStyle(self: DataGridView) -> DataGridViewAdvancedBorderStyle



"""

 AdvancedColumnHeadersBorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the border style of the column header cells in the System.Windows.Forms.DataGridView.



Get: AdvancedColumnHeadersBorderStyle(self: DataGridView) -> DataGridViewAdvancedBorderStyle



"""

 AdvancedRowHeadersBorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the border style of the row header cells in the System.Windows.Forms.DataGridView.



Get: AdvancedRowHeadersBorderStyle(self: DataGridView) -> DataGridViewAdvancedBorderStyle



"""

 AllowUserToAddRows=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the option to add rows is displayed to the user.



Get: AllowUserToAddRows(self: DataGridView) -> bool



Set: AllowUserToAddRows(self: DataGridView)=value

"""

 AllowUserToDeleteRows=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the user is allowed to delete rows from the System.Windows.Forms.DataGridView.



Get: AllowUserToDeleteRows(self: DataGridView) -> bool



Set: AllowUserToDeleteRows(self: DataGridView)=value

"""

 AllowUserToOrderColumns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether manual column repositioning is enabled.



Get: AllowUserToOrderColumns(self: DataGridView) -> bool



Set: AllowUserToOrderColumns(self: DataGridView)=value

"""

 AllowUserToResizeColumns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether users can resize columns.



Get: AllowUserToResizeColumns(self: DataGridView) -> bool



Set: AllowUserToResizeColumns(self: DataGridView)=value

"""

 AllowUserToResizeRows=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether users can resize rows.



Get: AllowUserToResizeRows(self: DataGridView) -> bool



Set: AllowUserToResizeRows(self: DataGridView)=value

"""

 AlternatingRowsDefaultCellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default cell style applied to odd-numbered rows of the System.Windows.Forms.DataGridView.



Get: AlternatingRowsDefaultCellStyle(self: DataGridView) -> DataGridViewCellStyle



Set: AlternatingRowsDefaultCellStyle(self: DataGridView)=value

"""

 AutoGenerateColumns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether columns are created automatically when the System.Windows.Forms.DataGridView.DataSource or System.Windows.Forms.DataGridView.DataMember properties are set.



Get: AutoGenerateColumns(self: DataGridView) -> bool



Set: AutoGenerateColumns(self: DataGridView)=value

"""

 AutoSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AutoSize(self: DataGridView) -> bool



Set: AutoSize(self: DataGridView)=value

"""

 AutoSizeColumnsMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating how column widths are determined.



Get: AutoSizeColumnsMode(self: DataGridView) -> DataGridViewAutoSizeColumnsMode



Set: AutoSizeColumnsMode(self: DataGridView)=value

"""

 AutoSizeRowsMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating how row heights are determined.



Get: AutoSizeRowsMode(self: DataGridView) -> DataGridViewAutoSizeRowsMode



Set: AutoSizeRowsMode(self: DataGridView)=value

"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color for the control.



Get: BackColor(self: DataGridView) -> Color



Set: BackColor(self: DataGridView)=value

"""

 BackgroundColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of the System.Windows.Forms.DataGridView.



Get: BackgroundColor(self: DataGridView) -> Color



Set: BackgroundColor(self: DataGridView)=value

"""

 BackgroundImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background image displayed in the control.



Get: BackgroundImage(self: DataGridView) -> Image



Set: BackgroundImage(self: DataGridView)=value

"""

 BackgroundImageLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background image layout as defined in the System.Windows.Forms.ImageLayout enumeration.



Get: BackgroundImageLayout(self: DataGridView) -> ImageLayout



Set: BackgroundImageLayout(self: DataGridView)=value

"""

 BorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the border style for the System.Windows.Forms.DataGridView.



Get: BorderStyle(self: DataGridView) -> BorderStyle



Set: BorderStyle(self: DataGridView)=value

"""

 CanEnableIme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value,to enable IME support.



"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if events can be raised on the control.



"""

 CellBorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the cell border style for the System.Windows.Forms.DataGridView.



Get: CellBorderStyle(self: DataGridView) -> DataGridViewCellBorderStyle



Set: CellBorderStyle(self: DataGridView)=value

"""

 ClipboardCopyMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether users can copy cell text values to the System.Windows.Forms.Clipboard and whether row and column header text is included.



Get: ClipboardCopyMode(self: DataGridView) -> DataGridViewClipboardCopyMode



Set: ClipboardCopyMode(self: DataGridView)=value

"""

 ColumnCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of columns displayed in the System.Windows.Forms.DataGridView.



Get: ColumnCount(self: DataGridView) -> int



Set: ColumnCount(self: DataGridView)=value

"""

 ColumnHeadersBorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the border style applied to the column headers.



Get: ColumnHeadersBorderStyle(self: DataGridView) -> DataGridViewHeaderBorderStyle



Set: ColumnHeadersBorderStyle(self: DataGridView)=value

"""

 ColumnHeadersDefaultCellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default column header style.



Get: ColumnHeadersDefaultCellStyle(self: DataGridView) -> DataGridViewCellStyle



Set: ColumnHeadersDefaultCellStyle(self: DataGridView)=value

"""

 ColumnHeadersHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height,in pixels,of the column headers row



Get: ColumnHeadersHeight(self: DataGridView) -> int



Set: ColumnHeadersHeight(self: DataGridView)=value

"""

 ColumnHeadersHeightSizeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the height of the column headers is adjustable and whether it can be adjusted by the user or is automatically adjusted to fit the contents of the headers.



Get: ColumnHeadersHeightSizeMode(self: DataGridView) -> DataGridViewColumnHeadersHeightSizeMode



Set: ColumnHeadersHeightSizeMode(self: DataGridView)=value

"""

 ColumnHeadersVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the column header row is displayed.



Get: ColumnHeadersVisible(self: DataGridView) -> bool



Set: ColumnHeadersVisible(self: DataGridView)=value

"""

 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection that contains all the columns in the control.



Get: Columns(self: DataGridView) -> DataGridViewColumnCollection



"""

 CreateParams=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the required creation parameters when the control handle is created.



"""

 CurrentCell=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the currently active cell.



Get: CurrentCell(self: DataGridView) -> DataGridViewCell



Set: CurrentCell(self: DataGridView)=value

"""

 CurrentCellAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row and column indexes of the currently active cell.



Get: CurrentCellAddress(self: DataGridView) -> Point



"""

 CurrentRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row containing the current cell.



Get: CurrentRow(self: DataGridView) -> DataGridViewRow



"""

 DataMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the list or table in the data source for which the System.Windows.Forms.DataGridView is displaying data.



Get: DataMember(self: DataGridView) -> str



Set: DataMember(self: DataGridView)=value

"""

 DataSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the data source that the System.Windows.Forms.DataGridView is displaying data for.



Get: DataSource(self: DataGridView) -> object



Set: DataSource(self: DataGridView)=value

"""

 DefaultCellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default cell style to be applied to the cells in the System.Windows.Forms.DataGridView if no other cell style properties are set.



Get: DefaultCellStyle(self: DataGridView) -> DataGridViewCellStyle



Set: DefaultCellStyle(self: DataGridView)=value

"""

 DefaultCursor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default cursor for the control.



"""

 DefaultImeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default Input Method Editor (IME) mode supported by the control.



"""

 DefaultMargin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the space,in pixels,that is specified by default between controls.



"""

 DefaultMaximumSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length and height,in pixels,that is specified as the default maximum size of a control.



"""

 DefaultMinimumSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length and height,in pixels,that is specified as the default minimum size of a control.



"""

 DefaultPadding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the internal spacing,in pixels,of the contents of a control.



"""

 DefaultSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default initial size of the control.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 DisplayRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rectangle that represents the display area of the control.



Get: DisplayRectangle(self: DataGridView) -> Rectangle



"""

 DoubleBuffered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this control should redraw its surface using a secondary buffer to reduce or prevent flicker.



"""

 EditingControl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the control hosted by the current cell,if a cell with an editing control is in edit mode.



Get: EditingControl(self: DataGridView) -> Control



"""

 EditingPanel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the panel that contains the System.Windows.Forms.DataGridView.EditingControl.



Get: EditingPanel(self: DataGridView) -> Panel



"""

 EditMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating how to begin editing a cell.



Get: EditMode(self: DataGridView) -> DataGridViewEditMode



Set: EditMode(self: DataGridView)=value

"""

 EnableHeadersVisualStyles=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether row and column headers use the visual styles of the user's current theme if visual styles are enabled for the application.



Get: EnableHeadersVisualStyles(self: DataGridView) -> bool



Set: EnableHeadersVisualStyles(self: DataGridView)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 FirstDisplayedCell=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the first cell currently displayed in the System.Windows.Forms.DataGridView; typically,this cell is in the upper left corner.



Get: FirstDisplayedCell(self: DataGridView) -> DataGridViewCell



Set: FirstDisplayedCell(self: DataGridView)=value

"""

 FirstDisplayedScrollingColumnHiddenWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the width of the portion of the column that is currently scrolled out of view..



Get: FirstDisplayedScrollingColumnHiddenWidth(self: DataGridView) -> int



"""

 FirstDisplayedScrollingColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of the column that is the first column displayed on the System.Windows.Forms.DataGridView.



Get: FirstDisplayedScrollingColumnIndex(self: DataGridView) -> int



Set: FirstDisplayedScrollingColumnIndex(self: DataGridView)=value

"""

 FirstDisplayedScrollingRowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of the row that is the first row displayed on the System.Windows.Forms.DataGridView.



Get: FirstDisplayedScrollingRowIndex(self: DataGridView) -> int



Set: FirstDisplayedScrollingRowIndex(self: DataGridView)=value

"""

 Font=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the font of the text displayed by the System.Windows.Forms.DataGridView.



Get: Font(self: DataGridView) -> Font



Set: Font(self: DataGridView)=value

"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the font of the control.



"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of the System.Windows.Forms.DataGridView.



Get: ForeColor(self: DataGridView) -> Color



Set: ForeColor(self: DataGridView)=value

"""

 GridColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of the grid lines separating the cells of the System.Windows.Forms.DataGridView.



Get: GridColor(self: DataGridView) -> Color



Set: GridColor(self: DataGridView)=value

"""

 HorizontalScrollBar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the horizontal scroll bar of the control.



"""

 HorizontalScrollingOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of pixels by which the control is scrolled horizontally.



Get: HorizontalScrollingOffset(self: DataGridView) -> int



Set: HorizontalScrollingOffset(self: DataGridView)=value

"""

 ImeModeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the IME mode of a control.



"""

 IsCurrentCellDirty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current cell has uncommitted changes.



Get: IsCurrentCellDirty(self: DataGridView) -> bool



"""

 IsCurrentCellInEditMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the currently active cell is being edited.



Get: IsCurrentCellInEditMode(self: DataGridView) -> bool



"""

 IsCurrentRowDirty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current row has uncommitted changes.



Get: IsCurrentRowDirty(self: DataGridView) -> bool



"""

 MultiSelect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the user is allowed to select more than one cell,row,or column of the System.Windows.Forms.DataGridView at a time.



Get: MultiSelect(self: DataGridView) -> bool



Set: MultiSelect(self: DataGridView)=value

"""

 NewRowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the row for new records.



Get: NewRowIndex(self: DataGridView) -> int



"""

 Padding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this control.



Get: Padding(self: DataGridView) -> Padding



Set: Padding(self: DataGridView)=value

"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the user can edit the cells of the System.Windows.Forms.DataGridView control.



Get: ReadOnly(self: DataGridView) -> bool



Set: ReadOnly(self: DataGridView)=value

"""

 RenderRightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is now obsolete.



"""

 ResizeRedraw=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control redraws itself when resized.



"""

 RowCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of rows displayed in the System.Windows.Forms.DataGridView.



Get: RowCount(self: DataGridView) -> int



Set: RowCount(self: DataGridView)=value

"""

 RowHeadersBorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the border style of the row header cells.



Get: RowHeadersBorderStyle(self: DataGridView) -> DataGridViewHeaderBorderStyle



Set: RowHeadersBorderStyle(self: DataGridView)=value

"""

 RowHeadersDefaultCellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default style applied to the row header cells.



Get: RowHeadersDefaultCellStyle(self: DataGridView) -> DataGridViewCellStyle



Set: RowHeadersDefaultCellStyle(self: DataGridView)=value

"""

 RowHeadersVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the column that contains row headers is displayed.



Get: RowHeadersVisible(self: DataGridView) -> bool



Set: RowHeadersVisible(self: DataGridView)=value

"""

 RowHeadersWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width,in pixels,of the column that contains the row headers.



Get: RowHeadersWidth(self: DataGridView) -> int



Set: RowHeadersWidth(self: DataGridView)=value

"""

 RowHeadersWidthSizeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the width of the row headers is adjustable and whether it can be adjusted by the user or is automatically adjusted to fit the contents of the headers.



Get: RowHeadersWidthSizeMode(self: DataGridView) -> DataGridViewRowHeadersWidthSizeMode



Set: RowHeadersWidthSizeMode(self: DataGridView)=value

"""

 Rows=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection that contains all the rows in the System.Windows.Forms.DataGridView control.



Get: Rows(self: DataGridView) -> DataGridViewRowCollection



"""

 RowsDefaultCellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default style applied to the row cells of the System.Windows.Forms.DataGridView.



Get: RowsDefaultCellStyle(self: DataGridView) -> DataGridViewCellStyle



Set: RowsDefaultCellStyle(self: DataGridView)=value

"""

 RowTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the row that represents the template for all the rows in the control.



Get: RowTemplate(self: DataGridView) -> DataGridViewRow



Set: RowTemplate(self: DataGridView)=value

"""

 ScaleChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines the scaling of child controls.



"""

 ScrollBars=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type of scroll bars to display for the System.Windows.Forms.DataGridView control.



Get: ScrollBars(self: DataGridView) -> ScrollBars



Set: ScrollBars(self: DataGridView)=value

"""

 SelectedCells=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of cells selected by the user.



Get: SelectedCells(self: DataGridView) -> DataGridViewSelectedCellCollection



"""

 SelectedColumns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of columns selected by the user.



Get: SelectedColumns(self: DataGridView) -> DataGridViewSelectedColumnCollection



"""

 SelectedRows=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of rows selected by the user.



Get: SelectedRows(self: DataGridView) -> DataGridViewSelectedRowCollection



"""

 SelectionMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating how the cells of the System.Windows.Forms.DataGridView can be selected.



Get: SelectionMode(self: DataGridView) -> DataGridViewSelectionMode



Set: SelectionMode(self: DataGridView)=value

"""

 ShowCellErrors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to show cell errors.



Get: ShowCellErrors(self: DataGridView) -> bool



Set: ShowCellErrors(self: DataGridView)=value

"""

 ShowCellToolTips=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether or not ToolTips will show when the mouse pointer pauses on a cell.



Get: ShowCellToolTips(self: DataGridView) -> bool



Set: ShowCellToolTips(self: DataGridView)=value

"""

 ShowEditingIcon=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether or not the editing glyph is visible in the row header of the cell being edited.



Get: ShowEditingIcon(self: DataGridView) -> bool



Set: ShowEditingIcon(self: DataGridView)=value

"""

 ShowFocusCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control should display focus rectangles.



"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user interface is in the appropriate state to show or hide keyboard accelerators.



"""

 ShowRowErrors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether row headers will display error glyphs for each row that contains a data entry error.



Get: ShowRowErrors(self: DataGridView) -> bool



Set: ShowRowErrors(self: DataGridView)=value

"""

 SortedColumn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column by which the System.Windows.Forms.DataGridView contents are currently sorted.



Get: SortedColumn(self: DataGridView) -> DataGridViewColumn



"""

 SortOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the items in the System.Windows.Forms.DataGridView control are sorted in ascending or descending order,or are not sorted.



Get: SortOrder(self: DataGridView) -> SortOrder



"""

 StandardTab=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the TAB key moves the focus to the next control in the tab order rather than moving focus to the next cell in the control.



Get: StandardTab(self: DataGridView) -> bool



Set: StandardTab(self: DataGridView)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text associated with the control.



Get: Text(self: DataGridView) -> str



Set: Text(self: DataGridView)=value

"""

 TopLeftHeaderCell=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the header cell located in the upper left corner of the System.Windows.Forms.DataGridView control.



Get: TopLeftHeaderCell(self: DataGridView) -> DataGridViewHeaderCell



Set: TopLeftHeaderCell(self: DataGridView)=value

"""

 UserSetCursor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default or user-specified value of the System.Windows.Forms.Control.Cursor property.



Get: UserSetCursor(self: DataGridView) -> Cursor



"""

 VerticalScrollBar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the vertical scroll bar of the control.



"""

 VerticalScrollingOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of pixels by which the control is scrolled vertically.



Get: VerticalScrollingOffset(self: DataGridView) -> int



"""

 VirtualMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether you have provided your own data-management operations for the System.Windows.Forms.DataGridView control.



Get: VirtualMode(self: DataGridView) -> bool



Set: VirtualMode(self: DataGridView)=value

"""


 AllowUserToAddRowsChanged=None
 AllowUserToDeleteRowsChanged=None
 AllowUserToOrderColumnsChanged=None
 AllowUserToResizeColumnsChanged=None
 AllowUserToResizeRowsChanged=None
 AlternatingRowsDefaultCellStyleChanged=None
 AutoGenerateColumnsChanged=None
 AutoSizeColumnModeChanged=None
 AutoSizeColumnsModeChanged=None
 AutoSizeRowsModeChanged=None
 BackColorChanged=None
 BackgroundColorChanged=None
 BackgroundImageChanged=None
 BackgroundImageLayoutChanged=None
 BorderStyleChanged=None
 CancelRowEdit=None
 CellBeginEdit=None
 CellBorderStyleChanged=None
 CellClick=None
 CellContentClick=None
 CellContentDoubleClick=None
 CellContextMenuStripChanged=None
 CellContextMenuStripNeeded=None
 CellDoubleClick=None
 CellEndEdit=None
 CellEnter=None
 CellErrorTextChanged=None
 CellErrorTextNeeded=None
 CellFormatting=None
 CellLeave=None
 CellMouseClick=None
 CellMouseDoubleClick=None
 CellMouseDown=None
 CellMouseEnter=None
 CellMouseLeave=None
 CellMouseMove=None
 CellMouseUp=None
 CellPainting=None
 CellParsing=None
 CellStateChanged=None
 CellStyleChanged=None
 CellStyleContentChanged=None
 CellToolTipTextChanged=None
 CellToolTipTextNeeded=None
 CellValidated=None
 CellValidating=None
 CellValueChanged=None
 CellValueNeeded=None
 CellValuePushed=None
 ColumnAdded=None
 ColumnContextMenuStripChanged=None
 ColumnDataPropertyNameChanged=None
 ColumnDefaultCellStyleChanged=None
 ColumnDisplayIndexChanged=None
 ColumnDividerDoubleClick=None
 ColumnDividerWidthChanged=None
 ColumnHeaderCellChanged=None
 ColumnHeaderMouseClick=None
 ColumnHeaderMouseDoubleClick=None
 ColumnHeadersBorderStyleChanged=None
 ColumnHeadersDefaultCellStyleChanged=None
 ColumnHeadersHeightChanged=None
 ColumnHeadersHeightSizeModeChanged=None
 ColumnMinimumWidthChanged=None
 ColumnNameChanged=None
 ColumnRemoved=None
 ColumnSortModeChanged=None
 ColumnStateChanged=None
 ColumnToolTipTextChanged=None
 ColumnWidthChanged=None
 CurrentCellChanged=None
 CurrentCellDirtyStateChanged=None
 DataBindingComplete=None
 DataError=None
 DataGridViewAccessibleObject=None
 DataGridViewControlCollection=None
 DataGridViewTopRowAccessibleObject=None
 DataMemberChanged=None
 DataSourceChanged=None
 DefaultCellStyleChanged=None
 DefaultValuesNeeded=None
 EditingControlShowing=None
 EditModeChanged=None
 FontChanged=None
 ForeColorChanged=None
 GridColorChanged=None
 HitTestInfo=None
 MultiSelectChanged=None
 NewRowNeeded=None
 PaddingChanged=None
 ReadOnlyChanged=None
 RowContextMenuStripChanged=None
 RowContextMenuStripNeeded=None
 RowDefaultCellStyleChanged=None
 RowDirtyStateNeeded=None
 RowDividerDoubleClick=None
 RowDividerHeightChanged=None
 RowEnter=None
 RowErrorTextChanged=None
 RowErrorTextNeeded=None
 RowHeaderCellChanged=None
 RowHeaderMouseClick=None
 RowHeaderMouseDoubleClick=None
 RowHeadersBorderStyleChanged=None
 RowHeadersDefaultCellStyleChanged=None
 RowHeadersWidthChanged=None
 RowHeadersWidthSizeModeChanged=None
 RowHeightChanged=None
 RowHeightInfoNeeded=None
 RowHeightInfoPushed=None
 RowLeave=None
 RowMinimumHeightChanged=None
 RowPostPaint=None
 RowPrePaint=None
 RowsAdded=None
 RowsDefaultCellStyleChanged=None
 RowsRemoved=None
 RowStateChanged=None
 RowUnshared=None
 RowValidated=None
 RowValidating=None
 Scroll=None
 SelectionChanged=None
 SortCompare=None
 Sorted=None
 StyleChanged=None
 TextChanged=None
 UserAddedRow=None
 UserDeletedRow=None
 UserDeletingRow=None

