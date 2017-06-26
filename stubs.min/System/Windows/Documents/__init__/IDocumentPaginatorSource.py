class IDocumentPaginatorSource:
    """ Defines the source object that performs actual content pagination. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DocumentPaginator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When implemented in a derived class, gets the object that performs content pagination.

Get: DocumentPaginator(self: IDocumentPaginatorSource) -> DocumentPaginator

"""


