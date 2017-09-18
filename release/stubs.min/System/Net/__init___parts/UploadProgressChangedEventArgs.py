class UploadProgressChangedEventArgs(ProgressChangedEventArgs):
 """ Provides data for the System.Net.WebClient.UploadProgressChanged event of a System.Net.WebClient. """
 BytesReceived=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of bytes received.



Get: BytesReceived(self: UploadProgressChangedEventArgs) -> Int64



"""

 BytesSent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of bytes sent.



Get: BytesSent(self: UploadProgressChangedEventArgs) -> Int64



"""

 TotalBytesToReceive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total number of bytes in a System.Net.WebClient data upload operation.



Get: TotalBytesToReceive(self: UploadProgressChangedEventArgs) -> Int64



"""

 TotalBytesToSend=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total number of bytes to send.



Get: TotalBytesToSend(self: UploadProgressChangedEventArgs) -> Int64



"""


