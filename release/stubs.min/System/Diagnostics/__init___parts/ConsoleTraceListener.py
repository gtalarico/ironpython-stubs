class ConsoleTraceListener(TextWriterTraceListener,IDisposable):
 """
 Directs tracing or debugging output to either the standard output or the standard error stream.

 

 ConsoleTraceListener()

 ConsoleTraceListener(useErrorStream: bool)
 """
 def Close(self):
  """
  Close(self: ConsoleTraceListener)

   Closes the output to the stream specified for this trace listener.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: TextWriterTraceListener,disposing: bool)

   Disposes this System.Diagnostics.TextWriterTraceListener object.

  

   disposing: true to release managed resources; if false,

    System.Diagnostics.TextWriterTraceListener.Dispose(System.Boolean) has no effect.
  """
  pass
 def GetSupportedAttributes(self,*args):
  """
  GetSupportedAttributes(self: TraceListener) -> Array[str]

  

   Gets the custom attributes supported by the trace listener.

   Returns: A string array naming the custom attributes supported by the trace listener,or null if there 

    are no custom attributes.
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
 def WriteIndent(self,*args):
  """
  WriteIndent(self: TraceListener)

   Writes the indent to the listener you create when you implement this class,and resets the 

    System.Diagnostics.TraceListener.NeedIndent property to false.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,useErrorStream=None):
  """
  __new__(cls: type)

  __new__(cls: type,useErrorStream: bool)
  """
  pass
 NeedIndent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to indent the output.



"""


