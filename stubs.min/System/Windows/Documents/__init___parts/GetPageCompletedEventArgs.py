class GetPageCompletedEventArgs(AsyncCompletedEventArgs):
    """
    Provides data for the System.Windows.Documents.DocumentPaginator.GetPageCompleted event.
    
    GetPageCompletedEventArgs(page: DocumentPage, pageNumber: int, error: Exception, cancelled: bool, userState: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, page, pageNumber, error, cancelled, userState):
        """ __new__(cls: type, page: DocumentPage, pageNumber: int, error: Exception, cancelled: bool, userState: object) """
        pass

    DocumentPage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Documents.DocumentPage for the page specified in the call to System.Windows.Documents.DocumentPaginator.GetPageAsync(System.Int32,System.Object).

Get: DocumentPage(self: GetPageCompletedEventArgs) -> DocumentPage

"""

    PageNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the page number passed to System.Windows.Documents.DocumentPaginator.GetPageAsync(System.Int32,System.Object).

Get: PageNumber(self: GetPageCompletedEventArgs) -> int

"""


