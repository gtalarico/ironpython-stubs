class NavigationEventArgs(EventArgs):
 """ Provides data for non-cancelable navigation events,including System.Windows.Navigation.NavigationWindow.LoadCompleted,System.Windows.Navigation.NavigationWindow.Navigated,and System.Windows.Navigation.NavigationWindow.NavigationStopped. """
 Content=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the root node of the target page's content.

Get: Content(self: NavigationEventArgs) -> object

"""

 ExtraData=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an optional user-defined data object.

Get: ExtraData(self: NavigationEventArgs) -> object

"""

 IsNavigationInitiator=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the current navigator initiated the navigation.

Get: IsNavigationInitiator(self: NavigationEventArgs) -> bool

"""

 Navigator=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the navigator that raised the event

Get: Navigator(self: NavigationEventArgs) -> object

"""

 Uri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the uniform resource identifier (URI)�of the target page.

Get: Uri(self: NavigationEventArgs) -> Uri

"""

 WebResponse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Web response to allow access to HTTP headers and other properties.

Get: WebResponse(self: NavigationEventArgs) -> WebResponse

"""


