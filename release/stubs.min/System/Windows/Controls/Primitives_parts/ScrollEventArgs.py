class ScrollEventArgs(RoutedEventArgs):
 """
 Provides data for a System.Windows.Controls.Primitives.ScrollBar.Scroll event that occurs when the System.Windows.Controls.Primitives.Thumb of a System.Windows.Controls.Primitives.ScrollBar moves.

 

 ScrollEventArgs(scrollEventType: ScrollEventType,newValue: float)
 """
 @staticmethod
 def __new__(self,scrollEventType,newValue):
  """ __new__(cls: type,scrollEventType: ScrollEventType,newValue: float) """
  pass
 NewValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that represents the new location of the System.Windows.Controls.Primitives.Thumb in the System.Windows.Controls.Primitives.ScrollBar.



Get: NewValue(self: ScrollEventArgs) -> float



"""

 ScrollEventType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Controls.Primitives.ScrollEventType enumeration value that describes the change in the System.Windows.Controls.Primitives.Thumb position that caused this event.



Get: ScrollEventType(self: ScrollEventArgs) -> ScrollEventType



"""


