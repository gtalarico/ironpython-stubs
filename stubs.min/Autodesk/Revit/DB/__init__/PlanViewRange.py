class PlanViewRange(object, IDisposable):
    """
    This class represents the view range of a plan view or a plan region.
       It records the element ids of the levels which a plane is relative to
       and the offset of each plane from that level.
    """
    def Dispose(self):
        """ Dispose(self: PlanViewRange) """
        pass

    def GetLevelId(self, planViewPlane):
        """
        GetLevelId(self: PlanViewRange, planViewPlane: PlanViewPlane) -> ElementId
        
            Get the element id of the level for a View Depth plane
        
            planViewPlane: The plane whose level will be returned
            Returns: Id of the level
        """
        pass

    def GetOffset(self, planViewPlane):
        """
        GetOffset(self: PlanViewRange, planViewPlane: PlanViewPlane) -> float
        
            Get the offset value associated with a View Depth plane
        
            planViewPlane: View Depth plane
            Returns: Offset value
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PlanViewRange, disposing: bool) """
        pass

    def SetLevelId(self, planViewPlane, id):
        """
        SetLevelId(self: PlanViewRange, planViewPlane: PlanViewPlane, id: ElementId)
            Set the level for a  View Depth plane
        
            planViewPlane: The View Depth plane
            id: Id of the level
        """
        pass

    def SetOffset(self, planViewPlane, offset):
        """
        SetOffset(self: PlanViewRange, planViewPlane: PlanViewPlane, offset: float)
            Set the offset value associated with a View Depth plane
        
            planViewPlane: View Depth plane
            offset: Offset value
        """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PlanViewRange) -> bool

"""


    Current = None
    LevelAbove = None
    LevelBelow = None
    Unlimited = None

