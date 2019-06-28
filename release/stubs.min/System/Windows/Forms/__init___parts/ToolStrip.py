class ToolStrip:
 """
 Provides a container for Windows toolbar objects.
 
 ToolStrip()
 ToolStrip(*items: Array[ToolStripItem])
 """
 def AccessibilityNotifyClients(self,*args):
  """
  AccessibilityNotifyClients(self: Control,accEvent: AccessibleEvents,childID: int)
   Notifies the accessibility client applications of the specified 
    System.Windows.Forms.AccessibleEvents for the specified child control.
  
  
   accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications 
    of.
  
   childID: The child System.Windows.Forms.Control to notify of the accessible event.
  AccessibilityNotifyClients(self: Control,accEvent: AccessibleEvents,objectID: int,childID: int)
   Notifies the accessibility client applications of the specified 
    System.Windows.Forms.AccessibleEvents for the specified child control .
  
  
   accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications 
    of.
  
   objectID: The identifier of the System.Windows.Forms.AccessibleObject.
   childID: The child System.Windows.Forms.Control to notify of the accessible event.
  """
  pass
 def AdjustFormScrollbars(self,*args):
  """
  AdjustFormScrollbars(self: ScrollableControl,displayScrollbars: bool)
   Adjusts the scroll bars on the container based on the current control positions and the 
    control currently selected.
  
  
   displayScrollbars: true to show the scroll bars; otherwise,false.
  """
  pass
 def CreateAccessibilityInstance(self,*args):
  """
  CreateAccessibilityInstance(self: ToolStrip) -> AccessibleObject
  
   Creates a new accessibility object for the System.Windows.Forms.ToolStrip item.
   Returns: A new System.Windows.Forms.AccessibleObject for the System.Windows.Forms.ToolStrip item.
  """
  pass
 def CreateControlsInstance(self,*args):
  """ CreateControlsInstance(self: ToolStrip) -> ControlCollection """
  pass
 def CreateDefaultItem(self,*args):
  """
  CreateDefaultItem(self: ToolStrip,text: str,image: Image,onClick: EventHandler) -> ToolStripItem
  
   Creates a default System.Windows.Forms.ToolStripItem with the specified text,image,and 
    event handler on a new System.Windows.Forms.ToolStrip instance.
  
  
   text: The text to use for the System.Windows.Forms.ToolStripItem. If the text parameter is a 
    hyphen (-),this method creates a System.Windows.Forms.ToolStripSeparator.
  
   image: The System.Drawing.Image to display on the System.Windows.Forms.ToolStripItem.
   onClick: An event handler that raises the System.Windows.Forms.Control.Click event when the 
    System.Windows.Forms.ToolStripItem is clicked.
  
   Returns: A 
    System.Windows.Forms.ToolStripButton.#ctor(System.String,System.Drawing.Image,System.Event
    Handler),or a System.Windows.Forms.ToolStripSeparator if the text parameter is a hyphen 
    (-).
  """
  pass
 def CreateHandle(self,*args):
  """
  CreateHandle(self: Control)
   Creates a handle for the control.
  """
  pass
 def CreateLayoutSettings(self,*args):
  """
  CreateLayoutSettings(self: ToolStrip,layoutStyle: ToolStripLayoutStyle) -> LayoutSettings
  
   Specifies the visual arrangement for the System.Windows.Forms.ToolStrip.
  
   layoutStyle: The visual arrangement to be applied to the System.Windows.Forms.ToolStrip.
   Returns: One of the System.Windows.Forms.ToolStripLayoutStyle values. The default is null.
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
  Dispose(self: ToolStrip,disposing: bool)
   Releases the unmanaged resources used by the System.Windows.Forms.ToolStrip and 
    optionally releases the managed resources.
  
  
   disposing: true to release both managed and unmanaged resources; false to release only unmanaged 
    resources.
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
 def GetChildAtPoint(self,*__args):
  """
  GetChildAtPoint(self: ToolStrip,point: Point) -> Control
  
   This method is not relevant for this class.
  
   point: A System.Drawing.Point.
   Returns: A System.Windows.Forms.Control.
  GetChildAtPoint(self: ToolStrip,pt: Point,skipValue: GetChildAtPointSkip) -> Control
  
   This method is not relevant for this class.
  
   pt: A System.Drawing.Point value.
   skipValue: A System.Windows.Forms.GetChildAtPointSkip  value.
   Returns: A System.Windows.Forms.Control.
  """
  pass
 def GetItemAt(self,*__args):
  """
  GetItemAt(self: ToolStrip,x: int,y: int) -> ToolStripItem
  
   Returns the item located at the specified x- and y-coordinates of the 
    System.Windows.Forms.ToolStrip client area.
  
  
   x: The horizontal coordinate,in pixels,from the left edge of the client area.
   y: The vertical coordinate,in pixels,from the top edge of the client area.
   Returns: The System.Windows.Forms.ToolStripItem located at the specified location,or null if the 
    System.Windows.Forms.ToolStripItem is not found.
  
  GetItemAt(self: ToolStrip,point: Point) -> ToolStripItem
  
   Returns the item located at the specified point in the client area of the 
    System.Windows.Forms.ToolStrip.
  
  
   point: The System.Drawing.Point at which to search for the System.Windows.Forms.ToolStripItem.
   Returns: The System.Windows.Forms.ToolStripItem at the specified location,or null if the 
    System.Windows.Forms.ToolStripItem is not found.
  """
  pass
 def GetNextItem(self,start,direction):
  """
  GetNextItem(self: ToolStrip,start: ToolStripItem,direction: ArrowDirection) -> ToolStripItem
  
   Retrieves the next System.Windows.Forms.ToolStripItem from the specified reference point 
    and moving in the specified direction.
  
  
   start: The System.Windows.Forms.ToolStripItem that is the reference point from which to begin 
    the retrieval of the next item.
  
   direction: One of the values of System.Windows.Forms.ArrowDirection that specifies the direction to 
    move.
  
   Returns: A System.Windows.Forms.ToolStripItem that is specified by the start parameter and is next 
    in the order as specified by the direction parameter.
  """
  pass
 def GetScaledBounds(self,*args):
  """
  GetScaledBounds(self: Control,bounds: Rectangle,factor: SizeF,specified: BoundsSpecified) -> Rectangle
  
   Retrieves the bounds within which the control is scaled.
  
   bounds: A System.Drawing.Rectangle that specifies the area for which to retrieve the display 
    bounds.
  
   factor: The height and width of the control's bounds.
   specified: One of the values of System.Windows.Forms.BoundsSpecified that specifies the bounds of 
    the control to use when defining its size and position.
  
   Returns: A System.Drawing.Rectangle representing the bounds within which the control is scaled.
  """
  pass
 def GetScrollState(self,*args):
  """
  GetScrollState(self: ScrollableControl,bit: int) -> bool
  
   Determines whether the specified flag has been set.
  
   bit: The flag to check.
   Returns: true if the specified flag has been set; otherwise,false.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Component,service: Type) -> object
  
   Returns an object that represents a service provided by the 
    System.ComponentModel.Component or by its System.ComponentModel.Container.
  
  
   service: A service provided by the System.ComponentModel.Component.
   Returns: An System.Object that represents a service provided by the 
    System.ComponentModel.Component,or null if the System.ComponentModel.Component does not 
    provide the specified service.
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
  
   toInvoke: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Click event 
    to.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def InvokePaint(self,*args):
  """
  InvokePaint(self: Control,c: Control,e: PaintEventArgs)
   Raises the System.Windows.Forms.Control.Paint event for the specified control.
  
   c: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Paint event 
    to.
  
   e: An System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def InvokePaintBackground(self,*args):
  """
  InvokePaintBackground(self: Control,c: Control,e: PaintEventArgs)
   Raises the PaintBackground event for the specified control.
  
   c: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Paint event 
    to.
  
   e: An System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def IsInputChar(self,*args):
  """
  IsInputChar(self: ToolStrip,charCode: Char) -> bool
  
   Determines whether a character is an input character that the item recognizes.
  
   charCode: The character to test.
   Returns: true if the character should be sent directly to the item and not preprocessed; 
    otherwise,false.
  """
  pass
 def IsInputKey(self,*args):
  """
  IsInputKey(self: ToolStrip,keyData: Keys) -> bool
  
   Determines whether the specified key is a regular input key or a special key that 
    requires preprocessing.
  
  
   keyData: One of the System.Windows.Forms.Keys values.
   Returns: true if the specified key is a regular input key; otherwise,false.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject
  
   Creates a shallow copy of the current System.MarshalByRefObject object.
  
   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause 
    the object to be assigned a new identity when it is marshaled across a remoting boundary. 
    A value of false is usually appropriate. true to copy the current 
    System.MarshalByRefObject object's identity to its clone,which will cause remoting 
    client calls to be routed to the remote server object.
  
   Returns: A shallow copy of the current System.MarshalByRefObject object.
  MemberwiseClone(self: object) -> object
  
   Creates a shallow copy of the current System.Object.
   Returns: A shallow copy of the current System.Object.
  """
  pass
 def NotifyInvalidate(self,*args):
  """
  NotifyInvalidate(self: Control,invalidatedArea: Rectangle)
   Raises the System.Windows.Forms.Control.Invalidated event with a specified region of the 
    control to invalidate.
  
  
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
 def OnBeginDrag(self,*args):
  """
  OnBeginDrag(self: ToolStrip,e: EventArgs)
   Raises the System.Windows.Forms.ToolStrip.BeginDrag event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnBindingContextChanged(self,*args):
  """
  OnBindingContextChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.BindingContextChanged event.
  
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
 def OnCursorChanged(self,*args):
  """
  OnCursorChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.CursorChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDockChanged(self,*args):
  """
  OnDockChanged(self: ToolStrip,e: EventArgs)
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
  OnEnabledChanged(self: ToolStrip,e: EventArgs)
   Raises the System.Windows.Forms.Control.Enabled event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnEndDrag(self,*args):
  """
  OnEndDrag(self: ToolStrip,e: EventArgs)
   Raises the System.Windows.Forms.ToolStrip.EndDrag event.
  
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
  OnFontChanged(self: ToolStrip,e: EventArgs)
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
  OnHandleCreated(self: ToolStrip,e: EventArgs)
   Raises the System.Windows.Forms.Control.HandleCreated event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleDestroyed(self,*args):
  """
  OnHandleDestroyed(self: ToolStrip,e: EventArgs)
   Raises the System.Windows.Forms.Control.HandleDestroyed event.
  
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
  OnInvalidated(self: ToolStrip,e: InvalidateEventArgs)
   e: An System.Windows.Forms.InvalidateEventArgs that contains the event data.
  """
  pass
 def OnItemAdded(self,*args):
  """
  OnItemAdded(self: ToolStrip,e: ToolStripItemEventArgs)
   Raises the System.Windows.Forms.ToolStrip.ItemAdded event.
  
   e: A System.Windows.Forms.ToolStripItemEventArgs that contains the event data.
  """
  pass
 def OnItemClicked(self,*args):
  """
  OnItemClicked(self: ToolStrip,e: ToolStripItemClickedEventArgs)
   Raises the System.Windows.Forms.ToolStrip.ItemClicked event.
  
   e: A System.Windows.Forms.ToolStripItemClickedEventArgs that contains the event data.
  """
  pass
 def OnItemRemoved(self,*args):
  """
  OnItemRemoved(self: ToolStrip,e: ToolStripItemEventArgs)
   Raises the System.Windows.Forms.ToolStrip.ItemRemoved event.
  
   e: A System.Windows.Forms.ToolStripItemEventArgs that contains the event data.
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
  OnLayout(self: ToolStrip,e: LayoutEventArgs)
   Raises the System.Windows.Forms.Control.Layout event.
  
   e: A System.Windows.Forms.LayoutEventArgs that contains the event data.
  """
  pass
 def OnLayoutCompleted(self,*args):
  """
  OnLayoutCompleted(self: ToolStrip,e: EventArgs)
   Raises the System.Windows.Forms.ToolStrip.LayoutCompleted event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnLayoutStyleChanged(self,*args):
  """
  OnLayoutStyleChanged(self: ToolStrip,e: EventArgs)
   Raises the System.Windows.Forms.ToolStrip.LayoutStyleChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnLeave(self,*args):
  """
  OnLeave(self: ToolStrip,e: EventArgs)
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
  OnLostFocus(self: ToolStrip,e: EventArgs)
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
  OnMouseCaptureChanged(self: ToolStrip,e: EventArgs)
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
  OnMouseDown(self: ToolStrip,mea: MouseEventArgs)
   Raises the System.Windows.Forms.Control.MouseDown event.
  
   mea: A System.Windows.Forms.MouseEventArgs that contains the event data.
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
  OnMouseLeave(self: ToolStrip,e: EventArgs)
   Raises the System.Windows.Forms.Control.MouseLeave event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnMouseMove(self,*args):
  """
  OnMouseMove(self: ToolStrip,mea: MouseEventArgs)
   Raises the System.Windows.Forms.Control.MouseMove event.
  
   mea: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseUp(self,*args):
  """
  OnMouseUp(self: ToolStrip,mea: MouseEventArgs)
   Raises the System.Windows.Forms.Control.MouseUp event.
  
   mea: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseWheel(self,*args):
  """
  OnMouseWheel(self: ScrollableControl,e: MouseEventArgs)
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
  OnPaddingChanged(self: ScrollableControl,e: EventArgs)
   Raises the System.Windows.Forms.Control.PaddingChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnPaint(self,*args):
  """
  OnPaint(self: ToolStrip,e: PaintEventArgs)
   Raises the System.Windows.Forms.Control.Paint event.
  
   e: A System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def OnPaintBackground(self,*args):
  """
  OnPaintBackground(self: ToolStrip,e: PaintEventArgs)
   Raises the System.Windows.Forms.Control.Paint event for the 
    System.Windows.Forms.ToolStrip background.
  
  
   e: A System.Windows.Forms.PaintEventArgs that contains information about the control to 
    paint.
  """
  pass
 def OnPaintGrip(self,*args):
  """
  OnPaintGrip(self: ToolStrip,e: PaintEventArgs)
   Raises the System.Windows.Forms.ToolStrip.PaintGrip event.
  
   e: A System.Windows.Forms.PaintEventArgs that contains the event data.
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
    System.Windows.Forms.Control.BackgroundImage property value of the control's container 
    changes.
  
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentBindingContextChanged(self,*args):
  """
  OnParentBindingContextChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.BindingContextChanged event when the 
    System.Windows.Forms.Control.BindingContext property value of the control's container 
    changes.
  
  
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
    System.Windows.Forms.Control.RightToLeft property value of the control's container 
    changes.
  
  
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
 def OnRendererChanged(self,*args):
  """
  OnRendererChanged(self: ToolStrip,e: EventArgs)
   Raises the System.Windows.Forms.ToolStrip.RendererChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnResize(self,*args):
  """
  OnResize(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.Resize event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRightToLeftChanged(self,*args):
  """
  OnRightToLeftChanged(self: ToolStrip,e: EventArgs)
   Raises the System.Windows.Forms.Control.RightToLeftChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnScroll(self,*args):
  """
  OnScroll(self: ToolStrip,se: ScrollEventArgs)
   se: A System.Windows.Forms.ScrollEventArgs that contains the event data.
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
  OnTabStopChanged(self: ToolStrip,e: EventArgs)
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
  OnVisibleChanged(self: ToolStrip,e: EventArgs)
   Raises the System.Windows.Forms.ToolStripItem.VisibleChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def ProcessCmdKey(self,*args):
  """
  ProcessCmdKey(self: ToolStrip,m: Message,keyData: Keys) -> (bool,Message)
  
   Processes a command key.
  
   m: A System.Windows.Forms.Message,passed by reference,that represents the window message 
    to process.
  
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
  ProcessDialogKey(self: ToolStrip,keyData: Keys) -> bool
  
   Processes a dialog box key.
  
   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
   Returns: true if the key was processed by the control; otherwise,false.
  """
  pass
 def ProcessKeyEventArgs(self,*args):
  """
  ProcessKeyEventArgs(self: Control,m: Message) -> (bool,Message)
  
   Processes a key message and generates the appropriate control events.
  
   m: A System.Windows.Forms.Message,passed by reference,that represents the window message 
    to process.
  
   Returns: true if the message was processed by the control; otherwise,false.
  """
  pass
 def ProcessKeyMessage(self,*args):
  """
  ProcessKeyMessage(self: Control,m: Message) -> (bool,Message)
  
   Processes a keyboard message.
  
   m: A System.Windows.Forms.Message,passed by reference,that represents the window message 
    to process.
  
   Returns: true if the message was processed by the control; otherwise,false.
  """
  pass
 def ProcessKeyPreview(self,*args):
  """
  ProcessKeyPreview(self: Control,m: Message) -> (bool,Message)
  
   Previews a keyboard message.
  
   m: A System.Windows.Forms.Message,passed by reference,that represents the window message 
    to process.
  
   Returns: true if the message was processed by the control; otherwise,false.
  """
  pass
 def ProcessMnemonic(self,*args):
  """
  ProcessMnemonic(self: ToolStrip,charCode: Char) -> bool
  
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
 def RescaleConstantsForDpi(self,*args):
  """ RescaleConstantsForDpi(self: Control,deviceDpiOld: int,deviceDpiNew: int) """
  pass
 def ResetMinimumSize(self):
  """
  ResetMinimumSize(self: ToolStrip)
   This method is not relevant for this class.
  """
  pass
 def ResetMouseEventArgs(self,*args):
  """
  ResetMouseEventArgs(self: Control)
   Resets the control to handle the System.Windows.Forms.Control.MouseLeave event.
  """
  pass
 def RestoreFocus(self,*args):
  """
  RestoreFocus(self: ToolStrip)
   Controls the return location of the focus.
  """
  pass
 def RtlTranslateAlignment(self,*args):
  """
  RtlTranslateAlignment(self: Control,align: HorizontalAlignment) -> HorizontalAlignment
  
   Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate 
    System.Windows.Forms.HorizontalAlignment to support right-to-left text.
  
  
   align: One of the System.Windows.Forms.HorizontalAlignment values.
   Returns: One of the System.Windows.Forms.HorizontalAlignment values.
  RtlTranslateAlignment(self: Control,align: LeftRightAlignment) -> LeftRightAlignment
  
   Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate 
    System.Windows.Forms.LeftRightAlignment to support right-to-left text.
  
  
   align: One of the System.Windows.Forms.LeftRightAlignment values.
   Returns: One of the System.Windows.Forms.LeftRightAlignment values.
  RtlTranslateAlignment(self: Control,align: ContentAlignment) -> ContentAlignment
  
   Converts the specified System.Drawing.ContentAlignment to the appropriate 
    System.Drawing.ContentAlignment to support right-to-left text.
  
  
   align: One of the System.Drawing.ContentAlignment values.
   Returns: One of the System.Drawing.ContentAlignment values.
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
  ScaleControl(self: ScrollableControl,factor: SizeF,specified: BoundsSpecified)
   factor: The factor by which the height and width of the control will be scaled.
   specified: A System.Windows.Forms.BoundsSpecified value that specifies the bounds of the control to 
    use when defining its size and position.
  """
  pass
 def ScaleCore(self,*args):
  """
  ScaleCore(self: ScrollableControl,dx: Single,dy: Single)
   dx: The horizontal scaling factor.
   dy: The vertical scaling factor.
  """
  pass
 def ScrollToControl(self,*args):
  """
  ScrollToControl(self: ScrollableControl,activeControl: Control) -> Point
  
   Calculates the scroll offset to the specified child control.
  
   activeControl: The child control to scroll into view.
   Returns: The upper-left hand System.Drawing.Point of the display area relative to the client area 
    required to scroll the control into view.
  """
  pass
 def Select(self):
  """
  Select(self: ToolStrip,directed: bool,forward: bool)
   Activates a child control. Optionally specifies the direction in the tab order to select 
    the control from.
  
  
   directed: true to specify the direction of the control to select; otherwise,false.
   forward: true to move forward in the tab order; false to move backward in the tab order.
  """
  pass
 def SetAutoScrollMargin(self,x,y):
  """
  SetAutoScrollMargin(self: ToolStrip,x: int,y: int)
   This method is not relevant for this class.
  
   x: An System.Int32.
   y: An System.Int32.
  """
  pass
 def SetAutoSizeMode(self,*args):
  """
  SetAutoSizeMode(self: Control,mode: AutoSizeMode)
   Sets a value indicating how a control will behave when its 
    System.Windows.Forms.Control.AutoSize property is enabled.
  
  
   mode: One of the System.Windows.Forms.AutoSizeMode values.
  """
  pass
 def SetBoundsCore(self,*args):
  """
  SetBoundsCore(self: ToolStrip,x: int,y: int,width: int,height: int,specified: BoundsSpecified)
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
 def SetDisplayedItems(self,*args):
  """
  SetDisplayedItems(self: ToolStrip)
   Resets the collection of displayed and overflow items after a layout is done.
  """
  pass
 def SetDisplayRectLocation(self,*args):
  """
  SetDisplayRectLocation(self: ScrollableControl,x: int,y: int)
   Positions the display window to the specified value.
  
   x: The horizontal offset at which to position the System.Windows.Forms.ScrollableControl.
   y: The vertical offset at which to position the System.Windows.Forms.ScrollableControl.
  """
  pass
 def SetItemLocation(self,*args):
  """
  SetItemLocation(self: ToolStrip,item: ToolStripItem,location: Point)
   Anchors a System.Windows.Forms.ToolStripItem to a particular place on a 
    System.Windows.Forms.ToolStrip.
  
  
   item: The System.Windows.Forms.ToolStripItem to anchor.
   location: A System.Drawing.Point representing the x and y client coordinates of the 
    System.Windows.Forms.ToolStripItem location,in pixels.
  """
  pass
 def SetItemParent(self,*args):
  """
  SetItemParent(item: ToolStripItem,parent: ToolStrip)
   Enables you to change the parent System.Windows.Forms.ToolStrip of a 
    System.Windows.Forms.ToolStripItem.
  
  
   item: The System.Windows.Forms.ToolStripItem whose System.Windows.Forms.Control.Parent property 
    is to be changed.
  
   parent: The System.Windows.Forms.ToolStrip that is the parent of the 
    System.Windows.Forms.ToolStripItem referred to by the item parameter.
  """
  pass
 def SetScrollState(self,*args):
  """
  SetScrollState(self: ScrollableControl,bit: int,value: bool)
   Sets the specified scroll state flag.
  
   bit: The scroll state flag to set.
   value: The value to set the flag.
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
  SetVisibleCore(self: ToolStrip,visible: bool)
   Retrieves a value that sets the System.Windows.Forms.ToolStripItem to the specified 
    visibility state.
  
  
   visible: true if the System.Windows.Forms.ToolStripItem is visible; otherwise,false.
  """
  pass
 def SizeFromClientSize(self,*args):
  """
  SizeFromClientSize(self: Control,clientSize: Size) -> Size
  
   Determines the size of the entire control from the height and width of its client area.
  
   clientSize: A System.Drawing.Size value representing the height and width of the control's client 
    area.
  
   Returns: A System.Drawing.Size value representing the height and width of the entire control.
  """
  pass
 def ToString(self):
  """ ToString(self: ToolStrip) -> str """
  pass
 def UpdateBounds(self,*args):
  """
  UpdateBounds(self: Control)
   Updates the bounds of the control with the current size and location.
  UpdateBounds(self: Control,x: int,y: int,width: int,height: int)
   Updates the bounds of the control with the specified size and location.
  
   x: The System.Drawing.Point.X coordinate of the control.
   y: The System.Drawing.Point.Y coordinate of the control.
   width: The System.Drawing.Size.Width of the control.
   height: The System.Drawing.Size.Height of the control.
  UpdateBounds(self: Control,x: int,y: int,width: int,height: int,clientWidth: int,clientHeight: int)
   Updates the bounds of the control with the specified size,location,and client size.
  
   x: The System.Drawing.Point.X coordinate of the control.
   y: The System.Drawing.Point.Y coordinate of the control.
   width: The System.Drawing.Size.Width of the control.
   height: The System.Drawing.Size.Height of the control.
   clientWidth: The client System.Drawing.Size.Width of the control.
   clientHeight: The client System.Drawing.Size.Height of the control.
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
  WndProc(self: ToolStrip,m: Message) -> Message
  
   Processes Windows messages.
  
   m: The Windows System.Windows.Forms.Message to process.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,items=None):
  """
  __new__(cls: type)
  __new__(cls: type,*items: Array[ToolStripItem])
  """
  pass
 def __str__(self,*args):
  pass
 AllowDrop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether drag-and-drop and item reordering are handled through events that you implement.

