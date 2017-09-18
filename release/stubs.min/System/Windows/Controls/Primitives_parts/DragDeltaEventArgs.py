class DragDeltaEventArgs(RoutedEventArgs):
 """
 Provides information about the System.Windows.Controls.Primitives.Thumb.DragDelta event that occurs one or more times when a user drags a System.Windows.Controls.Primitives.Thumb control with the mouse.

 

 DragDeltaEventArgs(horizontalChange: float,verticalChange: float)
 """
 @staticmethod
 def __new__(self,horizontalChange,verticalChange):
  """ __new__(cls: type,horizontalChange: float,verticalChange: float) """
  pass
 HorizontalChange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the horizontal distance that the mouse has moved since the previous System.Windows.Controls.Primitives.Thumb.DragDelta event when the user drags the System.Windows.Controls.Primitives.Thumb control with the mouse.



Get: HorizontalChange(self: DragDeltaEventArgs) -> float



"""

 VerticalChange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the vertical distance that the mouse has moved since the previous System.Windows.Controls.Primitives.Thumb.DragDelta event when the user drags the System.Windows.Controls.Primitives.Thumb with the mouse.



Get: VerticalChange(self: DragDeltaEventArgs) -> float



"""


