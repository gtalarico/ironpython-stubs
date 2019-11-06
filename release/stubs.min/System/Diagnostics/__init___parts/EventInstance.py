class EventInstance(object):
 """
 Represents language-neutral information for an event log entry.
 
 EventInstance(instanceId: Int64,categoryId: int)
 EventInstance(instanceId: Int64,categoryId: int,entryType: EventLogEntryType)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return EventInstance()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,instanceId,categoryId,entryType=None):
  """
  __new__(cls: type,instanceId: Int64,categoryId: int)
  __new__(cls: type,instanceId: Int64,categoryId: int,entryType: EventLogEntryType)
  """
  pass
 CategoryId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the resource identifier that specifies the application-defined category of the event entry.

Get: CategoryId(self: EventInstance) -> int

Set: CategoryId(self: EventInstance)=value
"""

 EntryType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the event type of the event log entry.

Get: EntryType(self: EventInstance) -> EventLogEntryType

Set: EntryType(self: EventInstance)=value
"""

 InstanceId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the resource identifier that designates the message text of the event entry.

Get: InstanceId(self: EventInstance) -> Int64

Set: InstanceId(self: EventInstance)=value
"""