Get: AllowDrop(self: ToolStrip) -> bool

Set: AllowDrop(self: ToolStrip)=value
"""

 AllowItemReorder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether drag-and-drop and item reordering are handled privately by the System.Windows.Forms.ToolStrip class.

Get: AllowItemReorder(self: ToolStrip) -> bool

Set: AllowItemReorder(self: ToolStrip)=value
"""

 AllowMerge=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether multiple System.Windows.Forms.MenuStrip,System.Windows.Forms.ToolStripDropDownMenu,System.Windows.Forms.ToolStripMenuItem,and other types can be combined.

Get: AllowMerge(self: ToolStrip) -> bool

Set: AllowMerge(self: ToolStrip)=value
"""

 Anchor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the edges of the container to which a System.Windows.Forms.ToolStrip is bound and determines how a System.Windows.Forms.ToolStrip is resized with its parent.

Get: Anchor(self: ToolStrip) -> AnchorStyles

Set: Anchor(self: ToolStrip)=value
"""

 AutoScroll=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: AutoScroll(self: ToolStrip) -> bool

Set: AutoScroll(self: ToolStrip)=value
"""

 AutoScrollMargin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: AutoScrollMargin(self: ToolStrip) -> Size

Set: AutoScrollMargin(self: ToolStrip)=value
"""

 AutoScrollMinSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: AutoScrollMinSize(self: ToolStrip) -> Size

