class EventSourceCreationData(object):
 """
 Represents the configuration settings used to create an event log source on the local computer or a remote computer.

 

 EventSourceCreationData(source: str,logName: str)
 """
 @staticmethod
 def __new__(self,source,logName):
  """ __new__(cls: type,source: str,logName: str) """
  pass
 CategoryCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of categories in the category resource file.



Get: CategoryCount(self: EventSourceCreationData) -> int



Set: CategoryCount(self: EventSourceCreationData)=value

"""

 CategoryResourceFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the path of the resource file that contains category strings for the source.



Get: CategoryResourceFile(self: EventSourceCreationData) -> str



Set: CategoryResourceFile(self: EventSourceCreationData)=value

"""

 LogName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the event log to which the source writes entries.



Get: LogName(self: EventSourceCreationData) -> str



Set: LogName(self: EventSourceCreationData)=value

"""

 MachineName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the computer on which to register the event source.



Get: MachineName(self: EventSourceCreationData) -> str



Set: MachineName(self: EventSourceCreationData)=value

"""

 MessageResourceFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the path of the message resource file that contains message formatting strings for the source.



Get: MessageResourceFile(self: EventSourceCreationData) -> str



Set: MessageResourceFile(self: EventSourceCreationData)=value

"""

 ParameterResourceFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the path of the resource file that contains message parameter strings for the source.



Get: ParameterResourceFile(self: EventSourceCreationData) -> str



Set: ParameterResourceFile(self: EventSourceCreationData)=value

"""

 Source=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name to register with the event log as an event source.



Get: Source(self: EventSourceCreationData) -> str



Set: Source(self: EventSourceCreationData)=value

"""


