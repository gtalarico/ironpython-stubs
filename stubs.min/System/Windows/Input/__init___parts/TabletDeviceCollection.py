class TabletDeviceCollection(object, ICollection, IEnumerable):
    """ Contains the System.Windows.Input.TabletDevice objects that represent the digitizer devices of a tablet device. """
    def CopyTo(self, array, index):
        """
        CopyTo(self: TabletDeviceCollection, array: Array[TabletDevice], index: int)
            Copies all elements in the current collection to the specified one-dimensional array, starting at the specified destination array index.
        
            array: The one-dimensional array that is the destination of elements copied from the collection. The array must have zero-based indexing.
            index: The zero-based index in the array parameter where copying begins.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Windows.Input.TabletDevice objects in the collection.

Get: Count(self: TabletDeviceCollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether access to the collection is synchronized (thread safe).

Get: IsSynchronized(self: TabletDeviceCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the collection.

Get: SyncRoot(self: TabletDeviceCollection) -> object

"""


