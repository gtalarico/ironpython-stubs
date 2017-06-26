class MouseWheelEventArgs(MouseEventArgs):
 """
 Provides data for various events that report changes to the mouse wheel delta value of a mouse device.
 
 MouseWheelEventArgs(mouse: MouseDevice,timestamp: int,delta: int)
 """
 @staticmethod
 def __new__(self,mouse,timestamp,delta):
  """ __new__(cls: type,mouse: MouseDevice,timestamp: int,delta: int) """
  pass
 Delta=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates the amount that the mouse wheel has changed.

Get: Delta(self: MouseWheelEventArgs) -> int

"""


