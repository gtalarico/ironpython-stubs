class EventLog(Component,IComponent,IDisposable,ISupportInitialize):
 """
 Provides interaction with Windows event logs.

 

 EventLog()

 EventLog(logName: str)

 EventLog(logName: str,machineName: str)

 EventLog(logName: str,machineName: str,source: str)
 """
 def BeginInit(self):
  """
  BeginInit(self: EventLog)

   Begins the initialization of an System.Diagnostics.EventLog used on a form or used by another 

    component. The initialization occurs at runtime.
  """
  pass
 def Clear(self):
  """
  Clear(self: EventLog)

   Removes all entries from the event log.
  """
  pass
 def Close(self):
  """
  Close(self: EventLog)

   Closes the event log and releases read and write handles.
  """
  pass
 @staticmethod
 def CreateEventSource(*__args):
  """
  CreateEventSource(sourceData: EventSourceCreationData)

   Establishes a valid event source for writing localized event messages,using the specified 

    configuration properties for the event source and the corresponding event log.

  

  

   sourceData: The configuration properties for the event source and its target event log.

  CreateEventSource(source: str,logName: str,machineName: str)

   Establishes the specified source name as a valid event source for writing entries to a log on 

    the specified computer. This method can also be used to create a new custom log on the specified 

    computer.

  

  

   source: The source by which the application is registered on the specified computer.

   logName: The name of the log the source's entries are written to. Possible values include Application,

    System,or a custom event log. If you do not specify a value,logName defaults to Application.

  

   machineName: The name of the computer to register this event source with,or "." for the local computer.

  CreateEventSource(source: str,logName: str)

   Establishes the specified source name as a valid event source for writing entries to a log on 

    the local computer. This method can also create a new custom log on the local computer.

  

  

   source: The source name by which the application is registered on the local computer.

   logName: The name of the log the source's entries are written to. Possible values include Application,

    System,or a custom event log.
  """
  pass
 @staticmethod
 def Delete(logName,machineName=None):
  """
  Delete(logName: str,machineName: str)

   Removes an event log from the specified computer.

  

   logName: The name of the log to delete. Possible values include: Application,Security,System,and any 

    custom event logs on the specified computer.

  

   machineName: The name of the computer to delete the log from,or "." for the local computer.

  Delete(logName: str)

   Removes an event log from the local computer.

  

   logName: The name of the log to delete. Possible values include: Application,Security,System,and any 

    custom event logs on the computer.
  """
  pass
 @staticmethod
 def DeleteEventSource(source,machineName=None):
  """
  DeleteEventSource(source: str,machineName: str)

   Removes the application's event source registration from the specified computer.

  

   source: The name by which the application is registered in the event log system.

   machineName: The name of the computer to remove the registration from,or "." for the local computer.

  DeleteEventSource(source: str)

   Removes the event source registration from the event log of the local computer.

  

   source: The name by which the application is registered in the event log system.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: EventLog,disposing: bool)

   Releases the unmanaged resources used by the System.Diagnostics.EventLog,and optionally 

    releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def EndInit(self):
  """
  EndInit(self: EventLog)

   Ends the initialization of an System.Diagnostics.EventLog used on a form or by another 

    component. The initialization occurs at runtime.
  """
  pass
 @staticmethod
 def Exists(logName,machineName=None):
  """
  Exists(logName: str,machineName: str) -> bool

  

   Determines whether the log exists on the specified computer.

  

   logName: The log for which to search. Possible values include: Application,Security,System,other 

    application-specific logs (such as those associated with Active Directory),or any custom log on 

    the computer.

  

   machineName: The name of the computer on which to search for the log,or "." for the local computer.

   Returns: true if the log exists on the specified computer; otherwise,false.

  Exists(logName: str) -> bool

  

   Determines whether the log exists on the local computer.

  

   logName: The name of the log to search for. Possible values include: Application,Security,System,other 

    application-specific logs (such as those associated with Active Directory),or any custom log on 

    the computer.

  

   Returns: true if the log exists on the local computer; otherwise,false.
  """
  pass
 @staticmethod
 def GetEventLogs(machineName=None):
  """
  GetEventLogs(machineName: str) -> Array[EventLog]

  

   Searches for all event logs on the given computer and creates an array of 

    System.Diagnostics.EventLog objects that contain the list.

  

  

   machineName: The computer on which to search for event logs.

   Returns: An array of type System.Diagnostics.EventLog that represents the logs on the given computer.

  GetEventLogs() -> Array[EventLog]

  

   Searches for all event logs on the local computer and creates an array of 

    System.Diagnostics.EventLog objects that contain the list.

  

   Returns: An array of type System.Diagnostics.EventLog that represents the logs on the local computer.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Component,service: Type) -> object

  

   Returns an object that represents a service provided by the System.ComponentModel.Component or 

    by its System.ComponentModel.Container.

  

  

   service: A service provided by the System.ComponentModel.Component.

   Returns: An System.Object that represents a service provided by the System.ComponentModel.Component,or 

    null if the System.ComponentModel.Component does not provide the specified service.
  """
  pass
 @staticmethod
 def LogNameFromSourceName(source,machineName):
  """
  LogNameFromSourceName(source: str,machineName: str) -> str

  

   Gets the name of the log to which the specified source is registered.

  

   source: The name of the event source.

   machineName: The name of the computer on which to look,or "." for the local computer.

   Returns: The name of the log associated with the specified source in the registry.
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
 def ModifyOverflowPolicy(self,action,retentionDays):
  """
  ModifyOverflowPolicy(self: EventLog,action: OverflowAction,retentionDays: int)

   Changes the configured behavior for writing new entries when the event log reaches its maximum 

    file size.

  

  

   action: The overflow behavior for writing new entries to the event log.

   retentionDays: The minimum number of days each event log entry is retained. This parameter is used only if 

    action is set to System.Diagnostics.OverflowAction.OverwriteOlder.
  """
  pass
 def RegisterDisplayName(self,resourceFile,resourceId):
  """
  RegisterDisplayName(self: EventLog,resourceFile: str,resourceId: Int64)

   Specifies the localized name of the event log,which is displayed in the server Event Viewer.

  

   resourceFile: The fully specified path to a localized resource file.

   resourceId: The resource identifier that indexes a localized string within the resource file.
  """
  pass
 @staticmethod
 def SourceExists(source,machineName=None):
  """
  SourceExists(source: str,machineName: str) -> bool

  

   Determines whether an event source is registered on a specified computer.

  

   source: The name of the event source.

   machineName: The name the computer on which to look,or "." for the local computer.

   Returns: true if the event source is registered on the given computer; otherwise,false.

  SourceExists(source: str) -> bool

  

   Determines whether an event source is registered on the local computer.

  

   source: The name of the event source.

   Returns: true if the event source is registered on the local computer; otherwise,false.
  """
  pass
 def WriteEntry(self,*__args):
  """
  WriteEntry(self: EventLog,message: str,type: EventLogEntryType,eventID: int,category: Int16)

   Writes an entry with the given message text,application-defined event identifier,and 

    application-defined category to the event log.

  

  

   message: The string to write to the event log.

   type: One of the System.Diagnostics.EventLogEntryType values.

   eventID: The application-specific identifier for the event.

   category: The application-specific subcategory associated with the message.

  WriteEntry(source: str,message: str,type: EventLogEntryType,eventID: int)

   Writes an entry with the given message text and application-defined event identifier to the 

    event log,using the specified registered event source.

  

  

   source: The source by which the application is registered on the specified computer.

   message: The string to write to the event log.

   type: One of the System.Diagnostics.EventLogEntryType values.

   eventID: The application-specific identifier for the event.

  WriteEntry(source: str,message: str,type: EventLogEntryType,eventID: int,category: Int16)

   Writes an entry with the given message text,application-defined event identifier,and 

    application-defined category to the event log,using the specified registered event source. The 

    category can be used by the Event Viewer to filter events in the log.

  

  

   source: The source by which the application is registered on the specified computer.

   message: The string to write to the event log.

   type: One of the System.Diagnostics.EventLogEntryType values.

   eventID: The application-specific identifier for the event.

   category: The application-specific subcategory associated with the message.

  WriteEntry(self: EventLog,message: str,type: EventLogEntryType,eventID: int,category: Int16,rawData: Array[Byte])

   Writes an entry with the given message text,application-defined event identifier,and 

    application-defined category to the event log,and appends binary data to the message.

  

  

   message: The string to write to the event log.

   type: One of the System.Diagnostics.EventLogEntryType values.

   eventID: The application-specific identifier for the event.

   category: The application-specific subcategory associated with the message.

   rawData: An array of bytes that holds the binary data associated with the entry.

  WriteEntry(source: str,message: str,type: EventLogEntryType,eventID: int,category: Int16,rawData: Array[Byte])

   Writes an entry with the given message text,application-defined event identifier,and 

    application-defined category to the event log (using the specified registered event source) and 

    appends binary data to the message.

  

  

   source: The source by which the application is registered on the specified computer.

   message: The string to write to the event log.

   type: One of the System.Diagnostics.EventLogEntryType values.

   eventID: The application-specific identifier for the event.

   category: The application-specific subcategory associated with the message.

   rawData: An array of bytes that holds the binary data associated with the entry.

  WriteEntry(source: str,message: str)

   Writes an information type entry with the given message text to the event log,using the 

    specified registered event source.

  

  

   source: The source by which the application is registered on the specified computer.

   message: The string to write to the event log.

  WriteEntry(self: EventLog,message: str)

   Writes an information type entry,with the given message text,to the event log.

  

   message: The string to write to the event log.

  WriteEntry(self: EventLog,message: str,type: EventLogEntryType)

   Writes an error,warning,information,success audit,or failure audit entry with the given 

    message text to the event log.

  

  

   message: The string to write to the event log.

   type: One of the System.Diagnostics.EventLogEntryType values.

  WriteEntry(self: EventLog,message: str,type: EventLogEntryType,eventID: int)

   Writes an entry with the given message text and application-defined event identifier to the 

    event log.

  

  

   message: The string to write to the event log.

   type: One of the System.Diagnostics.EventLogEntryType values.

   eventID: The application-specific identifier for the event.

  WriteEntry(source: str,message: str,type: EventLogEntryType)

   Writes an error,warning,information,success audit,or failure audit entry with the given 

    message text to the event log,using the specified registered event source.

  

  

   source: The source by which the application is registered on the specified computer.

   message: The string to write to the event log.

   type: One of the System.Diagnostics.EventLogEntryType values.
  """
  pass
 def WriteEvent(self,*__args):
  """
  WriteEvent(source: str,instance: EventInstance,*values: Array[object])

   Writes an event log entry with the given event data and message replacement strings,using the 

    specified registered event source.

  

  

   source: The name of the event source registered for the application on the specified computer.

   instance: An System.Diagnostics.EventInstance instance that represents a localized event log entry.

   values: An array of strings to merge into the message text of the event log entry.

  WriteEvent(source: str,instance: EventInstance,data: Array[Byte],*values: Array[object])

   Writes an event log entry with the given event data,message replacement strings,and associated 

    binary data,and using the specified registered event source.

  

  

   source: The name of the event source registered for the application on the specified computer.

   instance: An System.Diagnostics.EventInstance instance that represents a localized event log entry.

   data: An array of bytes that holds the binary data associated with the entry.

   values: An array of strings to merge into the message text of the event log entry.

  WriteEvent(self: EventLog,instance: EventInstance,*values: Array[object])

   Writes a localized entry to the event log.

  

   instance: An System.Diagnostics.EventInstance instance that represents a localized event log entry.

   values: An array of strings to merge into the message text of the event log entry.

  WriteEvent(self: EventLog,instance: EventInstance,data: Array[Byte],*values: Array[object])

   Writes an event log entry with the given event data,message replacement strings,and associated 

    binary data.

  

  

   instance: An System.Diagnostics.EventInstance instance that represents a localized event log entry.

   data: An array of bytes that holds the binary data associated with the entry.

   values: An array of strings to merge into the message text of the event log entry.
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
 def __new__(self,logName=None,machineName=None,source=None):
  """
  __new__(cls: type)

  __new__(cls: type,logName: str)

  __new__(cls: type,logName: str,machineName: str)

  __new__(cls: type,logName: str,machineName: str,source: str)
  """
  pass
 def __str__(self,*args):
  pass
 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 EnableRaisingEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Diagnostics.EventLog receives System.Diagnostics.EventLog.EntryWritten event notifications.



Get: EnableRaisingEvents(self: EventLog) -> bool



Set: EnableRaisingEvents(self: EventLog)=value

"""

 Entries=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the contents of the event log.



