class DownloadProgressChangedEventArgs(ProgressChangedEventArgs):
 """ Provides data for the System.Net.WebClient.DownloadProgressChanged event of a System.Net.WebClient. """
 BytesReceived=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of bytes received.



Get: BytesReceived(self: DownloadProgressChangedEventArgs) -> Int64



"""

 TotalBytesToReceive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total number of bytes in a System.Net.WebClient data download operation.



Get: TotalBytesToReceive(self: DownloadProgressChangedEventArgs) -> Int64



"""


