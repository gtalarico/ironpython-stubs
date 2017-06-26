class NavigationProgressEventArgs(EventArgs):
    """ Provides data for the System.Windows.Application.NavigationProgress and System.Windows.Navigation.NavigationWindow.NavigationProgress events. """
    BytesRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of bytes that have been read.

Get: BytesRead(self: NavigationProgressEventArgs) -> Int64

"""

    MaxBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum number of bytes.

Get: MaxBytes(self: NavigationProgressEventArgs) -> Int64

"""

    Navigator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the navigator that raised the event

Get: Navigator(self: NavigationProgressEventArgs) -> object

"""

    Uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the uniform resource identifier (URI) of the target page.

Get: Uri(self: NavigationProgressEventArgs) -> Uri

"""