Get: Entries(self: EventLog) -> EventLogEntryCollection



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Log=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the log to read from or write to.



Get: Log(self: EventLog) -> str



Set: Log(self: EventLog)=value

"""

 LogDisplayName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the event log's friendly name.



Get: LogDisplayName(self: EventLog) -> str



"""

 MachineName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the computer on which to read or write events.



Get: MachineName(self: EventLog) -> str



Set: MachineName(self: EventLog)=value

"""

 MaximumKilobytes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum event log size in kilobytes.



Get: MaximumKilobytes(self: EventLog) -> Int64



Set: MaximumKilobytes(self: EventLog)=value

"""

 MinimumRetentionDays=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of days to retain entries in the event log.



Get: MinimumRetentionDays(self: EventLog) -> int



"""

 OverflowAction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the configured behavior for storing new entries when the event log reaches its maximum log file size.



Get: OverflowAction(self: EventLog) -> OverflowAction



"""

 Source=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the source name to register and use when writing to the event log.



Get: Source(self: EventLog) -> str



Set: Source(self: EventLog)=value

"""

 SynchronizingObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object used to marshal the event handler calls issued as a result of an System.Diagnostics.EventLog entry written event.



Get: SynchronizingObject(self: EventLog) -> ISynchronizeInvoke



Set: SynchronizingObject(self: EventLog)=value

"""


 EntryWritten=None

