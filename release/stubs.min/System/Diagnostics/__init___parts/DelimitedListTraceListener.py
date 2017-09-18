class DelimitedListTraceListener(TextWriterTraceListener,IDisposable):
 """
 Directs tracing or debugging output to a text writer,such as a stream writer,or to a stream,such as a file stream.

 

 DelimitedListTraceListener(stream: Stream)

 DelimitedListTraceListener(stream: Stream,name: str)

 DelimitedListTraceListener(writer: TextWriter)

 DelimitedListTraceListener(writer: TextWriter,name: str)

 DelimitedListTraceListener(fileName: str)

 DelimitedListTraceListener(fileName: str,name: str)
 """
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
  GetSupportedAttributes(self: DelimitedListTraceListener) -> Array[str]

  

   Returns the custom configuration file attribute supported by the delimited trace listener.

   Returns: A string array that contains the single value "delimiter".
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
  TraceData(self: DelimitedListTraceListener,eventCache: TraceEventCache,source: str,eventType: TraceEventType,id: int,*data: Array[object])

   Writes trace information,an array of data objects,and event information to the output file or 

    stream.

  

  

   eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID,thread ID,and 

    stack trace information.

  

   source: A name used to identify the output,typically the name of the application that generated the 

    trace event.

  

   eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 

    the trace.

  

   id: A numeric identifier for the event.

   data: An array of data objects to write to the output file or stream.

  TraceData(self: DelimitedListTraceListener,eventCache: TraceEventCache,source: str,eventType: TraceEventType,id: int,data: object)

   Writes trace information,a data object,and event information to the output file or stream.

  

   eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID,thread ID,and 

    stack trace information.

  

   source: A name used to identify the output,typically the name of the application that generated the 

    trace event.

  

   eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 

    the trace.

  

   id: A numeric identifier for the event.

   data: A data object to write to the output file or stream.
  """
  pass
 def TraceEvent(self,eventCache,source,eventType,id,*__args):
  """
  TraceEvent(self: DelimitedListTraceListener,eventCache: TraceEventCache,source: str,eventType: TraceEventType,id: int,message: str)

   Writes trace information,a message,and event information to the output file or stream.

  

   eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID,thread ID,and 

    stack trace information.

  

   source: A name used to identify the output,typically the name of the application that generated the 

    trace event.

  

   eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 

    the trace.

  

   id: A numeric identifier for the event.

   message: The trace message to write to the output file or stream.

  TraceEvent(self: DelimitedListTraceListener,eventCache: TraceEventCache,source: str,eventType: TraceEventType,id: int,format: str,*args: Array[object])

   Writes trace information,a formatted array of objects,and event information to the output file 

    or stream.

  

  

   eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID,thread ID,and 

    stack trace information.

  

   source: A name used to identify the output,typically the name of the application that generated the 

    trace event.

  

   eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 

    the trace.

  

   id: A numeric identifier for the event.

   format: A format string that contains zero or more format items that correspond to objects in the args 

    array.

  

   args: An array containing zero or more objects to format.
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
 def __new__(self,*__args):
  """
  __new__(cls: type,stream: Stream)

  __new__(cls: type,stream: Stream,name: str)

  __new__(cls: type,writer: TextWriter)

  __new__(cls: type,writer: TextWriter,name: str)

  __new__(cls: type,fileName: str)

  __new__(cls: type,fileName: str,name: str)
  """
  pass
 Delimiter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the delimiter for the delimited list.



Get: Delimiter(self: DelimitedListTraceListener) -> str



Set: Delimiter(self: DelimitedListTraceListener)=value

"""

 NeedIndent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to indent the output.



"""


