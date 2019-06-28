class AxHost:
 """ Wraps ActiveX controls and exposes them as fully featured Windows Forms controls. """
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
 def AttachInterfaces(self,*args):
  """
  AttachInterfaces(self: AxHost)
   When overridden in a derived class,attaches interfaces to the underlying ActiveX control.
  """
  pass
 def BeginInit(self):
  """
  BeginInit(self: AxHost)
   Begins the initialization of the ActiveX control.
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
  """ CreateHandle(self: AxHost) """
  pass
 def CreateInstanceCore(self,*args):
  """
  CreateInstanceCore(self: AxHost,clsid: Guid) -> object
  
   Called by the system to create the ActiveX control.
  
   clsid: The CLSID of the ActiveX control.
   Returns: An System.Object representing the ActiveX control.
  """
  pass
 def CreateSink(self,*args):
  """
  CreateSink(self: AxHost)
   Called by the control to prepare it for listening to events.
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
  """ DestroyHandle(self: AxHost) """
  pass
 def DetachSink(self,*args):
  """
  DetachSink(self: AxHost)
   Called by the control when it stops listening to events.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: AxHost,disposing: bool)
   disposing: true to release both managed and unmanaged resources; false to release only unmanaged 
    resources.
  """
  pass
 def DoVerb(self,verb):
  """
  DoVerb(self: AxHost,verb: int)
   Requests that an object perform an action in response to an end-user's action.
  
   verb: One of the actions enumerated for the object in IOleObject::EnumVerbs.
  """
  pass
 def DrawToBitmap(self,bitmap,targetBounds):
  """
  DrawToBitmap(self: AxHost,bitmap: Bitmap,targetBounds: Rectangle)
   This method is not supported by this control.
  
   bitmap: A System.Drawing.Bitmap.
   targetBounds: A System.Drawing.Rectangle.
  """
  pass
 def EndInit(self):
  """
  EndInit(self: AxHost)
   Ends the initialization of an ActiveX control.
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
 def GetColorFromOleColor(self,*args):
  """
  GetColorFromOleColor(color: UInt32) -> Color
  
   Returns a System.Drawing.Color structure that corresponds to the specified OLE color 
    value.
  
  
   color: The OLE color value to translate.
   Returns: The System.Drawing.Color structure that represents the translated OLE color value.
  """
  pass
 def GetFontFromIFont(self,*args):
  """
  GetFontFromIFont(font: object) -> Font
  
   Returns a System.Drawing.Font created from the specified OLE IFont object.
  
   font: The IFont to create a System.Drawing.Font from.
   Returns: The System.Drawing.Font created from the specified IFont,
    System.Windows.Forms.Control.DefaultFont if the font could not be created,or null if 
    font is null.
  """
  pass
 def GetFontFromIFontDisp(self,*args):
  """
  GetFontFromIFontDisp(font: object) -> Font
  
   Returns a System.Drawing.Font created from the specified OLE IFontDisp object.
  
   font: The IFontDisp to create a System.Drawing.Font from.
   Returns: The System.Drawing.Font created from the specified IFontDisp,
    System.Windows.Forms.Control.DefaultFont if the font could not be created,or null if 
    font is null.
  """
  pass
 def GetIFontDispFromFont(self,*args):
  """
  GetIFontDispFromFont(font: Font) -> object
  
   Returns an OLE IFontDisp object created from the specified System.Drawing.Font object.
  
   font: The font to create an IFontDisp object from.
   Returns: The IFontDisp object created from the specified font or null if font is null.
  """
  pass
 def GetIFontFromFont(self,*args):
  """
  GetIFontFromFont(font: Font) -> object
  
   Returns an OLE IFont object created from the specified System.Drawing.Font object.
  
   font: The font to create an IFont object from.
   Returns: The IFont object created from the specified font,or null if font is null or the IFont 
    could not be created.
  """
  pass
 def GetIPictureDispFromPicture(self,*args):
  """
  GetIPictureDispFromPicture(image: Image) -> object
  
   Returns an OLE IPictureDisp object corresponding to the specified System.Drawing.Image.
  
   image: The System.Drawing.Image to convert.
   Returns: An System.Object representing the OLE IPictureDisp object.
  """
  pass
 def GetIPictureFromCursor(self,*args):
  """
  GetIPictureFromCursor(cursor: Cursor) -> object
  
   Returns an OLE IPicture object corresponding to the specified System.Windows.Forms.Cursor.
  
   cursor: System.Windows.Forms.Cursor
   Returns: An System.Object representing the OLE IPicture object.
  """
  pass
 def GetIPictureFromPicture(self,*args):
  """
  GetIPictureFromPicture(image: Image) -> object
  
   Returns an OLE IPicture object corresponding to the specified System.Drawing.Image.
  
   image: The System.Drawing.Image to convert.
   Returns: An System.Object representing the OLE IPicture object.
  """
  pass
 def GetOADateFromTime(self,*args):
  """
  GetOADateFromTime(time: DateTime) -> float
  
   Returns an OLE Automation date that corresponds to the specified System.DateTime 
    structure.
  
  
   time: The System.DateTime structure to translate.
   Returns: A double-precision floating-point number that contains an OLE Automation date equivalent 
    to specified time value.
  """
  pass
 def GetOcx(self):
  """
  GetOcx(self: AxHost) -> object
  
   Retrieves a reference to the underlying ActiveX control.
   Returns: An object that represents the ActiveX control.
  """
  pass
 def GetOleColorFromColor(self,*args):
  """
  GetOleColorFromColor(color: Color) -> UInt32
  
   Returns an OLE color value that corresponds to the specified System.Drawing.Color 
    structure.
  
  
   color: The System.Drawing.Color structure to translate.
   Returns: The OLE color value that represents the translated System.Drawing.Color structure.
  """
  pass
 def GetPictureFromIPicture(self,*args):
  """
  GetPictureFromIPicture(picture: object) -> Image
  
   Returns an System.Drawing.Image corresponding to the specified OLE IPicture object.
  
   picture: The IPicture to convert.
   Returns: An System.Drawing.Image representing the IPicture.
  """
  pass
 def GetPictureFromIPictureDisp(self,*args):
  """
  GetPictureFromIPictureDisp(picture: object) -> Image
  
   Returns an System.Drawing.Image corresponding to the specified OLE IPictureDisp object.
  
   picture: The IPictureDisp to convert.
   Returns: An System.Drawing.Image representing the IPictureDisp.
  """
  pass
 def GetScaledBounds(self,*args):
  """
  GetScaledBounds(self: AxHost,bounds: Rectangle,factor: SizeF,specified: BoundsSpecified) -> Rectangle
  
   Called by the system to retrieve the current bounds of the ActiveX control.
  
   bounds: The original bounds of the ActiveX control.
   factor: A scaling factor.
   specified: A System.Windows.Forms.BoundsSpecified value.
   Returns: The unmodified bounds value.
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
 def GetTimeFromOADate(self,*args):
  """
  GetTimeFromOADate(date: float) -> DateTime
  
   Returns a System.DateTime structure that corresponds to the specified OLE Automation date.
  
   date: The OLE Automate date to translate.
   Returns: A System.DateTime that represents the same date and time as date.
  """
  pass
 def GetTopLevel(self,*args):
  """
  GetTopLevel(self: Control) -> bool
  
   Determines if the control is a top-level control.
   Returns: true if the control is a top-level control; otherwise,false.
  """
  pass
 def HasPropertyPages(self):
  """
  HasPropertyPages(self: AxHost) -> bool
  
   Determines if the ActiveX control has a property page.
   Returns: true if the ActiveX control has a property page; otherwise,false.
  """
  pass
 def InitLayout(self,*args):
  """
  InitLayout(self: Control)
   Called after the control has been added to another container.
  """
  pass
 def InvokeEditMode(self):
  """
  InvokeEditMode(self: AxHost)
   Attempts to activate the editing mode of the hosted control.
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
  IsInputChar(self: AxHost,charCode: Char) -> bool
  
   Determines if a character is an input character that the ActiveX control recognizes.
  
   charCode: The character to test.
   Returns: true if the character should be sent directly to the ActiveX control and not 
    preprocessed; otherwise,false.
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
 def MakeDirty(self):
  """
  MakeDirty(self: AxHost)
   Announces to the component change service that the System.Windows.Forms.AxHost has 
    changed.
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
  OnBackColorChanged(self: AxHost,e: EventArgs)
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
  OnFontChanged(self: AxHost,e: EventArgs)
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnForeColorChanged(self,*args):
  """
  OnForeColorChanged(self: AxHost,e: EventArgs)
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
  OnHandleCreated(self: AxHost,e: EventArgs)
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
 def OnInPlaceActive(self,*args):
  """
  OnInPlaceActive(self: AxHost)
   Called when the control transitions to the in-place active state.
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
  OnLostFocus(self: AxHost,e: EventArgs)
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
  
   pevent: A System.Windows.Forms.PaintEventArgs that contains information about the control to 
    paint.
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
 def PreProcessMessage(self,msg):
  """
  PreProcessMessage(self: AxHost,msg: Message) -> (bool,Message)
  
   msg: A System.Windows.Forms.Message,passed by reference,that represents the message to 
    process. The possible values are WM_KEYDOWN,WM_SYSKEYDOWN,WM_CHAR,and WM_SYSCHAR.
  
   Returns: true if the message was processed by the control; otherwise,false.
  """
  pass
 def ProcessCmdKey(self,*args):
  """
  ProcessCmdKey(self: Control,msg: Message,keyData: Keys) -> (bool,Message)
  
   Processes a command key.
  
   msg: A System.Windows.Forms.Message,passed by reference,that represents the window message 
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
  ProcessDialogKey(self: AxHost,keyData: Keys) -> bool
  
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
  ProcessMnemonic(self: AxHost,charCode: Char) -> bool
  
   charCode: The character to process.
   Returns: true if the character was processed as a mnemonic by the control; otherwise,false.
  """
  pass
 def PropsValid(self,*args):
  """
  PropsValid(self: AxHost) -> bool
  
   Returns a value that indicates whether the hosted control is in a state in which its 
    properties can be accessed.
  
   Returns: true if the properties of the hosted control can be accessed; otherwise,false.
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
 def RaiseOnMouseDown(self,*args):
  """
  RaiseOnMouseDown(self: AxHost,o1: object,o2: object,o3: object,o4: object)
   Raises the System.Windows.Forms.AxHost.MouseDown event using the specified objects.
  
   o1: One of the System.Windows.Forms.MouseButtons values that indicate which mouse button was 
    pressed.
  
   o2: Not used.
   o3: The x-coordinate of a mouse click,in pixels.
   o4: The y-coordinate of a mouse click,in pixels.
  RaiseOnMouseDown(self: AxHost,button: Int16,shift: Int16,x: Single,y: Single)
   Raises the System.Windows.Forms.AxHost.MouseDown event using the specified 
    single-precision floating-point numbers.
  
  
   button: One of the System.Windows.Forms.MouseButtons values that indicate which mouse button was 
    pressed.
  
   shift: Not used.
   x: The x-coordinate of a mouse click,in pixels.
   y: The y-coordinate of a mouse click,in pixels.
  RaiseOnMouseDown(self: AxHost,button: Int16,shift: Int16,x: int,y: int)
   Raises the System.Windows.Forms.AxHost.MouseDown event using the specified 32-bit signed 
    integers.
  
  
   button: One of the System.Windows.Forms.MouseButtons values that indicate which mouse button was 
    pressed.
  
   shift: Not used.
   x: The x-coordinate of a mouse click,in pixels.
   y: The y-coordinate of a mouse click,in pixels.
  """
  pass
 def RaiseOnMouseMove(self,*args):
  """
  RaiseOnMouseMove(self: AxHost,o1: object,o2: object,o3: object,o4: object)
   Raises the System.Windows.Forms.AxHost.MouseMove event using the specified objects.
  
   o1: One of the System.Windows.Forms.MouseButtons values that indicate which mouse button was 
    pressed.
  
   o2: Not used.
   o3: The x-coordinate of a mouse click,in pixels.
   o4: The y-coordinate of a mouse click,in pixels.
  RaiseOnMouseMove(self: AxHost,button: Int16,shift: Int16,x: Single,y: Single)
   Raises the System.Windows.Forms.AxHost.MouseMove event using the specified 
    single-precision floating-point numbers.
  
  
   button: One of the System.Windows.Forms.MouseButtons values that indicate which mouse button was 
    pressed.
  
   shift: Not used.
   x: The x-coordinate of a mouse click,in pixels.
   y: The y-coordinate of a mouse click,in pixels.
  RaiseOnMouseMove(self: AxHost,button: Int16,shift: Int16,x: int,y: int)
   Raises the System.Windows.Forms.AxHost.MouseMove event using the specified 32-bit signed 
    integers.
  
  
   button: One of the System.Windows.Forms.MouseButtons values that indicate which mouse button was 
    pressed.
  
   shift: Not used.
   x: The x-coordinate of a mouse click,in pixels.
   y: The y-coordinate of a mouse click,in pixels.
  """
  pass
 def RaiseOnMouseUp(self,*args):
  """
  RaiseOnMouseUp(self: AxHost,o1: object,o2: object,o3: object,o4: object)
   Raises the System.Windows.Forms.AxHost.MouseUp event using the specified objects.
  
   o1: One of the System.Windows.Forms.MouseButtons values that indicate which mouse button was 
    pressed.
  
   o2: Not used.
   o3: The x-coordinate of a mouse click,in pixels.
   o4: The y-coordinate of a mouse click,in pixels.
  RaiseOnMouseUp(self: AxHost,button: Int16,shift: Int16,x: Single,y: Single)
   Raises the System.Windows.Forms.AxHost.MouseUp event using the specified single-precision 
    floating-point numbers.
  
  
   button: One of the System.Windows.Forms.MouseButtons values that indicate which mouse button was 
    pressed.
  
   shift: Not used.
   x: The x-coordinate of a mouse click,in pixels.
   y: The y-coordinate of a mouse click,in pixels.
  RaiseOnMouseUp(self: AxHost,button: Int16,shift: Int16,x: int,y: int)
   Raises the System.Windows.Forms.AxHost.MouseUp event using the specified 32-bit signed 
    integers.
  
  
   button: One of the System.Windows.Forms.MouseButtons values that indicate which mouse button was 
    pressed.
  
   shift: Not used.
   x: The x-coordinate of a mouse click,in pixels.
   y: The y-coordinate of a mouse click,in pixels.
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
 def ResetMouseEventArgs(self,*args):
  """
  ResetMouseEventArgs(self: Control)
   Resets the control to handle the System.Windows.Forms.Control.MouseLeave event.
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
  ScaleControl(self: Control,factor: SizeF,specified: BoundsSpecified)
   Scales a control's location,size,padding and margin.
  
   factor: The factor by which the height and width of the control will be scaled.
   specified: A System.Windows.Forms.BoundsSpecified value that specifies the bounds of the control to 
    use when defining its size and position.
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
   Activates a child control. Optionally specifies the direction in the tab order to select 
    the control from.
  
  
   directed: true to specify the direction of the control to select; otherwise,false.
   forward: true to move forward in the tab order; false to move backward in the tab order.
  """
  pass
 def SetAboutBoxDelegate(self,*args):
  """ SetAboutBoxDelegate(self: AxHost,d: AboutBoxDelegate) """
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
  SetBoundsCore(self: AxHost,x: int,y: int,width: int,height: int,specified: BoundsSpecified)
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
  SetVisibleCore(self: AxHost,value: bool)
   value: true to make the control visible; otherwise,false.
  """
  pass
 def ShowAboutBox(self):
  """
  ShowAboutBox(self: AxHost)
   Displays the ActiveX control's About dialog box.
  """
  pass
 def ShowPropertyPages(self,control=None):
  """
  ShowPropertyPages(self: AxHost)
   Displays the property pages associated with the ActiveX control.
  ShowPropertyPages(self: AxHost,control: Control)
   Displays the property pages associated with the ActiveX control assigned to the specified 
    parent control.
  
  
   control: The parent System.Windows.Forms.Control of the ActiveX control.
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
  WndProc(self: AxHost,m: Message) -> Message
  
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
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type,clsid: str)
  __new__(cls: type,clsid: str,flags: int)
  """
  pass
 def __str__(self,*args):
  pass
 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This member is not meaningful for this control.

Get: BackColor(self: AxHost) -> Color

Set: BackColor(self: AxHost)=value
"""

 BackgroundImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: BackgroundImage(self: AxHost) -> Image

