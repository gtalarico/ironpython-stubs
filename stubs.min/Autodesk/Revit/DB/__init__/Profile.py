class Profile(GeometryObject, IDisposable):
    """ A geometric profile consisting of a loop of curves. """
    def Clone(self):
        """
        Clone(self: Profile) -> Profile
        
            Returns a copy of this profile.
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

    Curves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the curves that make up the boundary of the profile.

Get: Curves(self: Profile) -> CurveArray

"""

    Filled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set whether the profile is filled.

Get: Filled(self: Profile) -> bool

Set: Filled(self: Profile) = value
"""


