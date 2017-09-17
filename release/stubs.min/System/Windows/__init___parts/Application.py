class Application(DispatcherObject,IHaveResources,IQueryAmbient):
 """
 Encapsulates a Windows Presentation Foundation (WPF) application.
 
 Application()
 """
 def FindResource(self,resourceKey):
  """
  FindResource(self: Application,resourceKey: object) -> object
  
   Searches for a user interface (UI) resource,such as a System.Windows.Style or 
    System.Windows.Media.Brush,with the specified key,and throws an exception if 
    the requested resource is not found (see Resources Overview).
  
  
   resourceKey: The name of the resource to find.
   Returns: The requested resource object. If the requested resource is not found,a 
    System.Windows.ResourceReferenceKeyNotFoundException is thrown.
  """
  pass
 @staticmethod
 def GetContentStream(uriContent):
  """
  GetContentStream(uriContent: Uri) -> StreamResourceInfo
  
   Returns a resource stream for a content data file that is located at the 
    specified System.Uri (see WPF Application Resource,Content,and Data Files).
  
  
   uriContent: The relative System.Uri that maps to a loose resource.
   Returns: A System.Windows.Resources.StreamResourceInfo that contains a content data file 
    that is located at the specified System.Uri. If a loose resource is not found,
    null is returned.
  """
  pass
 @staticmethod
 def GetCookie(uri):
  """
  GetCookie(uri: Uri) -> str
  
   Retrieves a cookie for the location specified by a System.Uri.
  
   uri: The System.Uri that specifies the location for which a cookie was created.
   Returns: A System.String value,if the cookie exists; otherwise,a 
    System.ComponentModel.Win32Exception is thrown.
  """
  pass
 @staticmethod
 def GetRemoteStream(uriRemote):
  """
  GetRemoteStream(uriRemote: Uri) -> StreamResourceInfo
  
   Returns a resource stream for a site-of-origin data file that is located at the 
    specified System.Uri (see WPF Application Resource,Content,and Data Files).
  
  
   uriRemote: The System.Uri that maps to a loose resource at the site of origin.
   Returns: A System.Windows.Resources.StreamResourceInfo that contains a resource stream 
    for a site-of-origin data file that is located at the specified System.Uri. If 
    the loose resource is not found,null is returned.
  """
  pass
 @staticmethod
 def GetResourceStream(uriResource):
  """
  GetResourceStream(uriResource: Uri) -> StreamResourceInfo
  
   Returns a resource stream for a resource data file that is located at the 
    specified System.Uri (see WPF Application Resource,Content,and Data Files).
  
  
   uriResource: The System.Uri that maps to an embedded resource.
   Returns: A System.Windows.Resources.StreamResourceInfo that contains a resource stream 
    for resource data file that is located at the specified System.Uri.
  """
  pass
 @staticmethod
 def LoadComponent(*__args):
  """
  LoadComponent(resourceLocator: Uri) -> object
  
   Loads a XAML file that is located at the specified uniform resource identifier 
    (URI),and converts it to an instance of the object that is specified by the 
    root element of the XAML file.
  
  
   resourceLocator: A System.Uri that maps to a relative XAML file.
   Returns: An instance of the root element specified by the XAML file loaded.
  LoadComponent(component: object,resourceLocator: Uri)
   Loads a XAML file that is located at the specified uniform resource identifier 
    (URI) and converts it to an instance of the object that is specified by the 
    root element of the XAML file.
  
  
   component: An object of the same type as the root element of the XAML file.
   resourceLocator: A System.Uri that maps to a relative XAML file.
  """
  pass
 def OnActivated(self,*args):
  """
  OnActivated(self: Application,e: EventArgs)
   Raises the System.Windows.Application.Activated event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnDeactivated(self,*args):
  """
  OnDeactivated(self: Application,e: EventArgs)
   Raises the System.Windows.Application.Deactivated event.
  
   e: An System.EventArgs that contains the event data.
  """
  pass
 def OnExit(self,*args):
  """
  OnExit(self: Application,e: ExitEventArgs)
   Raises the System.Windows.Application.Exit event.
  
   e: An System.Windows.ExitEventArgs that contains the event data.
  """
  pass
 def OnFragmentNavigation(self,*args):
  """
  OnFragmentNavigation(self: Application,e: FragmentNavigationEventArgs)
   Raises the System.Windows.Application.FragmentNavigation event.
  
   e: A System.Windows.Navigation.FragmentNavigationEventArgs that contains the event 
    data.
  """
  pass
 def OnLoadCompleted(self,*args):
  """
  OnLoadCompleted(self: Application,e: NavigationEventArgs)
   Raises the System.Windows.Application.LoadCompleted event.
  
   e: A System.Windows.Navigation.NavigationEventArgs that contains the event data.
  """
  pass
 def OnNavigated(self,*args):
  """
  OnNavigated(self: Application,e: NavigationEventArgs)
   Raises the System.Windows.Application.Navigated event.
  
   e: A System.Windows.Navigation.NavigationEventArgs that contains the event data.
  """
  pass
 def OnNavigating(self,*args):
  """
  OnNavigating(self: Application,e: NavigatingCancelEventArgs)
   Raises the System.Windows.Application.Navigating event.
  
   e: A System.Windows.Navigation.NavigatingCancelEventArgs that contains the event 
    data.
  """
  pass
 def OnNavigationFailed(self,*args):
  """
  OnNavigationFailed(self: Application,e: NavigationFailedEventArgs)
   Raises the System.Windows.Application.NavigationFailed event.
  
   e: A System.Windows.Navigation.NavigationFailedEventArgs that contains the event 
    data.
  """
  pass
 def OnNavigationProgress(self,*args):
  """
  OnNavigationProgress(self: Application,e: NavigationProgressEventArgs)
   Raises the System.Windows.Application.NavigationProgress event.
  
   e: A System.Windows.Navigation.NavigationProgressEventArgs that contains the event 
    data.
  """
  pass
 def OnNavigationStopped(self,*args):
  """
  OnNavigationStopped(self: Application,e: NavigationEventArgs)
   Raises the System.Windows.Application.NavigationStopped event.
  
   e: A System.Windows.Navigation.NavigationEventArgs that contains the event data.
  """
  pass
 def OnSessionEnding(self,*args):
  """
  OnSessionEnding(self: Application,e: SessionEndingCancelEventArgs)
   Raises the System.Windows.Application.SessionEnding event.
  
   e: A System.Windows.SessionEndingCancelEventArgs that contains the event data.
  """
  pass
 def OnStartup(self,*args):
  """
  OnStartup(self: Application,e: StartupEventArgs)
   Raises the System.Windows.Application.Startup event.
  
   e: A System.Windows.StartupEventArgs that contains the event data.
  """
  pass
 def Run(self,window=None):
  """
  Run(self: Application,window: Window) -> int
  
   Starts a Windows Presentation Foundation (WPF) application and opens the 
    specified window.
  
  
   window: A System.Windows.Window that opens automatically when an application starts.
   Returns: The System.Int32 application exit code that is returned to the operating system 
    when the application shuts down. By default,the exit code value is 0.
  
  Run(self: Application) -> int
  
   Starts a Windows Presentation Foundation (WPF) application.
   Returns: The System.Int32 application exit code that is returned to the operating system 
    when the application shuts down. By default,the exit code value is 0.
  """
  pass
 @staticmethod
 def SetCookie(uri,value):
  """
  SetCookie(uri: Uri,value: str)
   Creates a cookie for the location specified by a System.Uri.
  
   uri: The System.Uri that specifies the location for which the cookie should be 
    created.
  
   value: The System.String that contains the cookie data.
  """
  pass
 def Shutdown(self,exitCode=None):
  """
  Shutdown(self: Application,exitCode: int)
   Shuts down an application that returns the specified exit code to the operating 
    system.
  
  
   exitCode: An integer exit code for an application. The default exit code is 0.
  Shutdown(self: Application)
   Shuts down an application.
  """
  pass
 def TryFindResource(self,resourceKey):
  """
  TryFindResource(self: Application,resourceKey: object) -> object
  
   Searches for the specified resource.
  
   resourceKey: The name of the resource to find.
   Returns: The requested resource object. If the requested resource is not found,a null 
    reference is returned.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 MainWindow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the main window of the application.

Get: MainWindow(self: Application) -> Window

Set: MainWindow(self: Application)=value
"""

 Properties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of application-scope properties.

Get: Properties(self: Application) -> IDictionary

"""

 Resources=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a collection of application-scope resources,such as styles and brushes.

Get: Resources(self: Application) -> ResourceDictionary

Set: Resources(self: Application)=value
"""

 ShutdownMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the condition that causes the System.Windows.Application.Shutdown method to be called.

Get: ShutdownMode(self: Application) -> ShutdownMode

Set: ShutdownMode(self: Application)=value
"""

 StartupUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a UI that is automatically shown when an application starts.

Get: StartupUri(self: Application) -> Uri

Set: StartupUri(self: Application)=value
"""

 Windows=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the instantiated windows in an application.

Get: Windows(self: Application) -> WindowCollection

"""


 Activated=None
 Current=None
 Deactivated=None
 DispatcherUnhandledException=None
 Exit=None
 FragmentNavigation=None
 LoadCompleted=None
 Navigated=None
 Navigating=None
 NavigationFailed=None
 NavigationProgress=None
 NavigationStopped=None
 ResourceAssembly=None
 SessionEnding=None
 Startup=None

