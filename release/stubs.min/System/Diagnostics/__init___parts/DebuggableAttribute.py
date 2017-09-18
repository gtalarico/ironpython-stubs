class DebuggableAttribute(Attribute,_Attribute):
 """
 Modifies code generation for runtime just-in-time (JIT) debugging. This class cannot be inherited.

 

 DebuggableAttribute(isJITTrackingEnabled: bool,isJITOptimizerDisabled: bool)

 DebuggableAttribute(modes: DebuggingModes)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,isJITTrackingEnabled: bool,isJITOptimizerDisabled: bool)

  __new__(cls: type,modes: DebuggingModes)
  """
  pass
 DebuggingFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the debugging modes for the attribute.



Get: DebuggingFlags(self: DebuggableAttribute) -> DebuggingModes



"""

 IsJITOptimizerDisabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the runtime optimizer is disabled.



Get: IsJITOptimizerDisabled(self: DebuggableAttribute) -> bool



"""

 IsJITTrackingEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the runtime will track information during code generation for the debugger.



Get: IsJITTrackingEnabled(self: DebuggableAttribute) -> bool



"""


 DebuggingModes=None

