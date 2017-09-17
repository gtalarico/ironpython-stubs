class FrameworkContentElement(ContentElement,IInputElement,IAnimatable,IFrameworkInputElement,ISupportInitialize,IQueryAmbient):
 """
 System.Windows.FrameworkContentElement is the WPF framework-level implementation and expansion of the System.Windows.ContentElement base class. System.Windows.FrameworkContentElement adds support for additional input APIs (including tooltips and context menus),storyboards,data context for data�binding,styles support,and logical tree helper APIs.
 
 FrameworkContentElement()
 """
 def AddLogicalChild(self,*args):
  """
  AddLogicalChild(self: FrameworkContentElement,child: object)
   Adds the provided element as a child of this element.
  
   child: The child element to be added.
  """
  pass
 def BeginInit(self):
  """
  BeginInit(self: FrameworkContentElement)
   Called before an element is initialized.
  """
  pass
 def BeginStoryboard(self,storyboard,handoffBehavior=None,isControllable=None):
  """
  BeginStoryboard(self: FrameworkContentElement,storyboard: Storyboard,handoffBehavior: HandoffBehavior,isControllable: bool)
   Begins the sequence of actions that are contained in the provided storyboard,
    with specified state for control of the animation after it is started.
  
  
   storyboard: The storyboard to begin.
   handoffBehavior: A value of the enumeration that describes behavior to use if a  property 
    described in the storyboard is already animated.
  
   isControllable: Declares whether the animation is controllable (can be paused) after it is 
    started.
  
  BeginStoryboard(self: FrameworkContentElement,storyboard: Storyboard,handoffBehavior: HandoffBehavior)
   Begins the sequence of actions that are contained in the provided storyboard,
    with options specified for what should occur if the property is already 
    animated.
  
  
   storyboard: The storyboard to begin.
   handoffBehavior: A value of the enumeration that describes behavior to use if a property 
    described in the storyboard is already animated.
  
  BeginStoryboard(self: FrameworkContentElement,storyboard: Storyboard)
   Begins the sequence of actions that are contained in the provided storyboard.
  
   storyboard: The storyboard to begin.
  """
  pass
 def BringIntoView(self):
  """
  BringIntoView(self: FrameworkContentElement)
   Attempts to bring this element into view,within any scrollable regions it is 
    contained within.
  """
  pass
 def EndInit(self):
  """
  EndInit(self: FrameworkContentElement)
   Called immediately after an element is initialized.
  """
  pass
 def FindName(self,name):
  """
  FindName(self: FrameworkContentElement,name: str) -> object
  
   Finds an element that has the provided identifier name.
  
   name: Name of the element to search for.
   Returns: The requested element. May be null if no matching element was found.
  """
  pass
 def FindResource(self,resourceKey):
  """
  FindResource(self: FrameworkContentElement,resourceKey: object) -> object
  
   Searches for a resource with the specified key,and will throw an exception if 
    the requested resource is not found.
  
  
   resourceKey: Key identifier of the resource to be found.
   Returns: The found resource,or null if no matching resource was found (but will also 
    throw an exception if null).
  """
  pass
 def GetBindingExpression(self,dp):
  """
  GetBindingExpression(self: FrameworkContentElement,dp: DependencyProperty) -> BindingExpression
  
   Gets the System.Windows.Data.BindingExpression for the specified property's 
    binding.
  
  
   dp: The target System.Windows.DependencyProperty from which to get the binding.
   Returns: Returns a System.Windows.Data.BindingExpression if the target is data bound; 
    otherwise,null.
  """
  pass
 def GetUIParentCore(self,*args):
  """
  GetUIParentCore(self: FrameworkContentElement) -> DependencyObject
  
   Returns an alternative logical parent for this element if there is no visual 
    parent. In this case,a System.Windows.FrameworkContentElement  parent is 
    always the same value as the System.Windows.FrameworkContentElement.Parent 
    property.
  
   Returns: Returns something other than null whenever a WPF framework-level implementation 
    of this method has a non-visual parent connection.
  """
  pass
 def MoveFocus(self,request):
  """
  MoveFocus(self: FrameworkContentElement,request: TraversalRequest) -> bool
  
   Moves the keyboard focus from this element to another element.
  
   request: The direction that focus is to be moved,as a value of the enumeration.
   Returns: Returns true if focus is moved successfully; false if the target element in 
    direction as specified does not exist.
  """
  pass
 def OnContextMenuClosing(self,*args):
  """
  OnContextMenuClosing(self: FrameworkContentElement,e: ContextMenuEventArgs)
   Invoked whenever the System.Windows.FrameworkContentElement.ContextMenuClosing 
    routed event reaches this class in its route. Implement this method to add 
    class handling for this event.
  
  
   e: Provides data about the event.
  """
  pass
 def OnContextMenuOpening(self,*args):
  """
  OnContextMenuOpening(self: FrameworkContentElement,e: ContextMenuEventArgs)
   Invoked whenever the System.Windows.FrameworkContentElement.ContextMenuOpening 
    routed event reaches this class in its route. Implement this method to add 
    class handling for this event.
  
  
   e: Event data for the event.
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
  OnGotFocus(self: FrameworkContentElement,e: RoutedEventArgs)
   Class handler for the System.Windows.ContentElement.GotFocus event.
  
   e: Event data for the event.
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
 def OnInitialized(self,*args):
  """
  OnInitialized(self: FrameworkContentElement,e: EventArgs)
   Raises the System.Windows.FrameworkContentElement.Initialized event. This 
    method is invoked whenever System.Windows.FrameworkContentElement.IsInitialized 
    is set to true.
  
  
   e: Event data for the event.
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
  OnPropertyChanged(self: FrameworkContentElement,e: DependencyPropertyChangedEventArgs)
   Invoked whenever the effective value of any dependency property on this 
    System.Windows.FrameworkContentElement has been updated. The specific 
    dependency property that changed is reported in the arguments parameter. 
    Overrides 
    System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
    rtyChangedEventArgs).
  
  
   e: The event data that describes the property that changed,including the old and 
    new values.
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
 def OnStyleChanged(self,*args):
  """
  OnStyleChanged(self: FrameworkContentElement,oldStyle: Style,newStyle: Style)
   Invoked when the style that is in use on this element changes.
  
   oldStyle: The old style.
   newStyle: The new style.
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
 def OnToolTipClosing(self,*args):
  """
  OnToolTipClosing(self: FrameworkContentElement,e: ToolTipEventArgs)
   Invoked whenever the System.Windows.FrameworkContentElement.ToolTipClosing 
    routed event reaches this class in its route. Implement this method to add 
    class handling for this event.
  
  
   e: Provides data about the event.
  """
  pass
 def OnToolTipOpening(self,*args):
  """
  OnToolTipOpening(self: FrameworkContentElement,e: ToolTipEventArgs)
   Invoked whenever the System.Windows.FrameworkContentElement.ToolTipOpening 
    routed event reaches this class in its route. Implement this method to add 
    class handling for this event.
  
  
   e: Provides data about the event.
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
  PredictFocus(self: FrameworkContentElement,direction: FocusNavigationDirection) -> DependencyObject
  
   Determines the next element that would receive focus relative to this element 
    for a provided focus movement direction,but does not actually move the focus. 
    This method is sealed and cannot be overridden.
  
  
   direction: The direction for which a prospective focus change should be determined.
   Returns: The next element that focus would move to if focus were actually traversed. May 
    return null if focus cannot be moved relative to this element for the provided 
    direction.
  """
  pass
 def RegisterName(self,name,scopedElement):
  """
  RegisterName(self: FrameworkContentElement,name: str,scopedElement: object)
   Provides an accessor that simplifies access to the System.Windows.NameScope 
    registration method.
  
  
   name: Name to use for the specified name-object mapping.
   scopedElement: Object for the mapping.
  """
  pass
 def RemoveLogicalChild(self,*args):
  """
  RemoveLogicalChild(self: FrameworkContentElement,child: object)
   Removes the specified element from the logical tree for this element.
  
   child: The element to remove.
  """
  pass
 def SetBinding(self,dp,*__args):
  """
  SetBinding(self: FrameworkContentElement,dp: DependencyProperty,path: str) -> BindingExpression
  
   Attaches a binding to this element,based on the provided source property name 
    as a path qualification to the data source.
  
  
   dp: Identifies the bound property.
   path: The source property name or the path to the property used for the binding.
   Returns: Records the conditions of the binding. This return value can be useful for 
    error checking.
  
  SetBinding(self: FrameworkContentElement,dp: DependencyProperty,binding: BindingBase) -> BindingExpressionBase
  
   Attaches a binding to this element,based on the provided binding object.
  
   dp: Identifies the bound property.
   binding: Represents a data binding.
   Returns: Records the conditions of the binding. This return value can be useful for 
    error checking.
  """
  pass
 def SetResourceReference(self,dp,name):
  """
  SetResourceReference(self: FrameworkContentElement,dp: DependencyProperty,name: object)
   Searches for a resource with the specified name and sets up a resource 
    reference to it for the specified property.
  
  
   dp: The property to which the resource is bound.
   name: The name of the resource.
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
 def ShouldSerializeResources(self):
  """
  ShouldSerializeResources(self: FrameworkContentElement) -> bool
  
   Returns whether serialization processes should serialize the contents of the 
    System.Windows.FrameworkContentElement.Resources property on instances of this 
    class.
  
   Returns: true if the System.Windows.FrameworkContentElement.Resources property value 
    should be serialized; otherwise,false.
  """
  pass
 def ShouldSerializeStyle(self):
  """
  ShouldSerializeStyle(self: FrameworkContentElement) -> bool
  
   Returns whether serialization processes should serialize the contents of the 
    System.Windows.FrameworkContentElement.Style property on instances of this 
    class.
  
   Returns: true if the System.Windows.FrameworkContentElement.Style property value should 
    be serialized; otherwise,false.
  """
  pass
 def TryFindResource(self,resourceKey):
  """
  TryFindResource(self: FrameworkContentElement,resourceKey: object) -> object
  
   Searches for a resource with the specified key,and returns that resource if 
    found.
  
  
   resourceKey: Key identifier of the resource to be found.
   Returns: The found resource. If no resource was found,null is returned.
  """
  pass
 def UnregisterName(self,name):
  """
  UnregisterName(self: FrameworkContentElement,name: str)
   Simplifies access to the System.Windows.NameScope de-registration method.
  
   name: Name of the name-object pair to remove from the current scope.
  """
  pass
 def UpdateDefaultStyle(self):
  """ UpdateDefaultStyle(self: FrameworkContentElement) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 BindingGroup=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Data.BindingGroup that is used for the element.

Get: BindingGroup(self: FrameworkContentElement) -> BindingGroup

Set: BindingGroup(self: FrameworkContentElement)=value
"""

 ContextMenu=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the context menu element that should appear whenever the context menu is requested via user interface (UI) from within this element.

