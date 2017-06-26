class InputDevice(DispatcherObject):
 """ Abstract class that describes an input devices. """
 ActiveSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the System.Windows.PresentationSource that is reporting input for this device.

Get: ActiveSource(self: InputDevice) -> PresentationSource

"""

 Target=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the element that receives input from this device.

Get: Target(self: InputDevice) -> IInputElement

"""


