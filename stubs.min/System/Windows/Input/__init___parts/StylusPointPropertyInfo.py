class StylusPointPropertyInfo(StylusPointProperty):
 """
 Specifies the constraints of a property in a System.Windows.Input.StylusPoint.
 
 StylusPointPropertyInfo(stylusPointProperty: StylusPointProperty)
 StylusPointPropertyInfo(stylusPointProperty: StylusPointProperty,minimum: int,maximum: int,unit: StylusPointPropertyUnit,resolution: Single)
 """
 @staticmethod
 def __new__(self,stylusPointProperty,minimum=None,maximum=None,unit=None,resolution=None):
  """
  __new__(cls: type,stylusPointProperty: StylusPointProperty)
  __new__(cls: type,stylusPointProperty: StylusPointProperty,minimum: int,maximum: int,unit: StylusPointPropertyUnit,resolution: Single)
  """
  pass
 Maximum=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the maximum value accepted for the System.Windows.Input.StylusPoint property.

Get: Maximum(self: StylusPointPropertyInfo) -> int

"""

 Minimum=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the minimum value accepted for the System.Windows.Input.StylusPoint property.

Get: Minimum(self: StylusPointPropertyInfo) -> int

"""

 Resolution=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the scale that converts a System.Windows.Input.StylusPoint property value into units.

Get: Resolution(self: StylusPointPropertyInfo) -> Single

"""

 Unit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of measurement that is used by System.Windows.Input.StylusPoint property.

Get: Unit(self: StylusPointPropertyInfo) -> StylusPointPropertyUnit

"""


