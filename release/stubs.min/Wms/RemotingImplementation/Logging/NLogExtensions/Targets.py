# encoding: utf-8
# module Wms.RemotingImplementation.Logging.NLogExtensions.Targets calls itself Targets
# from Wms.RemotingImplementation,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ExceptionExtensions:
 # no doc
 @staticmethod
 def IsLoggedToInternalLogger(exception):
  """ IsLoggedToInternalLogger(exception: Exception) -> bool """
  pass
 @staticmethod
 def MustBeRethrown(exception):
  """ MustBeRethrown(exception: Exception) -> bool """
  pass
 @staticmethod
 def MustBeRethrownImmediately(exception):
  """ MustBeRethrownImmediately(exception: Exception) -> bool """
  pass
 __all__=[
  'IsLoggedToInternalLogger',
  'MustBeRethrown',
  'MustBeRethrownImmediately',
 ]


class LogLevelExtensions:
 # no doc
 @staticmethod
 def ToSeverity(level):
  """ ToSeverity(level: LogLevel) -> LogSeverity """
  pass
 __all__=[
  'ToSeverity',
 ]


class StackdriverLabel:
 """
 StackdriverLabel()
 StackdriverLabel(parameterName: str,parameterLayout: Layout)
 """
 @staticmethod
 def __new__(self,parameterName=None,parameterLayout=None):
  """
  __new__(cls: type)
  __new__(cls: type,parameterName: str,parameterLayout: Layout)
  """
  pass
 Layout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Layout(self: StackdriverLabel) -> Layout

Set: Layout(self: StackdriverLabel)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: StackdriverLabel) -> str

Set: Name(self: StackdriverLabel)=value
"""



class StackDriverLoggingTarget:
 """ StackDriverLoggingTarget() """
 def CloseTarget(self,*args):
  """ CloseTarget(self: StackDriverLoggingTarget) """
  pass
 def Dispose(self):
  """
  Dispose(self: Target,disposing: bool)
   Releases unmanaged and - optionally - managed resources.
  
   disposing: True to release both managed and unmanaged resources; false to release only unmanaged 
    resources.
  """
  pass
 def FlushAsync(self,*args):
  """
  FlushAsync(self: Target,asyncContinuation: AsyncContinuation)
   Flush any pending log messages asynchronously (in case of asynchronous targets).
  
   asyncContinuation: The asynchronous continuation.
  """
  pass
 def InitializeTarget(self,*args):
  """
  InitializeTarget(self: Target)
   Initializes the target. Can be used by inheriting classes
     to initialize 
    logging.
  """
  pass
 def MergeEventProperties(self,*args):
  """
  MergeEventProperties(self: Target,logEvent: LogEventInfo)
   Merges (copies) the event context properties from any event info object stored in
      
      parameters of the given event info object.
  
  
   logEvent: The event info object to perform the merge to.
  """
  pass
 def RenderLogEvent(self,*args):
  """
  RenderLogEvent(self: Target,layout: Layout,logEvent: LogEventInfo) -> str
  
   Renders the event info in layout.
  
   layout: The layout.
   logEvent: The event info.
   Returns: String representing log event.
  """
  pass
 def Write(self,*args):
  """
  Write(self: StackDriverLoggingTarget,logEvent: LogEventInfo)Write(self: StackDriverLoggingTarget,logEvents: Array[AsyncLogEventInfo])Write(self: Target,logEvent: AsyncLogEventInfo)
   Writes async log event to the log target.
  
   logEvent: Async Log event to be written out.
  Write(self: Target,logEvents: IList[AsyncLogEventInfo])
  """
  pass
 def WriteAsyncThreadSafe(self,*args):
  """
  WriteAsyncThreadSafe(self: Target,logEvent: AsyncLogEventInfo)
   Writes a log event to the log target,in a thread safe manner.
  
   logEvent: Log event to be written out.
  WriteAsyncThreadSafe(self: Target,logEvents: Array[AsyncLogEventInfo])
   NOTE! Obsolete,instead override WriteAsyncThreadSafe(IList{AsyncLogEventInfo} logEvents)
    
     
     Writes an array of logging events to the log target,in a 
    thread safe manner.
  
  
   logEvents: Logging events to be written out.
  WriteAsyncThreadSafe(self: Target,logEvents: IList[AsyncLogEventInfo])
  """
  pass
 def WriteToStackDriver(self,projectId,logId,logEvent):
  """ WriteToStackDriver(self: StackDriverLoggingTarget,projectId: str,logId: str,logEvent: LogEventInfo) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 Client=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Client(self: StackDriverLoggingTarget) -> LoggingServiceV2Client

Set: Client(self: StackDriverLoggingTarget)=value
"""

 IsInitialized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the target has been initialized.

"""

 Labels=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Labels(self: StackDriverLoggingTarget) -> IList[StackdriverLabel]

"""

 LoggingConfiguration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the logging configuration this target is part of.

"""

 LogId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LogId(self: StackDriverLoggingTarget) -> str

Set: LogId(self: StackDriverLoggingTarget)=value
"""

 ProjectId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ProjectId(self: StackDriverLoggingTarget) -> str

Set: ProjectId(self: StackDriverLoggingTarget)=value
"""

 SyncRoot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the object which can be used to synchronize asynchronous operations that must rely on the .

"""