Set: AutoScrollMinSize(self: ToolStrip)=value
"""

 AutoScrollPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: AutoScrollPosition(self: ToolStrip) -> Point

Set: AutoScrollPosition(self: ToolStrip)=value
"""

 AutoSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control is automatically resized to display its entire contents.

Get: AutoSize(self: ToolStrip) -> bool

Set: AutoSize(self: ToolStrip)=value
"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color for the System.Windows.Forms.ToolStrip.

Get: BackColor(self: ToolStrip) -> Color

Set: BackColor(self: ToolStrip)=value
"""

 BindingContext=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the binding context for the System.Windows.Forms.ToolStrip.

Get: BindingContext(self: ToolStrip) -> BindingContext

Set: BindingContext(self: ToolStrip)=value
"""

 CanEnableIme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value,to enable IME support.

"""

 CanOverflow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether items in the System.Windows.Forms.ToolStrip can be sent to an overflow menu.

Get: CanOverflow(self: ToolStrip) -> bool

Set: CanOverflow(self: ToolStrip)=value
"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if events can be raised on the control.

"""

 CausesValidation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ToolStrip causes validation to be performed on any controls that require validation when it receives focus.

Get: CausesValidation(self: ToolStrip) -> bool

Set: CausesValidation(self: ToolStrip)=value
"""

 Controls=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: Controls(self: ToolStrip) -> ControlCollection

"""

 CreateParams=property(lambda self: object(),lambda self,v: None,lambda self: None)

 Cursor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the cursor that is displayed when the mouse pointer is over the System.Windows.Forms.ToolStrip.

