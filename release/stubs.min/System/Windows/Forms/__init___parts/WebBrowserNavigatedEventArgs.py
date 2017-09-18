class WebBrowserNavigatedEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.WebBrowser.Navigated event.

 

 WebBrowserNavigatedEventArgs(url: Uri)
 """
 @staticmethod
 def __new__(self,url):
  """ __new__(cls: type,url: Uri) """
  pass
 Url=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the location of the document to which the System.Windows.Forms.WebBrowser control has navigated.



Get: Url(self: WebBrowserNavigatedEventArgs) -> Uri



"""


