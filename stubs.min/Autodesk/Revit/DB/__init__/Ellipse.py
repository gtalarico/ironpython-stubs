class Ellipse(Curve, IDisposable):
    """ A whole or partial ellipse. """
    @staticmethod
    def Create(center, xRadius, yRadius, xAxis, yAxis, startParameter, endParameter):
        """
        Create(center: XYZ, xRadius: float, yRadius: float, xAxis: XYZ, yAxis: XYZ, startParameter: float, endParameter: float) -> Ellipse
        
            Creates a new geometric ellipse or elliptical arc object.
        
            center: The center.
            xRadius: The x vector radius of the ellipse.
            yRadius: The y vector radius of the ellipse.
            xAxis: The x axis to define the ellipse plane.  Must be normalized.
            yAxis: The y axis to define the ellipse plane.   Must be normalized.
            startParameter: The raw parameter value at the start of the ellipse.
            endParameter: The raw parameter value at the end of the ellipse.
            Returns: The new ellipse or elliptical arc.
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

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the center of the ellipse.

Get: Center(self: Ellipse) -> XYZ

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the normal to the plane in which the ellipse is defined.

Get: Normal(self: Ellipse) -> XYZ

"""

    RadiusX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the X vector radius of the ellipse.

Get: RadiusX(self: Ellipse) -> float

"""

    RadiusY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Y vector radius of the ellipse.

Get: RadiusY(self: Ellipse) -> float

"""

    XDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The X direction.

Get: XDirection(self: Ellipse) -> XYZ

"""

    YDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Y direction.

Get: YDirection(self: Ellipse) -> XYZ

"""


