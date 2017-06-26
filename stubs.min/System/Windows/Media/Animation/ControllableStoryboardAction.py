class ControllableStoryboardAction(TriggerAction):
    """ Manipulates a System.Windows.Media.Animation.Storyboard that has been applied by a System.Windows.Media.Animation.BeginStoryboard action. """
    BeginStoryboardName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Animation.BeginStoryboard.Name of the System.Windows.Media.Animation.BeginStoryboard that began the System.Windows.Media.Animation.Storyboard you want to interactively control.

Get: BeginStoryboardName(self: ControllableStoryboardAction) -> str

Set: BeginStoryboardName(self: ControllableStoryboardAction) = value
"""


