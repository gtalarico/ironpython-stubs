class CorrectionFactor(APIObject, IDisposable):
    """ Represents electrical correction factor information. """
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

    Factor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get factor value of wire correction factor.

Get: Factor(self: CorrectionFactor) -> float

"""

    Temperature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get temperature which is used for specifying correction factor.

Get: Temperature(self: CorrectionFactor) -> Int64

"""


