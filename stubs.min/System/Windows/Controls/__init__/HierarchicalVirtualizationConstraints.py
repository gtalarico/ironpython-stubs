class HierarchicalVirtualizationConstraints(object):
    """ HierarchicalVirtualizationConstraints(cacheLength: VirtualizationCacheLength, cacheLengthUnit: VirtualizationCacheLengthUnit, viewport: Rect) """
    def Equals(self, *__args):
        """
        Equals(self: HierarchicalVirtualizationConstraints, comparisonConstraints: HierarchicalVirtualizationConstraints) -> bool
        Equals(self: HierarchicalVirtualizationConstraints, oCompare: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: HierarchicalVirtualizationConstraints) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cacheLength, cacheLengthUnit, viewport):
        """
        __new__[HierarchicalVirtualizationConstraints]() -> HierarchicalVirtualizationConstraints
        
        __new__(cls: type, cacheLength: VirtualizationCacheLength, cacheLengthUnit: VirtualizationCacheLengthUnit, viewport: Rect)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    CacheLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheLength(self: HierarchicalVirtualizationConstraints) -> VirtualizationCacheLength

"""

    CacheLengthUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheLengthUnit(self: HierarchicalVirtualizationConstraints) -> VirtualizationCacheLengthUnit

"""

    Viewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Viewport(self: HierarchicalVirtualizationConstraints) -> Rect

"""


