class Underline(Span, IInputElement, IAnimatable, IFrameworkInputElement, ISupportInitialize, IQueryAmbient, IAddChild):
    """
    An inline-level flow content element which causes content to render with an underlined text decoration.
    
    Underline()
    Underline(childInline: Inline)
    Underline(childInline: Inline, insertionPosition: TextPointer)
    Underline(start: TextPointer, end: TextPointer)
    """
    def AddLogicalChild(self, *args): #cannot find CLR method
        """
        AddLogicalChild(self: FrameworkContentElement, child: object)
            Adds the provided element as a child of this element.
        
            child: The child element to be added.
        """
        pass

    def GetUIParentCore(self, *args): #cannot find CLR method
        """
        GetUIParentCore(self: FrameworkContentElement) -> DependencyObject
        
            Returns an alternative logical parent for this element if there is no visual parent. In this case, a System.Windows.FrameworkContentElement  parent is always the same value as the 
             System.Windows.FrameworkContentElement.Parent property.
        
            Returns: Returns something other than null whenever a WPF framework-level implementation of this method has a non-visual parent connection.
        """
        pass

    def OnContextMenuClosing(self, *args): #cannot find CLR method
        """
        OnContextMenuClosing(self: FrameworkContentElement, e: ContextMenuEventArgs)
            Invoked whenever the System.Windows.FrameworkContentElement.ContextMenuClosing routed event reaches this class in its route. Implement this method to add class handling for this event.
        
            e: Provides data about the event.
        """
        pass

    def OnContextMenuOpening(self, *args): #cannot find CLR method
        """
        OnContextMenuOpening(self: FrameworkContentElement, e: ContextMenuEventArgs)
            Invoked whenever the System.Windows.FrameworkContentElement.ContextMenuOpening routed event reaches this class in its route. Implement this method to add class handling for this event.
        
            e: Event data for the event.
        """
        pass

    def OnCreateAutomationPeer(self, *args): #cannot find CLR method
        """
        OnCreateAutomationPeer(self: ContentElement) -> AutomationPeer
        
            Returns class-specific System.Windows.Automation.Peers.AutomationPeer implementations for the Windows Presentation Foundation (WPF) infrastructure.
            Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
        """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: ContentElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: ContentElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: ContentElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDrop(self, *args): #cannot find CLR method
        """
        OnDrop(self: ContentElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: ContentElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: FrameworkContentElement, e: RoutedEventArgs)
            Class handler for the System.Windows.ContentElement.GotFocus event.
        
            e: Event data for the event.
        """
        pass

    def OnGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnGotKeyboardFocus(self: ContentElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
        """
        pass

    def OnGotMouseCapture(self, *args): #cannot find CLR method
        """
        OnGotMouseCapture(self: ContentElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnGotStylusCapture(self, *args): #cannot find CLR method
        """
        OnGotStylusCapture(self: ContentElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnGotTouchCapture(self, *args): #cannot find CLR method
        """
        OnGotTouchCapture(self: ContentElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.ContentElement.GotTouchCapture routed event that occurs when a touch is captured to this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnInitialized(self, *args): #cannot find CLR method
        """
        OnInitialized(self: FrameworkContentElement, e: EventArgs)
            Raises the System.Windows.FrameworkContentElement.Initialized event. This method is invoked whenever System.Windows.FrameworkContentElement.IsInitialized is set to true.
        
            e: Event data for the event.
        """
        pass

    def OnIsKeyboardFocusedChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusedChanged(self: ContentElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.IsKeyboardFocusedChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsKeyboardFocusWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusWithinChanged(self: ContentElement, e: DependencyPropertyChangedEventArgs)
            Invoked just before the System.Windows.ContentElement.IsKeyboardFocusWithinChanged event is raised by this element. Implement this method to add class handling for this event.
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsMouseCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCapturedChanged(self: ContentElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.IsMouseCapturedChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsMouseCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCaptureWithinChanged(self: ContentElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.IsMouseCaptureWithinChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsMouseDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseDirectlyOverChanged(self: ContentElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.IsMouseDirectlyOverChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsStylusCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCapturedChanged(self: ContentElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.IsStylusCapturedChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsStylusCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCaptureWithinChanged(self: ContentElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.IsStylusCaptureWithinChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsStylusDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusDirectlyOverChanged(self: ContentElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.IsStylusDirectlyOverChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: ContentElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: ContentElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: ContentElement, e: RoutedEventArgs)
            Raises the System.Windows.ContentElement.LostFocus�routed event by using the event data that is provided.
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must contain the identifier for the System.Windows.ContentElement.LostFocus event.
        """
        pass

    def OnLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnLostKeyboardFocus(self: ContentElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
        """
        pass

    def OnLostMouseCapture(self, *args): #cannot find CLR method
        """
        OnLostMouseCapture(self: ContentElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains event data.
        """
        pass

    def OnLostStylusCapture(self, *args): #cannot find CLR method
        """
        OnLostStylusCapture(self: ContentElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains event data.
        """
        pass

    def OnLostTouchCapture(self, *args): #cannot find CLR method
        """
        OnLostTouchCapture(self: ContentElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.ContentElement.LostTouchCapture routed event that occurs when this element loses a touch capture.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: ContentElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. This event data reports details about the mouse button that was pressed and the handled state.
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: ContentElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: ContentElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonDown(self: ContentElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.MouseLeftButtonDown�routed event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was pressed.
        """
        pass

    def OnMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonUp(self: ContentElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.MouseLeftButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was released.
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: ContentElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonDown(self: ContentElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.MouseRightButtonDown�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was pressed.
        """
        pass

    def OnMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonUp(self: ContentElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.MouseRightButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was released.
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: ContentElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the mouse button was released.
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: ContentElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragEnter(self, *args): #cannot find CLR method
        """
        OnPreviewDragEnter(self: ContentElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragLeave(self, *args): #cannot find CLR method
        """
        OnPreviewDragLeave(self: ContentElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragOver(self, *args): #cannot find CLR method
        """
        OnPreviewDragOver(self: ContentElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDrop(self, *args): #cannot find CLR method
        """
        OnPreviewDrop(self: ContentElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewGiveFeedback(self, *args): #cannot find CLR method
        """
        OnPreviewGiveFeedback(self: ContentElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        """
        pass

    def OnPreviewGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewGotKeyboardFocus(self: ContentElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: ContentElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnPreviewKeyUp(self, *args): #cannot find CLR method
        """
        OnPreviewKeyUp(self: ContentElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnPreviewLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewLostKeyboardFocus(self: ContentElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
        """
        pass

    def OnPreviewMouseDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDown(self: ContentElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that one or more mouse buttons were pressed.
        """
        pass

    def OnPreviewMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonDown(self: ContentElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.PreviewMouseLeftButtonDown�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was pressed.
        """
        pass

    def OnPreviewMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonUp(self: ContentElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.PreviewMouseLeftButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was released.
        """
        pass

    def OnPreviewMouseMove(self, *args): #cannot find CLR method
        """
        OnPreviewMouseMove(self: ContentElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnPreviewMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonDown(self: ContentElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.PreviewMouseRightButtonDown�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was pressed.
        """
        pass

    def OnPreviewMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonUp(self: ContentElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.ContentElement.PreviewMouseRightButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was released.
        """
        pass

    def OnPreviewMouseUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseUp(self: ContentElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that one or more mouse buttons were released.
        """
        pass

    def OnPreviewMouseWheel(self, *args): #cannot find CLR method
        """
        OnPreviewMouseWheel(self: ContentElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        """
        pass

    def OnPreviewQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnPreviewQueryContinueDrag(self: ContentElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonDown(self: ContentElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonUp(self: ContentElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusDown(self: ContentElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInAirMove(self: ContentElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusInRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInRange(self: ContentElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusMove(self: ContentElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusOutOfRange(self: ContentElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnPreviewStylusSystemGesture(self: ContentElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusUp(self: ContentElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewTextInput(self, *args): #cannot find CLR method
        """
        OnPreviewTextInput(self: ContentElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event reaches an element in its route that is derived from this class. Implement this method to add class 
             handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchDown(self, *args): #cannot find CLR method
        """
        OnPreviewTouchDown(self: ContentElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.ContentElement.PreviewTouchDown routed event that occurs when a touch presses this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchMove(self, *args): #cannot find CLR method
        """
        OnPreviewTouchMove(self: ContentElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.ContentElement.PreviewTouchMove routed event that occurs when a touch moves while inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchUp(self, *args): #cannot find CLR method
        """
        OnPreviewTouchUp(self: ContentElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.ContentElement.PreviewTouchUp routed event that occurs when a touch is released inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: TextElement, e: DependencyPropertyChangedEventArgs)
            Handles notifications that one or more of the dependency properties that exist on the element have had their effective values changed.
        
            e: Arguments associated with the property value change.  The System.Windows.DependencyPropertyChangedEventArgs.Property property specifies which property has changed, the 
             System.Windows.DependencyPropertyChangedEventArgs.OldValue property specifies the previous property value, and the System.Windows.DependencyPropertyChangedEventArgs.NewValue property specifies the new 
             property value.
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: ContentElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        """
        pass

    def OnQueryCursor(self, *args): #cannot find CLR method
        """
        OnQueryCursor(self: ContentElement, e: QueryCursorEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: FrameworkContentElement, oldStyle: Style, newStyle: Style)
            Invoked when the style that is in use on this element changes.
        
            oldStyle: The old style.
            newStyle: The new style.
        """
        pass

    def OnStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnStylusButtonDown(self: ContentElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnStylusButtonUp(self: ContentElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: ContentElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: ContentElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached event is raised by this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnStylusInAirMove(self: ContentElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusInRange(self, *args): #cannot find CLR method
        """
        OnStylusInRange(self: ContentElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: ContentElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached event is raised by this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: ContentElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnStylusOutOfRange(self: ContentElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnStylusSystemGesture(self: ContentElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event data.
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: ContentElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnTextInput(self, *args): #cannot find CLR method
        """
        OnTextInput(self: ContentElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        """
        pass

    def OnToolTipClosing(self, *args): #cannot find CLR method
        """
        OnToolTipClosing(self: FrameworkContentElement, e: ToolTipEventArgs)
            Invoked whenever the System.Windows.FrameworkContentElement.ToolTipClosing routed event reaches this class in its route. Implement this method to add class handling for this event.
        
            e: Provides data about the event.
        """
        pass

    def OnToolTipOpening(self, *args): #cannot find CLR method
        """
        OnToolTipOpening(self: FrameworkContentElement, e: ToolTipEventArgs)
            Invoked whenever the System.Windows.FrameworkContentElement.ToolTipOpening routed event reaches this class in its route. Implement this method to add class handling for this event.
        
            e: Provides data about the event.
        """
        pass

    def OnTouchDown(self, *args): #cannot find CLR method
        """
        OnTouchDown(self: ContentElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.ContentElement.TouchDown routed event that occurs when a touch presses inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchEnter(self, *args): #cannot find CLR method
        """
        OnTouchEnter(self: ContentElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.ContentElement.TouchEnter routed event that occurs when a touch moves from outside to inside the bounds of this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchLeave(self, *args): #cannot find CLR method
        """
        OnTouchLeave(self: ContentElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.ContentElement.TouchLeave routed event that occurs when a touch moves from inside to outside the bounds of this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchMove(self, *args): #cannot find CLR method
        """
        OnTouchMove(self: ContentElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.ContentElement.TouchMove routed event that occurs when a touch moves while inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchUp(self, *args): #cannot find CLR method
        """
        OnTouchUp(self: ContentElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.ContentElement.TouchUp routed event that occurs when a touch is released inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def RemoveLogicalChild(self, *args): #cannot find CLR method
        """
        RemoveLogicalChild(self: FrameworkContentElement, child: object)
            Removes the specified element from the logical tree for this element.
        
            child: The element to remove.
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, childInline: Inline)
        __new__(cls: type, childInline: Inline, insertionPosition: TextPointer)
        __new__(cls: type, start: TextPointer, end: TextPointer)
        """
        pass

    DefaultStyleKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key to use to find the style template for this control in themes.

"""

    IsEnabledCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that becomes the return value of System.Windows.ContentElement.IsEnabled in derived classes.

"""

    LogicalChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerator that can iterate the logical children of the element.

"""


