class OpenWriteCompletedEventArgs(AsyncCompletedEventArgs):
    """ Provides data for the System.Net.WebClient.OpenWriteCompleted event. """
    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a writable stream that is used to send data to a server.

Get: Result(self: OpenWriteCompletedEventArgs) -> Stream

"""


