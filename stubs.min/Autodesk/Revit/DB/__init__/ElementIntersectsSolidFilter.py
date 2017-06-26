class ElementIntersectsSolidFilter(ElementIntersectsFilter, IDisposable):
    """
    A filter to find elements that intersect the given solid geometry.
    
    ElementIntersectsSolidFilter(solid: Solid, inverted: bool)
    ElementIntersectsSolidFilter(solid: Solid)
    """
    def Dispose(self):
        """ Dispose(self: ElementFilter, A_0: bool) """
        pass

    def GetSolid(self):
        """
        GetSolid(self: ElementIntersectsSolidFilter) -> Solid
        
            Gets the target solid geometry.
            Returns: The solid geometry.
        """
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
    def __new__(self, solid, inverted=None):
        """
        __new__(cls: type, solid: Solid, inverted: bool)
        __new__(cls: type, solid: Solid)
        """
        pass

