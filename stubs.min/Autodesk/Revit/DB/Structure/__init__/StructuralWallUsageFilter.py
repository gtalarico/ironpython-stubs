class StructuralWallUsageFilter(ElementSlowFilter, IDisposable):
    """
    A filter used to match walls that have the given structural wall usage.
    
    StructuralWallUsageFilter(structuralWallUsage: StructuralWallUsage, inverted: bool)
    StructuralWallUsageFilter(structuralWallUsage: StructuralWallUsage)
    """
    def Dispose(self):
        """ Dispose(self: ElementFilter, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ElementFilter, disposing: bool) """
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
    def __new__(self, structuralWallUsage, inverted=None):
        """
        __new__(cls: type, structuralWallUsage: StructuralWallUsage, inverted: bool)
        __new__(cls: type, structuralWallUsage: StructuralWallUsage)
        """
        pass

    StructuralWallUsage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The wall structural usage.

Get: StructuralWallUsage(self: StructuralWallUsageFilter) -> StructuralWallUsage

"""


