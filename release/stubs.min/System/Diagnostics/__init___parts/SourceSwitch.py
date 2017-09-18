class SourceSwitch(Switch):
 """
 Provides a multilevel switch to control tracing and debug output without recompiling your code.

 

 SourceSwitch(name: str)

 SourceSwitch(displayName: str,defaultSwitchValue: str)
 """
 def ShouldTrace(self,eventType):
  """
  ShouldTrace(self: SourceSwitch,eventType: TraceEventType) -> bool

  

   Determines if trace listeners should be called,based on the trace event type.

  

   eventType: One of the System.Diagnostics.TraceEventType values.

   Returns: True if the trace listeners should be called; otherwise,false.
  """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,name: str)

  __new__(cls: type,displayName: str,defaultSwitchValue: str)
  """
  pass
 Level=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the level of the switch.



Get: Level(self: SourceSwitch) -> SourceLevels



Set: Level(self: SourceSwitch)=value

"""

 SwitchSetting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current setting for this switch.



"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the switch.



"""


