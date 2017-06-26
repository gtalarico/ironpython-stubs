class SweptProfile(object, IDisposable):
    """ Represents an extruded profile swept along a driving curve. """
    def Dispose(self):
        """ Dispose(self: SweptProfile) """
        pass

    def GetDrivingCurve(self):
        """
        GetDrivingCurve(self: SweptProfile) -> Curve
        
            Provides access to the curve that dictates the path of the swept profile.
            Returns: A curve that defines the path of the swept profile.
        """
        pass

    def GetSweptProfile(self):
        """
        GetSweptProfile(self: SweptProfile) -> Profile
        
            Returns an object that describes the profile that is swept along the driving 
             curve.
        
            Returns: A geometric profile object.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SweptProfile, disposing: bool) """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    EndSetBack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The distance from the end of the driving curve to the point where the sweep actually ends.

Get: EndSetBack(self: SweptProfile) -> float

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: SweptProfile) -> bool

"""

    StartSetBack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The distance from the start of the driving curve to the point where the sweep actually begins.

Get: StartSetBack(self: SweptProfile) -> float

"""


