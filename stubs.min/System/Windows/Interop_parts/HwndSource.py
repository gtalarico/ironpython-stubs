class HwndSource(PresentationSource,IDisposable,IWin32Window,IKeyboardInputSink):
 """
 Presents Windows Presentation Foundation (WPF) content in a Win32 window.
 
 HwndSource(classStyle: int,style: int,exStyle: int,x: int,y: int,name: str,parent: IntPtr)
 HwndSource(classStyle: int,style: int,exStyle: int,x: int,y: int,width: int,height: int,name: str,parent: IntPtr,adjustSizingForNonClientArea: bool)
 HwndSource(classStyle: int,style: int,exStyle: int,x: int,y: int,width: int,height: int,name: str,parent: IntPtr)
 HwndSource(parameters: HwndSourceParameters)
 """
 def AddHook(self,hook):
  """
  AddHook(self: HwndSource,hook: HwndSourceHook)
   Adds an event handler that receives all window messages.
  
   hook: The handler implementation (based on the System.Windows.Interop.HwndSourceHook 
    delegate) that receives the window messages.
  """
  pass
 def AddSource(self,*args):
  """
  AddSource(self: PresentationSource)
   Adds a System.Windows.PresentationSource derived class instance to the list of 
    known presentation sources.
  """
  pass
 def ClearContentRenderedListeners(self,*args):
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
    System.Windows.Interop.HwndSource,and raises the 
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
 def GetCompositionTargetCore(self,*args):
  """
  GetCompositionTargetCore(self: HwndSource) -> CompositionTarget
  
   Gets the visual target of the window.
   Returns: Returns the visual target of the window.
  """
  pass
 def HasFocusWithinCore(self,*args):
  """
  HasFocusWithinCore(self: HwndSource) -> bool
  
   Gets a value that indicates whether the sink or one of its contained components 
    has focus.
  
   Returns: true if the sink or one of its contained components has focus; otherwise,false.
  """
  pass
 def OnDpiChanged(self,*args):
  """ OnDpiChanged(self: HwndSource,e: HwndDpiChangedEventArgs) """
  pass
 def OnMnemonicCore(self,*args):
  """
  OnMnemonicCore(self: HwndSource,msg: MSG,modifiers: ModifierKeys) -> (bool,MSG)
  
   Called when one of the mnemonics (access keys) for this sink is invoked.
  
   msg: The message for the mnemonic and associated data.
   modifiers: Modifier keys.
   Returns: true if the message was handled; otherwise,false.
  """
  pass
 def RegisterKeyboardInputSinkCore(self,*args):
  """
  RegisterKeyboardInputSinkCore(self: HwndSource,sink: IKeyboardInputSink) -> IKeyboardInputSite
  
   Registers the System.Windows.Interop.IKeyboardInputSink interface of a 
    contained component.
  
  
   sink: The System.Windows.Interop.IKeyboardInputSink sink of the contained component.
   Returns: The System.Windows.Interop.IKeyboardInputSite site of the contained component.
  """
  pass
 def RemoveHook(self,hook):
  """
  RemoveHook(self: HwndSource,hook: HwndSourceHook)
   Removes the event handlers that were added by 
    System.Windows.Interop.HwndSource.AddHook(System.Windows.Interop.HwndSourceHook)
    .
  
  
   hook: The event handler to remove.
  """
  pass
 def RemoveSource(self,*args):
  """
  RemoveSource(self: PresentationSource)
   Removes a System.Windows.PresentationSource derived class instance from the 
    list of known presentation sources.
  """
  pass
 def RootChanged(self,*args):
  """
  RootChanged(self: PresentationSource,oldRoot: Visual,newRoot: Visual)
   Provides notification that the root System.Windows.Media.Visual has changed.
  
   oldRoot: The old root System.Windows.Media.Visual.
   newRoot: The new root System.Windows.Media.Visual.
  """
  pass
 def TabIntoCore(self,*args):
  """
  TabIntoCore(self: HwndSource,request: TraversalRequest) -> bool
  
   Sets focus on either the first tab stop or the last tab stop of the sink.
  
   request: Specifies whether focus should be set to the first or the last tab stop.
   Returns: true if the focus has been set as requested; false,if there are no tab stops.
  """
  pass
 def TranslateAcceleratorCore(self,*args):
  """
  TranslateAcceleratorCore(self: HwndSource,msg: MSG,modifiers: ModifierKeys) -> (bool,MSG)
  
   Processes keyboard input at the key-down message level.
  
   msg: The message and associated data. Do not modify this structure. It is passed by 
    reference for performance reasons only.
  
   modifiers: Modifier keys.
   Returns: true if the message was handled by the method implementation; otherwise,false.
  """
  pass
 def TranslateCharCore(self,*args):
  """
  TranslateCharCore(self: HwndSource,msg: MSG,modifiers: ModifierKeys) -> (bool,MSG)
  
   Processes WM_CHAR,WM_SYSCHAR,WM_DEADCHAR,and WM_SYSDEADCHAR input messages 
    before the 
    System.Windows.Interop.IKeyboardInputSink.OnMnemonic(System.Windows.Interop.MSG@
    ,System.Windows.Input.ModifierKeys) method is called.
  
  
   msg: The message and associated data. Do not modify this structure. It is passed by 
    reference for performance reasons only.
  
   modifiers: Modifier keys.
   Returns: true if the message was processed and 
    System.Windows.Interop.IKeyboardInputSink.OnMnemonic(System.Windows.Interop.MSG@
    ,System.Windows.Input.ModifierKeys) should not be called; otherwise,false.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,classStyle: int,style: int,exStyle: int,x: int,y: int,name: str,parent: IntPtr)
  __new__(cls: type,classStyle: int,style: int,exStyle: int,x: int,y: int,width: int,height: int,name: str,parent: IntPtr,adjustSizingForNonClientArea: bool)
  __new__(cls: type,classStyle: int,style: int,exStyle: int,x: int,y: int,width: int,height: int,name: str,parent: IntPtr)
  __new__(cls: type,parameters: HwndSourceParameters)
  """
  pass
 AcquireHwndFocusInMenuMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value that determines whether to acquire Win32 focus for the WPF containing window for this System.Windows.Interop.HwndSource.

