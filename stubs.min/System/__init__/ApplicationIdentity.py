class ApplicationIdentity(object, ISerializable):
    """
    Provides the ability to uniquely identify a manifest-activated application. This class cannot be inherited.
    
    ApplicationIdentity(applicationIdentityFullName: str)
    """
    def ToString(self):
        """
        ToString(self: ApplicationIdentity) -> str
        
            Returns the full name of the manifest-activated application.
            Returns: The full name of the manifest-activated application.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, applicationIdentityFullName):
        """ __new__(cls: type, applicationIdentityFullName: str) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CodeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the location of the deployment manifest as a URL.

Get: CodeBase(self: ApplicationIdentity) -> str

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the full name of the application.

Get: FullName(self: ApplicationIdentity) -> str

"""


