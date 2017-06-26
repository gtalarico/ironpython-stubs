class UploadValuesCompletedEventArgs(AsyncCompletedEventArgs):
    """ Provides data for the System.Net.WebClient.UploadValuesCompleted event. """
    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the server reply to a data upload operation started by calling an erload:System.Net.WebClient.UploadValuesAsync method.

Get: Result(self: UploadValuesCompletedEventArgs) -> Array[Byte]

"""