Get: AcquireHwndFocusInMenuMode(self: HwndSource) -> bool

"""

 ChildKeyboardInputSinks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a sequence of registered input sinks.

Get: ChildKeyboardInputSinks(self: HwndSource) -> IEnumerable[IKeyboardInputSink]

"""

 CompositionTarget=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the visual manager for the hosted window.

Get: CompositionTarget(self: HwndSource) -> HwndTarget

"""

 Handle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the window handle for this System.Windows.Interop.HwndSource.

Get: Handle(self: HwndSource) -> IntPtr

"""

 IsDisposed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether System.Windows.Interop.HwndSource.Dispose has been called on this System.Windows.Interop.HwndSource.

Get: IsDisposed(self: HwndSource) -> bool

"""

 KeyboardInputSiteCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a reference to the component's container's System.Windows.Interop.IKeyboardInputSite interface.

"""

 RestoreFocusMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Input.RestoreFocusMode for the window.

Get: RestoreFocusMode(self: HwndSource) -> RestoreFocusMode

"""

 RootVisual=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.CompositionTarget.RootVisual of the window.

Get: RootVisual(self: HwndSource) -> Visual

Set: RootVisual(self: HwndSource)=value
"""

 SizeToContent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get or sets whether and how the window is sized to its content.

Get: SizeToContent(self: HwndSource) -> SizeToContent

Set: SizeToContent(self: HwndSource)=value
"""

 UsesPerPixelOpacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that declares whether the per-pixel opacity of the source window content is respected.

Get: UsesPerPixelOpacity(self: HwndSource) -> bool

"""


 AutoResized=None
 DefaultAcquireHwndFocusInMenuMode=True
 Disposed=None
 DpiChanged=None
 SizeToContentChanged=None

