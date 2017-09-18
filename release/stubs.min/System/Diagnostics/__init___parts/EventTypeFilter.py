class EventTypeFilter(TraceFilter):
 """
 Indicates whether a listener should trace based on the event type.

 

 EventTypeFilter(level: SourceLevels)
 """
 def ShouldTrace(self,cache,source,eventType,id,formatOrMessage,args,data1,data):
  """
  ShouldTrace(self: EventTypeFilter,cache: TraceEventCache,source: str,eventType: TraceEventType,id: int,formatOrMessage: str,args: Array[object],data1: object,data: Array[object]) -> bool

  

   Determines whether the trace listener should trace the event.

  

   cache: A System.Diagnostics.TraceEventCache that represents the information cache for the trace event.

   source: The name of the source.

   eventType: One of the System.Diagnostics.TraceEventType values.

   id: A trace identifier number.

   formatOrMessage: The format to use for writing an array of arguments,or a message to write.

   args: An array of argument objects.

   data1: A trace data object.

   data: An array of trace data objects.

   Returns: trueif the trace should be produced; otherwise,false.
  """
  pass
 @staticmethod
 def __new__(self,level):
  """ __new__(cls: type,level: SourceLevels) """
  pass
 EventType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the event type of the messages to trace.



Get: EventType(self: EventTypeFilter) -> SourceLevels



Set: EventType(self: EventTypeFilter)=value

"""


