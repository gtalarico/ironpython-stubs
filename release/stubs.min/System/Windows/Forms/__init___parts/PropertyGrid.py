class PropertyGrid:
 """
 Provides a user interface for browsing the properties of an object.
 
 PropertyGrid()
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
  AdjustFormScrollbars(self: ContainerControl,displayScrollbars: bool)
   displayScrollbars: true to show the scroll bars; otherwise,false.
  """
  pass
 def CollapseAllGridItems(self):
  """
  CollapseAllGridItems(self: PropertyGrid)
   Collapses all the categories in the System.Windows.Forms.PropertyGrid.
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
 def CreatePropertyTab(self,*args):
  """
  CreatePropertyTab(self: PropertyGrid,tabType: Type) -> PropertyTab
  
   When overridden in a derived class,enables the creation of a 
    System.Windows.Forms.Design.PropertyTab.
  
  
   tabType: The type of tab to create.
   Returns: The newly created property tab. Returns null in its default implementation.
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
  Dispose(self: PropertyGrid,disposing: bool)
   Disposes of the resources (other than memory) used by the 
    System.Windows.Forms.PropertyGrid.
  
  
   disposing: true to release both managed and unmanaged resources; false to release only unmanaged 
    resources.
  """
  pass
 def ExpandAllGridItems(self):
  """
  ExpandAllGridItems(self: PropertyGrid)
   Expands all the categories in the System.Windows.Forms.PropertyGrid.
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
  IsInputChar(self: Control,charCode: Char) -> bool
  
   Determines if a character is an input character that the control recognizes.
  
   charCode: The character to test.
   Returns: true if the character should be sent directly to the control and not preprocessed; 
    otherwise,false.
  """
  pass
 def IsInputKey(self,*args):
  """
  IsInputKey(self: Control,keyData: Keys) -> bool
  
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
 def OnAutoValidateChanged(self,*args):
  """
  OnAutoValidateChanged(self: ContainerControl,e: EventArgs)
   Raises the System.Windows.Forms.ContainerControl.AutoValidateChanged event.
  
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
 def OnComComponentNameChanged(self,*args):
  """
  OnComComponentNameChanged(self: PropertyGrid,e: ComponentRenameEventArgs)
   Raises the 
    System.Windows.Forms.ComponentModel.Com2Interop.IComPropertyBrowser.ComComponentNameChange
    d event.
  
  
   e: A System.ComponentModel.Design.ComponentRenameEventArgs that contains the event data.
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
  """ OnCreateControl(self: ContainerControl) """
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
 def OnEnabledChanged(self,*args):
  """
  OnEnabledChanged(self: PropertyGrid,e: EventArgs)
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
  OnFontChanged(self: PropertyGrid,e: EventArgs)
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
  OnGotFocus(self: PropertyGrid,e: EventArgs)
   Raises the System.Windows.Forms.Control.GotFocus event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleCreated(self,*args):
  """
  OnHandleCreated(self: PropertyGrid,e: EventArgs)
   Raises the System.Windows.Forms.Control.HandleCreated event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleDestroyed(self,*args):
  """
  OnHandleDestroyed(self: PropertyGrid,e: EventArgs)
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
  OnLayout(self: ContainerControl,e: LayoutEventArgs)
   Raises the System.Windows.Forms.Control.Layout event.
  
   e: A System.Windows.Forms.LayoutEventArgs that contains the event data.
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
  OnMouseDown(self: PropertyGrid,me: MouseEventArgs)
   Raises the System.Windows.Forms.Control.MouseDown event.
  
   me: A System.Windows.Forms.MouseEventArgs that contains the event data.
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
  OnMouseMove(self: PropertyGrid,me: MouseEventArgs)
   Raises the System.Windows.Forms.Control.MouseMove event.
  
   me: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseUp(self,*args):
  """
  OnMouseUp(self: PropertyGrid,me: MouseEventArgs)
   Raises the System.Windows.Forms.Control.MouseUp event.
  
   me: A System.Windows.Forms.MouseEventArgs that contains the event data.
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
 def OnNotifyPropertyValueUIItemsChanged(self,*args):
  """
  OnNotifyPropertyValueUIItemsChanged(self: PropertyGrid,sender: object,e: EventArgs)
   Raises the 
    System.Drawing.Design.IPropertyValueUIService.NotifyPropertyValueUIItemsChanged event.
  
  
   sender: The source of the event.
   e: A System.EventArgs that contains the event data.
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
  OnPaint(self: PropertyGrid,pevent: PaintEventArgs)
   Raises the System.Windows.Forms.Control.Paint event.
  
   pevent: A System.Windows.Forms.PaintEventArgs that contains the event data.
  """
  pass
 def OnPaintBackground(self,*args):
  """
  OnPaintBackground(self: ScrollableControl,e: PaintEventArgs)
   Paints the background of the control.
  
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
  OnParentChanged(self: ContainerControl,e: EventArgs)
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
 def OnPropertySortChanged(self,*args):
  """
  OnPropertySortChanged(self: PropertyGrid,e: EventArgs)
   Raises the System.Windows.Forms.PropertyGrid.PropertySortChanged event.
  
   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnPropertyTabChanged(self,*args):
  """
  OnPropertyTabChanged(self: PropertyGrid,e: PropertyTabChangedEventArgs)
   Raises the System.Windows.Forms.PropertyGrid.PropertyTabChanged event.
  
   e: A System.Windows.Forms.PropertyTabChangedEventArgs that contains the event data.
  """
  pass
 def OnPropertyValueChanged(self,*args):
  """
  OnPropertyValueChanged(self: PropertyGrid,e: PropertyValueChangedEventArgs)
   Raises the System.Windows.Forms.PropertyGrid.PropertyValueChanged event.
  
   e: A System.Windows.Forms.PropertyValueChangedEventArgs that contains the event data.
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
  OnResize(self: PropertyGrid,e: EventArgs)
   Raises the System.Windows.Forms.Control.Resize event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRightToLeftChanged(self,*args):
  """
  OnRightToLeftChanged(self: ScrollableControl,e: EventArgs)
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnScroll(self,*args):
  """
  OnScroll(self: ScrollableControl,se: ScrollEventArgs)
   Raises the System.Windows.Forms.ScrollableControl.Scroll event.
  
   se: A System.Windows.Forms.ScrollEventArgs that contains the event data.
  """
  pass
 def OnSelectedGridItemChanged(self,*args):
  """
  OnSelectedGridItemChanged(self: PropertyGrid,e: SelectedGridItemChangedEventArgs)
   Raises the System.Windows.Forms.PropertyGrid.SelectedGridItemChanged event.
  
   e: A System.Windows.Forms.SelectedGridItemChangedEventArgs that contains the event data.
  """
  pass
 def OnSelectedObjectsChanged(self,*args):
  """
  OnSelectedObjectsChanged(self: PropertyGrid,e: EventArgs)
   Raises the System.Windows.Forms.PropertyGrid.SelectedObjectsChanged event.
  
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
  OnSystemColorsChanged(self: PropertyGrid,e: EventArgs)
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
  OnVisibleChanged(self: PropertyGrid,e: EventArgs)
   Raises the System.Windows.Forms.Control.VisibleChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def ProcessCmdKey(self,*args):
  """
  ProcessCmdKey(self: ContainerControl,msg: Message,keyData: Keys) -> (bool,Message)
  
   msg: A System.Windows.Forms.Message,passed by reference,that represents the window message 
    to process.
  
   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
   Returns: true if the character was processed by the control; otherwise,false.
  """
  pass
 def ProcessDialogChar(self,*args):
  """
  ProcessDialogChar(self: ContainerControl,charCode: Char) -> bool
  
   charCode: The character to process.
   Returns: true if the character was processed by the control; otherwise,false.
  """
  pass
 def ProcessDialogKey(self,*args):
  """
  ProcessDialogKey(self: PropertyGrid,keyData: Keys) -> bool
  
   Processes a dialog key.
  
   keyData: Specifies key codes and modifiers.
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
  ProcessMnemonic(self: ContainerControl,charCode: Char) -> bool
  
   charCode: The character to process.
   Returns: true if the character was processed as a mnemonic by the control; otherwise,false.
  """
  pass
 def ProcessTabKey(self,*args):
  """
  ProcessTabKey(self: ContainerControl,forward: bool) -> bool
  
   Selects the next available control and makes it the active control.
  
   forward: true to cycle forward through the controls in the System.Windows.Forms.ContainerControl; 
    otherwise,false.
  
   Returns: true if a control is selected; otherwise,false.
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
  """ Refresh(self: PropertyGrid) """
  pass
 def RefreshTabs(self,tabScope):
  """
  RefreshTabs(self: PropertyGrid,tabScope: PropertyTabScope)
   Refreshes the property tabs of the specified scope.
  
   tabScope: Either the Component or Document value of System.ComponentModel.PropertyTabScope.
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
 def ResetSelectedProperty(self):
  """
  ResetSelectedProperty(self: PropertyGrid)
   Resets the selected property to its default value.
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
  ScaleCore(self: PropertyGrid,dx: Single,dy: Single)
   This method is not relevant for this class.
  
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
  Select(self: ContainerControl,directed: bool,forward: bool)
   directed: true to specify the direction of the control to select; otherwise,false.
   forward: true to move forward in the tab order; false to move backward in the tab order.
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
 def SetDisplayRectLocation(self,*args):
  """
  SetDisplayRectLocation(self: ScrollableControl,x: int,y: int)
   Positions the display window to the specified value.
  
   x: The horizontal offset at which to position the System.Windows.Forms.ScrollableControl.
   y: The vertical offset at which to position the System.Windows.Forms.ScrollableControl.
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
  SetVisibleCore(self: Control,value: bool)
   Sets the control to the specified visible state.
  
   value: true to make the control visible; otherwise,false.
  """
  pass
 def ShowEventsButton(self,*args):
  """ ShowEventsButton(self: PropertyGrid,value: bool) """
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
 def UpdateDefaultButton(self,*args):
  """
  UpdateDefaultButton(self: ContainerControl)
   When overridden by a derived class,updates which button is the default button.
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
  WndProc(self: PropertyGrid,m: Message) -> Message
  
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
 def __str__(self,*args):
  pass
 AutoScaleFactor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the scaling factor between the current and design-time automatic scaling dimensions.

"""

 AutoScroll=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: AutoScroll(self: PropertyGrid) -> bool

