class MouseEventArgs(InputEventArgs):
 """
 Provides data for mouse related routed events that do not specifically involve mouse buttons or the mouse wheel,for example System.Windows.UIElement.MouseMove.
 
 MouseEventArgs(mouse: MouseDevice,timestamp: int)
 MouseEventArgs(mouse: MouseDevice,timestamp: int,stylusDevice: StylusDevice)
 """
 def GetPosition(self,relativeTo):
  """
  GetPosition(self: MouseEventArgs,relativeTo: IInputElement) -> Point
  
   Returns the position of the mouse pointer relative to the specified element.
  
   relativeTo: The element to use as the frame of reference for calculating the position of 
    the mouse pointer.
  
   Returns: The x- and y-coordinates of the mouse pointer position relative to the 
    specified object.
  """
  pass
 @staticmethod
 def __new__(self,mouse,timestamp,stylusDevice=None):
  """
  __new__(cls: type,mouse: MouseDevice,timestamp: int)
  __new__(cls: type,mouse: MouseDevice,timestamp: int,stylusDevice: StylusDevice)
  """
  pass
 LeftButton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current state of the left mouse button.

Get: LeftButton(self: MouseEventArgs) -> MouseButtonState

"""

 MiddleButton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current state of the middle mouse button.

Get: MiddleButton(self: MouseEventArgs) -> MouseButtonState

"""

 MouseDevice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the mouse device associated with this event.

Get: MouseDevice(self: MouseEventArgs) -> MouseDevice

"""

 RightButton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current state of the right mouse button.

Get: RightButton(self: MouseEventArgs) -> MouseButtonState

"""

 StylusDevice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the stylus device associated with this event.

Get: StylusDevice(self: MouseEventArgs) -> StylusDevice

"""

 XButton1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current state of the first extended mouse button.

Get: XButton1(self: MouseEventArgs) -> MouseButtonState

"""

 XButton2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the state of the second extended mouse button.

Get: XButton2(self: MouseEventArgs) -> MouseButtonState

"""


