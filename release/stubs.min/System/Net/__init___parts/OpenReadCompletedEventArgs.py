class OpenReadCompletedEventArgs(AsyncCompletedEventArgs):
 """ Provides data for the System.Net.WebClient.OpenReadCompleted event. """
 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a readable stream that contains data downloaded by a erload:System.Net.WebClient.DownloadDataAsync method.



Get: Result(self: OpenReadCompletedEventArgs) -> Stream



"""


