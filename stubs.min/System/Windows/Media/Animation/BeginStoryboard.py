class BeginStoryboard(TriggerAction):
    """
    A trigger action that begins a System.Windows.Media.Animation.Storyboard and distributes its animations to their targeted objects and properties.
    
    BeginStoryboard()
    """
    HandoffBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the proper hand-off behavior to start an animation clock in this storyboard

Get: HandoffBehavior(self: BeginStoryboard) -> HandoffBehavior

Set: HandoffBehavior(self: BeginStoryboard) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Windows.Media.Animation.BeginStoryboard object. By naming the System.Windows.Media.Animation.BeginStoryboard object, the System.Windows.Media.Animation.Storyboard can be controlled after it is started.

Get: Name(self: BeginStoryboard) -> str

Set: Name(self: BeginStoryboard) = value
"""

    Storyboard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Animation.Storyboard that this System.Windows.Media.Animation.BeginStoryboard starts.

Get: Storyboard(self: BeginStoryboard) -> Storyboard

Set: Storyboard(self: BeginStoryboard) = value
"""


    StoryboardProperty = None

