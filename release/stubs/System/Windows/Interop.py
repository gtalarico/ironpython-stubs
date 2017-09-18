# encoding: utf-8
# module System.Windows.Interop calls itself Interop
# from PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, WindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IKeyboardInputSink:
    """ Provides a keyboard sink for components that manages tabbing, accelerators, and mnemonics across interop boundaries and between HWNDs. This interface implements keyboard message management in WPF-Win32 interoperation scenarios. """
    def HasFocusWithin(self):
        """
        HasFocusWithin(self: IKeyboardInputSink) -> bool
        
            Gets a value that indicates whether the sink or one of its contained components 
             has focus.
        
            Returns: true if the sink or one of its contained components has focus; otherwise, false.
        """
        pass

    def OnMnemonic(self, msg, modifiers):
        """
        OnMnemonic(self: IKeyboardInputSink, msg: MSG, modifiers: ModifierKeys) -> (bool, MSG)
        
            Called when one of the mnemonics (access keys) for this sink is invoked.
        
            msg: The message for the mnemonic and associated data. Do not modify this message 
             structure. It is passed by reference for performance reasons only.
        
            modifiers: Modifier keys.
            Returns: true if the message was handled; otherwise, false.
        """
        pass

    def RegisterKeyboardInputSink(self, sink):
        """
        RegisterKeyboardInputSink(self: IKeyboardInputSink, sink: IKeyboardInputSink) -> IKeyboardInputSite
        
            Registers the System.Windows.Interop.IKeyboardInputSink interface of a 
             contained component.
        
        
            sink: The System.Windows.Interop.IKeyboardInputSink sink of the contained component.
            Returns: The System.Windows.Interop.IKeyboardInputSite site of the contained component.
        """
        pass

    def TabInto(self, request):
        """
        TabInto(self: IKeyboardInputSink, request: TraversalRequest) -> bool
        
            Sets focus on either the first tab stop or the last tab stop of the sink.
        
            request: Specifies whether focus should be set to the first or the last tab stop.
            Returns: true if the focus has been set as requested; false, if there are no tab stops.
        """
        pass

    def TranslateAccelerator(self, msg, modifiers):
        """
        TranslateAccelerator(self: IKeyboardInputSink, msg: MSG, modifiers: ModifierKeys) -> (bool, MSG)
        
            Processes keyboard input at the keydown message level.
        
            msg: The message and associated data. Do not modify this structure. It is passed by 
             reference for performance reasons only.
        
            modifiers: Modifier keys.
            Returns: true if the message was handled by the method implementation; otherwise, false.
        """
        pass

    def TranslateChar(self, msg, modifiers):
        """
        TranslateChar(self: IKeyboardInputSink, msg: MSG, modifiers: ModifierKeys) -> (bool, MSG)
        
            Processes WM_CHAR, WM_SYSCHAR, WM_DEADCHAR, and WM_SYSDEADCHAR input messages 
             before 
             System.Windows.Interop.IKeyboardInputSink.OnMnemonic(System.Windows.Interop.MSG@
             ,System.Windows.Input.ModifierKeys) is called.
        
        
            msg: The message and associated data. Do not modify this structure. It is passed by 
             reference for performance reasons only.
        
            modifiers: Modifier keys.
            Returns: true if the message was processed and 
             System.Windows.Interop.IKeyboardInputSink.OnMnemonic(System.Windows.Interop.MSG@
             ,System.Windows.Input.ModifierKeys) should not be called; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    KeyboardInputSite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a reference to the component's container's System.Windows.Interop.IKeyboardInputSite interface.

Get: KeyboardInputSite(self: IKeyboardInputSink) -> IKeyboardInputSite

Set: KeyboardInputSite(self: IKeyboardInputSink) = value
"""



class IWin32Window:
    """ Defines the contract for Win32 window handles. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the window handle.

Get: Handle(self: IWin32Window) -> IntPtr

"""



