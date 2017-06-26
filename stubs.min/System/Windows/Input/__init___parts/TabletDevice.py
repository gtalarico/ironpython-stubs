class TabletDevice(InputDevice):
 """ Represents the digitizer device of a Tablet PC. """
 def ToString(self):
  """
  ToString(self: TabletDevice) -> str
  
   Returns the name of the tablet device.
   Returns: A System.String that contains the name of the System.Windows.Input.TabletDevice.
  """
  pass
 ActiveSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.PresentationSource that reports current input for the tablet device.

Get: ActiveSource(self: TabletDevice) -> PresentationSource

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unique identifier for the tablet device on the system.

Get: Id(self: TabletDevice) -> int

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the tablet device.

Get: Name(self: TabletDevice) -> str

"""

 ProductId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the product identifier for the tablet device.

Get: ProductId(self: TabletDevice) -> str

"""

 StylusDevices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Input.StylusDeviceCollection associated with the tablet device.

Get: StylusDevices(self: TabletDevice) -> StylusDeviceCollection

"""

 SupportedStylusPointProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of System.Windows.Input.StylusPointProperty objects that the System.Windows.Input.TabletDevice supports.

Get: SupportedStylusPointProperties(self: TabletDevice) -> ReadOnlyCollection[StylusPointProperty]

"""

 TabletHardwareCapabilities=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Input.TabletHardwareCapabilities for the tablet device.

Get: TabletHardwareCapabilities(self: TabletDevice) -> TabletHardwareCapabilities

"""

 Target=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.IInputElement that provides basic input processing for the tablet device.

Get: Target(self: TabletDevice) -> IInputElement

"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Input.TabletDeviceType of the tablet device.

Get: Type(self: TabletDevice) -> TabletDeviceType

"""


