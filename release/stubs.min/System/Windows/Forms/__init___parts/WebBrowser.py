class WebBrowser(WebBrowserBase,IComponent,IDisposable,IOleControl,IOleObject,IOleInPlaceObject,IOleInPlaceActiveObject,IOleWindow,IViewObject,IViewObject2,IPersist,IPersistStreamInit,IPersistPropertyBag,IPersistStorage,IQuickActivate,ISupportOleDropSource,IDropTarget,ISynchronizeInvoke,IWin32Window,IArrangedElement,IBindableComponent):
 """
 Enables the user to navigate Web pages inside your form.
 
 WebBrowser()
 """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return WebBrowser()

 def AccessibilityNotifyClients(self,*args):
  """
  AccessibilityNotifyClients(self: Control,accEvent: AccessibleEvents,childID: int)
   Notifies the accessibility client applications of the specified System.Windows.Forms.AccessibleEvents for the specified child control.
  
   accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications of.
   childID: The child System.Windows.Forms.Control to notify of the accessible event.
  AccessibilityNotifyClients(self: Control,accEvent: AccessibleEvents,objectID: int,childID: int)
   Notifies the accessibility client applications of the specified System.Windows.Forms.AccessibleEvents for the specified child control .
  
   accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications of.
   objectID: The identifier of the System.Windows.Forms.AccessibleObject.
   childID: The child System.Windows.Forms.Control to notify of the accessible event.
  """
  pass
 def AttachInterfaces(self,*args):
  """
  AttachInterfaces(self: WebBrowser,nativeActiveXObject: object)
   Called by the control when the underlying ActiveX control is created.
  
   nativeActiveXObject: An object that represents the underlying ActiveX control.
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
 def CreateSink(self,*args):
  """
  CreateSink(self: WebBrowser)
   Associates the underlying ActiveX control with a client that can handle control events.
  """
  pass
 def CreateWebBrowserSiteBase(self,*args):
  """
  CreateWebBrowserSiteBase(self: WebBrowser) -> WebBrowserSiteBase
  
   Returns a reference to the unmanaged WebBrowser ActiveX control site,which you can extend to customize the managed System.Windows.Forms.WebBrowser control.
   Returns: A System.Windows.Forms.WebBrowser.WebBrowserSite that represents the WebBrowser ActiveX control site.
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
 def DetachInterfaces(self,*args):
  """
  DetachInterfaces(self: WebBrowser)
   Called by the control when the underlying ActiveX control is discarded.
  """
  pass
 def DetachSink(self,*args):
  """
  DetachSink(self: WebBrowser)
   Releases the event-handling client attached in the System.Windows.Forms.WebBrowser.CreateSink method from the underlying ActiveX control.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: WebBrowser,disposing: bool)
   Releases the unmanaged resources used by the System.Windows.Forms.WebBrowser and optionally releases the managed resources.
  
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
 def GetAutoSizeMode(self,*args):
  """
  GetAutoSizeMode(self: Control) -> AutoSizeMode
  
   Retrieves a value indicating how a control will behave when its System.Windows.Forms.Control.AutoSize property is enabled.
   Returns: One of the System.Windows.Forms.AutoSizeMode values.
  """
  pass
 def GetScaledBounds(self,*args):
  """
  GetScaledBounds(self: Control,bounds: Rectangle,factor: SizeF,specified: BoundsSpecified) -> Rectangle
  
   Retrieves the bounds within which the control is scaled.
  
   bounds: A System.Drawing.Rectangle that specifies the area for which to retrieve the display bounds.
   factor: The height and width of the control's bounds.
   specified: One of the values of System.Windows.Forms.BoundsSpecified that specifies the bounds of the control to use when defining its size and position.
   Returns: A System.Drawing.Rectangle representing the bounds within which the control is scaled.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Component,service: Type) -> object
  
   Returns an object that represents a service provided by the System.ComponentModel.Component or by its System.ComponentModel.Container.
  
   service: A service provided by the System.ComponentModel.Component.
   Returns: An System.Object that represents a service provided by the System.ComponentModel.Component,or null if the System.ComponentModel.Component does not provide the specified service.
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
 def GoBack(self):
  """
  GoBack(self: WebBrowser) -> bool
  
   Navigates the System.Windows.Forms.WebBrowser control to the previous page in the navigation history,if one is available.
   Returns: true if the navigation succeeds; false if a previous page in the navigation history is not available.
  """
  pass
 def GoForward(self):
  """
  GoForward(self: WebBrowser) -> bool
  
   Navigates the System.Windows.Forms.WebBrowser control to the next page in the navigation history,if one is available.
   Returns: true if the navigation succeeds; false if a subsequent page in the navigation history is not available.
  """
  pass
 def GoHome(self):
  """
  GoHome(self: WebBrowser)
   Navigates the System.Windows.Forms.WebBrowser control to the home page of the current user.
  """
  pass
 def GoSearch(self):
  """
  GoSearch(self: WebBrowser)
   Navigates the System.Windows.Forms.WebBrowser control to the default search page of the current user.
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
  IsInputChar(self: WebBrowserBase,charCode: Char) -> bool
  
   charCode: The character to test.
   Returns: true if the character should be sent directly to the control and not preprocessed; otherwise,false.
  """
  pass
 def IsInputKey(self,*args):
  """
  IsInputKey(self: Control,keyData: Keys) -> bool
  
   Determines whether the specified key is a regular input key or a special key that requires preprocessing.
  
   keyData: One of the System.Windows.Forms.Keys values.
   Returns: true if the specified key is a regular input key; otherwise,false.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject
  
   Creates a shallow copy of the current System.MarshalByRefObject object.
  
   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone,which will cause remoting client calls to be routed to the remote server object.
   Returns: A shallow copy of the current System.MarshalByRefObject object.
  MemberwiseClone(self: object) -> object
  
   Creates a shallow copy of the current System.Object.
   Returns: A shallow copy of the current System.Object.
  """
  pass
 def Navigate(self,*__args):
  """
  Navigate(self: WebBrowser,url: Uri)
   Loads the document at the location indicated by the specified System.Uri into the System.Windows.Forms.WebBrowser control,replacing the previous document.
  
   url: A System.Uri representing the URL of the document to load.
  Navigate(self: WebBrowser,urlString: str)
   Loads the document at the specified Uniform Resource Locator (URL) into the System.Windows.Forms.WebBrowser control,replacing the previous document.
  
   urlString: The URL of the document to load.
  Navigate(self: WebBrowser,url: Uri,targetFrameName: str)
   Loads the document at the location indicated by the specified System.Uri into the System.Windows.Forms.WebBrowser control,replacing the contents of the Web page frame with the specified name.
  
   url: A System.Uri representing the URL of the document to load.
   targetFrameName: The name of the frame in which to load the document.
  Navigate(self: WebBrowser,urlString: str,targetFrameName: str)
   Loads the document at the specified Uniform Resource Locator (URL) into the System.Windows.Forms.WebBrowser control,replacing the contents of the Web page frame with the specified name.
  
   urlString: The URL of the document to load.
   targetFrameName: The name of the frame in which to load the document.
  Navigate(self: WebBrowser,url: Uri,newWindow: bool)
   Loads the document at the location indicated by the specified System.Uri into a new browser window or into the System.Windows.Forms.WebBrowser control.
  
   url: A System.Uri representing the URL of the document to load.
   newWindow: true to load the document into a new browser window; false to load the document into the System.Windows.Forms.WebBrowser control.
  Navigate(self: WebBrowser,urlString: str,newWindow: bool)
   Loads the document at the specified Uniform Resource Locator (URL) into a new browser window or into the System.Windows.Forms.WebBrowser control.
  
   urlString: The URL of the document to load.
   newWindow: true to load the document into a new browser window; false to load the document into the System.Windows.Forms.WebBrowser control.
  Navigate(self: WebBrowser,url: Uri,targetFrameName: str,postData: Array[Byte],additionalHeaders: str)
   Loads the document at the location indicated by the specified System.Uri into the System.Windows.Forms.WebBrowser control,requesting it using the specified HTTP data and replacing the contents of the Web page frame with the specified name.
  
   url: A System.Uri representing the URL of the document to load.
   targetFrameName: The name of the frame in which to load the document.
   postData: HTTP POST data such as form data.
   additionalHeaders: HTTP headers to add to the default headers.
  Navigate(self: WebBrowser,urlString: str,targetFrameName: str,postData: Array[Byte],additionalHeaders: str)
   Loads the document at the specified Uniform Resource Locator (URL) into the System.Windows.Forms.WebBrowser control,requesting it using the specified HTTP data and replacing the contents of the Web page frame with the specified name.
  
   urlString: The URL of the document to load.
   targetFrameName: The name of the frame in which to load the document.
   postData: HTTP POST data such as form data.
   additionalHeaders: HTTP headers to add to the default headers.
  """
  pass
 def NotifyInvalidate(self,*args):
  """
  NotifyInvalidate(self: Control,invalidatedArea: Rectangle)
   Raises the System.Windows.Forms.Control.Invalidated event with a specified region of the control to invalidate.
  
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
  OnBackColorChanged(self: WebBrowserBase,e: EventArgs)
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
 def OnCanGoBackChanged(self,*args):
  """
  OnCanGoBackChanged(self: WebBrowser,e: EventArgs)
   Raises the System.Windows.Forms.WebBrowser.CanGoBackChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnCanGoForwardChanged(self,*args):
  """
  OnCanGoForwardChanged(self: WebBrowser,e: EventArgs)
   Raises the System.Windows.Forms.WebBrowser.CanGoForwardChanged event.
  
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
 def OnDocumentCompleted(self,*args):
  """
  OnDocumentCompleted(self: WebBrowser,e: WebBrowserDocumentCompletedEventArgs)
   Raises the System.Windows.Forms.WebBrowser.DocumentCompleted event.
  
   e: A System.Windows.Forms.WebBrowserDocumentCompletedEventArgs that contains the event data.
  """
  pass
 def OnDocumentTitleChanged(self,*args):
  """
  OnDocumentTitleChanged(self: WebBrowser,e: EventArgs)
   Raises the System.Windows.Forms.WebBrowser.DocumentTitleChanged event.
  
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
 def OnEncryptionLevelChanged(self,*args):
  """
  OnEncryptionLevelChanged(self: WebBrowser,e: EventArgs)
   Raises the System.Windows.Forms.WebBrowser.EncryptionLevelChanged event.
  
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
 def OnFileDownload(self,*args):
  """
  OnFileDownload(self: WebBrowser,e: EventArgs)
   Raises the System.Windows.Forms.WebBrowser.FileDownload event.
  
   e: A System.ComponentModel.CancelEventArgs that contains the event data.
  """
  pass
 def OnFontChanged(self,*args):
  """
  OnFontChanged(self: WebBrowserBase,e: EventArgs)
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnForeColorChanged(self,*args):
  """
  OnForeColorChanged(self: WebBrowserBase,e: EventArgs)
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
  OnGotFocus(self: WebBrowserBase,e: EventArgs)
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleCreated(self,*args):
  """
  OnHandleCreated(self: WebBrowserBase,e: EventArgs)
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
  OnLostFocus(self: WebBrowserBase,e: EventArgs)
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
 def OnNavigated(self,*args):
  """
  OnNavigated(self: WebBrowser,e: WebBrowserNavigatedEventArgs)
   Raises the System.Windows.Forms.WebBrowser.Navigated event.
  
   e: A System.Windows.Forms.WebBrowserNavigatedEventArgs that contains the event data.
  """
  pass
 def OnNavigating(self,*args):
  """
  OnNavigating(self: WebBrowser,e: WebBrowserNavigatingEventArgs)
   Raises the System.Windows.Forms.WebBrowser.Navigating event.
  
   e: A System.Windows.Forms.WebBrowserNavigatingEventArgs that contains the event data.
  """
  pass
 def OnNewWindow(self,*args):
  """
  OnNewWindow(self: WebBrowser,e: CancelEventArgs)
   Raises the System.Windows.Forms.WebBrowser.NewWindow event.
  
   e: A System.ComponentModel.CancelEventArgs that contains the event data.
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
   Raises the System.Windows.Forms.Control.BackColorChanged event when the System.Windows.Forms.Control.BackColor property value of the control's container changes.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentBackgroundImageChanged(self,*args):
  """
  OnParentBackgroundImageChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.BackgroundImageChanged event when the System.Windows.Forms.Control.BackgroundImage property value of the control's container changes.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentBindingContextChanged(self,*args):
  """
  OnParentBindingContextChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.BindingContextChanged event when the System.Windows.Forms.Control.BindingContext property value of the control's container changes.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentChanged(self,*args):
  """
  OnParentChanged(self: WebBrowserBase,e: EventArgs)
   This member overrides System.Windows.Forms.Control.OnParentChanged(System.EventArgs).
  
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
   Raises the System.Windows.Forms.Control.EnabledChanged event when the System.Windows.Forms.Control.Enabled property value of the control's container changes.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentFontChanged(self,*args):
  """
  OnParentFontChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.FontChanged event when the System.Windows.Forms.Control.Font property value of the control's container changes.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentForeColorChanged(self,*args):
  """
  OnParentForeColorChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.ForeColorChanged event when the System.Windows.Forms.Control.ForeColor property value of the control's container changes.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentRightToLeftChanged(self,*args):
  """
  OnParentRightToLeftChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.RightToLeftChanged event when the System.Windows.Forms.Control.RightToLeft property value of the control's container changes.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnParentVisibleChanged(self,*args):
  """
  OnParentVisibleChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.VisibleChanged event when the System.Windows.Forms.Control.Visible property value of the control's container changes.
  
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
 def OnProgressChanged(self,*args):
  """
  OnProgressChanged(self: WebBrowser,e: WebBrowserProgressChangedEventArgs)
   Raises the System.Windows.Forms.WebBrowser.ProgressChanged event.
  
   e: A System.Windows.Forms.WebBrowserProgressChangedEventArgs that contains the event data.
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
  OnRightToLeftChanged(self: WebBrowserBase,e: EventArgs)
   This method is not meaningful for this control.
  
   e: An System.EventArgs object.
  """
  pass
 def OnSizeChanged(self,*args):
  """
  OnSizeChanged(self: Control,e: EventArgs)
   Raises the System.Windows.Forms.Control.SizeChanged event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnStatusTextChanged(self,*args):
  """
  OnStatusTextChanged(self: WebBrowser,e: EventArgs)
   Raises the System.Windows.Forms.WebBrowser.StatusTextChanged event.
  
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
  OnVisibleChanged(self: WebBrowserBase,e: EventArgs)
   This member overrides System.Windows.Forms.Control.OnVisibleChanged(System.EventArgs).
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def Print(self):
  """
  Print(self: WebBrowser)
   Prints the document currently displayed in the System.Windows.Forms.WebBrowser control using the current print and page settings.
  """
  pass
 def ProcessCmdKey(self,*args):
  """
  ProcessCmdKey(self: Control,msg: Message,keyData: Keys) -> (bool,Message)
  
   Processes a command key.
  
   msg: A System.Windows.Forms.Message,passed by reference,that represents the window message to process.
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
  ProcessDialogKey(self: WebBrowserBase,keyData: Keys) -> bool
  
   Processes a dialog key if the WebBrowser ActiveX control does not process it.
  
   keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
   Returns: true if the key was processed by the System.Windows.Forms.WebBrowserBase; otherwise,false.
  """
  pass
 def ProcessKeyEventArgs(self,*args):
  """
  ProcessKeyEventArgs(self: Control,m: Message) -> (bool,Message)
  
   Processes a key message and generates the appropriate control events.
  
   m: A System.Windows.Forms.Message,passed by reference,that represents the window message to process.
   Returns: true if the message was processed by the control; otherwise,false.
  """
  pass
 def ProcessKeyMessage(self,*args):
  """
  ProcessKeyMessage(self: Control,m: Message) -> (bool,Message)
  
   Processes a keyboard message.
  
   m: A System.Windows.Forms.Message,passed by reference,that represents the window message to process.
   Returns: true if the message was processed by the control; otherwise,false.
  """
  pass
 def ProcessKeyPreview(self,*args):
  """
  ProcessKeyPreview(self: Control,m: Message) -> (bool,Message)
  
   Previews a keyboard message.
  
   m: A System.Windows.Forms.Message,passed by reference,that represents the window message to process.
   Returns: true if the message was processed by the control; otherwise,false.
  """
  pass
 def ProcessMnemonic(self,*args):
  """
  ProcessMnemonic(self: WebBrowserBase,charCode: Char) -> bool
  
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
 def Refresh(self,opt=None):
  """
  Refresh(self: WebBrowser)
   Reloads the document currently displayed in the System.Windows.Forms.WebBrowser control by checking the server for an updated version.
  Refresh(self: WebBrowser,opt: WebBrowserRefreshOption)
   Reloads the document currently displayed in the System.Windows.Forms.WebBrowser control using the specified refresh options.
  
   opt: One of the System.Windows.Forms.WebBrowserRefreshOption values.
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
  
   Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate System.Windows.Forms.HorizontalAlignment to support right-to-left text.
  
   align: One of the System.Windows.Forms.HorizontalAlignment values.
   Returns: One of the System.Windows.Forms.HorizontalAlignment values.
  RtlTranslateAlignment(self: Control,align: LeftRightAlignment) -> LeftRightAlignment
  
   Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate System.Windows.Forms.LeftRightAlignment to support right-to-left text.
  
   align: One of the System.Windows.Forms.LeftRightAlignment values.
   Returns: One of the System.Windows.Forms.LeftRightAlignment values.
  RtlTranslateAlignment(self: Control,align: ContentAlignment) -> ContentAlignment
  
   Converts the specified System.Drawing.ContentAlignment to the appropriate System.Drawing.ContentAlignment to support right-to-left text.
  
   align: One of the System.Drawing.ContentAlignment values.
   Returns: One of the System.Drawing.ContentAlignment values.
  """
  pass
 def RtlTranslateContent(self,*args):
  """
  RtlTranslateContent(self: Control,align: ContentAlignment) -> ContentAlignment
  
   Converts the specified System.Drawing.ContentAlignment to the appropriate System.Drawing.ContentAlignment to support right-to-left text.
  
   align: One of the System.Drawing.ContentAlignment values.
   Returns: One of the System.Drawing.ContentAlignment values.
  """
  pass
 def RtlTranslateHorizontal(self,*args):
  """
  RtlTranslateHorizontal(self: Control,align: HorizontalAlignment) -> HorizontalAlignment
  
   Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate System.Windows.Forms.HorizontalAlignment to support right-to-left text.
  
   align: One of the System.Windows.Forms.HorizontalAlignment values.
   Returns: One of the System.Windows.Forms.HorizontalAlignment values.
  """
  pass
 def RtlTranslateLeftRight(self,*args):
  """
  RtlTranslateLeftRight(self: Control,align: LeftRightAlignment) -> LeftRightAlignment
  
   Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate System.Windows.Forms.LeftRightAlignment to support right-to-left text.
  
   align: One of the System.Windows.Forms.LeftRightAlignment values.
   Returns: One of the System.Windows.Forms.LeftRightAlignment values.
  """
  pass
 def ScaleControl(self,*args):
  """
  ScaleControl(self: Control,factor: SizeF,specified: BoundsSpecified)
   Scales a control's location,size,padding and margin.
  
   factor: The factor by which the height and width of the control will be scaled.
   specified: A System.Windows.Forms.BoundsSpecified value that specifies the bounds of the control to use when defining its size and position.
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
   Activates a child control. Optionally specifies the direction in the tab order to select the control from.
  
   directed: true to specify the direction of the control to select; otherwise,false.
   forward: true to move forward in the tab order; false to move backward in the tab order.
  """
  pass
 def SetAutoSizeMode(self,*args):
  """
  SetAutoSizeMode(self: Control,mode: AutoSizeMode)
   Sets a value indicating how a control will behave when its System.Windows.Forms.Control.AutoSize property is enabled.
  
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
 def ShowPageSetupDialog(self):
  """
  ShowPageSetupDialog(self: WebBrowser)
   Opens the Internet Explorer Page Setup dialog box.
  """
  pass
 def ShowPrintDialog(self):
  """
  ShowPrintDialog(self: WebBrowser)
   Opens the Internet Explorer Print dialog box without setting header and footer values.
  """
  pass
 def ShowPrintPreviewDialog(self):
  """
  ShowPrintPreviewDialog(self: WebBrowser)
   Opens the Internet Explorer Print Preview dialog box.
  """
  pass
 def ShowPropertiesDialog(self):
  """
  ShowPropertiesDialog(self: WebBrowser)
   Opens the Internet Explorer Properties dialog box for the current document.
  """
  pass
 def ShowSaveAsDialog(self):
  """
  ShowSaveAsDialog(self: WebBrowser)
   Opens the Internet Explorer Save Web Page dialog box or the Save dialog box of the hosted document if it is not an HTML page.
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
 def Stop(self):
  """
  Stop(self: WebBrowser)
   Cancels any pending navigation and stops any dynamic page elements,such as background sounds and animations.
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
  WndProc(self: WebBrowser,m: Message) -> Message
  
   m: The windows System.Windows.Forms.Message to process.
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
 AllowNavigation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control can navigate to another page after its initial page has been loaded.

