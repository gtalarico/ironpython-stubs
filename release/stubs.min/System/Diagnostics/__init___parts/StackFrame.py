class StackFrame(object):
 """
 Provides information about a System.Diagnostics.StackFrame,which represents a function call on the call stack for the current thread.

 

 StackFrame()

 StackFrame(fNeedFileInfo: bool)

 StackFrame(skipFrames: int)

 StackFrame(skipFrames: int,fNeedFileInfo: bool)

 StackFrame(fileName: str,lineNumber: int)

 StackFrame(fileName: str,lineNumber: int,colNumber: int)
 """
 def GetFileColumnNumber(self):
  """
  GetFileColumnNumber(self: StackFrame) -> int

  

   Gets the column number in the file that contains the code that is executing. This information is 

    typically extracted from the debugging symbols for the executable.

  

   Returns: The file column number,or 0 (zero) if the file column number cannot be determined.
  """
  pass
 def GetFileLineNumber(self):
  """
  GetFileLineNumber(self: StackFrame) -> int

  

   Gets the line number in the file that contains the code that is executing. This information is 

    typically extracted from the debugging symbols for the executable.

  

   Returns: The file line number,or 0 (zero) if the file line number cannot be determined.
  """
  pass
 def GetFileName(self):
  """
  GetFileName(self: StackFrame) -> str

  

   Gets the file name that contains the code that is executing. This information is typically 

    extracted from the debugging symbols for the executable.

  

   Returns: The file name,or null if the file name cannot be determined.
  """
  pass
 def GetILOffset(self):
  """
  GetILOffset(self: StackFrame) -> int

  

   Gets the offset from the start of the Microsoft intermediate language (MSIL) code for the method 

    that is executing. This offset might be an approximation depending on whether or not the 

    just-in-time (JIT) compiler is generating debugging code. The generation of this debugging 

    information is controlled by the System.Diagnostics.DebuggableAttribute.

  

   Returns: The offset from the start of the MSIL code for the method that is executing.
  """
  pass
 def GetMethod(self):
  """
  GetMethod(self: StackFrame) -> MethodBase

  

   Gets the method in which the frame is executing.

   Returns: The method in which the frame is executing.
  """
  pass
 def GetNativeOffset(self):
  """
  GetNativeOffset(self: StackFrame) -> int

  

   Gets the offset from the start of the native just-in-time (JIT)-compiled code for the method 

    that is being executed. The generation of this debugging information is controlled by the 

    System.Diagnostics.DebuggableAttribute class.

  

   Returns: The offset from the start of the JIT-compiled code for the method that is being executed.
  """
  pass
 def ToString(self):
  """
  ToString(self: StackFrame) -> str

  

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

  __new__(cls: type,fileName: str,lineNumber: int)

  __new__(cls: type,fileName: str,lineNumber: int,colNumber: int)
  """
  pass
 OFFSET_UNKNOWN=-1

