class IKeyboardInputSink:
 """ Provides a keyboard sink for components that manages tabbing,accelerators,and mnemonics across interop boundaries and between HWNDs. This interface implements keyboard message management in WPF-Win32 interoperation scenarios. """
 def HasFocusWithin(self):
  """
  HasFocusWithin(self: IKeyboardInputSink) -> bool
  
   Gets a value that indicates whether the sink or one of its contained components 
    has focus.
  
   Returns: true if the sink or one of its contained components has focus; otherwise,false.
  """
  pass
 def OnMnemonic(self,msg,modifiers):
  """
  OnMnemonic(self: IKeyboardInputSink,msg: MSG,modifiers: ModifierKeys) -> (bool,MSG)
  
   Called when one of the mnemonics (access keys) for this sink is invoked.
  
   msg: The message for the mnemonic and associated data. Do not modify this message 
    structure. It is passed by reference for performance reasons only.
  
   modifiers: Modifier keys.
   Returns: true if the message was handled; otherwise,false.
  """
  pass
 def RegisterKeyboardInputSink(self,sink):
  """
  RegisterKeyboardInputSink(self: IKeyboardInputSink,sink: IKeyboardInputSink) -> IKeyboardInputSite
  
   Registers the System.Windows.Interop.IKeyboardInputSink interface of a 
    contained component.
  
  
   sink: The System.Windows.Interop.IKeyboardInputSink sink of the contained component.
   Returns: The System.Windows.Interop.IKeyboardInputSite site of the contained component.
  """
  pass
 def TabInto(self,request):
  """
  TabInto(self: IKeyboardInputSink,request: TraversalRequest) -> bool
  
   Sets focus on either the first tab stop or the last tab stop of the sink.
  
   request: Specifies whether focus should be set to the first or the last tab stop.
   Returns: true if the focus has been set as requested; false,if there are no tab stops.
  """
  pass
 def TranslateAccelerator(self,msg,modifiers):
  """
  TranslateAccelerator(self: IKeyboardInputSink,msg: MSG,modifiers: ModifierKeys) -> (bool,MSG)
  
   Processes keyboard input at the keydown message level.
  
   msg: The message and associated data. Do not modify this structure. It is passed by 
    reference for performance reasons only.
  
   modifiers: Modifier keys.
   Returns: true if the message was handled by the method implementation; otherwise,false.
  """
  pass
 def TranslateChar(self,msg,modifiers):
  """
  TranslateChar(self: IKeyboardInputSink,msg: MSG,modifiers: ModifierKeys) -> (bool,MSG)
  
   Processes WM_CHAR,WM_SYSCHAR,WM_DEADCHAR,and WM_SYSDEADCHAR input messages 
    before 
    System.Windows.Interop.IKeyboardInputSink.OnMnemonic(System.Windows.Interop.MSG@
    ,System.Windows.Input.ModifierKeys) is called.
  
  
   msg: The message and associated data. Do not modify this structure. It is passed by 
    reference for performance reasons only.
  
   modifiers: Modifier keys.
   Returns: true if the message was processed and 
    System.Windows.Interop.IKeyboardInputSink.OnMnemonic(System.Windows.Interop.MSG@
    ,System.Windows.Input.ModifierKeys) should not be called; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 KeyboardInputSite=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a reference to the component's container's System.Windows.Interop.IKeyboardInputSite interface.

Get: KeyboardInputSite(self: IKeyboardInputSink) -> IKeyboardInputSite

Set: KeyboardInputSite(self: IKeyboardInputSink)=value
"""


