class DefinitionGroup(APIObject, IDisposable):
    """ The DefinitionGroup is a container that is used to hold shared parameter definitions on disk. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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

    Definitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Definitions property returns an object that contains all the shared parameter
definitions within the group.

Get: Definitions(self: DefinitionGroup) -> Definitions

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the name of the parameter group.

Get: Name(self: DefinitionGroup) -> str

"""


