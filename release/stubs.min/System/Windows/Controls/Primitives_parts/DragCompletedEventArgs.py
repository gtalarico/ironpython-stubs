class DragCompletedEventArgs(RoutedEventArgs):
 """
 Provides information about the System.Windows.Controls.Primitives.Thumb.DragCompleted event that occurs when a user completes a drag operation with the mouse of a System.Windows.Controls.Primitives.Thumb control.

 

 DragCompletedEventArgs(horizontalChange: float,verticalChange: float,canceled: bool)
 """
 @staticmethod
 def __new__(self,horizontalChange,verticalChange,canceled):
  """ __new__(cls: type,horizontalChange: float,verticalChange: float,canceled: bool) """
  pass
 Canceled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the drag operation for a System.Windows.Controls.Primitives.Thumb was canceled by a call to the System.Windows.Controls.Primitives.Thumb.CancelDrag method.



Get: Canceled(self: DragCompletedEventArgs) -> bool



"""

 HorizontalChange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the horizontal change in position of the System.Windows.Controls.Primitives.Thumb after the user drags the control with the mouse.



Get: HorizontalChange(self: DragCompletedEventArgs) -> float



"""

 VerticalChange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the vertical change in position of the System.Windows.Controls.Primitives.Thumb after the user drags the control with the mouse.



Get: VerticalChange(self: DragCompletedEventArgs) -> float



"""


