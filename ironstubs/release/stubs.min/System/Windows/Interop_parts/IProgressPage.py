class IProgressPage:
 """ Defines the interaction between Windows Presentation Foundation (WPF) applications that are hosting interoperation content,and a host supplied progress page. """
 def UpdateProgress(self,bytesDownloaded,bytesTotal):
  """
  UpdateProgress(self: IProgressPage,bytesDownloaded: Int64,bytesTotal: Int64)
   Provides upload progress numeric information that can be used to update the 
    progress indicators.
  
  
   bytesDownloaded: Total bytes downloaded thus far.
   bytesTotal: Total bytes that need to be downloaded for the application.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 ApplicationName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets  the application's name.

Get: ApplicationName(self: IProgressPage) -> str

Set: ApplicationName(self: IProgressPage)=value
"""

 DeploymentPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Uri path to the application deployment manifest.

Get: DeploymentPath(self: IProgressPage) -> Uri

Set: DeploymentPath(self: IProgressPage)=value
"""

 PublisherName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the application's publisher.

Get: PublisherName(self: IProgressPage) -> str

Set: PublisherName(self: IProgressPage)=value
"""

 RefreshCallback=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a reference to a System.Windows.Threading.DispatcherOperationCallback handler,that can handle the case of a user-initiated Refresh command.

Get: RefreshCallback(self: IProgressPage) -> DispatcherOperationCallback

Set: RefreshCallback(self: IProgressPage)=value
"""

 StopCallback=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a reference to a System.Windows.Threading.DispatcherOperationCallback handler,that can handle the case of a user-initiated Stop command.

Get: StopCallback(self: IProgressPage) -> DispatcherOperationCallback

Set: StopCallback(self: IProgressPage)=value
"""


