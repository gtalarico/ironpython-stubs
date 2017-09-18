class TextBoxBase(Control,IResource,IAnimatable,IInputElement,IFrameworkInputElement,ISupportInitialize,IHaveResources,IQueryAmbient):
 """ An abstract base class that provides functionality for text editing controls,including System.Windows.Controls.TextBox and System.Windows.Controls.RichTextBox. """
 def AddLogicalChild(self,*args):
  """
  AddLogicalChild(self: FrameworkElement,child: object)

   Adds the provided object to the logical tree of this element.

  

   child: Child element to be added.
  """
  pass
 def AddVisualChild(self,*args):
  """
  AddVisualChild(self: Visual,child: Visual)

   Defines the parent-child relationship between two visuals.

  

   child: The child visual object to add to parent visual.
  """
  pass
 def AppendText(self,textData):
  """
  AppendText(self: TextBoxBase,textData: str)

   Appends a string to the contents of a text control.

  

   textData: A string that specifies the text to append to the current contents of the text control.
  """
  pass
 def ArrangeCore(self,*args):
  """
  ArrangeCore(self: FrameworkElement,finalRect: Rect)

   Implements System.Windows.UIElement.ArrangeCore(System.Windows.Rect) (defined as virtual in 

    System.Windows.UIElement) and seals the implementation.

  

  

   finalRect: The final area within the parent that this element should use to arrange itself and its children.
  """
  pass
 def ArrangeOverride(self,*args):
  """
  ArrangeOverride(self: Control,arrangeBounds: Size) -> Size

  

   Called to arrange and size the content of a System.Windows.Controls.Control object.

  

   arrangeBounds: The computed size that is used to arrange the content.

   Returns: The size of the control.
  """
  pass
 def BeginChange(self):
  """
  BeginChange(self: TextBoxBase)

   Begins a change block.
  """
  pass
 def Copy(self):
  """
  Copy(self: TextBoxBase)

   Copies the current selection of the text editing control to the System.Windows.Clipboard.
  """
  pass
 def Cut(self):
  """
  Cut(self: TextBoxBase)

   Removes the current selection from the text editing control and copies it to the 

    System.Windows.Clipboard.
  """
  pass
 def DeclareChangeBlock(self):
  """
  DeclareChangeBlock(self: TextBoxBase) -> IDisposable

  

   Creates a change block.

   Returns: An System.IDisposable object that refers to a new change block.
  """
  pass
 def EndChange(self):
  """
  EndChange(self: TextBoxBase)

   Ends a change block.
  """
  pass
 def GetLayoutClip(self,*args):
  """
  GetLayoutClip(self: FrameworkElement,layoutSlotSize: Size) -> Geometry

  

   Returns a geometry for a clipping mask. The mask applies if the layout system attempts to 

    arrange an element that is larger than the available display space.

  

  

   layoutSlotSize: The size of the part of the element that does visual presentation.

   Returns: The clipping geometry.
  """
  pass
 def GetTemplateChild(self,*args):
  """
  GetTemplateChild(self: FrameworkElement,childName: str) -> DependencyObject

  

   Returns the named element in the visual tree of an instantiated 

    System.Windows.Controls.ControlTemplate.

  

  

   childName: Name of the child to find.

   Returns: The requested element. May be null if no element of the requested name exists.
  """
  pass
 def GetUIParentCore(self,*args):
  """
  GetUIParentCore(self: FrameworkElement) -> DependencyObject

  

   Returns an alternative logical parent for this element if there is no visual parent.

   Returns: Returns something other than null whenever a WPF framework-level implementation of this method 

    has a non-visual parent connection.
  """
  pass
 def GetVisualChild(self,*args):
  """
  GetVisualChild(self: FrameworkElement,index: int) -> Visual

  

   Overrides System.Windows.Media.Visual.GetVisualChild(System.Int32),and returns a child at the 

    specified index from a collection of child elements.

  

  

   index: The zero-based index of the requested child element in the collection.

   Returns: The requested child element. This should not return null; if the provided index is out of range,

    an exception is thrown.
  """
  pass
 def HitTestCore(self,*args):
  """
  HitTestCore(self: UIElement,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult

  

   Implements 

    System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestParameters) to 

    supply base element hit testing behavior (returning System.Windows.Media.GeometryHitTestResult).

  

  

   hitTestParameters: Describes the hit test to perform,including the initial hit point.

   Returns: Results of the test,including the evaluated geometry.

  HitTestCore(self: UIElement,hitTestParameters: PointHitTestParameters) -> HitTestResult

  

   Implements System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParameters) 

    to supply base element hit testing behavior (returning System.Windows.Media.HitTestResult).

  

  

   hitTestParameters: Describes the hit test to perform,including the initial hit point.

   Returns: Results of the test,including the evaluated point.
  """
  pass
 def LineDown(self):
  """
  LineDown(self: TextBoxBase)

   Scrolls the contents of the control down by one line.
  """
  pass
 def LineLeft(self):
  """
  LineLeft(self: TextBoxBase)

   Scrolls the contents of the control to the left by one line.
  """
  pass
 def LineRight(self):
  """
  LineRight(self: TextBoxBase)

   Scrolls the contents of the control to the right by one line.
  """
  pass
 def LineUp(self):
  """
  LineUp(self: TextBoxBase)

   Scrolls the contents of the control upward by one line.
  """
  pass
 def LockCurrentUndoUnit(self):
  """
  LockCurrentUndoUnit(self: TextBoxBase)

   Locks the most recent undo unit of the undo stack of the application. This prevents the locked 

    unit from being merged with undo units that are added subsequently.
  """
  pass
 def MeasureCore(self,*args):
  """
  MeasureCore(self: FrameworkElement,availableSize: Size) -> Size

  

   Implements basic measure-pass layout system behavior for System.Windows.FrameworkElement.

  

   availableSize: The available size that the parent element can give to the child elements.

   Returns: The desired size of this element in layout.
  """
  pass
 def MeasureOverride(self,*args):
  """
  MeasureOverride(self: Control,constraint: Size) -> Size

  

   Called to remeasure a control.

  

   constraint: The maximum size that the method can return.

   Returns: The size of the control,up to the maximum specified by constraint.
  """
  pass
 def OnAccessKey(self,*args):
  """
  OnAccessKey(self: UIElement,e: AccessKeyEventArgs)

   Provides class handling for when an access key that is meaningful for this element is invoked.

  

   e: The event data to the access key event. The event data reports which key was invoked,and 

    indicate whether the System.Windows.Input.AccessKeyManager object that controls the sending of 

    these events also sent this access key invocation to other elements.
  """
  pass
 def OnApplyTemplate(self):
  """
  OnApplyTemplate(self: TextBoxBase)

   Is called when a control template is applied.
  """
  pass
 def OnChildDesiredSizeChanged(self,*args):
  """
  OnChildDesiredSizeChanged(self: UIElement,child: UIElement)

   Supports layout behavior when a child element is resized.

  

   child: The child element that is being resized.
  """
  pass
 def OnContextMenuClosing(self,*args):
  """
  OnContextMenuClosing(self: FrameworkElement,e: ContextMenuEventArgs)

   Invoked whenever an unhandled System.Windows.FrameworkElement.ContextMenuClosing routed event 

    reaches this class in its route. Implement this method to add class handling for this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnContextMenuOpening(self,*args):
  """
  OnContextMenuOpening(self: TextBoxBase,e: ContextMenuEventArgs)

   Called whenever an unhandled System.Windows.FrameworkElement.ContextMenuOpening routed event 

    reaches this class in its route. Implement this method to add class handling for this event.

  

  

   e: Arguments of the event.
  """
  pass
 def OnCreateAutomationPeer(self,*args):
  """
  OnCreateAutomationPeer(self: UIElement) -> AutomationPeer

  

   Returns class-specific System.Windows.Automation.Peers.AutomationPeer implementations for the 

    Windows Presentation Foundation (WPF) infrastructure.

  

   Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
  """
  pass
 def OnDpiChanged(self,*args):
  """ OnDpiChanged(self: Visual,oldDpi: DpiScale,newDpi: DpiScale) """
  pass
 def OnDragEnter(self,*args):
  """
  OnDragEnter(self: TextBoxBase,e: DragEventArgs)

   Invoked whenever an unhandled System.Windows.DragDrop.DragEnter attached routed event reaches an 

    element derived from this class in its route. Implement this method to add class handling for 

    this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnDragLeave(self,*args):
  """
  OnDragLeave(self: TextBoxBase,e: DragEventArgs)

   Invoked whenever an unhandled System.Windows.DragDrop.DragLeave attached routed event reaches an 

    element derived from this class in its route. Implement this method to add class handling for 

    this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnDragOver(self,*args):
  """
  OnDragOver(self: TextBoxBase,e: DragEventArgs)

   Invoked whenever an unhandled System.Windows.DragDrop.DragOver attached routed event reaches an 

    element derived from this class in its route. Implement this method to add class handling for 

    this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnDrop(self,*args):
  """
  OnDrop(self: TextBoxBase,e: DragEventArgs)

   Invoked whenever an unhandled System.Windows.DragDrop.DragEnter attached routed event reaches an 

    element derived from this class in its route. Implement this method to add class handling for 

    this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnGiveFeedback(self,*args):
  """
  OnGiveFeedback(self: TextBoxBase,e: GiveFeedbackEventArgs)

   Invoked whenever an unhandled System.Windows.DragDrop.GiveFeedback attached routed event reaches 

    an element derived from this class in its route. Implement this method to add class handling for 

    this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnGotFocus(self,*args):
  """
  OnGotFocus(self: FrameworkElement,e: RoutedEventArgs)

   Invoked whenever an unhandled System.Windows.UIElement.GotFocus event reaches this element in 

    its route.

  

  

   e: The System.Windows.RoutedEventArgs that contains the event data.
  """
  pass
 def OnGotKeyboardFocus(self,*args):
  """
  OnGotKeyboardFocus(self: TextBoxBase,e: KeyboardFocusChangedEventArgs)

   Invoked whenever an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus attached routed 

    event reaches an element derived from this class in its route. Implement this method to add 

    class handling for this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnGotMouseCapture(self,*args):
  """
  OnGotMouseCapture(self: UIElement,e: MouseEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  """
  pass
 def OnGotStylusCapture(self,*args):
  """
  OnGotStylusCapture(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnGotTouchCapture(self,*args):
  """
  OnGotTouchCapture(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.GotTouchCapture routed event that 

    occurs when a touch is captured to this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnInitialized(self,*args):
  """
  OnInitialized(self: FrameworkElement,e: EventArgs)

   Raises the System.Windows.FrameworkElement.Initialized event. This method is invoked whenever 

    System.Windows.FrameworkElement.IsInitialized is set to true internally.

  

  

   e: The System.Windows.RoutedEventArgs that contains the event data.
  """
  pass
 def OnIsKeyboardFocusedChanged(self,*args):
  """
  OnIsKeyboardFocusedChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)

   Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged event is raised on 

    this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
  """
  pass
 def OnIsKeyboardFocusWithinChanged(self,*args):
  """
  OnIsKeyboardFocusWithinChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)

   Invoked just before the System.Windows.UIElement.IsKeyboardFocusWithinChanged event is raised by 

    this element. Implement this method to add class handling for this event.

  

  

   e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
  """
  pass
 def OnIsMouseCapturedChanged(self,*args):
  """
  OnIsMouseCapturedChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)

   Invoked when an unhandled System.Windows.UIElement.IsMouseCapturedChanged event is raised on 

    this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
  """
  pass
 def OnIsMouseCaptureWithinChanged(self,*args):
  """
  OnIsMouseCaptureWithinChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)

   Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged event is raised 

    on this element. Implement this method to add class handling for this event.

  

  

   e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
  """
  pass
 def OnIsMouseDirectlyOverChanged(self,*args):
  """
  OnIsMouseDirectlyOverChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)

   Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged event is raised on 

    this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
  """
  pass
 def OnIsStylusCapturedChanged(self,*args):
  """
  OnIsStylusCapturedChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)

   Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged event is raised on 

    this element. Implement this method to add class handling for this event.

  

  

   e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
  """
  pass
 def OnIsStylusCaptureWithinChanged(self,*args):
  """
  OnIsStylusCaptureWithinChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)

   Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged event is raised 

    on this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
  """
  pass
 def OnIsStylusDirectlyOverChanged(self,*args):
  """
  OnIsStylusDirectlyOverChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)

   Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged event is raised 

    on this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
  """
  pass
 def OnKeyDown(self,*args):
  """
  OnKeyDown(self: TextBoxBase,e: KeyEventArgs)

   Invoked whenever an unhandled System.Windows.Input.Keyboard.KeyDown attached routed event 

    reaches an element derived from this class in its route. Implement this method to add class 

    handling for this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnKeyUp(self,*args):
  """
  OnKeyUp(self: TextBoxBase,e: KeyEventArgs)

   Invoked whenever an unhandled System.Windows.Input.Keyboard.KeyUp attached routed event reaches 

    an element derived from this class in its route. Implement this method to add class handling for 

    this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnLostFocus(self,*args):
  """
  OnLostFocus(self: TextBoxBase,e: RoutedEventArgs)

   Raises the System.Windows.UIElement.LostFocus event (using the provided arguments).

  

   e: Provides data about the event.
  """
  pass
 def OnLostKeyboardFocus(self,*args):
  """
  OnLostKeyboardFocus(self: TextBoxBase,e: KeyboardFocusChangedEventArgs)

   Invoked whenever an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus attached routed 

    event reaches an element derived from this class in its route. Implement this method to add 

    class handling for this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnLostMouseCapture(self,*args):
  """
  OnLostMouseCapture(self: UIElement,e: MouseEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseEventArgs that contains event data.
  """
  pass
 def OnLostStylusCapture(self,*args):
  """
  OnLostStylusCapture(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�attached event reaches 

    an element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains event data.
  """
  pass
 def OnLostTouchCapture(self,*args):
  """
  OnLostTouchCapture(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.LostTouchCapture routed event that 

    occurs when this element loses a touch capture.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnManipulationBoundaryFeedback(self,*args):
  """
  OnManipulationBoundaryFeedback(self: UIElement,e: ManipulationBoundaryFeedbackEventArgs)

   Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event occurs.

  

   e: The data for the event.
  """
  pass
 def OnManipulationCompleted(self,*args):
  """
  OnManipulationCompleted(self: UIElement,e: ManipulationCompletedEventArgs)

   Called when the System.Windows.UIElement.ManipulationCompleted event occurs.

  

   e: The data for the event.
  """
  pass
 def OnManipulationDelta(self,*args):
  """
  OnManipulationDelta(self: UIElement,e: ManipulationDeltaEventArgs)

   Called when the System.Windows.UIElement.ManipulationDelta event occurs.

  

   e: The data for the event.
  """
  pass
 def OnManipulationInertiaStarting(self,*args):
  """
  OnManipulationInertiaStarting(self: UIElement,e: ManipulationInertiaStartingEventArgs)

   Called when the System.Windows.UIElement.ManipulationInertiaStarting event occurs.

  

   e: The data for the event.
  """
  pass
 def OnManipulationStarted(self,*args):
  """
  OnManipulationStarted(self: UIElement,e: ManipulationStartedEventArgs)

   Called when the System.Windows.UIElement.ManipulationStarted event occurs.

  

   e: The data for the event.
  """
  pass
 def OnManipulationStarting(self,*args):
  """
  OnManipulationStarting(self: UIElement,e: ManipulationStartingEventArgs)

   Provides class handling for the System.Windows.UIElement.ManipulationStarting routed event that 

    occurs when the manipulation processor is first created.

  

  

   e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event data.
  """
  pass
 def OnMouseDoubleClick(self,*args):
  """
  OnMouseDoubleClick(self: Control,e: MouseButtonEventArgs)

   Raises the System.Windows.Controls.Control.MouseDoubleClick routed event.

  

   e: The event data.
  """
  pass
 def OnMouseDown(self,*args):
  """
  OnMouseDown(self: TextBoxBase,e: MouseButtonEventArgs)

   Invoked whenever an unhandled System.Windows.Input.Mouse.MouseDown attached routed event reaches 

    an element derived from this class in its route. Implement this method to add class handling for 

    this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnMouseEnter(self,*args):
  """
  OnMouseEnter(self: UIElement,e: MouseEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event is raised on this 

    element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseLeave(self,*args):
  """
  OnMouseLeave(self: UIElement,e: MouseEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event is raised on this 

    element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  """
  pass
 def OnMouseLeftButtonDown(self,*args):
  """
  OnMouseLeftButtonDown(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed event is raised on 

    this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the left mouse button was pressed.
  """
  pass
 def OnMouseLeftButtonUp(self,*args):
  """
  OnMouseLeftButtonUp(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the left mouse button was released.
  """
  pass
 def OnMouseMove(self,*args):
  """
  OnMouseMove(self: TextBoxBase,e: MouseEventArgs)

   Invoked whenever an unhandled System.Windows.Input.Mouse.MouseMove attached routed event reaches 

    an element derived from this class in its route. Implement this method to add class handling for 

    this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnMouseRightButtonDown(self,*args):
  """
  OnMouseRightButtonDown(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the right mouse button was pressed.
  """
  pass
 def OnMouseRightButtonUp(self,*args):
  """
  OnMouseRightButtonUp(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the right mouse button was released.
  """
  pass
 def OnMouseUp(self,*args):
  """
  OnMouseUp(self: TextBoxBase,e: MouseButtonEventArgs)

   Invoked whenever an unhandled System.Windows.Input.Mouse.MouseUp event reaches an element 

    derived from this class in its route. Implement this method to add class handling for this 

    event.

  

  

   e: Arguments of the event. These arguments will include details about which mouse button was 

    depressed,and the handled state.
  """
  pass
 def OnMouseWheel(self,*args):
  """
  OnMouseWheel(self: TextBoxBase,e: MouseWheelEventArgs)

   Is called when a System.Windows.UIElement.MouseWheel event is routed to this class (or to a 

    class that inherits from this class).

  

  

   e: The mouse wheel arguments that are associated with this event.
  """
  pass
 def OnPreviewDragEnter(self,*args):
  """
  OnPreviewDragEnter(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnPreviewDragLeave(self,*args):
  """
  OnPreviewDragLeave(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnPreviewDragOver(self,*args):
  """
  OnPreviewDragOver(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnPreviewDrop(self,*args):
  """
  OnPreviewDrop(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event reaches an element 

    in its route that is derived from this class. Implement this method to add class handling for 

    this event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnPreviewGiveFeedback(self,*args):
  """
  OnPreviewGiveFeedback(self: UIElement,e: GiveFeedbackEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
  """
  pass
 def OnPreviewGotKeyboardFocus(self,*args):
  """
  OnPreviewGotKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)

   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
  """
  pass
 def OnPreviewKeyDown(self,*args):
  """
  OnPreviewKeyDown(self: TextBoxBase,e: KeyEventArgs)

   Called when the System.Windows.UIElement.KeyDown occurs.

  

   e: The event data.
  """
  pass
 def OnPreviewKeyUp(self,*args):
  """
  OnPreviewKeyUp(self: UIElement,e: KeyEventArgs)

   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  """
  pass
 def OnPreviewLostKeyboardFocus(self,*args):
  """
  OnPreviewLostKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)

   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
  """
  pass
 def OnPreviewMouseDoubleClick(self,*args):
  """
  OnPreviewMouseDoubleClick(self: Control,e: MouseButtonEventArgs)

   Raises the System.Windows.Controls.Control.PreviewMouseDoubleClick routed event.

  

   e: The event data.
  """
  pass
 def OnPreviewMouseDown(self,*args):
  """
  OnPreviewMouseDown(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�routed event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that one or more mouse buttons were pressed.
  """
  pass
 def OnPreviewMouseLeftButtonDown(self,*args):
  """
  OnPreviewMouseLeftButtonDown(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�routed event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the left mouse button was pressed.
  """
  pass
 def OnPreviewMouseLeftButtonUp(self,*args):
  """
  OnPreviewMouseLeftButtonUp(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�routed event reaches 

    an element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the left mouse button was released.
  """
  pass
 def OnPreviewMouseMove(self,*args):
  """
  OnPreviewMouseMove(self: UIElement,e: MouseEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  """
  pass
 def OnPreviewMouseRightButtonDown(self,*args):
  """
  OnPreviewMouseRightButtonDown(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�routed event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the right mouse button was pressed.
  """
  pass
 def OnPreviewMouseRightButtonUp(self,*args):
  """
  OnPreviewMouseRightButtonUp(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�routed event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the right mouse button was released.
  """
  pass
 def OnPreviewMouseUp(self,*args):
  """
  OnPreviewMouseUp(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that one or more mouse buttons were released.
  """
  pass
 def OnPreviewMouseWheel(self,*args):
  """
  OnPreviewMouseWheel(self: UIElement,e: MouseWheelEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
  """
  pass
 def OnPreviewQueryContinueDrag(self,*args):
  """
  OnPreviewQueryContinueDrag(self: UIElement,e: QueryContinueDragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusButtonDown(self,*args):
  """
  OnPreviewStylusButtonDown(self: UIElement,e: StylusButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusButtonUp(self,*args):
  """
  OnPreviewStylusButtonUp(self: UIElement,e: StylusButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusDown(self,*args):
  """
  OnPreviewStylusDown(self: UIElement,e: StylusDownEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�attached event reaches 

    an element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusInAirMove(self,*args):
  """
  OnPreviewStylusInAirMove(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusInRange(self,*args):
  """
  OnPreviewStylusInRange(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusMove(self,*args):
  """
  OnPreviewStylusMove(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�attached event reaches 

    an element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusOutOfRange(self,*args):
  """
  OnPreviewStylusOutOfRange(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusSystemGesture(self,*args):
  """
  OnPreviewStylusSystemGesture(self: UIElement,e: StylusSystemGestureEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event data.
  """
  pass
 def OnPreviewStylusUp(self,*args):
  """
  OnPreviewStylusUp(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnPreviewTextInput(self,*args):
  """
  OnPreviewTextInput(self: UIElement,e: TextCompositionEventArgs)

   Invoked when an unhandled System.Windows.Input.TextCompositionManager.PreviewTextInput�attached 

    event reaches an element in its route that is derived from this class. Implement this method to 

    add class handling for this event.

  

  

   e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
  """
  pass
 def OnPreviewTouchDown(self,*args):
  """
  OnPreviewTouchDown(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.PreviewTouchDown routed event that 

    occurs when a touch presses this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnPreviewTouchMove(self,*args):
  """
  OnPreviewTouchMove(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.PreviewTouchMove routed event that 

    occurs when a touch moves while inside this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnPreviewTouchUp(self,*args):
  """
  OnPreviewTouchUp(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed event that occurs 

    when a touch is released inside this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: FrameworkElement,e: DependencyPropertyChangedEventArgs)

   Invoked whenever the effective value of any dependency property on this 

    System.Windows.FrameworkElement has been updated. The specific dependency property that changed 

    is reported in the arguments parameter. Overrides 

    System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr

    gs).

  

  

   e: The event data that describes the property that changed,as well as old and new values.
  """
  pass
 def OnQueryContinueDrag(self,*args):
  """
  OnQueryContinueDrag(self: TextBoxBase,e: QueryContinueDragEventArgs)

   Invoked whenever an unhandled System.Windows.DragDrop.QueryContinueDrag attached  routed event 

    reaches an element derived from this class in its route. Implement this method to add class 

    handling for this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnQueryCursor(self,*args):
  """
  OnQueryCursor(self: TextBoxBase,e: QueryCursorEventArgs)

   Invoked whenever an unhandled System.Windows.Input.Mouse.QueryCursor attached routed event 

    reaches an element derived from this class in its route. Implement this method to add class 

    handling for this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnRender(self,*args):
  """
  OnRender(self: UIElement,drawingContext: DrawingContext)

   When overridden in a derived class,participates in rendering operations that are directed by 

    the layout system. The rendering instructions for this element are not used directly when this 

    method is invoked,and are instead preserved for later asynchronous use by layout and drawing.

  

  

   drawingContext: The drawing instructions for a specific element. This context is provided to the layout system.
  """
  pass
 def OnRenderSizeChanged(self,*args):
  """
  OnRenderSizeChanged(self: FrameworkElement,sizeInfo: SizeChangedInfo)

   Raises the System.Windows.FrameworkElement.SizeChanged event,using the specified information as 

    part of the eventual event data.

  

  

   sizeInfo: Details of the old and new size involved in the change.
  """
  pass
 def OnSelectionChanged(self,*args):
  """
  OnSelectionChanged(self: TextBoxBase,e: RoutedEventArgs)

   Is called when the caret or current selection changes position.

  

   e: The arguments that are associated with the 

    System.Windows.Controls.Primitives.TextBoxBase.SelectionChanged event.
  """
  pass
 def OnStyleChanged(self,*args):
  """
  OnStyleChanged(self: FrameworkElement,oldStyle: Style,newStyle: Style)

   Invoked when the style in use on this element changes,which will invalidate the layout.

  

   oldStyle: The old style.

   newStyle: The new style.
  """
  pass
 def OnStylusButtonDown(self,*args):
  """
  OnStylusButtonDown(self: UIElement,e: StylusButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  """
  pass
 def OnStylusButtonUp(self,*args):
  """
  OnStylusButtonUp(self: UIElement,e: StylusButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  """
  pass
 def OnStylusDown(self,*args):
  """
  OnStylusDown(self: UIElement,e: StylusDownEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
  """
  pass
 def OnStylusEnter(self,*args):
  """
  OnStylusEnter(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached event is raised by 

    this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusInAirMove(self,*args):
  """
  OnStylusInAirMove(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusInRange(self,*args):
  """
  OnStylusInRange(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusLeave(self,*args):
  """
  OnStylusLeave(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached event is raised by 

    this element. Implement this method to add class handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusMove(self,*args):
  """
  OnStylusMove(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusOutOfRange(self,*args):
  """
  OnStylusOutOfRange(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnStylusSystemGesture(self,*args):
  """
  OnStylusSystemGesture(self: UIElement,e: StylusSystemGestureEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�attached event reaches 

    an element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event data.
  """
  pass
 def OnStylusUp(self,*args):
  """
  OnStylusUp(self: UIElement,e: StylusEventArgs)

   Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event reaches an element 

    in its route that is derived from this class. Implement this method to add class handling for 

    this event.

  

  

   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  """
  pass
 def OnTemplateChanged(self,*args):
  """
  OnTemplateChanged(self: TextBoxBase,oldTemplate: ControlTemplate,newTemplate: ControlTemplate)

   Is called when the control template changes.

  

   oldTemplate: A System.Windows.Controls.ControlTemplate object that specifies the control template that is 

    currently active.

  

   newTemplate: A System.Windows.Controls.ControlTemplate object that specifies a new control template to use.
  """
  pass
 def OnTextChanged(self,*args):
  """
  OnTextChanged(self: TextBoxBase,e: TextChangedEventArgs)

   Is called when content in this editing control changes.

  

   e: The arguments that are associated with the 

    System.Windows.Controls.Primitives.TextBoxBase.TextChanged event.
  """
  pass
 def OnTextInput(self,*args):
  """
  OnTextInput(self: TextBoxBase,e: TextCompositionEventArgs)

   Invoked whenever an unhandled System.Windows.Input.TextCompositionManager.TextInput attached 

    routed event reaches an element derived from this class in its route. Implement this method to 

    add class handling for this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnToolTipClosing(self,*args):
  """
  OnToolTipClosing(self: FrameworkElement,e: ToolTipEventArgs)

   Invoked whenever an unhandled System.Windows.FrameworkElement.ToolTipClosing routed event 

    reaches this class in its route. Implement this method to add class handling for this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnToolTipOpening(self,*args):
  """
  OnToolTipOpening(self: FrameworkElement,e: ToolTipEventArgs)

   Invoked whenever the System.Windows.FrameworkElement.ToolTipOpening routed event reaches this 

    class in its route. Implement this method to add class handling for this event.

  

  

   e: Provides data about the event.
  """
  pass
 def OnTouchDown(self,*args):
  """
  OnTouchDown(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.TouchDown routed event that occurs when 

    a touch presses inside this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnTouchEnter(self,*args):
  """
  OnTouchEnter(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.TouchEnter routed event that occurs 

    when a touch moves from outside to inside the bounds of this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnTouchLeave(self,*args):
  """
  OnTouchLeave(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.TouchLeave routed event that occurs 

    when a touch moves from inside to outside the bounds of this System.Windows.UIElement.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnTouchMove(self,*args):
  """
  OnTouchMove(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.TouchMove routed event that occurs when 

    a touch moves while inside this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnTouchUp(self,*args):
  """
  OnTouchUp(self: UIElement,e: TouchEventArgs)

   Provides class handling for the System.Windows.UIElement.TouchUp routed event that occurs when a 

    touch is released inside this element.

  

  

   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  """
  pass
 def OnVisualChildrenChanged(self,*args):
  """
  OnVisualChildrenChanged(self: Visual,visualAdded: DependencyObject,visualRemoved: DependencyObject)

   Called when the System.Windows.Media.VisualCollection of the visual object is modified.

  

   visualAdded: The System.Windows.Media.Visual that was added to the collection

   visualRemoved: The System.Windows.Media.Visual that was removed from the collection
  """
  pass
 def OnVisualParentChanged(self,*args):
  """
  OnVisualParentChanged(self: FrameworkElement,oldParent: DependencyObject)

   Invoked when the parent of this element in the visual tree is changed. Overrides 

    System.Windows.UIElement.OnVisualParentChanged(System.Windows.DependencyObject).

  

  

   oldParent: The old parent element. May be null to indicate that the element did not have a visual parent 

    previously.
  """
  pass
 def PageDown(self):
  """
  PageDown(self: TextBoxBase)

   Scrolls the contents of the control down by one page.
  """
  pass
 def PageLeft(self):
  """
  PageLeft(self: TextBoxBase)

   Scrolls the contents of the control to the left by one page.
  """
  pass
 def PageRight(self):
  """
  PageRight(self: TextBoxBase)

   Scrolls the contents of the control to the right by one page.
  """
  pass
 def PageUp(self):
  """
  PageUp(self: TextBoxBase)

   Scrolls the contents of the control up by one page.
  """
  pass
 def ParentLayoutInvalidated(self,*args):
  """
  ParentLayoutInvalidated(self: FrameworkElement,child: UIElement)

   Supports incremental layout implementations in specialized subclasses of 

    System.Windows.FrameworkElement. 

    System.Windows.FrameworkElement.ParentLayoutInvalidated(System.Windows.UIElement)  is invoked 

    when a child element has invalidated a property that is marked in metadata as affecting the 

    parent's measure or arrange passes during layout.

  

  

   child: The child element reporting the change.
  """
  pass
 def Paste(self):
  """
  Paste(self: TextBoxBase)

   Pastes the contents of the Clipboard over the current selection in the text editing control.
  """
  pass
 def Redo(self):
  """
  Redo(self: TextBoxBase) -> bool

  

   Undoes the most recent undo command. In other words,redoes the most recent undo unit on the 

    undo stack.

  

   Returns: true if the redo operation was successful; otherwise,false. This method returns false if there 

    is no undo command available (the undo stack is empty).
  """
  pass
 def RemoveLogicalChild(self,*args):
  """
  RemoveLogicalChild(self: FrameworkElement,child: object)

   Removes the provided object from this element's logical tree. System.Windows.FrameworkElement 

    updates the affected logical tree parent pointers to keep in sync with this deletion.

  

  

   child: The element to remove.
  """
  pass
 def RemoveVisualChild(self,*args):
  """
  RemoveVisualChild(self: Visual,child: Visual)

   Removes the parent-child relationship between two visuals.

  

   child: The child visual object to remove from the parent visual.
  """
  pass
 def ScrollToEnd(self):
  """
  ScrollToEnd(self: TextBoxBase)

   Scrolls the view of the editing control to the end of the content.
  """
  pass
 def ScrollToHome(self):
  """
  ScrollToHome(self: TextBoxBase)

   Scrolls the view of the editing control to the beginning of the viewport.
  """
  pass
 def ScrollToHorizontalOffset(self,offset):
  """
  ScrollToHorizontalOffset(self: TextBoxBase,offset: float)

   Scrolls the contents of the editing control to the specified horizontal offset.

  

   offset: A double value that specifies the horizontal offset to scroll to.
  """
  pass
 def ScrollToVerticalOffset(self,offset):
  """
  ScrollToVerticalOffset(self: TextBoxBase,offset: float)

   Scrolls the contents of the editing control to the specified vertical offset.

  

   offset: A double value that specifies the vertical offset to scroll to.
  """
  pass
 def SelectAll(self):
  """
  SelectAll(self: TextBoxBase)

   Selects all the contents of the text editing control.
  """
  pass
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool

  

   Returns a value that indicates whether serialization processes should serialize the value for 

    the provided dependency property.

  

  

   dp: The identifier for the dependency property that should be serialized.

   Returns: true if the dependency property that is supplied should be value-serialized; otherwise,false.
  """
  pass
 def Undo(self):
  """
  Undo(self: TextBoxBase) -> bool

  

   Undoes the most recent undo command. In other words,undoes the most recent undo unit on the 

    undo stack.

  

   Returns: true if the undo operation was successful; otherwise,false. This method returns false if the 

    undo stack is empty.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 AcceptsReturn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates how the text editing control responds when the user presses the ENTER key.



Get: AcceptsReturn(self: TextBoxBase) -> bool



Set: AcceptsReturn(self: TextBoxBase)=value

"""

 AcceptsTab=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates how the text editing control responds when the user presses the TAB key.



Get: AcceptsTab(self: TextBoxBase) -> bool



Set: AcceptsTab(self: TextBoxBase)=value

"""

 AutoWordSelection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines whether when a user selects part of a word by dragging across it with the mouse,the rest of the word is selected.



Get: AutoWordSelection(self: TextBoxBase) -> bool



Set: AutoWordSelection(self: TextBoxBase)=value

"""

 CanRedo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the most recent undo action can be redone.



Get: CanRedo(self: TextBoxBase) -> bool



"""

 CanUndo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the most recent action can be undone.



Get: CanUndo(self: TextBoxBase) -> bool



"""

 CaretBrush=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the brush that is used to paint the caret of the text box.



Get: CaretBrush(self: TextBoxBase) -> Brush



Set: CaretBrush(self: TextBoxBase)=value

"""

 DefaultStyleKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the key to use to reference the style for this control,when theme styles are used or defined.



"""

 ExtentHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the vertical size of the visible content area.



Get: ExtentHeight(self: TextBoxBase) -> float



"""

 ExtentWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the horizontal size of the visible content area.



Get: ExtentWidth(self: TextBoxBase) -> float



"""

 HandlesScrolling=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether a control supports scrolling.



"""

 HasEffectiveKeyboardFocus=property(lambda self: object(),lambda self,v: None,lambda self: None)

 HorizontalOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the horizontal scroll position.



Get: HorizontalOffset(self: TextBoxBase) -> float



"""

 HorizontalScrollBarVisibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether a horizontal scroll bar is shown.



Get: HorizontalScrollBarVisibility(self: TextBoxBase) -> ScrollBarVisibility



Set: HorizontalScrollBarVisibility(self: TextBoxBase)=value

"""

 InheritanceBehavior=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the scope limits for property value inheritance,resource key lookup,and RelativeSource FindAncestor lookup.



"""

 IsEnabledCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.



"""

 IsInactiveSelectionHighlightEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsInactiveSelectionHighlightEnabled(self: TextBoxBase) -> bool



Set: IsInactiveSelectionHighlightEnabled(self: TextBoxBase)=value

"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the text editing control is read-only to a user interacting with the control.



Get: IsReadOnly(self: TextBoxBase) -> bool



Set: IsReadOnly(self: TextBoxBase)=value

"""

 IsReadOnlyCaretVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether a read-only text box displays a caret.



Get: IsReadOnlyCaretVisible(self: TextBoxBase) -> bool



Set: IsReadOnlyCaretVisible(self: TextBoxBase)=value

"""

 IsSelectionActive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSelectionActive(self: TextBoxBase) -> bool



"""

 IsUndoEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether undo support is enabled for the text-editing control.



Get: IsUndoEnabled(self: TextBoxBase) -> bool



Set: IsUndoEnabled(self: TextBoxBase)=value

"""

 LogicalChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an enumerator for logical child elements of this element.



"""

 SelectionBrush=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the brush that highlights selected text.



Get: SelectionBrush(self: TextBoxBase) -> Brush



Set: SelectionBrush(self: TextBoxBase)=value

"""

 SelectionOpacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the opacity of the System.Windows.Controls.Primitives.TextBoxBase.SelectionBrush.



Get: SelectionOpacity(self: TextBoxBase) -> float



Set: SelectionOpacity(self: TextBoxBase)=value

"""

 SpellCheck=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Windows.Controls.SpellCheck object that provides access to spelling errors in the text contents of a System.Windows.Controls.Primitives.TextBoxBase or System.Windows.Controls.RichTextBox.



Get: SpellCheck(self: TextBoxBase) -> SpellCheck



"""

 StylusPlugIns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of all stylus plug-in (customization) objects associated with this element.



"""

 UndoLimit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of actions stored in the undo queue.



Get: UndoLimit(self: TextBoxBase) -> int



Set: UndoLimit(self: TextBoxBase)=value

"""

 VerticalOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the vertical scroll position.



Get: VerticalOffset(self: TextBoxBase) -> float



"""

 VerticalScrollBarVisibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether a vertical scroll bar is shown.



Get: VerticalScrollBarVisibility(self: TextBoxBase) -> ScrollBarVisibility



Set: VerticalScrollBarVisibility(self: TextBoxBase)=value

"""

 ViewportHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the vertical size of the scrollable content area.



Get: ViewportHeight(self: TextBoxBase) -> float



"""

 ViewportWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the horizontal size of the scrollable content area.



Get: ViewportWidth(self: TextBoxBase) -> float



"""

 VisualBitmapEffect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.Effects.BitmapEffect value for the System.Windows.Media.Visual.



"""

 VisualBitmapEffectInput=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.Effects.BitmapEffectInput value for the System.Windows.Media.Visual.



"""

 VisualBitmapScalingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.BitmapScalingMode for the System.Windows.Media.Visual.



"""

 VisualCacheMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a cached representation of the System.Windows.Media.Visual.



"""

 VisualChildrenCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of visual child elements within this element.



"""

 VisualClearTypeHint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.ClearTypeHint that determines how ClearType is rendered in the System.Windows.Media.Visual.



"""

 VisualClip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the clip region of the System.Windows.Media.Visual as a System.Windows.Media.Geometry value.



"""

 VisualEdgeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the edge mode of the System.Windows.Media.Visual as an System.Windows.Media.EdgeMode value.



"""

 VisualEffect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the bitmap effect to apply to the System.Windows.Media.Visual.



"""

 VisualOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the offset value of the visual object.



"""

 VisualOpacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the opacity of the System.Windows.Media.Visual.



"""

 VisualOpacityMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.Brush value that represents the opacity mask of the System.Windows.Media.Visual.



"""

 VisualParent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the visual tree parent of the visual object.



"""

 VisualScrollableAreaClip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a clipped scrollable area for the System.Windows.Media.Visual.



"""

 VisualTextHintingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.TextHintingMode of the System.Windows.Media.Visual.



"""

 VisualTextRenderingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.TextRenderingMode of the System.Windows.Media.Visual.



"""

 VisualTransform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.Transform value for the System.Windows.Media.Visual.



"""

 VisualXSnappingGuidelines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the x-coordinate (vertical) guideline collection.



"""

 VisualYSnappingGuidelines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the y-coordinate (horizontal) guideline collection.



"""


 AcceptsReturnProperty=None
 AcceptsTabProperty=None
 AutoWordSelectionProperty=None
 CaretBrushProperty=None
 HorizontalScrollBarVisibilityProperty=None
 IsInactiveSelectionHighlightEnabledProperty=None
 IsReadOnlyCaretVisibleProperty=None
 IsReadOnlyProperty=None
 IsSelectionActiveProperty=None
 IsUndoEnabledProperty=None
 SelectionBrushProperty=None
 SelectionChanged=None
 SelectionChangedEvent=None
 SelectionOpacityProperty=None
 TextChanged=None
 TextChangedEvent=None
 UndoLimitProperty=None
 VerticalScrollBarVisibilityProperty=None

