class ListBox(ListControl,IComponent,IDisposable,IOleControl,IOleObject,IOleInPlaceObject,IOleInPlaceActiveObject,IOleWindow,IViewObject,IViewObject2,IPersist,IPersistStreamInit,IPersistPropertyBag,IPersistStorage,IQuickActivate,ISupportOleDropSource,IDropTarget,ISynchronizeInvoke,IWin32Window,IArrangedElement,IBindableComponent):
 """
 Represents a Windows control to display a list of items.

 

 ListBox()
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
 def AddItemsCore(self,*args):
  """
  AddItemsCore(self: ListBox,value: Array[object])

   This member is obsolete,and there is no replacement.

  

   value: An array of objects.
  """
  pass
 def BeginUpdate(self):
  """
  BeginUpdate(self: ListBox)

   Maintains performance while items are added to the System.Windows.Forms.ListBox one at a time by 

    preventing the control from drawing until the System.Windows.Forms.ListBox.EndUpdate method is 

    called.
  """
  pass
 def ClearSelected(self):
  """
  ClearSelected(self: ListBox)

   Unselects all items in the System.Windows.Forms.ListBox.
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
  """
  CreateHandle(self: Control)

   Creates a handle for the control.
  """
  pass
 def CreateItemCollection(self,*args):
  """
  CreateItemCollection(self: ListBox) -> ObjectCollection

  

   Creates a new instance of the item collection.

   Returns: A System.Windows.Forms.ListBox.ObjectCollection that represents the new item collection.
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
  Dispose(self: Control,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.Control and its child controls 

    and optionally releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def EndUpdate(self):
  """
  EndUpdate(self: ListBox)

   Resumes painting the System.Windows.Forms.ListBox control after painting is suspended by the 

    System.Windows.Forms.ListBox.BeginUpdate method.
  """
  pass
 def FilterItemOnProperty(self,*args):
  """
  FilterItemOnProperty(self: ListControl,item: object,field: str) -> object

  

   Returns the current value of the System.Windows.Forms.ListControl item,if it is a property of 

    an object given the item and the property name.

  

  

   item: The object the System.Windows.Forms.ListControl item is bound to.

   field: The property name of the item the System.Windows.Forms.ListControl is bound to.

   Returns: The filtered object.

  FilterItemOnProperty(self: ListControl,item: object) -> object

  

   Retrieves the current value of the System.Windows.Forms.ListControl item,if it is a property of 

    an object,given the item.

  

  

   item: The object the System.Windows.Forms.ListControl item is bound to.

   Returns: The filtered object.
  """
  pass
 def FindString(self,s,startIndex=None):
  """
  FindString(self: ListBox,s: str,startIndex: int) -> int

  

   Finds the first item in the System.Windows.Forms.ListBox that starts with the specified string. 

    The search starts at a specific starting index.

  

  

   s: The text to search for.

   startIndex: The zero-based index of the item before the first item to be searched. Set to negative one (-1) 

    to search from the beginning of the control.

  

   Returns: The zero-based index of the first item found; returns ListBox.NoMatches if no match is found.

  FindString(self: ListBox,s: str) -> int

  

   Finds the first item in the System.Windows.Forms.ListBox that starts with the specified string.

  

   s: The text to search for.

   Returns: The zero-based index of the first item found; returns ListBox.NoMatches if no match is found.
  """
  pass
 def FindStringExact(self,s,startIndex=None):
  """
  FindStringExact(self: ListBox,s: str,startIndex: int) -> int

  

   Finds the first item in the System.Windows.Forms.ListBox that exactly matches the specified 

    string. The search starts at a specific starting index.

  

  

   s: The text to search for.

   startIndex: The zero-based index of the item before the first item to be searched. Set to negative one (-1) 

    to search from the beginning of the control.

  

   Returns: The zero-based index of the first item found; returns ListBox.NoMatches if no match is found.

  FindStringExact(self: ListBox,s: str) -> int

  

   Finds the first item in the System.Windows.Forms.ListBox that exactly matches the specified 

    string.

  

  

   s: The text to search for.

   Returns: The zero-based index of the first item found; returns ListBox.NoMatches if no match is found.
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
 def GetItemHeight(self,index):
  """
  GetItemHeight(self: ListBox,index: int) -> int

  

   Returns the height of an item in the System.Windows.Forms.ListBox.

  

   index: The zero-based index of the item to return the height for.

   Returns: The height,in pixels,of the specified item.
  """
  pass
 def GetItemRectangle(self,index):
  """
  GetItemRectangle(self: ListBox,index: int) -> Rectangle

  

   Returns the bounding rectangle for an item in the System.Windows.Forms.ListBox.

  

   index: The zero-based index of item whose bounding rectangle you want to return.

   Returns: A System.Drawing.Rectangle that represents the bounding rectangle for the specified item.
  """
  pass
 def GetScaledBounds(self,*args):
  """
  GetScaledBounds(self: ListBox,bounds: Rectangle,factor: SizeF,specified: BoundsSpecified) -> Rectangle

  

   Retrieves the bounds within which the System.Windows.Forms.ListBox is scaled.

  

   bounds: A System.Drawing.Rectangle that specifies the area for which to retrieve the display bounds.

   factor: The height and width of the control's bounds.

   specified: One of the values of System.Windows.Forms.BoundsSpecified that specifies the bounds of the 

    control to use when defining its size and position.

  

   Returns: A System.Drawing.Rectangle representing the bounds within which the control is scaled.
  """
  pass
 def GetSelected(self,index):
  """
  GetSelected(self: ListBox,index: int) -> bool

  

   Returns a value indicating whether the specified item is selected.

  

   index: The zero-based index of the item that determines whether it is selected.

   Returns: true if the specified item is currently selected in the System.Windows.Forms.ListBox; otherwise,

    false.
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
 def IndexFromPoint(self,*__args):
  """
  IndexFromPoint(self: ListBox,x: int,y: int) -> int

  

   Returns the zero-based index of the item at the specified coordinates.

  

   x: The x-coordinate of the location to search.

   y: The y-coordinate of the location to search.

   Returns: The zero-based index of the item found at the specified coordinates; returns ListBox.NoMatches 

    if no match is found.

  

  IndexFromPoint(self: ListBox,p: Point) -> int

  

   Returns the zero-based index of the item at the specified coordinates.

  

   p: A System.Drawing.Point object containing the coordinates used to obtain the item index.

   Returns: The zero-based index of the item found at the specified coordinates; returns ListBox.NoMatches 

    if no match is found.
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
  IsInputKey(self: ListControl,keyData: Keys) -> bool

  

   Handles special input keys,such as PAGE UP,PAGE DOWN,HOME,END,and so on.

  

   keyData: One of the values of System.Windows.Forms.Keys.

   Returns: true if the keyData parameter specifies the System.Windows.Forms.Keys.End,

    System.Windows.Forms.Keys.Home,System.Windows.Forms.Keys.PageUp,or 

    System.Windows.Forms.Keys.PageDown key; false if the keyData parameter specifies 

    System.Windows.Forms.Keys.Alt.
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
  OnBindingContextChanged(self: ListControl,e: EventArgs)

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
  OnChangeUICues(self: ListBox,e: UICuesEventArgs)

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
 def OnCursorChanged(self,*args):
  """
  OnCursorChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.CursorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDataSourceChanged(self,*args):
  """
  OnDataSourceChanged(self: ListBox,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDisplayMemberChanged(self,*args):
  """
  OnDisplayMemberChanged(self: ListBox,e: EventArgs)

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
 def OnDrawItem(self,*args):
  """
  OnDrawItem(self: ListBox,e: DrawItemEventArgs)

   Raises the System.Windows.Forms.ListBox.DrawItem event.

  

   e: A System.Windows.Forms.DrawItemEventArgs that contains the event data.
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
  OnFontChanged(self: ListBox,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnForeColorChanged(self,*args):
  """
  OnForeColorChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.ForeColorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnFormat(self,*args):
  """
  OnFormat(self: ListControl,e: ListControlConvertEventArgs)

   Raises the System.Windows.Forms.ListControl.Format event.

  

   e: A System.Windows.Forms.ListControlConvertEventArgs that contains the event data.
  """
  pass
 def OnFormatInfoChanged(self,*args):
  """
  OnFormatInfoChanged(self: ListControl,e: EventArgs)

   Raises the System.Windows.Forms.ListControl.FormatInfoChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnFormatStringChanged(self,*args):
  """
  OnFormatStringChanged(self: ListControl,e: EventArgs)

   Raises the System.Windows.Forms.ListControl.FormatStringChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnFormattingEnabledChanged(self,*args):
  """
  OnFormattingEnabledChanged(self: ListControl,e: EventArgs)

   Raises the System.Windows.Forms.ListControl.FormattingEnabledChanged event.

  

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
  OnHandleCreated(self: ListBox,e: EventArgs)

   Specifies when the window handle has been created so that column width and other characteristics 

    can be set. Inheriting classes should call base.OnHandleCreated.

  

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleDestroyed(self,*args):
  """
  OnHandleDestroyed(self: ListBox,e: EventArgs)

   Overridden to be sure that items are set up and cleared out correctly. Inheriting controls 

    should call base.OnHandleDestroyed.

  

  

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
 def OnMeasureItem(self,*args):
  """
  OnMeasureItem(self: ListBox,e: MeasureItemEventArgs)

   Raises the System.Windows.Forms.ListBox.MeasureItem event.

  

   e: A System.Windows.Forms.MeasureItemEventArgs that contains the event data.
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
  OnMouseHover(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.MouseHover event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseLeave(self,*args):
  """
  OnMouseLeave(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.MouseLeave event.

  

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
  OnParentChanged(self: ListBox,e: EventArgs)

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
  OnResize(self: ListBox,e: EventArgs)

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
 def OnSelectedIndexChanged(self,*args):
  """
  OnSelectedIndexChanged(self: ListBox,e: EventArgs)

   e: Event object with the details
  """
  pass
 def OnSelectedValueChanged(self,*args):
  """
  OnSelectedValueChanged(self: ListBox,e: EventArgs)

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
 def OnValueMemberChanged(self,*args):
  """
  OnValueMemberChanged(self: ListControl,e: EventArgs)

   Raises the System.Windows.Forms.ListControl.ValueMemberChanged event.

  

   e: An System.EventArgs that contains the event data.
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
 def RecreateHandle(self,*args):
  """
  RecreateHandle(self: Control)

   Forces the re-creation of the handle for the control.
  """
  pass
 def Refresh(self):
  """
  Refresh(self: ListBox)

   Forces the control to invalidate its client area and immediately redraw itself and any child 

    controls.
  """
  pass
 def RefreshItem(self,*args):
  """
  RefreshItem(self: ListBox,index: int)

   Refreshes the item contained at the specified index.

  

   index: The zero-based index of the element to refresh.
  """
  pass
 def RefreshItems(self,*args):
  """
  RefreshItems(self: ListBox)

   Refreshes all System.Windows.Forms.ListBox items and retrieves new strings for them.
  """
  pass
 def RescaleConstantsForDpi(self,*args):
  """ RescaleConstantsForDpi(self: ListBox,deviceDpiOld: int,deviceDpiNew: int) """
  pass
 def ResetBackColor(self):
  """ ResetBackColor(self: ListBox) """
  pass
 def ResetForeColor(self):
  """ ResetForeColor(self: ListBox) """
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
  ScaleControl(self: ListBox,factor: SizeF,specified: BoundsSpecified)

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
  SetBoundsCore(self: ListBox,x: int,y: int,width: int,height: int,specified: BoundsSpecified)

   Sets the specified bounds of the System.Windows.Forms.ListBox control.

  

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
 def SetItemCore(self,*args):
  """
  SetItemCore(self: ListBox,index: int,value: object)

   Sets the object with the specified index in the derived class.

  

   index: The array index of the object.

   value: The object.
  """
  pass
 def SetItemsCore(self,*args):
  """
  SetItemsCore(self: ListBox,value: IList)

   Clears the contents of the System.Windows.Forms.ListBox and adds the specified items to the 

    control.

  

  

   value: An array of objects to insert into the control.
  """
  pass
 def SetSelected(self,index,value):
  """
  SetSelected(self: ListBox,index: int,value: bool)

   Selects or clears the selection for the specified item in a System.Windows.Forms.ListBox.

  

   index: The zero-based index of the item in a System.Windows.Forms.ListBox to select or clear the 

    selection for.

  

   value: true to select the specified item; otherwise,false.
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
 def Sort(self,*args):
  """
  Sort(self: ListBox)

   Sorts the items in the System.Windows.Forms.ListBox.
  """
  pass
 def ToString(self):
  """
  ToString(self: ListBox) -> str

  

   Returns a string representation of the System.Windows.Forms.ListBox.

   Returns: A string that states the control type,the count of items in the System.Windows.Forms.ListBox 

    control,and the Text property of the first item in the System.Windows.Forms.ListBox,if the 

    count is not 0.
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
 def WmReflectCommand(self,*args):
  """
  WmReflectCommand(self: ListBox,m: Message) -> Message

  

   Processes the command message the System.Windows.Forms.ListView control receives from the 

    top-level window.

  

  

   m: The System.Windows.Forms.Message the top-level window sent to the System.Windows.Forms.ListBox 

    control.
  """
  pass
 def WndProc(self,*args):
  """
  WndProc(self: ListBox,m: Message) -> Message

  

   The list's window procedure.

  

   m: A Windows Message Object.
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
 AllowSelection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.ListBox currently enables selection of list items.



"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BackColor(self: ListBox) -> Color



Set: BackColor(self: ListBox)=value

"""

 BackgroundImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: BackgroundImage(self: ListBox) -> Image



Set: BackgroundImage(self: ListBox)=value

"""

 BackgroundImageLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background image layout for a System.Windows.Forms.ListBox as defined in the System.Windows.Forms.ImageLayout enumeration.



Get: BackgroundImageLayout(self: ListBox) -> ImageLayout



Set: BackgroundImageLayout(self: ListBox)=value

"""

 BorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type of border that is drawn around the System.Windows.Forms.ListBox.



Get: BorderStyle(self: ListBox) -> BorderStyle



Set: BorderStyle(self: ListBox)=value

"""

 CanEnableIme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value,to enable IME support.



"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if events can be raised on the control.



"""

 ColumnWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of columns in a multicolumn System.Windows.Forms.ListBox.



Get: ColumnWidth(self: ListBox) -> int



Set: ColumnWidth(self: ListBox)=value

"""

 CreateParams=property(lambda self: object(),lambda self,v: None,lambda self: None)

 CustomTabOffsets=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the width of the tabs between the items in the System.Windows.Forms.ListBox.



Get: CustomTabOffsets(self: ListBox) -> IntegerCollection



"""

 DataManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.CurrencyManager associated with this control.



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
 """Gets or sets a value indicating whether this control should redraw its surface using a secondary buffer to reduce or prevent flicker.



"""

 DrawMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the drawing mode for the control.



Get: DrawMode(self: ListBox) -> DrawMode



Set: DrawMode(self: ListBox)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Font=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Font(self: ListBox) -> Font



Set: Font(self: ListBox)=value

"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the font of the control.



"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ForeColor(self: ListBox) -> Color



Set: ForeColor(self: ListBox)=value

"""

 HorizontalExtent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width by which the horizontal scroll bar of a System.Windows.Forms.ListBox can scroll.



Get: HorizontalExtent(self: ListBox) -> int



Set: HorizontalExtent(self: ListBox)=value

"""

 HorizontalScrollbar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a horizontal scroll bar is displayed in the control.



Get: HorizontalScrollbar(self: ListBox) -> bool



Set: HorizontalScrollbar(self: ListBox)=value

"""

 ImeModeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the IME mode of a control.



"""

 IntegralHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control should resize to avoid showing partial items.



Get: IntegralHeight(self: ListBox) -> bool



Set: IntegralHeight(self: ListBox)=value

"""

 ItemHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of an item in the System.Windows.Forms.ListBox.



Get: ItemHeight(self: ListBox) -> int



Set: ItemHeight(self: ListBox)=value

"""

 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the items of the System.Windows.Forms.ListBox.



Get: Items(self: ListBox) -> ObjectCollection



"""

 MultiColumn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ListBox supports multiple columns.



Get: MultiColumn(self: ListBox) -> bool



Set: MultiColumn(self: ListBox)=value

"""

 Padding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant to this class.



Get: Padding(self: ListBox) -> Padding



Set: Padding(self: ListBox)=value

"""

 PreferredHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the combined height of all items in the System.Windows.Forms.ListBox.



Get: PreferredHeight(self: ListBox) -> int



"""

 RenderRightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is now obsolete.



"""

 ResizeRedraw=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control redraws itself when resized.



"""

 RightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether text displayed by the control is displayed from right to left.



Get: RightToLeft(self: ListBox) -> RightToLeft



Set: RightToLeft(self: ListBox)=value

"""

 ScaleChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines the scaling of child controls.



"""

 ScrollAlwaysVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the vertical scroll bar is shown at all times.



Get: ScrollAlwaysVisible(self: ListBox) -> bool



Set: ScrollAlwaysVisible(self: ListBox)=value

"""

 SelectedIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the zero-based index of the currently selected item in a System.Windows.Forms.ListBox.



Get: SelectedIndex(self: ListBox) -> int



Set: SelectedIndex(self: ListBox)=value

"""

 SelectedIndices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection that contains the zero-based indexes of all currently selected items in the System.Windows.Forms.ListBox.



Get: SelectedIndices(self: ListBox) -> SelectedIndexCollection



"""

 SelectedItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the currently selected item in the System.Windows.Forms.ListBox.



Get: SelectedItem(self: ListBox) -> object



Set: SelectedItem(self: ListBox)=value

"""

 SelectedItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection containing the currently selected items in the System.Windows.Forms.ListBox.



Get: SelectedItems(self: ListBox) -> SelectedObjectCollection



"""

 SelectionMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the method in which items are selected in the System.Windows.Forms.ListBox.



Get: SelectionMode(self: ListBox) -> SelectionMode



Set: SelectionMode(self: ListBox)=value

"""

 ShowFocusCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control should display focus rectangles.



"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user interface is in the appropriate state to show or hide keyboard accelerators.



"""

 Sorted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the items in the System.Windows.Forms.ListBox are sorted alphabetically.



Get: Sorted(self: ListBox) -> bool



Set: Sorted(self: ListBox)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or searches for the text of the currently selected item in the System.Windows.Forms.ListBox.



Get: Text(self: ListBox) -> str



Set: Text(self: ListBox)=value

"""

 TopIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of the first visible item in the System.Windows.Forms.ListBox.



Get: TopIndex(self: ListBox) -> int



Set: TopIndex(self: ListBox)=value

"""

 UseCustomTabOffsets=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ListBox recognizes and expands tab characters when it draws its strings by using the System.Windows.Forms.ListBox.CustomTabOffsets integer array.



Get: UseCustomTabOffsets(self: ListBox) -> bool



Set: UseCustomTabOffsets(self: ListBox)=value

"""

 UseTabStops=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ListBox can recognize and expand tab characters when drawing its strings.



Get: UseTabStops(self: ListBox) -> bool



Set: UseTabStops(self: ListBox)=value

"""


 BackgroundImageChanged=None
 BackgroundImageLayoutChanged=None
 Click=None
 DefaultItemHeight=13
 DrawItem=None
 IntegerCollection=None
 MeasureItem=None
 MouseClick=None
 NoMatches=-1
 ObjectCollection=None
 PaddingChanged=None
 Paint=None
 SelectedIndexChanged=None
 SelectedIndexCollection=None
 SelectedObjectCollection=None
 TextChanged=None