Get: ContextMenu(self: FrameworkContentElement) -> ContextMenu

Set: ContextMenu(self: FrameworkContentElement)=value
"""

 Cursor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the cursor that displays when the mouse pointer is over this element.

Get: Cursor(self: FrameworkContentElement) -> Cursor

Set: Cursor(self: FrameworkContentElement)=value
"""

 DataContext=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the data context for an element when it participates in data binding.

Get: DataContext(self: FrameworkContentElement) -> object

Set: DataContext(self: FrameworkContentElement)=value
"""

 DefaultStyleKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the key to use to find the style template for this control in themes.

"""

 FocusVisualStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object that enables customization of appearance,effects,or other style characteristics that will apply to this element when it captures keyboard focus.

Get: FocusVisualStyle(self: FrameworkContentElement) -> Style

Set: FocusVisualStyle(self: FrameworkContentElement)=value
"""

 ForceCursor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this System.Windows.FrameworkContentElement should force the user interface (UI) to render the cursor as declared by this instance's System.Windows.FrameworkContentElement.Cursor property.

Get: ForceCursor(self: FrameworkContentElement) -> bool

Set: ForceCursor(self: FrameworkContentElement)=value
"""

 InputScope=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the context for input used by this System.Windows.FrameworkContentElement.

Get: InputScope(self: FrameworkContentElement) -> InputScope

