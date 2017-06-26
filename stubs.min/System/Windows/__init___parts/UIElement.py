class UIElement(Visual,IResource,IAnimatable,IInputElement):
 """
 System.Windows.UIElement is a base class for WPF core level implementations building on Windows Presentation Foundation (WPF) elements and basic presentation characteristics.
 
 UIElement()
 """
 def AddHandler(self,routedEvent,handler,handledEventsToo=None):
  """
  AddHandler(self: UIElement,routedEvent: RoutedEvent,handler: Delegate,handledEventsToo: bool)
   Adds a�routed event handler for a specified routed event,adding the handler to 
    the handler collection on the current element. Specify handledEventsToo as true 
    to have the provided handler be invoked for routed event that had already been 
    marked as handled by another element along the event route.
  
  
   routedEvent: An identifier for the�routed event to be handled.
   handler: A reference to the handler implementation.
   handledEventsToo: true to register the handler such that it is invoked even when  the routed 
    event is marked handled in its event data; false to register the handler with 
    the default condition that it will not be invoked if the routed event is 
    already marked handled. The default is false.Do not routinely ask to rehandle a 
    routed event. For more information,see Remarks.
  
  AddHandler(self: UIElement,routedEvent: RoutedEvent,handler: Delegate)
   Adds a�routed event handler for a specified routed event,adding the handler to 
    the handler collection on the current element.
  
  
   routedEvent: An identifier for the�routed event to be handled.
   handler: A reference to the handler implementation.
  """
  pass
 def AddToEventRoute(self,route,e):
  """
  AddToEventRoute(self: UIElement,route: EventRoute,e: RoutedEventArgs)
   Adds handlers to the specified System.Windows.EventRoute for the current 
    System.Windows.UIElement event handler collection.
  
  
   route: The event route that handlers are added to.
   e: The event data that is used to add the handlers. This method uses the 
    System.Windows.RoutedEventArgs.RoutedEvent property of the event data to create 
    the handlers.
  """
  pass
 def AddVisualChild(self,*args):
  """
  AddVisualChild(self: Visual,child: Visual)
   Defines the parent-child relationship between two visuals.
  
   child: The child visual object to add to parent visual.
  AddVisualChild(self: Window_16$17,child: Window_16$17)AddVisualChild(self: Label_17$18,child: Label_17$18)AddVisualChild(self: TextBox_18$19,child: TextBox_18$19)AddVisualChild(self: Button_19$20,child: Button_19$20)AddVisualChild(self: CheckBox_20$21,child: CheckBox_20$21)AddVisualChild(self: ComboBox_21$22,child: ComboBox_21$22)AddVisualChild(self: Separator_22$23,child: Separator_22$23)
  """
  pass
 def ApplyAnimationClock(self,dp,clock,handoffBehavior=None):
  """
  ApplyAnimationClock(self: UIElement,dp: DependencyProperty,clock: AnimationClock,handoffBehavior: HandoffBehavior)
   Applies an animation to a specified�dependency property on this element,with 
    the ability to specify what happens if the property already has a running 
    animation.
  
  
   dp: The property to animate.
   clock: The animation clock that controls and declares the animation.
   handoffBehavior: A value of the enumeration. The default is 
    System.Windows.Media.Animation.HandoffBehavior.SnapshotAndReplace,which will 
    stop any existing animation and replace with the new one.
  
  ApplyAnimationClock(self: UIElement,dp: DependencyProperty,clock: AnimationClock)
   Applies an animation to a specified�dependency property on this element. Any 
    existing animations are stopped and replaced with the new animation.
  
  
   dp: The identifier for the property to animate.
   clock: The animation clock that controls and declares the animation.
  """
  pass
 def Arrange(self,finalRect):
  """
  Arrange(self: UIElement,finalRect: Rect)
   Positions child elements and determines a size for a System.Windows.UIElement. 
    Parent elements call this method from their 
    System.Windows.UIElement.ArrangeCore(System.Windows.Rect) implementation (or a 
    WPF framework-level equivalent) to form a recursive layout update. This method 
    constitutes the second pass of a layout update.
  
  
   finalRect: The final size that the parent computes for the child element,provided as a 
    System.Windows.Rect instance.
  """
  pass
 def ArrangeCore(self,*args):
  """
  ArrangeCore(self: UIElement,finalRect: Rect)
   Defines the template for WPF core-level arrange layout definition.
  
   finalRect: The final area within the parent that element should use to arrange itself and 
    its child elements.
  
  ArrangeCore(self: Window_16$17,finalRect: Rect)ArrangeCore(self: Label_17$18,finalRect: Rect)ArrangeCore(self: TextBox_18$19,finalRect: Rect)ArrangeCore(self: Button_19$20,finalRect: Rect)ArrangeCore(self: CheckBox_20$21,finalRect: Rect)ArrangeCore(self: ComboBox_21$22,finalRect: Rect)ArrangeCore(self: Separator_22$23,finalRect: Rect)
  """
  pass
 def BeginAnimation(self,dp,animation,handoffBehavior=None):
  """
  BeginAnimation(self: UIElement,dp: DependencyProperty,animation: AnimationTimeline,handoffBehavior: HandoffBehavior)
   Starts a specific animation for a specified animated property on this element,
    with the option of specifying what happens if the property already has a 
    running animation.
  
  
   dp: The property to animate,which is specified as the dependency property 
    identifier.
  
   animation: The timeline of the animation to be applied.
   handoffBehavior: A value of the enumeration that specifies how the new animation interacts with 
    any current (running) animations that are already affecting the property value.
  
  BeginAnimation(self: UIElement,dp: DependencyProperty,animation: AnimationTimeline)
   Starts an animation for a specified animated property on this element.
  
   dp: The property to animate,which is specified as a dependency property identifier.
   animation: The timeline of the animation to start.
  """
  pass
 def CaptureMouse(self):
  """
  CaptureMouse(self: UIElement) -> bool
  
   Attempts to force capture of the mouse to this element.
   Returns: true if the mouse is successfully captured; otherwise,false.
  """
  pass
 def CaptureStylus(self):
  """
  CaptureStylus(self: UIElement) -> bool
  
   Attempts to force capture of the stylus to this element.
   Returns: true if the stylus was successfully captured; otherwise,false.
  """
  pass
 def CaptureTouch(self,touchDevice):
  """
  CaptureTouch(self: UIElement,touchDevice: TouchDevice) -> bool
  
   Attempts to force capture of a touch to this element.
  
   touchDevice: The device to capture.
   Returns: true if the specified touch is captured to this element; otherwise,false.
  """
  pass
 def Focus(self):
  """
  Focus(self: UIElement) -> bool
  
   Attempts to set focus to this element.
   Returns: true if keyboard focus and logical focus were set to this element; false if 
    only logical focus was set to this element,or if the call to this method did 
    not force the focus to change.
  """
  pass
 def GetAnimationBaseValue(self,dp):
  """
  GetAnimationBaseValue(self: UIElement,dp: DependencyProperty) -> object
  
   Returns the base property value for the specified property on this element,
    disregarding any possible animated value from a running or stopped animation.
  
  
   dp: The�dependency property to check.
   Returns: The property value as if no animations are attached to the specified dependency 
    property.
  """
  pass
 def GetLayoutClip(self,*args):
  """
  GetLayoutClip(self: UIElement,layoutSlotSize: Size) -> Geometry
  
   Returns an alternative clipping geometry that represents the region that would 
    be clipped if System.Windows.UIElement.ClipToBounds were set to true.
  
  
   layoutSlotSize: The available size provided by the element.
   Returns: The potential clipping geometry.
  GetLayoutClip(self: Window_16$17,layoutSlotSize: Size) -> Geometry
  GetLayoutClip(self: Label_17$18,layoutSlotSize: Size) -> Geometry
  GetLayoutClip(self: TextBox_18$19,layoutSlotSize: Size) -> Geometry
  GetLayoutClip(self: Button_19$20,layoutSlotSize: Size) -> Geometry
  GetLayoutClip(self: CheckBox_20$21,layoutSlotSize: Size) -> Geometry
  GetLayoutClip(self: ComboBox_21$22,layoutSlotSize: Size) -> Geometry
  GetLayoutClip(self: Separator_22$23,layoutSlotSize: Size) -> Geometry
  """
  pass
 def GetUIParentCore(self,*args):
  """
  GetUIParentCore(self: UIElement) -> DependencyObject
  
   When overridden in a derived class,returns an alternative user interface (UI) 
    parent for this element if no visual parent exists.
  
   Returns: An object,if implementation of a derived class has an alternate parent 
    connection to report.
  
  GetUIParentCore(self: Window_16$17) -> DependencyObject
  GetUIParentCore(self: Label_17$18) -> DependencyObject
  GetUIParentCore(self: TextBox_18$19) -> DependencyObject
  GetUIParentCore(self: Button_19$20) -> DependencyObject
  GetUIParentCore(self: CheckBox_20$21) -> DependencyObject
  GetUIParentCore(self: ComboBox_21$22) -> DependencyObject
  GetUIParentCore(self: Separator_22$23) -> DependencyObject
  """
  pass
 def GetVisualChild(self,*args):
  """
  GetVisualChild(self: Visual,index: int) -> Visual
  
   Returns the specified System.Windows.Media.Visual in the parent 
    System.Windows.Media.VisualCollection.
  
  
   index: The index of the visual object in the System.Windows.Media.VisualCollection.
   Returns: The child in the System.Windows.Media.VisualCollection at the specified index 
    value.
  
  GetVisualChild(self: Window_16$17,index: int) -> Visual
  GetVisualChild(self: Label_17$18,index: int) -> Visual
  GetVisualChild(self: TextBox_18$19,index: int) -> Visual
  GetVisualChild(self: Button_19$20,index: int) -> Visual
  GetVisualChild(self: CheckBox_20$21,index: int) -> Visual
  GetVisualChild(self: ComboBox_21$22,index: int) -> Visual
  GetVisualChild(self: Separator_22$23,index: int) -> Visual
  """
  pass
 def HitTestCore(self,*args):
  """
  HitTestCore(self: UIElement,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  
   Implements 
    System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestPara
    meters) to supply base element hit testing behavior (returning 
    System.Windows.Media.GeometryHitTestResult).
  
  
   hitTestParameters: Describes the hit test to perform,including the initial hit point.
   Returns: Results of the test,including the evaluated geometry.
  HitTestCore(self: UIElement,hitTestParameters: PointHitTestParameters) -> HitTestResult
  
   Implements 
    System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParamet
    ers) to supply base element hit testing behavior (returning 
    System.Windows.Media.HitTestResult).
  
  
   hitTestParameters: Describes the hit test to perform,including the initial hit point.
   Returns: Results of the test,including the evaluated point.
  HitTestCore(self: Window_16$17,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: Window_16$17,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: Label_17$18,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: Label_17$18,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: TextBox_18$19,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: TextBox_18$19,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: Button_19$20,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: Button_19$20,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: CheckBox_20$21,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: CheckBox_20$21,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: ComboBox_21$22,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: ComboBox_21$22,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: Separator_22$23,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: Separator_22$23,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  """
  pass
 def InputHitTest(self,point):
  """
  InputHitTest(self: UIElement,point: Point) -> IInputElement
  
   Returns the input element within the current element that is at the specified 
    coordinates,relative to the current element's origin.
  
  
   point: The offset coordinates within this element.
   Returns: The element child that is located at the given position.
  """
  pass
 def InvalidateArrange(self):
  """
  InvalidateArrange(self: UIElement)
   Invalidates the arrange state (layout) for the element. After the invalidation,
    the element will have its layout updated,which will occur asynchronously 
    unless subsequently forced by System.Windows.UIElement.UpdateLayout.
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
   Invalidates the rendering of the element,and forces a complete new layout 
    pass. System.Windows.UIElement.OnRender(System.Windows.Media.DrawingContext) is 
    called after the layout cycle is completed.
  """
  pass
 def Measure(self,availableSize):
  """
  Measure(self: UIElement,availableSize: Size)
   Updates the System.Windows.UIElement.DesiredSize of a System.Windows.UIElement. 
    Parent elements call this method from their own 
    System.Windows.UIElement.MeasureCore(System.Windows.Size) implementations to 
    form a recursive layout update. Calling this method constitutes the first pass 
    (the "Measure" pass) of a layout update.
  
  
   availableSize: The available space that a parent element can allocate a child element. A child 
    element can request a larger space than what is available; the provided size 
    might be accommodated if scrolling is possible in the content model for the 
    current element.
  """
  pass
 def MeasureCore(self,*args):
  """
  MeasureCore(self: UIElement,availableSize: Size) -> Size
  
   When overridden in a derived class,provides measurement logic for sizing this 
    element properly,with consideration of the size of any child element content.
  
  
   availableSize: The available size that the parent element can allocate for the child.
   Returns: The desired size of this element in layout.
  MeasureCore(self: Window_16$17,availableSize: Size) -> Size
  MeasureCore(self: Label_17$18,availableSize: Size) -> Size
  MeasureCore(self: TextBox_18$19,availableSize: Size) -> Size
  MeasureCore(self: Button_19$20,availableSize: Size) -> Size
  MeasureCore(self: CheckBox_20$21,availableSize: Size) -> Size
  MeasureCore(self: ComboBox_21$22,availableSize: Size) -> Size
  MeasureCore(self: Separator_22$23,availableSize: Size) -> Size
  """
  pass
 def MoveFocus(self,request):
  """
  MoveFocus(self: UIElement,request: TraversalRequest) -> bool
  
   Attempts to move focus from this element to another element. The direction to 
    move focus is specified by a guidance direction,which is interpreted within 
    the organization of the visual parent for this element.
  
  
   request: A traversal request,which contains a property that indicates either a mode to 
    traverse in existing tab order,or a direction to move visually.
  
   Returns: true if the requested traversal was performed; otherwise,false.
  """
  pass
 def OnAccessKey(self,*args):
  """
  OnAccessKey(self: UIElement,e: AccessKeyEventArgs)
   Provides class handling for when an access key that is meaningful for this 
    element is invoked.
  
  
   e: The event data to the access key event. The event data reports which key was 
    invoked,and indicate whether the System.Windows.Input.AccessKeyManager object 
    that controls the sending of these events also sent this access key invocation 
    to other elements.
  
  OnAccessKey(self: Window_16$17,e: AccessKeyEventArgs)OnAccessKey(self: Label_17$18,e: AccessKeyEventArgs)OnAccessKey(self: TextBox_18$19,e: AccessKeyEventArgs)OnAccessKey(self: Button_19$20,e: AccessKeyEventArgs)OnAccessKey(self: CheckBox_20$21,e: AccessKeyEventArgs)OnAccessKey(self: ComboBox_21$22,e: AccessKeyEventArgs)OnAccessKey(self: Separator_22$23,e: AccessKeyEventArgs)
  """
  pass
 def OnChildDesiredSizeChanged(self,*args):
  """
  OnChildDesiredSizeChanged(self: UIElement,child: UIElement)
   Supports layout behavior when a child element is resized.
  
   child: The child element that is being resized.
  OnChildDesiredSizeChanged(self: Window_16$17,child: Window_16$17)OnChildDesiredSizeChanged(self: Label_17$18,child: Label_17$18)OnChildDesiredSizeChanged(self: TextBox_18$19,child: TextBox_18$19)OnChildDesiredSizeChanged(self: Button_19$20,child: Button_19$20)OnChildDesiredSizeChanged(self: CheckBox_20$21,child: CheckBox_20$21)OnChildDesiredSizeChanged(self: ComboBox_21$22,child: ComboBox_21$22)OnChildDesiredSizeChanged(self: Separator_22$23,child: Separator_22$23)
  """
  pass
 def OnCreateAutomationPeer(self,*args):
  """
  OnCreateAutomationPeer(self: UIElement) -> AutomationPeer
  
   Returns class-specific System.Windows.Automation.Peers.AutomationPeer 
    implementations for the Windows Presentation Foundation (WPF) infrastructure.
  
   Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
  OnCreateAutomationPeer(self: Window_16$17) -> AutomationPeer
  OnCreateAutomationPeer(self: Label_17$18) -> AutomationPeer
  OnCreateAutomationPeer(self: TextBox_18$19) -> AutomationPeer
  OnCreateAutomationPeer(self: Button_19$20) -> AutomationPeer
  OnCreateAutomationPeer(self: CheckBox_20$21) -> AutomationPeer
  OnCreateAutomationPeer(self: ComboBox_21$22) -> AutomationPeer
  OnCreateAutomationPeer(self: Separator_22$23) -> AutomationPeer
  """
  pass
 def OnDpiChanged(self,*args):
  """ OnDpiChanged(self: Visual,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: Window_16$17,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: Label_17$18,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: TextBox_18$19,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: Button_19$20,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: CheckBox_20$21,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: ComboBox_21$22,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: Separator_22$23,oldDpi: DpiScale,newDpi: DpiScale) """
  pass
 def OnDragEnter(self,*args):
  """
  OnDragEnter(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnDragEnter(self: Window_16$17,e: DragEventArgs)OnDragEnter(self: Label_17$18,e: DragEventArgs)OnDragEnter(self: TextBox_18$19,e: DragEventArgs)OnDragEnter(self: Button_19$20,e: DragEventArgs)OnDragEnter(self: CheckBox_20$21,e: DragEventArgs)OnDragEnter(self: ComboBox_21$22,e: DragEventArgs)OnDragEnter(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnDragLeave(self,*args):
  """
  OnDragLeave(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnDragLeave(self: Window_16$17,e: DragEventArgs)OnDragLeave(self: Label_17$18,e: DragEventArgs)OnDragLeave(self: TextBox_18$19,e: DragEventArgs)OnDragLeave(self: Button_19$20,e: DragEventArgs)OnDragLeave(self: CheckBox_20$21,e: DragEventArgs)OnDragLeave(self: ComboBox_21$22,e: DragEventArgs)OnDragLeave(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnDragOver(self,*args):
  """
  OnDragOver(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnDragOver(self: Window_16$17,e: DragEventArgs)OnDragOver(self: Label_17$18,e: DragEventArgs)OnDragOver(self: TextBox_18$19,e: DragEventArgs)OnDragOver(self: Button_19$20,e: DragEventArgs)OnDragOver(self: CheckBox_20$21,e: DragEventArgs)OnDragOver(self: ComboBox_21$22,e: DragEventArgs)OnDragOver(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnDrop(self,*args):
  """
  OnDrop(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnDrop(self: Window_16$17,e: DragEventArgs)OnDrop(self: Label_17$18,e: DragEventArgs)OnDrop(self: TextBox_18$19,e: DragEventArgs)OnDrop(self: Button_19$20,e: DragEventArgs)OnDrop(self: CheckBox_20$21,e: DragEventArgs)OnDrop(self: ComboBox_21$22,e: DragEventArgs)OnDrop(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnGiveFeedback(self,*args):
  """
  OnGiveFeedback(self: UIElement,e: GiveFeedbackEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
  OnGiveFeedback(self: Window_16$17,e: GiveFeedbackEventArgs)OnGiveFeedback(self: Label_17$18,e: GiveFeedbackEventArgs)OnGiveFeedback(self: TextBox_18$19,e: GiveFeedbackEventArgs)OnGiveFeedback(self: Button_19$20,e: GiveFeedbackEventArgs)OnGiveFeedback(self: CheckBox_20$21,e: GiveFeedbackEventArgs)OnGiveFeedback(self: ComboBox_21$22,e: GiveFeedbackEventArgs)OnGiveFeedback(self: Separator_22$23,e: GiveFeedbackEventArgs)
  """
  pass
 def OnGotFocus(self,*args):
  """
  OnGotFocus(self: UIElement,e: RoutedEventArgs)
   Raises the System.Windows.UIElement.GotFocus�routed event by using the event 
    data provided.
  
  
   e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
    contain the identifier for the System.Windows.UIElement.GotFocus event.
  
  OnGotFocus(self: Window_16$17,e: RoutedEventArgs)OnGotFocus(self: Label_17$18,e: RoutedEventArgs)OnGotFocus(self: TextBox_18$19,e: RoutedEventArgs)OnGotFocus(self: Button_19$20,e: RoutedEventArgs)OnGotFocus(self: CheckBox_20$21,e: RoutedEventArgs)OnGotFocus(self: Separator_22$23,e: RoutedEventArgs)
  """
  pass
 def OnGotKeyboardFocus(self,*args):
  """
  OnGotKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
    data.
  
  OnGotKeyboardFocus(self: Window_16$17,e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Label_17$18,e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: TextBox_18$19,e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Button_19$20,e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: CheckBox_20$21,e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: ComboBox_21$22,e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Separator_22$23,e: KeyboardFocusChangedEventArgs)
  """
  pass
 def OnGotMouseCapture(self,*args):
  """
  OnGotMouseCapture(self: UIElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  OnGotMouseCapture(self: Window_16$17,e: MouseEventArgs)OnGotMouseCapture(self: Label_17$18,e: MouseEventArgs)OnGotMouseCapture(self: TextBox_18$19,e: MouseEventArgs)OnGotMouseCapture(self: Button_19$20,e: MouseEventArgs)OnGotMouseCapture(self: CheckBox_20$21,e: MouseEventArgs)OnGotMouseCapture(self: ComboBox_21$22,e: MouseEventArgs)OnGotMouseCapture(self: Separator_22$23,e: MouseEventArgs)
  """
  pass
 def OnGotStylusCapture(self,*args):
  """
  OnGotStylusCapture(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnGotStylusCapture(self: Window_16$17,e: StylusEventArgs)OnGotStylusCapture(self: Label_17$18,e: StylusEventArgs)OnGotStylusCapture(self: TextBox_18$19,e: StylusEventArgs)OnGotStylusCapture(self: Button_19$20,e: StylusEventArgs)OnGotStylusCapture(self: CheckBox_20$21,e: StylusEventArgs)OnGotStylusCapture(self: ComboBox_21$22,e: StylusEventArgs)OnGotStylusCapture(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnGotTouchCapture(self,*args):
  """
  OnGotTouchCapture(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.GotTouchCapture routed 
    event that occurs when a touch is captured to this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnGotTouchCapture(self: Window_16$17,e: TouchEventArgs)OnGotTouchCapture(self: Label_17$18,e: TouchEventArgs)OnGotTouchCapture(self: TextBox_18$19,e: TouchEventArgs)OnGotTouchCapture(self: Button_19$20,e: TouchEventArgs)OnGotTouchCapture(self: CheckBox_20$21,e: TouchEventArgs)OnGotTouchCapture(self: ComboBox_21$22,e: TouchEventArgs)OnGotTouchCapture(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnIsKeyboardFocusedChanged(self,*args):
  """
  OnIsKeyboardFocusedChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  
  OnIsKeyboardFocusedChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnIsKeyboardFocusWithinChanged(self,*args):
  """
  OnIsKeyboardFocusWithinChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)
   Invoked just before the System.Windows.UIElement.IsKeyboardFocusWithinChanged 
    event is raised by this element. Implement this method to add class handling 
    for this event.
  
  
   e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  
  OnIsKeyboardFocusWithinChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnIsMouseCapturedChanged(self,*args):
  """
  OnIsMouseCapturedChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.UIElement.IsMouseCapturedChanged event 
    is raised on this element. Implement this method to add class handling for this 
    event.
  
  
   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  
  OnIsMouseCapturedChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnIsMouseCaptureWithinChanged(self,*args):
  """
  OnIsMouseCaptureWithinChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  
  OnIsMouseCaptureWithinChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnIsMouseDirectlyOverChanged(self,*args):
  """
  OnIsMouseDirectlyOverChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  
  OnIsMouseDirectlyOverChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnIsStylusCapturedChanged(self,*args):
  """
  OnIsStylusCapturedChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  
  OnIsStylusCapturedChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnIsStylusCaptureWithinChanged(self,*args):
  """
  OnIsStylusCaptureWithinChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  
  OnIsStylusCaptureWithinChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnIsStylusDirectlyOverChanged(self,*args):
  """
  OnIsStylusDirectlyOverChanged(self: UIElement,e: DependencyPropertyChangedEventArgs)
   Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
    data.
  
  OnIsStylusDirectlyOverChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnKeyDown(self,*args):
  """
  OnKeyDown(self: UIElement,e: KeyEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.KeyDown�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  OnKeyDown(self: Window_16$17,e: KeyEventArgs)OnKeyDown(self: Label_17$18,e: KeyEventArgs)OnKeyDown(self: TextBox_18$19,e: KeyEventArgs)OnKeyDown(self: Button_19$20,e: KeyEventArgs)OnKeyDown(self: CheckBox_20$21,e: KeyEventArgs)OnKeyDown(self: ComboBox_21$22,e: KeyEventArgs)OnKeyDown(self: Separator_22$23,e: KeyEventArgs)
  """
  pass
 def OnKeyUp(self,*args):
  """
  OnKeyUp(self: UIElement,e: KeyEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  OnKeyUp(self: Window_16$17,e: KeyEventArgs)OnKeyUp(self: Label_17$18,e: KeyEventArgs)OnKeyUp(self: TextBox_18$19,e: KeyEventArgs)OnKeyUp(self: Button_19$20,e: KeyEventArgs)OnKeyUp(self: CheckBox_20$21,e: KeyEventArgs)OnKeyUp(self: ComboBox_21$22,e: KeyEventArgs)OnKeyUp(self: Separator_22$23,e: KeyEventArgs)
  """
  pass
 def OnLostFocus(self,*args):
  """
  OnLostFocus(self: UIElement,e: RoutedEventArgs)
   Raises the System.Windows.UIElement.LostFocus�routed event by using the event 
    data that is provided.
  
  
   e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
    contain the identifier for the System.Windows.UIElement.LostFocus event.
  
  OnLostFocus(self: Window_16$17,e: RoutedEventArgs)OnLostFocus(self: Label_17$18,e: RoutedEventArgs)OnLostFocus(self: TextBox_18$19,e: RoutedEventArgs)OnLostFocus(self: Button_19$20,e: RoutedEventArgs)OnLostFocus(self: CheckBox_20$21,e: RoutedEventArgs)OnLostFocus(self: ComboBox_21$22,e: RoutedEventArgs)OnLostFocus(self: Separator_22$23,e: RoutedEventArgs)
  """
  pass
 def OnLostKeyboardFocus(self,*args):
  """
  OnLostKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
  OnLostKeyboardFocus(self: Window_16$17,e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Label_17$18,e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: TextBox_18$19,e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Button_19$20,e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: CheckBox_20$21,e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: ComboBox_21$22,e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Separator_22$23,e: KeyboardFocusChangedEventArgs)
  """
  pass
 def OnLostMouseCapture(self,*args):
  """
  OnLostMouseCapture(self: UIElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains event data.
  OnLostMouseCapture(self: Window_16$17,e: MouseEventArgs)OnLostMouseCapture(self: Label_17$18,e: MouseEventArgs)OnLostMouseCapture(self: TextBox_18$19,e: MouseEventArgs)OnLostMouseCapture(self: Button_19$20,e: MouseEventArgs)OnLostMouseCapture(self: CheckBox_20$21,e: MouseEventArgs)OnLostMouseCapture(self: Separator_22$23,e: MouseEventArgs)
  """
  pass
 def OnLostStylusCapture(self,*args):
  """
  OnLostStylusCapture(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains event data.
  OnLostStylusCapture(self: Window_16$17,e: StylusEventArgs)OnLostStylusCapture(self: Label_17$18,e: StylusEventArgs)OnLostStylusCapture(self: TextBox_18$19,e: StylusEventArgs)OnLostStylusCapture(self: Button_19$20,e: StylusEventArgs)OnLostStylusCapture(self: CheckBox_20$21,e: StylusEventArgs)OnLostStylusCapture(self: ComboBox_21$22,e: StylusEventArgs)OnLostStylusCapture(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnLostTouchCapture(self,*args):
  """
  OnLostTouchCapture(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.LostTouchCapture 
    routed event that occurs when this element loses a touch capture.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnLostTouchCapture(self: Window_16$17,e: TouchEventArgs)OnLostTouchCapture(self: Label_17$18,e: TouchEventArgs)OnLostTouchCapture(self: TextBox_18$19,e: TouchEventArgs)OnLostTouchCapture(self: Button_19$20,e: TouchEventArgs)OnLostTouchCapture(self: CheckBox_20$21,e: TouchEventArgs)OnLostTouchCapture(self: ComboBox_21$22,e: TouchEventArgs)OnLostTouchCapture(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnManipulationBoundaryFeedback(self,*args):
  """
  OnManipulationBoundaryFeedback(self: UIElement,e: ManipulationBoundaryFeedbackEventArgs)
   Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event 
    occurs.
  
  
   e: The data for the event.
  OnManipulationBoundaryFeedback(self: Window_16$17,e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Label_17$18,e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: TextBox_18$19,e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Button_19$20,e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: CheckBox_20$21,e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: ComboBox_21$22,e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Separator_22$23,e: ManipulationBoundaryFeedbackEventArgs)
  """
  pass
 def OnManipulationCompleted(self,*args):
  """
  OnManipulationCompleted(self: UIElement,e: ManipulationCompletedEventArgs)
   Called when the System.Windows.UIElement.ManipulationCompleted event occurs.
  
   e: The data for the event.
  OnManipulationCompleted(self: Window_16$17,e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Label_17$18,e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: TextBox_18$19,e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Button_19$20,e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: CheckBox_20$21,e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: ComboBox_21$22,e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Separator_22$23,e: ManipulationCompletedEventArgs)
  """
  pass
 def OnManipulationDelta(self,*args):
  """
  OnManipulationDelta(self: UIElement,e: ManipulationDeltaEventArgs)
   Called when the System.Windows.UIElement.ManipulationDelta event occurs.
  
   e: The data for the event.
  OnManipulationDelta(self: Window_16$17,e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Label_17$18,e: ManipulationDeltaEventArgs)OnManipulationDelta(self: TextBox_18$19,e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Button_19$20,e: ManipulationDeltaEventArgs)OnManipulationDelta(self: CheckBox_20$21,e: ManipulationDeltaEventArgs)OnManipulationDelta(self: ComboBox_21$22,e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Separator_22$23,e: ManipulationDeltaEventArgs)
  """
  pass
 def OnManipulationInertiaStarting(self,*args):
  """
  OnManipulationInertiaStarting(self: UIElement,e: ManipulationInertiaStartingEventArgs)
   Called when the System.Windows.UIElement.ManipulationInertiaStarting event 
    occurs.
  
  
   e: The data for the event.
  OnManipulationInertiaStarting(self: Window_16$17,e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Label_17$18,e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: TextBox_18$19,e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Button_19$20,e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: CheckBox_20$21,e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: ComboBox_21$22,e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Separator_22$23,e: ManipulationInertiaStartingEventArgs)
  """
  pass
 def OnManipulationStarted(self,*args):
  """
  OnManipulationStarted(self: UIElement,e: ManipulationStartedEventArgs)
   Called when the System.Windows.UIElement.ManipulationStarted event occurs.
  
   e: The data for the event.
  OnManipulationStarted(self: Window_16$17,e: ManipulationStartedEventArgs)OnManipulationStarted(self: Label_17$18,e: ManipulationStartedEventArgs)OnManipulationStarted(self: TextBox_18$19,e: ManipulationStartedEventArgs)OnManipulationStarted(self: Button_19$20,e: ManipulationStartedEventArgs)OnManipulationStarted(self: CheckBox_20$21,e: ManipulationStartedEventArgs)OnManipulationStarted(self: ComboBox_21$22,e: ManipulationStartedEventArgs)OnManipulationStarted(self: Separator_22$23,e: ManipulationStartedEventArgs)
  """
  pass
 def OnManipulationStarting(self,*args):
  """
  OnManipulationStarting(self: UIElement,e: ManipulationStartingEventArgs)
   Provides class handling for the System.Windows.UIElement.ManipulationStarting 
    routed event that occurs when the manipulation processor is first created.
  
  
   e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event 
    data.
  
  OnManipulationStarting(self: Window_16$17,e: ManipulationStartingEventArgs)OnManipulationStarting(self: Label_17$18,e: ManipulationStartingEventArgs)OnManipulationStarting(self: TextBox_18$19,e: ManipulationStartingEventArgs)OnManipulationStarting(self: Button_19$20,e: ManipulationStartingEventArgs)OnManipulationStarting(self: CheckBox_20$21,e: ManipulationStartingEventArgs)OnManipulationStarting(self: ComboBox_21$22,e: ManipulationStartingEventArgs)OnManipulationStarting(self: Separator_22$23,e: ManipulationStartingEventArgs)
  """
  pass
 def OnMouseDown(self,*args):
  """
  OnMouseDown(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. 
    This event data reports details about the mouse button that was pressed and the 
    handled state.
  
  OnMouseDown(self: Window_16$17,e: MouseButtonEventArgs)OnMouseDown(self: Label_17$18,e: MouseButtonEventArgs)OnMouseDown(self: TextBox_18$19,e: MouseButtonEventArgs)OnMouseDown(self: Button_19$20,e: MouseButtonEventArgs)OnMouseDown(self: CheckBox_20$21,e: MouseButtonEventArgs)OnMouseDown(self: ComboBox_21$22,e: MouseButtonEventArgs)OnMouseDown(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnMouseEnter(self,*args):
  """
  OnMouseEnter(self: UIElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event 
    is raised on this element. Implement this method to add class handling for this 
    event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  OnMouseEnter(self: Window_16$17,e: MouseEventArgs)OnMouseEnter(self: Label_17$18,e: MouseEventArgs)OnMouseEnter(self: TextBox_18$19,e: MouseEventArgs)OnMouseEnter(self: Button_19$20,e: MouseEventArgs)OnMouseEnter(self: CheckBox_20$21,e: MouseEventArgs)OnMouseEnter(self: ComboBox_21$22,e: MouseEventArgs)OnMouseEnter(self: Separator_22$23,e: MouseEventArgs)
  """
  pass
 def OnMouseLeave(self,*args):
  """
  OnMouseLeave(self: UIElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event 
    is raised on this element. Implement this method to add class handling for this 
    event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  OnMouseLeave(self: Window_16$17,e: MouseEventArgs)OnMouseLeave(self: Label_17$18,e: MouseEventArgs)OnMouseLeave(self: TextBox_18$19,e: MouseEventArgs)OnMouseLeave(self: Button_19$20,e: MouseEventArgs)OnMouseLeave(self: CheckBox_20$21,e: MouseEventArgs)OnMouseLeave(self: ComboBox_21$22,e: MouseEventArgs)OnMouseLeave(self: Separator_22$23,e: MouseEventArgs)
  """
  pass
 def OnMouseLeftButtonDown(self,*args):
  """
  OnMouseLeftButtonDown(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed 
    event is raised on this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the left mouse button was pressed.
  
  OnMouseLeftButtonDown(self: Window_16$17,e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Label_17$18,e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: TextBox_18$19,e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Button_19$20,e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: CheckBox_20$21,e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: ComboBox_21$22,e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnMouseLeftButtonUp(self,*args):
  """
  OnMouseLeftButtonUp(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the left mouse button was released.
  
  OnMouseLeftButtonUp(self: Window_16$17,e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Label_17$18,e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: TextBox_18$19,e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Button_19$20,e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: CheckBox_20$21,e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: ComboBox_21$22,e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnMouseMove(self,*args):
  """
  OnMouseMove(self: UIElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  OnMouseMove(self: Window_16$17,e: MouseEventArgs)OnMouseMove(self: Label_17$18,e: MouseEventArgs)OnMouseMove(self: TextBox_18$19,e: MouseEventArgs)OnMouseMove(self: Button_19$20,e: MouseEventArgs)OnMouseMove(self: CheckBox_20$21,e: MouseEventArgs)OnMouseMove(self: Separator_22$23,e: MouseEventArgs)
  """
  pass
 def OnMouseRightButtonDown(self,*args):
  """
  OnMouseRightButtonDown(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the right mouse button was pressed.
  
  OnMouseRightButtonDown(self: Window_16$17,e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Label_17$18,e: MouseButtonEventArgs)OnMouseRightButtonDown(self: TextBox_18$19,e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Button_19$20,e: MouseButtonEventArgs)OnMouseRightButtonDown(self: CheckBox_20$21,e: MouseButtonEventArgs)OnMouseRightButtonDown(self: ComboBox_21$22,e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnMouseRightButtonUp(self,*args):
  """
  OnMouseRightButtonUp(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the right mouse button was released.
  
  OnMouseRightButtonUp(self: Window_16$17,e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Label_17$18,e: MouseButtonEventArgs)OnMouseRightButtonUp(self: TextBox_18$19,e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Button_19$20,e: MouseButtonEventArgs)OnMouseRightButtonUp(self: CheckBox_20$21,e: MouseButtonEventArgs)OnMouseRightButtonUp(self: ComboBox_21$22,e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnMouseUp(self,*args):
  """
  OnMouseUp(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the mouse button was released.
  
  OnMouseUp(self: Window_16$17,e: MouseButtonEventArgs)OnMouseUp(self: Label_17$18,e: MouseButtonEventArgs)OnMouseUp(self: TextBox_18$19,e: MouseButtonEventArgs)OnMouseUp(self: Button_19$20,e: MouseButtonEventArgs)OnMouseUp(self: CheckBox_20$21,e: MouseButtonEventArgs)OnMouseUp(self: ComboBox_21$22,e: MouseButtonEventArgs)OnMouseUp(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnMouseWheel(self,*args):
  """
  OnMouseWheel(self: UIElement,e: MouseWheelEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
  OnMouseWheel(self: Window_16$17,e: MouseWheelEventArgs)OnMouseWheel(self: Label_17$18,e: MouseWheelEventArgs)OnMouseWheel(self: TextBox_18$19,e: MouseWheelEventArgs)OnMouseWheel(self: Button_19$20,e: MouseWheelEventArgs)OnMouseWheel(self: CheckBox_20$21,e: MouseWheelEventArgs)OnMouseWheel(self: Separator_22$23,e: MouseWheelEventArgs)
  """
  pass
 def OnPreviewDragEnter(self,*args):
  """
  OnPreviewDragEnter(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnPreviewDragEnter(self: Window_16$17,e: DragEventArgs)OnPreviewDragEnter(self: Label_17$18,e: DragEventArgs)OnPreviewDragEnter(self: TextBox_18$19,e: DragEventArgs)OnPreviewDragEnter(self: Button_19$20,e: DragEventArgs)OnPreviewDragEnter(self: CheckBox_20$21,e: DragEventArgs)OnPreviewDragEnter(self: ComboBox_21$22,e: DragEventArgs)OnPreviewDragEnter(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnPreviewDragLeave(self,*args):
  """
  OnPreviewDragLeave(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnPreviewDragLeave(self: Window_16$17,e: DragEventArgs)OnPreviewDragLeave(self: Label_17$18,e: DragEventArgs)OnPreviewDragLeave(self: TextBox_18$19,e: DragEventArgs)OnPreviewDragLeave(self: Button_19$20,e: DragEventArgs)OnPreviewDragLeave(self: CheckBox_20$21,e: DragEventArgs)OnPreviewDragLeave(self: ComboBox_21$22,e: DragEventArgs)OnPreviewDragLeave(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnPreviewDragOver(self,*args):
  """
  OnPreviewDragOver(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnPreviewDragOver(self: Window_16$17,e: DragEventArgs)OnPreviewDragOver(self: Label_17$18,e: DragEventArgs)OnPreviewDragOver(self: TextBox_18$19,e: DragEventArgs)OnPreviewDragOver(self: Button_19$20,e: DragEventArgs)OnPreviewDragOver(self: CheckBox_20$21,e: DragEventArgs)OnPreviewDragOver(self: ComboBox_21$22,e: DragEventArgs)OnPreviewDragOver(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnPreviewDrop(self,*args):
  """
  OnPreviewDrop(self: UIElement,e: DragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.DragEventArgs that contains the event data.
  OnPreviewDrop(self: Window_16$17,e: DragEventArgs)OnPreviewDrop(self: Label_17$18,e: DragEventArgs)OnPreviewDrop(self: TextBox_18$19,e: DragEventArgs)OnPreviewDrop(self: Button_19$20,e: DragEventArgs)OnPreviewDrop(self: CheckBox_20$21,e: DragEventArgs)OnPreviewDrop(self: ComboBox_21$22,e: DragEventArgs)OnPreviewDrop(self: Separator_22$23,e: DragEventArgs)
  """
  pass
 def OnPreviewGiveFeedback(self,*args):
  """
  OnPreviewGiveFeedback(self: UIElement,e: GiveFeedbackEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
  OnPreviewGiveFeedback(self: Window_16$17,e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Label_17$18,e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: TextBox_18$19,e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Button_19$20,e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: CheckBox_20$21,e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: ComboBox_21$22,e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Separator_22$23,e: GiveFeedbackEventArgs)
  """
  pass
 def OnPreviewGotKeyboardFocus(self,*args):
  """
  OnPreviewGotKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
    data.
  
  OnPreviewGotKeyboardFocus(self: Window_16$17,e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Label_17$18,e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: TextBox_18$19,e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Button_19$20,e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: CheckBox_20$21,e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: ComboBox_21$22,e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Separator_22$23,e: KeyboardFocusChangedEventArgs)
  """
  pass
 def OnPreviewKeyDown(self,*args):
  """
  OnPreviewKeyDown(self: UIElement,e: KeyEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  OnPreviewKeyDown(self: Window_16$17,e: KeyEventArgs)OnPreviewKeyDown(self: Label_17$18,e: KeyEventArgs)OnPreviewKeyDown(self: TextBox_18$19,e: KeyEventArgs)OnPreviewKeyDown(self: Button_19$20,e: KeyEventArgs)OnPreviewKeyDown(self: CheckBox_20$21,e: KeyEventArgs)OnPreviewKeyDown(self: ComboBox_21$22,e: KeyEventArgs)OnPreviewKeyDown(self: Separator_22$23,e: KeyEventArgs)
  """
  pass
 def OnPreviewKeyUp(self,*args):
  """
  OnPreviewKeyUp(self: UIElement,e: KeyEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyEventArgs that contains the event data.
  OnPreviewKeyUp(self: Window_16$17,e: KeyEventArgs)OnPreviewKeyUp(self: Label_17$18,e: KeyEventArgs)OnPreviewKeyUp(self: TextBox_18$19,e: KeyEventArgs)OnPreviewKeyUp(self: Button_19$20,e: KeyEventArgs)OnPreviewKeyUp(self: CheckBox_20$21,e: KeyEventArgs)OnPreviewKeyUp(self: ComboBox_21$22,e: KeyEventArgs)OnPreviewKeyUp(self: Separator_22$23,e: KeyEventArgs)
  """
  pass
 def OnPreviewLostKeyboardFocus(self,*args):
  """
  OnPreviewLostKeyboardFocus(self: UIElement,e: KeyboardFocusChangedEventArgs)
   Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
    data.
  
  OnPreviewLostKeyboardFocus(self: Window_16$17,e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Label_17$18,e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: TextBox_18$19,e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Button_19$20,e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: CheckBox_20$21,e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: ComboBox_21$22,e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Separator_22$23,e: KeyboardFocusChangedEventArgs)
  """
  pass
 def OnPreviewMouseDown(self,*args):
  """
  OnPreviewMouseDown(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�
    routed event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that one or more mouse buttons were pressed.
  
  OnPreviewMouseDown(self: Window_16$17,e: MouseButtonEventArgs)OnPreviewMouseDown(self: Label_17$18,e: MouseButtonEventArgs)OnPreviewMouseDown(self: TextBox_18$19,e: MouseButtonEventArgs)OnPreviewMouseDown(self: Button_19$20,e: MouseButtonEventArgs)OnPreviewMouseDown(self: CheckBox_20$21,e: MouseButtonEventArgs)OnPreviewMouseDown(self: ComboBox_21$22,e: MouseButtonEventArgs)OnPreviewMouseDown(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnPreviewMouseLeftButtonDown(self,*args):
  """
  OnPreviewMouseLeftButtonDown(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�
    routed event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the left mouse button was pressed.
  
  OnPreviewMouseLeftButtonDown(self: Window_16$17,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Label_17$18,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: TextBox_18$19,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Button_19$20,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: CheckBox_20$21,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: ComboBox_21$22,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnPreviewMouseLeftButtonUp(self,*args):
  """
  OnPreviewMouseLeftButtonUp(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�
    routed event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the left mouse button was released.
  
  OnPreviewMouseLeftButtonUp(self: Window_16$17,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Label_17$18,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: TextBox_18$19,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Button_19$20,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: CheckBox_20$21,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: ComboBox_21$22,e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnPreviewMouseMove(self,*args):
  """
  OnPreviewMouseMove(self: UIElement,e: MouseEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseEventArgs that contains the event data.
  OnPreviewMouseMove(self: Window_16$17,e: MouseEventArgs)OnPreviewMouseMove(self: Label_17$18,e: MouseEventArgs)OnPreviewMouseMove(self: TextBox_18$19,e: MouseEventArgs)OnPreviewMouseMove(self: Button_19$20,e: MouseEventArgs)OnPreviewMouseMove(self: CheckBox_20$21,e: MouseEventArgs)OnPreviewMouseMove(self: ComboBox_21$22,e: MouseEventArgs)OnPreviewMouseMove(self: Separator_22$23,e: MouseEventArgs)
  """
  pass
 def OnPreviewMouseRightButtonDown(self,*args):
  """
  OnPreviewMouseRightButtonDown(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�
    routed event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the right mouse button was pressed.
  
  OnPreviewMouseRightButtonDown(self: Window_16$17,e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Label_17$18,e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: TextBox_18$19,e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Button_19$20,e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: CheckBox_20$21,e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: ComboBox_21$22,e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnPreviewMouseRightButtonUp(self,*args):
  """
  OnPreviewMouseRightButtonUp(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�
    routed event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that the right mouse button was released.
  
  OnPreviewMouseRightButtonUp(self: Window_16$17,e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Label_17$18,e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: TextBox_18$19,e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Button_19$20,e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: CheckBox_20$21,e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: ComboBox_21$22,e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnPreviewMouseUp(self,*args):
  """
  OnPreviewMouseUp(self: UIElement,e: MouseButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
    event data reports that one or more mouse buttons were released.
  
  OnPreviewMouseUp(self: Window_16$17,e: MouseButtonEventArgs)OnPreviewMouseUp(self: Label_17$18,e: MouseButtonEventArgs)OnPreviewMouseUp(self: TextBox_18$19,e: MouseButtonEventArgs)OnPreviewMouseUp(self: Button_19$20,e: MouseButtonEventArgs)OnPreviewMouseUp(self: CheckBox_20$21,e: MouseButtonEventArgs)OnPreviewMouseUp(self: ComboBox_21$22,e: MouseButtonEventArgs)OnPreviewMouseUp(self: Separator_22$23,e: MouseButtonEventArgs)
  """
  pass
 def OnPreviewMouseWheel(self,*args):
  """
  OnPreviewMouseWheel(self: UIElement,e: MouseWheelEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
  OnPreviewMouseWheel(self: Window_16$17,e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Label_17$18,e: MouseWheelEventArgs)OnPreviewMouseWheel(self: TextBox_18$19,e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Button_19$20,e: MouseWheelEventArgs)OnPreviewMouseWheel(self: CheckBox_20$21,e: MouseWheelEventArgs)OnPreviewMouseWheel(self: ComboBox_21$22,e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Separator_22$23,e: MouseWheelEventArgs)
  """
  pass
 def OnPreviewQueryContinueDrag(self,*args):
  """
  OnPreviewQueryContinueDrag(self: UIElement,e: QueryContinueDragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
  OnPreviewQueryContinueDrag(self: Window_16$17,e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Label_17$18,e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: TextBox_18$19,e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Button_19$20,e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: CheckBox_20$21,e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: ComboBox_21$22,e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Separator_22$23,e: QueryContinueDragEventArgs)
  """
  pass
 def OnPreviewStylusButtonDown(self,*args):
  """
  OnPreviewStylusButtonDown(self: UIElement,e: StylusButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  OnPreviewStylusButtonDown(self: Window_16$17,e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Label_17$18,e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: TextBox_18$19,e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Button_19$20,e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: CheckBox_20$21,e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: ComboBox_21$22,e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Separator_22$23,e: StylusButtonEventArgs)
  """
  pass
 def OnPreviewStylusButtonUp(self,*args):
  """
  OnPreviewStylusButtonUp(self: UIElement,e: StylusButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  OnPreviewStylusButtonUp(self: Window_16$17,e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Label_17$18,e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: TextBox_18$19,e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Button_19$20,e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: CheckBox_20$21,e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: ComboBox_21$22,e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Separator_22$23,e: StylusButtonEventArgs)
  """
  pass
 def OnPreviewStylusDown(self,*args):
  """
  OnPreviewStylusDown(self: UIElement,e: StylusDownEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
  OnPreviewStylusDown(self: Window_16$17,e: StylusDownEventArgs)OnPreviewStylusDown(self: Label_17$18,e: StylusDownEventArgs)OnPreviewStylusDown(self: TextBox_18$19,e: StylusDownEventArgs)OnPreviewStylusDown(self: Button_19$20,e: StylusDownEventArgs)OnPreviewStylusDown(self: CheckBox_20$21,e: StylusDownEventArgs)OnPreviewStylusDown(self: ComboBox_21$22,e: StylusDownEventArgs)OnPreviewStylusDown(self: Separator_22$23,e: StylusDownEventArgs)
  """
  pass
 def OnPreviewStylusInAirMove(self,*args):
  """
  OnPreviewStylusInAirMove(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnPreviewStylusInAirMove(self: Window_16$17,e: StylusEventArgs)OnPreviewStylusInAirMove(self: Label_17$18,e: StylusEventArgs)OnPreviewStylusInAirMove(self: TextBox_18$19,e: StylusEventArgs)OnPreviewStylusInAirMove(self: Button_19$20,e: StylusEventArgs)OnPreviewStylusInAirMove(self: CheckBox_20$21,e: StylusEventArgs)OnPreviewStylusInAirMove(self: ComboBox_21$22,e: StylusEventArgs)OnPreviewStylusInAirMove(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnPreviewStylusInRange(self,*args):
  """
  OnPreviewStylusInRange(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnPreviewStylusInRange(self: Window_16$17,e: StylusEventArgs)OnPreviewStylusInRange(self: Label_17$18,e: StylusEventArgs)OnPreviewStylusInRange(self: TextBox_18$19,e: StylusEventArgs)OnPreviewStylusInRange(self: Button_19$20,e: StylusEventArgs)OnPreviewStylusInRange(self: CheckBox_20$21,e: StylusEventArgs)OnPreviewStylusInRange(self: ComboBox_21$22,e: StylusEventArgs)OnPreviewStylusInRange(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnPreviewStylusMove(self,*args):
  """
  OnPreviewStylusMove(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnPreviewStylusMove(self: Window_16$17,e: StylusEventArgs)OnPreviewStylusMove(self: Label_17$18,e: StylusEventArgs)OnPreviewStylusMove(self: TextBox_18$19,e: StylusEventArgs)OnPreviewStylusMove(self: Button_19$20,e: StylusEventArgs)OnPreviewStylusMove(self: CheckBox_20$21,e: StylusEventArgs)OnPreviewStylusMove(self: ComboBox_21$22,e: StylusEventArgs)OnPreviewStylusMove(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnPreviewStylusOutOfRange(self,*args):
  """
  OnPreviewStylusOutOfRange(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnPreviewStylusOutOfRange(self: Window_16$17,e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Label_17$18,e: StylusEventArgs)OnPreviewStylusOutOfRange(self: TextBox_18$19,e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Button_19$20,e: StylusEventArgs)OnPreviewStylusOutOfRange(self: CheckBox_20$21,e: StylusEventArgs)OnPreviewStylusOutOfRange(self: ComboBox_21$22,e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnPreviewStylusSystemGesture(self,*args):
  """
  OnPreviewStylusSystemGesture(self: UIElement,e: StylusSystemGestureEventArgs)
   Invoked when an unhandled 
    System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches 
    an element in its route that is derived from this class. Implement this method 
    to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
    data.
  
  OnPreviewStylusSystemGesture(self: Window_16$17,e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Label_17$18,e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: TextBox_18$19,e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Button_19$20,e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: CheckBox_20$21,e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: ComboBox_21$22,e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Separator_22$23,e: StylusSystemGestureEventArgs)
  """
  pass
 def OnPreviewStylusUp(self,*args):
  """
  OnPreviewStylusUp(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnPreviewStylusUp(self: Window_16$17,e: StylusEventArgs)OnPreviewStylusUp(self: Label_17$18,e: StylusEventArgs)OnPreviewStylusUp(self: TextBox_18$19,e: StylusEventArgs)OnPreviewStylusUp(self: Button_19$20,e: StylusEventArgs)OnPreviewStylusUp(self: CheckBox_20$21,e: StylusEventArgs)OnPreviewStylusUp(self: ComboBox_21$22,e: StylusEventArgs)OnPreviewStylusUp(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnPreviewTextInput(self,*args):
  """
  OnPreviewTextInput(self: UIElement,e: TextCompositionEventArgs)
   Invoked when an unhandled 
    System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
  OnPreviewTextInput(self: Window_16$17,e: TextCompositionEventArgs)OnPreviewTextInput(self: Label_17$18,e: TextCompositionEventArgs)OnPreviewTextInput(self: TextBox_18$19,e: TextCompositionEventArgs)OnPreviewTextInput(self: Button_19$20,e: TextCompositionEventArgs)OnPreviewTextInput(self: CheckBox_20$21,e: TextCompositionEventArgs)OnPreviewTextInput(self: ComboBox_21$22,e: TextCompositionEventArgs)OnPreviewTextInput(self: Separator_22$23,e: TextCompositionEventArgs)
  """
  pass
 def OnPreviewTouchDown(self,*args):
  """
  OnPreviewTouchDown(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.PreviewTouchDown 
    routed event that occurs when a touch presses this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnPreviewTouchDown(self: Window_16$17,e: TouchEventArgs)OnPreviewTouchDown(self: Label_17$18,e: TouchEventArgs)OnPreviewTouchDown(self: TextBox_18$19,e: TouchEventArgs)OnPreviewTouchDown(self: Button_19$20,e: TouchEventArgs)OnPreviewTouchDown(self: CheckBox_20$21,e: TouchEventArgs)OnPreviewTouchDown(self: ComboBox_21$22,e: TouchEventArgs)OnPreviewTouchDown(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnPreviewTouchMove(self,*args):
  """
  OnPreviewTouchMove(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.PreviewTouchMove 
    routed event that occurs when a touch moves while inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnPreviewTouchMove(self: Window_16$17,e: TouchEventArgs)OnPreviewTouchMove(self: Label_17$18,e: TouchEventArgs)OnPreviewTouchMove(self: TextBox_18$19,e: TouchEventArgs)OnPreviewTouchMove(self: Button_19$20,e: TouchEventArgs)OnPreviewTouchMove(self: CheckBox_20$21,e: TouchEventArgs)OnPreviewTouchMove(self: ComboBox_21$22,e: TouchEventArgs)OnPreviewTouchMove(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnPreviewTouchUp(self,*args):
  """
  OnPreviewTouchUp(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed 
    event that occurs when a touch is released inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnPreviewTouchUp(self: Window_16$17,e: TouchEventArgs)OnPreviewTouchUp(self: Label_17$18,e: TouchEventArgs)OnPreviewTouchUp(self: TextBox_18$19,e: TouchEventArgs)OnPreviewTouchUp(self: Button_19$20,e: TouchEventArgs)OnPreviewTouchUp(self: CheckBox_20$21,e: TouchEventArgs)OnPreviewTouchUp(self: ComboBox_21$22,e: TouchEventArgs)OnPreviewTouchUp(self: Separator_22$23,e: TouchEventArgs)
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
  OnQueryContinueDrag(self: UIElement,e: QueryContinueDragEventArgs)
   Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
  OnQueryContinueDrag(self: Window_16$17,e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Label_17$18,e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: TextBox_18$19,e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Button_19$20,e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: CheckBox_20$21,e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: ComboBox_21$22,e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Separator_22$23,e: QueryContinueDragEventArgs)
  """
  pass
 def OnQueryCursor(self,*args):
  """
  OnQueryCursor(self: UIElement,e: QueryCursorEventArgs)
   Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
  OnQueryCursor(self: Window_16$17,e: QueryCursorEventArgs)OnQueryCursor(self: Label_17$18,e: QueryCursorEventArgs)OnQueryCursor(self: TextBox_18$19,e: QueryCursorEventArgs)OnQueryCursor(self: Button_19$20,e: QueryCursorEventArgs)OnQueryCursor(self: CheckBox_20$21,e: QueryCursorEventArgs)OnQueryCursor(self: ComboBox_21$22,e: QueryCursorEventArgs)OnQueryCursor(self: Separator_22$23,e: QueryCursorEventArgs)
  """
  pass
 def OnRender(self,*args):
  """
  OnRender(self: UIElement,drawingContext: DrawingContext)
   When overridden in a derived class,participates in rendering operations that 
    are directed by the layout system. The rendering instructions for this element 
    are not used directly when this method is invoked,and are instead preserved 
    for later asynchronous use by layout and drawing.
  
  
   drawingContext: The drawing instructions for a specific element. This context is provided to 
    the layout system.
  
  OnRender(self: Window_16$17,drawingContext: DrawingContext)OnRender(self: Label_17$18,drawingContext: DrawingContext)OnRender(self: TextBox_18$19,drawingContext: DrawingContext)OnRender(self: Button_19$20,drawingContext: DrawingContext)OnRender(self: CheckBox_20$21,drawingContext: DrawingContext)OnRender(self: ComboBox_21$22,drawingContext: DrawingContext)OnRender(self: Separator_22$23,drawingContext: DrawingContext)
  """
  pass
 def OnRenderSizeChanged(self,*args):
  """
  OnRenderSizeChanged(self: UIElement,info: SizeChangedInfo)
   When overridden in a derived class,participates in rendering operations that 
    are directed by the layout system. This method is invoked after layout update,
    and before rendering,if the element's System.Windows.UIElement.RenderSize has 
    changed as a result of layout update.
  
  
   info: The packaged parameters (System.Windows.SizeChangedInfo),which includes old 
    and new sizes,and which dimension actually changes.
  
  OnRenderSizeChanged(self: Window_16$17,sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Label_17$18,sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: TextBox_18$19,sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Button_19$20,sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: CheckBox_20$21,sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: ComboBox_21$22,sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Separator_22$23,sizeInfo: SizeChangedInfo)
  """
  pass
 def OnStylusButtonDown(self,*args):
  """
  OnStylusButtonDown(self: UIElement,e: StylusButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  OnStylusButtonDown(self: Window_16$17,e: StylusButtonEventArgs)OnStylusButtonDown(self: Label_17$18,e: StylusButtonEventArgs)OnStylusButtonDown(self: TextBox_18$19,e: StylusButtonEventArgs)OnStylusButtonDown(self: Button_19$20,e: StylusButtonEventArgs)OnStylusButtonDown(self: CheckBox_20$21,e: StylusButtonEventArgs)OnStylusButtonDown(self: ComboBox_21$22,e: StylusButtonEventArgs)OnStylusButtonDown(self: Separator_22$23,e: StylusButtonEventArgs)
  """
  pass
 def OnStylusButtonUp(self,*args):
  """
  OnStylusButtonUp(self: UIElement,e: StylusButtonEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
  OnStylusButtonUp(self: Window_16$17,e: StylusButtonEventArgs)OnStylusButtonUp(self: Label_17$18,e: StylusButtonEventArgs)OnStylusButtonUp(self: TextBox_18$19,e: StylusButtonEventArgs)OnStylusButtonUp(self: Button_19$20,e: StylusButtonEventArgs)OnStylusButtonUp(self: CheckBox_20$21,e: StylusButtonEventArgs)OnStylusButtonUp(self: ComboBox_21$22,e: StylusButtonEventArgs)OnStylusButtonUp(self: Separator_22$23,e: StylusButtonEventArgs)
  """
  pass
 def OnStylusDown(self,*args):
  """
  OnStylusDown(self: UIElement,e: StylusDownEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
  OnStylusDown(self: Window_16$17,e: StylusDownEventArgs)OnStylusDown(self: Label_17$18,e: StylusDownEventArgs)OnStylusDown(self: TextBox_18$19,e: StylusDownEventArgs)OnStylusDown(self: Button_19$20,e: StylusDownEventArgs)OnStylusDown(self: CheckBox_20$21,e: StylusDownEventArgs)OnStylusDown(self: ComboBox_21$22,e: StylusDownEventArgs)OnStylusDown(self: Separator_22$23,e: StylusDownEventArgs)
  """
  pass
 def OnStylusEnter(self,*args):
  """
  OnStylusEnter(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached 
    event is raised by this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnStylusEnter(self: Window_16$17,e: StylusEventArgs)OnStylusEnter(self: Label_17$18,e: StylusEventArgs)OnStylusEnter(self: TextBox_18$19,e: StylusEventArgs)OnStylusEnter(self: Button_19$20,e: StylusEventArgs)OnStylusEnter(self: CheckBox_20$21,e: StylusEventArgs)OnStylusEnter(self: ComboBox_21$22,e: StylusEventArgs)OnStylusEnter(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnStylusInAirMove(self,*args):
  """
  OnStylusInAirMove(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnStylusInAirMove(self: Window_16$17,e: StylusEventArgs)OnStylusInAirMove(self: Label_17$18,e: StylusEventArgs)OnStylusInAirMove(self: TextBox_18$19,e: StylusEventArgs)OnStylusInAirMove(self: Button_19$20,e: StylusEventArgs)OnStylusInAirMove(self: CheckBox_20$21,e: StylusEventArgs)OnStylusInAirMove(self: ComboBox_21$22,e: StylusEventArgs)OnStylusInAirMove(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnStylusInRange(self,*args):
  """
  OnStylusInRange(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnStylusInRange(self: Window_16$17,e: StylusEventArgs)OnStylusInRange(self: Label_17$18,e: StylusEventArgs)OnStylusInRange(self: TextBox_18$19,e: StylusEventArgs)OnStylusInRange(self: Button_19$20,e: StylusEventArgs)OnStylusInRange(self: CheckBox_20$21,e: StylusEventArgs)OnStylusInRange(self: ComboBox_21$22,e: StylusEventArgs)OnStylusInRange(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnStylusLeave(self,*args):
  """
  OnStylusLeave(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached 
    event is raised by this element. Implement this method to add class handling 
    for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnStylusLeave(self: Window_16$17,e: StylusEventArgs)OnStylusLeave(self: Label_17$18,e: StylusEventArgs)OnStylusLeave(self: TextBox_18$19,e: StylusEventArgs)OnStylusLeave(self: Button_19$20,e: StylusEventArgs)OnStylusLeave(self: CheckBox_20$21,e: StylusEventArgs)OnStylusLeave(self: ComboBox_21$22,e: StylusEventArgs)OnStylusLeave(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnStylusMove(self,*args):
  """
  OnStylusMove(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnStylusMove(self: Window_16$17,e: StylusEventArgs)OnStylusMove(self: Label_17$18,e: StylusEventArgs)OnStylusMove(self: TextBox_18$19,e: StylusEventArgs)OnStylusMove(self: Button_19$20,e: StylusEventArgs)OnStylusMove(self: CheckBox_20$21,e: StylusEventArgs)OnStylusMove(self: ComboBox_21$22,e: StylusEventArgs)OnStylusMove(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnStylusOutOfRange(self,*args):
  """
  OnStylusOutOfRange(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached 
    event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnStylusOutOfRange(self: Window_16$17,e: StylusEventArgs)OnStylusOutOfRange(self: Label_17$18,e: StylusEventArgs)OnStylusOutOfRange(self: TextBox_18$19,e: StylusEventArgs)OnStylusOutOfRange(self: Button_19$20,e: StylusEventArgs)OnStylusOutOfRange(self: CheckBox_20$21,e: StylusEventArgs)OnStylusOutOfRange(self: ComboBox_21$22,e: StylusEventArgs)OnStylusOutOfRange(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnStylusSystemGesture(self,*args):
  """
  OnStylusSystemGesture(self: UIElement,e: StylusSystemGestureEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
    data.
  
  OnStylusSystemGesture(self: Window_16$17,e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Label_17$18,e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: TextBox_18$19,e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Button_19$20,e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: CheckBox_20$21,e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: ComboBox_21$22,e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Separator_22$23,e: StylusSystemGestureEventArgs)
  """
  pass
 def OnStylusUp(self,*args):
  """
  OnStylusUp(self: UIElement,e: StylusEventArgs)
   Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event 
    reaches an element in its route that is derived from this class. Implement this 
    method to add class handling for this event.
  
  
   e: The System.Windows.Input.StylusEventArgs that contains the event data.
  OnStylusUp(self: Window_16$17,e: StylusEventArgs)OnStylusUp(self: Label_17$18,e: StylusEventArgs)OnStylusUp(self: TextBox_18$19,e: StylusEventArgs)OnStylusUp(self: Button_19$20,e: StylusEventArgs)OnStylusUp(self: CheckBox_20$21,e: StylusEventArgs)OnStylusUp(self: ComboBox_21$22,e: StylusEventArgs)OnStylusUp(self: Separator_22$23,e: StylusEventArgs)
  """
  pass
 def OnTextInput(self,*args):
  """
  OnTextInput(self: UIElement,e: TextCompositionEventArgs)
   Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�
    attached event reaches an element in its route that is derived from this class. 
    Implement this method to add class handling for this event.
  
  
   e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
  OnTextInput(self: Window_16$17,e: TextCompositionEventArgs)OnTextInput(self: Label_17$18,e: TextCompositionEventArgs)OnTextInput(self: TextBox_18$19,e: TextCompositionEventArgs)OnTextInput(self: Button_19$20,e: TextCompositionEventArgs)OnTextInput(self: CheckBox_20$21,e: TextCompositionEventArgs)OnTextInput(self: ComboBox_21$22,e: TextCompositionEventArgs)OnTextInput(self: Separator_22$23,e: TextCompositionEventArgs)
  """
  pass
 def OnTouchDown(self,*args):
  """
  OnTouchDown(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.TouchDown routed event 
    that occurs when a touch presses inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnTouchDown(self: Window_16$17,e: TouchEventArgs)OnTouchDown(self: Label_17$18,e: TouchEventArgs)OnTouchDown(self: TextBox_18$19,e: TouchEventArgs)OnTouchDown(self: Button_19$20,e: TouchEventArgs)OnTouchDown(self: CheckBox_20$21,e: TouchEventArgs)OnTouchDown(self: ComboBox_21$22,e: TouchEventArgs)OnTouchDown(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnTouchEnter(self,*args):
  """
  OnTouchEnter(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.TouchEnter routed 
    event that occurs when a touch moves from outside to inside the bounds of this 
    element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnTouchEnter(self: Window_16$17,e: TouchEventArgs)OnTouchEnter(self: Label_17$18,e: TouchEventArgs)OnTouchEnter(self: TextBox_18$19,e: TouchEventArgs)OnTouchEnter(self: Button_19$20,e: TouchEventArgs)OnTouchEnter(self: CheckBox_20$21,e: TouchEventArgs)OnTouchEnter(self: ComboBox_21$22,e: TouchEventArgs)OnTouchEnter(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnTouchLeave(self,*args):
  """
  OnTouchLeave(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.TouchLeave routed 
    event that occurs when a touch moves from inside to outside the bounds of this 
    System.Windows.UIElement.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnTouchLeave(self: Window_16$17,e: TouchEventArgs)OnTouchLeave(self: Label_17$18,e: TouchEventArgs)OnTouchLeave(self: TextBox_18$19,e: TouchEventArgs)OnTouchLeave(self: Button_19$20,e: TouchEventArgs)OnTouchLeave(self: CheckBox_20$21,e: TouchEventArgs)OnTouchLeave(self: ComboBox_21$22,e: TouchEventArgs)OnTouchLeave(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnTouchMove(self,*args):
  """
  OnTouchMove(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.TouchMove routed event 
    that occurs when a touch moves while inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnTouchMove(self: Window_16$17,e: TouchEventArgs)OnTouchMove(self: Label_17$18,e: TouchEventArgs)OnTouchMove(self: TextBox_18$19,e: TouchEventArgs)OnTouchMove(self: Button_19$20,e: TouchEventArgs)OnTouchMove(self: CheckBox_20$21,e: TouchEventArgs)OnTouchMove(self: ComboBox_21$22,e: TouchEventArgs)OnTouchMove(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnTouchUp(self,*args):
  """
  OnTouchUp(self: UIElement,e: TouchEventArgs)
   Provides class handling for the System.Windows.UIElement.TouchUp routed event 
    that occurs when a touch is released inside this element.
  
  
   e: A System.Windows.Input.TouchEventArgs that contains the event data.
  OnTouchUp(self: Window_16$17,e: TouchEventArgs)OnTouchUp(self: Label_17$18,e: TouchEventArgs)OnTouchUp(self: TextBox_18$19,e: TouchEventArgs)OnTouchUp(self: Button_19$20,e: TouchEventArgs)OnTouchUp(self: CheckBox_20$21,e: TouchEventArgs)OnTouchUp(self: ComboBox_21$22,e: TouchEventArgs)OnTouchUp(self: Separator_22$23,e: TouchEventArgs)
  """
  pass
 def OnVisualChildrenChanged(self,*args):
  """
  OnVisualChildrenChanged(self: Visual,visualAdded: DependencyObject,visualRemoved: DependencyObject)
   Called when the System.Windows.Media.VisualCollection of the visual object is 
    modified.
  
  
   visualAdded: The System.Windows.Media.Visual that was added to the collection
   visualRemoved: The System.Windows.Media.Visual that was removed from the collection
  OnVisualChildrenChanged(self: Window_16$17,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Label_17$18,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: TextBox_18$19,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Button_19$20,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: CheckBox_20$21,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: ComboBox_21$22,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Separator_22$23,visualAdded: DependencyObject,visualRemoved: DependencyObject)
  """
  pass
 def OnVisualParentChanged(self,*args):
  """
  OnVisualParentChanged(self: UIElement,oldParent: DependencyObject)
   Invoked when the parent element of this System.Windows.UIElement reports a 
    change to its underlying visual parent.
  
  
   oldParent: The previous parent. This may be provided as null if the 
    System.Windows.DependencyObject did not have a parent element previously.
  
  OnVisualParentChanged(self: Window_16$17,oldParent: DependencyObject)OnVisualParentChanged(self: Label_17$18,oldParent: DependencyObject)OnVisualParentChanged(self: TextBox_18$19,oldParent: DependencyObject)OnVisualParentChanged(self: Button_19$20,oldParent: DependencyObject)OnVisualParentChanged(self: CheckBox_20$21,oldParent: DependencyObject)OnVisualParentChanged(self: ComboBox_21$22,oldParent: DependencyObject)OnVisualParentChanged(self: Separator_22$23,oldParent: DependencyObject)
  """
  pass
 def PredictFocus(self,direction):
  """
  PredictFocus(self: UIElement,direction: FocusNavigationDirection) -> DependencyObject
  
   When overridden in a derived class,returns the element that would receive 
    focus for a specified focus traversal direction,without actually moving focus 
    to that element.
  
  
   direction: The direction of the requested focus traversal.
   Returns: The element that would have received focus if 
    System.Windows.UIElement.MoveFocus(System.Windows.Input.TraversalRequest) were 
    actually invoked.
  """
  pass
 def RaiseEvent(self,e):
  """
  RaiseEvent(self: UIElement,e: RoutedEventArgs)
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
  ReleaseAllTouchCaptures(self: UIElement)
   Releases all captured touch devices from this element.
  """
  pass
 def ReleaseMouseCapture(self):
  """
  ReleaseMouseCapture(self: UIElement)
   Releases the mouse capture,if this element held the capture.
  """
  pass
 def ReleaseStylusCapture(self):
  """
  ReleaseStylusCapture(self: UIElement)
   Releases the stylus device capture,if this element held the capture.
  """
  pass
 def ReleaseTouchCapture(self,touchDevice):
  """
  ReleaseTouchCapture(self: UIElement,touchDevice: TouchDevice) -> bool
  
   Attempts to release the specified touch device from this element.
  
   touchDevice: The device to release.
   Returns: true if the touch device is released; otherwise,false.
  """
  pass
 def RemoveHandler(self,routedEvent,handler):
  """
  RemoveHandler(self: UIElement,routedEvent: RoutedEvent,handler: Delegate)
   Removes the specified routed event handler from this element.
  
   routedEvent: The identifier of the�routed event for which the handler is attached.
   handler: The specific handler implementation to remove from the event handler collection 
    on this element.
  """
  pass
 def RemoveVisualChild(self,*args):
  """
  RemoveVisualChild(self: Visual,child: Visual)
   Removes the parent-child relationship between two visuals.
  
   child: The child visual object to remove from the parent visual.
  RemoveVisualChild(self: Window_16$17,child: Window_16$17)RemoveVisualChild(self: Label_17$18,child: Label_17$18)RemoveVisualChild(self: TextBox_18$19,child: TextBox_18$19)RemoveVisualChild(self: Button_19$20,child: Button_19$20)RemoveVisualChild(self: CheckBox_20$21,child: CheckBox_20$21)RemoveVisualChild(self: ComboBox_21$22,child: ComboBox_21$22)RemoveVisualChild(self: Separator_22$23,child: Separator_22$23)
  """
  pass
 def ShouldSerializeCommandBindings(self):
  """
  ShouldSerializeCommandBindings(self: UIElement) -> bool
  
   Returns whether serialization processes should serialize the contents of the 
    System.Windows.UIElement.CommandBindings property on instances of this class.
  
   Returns: true if the System.Windows.UIElement.CommandBindings property value should be 
    serialized; otherwise,false.
  """
  pass
 def ShouldSerializeInputBindings(self):
  """
  ShouldSerializeInputBindings(self: UIElement) -> bool
  
   Returns whether serialization processes should serialize the contents of the 
    System.Windows.UIElement.InputBindings property on instances of this class.
  
   Returns: true if the System.Windows.UIElement.InputBindings property value should be 
    serialized; otherwise,false.
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
 def TranslatePoint(self,point,relativeTo):
  """
  TranslatePoint(self: UIElement,point: Point,relativeTo: UIElement) -> Point
  
   Translates a point relative to this element to coordinates that are relative to 
    the specified element.
  
  
   point: The point value,as relative to this element.
   relativeTo: The element to translate the given point into.
   Returns: A point value,now relative to the target element rather than this source 
    element.
  """
  pass
 def UpdateLayout(self):
  """
  UpdateLayout(self: UIElement)
   Ensures that all visual child elements of this element are properly updated for 
    layout.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 AllowDrop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this element can be used as the target of a drag-and-drop operation.  This is a dependency property.

Get: AllowDrop(self: UIElement) -> bool

Set: AllowDrop(self: UIElement)=value
"""

 AreAnyTouchesCaptured=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether at least one touch is captured to this element.

Get: AreAnyTouchesCaptured(self: UIElement) -> bool

"""

 AreAnyTouchesCapturedWithin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether at least one touch is captured to this element or to any child elements in its visual tree.

Get: AreAnyTouchesCapturedWithin(self: UIElement) -> bool

"""

 AreAnyTouchesDirectlyOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether at least one touch is pressed over this element.

Get: AreAnyTouchesDirectlyOver(self: UIElement) -> bool

"""

 AreAnyTouchesOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether at least one touch is pressed over this element or any child elements in its visual tree.

Get: AreAnyTouchesOver(self: UIElement) -> bool

"""

 BitmapEffect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a bitmap effect that applies directly to the rendered content for this element.  This is a dependency property.

Get: BitmapEffect(self: UIElement) -> BitmapEffect

Set: BitmapEffect(self: UIElement)=value
"""

 BitmapEffectInput=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an input source for the bitmap effect that applies directly to the rendered content for this element.  This is a dependency property.

Get: BitmapEffectInput(self: UIElement) -> BitmapEffectInput

Set: BitmapEffectInput(self: UIElement)=value
"""

 CacheMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a cached representation of the System.Windows.UIElement.

Get: CacheMode(self: UIElement) -> CacheMode

Set: CacheMode(self: UIElement)=value
"""

 Clip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the geometry used to define the outline of the contents of an element.  This is a dependency property.

Get: Clip(self: UIElement) -> Geometry

Set: Clip(self: UIElement)=value
"""

 ClipToBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to clip the content of this element (or content coming from the child elements of this element) to fit into the size of the containing element.   This is a dependency property.

Get: ClipToBounds(self: UIElement) -> bool

Set: ClipToBounds(self: UIElement)=value
"""

 CommandBindings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of System.Windows.Input.CommandBinding objects associated with this element. A System.Windows.Input.CommandBinding enables command handling for this element,and declares the linkage between a command,its events,and the handlers attached by this element.

Get: CommandBindings(self: UIElement) -> CommandBindingCollection

"""

 DesiredSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size that this element computed during the measure pass of the layout process.

Get: DesiredSize(self: UIElement) -> Size

"""

 Effect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the bitmap effect to apply to the System.Windows.UIElement. This is a dependency property.

Get: Effect(self: UIElement) -> Effect

Set: Effect(self: UIElement)=value
"""

 Focusable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the element can receive focus.  This is a dependency property.

Get: Focusable(self: UIElement) -> bool

Set: Focusable(self: UIElement)=value
"""

 HasAnimatedProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this element has any animated properties.

Get: HasAnimatedProperties(self: UIElement) -> bool

"""

 HasEffectiveKeyboardFocus=property(lambda self: object(),lambda self,v: None,lambda self: None)

 InputBindings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of input bindings associated with this element.

Get: InputBindings(self: UIElement) -> InputBindingCollection

"""

 IsArrangeValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the computed size and position of child elements in this element's layout are valid.

Get: IsArrangeValid(self: UIElement) -> bool

"""

 IsEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this element is enabled in the user interface (UI).  This is a dependency property.

Get: IsEnabled(self: UIElement) -> bool

Set: IsEnabled(self: UIElement)=value
"""

 IsEnabledCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.

"""

 IsFocused=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether this element has logical focus.  This is a dependency property.

Get: IsFocused(self: UIElement) -> bool

"""

 IsHitTestVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that declares whether this element can possibly be returned as a hit test result from some portion of its rendered content. This is a dependency property.

Get: IsHitTestVisible(self: UIElement) -> bool

Set: IsHitTestVisible(self: UIElement)=value
"""

 IsInputMethodEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether an input method system,such as an Input Method Editor (IME), is enabled for processing the input to this element.

Get: IsInputMethodEnabled(self: UIElement) -> bool

"""

 IsKeyboardFocused=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this element has keyboard focus.  This is a dependency property.

Get: IsKeyboardFocused(self: UIElement) -> bool

"""

 IsKeyboardFocusWithin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether keyboard focus is anywhere within the element or its visual tree child elements.  This is a dependency property.

Get: IsKeyboardFocusWithin(self: UIElement) -> bool

"""

 IsManipulationEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether manipulation events are enabled on this System.Windows.UIElement.

Get: IsManipulationEnabled(self: UIElement) -> bool

Set: IsManipulationEnabled(self: UIElement)=value
"""

 IsMeasureValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current size returned by layout measure is valid.

Get: IsMeasureValid(self: UIElement) -> bool

"""

 IsMouseCaptured=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the mouse is captured to this element.  This is a dependency property.

Get: IsMouseCaptured(self: UIElement) -> bool

"""

 IsMouseCaptureWithin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether mouse capture is held by this element or by child elements in its visual tree. This is a dependency property.

Get: IsMouseCaptureWithin(self: UIElement) -> bool

"""

 IsMouseDirectlyOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the position of the mouse pointer corresponds to�hit test results,which take element compositing into account.  This is a dependency property.

Get: IsMouseDirectlyOver(self: UIElement) -> bool

"""

 IsMouseOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the mouse pointer is located over this element (including child elements in the visual tree).  This is a dependency property.

Get: IsMouseOver(self: UIElement) -> bool

"""

 IsStylusCaptured=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the stylus is captured by this element.  This is a dependency property.

Get: IsStylusCaptured(self: UIElement) -> bool

"""

 IsStylusCaptureWithin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether stylus capture is held by this element,or an element within the element bounds and its visual tree. This is a dependency property.

Get: IsStylusCaptureWithin(self: UIElement) -> bool

"""

 IsStylusDirectlyOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the stylus position corresponds to�hit test results,which take element compositing into account.  This is a dependency property.

Get: IsStylusDirectlyOver(self: UIElement) -> bool

"""

 IsStylusOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the stylus cursor is located over this element (including visual child elements).  This is a dependency property.

Get: IsStylusOver(self: UIElement) -> bool

"""

 IsVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this element is visible in the user interface (UI).  This is a dependency property.

Get: IsVisible(self: UIElement) -> bool

"""

 Opacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the opacity factor applied to the entire System.Windows.UIElement when it is rendered in the user interface (UI).  This is a dependency property.

Get: Opacity(self: UIElement) -> float

Set: Opacity(self: UIElement)=value
"""

 OpacityMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an opacity mask,as a System.Windows.Media.Brush implementation that is applied to any alpha-channel masking for the rendered content of this element.  This is a dependency property.

Get: OpacityMask(self: UIElement) -> Brush

Set: OpacityMask(self: UIElement)=value
"""

 PersistId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that uniquely identifies this element.

Get: PersistId(self: UIElement) -> int

"""

 RenderSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets (or sets,but see Remarks) the final render size of this element.

Get: RenderSize(self: UIElement) -> Size

Set: RenderSize(self: UIElement)=value
"""

 RenderTransform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets transform information that affects the rendering position of this element.  This is a dependency property.

Get: RenderTransform(self: UIElement) -> Transform

Set: RenderTransform(self: UIElement)=value
"""

 RenderTransformOrigin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the center point of any possible render transform declared by System.Windows.UIElement.RenderTransform,relative to the bounds of the element.  This is a dependency property.

Get: RenderTransformOrigin(self: UIElement) -> Point

Set: RenderTransformOrigin(self: UIElement)=value
"""

 SnapsToDevicePixels=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines whether rendering for this element should use device-specific pixel settings during rendering.  This is a dependency property.

Get: SnapsToDevicePixels(self: UIElement) -> bool

Set: SnapsToDevicePixels(self: UIElement)=value
"""

 StylusPlugIns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of all stylus plug-in (customization) objects associated with this element.

"""

 TouchesCaptured=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all touch devices that are captured to this element.

Get: TouchesCaptured(self: UIElement) -> IEnumerable[TouchDevice]

"""

 TouchesCapturedWithin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all touch devices that are captured to this element or any child elements in its visual tree.

Get: TouchesCapturedWithin(self: UIElement) -> IEnumerable[TouchDevice]

"""

 TouchesDirectlyOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all touch devices that are over this element.

Get: TouchesDirectlyOver(self: UIElement) -> IEnumerable[TouchDevice]

"""

 TouchesOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all touch devices that are over this element or any child elements in its visual tree.

Get: TouchesOver(self: UIElement) -> IEnumerable[TouchDevice]

"""

 Uid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the unique identifier (for localization) for this element. This is a dependency property.

Get: Uid(self: UIElement) -> str

Set: Uid(self: UIElement)=value
"""

 Visibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the user interface (UI) visibility of this element.  This is a dependency property.

Get: Visibility(self: UIElement) -> Visibility

Set: Visibility(self: UIElement)=value
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
 """Gets the number of child elements for the System.Windows.Media.Visual.

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


 AllowDropProperty=None
 AreAnyTouchesCapturedProperty=None
 AreAnyTouchesCapturedWithinProperty=None
 AreAnyTouchesDirectlyOverProperty=None
 AreAnyTouchesOverProperty=None
 BitmapEffectInputProperty=None
 BitmapEffectProperty=None
 CacheModeProperty=None
 ClipProperty=None
 ClipToBoundsProperty=None
 DragEnter=None
 DragEnterEvent=None
 DragLeave=None
 DragLeaveEvent=None
 DragOver=None
 DragOverEvent=None
 Drop=None
 DropEvent=None
 EffectProperty=None
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
 IsHitTestVisibleChanged=None
 IsHitTestVisibleProperty=None
 IsKeyboardFocusedChanged=None
 IsKeyboardFocusedProperty=None
 IsKeyboardFocusWithinChanged=None
 IsKeyboardFocusWithinProperty=None
 IsManipulationEnabledProperty=None
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
 IsVisibleChanged=None
 IsVisibleProperty=None
 KeyDown=None
 KeyDownEvent=None
 KeyUp=None
 KeyUpEvent=None
 LayoutUpdated=None
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
 ManipulationBoundaryFeedback=None
 ManipulationBoundaryFeedbackEvent=None
 ManipulationCompleted=None
 ManipulationCompletedEvent=None
 ManipulationDelta=None
 ManipulationDeltaEvent=None
 ManipulationInertiaStarting=None
 ManipulationInertiaStartingEvent=None
 ManipulationStarted=None
 ManipulationStartedEvent=None
 ManipulationStarting=None
 ManipulationStartingEvent=None
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
 OpacityMaskProperty=None
 OpacityProperty=None
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
 RenderTransformOriginProperty=None
 RenderTransformProperty=None
 SnapsToDevicePixelsProperty=None
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
 UidProperty=None
 VisibilityProperty=None

