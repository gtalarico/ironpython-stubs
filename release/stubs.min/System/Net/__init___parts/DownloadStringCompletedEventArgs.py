class DownloadStringCompletedEventArgs(AsyncCompletedEventArgs):
 """ Provides data for the System.Net.WebClient.DownloadStringCompleted event. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DownloadStringCompletedEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the data that is downloaded by a erload:System.Net.WebClient.DownloadStringAsync method.

Get: Result(self: DownloadStringCompletedEventArgs) -> str

"""