Set: AutoScroll(self: PropertyGrid)=value
"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BackColor(self: PropertyGrid) -> Color

Set: BackColor(self: PropertyGrid)=value
"""

 BackgroundImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: BackgroundImage(self: PropertyGrid) -> Image

Set: BackgroundImage(self: PropertyGrid)=value
"""

 BackgroundImageLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: BackgroundImageLayout(self: PropertyGrid) -> ImageLayout

Set: BackgroundImageLayout(self: PropertyGrid)=value
"""

 BrowsableAttributes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the browsable attributes associated with the object that the property grid is attached to.

Get: BrowsableAttributes(self: PropertyGrid) -> AttributeCollection

Set: BrowsableAttributes(self: PropertyGrid)=value
"""

 CanEnableIme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value,to enable IME support.

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if events can be raised on the control.

"""

 CanShowCommands=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the commands pane can be made visible for the currently selected objects.

Get: CanShowCommands(self: PropertyGrid) -> bool

"""

 CanShowVisualStyleGlyphs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CanShowVisualStyleGlyphs(self: PropertyGrid) -> bool

Set: CanShowVisualStyleGlyphs(self: PropertyGrid)=value
"""

 CategoryForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text color used for category headings.

Get: CategoryForeColor(self: PropertyGrid) -> Color

Set: CategoryForeColor(self: PropertyGrid)=value
"""

 CategorySplitterColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CategorySplitterColor(self: PropertyGrid) -> Color

