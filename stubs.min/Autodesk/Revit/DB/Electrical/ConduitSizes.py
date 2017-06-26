class ConduitSizes(object, IEnumerable[ConduitSize], IEnumerable, IDisposable):
    """ Class ConduitSizeSet being used to store the conduit sizes. """
    def Contains(self, nominalDiameter):
        """
        Contains(self: ConduitSizes, nominalDiameter: float) -> bool
        
            Checks whether a conduit size with the nominal diameter exists.
        
            nominalDiameter: Nominal diameter.
            Returns: True if a conduit size with the nominal diameter exists.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ConduitSizes) """
        pass

    def GetConduitSizesIterator(self):
        """
        GetConduitSizesIterator(self: ConduitSizes) -> ConduitSizeIterator
        
            Returns a ConduitSizeIterator to the conduit sizes.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ConduitSizes) -> IEnumerator[ConduitSize]
        
            Returns an enumerator that iterates through a collection.
            Returns: An IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ConduitSizes, disposing: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ConduitSize](enumerable: IEnumerable[ConduitSize], value: ConduitSize) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Count of the items contained in the collection.

Get: Count(self: ConduitSizes) -> int

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ConduitSizes) -> bool

"""


