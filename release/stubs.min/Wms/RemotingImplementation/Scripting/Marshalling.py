# encoding: utf-8
# module Wms.RemotingImplementation.Scripting.Marshalling calls itself Marshalling
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class MarshalledPythonScriptEvaluator(MarshalledObject):
 """ MarshalledPythonScriptEvaluator(lifetime: TimeSpan) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MarshalledPythonScriptEvaluator()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def GetLibRoot():
  """ GetLibRoot() -> str """
  pass
 @staticmethod
 def GetStdLibRoot(path):
  """ GetStdLibRoot() -> (bool,str) """
  pass
 def RunScript(self,script,variables):
  """ RunScript[T](self: MarshalledPythonScriptEvaluator,script: str,variables: Dictionary[str,object]) -> T """
  pass
 @staticmethod
 def __new__(self,lifetime):
  """ __new__(cls: type,lifetime: TimeSpan) """
  pass
 StateServerChannelName=property(lambda self: object(),lambda self,v: None,lambda self: None)



class PythonStdoutInterProcessLogger(StreamWriter):
 """ PythonStdoutInterProcessLogger(loggerProxy: IMarshalledLogger,stream: Stream) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PythonStdoutInterProcessLogger()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Dispose(self):
  """
  Dispose(self: StreamWriter,disposing: bool)
   Releases the unmanaged resources used by the System.IO.StreamWriter and optionally releases the managed resources.
  
   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject
  
   Creates a shallow copy of the current System.MarshalByRefObject object.
  
   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the object to be assigned a new identity when it is marshaled across a remoting 
    boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone,which will cause remoting client calls 
    to be routed to the remote server object.
  
   Returns: A shallow copy of the current System.MarshalByRefObject object.
  MemberwiseClone(self: object) -> object
  
   Creates a shallow copy of the current System.Object.
   Returns: A shallow copy of the current System.Object.
  """
  pass
 def Write(self,*__args):
  """ Write(self: PythonStdoutInterProcessLogger,value: str) """
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
 @staticmethod
 def __new__(self,loggerProxy,stream):
  """ __new__(cls: type,loggerProxy: IMarshalledLogger,stream: Stream) """
  pass
 CoreNewLine=None