Set: CategorySplitterColor(self: PropertyGrid)=value
"""

 CommandsActiveLinkColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of active links in the executable commands region.

Get: CommandsActiveLinkColor(self: PropertyGrid) -> Color

Set: CommandsActiveLinkColor(self: PropertyGrid)=value
"""

 CommandsBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color of the hot commands region.

Get: CommandsBackColor(self: PropertyGrid) -> Color

Set: CommandsBackColor(self: PropertyGrid)=value
"""

 CommandsBorderColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CommandsBorderColor(self: PropertyGrid) -> Color

Set: CommandsBorderColor(self: PropertyGrid)=value
"""

 CommandsDisabledLinkColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the unavailable link color for the executable commands region.

Get: CommandsDisabledLinkColor(self: PropertyGrid) -> Color

Set: CommandsDisabledLinkColor(self: PropertyGrid)=value
"""

 CommandsForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color for the hot commands region.

Get: CommandsForeColor(self: PropertyGrid) -> Color

Set: CommandsForeColor(self: PropertyGrid)=value
"""

 CommandsLinkColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the link color for the executable commands region.

Get: CommandsLinkColor(self: PropertyGrid) -> Color

Set: CommandsLinkColor(self: PropertyGrid)=value
"""

 CommandsVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the commands pane is visible.

Get: CommandsVisible(self: PropertyGrid) -> bool

"""

 CommandsVisibleIfAvailable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the commands pane is visible for objects that expose verbs.

