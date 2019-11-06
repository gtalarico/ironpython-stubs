class UploadStringCompletedEventArgs(AsyncCompletedEventArgs):
 """ Provides data for the System.Net.WebClient.UploadStringCompleted event. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return UploadStringCompletedEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the server reply to a string upload operation that is started by calling an erload:System.Net.WebClient.UploadStringAsync method.

Get: Result(self: UploadStringCompletedEventArgs) -> str

"""


