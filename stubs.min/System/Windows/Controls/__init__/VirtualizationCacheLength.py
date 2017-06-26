class VirtualizationCacheLength(object, IEquatable[VirtualizationCacheLength]):
    """
    VirtualizationCacheLength(cacheBeforeViewport: float, cacheAfterViewport: float)
    VirtualizationCacheLength(cacheBeforeAndAfterViewport: float)
    """
    def Equals(self, *__args):
        """
        Equals(self: VirtualizationCacheLength, cacheLength: VirtualizationCacheLength) -> bool
        Equals(self: VirtualizationCacheLength, oCompare: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: VirtualizationCacheLength) -> int """
        pass

    def ToString(self):
        """ ToString(self: VirtualizationCacheLength) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[VirtualizationCacheLength]() -> VirtualizationCacheLength
        
        __new__(cls: type, cacheBeforeAndAfterViewport: float)
        __new__(cls: type, cacheBeforeViewport: float, cacheAfterViewport: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CacheAfterViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheAfterViewport(self: VirtualizationCacheLength) -> float

"""

    CacheBeforeViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheBeforeViewport(self: VirtualizationCacheLength) -> float

"""