Get: CommandsVisibleIfAvailable(self: PropertyGrid) -> bool

Set: CommandsVisibleIfAvailable(self: PropertyGrid)=value
"""

 ContextMenuDefaultLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default location for the shortcut menu.

Get: ContextMenuDefaultLocation(self: PropertyGrid) -> Point

"""

 Controls=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: Controls(self: PropertyGrid) -> ControlCollection

"""

 CreateParams=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the required creation parameters when the control handle is created.

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

 DefaultTabType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of the default tab.

"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

 DisabledItemForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DisabledItemForeColor(self: PropertyGrid) -> Color

Set: DisabledItemForeColor(self: PropertyGrid)=value
"""

 DoubleBuffered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this control should redraw its surface using a secondary buffer to reduce or prevent flicker.

"""

 DrawFlatToolbar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.PropertyGrid control paints its toolbar with flat buttons.

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the font of the control.

"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: ForeColor(self: PropertyGrid) -> Color

Set: ForeColor(self: PropertyGrid)=value
"""

 HelpBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color for the Help region.

Get: HelpBackColor(self: PropertyGrid) -> Color

Set: HelpBackColor(self: PropertyGrid)=value
"""

 HelpBorderColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HelpBorderColor(self: PropertyGrid) -> Color

Set: HelpBorderColor(self: PropertyGrid)=value
"""

 HelpForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color for the Help region.

Get: HelpForeColor(self: PropertyGrid) -> Color

Set: HelpForeColor(self: PropertyGrid)=value
"""

 HelpVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Help text is visible.

Get: HelpVisible(self: PropertyGrid) -> bool

Set: HelpVisible(self: PropertyGrid)=value
"""

 HScroll=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the horizontal scroll bar is visible.

"""

 ImeModeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the IME mode of a control.

"""

 LargeButtons=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether buttons appear in standard size or in large size.

Get: LargeButtons(self: PropertyGrid) -> bool

Set: LargeButtons(self: PropertyGrid)=value
"""

 LineColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of the gridlines and borders.

Get: LineColor(self: PropertyGrid) -> Color

Set: LineColor(self: PropertyGrid)=value
"""

 Padding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: Padding(self: PropertyGrid) -> Padding

