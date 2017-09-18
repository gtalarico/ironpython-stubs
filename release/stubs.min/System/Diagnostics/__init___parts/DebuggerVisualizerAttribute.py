class DebuggerVisualizerAttribute(Attribute,_Attribute):
 """
 Specifies that the type has a visualizer. This class cannot be inherited.

 

 DebuggerVisualizerAttribute(visualizerTypeName: str)

 DebuggerVisualizerAttribute(visualizerTypeName: str,visualizerObjectSourceTypeName: str)

 DebuggerVisualizerAttribute(visualizerTypeName: str,visualizerObjectSource: Type)

 DebuggerVisualizerAttribute(visualizer: Type)

 DebuggerVisualizerAttribute(visualizer: Type,visualizerObjectSource: Type)

 DebuggerVisualizerAttribute(visualizer: Type,visualizerObjectSourceTypeName: str)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,visualizerTypeName: str)

  __new__(cls: type,visualizerTypeName: str,visualizerObjectSourceTypeName: str)

  __new__(cls: type,visualizerTypeName: str,visualizerObjectSource: Type)

  __new__(cls: type,visualizer: Type)

  __new__(cls: type,visualizer: Type,visualizerObjectSource: Type)

  __new__(cls: type,visualizer: Type,visualizerObjectSourceTypeName: str)
  """
  pass
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the description of the visualizer.



Get: Description(self: DebuggerVisualizerAttribute) -> str



Set: Description(self: DebuggerVisualizerAttribute)=value

"""

 Target=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the target type when the attribute is applied at the assembly level.



Get: Target(self: DebuggerVisualizerAttribute) -> Type



Set: Target(self: DebuggerVisualizerAttribute)=value

"""

 TargetTypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the fully qualified type name when the attribute is applied at the assembly level.



Get: TargetTypeName(self: DebuggerVisualizerAttribute) -> str



Set: TargetTypeName(self: DebuggerVisualizerAttribute)=value

"""

 VisualizerObjectSourceTypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the fully qualified type name of the visualizer object source.



Get: VisualizerObjectSourceTypeName(self: DebuggerVisualizerAttribute) -> str



"""

 VisualizerTypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the fully qualified type name of the visualizer.



Get: VisualizerTypeName(self: DebuggerVisualizerAttribute) -> str



"""


