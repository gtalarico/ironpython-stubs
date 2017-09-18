# encoding: utf-8
# module System.Windows.Interop calls itself Interop
# from PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class CursorInteropHelper(object):
    """ Provides a static helper class for WPF/Win32 interoperation with one method, which is used to obtain a Windows Presentation Foundation (WPF)�System.Windows.Input.Cursor object based on a provided Win32 cursor handle. """
    @staticmethod
    def Create(cursorHandle):
        """
        Create(cursorHandle: SafeHandle) -> Cursor
        
            Returns a Windows Presentation Foundation (WPF)�System.Windows.Input.Cursor object based on a 
             provided Win32 cursor handle.
        
        
            cursorHandle: Cursor reference to use for interoperation.
            Returns: The Windows Presentation Foundation (WPF)�cursor object based on the provided Win32 cursor 
             handle.
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
        
            Creates a modifiable clone of this System.Windows.Interop.D3DImage object, making deep copies of 
             this object's values. When copying dependency properties, this method copies resource references 
             and data bindings (which may no longer resolve), but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
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
        
            Creates a modifiable clone of this System.Windows.Interop.D3DImage object, making deep copies of 
             this object's current values. Resource references, data bindings, and animations are not copied, 
             but their current values are copied.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
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
            Returns: A System.Windows.Media.Imaging.BitmapSource that is a software copy of the current state of the 
             back buffer; otherwise, null if the back buffer cannot be read.
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
        
            Makes the System.Windows.Interop.D3DImage unmodifiable or determines whether it can be made 
             unmodifiable.
        
        
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
            Locks the System.Windows.Interop.D3DImage and enables operations on the back buffer.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
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
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def SetBackBuffer(self, backBufferType, backBuffer, enableSoftwareFallback=None):
        """
        SetBackBuffer(self: D3DImage, backBufferType: D3DResourceType, backBuffer: IntPtr, enableSoftwareFallback: bool)SetBackBuffer(self: D3DImage, backBufferType: D3DResourceType, backBuffer: IntPtr)
            Assigns a Direct3D surface as the source of the back buffer.
        
            backBufferType: The type of Direct3D surface. Must be a valid System.Windows.Interop.D3DResourceType.
            backBuffer: The Direct3D surface to assign as the back buffer.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def TryLock(self, timeout):
        """
        TryLock(self: D3DImage, timeout: Duration) -> bool
        
            Attempts to lock the System.Windows.Interop.D3DImage and waits for the specified duration.
        
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
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
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


class IWin32Window:
    """ Defines the contract for Win32 window handles. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the window handle.

Get: Handle(self: IWin32Window) -> IntPtr

"""



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
        
            hook: The handler implementation (based on the System.Windows.Interop.HwndSourceHook delegate) that 
             receives the window messages.
        """
        pass

    def AddSource(self, *args): #cannot find CLR method
        """
        AddSource(self: PresentationSource)
            Adds a System.Windows.PresentationSource derived class instance to the list of known 
             presentation sources.
        """
        pass

    def ClearContentRenderedListeners(self, *args): #cannot find CLR method
        """
        ClearContentRenderedListeners(self: PresentationSource)
            Sets the list of listeners for the System.Windows.PresentationSource.ContentRendered event to 
             null.
        """
        pass

    def CreateHandleRef(self):
        """
        CreateHandleRef(self: HwndSource) -> HandleRef
        
            Gets the window handle for the System.Windows.Interop.HwndSource. The window handle is packaged 
             as part of a System.Runtime.InteropServices.HandleRef structure.
        
            Returns: A structure that contains the window handle for this System.Windows.Interop.HwndSource.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: HwndSource)
            Releases all managed resources that are used by the System.Windows.Interop.HwndSource, and 
             raises the System.Windows.Interop.HwndSource.Disposed event.
        """
        pass

    @staticmethod
    def FromHwnd(hwnd):
        """
        FromHwnd(hwnd: IntPtr) -> HwndSource
        
            Returns the System.Windows.Interop.HwndSource object of the specified window.
        
            hwnd: The provided window handle.
            Returns: The System.Windows.Interop.HwndSource object for the window that is specified by the hwnd window 
             handle.
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
        
            Gets a value that indicates whether the sink or one of its contained components has focus.
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
        
            Registers the System.Windows.Interop.IKeyboardInputSink interface of a contained component.
        
            sink: The System.Windows.Interop.IKeyboardInputSink sink of the contained component.
            Returns: The System.Windows.Interop.IKeyboardInputSite site of the contained component.
        """
        pass

    def RemoveHook(self, hook):
        """
        RemoveHook(self: HwndSource, hook: HwndSourceHook)
            Removes the event handlers that were added by 
             System.Windows.Interop.HwndSource.AddHook(System.Windows.Interop.HwndSourceHook).
        
        
            hook: The event handler to remove.
        """
        pass

    def RemoveSource(self, *args): #cannot find CLR method
        """
        RemoveSource(self: PresentationSource)
            Removes a System.Windows.PresentationSource derived class instance from the list of known 
             presentation sources.
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
        
            msg: The message and associated data. Do not modify this structure. It is passed by reference for 
             performance reasons only.
        
            modifiers: Modifier keys.
            Returns: true if the message was handled by the method implementation; otherwise, false.
        """
        pass

    def TranslateCharCore(self, *args): #cannot find CLR method
        """
        TranslateCharCore(self: HwndSource, msg: MSG, modifiers: ModifierKeys) -> (bool, MSG)
        
            Processes WM_CHAR, WM_SYSCHAR, WM_DEADCHAR, and WM_SYSDEADCHAR input messages before the 
             System.Windows.Interop.IKeyboardInputSink.OnMnemonic(System.Windows.Interop.MSG@,System.Windows.I
             nput.ModifierKeys) method is called.
        
        
            msg: The message and associated data. Do not modify this structure. It is passed by reference for 
             performance reasons only.
        
            modifiers: Modifier keys.
            Returns: true if the message was processed and 
             System.Windows.Interop.IKeyboardInputSink.OnMnemonic(System.Windows.Interop.MSG@,System.Windows.I
             nput.ModifierKeys) should not be called; otherwise, false.
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
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
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
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
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
        
            Returns the hash code for this System.Windows.Interop.HwndSourceParameters instance.
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
            Sets the values that are used for the window size of the System.Windows.Interop.HwndSource.
        
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
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, width: int, height: int)
        __new__[HwndSourceParameters]() -> HwndSourceParameters
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



class Imaging(object):
    """ Provides managed to unmanaged interoperation support for creating image objects. """
    @staticmethod
    def CreateBitmapSourceFromHBitmap(bitmap, palette, sourceRect, sizeOptions):
        """
        CreateBitmapSourceFromHBitmap(bitmap: IntPtr, palette: IntPtr, sourceRect: Int32Rect, sizeOptions: BitmapSizeOptions) -> BitmapSource
        
            Returns a managed System.Windows.Media.Imaging.BitmapSource, based on the provided pointer to an 
             unmanaged bitmap and palette information.
        
        
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
        
            Returns a managed System.Windows.Media.Imaging.BitmapSource, based on the provided pointer to an 
             unmanaged icon image.
        
        
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
        
            Returns a managed System.Windows.Media.Imaging.BitmapSource, based on the provided unmanaged 
             memory location.
        
        
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
            Checks whether the bitmap source content is from a known site of origin. This method is used to 
             make sure that pixel copying operations are safe.
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
        
            Makes an instance of System.Windows.Media.Imaging.BitmapSource or a derived class immutable.
        
            isChecking: true if this instance should actually freeze itself when this method is called; otherwise, false.
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
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
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
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
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
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


