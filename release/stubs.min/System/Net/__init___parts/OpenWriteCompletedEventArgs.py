class OpenWriteCompletedEventArgs(AsyncCompletedEventArgs):
 """ Provides data for the System.Net.WebClient.OpenWriteCompleted event. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return OpenWriteCompletedEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a writable stream that is used to send data to a server.

Get: Result(self: OpenWriteCompletedEventArgs) -> Stream

"""