Set: BackgroundImage(self: AxHost)=value
"""

 BackgroundImageLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: BackgroundImageLayout(self: AxHost) -> ImageLayout

Set: BackgroundImageLayout(self: AxHost)=value
"""

 CanEnableIme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value,to enable IME support.

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if events can be raised on the control.

"""

 ContainingControl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the control containing the ActiveX control.

Get: ContainingControl(self: AxHost) -> ContainerControl

Set: ContainingControl(self: AxHost)=value
"""

 ContextMenu=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: ContextMenu(self: AxHost) -> ContextMenu

Set: ContextMenu(self: AxHost)=value
"""

 CreateParams=property(lambda self: object(),lambda self,v: None,lambda self: None)

 Cursor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: Cursor(self: AxHost) -> Cursor

Set: Cursor(self: AxHost)=value
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

 EditMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns a value that indicates whether the hosted control is in edit mode.

Get: EditMode(self: AxHost) -> bool

"""

 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: Enabled(self: AxHost) -> bool

Set: Enabled(self: AxHost)=value
"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

 Font=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: Font(self: AxHost) -> Font

Set: Font(self: AxHost)=value
"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the font of the control.

"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: ForeColor(self: AxHost) -> Color

Set: ForeColor(self: AxHost)=value
"""

 HasAboutBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the ActiveX control has an About dialog box.

Get: HasAboutBox(self: AxHost) -> bool

"""

 ImeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: ImeMode(self: AxHost) -> ImeMode

