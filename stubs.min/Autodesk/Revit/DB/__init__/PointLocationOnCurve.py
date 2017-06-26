class PointLocationOnCurve(object, IDisposable):
    """
    Defines the measurement parameters necessary to create a point at a specific location on a curve.
    
    PointLocationOnCurve(measType: PointOnCurveMeasurementType, measValue: float, measFrom: PointOnCurveMeasureFrom)
    """
    def Dispose(self):
        """ Dispose(self: PointLocationOnCurve) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PointLocationOnCurve, disposing: bool) """
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
    def __new__(self, measType, measValue, measFrom):
        """ __new__(cls: type, measType: PointOnCurveMeasurementType, measValue: float, measFrom: PointOnCurveMeasureFrom) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PointLocationOnCurve) -> bool

"""

    MeasureFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The location on the curve from which the measurement is taken.

Get: MeasureFrom(self: PointLocationOnCurve) -> PointOnCurveMeasureFrom

Set: MeasureFrom(self: PointLocationOnCurve) = value
"""

    MeasurementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The measurement type.

Get: MeasurementType(self: PointLocationOnCurve) -> PointOnCurveMeasurementType

Set: MeasurementType(self: PointLocationOnCurve) = value
"""

    MeasurementValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The measurement value.

Get: MeasurementValue(self: PointLocationOnCurve) -> float

Set: MeasurementValue(self: PointLocationOnCurve) = value
"""


