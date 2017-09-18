class DownloadStringCompletedEventArgs(AsyncCompletedEventArgs):
 """ Provides data for the System.Net.WebClient.DownloadStringCompleted event. """
 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the data that is downloaded by a erload:System.Net.WebClient.DownloadStringAsync method.



Get: Result(self: DownloadStringCompletedEventArgs) -> str



"""


