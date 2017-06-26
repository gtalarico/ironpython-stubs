class StylusButton(object):
 """ Represents a button on a stylus. """
 def ToString(self):
  """
  ToString(self: StylusButton) -> str
  
   Creates a string representation of the System.Windows.Input.StylusButton.
  """
  pass
 Guid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Guid that represents the stylus button.

Get: Guid(self: StylusButton) -> Guid

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the stylus button.

Get: Name(self: StylusButton) -> str

"""

 StylusButtonState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the state of the stylus button.

Get: StylusButtonState(self: StylusButton) -> StylusButtonState

"""

 StylusDevice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the stylus that this button belongs to.

Get: StylusDevice(self: StylusButton) -> StylusDevice

"""


