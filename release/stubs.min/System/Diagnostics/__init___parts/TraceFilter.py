class TraceFilter(object):
 """ Provides the base class for trace filter implementations. """
 def ShouldTrace(self,cache,source,eventType,id,formatOrMessage,args,data1,data):
  """
  ShouldTrace(self: TraceFilter,cache: TraceEventCache,source: str,eventType: TraceEventType,id: int,formatOrMessage: str,args: Array[object],data1: object,data: Array[object]) -> bool

  

   When overridden in a derived class,determines whether the trace listener should trace the event.

  

   cache: The System.Diagnostics.TraceEventCache that contains information for the trace event.

   source: The name of the source.

   eventType: One of the System.Diagnostics.TraceEventType values specifying the type of event that has caused 

    the trace.

  

   id: A trace identifier number.

   formatOrMessage: Either the format to use for writing an array of arguments specified by the args parameter,or a 

    message to write.

  

   args: An array of argument objects.

   data1: A trace data object.

   data: An array of trace data objects.

   Returns: true to trace the specified event; otherwise,false.
  """
  pass
