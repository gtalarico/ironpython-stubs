class License(object, IDisposable):
    """ Provides the abstract base class for all licenses. A license is granted to a specific instance of a component. """
    def Dispose(self):
        """
        Dispose(self: License)
            When overridden in a derived class, disposes of the resources used by the license.
        """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    LicenseKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the license key granted to this component.

Get: LicenseKey(self: License) -> str

"""


