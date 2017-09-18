class SourceFilter(TraceFilter):
 """
 Indicates whether a listener should trace a message based on the source of a trace.

 

 SourceFilter(source: str)
 """
 def ShouldTrace(self,cache,source,eventType,id,formatOrMessage,args,data1,data):
  """
  ShouldTrace(self: SourceFilter,cache: TraceEventCache,source: str,eventType: TraceEventType,id: int,formatOrMessage: str,args: Array[object],data1: object,data: Array[object]) -> bool

  

   Determines whether the trace listener should trace the event.

  

   cache: An object that represents the information cache for the trace event.

   source: The name of the source.

   eventType: One of the enumeration values that identifies the event type.

   id: A trace identifier number.

   formatOrMessage: The format to use for writing an array of arguments or a message to write.

   args: An array of argument objects.

   data1: A trace data object.

   data: An array of trace data objects.

   Returns: true if the trace should be produced; otherwise,false.
  """
  pass
 @staticmethod
 def __new__(self,source):
  """ __new__(cls: type,source: str) """
  pass
 Source=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the trace source.



Get: Source(self: SourceFilter) -> str



Set: Source(self: SourceFilter)=value

"""


