class NavigationFailedEventArgs(EventArgs):
    """ Provides data for the NavigationFailed event. """
    Exception = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Exception that was raised as the result of a failed navigation.

Get: Exception(self: NavigationFailedEventArgs) -> Exception

"""

    ExtraData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the optional data System.Object that was passed when navigation commenced.

Get: ExtraData(self: NavigationFailedEventArgs) -> object

"""

    Handled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the failed navigation exception has been handled.

Get: Handled(self: NavigationFailedEventArgs) -> bool

Set: Handled(self: NavigationFailedEventArgs) = value
"""

    Navigator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The navigator that raised this event.

Get: Navigator(self: NavigationFailedEventArgs) -> object

"""

    Uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the uniform resource identifier (URI) for the content that could not be navigated to.

Get: Uri(self: NavigationFailedEventArgs) -> Uri

"""

    WebRequest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the web request that was used to request the specified content.

Get: WebRequest(self: NavigationFailedEventArgs) -> WebRequest

"""

    WebResponse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the web response that was returned after attempting to download the requested the specified content.

Get: WebResponse(self: NavigationFailedEventArgs) -> WebResponse

"""


