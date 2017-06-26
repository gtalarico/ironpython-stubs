class StylusSystemGestureEventArgs(StylusEventArgs):
 """
 Provides data for the System.Windows.UIElement.StylusSystemGesture event.
 
 StylusSystemGestureEventArgs(stylusDevice: StylusDevice,timestamp: int,systemGesture: SystemGesture)
 """
 @staticmethod
 def __new__(self,stylusDevice,timestamp,systemGesture):
  """ __new__(cls: type,stylusDevice: StylusDevice,timestamp: int,systemGesture: SystemGesture) """
  pass
 SystemGesture=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Input.SystemGesture that raises the event.

Get: SystemGesture(self: StylusSystemGestureEventArgs) -> SystemGesture

"""


