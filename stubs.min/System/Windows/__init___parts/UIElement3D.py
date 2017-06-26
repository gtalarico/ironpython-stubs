class UIElement3D(Visual3D, IResource, IVisual3DContainer, IAnimatable, IInputElement):
    """ System.Windows.UIElement3D is a base class for WPF core level implementations building on Windows Presentation Foundation (WPF) elements and basic presentation characteristics. """
    def AddHandler(self, routedEvent, handler, handledEventsToo=None):
        """
        AddHandler(self: UIElement3D, routedEvent: RoutedEvent, handler: Delegate, handledEventsToo: bool)
            Adds a routed event handler for a specified routed event, adding the handler to the handler collection on the current element. Specify handledEventsToo as true to have the provided handler be invoked for 
             routed event that had already been marked as handled by another element along the event route.
        
        
            routedEvent: An identifier for the routed event to be handled.
            handler: A reference to the handler implementation.
            handledEventsToo: true to register the handler such that it is invoked even when the routed event is marked handled in its event data; false to register the handler with the default condition that it will not be invoked if 
             the routed event is already marked handled. The default is false.Do not routinely ask to rehandle a routed event. For more information, see Remarks.
        
        AddHandler(self: UIElement3D, routedEvent: RoutedEvent, handler: Delegate)
            Adds a routed event handler for a specified routed event, adding the handler to the handler collection on the current element.
        
            routedEvent: An identifier for the�routed event to be handled.
            handler: A reference to the handler implementation.
        """
        pass

    def AddToEventRoute(self, route, e):
        """
        AddToEventRoute(self: UIElement3D, route: EventRoute, e: RoutedEventArgs)
            Adds handlers to the specified System.Windows.EventRoute for the current System.Windows.UIElement3D event handler collection.
        
            route: The event route that handlers are added to.
            e: The event data that is used to add the handlers. This method uses the System.Windows.RoutedEventArgs.RoutedEvent property of the event data to create the handlers.
        """
        pass

    def AddVisual3DChild(self, *args): #cannot find CLR method
        """
        AddVisual3DChild(self: Visual3D, child: Visual3D)
            Defines the parent-child relationship between two 3-D visuals.
        
            child: The child 3-D visual object to add to the parent 3-D visual object.
        """
        pass

    def CaptureMouse(self):
        """
        CaptureMouse(self: UIElement3D) -> bool
        
            Attempts to force capture of the mouse to this element.
            Returns: true if the mouse is successfully captured; otherwise, false.
        """
        pass

    def CaptureStylus(self):
        """
        CaptureStylus(self: UIElement3D) -> bool
        
            Attempts to force capture of the stylus to this element.
            Returns: true if the stylus was successfully captured; otherwise, false.
        """
        pass

    def CaptureTouch(self, touchDevice):
        """
        CaptureTouch(self: UIElement3D, touchDevice: TouchDevice) -> bool
        
            Attempts to force capture of a touch to this element.
        
            touchDevice: The device to capture.
            Returns: true if the specified touch is captured to this element; otherwise, false.
        """
        pass

    def Focus(self):
        """
        Focus(self: UIElement3D) -> bool
        
            Attempts to set the logical focus on this element.
            Returns: true if both logical and keyboard focus were set to this element; false if only logical focus was set.
        """
        pass

    def GetUIParentCore(self, *args): #cannot find CLR method
        """
        GetUIParentCore(self: UIElement3D) -> DependencyObject
        
            When overridden in a derived class, returns an alternative user interface (UI) parent for this element if no visual parent exists.
            Returns: An object, if implementation of a derived class has an alternate parent connection to report.
        """
        pass

    def GetVisual3DChild(self, *args): #cannot find CLR method
        """
        GetVisual3DChild(self: Visual3D, index: int) -> Visual3D
        
            Returns the specified System.Windows.Media.Media3D.Visual3D in the parent System.Windows.Media.Media3D.Visual3DCollection.
        
            index: The index of the 3-D visual object in the collection.
            Returns: The child in the collection at the specified index value.
        """
        pass

    def InvalidateModel(self):
        """
        InvalidateModel(self: UIElement3D)
            Invalidates the model that represents the element.
        """
        pass

    def MoveFocus(self, request):
        """
        MoveFocus(self: UIElement3D, request: TraversalRequest) -> bool
        
            Attempts to move focus from this element to another element. The direction to move focus is specified by a guidance direction, which is interpreted within the organization of the visual parent for this 
             element.
        
        
            request: A traversal request, which contains a property that indicates either a mode to traverse in existing tab order, or a direction to move visually.
            Returns: true if the requested traversal was performed; otherwise, false.
        """
        pass

    def OnAccessKey(self, *args): #cannot find CLR method
        """
        OnAccessKey(self: UIElement3D, e: AccessKeyEventArgs)
            Provides class handling for when an access key that is meaningful for this element is invoked.
        
            e: The event data to the access key event. The event data reports which key was invoked, and indicate whether the System.Windows.Input.AccessKeyManager object that controls the sending of these events also 
             sent this access key invocation to other elements.
        """
        pass

    def OnCreateAutomationPeer(self, *args): #cannot find CLR method
        """
        OnCreateAutomationPeer(self: UIElement3D) -> AutomationPeer
        
            Returns class-specific System.Windows.Automation.Peers.AutomationPeer implementations for the Windows Presentation Foundation (WPF) infrastructure.
            Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
        """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: UIElement3D, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: UIElement3D, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: UIElement3D, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDrop(self, *args): #cannot find CLR method
        """
        OnDrop(self: UIElement3D, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.Drop�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: UIElement3D, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: UIElement3D, e: RoutedEventArgs)
            Raises the System.Windows.UIElement3D.GotFocus�routed event by using the event data provided.
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must contain the identifier for the System.Windows.UIElement3D.GotFocus event.
        """
        pass

    def OnGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnGotKeyboardFocus(self: UIElement3D, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
        """
        pass

    def OnGotMouseCapture(self, *args): #cannot find CLR method
        """
        OnGotMouseCapture(self: UIElement3D, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnGotStylusCapture(self, *args): #cannot find CLR method
        """
        OnGotStylusCapture(self: UIElement3D, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnGotTouchCapture(self, *args): #cannot find CLR method
        """
        OnGotTouchCapture(self: UIElement3D, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement3D.GotTouchCapture routed event that occurs when a touch is captured to this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnIsKeyboardFocusedChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusedChanged(self: UIElement3D, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.IsKeyboardFocusedChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsKeyboardFocusWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusWithinChanged(self: UIElement3D, e: DependencyPropertyChangedEventArgs)
            Invoked just before the System.Windows.UIElement3D.IsKeyboardFocusWithinChanged event is raised by this element. Implement this method to add class handling for this event.
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsMouseCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCapturedChanged(self: UIElement3D, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.IsMouseCapturedChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsMouseCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCaptureWithinChanged(self: UIElement3D, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.IsMouseCaptureWithinChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsMouseDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseDirectlyOverChanged(self: UIElement3D, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.IsMouseDirectlyOverChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsStylusCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCapturedChanged(self: UIElement3D, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.IsStylusCapturedChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsStylusCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCaptureWithinChanged(self: UIElement3D, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.IsStylusCaptureWithinChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsStylusDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusDirectlyOverChanged(self: UIElement3D, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.IsStylusDirectlyOverChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: UIElement3D, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: UIElement3D, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: UIElement3D, e: RoutedEventArgs)
            Raises the System.Windows.UIElement3D.LostFocus�routed event by using the event data that is provided.
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must contain the identifier for the System.Windows.UIElement3D.LostFocus event.
        """
        pass

    def OnLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnLostKeyboardFocus(self: UIElement3D, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
        """
        pass

    def OnLostMouseCapture(self, *args): #cannot find CLR method
        """
        OnLostMouseCapture(self: UIElement3D, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains event data.
        """
        pass

    def OnLostStylusCapture(self, *args): #cannot find CLR method
        """
        OnLostStylusCapture(self: UIElement3D, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains event data.
        """
        pass

    def OnLostTouchCapture(self, *args): #cannot find CLR method
        """
        OnLostTouchCapture(self: UIElement3D, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement3D.LostTouchCapture routed event that occurs when this element loses a touch capture.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: UIElement3D, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. This event data reports details about the mouse button that was pressed and the handled state.
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: UIElement3D, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: UIElement3D, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonDown(self: UIElement3D, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.MouseLeftButtonDown�routed event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was pressed.
        """
        pass

    def OnMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonUp(self: UIElement3D, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.MouseLeftButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was released.
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: UIElement3D, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonDown(self: UIElement3D, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.MouseRightButtonDown�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was pressed.
        """
        pass

    def OnMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonUp(self: UIElement3D, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.MouseRightButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was released.
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: UIElement3D, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the mouse button was released.
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: UIElement3D, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragEnter(self, *args): #cannot find CLR method
        """
        OnPreviewDragEnter(self: UIElement3D, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragLeave(self, *args): #cannot find CLR method
        """
        OnPreviewDragLeave(self: UIElement3D, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragOver(self, *args): #cannot find CLR method
        """
        OnPreviewDragOver(self: UIElement3D, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDrop(self, *args): #cannot find CLR method
        """
        OnPreviewDrop(self: UIElement3D, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewGiveFeedback(self, *args): #cannot find CLR method
        """
        OnPreviewGiveFeedback(self: UIElement3D, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        """
        pass

    def OnPreviewGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewGotKeyboardFocus(self: UIElement3D, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: UIElement3D, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnPreviewKeyUp(self, *args): #cannot find CLR method
        """
        OnPreviewKeyUp(self: UIElement3D, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnPreviewLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewLostKeyboardFocus(self: UIElement3D, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewLostKeyboardFocus�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
        """
        pass

    def OnPreviewMouseDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDown(self: UIElement3D, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that one or more mouse buttons were pressed.
        """
        pass

    def OnPreviewMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonDown(self: UIElement3D, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.PreviewMouseLeftButtonDown�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was pressed.
        """
        pass

    def OnPreviewMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonUp(self: UIElement3D, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.PreviewMouseLeftButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was released.
        """
        pass

    def OnPreviewMouseMove(self, *args): #cannot find CLR method
        """
        OnPreviewMouseMove(self: UIElement3D, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnPreviewMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonDown(self: UIElement3D, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.PreviewMouseRightButtonDown�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was pressed.
        """
        pass

    def OnPreviewMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonUp(self: UIElement3D, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement3D.PreviewMouseRightButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was released.
        """
        pass

    def OnPreviewMouseUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseUp(self: UIElement3D, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that one or more mouse buttons were released.
        """
        pass

    def OnPreviewMouseWheel(self, *args): #cannot find CLR method
        """
        OnPreviewMouseWheel(self: UIElement3D, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        """
        pass

    def OnPreviewQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnPreviewQueryContinueDrag(self: UIElement3D, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonDown(self: UIElement3D, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonUp(self: UIElement3D, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusDown(self: UIElement3D, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInAirMove(self: UIElement3D, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusInRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInRange(self: UIElement3D, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusMove(self: UIElement3D, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusOutOfRange(self: UIElement3D, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnPreviewStylusSystemGesture(self: UIElement3D, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusUp(self: UIElement3D, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewTextInput(self, *args): #cannot find CLR method
        """
        OnPreviewTextInput(self: UIElement3D, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event reaches an element in its route that is derived from this class. Implement this method to add class 
             handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchDown(self, *args): #cannot find CLR method
        """
        OnPreviewTouchDown(self: UIElement3D, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement3D.PreviewTouchDown routed event that occurs when a touch presses this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchMove(self, *args): #cannot find CLR method
        """
        OnPreviewTouchMove(self: UIElement3D, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement3D.PreviewTouchMove routed event that occurs when a touch moves while inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchUp(self, *args): #cannot find CLR method
        """
        OnPreviewTouchUp(self: UIElement3D, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement3D.PreviewTouchUp routed event that occurs when a touch is released inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: DependencyObject, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this System.Windows.DependencyObject has been updated. The specific dependency property that changed is reported in the event data.
        
            e: Event data that will contain the dependency property identifier of interest, the property metadata for the type, and old and new values.
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: UIElement3D, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        """
        pass

    def OnQueryCursor(self, *args): #cannot find CLR method
        """
        OnQueryCursor(self: UIElement3D, e: QueryCursorEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
        """
        pass

    def OnStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnStylusButtonDown(self: UIElement3D, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnStylusButtonUp(self: UIElement3D, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: UIElement3D, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: UIElement3D, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached event is raised by this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnStylusInAirMove(self: UIElement3D, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusInRange(self, *args): #cannot find CLR method
        """
        OnStylusInRange(self: UIElement3D, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: UIElement3D, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached event is raised by this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: UIElement3D, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnStylusOutOfRange(self: UIElement3D, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnStylusSystemGesture(self: UIElement3D, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event data.
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: UIElement3D, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnTextInput(self, *args): #cannot find CLR method
        """
        OnTextInput(self: UIElement3D, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        """
        pass

    def OnTouchDown(self, *args): #cannot find CLR method
        """
        OnTouchDown(self: UIElement3D, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement3D.TouchDown routed event that occurs when a touch presses inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchEnter(self, *args): #cannot find CLR method
        """
        OnTouchEnter(self: UIElement3D, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement3D.TouchEnter routed event that occurs when a touch moves from outside to inside the bounds of this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchLeave(self, *args): #cannot find CLR method
        """
        OnTouchLeave(self: UIElement3D, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement3D.TouchLeave routed event that occurs when a touch moves from inside to outside the bounds of this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchMove(self, *args): #cannot find CLR method
        """
        OnTouchMove(self: UIElement3D, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement3D.TouchMove routed event that occurs when a touch moves while inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchUp(self, *args): #cannot find CLR method
        """
        OnTouchUp(self: UIElement3D, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement3D.TouchUp routed event that occurs when a touch is released inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnUpdateModel(self, *args): #cannot find CLR method
        """
        OnUpdateModel(self: UIElement3D)
            Participates in rendering operations when overridden in a derived class.
        """
        pass

    def OnVisualChildrenChanged(self, *args): #cannot find CLR method
        """
        OnVisualChildrenChanged(self: Visual3D, visualAdded: DependencyObject, visualRemoved: DependencyObject)
            Called when the System.Windows.Media.Media3D.Visual3DCollection of the visual object is modified.
        
            visualAdded: The System.Windows.Media.Media3D.Visual3D that was added to the collection.
            visualRemoved: The System.Windows.Media.Media3D.Visual3D that was removed from the collection.
        """
        pass

    def OnVisualParentChanged(self, *args): #cannot find CLR method
        """
        OnVisualParentChanged(self: UIElement3D, oldParent: DependencyObject)
            Invoked when the parent element of this System.Windows.UIElement3D reports a change to its underlying visual parent.
        
            oldParent: The previous parent. This may be provided as null if the System.Windows.DependencyObject did not have a parent element previously.
        """
        pass

    def PredictFocus(self, direction):
        """
        PredictFocus(self: UIElement3D, direction: FocusNavigationDirection) -> DependencyObject
        
            When overridden in a derived class, returns the element that would receive focus for a specified focus traversal direction, without actually moving focus to that element.
        
            direction: The direction of the requested focus traversal.
            Returns: The element that would have received focus if System.Windows.UIElement3D.MoveFocus(System.Windows.Input.TraversalRequest) were actually invoked.
        """
        pass

    def RaiseEvent(self, e):
        """
        RaiseEvent(self: UIElement3D, e: RoutedEventArgs)
            Raises a specific routed event. The System.Windows.RoutedEvent to be raised is identified within the System.Windows.RoutedEventArgs instance that is provided (as the 
             System.Windows.RoutedEventArgs.RoutedEvent property of that event data).
        
        
            e: A System.Windows.RoutedEventArgs that contains the event data and also identifies the event to raise.
        """
        pass

    def ReleaseAllTouchCaptures(self):
        """
        ReleaseAllTouchCaptures(self: UIElement3D)
            Releases all captured touch devices from this element.
        """
        pass

    def ReleaseMouseCapture(self):
        """
        ReleaseMouseCapture(self: UIElement3D)
            Releases the mouse capture, if this element held the capture.
        """
        pass

    def ReleaseStylusCapture(self):
        """
        ReleaseStylusCapture(self: UIElement3D)
            Releases the stylus device capture, if this element held the capture.
        """
        pass

    def ReleaseTouchCapture(self, touchDevice):
        """
        ReleaseTouchCapture(self: UIElement3D, touchDevice: TouchDevice) -> bool
        
            Attempts to release the specified touch device from this element.
        
            touchDevice: The device to release.
            Returns: true if the touch device is released; otherwise, false.
        """
        pass

    def RemoveHandler(self, routedEvent, handler):
        """
        RemoveHandler(self: UIElement3D, routedEvent: RoutedEvent, handler: Delegate)
            Removes the specified routed event handler from this element.
        
            routedEvent: The identifier of the�routed event for which the handler is attached.
            handler: The specific handler implementation to remove from the event handler collection on this element.
        """
        pass

    def RemoveVisual3DChild(self, *args): #cannot find CLR method
        """
        RemoveVisual3DChild(self: Visual3D, child: Visual3D)
            Removes the parent-child relationship between two 3-D visuals.
        
            child: The child 3-D visual object to remove from the parent visual.
        """
        pass

    def ShouldSerializeCommandBindings(self):
        """
        ShouldSerializeCommandBindings(self: UIElement3D) -> bool
        
            Returns whether serialization processes should serialize the contents of the System.Windows.UIElement3D.CommandBindings property on instances of this class.
            Returns: true if the System.Windows.UIElement3D.CommandBindings property value should be serialized; otherwise, false.
        """
        pass

    def ShouldSerializeInputBindings(self):
        """
        ShouldSerializeInputBindings(self: UIElement3D) -> bool
        
            Returns whether serialization processes should serialize the contents of the System.Windows.UIElement3D.InputBindings property on instances of this class.
            Returns: true if the System.Windows.UIElement3D.InputBindings property value should be serialized; otherwise, false.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for the provided dependency property.
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AllowDrop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether this element can be used as the target of a drag-and-drop operation.

Get: AllowDrop(self: UIElement3D) -> bool

Set: AllowDrop(self: UIElement3D) = value
"""

    AreAnyTouchesCaptured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether at least one touch is captured to this element.

Get: AreAnyTouchesCaptured(self: UIElement3D) -> bool

"""

    AreAnyTouchesCapturedWithin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether at least one touch is captured to this element or to any child elements in its visual tree.

Get: AreAnyTouchesCapturedWithin(self: UIElement3D) -> bool

"""

    AreAnyTouchesDirectlyOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether at least one touch is pressed over this element.

Get: AreAnyTouchesDirectlyOver(self: UIElement3D) -> bool

"""

    AreAnyTouchesOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether at least one touch is pressed over this element or any child elements in its visual tree.

Get: AreAnyTouchesOver(self: UIElement3D) -> bool

"""

    CommandBindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.Windows.Input.CommandBinding objects associated with this element.

Get: CommandBindings(self: UIElement3D) -> CommandBindingCollection

"""

    Focusable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the element can receive focus.

Get: Focusable(self: UIElement3D) -> bool

Set: Focusable(self: UIElement3D) = value
"""

    InputBindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of input bindings associated with this element.

Get: InputBindings(self: UIElement3D) -> InputBindingCollection

"""

    IsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether this element is enabled in the user interface (UI).

Get: IsEnabled(self: UIElement3D) -> bool

Set: IsEnabled(self: UIElement3D) = value
"""

    IsEnabledCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that becomes the return value of System.Windows.UIElement3D.IsEnabled in derived classes.

"""

    IsFocused = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that determines whether this element has logical focus.

Get: IsFocused(self: UIElement3D) -> bool

"""

    IsHitTestVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that declares whether this element can possibly be returned as a hit test result from some portion of its rendered content.

Get: IsHitTestVisible(self: UIElement3D) -> bool

Set: IsHitTestVisible(self: UIElement3D) = value
"""

    IsInputMethodEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether an input method system, such as an Input Method Editor (IME),  is enabled for processing the input to this element.

Get: IsInputMethodEnabled(self: UIElement3D) -> bool

"""

    IsKeyboardFocused = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this element has keyboard focus.

Get: IsKeyboardFocused(self: UIElement3D) -> bool

"""

    IsKeyboardFocusWithin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether keyboard focus is anywhere within the element or its visual tree child elements.

Get: IsKeyboardFocusWithin(self: UIElement3D) -> bool

"""

    IsMouseCaptured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the mouse is captured to this element.

Get: IsMouseCaptured(self: UIElement3D) -> bool

"""

    IsMouseCaptureWithin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that determines whether mouse capture is held by this element or by child elements in its visual tree.

Get: IsMouseCaptureWithin(self: UIElement3D) -> bool

"""

    IsMouseDirectlyOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the position of the mouse pointer corresponds to�hit test results, which take element compositing into account.

Get: IsMouseDirectlyOver(self: UIElement3D) -> bool

"""

    IsMouseOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the mouse pointer is located over this element (including child elements in the visual tree).

Get: IsMouseOver(self: UIElement3D) -> bool

"""

    IsStylusCaptured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the stylus is captured by this element.

Get: IsStylusCaptured(self: UIElement3D) -> bool

"""

    IsStylusCaptureWithin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that determines whether stylus capture is held by this element, or an element within the element bounds and its visual tree.

Get: IsStylusCaptureWithin(self: UIElement3D) -> bool

"""

    IsStylusDirectlyOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the stylus position corresponds to�hit test results, which take element compositing into account.

Get: IsStylusDirectlyOver(self: UIElement3D) -> bool

"""

    IsStylusOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the stylus cursor is located over this element (including visual child elements).

Get: IsStylusOver(self: UIElement3D) -> bool

"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this element is visible in the user interface (UI).

Get: IsVisible(self: UIElement3D) -> bool

"""

    TouchesCaptured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all touch devices that are captured to this element.

Get: TouchesCaptured(self: UIElement3D) -> IEnumerable[TouchDevice]

"""

    TouchesCapturedWithin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all touch devices that are captured to this element or any child elements in its visual tree.

Get: TouchesCapturedWithin(self: UIElement3D) -> IEnumerable[TouchDevice]

"""

    TouchesDirectlyOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all touch devices that are over this element.

Get: TouchesDirectlyOver(self: UIElement3D) -> IEnumerable[TouchDevice]

"""

    TouchesOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all touch devices that are over this element or any child elements in its visual tree.

Get: TouchesOver(self: UIElement3D) -> IEnumerable[TouchDevice]

"""

    Visibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the user interface (UI) visibility of this element.

Get: Visibility(self: UIElement3D) -> Visibility

Set: Visibility(self: UIElement3D) = value
"""

    Visual3DChildrenCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of child elements for the System.Windows.Media.Media3D.Visual3D object.

"""

    Visual3DModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Media3D.Model3D object to render.

"""


    AllowDropProperty = None
    AreAnyTouchesCapturedProperty = None
    AreAnyTouchesCapturedWithinProperty = None
    AreAnyTouchesDirectlyOverProperty = None
    AreAnyTouchesOverProperty = None
    DragEnter = None
    DragEnterEvent = None
    DragLeave = None
    DragLeaveEvent = None
    DragOver = None
    DragOverEvent = None
    Drop = None
    DropEvent = None
    FocusableChanged = None
    FocusableProperty = None
    GiveFeedback = None
    GiveFeedbackEvent = None
    GotFocus = None
    GotFocusEvent = None
    GotKeyboardFocus = None
    GotKeyboardFocusEvent = None
    GotMouseCapture = None
    GotMouseCaptureEvent = None
    GotStylusCapture = None
    GotStylusCaptureEvent = None
    GotTouchCapture = None
    GotTouchCaptureEvent = None
    IsEnabledChanged = None
    IsEnabledProperty = None
    IsFocusedProperty = None
    IsHitTestVisibleChanged = None
    IsHitTestVisibleProperty = None
    IsKeyboardFocusedChanged = None
    IsKeyboardFocusedProperty = None
    IsKeyboardFocusWithinChanged = None
    IsKeyboardFocusWithinProperty = None
    IsMouseCapturedChanged = None
    IsMouseCapturedProperty = None
    IsMouseCaptureWithinChanged = None
    IsMouseCaptureWithinProperty = None
    IsMouseDirectlyOverChanged = None
    IsMouseDirectlyOverProperty = None
    IsMouseOverProperty = None
    IsStylusCapturedChanged = None
    IsStylusCapturedProperty = None
    IsStylusCaptureWithinChanged = None
    IsStylusCaptureWithinProperty = None
    IsStylusDirectlyOverChanged = None
    IsStylusDirectlyOverProperty = None
    IsStylusOverProperty = None
    IsVisibleChanged = None
    IsVisibleProperty = None
    KeyDown = None
    KeyDownEvent = None
    KeyUp = None
    KeyUpEvent = None
    LostFocus = None
    LostFocusEvent = None
    LostKeyboardFocus = None
    LostKeyboardFocusEvent = None
    LostMouseCapture = None
    LostMouseCaptureEvent = None
    LostStylusCapture = None
    LostStylusCaptureEvent = None
    LostTouchCapture = None
    LostTouchCaptureEvent = None
    MouseDown = None
    MouseDownEvent = None
    MouseEnter = None
    MouseEnterEvent = None
    MouseLeave = None
    MouseLeaveEvent = None
    MouseLeftButtonDown = None
    MouseLeftButtonDownEvent = None
    MouseLeftButtonUp = None
    MouseLeftButtonUpEvent = None
    MouseMove = None
    MouseMoveEvent = None
    MouseRightButtonDown = None
    MouseRightButtonDownEvent = None
    MouseRightButtonUp = None
    MouseRightButtonUpEvent = None
    MouseUp = None
    MouseUpEvent = None
    MouseWheel = None
    MouseWheelEvent = None
    PreviewDragEnter = None
    PreviewDragEnterEvent = None
    PreviewDragLeave = None
    PreviewDragLeaveEvent = None
    PreviewDragOver = None
    PreviewDragOverEvent = None
    PreviewDrop = None
    PreviewDropEvent = None
    PreviewGiveFeedback = None
    PreviewGiveFeedbackEvent = None
    PreviewGotKeyboardFocus = None
    PreviewGotKeyboardFocusEvent = None
    PreviewKeyDown = None
    PreviewKeyDownEvent = None
    PreviewKeyUp = None
    PreviewKeyUpEvent = None
    PreviewLostKeyboardFocus = None
    PreviewLostKeyboardFocusEvent = None
    PreviewMouseDown = None
    PreviewMouseDownEvent = None
    PreviewMouseLeftButtonDown = None
    PreviewMouseLeftButtonDownEvent = None
    PreviewMouseLeftButtonUp = None
    PreviewMouseLeftButtonUpEvent = None
    PreviewMouseMove = None
    PreviewMouseMoveEvent = None
    PreviewMouseRightButtonDown = None
    PreviewMouseRightButtonDownEvent = None
    PreviewMouseRightButtonUp = None
    PreviewMouseRightButtonUpEvent = None
    PreviewMouseUp = None
    PreviewMouseUpEvent = None
    PreviewMouseWheel = None
    PreviewMouseWheelEvent = None
    PreviewQueryContinueDrag = None
    PreviewQueryContinueDragEvent = None
    PreviewStylusButtonDown = None
    PreviewStylusButtonDownEvent = None
    PreviewStylusButtonUp = None
    PreviewStylusButtonUpEvent = None
    PreviewStylusDown = None
    PreviewStylusDownEvent = None
    PreviewStylusInAirMove = None
    PreviewStylusInAirMoveEvent = None
    PreviewStylusInRange = None
    PreviewStylusInRangeEvent = None
    PreviewStylusMove = None
    PreviewStylusMoveEvent = None
    PreviewStylusOutOfRange = None
    PreviewStylusOutOfRangeEvent = None
    PreviewStylusSystemGesture = None
    PreviewStylusSystemGestureEvent = None
    PreviewStylusUp = None
    PreviewStylusUpEvent = None
    PreviewTextInput = None
    PreviewTextInputEvent = None
    PreviewTouchDown = None
    PreviewTouchDownEvent = None
    PreviewTouchMove = None
    PreviewTouchMoveEvent = None
    PreviewTouchUp = None
    PreviewTouchUpEvent = None
    QueryContinueDrag = None
    QueryContinueDragEvent = None
    QueryCursor = None
    QueryCursorEvent = None
    StylusButtonDown = None
    StylusButtonDownEvent = None
    StylusButtonUp = None
    StylusButtonUpEvent = None
    StylusDown = None
    StylusDownEvent = None
    StylusEnter = None
    StylusEnterEvent = None
    StylusInAirMove = None
    StylusInAirMoveEvent = None
    StylusInRange = None
    StylusInRangeEvent = None
    StylusLeave = None
    StylusLeaveEvent = None
    StylusMove = None
    StylusMoveEvent = None
    StylusOutOfRange = None
    StylusOutOfRangeEvent = None
    StylusSystemGesture = None
    StylusSystemGestureEvent = None
    StylusUp = None
    StylusUpEvent = None
    TextInput = None
    TextInputEvent = None
    TouchDown = None
    TouchDownEvent = None
    TouchEnter = None
    TouchEnterEvent = None
    TouchLeave = None
    TouchLeaveEvent = None
    TouchMove = None
    TouchMoveEvent = None
    TouchUp = None
    TouchUpEvent = None
    VisibilityProperty = None