Get: Cursor(self: ToolStrip) -> Cursor

Set: Cursor(self: ToolStrip)=value
"""

 DefaultCursor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default cursor for the control.

"""

 DefaultDock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the docking location of the System.Windows.Forms.ToolStrip,indicating which borders are docked to the container.

"""

 DefaultDropDownDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value representing the default direction in which a System.Windows.Forms.ToolStripDropDown control is displayed relative to the System.Windows.Forms.ToolStrip.

Get: DefaultDropDownDirection(self: ToolStrip) -> ToolStripDropDownDirection

Set: DefaultDropDownDirection(self: ToolStrip)=value
"""

 DefaultGripMargin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default spacing,in pixels,between the sizing grip and the edges of the System.Windows.Forms.ToolStrip.

"""

 DefaultImeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default Input Method Editor (IME) mode supported by the control.

"""

 DefaultMargin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the spacing,in pixels,between the System.Windows.Forms.ToolStrip and the System.Windows.Forms.ToolStripContainer.

"""

 DefaultMaximumSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length and height,in pixels,that is specified as the default maximum size of a control.

"""

 DefaultMinimumSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length and height,in pixels,that is specified as the default minimum size of a control.

"""

 DefaultPadding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the internal spacing,in pixels,of the contents of a System.Windows.Forms.ToolStrip.

"""

 DefaultShowItemToolTips=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether ToolTips are shown for the System.Windows.Forms.ToolStrip by default.

