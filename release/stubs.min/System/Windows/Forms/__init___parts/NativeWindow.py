class NativeWindow(MarshalByRefObject,IWin32Window):
 """
 Provides a low-level encapsulation of a window handle and a window procedure.

 

 NativeWindow()
 """
 def AssignHandle(self,handle):
  """
  AssignHandle(self: NativeWindow,handle: IntPtr)

   Assigns a handle to this window.

  

   handle: The handle to assign to this window.
  """
  pass
 def CreateHandle(self,cp):
  """
  CreateHandle(self: NativeWindow,cp: CreateParams)

   Creates a window and its handle with the specified creation parameters.

  

   cp: A System.Windows.Forms.CreateParams that specifies the creation parameters for this window.
  """
  pass
 def DefWndProc(self,m):
  """
  DefWndProc(self: NativeWindow,m: Message) -> Message

  

   Invokes the default window procedure associated with this window.

  

   m: The message that is currently being processed.
  """
  pass
 def DestroyHandle(self):
  """
  DestroyHandle(self: NativeWindow)

   Destroys the window and its handle.
  """
  pass
 @staticmethod
 def FromHandle(handle):
  """
  FromHandle(handle: IntPtr) -> NativeWindow

  

   Retrieves the window associated with the specified handle.

  

   handle: A handle to a window.

   Returns: The System.Windows.Forms.NativeWindow associated with the specified handle. This method returns 

    null when the handle does not have an associated window.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def OnHandleChange(self,*args):
  """
  OnHandleChange(self: NativeWindow)

   Specifies a notification method that is called when the handle for a window is changed.
  """
  pass
 def OnThreadException(self,*args):
  """
  OnThreadException(self: NativeWindow,e: Exception)

   When overridden in a derived class,manages an unhandled thread exception.

  

   e: An System.Exception that specifies the unhandled thread exception.
  """
  pass
 def ReleaseHandle(self):
  """
  ReleaseHandle(self: NativeWindow)

   Releases the handle associated with this window.
  """
  pass
 def WndProc(self,*args):
  """
  WndProc(self: NativeWindow,m: Message) -> Message

  

   Invokes the default window procedure associated with this window.

  

   m: A System.Windows.Forms.Message that is associated with the current Windows message.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Handle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the handle for this window.



Get: Handle(self: NativeWindow) -> IntPtr



"""


