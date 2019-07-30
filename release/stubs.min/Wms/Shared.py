# encoding: utf-8
# module Wms.Shared calls itself Shared
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class ILoggingService:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ILoggingService()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Debug(self,*__args):
  """ Debug(self: ILoggingService,message: str)Debug(self: ILoggingService,format: str,*args: Array[object]) """
  pass
 def Error(self,*__args):
  """ Error(self: ILoggingService,exception: Exception)Error(self: ILoggingService,message: str)Error(self: ILoggingService,format: str,*args: Array[object]) """
  pass
 def Fatal(self,*__args):
  """ Fatal(self: ILoggingService,exception: Exception)Fatal(self: ILoggingService,message: str)Fatal(self: ILoggingService,format: str,*args: Array[object]) """
  pass
 def Info(self,*__args):
  """ Info(self: ILoggingService,message: str)Info(self: ILoggingService,format: str,*args: Array[object]) """
  pass
 def Trace(self,*__args):
  """ Trace(self: ILoggingService,message: str)Trace(self: ILoggingService,format: str,*args: Array[object]) """
  pass
 def Warn(self,*__args):
  """ Warn(self: ILoggingService,message: str)Warn(self: ILoggingService,format: str,*args: Array[object])Warn(self: ILoggingService,exception: Exception) """
  pass
 def Write(self,*__args):
  """ Write(self: ILoggingService,message: str)Write(self: ILoggingService,message: object)Write(self: ILoggingService,message: object,category: str)Write(self: ILoggingService,exception: Exception) """
  pass
 def WriteDebug(self,message,category):
  """ WriteDebug(self: ILoggingService,message: str,category: str) """
  pass
 def WriteError(self,message,category=None):
  """ WriteError(self: ILoggingService,message: object)WriteError(self: ILoggingService,message: object,category: str) """
  pass
 def WriteFatal(self,message,category):
  """ WriteFatal(self: ILoggingService,message: str,category: str) """
  pass
 def WriteInfo(self,message,category):
  """ WriteInfo(self: ILoggingService,message: str,category: str) """
  pass
 def WriteTrace(self,message,category):
  """ WriteTrace(self: ILoggingService,message: str,category: str) """
  pass
 def WriteWarn(self,message,category):
  """ WriteWarn(self: ILoggingService,message: str,category: str) """
  pass
 def WriteWarning(self,message):
  """ WriteWarning(self: ILoggingService,message: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class ITraceLoggingService:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ITraceLoggingService()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def IsTracingEnabled(self):
  """ IsTracingEnabled(self: ITraceLoggingService) -> bool """
  pass
 def ToggleEnableTracing(self):
  """ ToggleEnableTracing(self: ITraceLoggingService) -> bool """
  pass
 def Trace(self,properties,eventType,*__args):
  """ Trace(self: ITraceLoggingService,properties: IDictionary[str,object],eventType: TraceType,format: str,*args: Array[object])Trace(self: ITraceLoggingService,properties: IDictionary[str,object],eventType: TraceType,message: str) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class TraceExtProperties:
 """ enum TraceExtProperties,values: ElapsedSeconds (4),MethodId (0),MethodName (1),MethodPreviousId (6),MethodPreviousName (5),ParameterList (3),ReturnParam (2),TimeStart (7),TimeStop (8) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TraceExtProperties()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 ElapsedSeconds=None
 MethodId=None
 MethodName=None
 MethodPreviousId=None
 MethodPreviousName=None
 ParameterList=None
 ReturnParam=None
 TimeStart=None
 TimeStop=None
 value__=None


class TraceType:
 """ enum TraceType,values: Start (1),Stop (0) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TraceType()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Start=None
 Stop=None
 value__=None


