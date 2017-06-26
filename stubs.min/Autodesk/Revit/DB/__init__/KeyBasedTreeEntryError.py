class KeyBasedTreeEntryError(object, IDisposable):
    """ This class contains information about a problem encountered while creating a KeyBasedTreeEntries object. """
    def Dispose(self):
        """ Dispose(self: KeyBasedTreeEntryError) """
        pass

    def GetEntry(self):
        """
        GetEntry(self: KeyBasedTreeEntryError) -> KeyBasedTreeEntry
        
            Gets the entry for which an error occurred while building the 
             KeyBasedTreeEntries object.
        
            Returns: A copy of the KeyBasedTreeEntry.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: KeyBasedTreeEntryError, disposing: bool) """
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

    ErrorType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates which of possible types of problems with loading and/or building
   a KeyBasedTreeEntries that this KeyBasedTreeEntryError represents.

Get: ErrorType(self: KeyBasedTreeEntryError) -> KeyBasedTreeEntryErrorType

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: KeyBasedTreeEntryError) -> bool

"""