"""

 DefaultSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default size of the System.Windows.Forms.ToolStrip.

"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

 DisplayedItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the subset of items that are currently displayed on the System.Windows.Forms.ToolStrip,including items that are automatically added into the System.Windows.Forms.ToolStrip.

"""

 DisplayRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves the current display rectangle.

Get: DisplayRectangle(self: ToolStrip) -> Rectangle

"""

 Dock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets which System.Windows.Forms.ToolStrip borders are docked to its parent control and determines how a System.Windows.Forms.ToolStrip is resized with its parent.

Get: Dock(self: ToolStrip) -> DockStyle

Set: Dock(self: ToolStrip)=value
"""

 DoubleBuffered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this control should redraw its surface using a secondary buffer to reduce or prevent flicker.

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

 Font=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the font used to display text in the control.

Get: Font(self: ToolStrip) -> Font

Set: Font(self: ToolStrip)=value
"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the font of the control.

"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of the System.Windows.Forms.ToolStrip.

Get: ForeColor(self: ToolStrip) -> Color

Set: ForeColor(self: ToolStrip)=value
"""

 GripDisplayStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the orientation of the System.Windows.Forms.ToolStrip move handle.

Get: GripDisplayStyle(self: ToolStrip) -> ToolStripGripDisplayStyle

"""

 GripMargin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the space around the System.Windows.Forms.ToolStrip move handle.

