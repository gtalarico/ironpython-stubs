class SizeChangedEventArgs(RoutedEventArgs):
    """ Provides data related to the System.Windows.FrameworkElement.SizeChanged event. """
    HeightChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.FrameworkElement.Height component of the size changed.

Get: HeightChanged(self: SizeChangedEventArgs) -> bool

"""

    NewSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the new System.Windows.Size of the object.

Get: NewSize(self: SizeChangedEventArgs) -> Size

"""

    PreviousSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the previous System.Windows.Size of the object.

Get: PreviousSize(self: SizeChangedEventArgs) -> Size

"""

    WidthChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.FrameworkElement.Width component of the size changed.

Get: WidthChanged(self: SizeChangedEventArgs) -> bool

"""


