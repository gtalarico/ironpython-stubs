class ToolStripDropDown(ToolStrip, IComponent, IDisposable, IOleControl, IOleObject, IOleInPlaceObject, IOleInPlaceActiveObject, IOleWindow, IViewObject, IViewObject2, IPersist, IPersistStreamInit, IPersistPropertyBag, IPersistStorage, IQuickActivate, ISupportOleDropSource, IDropTarget, ISynchronizeInvoke, IWin32Window, IArrangedElement, IBindableComponent, ISupportToolStripPanel):
    """
    Represents a control that allows the user to select a single item from a list that is displayed when the user clicks a System.Windows.Forms.ToolStripDropDownButton. Although System.Windows.Forms.ToolStripDropDownMenu and System.Windows.Forms.ToolStripDropDown replace and add functionality to the System.Windows.Forms.Menu control of previous versions, System.Windows.Forms.Menu is retained for both backward compatibility and future use if you choose.
    
    ToolStripDropDown()
    """
    def AccessibilityNotifyClients(self, *args): #cannot find CLR method
        """
        AccessibilityNotifyClients(self: Control, accEvent: AccessibleEvents, objectID: int, childID: int)
            Notifies the accessibility client applications of the specified System.Windows.Forms.AccessibleEvents for the specified child control .
        
            accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications of.
            objectID: The identifier of the System.Windows.Forms.AccessibleObject.
            childID: The child System.Windows.Forms.Control to notify of the accessible event.
        AccessibilityNotifyClients(self: Control, accEvent: AccessibleEvents, childID: int)
            Notifies the accessibility client applications of the specified System.Windows.Forms.AccessibleEvents for the specified child control.
        
            accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications of.
            childID: The child System.Windows.Forms.Control to notify of the accessible event.
        """
        pass

    def AdjustFormScrollbars(self, *args): #cannot find CLR method
        """
        AdjustFormScrollbars(self: ScrollableControl, displayScrollbars: bool)
            Adjusts the scroll bars on the container based on the current control positions and the control currently selected.
        
            displayScrollbars: true to show the scroll bars; otherwise, false.
        """
        pass

    def Close(self, reason=None):
        """
        Close(self: ToolStripDropDown, reason: ToolStripDropDownCloseReason)
            Closes the System.Windows.Forms.ToolStripDropDown control for the specified reason.
        
            reason: One of the System.Windows.Forms.ToolStripDropDownCloseReason values.
        Close(self: ToolStripDropDown)
            Closes the System.Windows.Forms.ToolStripDropDown control.
        """
        pass

    def CreateAccessibilityInstance(self, *args): #cannot find CLR method
        """
        CreateAccessibilityInstance(self: ToolStripDropDown) -> AccessibleObject
        
            Creates a new accessibility object for the System.Windows.Forms.ToolStripDropDown.
            Returns: A new System.Windows.Forms.AccessibleObject for the control.
        """
        pass

    def CreateControlsInstance(self, *args): #cannot find CLR method
        """ CreateControlsInstance(self: ToolStrip) -> ControlCollection """
        pass

    def CreateDefaultItem(self, *args): #cannot find CLR method
        """
        CreateDefaultItem(self: ToolStrip, text: str, image: Image, onClick: EventHandler) -> ToolStripItem
        
            Creates a default System.Windows.Forms.ToolStripItem with the specified text, image, and event handler on a new System.Windows.Forms.ToolStrip instance.
        
            text: The text to use for the System.Windows.Forms.ToolStripItem. If the text parameter is a hyphen (-), this method creates a System.Windows.Forms.ToolStripSeparator.
            image: The System.Drawing.Image to display on the System.Windows.Forms.ToolStripItem.
            onClick: An event handler that raises the System.Windows.Forms.Control.Click event when the System.Windows.Forms.ToolStripItem is clicked.
            Returns: A System.Windows.Forms.ToolStripButton.#ctor(System.String,System.Drawing.Image,System.EventHandler), or a System.Windows.Forms.ToolStripSeparator if the text parameter is a hyphen (-).
        """
        pass

    def CreateHandle(self, *args): #cannot find CLR method
        """ CreateHandle(self: ToolStripDropDown) """
        pass

    def CreateLayoutSettings(self, *args): #cannot find CLR method
        """
        CreateLayoutSettings(self: ToolStripDropDown, style: ToolStripLayoutStyle) -> LayoutSettings
        
            Applies various layout options to the System.Windows.Forms.ToolStripDropDown.
        
            style: One of the System.Windows.Forms.ToolStripLayoutStyle values. The possibilities are System.Windows.Forms.ToolStripLayoutStyle.Flow, System.Windows.Forms.ToolStripLayoutStyle.HorizontalStackWithOverflow, 
             System.Windows.Forms.ToolStripLayoutStyle.StackWithOverflow, System.Windows.Forms.ToolStripLayoutStyle.Table, and System.Windows.Forms.ToolStripLayoutStyle.VerticalStackWithOverflow.
        
            Returns: The System.Windows.Forms.LayoutSettings for this System.Windows.Forms.ToolStripDropDown.
        """
        pass

    def DefWndProc(self, *args): #cannot find CLR method
        """
        DefWndProc(self: Control, m: Message) -> Message
        
            Sends the specified message to the default window procedure.
        
            m: The Windows System.Windows.Forms.Message to process.
        """
        pass

    def DestroyHandle(self, *args): #cannot find CLR method
        """
        DestroyHandle(self: Control)
            Destroys the handle associated with the control.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ToolStripDropDown, disposing: bool)
            Releases the unmanaged resources used by the System.Windows.Forms.ToolStripDropDown and optionally releases the managed resources.
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GetAccessibilityObjectById(self, *args): #cannot find CLR method
        """
        GetAccessibilityObjectById(self: Control, objectId: int) -> AccessibleObject
        
            Retrieves the specified System.Windows.Forms.AccessibleObject.
        
            objectId: An Int32 that identifies the System.Windows.Forms.AccessibleObject to retrieve.
            Returns: An System.Windows.Forms.AccessibleObject.
        """
        pass

    def GetAutoSizeMode(self, *args): #cannot find CLR method
        """
        GetAutoSizeMode(self: Control) -> AutoSizeMode
        
            Retrieves a value indicating how a control will behave when its System.Windows.Forms.Control.AutoSize property is enabled.
            Returns: One of the System.Windows.Forms.AutoSizeMode values.
        """
        pass

    def GetScaledBounds(self, *args): #cannot find CLR method
        """
        GetScaledBounds(self: Control, bounds: Rectangle, factor: SizeF, specified: BoundsSpecified) -> Rectangle
        
            Retrieves the bounds within which the control is scaled.
        
            bounds: A System.Drawing.Rectangle that specifies the area for which to retrieve the display bounds.
            factor: The height and width of the control's bounds.
            specified: One of the values of System.Windows.Forms.BoundsSpecified that specifies the bounds of the control to use when defining its size and position.
            Returns: A System.Drawing.Rectangle representing the bounds within which the control is scaled.
        """
        pass

    def GetScrollState(self, *args): #cannot find CLR method
        """
        GetScrollState(self: ScrollableControl, bit: int) -> bool
        
            Determines whether the specified flag has been set.
        
            bit: The flag to check.
            Returns: true if the specified flag has been set; otherwise, false.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or by its System.ComponentModel.Container.
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def GetStyle(self, *args): #cannot find CLR method
        """
        GetStyle(self: Control, flag: ControlStyles) -> bool
        
            Retrieves the value of the specified control style bit for the control.
        
            flag: The System.Windows.Forms.ControlStyles bit to return the value from.
            Returns: true if the specified control style bit is set to true; otherwise, false.
        """
        pass

    def GetTopLevel(self, *args): #cannot find CLR method
        """
        GetTopLevel(self: Control) -> bool
        
            Determines if the control is a top-level control.
            Returns: true if the control is a top-level control; otherwise, false.
        """
        pass

    def InitLayout(self, *args): #cannot find CLR method
        """
        InitLayout(self: Control)
            Called after the control has been added to another container.
        """
        pass

    def InvokeGotFocus(self, *args): #cannot find CLR method
        """
        InvokeGotFocus(self: Control, toInvoke: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.GotFocus event for the specified control.
        
            toInvoke: The System.Windows.Forms.Control to assign the event to.
            e: An System.EventArgs that contains the event data.
        """
        pass

    def InvokeLostFocus(self, *args): #cannot find CLR method
        """
        InvokeLostFocus(self: Control, toInvoke: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.LostFocus event for the specified control.
        
            toInvoke: The System.Windows.Forms.Control to assign the event to.
            e: An System.EventArgs that contains the event data.
        """
        pass

    def InvokeOnClick(self, *args): #cannot find CLR method
        """
        InvokeOnClick(self: Control, toInvoke: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Click event for the specified control.
        
            toInvoke: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Click event to.
            e: An System.EventArgs that contains the event data.
        """
        pass

    def InvokePaint(self, *args): #cannot find CLR method
        """
        InvokePaint(self: Control, c: Control, e: PaintEventArgs)
            Raises the System.Windows.Forms.Control.Paint event for the specified control.
        
            c: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Paint event to.
            e: An System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def InvokePaintBackground(self, *args): #cannot find CLR method
        """
        InvokePaintBackground(self: Control, c: Control, e: PaintEventArgs)
            Raises the PaintBackground event for the specified control.
        
            c: The System.Windows.Forms.Control to assign the System.Windows.Forms.Control.Paint event to.
            e: An System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def IsInputChar(self, *args): #cannot find CLR method
        """
        IsInputChar(self: ToolStrip, charCode: Char) -> bool
        
            Determines whether a character is an input character that the item recognizes.
        
            charCode: The character to test.
            Returns: true if the character should be sent directly to the item and not preprocessed; otherwise, false.
        """
        pass

    def IsInputKey(self, *args): #cannot find CLR method
        """
        IsInputKey(self: ToolStrip, keyData: Keys) -> bool
        
            Determines whether the specified key is a regular input key or a special key that requires preprocessing.
        
            keyData: One of the System.Windows.Forms.Keys values.
            Returns: true if the specified key is a regular input key; otherwise, false.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A value of false is 
             usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def NotifyInvalidate(self, *args): #cannot find CLR method
        """
        NotifyInvalidate(self: Control, invalidatedArea: Rectangle)
            Raises the System.Windows.Forms.Control.Invalidated event with a specified region of the control to invalidate.
        
            invalidatedArea: A System.Drawing.Rectangle representing the area to invalidate.
        """
        pass

    def OnAutoSizeChanged(self, *args): #cannot find CLR method
        """
        OnAutoSizeChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.AutoSizeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnBackColorChanged(self, *args): #cannot find CLR method
        """
        OnBackColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackColorChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnBackgroundImageChanged(self, *args): #cannot find CLR method
        """
        OnBackgroundImageChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackgroundImageChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnBackgroundImageLayoutChanged(self, *args): #cannot find CLR method
        """
        OnBackgroundImageLayoutChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackgroundImageLayoutChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnBeginDrag(self, *args): #cannot find CLR method
        """
        OnBeginDrag(self: ToolStrip, e: EventArgs)
            Raises the System.Windows.Forms.ToolStrip.BeginDrag event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnBindingContextChanged(self, *args): #cannot find CLR method
        """
        OnBindingContextChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BindingContextChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnCausesValidationChanged(self, *args): #cannot find CLR method
        """
        OnCausesValidationChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.CausesValidationChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnChangeUICues(self, *args): #cannot find CLR method
        """
        OnChangeUICues(self: Control, e: UICuesEventArgs)
            Raises the System.Windows.Forms.Control.ChangeUICues event.
        
            e: A System.Windows.Forms.UICuesEventArgs that contains the event data.
        """
        pass

    def OnClick(self, *args): #cannot find CLR method
        """
        OnClick(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Click event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnClientSizeChanged(self, *args): #cannot find CLR method
        """
        OnClientSizeChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ClientSizeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnClosed(self, *args): #cannot find CLR method
        """
        OnClosed(self: ToolStripDropDown, e: ToolStripDropDownClosedEventArgs)
            Raises the System.Windows.Forms.ToolStripDropDown.Closed event.
        
            e: A System.Windows.Forms.ToolStripDropDownClosedEventArgs that contains the event data.
        """
        pass

    def OnClosing(self, *args): #cannot find CLR method
        """
        OnClosing(self: ToolStripDropDown, e: ToolStripDropDownClosingEventArgs)
            Raises the System.Windows.Forms.ToolStripDropDown.Closing event.
        
            e: A System.Windows.Forms.ToolStripDropDownClosingEventArgs that contains the event data.
        """
        pass

    def OnContextMenuChanged(self, *args): #cannot find CLR method
        """
        OnContextMenuChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ContextMenuChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnContextMenuStripChanged(self, *args): #cannot find CLR method
        """
        OnContextMenuStripChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ContextMenuStripChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnControlAdded(self, *args): #cannot find CLR method
        """
        OnControlAdded(self: Control, e: ControlEventArgs)
            Raises the System.Windows.Forms.Control.ControlAdded event.
        
            e: A System.Windows.Forms.ControlEventArgs that contains the event data.
        """
        pass

    def OnControlRemoved(self, *args): #cannot find CLR method
        """
        OnControlRemoved(self: Control, e: ControlEventArgs)
            Raises the System.Windows.Forms.Control.ControlRemoved event.
        
            e: A System.Windows.Forms.ControlEventArgs that contains the event data.
        """
        pass

    def OnCreateControl(self, *args): #cannot find CLR method
        """
        OnCreateControl(self: Control)
            Raises the System.Windows.Forms.Control.CreateControl method.
        """
        pass

    def OnCursorChanged(self, *args): #cannot find CLR method
        """
        OnCursorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.CursorChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnDockChanged(self, *args): #cannot find CLR method
        """
        OnDockChanged(self: ToolStrip, e: EventArgs)
            Raises the System.Windows.Forms.Control.DockChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnDoubleClick(self, *args): #cannot find CLR method
        """
        OnDoubleClick(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.DoubleClick event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnDragDrop(self, *args): #cannot find CLR method
        """
        OnDragDrop(self: Control, drgevent: DragEventArgs)
            Raises the System.Windows.Forms.Control.DragDrop event.
        
            drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
        """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: Control, drgevent: DragEventArgs)
            Raises the System.Windows.Forms.Control.DragEnter event.
        
            drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.DragLeave event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: Control, drgevent: DragEventArgs)
            Raises the System.Windows.Forms.Control.DragOver event.
        
            drgevent: A System.Windows.Forms.DragEventArgs that contains the event data.
        """
        pass

    def OnEnabledChanged(self, *args): #cannot find CLR method
        """
        OnEnabledChanged(self: ToolStrip, e: EventArgs)
            Raises the System.Windows.Forms.Control.Enabled event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnEndDrag(self, *args): #cannot find CLR method
        """
        OnEndDrag(self: ToolStrip, e: EventArgs)
            Raises the System.Windows.Forms.ToolStrip.EndDrag event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnEnter(self, *args): #cannot find CLR method
        """
        OnEnter(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Enter event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnFontChanged(self, *args): #cannot find CLR method
        """
        OnFontChanged(self: ToolStrip, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnForeColorChanged(self, *args): #cannot find CLR method
        """
        OnForeColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ForeColorChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: Control, gfbevent: GiveFeedbackEventArgs)
            Raises the System.Windows.Forms.Control.GiveFeedback event.
        
            gfbevent: A System.Windows.Forms.GiveFeedbackEventArgs that contains the event data.
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.GotFocus event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnHandleCreated(self, *args): #cannot find CLR method
        """
        OnHandleCreated(self: ToolStripDropDown, e: EventArgs)
            Raises the System.Windows.Forms.Control.HandleCreated event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnHandleDestroyed(self, *args): #cannot find CLR method
        """
        OnHandleDestroyed(self: ToolStrip, e: EventArgs)
            Raises the System.Windows.Forms.Control.HandleDestroyed event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnHelpRequested(self, *args): #cannot find CLR method
        """
        OnHelpRequested(self: Control, hevent: HelpEventArgs)
            Raises the System.Windows.Forms.Control.HelpRequested event.
        
            hevent: A System.Windows.Forms.HelpEventArgs that contains the event data.
        """
        pass

    def OnImeModeChanged(self, *args): #cannot find CLR method
        """
        OnImeModeChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ImeModeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnInvalidated(self, *args): #cannot find CLR method
        """
        OnInvalidated(self: ToolStrip, e: InvalidateEventArgs)
            e: An System.Windows.Forms.InvalidateEventArgs that contains the event data.
        """
        pass

    def OnItemAdded(self, *args): #cannot find CLR method
        """
        OnItemAdded(self: ToolStrip, e: ToolStripItemEventArgs)
            Raises the System.Windows.Forms.ToolStrip.ItemAdded event.
        
            e: A System.Windows.Forms.ToolStripItemEventArgs that contains the event data.
        """
        pass

    def OnItemClicked(self, *args): #cannot find CLR method
        """
        OnItemClicked(self: ToolStripDropDown, e: ToolStripItemClickedEventArgs)
            Raises the System.Windows.Forms.ToolStrip.ItemClicked event.
        
            e: A System.Windows.Forms.ToolStripItemClickedEventArgs that contains the event data.
        """
        pass

    def OnItemRemoved(self, *args): #cannot find CLR method
        """
        OnItemRemoved(self: ToolStrip, e: ToolStripItemEventArgs)
            Raises the System.Windows.Forms.ToolStrip.ItemRemoved event.
        
            e: A System.Windows.Forms.ToolStripItemEventArgs that contains the event data.
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: Control, e: KeyEventArgs)
            Raises the System.Windows.Forms.Control.KeyDown event.
        
            e: A System.Windows.Forms.KeyEventArgs that contains the event data.
        """
        pass

    def OnKeyPress(self, *args): #cannot find CLR method
        """
        OnKeyPress(self: Control, e: KeyPressEventArgs)
            Raises the System.Windows.Forms.Control.KeyPress event.
        
            e: A System.Windows.Forms.KeyPressEventArgs that contains the event data.
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: Control, e: KeyEventArgs)
            Raises the System.Windows.Forms.Control.KeyUp event.
        
            e: A System.Windows.Forms.KeyEventArgs that contains the event data.
        """
        pass

    def OnLayout(self, *args): #cannot find CLR method
        """
        OnLayout(self: ToolStripDropDown, e: LayoutEventArgs)
            Raises the System.Windows.Forms.Control.Layout event.
        
            e: A System.Windows.Forms.LayoutEventArgs that contains the event data.
        """
        pass

    def OnLayoutCompleted(self, *args): #cannot find CLR method
        """
        OnLayoutCompleted(self: ToolStrip, e: EventArgs)
            Raises the System.Windows.Forms.ToolStrip.LayoutCompleted event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnLayoutStyleChanged(self, *args): #cannot find CLR method
        """
        OnLayoutStyleChanged(self: ToolStrip, e: EventArgs)
            Raises the System.Windows.Forms.ToolStrip.LayoutStyleChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnLeave(self, *args): #cannot find CLR method
        """
        OnLeave(self: ToolStrip, e: EventArgs)
            Raises the System.Windows.Forms.Control.Leave event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnLocationChanged(self, *args): #cannot find CLR method
        """
        OnLocationChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.LocationChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: ToolStrip, e: EventArgs)
            Raises the System.Windows.Forms.Control.LostFocus event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMarginChanged(self, *args): #cannot find CLR method
        """
        OnMarginChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MarginChanged event.
        
            e: A System.EventArgs that contains the event data.
        """
        pass

    def OnMouseCaptureChanged(self, *args): #cannot find CLR method
        """
        OnMouseCaptureChanged(self: ToolStrip, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseClick(self, *args): #cannot find CLR method
        """
        OnMouseClick(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseClick event.
        
            e: An System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseDoubleClick(self, *args): #cannot find CLR method
        """
        OnMouseDoubleClick(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseDoubleClick event.
        
            e: An System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: ToolStrip, mea: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseDown event.
        
            mea: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseEnter event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseHover(self, *args): #cannot find CLR method
        """
        OnMouseHover(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseHover event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: ToolStrip, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseLeave event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: ToolStrip, mea: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseMove event.
        
            mea: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: ToolStripDropDown, mea: MouseEventArgs)
            Raises the System.Windows.Forms.ToolStripItem.MouseUp event.
        
            mea: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: ScrollableControl, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseWheel event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMove(self, *args): #cannot find CLR method
        """
        OnMove(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Move event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnNotifyMessage(self, *args): #cannot find CLR method
        """
        OnNotifyMessage(self: Control, m: Message)
            Notifies the control of Windows messages.
        
            m: A System.Windows.Forms.Message that represents the Windows message.
        """
        pass

    def OnOpened(self, *args): #cannot find CLR method
        """
        OnOpened(self: ToolStripDropDown, e: EventArgs)
            Raises the System.Windows.Forms.ToolStripDropDown.Opened event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnOpening(self, *args): #cannot find CLR method
        """
        OnOpening(self: ToolStripDropDown, e: CancelEventArgs)
            Raises the System.Windows.Forms.ToolStripDropDown.Opening event.
        
            e: A System.ComponentModel.CancelEventArgs that contains the event data.
        """
        pass

    def OnPaddingChanged(self, *args): #cannot find CLR method
        """
        OnPaddingChanged(self: ScrollableControl, e: EventArgs)
            Raises the System.Windows.Forms.Control.PaddingChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnPaint(self, *args): #cannot find CLR method
        """
        OnPaint(self: ToolStrip, e: PaintEventArgs)
            Raises the System.Windows.Forms.Control.Paint event.
        
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def OnPaintBackground(self, *args): #cannot find CLR method
        """
        OnPaintBackground(self: ToolStrip, e: PaintEventArgs)
            Raises the System.Windows.Forms.Control.Paint event for the System.Windows.Forms.ToolStrip background.
        
            e: A System.Windows.Forms.PaintEventArgs that contains information about the control to paint.
        """
        pass

    def OnPaintGrip(self, *args): #cannot find CLR method
        """
        OnPaintGrip(self: ToolStrip, e: PaintEventArgs)
            Raises the System.Windows.Forms.ToolStrip.PaintGrip event.
        
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def OnParentBackColorChanged(self, *args): #cannot find CLR method
        """
        OnParentBackColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackColorChanged event when the System.Windows.Forms.Control.BackColor property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentBackgroundImageChanged(self, *args): #cannot find CLR method
        """
        OnParentBackgroundImageChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackgroundImageChanged event when the System.Windows.Forms.Control.BackgroundImage property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentBindingContextChanged(self, *args): #cannot find CLR method
        """
        OnParentBindingContextChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BindingContextChanged event when the System.Windows.Forms.Control.BindingContext property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentChanged(self, *args): #cannot find CLR method
        """
        OnParentChanged(self: ToolStripDropDown, e: EventArgs)
            Raises the System.Windows.Forms.Control.ParentChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentCursorChanged(self, *args): #cannot find CLR method
        """
        OnParentCursorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.CursorChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentEnabledChanged(self, *args): #cannot find CLR method
        """
        OnParentEnabledChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.EnabledChanged event when the System.Windows.Forms.Control.Enabled property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentFontChanged(self, *args): #cannot find CLR method
        """
        OnParentFontChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.FontChanged event when the System.Windows.Forms.Control.Font property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentForeColorChanged(self, *args): #cannot find CLR method
        """
        OnParentForeColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ForeColorChanged event when the System.Windows.Forms.Control.ForeColor property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentRightToLeftChanged(self, *args): #cannot find CLR method
        """
        OnParentRightToLeftChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.RightToLeftChanged event when the System.Windows.Forms.Control.RightToLeft property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentVisibleChanged(self, *args): #cannot find CLR method
        """
        OnParentVisibleChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.VisibleChanged event when the System.Windows.Forms.Control.Visible property value of the control's container changes.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: Control, e: PreviewKeyDownEventArgs)
            Raises the System.Windows.Forms.Control.PreviewKeyDown event.
        
            e: A System.Windows.Forms.PreviewKeyDownEventArgs that contains the event data.
        """
        pass

    def OnPrint(self, *args): #cannot find CLR method
        """
        OnPrint(self: Control, e: PaintEventArgs)
            Raises the System.Windows.Forms.Control.Paint event.
        
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: Control, qcdevent: QueryContinueDragEventArgs)
            Raises the System.Windows.Forms.Control.QueryContinueDrag event.
        
            qcdevent: A System.Windows.Forms.QueryContinueDragEventArgs that contains the event data.
        """
        pass

    def OnRegionChanged(self, *args): #cannot find CLR method
        """
        OnRegionChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.RegionChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnRendererChanged(self, *args): #cannot find CLR method
        """
        OnRendererChanged(self: ToolStrip, e: EventArgs)
            Raises the System.Windows.Forms.ToolStrip.RendererChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnResize(self, *args): #cannot find CLR method
        """
        OnResize(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Resize event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnRightToLeftChanged(self, *args): #cannot find CLR method
        """
        OnRightToLeftChanged(self: ToolStrip, e: EventArgs)
            Raises the System.Windows.Forms.Control.RightToLeftChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnScroll(self, *args): #cannot find CLR method
        """
        OnScroll(self: ToolStrip, se: ScrollEventArgs)
            se: A System.Windows.Forms.ScrollEventArgs that contains the event data.
        """
        pass

    def OnSizeChanged(self, *args): #cannot find CLR method
        """
        OnSizeChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.SizeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.StyleChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnSystemColorsChanged(self, *args): #cannot find CLR method
        """
        OnSystemColorsChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.SystemColorsChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnTabIndexChanged(self, *args): #cannot find CLR method
        """
        OnTabIndexChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.TabIndexChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnTabStopChanged(self, *args): #cannot find CLR method
        """
        OnTabStopChanged(self: ToolStrip, e: EventArgs)
            Raises the System.Windows.Forms.Control.TabStopChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnTextChanged(self, *args): #cannot find CLR method
        """
        OnTextChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.TextChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnValidated(self, *args): #cannot find CLR method
        """
        OnValidated(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Validated event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnValidating(self, *args): #cannot find CLR method
        """
        OnValidating(self: Control, e: CancelEventArgs)
            Raises the System.Windows.Forms.Control.Validating event.
        
            e: A System.ComponentModel.CancelEventArgs that contains the event data.
        """
        pass

    def OnVisibleChanged(self, *args): #cannot find CLR method
        """
        OnVisibleChanged(self: ToolStripDropDown, e: EventArgs)
            Raises the System.Windows.Forms.ToolStripItem.VisibleChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def ProcessCmdKey(self, *args): #cannot find CLR method
        """
        ProcessCmdKey(self: ToolStrip, m: Message, keyData: Keys) -> (bool, Message)
        
            Processes a command key.
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to process.
            keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
            Returns: true if the character was processed by the control; otherwise, false.
        """
        pass

    def ProcessDialogChar(self, *args): #cannot find CLR method
        """
        ProcessDialogChar(self: ToolStripDropDown, charCode: Char) -> bool
        
            Processes a dialog box character.
        
            charCode: The character to process.
            Returns: true if the character was processed by the control; otherwise, false.
        """
        pass

    def ProcessDialogKey(self, *args): #cannot find CLR method
        """
        ProcessDialogKey(self: ToolStripDropDown, keyData: Keys) -> bool
        
            Processes a dialog box key.
        
            keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
            Returns: true if the key was processed by the control; otherwise, false.
        """
        pass

    def ProcessKeyEventArgs(self, *args): #cannot find CLR method
        """
        ProcessKeyEventArgs(self: Control, m: Message) -> (bool, Message)
        
            Processes a key message and generates the appropriate control events.
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to process.
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessKeyMessage(self, *args): #cannot find CLR method
        """
        ProcessKeyMessage(self: Control, m: Message) -> (bool, Message)
        
            Processes a keyboard message.
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to process.
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessKeyPreview(self, *args): #cannot find CLR method
        """
        ProcessKeyPreview(self: Control, m: Message) -> (bool, Message)
        
            Previews a keyboard message.
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to process.
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessMnemonic(self, *args): #cannot find CLR method
        """
        ProcessMnemonic(self: ToolStripDropDown, charCode: Char) -> bool
        
            Processes a mnemonic character.
        
            charCode: The character to process.
            Returns: true if the character was processed as a mnemonic by the control; otherwise, false.
        """
        pass

    def RaiseDragEvent(self, *args): #cannot find CLR method
        """
        RaiseDragEvent(self: Control, key: object, e: DragEventArgs)
            Raises the appropriate drag event.
        
            key: The event to raise.
            e: A System.Windows.Forms.DragEventArgs that contains the event data.
        """
        pass

    def RaiseKeyEvent(self, *args): #cannot find CLR method
        """
        RaiseKeyEvent(self: Control, key: object, e: KeyEventArgs)
            Raises the appropriate key event.
        
            key: The event to raise.
            e: A System.Windows.Forms.KeyEventArgs that contains the event data.
        """
        pass

    def RaiseMouseEvent(self, *args): #cannot find CLR method
        """
        RaiseMouseEvent(self: Control, key: object, e: MouseEventArgs)
            Raises the appropriate mouse event.
        
            key: The event to raise.
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def RaisePaintEvent(self, *args): #cannot find CLR method
        """
        RaisePaintEvent(self: Control, key: object, e: PaintEventArgs)
            Raises the appropriate paint event.
        
            key: The event to raise.
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def RecreateHandle(self, *args): #cannot find CLR method
        """
        RecreateHandle(self: Control)
            Forces the re-creation of the handle for the control.
        """
        pass

    def ResetMouseEventArgs(self, *args): #cannot find CLR method
        """
        ResetMouseEventArgs(self: Control)
            Resets the control to handle the System.Windows.Forms.Control.MouseLeave event.
        """
        pass

    def RestoreFocus(self, *args): #cannot find CLR method
        """
        RestoreFocus(self: ToolStrip)
            Controls the return location of the focus.
        """
        pass

    def RtlTranslateAlignment(self, *args): #cannot find CLR method
        """
        RtlTranslateAlignment(self: Control, align: ContentAlignment) -> ContentAlignment
        
            Converts the specified System.Drawing.ContentAlignment to the appropriate System.Drawing.ContentAlignment to support right-to-left text.
        
            align: One of the System.Drawing.ContentAlignment values.
            Returns: One of the System.Drawing.ContentAlignment values.
        RtlTranslateAlignment(self: Control, align: LeftRightAlignment) -> LeftRightAlignment
        
            Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate System.Windows.Forms.LeftRightAlignment to support right-to-left text.
        
            align: One of the System.Windows.Forms.LeftRightAlignment values.
            Returns: One of the System.Windows.Forms.LeftRightAlignment values.
        RtlTranslateAlignment(self: Control, align: HorizontalAlignment) -> HorizontalAlignment
        
            Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate System.Windows.Forms.HorizontalAlignment to support right-to-left text.
        
            align: One of the System.Windows.Forms.HorizontalAlignment values.
            Returns: One of the System.Windows.Forms.HorizontalAlignment values.
        """
        pass

    def RtlTranslateContent(self, *args): #cannot find CLR method
        """
        RtlTranslateContent(self: Control, align: ContentAlignment) -> ContentAlignment
        
            Converts the specified System.Drawing.ContentAlignment to the appropriate System.Drawing.ContentAlignment to support right-to-left text.
        
            align: One of the System.Drawing.ContentAlignment values.
            Returns: One of the System.Drawing.ContentAlignment values.
        """
        pass

    def RtlTranslateHorizontal(self, *args): #cannot find CLR method
        """
        RtlTranslateHorizontal(self: Control, align: HorizontalAlignment) -> HorizontalAlignment
        
            Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate System.Windows.Forms.HorizontalAlignment to support right-to-left text.
        
            align: One of the System.Windows.Forms.HorizontalAlignment values.
            Returns: One of the System.Windows.Forms.HorizontalAlignment values.
        """
        pass

    def RtlTranslateLeftRight(self, *args): #cannot find CLR method
        """
        RtlTranslateLeftRight(self: Control, align: LeftRightAlignment) -> LeftRightAlignment
        
            Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate System.Windows.Forms.LeftRightAlignment to support right-to-left text.
        
            align: One of the System.Windows.Forms.LeftRightAlignment values.
            Returns: One of the System.Windows.Forms.LeftRightAlignment values.
        """
        pass

    def ScaleControl(self, *args): #cannot find CLR method
        """
        ScaleControl(self: ToolStripDropDown, factor: SizeF, specified: BoundsSpecified)
            Scales a control's location, size, padding and margin.
        
            factor: The factor by which the height and width of the control will be scaled.
            specified: A value that specifies the bounds of the control to use when defining its size and position.
        """
        pass

    def ScaleCore(self, *args): #cannot find CLR method
        """
        ScaleCore(self: ToolStripDropDown, dx: Single, dy: Single)
            This method is not relevant to this class.
        
            dx: The horizontal scaling factor.
            dy: The vertical scaling factor.
        """
        pass

    def ScrollToControl(self, *args): #cannot find CLR method
        """
        ScrollToControl(self: ScrollableControl, activeControl: Control) -> Point
        
            Calculates the scroll offset to the specified child control.
        
            activeControl: The child control to scroll into view.
            Returns: The upper-left hand System.Drawing.Point of the display area relative to the client area required to scroll the control into view.
        """
        pass

    def Select(self):
        """
        Select(self: ToolStrip, directed: bool, forward: bool)
            Activates a child control. Optionally specifies the direction in the tab order to select the control from.
        
            directed: true to specify the direction of the control to select; otherwise, false.
            forward: true to move forward in the tab order; false to move backward in the tab order.
        """
        pass

    def SetAutoSizeMode(self, *args): #cannot find CLR method
        """
        SetAutoSizeMode(self: Control, mode: AutoSizeMode)
            Sets a value indicating how a control will behave when its System.Windows.Forms.Control.AutoSize property is enabled.
        
            mode: One of the System.Windows.Forms.AutoSizeMode values.
        """
        pass

    def SetBoundsCore(self, *args): #cannot find CLR method
        """
        SetBoundsCore(self: ToolStripDropDown, x: int, y: int, width: int, height: int, specified: BoundsSpecified)
            Performs the work of setting the specified bounds of this control.
        
            x: The new System.Windows.Forms.Control.Left property value of the control.
            y: The new System.Windows.Forms.Control.Top property value of the control.
            width: The new System.Windows.Forms.Control.Width property value of the control.
            height: The new System.Windows.Forms.Control.Height property value of the control.
            specified: A bitwise combination of the System.Windows.Forms.BoundsSpecified values.
        """
        pass

    def SetClientSizeCore(self, *args): #cannot find CLR method
        """
        SetClientSizeCore(self: Control, x: int, y: int)
            Sets the size of the client area of the control.
        
            x: The client area width, in pixels.
            y: The client area height, in pixels.
        """
        pass

    def SetDisplayedItems(self, *args): #cannot find CLR method
        """
        SetDisplayedItems(self: ToolStrip)
            Resets the collection of displayed and overflow items after a layout is done.
        """
        pass

    def SetDisplayRectLocation(self, *args): #cannot find CLR method
        """
        SetDisplayRectLocation(self: ScrollableControl, x: int, y: int)
            Positions the display window to the specified value.
        
            x: The horizontal offset at which to position the System.Windows.Forms.ScrollableControl.
            y: The vertical offset at which to position the System.Windows.Forms.ScrollableControl.
        """
        pass

    def SetItemLocation(self, *args): #cannot find CLR method
        """
        SetItemLocation(self: ToolStrip, item: ToolStripItem, location: Point)
            Anchors a System.Windows.Forms.ToolStripItem to a particular place on a System.Windows.Forms.ToolStrip.
        
            item: The System.Windows.Forms.ToolStripItem to anchor.
            location: A System.Drawing.Point representing the x and y client coordinates of the System.Windows.Forms.ToolStripItem location, in pixels.
        """
        pass

    def SetScrollState(self, *args): #cannot find CLR method
        """
        SetScrollState(self: ScrollableControl, bit: int, value: bool)
            Sets the specified scroll state flag.
        
            bit: The scroll state flag to set.
            value: The value to set the flag.
        """
        pass

    def SetStyle(self, *args): #cannot find CLR method
        """
        SetStyle(self: Control, flag: ControlStyles, value: bool)
            Sets a specified System.Windows.Forms.ControlStyles flag to either true or false.
        
            flag: The System.Windows.Forms.ControlStyles bit to set.
            value: true to apply the specified style to the control; otherwise, false.
        """
        pass

    def SetTopLevel(self, *args): #cannot find CLR method
        """
        SetTopLevel(self: Control, value: bool)
            Sets the control as the top-level control.
        
            value: true to set the control as the top-level control; otherwise, false.
        """
        pass

    def SetVisibleCore(self, *args): #cannot find CLR method
        """
        SetVisibleCore(self: ToolStripDropDown, visible: bool)
            Adjusts the size of the owner System.Windows.Forms.ToolStrip to accommodate the System.Windows.Forms.ToolStripDropDown if the owner System.Windows.Forms.ToolStrip is currently displayed, or clears and 
             resets active System.Windows.Forms.ToolStripDropDown child controls of the System.Windows.Forms.ToolStrip if the System.Windows.Forms.ToolStrip is not currently displayed.
        
        
            visible: true if the owner System.Windows.Forms.ToolStrip is currently displayed; otherwise, false.
        """
        pass

    def Show(self, *__args):
        """
        Show(self: ToolStripDropDown, screenLocation: Point)
            Positions the System.Windows.Forms.ToolStripDropDown relative to the specified screen location.
        
            screenLocation: The horizontal and vertical location of the screen's upper-left corner, in pixels.
        Show(self: ToolStripDropDown, position: Point, direction: ToolStripDropDownDirection)
            Positions the System.Windows.Forms.ToolStripDropDown relative to the specified control location and with the specified direction relative to the parent control.
        
            position: The horizontal and vertical location of the reference control's upper-left corner, in pixels.
            direction: One of the System.Windows.Forms.ToolStripDropDownDirection values.
        Show(self: ToolStripDropDown, x: int, y: int)
            Positions the System.Windows.Forms.ToolStripDropDown relative to the specified screen coordinates.
        
            x: The horizontal screen coordinate, in pixels.
            y: The vertical screen coordinate, in pixels.
        Show(self: ToolStripDropDown, control: Control, x: int, y: int)
            Positions the System.Windows.Forms.ToolStripDropDown relative to the specified control's horizontal and vertical screen coordinates.
        
            control: The control (typically, a System.Windows.Forms.ToolStripDropDownButton) that is the reference point for the System.Windows.Forms.ToolStripDropDown position.
            x: The horizontal screen coordinate of the control, in pixels.
            y: The vertical screen coordinate of the control, in pixels.
        Show(self: ToolStripDropDown)
            Displays the System.Windows.Forms.ToolStripDropDown control in its default position.
        Show(self: ToolStripDropDown, control: Control, position: Point)
            Positions the System.Windows.Forms.ToolStripDropDown relative to the specified control location.
        
            control: The control (typically, a System.Windows.Forms.ToolStripDropDownButton) that is the reference point for the System.Windows.Forms.ToolStripDropDown position.
            position: The horizontal and vertical location of the reference control's upper-left corner, in pixels.
        Show(self: ToolStripDropDown, control: Control, position: Point, direction: ToolStripDropDownDirection)
            Positions the System.Windows.Forms.ToolStripDropDown relative to the specified control at the specified location and with the specified direction relative to the parent control.
        
            control: The control (typically, a System.Windows.Forms.ToolStripDropDownButton) that is the reference point for the System.Windows.Forms.ToolStripDropDown position.
            position: The horizontal and vertical location of the reference control's upper-left corner, in pixels.
            direction: One of the System.Windows.Forms.ToolStripDropDownDirection values.
        """
        pass

    def SizeFromClientSize(self, *args): #cannot find CLR method
        """
        SizeFromClientSize(self: Control, clientSize: Size) -> Size
        
            Determines the size of the entire control from the height and width of its client area.
        
            clientSize: A System.Drawing.Size value representing the height and width of the control's client area.
            Returns: A System.Drawing.Size value representing the height and width of the entire control.
        """
        pass

    def UpdateBounds(self, *args): #cannot find CLR method
        """
        UpdateBounds(self: Control, x: int, y: int, width: int, height: int, clientWidth: int, clientHeight: int)
            Updates the bounds of the control with the specified size, location, and client size.
        
            x: The System.Drawing.Point.X coordinate of the control.
            y: The System.Drawing.Point.Y coordinate of the control.
            width: The System.Drawing.Size.Width of the control.
            height: The System.Drawing.Size.Height of the control.
            clientWidth: The client System.Drawing.Size.Width of the control.
            clientHeight: The client System.Drawing.Size.Height of the control.
        UpdateBounds(self: Control, x: int, y: int, width: int, height: int)
            Updates the bounds of the control with the specified size and location.
        
            x: The System.Drawing.Point.X coordinate of the control.
            y: The System.Drawing.Point.Y coordinate of the control.
            width: The System.Drawing.Size.Width of the control.
            height: The System.Drawing.Size.Height of the control.
        UpdateBounds(self: Control)
            Updates the bounds of the control with the current size and location.
        """
        pass

    def UpdateStyles(self, *args): #cannot find CLR method
        """
        UpdateStyles(self: Control)
            Forces the assigned styles to be reapplied to the control.
        """
        pass

    def UpdateZOrder(self, *args): #cannot find CLR method
        """
        UpdateZOrder(self: Control)
            Updates the control in its parent's z-order.
        """
        pass

    def WndProc(self, *args): #cannot find CLR method
        """
        WndProc(self: ToolStripDropDown, m: Message) -> Message
        
            m: The Windows System.Windows.Forms.Message to process.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AllowItemReorder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not relevant to this class.

Get: AllowItemReorder(self: ToolStripDropDown) -> bool

Set: AllowItemReorder(self: ToolStripDropDown) = value
"""

    AllowTransparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the System.Windows.Forms.ToolStripDropDown.Opacity of the form can be adjusted.

Get: AllowTransparency(self: ToolStripDropDown) -> bool

Set: AllowTransparency(self: ToolStripDropDown) = value
"""

    Anchor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not relevant to this class.

Get: Anchor(self: ToolStripDropDown) -> AnchorStyles

Set: Anchor(self: ToolStripDropDown) = value
"""

    AutoClose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the System.Windows.Forms.ToolStripDropDown control should automatically close when it has lost activation.

Get: AutoClose(self: ToolStripDropDown) -> bool

Set: AutoClose(self: ToolStripDropDown) = value
"""

    AutoSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the System.Windows.Forms.ToolStripDropDown automatically adjusts its size when the form is resized.

Get: AutoSize(self: ToolStripDropDown) -> bool

Set: AutoSize(self: ToolStripDropDown) = value
"""

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value, to enable IME support.

"""

    CanOverflow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the items in a System.Windows.Forms.ToolStripDropDown can be sent to an overflow menu.

Get: CanOverflow(self: ToolStripDropDown) -> bool

Set: CanOverflow(self: ToolStripDropDown) = value
"""

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if events can be raised on the control.

"""

    ContextMenu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not relevant to this class.

Get: ContextMenu(self: ToolStripDropDown) -> ContextMenu

Set: ContextMenu(self: ToolStripDropDown) = value
"""

    ContextMenuStrip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not relevant to this class.

Get: ContextMenuStrip(self: ToolStripDropDown) -> ContextMenuStrip

Set: ContextMenuStrip(self: ToolStripDropDown) = value
"""

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets parameters of a new window.

"""

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default cursor for the control.

"""

    DefaultDock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultDropDownDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the direction in which the System.Windows.Forms.ToolStripDropDown is displayed relative to the System.Windows.Forms.ToolStrip.

Get: DefaultDropDownDirection(self: ToolStripDropDown) -> ToolStripDropDownDirection

Set: DefaultDropDownDirection(self: ToolStripDropDown) = value
"""

    DefaultGripMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default spacing, in pixels, between the sizing grip and the edges of the System.Windows.Forms.ToolStrip.

"""

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default Input Method Editor (IME) mode supported by the control.

"""

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the spacing, in pixels, between the System.Windows.Forms.ToolStrip and the System.Windows.Forms.ToolStripContainer.

"""

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length and height, in pixels, that is specified as the default maximum size of a control.

"""

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length and height, in pixels, that is specified as the default minimum size of a control.

"""

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultShowItemToolTips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default size of the System.Windows.Forms.ToolStrip.

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    DisplayedItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the subset of items that are currently displayed on the System.Windows.Forms.ToolStrip, including items that are automatically added into the System.Windows.Forms.ToolStrip.

"""

    Dock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not relevant to this class.

Get: Dock(self: ToolStripDropDown) -> DockStyle

Set: Dock(self: ToolStripDropDown) = value
"""

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether this control should redraw its surface using a secondary buffer to reduce or prevent flicker.

"""

    DropShadowEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether a three-dimensional shadow effect appears when the System.Windows.Forms.ToolStripDropDown is displayed.

Get: DropShadowEnabled(self: ToolStripDropDown) -> bool

Set: DropShadowEnabled(self: ToolStripDropDown) = value
"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    Font = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the font of the text displayed on the System.Windows.Forms.ToolStripDropDown.

Get: Font(self: ToolStripDropDown) -> Font

Set: Font(self: ToolStripDropDown) = value
"""

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height of the font of the control.

"""

    GripDisplayStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not relevant to this class.

Get: GripDisplayStyle(self: ToolStripDropDown) -> ToolStripGripDisplayStyle

"""

    GripMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not relevant to this class.

Get: GripMargin(self: ToolStripDropDown) -> Padding

Set: GripMargin(self: ToolStripDropDown) = value
"""

    GripRectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not relevant to this class.

Get: GripRectangle(self: ToolStripDropDown) -> Rectangle

"""

    GripStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not relevant to this class.

Get: GripStyle(self: ToolStripDropDown) -> ToolStripGripStyle

Set: GripStyle(self: ToolStripDropDown) = value
"""

    HScroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the horizontal scroll bar is visible.

"""

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the IME mode of a control.

"""

    IsAutoGenerated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this System.Windows.Forms.ToolStripDropDown was automatically generated.

Get: IsAutoGenerated(self: ToolStripDropDown) -> bool

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not relevant to this class.

Get: Location(self: ToolStripDropDown) -> Point

Set: Location(self: ToolStripDropDown) = value
"""

    MaxItemSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum height and width, in pixels, of the System.Windows.Forms.ToolStripDropDown.

"""

    Opacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the opacity of the form.

Get: Opacity(self: ToolStripDropDown) -> float

Set: Opacity(self: ToolStripDropDown) = value
"""

    OverflowButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not relevant to this class.

Get: OverflowButton(self: ToolStripDropDown) -> ToolStripOverflowButton

"""

    OwnerItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Forms.ToolStripItem that is the owner of this System.Windows.Forms.ToolStripDropDown.

Get: OwnerItem(self: ToolStripDropDown) -> ToolStripItem

Set: OwnerItem(self: ToolStripDropDown) = value
"""

    Region = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the window region associated with the System.Windows.Forms.ToolStripDropDown.

Get: Region(self: ToolStripDropDown) -> Region

Set: Region(self: ToolStripDropDown) = value
"""

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is now obsolete.

"""

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the control redraws itself when resized.

"""

    RightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightToLeft(self: ToolStripDropDown) -> RightToLeft

Set: RightToLeft(self: ToolStripDropDown) = value
"""

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that determines the scaling of child controls.

"""

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the control should display focus rectangles.

"""

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the user interface is in the appropriate state to show or hide keyboard accelerators.

"""

    Stretch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not relevant to this class.

Get: Stretch(self: ToolStripDropDown) -> bool

Set: Stretch(self: ToolStripDropDown) = value
"""

    TabIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not relevant to this class.

Get: TabIndex(self: ToolStripDropDown) -> int

Set: TabIndex(self: ToolStripDropDown) = value
"""

    TextDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the direction in which to draw the text on the item.

Get: TextDirection(self: ToolStripDropDown) -> ToolStripTextDirection

Set: TextDirection(self: ToolStripDropDown) = value
"""

    TopLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the System.Windows.Forms.ToolStripDropDown is a top-level control.

Get: TopLevel(self: ToolStripDropDown) -> bool

Set: TopLevel(self: ToolStripDropDown) = value
"""

    TopMost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the form should be displayed as a topmost form.

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the System.Windows.Forms.ToolStripDropDown is visible or hidden.

Get: Visible(self: ToolStripDropDown) -> bool

Set: Visible(self: ToolStripDropDown) = value
"""

    VScroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the vertical scroll bar is visible.

"""


    BackgroundImageChanged = None
    BackgroundImageLayoutChanged = None
    BindingContextChanged = None
    ChangeUICues = None
    Closed = None
    Closing = None
    ContextMenuChanged = None
    ContextMenuStripChanged = None
    DockChanged = None
    Enter = None
    FontChanged = None
    ForeColorChanged = None
    GiveFeedback = None
    HelpRequested = None
    ImeModeChanged = None
    KeyDown = None
    KeyPress = None
    KeyUp = None
    Leave = None
    Opened = None
    Opening = None
    RegionChanged = None
    Scroll = None
    StyleChanged = None
    TabIndexChanged = None
    TabStopChanged = None
    TextChanged = None
    ToolStripDropDownAccessibleObject = None
    Validated = None
    Validating = None

