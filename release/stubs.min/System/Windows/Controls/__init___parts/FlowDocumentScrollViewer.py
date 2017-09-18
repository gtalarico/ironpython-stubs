class FlowDocumentScrollViewer(Control,IResource,IAnimatable,IInputElement,IFrameworkInputElement,ISupportInitialize,IHaveResources,IQueryAmbient,IAddChild,IServiceProvider,IJournalState):
 """
 Provides a control for viewing flow content in a continuous scrolling mode.

 

 FlowDocumentScrollViewer()
 """
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
 def CancelPrint(self):
  """
  CancelPrint(self: FlowDocumentScrollViewer)

   Cancels any current printing job.
  """
  pass
 def DecreaseZoom(self):
  """
  DecreaseZoom(self: FlowDocumentScrollViewer)

   Executes the System.Windows.Input.NavigationCommands.DecreaseZoom routed command.
  """
  pass
 def Find(self):
  """
  Find(self: FlowDocumentScrollViewer)

   Toggles the Find dialog.
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
 def IncreaseZoom(self):
  """
  IncreaseZoom(self: FlowDocumentScrollViewer)

   Executes the System.Windows.Input.NavigationCommands.IncreaseZoom routed command.
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
  OnApplyTemplate(self: FlowDocumentScrollViewer)

   Builds the visual tree for the System.Windows.Controls.FlowDocumentScrollViewer.
  """
  pass
 def OnCancelPrintCommand(self,*args):
  """
  OnCancelPrintCommand(self: FlowDocumentScrollViewer)

   Handles the System.Windows.Input.ApplicationCommands.CancelPrint�routed command.
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
  OnContextMenuOpening(self: FlowDocumentScrollViewer,e: ContextMenuEventArgs)

   Invoked whenever an unhandled System.Windows.FrameworkElement.ContextMenuOpening routed event 

    reaches this class in its route. Implement this method to add class handling for this event.

  

  

   e: Arguments of the event.
  """
  pass
 def OnCreateAutomationPeer(self,*args):
  """
  OnCreateAutomationPeer(self: FlowDocumentScrollViewer) -> AutomationPeer

  

   Creates and returns an System.Windows.Automation.Peers.AutomationPeer object for this 

    System.Windows.Controls.FlowDocumentScrollViewer.

  

   Returns: An System.Windows.Automation.Peers.AutomationPeer object for this 

    System.Windows.Controls.FlowDocumentScrollViewer.
  """
  pass
 def OnDecreaseZoomCommand(self,*args):
  """
  OnDecreaseZoomCommand(self: FlowDocumentScrollViewer)

   Handles the System.Windows.Input.NavigationCommands.DecreaseZoom�routed command.
  """
  pass
 def OnDpiChanged(self,*args):
  """ OnDpiChanged(self: Visual,oldDpi: DpiScale,newDpi: DpiScale) """
  pass
 def OnDragEnter(self,*args):
  """
  OnDragEnter(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event reaches an element in 

    its route that is derived from this class. Implement this method to add class handling for this 

    event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnDragLeave(self,*args):
  """
  OnDragLeave(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event reaches an element in 

    its route that is derived from this class. Implement this method to add class handling for this 

    event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnDragOver(self,*args):
  """
  OnDragOver(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event reaches an element in 

    its route that is derived from this class. Implement this method to add class handling for this 

    event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnDrop(self,*args):
  """
  OnDrop(self: UIElement,e: DragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event reaches an element in 

    its route that is derived from this class. Implement this method to add class handling for this 

    event.

  

  

   e: The System.Windows.DragEventArgs that contains the event data.
  """
  pass
 def OnFindCommand(self,*args):
  """
  OnFindCommand(self: FlowDocumentScrollViewer)

   Handles the System.Windows.Input.ApplicationCommands.Find�routed command.
  """
  pass
 def OnGiveFeedback(self,*args):
  """
  OnGiveFeedback(self: UIElement,e: GiveFeedbackEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event reaches an element 

    in its route that is derived from this class. Implement this method to add class handling for 

    this event.

  

  

   e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
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
  OnGotKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)

   Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�attached event reaches 

    an element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
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
 def OnIncreaseZoomCommand(self,*args):
  """
  OnIncreaseZoomCommand(self: FlowDocumentScrollViewer)

   Handles the System.Windows.Input.NavigationCommands.IncreaseZoom�routed command.
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
  OnKeyDown(self: FlowDocumentScrollViewer,e: KeyEventArgs)

   Handles the System.Windows.UIElement.KeyDown �routed event.

  

   e: A System.Windows.Input.KeyEventArgs object containing the arguments associated with the 

    System.Windows.UIElement.KeyDown routed event.
  """
  pass
 def OnKeyUp(self,*args):
  """
  OnKeyUp(self: UIElement,e: KeyEventArgs)

   Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event reaches an element 

    in its route that is derived from this class. Implement this method to add class handling for 

    this event.

  

  

   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  """
  pass
 def OnLostFocus(self,*args):
  """
  OnLostFocus(self: UIElement,e: RoutedEventArgs)

   Raises the System.Windows.UIElement.LostFocus�routed event by using the event data that is 

    provided.

  

  

   e: A System.Windows.RoutedEventArgs that contains event data. This event data must contain the 

    identifier for the System.Windows.UIElement.LostFocus event.
  """
  pass
 def OnLostKeyboardFocus(self,*args):
  """
  OnLostKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)

   Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�attached event reaches 

    an element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
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
  OnMouseDown(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event reaches an element 

    in its route that is derived from this class. Implement this method to add class handling for 

    this event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. This event data 

    reports details about the mouse button that was pressed and the handled state.
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
  OnMouseMove(self: UIElement,e: MouseEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event reaches an element 

    in its route that is derived from this class. Implement this method to add class handling for 

    this event.

  

  

   e: The System.Windows.Input.MouseEventArgs that contains the event data.
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
  OnMouseUp(self: UIElement,e: MouseButtonEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event reaches an element in 

    its route that is derived from this class. Implement this method to add class handling for this 

    event.

  

  

   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data 

    reports that the mouse button was released.
  """
  pass
 def OnMouseWheel(self,*args):
  """
  OnMouseWheel(self: FlowDocumentScrollViewer,e: MouseWheelEventArgs)

   Handles the System.Windows.UIElement.MouseWheel �routed event.

  

   e: A System.Windows.Input.MouseWheelEventArgs object containing arguments associated with the 

    System.Windows.UIElement.MouseWheel routed event.
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
  OnPreviewKeyDown(self: UIElement,e: KeyEventArgs)

   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.KeyEventArgs that contains the event data.
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
 def OnPrintCommand(self,*args):
  """
  OnPrintCommand(self: FlowDocumentScrollViewer)

   Handles the System.Windows.Input.ApplicationCommands.Print�routed command.
  """
  pass
 def OnPrintCompleted(self,*args):
  """
  OnPrintCompleted(self: FlowDocumentScrollViewer)

   Called when a printing job has completed.
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
  OnQueryContinueDrag(self: UIElement,e: QueryContinueDragEventArgs)

   Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
  """
  pass
 def OnQueryCursor(self,*args):
  """
  OnQueryCursor(self: UIElement,e: QueryCursorEventArgs)

   Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event reaches an 

    element in its route that is derived from this class. Implement this method to add class 

    handling for this event.

  

  

   e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
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
  OnTemplateChanged(self: Control,oldTemplate: ControlTemplate,newTemplate: ControlTemplate)

   Called whenever the control's template changes.

  

   oldTemplate: The old template.

   newTemplate: The new template.
  """
  pass
 def OnTextInput(self,*args):
  """
  OnTextInput(self: UIElement,e: TextCompositionEventArgs)

   Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�attached event 

    reaches an element in its route that is derived from this class. Implement this method to add 

    class handling for this event.

  

  

   e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
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
 def Print(self):
  """
  Print(self: FlowDocumentScrollViewer)

   Invokes a standard Print dialog which can be used to print the contents of the 

    System.Windows.Controls.FlowDocumentScrollViewer and configure printing preferences.
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
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool

  

   Returns a value that indicates whether serialization processes should serialize the value for 

    the provided dependency property.

  

  

   dp: The identifier for the dependency property that should be serialized.

   Returns: true if the dependency property that is supplied should be value-serialized; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 CanDecreaseZoom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.Windows.Controls.FlowDocumentScrollViewer.Zoom level can be decreased.



Get: CanDecreaseZoom(self: FlowDocumentScrollViewer) -> bool



"""

 CanIncreaseZoom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.Windows.Controls.FlowDocumentScrollViewer.Zoom level can be increased.



Get: CanIncreaseZoom(self: FlowDocumentScrollViewer) -> bool



"""

 DefaultStyleKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the key to use to reference the style for this control,when theme styles are used or defined.



"""

 Document=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Windows.Documents.FlowDocument that hosts the content to be displayed by the System.Windows.Controls.FlowDocumentScrollViewer.



Get: Document(self: FlowDocumentScrollViewer) -> FlowDocument



Set: Document(self: FlowDocumentScrollViewer)=value

"""

 HandlesScrolling=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether a control supports scrolling.



"""

 HasEffectiveKeyboardFocus=property(lambda self: object(),lambda self,v: None,lambda self: None)

 HorizontalScrollBarVisibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether a horizontal scroll bar is shown.



Get: HorizontalScrollBarVisibility(self: FlowDocumentScrollViewer) -> ScrollBarVisibility



Set: HorizontalScrollBarVisibility(self: FlowDocumentScrollViewer)=value

"""

 InheritanceBehavior=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the scope limits for property value inheritance,resource key lookup,and RelativeSource FindAncestor lookup.



"""

 IsEnabledCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.



"""

 IsInactiveSelectionHighlightEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsInactiveSelectionHighlightEnabled(self: FlowDocumentScrollViewer) -> bool



Set: IsInactiveSelectionHighlightEnabled(self: FlowDocumentScrollViewer)=value

"""

 IsSelectionActive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSelectionActive(self: FlowDocumentScrollViewer) -> bool



"""

 IsSelectionEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether selection of content within the System.Windows.Controls.FlowDocumentScrollViewer is enabled.



Get: IsSelectionEnabled(self: FlowDocumentScrollViewer) -> bool



Set: IsSelectionEnabled(self: FlowDocumentScrollViewer)=value

"""

 IsToolBarVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the System.Windows.Controls.FlowDocumentScrollViewer toolbar is visible.



Get: IsToolBarVisible(self: FlowDocumentScrollViewer) -> bool



Set: IsToolBarVisible(self: FlowDocumentScrollViewer)=value

"""

 LogicalChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an enumerator that can iterate the logical children of the System.Windows.Controls.FlowDocumentScrollViewer.



"""

 MaxZoom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum allowable System.Windows.Controls.FlowDocumentScrollViewer.Zoom level for the System.Windows.Controls.FlowDocumentScrollViewer.



Get: MaxZoom(self: FlowDocumentScrollViewer) -> float



Set: MaxZoom(self: FlowDocumentScrollViewer)=value

"""

 MinZoom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum allowable System.Windows.Controls.FlowDocumentScrollViewer.Zoom level for the System.Windows.Controls.FlowDocumentScrollViewer.



Get: MinZoom(self: FlowDocumentScrollViewer) -> float



Set: MinZoom(self: FlowDocumentScrollViewer)=value

"""

 Selection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the selected content of the System.Windows.Controls.FlowDocumentScrollViewer.



Get: Selection(self: FlowDocumentScrollViewer) -> TextSelection



"""

 SelectionBrush=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the brush that highlights the selected text.



Get: SelectionBrush(self: FlowDocumentScrollViewer) -> Brush



Set: SelectionBrush(self: FlowDocumentScrollViewer)=value

"""

 SelectionOpacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the opacity of the System.Windows.Controls.FlowDocumentScrollViewer.SelectionBrush.



Get: SelectionOpacity(self: FlowDocumentScrollViewer) -> float



Set: SelectionOpacity(self: FlowDocumentScrollViewer)=value

"""

 StylusPlugIns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of all stylus plug-in (customization) objects associated with this element.



"""

 VerticalScrollBarVisibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether a vertical scroll bar is shown.



Get: VerticalScrollBarVisibility(self: FlowDocumentScrollViewer) -> ScrollBarVisibility



Set: VerticalScrollBarVisibility(self: FlowDocumentScrollViewer)=value

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

 Zoom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current zoom level.



Get: Zoom(self: FlowDocumentScrollViewer) -> float



Set: Zoom(self: FlowDocumentScrollViewer)=value

"""

 ZoomIncrement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the zoom increment.



Get: ZoomIncrement(self: FlowDocumentScrollViewer) -> float



Set: ZoomIncrement(self: FlowDocumentScrollViewer)=value

"""


 CanDecreaseZoomProperty=None
 CanIncreaseZoomProperty=None
 DocumentProperty=None
 HorizontalScrollBarVisibilityProperty=None
 IsInactiveSelectionHighlightEnabledProperty=None
 IsSelectionActiveProperty=None
 IsSelectionEnabledProperty=None
 IsToolBarVisibleProperty=None
 MaxZoomProperty=None
 MinZoomProperty=None
 SelectionBrushProperty=None
 SelectionOpacityProperty=None
 VerticalScrollBarVisibilityProperty=None
 ZoomIncrementProperty=None
 ZoomProperty=None

