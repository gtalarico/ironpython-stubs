class UIElement(Visual, IResource, IAnimatable, IInputElement):
    """
    System.Windows.UIElement is a base class for WPF core level implementations building on Windows Presentation Foundation (WPF) elements and basic presentation characteristics.
    
    UIElement()
    """
    def AddHandler(self, routedEvent, handler, handledEventsToo=None):
        """
        AddHandler(self: UIElement, routedEvent: RoutedEvent, handler: Delegate, handledEventsToo: bool)
            Adds a�routed event handler for a specified routed event, adding the handler to the handler collection on the current element. Specify handledEventsToo as true to have the provided handler be invoked for 
             routed event that had already been marked as handled by another element along the event route.
        
        
            routedEvent: An identifier for the�routed event to be handled.
            handler: A reference to the handler implementation.
            handledEventsToo: true to register the handler such that it is invoked even when  the routed event is marked handled in its event data; false to register the handler with the default condition that it will not be invoked if 
             the routed event is already marked handled. The default is false.Do not routinely ask to rehandle a routed event. For more information, see Remarks.
        
        AddHandler(self: UIElement, routedEvent: RoutedEvent, handler: Delegate)
            Adds a�routed event handler for a specified routed event, adding the handler to the handler collection on the current element.
        
            routedEvent: An identifier for the�routed event to be handled.
            handler: A reference to the handler implementation.
        """
        pass

    def AddToEventRoute(self, route, e):
        """
        AddToEventRoute(self: UIElement, route: EventRoute, e: RoutedEventArgs)
            Adds handlers to the specified System.Windows.EventRoute for the current System.Windows.UIElement event handler collection.
        
            route: The event route that handlers are added to.
            e: The event data that is used to add the handlers. This method uses the System.Windows.RoutedEventArgs.RoutedEvent property of the event data to create the handlers.
        """
        pass

    def AddVisualChild(self, *args): #cannot find CLR method
        """
        AddVisualChild(self: Visual, child: Visual)
            Defines the parent-child relationship between two visuals.
        
            child: The child visual object to add to parent visual.
        """
        pass

    def ApplyAnimationClock(self, dp, clock, handoffBehavior=None):
        """
        ApplyAnimationClock(self: UIElement, dp: DependencyProperty, clock: AnimationClock, handoffBehavior: HandoffBehavior)
            Applies an animation to a specified�dependency property on this element, with the ability to specify what happens if the property already has a running animation.
        
            dp: The property to animate.
            clock: The animation clock that controls and declares the animation.
            handoffBehavior: A value of the enumeration. The default is System.Windows.Media.Animation.HandoffBehavior.SnapshotAndReplace, which will stop any existing animation and replace with the new one.
        ApplyAnimationClock(self: UIElement, dp: DependencyProperty, clock: AnimationClock)
            Applies an animation to a specified�dependency property on this element. Any existing animations are stopped and replaced with the new animation.
        
            dp: The identifier for the property to animate.
            clock: The animation clock that controls and declares the animation.
        """
        pass

    def Arrange(self, finalRect):
        """
        Arrange(self: UIElement, finalRect: Rect)
            Positions child elements and determines a size for a System.Windows.UIElement. Parent elements call this method from their System.Windows.UIElement.ArrangeCore(System.Windows.Rect) implementation (or a WPF 
             framework-level equivalent) to form a recursive layout update. This method constitutes the second pass of a layout update.
        
        
            finalRect: The final size that the parent computes for the child element, provided as a System.Windows.Rect instance.
        """
        pass

    def ArrangeCore(self, *args): #cannot find CLR method
        """
        ArrangeCore(self: UIElement, finalRect: Rect)
            Defines the template for WPF core-level arrange layout definition.
        
            finalRect: The final area within the parent that element should use to arrange itself and its child elements.
        """
        pass

    def BeginAnimation(self, dp, animation, handoffBehavior=None):
        """
        BeginAnimation(self: UIElement, dp: DependencyProperty, animation: AnimationTimeline, handoffBehavior: HandoffBehavior)
            Starts a specific animation for a specified animated property on this element, with the option of specifying what happens if the property already has a running animation.
        
            dp: The property to animate, which is specified as the dependency property identifier.
            animation: The timeline of the animation to be applied.
            handoffBehavior: A value of the enumeration that specifies how the new animation interacts with any current (running) animations that are already affecting the property value.
        BeginAnimation(self: UIElement, dp: DependencyProperty, animation: AnimationTimeline)
            Starts an animation for a specified animated property on this element.
        
            dp: The property to animate, which is specified as a dependency property identifier.
            animation: The timeline of the animation to start.
        """
        pass

    def CaptureMouse(self):
        """
        CaptureMouse(self: UIElement) -> bool
        
            Attempts to force capture of the mouse to this element.
            Returns: true if the mouse is successfully captured; otherwise, false.
        """
        pass

    def CaptureStylus(self):
        """
        CaptureStylus(self: UIElement) -> bool
        
            Attempts to force capture of the stylus to this element.
            Returns: true if the stylus was successfully captured; otherwise, false.
        """
        pass

    def CaptureTouch(self, touchDevice):
        """
        CaptureTouch(self: UIElement, touchDevice: TouchDevice) -> bool
        
            Attempts to force capture of a touch to this element.
        
            touchDevice: The device to capture.
            Returns: true if the specified touch is captured to this element; otherwise, false.
        """
        pass

    def Focus(self):
        """
        Focus(self: UIElement) -> bool
        
            Attempts to set focus to this element.
            Returns: true if keyboard focus and logical focus were set to this element; false if only logical focus was set to this element, or if the call to this method did not force the focus to change.
        """
        pass

    def GetAnimationBaseValue(self, dp):
        """
        GetAnimationBaseValue(self: UIElement, dp: DependencyProperty) -> object
        
            Returns the base property value for the specified property on this element, disregarding any possible animated value from a running or stopped animation.
        
            dp: The�dependency property to check.
            Returns: The property value as if no animations are attached to the specified dependency property.
        """
        pass

    def GetLayoutClip(self, *args): #cannot find CLR method
        """
        GetLayoutClip(self: UIElement, layoutSlotSize: Size) -> Geometry
        
            Returns an alternative clipping geometry that represents the region that would be clipped if System.Windows.UIElement.ClipToBounds were set to true.
        
            layoutSlotSize: The available size provided by the element.
            Returns: The potential clipping geometry.
        """
        pass

    def GetUIParentCore(self, *args): #cannot find CLR method
        """
        GetUIParentCore(self: UIElement) -> DependencyObject
        
            When overridden in a derived class, returns an alternative user interface (UI) parent for this element if no visual parent exists.
            Returns: An object, if implementation of a derived class has an alternate parent connection to report.
        """
        pass

    def GetVisualChild(self, *args): #cannot find CLR method
        """
        GetVisualChild(self: Visual, index: int) -> Visual
        
            Returns the specified System.Windows.Media.Visual in the parent System.Windows.Media.VisualCollection.
        
            index: The index of the visual object in the System.Windows.Media.VisualCollection.
            Returns: The child in the System.Windows.Media.VisualCollection at the specified index value.
        """
        pass

    def HitTestCore(self, *args): #cannot find CLR method
        """
        HitTestCore(self: UIElement, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        
            Implements System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestParameters) to supply base element hit testing behavior (returning System.Windows.Media.GeometryHitTestResult).
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated geometry.
        HitTestCore(self: UIElement, hitTestParameters: PointHitTestParameters) -> HitTestResult
        
            Implements System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParameters) to supply base element hit testing behavior (returning System.Windows.Media.HitTestResult).
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated point.
        """
        pass

    def InputHitTest(self, point):
        """
        InputHitTest(self: UIElement, point: Point) -> IInputElement
        
            Returns the input element within the current element that is at the specified coordinates, relative to the current element's origin.
        
            point: The offset coordinates within this element.
            Returns: The element child that is located at the given position.
        """
        pass

    def InvalidateArrange(self):
        """
        InvalidateArrange(self: UIElement)
            Invalidates the arrange state (layout) for the element. After the invalidation, the element will have its layout updated, which will occur asynchronously unless subsequently forced by 
             System.Windows.UIElement.UpdateLayout.
        """
        pass

    def InvalidateMeasure(self):
        """
        InvalidateMeasure(self: UIElement)
            Invalidates the measurement state (layout) for the element.
        """
        pass

    def InvalidateVisual(self):
        """
        InvalidateVisual(self: UIElement)
            Invalidates the rendering of the element, and forces a complete new layout pass. System.Windows.UIElement.OnRender(System.Windows.Media.DrawingContext) is called after the layout cycle is completed.
        """
        pass

    def Measure(self, availableSize):
        """
        Measure(self: UIElement, availableSize: Size)
            Updates the System.Windows.UIElement.DesiredSize of a System.Windows.UIElement. Parent elements call this method from their own System.Windows.UIElement.MeasureCore(System.Windows.Size) implementations to 
             form a recursive layout update. Calling this method constitutes the first pass (the "Measure" pass) of a layout update.
        
        
            availableSize: The available space that a parent element can allocate a child element. A child element can request a larger space than what is available; the provided size might be accommodated if scrolling is possible 
             in the content model for the current element.
        """
        pass

    def MeasureCore(self, *args): #cannot find CLR method
        """
        MeasureCore(self: UIElement, availableSize: Size) -> Size
        
            When overridden in a derived class, provides measurement logic for sizing this element properly, with consideration of the size of any child element content.
        
            availableSize: The available size that the parent element can allocate for the child.
            Returns: The desired size of this element in layout.
        """
        pass

    def MoveFocus(self, request):
        """
        MoveFocus(self: UIElement, request: TraversalRequest) -> bool
        
            Attempts to move focus from this element to another element. The direction to move focus is specified by a guidance direction, which is interpreted within the organization of the visual parent for this 
             element.
        
        
            request: A traversal request, which contains a property that indicates either a mode to traverse in existing tab order, or a direction to move visually.
            Returns: true if the requested traversal was performed; otherwise, false.
        """
        pass

    def OnAccessKey(self, *args): #cannot find CLR method
        """
        OnAccessKey(self: UIElement, e: AccessKeyEventArgs)
            Provides class handling for when an access key that is meaningful for this element is invoked.
        
            e: The event data to the access key event. The event data reports which key was invoked, and indicate whether the System.Windows.Input.AccessKeyManager object that controls the sending of these events also 
             sent this access key invocation to other elements.
        """
        pass

    def OnChildDesiredSizeChanged(self, *args): #cannot find CLR method
        """
        OnChildDesiredSizeChanged(self: UIElement, child: UIElement)
            Supports layout behavior when a child element is resized.
        
            child: The child element that is being resized.
        """
        pass

    def OnCreateAutomationPeer(self, *args): #cannot find CLR method
        """
        OnCreateAutomationPeer(self: UIElement) -> AutomationPeer
        
            Returns class-specific System.Windows.Automation.Peers.AutomationPeer implementations for the Windows Presentation Foundation (WPF) infrastructure.
            Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: Visual, oldDpi: DpiScale, newDpi: DpiScale) """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDrop(self, *args): #cannot find CLR method
        """
        OnDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: UIElement, e: RoutedEventArgs)
            Raises the System.Windows.UIElement.GotFocus�routed event by using the event data provided.
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must contain the identifier for the System.Windows.UIElement.GotFocus event.
        """
        pass

    def OnGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
        """
        pass

    def OnGotMouseCapture(self, *args): #cannot find CLR method
        """
        OnGotMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnGotStylusCapture(self, *args): #cannot find CLR method
        """
        OnGotStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnGotTouchCapture(self, *args): #cannot find CLR method
        """
        OnGotTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.GotTouchCapture routed event that occurs when a touch is captured to this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnIsKeyboardFocusedChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsKeyboardFocusWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked just before the System.Windows.UIElement.IsKeyboardFocusWithinChanged event is raised by this element. Implement this method to add class handling for this event.
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsMouseCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCapturedChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsMouseCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsMouseDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsStylusCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsStylusCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsStylusDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: UIElement, e: RoutedEventArgs)
            Raises the System.Windows.UIElement.LostFocus�routed event by using the event data that is provided.
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must contain the identifier for the System.Windows.UIElement.LostFocus event.
        """
        pass

    def OnLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
        """
        pass

    def OnLostMouseCapture(self, *args): #cannot find CLR method
        """
        OnLostMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains event data.
        """
        pass

    def OnLostStylusCapture(self, *args): #cannot find CLR method
        """
        OnLostStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains event data.
        """
        pass

    def OnLostTouchCapture(self, *args): #cannot find CLR method
        """
        OnLostTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.LostTouchCapture routed event that occurs when this element loses a touch capture.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnManipulationBoundaryFeedback(self, *args): #cannot find CLR method
        """
        OnManipulationBoundaryFeedback(self: UIElement, e: ManipulationBoundaryFeedbackEventArgs)
            Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event occurs.
        
            e: The data for the event.
        """
        pass

    def OnManipulationCompleted(self, *args): #cannot find CLR method
        """
        OnManipulationCompleted(self: UIElement, e: ManipulationCompletedEventArgs)
            Called when the System.Windows.UIElement.ManipulationCompleted event occurs.
        
            e: The data for the event.
        """
        pass

    def OnManipulationDelta(self, *args): #cannot find CLR method
        """
        OnManipulationDelta(self: UIElement, e: ManipulationDeltaEventArgs)
            Called when the System.Windows.UIElement.ManipulationDelta event occurs.
        
            e: The data for the event.
        """
        pass

    def OnManipulationInertiaStarting(self, *args): #cannot find CLR method
        """
        OnManipulationInertiaStarting(self: UIElement, e: ManipulationInertiaStartingEventArgs)
            Called when the System.Windows.UIElement.ManipulationInertiaStarting event occurs.
        
            e: The data for the event.
        """
        pass

    def OnManipulationStarted(self, *args): #cannot find CLR method
        """
        OnManipulationStarted(self: UIElement, e: ManipulationStartedEventArgs)
            Called when the System.Windows.UIElement.ManipulationStarted event occurs.
        
            e: The data for the event.
        """
        pass

    def OnManipulationStarting(self, *args): #cannot find CLR method
        """
        OnManipulationStarting(self: UIElement, e: ManipulationStartingEventArgs)
            Provides class handling for the System.Windows.UIElement.ManipulationStarting routed event that occurs when the manipulation processor is first created.
        
            e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event data.
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. This event data reports details about the mouse button that was pressed and the handled state.
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was pressed.
        """
        pass

    def OnMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was released.
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was pressed.
        """
        pass

    def OnMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was released.
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the mouse button was released.
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragEnter(self, *args): #cannot find CLR method
        """
        OnPreviewDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragLeave(self, *args): #cannot find CLR method
        """
        OnPreviewDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragOver(self, *args): #cannot find CLR method
        """
        OnPreviewDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDrop(self, *args): #cannot find CLR method
        """
        OnPreviewDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewGiveFeedback(self, *args): #cannot find CLR method
        """
        OnPreviewGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        """
        pass

    def OnPreviewGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnPreviewKeyUp(self, *args): #cannot find CLR method
        """
        OnPreviewKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnPreviewLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
        """
        pass

    def OnPreviewMouseDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that one or more mouse buttons were pressed.
        """
        pass

    def OnPreviewMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was pressed.
        """
        pass

    def OnPreviewMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was released.
        """
        pass

    def OnPreviewMouseMove(self, *args): #cannot find CLR method
        """
        OnPreviewMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnPreviewMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was pressed.
        """
        pass

    def OnPreviewMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was released.
        """
        pass

    def OnPreviewMouseUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that one or more mouse buttons were released.
        """
        pass

    def OnPreviewMouseWheel(self, *args): #cannot find CLR method
        """
        OnPreviewMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        """
        pass

    def OnPreviewQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnPreviewQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusInRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnPreviewStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewTextInput(self, *args): #cannot find CLR method
        """
        OnPreviewTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event reaches an element in its route that is derived from this class. Implement this method to add class 
             handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchDown(self, *args): #cannot find CLR method
        """
        OnPreviewTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchDown routed event that occurs when a touch presses this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchMove(self, *args): #cannot find CLR method
        """
        OnPreviewTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchMove routed event that occurs when a touch moves while inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchUp(self, *args): #cannot find CLR method
        """
        OnPreviewTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed event that occurs when a touch is released inside this element.
        
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
        OnQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        """
        pass

    def OnQueryCursor(self, *args): #cannot find CLR method
        """
        OnQueryCursor(self: UIElement, e: QueryCursorEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
        """
        pass

    def OnRender(self, *args): #cannot find CLR method
        """
        OnRender(self: UIElement, drawingContext: DrawingContext)
            When overridden in a derived class, participates in rendering operations that are directed by the layout system. The rendering instructions for this element are not used directly when this method is 
             invoked, and are instead preserved for later asynchronous use by layout and drawing.
        
        
            drawingContext: The drawing instructions for a specific element. This context is provided to the layout system.
        """
        pass

    def OnRenderSizeChanged(self, *args): #cannot find CLR method
        """
        OnRenderSizeChanged(self: UIElement, info: SizeChangedInfo)
            When overridden in a derived class, participates in rendering operations that are directed by the layout system. This method is invoked after layout update, and before rendering, if the element's 
             System.Windows.UIElement.RenderSize has changed as a result of layout update.
        
        
            info: The packaged parameters (System.Windows.SizeChangedInfo), which includes old and new sizes, and which dimension actually changes.
        """
        pass

    def OnStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached event is raised by this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusInRange(self, *args): #cannot find CLR method
        """
        OnStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached event is raised by this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event data.
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnTextInput(self, *args): #cannot find CLR method
        """
        OnTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        """
        pass

    def OnTouchDown(self, *args): #cannot find CLR method
        """
        OnTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchDown routed event that occurs when a touch presses inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchEnter(self, *args): #cannot find CLR method
        """
        OnTouchEnter(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchEnter routed event that occurs when a touch moves from outside to inside the bounds of this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchLeave(self, *args): #cannot find CLR method
        """
        OnTouchLeave(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchLeave routed event that occurs when a touch moves from inside to outside the bounds of this System.Windows.UIElement.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchMove(self, *args): #cannot find CLR method
        """
        OnTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchMove routed event that occurs when a touch moves while inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchUp(self, *args): #cannot find CLR method
        """
        OnTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchUp routed event that occurs when a touch is released inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnVisualChildrenChanged(self, *args): #cannot find CLR method
        """
        OnVisualChildrenChanged(self: Visual, visualAdded: DependencyObject, visualRemoved: DependencyObject)
            Called when the System.Windows.Media.VisualCollection of the visual object is modified.
        
            visualAdded: The System.Windows.Media.Visual that was added to the collection
            visualRemoved: The System.Windows.Media.Visual that was removed from the collection
        """
        pass

    def OnVisualParentChanged(self, *args): #cannot find CLR method
        """
        OnVisualParentChanged(self: UIElement, oldParent: DependencyObject)
            Invoked when the parent element of this System.Windows.UIElement reports a change to its underlying visual parent.
        
            oldParent: The previous parent. This may be provided as null if the System.Windows.DependencyObject did not have a parent element previously.
        """
        pass

    def PredictFocus(self, direction):
        """
        PredictFocus(self: UIElement, direction: FocusNavigationDirection) -> DependencyObject
        
            When overridden in a derived class, returns the element that would receive focus for a specified focus traversal direction, without actually moving focus to that element.
        
            direction: The direction of the requested focus traversal.
            Returns: The element that would have received focus if System.Windows.UIElement.MoveFocus(System.Windows.Input.TraversalRequest) were actually invoked.
        """
        pass

    def RaiseEvent(self, e):
        """
        RaiseEvent(self: UIElement, e: RoutedEventArgs)
            Raises a specific routed event. The System.Windows.RoutedEvent to be raised is identified within the System.Windows.RoutedEventArgs instance that is provided (as the 
             System.Windows.RoutedEventArgs.RoutedEvent property of that event data).
        
        
            e: A System.Windows.RoutedEventArgs that contains the event data and also identifies the event to raise.
        """
        pass

    def ReleaseAllTouchCaptures(self):
        """
        ReleaseAllTouchCaptures(self: UIElement)
            Releases all captured touch devices from this element.
        """
        pass

    def ReleaseMouseCapture(self):
        """
        ReleaseMouseCapture(self: UIElement)
            Releases the mouse capture, if this element held the capture.
        """
        pass

    def ReleaseStylusCapture(self):
        """
        ReleaseStylusCapture(self: UIElement)
            Releases the stylus device capture, if this element held the capture.
        """
        pass

    def ReleaseTouchCapture(self, touchDevice):
        """
        ReleaseTouchCapture(self: UIElement, touchDevice: TouchDevice) -> bool
        
            Attempts to release the specified touch device from this element.
        
            touchDevice: The device to release.
            Returns: true if the touch device is released; otherwise, false.
        """
        pass

    def RemoveHandler(self, routedEvent, handler):
        """
        RemoveHandler(self: UIElement, routedEvent: RoutedEvent, handler: Delegate)
            Removes the specified routed event handler from this element.
        
            routedEvent: The identifier of the�routed event for which the handler is attached.
            handler: The specific handler implementation to remove from the event handler collection on this element.
        """
        pass

    def RemoveVisualChild(self, *args): #cannot find CLR method
        """
        RemoveVisualChild(self: Visual, child: Visual)
            Removes the parent-child relationship between two visuals.
        
            child: The child visual object to remove from the parent visual.
        """
        pass

    def ShouldSerializeCommandBindings(self):
        """
        ShouldSerializeCommandBindings(self: UIElement) -> bool
        
            Returns whether serialization processes should serialize the contents of the System.Windows.UIElement.CommandBindings property on instances of this class.
            Returns: true if the System.Windows.UIElement.CommandBindings property value should be serialized; otherwise, false.
        """
        pass

    def ShouldSerializeInputBindings(self):
        """
        ShouldSerializeInputBindings(self: UIElement) -> bool
        
            Returns whether serialization processes should serialize the contents of the System.Windows.UIElement.InputBindings property on instances of this class.
            Returns: true if the System.Windows.UIElement.InputBindings property value should be serialized; otherwise, false.
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

    def TranslatePoint(self, point, relativeTo):
        """
        TranslatePoint(self: UIElement, point: Point, relativeTo: UIElement) -> Point
        
            Translates a point relative to this element to coordinates that are relative to the specified element.
        
            point: The point value, as relative to this element.
            relativeTo: The element to translate the given point into.
            Returns: A point value, now relative to the target element rather than this source element.
        """
        pass

    def UpdateLayout(self):
        """
        UpdateLayout(self: UIElement)
            Ensures that all visual child elements of this element are properly updated for layout.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AllowDrop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether this element can be used as the target of a drag-and-drop operation.  This is a dependency property.

Get: AllowDrop(self: UIElement) -> bool

Set: AllowDrop(self: UIElement) = value
"""

    AreAnyTouchesCaptured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether at least one touch is captured to this element.

Get: AreAnyTouchesCaptured(self: UIElement) -> bool

"""

    AreAnyTouchesCapturedWithin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether at least one touch is captured to this element or to any child elements in its visual tree.

Get: AreAnyTouchesCapturedWithin(self: UIElement) -> bool

"""

    AreAnyTouchesDirectlyOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether at least one touch is pressed over this element.

Get: AreAnyTouchesDirectlyOver(self: UIElement) -> bool

"""

    AreAnyTouchesOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether at least one touch is pressed over this element or any child elements in its visual tree.

Get: AreAnyTouchesOver(self: UIElement) -> bool

"""

    BitmapEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a bitmap effect that applies directly to the rendered content for this element.  This is a dependency property.

Get: BitmapEffect(self: UIElement) -> BitmapEffect

Set: BitmapEffect(self: UIElement) = value
"""

    BitmapEffectInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an input source for the bitmap effect that applies directly to the rendered content for this element.  This is a dependency property.

Get: BitmapEffectInput(self: UIElement) -> BitmapEffectInput

Set: BitmapEffectInput(self: UIElement) = value
"""

    CacheMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a cached representation of the System.Windows.UIElement.

Get: CacheMode(self: UIElement) -> CacheMode

Set: CacheMode(self: UIElement) = value
"""

    Clip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the geometry used to define the outline of the contents of an element.  This is a dependency property.

Get: Clip(self: UIElement) -> Geometry

Set: Clip(self: UIElement) = value
"""

    ClipToBounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to clip the content of this element (or content coming from the child elements of this element) to fit into the size of the containing element.   This is a dependency property.

Get: ClipToBounds(self: UIElement) -> bool

Set: ClipToBounds(self: UIElement) = value
"""

    CommandBindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.Windows.Input.CommandBinding objects associated with this element. A System.Windows.Input.CommandBinding enables command handling for this element, and declares the linkage between a command, its events, and the handlers attached by this element.

Get: CommandBindings(self: UIElement) -> CommandBindingCollection

"""

    DesiredSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size that this element computed during the measure pass of the layout process.

Get: DesiredSize(self: UIElement) -> Size

"""

    Effect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the bitmap effect to apply to the System.Windows.UIElement. This is a dependency property.

Get: Effect(self: UIElement) -> Effect

Set: Effect(self: UIElement) = value
"""

    Focusable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the element can receive focus.  This is a dependency property.

Get: Focusable(self: UIElement) -> bool

Set: Focusable(self: UIElement) = value
"""

    HasAnimatedProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this element has any animated properties.

Get: HasAnimatedProperties(self: UIElement) -> bool

"""

    HasEffectiveKeyboardFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InputBindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of input bindings associated with this element.

Get: InputBindings(self: UIElement) -> InputBindingCollection

"""

    IsArrangeValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the computed size and position of child elements in this element's layout are valid.

Get: IsArrangeValid(self: UIElement) -> bool

"""

    IsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether this element is enabled in the user interface (UI).  This is a dependency property.

Get: IsEnabled(self: UIElement) -> bool

Set: IsEnabled(self: UIElement) = value
"""

    IsEnabledCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.

"""

    IsFocused = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that determines whether this element has logical focus.  This is a dependency property.

Get: IsFocused(self: UIElement) -> bool

"""

    IsHitTestVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that declares whether this element can possibly be returned as a hit test result from some portion of its rendered content. This is a dependency property.

Get: IsHitTestVisible(self: UIElement) -> bool

Set: IsHitTestVisible(self: UIElement) = value
"""

    IsInputMethodEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether an input method system, such as an Input Method Editor (IME),  is enabled for processing the input to this element.

Get: IsInputMethodEnabled(self: UIElement) -> bool

"""

    IsKeyboardFocused = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this element has keyboard focus.  This is a dependency property.

Get: IsKeyboardFocused(self: UIElement) -> bool

"""

    IsKeyboardFocusWithin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether keyboard focus is anywhere within the element or its visual tree child elements.  This is a dependency property.

Get: IsKeyboardFocusWithin(self: UIElement) -> bool

"""

    IsManipulationEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether manipulation events are enabled on this System.Windows.UIElement.

Get: IsManipulationEnabled(self: UIElement) -> bool

Set: IsManipulationEnabled(self: UIElement) = value
"""

    IsMeasureValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current size returned by layout measure is valid.

Get: IsMeasureValid(self: UIElement) -> bool

"""

    IsMouseCaptured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the mouse is captured to this element.  This is a dependency property.

Get: IsMouseCaptured(self: UIElement) -> bool

"""

    IsMouseCaptureWithin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that determines whether mouse capture is held by this element or by child elements in its visual tree. This is a dependency property.

Get: IsMouseCaptureWithin(self: UIElement) -> bool

"""

    IsMouseDirectlyOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the position of the mouse pointer corresponds to�hit test results, which take element compositing into account.  This is a dependency property.

Get: IsMouseDirectlyOver(self: UIElement) -> bool

"""

    IsMouseOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the mouse pointer is located over this element (including child elements in the visual tree).  This is a dependency property.

Get: IsMouseOver(self: UIElement) -> bool

"""

    IsStylusCaptured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the stylus is captured by this element.  This is a dependency property.

Get: IsStylusCaptured(self: UIElement) -> bool

"""

    IsStylusCaptureWithin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that determines whether stylus capture is held by this element, or an element within the element bounds and its visual tree. This is a dependency property.

Get: IsStylusCaptureWithin(self: UIElement) -> bool

"""

    IsStylusDirectlyOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the stylus position corresponds to�hit test results, which take element compositing into account.  This is a dependency property.

Get: IsStylusDirectlyOver(self: UIElement) -> bool

"""

    IsStylusOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the stylus cursor is located over this element (including visual child elements).  This is a dependency property.

Get: IsStylusOver(self: UIElement) -> bool

"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this element is visible in the user interface (UI).  This is a dependency property.

Get: IsVisible(self: UIElement) -> bool

"""

    Opacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the opacity factor applied to the entire System.Windows.UIElement when it is rendered in the user interface (UI).  This is a dependency property.

Get: Opacity(self: UIElement) -> float

Set: Opacity(self: UIElement) = value
"""

    OpacityMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an opacity mask, as a System.Windows.Media.Brush implementation that is applied to any alpha-channel masking for the rendered content of this element.  This is a dependency property.

Get: OpacityMask(self: UIElement) -> Brush

Set: OpacityMask(self: UIElement) = value
"""

    PersistId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that uniquely identifies this element.

Get: PersistId(self: UIElement) -> int

"""

    RenderSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets (or sets, but see Remarks) the final render size of this element.

Get: RenderSize(self: UIElement) -> Size

Set: RenderSize(self: UIElement) = value
"""

    RenderTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets transform information that affects the rendering position of this element.  This is a dependency property.

Get: RenderTransform(self: UIElement) -> Transform

Set: RenderTransform(self: UIElement) = value
"""

    RenderTransformOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the center point of any possible render transform declared by System.Windows.UIElement.RenderTransform, relative to the bounds of the element.  This is a dependency property.

Get: RenderTransformOrigin(self: UIElement) -> Point

Set: RenderTransformOrigin(self: UIElement) = value
"""

    SnapsToDevicePixels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines whether rendering for this element should use device-specific pixel settings during rendering.  This is a dependency property.

Get: SnapsToDevicePixels(self: UIElement) -> bool

Set: SnapsToDevicePixels(self: UIElement) = value
"""

    StylusPlugIns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all stylus plug-in (customization) objects associated with this element.

"""

    TouchesCaptured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all touch devices that are captured to this element.

Get: TouchesCaptured(self: UIElement) -> IEnumerable[TouchDevice]

"""

    TouchesCapturedWithin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all touch devices that are captured to this element or any child elements in its visual tree.

Get: TouchesCapturedWithin(self: UIElement) -> IEnumerable[TouchDevice]

"""

    TouchesDirectlyOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all touch devices that are over this element.

Get: TouchesDirectlyOver(self: UIElement) -> IEnumerable[TouchDevice]

"""

    TouchesOver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all touch devices that are over this element or any child elements in its visual tree.

Get: TouchesOver(self: UIElement) -> IEnumerable[TouchDevice]

"""

    Uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the unique identifier (for localization) for this element. This is a dependency property.

Get: Uid(self: UIElement) -> str

Set: Uid(self: UIElement) = value
"""

    Visibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the user interface (UI) visibility of this element.  This is a dependency property.

Get: Visibility(self: UIElement) -> Visibility

Set: Visibility(self: UIElement) = value
"""

    VisualBitmapEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffect value for the System.Windows.Media.Visual.

"""

    VisualBitmapEffectInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffectInput value for the System.Windows.Media.Visual.

"""

    VisualBitmapScalingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.BitmapScalingMode for the System.Windows.Media.Visual.

"""

    VisualCacheMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a cached representation of the System.Windows.Media.Visual.

"""

    VisualChildrenCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of child elements for the System.Windows.Media.Visual.

"""

    VisualClearTypeHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.ClearTypeHint that determines how ClearType is rendered in the System.Windows.Media.Visual.

"""

    VisualClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the clip region of the System.Windows.Media.Visual as a System.Windows.Media.Geometry value.

"""

    VisualEdgeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the edge mode of the System.Windows.Media.Visual as an System.Windows.Media.EdgeMode value.

"""

    VisualEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the bitmap effect to apply to the System.Windows.Media.Visual.

"""

    VisualOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the offset value of the visual object.

"""

    VisualOpacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the opacity of the System.Windows.Media.Visual.

"""

    VisualOpacityMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Brush value that represents the opacity mask of the System.Windows.Media.Visual.

"""

    VisualParent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual tree parent of the visual object.

"""

    VisualScrollableAreaClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a clipped scrollable area for the System.Windows.Media.Visual.

"""

    VisualTextHintingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextHintingMode of the System.Windows.Media.Visual.

"""

    VisualTextRenderingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextRenderingMode of the System.Windows.Media.Visual.

"""

    VisualTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Transform value for the System.Windows.Media.Visual.

"""

    VisualXSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate (vertical) guideline collection.

"""

    VisualYSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate (horizontal) guideline collection.

"""


    AllowDropProperty = None
    AreAnyTouchesCapturedProperty = None
    AreAnyTouchesCapturedWithinProperty = None
    AreAnyTouchesDirectlyOverProperty = None
    AreAnyTouchesOverProperty = None
    BitmapEffectInputProperty = None
    BitmapEffectProperty = None
    CacheModeProperty = None
    ClipProperty = None
    ClipToBoundsProperty = None
    DragEnter = None
    DragEnterEvent = None
    DragLeave = None
    DragLeaveEvent = None
    DragOver = None
    DragOverEvent = None
    Drop = None
    DropEvent = None
    EffectProperty = None
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
    IsManipulationEnabledProperty = None
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
    LayoutUpdated = None
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
    ManipulationBoundaryFeedback = None
    ManipulationBoundaryFeedbackEvent = None
    ManipulationCompleted = None
    ManipulationCompletedEvent = None
    ManipulationDelta = None
    ManipulationDeltaEvent = None
    ManipulationInertiaStarting = None
    ManipulationInertiaStartingEvent = None
    ManipulationStarted = None
    ManipulationStartedEvent = None
    ManipulationStarting = None
    ManipulationStartingEvent = None
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
    OpacityMaskProperty = None
    OpacityProperty = None
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
    RenderTransformOriginProperty = None
    RenderTransformProperty = None
    SnapsToDevicePixelsProperty = None
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
    UidProperty = None
    VisibilityProperty = None

