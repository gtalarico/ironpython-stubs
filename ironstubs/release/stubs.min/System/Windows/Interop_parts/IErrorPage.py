class IErrorPage:
 """ Defines the interaction between Windows Presentation Foundation (WPF) applications that are hosting interoperation content and interpreted by the Windows Presentation Foundation (WPF) executable,and a host supplied error page. """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 DeploymentPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the path to an application's deployment manifest.

Get: DeploymentPath(self: IErrorPage) -> Uri

Set: DeploymentPath(self: IErrorPage)=value
"""

 ErrorFlag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether this represents an error or some other condition such as a warning. true denotes an error.

Get: ErrorFlag(self: IErrorPage) -> bool

Set: ErrorFlag(self: IErrorPage)=value
"""

 ErrorText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a verbose description of the error.

Get: ErrorText(self: IErrorPage) -> str

Set: ErrorText(self: IErrorPage)=value
"""

 ErrorTitle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the string title of the error page.

Get: ErrorTitle(self: IErrorPage) -> str

Set: ErrorTitle(self: IErrorPage)=value
"""

 GetWinFxCallback=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a reference to a System.Windows.Threading.DispatcherOperationCallback  handler,which can handle requests for Microsoft .NET Framework runtime downloads.

Get: GetWinFxCallback(self: IErrorPage) -> DispatcherOperationCallback

Set: GetWinFxCallback(self: IErrorPage)=value
"""

 LogFilePath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the string path to the error's log file,if any.

Get: LogFilePath(self: IErrorPage) -> str

Set: LogFilePath(self: IErrorPage)=value
"""

 RefreshCallback=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a reference to a System.Windows.Threading.DispatcherOperationCallback handler,that can handle refresh of the error page.

Get: RefreshCallback(self: IErrorPage) -> DispatcherOperationCallback

Set: RefreshCallback(self: IErrorPage)=value
"""

 SupportUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a uniform resource identifier (URI) for support information associated with the error.

Get: SupportUri(self: IErrorPage) -> Uri

Set: SupportUri(self: IErrorPage)=value
"""