Set: InputScope(self: FrameworkContentElement)=value
"""

 IsEnabledCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that becomes the return value of System.Windows.ContentElement.IsEnabled in derived classes.

"""

 IsInitialized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this element has been initialized,either by being loaded as Extensible Application Markup Language (XAML),or by explicitly having its System.Windows.FrameworkContentElement.EndInit method called.

Get: IsInitialized(self: FrameworkContentElement) -> bool

"""

 IsLoaded=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this element has been loaded for presentation.

Get: IsLoaded(self: FrameworkContentElement) -> bool

"""

 Language=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets localization/globalization language information that applies to an individual element.

Get: Language(self: FrameworkContentElement) -> XmlLanguage

Set: Language(self: FrameworkContentElement)=value
"""

 LogicalChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an enumerator for the logical child elements of this element.

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the identifying name of the element. The name provides an instance reference so that programmatic code-behind,such as event handler code,can refer to an element once it is constructed during parsing of XAML.

Get: Name(self: FrameworkContentElement) -> str

Set: Name(self: FrameworkContentElement)=value
"""

 OverridesDefaultStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this element incorporates style properties from theme styles.

Get: OverridesDefaultStyle(self: FrameworkContentElement) -> bool

Set: OverridesDefaultStyle(self: FrameworkContentElement)=value
"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent in the logical tree for this element.

