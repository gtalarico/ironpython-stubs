class UploadStringCompletedEventArgs(AsyncCompletedEventArgs):
 """ Provides data for the System.Net.WebClient.UploadStringCompleted event. """
 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the server reply to a string upload operation that is started by calling an erload:System.Net.WebClient.UploadStringAsync method.



Get: Result(self: UploadStringCompletedEventArgs) -> str



"""


