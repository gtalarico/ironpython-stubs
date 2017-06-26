class DragStartedEventArgs(RoutedEventArgs):
    """
    Provides information about the System.Windows.Controls.Primitives.Thumb.DragStarted event that occurs when a user drags a System.Windows.Controls.Primitives.Thumb control with the mouse..
    
    DragStartedEventArgs(horizontalOffset: float, verticalOffset: float)
    """
    @staticmethod # known case of __new__
    def __new__(self, horizontalOffset, verticalOffset):
        """ __new__(cls: type, horizontalOffset: float, verticalOffset: float) """
        pass

    HorizontalOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the horizontal offset of the mouse click relative to the screen coordinates of the System.Windows.Controls.Primitives.Thumb.

Get: HorizontalOffset(self: DragStartedEventArgs) -> float

"""

    VerticalOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the vertical offset of the mouse click relative to the screen coordinates of the System.Windows.Controls.Primitives.Thumb.

Get: VerticalOffset(self: DragStartedEventArgs) -> float

"""