Set: ImeMode(self: AxHost)=value
"""

 ImeModeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the IME mode of a control.

"""

 OcxState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the persisted state of the ActiveX control.

Get: OcxState(self: AxHost) -> State

Set: OcxState(self: AxHost)=value
"""

 RenderRightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is now obsolete.

"""

 ResizeRedraw=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control redraws itself when resized.

"""

 RightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: RightToLeft(self: AxHost) -> bool

Set: RightToLeft(self: AxHost)=value
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
 """Set: Site(self: AxHost)=value
"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not relevant for this class.

Get: Text(self: AxHost) -> str

Set: Text(self: AxHost)=value
"""


 AboutBoxDelegate=None
 ActiveXInvokeKind=None
 AxComponentEditor=None
 BackColorChanged=None
 BackgroundImageChanged=None
 BackgroundImageLayoutChanged=None
 BindingContextChanged=None
 ChangeUICues=None
 Click=None
 ClsidAttribute=None
 ConnectionPointCookie=None
 ContextMenuChanged=None
 CursorChanged=None
 DoubleClick=None
 DragDrop=None
 DragEnter=None
 DragLeave=None
 DragOver=None
 EnabledChanged=None
 FontChanged=None
 ForeColorChanged=None
 GiveFeedback=None
 HelpRequested=None
 ImeModeChanged=None
 InvalidActiveXStateException=None
 KeyDown=None
 KeyPress=None
 KeyUp=None
 Layout=None
 MouseClick=None
 MouseDoubleClick=None
 MouseDown=None
 MouseEnter=None
 MouseHover=None
 MouseLeave=None
 MouseMove=None
 MouseUp=None
 MouseWheel=None
 Paint=None
 QueryAccessibilityHelp=None
 QueryContinueDrag=None
 RightToLeftChanged=None
 State=None
 StateConverter=None
 StyleChanged=None
 TextChanged=None
 TypeLibraryTimeStampAttribute=None

