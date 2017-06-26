class DuplicateTypeNamesHandlerArgs(object, IDisposable):
    """ A structure that provides information about an attempt to copy types with names that already exist in the destination document. """
    def Dispose(self):
        """ Dispose(self: DuplicateTypeNamesHandlerArgs) """
        pass

    def GetTypeIds(self):
        """
        GetTypeIds(self: DuplicateTypeNamesHandlerArgs) -> ICollection[ElementId]
        
            Returns ids of the types with duplicate names.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DuplicateTypeNamesHandlerArgs, disposing: bool) """
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

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The document that contains the types with duplicate names.

Get: Document(self: DuplicateTypeNamesHandlerArgs) -> Document

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DuplicateTypeNamesHandlerArgs) -> bool

"""


