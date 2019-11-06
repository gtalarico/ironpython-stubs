class UploadValuesCompletedEventArgs(AsyncCompletedEventArgs):
 """ Provides data for the System.Net.WebClient.UploadValuesCompleted event. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return UploadValuesCompletedEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the server reply to a data upload operation started by calling an erload:System.Net.WebClient.UploadValuesAsync method.

Get: Result(self: UploadValuesCompletedEventArgs) -> Array[Byte]

"""


