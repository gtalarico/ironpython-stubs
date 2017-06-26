class GiveFeedbackEventArgs(RoutedEventArgs):
    """ Contains arguments for the System.Windows.DragDrop.GiveFeedback event. """
    Effects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the effects of drag-and-drop operation.

Get: Effects(self: GiveFeedbackEventArgs) -> DragDropEffects

"""

    UseDefaultCursors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value indicating whether default cursor feedback behavior should be used for the associated drag-and-drop operation.

Get: UseDefaultCursors(self: GiveFeedbackEventArgs) -> bool

Set: UseDefaultCursors(self: GiveFeedbackEventArgs) = value
"""


