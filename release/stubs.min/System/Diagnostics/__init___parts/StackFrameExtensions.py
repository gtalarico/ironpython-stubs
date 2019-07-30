class StackFrameExtensions(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StackFrameExtensions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def GetNativeImageBase(stackFrame):
  """ GetNativeImageBase(stackFrame: StackFrame) -> IntPtr """
  pass
 @staticmethod
 def GetNativeIP(stackFrame):
  """ GetNativeIP(stackFrame: StackFrame) -> IntPtr """
  pass
 @staticmethod
 def HasILOffset(stackFrame):
  """ HasILOffset(stackFrame: StackFrame) -> bool """
  pass
 @staticmethod
 def HasMethod(stackFrame):
  """ HasMethod(stackFrame: StackFrame) -> bool """
  pass
 @staticmethod
 def HasNativeImage(stackFrame):
  """ HasNativeImage(stackFrame: StackFrame) -> bool """
  pass
 @staticmethod
 def HasSource(stackFrame):
  """ HasSource(stackFrame: StackFrame) -> bool """
  pass
 __all__=[
  'GetNativeImageBase',
  'GetNativeIP',
  'HasILOffset',
  'HasMethod',
  'HasNativeImage',
  'HasSource',
 ]

