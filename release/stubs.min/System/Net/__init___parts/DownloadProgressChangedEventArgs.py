class DownloadProgressChangedEventArgs(ProgressChangedEventArgs):
 """ Provides data for the System.Net.WebClient.DownloadProgressChanged event of a System.Net.WebClient. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DownloadProgressChangedEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 BytesReceived=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of bytes received.

Get: BytesReceived(self: DownloadProgressChangedEventArgs) -> Int64

"""

 TotalBytesToReceive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total number of bytes in a System.Net.WebClient data download operation.

Get: TotalBytesToReceive(self: DownloadProgressChangedEventArgs) -> Int64

"""


