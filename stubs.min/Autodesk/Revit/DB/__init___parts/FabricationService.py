class FabricationService(object, IDisposable):
    """ This object contains information about a fabrication service. """
    def Dispose(self):
        """ Dispose(self: FabricationService) """
        pass

    def GetButton(self, groupIndex, buttonIndex):
        """
        GetButton(self: FabricationService, groupIndex: int, buttonIndex: int) -> FabricationServiceButton
        
            Gets the service button for a given group index and button index from the 
             service.
        
        
            groupIndex: The group index.
            buttonIndex: The button index.
            Returns: The service button
        """
        pass

    def GetButtonCount(self, group):
        """
        GetButtonCount(self: FabricationService, group: int) -> int
        
            Gets the number of buttons for a given group in the service.
        
            group: The index of the group
            Returns: The number of buttons.
        """
        pass

    def GetGroupName(self, group):
        """
        GetGroupName(self: FabricationService, group: int) -> str
        
            Gets the name of a group based on group index.
        
            group: The index of the group.
            Returns: The name of the group.
        """
        pass

    def IsValidButtonIndex(self, groupIndex, buttonIndex):
        """
        IsValidButtonIndex(self: FabricationService, groupIndex: int, buttonIndex: int) -> bool
        
            Validates the button index.
        
            groupIndex: The group index.
            buttonIndex: The button index to check.
            Returns: True if larger or equal to 0 and less than GroupCount.
        """
        pass

    def IsValidGroupIndex(self, groupIndex):
        """
        IsValidGroupIndex(self: FabricationService, groupIndex: int) -> bool
        
            Validates the group index.
        
            groupIndex: The group index to check.
            Returns: True if larger or equal to 0 and less than GroupCount.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FabricationService, disposing: bool) """
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

    Abbreviation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The short name of service.

Get: Abbreviation(self: FabricationService) -> str

"""

    FabricationSystemName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fabrication system name of the service.

Get: FabricationSystemName(self: FabricationService) -> str

"""

    GroupCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of groups in the service.

Get: GroupCount(self: FabricationService) -> int

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FabricationService) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the service.

Get: Name(self: FabricationService) -> str

"""

    ServiceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The service identifier of the service.

Get: ServiceId(self: FabricationService) -> int

"""


