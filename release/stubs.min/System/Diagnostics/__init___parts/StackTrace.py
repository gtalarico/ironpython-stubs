class StackTrace(object):
 """
 Represents a stack trace,which is an ordered collection of one or more stack frames.

 

 StackTrace()

 StackTrace(fNeedFileInfo: bool)

 StackTrace(skipFrames: int)

 StackTrace(skipFrames: int,fNeedFileInfo: bool)

 StackTrace(e: Exception)

 StackTrace(e: Exception,fNeedFileInfo: bool)

 StackTrace(e: Exception,skipFrames: int)

 StackTrace(e: Exception,skipFrames: int,fNeedFileInfo: bool)

 StackTrace(frame: StackFrame)

 StackTrace(targetThread: Thread,needFileInfo: bool)
 """
 def GetFrame(self,index):
  """
  GetFrame(self: StackTrace,index: int) -> StackFrame

  

   Gets the specified stack frame.

  

   index: The index of the stack frame requested.

   Returns: The specified stack frame.
  """
  pass
 def GetFrames(self):
  """
  GetFrames(self: StackTrace) -> Array[StackFrame]

  

   Returns a copy of all stack frames in the current stack trace.

   Returns: An array of type System.Diagnostics.StackFrame representing the function calls in the stack 

    trace.
  """
  pass
 def ToString(self):
  """
  ToString(self: StackTrace) -> str

  

   Builds a readable representation of the stack trace.

   Returns: A readable representation of the stack trace.
  """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,fNeedFileInfo: bool)

  __new__(cls: type,skipFrames: int)

  __new__(cls: type,skipFrames: int,fNeedFileInfo: bool)

  __new__(cls: type,e: Exception)

  __new__(cls: type,e: Exception,fNeedFileInfo: bool)

  __new__(cls: type,e: Exception,skipFrames: int)

  __new__(cls: type,e: Exception,skipFrames: int,fNeedFileInfo: bool)

  __new__(cls: type,frame: StackFrame)

  __new__(cls: type,targetThread: Thread,needFileInfo: bool)
  """
  pass
 FrameCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of frames in the stack trace.



Get: FrameCount(self: StackTrace) -> int



"""


 METHODS_TO_SKIP=0

