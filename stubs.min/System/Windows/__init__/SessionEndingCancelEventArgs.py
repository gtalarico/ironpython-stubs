class SessionEndingCancelEventArgs(CancelEventArgs):
    """ Contains the event arguments for the System.Windows.Application.SessionEnding event. """
    ReasonSessionEnding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates why the session is ending.

Get: ReasonSessionEnding(self: SessionEndingCancelEventArgs) -> ReasonSessionEnding

"""


