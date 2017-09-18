class UploadFileCompletedEventArgs(AsyncCompletedEventArgs):
 """ Provides data for the System.Net.WebClient.UploadFileCompleted event. """
 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the server reply to a data upload operation that is started by calling an erload:System.Net.WebClient.UploadFileAsync method.



Get: Result(self: UploadFileCompletedEventArgs) -> Array[Byte]



"""


