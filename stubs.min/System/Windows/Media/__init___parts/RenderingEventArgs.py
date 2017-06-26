class RenderingEventArgs(EventArgs):
    """ Required arguments for the System.Windows.Media.CompositionTarget.Rendering event. """
    RenderingTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the estimated target time at which the next frame of an animation will be rendered.

Get: RenderingTime(self: RenderingEventArgs) -> TimeSpan

"""


