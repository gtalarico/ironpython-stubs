class QueryContinueDragEventArgs(RoutedEventArgs):
    """ Contains arguments for the System.Windows.DragDrop.QueryContinueDrag event. """
    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current status of the associated drag-and-drop operation.

Get: Action(self: QueryContinueDragEventArgs) -> DragAction

Set: Action(self: QueryContinueDragEventArgs) = value
"""

    EscapePressed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value indicating whether the ESC key has been pressed.

Get: EscapePressed(self: QueryContinueDragEventArgs) -> bool

"""

    KeyStates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag enumeration indicating the current state of the SHIFT, CTRL, and ALT keys, as well as the state of the mouse buttons.

Get: KeyStates(self: QueryContinueDragEventArgs) -> DragDropKeyStates

"""


