class Switch(object):
 """ Provides an abstract base class to create new debugging and tracing switches. """
 def GetSupportedAttributes(self,*args):
  """
  GetSupportedAttributes(self: Switch) -> Array[str]

  

   Gets the custom attributes supported by the switch.

   Returns: A string array that contains the names of the custom attributes supported by the switch,or null 

    if there no custom attributes are supported.
  """
  pass
 def OnSwitchSettingChanged(self,*args):
  """
  OnSwitchSettingChanged(self: Switch)

   Invoked when the System.Diagnostics.Switch.SwitchSetting property is changed.
  """
  pass
 def OnValueChanged(self,*args):
  """
  OnValueChanged(self: Switch)

   Invoked when the System.Diagnostics.Switch.Value property is changed.
  """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type,displayName: str,description: str)

  __new__(cls: type,displayName: str,description: str,defaultSwitchValue: str)
  """
  pass
 Attributes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the custom switch attributes defined in the application configuration file.



Get: Attributes(self: Switch) -> StringDictionary



"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a description of the switch.



Get: Description(self: Switch) -> str



"""

 DisplayName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a name used to identify the switch.



Get: DisplayName(self: Switch) -> str



"""

 SwitchSetting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current setting for this switch.



"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the switch.



"""


