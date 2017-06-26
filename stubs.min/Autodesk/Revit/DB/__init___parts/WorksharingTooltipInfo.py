class WorksharingTooltipInfo(object, IDisposable):
    """ Worksharing information about a single element suitable for display in an in-canvas tooltip. """
    def Dispose(self):
        """ Dispose(self: WorksharingTooltipInfo) """
        pass

    def GetRequesters(self):
        """
        GetRequesters(self: WorksharingTooltipInfo) -> IList[str]
        
            The ordered list of unique user names of users who have outstanding editing 
             requests for
           the specified element.
        
            Returns: The ordered list of unique user names.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WorksharingTooltipInfo, disposing: bool) """
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

    Creator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The user name of the user who created the element.

Get: Creator(self: WorksharingTooltipInfo) -> str

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: WorksharingTooltipInfo) -> bool

"""

    LastChangedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The user name of the most recent user who saved a user change of this element
   to the central model.

Get: LastChangedBy(self: WorksharingTooltipInfo) -> str

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current owner of the element or empty string if no one owns the element.

Get: Owner(self: WorksharingTooltipInfo) -> str

"""


