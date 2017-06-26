class NavigationService(object,IContentContainer):
 """ Contains methods,properties,and events to support navigation. """
 def AddBackEntry(self,state):
  """
  AddBackEntry(self: NavigationService,state: CustomContentState)
   Adds an entry to back navigation history that contains a 
    System.Windows.Navigation.CustomContentState object.
  
  
   state: A System.Windows.Navigation.CustomContentState object that represents 
    application-defined state that is associated with a specific piece of content.
  """
  pass
 @staticmethod
 def GetNavigationService(dependencyObject):
  """
  GetNavigationService(dependencyObject: DependencyObject) -> NavigationService
  
   Gets a reference to the System.Windows.Navigation.NavigationService for the 
    navigator whose content contains the specified System.Windows.DependencyObject.
  
  
   dependencyObject: The System.Windows.DependencyObject in content that is hosted by a navigator.
   Returns: A reference to the System.Windows.Navigation.NavigationService for the 
    navigator whose content contains the specified System.Windows.DependencyObject; 
    can be null in some cases (see Remarks).
  """
  pass
 def GoBack(self):
  """
  GoBack(self: NavigationService)
   Navigates to the most recent entry in back navigation history,if there is one.
  """
  pass
 def GoForward(self):
  """
  GoForward(self: NavigationService)
   Navigate to the most recent entry in forward navigation history,if there is 
    one.
  """
  pass
 def Navigate(self,*__args):
  """
  Navigate(self: NavigationService,source: Uri,navigationState: object,sandboxExternalContent: bool) -> bool
  
   Navigate asynchronously to source content located at a uniform resource 
    identifier (URI),pass an object containing navigation state for processing 
    during navigation,and sandbox the content.
  
  
   source: A System.Uri object initialized with the URI for the desired content.
   navigationState: An object that contains data to be used for processing during navigation.
   sandboxExternalContent: Download content into a partial trust security sandbox (with the default 
    Internet zone set of permissions,if true. The default is false.
  
   Returns: true if a navigation is not canceled; otherwise,false.
  Navigate(self: NavigationService,root: object,navigationState: object) -> bool
  
   Navigate asynchronously to content that is contained by an object,and pass an 
    object that contains data to be used for processing during navigation.
  
  
   root: An object that contains the content to navigate to.
   navigationState: An object that contains data to be used for processing during navigation.
   Returns: true if a navigation is not canceled; otherwise,false.
  Navigate(self: NavigationService,source: Uri,navigationState: object) -> bool
  
   Navigate asynchronously to source content located at a uniform resource 
    identifier (URI),and pass an object that contains data to be used for 
    processing during navigation.
  
  
   source: A System.Uri object initialized with the URI for the desired content.
   navigationState: An object that contains data to be used for processing during navigation.
   Returns: true if a navigation is not canceled; otherwise,false.
  Navigate(self: NavigationService,source: Uri) -> bool
  
   Navigate asynchronously to content that is specified by a uniform resource 
    identifier (URI).
  
  
   source: A System.Uri object initialized with the URI for the desired content.
   Returns: true if a navigation is not canceled; otherwise,false.
  Navigate(self: NavigationService,root: object) -> bool
  
   Navigate asynchronously to content that is contained by an object.
  
   root: An object that contains the content to navigate to.
   Returns: true if a navigation is not canceled; otherwise,false.
  """
  pass
 def Refresh(self):
  """
  Refresh(self: NavigationService)
   Reloads the current content.
  """
  pass
 def RemoveBackEntry(self):
  """
  RemoveBackEntry(self: NavigationService) -> JournalEntry
  
   Removes the most recent journal entry from back history.
   Returns: The most recent System.Windows.Navigation.JournalEntry in back navigation 
    history,if there is one.
  """
  pass
 def StopLoading(self):
  """
  StopLoading(self: NavigationService)
   Stops further downloading of content for the current navigation request.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CanGoBack=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether there is at least one entry in back navigation history.

Get: CanGoBack(self: NavigationService) -> bool

"""

 CanGoForward=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether there is at least one entry in forward navigation history.

Get: CanGoForward(self: NavigationService) -> bool

"""

 Content=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a reference to the object that contains the current content.

Get: Content(self: NavigationService) -> object

Set: Content(self: NavigationService)=value
"""

 CurrentSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the uniform resource identifier (URI) of the content that was last navigated to.

Get: CurrentSource(self: NavigationService) -> Uri

"""

 Source=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the uniform resource identifier (URI) of the current content,or the URI of new content that is currently being navigated to.

Get: Source(self: NavigationService) -> Uri

Set: Source(self: NavigationService)=value
"""


 FragmentNavigation=None
 LoadCompleted=None
 Navigated=None
 Navigating=None
 NavigationFailed=None
 NavigationProgress=None
 NavigationStopped=None

