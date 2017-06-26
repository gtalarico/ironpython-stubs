class WorksetKindFilter(WorksetFilter, IDisposable):
    """
    A filter used to match worksets of the given WorksetKind.
    
    WorksetKindFilter(worksetKind: WorksetKind, inverted: bool)
    WorksetKindFilter(worksetKind: WorksetKind)
    """
    def Dispose(self):
        """ Dispose(self: WorksetFilter, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WorksetFilter, disposing: bool) """
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
    def __new__(self, worksetKind, inverted=None):
        """
        __new__(cls: type, worksetKind: WorksetKind, inverted: bool)
        __new__(cls: type, worksetKind: WorksetKind)
        """
        pass

    WorksetKind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The WorksetKind.

Get: WorksetKind(self: WorksetKindFilter) -> WorksetKind

"""