Get: GripMargin(self: ToolStrip) -> Padding

Set: GripMargin(self: ToolStrip)=value
"""

 GripRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the boundaries of the System.Windows.Forms.ToolStrip move handle.

Get: GripRectangle(self: ToolStrip) -> Rectangle

"""

 GripStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the System.Windows.Forms.ToolStrip move handle is visible or hidden.

Get: GripStyle(self: ToolStrip) -> ToolStripGripStyle

Set: GripStyle(self: ToolStrip)=value
"""

 HasChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: HasChildren(self: ToolStrip) -> bool

"""

 HorizontalScroll=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: HorizontalScroll(self: ToolStrip) -> HScrollProperties

"""

 HScroll=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the horizontal scroll bar is visible.

"""

 ImageList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the image list that contains the image displayed on a System.Windows.Forms.ToolStrip item.

Get: ImageList(self: ToolStrip) -> ImageList

Set: ImageList(self: ToolStrip)=value
"""

 ImageScalingSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size,in pixels,of an image used on a System.Windows.Forms.ToolStrip.

Get: ImageScalingSize(self: ToolStrip) -> Size

Set: ImageScalingSize(self: ToolStrip)=value
"""

 ImeModeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the IME mode of a control.

"""

 IsCurrentlyDragging=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user is currently moving the System.Windows.Forms.ToolStrip from one System.Windows.Forms.ToolStripContainer to another.

Get: IsCurrentlyDragging(self: ToolStrip) -> bool

"""

 IsDropDown=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether a System.Windows.Forms.ToolStrip is a System.Windows.Forms.ToolStripDropDown control.

