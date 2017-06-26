class LinearDimension(AnnotationBase, IDisposable, ISerializable):
    """
    LinearDimension()
    LinearDimension(dimensionPlane: Plane, extensionLine1End: Point2d, extensionLine2End: Point2d, pointOnDimensionLine: Point2d)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """ ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """ NonConstOperation(self: CommonObject) """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """ OnSwitchToNonConst(self: GeometryBase) """
        pass

    def SetLocations(self, extensionLine1End, extensionLine2End, pointOnDimensionLine):
        """ SetLocations(self: LinearDimension, extensionLine1End: Point2d, extensionLine2End: Point2d, pointOnDimensionLine: Point2d) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dimensionPlane=None, extensionLine1End=None, extensionLine2End=None, pointOnDimensionLine=None):
        """
        __new__(cls: type)
        __new__(cls: type, dimensionPlane: Plane, extensionLine1End: Point2d, extensionLine2End: Point2d, pointOnDimensionLine: Point2d)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Aligned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Aligned(self: LinearDimension) -> bool

Set: Aligned(self: LinearDimension) = value
"""

    Arrowhead1End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arrowhead1End(self: LinearDimension) -> Point2d

"""

    Arrowhead2End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arrowhead2End(self: LinearDimension) -> Point2d

"""

    DimensionStyleIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionStyleIndex(self: LinearDimension) -> int

Set: DimensionStyleIndex(self: LinearDimension) = value
"""

    DistanceBetweenArrowTips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceBetweenArrowTips(self: LinearDimension) -> float

"""

    ExtensionLine1End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionLine1End(self: LinearDimension) -> Point2d

"""

    ExtensionLine2End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionLine2End(self: LinearDimension) -> Point2d

"""

    TextPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextPosition(self: LinearDimension) -> Point2d

Set: TextPosition(self: LinearDimension) = value
"""


