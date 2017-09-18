class TraceEventCache(object):
 """
 Provides trace event data specific to a thread and a process.

 

 TraceEventCache()
 """
 Callstack=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the call stack for the current thread.



Get: Callstack(self: TraceEventCache) -> str



"""

 DateTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the date and time at which the event trace occurred.



Get: DateTime(self: TraceEventCache) -> DateTime



"""

 LogicalOperationStack=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the correlation data,contained in a stack.



Get: LogicalOperationStack(self: TraceEventCache) -> Stack



"""

 ProcessId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unique identifier of the current process.



Get: ProcessId(self: TraceEventCache) -> int



"""

 ThreadId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a unique identifier for the current managed thread.



Get: ThreadId(self: TraceEventCache) -> str



"""

 Timestamp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current number of ticks in the timer mechanism.



Get: Timestamp(self: TraceEventCache) -> Int64



"""


