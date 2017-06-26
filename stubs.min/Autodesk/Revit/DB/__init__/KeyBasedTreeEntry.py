class KeyBasedTreeEntry(object, IDisposable):
    """ A key-based tree entry, containing the key, parent key, and children keys (if applicable). """
    def Dispose(self):
        """ Dispose(self: KeyBasedTreeEntry) """
        pass

    def GetChildrenKeys(self):
        """
        GetChildrenKeys(self: KeyBasedTreeEntry) -> IList[str]
        
            Gets a collection containing the keys of all children entry objects from this 
             entry.
        
            Returns: The collection containing the keys of all children entry objects from this 
             entry.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: KeyBasedTreeEntry, disposing: bool) """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: KeyBasedTreeEntry) -> bool

"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The key of this entry.

Get: Key(self: KeyBasedTreeEntry) -> str

"""

    ParentKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The parent key of this entry.

Get: ParentKey(self: KeyBasedTreeEntry) -> str

"""


