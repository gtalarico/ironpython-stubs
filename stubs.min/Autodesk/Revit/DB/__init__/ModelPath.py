class ModelPath(object, IDisposable):
    """ A path to a file stored on a disk or on a server. """
    def Compare(self, otherPath):
        """
        Compare(self: ModelPath, otherPath: ModelPath) -> int
        
            Compares this ModelPath with another
        
            otherPath: The path to compare against.
            Returns: A signed integer indicating the lexical relationship between
           two 
             ModelPaths. Value is less than zero if this path is less than
           the given 
             path; zero if the two are the same; and more than zero otherwise
        """
        pass

    def Dispose(self):
        """ Dispose(self: ModelPath) """
        pass

    def GetModelGUID(self):
        """
        GetModelGUID(self: ModelPath) -> Guid
        
            A GUID identifying the A360 model.
        """
        pass

    def GetProjectGUID(self):
        """
        GetProjectGUID(self: ModelPath) -> Guid
        
            A GUID identifying the A360 project to which the model is associated.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ModelPath, disposing: bool) """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
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

    CentralServerPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A path to the location of the central Revit server.

Get: CentralServerPath(self: ModelPath) -> str

"""

    Empty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether this path is empty

Get: Empty(self: ModelPath) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ModelPath) -> bool

"""

    ServerPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether this path is a server path (as opposed to a file path or cloud path)

Get: ServerPath(self: ModelPath) -> bool

"""


