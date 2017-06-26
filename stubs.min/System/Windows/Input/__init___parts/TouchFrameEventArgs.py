class TouchFrameEventArgs(EventArgs):
 """ Provides data for the System.Windows.Input.Touch.FrameReported event. """
 def GetPrimaryTouchPoint(self,relativeTo):
  """
  GetPrimaryTouchPoint(self: TouchFrameEventArgs,relativeTo: IInputElement) -> TouchPoint
  
   Returns the current touch point of the primary touch device relative to the 
    specified element.
  
  
   relativeTo: The element that defines the coordinate space. To use WPF absolute coordinates,
    specify relativeTo as null.
  
   Returns: The current position of the primary System.Windows.Input.TouchDevice relative 
    to the specified element; or null if the primary 
    System.Windows.Input.TouchDevice is not active.
  """
  pass
 def GetTouchPoints(self,relativeTo):
  """
  GetTouchPoints(self: TouchFrameEventArgs,relativeTo: IInputElement) -> TouchPointCollection
  
   Returns a collection that contains the current touch point for each active 
    touch device relative to the specified element.
  
  
   relativeTo: The element that defines the coordinate space. To use WPF absolute coordinates,
    specify relativeTo as null.
  
   Returns: A collection that contains the current System.Windows.Input.TouchPoint for each 
    active System.Windows.Input.TouchDevice.
  """
  pass
 def SuspendMousePromotionUntilTouchUp(self):
  """
  SuspendMousePromotionUntilTouchUp(self: TouchFrameEventArgs)
   This member is not implemented.
  """
  pass
 Timestamp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the time stamp for this event.

Get: Timestamp(self: TouchFrameEventArgs) -> int

"""


