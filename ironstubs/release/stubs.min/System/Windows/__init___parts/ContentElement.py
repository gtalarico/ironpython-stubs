class ContentElement(DependencyObject,IInputElement,IAnimatable):
 """
 Provides a WPF core-level base class for content elements. Content elements are designed for flow-style presentation,using an intuitive markup-oriented layout model and a deliberately simple object model.
 
 ContentElement()
 """
 def AddHandler(self,routedEvent,handler,handledEventsToo=None):
  """
  AddHandler(self: ContentElement,routedEvent: RoutedEvent,handler: Delegate,handledEventsToo: bool)
   Adds a�routed event handler for a specified routed event,adding the handler to 
    the handler collection on the current element. Specify handledEventsToo as true 
    to have the provided handler be invoked for routed event that had already been 
    marked as handled by another element along the event route.
  
  
   routedEvent: An identifier for the.routed event to be handled.
   handler: A reference to the handler implementation.
   handledEventsToo: true to register the handler such that it is invoked even when the routed event 
    is marked handled in its event data; false to register the handler with the 
    default condition that it will not be invoked if the routed event is already 
    marked handled. The default is false.Do not routinely ask to rehandle a routed 
    event. For more information,see Remarks.
  
  AddHandler(self: ContentElement,routedEvent: RoutedEvent,handler: Delegate)
   Adds a�routed event handler for a specified routed event,adding the handler to 
    the handler collection on the current element.
  
  
   routedEvent: An identifier for the routed event to be handled.
   handler: A reference to the handler implementation.
  """
  pass
 def AddToEventRoute(self,route,e):
  """
  AddToEventRoute(self: ContentElement,route: EventRoute,e: RoutedEventArgs)
   Adds handlers to the specified System.Windows.EventRoute for the current 
    System.Windows.ContentElement event handler collection.
  
  
   route: The event route that handlers are added to.
   e: The event data that is used to add the handlers. This method uses the 
    System.Windows.RoutedEventArgs.RoutedEvent property of the arguments to create 
    the handlers.
  """
  pass
 def ApplyAnimationClock(self,dp,clock,handoffBehavior=None):
  """
  ApplyAnimationClock(self: ContentElement,dp: DependencyProperty,clock: AnimationClock,handoffBehavior: HandoffBehavior)
   Applies an animation to a specified�dependency property on this element,with 
    the ability to specify what happens if the property already has a running 
    animation.
  
  
   dp: The property to animate.
   clock: The animation clock that controls and declares the animation.
   handoffBehavior: A value of the enumeration. The default is 
    System.Windows.Media.Animation.HandoffBehavior.SnapshotAndReplace,which will 
    stop any existing animation and replace with the new one.
  
  ApplyAnimationClock(self: ContentElement,dp: DependencyProperty,clock: AnimationClock)
   Applies an animation to a specified�dependency property on this element. Any 
    existing animations are stopped and replaced with the new animation.
  
  
   dp: The identifier for the property to animate.
   clock: The animation clock that controls and declares the animation.
  """
  pass
 def BeginAnimation(self,dp,animation,handoffBehavior=None):
  """
  BeginAnimation(self: ContentElement,dp: DependencyProperty,animation: AnimationTimeline,handoffBehavior: HandoffBehavior)
   Starts a specific animation for a specified animated property on this element,
    with the option of specifying what happens if the property already has a 
    running animation.
  
  
   dp: The property to animate,which is specified as the dependency property 
    identifier.
  
   animation: The timeline of the animation to be applied.
   handoffBehavior: A value of the enumeration that specifies how the new animation interacts with 
    any current (running) animations that are already affecting the property value.
  
  BeginAnimation(self: ContentElement,dp: DependencyProperty,animation: AnimationTimeline)
   Starts an animation for a specified animated property on this element.
  
   dp: The property to animate,which is specified as a dependency property identifier.
   animation: The timeline of the animation to start.
  """
  pass
 def CaptureMouse(self):
  """
  CaptureMouse(self: ContentElement) -> bool
  
   Attempts to force capture of the mouse to this element.
   Returns: true if the mouse is successfully captured; otherwise,false.
  """
  pass
 def CaptureStylus(self):
  """
  CaptureStylus(self: ContentElement) -> bool
  
   Attempts to force capture of the stylus to this element.
   Returns: true if the stylus is successfully captured; otherwise,false.
  """
  pass
 def CaptureTouch(self,touchDevice):
  """
  CaptureTouch(self: ContentElement,touchDevice: TouchDevice) -> bool
  
   Attempts to force capture of a touch to this element.
  
   touchDevice: The device to capture.
   Returns: true if the specified touch is captured to this element; otherwise,false.
  """
  pass
 def Focus(self):
  """
  Focus(self: ContentElement) -> bool
  
   Attempts to set focus to this element.
   Returns: true if keyboard focus could be set to this element; false if this method call 
    did not force focus.
  """
  pass
 def GetAnimationBaseValue(self,dp):
  """
  GetAnimationBaseValue(self: ContentElement,dp: DependencyProperty) -> object
  
   Returns the base property value for the specified property on this element,
    disregarding any possible animated value from a running or stopped animation.
  
  
   dp: The.dependency property to check.
   Returns: The property value as if no animations are attached to the specified dependency 
    property.
  """
  pass
 def GetUIParentCore(self,*args):
  """
  GetUIParentCore(self: ContentElement) -> DependencyObject
  
   When overridden in a derived class,returns an alternative user interface (UI) 
    parent for this element if no visual parent exists.
  
   Returns: An object,if implementation of a derived class has an alternate parent 
    connection to report.
  """
  pass
 def MoveFocus(self,request):
  """
  MoveFocus(self: ContentElement,request: TraversalRequest) -> bool
  
   Attempts to move focus from this element to another element. The direction to 
    move focus is specified by a guidance direction,which is interpreted within 
    the organization of the visual parent for this element.
  
  
   request: A traversal request,which contains a property that indicates either a mode to 
    traverse in existing tab order,or a direction to move visually.
  
   Returns: true if the requested traversal was performed; otherwise,false.
  """
  pass
 def OnCreateAutomationPeer(self,*args):
  """
  OnCreateAutomationPeer(self: ContentElement) -> AutomationPeer
  
   Returns class-specific System.Windows.Automation.Peers.AutomationPeer 
    implementations for the Windows Presentation Foundation (WPF) infrastructure.
  
   Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
  """
  pass
 def OnDragEnter(self,*args):
  """
  OnDragEnter(self: ContentElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnDragLeave(self,*args):
  """
  OnDragLeave(self: ContentElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnDragOver(self,*args):
  """
  OnDragOver(self: ContentElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnDrop(self,*args):
  """
  OnDrop(self: ContentElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnGiveFeedback(self,*args):
  """
  OnGiveFeedback(self: ContentElement,e: GiveFeedbackEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
  """
  pass
 def OnGotFocus(self,*args):
  """
  OnGotFocus(self: ContentElement,e: RoutedEventArgs)
   Raises the System.Windows.ContentElement.GotFocus�routed event by using the 
    event data provided.
  
  
   e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
    contain the identifier for the System.Windows.ContentElement.GotFocus event.
  """
  pass
 def OnGotKeyboardFocus(self,*args):
  """
  OnGotKeyboardFocus(self: ContentElement,e: KeyboardFocusChangedEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
    data.
  """
  pass
 def OnGotMouseCapture(self,*args):
  """
  OnGotMouseCapture(self: ContentElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  """
  pass
 def OnGotStylusCapture(self,*args):
  """
  OnGotStylusCapture(self: ContentElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnGotTouchCapture(self,*args):
  """
  OnGotTouchCapture(self: ContentElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.ContentElement.GotTouchCapture 
    routed event that occurs when a touch is captured to this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnIsKeyboardFocusedChanged(self,*args):
  """
  OnIsKeyboardFocusedChanged(self: ContentElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled 
    System.Windows.ContentElement.IsKeyboardFocusedChanged event is raised on this 
    element. Implement this method to add class handling for this event.
  
  
   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  """
  pass
 def OnIsKeyboardFocusWithinChanged(self,*args):
  """
  OnIsKeyboardFocusWithinChanged(self: ContentElement,e: DependencyPropertyChangedEventArgs)
   Invoked just before the 
    System.Windows.ContentElement.IsKeyboardFocusWithinChanged event is raised by 
    this element. Implement this method to add class handling for this event.
  
  
   e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  """
  pass
 def OnIsMouseCapturedChanged(self,*args):
  """
  OnIsMouseCapturedChanged(self: ContentElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.ContentElement.IsMouseCapturedChanged 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  """
  pass
 def OnIsMouseCaptureWithinChanged(self,*args):
  """
  OnIsMouseCaptureWithinChanged(self: ContentElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled 
    System.Windows.ContentElement.IsMouseCaptureWithinChanged event is raised on 
    this element. Implement this method to add class handling for this event.
  
  
   e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  """
  pass
 def OnIsMouseDirectlyOverChanged(self,*args):
  """
  OnIsMouseDirectlyOverChanged(self: ContentElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled 
    System.Windows.ContentElement.IsMouseDirectlyOverChanged event is raised on 
    this element. Implement this method to add class handling for this event.
  
  
   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  """
  pass
 def OnIsStylusCapturedChanged(self,*args):
  """
  OnIsStylusCapturedChanged(self: ContentElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.ContentElement.IsStylusCapturedChanged 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  """
  pass
 def OnIsStylusCaptureWithinChanged(self,*args):
  """
  OnIsStylusCaptureWithinChanged(self: ContentElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled 
    System.Windows.ContentElement.IsStylusCaptureWithinChanged event is raised on 
    this element. Implement this method to add class handling for this event.
  
  
   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  """
  pass
 def OnIsStylusDirectlyOverChanged(self,*args):
  """
  OnIsStylusDirectlyOverChanged(self: ContentElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled 
    System.Windows.ContentElement.IsStylusDirectlyOverChanged event is raised on 
    this element. Implement this method to add class handling for this event.
  
  
   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  """
  pass
 def OnKeyDown(self,*args):
  """
  OnKeyDown(self: ContentElement,e: KeyEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.KeyDown�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  """
  pass
 def OnKeyUp(self,*args):
  """
  OnKeyUp(self: ContentElement,e: KeyEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  """
  pass
 def OnLostFocus(self,*args):
  """
  OnLostFocus(self: ContentElement,e: RoutedEventArgs)
   Raises the System.Windows.ContentElement.LostFocus�routed event by using the 
    event data that is provided.
  
  
   e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
    contain the identifier for the System.Windows.ContentElement.LostFocus event.
  """
  pass
 def OnLostKeyboardFocus(self,*args):
  """
  OnLostKeyboardFocus(self: ContentElement,e: KeyboardFocusChangedEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
  """
  pass
 def OnLostMouseCapture(self,*args):
  """
  OnLostMouseCapture(self: ContentElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains event data.
  """
  pass
 def OnLostStylusCapture(self,*args):
  """
  OnLostStylusCapture(self: ContentElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains event data.
  """
  pass
 def OnLostTouchCapture(self,*args):
  """
  OnLostTouchCapture(self: ContentElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.ContentElement.LostTouchCapture 
    routed event that occurs when this element loses a touch capture.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnMouseDown(self,*args):
  """
  OnMouseDown(self: ContentElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. 
    This event data reports details about the mouse button that was pressed and the 
    handled state.
  """
  pass
 def OnMouseEnter(self,*args):
  """
  OnMouseEnter(self: ContentElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event 
    is raised on this element. Implement this method to add class handling for this 
    event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseLeave(self,*args):
  """
  OnMouseLeave(self: ContentElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event 
    is raised on this element. Implement this method to add class handling for this 
    event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseLeftButtonDown(self,*args):
  """
  OnMouseLeftButtonDown(self: ContentElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.ContentElement.MouseLeftButtonDown�
    routed event is raised on this element. Implement this method to add class 
    handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the left mouse button was pressed.
  """
  pass
 def OnMouseLeftButtonUp(self,*args):
  """
  OnMouseLeftButtonUp(self: ContentElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.ContentElement.MouseLeftButtonUp�
    routed event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the left mouse button was released.
  """
  pass
 def OnMouseMove(self,*args):
  """
  OnMouseMove(self: ContentElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseRightButtonDown(self,*args):
  """
  OnMouseRightButtonDown(self: ContentElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.ContentElement.MouseRightButtonDown�
    routed event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the right mouse button was pressed.
  """
  pass
 def OnMouseRightButtonUp(self,*args):
  """
  OnMouseRightButtonUp(self: ContentElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.ContentElement.MouseRightButtonUp�
    routed event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the right mouse button was released.
  """
  pass
 def OnMouseUp(self,*args):
  """
  OnMouseUp(self: ContentElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the mouse button was released.
  """
  pass
 def OnMouseWheel(self,*args):
  """
  OnMouseWheel(self: ContentElement,e: MouseWheelEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
  """
  pass
 def OnPreviewDragEnter(self,*args):
  """
  OnPreviewDragEnter(self: ContentElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnPreviewDragLeave(self,*args):
  """
  OnPreviewDragLeave(self: ContentElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnPreviewDragOver(self,*args):
  """
  OnPreviewDragOver(self: ContentElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnPreviewDrop(self,*args):
  """
  OnPreviewDrop(self: ContentElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnPreviewGiveFeedback(self,*args):
  """
  OnPreviewGiveFeedback(self: ContentElement,e: GiveFeedbackEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
  """
  pass
 def OnPreviewGotKeyboardFocus(self,*args):
  """
  OnPreviewGotKeyboardFocus(self: ContentElement,e: KeyboardFocusChangedEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
    data.
  """
  pass
 def OnPreviewKeyDown(self,*args):
  """
  OnPreviewKeyDown(self: ContentElement,e: KeyEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  """
  pass
 def OnPreviewKeyUp(self,*args):
  """
  OnPreviewKeyUp(self: ContentElement,e: KeyEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  """
  pass
 def OnPreviewLostKeyboardFocus(self,*args):
  """
  OnPreviewLostKeyboardFocus(self: ContentElement,e: KeyboardFocusChangedEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
    data.
  """
  pass
 def OnPreviewMouseDown(self,*args):
  """
  OnPreviewMouseDown(self: ContentElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�
    routed event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that one or more mouse buttons were pressed.
  """
  pass
 def OnPreviewMouseLeftButtonDown(self,*args):
  """
  OnPreviewMouseLeftButtonDown(self: ContentElement,e: MouseButtonEventArgs)
   Invoked when an unhandled 
    System.Windows.ContentElement.PreviewMouseLeftButtonDown�routed event reaches 
    an element in its route that is derived from this class. Implement this method 
    to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the left mouse button was pressed.
  """
  pass
 def OnPreviewMouseLeftButtonUp(self,*args):
  """
  OnPreviewMouseLeftButtonUp(self: ContentElement,e: MouseButtonEventArgs)
   Invoked when an unhandled 
    System.Windows.ContentElement.PreviewMouseLeftButtonUp�routed event reaches an 
    element in its route that is derived from this class. Implement this method to 
    add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the left mouse button was released.
  """
  pass
 def OnPreviewMouseMove(self,*args):
  """
  OnPreviewMouseMove(self: ContentElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  """
  pass
 def OnPreviewMouseRightButtonDown(self,*args):
  """
  OnPreviewMouseRightButtonDown(self: ContentElement,e: MouseButtonEventArgs)
   Invoked when an unhandled 
    System.Windows.ContentElement.PreviewMouseRightButtonDown�routed event reaches 
    an element in its route that is derived from this class. Implement this method 
    to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the right mouse button was pressed.
  """
  pass
 def OnPreviewMouseRightButtonUp(self,*args):
  """
  OnPreviewMouseRightButtonUp(self: ContentElement,e: MouseButtonEventArgs)
   Invoked when an unhandled 
    System.Windows.ContentElement.PreviewMouseRightButtonUp�routed event reaches an 
    element in its route that is derived from this class. Implement this method to 
    add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the right mouse button was released.
  """
  pass
 def OnPreviewMouseUp(self,*args):
  """
  OnPreviewMouseUp(self: ContentElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that one or more mouse buttons were released.
  """
  pass
 def OnPreviewMouseWheel(self,*args):
  """
  OnPreviewMouseWheel(self: ContentElement,e: MouseWheelEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
  """
  pass
 def OnPreviewQueryContinueDrag(self,*args):
  """
  OnPreviewQueryContinueDrag(self: ContentElement,e: QueryContinueDragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusButtonDown(self,*args):
  """
  OnPreviewStylusButtonDown(self: ContentElement,e: StylusButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusButtonUp(self,*args):
  """
  OnPreviewStylusButtonUp(self: ContentElement,e: StylusButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusDown(self,*args):
  """
  OnPreviewStylusDown(self: ContentElement,e: StylusDownEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusInAirMove(self,*args):
  """
  OnPreviewStylusInAirMove(self: ContentElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusInRange(self,*args):
  """
  OnPreviewStylusInRange(self: ContentElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusMove(self,*args):
  """
  OnPreviewStylusMove(self: ContentElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusOutOfRange(self,*args):
  """
  OnPreviewStylusOutOfRange(self: ContentElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusSystemGesture(self,*args):
  """
  OnPreviewStylusSystemGesture(self: ContentElement,e: StylusSystemGestureEventArgs)
   Invoked when an unhandled 
    System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches 
    an element in its route that is derived from this class. Implement this method 
    to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
    data.
  """
  pass
 def OnPreviewStylusUp(self,*args):
  """
  OnPreviewStylusUp(self: ContentElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewTextInput(self,*args):
  """
  OnPreviewTextInput(self: ContentElement,e: TextCompositionEventArgs)
   Invoked when an unhandled 
    System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
  """
  pass
 def OnPreviewTouchDown(self,*args):
  """
  OnPreviewTouchDown(self: ContentElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.ContentElement.PreviewTouchDown 
    routed event that occurs when a touch presses this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnPreviewTouchMove(self,*args):
  """
  OnPreviewTouchMove(self: ContentElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.ContentElement.PreviewTouchMove 
    routed event that occurs when a touch moves while inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnPreviewTouchUp(self,*args):
  """
  OnPreviewTouchUp(self: ContentElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.ContentElement.PreviewTouchUp 
    routed event that occurs when a touch is released inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: DependencyObject,e: DependencyPropertyChangedEventArgs)
   Invoked whenever the effective value of any dependency property on this 
    System.Windows.DependencyObject has been updated. The specific dependency 
    property that changed is reported in the event data.
  
  
   e: Event data that will contain the dependency property identifier of interest,
    the property metadata for the type,and old and new values.
  
  OnPropertyChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnQueryContinueDrag(self,*args):
  """
  OnQueryContinueDrag(self: ContentElement,e: QueryContinueDragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
  """
  pass
 def OnQueryCursor(self,*args):
  """
  OnQueryCursor(self: ContentElement,e: QueryCursorEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
  """
  pass
 def OnStylusButtonDown(self,*args):
  """
  OnStylusButtonDown(self: ContentElement,e: StylusButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  """
  pass
 def OnStylusButtonUp(self,*args):
  """
  OnStylusButtonUp(self: ContentElement,e: StylusButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  """
  pass
 def OnStylusDown(self,*args):
  """
  OnStylusDown(self: ContentElement,e: StylusDownEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
  """
  pass
 def OnStylusEnter(self,*args):
  """
  OnStylusEnter(self: ContentElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached 
    event is raised by this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusInAirMove(self,*args):
  """
  OnStylusInAirMove(self: ContentElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusInRange(self,*args):
  """
  OnStylusInRange(self: ContentElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusLeave(self,*args):
  """
  OnStylusLeave(self: ContentElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached 
    event is raised by this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusMove(self,*args):
  """
  OnStylusMove(self: ContentElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusOutOfRange(self,*args):
  """
  OnStylusOutOfRange(self: ContentElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusSystemGesture(self,*args):
  """
  OnStylusSystemGesture(self: ContentElement,e: StylusSystemGestureEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
    data.
  """
  pass
 def OnStylusUp(self,*args):
  """
  OnStylusUp(self: ContentElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnTextInput(self,*args):
  """
  OnTextInput(self: ContentElement,e: TextCompositionEventArgs)
   Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
  """
  pass
 def OnTouchDown(self,*args):
  """
  OnTouchDown(self: ContentElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.ContentElement.TouchDown routed 
    event that occurs when a touch presses inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnTouchEnter(self,*args):
  """
  OnTouchEnter(self: ContentElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.ContentElement.TouchEnter routed 
    event that occurs when a touch moves from outside to inside the bounds of this 
    element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnTouchLeave(self,*args):
  """
  OnTouchLeave(self: ContentElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.ContentElement.TouchLeave routed 
    event that occurs when a touch moves from inside to outside the bounds of this 
    element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnTouchMove(self,*args):
  """
  OnTouchMove(self: ContentElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.ContentElement.TouchMove routed 
    event that occurs when a touch moves while inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnTouchUp(self,*args):
  """
  OnTouchUp(self: ContentElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.ContentElement.TouchUp routed 
    event that occurs when a touch is released inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def PredictFocus(self,direction):
  """
  PredictFocus(self: ContentElement,direction: FocusNavigationDirection) -> DependencyObject
  
   When overridden in a derived class,returns the element that would receive 
    focus for a specified focus traversal direction,without actually moving focus 
    to that element.
  
  
   direction: The direction of the requested focus traversal.
   Returns: The element that would have received focus if 
    System.Windows.ContentElement.MoveFocus(System.Windows.Input.TraversalRequest) 
    were actually invoked.
  """
  pass
 def RaiseEvent(self,e):
  """
  RaiseEvent(self: ContentElement,e: RoutedEventArgs)
   Raises a specific routed event. The System.Windows.RoutedEvent to be raised is 
    identified within the System.Windows.RoutedEventArgs instance that is provided 
    (as the System.Windows.RoutedEventArgs.RoutedEvent property of that event 
    data).
  
  
   e: A System.Windows.RoutedEventArgs that contains the event data and also 
    identifies the event to raise.
  """
  pass
 def ReleaseAllTouchCaptures(self):
  """
  ReleaseAllTouchCaptures(self: ContentElement)
   Releases all captured touch devices from this element.
  """
  pass
 def ReleaseMouseCapture(self):
  """
  ReleaseMouseCapture(self: ContentElement)
   Releases the mouse capture,if this element held the capture.
  """
  pass
 def ReleaseStylusCapture(self):
  """
  ReleaseStylusCapture(self: ContentElement)
   Releases the stylus device capture,if this element held the capture.
  """
  pass
 def ReleaseTouchCapture(self,touchDevice):
  """
  ReleaseTouchCapture(self: ContentElement,touchDevice: TouchDevice) -> bool
  
   Attempts to release the specified touch device from this element.
  
   touchDevice: The device to release.
   Returns: true if the touch device is released; otherwise,false.
  """
  pass
 def RemoveHandler(self,routedEvent,handler):
  """
  RemoveHandler(self: ContentElement,routedEvent: RoutedEvent,handler: Delegate)
   Removes the specified�routed event handler from this element.
  
   routedEvent: The identifier of the.routed event for which the handler is attached.
   handler: The specific handler implementation to remove from the event handler collection 
    on this element.
  """
  pass
 def ShouldSerializeCommandBindings(self):
  """
  ShouldSerializeCommandBindings(self: ContentElement) -> bool
  
   Returns whether serialization processes should serialize the contents of the 
    System.Windows.ContentElement.CommandBindings property on instances of this 
    class.
  
   Returns: true if the System.Windows.ContentElement.CommandBindings property value should 
    be serialized; otherwise,false.
  """
  pass
 def ShouldSerializeInputBindings(self):
  """
  ShouldSerializeInputBindings(self: ContentElement) -> bool
  
   Returns whether serialization processes should serialize the contents of the 
    System.Windows.ContentElement.InputBindings property on instances of this 
    class.
  
   Returns: true if the System.Windows.ContentElement.InputBindings property value should 
    be serialized; otherwise,false.
  """
  pass
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool
  
   Returns a value that indicates whether serialization processes should serialize 
    the value for the provided dependency property.
  
  
   dp: The identifier for the dependency property that should be serialized.
   Returns: true if the dependency property that is supplied should be value-serialized; 
    otherwise,false.
  
  ShouldSerializeProperty(self: Window_16$17,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Label_17$18,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: TextBox_18$19,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Button_19$20,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: CheckBox_20$21,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: ComboBox_21$22,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Separator_22$23,dp: DependencyProperty) -> bool
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 AllowDrop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether this element can be used as the target of a drag-and-drop operation.

Get: AllowDrop(self: ContentElement) -> bool

Set: AllowDrop(self: ContentElement)=value
"""

 AreAnyTouchesCaptured=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether at least one touch is captured to this element.

Get: AreAnyTouchesCaptured(self: ContentElement) -> bool

"""

 AreAnyTouchesCapturedWithin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether at least one touch is captured to this element or to any child elements in its visual tree.

Get: AreAnyTouchesCapturedWithin(self: ContentElement) -> bool

"""

 AreAnyTouchesDirectlyOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether at least one touch is pressed over this element.

Get: AreAnyTouchesDirectlyOver(self: ContentElement) -> bool

"""

 AreAnyTouchesOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether at least one touch is pressed over this element or any child elements in its visual tree.

Get: AreAnyTouchesOver(self: ContentElement) -> bool

"""

 CommandBindings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of System.Windows.Input.CommandBinding objects that are associated with this element.

Get: CommandBindings(self: ContentElement) -> CommandBindingCollection

"""

 Focusable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the element can receive focus.

Get: Focusable(self: ContentElement) -> bool

Set: Focusable(self: ContentElement)=value
"""

 HasAnimatedProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this element has any animated properties.

Get: HasAnimatedProperties(self: ContentElement) -> bool

"""

 InputBindings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of input bindings that are associated with this element.

Get: InputBindings(self: ContentElement) -> InputBindingCollection

"""

 IsEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether this element is enabled in the user interface (UI).

Get: IsEnabled(self: ContentElement) -> bool

Set: IsEnabled(self: ContentElement)=value
"""

 IsEnabledCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that becomes the return value of System.Windows.ContentElement.IsEnabled in derived classes.

"""

 IsFocused=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether this element has logical focus.

Get: IsFocused(self: ContentElement) -> bool

"""

 IsInputMethodEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether an input method system,such as an Input Method Editor (IME),is enabled for processing the input to this element.

Get: IsInputMethodEnabled(self: ContentElement) -> bool

"""

 IsKeyboardFocused=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this element has keyboard focus.

Get: IsKeyboardFocused(self: ContentElement) -> bool

"""

 IsKeyboardFocusWithin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether keyboard focus is anywhere within the element or child elements.

Get: IsKeyboardFocusWithin(self: ContentElement) -> bool

"""

 IsMouseCaptured=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the mouse is captured by this element.

Get: IsMouseCaptured(self: ContentElement) -> bool

"""

 IsMouseCaptureWithin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether mouse capture is held by this element or by child elements in its element�tree.

Get: IsMouseCaptureWithin(self: ContentElement) -> bool

"""

 IsMouseDirectlyOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the position of the mouse pointer corresponds to�hit test results,which take element compositing into account.

Get: IsMouseDirectlyOver(self: ContentElement) -> bool

"""

 IsMouseOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the mouse pointer is located over this element (including visual child elements,or its control compositing).

Get: IsMouseOver(self: ContentElement) -> bool

"""

 IsStylusCaptured=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the stylus is captured to this element.

Get: IsStylusCaptured(self: ContentElement) -> bool

"""

 IsStylusCaptureWithin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether stylus capture is held by this element,including child elements and control compositing.

Get: IsStylusCaptureWithin(self: ContentElement) -> bool

"""

 IsStylusDirectlyOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the stylus position corresponds to�hit test results,which take element compositing into account.

Get: IsStylusDirectlyOver(self: ContentElement) -> bool

"""

 IsStylusOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the stylus is located over this element (including visual child elements).

Get: IsStylusOver(self: ContentElement) -> bool

"""

 TouchesCaptured=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all touch devices that are captured to this element.

Get: TouchesCaptured(self: ContentElement) -> IEnumerable[TouchDevice]

"""

 TouchesCapturedWithin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all touch devices that are captured to this element or any child elements in its visual tree.

Get: TouchesCapturedWithin(self: ContentElement) -> IEnumerable[TouchDevice]

"""

 TouchesDirectlyOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all touch devices that are over this element.

Get: TouchesDirectlyOver(self: ContentElement) -> IEnumerable[TouchDevice]

"""

 TouchesOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all touch devices that are over this element or any child elements in its visual tree.

Get: TouchesOver(self: ContentElement) -> IEnumerable[TouchDevice]

"""


 AllowDropProperty=None
 AreAnyTouchesCapturedProperty=None
 AreAnyTouchesCapturedWithinProperty=None
 AreAnyTouchesDirectlyOverProperty=None
 AreAnyTouchesOverProperty=None
 DragEnter=None
 DragEnterEvent=None
 DragLeave=None
 DragLeaveEvent=None
 DragOver=None
 DragOverEvent=None
 Drop=None
 DropEvent=None
 FocusableChanged=None
 FocusableProperty=None
 GiveFeedback=None
 GiveFeedbackEvent=None
 GotFocus=None
 GotFocusEvent=None
 GotKeyboardFocus=None
 GotKeyboardFocusEvent=None
 GotMouseCapture=None
 GotMouseCaptureEvent=None
 GotStylusCapture=None
 GotStylusCaptureEvent=None
 GotTouchCapture=None
 GotTouchCaptureEvent=None
 IsEnabledChanged=None
 IsEnabledProperty=None
 IsFocusedProperty=None
 IsKeyboardFocusedChanged=None
 IsKeyboardFocusedProperty=None
 IsKeyboardFocusWithinChanged=None
 IsKeyboardFocusWithinProperty=None
 IsMouseCapturedChanged=None
 IsMouseCapturedProperty=None
 IsMouseCaptureWithinChanged=None
 IsMouseCaptureWithinProperty=None
 IsMouseDirectlyOverChanged=None
 IsMouseDirectlyOverProperty=None
 IsMouseOverProperty=None
 IsStylusCapturedChanged=None
 IsStylusCapturedProperty=None
 IsStylusCaptureWithinChanged=None
 IsStylusCaptureWithinProperty=None
 IsStylusDirectlyOverChanged=None
 IsStylusDirectlyOverProperty=None
 IsStylusOverProperty=None
 KeyDown=None
 KeyDownEvent=None
 KeyUp=None
 KeyUpEvent=None
 LostFocus=None
 LostFocusEvent=None
 LostKeyboardFocus=None
 LostKeyboardFocusEvent=None
 LostMouseCapture=None
 LostMouseCaptureEvent=None
 LostStylusCapture=None
 LostStylusCaptureEvent=None
 LostTouchCapture=None
 LostTouchCaptureEvent=None
 MouseDown=None
 MouseDownEvent=None
 MouseEnter=None
 MouseEnterEvent=None
 MouseLeave=None
 MouseLeaveEvent=None
 MouseLeftButtonDown=None
 MouseLeftButtonDownEvent=None
 MouseLeftButtonUp=None
 MouseLeftButtonUpEvent=None
 MouseMove=None
 MouseMoveEvent=None
 MouseRightButtonDown=None
 MouseRightButtonDownEvent=None
 MouseRightButtonUp=None
 MouseRightButtonUpEvent=None
 MouseUp=None
 MouseUpEvent=None
 MouseWheel=None
 MouseWheelEvent=None
 PreviewDragEnter=None
 PreviewDragEnterEvent=None
 PreviewDragLeave=None
 PreviewDragLeaveEvent=None
 PreviewDragOver=None
 PreviewDragOverEvent=None
 PreviewDrop=None
 PreviewDropEvent=None
 PreviewGiveFeedback=None
 PreviewGiveFeedbackEvent=None
 PreviewGotKeyboardFocus=None
 PreviewGotKeyboardFocusEvent=None
 PreviewKeyDown=None
 PreviewKeyDownEvent=None
 PreviewKeyUp=None
 PreviewKeyUpEvent=None
 PreviewLostKeyboardFocus=None
 PreviewLostKeyboardFocusEvent=None
 PreviewMouseDown=None
 PreviewMouseDownEvent=None
 PreviewMouseLeftButtonDown=None
 PreviewMouseLeftButtonDownEvent=None
 PreviewMouseLeftButtonUp=None
 PreviewMouseLeftButtonUpEvent=None
 PreviewMouseMove=None
 PreviewMouseMoveEvent=None
 PreviewMouseRightButtonDown=None
 PreviewMouseRightButtonDownEvent=None
 PreviewMouseRightButtonUp=None
 PreviewMouseRightButtonUpEvent=None
 PreviewMouseUp=None
 PreviewMouseUpEvent=None
 PreviewMouseWheel=None
 PreviewMouseWheelEvent=None
 PreviewQueryContinueDrag=None
 PreviewQueryContinueDragEvent=None
 PreviewStylusButtonDown=None
 PreviewStylusButtonDownEvent=None
 PreviewStylusButtonUp=None
 PreviewStylusButtonUpEvent=None
 PreviewStylusDown=None
 PreviewStylusDownEvent=None
 PreviewStylusInAirMove=None
 PreviewStylusInAirMoveEvent=None
 PreviewStylusInRange=None
 PreviewStylusInRangeEvent=None
 PreviewStylusMove=None
 PreviewStylusMoveEvent=None
 PreviewStylusOutOfRange=None
 PreviewStylusOutOfRangeEvent=None
 PreviewStylusSystemGesture=None
 PreviewStylusSystemGestureEvent=None
 PreviewStylusUp=None
 PreviewStylusUpEvent=None
 PreviewTextInput=None
 PreviewTextInputEvent=None
 PreviewTouchDown=None
 PreviewTouchDownEvent=None
 PreviewTouchMove=None
 PreviewTouchMoveEvent=None
 PreviewTouchUp=None
 PreviewTouchUpEvent=None
 QueryContinueDrag=None
 QueryContinueDragEvent=None
 QueryCursor=None
 QueryCursorEvent=None
 StylusButtonDown=None
 StylusButtonDownEvent=None
 StylusButtonUp=None
 StylusButtonUpEvent=None
 StylusDown=None
 StylusDownEvent=None
 StylusEnter=None
 StylusEnterEvent=None
 StylusInAirMove=None
 StylusInAirMoveEvent=None
 StylusInRange=None
 StylusInRangeEvent=None
 StylusLeave=None
 StylusLeaveEvent=None
 StylusMove=None
 StylusMoveEvent=None
 StylusOutOfRange=None
 StylusOutOfRangeEvent=None
 StylusSystemGesture=None
 StylusSystemGestureEvent=None
 StylusUp=None
 StylusUpEvent=None
 TextInput=None
 TextInputEvent=None
 TouchDown=None
 TouchDownEvent=None
 TouchEnter=None
 TouchEnterEvent=None
 TouchLeave=None
 TouchLeaveEvent=None
 TouchMove=None
 TouchMoveEvent=None
 TouchUp=None
 TouchUpEvent=None

