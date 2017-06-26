class FabricationHostedInfo(object, IDisposable):
    """ The fabrication hosted element information. """
    def DisconnectFromHost(self):
        """
        DisconnectFromHost(self: FabricationHostedInfo)
            Disconnects the part from the host.
        """
        pass

    def Dispose(self):
        """ Dispose(self: FabricationHostedInfo) """
        pass

    def GetBearerCenterline(self):
        """
        GetBearerCenterline(self: FabricationHostedInfo) -> Line
        
            Gets the centerline of the bearer. The method is applicable only for bearer 
             hanger.
        
            Returns: The centerline of the bearer.
        """
        pass

    def PlaceOnHost(self, hostId, hostConnector, distance):
        """
        PlaceOnHost(self: FabricationHostedInfo, hostId: ElementId, hostConnector: Connector, distance: float)
            Places the part on the specified host.
        
            hostId: Id of the host fabrication part.
            hostConnector: The connector of the host.
            distance: The distance from the connector to place the hosted part. Units are in feet 
             (ft).
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FabricationHostedInfo, disposing: bool) """
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

    HostId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Id of the host.

Get: HostId(self: FabricationHostedInfo) -> ElementId

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FabricationHostedInfo) -> bool

"""


