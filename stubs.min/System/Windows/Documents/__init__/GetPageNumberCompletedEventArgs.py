class GetPageNumberCompletedEventArgs(AsyncCompletedEventArgs):
    """
    Provides data for the System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberCompleted event.
    
    GetPageNumberCompletedEventArgs(contentPosition: ContentPosition, pageNumber: int, error: Exception, cancelled: bool, userState: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, contentPosition, pageNumber, error, cancelled, userState):
        """ __new__(cls: type, contentPosition: ContentPosition, pageNumber: int, error: Exception, cancelled: bool, userState: object) """
        pass

    ContentPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Documents.ContentPosition passed to System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberAsync(System.Windows.Documents.ContentPosition).

Get: ContentPosition(self: GetPageNumberCompletedEventArgs) -> ContentPosition

"""

    PageNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the page number for the System.Windows.Documents.ContentPosition passed to System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberAsync(System.Windows.Documents.ContentPosition).

Get: PageNumber(self: GetPageNumberCompletedEventArgs) -> int

"""