Get: AllowNavigation(self: WebBrowser) -> bool

Set: AllowNavigation(self: WebBrowser)=value
"""

 AllowWebBrowserDrop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.WebBrowser control navigates to documents that are dropped onto it.

Get: AllowWebBrowserDrop(self: WebBrowser) -> bool

Set: AllowWebBrowserDrop(self: WebBrowser)=value
"""

 CanEnableIme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value,to enable IME support.

"""

 CanGoBack=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether a previous page in navigation history is available,which allows the System.Windows.Forms.WebBrowser.GoBack method to succeed.

Get: CanGoBack(self: WebBrowser) -> bool

"""

 CanGoForward=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether a subsequent page in navigation history is available,which allows the System.Windows.Forms.WebBrowser.GoForward method to succeed.

Get: CanGoForward(self: WebBrowser) -> bool

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if events can be raised on the control.

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
 """Gets the default size of the control.

"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

 Document=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Windows.Forms.HtmlDocument representing the Web page currently displayed in the System.Windows.Forms.WebBrowser control.

Get: Document(self: WebBrowser) -> HtmlDocument

"""

 DocumentStream=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a stream containing the contents of the Web page displayed in the System.Windows.Forms.WebBrowser control.

Get: DocumentStream(self: WebBrowser) -> Stream

