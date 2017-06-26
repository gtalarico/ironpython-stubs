class StartupEventArgs(EventArgs):
    """ Contains the arguments for the System.Windows.Application.Startup event. """
    Args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets command line arguments that were passed to the application from either the command prompt or the desktop.

Get: Args(self: StartupEventArgs) -> Array[str]

"""