Get: IsDropDown(self: ToolStrip) -> bool

"""

 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all the items that belong to a System.Windows.Forms.ToolStrip.

Get: Items(self: ToolStrip) -> ToolStripItemCollection

"""

 LayoutEngine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Passes a reference to the cached System.Windows.Forms.Control.LayoutEngine returned by the layout engine interface.

Get: LayoutEngine(self: ToolStrip) -> LayoutEngine

"""

 LayoutSettings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets layout scheme characteristics.

Get: LayoutSettings(self: ToolStrip) -> LayoutSettings

Set: LayoutSettings(self: ToolStrip)=value
"""

 LayoutStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating how the System.Windows.Forms.ToolStrip lays out the items collection.

Get: LayoutStyle(self: ToolStrip) -> ToolStripLayoutStyle

Set: LayoutStyle(self: ToolStrip)=value
"""

 MaxItemSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the maximum height and width,in pixels,of the System.Windows.Forms.ToolStrip.

"""

 Orientation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the orientation of the System.Windows.Forms.ToolStripPanel.

Get: Orientation(self: ToolStrip) -> Orientation

"""

 OverflowButton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ToolStripItem that is the overflow button for a System.Windows.Forms.ToolStrip with overflow enabled.

Get: OverflowButton(self: ToolStrip) -> ToolStripOverflowButton

"""

 Renderer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Windows.Forms.ToolStripRenderer used to customize the look and feel of a System.Windows.Forms.ToolStrip.

