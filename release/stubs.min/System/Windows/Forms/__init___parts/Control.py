class Control(Component,IComponent,IDisposable,IOleControl,IOleObject,IOleInPlaceObject,IOleInPlaceActiveObject,IOleWindow,IViewObject,IViewObject2,IPersist,IPersistStreamInit,IPersistPropertyBag,IPersistStorage,IQuickActivate,ISupportOleDropSource,IDropTarget,ISynchronizeInvoke,IWin32Window,IArrangedElement,IBindableComponent):
 """
 Defines the base class for controls,which are components with visual representation.

 

 Control()

 Control(text: str)

 Control(text: str,left: int,top: int,width: int,height: int)

 Control(parent: Control,text: str)

 Control(parent: Control,text: str,left: int,top: int,width: int,height: int)
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
 def BeginInvoke(self,method,args=None):
  """
  BeginInvoke(self: Control,method: Delegate,*args: Array[object]) -> IAsyncResult

  

   Executes the specified delegate asynchronously with the specified arguments,on the thread that 

    the control's underlying handle was created on.

  

  

   method: A delegate to a method that takes parameters of the same number and type that are contained in 

    the args parameter.

  

   args: An array of objects to pass as arguments to the given method. This can be null if no arguments 

    are needed.

  

   Returns: An System.IAsyncResult that represents the result of the 

    System.Windows.Forms.Control.BeginInvoke(System.Delegate) operation.

  

  BeginInvoke(self: Control,method: Delegate) -> IAsyncResult

  

   Executes the specified delegate asynchronously on the thread that the control's underlying 

    handle was created on.

  

  

   method: A delegate to a method that takes no parameters.

   Returns: An System.IAsyncResult that represents the result of the 

    System.Windows.Forms.Control.BeginInvoke(System.Delegate) operation.
  """
  pass
 def BringToFront(self):
  """
  BringToFront(self: Control)

   Brings the control to the front of the z-order.
  """
  pass
 def Contains(self,ctl):
  """
  Contains(self: Control,ctl: Control) -> bool

  

   Retrieves a value indicating whether the specified control is a child of the control.

  

   ctl: The System.Windows.Forms.Control to evaluate.

   Returns: true if the specified control is a child of the control; otherwise,false.
  """
  pass
 def CreateAccessibilityInstance(self,*args):
  """
  CreateAccessibilityInstance(self: Control) -> AccessibleObject

  

   Creates a new accessibility object for the control.

   Returns: A new System.Windows.Forms.AccessibleObject for the control.
  """
  pass
 def CreateControl(self):
  """
  CreateControl(self: Control)

   Forces the creation of the visible control,including the creation of the handle and any visible 

    child controls.
  """
  pass
 def CreateControlsInstance(self,*args):
  """
  CreateControlsInstance(self: Control) -> ControlCollection

  

   Creates a new instance of the control collection for the control.

   Returns: A new instance of System.Windows.Forms.Control.ControlCollection assigned to the control.
  """
  pass
 def CreateGraphics(self):
  """
  CreateGraphics(self: Control) -> Graphics

  

   Creates the System.Drawing.Graphics for the control.

   Returns: The System.Drawing.Graphics for the control.
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
  Dispose(self: Control,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.Control and its child controls 

    and optionally releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def DoDragDrop(self,data,allowedEffects):
  """
  DoDragDrop(self: Control,data: object,allowedEffects: DragDropEffects) -> DragDropEffects

  

   Begins a drag-and-drop operation.

  

   data: The data to drag.

   allowedEffects: One of the System.Windows.Forms.DragDropEffects values.

   Returns: A value from the System.Windows.Forms.DragDropEffects enumeration that represents the final 

    effect that was performed during the drag-and-drop operation.
  """
  pass
 def DrawToBitmap(self,bitmap,targetBounds):
  """
  DrawToBitmap(self: Control,bitmap: Bitmap,targetBounds: Rectangle)

   Supports rendering to the specified bitmap.

  

   bitmap: The bitmap to be drawn to.

   targetBounds: The bounds within which the control is rendered.
  """
  pass
 def EndInvoke(self,asyncResult):
  """
  EndInvoke(self: Control,asyncResult: IAsyncResult) -> object

  

   Retrieves the return value of the asynchronous operation represented by the System.IAsyncResult 

    passed.

  

  

   asyncResult: The System.IAsyncResult that represents a specific invoke asynchronous operation,returned when 

    calling System.Windows.Forms.Control.BeginInvoke(System.Delegate).

  

   Returns: The System.Object generated by the asynchronous operation.
  """
  pass
 def FindForm(self):
  """
  FindForm(self: Control) -> Form

  

   Retrieves the form that the control is on.

   Returns: The System.Windows.Forms.Form that the control is on.
  """
  pass
 def Focus(self):
  """
  Focus(self: Control) -> bool

  

   Sets input focus to the control.

   Returns: true if the input focus request was successful; otherwise,false.
  """
  pass
 @staticmethod
 def FromChildHandle(handle):
  """
  FromChildHandle(handle: IntPtr) -> Control

  

   Retrieves the control that contains the specified handle.

  

   handle: The window handle (HWND) to search for.

   Returns: The System.Windows.Forms.Control that represents the control associated with the specified 

    handle; returns null if no control with the specified handle is found.
  """
  pass
 @staticmethod
 def FromHandle(handle):
  """
  FromHandle(handle: IntPtr) -> Control

  

   Returns the control that is currently associated with the specified handle.

  

   handle: The window handle (HWND) to search for.

   Returns: A System.Windows.Forms.Control that represents the control associated with the specified handle; 

    returns null if no control with the specified handle is found.
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
 def GetChildAtPoint(self,pt,skipValue=None):
  """
  GetChildAtPoint(self: Control,pt: Point) -> Control

  

   Retrieves the child control that is located at the specified coordinates.

  

   pt: A System.Drawing.Point that contains the coordinates where you want to look for a control. 

    Coordinates are expressed relative to the upper-left corner of the control's client area.

  

   Returns: A System.Windows.Forms.Control that represents the control that is located at the specified 

    point.

  

  GetChildAtPoint(self: Control,pt: Point,skipValue: GetChildAtPointSkip) -> Control

  

   Retrieves the child control that is located at the specified coordinates,specifying whether to 

    ignore child controls of a certain type.

  

  

   pt: A System.Drawing.Point that contains the coordinates where you want to look for a control. 

    Coordinates are expressed relative to the upper-left corner of the control's client area.

  

   skipValue: One of the values of System.Windows.Forms.GetChildAtPointSkip,determining whether to ignore 

    child controls of a certain type.

  

   Returns: The child System.Windows.Forms.Control at the specified coordinates.
  """
  pass
 def GetContainerControl(self):
  """
  GetContainerControl(self: Control) -> IContainerControl

  

   Returns the next System.Windows.Forms.ContainerControl up the control's chain of parent controls.

   Returns: An System.Windows.Forms.IContainerControl,that represents the parent of the 

    System.Windows.Forms.Control.
  """
  pass
 def GetNextControl(self,ctl,forward):
  """
  GetNextControl(self: Control,ctl: Control,forward: bool) -> Control

  

   Retrieves the next control forward or back in the tab order of child controls.

  

   ctl: The System.Windows.Forms.Control to start the search with.

   forward: true to search forward in the tab order; false to search backward.

   Returns: The next System.Windows.Forms.Control in the tab order.
  """
  pass
 def GetPreferredSize(self,proposedSize):
  """
  GetPreferredSize(self: Control,proposedSize: Size) -> Size

  

   Retrieves the size of a rectangular area into which a control can be fitted.

  

   proposedSize: The custom-sized area for a control.

   Returns: An ordered pair of type System.Drawing.Size representing the width and height of a rectangle.
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
 def Hide(self):
  """
  Hide(self: Control)

   Conceals the control from the user.
  """
  pass
 def InitLayout(self,*args):
  """
  InitLayout(self: Control)

   Called after the control has been added to another container.
  """
  pass
 def Invalidate(self,*__args):
  """
  Invalidate(self: Control,invalidateChildren: bool)

   Invalidates a specific region of the control and causes a paint message to be sent to the 

    control. Optionally,invalidates the child controls assigned to the control.

  

  

   invalidateChildren: true to invalidate the control's child controls; otherwise,false.

  Invalidate(self: Control,rc: Rectangle)

   Invalidates the specified region of the control (adds it to the control's update region,which 

    is the area that will be repainted at the next paint operation),and causes a paint message to 

    be sent to the control.

  

  

   rc: A System.Drawing.Rectangle that represents the region to invalidate.

  Invalidate(self: Control,rc: Rectangle,invalidateChildren: bool)

   Invalidates the specified region of the control (adds it to the control's update region,which 

    is the area that will be repainted at the next paint operation),and causes a paint message to 

    be sent to the control. Optionally,invalidates the child controls assigned to the control.

  

  

   rc: A System.Drawing.Rectangle that represents the region to invalidate.

   invalidateChildren: true to invalidate the control's child controls; otherwise,false.

  Invalidate(self: Control,region: Region)

   Invalidates the specified region of the control (adds it to the control's update region,which 

    is the area that will be repainted at the next paint operation),and causes a paint message to 

    be sent to the control.

  

  

   region: The System.Drawing.Region to invalidate.

  Invalidate(self: Control,region: Region,invalidateChildren: bool)

   Invalidates the specified region of the control (adds it to the control's update region,which 

    is the area that will be repainted at the next paint operation),and causes a paint message to 

    be sent to the control. Optionally,invalidates the child controls assigned to the control.

  

  

   region: The System.Drawing.Region to invalidate.

   invalidateChildren: true to invalidate the control's child controls; otherwise,false.

  Invalidate(self: Control)

   Invalidates the entire surface of the control and causes the control to be redrawn.
  """
  pass
 def Invoke(self,method,args=None):
  """
  Invoke(self: Control,method: Delegate,*args: Array[object]) -> object

  

   Executes the specified delegate,on the thread that owns the control's underlying window handle,

    with the specified list of arguments.

  

  

   method: A delegate to a method that takes parameters of the same number and type that are contained in 

    the args parameter.

  

   args: An array of objects to pass as arguments to the specified method. This parameter can be null if 

    the method takes no arguments.

  

   Returns: An System.Object that contains the return value from the delegate being invoked,or null if the 

    delegate has no return value.

  

  Invoke(self: Control,method: Delegate) -> object

  

   Executes the specified delegate on the thread that owns the control's underlying window handle.

  

   method: A delegate that contains a method to be called in the control's thread context.

   Returns: The return value from the delegate being invoked,or null if the delegate has no return value.
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
 @staticmethod
 def IsKeyLocked(keyVal):
  """
  IsKeyLocked(keyVal: Keys) -> bool

  

   Determines whether the CAPS LOCK,NUM LOCK,or SCROLL LOCK key is in effect.

  

   keyVal: The CAPS LOCK,NUM LOCK,or SCROLL LOCK member of the System.Windows.Forms.Keys enumeration.

   Returns: true if the specified key or keys are in effect; otherwise,false.
  """
  pass
 @staticmethod
 def IsMnemonic(charCode,text):
  """
  IsMnemonic(charCode: Char,text: str) -> bool

  

   Determines if the specified character is the mnemonic character assigned to the control in the 

    specified string.

  

  

   charCode: The character to test.

   text: The string to search.

   Returns: true if the charCode character is the mnemonic character assigned to the control; otherwise,

    false.
  """
  pass
 def LogicalToDeviceUnits(self,value):
  """ LogicalToDeviceUnits(self: Control,value: int) -> int """
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
  OnEnter(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.Enter event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnFontChanged(self,*args):
  """
  OnFontChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.FontChanged event.

  

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
  OnHandleCreated(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.HandleCreated event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleDestroyed(self,*args):
  """
  OnHandleDestroyed(self: Control,e: EventArgs)

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
 def OnRegionChanged(self,*args):
  """
  OnRegionChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.RegionChanged event.

  

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
  OnRightToLeftChanged(self: Control,e: EventArgs)

   Raises the System.Windows.Forms.Control.RightToLeftChanged event.

  

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
 def PerformLayout(self,affectedControl=None,affectedProperty=None):
  """
  PerformLayout(self: Control,affectedControl: Control,affectedProperty: str)

   Forces the control to apply layout logic to all its child controls.

  

   affectedControl: A System.Windows.Forms.Control that represents the most recently changed control.

   affectedProperty: The name of the most recently changed property on the control.

  PerformLayout(self: Control)

   Forces the control to apply layout logic to all its child controls.
  """
  pass
 def PointToClient(self,p):
  """
  PointToClient(self: Control,p: Point) -> Point

  

   Computes the location of the specified screen point into client coordinates.

  

   p: The screen coordinate System.Drawing.Point to convert.

   Returns: A System.Drawing.Point that represents the converted System.Drawing.Point,p,in client 

    coordinates.
  """
  pass
 def PointToScreen(self,p):
  """
  PointToScreen(self: Control,p: Point) -> Point

  

   Computes the location of the specified client point into screen coordinates.

  

   p: The client coordinate System.Drawing.Point to convert.

   Returns: A System.Drawing.Point that represents the converted System.Drawing.Point,p,in screen 

    coordinates.
  """
  pass
 def PreProcessControlMessage(self,msg):
  """
  PreProcessControlMessage(self: Control,msg: Message) -> (PreProcessControlState,Message)

  

   Preprocesses keyboard or input messages within the message loop before they are dispatched.

  

   msg: A System.Windows.Forms.Message that represents the message to process.

   Returns: One of the System.Windows.Forms.PreProcessControlState values,depending on whether 

    System.Windows.Forms.Control.PreProcessMessage(System.Windows.Forms.Message@) is true or false 

    and whether System.Windows.Forms.Control.IsInputKey(System.Windows.Forms.Keys) or 

    System.Windows.Forms.Control.IsInputChar(System.Char) are true or false.
  """
  pass
 def PreProcessMessage(self,msg):
  """
  PreProcessMessage(self: Control,msg: Message) -> (bool,Message)

  

   Preprocesses keyboard or input messages within the message loop before they are dispatched.

  

   msg: A System.Windows.Forms.Message,passed by reference,that represents the message to process. The 

    possible values are WM_KEYDOWN,WM_SYSKEYDOWN,WM_CHAR,and WM_SYSCHAR.

  

   Returns: true if the message was processed by the control; otherwise,false.
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
 def RectangleToClient(self,r):
  """
  RectangleToClient(self: Control,r: Rectangle) -> Rectangle

  

   Computes the size and location of the specified screen rectangle in client coordinates.

  

   r: The screen coordinate System.Drawing.Rectangle to convert.

   Returns: A System.Drawing.Rectangle that represents the converted System.Drawing.Rectangle,r,in client 

    coordinates.
  """
  pass
 def RectangleToScreen(self,r):
  """
  RectangleToScreen(self: Control,r: Rectangle) -> Rectangle

  

   Computes the size and location of the specified client rectangle in screen coordinates.

  

   r: The client coordinate System.Drawing.Rectangle to convert.

   Returns: A System.Drawing.Rectangle that represents the converted System.Drawing.Rectangle,p,in screen 

    coordinates.
  """
  pass
 def ReflectMessage(self,*args):
  """
  ReflectMessage(hWnd: IntPtr,m: Message) -> (bool,Message)

  

   Reflects the specified message to the control that is bound to the specified handle.

  

   hWnd: An System.IntPtr representing the handle of the control to reflect the message to.

   m: A System.Windows.Forms.Message representing the Windows message to reflect.

   Returns: true if the message was reflected; otherwise,false.
  """
  pass
 def Refresh(self):
  """
  Refresh(self: Control)

   Forces the control to invalidate its client area and immediately redraw itself and any child 

    controls.
  """
  pass
 def RescaleConstantsForDpi(self,*args):
  """ RescaleConstantsForDpi(self: Control,deviceDpiOld: int,deviceDpiNew: int) """
  pass
 def ResetBackColor(self):
  """
  ResetBackColor(self: Control)

   Resets the System.Windows.Forms.Control.BackColor property to its default value.
  """
  pass
 def ResetBindings(self):
  """
  ResetBindings(self: Control)

   Causes a control bound to the System.Windows.Forms.BindingSource to reread all the items in the 

    list and refresh their displayed values.
  """
  pass
 def ResetCursor(self):
  """
  ResetCursor(self: Control)

   Resets the System.Windows.Forms.Control.Cursor property to its default value.
  """
  pass
 def ResetFont(self):
  """
  ResetFont(self: Control)

   Resets the System.Windows.Forms.Control.Font property to its default value.
  """
  pass
 def ResetForeColor(self):
  """
  ResetForeColor(self: Control)

   Resets the System.Windows.Forms.Control.ForeColor property to its default value.
  """
  pass
 def ResetImeMode(self):
  """
  ResetImeMode(self: Control)

   Resets the System.Windows.Forms.Control.ImeMode property to its default value.
  """
  pass
 def ResetMouseEventArgs(self,*args):
  """
  ResetMouseEventArgs(self: Control)

   Resets the control to handle the System.Windows.Forms.Control.MouseLeave event.
  """
  pass
 def ResetRightToLeft(self):
  """
  ResetRightToLeft(self: Control)

   Resets the System.Windows.Forms.Control.RightToLeft property to its default value.
  """
  pass
 def ResetText(self):
  """
  ResetText(self: Control)

   Resets the System.Windows.Forms.Control.Text property to its default value.
  """
  pass
 def ResumeLayout(self,performLayout=None):
  """
  ResumeLayout(self: Control,performLayout: bool)

   Resumes usual layout logic,optionally forcing an immediate layout of pending layout requests.

  

   performLayout: true to execute pending layout requests; otherwise,false.

  ResumeLayout(self: Control)

   Resumes usual layout logic.
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
 def Scale(self,*__args):
  """
  Scale(self: Control,factor: SizeF)

   Scales the control and all child controls by the specified scaling factor.

  

   factor: A System.Drawing.SizeF containing the horizontal and vertical scaling factors.

  Scale(self: Control,dx: Single,dy: Single)

   Scales the entire control and any child controls.

  

   dx: The horizontal scaling factor.

   dy: The vertical scaling factor.

  Scale(self: Control,ratio: Single)

   Scales the control and any child controls.

  

   ratio: The ratio to use for scaling.
  """
  pass
 def ScaleBitmapLogicalToDevice(self,logicalBitmap):
  """ ScaleBitmapLogicalToDevice(self: Control,logicalBitmap: Bitmap) -> Bitmap """
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
  Select(self: Control)

   Activates the control.
  """
  pass
 def SelectNextControl(self,ctl,forward,tabStopOnly,nested,wrap):
  """
  SelectNextControl(self: Control,ctl: Control,forward: bool,tabStopOnly: bool,nested: bool,wrap: bool) -> bool

  

   Activates the next control.

  

   ctl: The System.Windows.Forms.Control at which to start the search.

   forward: true to move forward in the tab order; false to move backward in the tab order.

   tabStopOnly: true to ignore the controls with the System.Windows.Forms.Control.TabStop property set to false; 

    otherwise,false.

  

   nested: true to include nested (children of child controls) child controls; otherwise,false.

   wrap: true to continue searching from the first control in the tab order after the last control has 

    been reached; otherwise,false.

  

   Returns: true if a control was activated; otherwise,false.
  """
  pass
 def SendToBack(self):
  """
  SendToBack(self: Control)

   Sends the control to the back of the z-order.
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
 def SetBounds(self,x,y,width,height,specified=None):
  """
  SetBounds(self: Control,x: int,y: int,width: int,height: int,specified: BoundsSpecified)

   Sets the specified bounds of the control to the specified location and size.

  

   x: The new System.Windows.Forms.Control.Left property value of the control.

   y: The new System.Windows.Forms.Control.Top property value of the control.

   width: The new System.Windows.Forms.Control.Width property value of the control.

   height: The new System.Windows.Forms.Control.Height property value of the control.

   specified: A bitwise combination of the System.Windows.Forms.BoundsSpecified values. For any parameter not 

    specified,the current value will be used.

  

  SetBounds(self: Control,x: int,y: int,width: int,height: int)

   Sets the bounds of the control to the specified location and size.

  

   x: The new System.Windows.Forms.Control.Left property value of the control.

   y: The new System.Windows.Forms.Control.Top property value of the control.

   width: The new System.Windows.Forms.Control.Width property value of the control.

   height: The new System.Windows.Forms.Control.Height property value of the control.
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
 def Show(self):
  """
  Show(self: Control)

   Displays the control to the user.
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
 def SuspendLayout(self):
  """
  SuspendLayout(self: Control)

   Temporarily suspends the layout logic for the control.
  """
  pass
 def Update(self):
  """
  Update(self: Control)

   Causes the control to redraw the invalidated regions within its client area.
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
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,text: str)

  __new__(cls: type,text: str,left: int,top: int,width: int,height: int)

  __new__(cls: type,parent: Control,text: str)

  __new__(cls: type,parent: Control,text: str,left: int,top: int,width: int,height: int)
  """
  pass
 def __str__(self,*args):
  pass
 AccessibilityObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.AccessibleObject assigned to the control.



Get: AccessibilityObject(self: Control) -> AccessibleObject



"""

 AccessibleDefaultActionDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default action description of the control for use by accessibility client applications.



Get: AccessibleDefaultActionDescription(self: Control) -> str



Set: AccessibleDefaultActionDescription(self: Control)=value

"""

 AccessibleDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the description of the control used by accessibility client applications.



Get: AccessibleDescription(self: Control) -> str



Set: AccessibleDescription(self: Control)=value

"""

 AccessibleName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the control used by accessibility client applications.



Get: AccessibleName(self: Control) -> str



Set: AccessibleName(self: Control)=value

"""

 AccessibleRole=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the accessible role of the control



Get: AccessibleRole(self: Control) -> AccessibleRole



Set: AccessibleRole(self: Control)=value

"""

 AllowDrop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control can accept data that the user drags onto it.



Get: AllowDrop(self: Control) -> bool



Set: AllowDrop(self: Control)=value

"""

 Anchor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the edges of the container to which a control is bound and determines how a control is resized with its parent.



Get: Anchor(self: Control) -> AnchorStyles



Set: Anchor(self: Control)=value

"""

 AutoScrollOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets where this control is scrolled to in System.Windows.Forms.ScrollableControl.ScrollControlIntoView(System.Windows.Forms.Control).



Get: AutoScrollOffset(self: Control) -> Point



Set: AutoScrollOffset(self: Control)=value

"""

 AutoSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.



Get: AutoSize(self: Control) -> bool



Set: AutoSize(self: Control)=value

"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color for the control.



Get: BackColor(self: Control) -> Color



Set: BackColor(self: Control)=value

"""

 BackgroundImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background image displayed in the control.



Get: BackgroundImage(self: Control) -> Image



Set: BackgroundImage(self: Control)=value

"""

 BackgroundImageLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background image layout as defined in the System.Windows.Forms.ImageLayout enumeration.



Get: BackgroundImageLayout(self: Control) -> ImageLayout



Set: BackgroundImageLayout(self: Control)=value

"""

 BindingContext=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Forms.BindingContext for the control.



Get: BindingContext(self: Control) -> BindingContext



Set: BindingContext(self: Control)=value

"""

 Bottom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the distance,in pixels,between the bottom edge of the control and the top edge of its container's client area.



Get: Bottom(self: Control) -> int



"""

 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size and location of the control including its nonclient elements,in pixels,relative to the parent control.



Get: Bounds(self: Control) -> Rectangle



Set: Bounds(self: Control)=value

"""

 CanEnableIme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value,to enable IME support.



"""

 CanFocus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control can receive focus.



Get: CanFocus(self: Control) -> bool



"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if events can be raised on the control.



"""

 CanSelect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control can be selected.



Get: CanSelect(self: Control) -> bool



"""

 Capture=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control has captured the mouse.



Get: Capture(self: Control) -> bool



Set: Capture(self: Control)=value

"""

 CausesValidation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control causes validation to be performed on any controls that require validation when it receives focus.



Get: CausesValidation(self: Control) -> bool



Set: CausesValidation(self: Control)=value

"""

 ClientRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rectangle that represents the client area of the control.



Get: ClientRectangle(self: Control) -> Rectangle



"""

 ClientSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height and width of the client area of the control.



Get: ClientSize(self: Control) -> Size



Set: ClientSize(self: Control)=value

"""

 CompanyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the company or creator of the application containing the control.



Get: CompanyName(self: Control) -> str



"""

 ContainsFocus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control,or one of its child controls,currently has the input focus.



Get: ContainsFocus(self: Control) -> bool



"""

 ContextMenu=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the shortcut menu associated with the control.



Get: ContextMenu(self: Control) -> ContextMenu



Set: ContextMenu(self: Control)=value

"""

 ContextMenuStrip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Forms.ContextMenuStrip associated with this control.



Get: ContextMenuStrip(self: Control) -> ContextMenuStrip



Set: ContextMenuStrip(self: Control)=value

"""

 Controls=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of controls contained within the control.



Get: Controls(self: Control) -> ControlCollection



"""

 Created=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control has been created.



Get: Created(self: Control) -> bool



"""

 CreateParams=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the required creation parameters when the control handle is created.



"""

 Cursor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the cursor that is displayed when the mouse pointer is over the control.



Get: Cursor(self: Control) -> Cursor



Set: Cursor(self: Control)=value

"""

 DataBindings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the data bindings for the control.



Get: DataBindings(self: Control) -> ControlBindingsCollection



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

 DeviceDpi=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DeviceDpi(self: Control) -> int



"""

 DisplayRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rectangle that represents the display area of the control.



Get: DisplayRectangle(self: Control) -> Rectangle



"""

 Disposing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the base System.Windows.Forms.Control class is in the process of disposing.



Get: Disposing(self: Control) -> bool



"""

 Dock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets which control borders are docked to its parent control and determines how a control is resized with its parent.



Get: Dock(self: Control) -> DockStyle



Set: Dock(self: Control)=value

"""

 DoubleBuffered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this control should redraw its surface using a secondary buffer to reduce or prevent flicker.



"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control can respond to user interaction.



Get: Enabled(self: Control) -> bool



Set: Enabled(self: Control)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Focused=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control has input focus.



Get: Focused(self: Control) -> bool



"""

 Font=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the font of the text displayed by the control.



Get: Font(self: Control) -> Font



Set: Font(self: Control)=value

"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the font of the control.



"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of the control.



Get: ForeColor(self: Control) -> Color



Set: ForeColor(self: Control)=value

"""

 Handle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the window handle that the control is bound to.



Get: Handle(self: Control) -> IntPtr



"""

 HasChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control contains one or more child controls.



Get: HasChildren(self: Control) -> bool



"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the control.



Get: Height(self: Control) -> int



Set: Height(self: Control)=value

"""

 ImeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Input Method Editor (IME) mode of the control.



Get: ImeMode(self: Control) -> ImeMode



Set: ImeMode(self: Control)=value

"""

 ImeModeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the IME mode of a control.



"""

 InvokeRequired=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the caller must call an invoke method when making method calls to the control because the caller is on a different thread than the one the control was created on.



Get: InvokeRequired(self: Control) -> bool



"""

 IsAccessible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control is visible to accessibility applications.



Get: IsAccessible(self: Control) -> bool



Set: IsAccessible(self: Control)=value

"""

 IsDisposed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control has been disposed of.



Get: IsDisposed(self: Control) -> bool



"""

 IsHandleCreated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control has a handle associated with it.



Get: IsHandleCreated(self: Control) -> bool



"""

 IsMirrored=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control is mirrored.



Get: IsMirrored(self: Control) -> bool



"""

 LayoutEngine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a cached instance of the control's layout engine.



Get: LayoutEngine(self: Control) -> LayoutEngine



"""

 Left=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the distance,in pixels,between the left edge of the control and the left edge of its container's client area.



Get: Left(self: Control) -> int



Set: Left(self: Control)=value

"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the coordinates of the upper-left corner of the control relative to the upper-left corner of its container.



Get: Location(self: Control) -> Point



Set: Location(self: Control)=value

"""

 Margin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the space between controls.



Get: Margin(self: Control) -> Padding



Set: Margin(self: Control)=value

"""

 MaximumSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size that is the upper limit that System.Windows.Forms.Control.GetPreferredSize(System.Drawing.Size) can specify.



Get: MaximumSize(self: Control) -> Size



Set: MaximumSize(self: Control)=value

"""

 MinimumSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size that is the lower limit that System.Windows.Forms.Control.GetPreferredSize(System.Drawing.Size) can specify.



Get: MinimumSize(self: Control) -> Size



Set: MinimumSize(self: Control)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the control.



Get: Name(self: Control) -> str



Set: Name(self: Control)=value

"""

 Padding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets padding within the control.



Get: Padding(self: Control) -> Padding



Set: Padding(self: Control)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the parent container of the control.



Get: Parent(self: Control) -> Control



Set: Parent(self: Control)=value

"""

 PreferredSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size of a rectangular area into which the control can fit.



Get: PreferredSize(self: Control) -> Size



"""

 ProductName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the product name of the assembly containing the control.



Get: ProductName(self: Control) -> str



"""

 ProductVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the version of the assembly containing the control.



Get: ProductVersion(self: Control) -> str



"""

 PropagatingImeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object that represents a propagating IME mode.



"""

 RecreatingHandle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control is currently re-creating its handle.



Get: RecreatingHandle(self: Control) -> bool



"""

 Region=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the window region associated with the control.



Get: Region(self: Control) -> Region



Set: Region(self: Control)=value

"""

 RenderRightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is now obsolete.



"""

 ResizeRedraw=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control redraws itself when resized.



"""

 Right=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the distance,in pixels,between the right edge of the control and the left edge of its container's client area.



Get: Right(self: Control) -> int



"""

 RightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether control's elements are aligned to support locales using right-to-left fonts.



Get: RightToLeft(self: Control) -> RightToLeft



Set: RightToLeft(self: Control)=value

"""

 ScaleChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines the scaling of child controls.



"""

 ShowFocusCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control should display focus rectangles.



"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user interface is in the appropriate state to show or hide keyboard accelerators.



"""

 Site=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the site of the control.



Get: Site(self: Control) -> ISite



Set: Site(self: Control)=value

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height and width of the control.



Get: Size(self: Control) -> Size



Set: Size(self: Control)=value

"""

 TabIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the tab order of the control within its container.



Get: TabIndex(self: Control) -> int



Set: TabIndex(self: Control)=value

"""

 TabStop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the user can give the focus to this control using the TAB key.



Get: TabStop(self: Control) -> bool



Set: TabStop(self: Control)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object that contains data about the control.



Get: Tag(self: Control) -> object



Set: Tag(self: Control)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text associated with this control.



Get: Text(self: Control) -> str



Set: Text(self: Control)=value

"""

 Top=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the distance,in pixels,between the top edge of the control and the top edge of its container's client area.



Get: Top(self: Control) -> int



Set: Top(self: Control)=value

"""

 TopLevelControl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent control that is not parented by another Windows Forms control. Typically,this is the outermost System.Windows.Forms.Form that the control is contained in.



Get: TopLevelControl(self: Control) -> Control



"""

 UseWaitCursor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to use the wait cursor for the current control and all child controls.



Get: UseWaitCursor(self: Control) -> bool



Set: UseWaitCursor(self: Control)=value

"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control and all its child controls are displayed.



Get: Visible(self: Control) -> bool



Set: Visible(self: Control)=value

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of the control.



Get: Width(self: Control) -> int



Set: Width(self: Control)=value

"""

 WindowTarget=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.



Get: WindowTarget(self: Control) -> IWindowTarget



Set: WindowTarget(self: Control)=value

"""


 AutoSizeChanged=None
 BackColorChanged=None
 BackgroundImageChanged=None
 BackgroundImageLayoutChanged=None
 BindingContextChanged=None
 CausesValidationChanged=None
 ChangeUICues=None
 CheckForIllegalCrossThreadCalls=False
 Click=None
 ClientSizeChanged=None
 ContextMenuChanged=None
 ContextMenuStripChanged=None
 ControlAccessibleObject=None
 ControlAdded=None
 ControlCollection=None
 ControlRemoved=None
 CursorChanged=None
 DefaultBackColor=None
 DefaultFont=None
 DefaultForeColor=None
 DockChanged=None
 DoubleClick=None
 DpiChangedAfterParent=None
 DpiChangedBeforeParent=None
 DragDrop=None
 DragEnter=None
 DragLeave=None
 DragOver=None
 EnabledChanged=None
 Enter=None
 FontChanged=None
 ForeColorChanged=None
 GiveFeedback=None
 GotFocus=None
 HandleCreated=None
 HandleDestroyed=None
 HelpRequested=None
 ImeModeChanged=None
 Invalidated=None
 KeyDown=None
 KeyPress=None
 KeyUp=None
 Layout=None
 Leave=None
 LocationChanged=None
 LostFocus=None
 MarginChanged=None
 ModifierKeys=None
 MouseButtons=None
 MouseCaptureChanged=None
 MouseClick=None
 MouseDoubleClick=None
 MouseDown=None
 MouseEnter=None
 MouseHover=None
 MouseLeave=None
 MouseMove=None
 MousePosition=None
 MouseUp=None
 MouseWheel=None
 Move=None
 PaddingChanged=None
 Paint=None
 ParentChanged=None
 PreviewKeyDown=None
 QueryAccessibilityHelp=None
 QueryContinueDrag=None
 RegionChanged=None
 Resize=None
 RightToLeftChanged=None
 SizeChanged=None
 StyleChanged=None
 SystemColorsChanged=None
 TabIndexChanged=None
 TabStopChanged=None
 TextChanged=None
 Validated=None
 Validating=None
 VisibleChanged=None

