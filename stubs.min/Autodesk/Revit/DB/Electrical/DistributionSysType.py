class DistributionSysType(ElementType, IDisposable):
    """ Represents a specific type of distribution system. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    ElectricalPhase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set electrical phase (single, triple or undefined) of distribution system.

Get: ElectricalPhase(self: DistributionSysType) -> ElectricalPhase

Set: ElectricalPhase(self: DistributionSysType) = value
"""

    ElectricalPhaseConfiguration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set electrical phase configuration (Y, delta or undefined) of distribution system.

Get: ElectricalPhaseConfiguration(self: DistributionSysType) -> ElectricalPhaseConfiguration

Set: ElectricalPhaseConfiguration(self: DistributionSysType) = value
"""

    IsInUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value which indicates whether this distribution system is in service now.

Get: IsInUse(self: DistributionSysType) -> bool

"""

    NumWires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set number of wires of distribution system.

Get: NumWires(self: DistributionSysType) -> int

Set: NumWires(self: DistributionSysType) = value
"""

    VoltageLineToGround = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set line to ground voltage of distribution system type.

Get: VoltageLineToGround(self: DistributionSysType) -> VoltageType

Set: VoltageLineToGround(self: DistributionSysType) = value
"""

    VoltageLineToLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set line to line voltage type of distribution system type.

Get: VoltageLineToLine(self: DistributionSysType) -> VoltageType

Set: VoltageLineToLine(self: DistributionSysType) = value
"""


