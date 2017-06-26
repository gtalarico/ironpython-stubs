class VisualTransition(DependencyObject):
    """
    Represents the visual behavior that occurs when a control transitions from one state to another.
    
    VisualTransition()
    """
    From = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Windows.VisualState to transition from.

Get: From(self: VisualTransition) -> str

Set: From(self: VisualTransition) = value
"""

    GeneratedDuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the time that it takes to move from one state to another.

Get: GeneratedDuration(self: VisualTransition) -> Duration

Set: GeneratedDuration(self: VisualTransition) = value
"""

    GeneratedEasingFunction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a custom mathematical formula that is used to transition between states.

Get: GeneratedEasingFunction(self: VisualTransition) -> IEasingFunction

Set: GeneratedEasingFunction(self: VisualTransition) = value
"""

    Storyboard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Animation.Storyboard that occurs when the transition occurs.

Get: Storyboard(self: VisualTransition) -> Storyboard

Set: Storyboard(self: VisualTransition) = value
"""

    To = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Windows.VisualState to transition to.

Get: To(self: VisualTransition) -> str

Set: To(self: VisualTransition) = value
"""