Get: Parent(self: FrameworkContentElement) -> DependencyObject

"""

 Resources=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current locally-defined resource dictionary.

Get: Resources(self: FrameworkContentElement) -> ResourceDictionary

Set: Resources(self: FrameworkContentElement)=value
"""

 Style=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style to be used by this element.

Get: Style(self: FrameworkContentElement) -> Style

Set: Style(self: FrameworkContentElement)=value
"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an arbitrary object value that can be used to store custom information about this element.

Get: Tag(self: FrameworkContentElement) -> object

Set: Tag(self: FrameworkContentElement)=value
"""

 TemplatedParent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a reference to the template parent of this element. This property is not relevant if the element was not created through a template.

Get: TemplatedParent(self: FrameworkContentElement) -> DependencyObject

"""

 ToolTip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the tool-tip object that is displayed for this element in the user interface (UI).

Get: ToolTip(self: FrameworkContentElement) -> object

Set: ToolTip(self: FrameworkContentElement)=value
"""


 BindingGroupProperty=None
 ContextMenuClosing=None
 ContextMenuClosingEvent=None
 ContextMenuOpening=None
 ContextMenuOpeningEvent=None
 ContextMenuProperty=None
 CursorProperty=None
 DataContextChanged=None
 DataContextProperty=None
 DefaultStyleKeyProperty=None
 FocusVisualStyleProperty=None
 ForceCursorProperty=None
 Initialized=None
 InputScopeProperty=None
 LanguageProperty=None
 Loaded=None
 LoadedEvent=None
 NameProperty=None
 OverridesDefaultStyleProperty=None
 SourceUpdated=None
 StyleProperty=None
 TagProperty=None
 TargetUpdated=None
 ToolTipClosing=None
 ToolTipClosingEvent=None
 ToolTipOpening=None
 ToolTipOpeningEvent=None
 ToolTipProperty=None
 Unloaded=None
 UnloadedEvent=None

