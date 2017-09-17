class StylusPointProperty(object):
 """
 Represents a property stored in a System.Windows.Input.StylusPoint.
 
 StylusPointProperty(identifier: Guid,isButton: bool)
 """
 def ToString(self):
  """ ToString(self: StylusPointProperty) -> str """
  pass
 @staticmethod
 def __new__(self,identifier,isButton):
  """
  __new__(cls: type,identifier: Guid,isButton: bool)
  __new__(cls: type,stylusPointProperty: StylusPointProperty)
  """
  pass
 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the GUID for the current System.Windows.Input.StylusPointProperty.

Get: Id(self: StylusPointProperty) -> Guid

"""

 IsButton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the System.Windows.Input.StylusPointProperty represents a button on the stylus.

Get: IsButton(self: StylusPointProperty) -> bool

"""


