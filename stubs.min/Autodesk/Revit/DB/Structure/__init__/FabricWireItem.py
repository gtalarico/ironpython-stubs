class FabricWireItem(object, IDisposable):
    """ Provides implementation for FabricWires stored in a Custom Fabric Sheet """
    @staticmethod
    def Create(distance, wireLength, wireType):
        """
        Create(distance: float, wireLength: float, wireType: ElementId) -> FabricWireItem
        
            Creates a new instance of a single Fabric wire.
        
            distance: The distance between this wire and the next wire in the Custom Fabric Sheet
            wireLength: Length of this wire
            wireType: The wire type of this wire
            Returns: The newly created Fabric wire instance.
        """
        pass

    def Dispose(self):
        """ Dispose(self: FabricWireItem) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FabricWireItem, disposing: bool) """
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

    Distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance to the next fabric wire item

Get: Distance(self: FabricWireItem) -> float

Set: Distance(self: FabricWireItem) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FabricWireItem) -> bool

"""

    WireLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Wire length for this wire item

Get: WireLength(self: FabricWireItem) -> float

Set: WireLength(self: FabricWireItem) = value
"""

    WireType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The wire type of this wire item

Get: WireType(self: FabricWireItem) -> ElementId

Set: WireType(self: FabricWireItem) = value
"""


