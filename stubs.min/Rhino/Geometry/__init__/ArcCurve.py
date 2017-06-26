class ArcCurve(Curve, IDisposable, ISerializable):
    """
    ArcCurve()
    ArcCurve(other: ArcCurve)
    ArcCurve(arc: Arc)
    ArcCurve(arc: Arc, t0: float, t1: float)
    ArcCurve(circle: Circle)
    ArcCurve(circle: Circle, t0: float, t1: float)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """ ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: Curve, disposing: bool) """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """ NonConstOperation(self: Curve) """
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
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, other: ArcCurve)
        __new__(cls: type, arc: Arc)
        __new__(cls: type, arc: Arc, t0: float, t1: float)
        __new__(cls: type, circle: Circle)
        __new__(cls: type, circle: Circle, t0: float, t1: float)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AngleDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleDegrees(self: ArcCurve) -> float

"""

    AngleRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleRadians(self: ArcCurve) -> float

"""

    Arc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc(self: ArcCurve) -> Arc

"""

    IsCompleteCircle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCompleteCircle(self: ArcCurve) -> bool

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: ArcCurve) -> float

"""


