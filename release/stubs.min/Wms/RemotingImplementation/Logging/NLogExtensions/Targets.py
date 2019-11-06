# encoding: utf-8
# module Wms.RemotingImplementation.Logging.NLogExtensions.Targets calls itself Targets
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class ExceptionExtensions(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ExceptionExtensions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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


class LogLevelExtensions(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return LogLevelExtensions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def ToSeverity(level):
  """ ToSeverity(level: LogLevel) -> LogSeverity """
  pass
 __all__=[
  'ToSeverity',
 ]


class StackdriverLabel(object):
 """
 StackdriverLabel()
 StackdriverLabel(parameterName: str,parameterLayout: Layout)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StackdriverLabel()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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



class StackDriverLoggingTarget(TargetWithLayout):
 """ StackDriverLoggingTarget() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StackDriverLoggingTarget()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def CloseTarget(self,*args):
  """ CloseTarget(self: StackDriverLoggingTarget) """
  pass
 def Dispose(self):
  """ Dispose(self: Target,disposing: bool) """
  pass
 def FlushAsync(self,*args):
  """ FlushAsync(self: Target,asyncContinuation: AsyncContinuation) """
  pass
 def InitializeTarget(self,*args):
  """ InitializeTarget(self: Target) """
  pass
 def MergeEventProperties(self,*args):
  """ MergeEventProperties(self: Target,logEvent: LogEventInfo) """
  pass
 def RenderLogEvent(self,*args):
  """ RenderLogEvent(self: Target,layout: Layout,logEvent: LogEventInfo) -> str """
  pass
 def Write(self,*args):
  """ Write(self: StackDriverLoggingTarget,logEvent: LogEventInfo)Write(self: StackDriverLoggingTarget,logEvents: Array[AsyncLogEventInfo])Write(self: Target,logEvent: AsyncLogEventInfo)Write(self: Target,logEvents: IList[AsyncLogEventInfo]) """
  pass
 def WriteAsyncThreadSafe(self,*args):
  """ WriteAsyncThreadSafe(self: Target,logEvent: AsyncLogEventInfo)WriteAsyncThreadSafe(self: Target,logEvents: Array[AsyncLogEventInfo])WriteAsyncThreadSafe(self: Target,logEvents: IList[AsyncLogEventInfo]) """
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

 Labels=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Labels(self: StackDriverLoggingTarget) -> IList[StackdriverLabel]

"""

 LoggingConfiguration=property(lambda self: object(),lambda self,v: None,lambda self: None)

 LogId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LogId(self: StackDriverLoggingTarget) -> str

Set: LogId(self: StackDriverLoggingTarget)=value
"""

 ProjectId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ProjectId(self: StackDriverLoggingTarget) -> str

Set: ProjectId(self: StackDriverLoggingTarget)=value
"""

 SyncRoot=property(lambda self: object(),lambda self,v: None,lambda self: None)



