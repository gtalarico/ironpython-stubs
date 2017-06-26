class StylusDownEventArgs(StylusEventArgs):
 """
 Provides data for the System.Windows.UIElement.StylusDown event.
 
 StylusDownEventArgs(stylusDevice: StylusDevice,timestamp: int)
 """
 @staticmethod
 def __new__(self,stylusDevice,timestamp):
  """ __new__(cls: type,stylusDevice: StylusDevice,timestamp: int) """
  pass
 TapCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of times the tablet pen was tapped.

Get: TapCount(self: StylusDownEventArgs) -> int

"""


