class TextEntity(AnnotationBase, IDisposable, ISerializable):
    """ TextEntity() """
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
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AnnotativeScalingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnnotativeScalingEnabled(self: TextEntity) -> bool

Set: AnnotativeScalingEnabled(self: TextEntity) = value
"""

    FontIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontIndex(self: TextEntity) -> int

Set: FontIndex(self: TextEntity) = value
"""

    Justification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Justification(self: TextEntity) -> TextJustification

Set: Justification(self: TextEntity) = value
"""

    MaskColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaskColor(self: TextEntity) -> Color

Set: MaskColor(self: TextEntity) = value
"""

    MaskEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaskEnabled(self: TextEntity) -> bool

Set: MaskEnabled(self: TextEntity) = value
"""

    MaskOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaskOffset(self: TextEntity) -> float

Set: MaskOffset(self: TextEntity) = value
"""

    MaskUsesViewportColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaskUsesViewportColor(self: TextEntity) -> bool

Set: MaskUsesViewportColor(self: TextEntity) = value
"""


