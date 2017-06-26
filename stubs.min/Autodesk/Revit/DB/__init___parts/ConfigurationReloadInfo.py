class ConfigurationReloadInfo(object, IDisposable):
    """
    This object contains information returned by a reload of the fabrication configuration.
    
    ConfigurationReloadInfo()
    """
    def Dispose(self):
        """ Dispose(self: ConfigurationReloadInfo) """
        pass

    def GetConnectivityValidation(self):
        """
        GetConnectivityValidation(self: ConfigurationReloadInfo) -> ConnectionValidationInfo
        
            Returns information about the post-reload connectivity validation.
            Returns: Information about the post-reload connectivity validation.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ConfigurationReloadInfo, disposing: bool) """
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

    Disconnects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of disconnections caused by the reload.

Get: Disconnects(self: ConfigurationReloadInfo) -> int

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ConfigurationReloadInfo) -> bool

"""

    ProfileNotAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current profile is not available in the disk configuration.

Get: ProfileNotAvailable(self: ConfigurationReloadInfo) -> bool

"""


