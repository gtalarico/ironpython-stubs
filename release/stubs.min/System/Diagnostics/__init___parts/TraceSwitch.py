class TraceSwitch(Switch):
 """
 Provides a multilevel switch to control tracing and debug output without recompiling your code.

 

 TraceSwitch(displayName: str,description: str)

 TraceSwitch(displayName: str,description: str,defaultSwitchValue: str)
 """
 @staticmethod
 def __new__(self,displayName,description,defaultSwitchValue=None):
  """
  __new__(cls: type,displayName: str,description: str)

  __new__(cls: type,displayName: str,description: str,defaultSwitchValue: str)
  """
  pass
 Level=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the trace level that determines the messages the switch allows.



Get: Level(self: TraceSwitch) -> TraceLevel



Set: Level(self: TraceSwitch)=value

"""

 SwitchSetting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current setting for this switch.



"""

 TraceError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the switch allows error-handling messages.



Get: TraceError(self: TraceSwitch) -> bool



"""

 TraceInfo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the switch allows informational messages.



Get: TraceInfo(self: TraceSwitch) -> bool



"""

 TraceVerbose=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the switch allows all messages.



Get: TraceVerbose(self: TraceSwitch) -> bool



"""

 TraceWarning=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the switch allows warning messages.



Get: TraceWarning(self: TraceSwitch) -> bool



"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the switch.



"""


