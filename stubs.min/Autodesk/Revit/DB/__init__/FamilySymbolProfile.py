class FamilySymbolProfile(SweepProfile, IDisposable):
    """ Represents a family symbol based profile for sweep or swept blend elements. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The angle of the rotation of the profile in radians.

Get: Angle(self: FamilySymbolProfile) -> float

Set: Angle(self: FamilySymbolProfile) = value
"""

    IsFlipped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the symbol profile is flipped or not.

Get: IsFlipped(self: FamilySymbolProfile) -> bool

Set: IsFlipped(self: FamilySymbolProfile) = value
"""

    Profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the family symbol of the profile.

Get: Profile(self: FamilySymbolProfile) -> FamilySymbol

Set: Profile(self: FamilySymbolProfile) = value
"""

    XOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset of the profile to the origin of the sketch plane in the X direction.

Get: XOffset(self: FamilySymbolProfile) -> float

Set: XOffset(self: FamilySymbolProfile) = value
"""

    YOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset of the profile to the origin of the sketch plane in the Y direction.

Get: YOffset(self: FamilySymbolProfile) -> float

Set: YOffset(self: FamilySymbolProfile) = value
"""


