class DynamicDocumentPaginator(DocumentPaginator):
    """ Provides an abstract base class that supports automatic background pagination and tracking content positions across repaginations in addition to the methods and properties of its own base class. """
    def GetObjectPosition(self, value):
        """
        GetObjectPosition(self: DynamicDocumentPaginator, value: object) -> ContentPosition
        
            When overridden in a derived class, returns a System.Windows.Documents.ContentPosition for the specified System.Object.
        
            value: The object to return the System.Windows.Documents.ContentPosition of.
            Returns: The System.Windows.Documents.ContentPosition of the given object.
        """
        pass

    def GetPageNumber(self, contentPosition):
        """
        GetPageNumber(self: DynamicDocumentPaginator, contentPosition: ContentPosition) -> int
        
            When overridden in a derived class, returns the zero-based page number of the specified System.Windows.Documents.ContentPosition.
        
            contentPosition: The content position whose page number is needed.
            Returns: An System.Int32 representing zero-based page number where the specified contentPosition appears.
        """
        pass

    def GetPageNumberAsync(self, contentPosition, userState=None):
        """
        GetPageNumberAsync(self: DynamicDocumentPaginator, contentPosition: ContentPosition, userState: object)
            Asynchronously, returns (through the This method raises the System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberCompleted event) the zero-based page number of the specified 
             System.Windows.Documents.ContentPosition.
        
        
            contentPosition: The content position element to return the page number of.
            userState: A unique identifier for the asynchronous task.
        GetPageNumberAsync(self: DynamicDocumentPaginator, contentPosition: ContentPosition)
            Asynchronously, returns (through the This method raises the System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberCompleted event) the zero-based page number of the specified 
             System.Windows.Documents.ContentPosition.
        
        
            contentPosition: The content position whose page number is needed.
        """
        pass

    def GetPagePosition(self, page):
        """
        GetPagePosition(self: DynamicDocumentPaginator, page: DocumentPage) -> ContentPosition
        
            When overridden in a derived class, gets the position of the specified page in the document's content.
        
            page: The page whose position is needed.
            Returns: A System.Windows.Documents.ContentPosition representing the position of page.
        """
        pass

    def OnGetPageNumberCompleted(self, *args): #cannot find CLR method
        """
        OnGetPageNumberCompleted(self: DynamicDocumentPaginator, e: GetPageNumberCompletedEventArgs)
            Raises the System.Windows.Documents.DynamicDocumentPaginator.GetPageNumberCompleted event.
        
            e: A System.Windows.Documents.GetPageNumberCompletedEventArgs that contains the event data.
        """
        pass

    def OnPaginationCompleted(self, *args): #cannot find CLR method
        """
        OnPaginationCompleted(self: DynamicDocumentPaginator, e: EventArgs)
            Raises the System.Windows.Documents.DynamicDocumentPaginator.PaginationCompleted event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def OnPaginationProgress(self, *args): #cannot find CLR method
        """
        OnPaginationProgress(self: DynamicDocumentPaginator, e: PaginationProgressEventArgs)
            Raises the System.Windows.Documents.DynamicDocumentPaginator.PaginationProgress event.
        
            e: A System.Windows.Documents.PaginationProgressEventArgs that contains the event data.
        """
        pass

    IsBackgroundPaginationEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether pagination is performed automatically in the background in response to certain events, such as a change in page size.

Get: IsBackgroundPaginationEnabled(self: DynamicDocumentPaginator) -> bool

Set: IsBackgroundPaginationEnabled(self: DynamicDocumentPaginator) = value
"""


    GetPageNumberCompleted = None
    PaginationCompleted = None
    PaginationProgress = None

