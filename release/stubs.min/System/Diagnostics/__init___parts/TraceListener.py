class TraceListener(MarshalByRefObject,IDisposable):
 """ Provides the abstract base class for the listeners who monitor trace and debug output. """
 def Close(self):
  """
  Close(self: TraceListener)

   When overridden in a derived class,closes the output stream so it no longer receives tracing or 

    debugging output.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: TraceListener)

   Releases all resources used by the System.Diagnostics.TraceListener.
  """
  pass
 def Fail(self,message,detailMessage=None):
  """
  Fail(self: TraceListener,message: str,detailMessage: str)

   Emits an error message and a detailed error message to the listener you create when you 

    implement the System.Diagnostics.TraceListener class.

  

  

   message: A message to emit.

   detailMessage: A detailed message to emit.

  Fail(self: TraceListener,message: str)

   Emits an error message to the listener you create when you implement the 

    System.Diagnostics.TraceListener class.

  

  

   message: A message to emit.
  """
  pass
 def Flush(self):
  """
  Flush(self: TraceListener)

   When overridden in a derived class,flushes the output buffer.
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
  TraceData(self: TraceListener,eventCache: TraceEventCache,source: str,eventType: TraceEventType,id: int,*data: Array[object])

   Writes trace information,an array of data objects and event information to the listener 

    specific output.

  

  

   eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID,thread ID,and 

    stack trace information.

  

   source: A name used to identify the output,typically the name of the application that generated the 

    trace event.

  

   eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 

    the trace.

  

   id: A numeric identifier for the event.

   data: An array of objects to emit as data.

  TraceData(self: TraceListener,eventCache: TraceEventCache,source: str,eventType: TraceEventType,id: int,data: object)

   Writes trace information,a data object and event information to the listener specific output.

  

   eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID,thread ID,and 

    stack trace information.

  

   source: A name used to identify the output,typically the name of the application that generated the 

    trace event.

  

   eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 

    the trace.

  

   id: A numeric identifier for the event.

   data: The trace data to emit.
  """
  pass
 def TraceEvent(self,eventCache,source,eventType,id,*__args):
  """
  TraceEvent(self: TraceListener,eventCache: TraceEventCache,source: str,eventType: TraceEventType,id: int,format: str,*args: Array[object])

   Writes trace information,a formatted array of objects and event information to the listener 

    specific output.

  

  

   eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID,thread ID,and 

    stack trace information.

  

   source: A name used to identify the output,typically the name of the application that generated the 

    trace event.

  

   eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 

    the trace.

  

   id: A numeric identifier for the event.

   format: A format string that contains zero or more format items,which correspond to objects in the args 

    array.

  

   args: An object array containing zero or more objects to format.

  TraceEvent(self: TraceListener,eventCache: TraceEventCache,source: str,eventType: TraceEventType,id: int,message: str)

   Writes trace information,a message,and event information to the listener specific output.

  

   eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID,thread ID,and 

    stack trace information.

  

   source: A name used to identify the output,typically the name of the application that generated the 

    trace event.

  

   eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 

    the trace.

  

   id: A numeric identifier for the event.

   message: A message to write.

  TraceEvent(self: TraceListener,eventCache: TraceEventCache,source: str,eventType: TraceEventType,id: int)

   Writes trace and event information to the listener specific output.

  

   eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID,thread ID,and 

    stack trace information.

  

   source: A name used to identify the output,typically the name of the application that generated the 

    trace event.

  

   eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 

    the trace.

  

   id: A numeric identifier for the event.
  """
  pass
 def TraceTransfer(self,eventCache,source,id,message,relatedActivityId):
  """
  TraceTransfer(self: TraceListener,eventCache: TraceEventCache,source: str,id: int,message: str,relatedActivityId: Guid)

   Writes trace information,a message,a related activity identity and event information to the 

    listener specific output.

  

  

   eventCache: A System.Diagnostics.TraceEventCache object that contains the current process ID,thread ID,and 

    stack trace information.

  

   source: A name used to identify the output,typically the name of the application that generated the 

    trace event.

  

   id: A numeric identifier for the event.

   message: A message to write.

   relatedActivityId: A System.Guid  object identifying a related activity.
  """
  pass
 def Write(self,*__args):
  """
  Write(self: TraceListener,message: str,category: str)

   Writes a category name and a message to the listener you create when you implement the 

    System.Diagnostics.TraceListener class.

  

  

   message: A message to write.

   category: A category name used to organize the output.

  Write(self: TraceListener,o: object,category: str)

   Writes a category name and the value of the object's System.Object.ToString method to the 

    listener you create when you implement the System.Diagnostics.TraceListener class.

  

  

   o: An System.Object whose fully qualified class name you want to write.

   category: A category name used to organize the output.

  Write(self: TraceListener,message: str)

   When overridden in a derived class,writes the specified message to the listener you create in 

    the derived class.

  

  

   message: A message to write.

  Write(self: TraceListener,o: object)

   Writes the value of the object's System.Object.ToString method to the listener you create when 

    you implement the System.Diagnostics.TraceListener class.

  

  

   o: An System.Object whose fully qualified class name you want to write.
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
  WriteLine(self: TraceListener,message: str,category: str)

   Writes a category name and a message to the listener you create when you implement the 

    System.Diagnostics.TraceListener class,followed by a line terminator.

  

  

   message: A message to write.

   category: A category name used to organize the output.

  WriteLine(self: TraceListener,o: object,category: str)

   Writes a category name and the value of the object's System.Object.ToString method to the 

    listener you create when you implement the System.Diagnostics.TraceListener class,followed by a 

    line terminator.

  

  

   o: An System.Object whose fully qualified class name you want to write.

   category: A category name used to organize the output.

  WriteLine(self: TraceListener,message: str)

   When overridden in a derived class,writes a message to the listener you create in the derived 

    class,followed by a line terminator.

  

  

   message: A message to write.

  WriteLine(self: TraceListener,o: object)

   Writes the value of the object's System.Object.ToString method to the listener you create when 

    you implement the System.Diagnostics.TraceListener class,followed by a line terminator.

  

  

   o: An System.Object whose fully qualified class name you want to write.
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
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type)

  __new__(cls: type,name: str)
  """
  pass
 Attributes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the custom trace listener attributes defined in the application configuration file.



Get: Attributes(self: TraceListener) -> StringDictionary



"""

 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the trace filter for the trace listener.



Get: Filter(self: TraceListener) -> TraceFilter



Set: Filter(self: TraceListener)=value

"""

 IndentLevel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the indent level.



Get: IndentLevel(self: TraceListener) -> int



Set: IndentLevel(self: TraceListener)=value

"""

 IndentSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of spaces in an indent.



Get: IndentSize(self: TraceListener) -> int



Set: IndentSize(self: TraceListener)=value

"""

 IsThreadSafe=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the trace listener is thread safe.



Get: IsThreadSafe(self: TraceListener) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a name for this System.Diagnostics.TraceListener.



Get: Name(self: TraceListener) -> str



Set: Name(self: TraceListener)=value

"""

 NeedIndent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to indent the output.



"""

 TraceOutputOptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the trace output options.



Get: TraceOutputOptions(self: TraceListener) -> TraceOptions



Set: TraceOutputOptions(self: TraceListener)=value

"""


