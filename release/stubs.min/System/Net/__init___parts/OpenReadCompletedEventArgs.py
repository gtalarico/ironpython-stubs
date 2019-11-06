class OpenReadCompletedEventArgs(AsyncCompletedEventArgs):
 """ Provides data for the System.Net.WebClient.OpenReadCompleted event. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return OpenReadCompletedEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a readable stream that contains data downloaded by a erload:System.Net.WebClient.DownloadDataAsync method.

Get: Result(self: OpenReadCompletedEventArgs) -> Stream

"""


