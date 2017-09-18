class BooleanSwitch(Switch):
 """
 Provides a simple on/off switch that controls debugging and tracing output.

 

 BooleanSwitch(displayName: str,description: str)

 BooleanSwitch(displayName: str,description: str,defaultSwitchValue: str)
 """
 @staticmethod
 def __new__(self,displayName,description,defaultSwitchValue=None):
  """
  __new__(cls: type,displayName: str,description: str)

  __new__(cls: type,displayName: str,description: str,defaultSwitchValue: str)
  """
  pass
 Enabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the switch is enabled or disabled.



Get: Enabled(self: BooleanSwitch) -> bool



Set: Enabled(self: BooleanSwitch)=value

"""

 SwitchSetting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current setting for this switch.



"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the switch.



"""


