class WireSize(APIObject, IDisposable):
    """ Represents specific electrical wire size information. """
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

    Ampacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get ampacity which be used for specifying size, the unit is ampere.

Get: Ampacity(self: WireSize) -> Int64

"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get diameter of wire.

Get: Diameter(self: WireSize) -> float

"""

    InUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set whether the size can be used in sizing.

Get: InUse(self: WireSize) -> bool

Set: InUse(self: WireSize) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get size symbol of wire.

Get: Size(self: WireSize) -> str

"""


