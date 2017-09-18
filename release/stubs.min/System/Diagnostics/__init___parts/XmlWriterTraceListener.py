class XmlWriterTraceListener(TextWriterTraceListener,IDisposable):
 """
 Directs tracing or debugging output as XML-encoded data to a System.IO.TextWriter or to a System.IO.Stream,such as a System.IO.FileStream.

 

 XmlWriterTraceListener(stream: Stream)

 XmlWriterTraceListener(stream: Stream,name: str)

 XmlWriterTraceListener(writer: TextWriter)

 XmlWriterTraceListener(writer: TextWriter,name: str)

 XmlWriterTraceListener(filename: str)

 XmlWriterTraceListener(filename: str,name: str)
 """
 def Close(self):
  """
  Close(self: XmlWriterTraceListener)

   Closes the System.Diagnostics.TextWriterTraceListener.Writer for this listener so that it no 

    longer receives tracing or debugging output.
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
 def Fail(self,message,detailMessage=None):
  """
  Fail(self: XmlWriterTraceListener,message: str,detailMessage: str)

   Writes trace information including an error message and a detailed error message to the file or 

    stream.

  

  

   message: The error message to write.

   detailMessage: The detailed error message to append to the error message.
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
 def TraceData(self,eventCache,source,eventType,id,data):
  """
  TraceData(self: XmlWriterTraceListener,eventCache: TraceEventCache,source: str,eventType: TraceEventType,id: int,*data: Array[object])

   Writes trace information,data objects,and event information to the file or stream.

  

   eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID,thread ID,and stack 

    trace information.

  

   source: The source name.

   eventType: One of the System.Diagnostics.TraceEventType values.

   id: A numeric identifier for the event.

   data: An array of data objects to emit.

  TraceData(self: XmlWriterTraceListener,eventCache: TraceEventCache,source: str,eventType: TraceEventType,id: int,data: object)

   Writes trace information,a data object,and event information to the file or stream.

  

   eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID,thread ID,and stack 

    trace information.

  

   source: The source name.

   eventType: One of the System.Diagnostics.TraceEventType values.

   id: A numeric identifier for the event.

   data: A data object to emit.
  """
  pass
 def TraceEvent(self,eventCache,source,eventType,id,*__args):
  """
  TraceEvent(self: XmlWriterTraceListener,eventCache: TraceEventCache,source: str,eventType: TraceEventType,id: int,message: str)

   Writes trace information,a message,and event information to the file or stream.

  

   eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID,thread ID,and stack 

    trace information.

  

   source: The source name.

   eventType: One of the System.Diagnostics.TraceEventType values.

   id: A numeric identifier for the event.

   message: The message to write.

  TraceEvent(self: XmlWriterTraceListener,eventCache: TraceEventCache,source: str,eventType: TraceEventType,id: int,format: str,*args: Array[object])

   Writes trace information,a formatted message,and event information to the file or stream.

  

   eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID,thread ID,and stack 

    trace information.

  

   source: The source name.

   eventType: One of the System.Diagnostics.TraceEventType values.

   id: A numeric identifier for the event.

   format: A format string that contains zero or more format items that correspond to objects in the args 

    array.

  

   args: An object array containing zero or more objects to format.
  """
  pass
 def TraceTransfer(self,eventCache,source,id,message,relatedActivityId):
  """
  TraceTransfer(self: XmlWriterTraceListener,eventCache: TraceEventCache,source: str,id: int,message: str,relatedActivityId: Guid)

   Writes trace information including the identity of a related activity,a message,and event 

    information to the file or stream.

  

  

   eventCache: A System.Diagnostics.TraceEventCache that contains the current process ID,thread ID,and stack 

    trace information.

  

   source: The source name.

   id: A numeric identifier for the event.

   message: A trace message to write.

   relatedActivityId: A System.Guid structure that identifies a related activity.
  """
  pass
 def Write(self,*__args):
  """
  Write(self: XmlWriterTraceListener,message: str)

   Writes a verbatim message without any additional context information to the file or stream.

  

   message: The message to write.
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
  WriteLine(self: XmlWriterTraceListener,message: str)

   Writes a verbatim message without any additional context information followed by the current 

    line terminator to the file or stream.

  

  

   message: The message to write.
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
  __new__(cls: type,stream: Stream)

  __new__(cls: type,stream: Stream,name: str)

  __new__(cls: type,writer: TextWriter)

  __new__(cls: type,writer: TextWriter,name: str)

  __new__(cls: type,filename: str)

  __new__(cls: type,filename: str,name: str)
  """
  pass
 NeedIndent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to indent the output.



"""



# variables with complex values

