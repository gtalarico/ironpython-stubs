class Form(ContainerControl,IComponent,IDisposable,IOleControl,IOleObject,IOleInPlaceObject,IOleInPlaceActiveObject,IOleWindow,IViewObject,IViewObject2,IPersist,IPersistStreamInit,IPersistPropertyBag,IPersistStorage,IQuickActivate,ISupportOleDropSource,IDropTarget,ISynchronizeInvoke,IWin32Window,IArrangedElement,IBindableComponent,IContainerControl):
 """
 Represents a window or dialog box that makes up an application's user interface.

 

 Form()
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
 def Activate(self):
  """
  Activate(self: Form)

   Activates the form and gives it focus.
  """
  pass
 def ActivateMdiChild(self,*args):
  """
  ActivateMdiChild(self: Form,form: Form)

   Activates the MDI child of a form.

  

   form: The child form to activate.
  """
  pass
 def AddOwnedForm(self,ownedForm):
  """
  AddOwnedForm(self: Form,ownedForm: Form)

   Adds an owned form to this form.

  

   ownedForm: The System.Windows.Forms.Form that this form will own.
  """
  pass
 def AdjustFormScrollbars(self,*args):
  """
  AdjustFormScrollbars(self: Form,displayScrollbars: bool)

   Adjusts the scroll bars on the container based on the current control positions and the control 

    currently selected.

  

  

   displayScrollbars: true to show the scroll bars; otherwise,false.
  """
  pass
 def ApplyAutoScaling(self,*args):
  """
  ApplyAutoScaling(self: Form)

   Resizes the form according to the current value of the 

    System.Windows.Forms.Form.AutoScaleBaseSize property and the size of the current font.
  """
  pass
 def CenterToParent(self,*args):
  """
  CenterToParent(self: Form)

   Centers the position of the form within the bounds of the parent form.
  """
  pass
 def CenterToScreen(self,*args):
  """
  CenterToScreen(self: Form)

   Centers the form on the current screen.
  """
  pass
 def Close(self):
  """
  Close(self: Form)

   Closes the form.
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
  CreateControlsInstance(self: Form) -> ControlCollection

   Returns: A new instance of System.Windows.Forms.Control.ControlCollection assigned to the control.
  """
  pass
 def CreateHandle(self,*args):
  """
  CreateHandle(self: Form)

   Creates the handle for the form. If a derived class overrides this function,it must call the 

    base implementation.
  """
  pass
 def DefWndProc(self,*args):
  """
  DefWndProc(self: Form,m: Message) -> Message

  

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
  Dispose(self: Form,disposing: bool)

   Disposes of the resources (other than memory) used by the System.Windows.Forms.Form.

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
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
 @staticmethod
 def GetAutoScaleSize(font):
  """
  GetAutoScaleSize(font: Font) -> SizeF

  

   Gets the size when autoscaling the form based on a specified font.

  

   font: A System.Drawing.Font representing the font to determine the autoscaled base size of the form.

   Returns: A System.Drawing.SizeF representing the autoscaled size of the form.
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
  GetScaledBounds(self: Form,bounds: Rectangle,factor: SizeF,specified: BoundsSpecified) -> Rectangle

  

   bounds: A System.Drawing.Rectangle that specifies the area for which to retrieve the display bounds.

   factor: The height and width of the control's bounds.

   specified: One of the values of System.Windows.Forms.BoundsSpecified that specifies the bounds of the 

    control to use when defining its size and position.

  

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
  IsInputKey(self: Control,keyData: Keys) -> bool

  

   Determines whether the specified key is a regular input key or a special key that requires 

    preprocessing.

  

  

   keyData: One of the System.Windows.Forms.Keys values.

   Returns: true if the specified key is a regular input key; otherwise,false.
  """
  pass
 def LayoutMdi(self,value):
  """
  LayoutMdi(self: Form,value: MdiLayout)

   Arranges the multiple-document interface (MDI) child forms within the MDI parent form.

  

   value: One of the System.Windows.Forms.MdiLayout values that defines the layout of MDI child forms.
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
 def OnActivated(self,*args):
  """
  OnActivated(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Form.Activated event.

  

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
  OnBackgroundImageChanged(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Control.BackgroundImageChanged event.

  

   e: An System.EventArgs that contains the data.
  """
  pass
 def OnBackgroundImageLayoutChanged(self,*args):
  """
  OnBackgroundImageLayoutChanged(self: Form,e: EventArgs)

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
 def OnClosed(self,*args):
  """
  OnClosed(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Form.Closed event.

  

   e: The System.EventArgs that contains the event data.
  """
  pass
 def OnClosing(self,*args):
  """
  OnClosing(self: Form,e: CancelEventArgs)

   Raises the System.Windows.Forms.Form.Closing event.

  

   e: A System.ComponentModel.CancelEventArgs that contains the event data.
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
  OnCreateControl(self: Form)

   Raises the CreateControl event.
  """
  pass
 def OnCursorChanged(self,*args):
  """
  OnCursorChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.CursorChanged event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDeactivate(self,*args):
  """
  OnDeactivate(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Form.Deactivate event.

  

   e: The System.EventArgs that contains the event data.
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
 def OnDpiChanged(self,*args):
  """ OnDpiChanged(self: Form,e: DpiChangedEventArgs) """
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
  OnEnabledChanged(self: Form,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnEnter(self,*args):
  """
  OnEnter(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Control.Enter event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnFontChanged(self,*args):
  """
  OnFontChanged(self: Form,e: EventArgs)

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
 def OnFormClosed(self,*args):
  """
  OnFormClosed(self: Form,e: FormClosedEventArgs)

   Raises the System.Windows.Forms.Form.FormClosed event.

  

   e: A System.Windows.Forms.FormClosedEventArgs that contains the event data.
  """
  pass
 def OnFormClosing(self,*args):
  """
  OnFormClosing(self: Form,e: FormClosingEventArgs)

   Raises the System.Windows.Forms.Form.FormClosing event.

  

   e: A System.Windows.Forms.FormClosingEventArgs that contains the event data.
  """
  pass
 def OnGetDpiScaledSize(self,*args):
  """ OnGetDpiScaledSize(self: Form,deviceDpiOld: int,deviceDpiNew: int,desiredSize: Size) -> (bool,Size) """
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
  OnHandleCreated(self: Form,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleDestroyed(self,*args):
  """
  OnHandleDestroyed(self: Form,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHelpButtonClicked(self,*args):
  """
  OnHelpButtonClicked(self: Form,e: CancelEventArgs)

   Raises the System.Windows.Forms.Form.HelpButtonClicked event.

  

   e: A System.ComponentModel.CancelEventArgs that contains the event data.
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
 def OnInputLanguageChanged(self,*args):
  """
  OnInputLanguageChanged(self: Form,e: InputLanguageChangedEventArgs)

   Raises the System.Windows.Forms.Form.InputLanguageChanged event.

  

   e: The System.Windows.Forms.InputLanguageChangedEventArgs that contains the event data.
  """
  pass
 def OnInputLanguageChanging(self,*args):
  """
  OnInputLanguageChanging(self: Form,e: InputLanguageChangingEventArgs)

   Raises the System.Windows.Forms.Form.InputLanguageChanging event.

  

   e: The System.Windows.Forms.InputLanguageChangingEventArgs that contains the event data.
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
  OnLayout(self: Form,levent: LayoutEventArgs)

   Raises the System.Windows.Forms.Control.Layout event.

  

   levent: The event data.
  """
  pass
 def OnLeave(self,*args):
  """
  OnLeave(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.Leave event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnLoad(self,*args):
  """
  OnLoad(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Form.Load event.

  

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
 def OnMaximizedBoundsChanged(self,*args):
  """
  OnMaximizedBoundsChanged(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Form.MaximizedBoundsChanged event.

  

   e: The System.EventArgs that contains the event data.
  """
  pass
 def OnMaximumSizeChanged(self,*args):
  """
  OnMaximumSizeChanged(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Form.MaximumSizeChanged event.

  

   e: The System.EventArgs that contains the event data.
  """
  pass
 def OnMdiChildActivate(self,*args):
  """
  OnMdiChildActivate(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Form.MdiChildActivate event.

  

   e: The System.EventArgs that contains the event data.
  """
  pass
 def OnMenuComplete(self,*args):
  """
  OnMenuComplete(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Form.MenuComplete event.

  

   e: The System.EventArgs that contains the event data.
  """
  pass
 def OnMenuStart(self,*args):
  """
  OnMenuStart(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Form.MenuStart event.

  

   e: The System.EventArgs that contains the event data.
  """
  pass
 def OnMinimumSizeChanged(self,*args):
  """
  OnMinimumSizeChanged(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Form.MinimumSizeChanged event.

  

   e: An System.EventArgs that contains the event data.
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
  OnPaint(self: Form,e: PaintEventArgs)

   e: A System.Windows.Forms.PaintEventArgs that contains the event data.
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
  OnResize(self: Form,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnResizeBegin(self,*args):
  """
  OnResizeBegin(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Form.ResizeBegin event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnResizeEnd(self,*args):
  """
  OnResizeEnd(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Form.ResizeEnd event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def OnRightToLeftChanged(self,*args):
  """
  OnRightToLeftChanged(self: ScrollableControl,e: EventArgs)

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnRightToLeftLayoutChanged(self,*args):
  """
  OnRightToLeftLayoutChanged(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Form.RightToLeftLayoutChanged event.

  

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
 def OnShown(self,*args):
  """
  OnShown(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Form.Shown event.

  

   e: A System.EventArgs that contains the event data.
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
  OnStyleChanged(self: Form,e: EventArgs)

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
  OnTextChanged(self: Form,e: EventArgs)

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
  OnVisibleChanged(self: Form,e: EventArgs)

   Raises the System.Windows.Forms.Control.VisibleChanged event.

  

   e: The System.EventArgs that contains the event data.
  """
  pass
 def ProcessCmdKey(self,*args):
  """
  ProcessCmdKey(self: Form,msg: Message,keyData: Keys) -> (bool,Message)

  

   Processes a command key.

  

   msg: A System.Windows.Forms.Message,passed by reference,that represents the Win32 message to 

    process.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   Returns: true if the keystroke was processed and consumed by the control; otherwise,false to allow 

    further processing.
  """
  pass
 def ProcessDialogChar(self,*args):
  """
  ProcessDialogChar(self: Form,charCode: Char) -> bool

  

   Processes a dialog character.

  

   charCode: The character to process.

   Returns: true if the character was processed by the control; otherwise,false.
  """
  pass
 def ProcessDialogKey(self,*args):
  """
  ProcessDialogKey(self: Form,keyData: Keys) -> bool

  

   Processes a dialog box key.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.

   Returns: true if the keystroke was processed and consumed by the control; otherwise,false to allow 

    further processing.
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
  ProcessKeyPreview(self: Form,m: Message) -> (bool,Message)

  

   m: A System.Windows.Forms.Message,passed by reference,that represents the window message to 

    process.

  

   Returns: true if the message was processed by the control; otherwise,false.
  """
  pass
 def ProcessMnemonic(self,*args):
  """
  ProcessMnemonic(self: Form,charCode: Char) -> bool

  

   Processes a mnemonic character.

  

   charCode: The character to process.

   Returns: true if the character was processed as a mnemonic by the control; otherwise,false.
  """
  pass
 def ProcessTabKey(self,*args):
  """
  ProcessTabKey(self: Form,forward: bool) -> bool

  

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
 def RemoveOwnedForm(self,ownedForm):
  """
  RemoveOwnedForm(self: Form,ownedForm: Form)

   Removes an owned form from this form.

  

   ownedForm: A System.Windows.Forms.Form representing the form to remove from the list of owned forms for 

    this form.
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
  ScaleControl(self: Form,factor: SizeF,specified: BoundsSpecified)

   Scales the location,size,padding,and margin of a control.

  

   factor: The factor by which the height and width of the control are scaled.

   specified: A System.Windows.Forms.BoundsSpecified value that specifies the bounds of the control to use 

    when defining its size and position.
  """
  pass
 def ScaleCore(self,*args):
  """
  ScaleCore(self: Form,x: Single,y: Single)

   Performs scaling of the form.

  

   x: Percentage to scale the form horizontally

   y: Percentage to scale the form vertically
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
  Select(self: Form,directed: bool,forward: bool)

   Selects this form,and optionally selects the next or previous control.

  

   directed: If set to true that the active control is changed

   forward: If directed is true,then this controls the direction in which focus is moved. If this is true,

    then the next control is selected; otherwise,the previous control is selected.
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
  SetBoundsCore(self: Form,x: int,y: int,width: int,height: int,specified: BoundsSpecified)

   x: The x-coordinate.

   y: The y-coordinate.

   width: The bounds width.

   height: The bounds height.

   specified: A value from the BoundsSpecified enumeration.
  """
  pass
 def SetClientSizeCore(self,*args):
  """
  SetClientSizeCore(self: Form,x: int,y: int)

   Sets the client size of the form. This will adjust the bounds of the form to make the client 

    size the requested size.

  

  

   x: Requested width of the client region.

   y: Requested height of the client region.
  """
  pass
 def SetDesktopBounds(self,x,y,width,height):
  """
  SetDesktopBounds(self: Form,x: int,y: int,width: int,height: int)

   Sets the bounds of the form in desktop coordinates.

  

   x: The x-coordinate of the form's location.

   y: The y-coordinate of the form's location.

   width: The width of the form.

   height: The height of the form.
  """
  pass
 def SetDesktopLocation(self,x,y):
  """
  SetDesktopLocation(self: Form,x: int,y: int)

   Sets the location of the form in desktop coordinates.

  

   x: The x-coordinate of the form's location.

   y: The y-coordinate of the form's location.
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
  SetVisibleCore(self: Form,value: bool)

   value: true to make the control visible; otherwise,false.
  """
  pass
 def Show(self,owner=None):
  """
  Show(self: Form,owner: IWin32Window)

   Shows the form with the specified owner to the user.

  

   owner: Any object that implements System.Windows.Forms.IWin32Window and represents the top-level window 

    that will own this form.
  """
  pass
 def ShowDialog(self,owner=None):
  """
  ShowDialog(self: Form,owner: IWin32Window) -> DialogResult

  

   Shows the form as a modal dialog box with the specified owner.

  

   owner: Any object that implements System.Windows.Forms.IWin32Window that represents the top-level 

    window that will own the modal dialog box.

  

   Returns: One of the System.Windows.Forms.DialogResult values.

  ShowDialog(self: Form) -> DialogResult

  

   Shows the form as a modal dialog box.

   Returns: One of the System.Windows.Forms.DialogResult values.
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
 def ToString(self):
  """
  ToString(self: Form) -> str

  

   Gets a string representing the current instance of the form.

   Returns: A string consisting of the fully qualified name of the form object's class,with the 

    System.Windows.Forms.Form.Text property of the form appended to the end. For example,if the 

    form is derived from the class MyForm in the MyNamespace namespace,and the 

    System.Windows.Forms.Form.Text property is set to Hello,World,this method will return 

    MyNamespace.MyForm,Text: Hello,World.
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
 def UpdateDefaultButton(self,*args):
  """
  UpdateDefaultButton(self: Form)

   Updates which button is the default button.
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
 def ValidateChildren(self,validationConstraints=None):
  """
  ValidateChildren(self: Form,validationConstraints: ValidationConstraints) -> bool

  

   validationConstraints: Places restrictions on which controls have their System.Windows.Forms.Control.Validating event 

    raised.

  

   Returns: true if all of the children validated successfully; otherwise,false. If called from the 

    System.Windows.Forms.Control.Validating or System.Windows.Forms.Control.Validated event 

    handlers,this method will always return false.

  

  ValidateChildren(self: Form) -> bool

   Returns: true if all of the children validated successfully; otherwise,false. If called from the 

    System.Windows.Forms.Control.Validating or System.Windows.Forms.Control.Validated event 

    handlers,this method will always return false.
  """
  pass
 def WndProc(self,*args):
  """
  WndProc(self: Form,m: Message) -> Message

  

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
 AcceptButton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the button on the form that is clicked when the user presses the ENTER key.



Get: AcceptButton(self: Form) -> IButtonControl



Set: AcceptButton(self: Form)=value

"""

 ActiveMdiChild=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the currently active multiple-document interface (MDI) child window.



Get: ActiveMdiChild(self: Form) -> Form



"""

 AllowTransparency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the opacity of the form can be adjusted.



Get: AllowTransparency(self: Form) -> bool



Set: AllowTransparency(self: Form)=value

"""

 AutoScale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the form adjusts its size to fit the height of the font used on the form and scales its controls.



Get: AutoScale(self: Form) -> bool



Set: AutoScale(self: Form)=value

"""

 AutoScaleBaseSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the base size used for autoscaling of the form.



Get: AutoScaleBaseSize(self: Form) -> Size



Set: AutoScaleBaseSize(self: Form)=value

"""

 AutoScaleFactor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the scaling factor between the current and design-time automatic scaling dimensions.



"""

 AutoScroll=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the form enables autoscrolling.



Get: AutoScroll(self: Form) -> bool



Set: AutoScroll(self: Form)=value

"""

 AutoSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Resize the form according to the setting of System.Windows.Forms.Form.AutoSizeMode.



Get: AutoSize(self: Form) -> bool



Set: AutoSize(self: Form)=value

"""

 AutoSizeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the mode by which the form automatically resizes itself.



Get: AutoSizeMode(self: Form) -> AutoSizeMode



Set: AutoSizeMode(self: Form)=value

"""

 AutoValidate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AutoValidate(self: Form) -> AutoValidate



Set: AutoValidate(self: Form)=value

"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: BackColor(self: Form) -> Color



Set: BackColor(self: Form)=value

"""

 CancelButton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the button control that is clicked when the user presses the ESC key.



Get: CancelButton(self: Form) -> IButtonControl



Set: CancelButton(self: Form)=value

"""

 CanEnableIme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value,to enable IME support.



"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if events can be raised on the control.



"""

 ClientSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size of the client area of the form.



Get: ClientSize(self: Form) -> Size



Set: ClientSize(self: Form)=value

"""

 ControlBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a control box is displayed in the caption bar of the form.



Get: ControlBox(self: Form) -> bool



Set: ControlBox(self: Form)=value

"""

 CreateParams=property(lambda self: object(),lambda self,v: None,lambda self: None)

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

 DesktopBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size and location of the form on the Windows desktop.



Get: DesktopBounds(self: Form) -> Rectangle



Set: DesktopBounds(self: Form)=value

"""

 DesktopLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the location of the form on the Windows desktop.



Get: DesktopLocation(self: Form) -> Point



Set: DesktopLocation(self: Form)=value

"""

 DialogResult=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the dialog result for the form.



Get: DialogResult(self: Form) -> DialogResult



Set: DialogResult(self: Form)=value

"""

 DoubleBuffered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this control should redraw its surface using a secondary buffer to reduce or prevent flicker.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the font of the control.



"""

 FormBorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the border style of the form.



Get: FormBorderStyle(self: Form) -> FormBorderStyle



Set: FormBorderStyle(self: Form)=value

"""

 HelpButton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a Help button should be displayed in the caption box of the form.



Get: HelpButton(self: Form) -> bool



Set: HelpButton(self: Form)=value

"""

 HScroll=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the horizontal scroll bar is visible.



"""

 Icon=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the icon for the form.



Get: Icon(self: Form) -> Icon



Set: Icon(self: Form)=value

"""

 ImeModeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the IME mode of a control.



"""

 IsMdiChild=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the form is a multiple-document interface (MDI) child form.



Get: IsMdiChild(self: Form) -> bool



"""

 IsMdiContainer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the form is a container for multiple-document interface (MDI) child forms.



Get: IsMdiContainer(self: Form) -> bool



Set: IsMdiContainer(self: Form)=value

"""

 IsRestrictedWindow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the form can use all windows and user input events without restriction.



Get: IsRestrictedWindow(self: Form) -> bool



"""

 KeyPreview=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the form will receive key events before the event is passed to the control that has focus.



Get: KeyPreview(self: Form) -> bool



Set: KeyPreview(self: Form)=value

"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Drawing.Point that represents the upper-left corner of the System.Windows.Forms.Form in screen coordinates.



Get: Location(self: Form) -> Point



Set: Location(self: Form)=value

"""

 MainMenuStrip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the primary menu container for the form.



Get: MainMenuStrip(self: Form) -> MenuStrip



Set: MainMenuStrip(self: Form)=value

"""

 Margin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the space between controls.



Get: Margin(self: Form) -> Padding



Set: Margin(self: Form)=value

"""

 MaximizeBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Maximize button is displayed in the caption bar of the form.



Get: MaximizeBox(self: Form) -> bool



Set: MaximizeBox(self: Form)=value

"""

 MaximizedBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the size of the form when it is maximized.



"""

 MaximumSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the maximum size the form can be resized to.



Get: MaximumSize(self: Form) -> Size



Set: MaximumSize(self: Form)=value

"""

 MdiChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an array of forms that represent the multiple-document interface (MDI) child forms that are parented to this form.



Get: MdiChildren(self: Form) -> Array[Form]



"""

 MdiParent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current multiple-document interface (MDI) parent form of this form.



Get: MdiParent(self: Form) -> Form



Set: MdiParent(self: Form)=value

"""

 Menu=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Forms.MainMenu that is displayed in the form.



Get: Menu(self: Form) -> MainMenu



Set: Menu(self: Form)=value

"""

 MergedMenu=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the merged menu for the form.



Get: MergedMenu(self: Form) -> MainMenu



"""

 MinimizeBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Minimize button is displayed in the caption bar of the form.



Get: MinimizeBox(self: Form) -> bool



Set: MinimizeBox(self: Form)=value

"""

 MinimumSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum size the form can be resized to.



Get: MinimumSize(self: Form) -> Size



Set: MinimumSize(self: Form)=value

"""

 Modal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this form is displayed modally.



Get: Modal(self: Form) -> bool



"""

 Opacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the opacity level of the form.



Get: Opacity(self: Form) -> float



Set: Opacity(self: Form)=value

"""

 OwnedForms=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an array of System.Windows.Forms.Form objects that represent all forms that are owned by this form.



Get: OwnedForms(self: Form) -> Array[Form]



"""

 Owner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the form that owns this form.



Get: Owner(self: Form) -> Form



Set: Owner(self: Form)=value

"""

 RenderRightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is now obsolete.



"""

 ResizeRedraw=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control redraws itself when resized.



"""

 RestoreBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the location and size of the form in its normal window state.



Get: RestoreBounds(self: Form) -> Rectangle



"""

 RightToLeftLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether right-to-left mirror placement is turned on.



Get: RightToLeftLayout(self: Form) -> bool



Set: RightToLeftLayout(self: Form)=value

"""

 ScaleChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines the scaling of child controls.



"""

 ShowFocusCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control should display focus rectangles.



"""

 ShowIcon=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether an icon is displayed in the caption bar of the form.



Get: ShowIcon(self: Form) -> bool



Set: ShowIcon(self: Form)=value

"""

 ShowInTaskbar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the form is displayed in the Windows taskbar.



Get: ShowInTaskbar(self: Form) -> bool



Set: ShowInTaskbar(self: Form)=value

"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user interface is in the appropriate state to show or hide keyboard accelerators.



"""

 ShowWithoutActivation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the window will be activated when it is shown.



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size of the form.



Get: Size(self: Form) -> Size



Set: Size(self: Form)=value

"""

 SizeGripStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style of the size grip to display in the lower-right corner of the form.



Get: SizeGripStyle(self: Form) -> SizeGripStyle



Set: SizeGripStyle(self: Form)=value

"""

 StartPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the starting position of the form at run time.



Get: StartPosition(self: Form) -> FormStartPosition



Set: StartPosition(self: Form)=value

"""

 TabIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the tab order of the control within its container.



Get: TabIndex(self: Form) -> int



Set: TabIndex(self: Form)=value

"""

 TabStop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the user can give the focus to this control using the TAB key.



Get: TabStop(self: Form) -> bool



Set: TabStop(self: Form)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Text(self: Form) -> str



Set: Text(self: Form)=value

"""

 TopLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to display the form as a top-level window.



Get: TopLevel(self: Form) -> bool



Set: TopLevel(self: Form)=value

"""

 TopMost=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the form should be displayed as a topmost form.



Get: TopMost(self: Form) -> bool



Set: TopMost(self: Form)=value

"""

 TransparencyKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color that will represent transparent areas of the form.



Get: TransparencyKey(self: Form) -> Color



Set: TransparencyKey(self: Form)=value

"""

 VScroll=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the vertical scroll bar is visible.



"""

 WindowState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether form is minimized,maximized,or normal.



Get: WindowState(self: Form) -> FormWindowState



Set: WindowState(self: Form)=value

"""


 Activated=None
 ActiveForm=None
 AutoSizeChanged=None
 AutoValidateChanged=None
 Closed=None
 Closing=None
 ControlCollection=None
 Deactivate=None
 DpiChanged=None
 FormClosed=None
 FormClosing=None
 HelpButtonClicked=None
 InputLanguageChanged=None
 InputLanguageChanging=None
 Load=None
 MarginChanged=None
 MaximizedBoundsChanged=None
 MaximumSizeChanged=None
 MdiChildActivate=None
 MenuComplete=None
 MenuStart=None
 MinimumSizeChanged=None
 ResizeBegin=None
 ResizeEnd=None
 RightToLeftLayoutChanged=None
 Shown=None
 TabIndexChanged=None
 TabStopChanged=None

