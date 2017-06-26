class NavigatingCancelEventArgs(CancelEventArgs):
 """ Provides data for the Navigating event. """
 Content=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a reference to the content object that is being navigated to.

Get: Content(self: NavigatingCancelEventArgs) -> object

"""

 ContentStateToSave=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the System.Windows.Navigation.CustomContentState object that is associated with the back navigation history entry for the page being navigated from.

Get: ContentStateToSave(self: NavigatingCancelEventArgs) -> CustomContentState

Set: ContentStateToSave(self: NavigatingCancelEventArgs)=value
"""

 ExtraData=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the optional data System.Object that was passed when navigation started.

Get: ExtraData(self: NavigatingCancelEventArgs) -> object

"""

 IsNavigationInitiator=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the navigator (System.Windows.Navigation.NavigationWindow,System.Windows.Controls.Frame) that is specified by System.Windows.Navigation.NavigatingCancelEventArgs.Navigator is servicing this navigation,or whether a parent navigator is doing so.

Get: IsNavigationInitiator(self: NavigatingCancelEventArgs) -> bool

"""

 NavigationMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Windows.Navigation.NavigationMode value that indicates the type of navigation that is occurring.

Get: NavigationMode(self: NavigatingCancelEventArgs) -> NavigationMode

"""

 Navigator=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The navigator that raised this event.

Get: Navigator(self: NavigatingCancelEventArgs) -> object

"""

 TargetContentState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Navigation.CustomContentState object that is to be applied to the content being navigated to.

Get: TargetContentState(self: NavigatingCancelEventArgs) -> CustomContentState

"""

 Uri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the uniform resource identifier (URI) for the content being navigated to.

Get: Uri(self: NavigatingCancelEventArgs) -> Uri

"""

 WebRequest=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Net.WebRequest object that is used to request the specified content.

Get: WebRequest(self: NavigatingCancelEventArgs) -> WebRequest

"""


