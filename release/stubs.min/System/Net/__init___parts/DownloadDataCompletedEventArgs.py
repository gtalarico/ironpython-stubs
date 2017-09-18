class DownloadDataCompletedEventArgs(AsyncCompletedEventArgs):
 """ Provides data for the System.Net.WebClient.DownloadDataCompleted event. """
 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the data that is downloaded by a erload:System.Net.WebClient.DownloadDataAsync method.



Get: Result(self: DownloadDataCompletedEventArgs) -> Array[Byte]



"""


