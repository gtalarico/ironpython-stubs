class EventLogTraceListener(TraceListener,IDisposable):
 """
 Provides a simple listener that directs tracing or debugging output to an System.Diagnostics.EventLog.

 

 EventLogTraceListener()

 EventLogTraceListener(eventLog: EventLog)

 EventLogTraceListener(source: str)
 """
 def Close(self):
  """
  Close(self: EventLogTraceListener)

   Closes the event log so that it no longer receives tracing or debugging output.
  """
  pass
 def Dispose(self):
  """ Dispose(self: EventLogTraceListener,disposing: bool) """
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
 def TraceData(self,eventCache,source,severity,id,data):
  """
  TraceData(self: EventLogTraceListener,eventCache: TraceEventCache,source: str,severity: TraceEventType,id: int,*data: Array[object])

   Writes trace information,an array of data objects,and event information to the event log.

  

   eventCache: An object that contains the current process ID,thread ID,and stack trace information.

   source: A name used to identify the output; typically the name of the application that generated the 

    trace event.

  

   severity: One of the enumeration values that specifies the type of event that has caused the trace.

   id: A numeric identifier for the event. The combination of source and id uniquely identifies an 

    event.

  

   data: An array of data objects.

  TraceData(self: EventLogTraceListener,eventCache: TraceEventCache,source: str,severity: TraceEventType,id: int,data: object)

   Writes trace information,a data object,and event information to the event log.

  

   eventCache: An object that contains the current process ID,thread ID,and stack trace information.

   source: A name used to identify the output; typically the name of the application that generated the 

    trace event.

  

   severity: One of the enumeration values that specifies the type of event that has caused the trace.

   id: A numeric identifier for the event. The combination of source and id uniquely identifies an 

    event.

  

   data: A data object to write to the output file or stream.
  """
  pass
 def TraceEvent(self,eventCache,source,*__args):
  """
  TraceEvent(self: EventLogTraceListener,eventCache: TraceEventCache,source: str,severity: TraceEventType,id: int,message: str)

   Writes trace information,a message,and event information to the event log.

  

   eventCache: An object that contains the current process ID,thread ID,and stack trace information.

   source: A name used to identify the output; typically the name of the application that generated the 

    trace event.

  

   severity: One of the enumeration values that specifies the type of event that has caused the trace.

   id: A numeric identifier for the event. The combination of source and id uniquely identifies an 

    event.

  

   message: The trace message.

  TraceEvent(self: EventLogTraceListener,eventCache: TraceEventCache,source: str,severity: TraceEventType,id: int,format: str,*args: Array[object])

   Writes trace information,a formatted array of objects,and event information to the event log.

  

   eventCache: An object that contains the current process ID,thread ID,and stack trace information.

   source: A name used to identify the output; typically the name of the application that generated the 

    trace event.

  

   severity: One of the enumeration values that specifies the type of event that has caused the trace.

   id: A numeric identifier for the event. The combination of source and id uniquely identifies an 

    event.

  

   format: A format string that contains zero or more format items that correspond to objects in the args 

    array.

  

   args: An object array containing zero or more objects to format.
  """
  pass
 def Write(self,*__args):
  """
  Write(self: EventLogTraceListener,message: str)

   Writes a message to the event log for this instance.

  

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
  WriteLine(self: EventLogTraceListener,message: str)

   Writes a message to the event log for this instance.

  

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
  __new__(cls: type)

  __new__(cls: type,eventLog: EventLog)

  __new__(cls: type,source: str)
  """
  pass
 EventLog=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the event log to write to.



Get: EventLog(self: EventLogTraceListener) -> EventLog



Set: EventLog(self: EventLogTraceListener)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of this System.Diagnostics.EventLogTraceListener.



Get: Name(self: EventLogTraceListener) -> str



Set: Name(self: EventLogTraceListener)=value

"""

 NeedIndent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to indent the output.



"""


