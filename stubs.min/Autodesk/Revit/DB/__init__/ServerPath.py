class ServerPath(ModelPath, IDisposable):
    """
    This class represents a path to a Revit Server location, rather than a
       location on disk or a network drive.
    
    ServerPath(centralServerLocation: str, path: str)
    """
    def Dispose(self):
        """ Dispose(self: ModelPath, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ModelPath, disposing: bool) """
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
    def __new__(self, centralServerLocation, path):
        """ __new__(cls: type, centralServerLocation: str, path: str) """
        pass

