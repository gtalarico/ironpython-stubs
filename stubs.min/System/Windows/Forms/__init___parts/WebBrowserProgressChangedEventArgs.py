class WebBrowserProgressChangedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.WebBrowser.ProgressChanged event.
    
    WebBrowserProgressChangedEventArgs(currentProgress: Int64, maximumProgress: Int64)
    """
    @staticmethod # known case of __new__
    def __new__(self, currentProgress, maximumProgress):
        """ __new__(cls: type, currentProgress: Int64, maximumProgress: Int64) """
        pass

    CurrentProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of bytes that have been downloaded.

Get: CurrentProgress(self: WebBrowserProgressChangedEventArgs) -> Int64

"""

    MaximumProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total number of bytes in the document being loaded.

Get: MaximumProgress(self: WebBrowserProgressChangedEventArgs) -> Int64

"""