Get: Renderer(self: ToolStrip) -> ToolStripRenderer

Set: Renderer(self: ToolStrip)=value
"""

 RenderMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates which visual styles will be applied to the System.Windows.Forms.ToolStrip.

Get: RenderMode(self: ToolStrip) -> ToolStripRenderMode

Set: RenderMode(self: ToolStrip)=value
"""

 RenderRightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is now obsolete.

"""

 ResizeRedraw=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control redraws itself when resized.

"""

 ScaleChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines the scaling of child controls.

"""

 ShowFocusCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control should display focus rectangles.

"""

 ShowItemToolTips=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether ToolTips are to be displayed on System.Windows.Forms.ToolStrip items.

Get: ShowItemToolTips(self: ToolStrip) -> bool

Set: ShowItemToolTips(self: ToolStrip)=value
"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user interface is in the appropriate state to show or hide keyboard accelerators.

"""

 Stretch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ToolStrip stretches from end to end in the System.Windows.Forms.ToolStripContainer.

Get: Stretch(self: ToolStrip) -> bool

Set: Stretch(self: ToolStrip)=value
"""

 TabStop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the user can give the focus to an item in the System.Windows.Forms.ToolStrip using the TAB key.

Get: TabStop(self: ToolStrip) -> bool

Set: TabStop(self: ToolStrip)=value
"""

 TextDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the direction in which to draw text on a System.Windows.Forms.ToolStrip.

Get: TextDirection(self: ToolStrip) -> ToolStripTextDirection

Set: TextDirection(self: ToolStrip)=value
"""

 VerticalScroll=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: VerticalScroll(self: ToolStrip) -> VScrollProperties

"""

 VScroll=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the vertical scroll bar is visible.

"""


 AutoSizeChanged=None
 BeginDrag=None
 CausesValidationChanged=None
 ControlAdded=None
 ControlRemoved=None
 CursorChanged=None
 EndDrag=None
 ForeColorChanged=None
 ItemAdded=None
 ItemClicked=None
 ItemRemoved=None
 LayoutCompleted=None
 LayoutStyleChanged=None
 PaintGrip=None
 RendererChanged=None
 ToolStripAccessibleObject=None

