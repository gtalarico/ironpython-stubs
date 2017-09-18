class ListView(Control,IComponent,IDisposable,IOleControl,IOleObject,IOleInPlaceObject,IOleInPlaceActiveObject,IOleWindow,IViewObject,IViewObject2,IPersist,IPersistStreamInit,IPersistPropertyBag,IPersistStorage,IQuickActivate,ISupportOleDropSource,IDropTarget,ISynchronizeInvoke,IWin32Window,IArrangedElement,IBindableComponent):
 """
 Represents a Windows list view control,which displays a collection of items that can be displayed using one of four different views.

 

 ListView()
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
 def ArrangeIcons(self,value=None):
  """
  ArrangeIcons(self: ListView)

   Arranges items in the control when they are displayed as icons based on the value of the 

    System.Windows.Forms.ListView.Alignment property.

  

  ArrangeIcons(self: ListView,value: ListViewAlignment)

   Arranges items in the control when they are displayed as icons with a specified alignment 

    setting.

  

  

   value: One of the System.Windows.Forms.ListViewAlignment values.
  """
  pass
 def AutoResizeColumn(self,columnIndex,headerAutoResize):
  """
  AutoResizeColumn(self: ListView,columnIndex: int,headerAutoResize: ColumnHeaderAutoResizeStyle)

   Resizes the width of the given column as indicated by the resize style.

  

   columnIndex: The zero-based index of the column to resize.

   headerAutoResize: One of the System.Windows.Forms.ColumnHeaderAutoResizeStyle values.
  """
  pass
 def AutoResizeColumns(self,headerAutoResize):
  """
  AutoResizeColumns(self: ListView,headerAutoResize: ColumnHeaderAutoResizeStyle)

   Resizes the width of the columns as indicated by the resize style.

  

   headerAutoResize: One of the System.Windows.Forms.ColumnHeaderAutoResizeStyle values.
  """
  pass
 def BeginUpdate(self):
  """
  BeginUpdate(self: ListView)

   Prevents the control from drawing until the System.Windows.Forms.ListView.EndUpdate method is 

    called.
  """
  pass
 def Clear(self):
  """
  Clear(self: ListView)

   Removes all items and columns from the control.
  """
  pass
 def CreateAccessibilityInstance(self,*args):
  """
  CreateAccessibilityInstance(self: Control) -> AccessibleObject

  

   Creates a new accessibility object for the control.

   Returns: A new System.Windows.Forms.AccessibleObject for the control.
  """
  pass
 def CreateControlsInstance(self,*args):
  """
  CreateControlsInstance(self: Control) -> ControlCollection

  

   Creates a new instance of the control collection for the control.

   Returns: A new instance of System.Windows.Forms.Control.ControlCollection assigned to the control.
  """
  pass
 def CreateHandle(self,*args):
  """ CreateHandle(self: ListView) """
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
  Dispose(self: ListView,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.ListView and optionally 

    releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def EndUpdate(self):
  """
  EndUpdate(self: ListView)

   Resumes drawing of the list view control after drawing is suspended by the 

    System.Windows.Forms.ListView.BeginUpdate method.
  """
  pass
 def EnsureVisible(self,index):
  """
  EnsureVisible(self: ListView,index: int)

   Ensures that the specified item is visible within the control,scrolling the contents of the 

    control if necessary.

  

  

   index: The zero-based index of the item to scroll into view.
  """
  pass
 def FindItemWithText(self,text,includeSubItemsInSearch=None,startIndex=None,isPrefixSearch=None):
  """
  FindItemWithText(self: ListView,text: str,includeSubItemsInSearch: bool,startIndex: int,isPrefixSearch: bool) -> ListViewItem

  

   Finds the first System.Windows.Forms.ListViewItem or 

    System.Windows.Forms.ListViewItem.ListViewSubItem,if indicated,that begins with the specified 

    text value. The search starts at the specified index.

  

  

   text: The text to search for.

   includeSubItemsInSearch: true to include subitems in the search; otherwise,false.

   startIndex: The index of the item at which to start the search.

   isPrefixSearch: true to allow partial matches; otherwise,false.

   Returns: The first System.Windows.Forms.ListViewItem that begins with the specified text value.

  FindItemWithText(self: ListView,text: str,includeSubItemsInSearch: bool,startIndex: int) -> ListViewItem

  

   Finds the first System.Windows.Forms.ListViewItem or 

    System.Windows.Forms.ListViewItem.ListViewSubItem,if indicated,that begins with the specified 

    text value. The search starts at the specified index.

  

  

   text: The text to search for.

   includeSubItemsInSearch: true to include subitems in the search; otherwise,false.

   startIndex: The index of the item at which to start the search.

   Returns: The first System.Windows.Forms.ListViewItem that begins with the specified text value.

  FindItemWithText(self: ListView,text: str) -> ListViewItem

  

   Finds the first System.Windows.Forms.ListViewItem that begins with the specified text value.

  

   text: The text to search for.

   Returns: The first System.Windows.Forms.ListViewItem that begins with the specified text value.
  """
  pass
 def FindNearestItem(self,*__args):
  """
  FindNearestItem(self: ListView,searchDirection: SearchDirectionHint,x: int,y: int) -> ListViewItem

  

   Finds the next item from the given x- and y-coordinates,searching in the specified direction.

  

   searchDirection: One of the System.Windows.Forms.SearchDirectionHint values.

   x: The x-coordinate for the point at which to begin searching.

   y: The y-coordinate for the point at which to begin searching.

   Returns: The System.Windows.Forms.ListViewItem that is closest to the given coordinates,searching in the 

    specified direction.

  

  FindNearestItem(self: ListView,dir: SearchDirectionHint,point: Point) -> ListViewItem

  

   Finds the next item from the given point,searching in the specified direction

  

   dir: One of the System.Windows.Forms.SearchDirectionHint values.

   point: The point at which to begin searching.

   Returns: The System.Windows.Forms.ListViewItem that is closest to the given point,searching in the 

    specified direction.
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
 def GetItemAt(self,x,y):
  """
  GetItemAt(self: ListView,x: int,y: int) -> ListViewItem

  

   Retrieves the item at the specified location.

  

   x: The x-coordinate of the location to search for an item (expressed in client coordinates).

   y: The y-coordinate of the location to search for an item (expressed in client coordinates).

   Returns: A System.Windows.Forms.ListViewItem that represents the item at the specified position. If there 

    is no item at the specified location,the method returns null.
  """
  pass
 def GetItemRect(self,index,portion=None):
  """
  GetItemRect(self: ListView,index: int,portion: ItemBoundsPortion) -> Rectangle

  

   Retrieves the specified portion of the bounding rectangle for a specific item within the list 

    view control.

  

  

   index: The zero-based index of the item within the System.Windows.Forms.ListView.ListViewItemCollection 

    whose bounding rectangle you want to return.

  

   portion: One of the System.Windows.Forms.ItemBoundsPortion values that represents a portion of the 

    System.Windows.Forms.ListViewItem for which to retrieve the bounding rectangle.

  

   Returns: A System.Drawing.Rectangle that represents the bounding rectangle for the specified portion of 

    the specified System.Windows.Forms.ListViewItem.

  

  GetItemRect(self: ListView,index: int) -> Rectangle

  

   Retrieves the bounding rectangle for a specific item within the list view control.

  

   index: The zero-based index of the item within the System.Windows.Forms.ListView.ListViewItemCollection 

    whose bounding rectangle you want to return.

  

   Returns: A System.Drawing.Rectangle that represents the bounding rectangle of the specified 

    System.Windows.Forms.ListViewItem.
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
 def HitTest(self,*__args):
  """
  HitTest(self: ListView,x: int,y: int) -> ListViewHitTestInfo

  

   Provides item information,given x- and y-coordinates.

  

   x: The x-coordinate at which to retrieve the item information. The coordinate is relative to the 

    upper-left corner of the control.

  

   y: The y-coordinate at which to retrieve the item information. The coordinate is relative to the 

    upper-left corner of the control.

  

   Returns: A System.Windows.Forms.ListViewHitTestInfo.

  HitTest(self: ListView,point: Point) -> ListViewHitTestInfo

  

   Provides item information,given a point.

  

   point: The System.Drawing.Point at which to retrieve the item information. The coordinates are relative 

    to the upper-left corner of the control.

  

   Returns: A System.Windows.Forms.ListViewHitTestInfo.
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
  IsInputKey(self: ListView,keyData: Keys) -> bool

  

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
 def NotifyInvalidate(self,*args):
  """
  NotifyInvalidate(self: Control,invalidatedArea: Rectangle)

   Raises the System.Windows.Forms.Control.Invalidated event with a specified region of the control 

    to invalidate.

  

  

   invalidatedArea: A System.Drawing.Rectangle representing the area to invalidate.
  """
  pass
 def OnAfterLabelEdit(self,*args):
  """
  OnAfterLabelEdit(self: ListView,e: LabelEditEventArgs)

   Raises the System.Windows.Forms.ListView.AfterLabelEdit event.

  

   e: A System.Windows.Forms.LabelEditEventArgs that contains the event data.
  """
  pass
 def OnAutoSizeChanged(self,*args):
  """
  OnAutoSizeChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.AutoSizeChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBackColorChanged(self,*args):
  """
  OnBackColorChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.BackColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBackgroundImageChanged(self,*args):
  """
  OnBackgroundImageChanged(self: ListView,e: EventArgs)

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
 def OnBeforeLabelEdit(self,*args):
  """
  OnBeforeLabelEdit(self: ListView,e: LabelEditEventArgs)

   Raises the System.Windows.Forms.ListView.BeforeLabelEdit event.

  

   e: A System.Windows.Forms.LabelEditEventArgs that contains the event data.
  """
  pass
 def OnBindingContextChanged(self,*args):
  """
  OnBindingContextChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.BindingContextChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnCacheVirtualItems(self,*args):
  """
  OnCacheVirtualItems(self: ListView,e: CacheVirtualItemsEventArgs)

   Raises the System.Windows.Forms.ListView.CacheVirtualItems event.

  

   e: A System.Windows.Forms.CacheVirtualItemsEventArgs that contains the event data.
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
 def OnColumnClick(self,*args):
  """
  OnColumnClick(self: ListView,e: ColumnClickEventArgs)

   Raises the System.Windows.Forms.ListView.ColumnClick event.

  

   e: A System.Windows.Forms.ColumnClickEventArgs that contains the event data.
  """
  pass
 def OnColumnReordered(self,*args):
  """
  OnColumnReordered(self: ListView,e: ColumnReorderedEventArgs)

   Raises the System.Windows.Forms.ListView.ColumnReordered event.

  

   e: The System.Windows.Forms.ColumnReorderedEventArgs that contains the event data.
  """
  pass
 def OnColumnWidthChanged(self,*args):
  """
  OnColumnWidthChanged(self: ListView,e: ColumnWidthChangedEventArgs)

   Raises the System.Windows.Forms.ListView.ColumnWidthChanged event.

  

   e: A System.Windows.Forms.ColumnWidthChangedEventArgs that contains the event data.
  """
  pass
 def OnColumnWidthChanging(self,*args):
  """
  OnColumnWidthChanging(self: ListView,e: ColumnWidthChangingEventArgs)

   Raises the System.Windows.Forms.ListView.ColumnWidthChanging event.

  

   e: A System.Windows.Forms.ColumnWidthChangingEventArgs  that contains the event data.
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
 def OnCursorChanged(self,*args):
  """
  OnCursorChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.CursorChanged event.

  

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
 def OnDrawColumnHeader(self,*args):
  """
  OnDrawColumnHeader(self: ListView,e: DrawListViewColumnHeaderEventArgs)

   Raises the System.Windows.Forms.ListView.DrawColumnHeader event.

  

   e: A System.Windows.Forms.DrawListViewColumnHeaderEventArgs that contains the event data.
  """
  pass
 def OnDrawItem(self,*args):
  """
  OnDrawItem(self: ListView,e: DrawListViewItemEventArgs)

   Raises the System.Windows.Forms.ListView.DrawItem event.

  

   e: A System.Windows.Forms.DrawListViewItemEventArgs that contains the event data.
  """
  pass
 def OnDrawSubItem(self,*args):
  """
  OnDrawSubItem(self: ListView,e: DrawListViewSubItemEventArgs)

   Raises the System.Windows.Forms.ListView.DrawSubItem event.

  

   e: A System.Windows.Forms.DrawListViewSubItemEventArgs that contains the event data.
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
  OnEnter(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.Enter event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnFontChanged(self,*args):
  """
  OnFontChanged(self: ListView,e: EventArgs)

   Raises the FontChanged event.

  

   e: The System.EventArgs that contains the event data.
  """
  pass
 def OnForeColorChanged(self,*args):
  """
  OnForeColorChanged(self: Control,e: EventArgs)

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
  OnHandleCreated(self: ListView,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleDestroyed(self,*args):
  """
  OnHandleDestroyed(self: ListView,e: EventArgs)

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
 def OnItemActivate(self,*args):
  """
  OnItemActivate(self: ListView,e: EventArgs)

   Raises the System.Windows.Forms.ListView.ItemActivate event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnItemCheck(self,*args):
  """
  OnItemCheck(self: ListView,ice: ItemCheckEventArgs)

   Raises the System.Windows.Forms.ListView.ItemCheck event.

  

   ice: An System.Windows.Forms.ItemCheckEventArgs that contains the event data.
  """
  pass
 def OnItemChecked(self,*args):
  """
  OnItemChecked(self: ListView,e: ItemCheckedEventArgs)

   Raises the System.Windows.Forms.ListView.ItemChecked event.

  

   e: An System.Windows.Forms.ItemCheckedEventArgs that contains the event data.
  """
  pass
 def OnItemDrag(self,*args):
  """
  OnItemDrag(self: ListView,e: ItemDragEventArgs)

   Raises the System.Windows.Forms.ListView.ItemDrag event.

  

   e: An System.Windows.Forms.ItemDragEventArgs that contains the event data.
  """
  pass
 def OnItemMouseHover(self,*args):
  """
  OnItemMouseHover(self: ListView,e: ListViewItemMouseHoverEventArgs)

   Raises the System.Windows.Forms.ListView.ItemMouseHover event.

  

   e: A System.Windows.Forms.ListViewItemMouseHoverEventArgs that contains the event data.
  """
  pass
 def OnItemSelectionChanged(self,*args):
  """
  OnItemSelectionChanged(self: ListView,e: ListViewItemSelectionChangedEventArgs)

   Raises the System.Windows.Forms.ListView.ItemSelectionChanged event.

  

   e: A System.Windows.Forms.ListViewItemSelectionChangedEventArgs that contains the event data.
  """
  pass
 def OnKeyDown(self,*args):
  """
  OnKeyDown(self: Control,e: KeyEventArgs)

   Raises the System.Windows.Forms.Control.KeyDown event.

  

   e: A System.Windows.Forms.KeyEventArgs that contains the event data.
  """
  pass
 def OnKeyPress(self,*args):
  """
  OnKeyPress(self: Control,e: KeyPressEventArgs)

   Raises the System.Windows.Forms.Control.KeyPress event.

  

   e: A System.Windows.Forms.KeyPressEventArgs that contains the event data.
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
  OnLayout(self: Control,levent: LayoutEventArgs)

   Raises the System.Windows.Forms.Control.Layout event.

  

   levent: A System.Windows.Forms.LayoutEventArgs that contains the event data.
  """
  pass
 def OnLeave(self,*args):
  """
  OnLeave(self: Control,e: EventArgs)

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
  OnMouseDown(self: Control,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseDown event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
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
  OnMouseHover(self: ListView,e: EventArgs)

   Raises the System.Windows.Forms.Control.MouseHover event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseLeave(self,*args):
  """
  OnMouseLeave(self: ListView,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseMove(self,*args):
  """
  OnMouseMove(self: Control,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseMove event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseUp(self,*args):
  """
  OnMouseUp(self: Control,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseUp event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseWheel(self,*args):
  """
  OnMouseWheel(self: Control,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseWheel event.

  

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
  OnPaint(self: Control,e: PaintEventArgs)

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
  OnParentChanged(self: ListView,e: EventArgs)

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
 def OnRegionChanged(self,*args):
  """
  OnRegionChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.RegionChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnResize(self,*args):
  """
  OnResize(self: ListView,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRetrieveVirtualItem(self,*args):
  """
  OnRetrieveVirtualItem(self: ListView,e: RetrieveVirtualItemEventArgs)

   Raises the System.Windows.Forms.ListView.RetrieveVirtualItem event.

  

   e: A System.Windows.Forms.RetrieveVirtualItemEventArgs that contains the event data.
  """
  pass
 def OnRightToLeftChanged(self,*args):
  """
  OnRightToLeftChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.RightToLeftChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRightToLeftLayoutChanged(self,*args):
  """
  OnRightToLeftLayoutChanged(self: ListView,e: EventArgs)

   Raises the System.Windows.Forms.ListView.RightToLeftLayoutChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnSearchForVirtualItem(self,*args):
  """
  OnSearchForVirtualItem(self: ListView,e: SearchForVirtualItemEventArgs)

   Raises the System.Windows.Forms.ListView.SearchForVirtualItem event.

  

   e: A System.Windows.Forms.SearchForVirtualItemEventArgs that contains the event data.
  """
  pass
 def OnSelectedIndexChanged(self,*args):
  """
  OnSelectedIndexChanged(self: ListView,e: EventArgs)

   Raises the System.Windows.Forms.ListView.SelectedIndexChanged event.

  

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
  OnSystemColorsChanged(self: ListView,e: EventArgs)

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
 def OnVirtualItemsSelectionRangeChanged(self,*args):
  """
  OnVirtualItemsSelectionRangeChanged(self: ListView,e: ListViewVirtualItemsSelectionRangeChangedEventArgs)

   Raises the System.Windows.Forms.ListView.VirtualItemsSelectionRangeChanged event.

  

   e: A System.Windows.Forms.ListViewVirtualItemsSelectionRangeChangedEventArgs that contains the 

    event data.
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
  ProcessDialogKey(self: Control,keyData: Keys) -> bool

  

   Processes a dialog key.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   Returns: true if the key was processed by the control; otherwise,false.
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
  ProcessKeyPreview(self: Control,m: Message) -> (bool,Message)

  

   Previews a keyboard message.

  

   m: A System.Windows.Forms.Message,passed by reference,that represents the window message to 

    process.

  

   Returns: true if the message was processed by the control; otherwise,false.
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
 def RealizeProperties(self,*args):
  """
  RealizeProperties(self: ListView)

   Initializes the properties of the System.Windows.Forms.ListView control that manage the 

    appearance of the control.
  """
  pass
 def RecreateHandle(self,*args):
  """
  RecreateHandle(self: Control)

   Forces the re-creation of the handle for the control.
  """
  pass
 def RedrawItems(self,startIndex,endIndex,invalidateOnly):
  """
  RedrawItems(self: ListView,startIndex: int,endIndex: int,invalidateOnly: bool)

   Forces a range of System.Windows.Forms.ListViewItem objects to be redrawn.

  

   startIndex: The index for the first item in the range to be redrawn.

   endIndex: The index for the last item of the range to be redrawn.

   invalidateOnly: true to invalidate the range of items; false to invalidate and repaint the items.
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
 def Sort(self):
  """
  Sort(self: ListView)

   Sorts the items of the list view.
  """
  pass
 def ToString(self):
  """
  ToString(self: ListView) -> str

  

   Returns a string representation of the System.Windows.Forms.ListView control.

   Returns: A string that states the control type,the count of items in the System.Windows.Forms.ListView 

    control,and the type of the first item in the System.Windows.Forms.ListView,if the count is 

    not 0.
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
 def UpdateExtendedStyles(self,*args):
  """
  UpdateExtendedStyles(self: ListView)

   Updates the extended styles applied to the list view control.
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
  WndProc(self: ListView,m: Message) -> Message

  

   Overrides System.Windows.Forms.Control.WndProc(System.Windows.Forms.Message@).

  

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
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 Activation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type of action the user must take to activate an item.



Get: Activation(self: ListView) -> ItemActivation



Set: Activation(self: ListView)=value

"""

 Alignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the alignment of items in the control.



Get: Alignment(self: ListView) -> ListViewAlignment



Set: Alignment(self: ListView)=value

"""

 AllowColumnReorder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the user can drag column headers to reorder columns in the control.



Get: AllowColumnReorder(self: ListView) -> bool



Set: AllowColumnReorder(self: ListView)=value

"""

 AutoArrange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether icons are automatically kept arranged.



Get: AutoArrange(self: ListView) -> bool



Set: AutoArrange(self: ListView)=value

"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color.



Get: BackColor(self: ListView) -> Color



Set: BackColor(self: ListView)=value

"""

 BackgroundImageLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an System.Windows.Forms.ImageLayout value.



Get: BackgroundImageLayout(self: ListView) -> ImageLayout



Set: BackgroundImageLayout(self: ListView)=value

"""

 BackgroundImageTiled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the background image of the System.Windows.Forms.ListView should be tiled.



Get: BackgroundImageTiled(self: ListView) -> bool



Set: BackgroundImageTiled(self: ListView)=value

"""

 BorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the border style of the control.



Get: BorderStyle(self: ListView) -> BorderStyle



Set: BorderStyle(self: ListView)=value

"""

 CanEnableIme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value,to enable IME support.



"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if events can be raised on the control.



"""

 CheckBoxes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a check box appears next to each item in the control.



Get: CheckBoxes(self: ListView) -> bool



Set: CheckBoxes(self: ListView)=value

"""

 CheckedIndices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the indexes of the currently checked items in the control.



Get: CheckedIndices(self: ListView) -> CheckedIndexCollection



"""

 CheckedItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the currently checked items in the control.



Get: CheckedItems(self: ListView) -> CheckedListViewItemCollection



"""

 Columns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of all column headers that appear in the control.



Get: Columns(self: ListView) -> ColumnHeaderCollection



"""

 CreateParams=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.



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

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 DoubleBuffered=property(lambda self: object(),lambda self,v: None,lambda self: None)

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 FocusedItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the item in the control that currently has focus.



Get: FocusedItem(self: ListView) -> ListViewItem



Set: FocusedItem(self: ListView)=value

"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the font of the control.



"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color.



Get: ForeColor(self: ListView) -> Color



Set: ForeColor(self: ListView)=value

"""

 FullRowSelect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether clicking an item selects all its subitems.



Get: FullRowSelect(self: ListView) -> bool



Set: FullRowSelect(self: ListView)=value

"""

 GridLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether grid lines appear between the rows and columns containing the items and subitems in the control.



Get: GridLines(self: ListView) -> bool



Set: GridLines(self: ListView)=value

"""

 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of System.Windows.Forms.ListViewGroup objects assigned to the control.



Get: Groups(self: ListView) -> ListViewGroupCollection



"""

 HeaderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the column header style.



Get: HeaderStyle(self: ListView) -> ColumnHeaderStyle



Set: HeaderStyle(self: ListView)=value

"""

 HideSelection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the selected item in the control remains highlighted when the control loses focus.



Get: HideSelection(self: ListView) -> bool



Set: HideSelection(self: ListView)=value

"""

 HotTracking=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the text of an item or subitem has the appearance of a hyperlink when the mouse pointer passes over it.



Get: HotTracking(self: ListView) -> bool



Set: HotTracking(self: ListView)=value

"""

 HoverSelection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether an item is automatically selected when the mouse pointer remains over the item for a few seconds.



Get: HoverSelection(self: ListView) -> bool



Set: HoverSelection(self: ListView)=value

"""

 ImeModeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the IME mode of a control.



"""

 InsertionMark=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object used to indicate the expected drop location when an item is dragged within a System.Windows.Forms.ListView control.



Get: InsertionMark(self: ListView) -> ListViewInsertionMark



"""

 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection containing all items in the control.



Get: Items(self: ListView) -> ListViewItemCollection



"""

 LabelEdit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the user can edit the labels of items in the control.



Get: LabelEdit(self: ListView) -> bool



Set: LabelEdit(self: ListView)=value

"""

 LabelWrap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether item labels wrap when items are displayed in the control as icons.



Get: LabelWrap(self: ListView) -> bool



Set: LabelWrap(self: ListView)=value

"""

 LargeImageList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Forms.ImageList to use when displaying items as large icons in the control.



Get: LargeImageList(self: ListView) -> ImageList



Set: LargeImageList(self: ListView)=value

"""

 ListViewItemSorter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the sorting comparer for the control.



Get: ListViewItemSorter(self: ListView) -> IComparer



Set: ListViewItemSorter(self: ListView)=value

"""

 MultiSelect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether multiple items can be selected.



Get: MultiSelect(self: ListView) -> bool



Set: MultiSelect(self: ListView)=value

"""

 OwnerDraw=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ListView control is drawn by the operating system or by code that you provide.



Get: OwnerDraw(self: ListView) -> bool



Set: OwnerDraw(self: ListView)=value

"""

 Padding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the space between the System.Windows.Forms.ListView control and its contents.



Get: Padding(self: ListView) -> Padding



Set: Padding(self: ListView)=value

"""

 RenderRightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is now obsolete.



"""

 ResizeRedraw=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control redraws itself when resized.



"""

 RightToLeftLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control is laid out from right to left.



Get: RightToLeftLayout(self: ListView) -> bool



Set: RightToLeftLayout(self: ListView)=value

"""

 ScaleChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines the scaling of child controls.



"""

 Scrollable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a scroll bar is added to the control when there is not enough room to display all items.



Get: Scrollable(self: ListView) -> bool



Set: Scrollable(self: ListView)=value

"""

 SelectedIndices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the indexes of the selected items in the control.



Get: SelectedIndices(self: ListView) -> SelectedIndexCollection



"""

 SelectedItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the items that are selected in the control.



Get: SelectedItems(self: ListView) -> SelectedListViewItemCollection



"""

 ShowFocusCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control should display focus rectangles.



"""

 ShowGroups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether items are displayed in groups.



Get: ShowGroups(self: ListView) -> bool



Set: ShowGroups(self: ListView)=value

"""

 ShowItemToolTips=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether ToolTips are shown for the System.Windows.Forms.ListViewItem objects contained in the System.Windows.Forms.ListView.



Get: ShowItemToolTips(self: ListView) -> bool



Set: ShowItemToolTips(self: ListView)=value

"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user interface is in the appropriate state to show or hide keyboard accelerators.



"""

 SmallImageList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Forms.ImageList to use when displaying items as small icons in the control.



Get: SmallImageList(self: ListView) -> ImageList



Set: SmallImageList(self: ListView)=value

"""

 Sorting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the sort order for items in the control.



Get: Sorting(self: ListView) -> SortOrder



Set: Sorting(self: ListView)=value

"""

 StateImageList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Forms.ImageList associated with application-defined states in the control.



Get: StateImageList(self: ListView) -> ImageList



Set: StateImageList(self: ListView)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.



Get: Text(self: ListView) -> str



Set: Text(self: ListView)=value

"""

 TileSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size of the tiles shown in tile view.



Get: TileSize(self: ListView) -> Size



Set: TileSize(self: ListView)=value

"""

 TopItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the first visible item in the control.



Get: TopItem(self: ListView) -> ListViewItem



Set: TopItem(self: ListView)=value

"""

 UseCompatibleStateImageBehavior=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ListView uses state image behavior that is compatible with the .NET Framework 1.1 or the .NET Framework 2.0.



Get: UseCompatibleStateImageBehavior(self: ListView) -> bool



Set: UseCompatibleStateImageBehavior(self: ListView)=value

"""

 View=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets how items are displayed in the control.



Get: View(self: ListView) -> View



Set: View(self: ListView)=value

"""

 VirtualListSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of System.Windows.Forms.ListViewItem objects contained in the list when in virtual mode.



Get: VirtualListSize(self: ListView) -> int



Set: VirtualListSize(self: ListView)=value

"""

 VirtualMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether you have provided your own data-management operations for the System.Windows.Forms.ListView control.



Get: VirtualMode(self: ListView) -> bool



Set: VirtualMode(self: ListView)=value

"""


 AfterLabelEdit=None
 BackgroundImageLayoutChanged=None
 BeforeLabelEdit=None
 CacheVirtualItems=None
 CheckedIndexCollection=None
 CheckedListViewItemCollection=None
 ColumnClick=None
 ColumnHeaderCollection=None
 ColumnReordered=None
 ColumnWidthChanged=None
 ColumnWidthChanging=None
 DrawColumnHeader=None
 DrawItem=None
 DrawSubItem=None
 ItemActivate=None
 ItemCheck=None
 ItemChecked=None
 ItemDrag=None
 ItemMouseHover=None
 ItemSelectionChanged=None
 ListViewItemCollection=None
 PaddingChanged=None
 Paint=None
 RetrieveVirtualItem=None
 RightToLeftLayoutChanged=None
 SearchForVirtualItem=None
 SelectedIndexChanged=None
 SelectedIndexCollection=None
 SelectedListViewItemCollection=None
 TextChanged=None
 VirtualItemsSelectionRangeChanged=None

