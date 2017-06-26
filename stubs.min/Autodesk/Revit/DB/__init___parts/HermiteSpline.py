class HermiteSpline(Curve, IDisposable):
    """ A Hermite spline. """
    @staticmethod
    def Create(controlPoints, periodic, tangents=None):
        """
        Create(controlPoints: IList[XYZ], periodic: bool) -> HermiteSpline
        Create(controlPoints: IList[XYZ], periodic: bool, tangents: HermiteSplineTangents) -> HermiteSpline
        """
        pass

    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: GeometryObject) """
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

    ControlPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The control points of the Hermite spline.

Get: ControlPoints(self: HermiteSpline) -> IList[XYZ]

Set: ControlPoints(self: HermiteSpline) = value
"""

    IsPeriodic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns whether the Hermite spline is periodic or not.

Get: IsPeriodic(self: HermiteSpline) -> bool

"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the params of the Hermite spline.

Get: Parameters(self: HermiteSpline) -> DoubleArray

"""

    Tangents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the tangents of the Hermite spline.

Get: Tangents(self: HermiteSpline) -> IList[XYZ]

"""


