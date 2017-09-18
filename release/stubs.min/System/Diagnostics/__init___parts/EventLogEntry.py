class EventLogEntry(Component,IComponent,IDisposable,ISerializable):
 """ Encapsulates a single record in the event log. This class cannot be inherited. """
 def Dispose(self):
  """
  Dispose(self: Component,disposing: bool)

   Releases the unmanaged resources used by the System.ComponentModel.Component and optionally 

    releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: EventLogEntry,otherEntry: EventLogEntry) -> bool

  

   Performs a comparison between two event log entries.

  

   otherEntry: The System.Diagnostics.EventLogEntry to compare.

   Returns: true if the System.Diagnostics.EventLogEntry objects are identical; otherwise,false.
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
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
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
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 Category=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the text associated with the System.Diagnostics.EventLogEntry.CategoryNumber property for this entry.



Get: Category(self: EventLogEntry) -> str



"""

 CategoryNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the category number of the event log entry.



Get: CategoryNumber(self: EventLogEntry) -> Int16



"""

 Data=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the binary data associated with the entry.



Get: Data(self: EventLogEntry) -> Array[Byte]



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 EntryType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the event type of this entry.



Get: EntryType(self: EventLogEntry) -> EventLogEntryType



"""

 EventID=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the application-specific event identifier for the current event entry.



Get: EventID(self: EventLogEntry) -> int



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of this entry in the event log.



Get: Index(self: EventLogEntry) -> int



"""

 InstanceId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the resource identifier that designates the message text of the event entry.



Get: InstanceId(self: EventLogEntry) -> Int64



"""

 MachineName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the computer on which this entry was generated.



Get: MachineName(self: EventLogEntry) -> str



"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the localized message associated with this event entry.



Get: Message(self: EventLogEntry) -> str



"""

 ReplacementStrings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the replacement strings associated with the event log entry.



Get: ReplacementStrings(self: EventLogEntry) -> Array[str]



"""

 Source=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the application that generated this event.



Get: Source(self: EventLogEntry) -> str



"""

 TimeGenerated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the local time at which this event was generated.



Get: TimeGenerated(self: EventLogEntry) -> DateTime



"""

 TimeWritten=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the local time at which this event was written to the log.



Get: TimeWritten(self: EventLogEntry) -> DateTime



"""

 UserName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the user who is responsible for this event.



Get: UserName(self: EventLogEntry) -> str



"""