Set: Padding(self: PropertyGrid)=value
"""

 PropertySort=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type of sorting the System.Windows.Forms.PropertyGrid uses to display properties.

Get: PropertySort(self: PropertyGrid) -> PropertySort

Set: PropertySort(self: PropertyGrid)=value
"""

 PropertyTabs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of property tabs that are displayed in the grid.

Get: PropertyTabs(self: PropertyGrid) -> PropertyTabCollection

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

 SelectedGridItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the selected grid item.

Get: SelectedGridItem(self: PropertyGrid) -> GridItem

Set: SelectedGridItem(self: PropertyGrid)=value
"""

 SelectedItemWithFocusBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SelectedItemWithFocusBackColor(self: PropertyGrid) -> Color

Set: SelectedItemWithFocusBackColor(self: PropertyGrid)=value
"""

 SelectedItemWithFocusForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SelectedItemWithFocusForeColor(self: PropertyGrid) -> Color

Set: SelectedItemWithFocusForeColor(self: PropertyGrid)=value
"""

 SelectedObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object for which the grid displays properties.

Get: SelectedObject(self: PropertyGrid) -> object

Set: SelectedObject(self: PropertyGrid)=value
"""

 SelectedObjects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the currently selected objects.

Get: SelectedObjects(self: PropertyGrid) -> Array[object]

Set: SelectedObjects(self: PropertyGrid)=value
"""

 SelectedTab=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the currently selected property tab.

Get: SelectedTab(self: PropertyGrid) -> PropertyTab

"""

 ShowFocusCues=property(lambda self: object(),lambda self,v: None,lambda self: None)

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user interface is in the appropriate state to show or hide keyboard accelerators.

"""

 ShowPropertyPageImage=property(lambda self: object(),lambda self,v: None,lambda self: None)

 Site=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Site(self: PropertyGrid) -> ISite

Set: Site(self: PropertyGrid)=value
"""

 SortByCategoryImage=property(lambda self: object(),lambda self,v: None,lambda self: None)

 SortByPropertyImage=property(lambda self: object(),lambda self,v: None,lambda self: None)

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Text(self: PropertyGrid) -> str

Set: Text(self: PropertyGrid)=value
"""

 ToolbarVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the toolbar is visible.

Get: ToolbarVisible(self: PropertyGrid) -> bool

Set: ToolbarVisible(self: PropertyGrid)=value
"""

 ToolStripRenderer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the painting functionality for System.Windows.Forms.ToolStrip objects.

"""

 UseCompatibleTextRendering=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines whether to use the System.Drawing.Graphics class (GDI+) or the System.Windows.Forms.TextRenderer class (GDI) to render text.

Get: UseCompatibleTextRendering(self: PropertyGrid) -> bool

Set: UseCompatibleTextRendering(self: PropertyGrid)=value
"""

 ViewBackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the background color in the grid.

Get: ViewBackColor(self: PropertyGrid) -> Color

Set: ViewBackColor(self: PropertyGrid)=value
"""

 ViewBorderColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ViewBorderColor(self: PropertyGrid) -> Color

Set: ViewBorderColor(self: PropertyGrid)=value
"""

 ViewForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the color of the text in the grid.

Get: ViewForeColor(self: PropertyGrid) -> Color

Set: ViewForeColor(self: PropertyGrid)=value
"""

 VScroll=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the vertical scroll bar is visible.

"""


 BackgroundImageChanged=None
 BackgroundImageLayoutChanged=None
 ForeColorChanged=None
 KeyDown=None
 KeyPress=None
 KeyUp=None
 MouseDown=None
 MouseEnter=None
 MouseLeave=None
 MouseMove=None
 MouseUp=None
 PaddingChanged=None
 PropertySortChanged=None
 PropertyTabChanged=None
 PropertyTabCollection=None
 PropertyValueChanged=None
 SelectedGridItemChanged=None
 SelectedObjectsChanged=None
 TextChanged=None

