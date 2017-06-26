class ExternalResourceMatchOptions(object, IDisposable):
    """
    Represents match options used to filter external resources when listing them from external resource server.
    
    ExternalResourceMatchOptions(resourceType: ExternalResourceType)
    """
    def Dispose(self):
        """ Dispose(self: ExternalResourceMatchOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExternalResourceMatchOptions, disposing: bool) """
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

    @staticmethod # known case of __new__
    def __new__(self, resourceType):
        """ __new__(cls: type, resourceType: ExternalResourceType) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExternalResourceMatchOptions) -> bool

"""

    ResourceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The desired resource type which external resources should match.

Get: ResourceType(self: ExternalResourceMatchOptions) -> ExternalResourceType

"""


