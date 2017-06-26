class PagesChangedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Documents.DocumentPaginator.PagesChanged event.
    
    PagesChangedEventArgs(start: int, count: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, start, count):
        """ __new__(cls: type, start: int, count: int) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of continuous pages that changed.

Get: Count(self: PagesChangedEventArgs) -> int

"""

    Start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the page number of the first page that changed.

Get: Start(self: PagesChangedEventArgs) -> int

"""


