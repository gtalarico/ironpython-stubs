# encoding: utf-8
# module System.Windows.Forms.Design calls itself Design
# from System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ComponentEditorForm(Form, IComponent, IDisposable, IOleControl, IOleObject, IOleInPlaceObject, IOleInPlaceActiveObject, IOleWindow, IViewObject, IViewObject2, IPersist, IPersistStreamInit, IPersistPropertyBag, IPersistStorage, IQuickActivate, ISupportOleDropSource, IDropTarget, ISynchronizeInvoke, IWin32Window, IArrangedElement, IBindableComponent, IContainerControl):
    """
    Provides a user interface for a System.Windows.Forms.Design.WindowsFormsComponentEditor.
    
    ComponentEditorForm(component: object, pageTypes: Array[Type])
    """
    def AccessibilityNotifyClients(self, *args): #cannot find CLR method
        """
        AccessibilityNotifyClients(self: Control, accEvent: AccessibleEvents, objectID: int, childID: int)
            Notifies the accessibility client applications of the specified 
             System.Windows.Forms.AccessibleEvents for the specified child control .
        
        
            accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications of.
            objectID: The identifier of the System.Windows.Forms.AccessibleObject.
            childID: The child System.Windows.Forms.Control to notify of the accessible event.
        AccessibilityNotifyClients(self: Control, accEvent: AccessibleEvents, childID: int)
            Notifies the accessibility client applications of the specified 
             System.Windows.Forms.AccessibleEvents for the specified child control.
        
        
            accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications of.
            childID: The child System.Windows.Forms.Control to notify of the accessible event.
        """
        pass

    def ActivateMdiChild(self, *args): #cannot find CLR method
        """
        ActivateMdiChild(self: Form, form: Form)
            Activates the MDI child of a form.
        
            form: The child form to activate.
        """
        pass

    def AdjustFormScrollbars(self, *args): #cannot find CLR method
        """
        AdjustFormScrollbars(self: Form, displayScrollbars: bool)
            Adjusts the scroll bars on the container based on the current control positions and the control 
             currently selected.
        
        
            displayScrollbars: true to show the scroll bars; otherwise, false.
        """
        pass

    def ApplyAutoScaling(self, *args): #cannot find CLR method
        """
        ApplyAutoScaling(self: Form)
            Resizes the form according to the current value of the 
             System.Windows.Forms.Form.AutoScaleBaseSize property and the size of the current font.
        """
        pass

    def CenterToParent(self, *args): #cannot find CLR method
        """
        CenterToParent(self: Form)
            Centers the position of the form within the bounds of the parent form.
        """
        pass

    def CenterToScreen(self, *args): #cannot find CLR method
        """
        CenterToScreen(self: Form)
            Centers the form on the current screen.
        """
        pass

    def CreateAccessibilityInstance(self, *args): #cannot find CLR method
        """
        CreateAccessibilityInstance(self: Control) -> AccessibleObject
        
            Creates a new accessibility object for the control.
            Returns: A new System.Windows.Forms.AccessibleObject for the control.
        """
        pass

    def CreateControlsInstance(self, *args): #cannot find CLR method
        """
        CreateControlsInstance(self: Form) -> ControlCollection
            Returns: A new instance of System.Windows.Forms.Control.ControlCollection assigned to the control.
        """
        pass

    def CreateHandle(self, *args): #cannot find CLR method
        """
        CreateHandle(self: Form)
            Creates the handle for the form. If a derived class overrides this function, it must call the 
             base implementation.
        """
        pass

    def DefWndProc(self, *args): #cannot find CLR method
        """
        DefWndProc(self: Form, m: Message) -> Message
        
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
        Dispose(self: Form, disposing: bool)
            Disposes of the resources (other than memory) used by the System.Windows.Forms.Form.
        
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
        
            Retrieves a value indicating how a control will behave when its 
             System.Windows.Forms.Control.AutoSize property is enabled.
        
            Returns: One of the System.Windows.Forms.AutoSizeMode values.
        """
        pass

    def GetScaledBounds(self, *args): #cannot find CLR method
        """
        GetScaledBounds(self: Form, bounds: Rectangle, factor: SizeF, specified: BoundsSpecified) -> Rectangle
        
            bounds: A System.Drawing.Rectangle that specifies the area for which to retrieve the display bounds.
            factor: The height and width of the control's bounds.
            specified: One of the values of System.Windows.Forms.BoundsSpecified that specifies the bounds of the 
             control to use when defining its size and position.
        
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
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
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
        IsInputChar(self: Control, charCode: Char) -> bool
        
            Determines if a character is an input character that the control recognizes.
        
            charCode: The character to test.
            Returns: true if the character should be sent directly to the control and not preprocessed; otherwise, 
             false.
        """
        pass

    def IsInputKey(self, *args): #cannot find CLR method
        """
        IsInputKey(self: Control, keyData: Keys) -> bool
        
            Determines whether the specified key is a regular input key or a special key that requires 
             preprocessing.
        
        
            keyData: One of the System.Windows.Forms.Keys values.
            Returns: true if the specified key is a regular input key; otherwise, false.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def NotifyInvalidate(self, *args): #cannot find CLR method
        """
        NotifyInvalidate(self: Control, invalidatedArea: Rectangle)
            Raises the System.Windows.Forms.Control.Invalidated event with a specified region of the control 
             to invalidate.
        
        
            invalidatedArea: A System.Drawing.Rectangle representing the area to invalidate.
        """
        pass

    def OnActivated(self, *args): #cannot find CLR method
        """
        OnActivated(self: ComponentEditorForm, e: EventArgs)
            Raises the System.Windows.Forms.Form.Activated event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnAutoSizeChanged(self, *args): #cannot find CLR method
        """
        OnAutoSizeChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.AutoSizeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnAutoValidateChanged(self, *args): #cannot find CLR method
        """
        OnAutoValidateChanged(self: ContainerControl, e: EventArgs)
            Raises the System.Windows.Forms.ContainerControl.AutoValidateChanged event.
        
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
        OnBackgroundImageChanged(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackgroundImageChanged event.
        
            e: An System.EventArgs that contains the data.
        """
        pass

    def OnBackgroundImageLayoutChanged(self, *args): #cannot find CLR method
        """
        OnBackgroundImageLayoutChanged(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackgroundImageLayoutChanged event.
        
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
        OnClosed(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.Closed event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def OnClosing(self, *args): #cannot find CLR method
        """
        OnClosing(self: Form, e: CancelEventArgs)
            Raises the System.Windows.Forms.Form.Closing event.
        
            e: A System.ComponentModel.CancelEventArgs that contains the event data.
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
        OnCreateControl(self: Form)
            Raises the CreateControl event.
        """
        pass

    def OnCursorChanged(self, *args): #cannot find CLR method
        """
        OnCursorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.CursorChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnDeactivate(self, *args): #cannot find CLR method
        """
        OnDeactivate(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.Deactivate event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def OnDockChanged(self, *args): #cannot find CLR method
        """
        OnDockChanged(self: Control, e: EventArgs)
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

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: Form, e: DpiChangedEventArgs) """
        pass

    def OnDpiChangedAfterParent(self, *args): #cannot find CLR method
        """ OnDpiChangedAfterParent(self: Control, e: EventArgs) """
        pass

    def OnDpiChangedBeforeParent(self, *args): #cannot find CLR method
        """ OnDpiChangedBeforeParent(self: Control, e: EventArgs) """
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
        OnEnabledChanged(self: Form, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnEnter(self, *args): #cannot find CLR method
        """
        OnEnter(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Control.Enter event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnFontChanged(self, *args): #cannot find CLR method
        """
        OnFontChanged(self: Form, e: EventArgs)
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

    def OnFormClosed(self, *args): #cannot find CLR method
        """
        OnFormClosed(self: Form, e: FormClosedEventArgs)
            Raises the System.Windows.Forms.Form.FormClosed event.
        
            e: A System.Windows.Forms.FormClosedEventArgs that contains the event data.
        """
        pass

    def OnFormClosing(self, *args): #cannot find CLR method
        """
        OnFormClosing(self: Form, e: FormClosingEventArgs)
            Raises the System.Windows.Forms.Form.FormClosing event.
        
            e: A System.Windows.Forms.FormClosingEventArgs that contains the event data.
        """
        pass

    def OnGetDpiScaledSize(self, *args): #cannot find CLR method
        """ OnGetDpiScaledSize(self: Form, deviceDpiOld: int, deviceDpiNew: int, desiredSize: Size) -> (bool, Size) """
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
        OnHandleCreated(self: Form, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnHandleDestroyed(self, *args): #cannot find CLR method
        """
        OnHandleDestroyed(self: Form, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnHelpButtonClicked(self, *args): #cannot find CLR method
        """
        OnHelpButtonClicked(self: Form, e: CancelEventArgs)
            Raises the System.Windows.Forms.Form.HelpButtonClicked event.
        
            e: A System.ComponentModel.CancelEventArgs that contains the event data.
        """
        pass

    def OnHelpRequested(self, *args): #cannot find CLR method
        """
        OnHelpRequested(self: ComponentEditorForm, e: HelpEventArgs)
            Raises the System.Windows.Forms.Control.HelpRequested event.
        
            e: A System.Windows.Forms.HelpEventArgs that contains the event data.
        """
        pass

    def OnImeModeChanged(self, *args): #cannot find CLR method
        """
        OnImeModeChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ImeModeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnInputLanguageChanged(self, *args): #cannot find CLR method
        """
        OnInputLanguageChanged(self: Form, e: InputLanguageChangedEventArgs)
            Raises the System.Windows.Forms.Form.InputLanguageChanged event.
        
            e: The System.Windows.Forms.InputLanguageChangedEventArgs that contains the event data.
        """
        pass

    def OnInputLanguageChanging(self, *args): #cannot find CLR method
        """
        OnInputLanguageChanging(self: Form, e: InputLanguageChangingEventArgs)
            Raises the System.Windows.Forms.Form.InputLanguageChanging event.
        
            e: The System.Windows.Forms.InputLanguageChangingEventArgs that contains the event data.
        """
        pass

    def OnInvalidated(self, *args): #cannot find CLR method
        """
        OnInvalidated(self: Control, e: InvalidateEventArgs)
            Raises the System.Windows.Forms.Control.Invalidated event.
        
            e: An System.Windows.Forms.InvalidateEventArgs that contains the event data.
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
        OnLayout(self: Form, levent: LayoutEventArgs)
            Raises the System.Windows.Forms.Control.Layout event.
        
            levent: The event data.
        """
        pass

    def OnLeave(self, *args): #cannot find CLR method
        """
        OnLeave(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.Leave event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnLoad(self, *args): #cannot find CLR method
        """
        OnLoad(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.Load event.
        
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
        OnLostFocus(self: Control, e: EventArgs)
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

    def OnMaximizedBoundsChanged(self, *args): #cannot find CLR method
        """
        OnMaximizedBoundsChanged(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.MaximizedBoundsChanged event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def OnMaximumSizeChanged(self, *args): #cannot find CLR method
        """
        OnMaximumSizeChanged(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.MaximumSizeChanged event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def OnMdiChildActivate(self, *args): #cannot find CLR method
        """
        OnMdiChildActivate(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.MdiChildActivate event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def OnMenuComplete(self, *args): #cannot find CLR method
        """
        OnMenuComplete(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.MenuComplete event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def OnMenuStart(self, *args): #cannot find CLR method
        """
        OnMenuStart(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.MenuStart event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def OnMinimumSizeChanged(self, *args): #cannot find CLR method
        """
        OnMinimumSizeChanged(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.MinimumSizeChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseCaptureChanged(self, *args): #cannot find CLR method
        """
        OnMouseCaptureChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseCaptureChanged event.
        
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
        OnMouseDown(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseDown event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
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
        OnMouseLeave(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseLeave event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseMove event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseUp event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
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

    def OnPaddingChanged(self, *args): #cannot find CLR method
        """
        OnPaddingChanged(self: ScrollableControl, e: EventArgs)
            Raises the System.Windows.Forms.Control.PaddingChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnPaint(self, *args): #cannot find CLR method
        """
        OnPaint(self: Form, e: PaintEventArgs)
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def OnPaintBackground(self, *args): #cannot find CLR method
        """
        OnPaintBackground(self: ScrollableControl, e: PaintEventArgs)
            Paints the background of the control.
        
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def OnParentBackColorChanged(self, *args): #cannot find CLR method
        """
        OnParentBackColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackColorChanged event when the 
             System.Windows.Forms.Control.BackColor property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentBackgroundImageChanged(self, *args): #cannot find CLR method
        """
        OnParentBackgroundImageChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackgroundImageChanged event when the 
             System.Windows.Forms.Control.BackgroundImage property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentBindingContextChanged(self, *args): #cannot find CLR method
        """
        OnParentBindingContextChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BindingContextChanged event when the 
             System.Windows.Forms.Control.BindingContext property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentChanged(self, *args): #cannot find CLR method
        """
        OnParentChanged(self: ContainerControl, e: EventArgs)
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
            Raises the System.Windows.Forms.Control.EnabledChanged event when the 
             System.Windows.Forms.Control.Enabled property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentFontChanged(self, *args): #cannot find CLR method
        """
        OnParentFontChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.FontChanged event when the 
             System.Windows.Forms.Control.Font property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentForeColorChanged(self, *args): #cannot find CLR method
        """
        OnParentForeColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ForeColorChanged event when the 
             System.Windows.Forms.Control.ForeColor property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentRightToLeftChanged(self, *args): #cannot find CLR method
        """
        OnParentRightToLeftChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.RightToLeftChanged event when the 
             System.Windows.Forms.Control.RightToLeft property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentVisibleChanged(self, *args): #cannot find CLR method
        """
        OnParentVisibleChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.VisibleChanged event when the 
             System.Windows.Forms.Control.Visible property value of the control's container changes.
        
        
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

    def OnResize(self, *args): #cannot find CLR method
        """
        OnResize(self: Form, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnResizeBegin(self, *args): #cannot find CLR method
        """
        OnResizeBegin(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.ResizeBegin event.
        
            e: A System.EventArgs that contains the event data.
        """
        pass

    def OnResizeEnd(self, *args): #cannot find CLR method
        """
        OnResizeEnd(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.ResizeEnd event.
        
            e: A System.EventArgs that contains the event data.
        """
        pass

    def OnRightToLeftChanged(self, *args): #cannot find CLR method
        """
        OnRightToLeftChanged(self: ScrollableControl, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnRightToLeftLayoutChanged(self, *args): #cannot find CLR method
        """
        OnRightToLeftLayoutChanged(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.RightToLeftLayoutChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnScroll(self, *args): #cannot find CLR method
        """
        OnScroll(self: ScrollableControl, se: ScrollEventArgs)
            Raises the System.Windows.Forms.ScrollableControl.Scroll event.
        
            se: A System.Windows.Forms.ScrollEventArgs that contains the event data.
        """
        pass

    def OnSelChangeSelector(self, *args): #cannot find CLR method
        """
        OnSelChangeSelector(self: ComponentEditorForm, source: object, e: TreeViewEventArgs)
            Switches between component editor pages.
        
            source: The source of the event.
            e: A System.Windows.Forms.TreeViewEventArgs that contains the event data.
        """
        pass

    def OnShown(self, *args): #cannot find CLR method
        """
        OnShown(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Form.Shown event.
        
            e: A System.EventArgs that contains the event data.
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
        OnStyleChanged(self: Form, e: EventArgs)
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
        OnTabStopChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.TabStopChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnTextChanged(self, *args): #cannot find CLR method
        """
        OnTextChanged(self: Form, e: EventArgs)
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
        OnVisibleChanged(self: Form, e: EventArgs)
            Raises the System.Windows.Forms.Control.VisibleChanged event.
        
            e: The System.EventArgs that contains the event data.
        """
        pass

    def PreProcessMessage(self, msg):
        """
        PreProcessMessage(self: ComponentEditorForm, msg: Message) -> (bool, Message)
        
            Provides a method to override in order to preprocess input messages before they are dispatched.
        
            msg: A System.Windows.Forms.Message that specifies the message to preprocess.
            Returns: true if the specified message is for a component editor page; otherwise, false.
        """
        pass

    def ProcessCmdKey(self, *args): #cannot find CLR method
        """
        ProcessCmdKey(self: Form, msg: Message, keyData: Keys) -> (bool, Message)
        
            Processes a command key.
        
            msg: A System.Windows.Forms.Message, passed by reference, that represents the Win32 message to 
             process.
        
            keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
            Returns: true if the keystroke was processed and consumed by the control; otherwise, false to allow 
             further processing.
        """
        pass

    def ProcessDialogChar(self, *args): #cannot find CLR method
        """
        ProcessDialogChar(self: Form, charCode: Char) -> bool
        
            Processes a dialog character.
        
            charCode: The character to process.
            Returns: true if the character was processed by the control; otherwise, false.
        """
        pass

    def ProcessDialogKey(self, *args): #cannot find CLR method
        """
        ProcessDialogKey(self: Form, keyData: Keys) -> bool
        
            Processes a dialog box key.
        
            keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
            Returns: true if the keystroke was processed and consumed by the control; otherwise, false to allow 
             further processing.
        """
        pass

    def ProcessKeyEventArgs(self, *args): #cannot find CLR method
        """
        ProcessKeyEventArgs(self: Control, m: Message) -> (bool, Message)
        
            Processes a key message and generates the appropriate control events.
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to 
             process.
        
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessKeyMessage(self, *args): #cannot find CLR method
        """
        ProcessKeyMessage(self: Control, m: Message) -> (bool, Message)
        
            Processes a keyboard message.
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to 
             process.
        
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessKeyPreview(self, *args): #cannot find CLR method
        """
        ProcessKeyPreview(self: Form, m: Message) -> (bool, Message)
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to 
             process.
        
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessMnemonic(self, *args): #cannot find CLR method
        """
        ProcessMnemonic(self: Form, charCode: Char) -> bool
        
            Processes a mnemonic character.
        
            charCode: The character to process.
            Returns: true if the character was processed as a mnemonic by the control; otherwise, false.
        """
        pass

    def ProcessTabKey(self, *args): #cannot find CLR method
        """
        ProcessTabKey(self: Form, forward: bool) -> bool
        
            forward: true to cycle forward through the controls in the System.Windows.Forms.ContainerControl; 
             otherwise, false.
        
            Returns: true if a control is selected; otherwise, false.
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

    def RescaleConstantsForDpi(self, *args): #cannot find CLR method
        """ RescaleConstantsForDpi(self: Control, deviceDpiOld: int, deviceDpiNew: int) """
        pass

    def ResetMouseEventArgs(self, *args): #cannot find CLR method
        """
        ResetMouseEventArgs(self: Control)
            Resets the control to handle the System.Windows.Forms.Control.MouseLeave event.
        """
        pass

    def RtlTranslateAlignment(self, *args): #cannot find CLR method
        """
        RtlTranslateAlignment(self: Control, align: ContentAlignment) -> ContentAlignment
        
            Converts the specified System.Drawing.ContentAlignment to the appropriate 
             System.Drawing.ContentAlignment to support right-to-left text.
        
        
            align: One of the System.Drawing.ContentAlignment values.
            Returns: One of the System.Drawing.ContentAlignment values.
        RtlTranslateAlignment(self: Control, align: LeftRightAlignment) -> LeftRightAlignment
        
            Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate 
             System.Windows.Forms.LeftRightAlignment to support right-to-left text.
        
        
            align: One of the System.Windows.Forms.LeftRightAlignment values.
            Returns: One of the System.Windows.Forms.LeftRightAlignment values.
        RtlTranslateAlignment(self: Control, align: HorizontalAlignment) -> HorizontalAlignment
        
            Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate 
             System.Windows.Forms.HorizontalAlignment to support right-to-left text.
        
        
            align: One of the System.Windows.Forms.HorizontalAlignment values.
            Returns: One of the System.Windows.Forms.HorizontalAlignment values.
        """
        pass

    def RtlTranslateContent(self, *args): #cannot find CLR method
        """
        RtlTranslateContent(self: Control, align: ContentAlignment) -> ContentAlignment
        
            Converts the specified System.Drawing.ContentAlignment to the appropriate 
             System.Drawing.ContentAlignment to support right-to-left text.
        
        
            align: One of the System.Drawing.ContentAlignment values.
            Returns: One of the System.Drawing.ContentAlignment values.
        """
        pass

    def RtlTranslateHorizontal(self, *args): #cannot find CLR method
        """
        RtlTranslateHorizontal(self: Control, align: HorizontalAlignment) -> HorizontalAlignment
        
            Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate 
             System.Windows.Forms.HorizontalAlignment to support right-to-left text.
        
        
            align: One of the System.Windows.Forms.HorizontalAlignment values.
            Returns: One of the System.Windows.Forms.HorizontalAlignment values.
        """
        pass

    def RtlTranslateLeftRight(self, *args): #cannot find CLR method
        """
        RtlTranslateLeftRight(self: Control, align: LeftRightAlignment) -> LeftRightAlignment
        
            Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate 
             System.Windows.Forms.LeftRightAlignment to support right-to-left text.
        
        
            align: One of the System.Windows.Forms.LeftRightAlignment values.
            Returns: One of the System.Windows.Forms.LeftRightAlignment values.
        """
        pass

    def ScaleControl(self, *args): #cannot find CLR method
        """
        ScaleControl(self: Form, factor: SizeF, specified: BoundsSpecified)
            Scales the location, size, padding, and margin of a control.
        
            factor: The factor by which the height and width of the control are scaled.
            specified: A System.Windows.Forms.BoundsSpecified value that specifies the bounds of the control to use 
             when defining its size and position.
        """
        pass

    def ScaleCore(self, *args): #cannot find CLR method
        """
        ScaleCore(self: Form, x: Single, y: Single)
            Performs scaling of the form.
        
            x: Percentage to scale the form horizontally
            y: Percentage to scale the form vertically
        """
        pass

    def ScrollToControl(self, *args): #cannot find CLR method
        """
        ScrollToControl(self: ScrollableControl, activeControl: Control) -> Point
        
            Calculates the scroll offset to the specified child control.
        
            activeControl: The child control to scroll into view.
            Returns: The upper-left hand System.Drawing.Point of the display area relative to the client area 
             required to scroll the control into view.
        """
        pass

    def Select(self):
        """
        Select(self: Form, directed: bool, forward: bool)
            Selects this form, and optionally selects the next or previous control.
        
            directed: If set to true that the active control is changed
            forward: If directed is true, then this controls the direction in which focus is moved. If this is true, 
             then the next control is selected; otherwise, the previous control is selected.
        """
        pass

    def SetAutoSizeMode(self, *args): #cannot find CLR method
        """
        SetAutoSizeMode(self: Control, mode: AutoSizeMode)
            Sets a value indicating how a control will behave when its System.Windows.Forms.Control.AutoSize 
             property is enabled.
        
        
            mode: One of the System.Windows.Forms.AutoSizeMode values.
        """
        pass

    def SetBoundsCore(self, *args): #cannot find CLR method
        """
        SetBoundsCore(self: Form, x: int, y: int, width: int, height: int, specified: BoundsSpecified)
            x: The x-coordinate.
            y: The y-coordinate.
            width: The bounds width.
            height: The bounds height.
            specified: A value from the BoundsSpecified enumeration.
        """
        pass

    def SetClientSizeCore(self, *args): #cannot find CLR method
        """
        SetClientSizeCore(self: Form, x: int, y: int)
            Sets the client size of the form. This will adjust the bounds of the form to make the client 
             size the requested size.
        
        
            x: Requested width of the client region.
            y: Requested height of the client region.
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
        SetVisibleCore(self: Form, value: bool)
            value: true to make the control visible; otherwise, false.
        """
        pass

    def ShowForm(self, *__args):
        """
        ShowForm(self: ComponentEditorForm, owner: IWin32Window) -> DialogResult
        
            Shows the form with the specified owner.
        
            owner: The System.Windows.Forms.IWin32Window to own the dialog.
            Returns: One of the System.Windows.Forms.DialogResult values indicating the result code returned from the 
             dialog box.
        
        ShowForm(self: ComponentEditorForm, owner: IWin32Window, page: int) -> DialogResult
        
            Shows the form and the specified page with the specified owner.
        
            owner: The System.Windows.Forms.IWin32Window to own the dialog.
            page: The index of the page to show.
            Returns: One of the System.Windows.Forms.DialogResult values indicating the result code returned from the 
             dialog box.
        
        ShowForm(self: ComponentEditorForm) -> DialogResult
        
            Shows the form. The form will have no owner window.
            Returns: One of the System.Windows.Forms.DialogResult values indicating the result code returned from the 
             dialog box.
        
        ShowForm(self: ComponentEditorForm, page: int) -> DialogResult
        
            Shows the specified page of the specified form. The form will have no owner window.
        
            page: The index of the page to show.
            Returns: One of the System.Windows.Forms.DialogResult values indicating the result code returned from the 
             dialog box.
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

    def UpdateDefaultButton(self, *args): #cannot find CLR method
        """
        UpdateDefaultButton(self: Form)
            Updates which button is the default button.
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
        WndProc(self: Form, m: Message) -> Message
        
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

    @staticmethod # known case of __new__
    def __new__(self, component, pageTypes):
        """ __new__(cls: type, component: object, pageTypes: Array[Type]) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AutoScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the scaling factor between the current and design-time automatic scaling dimensions.

"""

    AutoSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSize(self: ComponentEditorForm) -> bool

Set: AutoSize(self: ComponentEditorForm) = value
"""

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value, to enable IME support.

"""

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if events can be raised on the control.

"""

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default cursor for the control.

"""

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default Input Method Editor (IME) mode supported by the control.

"""

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the space, in pixels, that is specified by default between controls.

"""

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length and height, in pixels, that is specified as the default maximum size of a control.

"""

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length and height, in pixels, that is specified as the default minimum size of a control.

"""

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the internal spacing, in pixels, of the contents of a control.

"""

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether this control should redraw its surface using a secondary buffer to reduce or prevent flicker.

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height of the font of the control.

"""

    HScroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the horizontal scroll bar is visible.

"""

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the IME mode of a control.

"""

    MaximizedBounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets the size of the form when it is maximized.

"""

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is now obsolete.

"""

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the control redraws itself when resized.

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

    ShowWithoutActivation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the window will be activated when it is shown.

"""

    VScroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the vertical scroll bar is visible.

"""


    AutoSizeChanged = None


class ComponentEditorPage(Panel, IComponent, IDisposable, IOleControl, IOleObject, IOleInPlaceObject, IOleInPlaceActiveObject, IOleWindow, IViewObject, IViewObject2, IPersist, IPersistStreamInit, IPersistPropertyBag, IPersistStorage, IQuickActivate, ISupportOleDropSource, IDropTarget, ISynchronizeInvoke, IWin32Window, IArrangedElement, IBindableComponent):
    """
    Provides a base implementation for a System.Windows.Forms.Design.ComponentEditorPage.
    
    ComponentEditorPage()
    """
    def AccessibilityNotifyClients(self, *args): #cannot find CLR method
        """
        AccessibilityNotifyClients(self: Control, accEvent: AccessibleEvents, objectID: int, childID: int)
            Notifies the accessibility client applications of the specified 
             System.Windows.Forms.AccessibleEvents for the specified child control .
        
        
            accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications of.
            objectID: The identifier of the System.Windows.Forms.AccessibleObject.
            childID: The child System.Windows.Forms.Control to notify of the accessible event.
        AccessibilityNotifyClients(self: Control, accEvent: AccessibleEvents, childID: int)
            Notifies the accessibility client applications of the specified 
             System.Windows.Forms.AccessibleEvents for the specified child control.
        
        
            accEvent: The System.Windows.Forms.AccessibleEvents to notify the accessibility client applications of.
            childID: The child System.Windows.Forms.Control to notify of the accessible event.
        """
        pass

    def Activate(self):
        """
        Activate(self: ComponentEditorPage)
            Activates and displays the page.
        """
        pass

    def AdjustFormScrollbars(self, *args): #cannot find CLR method
        """
        AdjustFormScrollbars(self: ScrollableControl, displayScrollbars: bool)
            Adjusts the scroll bars on the container based on the current control positions and the control 
             currently selected.
        
        
            displayScrollbars: true to show the scroll bars; otherwise, false.
        """
        pass

    def ApplyChanges(self):
        """
        ApplyChanges(self: ComponentEditorPage)
            Applies changes to all the components being edited.
        """
        pass

    def CreateAccessibilityInstance(self, *args): #cannot find CLR method
        """
        CreateAccessibilityInstance(self: Control) -> AccessibleObject
        
            Creates a new accessibility object for the control.
            Returns: A new System.Windows.Forms.AccessibleObject for the control.
        """
        pass

    def CreateControlsInstance(self, *args): #cannot find CLR method
        """
        CreateControlsInstance(self: Control) -> ControlCollection
        
            Creates a new instance of the control collection for the control.
            Returns: A new instance of System.Windows.Forms.Control.ControlCollection assigned to the control.
        """
        pass

    def CreateHandle(self, *args): #cannot find CLR method
        """
        CreateHandle(self: Control)
            Creates a handle for the control.
        """
        pass

    def Deactivate(self):
        """
        Deactivate(self: ComponentEditorPage)
            Deactivates and hides the page.
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
        Dispose(self: Control, disposing: bool)
            Releases the unmanaged resources used by the System.Windows.Forms.Control and its child controls 
             and optionally releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def EnterLoadingMode(self, *args): #cannot find CLR method
        """
        EnterLoadingMode(self: ComponentEditorPage)
            Increments the loading counter.
        """
        pass

    def ExitLoadingMode(self, *args): #cannot find CLR method
        """
        ExitLoadingMode(self: ComponentEditorPage)
            Decrements the loading counter.
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
        
            Retrieves a value indicating how a control will behave when its 
             System.Windows.Forms.Control.AutoSize property is enabled.
        
            Returns: One of the System.Windows.Forms.AutoSizeMode values.
        """
        pass

    def GetControl(self):
        """
        GetControl(self: ComponentEditorPage) -> Control
        
            Gets the control that represents the window for this page.
            Returns: The System.Windows.Forms.Control that represents the window for this page.
        """
        pass

    def GetScaledBounds(self, *args): #cannot find CLR method
        """
        GetScaledBounds(self: Control, bounds: Rectangle, factor: SizeF, specified: BoundsSpecified) -> Rectangle
        
            Retrieves the bounds within which the control is scaled.
        
            bounds: A System.Drawing.Rectangle that specifies the area for which to retrieve the display bounds.
            factor: The height and width of the control's bounds.
            specified: One of the values of System.Windows.Forms.BoundsSpecified that specifies the bounds of the 
             control to use when defining its size and position.
        
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

    def GetSelectedComponent(self, *args): #cannot find CLR method
        """
        GetSelectedComponent(self: ComponentEditorPage) -> IComponent
        
            Gets the component that is to be edited.
            Returns: The System.ComponentModel.IComponent that is to be edited.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
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

    def IsFirstActivate(self, *args): #cannot find CLR method
        """
        IsFirstActivate(self: ComponentEditorPage) -> bool
        
            Gets a value indicating whether the page is being activated for the first time.
            Returns: true if this is the first time the page is being activated; otherwise, false.
        """
        pass

    def IsInputChar(self, *args): #cannot find CLR method
        """
        IsInputChar(self: Control, charCode: Char) -> bool
        
            Determines if a character is an input character that the control recognizes.
        
            charCode: The character to test.
            Returns: true if the character should be sent directly to the control and not preprocessed; otherwise, 
             false.
        """
        pass

    def IsInputKey(self, *args): #cannot find CLR method
        """
        IsInputKey(self: Control, keyData: Keys) -> bool
        
            Determines whether the specified key is a regular input key or a special key that requires 
             preprocessing.
        
        
            keyData: One of the System.Windows.Forms.Keys values.
            Returns: true if the specified key is a regular input key; otherwise, false.
        """
        pass

    def IsLoading(self, *args): #cannot find CLR method
        """
        IsLoading(self: ComponentEditorPage) -> bool
        
            Gets a value indicating whether the page is being loaded.
            Returns: true if the page is being loaded; otherwise, false.
        """
        pass

    def IsPageMessage(self, msg):
        """
        IsPageMessage(self: ComponentEditorPage, msg: Message) -> (bool, Message)
        
            Processes messages that could be handled by the page.
        
            msg: The message to process.
            Returns: true if the page processed the message; otherwise, false.
        """
        pass

    def LoadComponent(self, *args): #cannot find CLR method
        """
        LoadComponent(self: ComponentEditorPage)
            Loads the component into the page user interface (UI).
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def NotifyInvalidate(self, *args): #cannot find CLR method
        """
        NotifyInvalidate(self: Control, invalidatedArea: Rectangle)
            Raises the System.Windows.Forms.Control.Invalidated event with a specified region of the control 
             to invalidate.
        
        
            invalidatedArea: A System.Drawing.Rectangle representing the area to invalidate.
        """
        pass

    def OnApplyComplete(self):
        """
        OnApplyComplete(self: ComponentEditorPage)
            Called when the page and any sibling pages have applied their changes.
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
        OnDockChanged(self: Control, e: EventArgs)
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

    def OnDpiChangedAfterParent(self, *args): #cannot find CLR method
        """ OnDpiChangedAfterParent(self: Control, e: EventArgs) """
        pass

    def OnDpiChangedBeforeParent(self, *args): #cannot find CLR method
        """ OnDpiChangedBeforeParent(self: Control, e: EventArgs) """
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
        OnEnabledChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.EnabledChanged event.
        
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
        OnFontChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.FontChanged event.
        
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
        OnHandleCreated(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.HandleCreated event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnHandleDestroyed(self, *args): #cannot find CLR method
        """
        OnHandleDestroyed(self: Control, e: EventArgs)
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
        OnInvalidated(self: Control, e: InvalidateEventArgs)
            Raises the System.Windows.Forms.Control.Invalidated event.
        
            e: An System.Windows.Forms.InvalidateEventArgs that contains the event data.
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
        OnLayout(self: ScrollableControl, levent: LayoutEventArgs)
            levent: A System.Windows.Forms.LayoutEventArgs that contains the event data.
        """
        pass

    def OnLeave(self, *args): #cannot find CLR method
        """
        OnLeave(self: Control, e: EventArgs)
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
        OnLostFocus(self: Control, e: EventArgs)
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
        OnMouseCaptureChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseCaptureChanged event.
        
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
        OnMouseDown(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseDown event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
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
        OnMouseLeave(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.MouseLeave event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseMove event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: Control, e: MouseEventArgs)
            Raises the System.Windows.Forms.Control.MouseUp event.
        
            e: A System.Windows.Forms.MouseEventArgs that contains the event data.
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

    def OnPaddingChanged(self, *args): #cannot find CLR method
        """
        OnPaddingChanged(self: ScrollableControl, e: EventArgs)
            Raises the System.Windows.Forms.Control.PaddingChanged event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnPaint(self, *args): #cannot find CLR method
        """
        OnPaint(self: Control, e: PaintEventArgs)
            Raises the System.Windows.Forms.Control.Paint event.
        
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def OnPaintBackground(self, *args): #cannot find CLR method
        """
        OnPaintBackground(self: ScrollableControl, e: PaintEventArgs)
            Paints the background of the control.
        
            e: A System.Windows.Forms.PaintEventArgs that contains the event data.
        """
        pass

    def OnParentBackColorChanged(self, *args): #cannot find CLR method
        """
        OnParentBackColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackColorChanged event when the 
             System.Windows.Forms.Control.BackColor property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentBackgroundImageChanged(self, *args): #cannot find CLR method
        """
        OnParentBackgroundImageChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BackgroundImageChanged event when the 
             System.Windows.Forms.Control.BackgroundImage property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentBindingContextChanged(self, *args): #cannot find CLR method
        """
        OnParentBindingContextChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.BindingContextChanged event when the 
             System.Windows.Forms.Control.BindingContext property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentChanged(self, *args): #cannot find CLR method
        """
        OnParentChanged(self: Control, e: EventArgs)
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
            Raises the System.Windows.Forms.Control.EnabledChanged event when the 
             System.Windows.Forms.Control.Enabled property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentFontChanged(self, *args): #cannot find CLR method
        """
        OnParentFontChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.FontChanged event when the 
             System.Windows.Forms.Control.Font property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentForeColorChanged(self, *args): #cannot find CLR method
        """
        OnParentForeColorChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.ForeColorChanged event when the 
             System.Windows.Forms.Control.ForeColor property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentRightToLeftChanged(self, *args): #cannot find CLR method
        """
        OnParentRightToLeftChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.RightToLeftChanged event when the 
             System.Windows.Forms.Control.RightToLeft property value of the control's container changes.
        
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnParentVisibleChanged(self, *args): #cannot find CLR method
        """
        OnParentVisibleChanged(self: Control, e: EventArgs)
            Raises the System.Windows.Forms.Control.VisibleChanged event when the 
             System.Windows.Forms.Control.Visible property value of the control's container changes.
        
        
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

    def OnResize(self, *args): #cannot find CLR method
        """
        OnResize(self: Panel, eventargs: EventArgs)
            Fires the event indicating that the panel has been resized. Inheriting controls should use this 
             in favor of actually listening to the event, but should still call base.onResize to ensure that 
             the event is fired for external listeners.
        
        
            eventargs: An System.EventArgs that contains the event data.
        """
        pass

    def OnRightToLeftChanged(self, *args): #cannot find CLR method
        """
        OnRightToLeftChanged(self: ScrollableControl, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnScroll(self, *args): #cannot find CLR method
        """
        OnScroll(self: ScrollableControl, se: ScrollEventArgs)
            Raises the System.Windows.Forms.ScrollableControl.Scroll event.
        
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
        OnTabStopChanged(self: Control, e: EventArgs)
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
        OnVisibleChanged(self: ScrollableControl, e: EventArgs)
            e: An System.EventArgs that contains the event data.
        """
        pass

    def ProcessCmdKey(self, *args): #cannot find CLR method
        """
        ProcessCmdKey(self: Control, msg: Message, keyData: Keys) -> (bool, Message)
        
            Processes a command key.
        
            msg: A System.Windows.Forms.Message, passed by reference, that represents the window message to 
             process.
        
            keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
            Returns: true if the character was processed by the control; otherwise, false.
        """
        pass

    def ProcessDialogChar(self, *args): #cannot find CLR method
        """
        ProcessDialogChar(self: Control, charCode: Char) -> bool
        
            Processes a dialog character.
        
            charCode: The character to process.
            Returns: true if the character was processed by the control; otherwise, false.
        """
        pass

    def ProcessDialogKey(self, *args): #cannot find CLR method
        """
        ProcessDialogKey(self: Control, keyData: Keys) -> bool
        
            Processes a dialog key.
        
            keyData: One of the System.Windows.Forms.Keys values that represents the key to process.
            Returns: true if the key was processed by the control; otherwise, false.
        """
        pass

    def ProcessKeyEventArgs(self, *args): #cannot find CLR method
        """
        ProcessKeyEventArgs(self: Control, m: Message) -> (bool, Message)
        
            Processes a key message and generates the appropriate control events.
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to 
             process.
        
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessKeyMessage(self, *args): #cannot find CLR method
        """
        ProcessKeyMessage(self: Control, m: Message) -> (bool, Message)
        
            Processes a keyboard message.
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to 
             process.
        
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessKeyPreview(self, *args): #cannot find CLR method
        """
        ProcessKeyPreview(self: Control, m: Message) -> (bool, Message)
        
            Previews a keyboard message.
        
            m: A System.Windows.Forms.Message, passed by reference, that represents the window message to 
             process.
        
            Returns: true if the message was processed by the control; otherwise, false.
        """
        pass

    def ProcessMnemonic(self, *args): #cannot find CLR method
        """
        ProcessMnemonic(self: Control, charCode: Char) -> bool
        
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

    def ReloadComponent(self, *args): #cannot find CLR method
        """
        ReloadComponent(self: ComponentEditorPage)
            Reloads the component for the page.
        """
        pass

    def RescaleConstantsForDpi(self, *args): #cannot find CLR method
        """ RescaleConstantsForDpi(self: Control, deviceDpiOld: int, deviceDpiNew: int) """
        pass

    def ResetMouseEventArgs(self, *args): #cannot find CLR method
        """
        ResetMouseEventArgs(self: Control)
            Resets the control to handle the System.Windows.Forms.Control.MouseLeave event.
        """
        pass

    def RtlTranslateAlignment(self, *args): #cannot find CLR method
        """
        RtlTranslateAlignment(self: Control, align: ContentAlignment) -> ContentAlignment
        
            Converts the specified System.Drawing.ContentAlignment to the appropriate 
             System.Drawing.ContentAlignment to support right-to-left text.
        
        
            align: One of the System.Drawing.ContentAlignment values.
            Returns: One of the System.Drawing.ContentAlignment values.
        RtlTranslateAlignment(self: Control, align: LeftRightAlignment) -> LeftRightAlignment
        
            Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate 
             System.Windows.Forms.LeftRightAlignment to support right-to-left text.
        
        
            align: One of the System.Windows.Forms.LeftRightAlignment values.
            Returns: One of the System.Windows.Forms.LeftRightAlignment values.
        RtlTranslateAlignment(self: Control, align: HorizontalAlignment) -> HorizontalAlignment
        
            Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate 
             System.Windows.Forms.HorizontalAlignment to support right-to-left text.
        
        
            align: One of the System.Windows.Forms.HorizontalAlignment values.
            Returns: One of the System.Windows.Forms.HorizontalAlignment values.
        """
        pass

    def RtlTranslateContent(self, *args): #cannot find CLR method
        """
        RtlTranslateContent(self: Control, align: ContentAlignment) -> ContentAlignment
        
            Converts the specified System.Drawing.ContentAlignment to the appropriate 
             System.Drawing.ContentAlignment to support right-to-left text.
        
        
            align: One of the System.Drawing.ContentAlignment values.
            Returns: One of the System.Drawing.ContentAlignment values.
        """
        pass

    def RtlTranslateHorizontal(self, *args): #cannot find CLR method
        """
        RtlTranslateHorizontal(self: Control, align: HorizontalAlignment) -> HorizontalAlignment
        
            Converts the specified System.Windows.Forms.HorizontalAlignment to the appropriate 
             System.Windows.Forms.HorizontalAlignment to support right-to-left text.
        
        
            align: One of the System.Windows.Forms.HorizontalAlignment values.
            Returns: One of the System.Windows.Forms.HorizontalAlignment values.
        """
        pass

    def RtlTranslateLeftRight(self, *args): #cannot find CLR method
        """
        RtlTranslateLeftRight(self: Control, align: LeftRightAlignment) -> LeftRightAlignment
        
            Converts the specified System.Windows.Forms.LeftRightAlignment to the appropriate 
             System.Windows.Forms.LeftRightAlignment to support right-to-left text.
        
        
            align: One of the System.Windows.Forms.LeftRightAlignment values.
            Returns: One of the System.Windows.Forms.LeftRightAlignment values.
        """
        pass

    def SaveComponent(self, *args): #cannot find CLR method
        """
        SaveComponent(self: ComponentEditorPage)
            Saves the component from the page user interface (UI).
        """
        pass

    def ScaleControl(self, *args): #cannot find CLR method
        """
        ScaleControl(self: ScrollableControl, factor: SizeF, specified: BoundsSpecified)
            factor: The factor by which the height and width of the control will be scaled.
            specified: A System.Windows.Forms.BoundsSpecified value that specifies the bounds of the control to use 
             when defining its size and position.
        """
        pass

    def ScaleCore(self, *args): #cannot find CLR method
        """
        ScaleCore(self: ScrollableControl, dx: Single, dy: Single)
            dx: The horizontal scaling factor.
            dy: The vertical scaling factor.
        """
        pass

    def ScrollToControl(self, *args): #cannot find CLR method
        """
        ScrollToControl(self: ScrollableControl, activeControl: Control) -> Point
        
            Calculates the scroll offset to the specified child control.
        
            activeControl: The child control to scroll into view.
            Returns: The upper-left hand System.Drawing.Point of the display area relative to the client area 
             required to scroll the control into view.
        """
        pass

    def Select(self):
        """
        Select(self: Control, directed: bool, forward: bool)
            Activates a child control. Optionally specifies the direction in the tab order to select the 
             control from.
        
        
            directed: true to specify the direction of the control to select; otherwise, false.
            forward: true to move forward in the tab order; false to move backward in the tab order.
        """
        pass

    def SetAutoSizeMode(self, *args): #cannot find CLR method
        """
        SetAutoSizeMode(self: Control, mode: AutoSizeMode)
            Sets a value indicating how a control will behave when its System.Windows.Forms.Control.AutoSize 
             property is enabled.
        
        
            mode: One of the System.Windows.Forms.AutoSizeMode values.
        """
        pass

    def SetBoundsCore(self, *args): #cannot find CLR method
        """
        SetBoundsCore(self: Control, x: int, y: int, width: int, height: int, specified: BoundsSpecified)
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

    def SetComponent(self, component):
        """
        SetComponent(self: ComponentEditorPage, component: IComponent)
            Sets the component to be edited.
        
            component: The System.ComponentModel.IComponent to be edited.
        """
        pass

    def SetDirty(self, *args): #cannot find CLR method
        """
        SetDirty(self: ComponentEditorPage)
            Sets the page as changed since the last load or save.
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

    def SetScrollState(self, *args): #cannot find CLR method
        """
        SetScrollState(self: ScrollableControl, bit: int, value: bool)
            Sets the specified scroll state flag.
        
            bit: The scroll state flag to set.
            value: The value to set the flag.
        """
        pass

    def SetSite(self, site):
        """
        SetSite(self: ComponentEditorPage, site: IComponentEditorPageSite)
            Sets the site for this page.
        
            site: The site for this page.
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
        SetVisibleCore(self: Control, value: bool)
            Sets the control to the specified visible state.
        
            value: true to make the control visible; otherwise, false.
        """
        pass

    def ShowHelp(self):
        """
        ShowHelp(self: ComponentEditorPage)
            Shows Help information if the page supports Help information.
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

    def SupportsHelp(self):
        """
        SupportsHelp(self: ComponentEditorPage) -> bool
        
            Gets a value indicating whether the editor supports Help.
            Returns: true if the editor supports Help; otherwise, false. The default implementation returns false.
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
        WndProc(self: ScrollableControl, m: Message) -> Message
        
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

    AutoSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is not relevant for this class.

Get: AutoSize(self: ComponentEditorPage) -> bool

Set: AutoSize(self: ComponentEditorPage) = value
"""

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Windows.Forms.Control.ImeMode property can be set to an active value, to enable IME support.

"""

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if events can be raised on the control.

"""

    CommitOnDeactivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the editor should apply its changes before it is deactivated.

Get: CommitOnDeactivate(self: ComponentEditorPage) -> bool

Set: CommitOnDeactivate(self: ComponentEditorPage) = value
"""

    Component = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the component to edit.

"""

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the creation parameters for the control.

"""

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default cursor for the control.

"""

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default Input Method Editor (IME) mode supported by the control.

"""

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the space, in pixels, that is specified by default between controls.

"""

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length and height, in pixels, that is specified as the default maximum size of a control.

"""

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length and height, in pixels, that is specified as the default minimum size of a control.

"""

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the internal spacing, in pixels, of the contents of a control.

"""

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether this control should redraw its surface using a secondary buffer to reduce or prevent flicker.

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    FirstActivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the page is being activated for the first time.

"""

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height of the font of the control.

"""

    HScroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the horizontal scroll bar is visible.

"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the icon for the page.

Get: Icon(self: ComponentEditorPage) -> Icon

Set: Icon(self: ComponentEditorPage) = value
"""

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the IME mode of a control.

"""

    Loading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates how many load dependencies remain until loading has been completed.

"""

    LoadRequired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether a component must be loaded before editing can occur.

"""

    PageSite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the page site.

"""

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is now obsolete.

"""

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the control redraws itself when resized.

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

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the title of the page.

Get: Title(self: ComponentEditorPage) -> str

"""

    VScroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the vertical scroll bar is visible.

"""


    AutoSizeChanged = None


class PropertyTab(object, IExtenderProvider):
    """ Provides a base class for property tabs. """
    def CanExtend(self, extendee):
        """
        CanExtend(self: PropertyTab, extendee: object) -> bool
        
            Gets a value indicating whether this System.Windows.Forms.Design.PropertyTab can display 
             properties for the specified component.
        
        
            extendee: The object to test.
            Returns: true if the object can be extended; otherwise, false.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: PropertyTab)
            Releases all the resources used by the System.Windows.Forms.Design.PropertyTab.
        """
        pass

    def GetDefaultProperty(self, component):
        """
        GetDefaultProperty(self: PropertyTab, component: object) -> PropertyDescriptor
        
            Gets the default property of the specified component.
        
            component: The component to retrieve the default property of.
            Returns: A System.ComponentModel.PropertyDescriptor that represents the default property.
        """
        pass

    def GetProperties(self, *__args):
        """
        GetProperties(self: PropertyTab, context: ITypeDescriptorContext, component: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Gets the properties of the specified component that match the specified attributes and context.
        
            context: An System.ComponentModel.ITypeDescriptorContext that indicates the context to retrieve 
             properties from.
        
            component: The component to retrieve properties from.
            attributes: An array of type System.Attribute that indicates the attributes of the properties to retrieve.
            Returns: A System.ComponentModel.PropertyDescriptorCollection that contains the properties matching the 
             specified context and attributes.
        
        GetProperties(self: PropertyTab, component: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Gets the properties of the specified component that match the specified attributes.
        
            component: The component to retrieve properties from.
            attributes: An array of type System.Attribute that indicates the attributes of the properties to retrieve.
            Returns: A System.ComponentModel.PropertyDescriptorCollection that contains the properties.
        GetProperties(self: PropertyTab, component: object) -> PropertyDescriptorCollection
        
            Gets the properties of the specified component.
        
            component: The component to retrieve the properties of.
            Returns: A System.ComponentModel.PropertyDescriptorCollection that contains the properties of the 
             component.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Bitmap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the bitmap that is displayed for the System.Windows.Forms.Design.PropertyTab.

Get: Bitmap(self: PropertyTab) -> Bitmap

"""

    Components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the array of components the property tab is associated with.

Get: Components(self: PropertyTab) -> Array[object]

Set: Components(self: PropertyTab) = value
"""

    HelpKeyword = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Help keyword that is to be associated with this tab.

Get: HelpKeyword(self: PropertyTab) -> str

"""

    TabName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name for the property tab.

Get: TabName(self: PropertyTab) -> str

"""



class EventsTab(PropertyTab, IExtenderProvider):
    """
    Provides a System.Windows.Forms.Design.PropertyTab that can display events for selection and linking.
    
    EventsTab(sp: IServiceProvider)
    """
    def CanExtend(self, extendee):
        """
        CanExtend(self: EventsTab, extendee: object) -> bool
        
            Gets a value indicating whether the specified object can be extended.
        
            extendee: The object to test for extensibility.
            Returns: true if the specified object can be extended; otherwise, false.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: PropertyTab, disposing: bool)
            Releases the unmanaged resources used by the System.Windows.Forms.Design.PropertyTab and 
             optionally releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GetDefaultProperty(self, obj):
        """
        GetDefaultProperty(self: EventsTab, obj: object) -> PropertyDescriptor
        
            Gets the default property from the specified object.
        
            obj: The object to retrieve the default property of.
            Returns: A System.ComponentModel.PropertyDescriptor indicating the default property.
        """
        pass

    def GetProperties(self, *__args):
        """
        GetProperties(self: EventsTab, context: ITypeDescriptorContext, component: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Gets all the properties of the event tab that match the specified attributes and context.
        
            context: An System.ComponentModel.ITypeDescriptorContext that can be used to gain context information.
            component: The component to retrieve the properties of.
            attributes: An array of type System.Attribute that indicates the attributes of the event properties to 
             retrieve.
        
            Returns: A System.ComponentModel.PropertyDescriptorCollection that contains the properties. This will be 
             an empty System.ComponentModel.PropertyDescriptorCollection if the component does not implement 
             an event service.
        
        GetProperties(self: EventsTab, component: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Gets all the properties of the event tab that match the specified attributes.
        
            component: The component to retrieve the properties of.
            attributes: An array of System.Attribute that indicates the attributes of the event properties to retrieve.
            Returns: A System.ComponentModel.PropertyDescriptorCollection that contains the properties. This will be 
             an empty System.ComponentModel.PropertyDescriptorCollection if the component does not implement 
             an event service.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, sp):
        """ __new__(cls: type, sp: IServiceProvider) """
        pass

    HelpKeyword = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Help keyword for the tab.

Get: HelpKeyword(self: EventsTab) -> str

"""

    TabName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the tab.

Get: TabName(self: EventsTab) -> str

"""



class IUIService:
    """ Enables interaction with the user interface of the development environment object that is hosting the designer. """
    def CanShowComponentEditor(self, component):
        """
        CanShowComponentEditor(self: IUIService, component: object) -> bool
        
            Indicates whether the component can display a System.Windows.Forms.Design.ComponentEditorForm.
        
            component: The component to check for support for displaying a 
             System.Windows.Forms.Design.ComponentEditorForm.
        
            Returns: true if the specified component can display a component editor form; otherwise, false.
        """
        pass

    def GetDialogOwnerWindow(self):
        """
        GetDialogOwnerWindow(self: IUIService) -> IWin32Window
        
            Gets the window that should be used as the owner when showing dialog boxes.
            Returns: An System.Windows.Forms.IWin32Window that indicates the window to own any child dialog boxes.
        """
        pass

    def SetUIDirty(self):
        """
        SetUIDirty(self: IUIService)
            Sets a flag indicating the UI has changed.
        """
        pass

    def ShowComponentEditor(self, component, parent):
        """
        ShowComponentEditor(self: IUIService, component: object, parent: IWin32Window) -> bool
        
            Attempts to display a System.Windows.Forms.Design.ComponentEditorForm for a component.
        
            component: The component for which to display a System.Windows.Forms.Design.ComponentEditorForm.
            parent: The System.Windows.Forms.IWin32Window to parent any dialog boxes to.
            Returns: true if the attempt is successful; otherwise, false.
        """
        pass

    def ShowDialog(self, form):
        """
        ShowDialog(self: IUIService, form: Form) -> DialogResult
        
            Attempts to display the specified form in a dialog box.
        
            form: The System.Windows.Forms.Form to display.
            Returns: One of the System.Windows.Forms.DialogResult values indicating the result code returned by the 
             dialog box.
        """
        pass

    def ShowError(self, *__args):
        """
        ShowError(self: IUIService, ex: Exception, message: str)
            Displays the specified exception and information about the exception in a message box.
        
            ex: The System.Exception to display.
            message: A message to display that provides information about the exception.
        ShowError(self: IUIService, ex: Exception)
            Displays the specified exception and information about the exception in a message box.
        
            ex: The System.Exception to display.
        ShowError(self: IUIService, message: str)
            Displays the specified error message in a message box.
        
            message: The error message to display.
        """
        pass

    def ShowMessage(self, message, caption=None, buttons=None):
        """
        ShowMessage(self: IUIService, message: str, caption: str, buttons: MessageBoxButtons) -> DialogResult
        
            Displays the specified message in a message box with the specified caption and buttons to place 
             on the dialog box.
        
        
            message: The message to display.
            caption: The caption for the dialog box.
            buttons: One of the System.Windows.Forms.MessageBoxButtons values: 
             System.Windows.Forms.MessageBoxButtons.OK, System.Windows.Forms.MessageBoxButtons.OKCancel, 
             System.Windows.Forms.MessageBoxButtons.YesNo, or 
             System.Windows.Forms.MessageBoxButtons.YesNoCancel.
        
            Returns: One of the System.Windows.Forms.DialogResult values indicating the result code returned by the 
             dialog box.
        
        ShowMessage(self: IUIService, message: str, caption: str)
            Displays the specified message in a message box with the specified caption.
        
            message: The message to display.
            caption: The caption for the message box.
        ShowMessage(self: IUIService, message: str)
            Displays the specified message in a message box.
        
            message: The message to display
        """
        pass

    def ShowToolWindow(self, toolWindow):
        """
        ShowToolWindow(self: IUIService, toolWindow: Guid) -> bool
        
            Displays the specified tool window.
        
            toolWindow: A System.Guid identifier for the tool window. This can be a custom System.Guid or one of the 
             predefined values from System.ComponentModel.Design.StandardToolWindows.
        
            Returns: true if the tool window was successfully shown; false if it could not be shown or found.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Styles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of styles that are specific to the host's environment.

Get: Styles(self: IUIService) -> IDictionary

"""



class IWindowsFormsEditorService:
    """ Provides an interface for a System.Drawing.Design.UITypeEditor to display Windows Forms or to display a control in a drop-down area from a property grid control in design mode. """
    def CloseDropDown(self):
        """
        CloseDropDown(self: IWindowsFormsEditorService)
            Closes any previously opened drop down control area.
        """
        pass

    def DropDownControl(self, control):
        """
        DropDownControl(self: IWindowsFormsEditorService, control: Control)
            Displays the specified control in a drop down area below a value field of the property grid that 
             provides this service.
        
        
            control: The drop down list System.Windows.Forms.Control to open.
        """
        pass

    def ShowDialog(self, dialog):
        """
        ShowDialog(self: IWindowsFormsEditorService, dialog: Form) -> DialogResult
        
            Shows the specified System.Windows.Forms.Form.
        
            dialog: The System.Windows.Forms.Form to display.
            Returns: A System.Windows.Forms.DialogResult indicating the result code returned by the 
             System.Windows.Forms.Form.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ToolStripItemDesignerAvailability(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies controls that are visible in the designer.
    
    enum (flags) ToolStripItemDesignerAvailability, values: All (15), ContextMenuStrip (4), MenuStrip (2), None (0), StatusStrip (8), ToolStrip (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    All = None
    ContextMenuStrip = None
    MenuStrip = None
    None = None
    StatusStrip = None
    ToolStrip = None
    value__ = None


class ToolStripItemDesignerAvailabilityAttribute(Attribute, _Attribute):
    """
    Specifies which types a System.Windows.Forms.ToolStripItem can appear in. This class cannot be inherited.
    
    ToolStripItemDesignerAvailabilityAttribute()
    ToolStripItemDesignerAvailabilityAttribute(visibility: ToolStripItemDesignerAvailability)
    """
    def Equals(self, obj):
        """
        Equals(self: ToolStripItemDesignerAvailabilityAttribute, obj: object) -> bool
        
            obj: An System.Object to compare with this instance or null.
            Returns: true if obj equals the type and value of this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ToolStripItemDesignerAvailabilityAttribute) -> int
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def IsDefaultAttribute(self):
        """
        IsDefaultAttribute(self: ToolStripItemDesignerAvailabilityAttribute) -> bool
        
            When overriden in a derived class, indicates whether the value of this instance is the default 
             value for the derived class.
        
            Returns: true if this instance is the default attribute for the class; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, visibility=None):
        """
        __new__(cls: type)
        __new__(cls: type, visibility: ToolStripItemDesignerAvailability)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ItemAdditionVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visibility of a System.Windows.Forms.ToolStripItem.

Get: ItemAdditionVisibility(self: ToolStripItemDesignerAvailabilityAttribute) -> ToolStripItemDesignerAvailability

"""


    Default = None


class WindowsFormsComponentEditor(ComponentEditor):
    """ Provides a base class for editors that use a modal dialog to display a properties page similar to an ActiveX control's property page. """
    def EditComponent(self, *__args):
        """
        EditComponent(self: WindowsFormsComponentEditor, context: ITypeDescriptorContext, component: object, owner: IWin32Window) -> bool
        
            Creates an editor window that allows the user to edit the specified component.
        
            context: An System.ComponentModel.ITypeDescriptorContext that can be used to gain additional context 
             information.
        
            component: The component to edit.
            owner: An System.Windows.Forms.IWin32Window that the component belongs to.
            Returns: true if the component was changed during editing; otherwise, false.
        EditComponent(self: WindowsFormsComponentEditor, component: object, owner: IWin32Window) -> bool
        
            Creates an editor window that allows the user to edit the specified component, using the 
             specified window that owns the component.
        
        
            component: The component to edit.
            owner: An System.Windows.Forms.IWin32Window that the component belongs to.
            Returns: true if the component was changed during editing; otherwise, false.
        EditComponent(self: WindowsFormsComponentEditor, context: ITypeDescriptorContext, component: object) -> bool
        
            Creates an editor window that allows the user to edit the specified component, using the 
             specified context information.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that can be used to gain additional context 
             information.
        
            component: The component to edit.
            Returns: true if the component was changed during editing; otherwise, false.
        """
        pass

    def GetComponentEditorPages(self, *args): #cannot find CLR method
        """
        GetComponentEditorPages(self: WindowsFormsComponentEditor) -> Array[Type]
        
            Gets the component editor pages associated with the component editor.
            Returns: An array of component editor pages.
        """
        pass

    def GetInitialComponentEditorPageIndex(self, *args): #cannot find CLR method
        """
        GetInitialComponentEditorPageIndex(self: WindowsFormsComponentEditor) -> int
        
            Gets the index of the initial component editor page for the component editor to display.
            Returns: The index of the component editor page that the component editor will initially display.
        """
        pass


