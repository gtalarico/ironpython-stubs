class DataGrid(Control,IComponent,IDisposable,IOleControl,IOleObject,IOleInPlaceObject,IOleInPlaceActiveObject,IOleWindow,IViewObject,IViewObject2,IPersist,IPersistStreamInit,IPersistPropertyBag,IPersistStorage,IQuickActivate,ISupportOleDropSource,IDropTarget,ISynchronizeInvoke,IWin32Window,IArrangedElement,IBindableComponent,ISupportInitialize,IDataGridEditingService):
 """
 Displays ADO.NET data in a scrollable grid. The System.Windows.Forms.DataGridView control replaces and adds functionality to the System.Windows.Forms.DataGrid control; however,the System.Windows.Forms.DataGrid control is retained for both backward compatibility and future use,if you choose.

 

 DataGrid()
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
 def add_RowHeaderClick(self,*args):
  """ add_RowHeaderClick(self: DataGrid,value: EventHandler) """
  pass
 def BeginEdit(self,gridColumn,rowNumber):
  """
  BeginEdit(self: DataGrid,gridColumn: DataGridColumnStyle,rowNumber: int) -> bool

  

   Attempts to put the grid into a state where editing is allowed.

  

   gridColumn: A System.Windows.Forms.DataGridColumnStyle to edit.

   rowNumber: The number of the row to edit.

   Returns: true if the method is successful; otherwise,false.
  """
  pass
 def BeginInit(self):
  """
  BeginInit(self: DataGrid)

   Begins the initialization of a System.Windows.Forms.DataGrid that is used on a form or used by 

    another component. The initialization occurs at run time.
  """
  pass
 def CancelEditing(self,*args):
  """
  CancelEditing(self: DataGrid)

   Cancels the current edit operation and rolls back all changes.
  """
  pass
 def Collapse(self,row):
  """
  Collapse(self: DataGrid,row: int)

   Collapses child relations,if any exist for all rows,or for a specified row.

  

   row: The number of the row to collapse. If set to -1,all rows are collapsed.
  """
  pass
 def ColumnStartedEditing(self,*args):
  """
  ColumnStartedEditing(self: DataGrid,editingControl: Control)

   Informs the System.Windows.Forms.DataGrid control when the user begins to edit a column using 

    the specified control.

  

  

   editingControl: The System.Windows.Forms.Control used to edit the column.

  ColumnStartedEditing(self: DataGrid,bounds: Rectangle)

   Informs the System.Windows.Forms.DataGrid control when the user begins to edit the column at the 

    specified location.

  

  

   bounds: The System.Drawing.Rectangle that defines the location of the edited column.
  """
  pass
 def CreateAccessibilityInstance(self,*args):
  """
  CreateAccessibilityInstance(self: DataGrid) -> AccessibleObject

  

   Constructs a new instance of the accessibility object for this control.

   Returns: The System.Windows.Forms.Control.ControlAccessibleObject for this control.
  """
  pass
 def CreateControlsInstance(self,*args):
  """
  CreateControlsInstance(self: Control) -> ControlCollection

  

   Creates a new instance of the control collection for the control.

   Returns: A new instance of System.Windows.Forms.Control.ControlCollection assigned to the control.
  """
  pass
 def CreateGridColumn(self,*args):
  """
  CreateGridColumn(self: DataGrid,prop: PropertyDescriptor) -> DataGridColumnStyle

  

   Creates a new System.Windows.Forms.DataGridColumnStyle with the specified 

    System.ComponentModel.PropertyDescriptor.

  

  

   prop: The System.ComponentModel.PropertyDescriptor to use for creating the grid column style.

   Returns: The new System.Windows.Forms.DataGridColumnStyle.

  CreateGridColumn(self: DataGrid,prop: PropertyDescriptor,isDefault: bool) -> DataGridColumnStyle

  

   Creates a System.Windows.Forms.DataGridColumnStyle using the specified 

    System.ComponentModel.PropertyDescriptor.

  

  

   prop: The System.ComponentModel.PropertyDescriptor to use for creating the grid column style.

   isDefault: true to set the column style as the default; otherwise,false.

   Returns: The new System.Windows.Forms.DataGridColumnStyle.
  """
  pass
 def CreateHandle(self,*args):
  """
  CreateHandle(self: Control)

   Creates a handle for the control.
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
 def Dispose(self):
  """
  Dispose(self: DataGrid,disposing: bool)

   Disposes of the resources (other than memory) used by the System.Windows.Forms.DataGrid.

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def EndEdit(self,gridColumn,rowNumber,shouldAbort):
  """
  EndEdit(self: DataGrid,gridColumn: DataGridColumnStyle,rowNumber: int,shouldAbort: bool) -> bool

  

   Requests an end to an edit operation taking place on the System.Windows.Forms.DataGrid control.

  

   gridColumn: The System.Windows.Forms.DataGridColumnStyle to cease editing.

   rowNumber: The number of the row to cease editing.

   shouldAbort: Set to true if the current operation should be stopped.

   Returns: true if the editing operation ceases; otherwise,false.
  """
  pass
 def EndInit(self):
  """
  EndInit(self: DataGrid)

   Ends the initialization of a System.Windows.Forms.DataGrid that is used on a form or used by 

    another component. The initialization occurs at run time.
  """
  pass
 def Expand(self,row):
  """
  Expand(self: DataGrid,row: int)

   Displays child relations,if any exist,for all rows or a specific row.

  

   row: The number of the row to expand. If set to -1,all rows are expanded.
  """
  pass
 def GetAccessibilityObjectById(self,*args):
  """
  GetAccessibilityObjectById(self: Control,objectId: int) -> AccessibleObject

  

   Retrieves the specified System.Windows.Forms.AccessibleObject.

  

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
 def GetCellBounds(self,*__args):
  """
  GetCellBounds(self: DataGrid,dgc: DataGridCell) -> Rectangle

  

   Gets the System.Drawing.Rectangle of the cell specified by System.Windows.Forms.DataGridCell.

  

   dgc: The System.Windows.Forms.DataGridCell to look up.

   Returns: A System.Drawing.Rectangle that defines the current cell's corners.

  GetCellBounds(self: DataGrid,row: int,col: int) -> Rectangle

  

   Gets the System.Drawing.Rectangle of the cell specified by row and column number.

  

   row: The number of the cell's row.

   col: The number of the cell's column.

   Returns: A System.Drawing.Rectangle that defines the current cell's corners.
  """
  pass
 def GetCurrentCellBounds(self):
  """
  GetCurrentCellBounds(self: DataGrid) -> Rectangle

  

   Gets a System.Drawing.Rectangle that specifies the four corners of the selected cell.

   Returns: A System.Drawing.Rectangle that defines the current cell's corners.
  """
  pass
 def GetOutputTextDelimiter(self,*args):
  """
  GetOutputTextDelimiter(self: DataGrid) -> str

  

   Gets the string that is the delimiter between columns when row contents are copied to the 

    Clipboard.

  

   Returns: The string value "\t",which represents a tab used to separate columns in a row.
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
 def GridHScrolled(self,*args):
  """
  GridHScrolled(self: DataGrid,sender: object,se: ScrollEventArgs)

   Listens for the scroll event of the horizontal scroll bar.

  

   sender: An System.Object that contains data about the control.

   se: A System.Windows.Forms.ScrollEventArgs that contains the event data.
  """
  pass
 def GridVScrolled(self,*args):
  """
  GridVScrolled(self: DataGrid,sender: object,se: ScrollEventArgs)

   Listens for the scroll event of the vertical scroll bar.

  

   sender: An System.Object that contains data about the control.

   se: A System.Windows.Forms.ScrollEventArgs that contains the event data.
  """
  pass
 def HitTest(self,*__args):
  """
  HitTest(self: DataGrid,position: Point) -> HitTestInfo

  

   Gets information,such as row and column number of a clicked point on the grid,about the grid 

    using a specific System.Drawing.Point.

  

  

   position: A System.Drawing.Point that represents single x,y coordinate.

   Returns: A System.Windows.Forms.DataGrid.HitTestInfo that contains specific information about the grid.

  HitTest(self: DataGrid,x: int,y: int) -> HitTestInfo

  

   Gets information,such as row and column number of a clicked point on the grid,using the x and 

    y coordinate passed to the method.

  

  

   x: The horizontal position of the coordinate.

   y: The vertical position of the coordinate.

   Returns: A System.Windows.Forms.DataGrid.HitTestInfo that contains information about the clicked part of 

    the grid.
  """
  pass
 def InitLayout(self,*args):
  """
  InitLayout(self: Control)

   Called after the control has been added to another container.
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
 def IsExpanded(self,rowNumber):
  """
  IsExpanded(self: DataGrid,rowNumber: int) -> bool

  

   Gets a value that indicates whether the node of a specified row is expanded or collapsed.

  

   rowNumber: The number of the row in question.

   Returns: true if the node is expanded; otherwise,false.
  """
  pass
 def IsInputChar(self,*args):
  """
  IsInputChar(self: Control,charCode: Char) -> bool

  

   Determines if a character is an input character that the control recognizes.

  

   charCode: The character to test.

   Returns: true if the character should be sent directly to the control and not preprocessed; otherwise,

    false.
  """
  pass
 def IsInputKey(self,*args):
  """
  IsInputKey(self: Control,keyData: Keys) -> bool

  

   Determines whether the specified key is a regular input key or a special key that requires 

    preprocessing.

  

  

   keyData: One of the System.Windows.Forms.Keys values.

   Returns: true if the specified key is a regular input key; otherwise,false.
  """
  pass
 def IsSelected(self,row):
  """
  IsSelected(self: DataGrid,row: int) -> bool

  

   Gets a value indicating whether a specified row is selected.

  

   row: The number of the row you are interested in.

   Returns: true if the row is selected; otherwise,false.
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
 def NavigateBack(self):
  """
  NavigateBack(self: DataGrid)

   Navigates back to the table previously displayed in the grid.
  """
  pass
 def NavigateTo(self,rowNumber,relationName):
  """
  NavigateTo(self: DataGrid,rowNumber: int,relationName: str)

   Navigates to the table specified by row and relation name.

  

   rowNumber: The number of the row to navigate to.

   relationName: The name of the child relation to navigate to.
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
 def OnAllowNavigationChanged(self,*args):
  """
  OnAllowNavigationChanged(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.DataGrid.AllowNavigationChanged event.

  

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
 def OnBackButtonClicked(self,*args):
  """
  OnBackButtonClicked(self: DataGrid,sender: object,e: EventArgs)

   Listens for the caption's back button clicked event.

  

   sender: An System.Object that contains data about the control.

   e: An System.EventArgs that contains data about the event.
  """
  pass
 def OnBackColorChanged(self,*args):
  """
  OnBackColorChanged(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.Control.BackColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBackgroundColorChanged(self,*args):
  """
  OnBackgroundColorChanged(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.DataGrid.BackgroundColorChanged event.

  

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
  OnBindingContextChanged(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.Control.BindingContextChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBorderStyleChanged(self,*args):
  """
  OnBorderStyleChanged(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.DataGrid.BorderStyleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnCaptionVisibleChanged(self,*args):
  """
  OnCaptionVisibleChanged(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.DataGrid.CaptionVisibleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnCausesValidationChanged(self,*args):
  """
  OnCausesValidationChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.CausesValidationChanged event.

  

   e: An System.EventArgs that contains the event data.
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
  OnCurrentCellChanged(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.DataGrid.CurrentCellChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnCursorChanged(self,*args):
  """
  OnCursorChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.CursorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDataSourceChanged(self,*args):
  """
  OnDataSourceChanged(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.DataGrid.DataSourceChanged event.

  

   e: An System.EventArgs that contains the event data.
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
  OnDoubleClick(self: Control,e: EventArgs)

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
 def OnEnabledChanged(self,*args):
  """
  OnEnabledChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.EnabledChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnEnter(self,*args):
  """
  OnEnter(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.Control.Enter event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnFlatModeChanged(self,*args):
  """
  OnFlatModeChanged(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.DataGrid.FlatModeChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnFontChanged(self,*args):
  """
  OnFontChanged(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.Control.FontChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnForeColorChanged(self,*args):
  """
  OnForeColorChanged(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.Control.ForeColorChanged event.

  

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
  OnGotFocus(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.GotFocus event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleCreated(self,*args):
  """
  OnHandleCreated(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.Control.CreateHandle event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleDestroyed(self,*args):
  """
  OnHandleDestroyed(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.Control.DestroyHandle event.

  

   e: An System.EventArgs containing the event data.
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
  OnKeyDown(self: DataGrid,ke: KeyEventArgs)

   Raises the System.Windows.Forms.Control.KeyDown event.

  

   ke: A System.Windows.Forms.KeyEventArgs that provides data about the 

    System.Windows.Forms.Control.OnKeyDown(System.Windows.Forms.KeyEventArgs) event.
  """
  pass
 def OnKeyPress(self,*args):
  """
  OnKeyPress(self: DataGrid,kpe: KeyPressEventArgs)

   Raises the System.Windows.Forms.Control.KeyPress event.

  

   kpe: A System.Windows.Forms.KeyPressEventArgs that contains data about the 

    System.Windows.Forms.Control.OnKeyPress(System.Windows.Forms.KeyPressEventArgs) event
  """
  pass
 def OnKeyUp(self,*args):
  """
  OnKeyUp(self: Control,e: KeyEventArgs)

   Raises the System.Windows.Forms.Control.KeyUp event.

  

   e: A System.Windows.Forms.KeyEventArgs that contains the event data.
  """
  pass
 def OnLayout(self,*args):
  """
  OnLayout(self: DataGrid,levent: LayoutEventArgs)

   Raises the System.Windows.Forms.Control.Layout event,which repositions controls and updates 

    scroll bars.

  

  

   levent: A System.Windows.Forms.LayoutEventArgs that contains the event data.
  """
  pass
 def OnLeave(self,*args):
  """
  OnLeave(self: DataGrid,e: EventArgs)

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
  OnLostFocus(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.LostFocus event.

  

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
  OnMouseClick(self: Control,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseClick event.

  

   e: An System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseDoubleClick(self,*args):
  """
  OnMouseDoubleClick(self: Control,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseDoubleClick event.

  

   e: An System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseDown(self,*args):
  """
  OnMouseDown(self: DataGrid,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseDown event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains data about the 

    System.Windows.Forms.Control.OnMouseDown(System.Windows.Forms.MouseEventArgs) event.
  """
  pass
 def OnMouseEnter(self,*args):
  """
  OnMouseEnter(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.MouseEnter event.

  

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
  OnMouseLeave(self: DataGrid,e: EventArgs)

   Creates the System.Windows.Forms.Control.MouseLeave event.

  

   e: An System.EventArgs that contains data about the 

    System.Windows.Forms.Control.OnMouseLeave(System.EventArgs) event.
  """
  pass
 def OnMouseMove(self,*args):
  """
  OnMouseMove(self: DataGrid,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseMove event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains data about the 

    System.Windows.Forms.Control.OnMouseMove(System.Windows.Forms.MouseEventArgs) event.
  """
  pass
 def OnMouseUp(self,*args):
  """
  OnMouseUp(self: DataGrid,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseUp event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains data about the 

    System.Windows.Forms.Control.OnMouseUp(System.Windows.Forms.MouseEventArgs) event.
  """
  pass
 def OnMouseWheel(self,*args):
  """
  OnMouseWheel(self: DataGrid,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseWheel event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains data about the 

    System.Windows.Forms.Control.OnMouseUp(System.Windows.Forms.MouseEventArgs) event.
  """
  pass
 def OnMove(self,*args):
  """
  OnMove(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.Move event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnNavigate(self,*args):
  """
  OnNavigate(self: DataGrid,e: NavigateEventArgs)

   Raises the System.Windows.Forms.DataGrid.Navigate event.

  

   e: A System.Windows.Forms.NavigateEventArgs that contains the event data.
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
  OnPaint(self: DataGrid,pe: PaintEventArgs)

   Raises the System.Windows.Forms.Control.Paint event.

  

   pe: A System.Windows.Forms.PaintEventArgs which contains data about the event.
  """
  pass
 def OnPaintBackground(self,*args):
  """
  OnPaintBackground(self: DataGrid,ebe: PaintEventArgs)

   Overrides System.Windows.Forms.Control.OnPaintBackground(System.Windows.Forms.PaintEventArgs) to 

    prevent painting the background of the System.Windows.Forms.DataGrid control.

  

  

   ebe: A System.Windows.Forms.PaintEventArgs that contains information about the control to paint.
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
 def OnParentRowsLabelStyleChanged(self,*args):
  """
  OnParentRowsLabelStyleChanged(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.DataGrid.ParentRowsLabelStyleChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentRowsVisibleChanged(self,*args):
  """
  OnParentRowsVisibleChanged(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.DataGrid.ParentRowsVisibleChanged event.

  

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
  OnReadOnlyChanged(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.DataGrid.ReadOnlyChanged event

  

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
  OnResize(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.Control.Resize event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRightToLeftChanged(self,*args):
  """
  OnRightToLeftChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.RightToLeftChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRowHeaderClick(self,*args):
  """
  OnRowHeaderClick(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.DataGrid.RowHeaderClick event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnScroll(self,*args):
  """
  OnScroll(self: DataGrid,e: EventArgs)

   Raises the System.Windows.Forms.DataGrid.Scroll event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnShowParentDetailsButtonClicked(self,*args):
  """
  OnShowParentDetailsButtonClicked(self: DataGrid,sender: object,e: EventArgs)

   Raises the System.Windows.Forms.DataGrid.ShowParentDetailsButtonClick event.

  

   sender: The source of the event.

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnSizeChanged(self,*args):
  """
  OnSizeChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.SizeChanged event.

  

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
 def OnValidated(self,*args):
  """
  OnValidated(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.Validated event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnValidating(self,*args):
  """
  OnValidating(self: Control,e: CancelEventArgs)

   Raises the System.Windows.Forms.Control.Validating event.

  

   e: A System.ComponentModel.CancelEventArgs that contains the event data.
  """
  pass
 def OnVisibleChanged(self,*args):
  """
  OnVisibleChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.VisibleChanged event.

  

   e: An System.EventArgs that contains the event data.
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
  ProcessDialogKey(self: DataGrid,keyData: Keys) -> bool

  

   Gets or sets a value that indicates whether a key should be processed further.

  

   keyData: A System.Windows.Forms.Keys that contains data about the pressed key.

   Returns: true,the key should be processed; otherwise,false.
  """
  pass
 def ProcessGridKey(self,*args):
  """
  ProcessGridKey(self: DataGrid,ke: KeyEventArgs) -> bool

  

   Processes keys for grid navigation.

  

   ke: A System.Windows.Forms.KeyEventArgs that contains data about the key up or key down event.

   Returns: true,if the key was processed; otherwise false.
  """
  pass
 def ProcessKeyEventArgs(self,*args):
  """
  ProcessKeyEventArgs(self: Control,m: Message) -> (bool,Message)

  

   Processes a key message and generates the appropriate control events.

  

   m: A System.Windows.Forms.Message,passed by reference,that represents the window message to 

    process.

  

   Returns: true if the message was processed by the control; otherwise,false.
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
  ProcessKeyPreview(self: DataGrid,m: Message) -> (bool,Message)

  

   Previews a keyboard message and returns a value indicating if the key was consumed.

  

   m: A System.Windows.Forms.Message that contains data about the event. The parameter is passed by 

    reference.

  

   Returns: true,if the key was consumed; otherwise,false.
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
 def ProcessTabKey(self,*args):
  """
  ProcessTabKey(self: DataGrid,keyData: Keys) -> bool

  

   Gets a value indicating whether the Tab key should be processed.

  

   keyData: A System.Windows.Forms.Keys that contains data about which the pressed key.

   Returns: true if the TAB key should be processed; otherwise,false.
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
 def remove_RowHeaderClick(self,*args):
  """ remove_RowHeaderClick(self: DataGrid,value: EventHandler) """
  pass
 def RescaleConstantsForDpi(self,*args):
  """ RescaleConstantsForDpi(self: Control,deviceDpiOld: int,deviceDpiNew: int) """
  pass
 def ResetAlternatingBackColor(self):
  """
  ResetAlternatingBackColor(self: DataGrid)

   Resets the System.Windows.Forms.DataGrid.AlternatingBackColor property to its default color.
  """
  pass
 def ResetBackColor(self):
  """
  ResetBackColor(self: DataGrid)

   Resets the System.Windows.Forms.DataGrid.BackColor property to its default value.
  """
  pass
 def ResetForeColor(self):
  """
  ResetForeColor(self: DataGrid)

   Resets the System.Windows.Forms.DataGrid.ForeColor property to its default value.
  """
  pass
 def ResetGridLineColor(self):
  """
  ResetGridLineColor(self: DataGrid)

   Resets the System.Windows.Forms.DataGrid.GridLineColor property to its default value.
  """
  pass
 def ResetHeaderBackColor(self):
  """
  ResetHeaderBackColor(self: DataGrid)

   Resets the System.Windows.Forms.DataGrid.HeaderBackColor property to its default value.
  """
  pass
 def ResetHeaderFont(self):
  """
  ResetHeaderFont(self: DataGrid)

   Resets the System.Windows.Forms.DataGrid.HeaderFont property to its default value.
  """
  pass
 def ResetHeaderForeColor(self):
  """
  ResetHeaderForeColor(self: DataGrid)

   Resets the System.Windows.Forms.DataGrid.HeaderForeColor property to its default value.
  """
  pass
 def ResetLinkColor(self):
  """
  ResetLinkColor(self: DataGrid)

   Resets the System.Windows.Forms.DataGrid.LinkColor property to its default value.
  """
  pass
 def ResetLinkHoverColor(self):
  """
  ResetLinkHoverColor(self: DataGrid)

   Resets the System.Windows.Forms.DataGrid.LinkHoverColor property to its default value.
  """
  pass
 def ResetMouseEventArgs(self,*args):
  """
  ResetMouseEventArgs(self: Control)

   Resets the control to handle the System.Windows.Forms.Control.MouseLeave event.
  """
  pass
 def ResetSelection(self,*args):
  """
  ResetSelection(self: DataGrid)

   Turns off selection for all rows that are selected.
  """
  pass
 def ResetSelectionBackColor(self):
  """
  ResetSelectionBackColor(self: DataGrid)

   Resets the System.Windows.Forms.DataGrid.SelectionBackColor property to its default value.
  """
  pass
 def ResetSelectionForeColor(self):
  """
  ResetSelectionForeColor(self: DataGrid)

   Resets the System.Windows.Forms.DataGrid.SelectionForeColor property to its default value.
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
 def Select(self,row=None):
  """
  Select(self: DataGrid,row: int)

   Selects a specified row.

  

   row: The index of the row to select.
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
  SetBoundsCore(self: Control,x: int,y: int,width: int,height: int,specified: BoundsSpecified)

   Performs the work of setting the specified bounds of this control.

  

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
 def SetDataBinding(self,dataSource,dataMember):
  """
  SetDataBinding(self: DataGrid,dataSource: object,dataMember: str)

   Sets the System.Windows.Forms.DataGrid.DataSource and System.Windows.Forms.DataGrid.DataMember 

    properties at run time.

  

  

   dataSource: The data source for the System.Windows.Forms.DataGrid control.

   dataMember: The System.Windows.Forms.DataGrid.DataMember string that specifies the table to bind to within 

    the object returned by the System.Windows.Forms.DataGrid.DataSource property.
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
 def ShouldSerializeAlternatingBackColor(self,*args):
  """
  ShouldSerializeAlternatingBackColor(self: DataGrid) -> bool

  

   Indicates whether the System.Windows.Forms.DataGrid.AlternatingBackColor property should be 

    persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeBackgroundColor(self,*args):
  """
  ShouldSerializeBackgroundColor(self: DataGrid) -> bool

  

   Indicates whether the System.Windows.Forms.DataGrid.BackgroundColor property should be persisted.

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeCaptionBackColor(self,*args):
  """
  ShouldSerializeCaptionBackColor(self: DataGrid) -> bool

  

   Gets a value indicating whether the System.Windows.Forms.DataGrid.CaptionBackColor property 

    should be persisted.

  

   Returns: true if the property value has been changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeCaptionForeColor(self,*args):
  """
  ShouldSerializeCaptionForeColor(self: DataGrid) -> bool

  

   Gets a value indicating whether the System.Windows.Forms.DataGrid.CaptionForeColor property 

    should be persisted.

  

   Returns: true if the property value has been changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeGridLineColor(self,*args):
  """
  ShouldSerializeGridLineColor(self: DataGrid) -> bool

  

   Indicates whether the System.Windows.Forms.DataGrid.GridLineColor property should be persisted.

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeHeaderBackColor(self,*args):
  """
  ShouldSerializeHeaderBackColor(self: DataGrid) -> bool

  

   Indicates whether the System.Windows.Forms.DataGrid.HeaderBackColor property should be persisted.

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeHeaderFont(self,*args):
  """
  ShouldSerializeHeaderFont(self: DataGrid) -> bool

  

   Indicates whether the System.Windows.Forms.DataGrid.HeaderFont property should be persisted.

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeHeaderForeColor(self,*args):
  """
  ShouldSerializeHeaderForeColor(self: DataGrid) -> bool

  

   Indicates whether the System.Windows.Forms.DataGrid.HeaderForeColor property should be persisted.

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeLinkHoverColor(self,*args):
  """
  ShouldSerializeLinkHoverColor(self: DataGrid) -> bool

  

   Indicates whether the System.Windows.Forms.DataGrid.LinkHoverColor property should be persisted.

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeParentRowsBackColor(self,*args):
  """
  ShouldSerializeParentRowsBackColor(self: DataGrid) -> bool

  

   Indicates whether the System.Windows.Forms.DataGrid.ParentRowsBackColor property should be 

    persisted.

  

   Returns: true if the property value has been changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeParentRowsForeColor(self,*args):
  """
  ShouldSerializeParentRowsForeColor(self: DataGrid) -> bool

  

   Indicates whether the System.Windows.Forms.DataGrid.ParentRowsForeColor property should be 

    persisted.

  

   Returns: true if the property value has been changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializePreferredRowHeight(self,*args):
  """
  ShouldSerializePreferredRowHeight(self: DataGrid) -> bool

  

   Indicates whether the System.Windows.Forms.DataGrid.PreferredRowHeight property should be 

    persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeSelectionBackColor(self,*args):
  """
  ShouldSerializeSelectionBackColor(self: DataGrid) -> bool

  

   Indicates whether the System.Windows.Forms.DataGrid.SelectionBackColor property should be 

    persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
  """
  pass
 def ShouldSerializeSelectionForeColor(self,*args):
  """
  ShouldSerializeSelectionForeColor(self: DataGrid) -> bool

  

   Indicates whether the System.Windows.Forms.DataGrid.SelectionForeColor property should be 

    persisted.

  

   Returns: true if the property value has changed from its default; otherwise,false.
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
 def SubObjectsSiteChange(self,site):
  """
  SubObjectsSiteChange(self: DataGrid,site: bool)

   Adds or removes the System.Windows.Forms.DataGridTableStyle objects from the container that is 

    associated with the System.Windows.Forms.DataGrid.

  

  

   site: true to add the System.Windows.Forms.DataGridTableStyle objects to a container; false to remove 

    them.
  """
  pass
 def UnSelect(self,row):
  """
  UnSelect(self: DataGrid,row: int)

   Unselects a specified row.

  

   row: The index of the row to deselect.
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
  WndProc(self: Control,m: Message) -> Message

  

   Processes Windows messages.

  

   m: The Windows System.Windows.Forms.Message to process.
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
 AllowNavigation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether navigation is allowed.



Get: AllowNavigation(self: DataGrid) -> bool



Set: AllowNavigation(self: DataGrid)=value

"""

 AllowSorting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the grid can be resorted by clicking on a column header.



Get: AllowSorting(self: DataGrid) -> bool



Set: AllowSorting(self: DataGrid)=value

"""

 AlternatingBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of odd-numbered rows of the grid.



Get: AlternatingBackColor(self: DataGrid) -> Color



Set: AlternatingBackColor(self: DataGrid)=value

"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of even-numbered rows of the grid.



Get: BackColor(self: DataGrid) -> Color



Set: BackColor(self: DataGrid)=value

"""

 BackgroundColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of the non-row area of the grid.



Get: BackgroundColor(self: DataGrid) -> Color



Set: BackgroundColor(self: DataGrid)=value

"""

 BackgroundImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This member is not meaningful for this control.



Get: BackgroundImage(self: DataGrid) -> Image



Set: BackgroundImage(self: DataGrid)=value

"""

 BackgroundImageLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This member is not meaningful for this control.



Get: BackgroundImageLayout(self: DataGrid) -> ImageLayout



Set: BackgroundImageLayout(self: DataGrid)=value

"""

 BorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the grid's border style.



Get: BorderStyle(self: DataGrid) -> BorderStyle



Set: BorderStyle(self: DataGrid)=value

"""

 CanEnableIme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value,to enable IME support.



"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if events can be raised on the control.



"""

 CaptionBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of the caption area.



Get: CaptionBackColor(self: DataGrid) -> Color



Set: CaptionBackColor(self: DataGrid)=value

"""

 CaptionFont=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the font of the grid's caption.



Get: CaptionFont(self: DataGrid) -> Font



Set: CaptionFont(self: DataGrid)=value

"""

 CaptionForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of the caption area.



Get: CaptionForeColor(self: DataGrid) -> Color



Set: CaptionForeColor(self: DataGrid)=value

"""

 CaptionText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text of the grid's window caption.



Get: CaptionText(self: DataGrid) -> str



Set: CaptionText(self: DataGrid)=value

"""

 CaptionVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the grid's caption is visible.



Get: CaptionVisible(self: DataGrid) -> bool



Set: CaptionVisible(self: DataGrid)=value

"""

 ColumnHeadersVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the column headers of a table are visible.



Get: ColumnHeadersVisible(self: DataGrid) -> bool



Set: ColumnHeadersVisible(self: DataGrid)=value

"""

 CreateParams=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the required creation parameters when the control handle is created.



"""

 CurrentCell=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets which cell has the focus. Not available at design time.



Get: CurrentCell(self: DataGrid) -> DataGridCell



Set: CurrentCell(self: DataGrid)=value

"""

 CurrentRowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets index of the row that currently has focus.



Get: CurrentRowIndex(self: DataGrid) -> int



Set: CurrentRowIndex(self: DataGrid)=value

"""

 Cursor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This member is not meaningful for this control.



Get: Cursor(self: DataGrid) -> Cursor



Set: Cursor(self: DataGrid)=value

"""

 DataMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the specific list in a System.Windows.Forms.DataGrid.DataSource for which the System.Windows.Forms.DataGrid control displays a grid.



Get: DataMember(self: DataGrid) -> str



Set: DataMember(self: DataGrid)=value

"""

 DataSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the data source that the grid is displaying data for.



Get: DataSource(self: DataGrid) -> object



Set: DataSource(self: DataGrid)=value

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
 """Gets the default size of the control.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 DoubleBuffered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this control should redraw its surface using a secondary buffer to reduce or prevent flicker.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 FirstVisibleColumn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the first visible column in a grid.



Get: FirstVisibleColumn(self: DataGrid) -> int



"""

 FlatMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the grid displays in flat mode.



Get: FlatMode(self: DataGrid) -> bool



Set: FlatMode(self: DataGrid)=value

"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color (typically the color of the text) property of the System.Windows.Forms.DataGrid control.



Get: ForeColor(self: DataGrid) -> Color



Set: ForeColor(self: DataGrid)=value

"""

 GridLineColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of the grid lines.



Get: GridLineColor(self: DataGrid) -> Color



Set: GridLineColor(self: DataGrid)=value

"""

 GridLineStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the line style of the grid.



Get: GridLineStyle(self: DataGrid) -> DataGridLineStyle



Set: GridLineStyle(self: DataGrid)=value

"""

 HeaderBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of all row and column headers.



Get: HeaderBackColor(self: DataGrid) -> Color



Set: HeaderBackColor(self: DataGrid)=value

"""

 HeaderFont=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the font used for column headers.



Get: HeaderFont(self: DataGrid) -> Font



Set: HeaderFont(self: DataGrid)=value

"""

 HeaderForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of headers.



Get: HeaderForeColor(self: DataGrid) -> Color



Set: HeaderForeColor(self: DataGrid)=value

"""

 HorizScrollBar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the horizontal scroll bar for the grid.



"""

 ImeModeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the IME mode of a control.



"""

 LinkColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of the text that you can click to navigate to a child table.



Get: LinkColor(self: DataGrid) -> Color



Set: LinkColor(self: DataGrid)=value

"""

 LinkHoverColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This member is not meaningful for this control.



Get: LinkHoverColor(self: DataGrid) -> Color



Set: LinkHoverColor(self: DataGrid)=value

"""

 ListManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.CurrencyManager for this System.Windows.Forms.DataGrid control.



"""

 ParentRowsBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of parent rows.



Get: ParentRowsBackColor(self: DataGrid) -> Color



Set: ParentRowsBackColor(self: DataGrid)=value

"""

 ParentRowsForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of parent rows.



Get: ParentRowsForeColor(self: DataGrid) -> Color



Set: ParentRowsForeColor(self: DataGrid)=value

"""

 ParentRowsLabelStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the way parent row labels are displayed.



Get: ParentRowsLabelStyle(self: DataGrid) -> DataGridParentRowsLabelStyle



Set: ParentRowsLabelStyle(self: DataGrid)=value

"""

 ParentRowsVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the parent rows of a table are visible.



Get: ParentRowsVisible(self: DataGrid) -> bool



Set: ParentRowsVisible(self: DataGrid)=value

"""

 PreferredColumnWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default width of the grid columns in pixels.



Get: PreferredColumnWidth(self: DataGrid) -> int



Set: PreferredColumnWidth(self: DataGrid)=value

"""

 PreferredRowHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the preferred row height for the System.Windows.Forms.DataGrid control.



Get: PreferredRowHeight(self: DataGrid) -> int



Set: PreferredRowHeight(self: DataGrid)=value

"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the grid is in read-only mode.



Get: ReadOnly(self: DataGrid) -> bool



Set: ReadOnly(self: DataGrid)=value

"""

 RenderRightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is now obsolete.



"""

 ResizeRedraw=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control redraws itself when resized.



"""

 RowHeadersVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that specifies whether row headers are visible.



Get: RowHeadersVisible(self: DataGrid) -> bool



Set: RowHeadersVisible(self: DataGrid)=value

"""

 RowHeaderWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of row headers.



Get: RowHeaderWidth(self: DataGrid) -> int



Set: RowHeaderWidth(self: DataGrid)=value

"""

 ScaleChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines the scaling of child controls.



"""

 SelectionBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of selected rows.



Get: SelectionBackColor(self: DataGrid) -> Color



Set: SelectionBackColor(self: DataGrid)=value

"""

 SelectionForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or set the foreground color of selected rows.



Get: SelectionForeColor(self: DataGrid) -> Color



Set: SelectionForeColor(self: DataGrid)=value

"""

 ShowFocusCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control should display focus rectangles.



"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user interface is in the appropriate state to show or hide keyboard accelerators.



"""

 Site=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Site(self: DataGrid) -> ISite



Set: Site(self: DataGrid)=value

"""

 TableStyles=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of System.Windows.Forms.DataGridTableStyle objects for the grid.



Get: TableStyles(self: DataGrid) -> GridTableStylesCollection



"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This member is not meaningful for this control.



Get: Text(self: DataGrid) -> str



Set: Text(self: DataGrid)=value

"""

 VertScrollBar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the vertical scroll bar of the control.



"""

 VisibleColumnCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of visible columns.



Get: VisibleColumnCount(self: DataGrid) -> int



"""

 VisibleRowCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of rows visible.



Get: VisibleRowCount(self: DataGrid) -> int



"""


 AllowNavigationChanged=None
 BackButtonClick=None
 BackgroundColorChanged=None
 BackgroundImageChanged=None
 BackgroundImageLayoutChanged=None
 BorderStyleChanged=None
 CaptionVisibleChanged=None
 CurrentCellChanged=None
 CursorChanged=None
 DataSourceChanged=None
 FlatModeChanged=None
 HitTestInfo=None
 HitTestType=None
 Navigate=None
 ParentRowsLabelStyleChanged=None
 ParentRowsVisibleChanged=None
 ReadOnlyChanged=None
 Scroll=None
 ShowParentDetailsButtonClick=None
 TextChanged=None