Set: DocumentStream(self: WebBrowser)=value
"""

 DocumentText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the HTML contents of the page displayed in the System.Windows.Forms.WebBrowser control.

Get: DocumentText(self: WebBrowser) -> str

Set: DocumentText(self: WebBrowser)=value
"""

 DocumentTitle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the title of the document currently displayed in the System.Windows.Forms.WebBrowser control.

Get: DocumentTitle(self: WebBrowser) -> str

"""

 DocumentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of the document currently displayed in the System.Windows.Forms.WebBrowser control.

Get: DocumentType(self: WebBrowser) -> str

"""

 DoubleBuffered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this control should redraw its surface using a secondary buffer to reduce or prevent flicker.

"""

 EncryptionLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the encryption method used by the document currently displayed in the System.Windows.Forms.WebBrowser control.

Get: EncryptionLevel(self: WebBrowser) -> WebBrowserEncryptionLevel

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

 Focused=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control or any of its child windows has input focus.

Get: Focused(self: WebBrowser) -> bool

"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the font of the control.

"""

 ImeModeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the IME mode of a control.

"""

 IsBusy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.WebBrowser control is currently loading a new document.

Get: IsBusy(self: WebBrowser) -> bool

"""

 IsOffline=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.WebBrowser control is in offline mode.

Get: IsOffline(self: WebBrowser) -> bool

