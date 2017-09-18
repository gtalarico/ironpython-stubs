class TextWriterTraceListener(TraceListener,IDisposable):
 """
 Directs tracing or debugging output to a System.IO.TextWriter or to a System.IO.Stream,such as System.IO.FileStream.

 

 TextWriterTraceListener()

 TextWriterTraceListener(stream: Stream)

 TextWriterTraceListener(stream: Stream,name: str)

 TextWriterTraceListener(writer: TextWriter)

 TextWriterTraceListener(writer: TextWriter,name: str)

 TextWriterTraceListener(fileName: str)

 TextWriterTraceListener(fileName: str,name: str)
 """
 def Close(self):
  """
  Close(self: TextWriterTraceListener)

   Closes the System.Diagnostics.TextWriterTraceListener.Writer so that it no longer receives 

    tracing or debugging output.
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
 def Flush(self):
  """
  Flush(self: TextWriterTraceListener)

   Flushes the output buffer for the System.Diagnostics.TextWriterTraceListener.Writer.
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
  Write(self: TextWriterTraceListener,message: str)

   Writes a message to this instance's System.Diagnostics.TextWriterTraceListener.Writer.

  

   message: A message to write.
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
  WriteLine(self: TextWriterTraceListener,message: str)

   Writes a message to this instance's System.Diagnostics.TextWriterTraceListener.Writer followed 

    by a line terminator. The default line terminator is a carriage return followed by a line feed 

    (\r\n).

  

  

   message: A message to write.
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
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,stream: Stream)

  __new__(cls: type,stream: Stream,name: str)

  __new__(cls: type,writer: TextWriter)

  __new__(cls: type,writer: TextWriter,name: str)

  __new__(cls: type,fileName: str)

  __new__(cls: type,fileName: str,name: str)
  """
  pass
 NeedIndent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to indent the output.



"""

 Writer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text writer that receives the tracing or debugging output.



Get: Writer(self: TextWriterTraceListener) -> TextWriter



Set: Writer(self: TextWriterTraceListener)=value

"""


