class WebBrowserNavigatingEventArgs(CancelEventArgs):
 """
 Provides data for the System.Windows.Forms.WebBrowser.Navigating event.

 

 WebBrowserNavigatingEventArgs(url: Uri,targetFrameName: str)
 """
 @staticmethod
 def __new__(self,url,targetFrameName):
  """ __new__(cls: type,url: Uri,targetFrameName: str) """
  pass
 TargetFrameName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the Web page frame in which the new document will be loaded.



Get: TargetFrameName(self: WebBrowserNavigatingEventArgs) -> str



"""

 Url=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the location of the document to which the System.Windows.Forms.WebBrowser control is navigating.



Get: Url(self: WebBrowserNavigatingEventArgs) -> Uri



"""


