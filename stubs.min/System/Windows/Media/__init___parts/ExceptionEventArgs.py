class ExceptionEventArgs(EventArgs):
    """ Provides error exception data for media events. """
    ErrorException = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the exception that details the cause of the failure.

Get: ErrorException(self: ExceptionEventArgs) -> Exception

"""