class HwndHost(FrameworkElement, IResource, IAnimatable, IInputElement, IFrameworkInputElement, ISupportInitialize, IHaveResources, IQueryAmbient, IDisposable, IWin32Window, IKeyboardInputSink):
    """ Hosts a Win32 window as an element within�Windows Presentation Foundation (WPF)�content. """
    def AddLogicalChild(self, *args): #cannot find CLR method
        """
        AddLogicalChild(self: FrameworkElement, child: object)
            Adds the provided object to the logical tree of this element.
        
            child: Child element to be added.
        AddLogicalChild(self: Window_16$17, child: object)AddLogicalChild(self: Label_17$18, child: object)AddLogicalChild(self: TextBox_18$19, child: object)AddLogicalChild(self: Button_19$20, child: object)AddLogicalChild(self: CheckBox_20$21, child: object)AddLogicalChild(self: ComboBox_21$22, child: object)AddLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def AddVisualChild(self, *args): #cannot find CLR method
        """
        AddVisualChild(self: Visual, child: Visual)
            Defines the parent-child relationship between two visuals.
        
            child: The child visual object to add to parent visual.
        AddVisualChild(self: Window_16$17, child: Window_16$17)AddVisualChild(self: Label_17$18, child: Label_17$18)AddVisualChild(self: TextBox_18$19, child: TextBox_18$19)AddVisualChild(self: Button_19$20, child: Button_19$20)AddVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)AddVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)AddVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ArrangeCore(self, *args): #cannot find CLR method
        """
        ArrangeCore(self: FrameworkElement, finalRect: Rect)
            Implements System.Windows.UIElement.ArrangeCore(System.Windows.Rect) (defined 
             as virtual in System.Windows.UIElement) and seals the implementation.
        
        
            finalRect: The final area within the parent that this element should use to arrange itself 
             and its children.
        
        ArrangeCore(self: Window_16$17, finalRect: Rect)ArrangeCore(self: Label_17$18, finalRect: Rect)ArrangeCore(self: TextBox_18$19, finalRect: Rect)ArrangeCore(self: Button_19$20, finalRect: Rect)ArrangeCore(self: CheckBox_20$21, finalRect: Rect)ArrangeCore(self: ComboBox_21$22, finalRect: Rect)ArrangeCore(self: Separator_22$23, finalRect: Rect)
        """
        pass

    def ArrangeOverride(self, *args): #cannot find CLR method
        """
        ArrangeOverride(self: FrameworkElement, finalSize: Size) -> Size
        
            When overridden in a derived class, positions child elements and determines a 
             size for a System.Windows.FrameworkElement derived class.
        
        
            finalSize: The final area within the parent that this element should use to arrange itself 
             and its children.
        
            Returns: The actual size used.
        ArrangeOverride(self: Window_16$17, arrangeBounds: Size) -> Size
        ArrangeOverride(self: Label_17$18, arrangeBounds: Size) -> Size
        ArrangeOverride(self: TextBox_18$19, arrangeBounds: Size) -> Size
        ArrangeOverride(self: Button_19$20, arrangeBounds: Size) -> Size
        ArrangeOverride(self: CheckBox_20$21, arrangeBounds: Size) -> Size
        ArrangeOverride(self: ComboBox_21$22, arrangeBounds: Size) -> Size
        ArrangeOverride(self: Separator_22$23, arrangeBounds: Size) -> Size
        """
        pass

    def BuildWindowCore(self, *args): #cannot find CLR method
        """
        BuildWindowCore(self: HwndHost, hwndParent: HandleRef) -> HandleRef
        
            When overridden in a derived class, creates the window to be hosted.
        
            hwndParent: The window handle of the parent window.
            Returns: The handle to the child Win32�window to create.
        """
        pass

    def DestroyWindowCore(self, *args): #cannot find CLR method
        """
        DestroyWindowCore(self: HwndHost, hwnd: HandleRef)
            When overridden in a derived class, destroys the hosted window.
        
            hwnd: A structure that contains the window handle.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: HwndHost)
            Immediately frees any system resources that the object might hold.
        """
        pass

    def GetLayoutClip(self, *args): #cannot find CLR method
        """
        GetLayoutClip(self: FrameworkElement, layoutSlotSize: Size) -> Geometry
        
            Returns a geometry for a clipping mask. The mask applies if the layout system 
             attempts to arrange an element that is larger than the available display space.
        
        
            layoutSlotSize: The size of the part of the element that does visual presentation.
            Returns: The clipping geometry.
        GetLayoutClip(self: Window_16$17, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Label_17$18, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: TextBox_18$19, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Button_19$20, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: CheckBox_20$21, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: ComboBox_21$22, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Separator_22$23, layoutSlotSize: Size) -> Geometry
        """
        pass

    def GetTemplateChild(self, *args): #cannot find CLR method
        """
        GetTemplateChild(self: FrameworkElement, childName: str) -> DependencyObject
        
            Returns the named element in the visual tree of an instantiated 
             System.Windows.Controls.ControlTemplate.
        
        
            childName: Name of the child to find.
            Returns: The requested element. May be null if no element of the requested name exists.
        GetTemplateChild(self: Window_16$17, childName: str) -> DependencyObject
        GetTemplateChild(self: Label_17$18, childName: str) -> DependencyObject
        GetTemplateChild(self: TextBox_18$19, childName: str) -> DependencyObject
        GetTemplateChild(self: Button_19$20, childName: str) -> DependencyObject
        GetTemplateChild(self: CheckBox_20$21, childName: str) -> DependencyObject
        GetTemplateChild(self: ComboBox_21$22, childName: str) -> DependencyObject
        GetTemplateChild(self: Separator_22$23, childName: str) -> DependencyObject
        """
        pass

    def GetUIParentCore(self, *args): #cannot find CLR method
        """
        GetUIParentCore(self: FrameworkElement) -> DependencyObject
        
            Returns an alternative logical parent for this element if there is no visual 
             parent.
        
            Returns: Returns something other than null whenever a WPF framework-level implementation 
             of this method has a non-visual parent connection.
        
        GetUIParentCore(self: Window_16$17) -> DependencyObject
        GetUIParentCore(self: Label_17$18) -> DependencyObject
        GetUIParentCore(self: TextBox_18$19) -> DependencyObject
        GetUIParentCore(self: Button_19$20) -> DependencyObject
        GetUIParentCore(self: CheckBox_20$21) -> DependencyObject
        GetUIParentCore(self: ComboBox_21$22) -> DependencyObject
        GetUIParentCore(self: Separator_22$23) -> DependencyObject
        """
        pass

    def GetVisualChild(self, *args): #cannot find CLR method
        """
        GetVisualChild(self: FrameworkElement, index: int) -> Visual
        
            Overrides System.Windows.Media.Visual.GetVisualChild(System.Int32), and returns 
             a child at the specified index from a collection of child elements.
        
        
            index: The zero-based index of the requested child element in the collection.
            Returns: The requested child element. This should not return null; if the provided index 
             is out of range, an exception is thrown.
        
        GetVisualChild(self: Window_16$17, index: int) -> Visual
        GetVisualChild(self: Label_17$18, index: int) -> Visual
        GetVisualChild(self: TextBox_18$19, index: int) -> Visual
        GetVisualChild(self: Button_19$20, index: int) -> Visual
        GetVisualChild(self: CheckBox_20$21, index: int) -> Visual
        GetVisualChild(self: ComboBox_21$22, index: int) -> Visual
        GetVisualChild(self: Separator_22$23, index: int) -> Visual
        """
        pass

    def HasFocusWithinCore(self, *args): #cannot find CLR method
        """
        HasFocusWithinCore(self: HwndHost) -> bool
        
            Gets a value that indicates whether the sink or one of its contained components 
             has focus.
        
            Returns: true if the sink or one of its contained components has focus; otherwise, false.
        """
        pass

    def HitTestCore(self, *args): #cannot find CLR method
        """
        HitTestCore(self: UIElement, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestPara
             meters) to supply base element hit testing behavior (returning 
             System.Windows.Media.GeometryHitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated geometry.
        HitTestCore(self: UIElement, hitTestParameters: PointHitTestParameters) -> HitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParamet
             ers) to supply base element hit testing behavior (returning 
             System.Windows.Media.HitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated point.
        HitTestCore(self: Window_16$17, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Window_16$17, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        """
        pass

    def MeasureCore(self, *args): #cannot find CLR method
        """
        MeasureCore(self: FrameworkElement, availableSize: Size) -> Size
        
            Implements basic measure-pass layout system behavior for 
             System.Windows.FrameworkElement.
        
        
            availableSize: The available size that the parent element can give to the child elements.
            Returns: The desired size of this element in layout.
        MeasureCore(self: Window_16$17, availableSize: Size) -> Size
        MeasureCore(self: Label_17$18, availableSize: Size) -> Size
        MeasureCore(self: TextBox_18$19, availableSize: Size) -> Size
        MeasureCore(self: Button_19$20, availableSize: Size) -> Size
        MeasureCore(self: CheckBox_20$21, availableSize: Size) -> Size
        MeasureCore(self: ComboBox_21$22, availableSize: Size) -> Size
        MeasureCore(self: Separator_22$23, availableSize: Size) -> Size
        """
        pass

    def MeasureOverride(self, *args): #cannot find CLR method
        """
        MeasureOverride(self: HwndHost, constraint: Size) -> Size
        
            Returns the size of the window represented by the 
             System.Windows.Interop.HwndHost object, as requested by layout engine 
             operations.
        
        
            constraint: The size of the System.Windows.Interop.HwndHost object.
            Returns: The size of the System.Windows.Interop.HwndHost object.
        """
        pass

    def OnAccessKey(self, *args): #cannot find CLR method
        """
        OnAccessKey(self: UIElement, e: AccessKeyEventArgs)
            Provides class handling for when an access key that is meaningful for this 
             element is invoked.
        
        
            e: The event data to the access key event. The event data reports which key was 
             invoked, and indicate whether the System.Windows.Input.AccessKeyManager object 
             that controls the sending of these events also sent this access key invocation 
             to other elements.
        
        OnAccessKey(self: Window_16$17, e: AccessKeyEventArgs)OnAccessKey(self: Label_17$18, e: AccessKeyEventArgs)OnAccessKey(self: TextBox_18$19, e: AccessKeyEventArgs)OnAccessKey(self: Button_19$20, e: AccessKeyEventArgs)OnAccessKey(self: CheckBox_20$21, e: AccessKeyEventArgs)OnAccessKey(self: ComboBox_21$22, e: AccessKeyEventArgs)OnAccessKey(self: Separator_22$23, e: AccessKeyEventArgs)
        """
        pass

    def OnChildDesiredSizeChanged(self, *args): #cannot find CLR method
        """
        OnChildDesiredSizeChanged(self: UIElement, child: UIElement)
            Supports layout behavior when a child element is resized.
        
            child: The child element that is being resized.
        OnChildDesiredSizeChanged(self: Window_16$17, child: Window_16$17)OnChildDesiredSizeChanged(self: Label_17$18, child: Label_17$18)OnChildDesiredSizeChanged(self: TextBox_18$19, child: TextBox_18$19)OnChildDesiredSizeChanged(self: Button_19$20, child: Button_19$20)OnChildDesiredSizeChanged(self: CheckBox_20$21, child: CheckBox_20$21)OnChildDesiredSizeChanged(self: ComboBox_21$22, child: ComboBox_21$22)OnChildDesiredSizeChanged(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def OnContextMenuClosing(self, *args): #cannot find CLR method
        """
        OnContextMenuClosing(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuClosing routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: Provides data about the event.
        OnContextMenuClosing(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuClosing(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuClosing(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuClosing(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuClosing(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuClosing(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuClosing(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnContextMenuOpening(self, *args): #cannot find CLR method
        """
        OnContextMenuOpening(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuOpening routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnContextMenuOpening(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuOpening(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuOpening(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuOpening(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuOpening(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuOpening(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuOpening(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnCreateAutomationPeer(self, *args): #cannot find CLR method
        """
        OnCreateAutomationPeer(self: HwndHost) -> AutomationPeer
        
            Creates an System.Windows.Automation.Peers.AutomationPeer for 
             System.Windows.Interop.HwndHost .
        
            Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: HwndHost, oldDpi: DpiScale, newDpi: DpiScale) """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragEnter(self: Window_16$17, e: DragEventArgs)OnDragEnter(self: Label_17$18, e: DragEventArgs)OnDragEnter(self: TextBox_18$19, e: DragEventArgs)OnDragEnter(self: Button_19$20, e: DragEventArgs)OnDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragLeave(self: Window_16$17, e: DragEventArgs)OnDragLeave(self: Label_17$18, e: DragEventArgs)OnDragLeave(self: TextBox_18$19, e: DragEventArgs)OnDragLeave(self: Button_19$20, e: DragEventArgs)OnDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragOver(self: Window_16$17, e: DragEventArgs)OnDragOver(self: Label_17$18, e: DragEventArgs)OnDragOver(self: TextBox_18$19, e: DragEventArgs)OnDragOver(self: Button_19$20, e: DragEventArgs)OnDragOver(self: CheckBox_20$21, e: DragEventArgs)OnDragOver(self: ComboBox_21$22, e: DragEventArgs)OnDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDrop(self, *args): #cannot find CLR method
        """
        OnDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDrop(self: Window_16$17, e: DragEventArgs)OnDrop(self: Label_17$18, e: DragEventArgs)OnDrop(self: TextBox_18$19, e: DragEventArgs)OnDrop(self: Button_19$20, e: DragEventArgs)OnDrop(self: CheckBox_20$21, e: DragEventArgs)OnDrop(self: ComboBox_21$22, e: DragEventArgs)OnDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: FrameworkElement, e: RoutedEventArgs)
            Invoked whenever an unhandled System.Windows.UIElement.GotFocus event reaches 
             this element in its route.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnGotFocus(self: Window_16$17, e: RoutedEventArgs)OnGotFocus(self: Label_17$18, e: RoutedEventArgs)OnGotFocus(self: TextBox_18$19, e: RoutedEventArgs)OnGotFocus(self: Button_19$20, e: RoutedEventArgs)OnGotFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnGotFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnGotMouseCapture(self, *args): #cannot find CLR method
        """
        OnGotMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnGotMouseCapture(self: Window_16$17, e: MouseEventArgs)OnGotMouseCapture(self: Label_17$18, e: MouseEventArgs)OnGotMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnGotMouseCapture(self: Button_19$20, e: MouseEventArgs)OnGotMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnGotMouseCapture(self: ComboBox_21$22, e: MouseEventArgs)OnGotMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnGotStylusCapture(self, *args): #cannot find CLR method
        """
        OnGotStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnGotStylusCapture(self: Window_16$17, e: StylusEventArgs)OnGotStylusCapture(self: Label_17$18, e: StylusEventArgs)OnGotStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnGotStylusCapture(self: Button_19$20, e: StylusEventArgs)OnGotStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnGotStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnGotStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnGotTouchCapture(self, *args): #cannot find CLR method
        """
        OnGotTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.GotTouchCapture routed 
             event that occurs when a touch is captured to this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnGotTouchCapture(self: Window_16$17, e: TouchEventArgs)OnGotTouchCapture(self: Label_17$18, e: TouchEventArgs)OnGotTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnGotTouchCapture(self: Button_19$20, e: TouchEventArgs)OnGotTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnGotTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnGotTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnInitialized(self, *args): #cannot find CLR method
        """
        OnInitialized(self: FrameworkElement, e: EventArgs)
            Raises the System.Windows.FrameworkElement.Initialized event. This method is 
             invoked whenever System.Windows.FrameworkElement.IsInitialized is set to true 
             internally.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnInitialized(self: Window_16$17, e: EventArgs)OnInitialized(self: Label_17$18, e: EventArgs)OnInitialized(self: TextBox_18$19, e: EventArgs)OnInitialized(self: Button_19$20, e: EventArgs)OnInitialized(self: CheckBox_20$21, e: EventArgs)OnInitialized(self: ComboBox_21$22, e: EventArgs)OnInitialized(self: Separator_22$23, e: EventArgs)
        """
        pass

    def OnIsKeyboardFocusedChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsKeyboardFocusWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked just before the System.Windows.UIElement.IsKeyboardFocusWithinChanged 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCapturedChanged event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: HwndHost, e: KeyEventArgs)
            Called when the hosted window receives a WM_KEYDOWN message.
        
            e: The event data.
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: HwndHost, e: KeyEventArgs)
            Called when the hosted window receives a WM_KEYUP message.
        
            e: The event data.
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: UIElement, e: RoutedEventArgs)
            Raises the System.Windows.UIElement.LostFocus�routed event by using the event 
             data that is provided.
        
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
             contain the identifier for the System.Windows.UIElement.LostFocus event.
        
        OnLostFocus(self: Window_16$17, e: RoutedEventArgs)OnLostFocus(self: Label_17$18, e: RoutedEventArgs)OnLostFocus(self: TextBox_18$19, e: RoutedEventArgs)OnLostFocus(self: Button_19$20, e: RoutedEventArgs)OnLostFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnLostFocus(self: ComboBox_21$22, e: RoutedEventArgs)OnLostFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
        OnLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnLostMouseCapture(self, *args): #cannot find CLR method
        """
        OnLostMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains event data.
        OnLostMouseCapture(self: Window_16$17, e: MouseEventArgs)OnLostMouseCapture(self: Label_17$18, e: MouseEventArgs)OnLostMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnLostMouseCapture(self: Button_19$20, e: MouseEventArgs)OnLostMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnLostMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnLostStylusCapture(self, *args): #cannot find CLR method
        """
        OnLostStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains event data.
        OnLostStylusCapture(self: Window_16$17, e: StylusEventArgs)OnLostStylusCapture(self: Label_17$18, e: StylusEventArgs)OnLostStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnLostStylusCapture(self: Button_19$20, e: StylusEventArgs)OnLostStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnLostStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnLostStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnLostTouchCapture(self, *args): #cannot find CLR method
        """
        OnLostTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.LostTouchCapture 
             routed event that occurs when this element loses a touch capture.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnLostTouchCapture(self: Window_16$17, e: TouchEventArgs)OnLostTouchCapture(self: Label_17$18, e: TouchEventArgs)OnLostTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnLostTouchCapture(self: Button_19$20, e: TouchEventArgs)OnLostTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnLostTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnLostTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnManipulationBoundaryFeedback(self, *args): #cannot find CLR method
        """
        OnManipulationBoundaryFeedback(self: UIElement, e: ManipulationBoundaryFeedbackEventArgs)
            Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationBoundaryFeedback(self: Window_16$17, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Label_17$18, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: TextBox_18$19, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Button_19$20, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: CheckBox_20$21, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: ComboBox_21$22, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Separator_22$23, e: ManipulationBoundaryFeedbackEventArgs)
        """
        pass

    def OnManipulationCompleted(self, *args): #cannot find CLR method
        """
        OnManipulationCompleted(self: UIElement, e: ManipulationCompletedEventArgs)
            Called when the System.Windows.UIElement.ManipulationCompleted event occurs.
        
            e: The data for the event.
        OnManipulationCompleted(self: Window_16$17, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Label_17$18, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: TextBox_18$19, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Button_19$20, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: CheckBox_20$21, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: ComboBox_21$22, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Separator_22$23, e: ManipulationCompletedEventArgs)
        """
        pass

    def OnManipulationDelta(self, *args): #cannot find CLR method
        """
        OnManipulationDelta(self: UIElement, e: ManipulationDeltaEventArgs)
            Called when the System.Windows.UIElement.ManipulationDelta event occurs.
        
            e: The data for the event.
        OnManipulationDelta(self: Window_16$17, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Label_17$18, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: TextBox_18$19, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Button_19$20, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: CheckBox_20$21, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: ComboBox_21$22, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Separator_22$23, e: ManipulationDeltaEventArgs)
        """
        pass

    def OnManipulationInertiaStarting(self, *args): #cannot find CLR method
        """
        OnManipulationInertiaStarting(self: UIElement, e: ManipulationInertiaStartingEventArgs)
            Called when the System.Windows.UIElement.ManipulationInertiaStarting event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationInertiaStarting(self: Window_16$17, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Label_17$18, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: TextBox_18$19, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Button_19$20, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: CheckBox_20$21, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: ComboBox_21$22, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Separator_22$23, e: ManipulationInertiaStartingEventArgs)
        """
        pass

    def OnManipulationStarted(self, *args): #cannot find CLR method
        """
        OnManipulationStarted(self: UIElement, e: ManipulationStartedEventArgs)
            Called when the System.Windows.UIElement.ManipulationStarted event occurs.
        
            e: The data for the event.
        OnManipulationStarted(self: Window_16$17, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Label_17$18, e: ManipulationStartedEventArgs)OnManipulationStarted(self: TextBox_18$19, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Button_19$20, e: ManipulationStartedEventArgs)OnManipulationStarted(self: CheckBox_20$21, e: ManipulationStartedEventArgs)OnManipulationStarted(self: ComboBox_21$22, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Separator_22$23, e: ManipulationStartedEventArgs)
        """
        pass

    def OnManipulationStarting(self, *args): #cannot find CLR method
        """
        OnManipulationStarting(self: UIElement, e: ManipulationStartingEventArgs)
            Provides class handling for the System.Windows.UIElement.ManipulationStarting 
             routed event that occurs when the manipulation processor is first created.
        
        
            e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event 
             data.
        
        OnManipulationStarting(self: Window_16$17, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Label_17$18, e: ManipulationStartingEventArgs)OnManipulationStarting(self: TextBox_18$19, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Button_19$20, e: ManipulationStartingEventArgs)OnManipulationStarting(self: CheckBox_20$21, e: ManipulationStartingEventArgs)OnManipulationStarting(self: ComboBox_21$22, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Separator_22$23, e: ManipulationStartingEventArgs)
        """
        pass

    def OnMnemonicCore(self, *args): #cannot find CLR method
        """
        OnMnemonicCore(self: HwndHost, msg: MSG, modifiers: ModifierKeys) -> (bool, MSG)
        
            Called when one of the mnemonics (access keys) for this sink is invoked.
        
            msg: The message for the mnemonic and associated data.
            modifiers: Modifier keys.
            Returns: Always returns false.
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. 
             This event data reports details about the mouse button that was pressed and the 
             handled state.
        
        OnMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseEnter(self: Window_16$17, e: MouseEventArgs)OnMouseEnter(self: Label_17$18, e: MouseEventArgs)OnMouseEnter(self: TextBox_18$19, e: MouseEventArgs)OnMouseEnter(self: Button_19$20, e: MouseEventArgs)OnMouseEnter(self: CheckBox_20$21, e: MouseEventArgs)OnMouseEnter(self: ComboBox_21$22, e: MouseEventArgs)OnMouseEnter(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseLeave(self: Window_16$17, e: MouseEventArgs)OnMouseLeave(self: Label_17$18, e: MouseEventArgs)OnMouseLeave(self: TextBox_18$19, e: MouseEventArgs)OnMouseLeave(self: Button_19$20, e: MouseEventArgs)OnMouseLeave(self: CheckBox_20$21, e: MouseEventArgs)OnMouseLeave(self: ComboBox_21$22, e: MouseEventArgs)OnMouseLeave(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseMove(self: Window_16$17, e: MouseEventArgs)OnMouseMove(self: Label_17$18, e: MouseEventArgs)OnMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnMouseMove(self: Button_19$20, e: MouseEventArgs)OnMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the mouse button was released.
        
        OnMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewDragEnter(self, *args): #cannot find CLR method
        """
        OnPreviewDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragEnter(self: Window_16$17, e: DragEventArgs)OnPreviewDragEnter(self: Label_17$18, e: DragEventArgs)OnPreviewDragEnter(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragEnter(self: Button_19$20, e: DragEventArgs)OnPreviewDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragLeave(self, *args): #cannot find CLR method
        """
        OnPreviewDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragLeave(self: Window_16$17, e: DragEventArgs)OnPreviewDragLeave(self: Label_17$18, e: DragEventArgs)OnPreviewDragLeave(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragLeave(self: Button_19$20, e: DragEventArgs)OnPreviewDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragOver(self, *args): #cannot find CLR method
        """
        OnPreviewDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragOver(self: Window_16$17, e: DragEventArgs)OnPreviewDragOver(self: Label_17$18, e: DragEventArgs)OnPreviewDragOver(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragOver(self: Button_19$20, e: DragEventArgs)OnPreviewDragOver(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragOver(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDrop(self, *args): #cannot find CLR method
        """
        OnPreviewDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDrop(self: Window_16$17, e: DragEventArgs)OnPreviewDrop(self: Label_17$18, e: DragEventArgs)OnPreviewDrop(self: TextBox_18$19, e: DragEventArgs)OnPreviewDrop(self: Button_19$20, e: DragEventArgs)OnPreviewDrop(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDrop(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewGiveFeedback(self, *args): #cannot find CLR method
        """
        OnPreviewGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnPreviewGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnPreviewGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyDown(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyDown(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyDown(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewKeyUp(self, *args): #cannot find CLR method
        """
        OnPreviewKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyUp(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyUp(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyUp(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewMouseDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were pressed.
        
        OnPreviewMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnPreviewMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnPreviewMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseMove(self, *args): #cannot find CLR method
        """
        OnPreviewMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnPreviewMouseMove(self: Window_16$17, e: MouseEventArgs)OnPreviewMouseMove(self: Label_17$18, e: MouseEventArgs)OnPreviewMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnPreviewMouseMove(self: Button_19$20, e: MouseEventArgs)OnPreviewMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnPreviewMouseMove(self: ComboBox_21$22, e: MouseEventArgs)OnPreviewMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnPreviewMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnPreviewMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were released.
        
        OnPreviewMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseWheel(self, *args): #cannot find CLR method
        """
        OnPreviewMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnPreviewMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: ComboBox_21$22, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnPreviewQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnPreviewQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnPreviewStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnPreviewStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnPreviewStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnPreviewStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnPreviewStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnPreviewStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnPreviewStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnPreviewStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnPreviewStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusInRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnPreviewStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches 
             an element in its route that is derived from this class. Implement this method 
             to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnPreviewStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnPreviewStylusUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusUp(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusUp(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusUp(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewTextInput(self, *args): #cannot find CLR method
        """
        OnPreviewTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnPreviewTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnPreviewTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnPreviewTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnPreviewTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnPreviewTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnPreviewTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnPreviewTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnPreviewTouchDown(self, *args): #cannot find CLR method
        """
        OnPreviewTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchDown 
             routed event that occurs when a touch presses this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchDown(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchDown(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchDown(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchMove(self, *args): #cannot find CLR method
        """
        OnPreviewTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchMove 
             routed event that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchMove(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchMove(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchMove(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchUp(self, *args): #cannot find CLR method
        """
        OnPreviewTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed 
             event that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchUp(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchUp(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchUp(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: FrameworkElement, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this 
             System.Windows.FrameworkElement has been updated. The specific dependency 
             property that changed is reported in the arguments parameter. Overrides 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
             rtyChangedEventArgs).
        
        
            e: The event data that describes the property that changed, as well as old and new 
             values.
        
        OnPropertyChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnQueryCursor(self, *args): #cannot find CLR method
        """
        OnQueryCursor(self: UIElement, e: QueryCursorEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
        OnQueryCursor(self: Window_16$17, e: QueryCursorEventArgs)OnQueryCursor(self: Label_17$18, e: QueryCursorEventArgs)OnQueryCursor(self: TextBox_18$19, e: QueryCursorEventArgs)OnQueryCursor(self: Button_19$20, e: QueryCursorEventArgs)OnQueryCursor(self: CheckBox_20$21, e: QueryCursorEventArgs)OnQueryCursor(self: ComboBox_21$22, e: QueryCursorEventArgs)OnQueryCursor(self: Separator_22$23, e: QueryCursorEventArgs)
        """
        pass

    def OnRender(self, *args): #cannot find CLR method
        """
        OnRender(self: UIElement, drawingContext: DrawingContext)
            When overridden in a derived class, participates in rendering operations that 
             are directed by the layout system. The rendering instructions for this element 
             are not used directly when this method is invoked, and are instead preserved 
             for later asynchronous use by layout and drawing.
        
        
            drawingContext: The drawing instructions for a specific element. This context is provided to 
             the layout system.
        
        OnRender(self: Window_16$17, drawingContext: DrawingContext)OnRender(self: Label_17$18, drawingContext: DrawingContext)OnRender(self: TextBox_18$19, drawingContext: DrawingContext)OnRender(self: Button_19$20, drawingContext: DrawingContext)OnRender(self: CheckBox_20$21, drawingContext: DrawingContext)OnRender(self: ComboBox_21$22, drawingContext: DrawingContext)OnRender(self: Separator_22$23, drawingContext: DrawingContext)
        """
        pass

    def OnRenderSizeChanged(self, *args): #cannot find CLR method
        """
        OnRenderSizeChanged(self: FrameworkElement, sizeInfo: SizeChangedInfo)
            Raises the System.Windows.FrameworkElement.SizeChanged event, using the 
             specified information as part of the eventual event data.
        
        
            sizeInfo: Details of the old and new size involved in the change.
        OnRenderSizeChanged(self: Window_16$17, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Label_17$18, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: TextBox_18$19, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Button_19$20, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: CheckBox_20$21, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: ComboBox_21$22, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Separator_22$23, sizeInfo: SizeChangedInfo)
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: FrameworkElement, oldStyle: Style, newStyle: Style)
            Invoked when the style in use on this element changes, which will invalidate 
             the layout.
        
        
            oldStyle: The old style.
            newStyle: The new style.
        OnStyleChanged(self: Window_16$17, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Label_17$18, oldStyle: Style, newStyle: Style)OnStyleChanged(self: TextBox_18$19, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Button_19$20, oldStyle: Style, newStyle: Style)OnStyleChanged(self: CheckBox_20$21, oldStyle: Style, newStyle: Style)OnStyleChanged(self: ComboBox_21$22, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Separator_22$23, oldStyle: Style, newStyle: Style)
        """
        pass

    def OnStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusEnter(self: Window_16$17, e: StylusEventArgs)OnStylusEnter(self: Label_17$18, e: StylusEventArgs)OnStylusEnter(self: TextBox_18$19, e: StylusEventArgs)OnStylusEnter(self: Button_19$20, e: StylusEventArgs)OnStylusEnter(self: CheckBox_20$21, e: StylusEventArgs)OnStylusEnter(self: ComboBox_21$22, e: StylusEventArgs)OnStylusEnter(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInRange(self, *args): #cannot find CLR method
        """
        OnStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInRange(self: Window_16$17, e: StylusEventArgs)OnStylusInRange(self: Label_17$18, e: StylusEventArgs)OnStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusInRange(self: Button_19$20, e: StylusEventArgs)OnStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusLeave(self: Window_16$17, e: StylusEventArgs)OnStylusLeave(self: Label_17$18, e: StylusEventArgs)OnStylusLeave(self: TextBox_18$19, e: StylusEventArgs)OnStylusLeave(self: Button_19$20, e: StylusEventArgs)OnStylusLeave(self: CheckBox_20$21, e: StylusEventArgs)OnStylusLeave(self: ComboBox_21$22, e: StylusEventArgs)OnStylusLeave(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusMove(self: Window_16$17, e: StylusEventArgs)OnStylusMove(self: Label_17$18, e: StylusEventArgs)OnStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusMove(self: Button_19$20, e: StylusEventArgs)OnStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusUp(self: Window_16$17, e: StylusEventArgs)OnStylusUp(self: Label_17$18, e: StylusEventArgs)OnStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnStylusUp(self: Button_19$20, e: StylusEventArgs)OnStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnTextInput(self, *args): #cannot find CLR method
        """
        OnTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnToolTipClosing(self, *args): #cannot find CLR method
        """
        OnToolTipClosing(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever an unhandled System.Windows.FrameworkElement.ToolTipClosing 
             routed event reaches this class in its route. Implement this method to add 
             class handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipClosing(self: Window_16$17, e: ToolTipEventArgs)OnToolTipClosing(self: Label_17$18, e: ToolTipEventArgs)OnToolTipClosing(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipClosing(self: Button_19$20, e: ToolTipEventArgs)OnToolTipClosing(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipClosing(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipClosing(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnToolTipOpening(self, *args): #cannot find CLR method
        """
        OnToolTipOpening(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever the System.Windows.FrameworkElement.ToolTipOpening routed 
             event reaches this class in its route. Implement this method to add class 
             handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipOpening(self: Window_16$17, e: ToolTipEventArgs)OnToolTipOpening(self: Label_17$18, e: ToolTipEventArgs)OnToolTipOpening(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipOpening(self: Button_19$20, e: ToolTipEventArgs)OnToolTipOpening(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipOpening(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipOpening(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnTouchDown(self, *args): #cannot find CLR method
        """
        OnTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchDown routed event 
             that occurs when a touch presses inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchDown(self: Window_16$17, e: TouchEventArgs)OnTouchDown(self: Label_17$18, e: TouchEventArgs)OnTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnTouchDown(self: Button_19$20, e: TouchEventArgs)OnTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchEnter(self, *args): #cannot find CLR method
        """
        OnTouchEnter(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchEnter routed 
             event that occurs when a touch moves from outside to inside the bounds of this 
             element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchEnter(self: Window_16$17, e: TouchEventArgs)OnTouchEnter(self: Label_17$18, e: TouchEventArgs)OnTouchEnter(self: TextBox_18$19, e: TouchEventArgs)OnTouchEnter(self: Button_19$20, e: TouchEventArgs)OnTouchEnter(self: CheckBox_20$21, e: TouchEventArgs)OnTouchEnter(self: ComboBox_21$22, e: TouchEventArgs)OnTouchEnter(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchLeave(self, *args): #cannot find CLR method
        """
        OnTouchLeave(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchLeave routed 
             event that occurs when a touch moves from inside to outside the bounds of this 
             System.Windows.UIElement.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchLeave(self: Window_16$17, e: TouchEventArgs)OnTouchLeave(self: Label_17$18, e: TouchEventArgs)OnTouchLeave(self: TextBox_18$19, e: TouchEventArgs)OnTouchLeave(self: Button_19$20, e: TouchEventArgs)OnTouchLeave(self: CheckBox_20$21, e: TouchEventArgs)OnTouchLeave(self: ComboBox_21$22, e: TouchEventArgs)OnTouchLeave(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchMove(self, *args): #cannot find CLR method
        """
        OnTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchMove routed event 
             that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchMove(self: Window_16$17, e: TouchEventArgs)OnTouchMove(self: Label_17$18, e: TouchEventArgs)OnTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnTouchMove(self: Button_19$20, e: TouchEventArgs)OnTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchUp(self, *args): #cannot find CLR method
        """
        OnTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchUp routed event 
             that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchUp(self: Window_16$17, e: TouchEventArgs)OnTouchUp(self: Label_17$18, e: TouchEventArgs)OnTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnTouchUp(self: Button_19$20, e: TouchEventArgs)OnTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnVisualChildrenChanged(self, *args): #cannot find CLR method
        """
        OnVisualChildrenChanged(self: Visual, visualAdded: DependencyObject, visualRemoved: DependencyObject)
            Called when the System.Windows.Media.VisualCollection of the visual object is 
             modified.
        
        
            visualAdded: The System.Windows.Media.Visual that was added to the collection
            visualRemoved: The System.Windows.Media.Visual that was removed from the collection
        OnVisualChildrenChanged(self: Window_16$17, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Label_17$18, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: TextBox_18$19, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Button_19$20, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: CheckBox_20$21, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: ComboBox_21$22, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Separator_22$23, visualAdded: DependencyObject, visualRemoved: DependencyObject)
        """
        pass

    def OnVisualParentChanged(self, *args): #cannot find CLR method
        """
        OnVisualParentChanged(self: FrameworkElement, oldParent: DependencyObject)
            Invoked when the parent of this element in the visual tree is changed. 
             Overrides 
             System.Windows.UIElement.OnVisualParentChanged(System.Windows.DependencyObject).
        
        
            oldParent: The old parent element. May be null to indicate that the element did not have a 
             visual parent previously.
        
        OnVisualParentChanged(self: Window_16$17, oldParent: DependencyObject)OnVisualParentChanged(self: Label_17$18, oldParent: DependencyObject)OnVisualParentChanged(self: TextBox_18$19, oldParent: DependencyObject)OnVisualParentChanged(self: Button_19$20, oldParent: DependencyObject)OnVisualParentChanged(self: CheckBox_20$21, oldParent: DependencyObject)OnVisualParentChanged(self: ComboBox_21$22, oldParent: DependencyObject)OnVisualParentChanged(self: Separator_22$23, oldParent: DependencyObject)
        """
        pass

    def OnWindowPositionChanged(self, *args): #cannot find CLR method
        """
        OnWindowPositionChanged(self: HwndHost, rcBoundingBox: Rect)
            Called when the hosted window's position changes.
        
            rcBoundingBox: The window's position.
        """
        pass

    def ParentLayoutInvalidated(self, *args): #cannot find CLR method
        """
        ParentLayoutInvalidated(self: FrameworkElement, child: UIElement)
            Supports incremental layout implementations in specialized subclasses of 
             System.Windows.FrameworkElement. 
             System.Windows.FrameworkElement.ParentLayoutInvalidated(System.Windows.UIElement
             )  is invoked when a child element has invalidated a property that is marked in 
             metadata as affecting the parent's measure or arrange passes during layout.
        
        
            child: The child element reporting the change.
        ParentLayoutInvalidated(self: Window_16$17, child: UIElement)ParentLayoutInvalidated(self: Label_17$18, child: UIElement)ParentLayoutInvalidated(self: TextBox_18$19, child: UIElement)ParentLayoutInvalidated(self: Button_19$20, child: UIElement)ParentLayoutInvalidated(self: CheckBox_20$21, child: UIElement)ParentLayoutInvalidated(self: ComboBox_21$22, child: UIElement)ParentLayoutInvalidated(self: Separator_22$23, child: UIElement)
        """
        pass

    def RegisterKeyboardInputSinkCore(self, *args): #cannot find CLR method
        """
        RegisterKeyboardInputSinkCore(self: HwndHost, sink: IKeyboardInputSink) -> IKeyboardInputSite
        
            Registers the System.Windows.Interop.IKeyboardInputSink interface of a 
             contained component.
        
        
            sink: The System.Windows.Interop.IKeyboardInputSink sink of the contained component.
            Returns: The System.Windows.Interop.IKeyboardInputSite site of the contained component.
        """
        pass

    def RemoveLogicalChild(self, *args): #cannot find CLR method
        """
        RemoveLogicalChild(self: FrameworkElement, child: object)
            Removes the provided object from this element's logical tree. 
             System.Windows.FrameworkElement updates the affected logical tree parent 
             pointers to keep in sync with this deletion.
        
        
            child: The element to remove.
        RemoveLogicalChild(self: Window_16$17, child: object)RemoveLogicalChild(self: Label_17$18, child: object)RemoveLogicalChild(self: TextBox_18$19, child: object)RemoveLogicalChild(self: Button_19$20, child: object)RemoveLogicalChild(self: CheckBox_20$21, child: object)RemoveLogicalChild(self: ComboBox_21$22, child: object)RemoveLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def RemoveVisualChild(self, *args): #cannot find CLR method
        """
        RemoveVisualChild(self: Visual, child: Visual)
            Removes the parent-child relationship between two visuals.
        
            child: The child visual object to remove from the parent visual.
        RemoveVisualChild(self: Window_16$17, child: Window_16$17)RemoveVisualChild(self: Label_17$18, child: Label_17$18)RemoveVisualChild(self: TextBox_18$19, child: TextBox_18$19)RemoveVisualChild(self: Button_19$20, child: Button_19$20)RemoveVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)RemoveVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)RemoveVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize 
             the value for the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; 
             otherwise, false.
        
        ShouldSerializeProperty(self: Window_16$17, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Label_17$18, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: TextBox_18$19, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Button_19$20, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: CheckBox_20$21, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: ComboBox_21$22, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Separator_22$23, dp: DependencyProperty) -> bool
        """
        pass

    def TabIntoCore(self, *args): #cannot find CLR method
        """
        TabIntoCore(self: HwndHost, request: TraversalRequest) -> bool
        
            Sets focus on either the first tab stop or the last tab stop of the sink.
        
            request: Specifies whether focus should be set to the first or the last tab stop.
            Returns: Always returns false.
        """
        pass

    def TranslateAcceleratorCore(self, *args): #cannot find CLR method
        """
        TranslateAcceleratorCore(self: HwndHost, msg: MSG, modifiers: ModifierKeys) -> (bool, MSG)
        
            Processes keyboard input at the keydown message level.
        
            msg: The message and associated data. Do not modify this structure. It is passed by 
             reference for performance reasons only.
        
            modifiers: Modifier keys.
            Returns: Always returns false.
        """
        pass

    def TranslateCharCore(self, *args): #cannot find CLR method
        """
        TranslateCharCore(self: HwndHost, msg: MSG, modifiers: ModifierKeys) -> (bool, MSG)
        
            Processes WM_CHAR, WM_SYSCHAR, WM_DEADCHAR, and WM_SYSDEADCHAR input messages 
             before the 
             System.Windows.Interop.IKeyboardInputSink.OnMnemonic(System.Windows.Interop.MSG@
             ,System.Windows.Input.ModifierKeys) method is called.
        
        
            msg: The message and associated data. Do not modify this structure. It is passed by 
             reference for performance reasons only.
        
            modifiers: Modifier keys.
            Returns: Always returns false.
        """
        pass

    def UpdateWindowPos(self):
        """
        UpdateWindowPos(self: HwndHost)
            Updates the child window's size, visibility, and position to reflect the 
             current state of the element.
        """
        pass

    def WndProc(self, *args): #cannot find CLR method
        """
        WndProc(self: HwndHost, hwnd: IntPtr, msg: int, wParam: IntPtr, lParam: IntPtr, handled: bool) -> (IntPtr, bool)
        
            When overridden in a derived class, accesses the window process (handle) of the 
             hosted child window.
        
        
            hwnd: The window handle of the hosted window.
            msg: The message to act upon.
            wParam: Information that may be relevant to handling the message. This is typically 
             used to store small pieces of information, such as flags.
        
            lParam: Information that may be relevant to handling the message. This is typically 
             used to reference an object.
        
            handled: Whether events resulting should be marked handled.
            Returns: The window handle of the child window.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DefaultStyleKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key to use to reference the style for this control, when theme styles are used or defined.

"""

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the window handle  of the hosted window.

Get: Handle(self: HwndHost) -> IntPtr

"""

    HasEffectiveKeyboardFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InheritanceBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the scope limits for property value inheritance, resource key lookup, and RelativeSource FindAncestor lookup.

"""

    IsEnabledCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.

"""

    LogicalChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerator for logical child elements of this element.

"""

    StylusPlugIns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all stylus plug-in (customization) objects associated with this element.

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
    """Gets the number of visual child elements within this element.

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


    DpiChanged = None
    DpiChangedEvent = None
    MessageHook = None


class ActiveXHost(HwndHost, IResource, IAnimatable, IInputElement, IFrameworkInputElement, ISupportInitialize, IHaveResources, IQueryAmbient, IDisposable, IWin32Window, IKeyboardInputSink):
    """ Hosts an ActiveX control as an element within Windows Presentation Foundation (WPF) content. """
    def AddLogicalChild(self, *args): #cannot find CLR method
        """
        AddLogicalChild(self: FrameworkElement, child: object)
            Adds the provided object to the logical tree of this element.
        
            child: Child element to be added.
        AddLogicalChild(self: Window_16$17, child: object)AddLogicalChild(self: Label_17$18, child: object)AddLogicalChild(self: TextBox_18$19, child: object)AddLogicalChild(self: Button_19$20, child: object)AddLogicalChild(self: CheckBox_20$21, child: object)AddLogicalChild(self: ComboBox_21$22, child: object)AddLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def AddVisualChild(self, *args): #cannot find CLR method
        """
        AddVisualChild(self: Visual, child: Visual)
            Defines the parent-child relationship between two visuals.
        
            child: The child visual object to add to parent visual.
        AddVisualChild(self: Window_16$17, child: Window_16$17)AddVisualChild(self: Label_17$18, child: Label_17$18)AddVisualChild(self: TextBox_18$19, child: TextBox_18$19)AddVisualChild(self: Button_19$20, child: Button_19$20)AddVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)AddVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)AddVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ArrangeCore(self, *args): #cannot find CLR method
        """
        ArrangeCore(self: FrameworkElement, finalRect: Rect)
            Implements System.Windows.UIElement.ArrangeCore(System.Windows.Rect) (defined 
             as virtual in System.Windows.UIElement) and seals the implementation.
        
        
            finalRect: The final area within the parent that this element should use to arrange itself 
             and its children.
        
        ArrangeCore(self: Window_16$17, finalRect: Rect)ArrangeCore(self: Label_17$18, finalRect: Rect)ArrangeCore(self: TextBox_18$19, finalRect: Rect)ArrangeCore(self: Button_19$20, finalRect: Rect)ArrangeCore(self: CheckBox_20$21, finalRect: Rect)ArrangeCore(self: ComboBox_21$22, finalRect: Rect)ArrangeCore(self: Separator_22$23, finalRect: Rect)
        """
        pass

    def ArrangeOverride(self, *args): #cannot find CLR method
        """
        ArrangeOverride(self: FrameworkElement, finalSize: Size) -> Size
        
            When overridden in a derived class, positions child elements and determines a 
             size for a System.Windows.FrameworkElement derived class.
        
        
            finalSize: The final area within the parent that this element should use to arrange itself 
             and its children.
        
            Returns: The actual size used.
        ArrangeOverride(self: Window_16$17, arrangeBounds: Size) -> Size
        ArrangeOverride(self: Label_17$18, arrangeBounds: Size) -> Size
        ArrangeOverride(self: TextBox_18$19, arrangeBounds: Size) -> Size
        ArrangeOverride(self: Button_19$20, arrangeBounds: Size) -> Size
        ArrangeOverride(self: CheckBox_20$21, arrangeBounds: Size) -> Size
        ArrangeOverride(self: ComboBox_21$22, arrangeBounds: Size) -> Size
        ArrangeOverride(self: Separator_22$23, arrangeBounds: Size) -> Size
        """
        pass

    def BuildWindowCore(self, *args): #cannot find CLR method
        """
        BuildWindowCore(self: ActiveXHost, hwndParent: HandleRef) -> HandleRef
        
            Creates the System.Windows.Interop.ActiveXHost window and assigns it to a 
             parent.
        
        
            hwndParent: The parent window.
            Returns: A System.Runtime.InteropServices.HandleRef to the 
             System.Windows.Interop.ActiveXHost window.
        """
        pass

    def DestroyWindowCore(self, *args): #cannot find CLR method
        """
        DestroyWindowCore(self: ActiveXHost, hwnd: HandleRef)
            Destroys the hosted window.
        
            hwnd: A structure that contains the window handle.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ActiveXHost, disposing: bool)
            Releases the unmanaged resources that are used by the 
             System.Windows.Interop.ActiveXHost and optionally releases the managed 
             resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only 
             unmanaged resources.
        """
        pass

    def GetLayoutClip(self, *args): #cannot find CLR method
        """
        GetLayoutClip(self: FrameworkElement, layoutSlotSize: Size) -> Geometry
        
            Returns a geometry for a clipping mask. The mask applies if the layout system 
             attempts to arrange an element that is larger than the available display space.
        
        
            layoutSlotSize: The size of the part of the element that does visual presentation.
            Returns: The clipping geometry.
        GetLayoutClip(self: Window_16$17, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Label_17$18, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: TextBox_18$19, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Button_19$20, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: CheckBox_20$21, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: ComboBox_21$22, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Separator_22$23, layoutSlotSize: Size) -> Geometry
        """
        pass

    def GetTemplateChild(self, *args): #cannot find CLR method
        """
        GetTemplateChild(self: FrameworkElement, childName: str) -> DependencyObject
        
            Returns the named element in the visual tree of an instantiated 
             System.Windows.Controls.ControlTemplate.
        
        
            childName: Name of the child to find.
            Returns: The requested element. May be null if no element of the requested name exists.
        GetTemplateChild(self: Window_16$17, childName: str) -> DependencyObject
        GetTemplateChild(self: Label_17$18, childName: str) -> DependencyObject
        GetTemplateChild(self: TextBox_18$19, childName: str) -> DependencyObject
        GetTemplateChild(self: Button_19$20, childName: str) -> DependencyObject
        GetTemplateChild(self: CheckBox_20$21, childName: str) -> DependencyObject
        GetTemplateChild(self: ComboBox_21$22, childName: str) -> DependencyObject
        GetTemplateChild(self: Separator_22$23, childName: str) -> DependencyObject
        """
        pass

    def GetUIParentCore(self, *args): #cannot find CLR method
        """
        GetUIParentCore(self: FrameworkElement) -> DependencyObject
        
            Returns an alternative logical parent for this element if there is no visual 
             parent.
        
            Returns: Returns something other than null whenever a WPF framework-level implementation 
             of this method has a non-visual parent connection.
        
        GetUIParentCore(self: Window_16$17) -> DependencyObject
        GetUIParentCore(self: Label_17$18) -> DependencyObject
        GetUIParentCore(self: TextBox_18$19) -> DependencyObject
        GetUIParentCore(self: Button_19$20) -> DependencyObject
        GetUIParentCore(self: CheckBox_20$21) -> DependencyObject
        GetUIParentCore(self: ComboBox_21$22) -> DependencyObject
        GetUIParentCore(self: Separator_22$23) -> DependencyObject
        """
        pass

    def GetVisualChild(self, *args): #cannot find CLR method
        """
        GetVisualChild(self: FrameworkElement, index: int) -> Visual
        
            Overrides System.Windows.Media.Visual.GetVisualChild(System.Int32), and returns 
             a child at the specified index from a collection of child elements.
        
        
            index: The zero-based index of the requested child element in the collection.
            Returns: The requested child element. This should not return null; if the provided index 
             is out of range, an exception is thrown.
        
        GetVisualChild(self: Window_16$17, index: int) -> Visual
        GetVisualChild(self: Label_17$18, index: int) -> Visual
        GetVisualChild(self: TextBox_18$19, index: int) -> Visual
        GetVisualChild(self: Button_19$20, index: int) -> Visual
        GetVisualChild(self: CheckBox_20$21, index: int) -> Visual
        GetVisualChild(self: ComboBox_21$22, index: int) -> Visual
        GetVisualChild(self: Separator_22$23, index: int) -> Visual
        """
        pass

    def HasFocusWithinCore(self, *args): #cannot find CLR method
        """
        HasFocusWithinCore(self: HwndHost) -> bool
        
            Gets a value that indicates whether the sink or one of its contained components 
             has focus.
        
            Returns: true if the sink or one of its contained components has focus; otherwise, false.
        """
        pass

    def HitTestCore(self, *args): #cannot find CLR method
        """
        HitTestCore(self: UIElement, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestPara
             meters) to supply base element hit testing behavior (returning 
             System.Windows.Media.GeometryHitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated geometry.
        HitTestCore(self: UIElement, hitTestParameters: PointHitTestParameters) -> HitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParamet
             ers) to supply base element hit testing behavior (returning 
             System.Windows.Media.HitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated point.
        HitTestCore(self: Window_16$17, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Window_16$17, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        """
        pass

    def MeasureCore(self, *args): #cannot find CLR method
        """
        MeasureCore(self: FrameworkElement, availableSize: Size) -> Size
        
            Implements basic measure-pass layout system behavior for 
             System.Windows.FrameworkElement.
        
        
            availableSize: The available size that the parent element can give to the child elements.
            Returns: The desired size of this element in layout.
        MeasureCore(self: Window_16$17, availableSize: Size) -> Size
        MeasureCore(self: Label_17$18, availableSize: Size) -> Size
        MeasureCore(self: TextBox_18$19, availableSize: Size) -> Size
        MeasureCore(self: Button_19$20, availableSize: Size) -> Size
        MeasureCore(self: CheckBox_20$21, availableSize: Size) -> Size
        MeasureCore(self: ComboBox_21$22, availableSize: Size) -> Size
        MeasureCore(self: Separator_22$23, availableSize: Size) -> Size
        """
        pass

    def MeasureOverride(self, *args): #cannot find CLR method
        """
        MeasureOverride(self: ActiveXHost, swConstraint: Size) -> Size
        
            Returns the size of the window represented by the 
             System.Windows.Interop.HwndHost object, as requested by layout engine 
             operations.
        
        
            swConstraint: The size of the System.Windows.Interop.HwndHost object.
            Returns: The size of the System.Windows.Interop.HwndHost object.
        """
        pass

    def OnAccessKey(self, *args): #cannot find CLR method
        """
        OnAccessKey(self: ActiveXHost, args: AccessKeyEventArgs)
            Provides class handling for when an access key that is meaningful for this 
             element is invoked.
        
        
            args: The event data to the access key event. The event data reports which key was 
             invoked, and indicate whether the System.Windows.Input.AccessKeyManager object 
             that controls the sending of these events also sent this access key invocation 
             to other elements.
        """
        pass

    def OnChildDesiredSizeChanged(self, *args): #cannot find CLR method
        """
        OnChildDesiredSizeChanged(self: UIElement, child: UIElement)
            Supports layout behavior when a child element is resized.
        
            child: The child element that is being resized.
        OnChildDesiredSizeChanged(self: Window_16$17, child: Window_16$17)OnChildDesiredSizeChanged(self: Label_17$18, child: Label_17$18)OnChildDesiredSizeChanged(self: TextBox_18$19, child: TextBox_18$19)OnChildDesiredSizeChanged(self: Button_19$20, child: Button_19$20)OnChildDesiredSizeChanged(self: CheckBox_20$21, child: CheckBox_20$21)OnChildDesiredSizeChanged(self: ComboBox_21$22, child: ComboBox_21$22)OnChildDesiredSizeChanged(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def OnContextMenuClosing(self, *args): #cannot find CLR method
        """
        OnContextMenuClosing(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuClosing routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: Provides data about the event.
        OnContextMenuClosing(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuClosing(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuClosing(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuClosing(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuClosing(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuClosing(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuClosing(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnContextMenuOpening(self, *args): #cannot find CLR method
        """
        OnContextMenuOpening(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuOpening routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnContextMenuOpening(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuOpening(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuOpening(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuOpening(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuOpening(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuOpening(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuOpening(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnCreateAutomationPeer(self, *args): #cannot find CLR method
        """
        OnCreateAutomationPeer(self: HwndHost) -> AutomationPeer
        
            Creates an System.Windows.Automation.Peers.AutomationPeer for 
             System.Windows.Interop.HwndHost .
        
            Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: HwndHost, oldDpi: DpiScale, newDpi: DpiScale) """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragEnter(self: Window_16$17, e: DragEventArgs)OnDragEnter(self: Label_17$18, e: DragEventArgs)OnDragEnter(self: TextBox_18$19, e: DragEventArgs)OnDragEnter(self: Button_19$20, e: DragEventArgs)OnDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragLeave(self: Window_16$17, e: DragEventArgs)OnDragLeave(self: Label_17$18, e: DragEventArgs)OnDragLeave(self: TextBox_18$19, e: DragEventArgs)OnDragLeave(self: Button_19$20, e: DragEventArgs)OnDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragOver(self: Window_16$17, e: DragEventArgs)OnDragOver(self: Label_17$18, e: DragEventArgs)OnDragOver(self: TextBox_18$19, e: DragEventArgs)OnDragOver(self: Button_19$20, e: DragEventArgs)OnDragOver(self: CheckBox_20$21, e: DragEventArgs)OnDragOver(self: ComboBox_21$22, e: DragEventArgs)OnDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDrop(self, *args): #cannot find CLR method
        """
        OnDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDrop(self: Window_16$17, e: DragEventArgs)OnDrop(self: Label_17$18, e: DragEventArgs)OnDrop(self: TextBox_18$19, e: DragEventArgs)OnDrop(self: Button_19$20, e: DragEventArgs)OnDrop(self: CheckBox_20$21, e: DragEventArgs)OnDrop(self: ComboBox_21$22, e: DragEventArgs)OnDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: FrameworkElement, e: RoutedEventArgs)
            Invoked whenever an unhandled System.Windows.UIElement.GotFocus event reaches 
             this element in its route.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnGotFocus(self: Window_16$17, e: RoutedEventArgs)OnGotFocus(self: Label_17$18, e: RoutedEventArgs)OnGotFocus(self: TextBox_18$19, e: RoutedEventArgs)OnGotFocus(self: Button_19$20, e: RoutedEventArgs)OnGotFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnGotFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnGotMouseCapture(self, *args): #cannot find CLR method
        """
        OnGotMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnGotMouseCapture(self: Window_16$17, e: MouseEventArgs)OnGotMouseCapture(self: Label_17$18, e: MouseEventArgs)OnGotMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnGotMouseCapture(self: Button_19$20, e: MouseEventArgs)OnGotMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnGotMouseCapture(self: ComboBox_21$22, e: MouseEventArgs)OnGotMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnGotStylusCapture(self, *args): #cannot find CLR method
        """
        OnGotStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnGotStylusCapture(self: Window_16$17, e: StylusEventArgs)OnGotStylusCapture(self: Label_17$18, e: StylusEventArgs)OnGotStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnGotStylusCapture(self: Button_19$20, e: StylusEventArgs)OnGotStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnGotStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnGotStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnGotTouchCapture(self, *args): #cannot find CLR method
        """
        OnGotTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.GotTouchCapture routed 
             event that occurs when a touch is captured to this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnGotTouchCapture(self: Window_16$17, e: TouchEventArgs)OnGotTouchCapture(self: Label_17$18, e: TouchEventArgs)OnGotTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnGotTouchCapture(self: Button_19$20, e: TouchEventArgs)OnGotTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnGotTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnGotTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnInitialized(self, *args): #cannot find CLR method
        """
        OnInitialized(self: FrameworkElement, e: EventArgs)
            Raises the System.Windows.FrameworkElement.Initialized event. This method is 
             invoked whenever System.Windows.FrameworkElement.IsInitialized is set to true 
             internally.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnInitialized(self: Window_16$17, e: EventArgs)OnInitialized(self: Label_17$18, e: EventArgs)OnInitialized(self: TextBox_18$19, e: EventArgs)OnInitialized(self: Button_19$20, e: EventArgs)OnInitialized(self: CheckBox_20$21, e: EventArgs)OnInitialized(self: ComboBox_21$22, e: EventArgs)OnInitialized(self: Separator_22$23, e: EventArgs)
        """
        pass

    def OnIsKeyboardFocusedChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsKeyboardFocusWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked just before the System.Windows.UIElement.IsKeyboardFocusWithinChanged 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCapturedChanged event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: HwndHost, e: KeyEventArgs)
            Called when the hosted window receives a WM_KEYDOWN message.
        
            e: The event data.
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: HwndHost, e: KeyEventArgs)
            Called when the hosted window receives a WM_KEYUP message.
        
            e: The event data.
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: UIElement, e: RoutedEventArgs)
            Raises the System.Windows.UIElement.LostFocus�routed event by using the event 
             data that is provided.
        
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
             contain the identifier for the System.Windows.UIElement.LostFocus event.
        
        OnLostFocus(self: Window_16$17, e: RoutedEventArgs)OnLostFocus(self: Label_17$18, e: RoutedEventArgs)OnLostFocus(self: TextBox_18$19, e: RoutedEventArgs)OnLostFocus(self: Button_19$20, e: RoutedEventArgs)OnLostFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnLostFocus(self: ComboBox_21$22, e: RoutedEventArgs)OnLostFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
        OnLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnLostMouseCapture(self, *args): #cannot find CLR method
        """
        OnLostMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains event data.
        OnLostMouseCapture(self: Window_16$17, e: MouseEventArgs)OnLostMouseCapture(self: Label_17$18, e: MouseEventArgs)OnLostMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnLostMouseCapture(self: Button_19$20, e: MouseEventArgs)OnLostMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnLostMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnLostStylusCapture(self, *args): #cannot find CLR method
        """
        OnLostStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains event data.
        OnLostStylusCapture(self: Window_16$17, e: StylusEventArgs)OnLostStylusCapture(self: Label_17$18, e: StylusEventArgs)OnLostStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnLostStylusCapture(self: Button_19$20, e: StylusEventArgs)OnLostStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnLostStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnLostStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnLostTouchCapture(self, *args): #cannot find CLR method
        """
        OnLostTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.LostTouchCapture 
             routed event that occurs when this element loses a touch capture.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnLostTouchCapture(self: Window_16$17, e: TouchEventArgs)OnLostTouchCapture(self: Label_17$18, e: TouchEventArgs)OnLostTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnLostTouchCapture(self: Button_19$20, e: TouchEventArgs)OnLostTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnLostTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnLostTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnManipulationBoundaryFeedback(self, *args): #cannot find CLR method
        """
        OnManipulationBoundaryFeedback(self: UIElement, e: ManipulationBoundaryFeedbackEventArgs)
            Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationBoundaryFeedback(self: Window_16$17, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Label_17$18, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: TextBox_18$19, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Button_19$20, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: CheckBox_20$21, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: ComboBox_21$22, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Separator_22$23, e: ManipulationBoundaryFeedbackEventArgs)
        """
        pass

    def OnManipulationCompleted(self, *args): #cannot find CLR method
        """
        OnManipulationCompleted(self: UIElement, e: ManipulationCompletedEventArgs)
            Called when the System.Windows.UIElement.ManipulationCompleted event occurs.
        
            e: The data for the event.
        OnManipulationCompleted(self: Window_16$17, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Label_17$18, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: TextBox_18$19, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Button_19$20, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: CheckBox_20$21, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: ComboBox_21$22, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Separator_22$23, e: ManipulationCompletedEventArgs)
        """
        pass

    def OnManipulationDelta(self, *args): #cannot find CLR method
        """
        OnManipulationDelta(self: UIElement, e: ManipulationDeltaEventArgs)
            Called when the System.Windows.UIElement.ManipulationDelta event occurs.
        
            e: The data for the event.
        OnManipulationDelta(self: Window_16$17, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Label_17$18, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: TextBox_18$19, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Button_19$20, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: CheckBox_20$21, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: ComboBox_21$22, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Separator_22$23, e: ManipulationDeltaEventArgs)
        """
        pass

    def OnManipulationInertiaStarting(self, *args): #cannot find CLR method
        """
        OnManipulationInertiaStarting(self: UIElement, e: ManipulationInertiaStartingEventArgs)
            Called when the System.Windows.UIElement.ManipulationInertiaStarting event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationInertiaStarting(self: Window_16$17, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Label_17$18, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: TextBox_18$19, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Button_19$20, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: CheckBox_20$21, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: ComboBox_21$22, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Separator_22$23, e: ManipulationInertiaStartingEventArgs)
        """
        pass

    def OnManipulationStarted(self, *args): #cannot find CLR method
        """
        OnManipulationStarted(self: UIElement, e: ManipulationStartedEventArgs)
            Called when the System.Windows.UIElement.ManipulationStarted event occurs.
        
            e: The data for the event.
        OnManipulationStarted(self: Window_16$17, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Label_17$18, e: ManipulationStartedEventArgs)OnManipulationStarted(self: TextBox_18$19, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Button_19$20, e: ManipulationStartedEventArgs)OnManipulationStarted(self: CheckBox_20$21, e: ManipulationStartedEventArgs)OnManipulationStarted(self: ComboBox_21$22, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Separator_22$23, e: ManipulationStartedEventArgs)
        """
        pass

    def OnManipulationStarting(self, *args): #cannot find CLR method
        """
        OnManipulationStarting(self: UIElement, e: ManipulationStartingEventArgs)
            Provides class handling for the System.Windows.UIElement.ManipulationStarting 
             routed event that occurs when the manipulation processor is first created.
        
        
            e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event 
             data.
        
        OnManipulationStarting(self: Window_16$17, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Label_17$18, e: ManipulationStartingEventArgs)OnManipulationStarting(self: TextBox_18$19, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Button_19$20, e: ManipulationStartingEventArgs)OnManipulationStarting(self: CheckBox_20$21, e: ManipulationStartingEventArgs)OnManipulationStarting(self: ComboBox_21$22, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Separator_22$23, e: ManipulationStartingEventArgs)
        """
        pass

    def OnMnemonicCore(self, *args): #cannot find CLR method
        """
        OnMnemonicCore(self: HwndHost, msg: MSG, modifiers: ModifierKeys) -> (bool, MSG)
        
            Called when one of the mnemonics (access keys) for this sink is invoked.
        
            msg: The message for the mnemonic and associated data.
            modifiers: Modifier keys.
            Returns: Always returns false.
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. 
             This event data reports details about the mouse button that was pressed and the 
             handled state.
        
        OnMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseEnter(self: Window_16$17, e: MouseEventArgs)OnMouseEnter(self: Label_17$18, e: MouseEventArgs)OnMouseEnter(self: TextBox_18$19, e: MouseEventArgs)OnMouseEnter(self: Button_19$20, e: MouseEventArgs)OnMouseEnter(self: CheckBox_20$21, e: MouseEventArgs)OnMouseEnter(self: ComboBox_21$22, e: MouseEventArgs)OnMouseEnter(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseLeave(self: Window_16$17, e: MouseEventArgs)OnMouseLeave(self: Label_17$18, e: MouseEventArgs)OnMouseLeave(self: TextBox_18$19, e: MouseEventArgs)OnMouseLeave(self: Button_19$20, e: MouseEventArgs)OnMouseLeave(self: CheckBox_20$21, e: MouseEventArgs)OnMouseLeave(self: ComboBox_21$22, e: MouseEventArgs)OnMouseLeave(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseMove(self: Window_16$17, e: MouseEventArgs)OnMouseMove(self: Label_17$18, e: MouseEventArgs)OnMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnMouseMove(self: Button_19$20, e: MouseEventArgs)OnMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the mouse button was released.
        
        OnMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewDragEnter(self, *args): #cannot find CLR method
        """
        OnPreviewDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragEnter(self: Window_16$17, e: DragEventArgs)OnPreviewDragEnter(self: Label_17$18, e: DragEventArgs)OnPreviewDragEnter(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragEnter(self: Button_19$20, e: DragEventArgs)OnPreviewDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragLeave(self, *args): #cannot find CLR method
        """
        OnPreviewDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragLeave(self: Window_16$17, e: DragEventArgs)OnPreviewDragLeave(self: Label_17$18, e: DragEventArgs)OnPreviewDragLeave(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragLeave(self: Button_19$20, e: DragEventArgs)OnPreviewDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragOver(self, *args): #cannot find CLR method
        """
        OnPreviewDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragOver(self: Window_16$17, e: DragEventArgs)OnPreviewDragOver(self: Label_17$18, e: DragEventArgs)OnPreviewDragOver(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragOver(self: Button_19$20, e: DragEventArgs)OnPreviewDragOver(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragOver(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDrop(self, *args): #cannot find CLR method
        """
        OnPreviewDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDrop(self: Window_16$17, e: DragEventArgs)OnPreviewDrop(self: Label_17$18, e: DragEventArgs)OnPreviewDrop(self: TextBox_18$19, e: DragEventArgs)OnPreviewDrop(self: Button_19$20, e: DragEventArgs)OnPreviewDrop(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDrop(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewGiveFeedback(self, *args): #cannot find CLR method
        """
        OnPreviewGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnPreviewGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnPreviewGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyDown(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyDown(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyDown(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewKeyUp(self, *args): #cannot find CLR method
        """
        OnPreviewKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyUp(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyUp(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyUp(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewMouseDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were pressed.
        
        OnPreviewMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnPreviewMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnPreviewMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseMove(self, *args): #cannot find CLR method
        """
        OnPreviewMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnPreviewMouseMove(self: Window_16$17, e: MouseEventArgs)OnPreviewMouseMove(self: Label_17$18, e: MouseEventArgs)OnPreviewMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnPreviewMouseMove(self: Button_19$20, e: MouseEventArgs)OnPreviewMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnPreviewMouseMove(self: ComboBox_21$22, e: MouseEventArgs)OnPreviewMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnPreviewMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnPreviewMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were released.
        
        OnPreviewMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseWheel(self, *args): #cannot find CLR method
        """
        OnPreviewMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnPreviewMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: ComboBox_21$22, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnPreviewQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnPreviewQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnPreviewStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnPreviewStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnPreviewStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnPreviewStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnPreviewStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnPreviewStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnPreviewStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnPreviewStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnPreviewStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusInRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnPreviewStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches 
             an element in its route that is derived from this class. Implement this method 
             to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnPreviewStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnPreviewStylusUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusUp(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusUp(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusUp(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewTextInput(self, *args): #cannot find CLR method
        """
        OnPreviewTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnPreviewTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnPreviewTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnPreviewTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnPreviewTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnPreviewTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnPreviewTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnPreviewTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnPreviewTouchDown(self, *args): #cannot find CLR method
        """
        OnPreviewTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchDown 
             routed event that occurs when a touch presses this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchDown(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchDown(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchDown(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchMove(self, *args): #cannot find CLR method
        """
        OnPreviewTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchMove 
             routed event that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchMove(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchMove(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchMove(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchUp(self, *args): #cannot find CLR method
        """
        OnPreviewTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed 
             event that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchUp(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchUp(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchUp(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: ActiveXHost, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this 
             System.Windows.FrameworkElement has been updated. The specific dependency 
             property that changed is reported in the arguments parameter. Overrides 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
             rtyChangedEventArgs).
        
        
            e: The event data that describes the property that changed, as well as old and new 
             values.
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnQueryCursor(self, *args): #cannot find CLR method
        """
        OnQueryCursor(self: UIElement, e: QueryCursorEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
        OnQueryCursor(self: Window_16$17, e: QueryCursorEventArgs)OnQueryCursor(self: Label_17$18, e: QueryCursorEventArgs)OnQueryCursor(self: TextBox_18$19, e: QueryCursorEventArgs)OnQueryCursor(self: Button_19$20, e: QueryCursorEventArgs)OnQueryCursor(self: CheckBox_20$21, e: QueryCursorEventArgs)OnQueryCursor(self: ComboBox_21$22, e: QueryCursorEventArgs)OnQueryCursor(self: Separator_22$23, e: QueryCursorEventArgs)
        """
        pass

    def OnRender(self, *args): #cannot find CLR method
        """
        OnRender(self: UIElement, drawingContext: DrawingContext)
            When overridden in a derived class, participates in rendering operations that 
             are directed by the layout system. The rendering instructions for this element 
             are not used directly when this method is invoked, and are instead preserved 
             for later asynchronous use by layout and drawing.
        
        
            drawingContext: The drawing instructions for a specific element. This context is provided to 
             the layout system.
        
        OnRender(self: Window_16$17, drawingContext: DrawingContext)OnRender(self: Label_17$18, drawingContext: DrawingContext)OnRender(self: TextBox_18$19, drawingContext: DrawingContext)OnRender(self: Button_19$20, drawingContext: DrawingContext)OnRender(self: CheckBox_20$21, drawingContext: DrawingContext)OnRender(self: ComboBox_21$22, drawingContext: DrawingContext)OnRender(self: Separator_22$23, drawingContext: DrawingContext)
        """
        pass

    def OnRenderSizeChanged(self, *args): #cannot find CLR method
        """
        OnRenderSizeChanged(self: FrameworkElement, sizeInfo: SizeChangedInfo)
            Raises the System.Windows.FrameworkElement.SizeChanged event, using the 
             specified information as part of the eventual event data.
        
        
            sizeInfo: Details of the old and new size involved in the change.
        OnRenderSizeChanged(self: Window_16$17, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Label_17$18, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: TextBox_18$19, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Button_19$20, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: CheckBox_20$21, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: ComboBox_21$22, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Separator_22$23, sizeInfo: SizeChangedInfo)
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: FrameworkElement, oldStyle: Style, newStyle: Style)
            Invoked when the style in use on this element changes, which will invalidate 
             the layout.
        
        
            oldStyle: The old style.
            newStyle: The new style.
        OnStyleChanged(self: Window_16$17, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Label_17$18, oldStyle: Style, newStyle: Style)OnStyleChanged(self: TextBox_18$19, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Button_19$20, oldStyle: Style, newStyle: Style)OnStyleChanged(self: CheckBox_20$21, oldStyle: Style, newStyle: Style)OnStyleChanged(self: ComboBox_21$22, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Separator_22$23, oldStyle: Style, newStyle: Style)
        """
        pass

    def OnStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusEnter(self: Window_16$17, e: StylusEventArgs)OnStylusEnter(self: Label_17$18, e: StylusEventArgs)OnStylusEnter(self: TextBox_18$19, e: StylusEventArgs)OnStylusEnter(self: Button_19$20, e: StylusEventArgs)OnStylusEnter(self: CheckBox_20$21, e: StylusEventArgs)OnStylusEnter(self: ComboBox_21$22, e: StylusEventArgs)OnStylusEnter(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInRange(self, *args): #cannot find CLR method
        """
        OnStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInRange(self: Window_16$17, e: StylusEventArgs)OnStylusInRange(self: Label_17$18, e: StylusEventArgs)OnStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusInRange(self: Button_19$20, e: StylusEventArgs)OnStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusLeave(self: Window_16$17, e: StylusEventArgs)OnStylusLeave(self: Label_17$18, e: StylusEventArgs)OnStylusLeave(self: TextBox_18$19, e: StylusEventArgs)OnStylusLeave(self: Button_19$20, e: StylusEventArgs)OnStylusLeave(self: CheckBox_20$21, e: StylusEventArgs)OnStylusLeave(self: ComboBox_21$22, e: StylusEventArgs)OnStylusLeave(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusMove(self: Window_16$17, e: StylusEventArgs)OnStylusMove(self: Label_17$18, e: StylusEventArgs)OnStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusMove(self: Button_19$20, e: StylusEventArgs)OnStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusUp(self: Window_16$17, e: StylusEventArgs)OnStylusUp(self: Label_17$18, e: StylusEventArgs)OnStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnStylusUp(self: Button_19$20, e: StylusEventArgs)OnStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnTextInput(self, *args): #cannot find CLR method
        """
        OnTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnToolTipClosing(self, *args): #cannot find CLR method
        """
        OnToolTipClosing(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever an unhandled System.Windows.FrameworkElement.ToolTipClosing 
             routed event reaches this class in its route. Implement this method to add 
             class handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipClosing(self: Window_16$17, e: ToolTipEventArgs)OnToolTipClosing(self: Label_17$18, e: ToolTipEventArgs)OnToolTipClosing(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipClosing(self: Button_19$20, e: ToolTipEventArgs)OnToolTipClosing(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipClosing(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipClosing(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnToolTipOpening(self, *args): #cannot find CLR method
        """
        OnToolTipOpening(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever the System.Windows.FrameworkElement.ToolTipOpening routed 
             event reaches this class in its route. Implement this method to add class 
             handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipOpening(self: Window_16$17, e: ToolTipEventArgs)OnToolTipOpening(self: Label_17$18, e: ToolTipEventArgs)OnToolTipOpening(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipOpening(self: Button_19$20, e: ToolTipEventArgs)OnToolTipOpening(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipOpening(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipOpening(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnTouchDown(self, *args): #cannot find CLR method
        """
        OnTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchDown routed event 
             that occurs when a touch presses inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchDown(self: Window_16$17, e: TouchEventArgs)OnTouchDown(self: Label_17$18, e: TouchEventArgs)OnTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnTouchDown(self: Button_19$20, e: TouchEventArgs)OnTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchEnter(self, *args): #cannot find CLR method
        """
        OnTouchEnter(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchEnter routed 
             event that occurs when a touch moves from outside to inside the bounds of this 
             element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchEnter(self: Window_16$17, e: TouchEventArgs)OnTouchEnter(self: Label_17$18, e: TouchEventArgs)OnTouchEnter(self: TextBox_18$19, e: TouchEventArgs)OnTouchEnter(self: Button_19$20, e: TouchEventArgs)OnTouchEnter(self: CheckBox_20$21, e: TouchEventArgs)OnTouchEnter(self: ComboBox_21$22, e: TouchEventArgs)OnTouchEnter(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchLeave(self, *args): #cannot find CLR method
        """
        OnTouchLeave(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchLeave routed 
             event that occurs when a touch moves from inside to outside the bounds of this 
             System.Windows.UIElement.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchLeave(self: Window_16$17, e: TouchEventArgs)OnTouchLeave(self: Label_17$18, e: TouchEventArgs)OnTouchLeave(self: TextBox_18$19, e: TouchEventArgs)OnTouchLeave(self: Button_19$20, e: TouchEventArgs)OnTouchLeave(self: CheckBox_20$21, e: TouchEventArgs)OnTouchLeave(self: ComboBox_21$22, e: TouchEventArgs)OnTouchLeave(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchMove(self, *args): #cannot find CLR method
        """
        OnTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchMove routed event 
             that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchMove(self: Window_16$17, e: TouchEventArgs)OnTouchMove(self: Label_17$18, e: TouchEventArgs)OnTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnTouchMove(self: Button_19$20, e: TouchEventArgs)OnTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchUp(self, *args): #cannot find CLR method
        """
        OnTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchUp routed event 
             that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchUp(self: Window_16$17, e: TouchEventArgs)OnTouchUp(self: Label_17$18, e: TouchEventArgs)OnTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnTouchUp(self: Button_19$20, e: TouchEventArgs)OnTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnVisualChildrenChanged(self, *args): #cannot find CLR method
        """
        OnVisualChildrenChanged(self: Visual, visualAdded: DependencyObject, visualRemoved: DependencyObject)
            Called when the System.Windows.Media.VisualCollection of the visual object is 
             modified.
        
        
            visualAdded: The System.Windows.Media.Visual that was added to the collection
            visualRemoved: The System.Windows.Media.Visual that was removed from the collection
        OnVisualChildrenChanged(self: Window_16$17, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Label_17$18, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: TextBox_18$19, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Button_19$20, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: CheckBox_20$21, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: ComboBox_21$22, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Separator_22$23, visualAdded: DependencyObject, visualRemoved: DependencyObject)
        """
        pass

    def OnVisualParentChanged(self, *args): #cannot find CLR method
        """
        OnVisualParentChanged(self: FrameworkElement, oldParent: DependencyObject)
            Invoked when the parent of this element in the visual tree is changed. 
             Overrides 
             System.Windows.UIElement.OnVisualParentChanged(System.Windows.DependencyObject).
        
        
            oldParent: The old parent element. May be null to indicate that the element did not have a 
             visual parent previously.
        
        OnVisualParentChanged(self: Window_16$17, oldParent: DependencyObject)OnVisualParentChanged(self: Label_17$18, oldParent: DependencyObject)OnVisualParentChanged(self: TextBox_18$19, oldParent: DependencyObject)OnVisualParentChanged(self: Button_19$20, oldParent: DependencyObject)OnVisualParentChanged(self: CheckBox_20$21, oldParent: DependencyObject)OnVisualParentChanged(self: ComboBox_21$22, oldParent: DependencyObject)OnVisualParentChanged(self: Separator_22$23, oldParent: DependencyObject)
        """
        pass

    def OnWindowPositionChanged(self, *args): #cannot find CLR method
        """
        OnWindowPositionChanged(self: ActiveXHost, bounds: Rect)
            Called when the hosted window's position changes.
        
            bounds: The window's position.
        """
        pass

    def ParentLayoutInvalidated(self, *args): #cannot find CLR method
        """
        ParentLayoutInvalidated(self: FrameworkElement, child: UIElement)
            Supports incremental layout implementations in specialized subclasses of 
             System.Windows.FrameworkElement. 
             System.Windows.FrameworkElement.ParentLayoutInvalidated(System.Windows.UIElement
             )  is invoked when a child element has invalidated a property that is marked in 
             metadata as affecting the parent's measure or arrange passes during layout.
        
        
            child: The child element reporting the change.
        ParentLayoutInvalidated(self: Window_16$17, child: UIElement)ParentLayoutInvalidated(self: Label_17$18, child: UIElement)ParentLayoutInvalidated(self: TextBox_18$19, child: UIElement)ParentLayoutInvalidated(self: Button_19$20, child: UIElement)ParentLayoutInvalidated(self: CheckBox_20$21, child: UIElement)ParentLayoutInvalidated(self: ComboBox_21$22, child: UIElement)ParentLayoutInvalidated(self: Separator_22$23, child: UIElement)
        """
        pass

    def RegisterKeyboardInputSinkCore(self, *args): #cannot find CLR method
        """
        RegisterKeyboardInputSinkCore(self: HwndHost, sink: IKeyboardInputSink) -> IKeyboardInputSite
        
            Registers the System.Windows.Interop.IKeyboardInputSink interface of a 
             contained component.
        
        
            sink: The System.Windows.Interop.IKeyboardInputSink sink of the contained component.
            Returns: The System.Windows.Interop.IKeyboardInputSite site of the contained component.
        """
        pass

    def RemoveLogicalChild(self, *args): #cannot find CLR method
        """
        RemoveLogicalChild(self: FrameworkElement, child: object)
            Removes the provided object from this element's logical tree. 
             System.Windows.FrameworkElement updates the affected logical tree parent 
             pointers to keep in sync with this deletion.
        
        
            child: The element to remove.
        RemoveLogicalChild(self: Window_16$17, child: object)RemoveLogicalChild(self: Label_17$18, child: object)RemoveLogicalChild(self: TextBox_18$19, child: object)RemoveLogicalChild(self: Button_19$20, child: object)RemoveLogicalChild(self: CheckBox_20$21, child: object)RemoveLogicalChild(self: ComboBox_21$22, child: object)RemoveLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def RemoveVisualChild(self, *args): #cannot find CLR method
        """
        RemoveVisualChild(self: Visual, child: Visual)
            Removes the parent-child relationship between two visuals.
        
            child: The child visual object to remove from the parent visual.
        RemoveVisualChild(self: Window_16$17, child: Window_16$17)RemoveVisualChild(self: Label_17$18, child: Label_17$18)RemoveVisualChild(self: TextBox_18$19, child: TextBox_18$19)RemoveVisualChild(self: Button_19$20, child: Button_19$20)RemoveVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)RemoveVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)RemoveVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize 
             the value for the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; 
             otherwise, false.
        
        ShouldSerializeProperty(self: Window_16$17, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Label_17$18, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: TextBox_18$19, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Button_19$20, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: CheckBox_20$21, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: ComboBox_21$22, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Separator_22$23, dp: DependencyProperty) -> bool
        """
        pass

    def TabIntoCore(self, *args): #cannot find CLR method
        """
        TabIntoCore(self: HwndHost, request: TraversalRequest) -> bool
        
            Sets focus on either the first tab stop or the last tab stop of the sink.
        
            request: Specifies whether focus should be set to the first or the last tab stop.
            Returns: Always returns false.
        """
        pass

    def TranslateAcceleratorCore(self, *args): #cannot find CLR method
        """
        TranslateAcceleratorCore(self: HwndHost, msg: MSG, modifiers: ModifierKeys) -> (bool, MSG)
        
            Processes keyboard input at the keydown message level.
        
            msg: The message and associated data. Do not modify this structure. It is passed by 
             reference for performance reasons only.
        
            modifiers: Modifier keys.
            Returns: Always returns false.
        """
        pass

    def TranslateCharCore(self, *args): #cannot find CLR method
        """
        TranslateCharCore(self: HwndHost, msg: MSG, modifiers: ModifierKeys) -> (bool, MSG)
        
            Processes WM_CHAR, WM_SYSCHAR, WM_DEADCHAR, and WM_SYSDEADCHAR input messages 
             before the 
             System.Windows.Interop.IKeyboardInputSink.OnMnemonic(System.Windows.Interop.MSG@
             ,System.Windows.Input.ModifierKeys) method is called.
        
        
            msg: The message and associated data. Do not modify this structure. It is passed by 
             reference for performance reasons only.
        
            modifiers: Modifier keys.
            Returns: Always returns false.
        """
        pass

    def WndProc(self, *args): #cannot find CLR method
        """
        WndProc(self: HwndHost, hwnd: IntPtr, msg: int, wParam: IntPtr, lParam: IntPtr, handled: bool) -> (IntPtr, bool)
        
            When overridden in a derived class, accesses the window process (handle) of the 
             hosted child window.
        
        
            hwnd: The window handle of the hosted window.
            msg: The message to act upon.
            wParam: Information that may be relevant to handling the message. This is typically 
             used to store small pieces of information, such as flags.
        
            lParam: Information that may be relevant to handling the message. This is typically 
             used to reference an object.
        
            handled: Whether events resulting should be marked handled.
            Returns: The window handle of the child window.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DefaultStyleKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key to use to reference the style for this control, when theme styles are used or defined.

"""

    HasEffectiveKeyboardFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InheritanceBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the scope limits for property value inheritance, resource key lookup, and RelativeSource FindAncestor lookup.

"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Interop.ActiveXHost.Dispose(System.Boolean) method has been called on the System.Windows.Interop.ActiveXHost instance.

"""

    IsEnabledCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.

"""

    LogicalChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerator for logical child elements of this element.

"""

    StylusPlugIns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all stylus plug-in (customization) objects associated with this element.

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
    """Gets the number of visual child elements within this element.

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



class BrowserInteropHelper(object):
    """ A helper class that provides information about the browser environment in which a XAML browser application (XBAP) application is hosted. """
    ClientSite = None
    HostScript = None
    IsBrowserHosted = False
    Source = None
    __all__ = []


class ComponentDispatcher(object):
    """ Enables shared control of the message pump between Win32 and WPF in interoperation scenarios. """
    @staticmethod
    def PopModal():
        """
        PopModal()
            Called to indicate that a modal thread is no longer modal.
        """
        pass

    @staticmethod
    def PushModal():
        """
        PushModal()
            Called to indicate that the thread is modal.
        """
        pass

    @staticmethod
    def RaiseIdle():
        """
        RaiseIdle()
            Called to indicate that a thread is idle.
        """
        pass

    @staticmethod
    def RaiseThreadMessage(msg):
        """
        RaiseThreadMessage(msg: MSG) -> (bool, MSG)
        
            Indicates that a new message is available for possible handling.
        
            msg: The message and its associated data.
            Returns: true, if one of the modules listening to the message loop processed the 
             message. The owner of the message loop should ignore the message. false, if the 
             message was not processed. In this case, the owner of the message pump should 
             call the Win32 function TranslateMessage followed by DispatchMessage.
        """
        pass

    CurrentKeyboardMessage = None
    EnterThreadModal = None
    IsThreadModal = True
    LeaveThreadModal = None
    ThreadFilterMessage = None
    ThreadIdle = None
    ThreadPreprocessMessage = None
    __all__ = [
        'EnterThreadModal',
        'LeaveThreadModal',
        'PopModal',
        'PushModal',
        'RaiseIdle',
        'RaiseThreadMessage',
        'ThreadFilterMessage',
        'ThreadIdle',
        'ThreadPreprocessMessage',
    ]


class CursorInteropHelper(object):
    """ Provides a static helper class for WPF/Win32 interoperation with one method, which is used to obtain a Windows Presentation Foundation (WPF)�System.Windows.Input.Cursor object based on a provided Win32 cursor handle. """
    @staticmethod
    def Create(cursorHandle):
        """
        Create(cursorHandle: SafeHandle) -> Cursor
        
            Returns a Windows Presentation Foundation (WPF)�System.Windows.Input.Cursor 
             object based on a provided Win32 cursor handle.
        
        
            cursorHandle: Cursor reference to use for interoperation.
            Returns: The Windows Presentation Foundation (WPF)�cursor object based on the provided 
             Win32 cursor handle.
        """
        pass

    __all__ = [
        'Create',
    ]


class D3DImage(ImageSource, ISealable, IAnimatable, IResource, IFormattable, IAppDomainShutdownListener):
    """
    An System.Windows.Media.ImageSource that displays a user-created Direct3D surface.
    
    D3DImage()
    D3DImage(dpiX: float, dpiY: float)
    """
    def AddDirtyRect(self, dirtyRect):
        """
        AddDirtyRect(self: D3DImage, dirtyRect: Int32Rect)
            Specifies the area of the back buffer that changed.
        
            dirtyRect: An System.Windows.Int32Rect that represents the area that changed.
        """
        pass

    def Clone(self):
        """
        Clone(self: D3DImage) -> D3DImage
        
            Creates a modifiable clone of this System.Windows.Interop.D3DImage object, 
             making deep copies of this object's values. When copying dependency properties, 
             this method copies resource references and data bindings (which may no longer 
             resolve), but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's 
             System.Windows.Freezable.IsFrozen property will be false even if the source's 
             System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: D3DImage, sourceFreezable: Freezable)
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: D3DImage) -> D3DImage
        
            Creates a modifiable clone of this System.Windows.Interop.D3DImage object, 
             making deep copies of this object's current values. Resource references, data 
             bindings, and animations are not copied, but their current values are copied.
        
            Returns: A modifiable clone of the current object. The cloned object's 
             System.Windows.Freezable.IsFrozen property will be false even if the source's 
             System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: D3DImage, sourceFreezable: Freezable)
            sourceFreezable: The System.Windows.Freezable to be cloned.
        """
        pass

    def CopyBackBuffer(self, *args): #cannot find CLR method
        """
        CopyBackBuffer(self: D3DImage) -> BitmapSource
        
            Creates a software copy of the System.Windows.Interop.D3DImage.
            Returns: A System.Windows.Media.Imaging.BitmapSource that is a software copy of the 
             current state of the back buffer; otherwise, null if the back buffer cannot be 
             read.
        """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """
        CreateInstanceCore(self: D3DImage) -> Freezable
        
            When implemented in a derived class, creates a new instance of the 
             System.Windows.Interop.D3DImage derived class.
        
            Returns: The new instance.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: D3DImage, isChecking: bool) -> bool
        
            Makes the System.Windows.Interop.D3DImage unmodifiable or determines whether it 
             can be made unmodifiable.
        
        
            isChecking: Has no effect.
            Returns: false in all cases.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: D3DImage, sourceFreezable: Freezable)
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: D3DImage, sourceFreezable: Freezable)
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
        """
        pass

    def Lock(self):
        """
        Lock(self: D3DImage)
            Locks the System.Windows.Interop.D3DImage and enables operations on the back 
             buffer.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure 
             and is not intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
             rtyChangedEventArgs) to also invoke any System.Windows.Freezable.Changed 
             handlers in response to a changing dependency property of type 
             System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old 
             and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid 
             thread. Inheritors of System.Windows.Freezable must call this method at the 
             beginning of any API that reads data members that are not dependency 
             properties.
        """
        pass

    def SetBackBuffer(self, backBufferType, backBuffer, enableSoftwareFallback=None):
        """
        SetBackBuffer(self: D3DImage, backBufferType: D3DResourceType, backBuffer: IntPtr, enableSoftwareFallback: bool)SetBackBuffer(self: D3DImage, backBufferType: D3DResourceType, backBuffer: IntPtr)
            Assigns a Direct3D surface as the source of the back buffer.
        
            backBufferType: The type of Direct3D surface. Must be a valid 
             System.Windows.Interop.D3DResourceType.
        
            backBuffer: The Direct3D surface to assign as the back buffer.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize 
             the value for the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; 
             otherwise, false.
        
        ShouldSerializeProperty(self: Window_16$17, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Label_17$18, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: TextBox_18$19, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Button_19$20, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: CheckBox_20$21, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: ComboBox_21$22, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Separator_22$23, dp: DependencyProperty) -> bool
        """
        pass

    def TryLock(self, timeout):
        """
        TryLock(self: D3DImage, timeout: Duration) -> bool
        
            Attempts to lock the System.Windows.Interop.D3DImage and waits for the 
             specified duration.
        
        
            timeout: The duration to wait for the lock to be acquired.
            Returns: true if the lock was acquired; otherwise, false.
        """
        pass

    def Unlock(self):
        """
        Unlock(self: D3DImage)
            Decrements the lock count for the System.Windows.Interop.D3DImage.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the 
             System.Windows.Freezable and invokes its System.Windows.Freezable.OnChanged 
             method. Classes that derive from System.Windows.Freezable should call this 
             method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being 
             accessed from a valid threading context. System.Windows.Freezable inheritors 
             should call this method at the beginning of any API that writes to data members 
             that are not dependency properties.
        """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dpiX=None, dpiY=None):
        """
        __new__(cls: type)
        __new__(cls: type, dpiX: float, dpiY: float)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of the System.Windows.Interop.D3DImage.

Get: Height(self: D3DImage) -> float

"""

    IsFrontBufferAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a front buffer exists.

Get: IsFrontBufferAvailable(self: D3DImage) -> bool

"""

    Metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the metadata associated with the image source.

Get: Metadata(self: D3DImage) -> ImageMetadata

"""

    PixelHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of the System.Windows.Interop.D3DImage, in pixels.

Get: PixelHeight(self: D3DImage) -> int

"""

    PixelWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width of the System.Windows.Interop.D3DImage, in pixels.

Get: PixelWidth(self: D3DImage) -> int

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width of the System.Windows.Interop.D3DImage.

Get: Width(self: D3DImage) -> float

"""


    IsFrontBufferAvailableChanged = None
    IsFrontBufferAvailableProperty = None


class D3DResourceType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the Direct3D surface types that are compatible with the System.Windows.Interop.D3DImage class.
    
    enum D3DResourceType, values: IDirect3DSurface9 (0)
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

    IDirect3DSurface9 = None
    value__ = None


class DocObjHost(MarshalByRefObject, IServiceProvider, IHostService, IBrowserHostServices, IByteRangeDownloaderService):
    """
    This type or member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.
    
    DocObjHost()
    """
    def InitializeLifetimeService(self):
        """
        InitializeLifetimeService(self: DocObjHost) -> object
        
            This type or member supports the Windows Presentation Foundation (WPF) 
             infrastructure and is not intended to be used directly from your code.
        
            Returns: A new System.Runtime.Remoting.Lifetime.ILease object.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which 
             will cause the object to be assigned a new identity when it is marshaled across 
             a remoting boundary. A value of false is usually appropriate. true to copy the 
             current System.MarshalByRefObject object's identity to its clone, which will 
             cause remoting client calls to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class DynamicScriptObject(DynamicObject, IDynamicMetaObjectProvider):
    """ Enables calls from a XAML browser application (XBAP) to the HTML window that hosts the application. """
    def ToString(self):
        """
        ToString(self: DynamicScriptObject) -> str
        
            Attempts to convert the script object to a string representation.
            Returns: A string representation of the script object, if the object can be converted; 
             otherwise, a string representation of the object's default property or method.
        """
        pass

    def TryGetIndex(self, binder, indexes, result):
        """
        TryGetIndex(self: DynamicScriptObject, binder: GetIndexBinder, indexes: Array[object]) -> (bool, object)
        
            Gets an indexed value from the script object by using the first index value 
             from the indexes collection.
        
        
            binder: The binder provided by the call site.
            indexes: The index to be retrieved.
            Returns: Always returns true.
        """
        pass

    def TryGetMember(self, binder, result):
        """
        TryGetMember(self: DynamicScriptObject, binder: GetMemberBinder) -> (bool, object)
        
            Gets an member value from the script object.
        
            binder: The binder provided by the call site.
            Returns: Always returns true.
        """
        pass

    def TryInvoke(self, binder, args, result):
        """
        TryInvoke(self: DynamicScriptObject, binder: InvokeBinder, args: Array[object]) -> (bool, object)
        
            Calls the default script method.
        
            binder: The binder provided by the call site.
            args: The arguments to pass to the default method.
            Returns: Always return true.
        """
        pass

    def TryInvokeMember(self, binder, args, result):
        """
        TryInvokeMember(self: DynamicScriptObject, binder: InvokeMemberBinder, args: Array[object]) -> (bool, object)
        
            Calls a method on the script object.
        
            binder: The binder provided by the call site.
            args: The arguments to pass to the default method.
            Returns: Always return true.
        """
        pass

    def TrySetIndex(self, binder, indexes, value):
        """
        TrySetIndex(self: DynamicScriptObject, binder: SetIndexBinder, indexes: Array[object], value: object) -> bool
        
            Sets a member on the script object by using the first index specified in the 
             indexes collection.
        
        
            binder: The binder provided by the call site.
            indexes: The index to be retrieved.
            value: The method result
            Returns: Always returns true.
        """
        pass

    def TrySetMember(self, binder, value):
        """
        TrySetMember(self: DynamicScriptObject, binder: SetMemberBinder, value: object) -> bool
        
            Sets a member on the script object to the specified value.
        
            binder: The binder provided by the call site.
            value: The value to set for the member.
            Returns: Always returns true.
        """
        pass

    def __dir__(self, *args): #cannot find CLR method
        """ __dir__(self: IDynamicMetaObjectProvider) -> list """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class HwndSource(PresentationSource, IDisposable, IWin32Window, IKeyboardInputSink):
    """
    Presents Windows Presentation Foundation (WPF) content in a Win32 window.
    
    HwndSource(classStyle: int, style: int, exStyle: int, x: int, y: int, name: str, parent: IntPtr)
    HwndSource(classStyle: int, style: int, exStyle: int, x: int, y: int, width: int, height: int, name: str, parent: IntPtr, adjustSizingForNonClientArea: bool)
    HwndSource(classStyle: int, style: int, exStyle: int, x: int, y: int, width: int, height: int, name: str, parent: IntPtr)
    HwndSource(parameters: HwndSourceParameters)
    """
    def AddHook(self, hook):
        """
        AddHook(self: HwndSource, hook: HwndSourceHook)
            Adds an event handler that receives all window messages.
        
            hook: The handler implementation (based on the System.Windows.Interop.HwndSourceHook 
             delegate) that receives the window messages.
        """
        pass

    def AddSource(self, *args): #cannot find CLR method
        """
        AddSource(self: PresentationSource)
            Adds a System.Windows.PresentationSource derived class instance to the list of 
             known presentation sources.
        """
        pass

    def ClearContentRenderedListeners(self, *args): #cannot find CLR method
        """
        ClearContentRenderedListeners(self: PresentationSource)
            Sets the list of listeners for the 
             System.Windows.PresentationSource.ContentRendered event to null.
        """
        pass

    def CreateHandleRef(self):
        """
        CreateHandleRef(self: HwndSource) -> HandleRef
        
            Gets the window handle for the System.Windows.Interop.HwndSource. The window 
             handle is packaged as part of a System.Runtime.InteropServices.HandleRef 
             structure.
        
            Returns: A structure that contains the window handle for this 
             System.Windows.Interop.HwndSource.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: HwndSource)
            Releases all managed resources that are used by the 
             System.Windows.Interop.HwndSource, and raises the 
             System.Windows.Interop.HwndSource.Disposed event.
        """
        pass

    @staticmethod
    def FromHwnd(hwnd):
        """
        FromHwnd(hwnd: IntPtr) -> HwndSource
        
            Returns the System.Windows.Interop.HwndSource object of the specified window.
        
            hwnd: The provided window handle.
            Returns: The System.Windows.Interop.HwndSource object for the window that is specified 
             by the hwnd window handle.
        """
        pass

    def GetCompositionTargetCore(self, *args): #cannot find CLR method
        """
        GetCompositionTargetCore(self: HwndSource) -> CompositionTarget
        
            Gets the visual target of the window.
            Returns: Returns the visual target of the window.
        """
        pass

    def HasFocusWithinCore(self, *args): #cannot find CLR method
        """
        HasFocusWithinCore(self: HwndSource) -> bool
        
            Gets a value that indicates whether the sink or one of its contained components 
             has focus.
        
            Returns: true if the sink or one of its contained components has focus; otherwise, false.
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: HwndSource, e: HwndDpiChangedEventArgs) """
        pass

    def OnMnemonicCore(self, *args): #cannot find CLR method
        """
        OnMnemonicCore(self: HwndSource, msg: MSG, modifiers: ModifierKeys) -> (bool, MSG)
        
            Called when one of the mnemonics (access keys) for this sink is invoked.
        
            msg: The message for the mnemonic and associated data.
            modifiers: Modifier keys.
            Returns: true if the message was handled; otherwise, false.
        """
        pass

    def RegisterKeyboardInputSinkCore(self, *args): #cannot find CLR method
        """
        RegisterKeyboardInputSinkCore(self: HwndSource, sink: IKeyboardInputSink) -> IKeyboardInputSite
        
            Registers the System.Windows.Interop.IKeyboardInputSink interface of a 
             contained component.
        
        
            sink: The System.Windows.Interop.IKeyboardInputSink sink of the contained component.
            Returns: The System.Windows.Interop.IKeyboardInputSite site of the contained component.
        """
        pass

    def RemoveHook(self, hook):
        """
        RemoveHook(self: HwndSource, hook: HwndSourceHook)
            Removes the event handlers that were added by 
             System.Windows.Interop.HwndSource.AddHook(System.Windows.Interop.HwndSourceHook)
             .
        
        
            hook: The event handler to remove.
        """
        pass

    def RemoveSource(self, *args): #cannot find CLR method
        """
        RemoveSource(self: PresentationSource)
            Removes a System.Windows.PresentationSource derived class instance from the 
             list of known presentation sources.
        """
        pass

    def RootChanged(self, *args): #cannot find CLR method
        """
        RootChanged(self: PresentationSource, oldRoot: Visual, newRoot: Visual)
            Provides notification that the root System.Windows.Media.Visual has changed.
        
            oldRoot: The old root System.Windows.Media.Visual.
            newRoot: The new root System.Windows.Media.Visual.
        """
        pass

    def TabIntoCore(self, *args): #cannot find CLR method
        """
        TabIntoCore(self: HwndSource, request: TraversalRequest) -> bool
        
            Sets focus on either the first tab stop or the last tab stop of the sink.
        
            request: Specifies whether focus should be set to the first or the last tab stop.
            Returns: true if the focus has been set as requested; false, if there are no tab stops.
        """
        pass

    def TranslateAcceleratorCore(self, *args): #cannot find CLR method
        """
        TranslateAcceleratorCore(self: HwndSource, msg: MSG, modifiers: ModifierKeys) -> (bool, MSG)
        
            Processes keyboard input at the key-down message level.
        
            msg: The message and associated data. Do not modify this structure. It is passed by 
             reference for performance reasons only.
        
            modifiers: Modifier keys.
            Returns: true if the message was handled by the method implementation; otherwise, false.
        """
        pass

    def TranslateCharCore(self, *args): #cannot find CLR method
        """
        TranslateCharCore(self: HwndSource, msg: MSG, modifiers: ModifierKeys) -> (bool, MSG)
        
            Processes WM_CHAR, WM_SYSCHAR, WM_DEADCHAR, and WM_SYSDEADCHAR input messages 
             before the 
             System.Windows.Interop.IKeyboardInputSink.OnMnemonic(System.Windows.Interop.MSG@
             ,System.Windows.Input.ModifierKeys) method is called.
        
        
            msg: The message and associated data. Do not modify this structure. It is passed by 
             reference for performance reasons only.
        
            modifiers: Modifier keys.
            Returns: true if the message was processed and 
             System.Windows.Interop.IKeyboardInputSink.OnMnemonic(System.Windows.Interop.MSG@
             ,System.Windows.Input.ModifierKeys) should not be called; otherwise, false.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, classStyle: int, style: int, exStyle: int, x: int, y: int, name: str, parent: IntPtr)
        __new__(cls: type, classStyle: int, style: int, exStyle: int, x: int, y: int, width: int, height: int, name: str, parent: IntPtr, adjustSizingForNonClientArea: bool)
        __new__(cls: type, classStyle: int, style: int, exStyle: int, x: int, y: int, width: int, height: int, name: str, parent: IntPtr)
        __new__(cls: type, parameters: HwndSourceParameters)
        """
        pass

    AcquireHwndFocusInMenuMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value that determines whether to acquire Win32 focus for the WPF containing window for this System.Windows.Interop.HwndSource.

Get: AcquireHwndFocusInMenuMode(self: HwndSource) -> bool

"""

    ChildKeyboardInputSinks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a sequence of registered input sinks.

Get: ChildKeyboardInputSinks(self: HwndSource) -> IEnumerable[IKeyboardInputSink]

"""

    CompositionTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual manager for the hosted window.

Get: CompositionTarget(self: HwndSource) -> HwndTarget

"""

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the window handle for this System.Windows.Interop.HwndSource.

Get: Handle(self: HwndSource) -> IntPtr

"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether System.Windows.Interop.HwndSource.Dispose has been called on this System.Windows.Interop.HwndSource.

Get: IsDisposed(self: HwndSource) -> bool

"""

    KeyboardInputSiteCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a reference to the component's container's System.Windows.Interop.IKeyboardInputSite interface.

"""

    RestoreFocusMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Input.RestoreFocusMode for the window.

Get: RestoreFocusMode(self: HwndSource) -> RestoreFocusMode

"""

    RootVisual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.CompositionTarget.RootVisual of the window.

Get: RootVisual(self: HwndSource) -> Visual

Set: RootVisual(self: HwndSource) = value
"""

    SizeToContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or sets whether and how the window is sized to its content.

Get: SizeToContent(self: HwndSource) -> SizeToContent

Set: SizeToContent(self: HwndSource) = value
"""

    UsesPerPixelOpacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that declares whether the per-pixel opacity of the source window content is respected.

Get: UsesPerPixelOpacity(self: HwndSource) -> bool

"""


    AutoResized = None
    DefaultAcquireHwndFocusInMenuMode = True
    Disposed = None
    DpiChanged = None
    SizeToContentChanged = None


class HwndSourceHook(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles Win32 window messages.
    
    HwndSourceHook(object: object, method: IntPtr)
    """
    def BeginInvoke(self, hwnd, msg, wParam, lParam, handled, callback, object):
        """ BeginInvoke(self: HwndSourceHook, hwnd: IntPtr, msg: int, wParam: IntPtr, lParam: IntPtr, handled: bool, callback: AsyncCallback, object: object) -> (IAsyncResult, bool) """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new 
             delegate.
        
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by 
             the current delegate.-or- null, if the method represented by the current 
             delegate does not require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, handled, result):
        """ EndInvoke(self: HwndSourceHook, handled: bool, result: IAsyncResult) -> (IntPtr, bool) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, hwnd, msg, wParam, lParam, handled):
        """ Invoke(self: HwndSourceHook, hwnd: IntPtr, msg: int, wParam: IntPtr, lParam: IntPtr, handled: bool) -> (IntPtr, bool) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate 
             that is equal to the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new 
             System.Delegate without value in its invocation list; otherwise, this instance 
             with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class HwndSourceParameters(object):
    """
    Contains the parameters that are used to create an System.Windows.Interop.HwndSource object using the System.Windows.Interop.HwndSource.#ctor(System.Windows.Interop.HwndSourceParameters) constructor.
    
    HwndSourceParameters(name: str)
    HwndSourceParameters(name: str, width: int, height: int)
    """
    def Equals(self, obj):
        """
        Equals(self: HwndSourceParameters, obj: HwndSourceParameters) -> bool
        
            Determines whether this structure is equal to a specified 
             System.Windows.Interop.HwndSourceParameters structure.
        
        
            obj: The structure to be tested for equality.
            Returns: true if the structures are equal; otherwise, false.
        Equals(self: HwndSourceParameters, obj: object) -> bool
        
            Determines whether this structure is equal to a specified object.
        
            obj: The objects to be tested for equality.
            Returns: true if the comparison is equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HwndSourceParameters) -> int
        
            Returns the hash code for this System.Windows.Interop.HwndSourceParameters 
             instance.
        
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def SetPosition(self, x, y):
        """
        SetPosition(self: HwndSourceParameters, x: int, y: int)
            Sets the values that are used for the screen position of the window for the 
             System.Windows.Interop.HwndSource.
        
        
            x: The position of the left edge of the window.
            y: The position of the upper edge of the window.
        """
        pass

    def SetSize(self, width, height):
        """
        SetSize(self: HwndSourceParameters, width: int, height: int)
            Sets the values that are used for the window size of the 
             System.Windows.Interop.HwndSource.
        
        
            width: The width of the window, in device pixels.
            height: The height of the window, in device pixels.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, width=None, height=None):
        """
        __new__[HwndSourceParameters]() -> HwndSourceParameters
        
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, width: int, height: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    AcquireHwndFocusInMenuMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value that determines whether to acquire Win32 focus for the WPF containing window when an System.Windows.Interop.HwndSource is created.

Get: AcquireHwndFocusInMenuMode(self: HwndSourceParameters) -> bool

Set: AcquireHwndFocusInMenuMode(self: HwndSourceParameters) = value
"""

    AdjustSizingForNonClientArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to include the nonclient area for sizing.

Get: AdjustSizingForNonClientArea(self: HwndSourceParameters) -> bool

Set: AdjustSizingForNonClientArea(self: HwndSourceParameters) = value
"""

    ExtendedWindowStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the extended Microsoft Windows styles for the window.

Get: ExtendedWindowStyle(self: HwndSourceParameters) -> int

Set: ExtendedWindowStyle(self: HwndSourceParameters) = value
"""

    HasAssignedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a size was assigned.

Get: HasAssignedSize(self: HwndSourceParameters) -> bool

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates the height of the window.

Get: Height(self: HwndSourceParameters) -> int

Set: Height(self: HwndSourceParameters) = value
"""

    HwndSourceHook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the message hook for the window.

Get: HwndSourceHook(self: HwndSourceParameters) -> HwndSourceHook

Set: HwndSourceHook(self: HwndSourceParameters) = value
"""

    ParentWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the window handle (HWND) of the parent for the created window.

Get: ParentWindow(self: HwndSourceParameters) -> IntPtr

Set: ParentWindow(self: HwndSourceParameters) = value
"""

    PositionX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the left-edge position of the window.

Get: PositionX(self: HwndSourceParameters) -> int

Set: PositionX(self: HwndSourceParameters) = value
"""

    PositionY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the upper-edge position of the window.

Get: PositionY(self: HwndSourceParameters) -> int

Set: PositionY(self: HwndSourceParameters) = value
"""

    RestoreFocusMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets how WPF handles restoring focus to the window.

Get: RestoreFocusMode(self: HwndSourceParameters) -> RestoreFocusMode

Set: RestoreFocusMode(self: HwndSourceParameters) = value
"""

    TreatAncestorsAsNonClientArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatAncestorsAsNonClientArea(self: HwndSourceParameters) -> bool

Set: TreatAncestorsAsNonClientArea(self: HwndSourceParameters) = value
"""

    TreatAsInputRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TreatAsInputRoot(self: HwndSourceParameters) -> bool

Set: TreatAsInputRoot(self: HwndSourceParameters) = value
"""

    UsesPerPixelOpacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that declares whether the per-pixel opacity of the source window content is respected.

Get: UsesPerPixelOpacity(self: HwndSourceParameters) -> bool

Set: UsesPerPixelOpacity(self: HwndSourceParameters) = value
"""

    UsesPerPixelTransparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UsesPerPixelTransparency(self: HwndSourceParameters) -> bool

Set: UsesPerPixelTransparency(self: HwndSourceParameters) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates the width of the window.

Get: Width(self: HwndSourceParameters) -> int

Set: Width(self: HwndSourceParameters) = value
"""

    WindowClassStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Microsoft Windows class style for the window.

Get: WindowClassStyle(self: HwndSourceParameters) -> int

Set: WindowClassStyle(self: HwndSourceParameters) = value
"""

    WindowName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the window.

Get: WindowName(self: HwndSourceParameters) -> str

Set: WindowName(self: HwndSourceParameters) = value
"""

    WindowStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the style for the window.

Get: WindowStyle(self: HwndSourceParameters) -> int

Set: WindowStyle(self: HwndSourceParameters) = value
"""



class HwndTarget(CompositionTarget, IDisposable, ICompositionTarget):
    """
    Represents a binding to a window handle that supports visual composition.
    
    HwndTarget(hwnd: IntPtr)
    """
    def Dispose(self):
        """
        Dispose(self: HwndTarget)
            Releases all resources used by the System.Windows.Interop.HwndTarget.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, hwnd):
        """ __new__(cls: type, hwnd: IntPtr) """
        pass

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the background color of the window referenced by this System.Windows.Interop.HwndTarget.

Get: BackgroundColor(self: HwndTarget) -> Color

Set: BackgroundColor(self: HwndTarget) = value
"""

    RenderMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rendering mode for the window referenced by this System.Windows.Interop.HwndTarget.

Get: RenderMode(self: HwndTarget) -> RenderMode

Set: RenderMode(self: HwndTarget) = value
"""

    RootVisual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the root visual object of the page that is hosted by the window.

Set: RootVisual(self: HwndTarget) = value
"""

    TransformFromDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a matrix that transforms the coordinates of the device that is associated with the rendering destination of this target.

Get: TransformFromDevice(self: HwndTarget) -> Matrix

"""

    TransformToDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a matrix that transforms the coordinates of this target to the device that is associated with the rendering destination.

Get: TransformToDevice(self: HwndTarget) -> Matrix

"""

    UsesPerPixelOpacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that declares whether the per-pixel opacity value of the source window content is used for rendering.

Get: UsesPerPixelOpacity(self: HwndTarget) -> bool

"""



class IErrorPage:
    """ Defines the interaction between Windows Presentation Foundation (WPF) applications that are hosting interoperation content and interpreted by the Windows Presentation Foundation (WPF) executable, and a host supplied error page. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DeploymentPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the path to an application's deployment manifest.

Get: DeploymentPath(self: IErrorPage) -> Uri

Set: DeploymentPath(self: IErrorPage) = value
"""

    ErrorFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether this represents an error or some other condition such as a warning. true denotes an error.

Get: ErrorFlag(self: IErrorPage) -> bool

Set: ErrorFlag(self: IErrorPage) = value
"""

    ErrorText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a verbose description of the error.

Get: ErrorText(self: IErrorPage) -> str

Set: ErrorText(self: IErrorPage) = value
"""

    ErrorTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the string title of the error page.

Get: ErrorTitle(self: IErrorPage) -> str

Set: ErrorTitle(self: IErrorPage) = value
"""

    GetWinFxCallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a reference to a System.Windows.Threading.DispatcherOperationCallback  handler, which can handle requests for Microsoft .NET Framework runtime downloads.

Get: GetWinFxCallback(self: IErrorPage) -> DispatcherOperationCallback

Set: GetWinFxCallback(self: IErrorPage) = value
"""

    LogFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the string path to the error's log file, if any.

Get: LogFilePath(self: IErrorPage) -> str

Set: LogFilePath(self: IErrorPage) = value
"""

    RefreshCallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a reference to a System.Windows.Threading.DispatcherOperationCallback handler, that can handle refresh of the error page.

Get: RefreshCallback(self: IErrorPage) -> DispatcherOperationCallback

Set: RefreshCallback(self: IErrorPage) = value
"""

    SupportUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a uniform resource identifier (URI) for support information associated with the error.

Get: SupportUri(self: IErrorPage) -> Uri

Set: SupportUri(self: IErrorPage) = value
"""



class IKeyboardInputSite:
    """ Manages keyboard focus within the container.  This interface implements keyboard message management in WPF-Win32 interoperation scenarios. """
    def OnNoMoreTabStops(self, request):
        """
        OnNoMoreTabStops(self: IKeyboardInputSite, request: TraversalRequest) -> bool
        
            Called by a contained component when it has reached its last tab stop and has 
             no further items to tab to.
        
        
            request: Specifies whether focus should be set to the first or the last tab stop.
            Returns: If this method returns true, the site has shifted focus to another component. 
             If this method returns false, focus is still within the calling component. The 
             component should "wrap around" and set focus to its first contained tab stop.
        """
        pass

    def Unregister(self):
        """
        Unregister(self: IKeyboardInputSite)
            Unregisters a child keyboard input sink from this site.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Sink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the keyboard sink associated with this site.

Get: Sink(self: IKeyboardInputSite) -> IKeyboardInputSink

"""



class Imaging(object):
    """ Provides managed to unmanaged interoperation support for creating image objects. """
    @staticmethod
    def CreateBitmapSourceFromHBitmap(bitmap, palette, sourceRect, sizeOptions):
        """
        CreateBitmapSourceFromHBitmap(bitmap: IntPtr, palette: IntPtr, sourceRect: Int32Rect, sizeOptions: BitmapSizeOptions) -> BitmapSource
        
            Returns a managed System.Windows.Media.Imaging.BitmapSource, based on the 
             provided pointer to an unmanaged bitmap and palette information.
        
        
            bitmap: A pointer to the unmanaged bitmap.
            palette: A pointer to the bitmap's palette map.
            sourceRect: The size of the source image.
            sizeOptions: A value of the enumeration that specifies how to handle conversions.
            Returns: The created System.Windows.Media.Imaging.BitmapSource.
        """
        pass

    @staticmethod
    def CreateBitmapSourceFromHIcon(icon, sourceRect, sizeOptions):
        """
        CreateBitmapSourceFromHIcon(icon: IntPtr, sourceRect: Int32Rect, sizeOptions: BitmapSizeOptions) -> BitmapSource
        
            Returns a managed System.Windows.Media.Imaging.BitmapSource, based on the 
             provided pointer to an unmanaged icon image.
        
        
            icon: A pointer to the unmanaged icon source.
            sourceRect: The size of the source image.
            sizeOptions: A value of the enumeration that specifies how to handle conversions.
            Returns: The created System.Windows.Media.Imaging.BitmapSource.
        """
        pass

    @staticmethod
    def CreateBitmapSourceFromMemorySection(section, pixelWidth, pixelHeight, format, stride, offset):
        """
        CreateBitmapSourceFromMemorySection(section: IntPtr, pixelWidth: int, pixelHeight: int, format: PixelFormat, stride: int, offset: int) -> BitmapSource
        
            Returns a managed System.Windows.Media.Imaging.BitmapSource, based on the 
             provided unmanaged memory location.
        
        
            section: A pointer to a memory section.
            pixelWidth: An integer that specifies the width, in pixels, of the bitmap.
            pixelHeight: An integer that specifies the height, in pixels, of the bitmap.
            format: A value of the enumeration.
            stride: The stride of the bitmap.
            offset: The byte offset into the memory stream where the image starts.
            Returns: The created System.Windows.Media.Imaging.BitmapSource.
        """
        pass

    __all__ = [
        'CreateBitmapSourceFromHBitmap',
        'CreateBitmapSourceFromHIcon',
        'CreateBitmapSourceFromMemorySection',
    ]


class InteropBitmap(BitmapSource, ISealable, IAnimatable, IResource, IFormattable):
    """ System.Windows.Interop.InteropBitmap enables developers to improve rendering performance of non-WPF�UIs that are hosted by WPF in interoperability scenarios. """
    def CheckIfSiteOfOrigin(self, *args): #cannot find CLR method
        """
        CheckIfSiteOfOrigin(self: BitmapSource)
            Checks whether the bitmap source content is from a known site of origin. This 
             method is used to make sure that pixel copying operations are safe.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: InteropBitmap, sourceFreezable: Freezable) """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: InteropBitmap, sourceFreezable: Freezable) """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """ CreateInstanceCore(self: InteropBitmap) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: BitmapSource, isChecking: bool) -> bool
        
            Makes an instance of System.Windows.Media.Imaging.BitmapSource or a derived 
             class immutable.
        
        
            isChecking: true if this instance should actually freeze itself when this method is called; 
             otherwise, false.
        
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if 
             it cannot be made unmodifiable. If isChecking is false, this method returns 
             true if the if this System.Windows.Media.Animation.Animatable is now 
             unmodifiable, or false if it cannot be made unmodifiable, with the side effect 
             of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: InteropBitmap, sourceFreezable: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: InteropBitmap, sourceFreezable: Freezable) """
        pass

    def Invalidate(self, dirtyRect=None):
        """
        Invalidate(self: InteropBitmap, dirtyRect: Nullable[Int32Rect])Invalidate(self: InteropBitmap)
            Forces the hosted non-WPF�UI to be rendered.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure 
             and is not intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
             rtyChangedEventArgs) to also invoke any System.Windows.Freezable.Changed 
             handlers in response to a changing dependency property of type 
             System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old 
             and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid 
             thread. Inheritors of System.Windows.Freezable must call this method at the 
             beginning of any API that reads data members that are not dependency 
             properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize 
             the value for the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; 
             otherwise, false.
        
        ShouldSerializeProperty(self: Window_16$17, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Label_17$18, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: TextBox_18$19, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Button_19$20, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: CheckBox_20$21, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: ComboBox_21$22, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Separator_22$23, dp: DependencyProperty) -> bool
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the 
             System.Windows.Freezable and invokes its System.Windows.Freezable.OnChanged 
             method. Classes that derive from System.Windows.Freezable should call this 
             method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being 
             accessed from a valid threading context. System.Windows.Freezable inheritors 
             should call this method at the beginning of any API that writes to data members 
             that are not dependency properties.
        """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class IProgressPage:
    """ Defines the interaction between Windows Presentation Foundation (WPF) applications that are hosting interoperation content, and a host supplied progress page. """
    def UpdateProgress(self, bytesDownloaded, bytesTotal):
        """
        UpdateProgress(self: IProgressPage, bytesDownloaded: Int64, bytesTotal: Int64)
            Provides upload progress numeric information that can be used to update the 
             progress indicators.
        
        
            bytesDownloaded: Total bytes downloaded thus far.
            bytesTotal: Total bytes that need to be downloaded for the application.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ApplicationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets  the application's name.

Get: ApplicationName(self: IProgressPage) -> str

Set: ApplicationName(self: IProgressPage) = value
"""

    DeploymentPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Uri path to the application deployment manifest.

Get: DeploymentPath(self: IProgressPage) -> Uri

Set: DeploymentPath(self: IProgressPage) = value
"""

    PublisherName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the application's publisher.

Get: PublisherName(self: IProgressPage) -> str

Set: PublisherName(self: IProgressPage) = value
"""

    RefreshCallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a reference to a System.Windows.Threading.DispatcherOperationCallback handler, that can handle the case of a user-initiated Refresh command.

Get: RefreshCallback(self: IProgressPage) -> DispatcherOperationCallback

Set: RefreshCallback(self: IProgressPage) = value
"""

    StopCallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a reference to a System.Windows.Threading.DispatcherOperationCallback handler, that can handle the case of a user-initiated Stop command.

Get: StopCallback(self: IProgressPage) -> DispatcherOperationCallback

Set: StopCallback(self: IProgressPage) = value
"""



class MSG(object):
    """ Contains message information from a thread's message queue. """
    hwnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the window handle (HWND) to the window whose window procedure receives the message.

Get: hwnd(self: MSG) -> IntPtr

Set: hwnd(self: MSG) = value
"""

    lParam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the lParam value that specifies additional information about the message. The exact meaning depends on the value of the System.Windows.Interop.MSG.message member.

Get: lParam(self: MSG) -> IntPtr

Set: lParam(self: MSG) = value
"""

    message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the message identifier.

Get: message(self: MSG) -> int

Set: message(self: MSG) = value
"""

    pt_x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x coordinate of the cursor position on the screen, when the message was posted.

Get: pt_x(self: MSG) -> int

Set: pt_x(self: MSG) = value
"""

    pt_y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y coordinate of the cursor position on the screen, when the message was posted.

Get: pt_y(self: MSG) -> int

Set: pt_y(self: MSG) = value
"""

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the time at which the message was posted.

Get: time(self: MSG) -> int

Set: time(self: MSG) = value
"""

    wParam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the wParam value for the message, which specifies additional information about the message. The exact meaning depends on the value of the message.

Get: wParam(self: MSG) -> IntPtr

Set: wParam(self: MSG) = value
"""



class RenderMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the rendering preference.
    
    enum RenderMode, values: Default (0), SoftwareOnly (1)
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

    Default = None
    SoftwareOnly = None
    value__ = None


class ThreadMessageEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Windows.Interop.ComponentDispatcher.ThreadFilterMessage and System.Windows.Interop.ComponentDispatcher.ThreadPreprocessMessage events.
    
    ThreadMessageEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, msg, handled, callback, object):
        """ BeginInvoke(self: ThreadMessageEventHandler, msg: MSG, handled: bool, callback: AsyncCallback, object: object) -> (IAsyncResult, MSG, bool) """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new 
             delegate.
        
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by 
             the current delegate.-or- null, if the method represented by the current 
             delegate does not require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, msg, handled, result):
        """ EndInvoke(self: ThreadMessageEventHandler, msg: MSG, handled: bool, result: IAsyncResult) -> (MSG, bool) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, msg, handled):
        """ Invoke(self: ThreadMessageEventHandler, msg: MSG, handled: bool) -> (MSG, bool) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate 
             that is equal to the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new 
             System.Delegate without value in its invocation list; otherwise, this instance 
             with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class WindowInteropHelper(object):
    """
    Assists interoperation between Windows Presentation Foundation (WPF) and Win32 code.
    
    WindowInteropHelper(window: Window)
    """
    def EnsureHandle(self):
        """
        EnsureHandle(self: WindowInteropHelper) -> IntPtr
        
            Creates the HWND of the window if the HWND has not been created yet.
            Returns: An System.IntPtr that represents the HWND.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, window):
        """ __new__(cls: type, window: Window) """
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the window handle for a Windows Presentation Foundation (WPF) window�that is used to create this System.Windows.Interop.WindowInteropHelper.

Get: Handle(self: WindowInteropHelper) -> IntPtr

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the handle of the Windows Presentation Foundation (WPF)�owner window.

Get: Owner(self: WindowInteropHelper) -> IntPtr

Set: Owner(self: WindowInteropHelper) = value
"""



