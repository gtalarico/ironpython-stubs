class TouchPoint(object,IEquatable[TouchPoint]):
 """
 Represents a single touch point from a multitouch message source.
 
 TouchPoint(device: TouchDevice,position: Point,bounds: Rect,action: TouchAction)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,device,position,bounds,action):
  """ __new__(cls: type,device: TouchDevice,position: Point,bounds: Rect,action: TouchAction) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Action=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the last action that occurred at this location.

Get: Action(self: TouchPoint) -> TouchAction

"""

 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bounds of the area that the finger has in contact with the screen.

Get: Bounds(self: TouchPoint) -> Rect

"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the location of the touch point.

Get: Position(self: TouchPoint) -> Point

"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size of the System.Windows.Input.TouchPoint.Bounds property.

Get: Size(self: TouchPoint) -> Size

"""

 TouchDevice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the touch device that generated this System.Windows.Input.TouchPoint.

Get: TouchDevice(self: TouchPoint) -> TouchDevice

"""


