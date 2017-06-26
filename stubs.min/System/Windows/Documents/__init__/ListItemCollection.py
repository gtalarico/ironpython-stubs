class ListItemCollection(TextElementCollection[ListItem], IList, ICollection, IEnumerable, ICollection[ListItem], IEnumerable[ListItem]):
    """ Represents a collection of System.Windows.Documents.ListItem elements. System.Windows.Documents.ListItemCollection defines the allowable child content of a System.Windows.Documents.List element. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    FirstListItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the first System.Windows.Documents.ListItem element within this instance of System.Windows.Documents.ListItemCollection.

Get: FirstListItem(self: ListItemCollection) -> ListItem

"""

    LastListItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the last System.Windows.Documents.ListItem element within this instance of System.Windows.Documents.ListItemCollection.

Get: LastListItem(self: ListItemCollection) -> ListItem

"""