"""

 IsWebBrowserContextMenuEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or a sets a value indicating whether the shortcut menu of the System.Windows.Forms.WebBrowser control is enabled.

Get: IsWebBrowserContextMenuEnabled(self: WebBrowser) -> bool

Set: IsWebBrowserContextMenuEnabled(self: WebBrowser)=value
"""

 ObjectForScripting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object that can be accessed by scripting code that is contained within a Web page displayed in the System.Windows.Forms.WebBrowser control.

Get: ObjectForScripting(self: WebBrowser) -> object

Set: ObjectForScripting(self: WebBrowser)=value
"""

 Padding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is not meaningful for this control.

Get: Padding(self: WebBrowser) -> Padding

Set: Padding(self: WebBrowser)=value
"""

 ReadyState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the current state of the System.Windows.Forms.WebBrowser control.

Get: ReadyState(self: WebBrowser) -> WebBrowserReadyState

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

 ScriptErrorsSuppressed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.WebBrowser displays dialog boxes such as script error messages.

Get: ScriptErrorsSuppressed(self: WebBrowser) -> bool

Set: ScriptErrorsSuppressed(self: WebBrowser)=value
"""

 ScrollBarsEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether scroll bars are displayed in the System.Windows.Forms.WebBrowser control.

Get: ScrollBarsEnabled(self: WebBrowser) -> bool

Set: ScrollBarsEnabled(self: WebBrowser)=value
"""

 ShowFocusCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control should display focus rectangles.

"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user interface is in the appropriate state to show or hide keyboard accelerators.

"""

 StatusText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the status text of the System.Windows.Forms.WebBrowser control.

Get: StatusText(self: WebBrowser) -> str

"""

 Url=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the URL of the current document.

Get: Url(self: WebBrowser) -> Uri

Set: Url(self: WebBrowser)=value
"""

 Version=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the version of Internet Explorer installed.

Get: Version(self: WebBrowser) -> Version

"""

 WebBrowserShortcutsEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether keyboard shortcuts are enabled within the System.Windows.Forms.WebBrowser control.

Get: WebBrowserShortcutsEnabled(self: WebBrowser) -> bool

Set: WebBrowserShortcutsEnabled(self: WebBrowser)=value
"""


 CanGoBackChanged=None
 CanGoForwardChanged=None
 DocumentCompleted=None
 DocumentTitleChanged=None
 EncryptionLevelChanged=None
 FileDownload=None
 Navigated=None
 Navigating=None
 NewWindow=None
 PaddingChanged=None
 ProgressChanged=None
 StatusTextChanged=None
 WebBrowserSite=None

