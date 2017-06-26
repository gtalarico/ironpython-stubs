class RequestNavigateEventArgs(RoutedEventArgs):
 """
 Provides data for the System.Windows.Documents.Hyperlink.RequestNavigate event.
 
 RequestNavigateEventArgs(uri: Uri,target: str)
 """
 @staticmethod
 def __new__(self,uri,target):
  """
  __new__(cls: type)
  __new__(cls: type,uri: Uri,target: str)
  """
  pass
 Target=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The navigator that will host the content that is navigated to.

Get: Target(self: RequestNavigateEventArgs) -> str

"""

 Uri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The uniform resource identifier (URI) for the content that is being navigated to.

Get: Uri(self: RequestNavigateEventArgs) -> Uri

"""


