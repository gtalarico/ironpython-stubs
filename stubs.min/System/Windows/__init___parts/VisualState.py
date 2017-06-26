class VisualState(DependencyObject):
    """
    Represents the visual appearance of the control when it is in a specific state.
    
    VisualState()
    """
    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Windows.VisualState.

Get: Name(self: VisualState) -> str

Set: Name(self: VisualState) = value
"""

    Storyboard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Windows.Media.Animation.Storyboard that defines the appearance of the control when it is in the state that is represented by the System.Windows.VisualState.

Get: Storyboard(self: VisualState) -> Storyboard

Set: Storyboard(self: VisualState) = value
"""


