class ContextMenuEventArgs(RoutedEventArgs):
    """ Provides data for the context menu event. """
    CursorLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the horizontal position of the mouse.

Get: CursorLeft(self: ContextMenuEventArgs) -> float

"""

    CursorTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the vertical position of the mouse.

Get: CursorTop(self: ContextMenuEventArgs) -> float

"""


