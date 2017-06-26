class StylusButtonEventArgs(StylusEventArgs):
 """
 Provides data for the System.Windows.UIElement.StylusButtonDown and System.Windows.UIElement.StylusButtonUp events.
 
 StylusButtonEventArgs(stylusDevice: StylusDevice,timestamp: int,button: StylusButton)
 """
 @staticmethod
 def __new__(self,stylusDevice,timestamp,button):
  """ __new__(cls: type,stylusDevice: StylusDevice,timestamp: int,button: StylusButton) """
  pass
 StylusButton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Input.StylusButton that raises this event.

Get: StylusButton(self: StylusButtonEventArgs) -> StylusButton

"""


