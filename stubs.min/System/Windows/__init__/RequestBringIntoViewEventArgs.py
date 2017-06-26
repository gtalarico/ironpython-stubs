class RequestBringIntoViewEventArgs(RoutedEventArgs):
    """ Provides data for the System.Windows.FrameworkElement.RequestBringIntoView�routed event. """
    TargetObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object that should be made visible in response to the event.

Get: TargetObject(self: RequestBringIntoViewEventArgs) -> DependencyObject

"""

    TargetRect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rectangular region in the object's coordinate space which should be made visible.

Get: TargetRect(self: RequestBringIntoViewEventArgs) -> Rect

"""


