class DefaultTraceListener(TraceListener,IDisposable):
 """
 Provides the default output methods and behavior for tracing.

 

 DefaultTraceListener()
 """
 def Dispose(self):
  """
  Dispose(self: TraceListener,disposing: bool)

   Releases the unmanaged resources used by the System.Diagnostics.TraceListener and optionally 

    releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def Fail(self,message,detailMessage=None):
  """
  Fail(self: DefaultTraceListener,message: str,detailMessage: str)

   Emits or displays detailed messages and a stack trace for an assertion that always fails.

  

   message: The message to emit or display.

   detailMessage: The detailed message to emit or display.

  Fail(self: DefaultTraceListener,message: str)

   Emits or displays a message and a stack trace for an assertion that always fails.

  

   message: The message to emit or display.
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
 def Write(self,*__args):
  """
  Write(self: DefaultTraceListener,message: str)

   Writes the output to the OutputDebugString function and to the 

    System.Diagnostics.Debugger.Log(System.Int32,System.String,System.String) method.

  

  

   message: The message to write to OutputDebugString and 

    System.Diagnostics.Debugger.Log(System.Int32,System.String,System.String).
  """
  pass
 def WriteIndent(self,*args):
  """
  WriteIndent(self: TraceListener)

   Writes the indent to the listener you create when you implement this class,and resets the 

    System.Diagnostics.TraceListener.NeedIndent property to false.
  """
  pass
 def WriteLine(self,*__args):
  """
  WriteLine(self: DefaultTraceListener,message: str)

   Writes the output to the OutputDebugString function and to the 

    System.Diagnostics.Debugger.Log(System.Int32,System.String,System.String) method,followed by a 

    carriage return and line feed (\r\n).

  

  

   message: The message to write to OutputDebugString and 

    System.Diagnostics.Debugger.Log(System.Int32,System.String,System.String).
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
 AssertUiEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the application is running in user-interface mode.



Get: AssertUiEnabled(self: DefaultTraceListener) -> bool



Set: AssertUiEnabled(self: DefaultTraceListener)=value

"""

 LogFileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of a log file to write trace or debug messages to.



Get: LogFileName(self: DefaultTraceListener) -> str



Set: LogFileName(self: DefaultTraceListener)=value

"""

 NeedIndent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to indent the output.



"""


