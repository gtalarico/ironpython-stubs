class UploadDataCompletedEventArgs(AsyncCompletedEventArgs):
 """ Provides data for the System.Net.WebClient.UploadDataCompleted event. """
 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the server reply to a data upload operation started by calling an erload:System.Net.WebClient.UploadDataAsync method.



Get: Result(self: UploadDataCompletedEventArgs) -> Array[Byte]



"""


