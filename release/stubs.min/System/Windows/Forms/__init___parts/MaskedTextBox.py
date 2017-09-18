class MaskedTextBox(TextBoxBase,IComponent,IDisposable,IOleControl,IOleObject,IOleInPlaceObject,IOleInPlaceActiveObject,IOleWindow,IViewObject,IViewObject2,IPersist,IPersistStreamInit,IPersistPropertyBag,IPersistStorage,IQuickActivate,ISupportOleDropSource,IDropTarget,ISynchronizeInvoke,IWin32Window,IArrangedElement,IBindableComponent):
 """
 Uses a mask to distinguish between proper and improper user input.

 

 MaskedTextBox()

 MaskedTextBox(mask: str)

 MaskedTextBox(maskedTextProvider: MaskedTextProvider)
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
 def ClearUndo(self):
  """
  ClearUndo(self: MaskedTextBox)

   Clears information about the most recent operation from the undo buffer of the text box. This 

    method is not supported by System.Windows.Forms.MaskedTextBox.
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
  CreateHandle(self: MaskedTextBox)

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
 def GetCharFromPosition(self,pt):
  """
  GetCharFromPosition(self: MaskedTextBox,pt: Point) -> Char

  

   pt: The location from which to seek the nearest character.

   Returns: The character at the specified location.
  """
  pass
 def GetCharIndexFromPosition(self,pt):
  """
  GetCharIndexFromPosition(self: MaskedTextBox,pt: Point) -> int

  

   pt: The location to search.

   Returns: The zero-based character index at the specified location.
  """
  pass
 def GetFirstCharIndexFromLine(self,lineNumber):
  """
  GetFirstCharIndexFromLine(self: MaskedTextBox,lineNumber: int) -> int

  

   Retrieves the index of the first character of a given line. This method is not supported by 

    System.Windows.Forms.MaskedTextBox.

  

  

   lineNumber: This parameter is not used.

   Returns: This method will always return 0.
  """
  pass
 def GetFirstCharIndexOfCurrentLine(self):
  """
  GetFirstCharIndexOfCurrentLine(self: MaskedTextBox) -> int

  

   Retrieves the index of the first character of the current line. This method is not supported by 

    System.Windows.Forms.MaskedTextBox.

  

   Returns: This method will always return 0.
  """
  pass
 def GetLineFromCharIndex(self,index):
  """
  GetLineFromCharIndex(self: MaskedTextBox,index: int) -> int

  

   Retrieves the line number from the specified character position within the text of the control. 

    This method is not supported by System.Windows.Forms.MaskedTextBox.

  

  

   index: This parameter is not used.

   Returns: This method will always return 0.
  """
  pass
 def GetPositionFromCharIndex(self,index):
  """
  GetPositionFromCharIndex(self: MaskedTextBox,index: int) -> Point

  

   index: The index of the character for which to retrieve the location.

   Returns: The location of the specified character within the client rectangle of the control.
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
  IsInputKey(self: MaskedTextBox,keyData: Keys) -> bool

  

   Determines whether the specified key is an input key or a special key that requires 

    preprocessing.

  

  

   keyData: One of the System.Windows.Forms.Keys values.
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
 def OnAcceptsTabChanged(self,*args):
  """
  OnAcceptsTabChanged(self: TextBoxBase,e: EventArgs)

   Raises the System.Windows.Forms.TextBoxBase.AcceptsTabChanged event.

  

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
 def OnBackColorChanged(self,*args):
  """
  OnBackColorChanged(self: MaskedTextBox,e: EventArgs)

   Occurs when the value of the System.Windows.Forms.Control.BackColor property changes.

  

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
 def OnBorderStyleChanged(self,*args):
  """
  OnBorderStyleChanged(self: TextBoxBase,e: EventArgs)

   Raises the System.Windows.Forms.TextBoxBase.BorderStyleChanged event.

  

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
  OnFontChanged(self: TextBoxBase,e: EventArgs)

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
  OnHandleCreated(self: MaskedTextBox,e: EventArgs)

   Raises the System.Windows.Forms.Control.HandleCreated event.

  

   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnHandleDestroyed(self,*args):
  """
  OnHandleDestroyed(self: TextBoxBase,e: EventArgs)

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
 def OnHideSelectionChanged(self,*args):
  """
  OnHideSelectionChanged(self: TextBoxBase,e: EventArgs)

   Raise the System.Windows.Forms.TextBoxBase.HideSelectionChanged event.

  

   e: An System.EventArgs that contains the event data.
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
 def OnIsOverwriteModeChanged(self,*args):
  """
  OnIsOverwriteModeChanged(self: MaskedTextBox,e: EventArgs)

   Raises the System.Windows.Forms.MaskedTextBox.IsOverwriteModeChanged event.

  

   e: An System.EventArgs that contains event data.
  """
  pass
 def OnKeyDown(self,*args):
  """
  OnKeyDown(self: MaskedTextBox,e: KeyEventArgs)

   e: A System.Windows.Forms.KeyEventArgs that contains the event data.
  """
  pass
 def OnKeyPress(self,*args):
  """
  OnKeyPress(self: MaskedTextBox,e: KeyPressEventArgs)

   e: A System.Windows.Forms.KeyPressEventArgs that contains the event data.
  """
  pass
 def OnKeyUp(self,*args):
  """
  OnKeyUp(self: MaskedTextBox,e: KeyEventArgs)

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
 def OnMaskChanged(self,*args):
  """
  OnMaskChanged(self: MaskedTextBox,e: EventArgs)

   Raises the System.Windows.Forms.MaskedTextBox.MaskChanged event.

  

   e: An System.EventArgs that contains event data.
  """
  pass
 def OnModifiedChanged(self,*args):
  """
  OnModifiedChanged(self: TextBoxBase,e: EventArgs)

   Raises the System.Windows.Forms.TextBoxBase.ModifiedChanged event.

  

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
  OnMouseUp(self: TextBoxBase,mevent: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseUp event.

  

   mevent: The event data.
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
 def OnMultilineChanged(self,*args):
  """
  OnMultilineChanged(self: MaskedTextBox,e: EventArgs)

   Typically raises the System.Windows.Forms.MaskedTextBox.MultilineChanged event,but disabled for 

    System.Windows.Forms.MaskedTextBox.

  

  

   e: An System.EventArgs that contains event data.
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
  OnPaddingChanged(self: TextBoxBase,e: EventArgs)

   This method is not relevant for this class.

  

   e: An System.EventArgs that contains the event data.
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
 def OnReadOnlyChanged(self,*args):
  """
  OnReadOnlyChanged(self: TextBoxBase,e: EventArgs)

   Raises the System.Windows.Forms.TextBoxBase.ReadOnlyChanged event.

  

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
 def OnTextAlignChanged(self,*args):
  """
  OnTextAlignChanged(self: MaskedTextBox,e: EventArgs)

   Raises the System.Windows.Forms.MaskedTextBox.TextAlignChanged event.

  

   e: An System.EventArgs that contains event data.
  """
  pass
 def OnTextChanged(self,*args):
  """
  OnTextChanged(self: MaskedTextBox,e: EventArgs)

   Raises the System.Windows.Forms.Control.TextChanged event.

  

   e: An System.EventArgs that contains event data.
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
  OnValidating(self: MaskedTextBox,e: CancelEventArgs)

   Raises the System.Windows.Forms.Control.Validating event.

  

   e: A System.ComponentModel.CancelEventArgs that contains event data.
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
  ProcessCmdKey(self: MaskedTextBox,msg: Message,keyData: Keys) -> (bool,Message)

  

   msg: A System.Windows.Forms.Message,passed by reference that represents the window message to 

    process.

  

   keyData: One of the System.Windows.Forms.Keys values that represents the shortcut key to process.

   Returns: true if the command key was processed by the control; otherwise,false.
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
  ProcessDialogKey(self: TextBoxBase,keyData: Keys) -> bool

  

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
  ProcessKeyMessage(self: MaskedTextBox,m: Message) -> (bool,Message)

  

   Overrides the base implementation of this method to handle input language changes.

  

   m: A System.Windows.Forms.Message,passed by reference that represents the window message to 

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
 def ScrollToCaret(self):
  """
  ScrollToCaret(self: MaskedTextBox)

   Scrolls the contents of the control to the current caret position. This method is not supported 

    by System.Windows.Forms.MaskedTextBox.
  """
  pass
 def Select(self,start=None,length=None):
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
  SetBoundsCore(self: TextBoxBase,x: int,y: int,width: int,height: int,specified: BoundsSpecified)

   Sets the specified bounds of the System.Windows.Forms.TextBoxBase control.

  

   x: The new System.Windows.Forms.Control.Left property value of the control.

   y: The new System.Windows.Forms.Control.Top property value of the control.

   width: The new System.Windows.Forms.Control.Width property value of the control.

   height: Not used.

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
 def ToString(self):
  """
  ToString(self: MaskedTextBox) -> str

  

   Returns a string that represents the current masked text box. This method overrides 

    System.Windows.Forms.TextBoxBase.ToString.

  

   Returns: A System.String that contains information about the current System.Windows.Forms.MaskedTextBox. 

    The string includes the type,a simplified view of the input string,and the formatted input 

    string.
  """
  pass
 def Undo(self):
  """
  Undo(self: MaskedTextBox)

   Undoes the last edit operation in the text box. This method is not supported by 

    System.Windows.Forms.MaskedTextBox.
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
 def ValidateText(self):
  """
  ValidateText(self: MaskedTextBox) -> object

  

   Converts the user input string to an instance of the validating type.

   Returns: If successful,an System.Object of the type specified by the 

    System.Windows.Forms.MaskedTextBox.ValidatingType property; otherwise,null to indicate 

    conversion failure.
  """
  pass
 def WndProc(self,*args):
  """
  WndProc(self: MaskedTextBox,m: Message) -> Message

  

   Processes text messages.

  

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
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,mask: str)

  __new__(cls: type,maskedTextProvider: MaskedTextProvider)
  """
  pass
 def __str__(self,*args):
  pass
 AcceptsTab=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value determining how TAB keys are handled for multiline configurations. This property is not supported by System.Windows.Forms.MaskedTextBox.



Get: AcceptsTab(self: MaskedTextBox) -> bool



Set: AcceptsTab(self: MaskedTextBox)=value

"""

 AllowPromptAsInput=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether System.Windows.Forms.MaskedTextBox.PromptChar can be entered as valid data by the user.



Get: AllowPromptAsInput(self: MaskedTextBox) -> bool



Set: AllowPromptAsInput(self: MaskedTextBox)=value

"""

 AsciiOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.MaskedTextBox control accepts characters outside of the ASCII character set.



Get: AsciiOnly(self: MaskedTextBox) -> bool



Set: AsciiOnly(self: MaskedTextBox)=value

"""

 BeepOnError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the masked text box control raises the system beep for each user key stroke that it rejects.



Get: BeepOnError(self: MaskedTextBox) -> bool



Set: BeepOnError(self: MaskedTextBox)=value

"""

 CanEnableIme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value,to enable IME support.



"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if events can be raised on the control.



"""

 CanUndo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user can undo the previous operation. This property is not supported by System.Windows.Forms.MaskedTextBox.



Get: CanUndo(self: MaskedTextBox) -> bool



"""

 CreateParams=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the required creation parameters when the control handle is created.



"""

 Culture=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the culture information associated with the masked text box.



Get: Culture(self: MaskedTextBox) -> CultureInfo



Set: Culture(self: MaskedTextBox)=value

"""

 CutCopyMaskFormat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines whether literals and prompt characters are copied to the clipboard.



Get: CutCopyMaskFormat(self: MaskedTextBox) -> MaskFormat



Set: CutCopyMaskFormat(self: MaskedTextBox)=value

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
 """Gets or sets a value indicating whether control drawing is done in a buffer before the control is displayed. This property is not relevant for this class.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the font of the control.



"""

 FormatProvider=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.IFormatProvider to use when performing type validation.



Get: FormatProvider(self: MaskedTextBox) -> IFormatProvider



Set: FormatProvider(self: MaskedTextBox)=value

"""

 HidePromptOnLeave=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the prompt characters in the input mask are hidden when the masked text box loses focus.



Get: HidePromptOnLeave(self: MaskedTextBox) -> bool



Set: HidePromptOnLeave(self: MaskedTextBox)=value

"""

 ImeModeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Input Method Editor (IME) mode of a control.



"""

 InsertKeyMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text insertion mode of the masked text box control.



Get: InsertKeyMode(self: MaskedTextBox) -> InsertKeyMode



Set: InsertKeyMode(self: MaskedTextBox)=value

"""

 IsOverwriteMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that specifies whether new user input overwrites existing input.



Get: IsOverwriteMode(self: MaskedTextBox) -> bool



"""

 Lines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the lines of text in multiline configurations. This property is not supported by System.Windows.Forms.MaskedTextBox.



Get: Lines(self: MaskedTextBox) -> Array[str]



Set: Lines(self: MaskedTextBox)=value

"""

 Mask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the input mask to use at run time.



Get: Mask(self: MaskedTextBox) -> str



Set: Mask(self: MaskedTextBox)=value

"""

 MaskCompleted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether all required inputs have been entered into the input mask.



Get: MaskCompleted(self: MaskedTextBox) -> bool



"""

 MaskedTextProvider=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a clone of the mask provider associated with this instance of the masked text box control.



Get: MaskedTextProvider(self: MaskedTextBox) -> MaskedTextProvider



"""

 MaskFull=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether all required and optional inputs have been entered into the input mask.



Get: MaskFull(self: MaskedTextBox) -> bool



"""

 MaxLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum number of characters the user can type or paste into the text box control. This property is not supported by System.Windows.Forms.MaskedTextBox.



Get: MaxLength(self: MaskedTextBox) -> int



Set: MaxLength(self: MaskedTextBox)=value

"""

 Multiline=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this is a multiline text box control. This property is not fully supported by System.Windows.Forms.MaskedTextBox.



Get: Multiline(self: MaskedTextBox) -> bool



Set: Multiline(self: MaskedTextBox)=value

"""

 PasswordChar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the character to be displayed in substitute for user input.



Get: PasswordChar(self: MaskedTextBox) -> Char



Set: PasswordChar(self: MaskedTextBox)=value

"""

 PromptChar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the character used to represent the absence of user input in System.Windows.Forms.MaskedTextBox.



Get: PromptChar(self: MaskedTextBox) -> Char



Set: PromptChar(self: MaskedTextBox)=value

"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether text in the text box is read-only.



Get: ReadOnly(self: MaskedTextBox) -> bool



Set: ReadOnly(self: MaskedTextBox)=value

"""

 RejectInputOnFirstFailure=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the parsing of user input should stop after the first invalid character is reached.



Get: RejectInputOnFirstFailure(self: MaskedTextBox) -> bool



Set: RejectInputOnFirstFailure(self: MaskedTextBox)=value

"""

 RenderRightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property is now obsolete.



"""

 ResetOnPrompt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines how an input character that matches the prompt character should be handled.



Get: ResetOnPrompt(self: MaskedTextBox) -> bool



Set: ResetOnPrompt(self: MaskedTextBox)=value

"""

 ResetOnSpace=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines how a space input character should be handled.



Get: ResetOnSpace(self: MaskedTextBox) -> bool



Set: ResetOnSpace(self: MaskedTextBox)=value

"""

 ResizeRedraw=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the control redraws itself when resized.



"""

 ScaleChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines the scaling of child controls.



"""

 SelectedText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current selection in the System.Windows.Forms.MaskedTextBox control.



Get: SelectedText(self: MaskedTextBox) -> str



Set: SelectedText(self: MaskedTextBox)=value

"""

 ShowFocusCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the control should display focus rectangles.



"""

 ShowKeyboardCues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the user interface is in the appropriate state to show or hide keyboard accelerators.



"""

 SkipLiterals=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the user is allowed to reenter literal values.



Get: SkipLiterals(self: MaskedTextBox) -> bool



Set: SkipLiterals(self: MaskedTextBox)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text as it is currently displayed to the user.



Get: Text(self: MaskedTextBox) -> str



Set: Text(self: MaskedTextBox)=value

"""

 TextAlign=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets how text is aligned in a masked text box control.



Get: TextAlign(self: MaskedTextBox) -> HorizontalAlignment



Set: TextAlign(self: MaskedTextBox)=value

"""

 TextLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length of the displayed text.



Get: TextLength(self: MaskedTextBox) -> int



"""

 TextMaskFormat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines whether literals and prompt characters are included in the formatted string.



Get: TextMaskFormat(self: MaskedTextBox) -> MaskFormat



Set: TextMaskFormat(self: MaskedTextBox)=value

"""

 UseSystemPasswordChar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the operating system-supplied password character should be used.



Get: UseSystemPasswordChar(self: MaskedTextBox) -> bool



Set: UseSystemPasswordChar(self: MaskedTextBox)=value

"""

 ValidatingType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the data type used to verify the data input by the user.



Get: ValidatingType(self: MaskedTextBox) -> Type



Set: ValidatingType(self: MaskedTextBox)=value

"""

 WordWrap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a multiline text box control automatically wraps words to the beginning of the next line when necessary. This property is not supported by System.Windows.Forms.MaskedTextBox.



Get: WordWrap(self: MaskedTextBox) -> bool



Set: WordWrap(self: MaskedTextBox)=value

"""


 AcceptsTabChanged=None
 IsOverwriteModeChanged=None
 MaskChanged=None
 MaskInputRejected=None
 MultilineChanged=None
 TextAlignChanged=None
 TypeValidationCompleted=None

