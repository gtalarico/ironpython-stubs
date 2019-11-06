class UploadFileCompletedEventArgs(AsyncCompletedEventArgs):
 """ Provides data for the System.Net.WebClient.UploadFileCompleted event. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return UploadFileCompletedEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the server reply to a data upload operation that is started by calling an erload:System.Net.WebClient.UploadFileAsync method.

Get: Result(self: UploadFileCompletedEventArgs) -> Array[Byte]

"""


