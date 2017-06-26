class SeekStoryboard(ControllableStoryboardAction):
    """
    A trigger action that provides functionality for seeking (skipping) to a specified time within the active period of a System.Windows.Media.Animation.Storyboard.
    
    SeekStoryboard()
    """
    def ShouldSerializeOffset(self):
        """
        ShouldSerializeOffset(self: SeekStoryboard) -> bool
        
            Returns a value that indicates whether the System.Windows.Media.Animation.SeekStoryboard.Offset property of this System.Windows.Media.Animation.SeekStoryboard should be serialized.
            Returns: true if the System.Windows.Media.Animation.SeekStoryboard.Offset property of this System.Windows.Media.Animation.SeekStoryboard should be serialized; otherwise, false.
        """
        pass

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount by which the storyboard should move forward or backward from the seek origin System.Windows.Media.Animation.SeekStoryboard.Origin. .

Get: Offset(self: SeekStoryboard) -> TimeSpan

Set: Offset(self: SeekStoryboard) = value
"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the position from which this seek operation's System.Windows.Media.Animation.SeekStoryboard.Offset is applied.

Get: Origin(self: SeekStoryboard) -> TimeSeekOrigin

Set: Origin(self: SeekStoryboard) = value
"""


