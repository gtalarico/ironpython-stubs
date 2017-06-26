class RebarShapeMultiplanarDefinition(object, IDisposable):
    """
    A specification for a simple 3D rebar shape.
    
    RebarShapeMultiplanarDefinition(outOfPlaneBendDiameter: float)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeMultiplanarDefinition) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeMultiplanarDefinition, disposing: bool) """
        pass

    def SetPresenceOfSegments(self, isDuplicateShapePresent, isStartConnectorPresent, isEndConnectorPresent):
        """
        SetPresenceOfSegments(self: RebarShapeMultiplanarDefinition, isDuplicateShapePresent: bool, isStartConnectorPresent: bool, isEndConnectorPresent: bool)
            Simultaneously set the presence of all 3D segments.
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

    @staticmethod # known case of __new__
    def __new__(self, outOfPlaneBendDiameter):
        """ __new__(cls: type, outOfPlaneBendDiameter: float) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DepthParamId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the parameter driving the multiplanar depth.
   The depth is measured center-to-center of the bar.
   A valid shape parameter must be assigned to DepthParamId before
   the MultiplanarDefinition can be used in RebarShape creation.

Get: DepthParamId(self: RebarShapeMultiplanarDefinition) -> ElementId

Set: DepthParamId(self: RebarShapeMultiplanarDefinition) = value
"""

    IsDuplicateShapePresent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the shape definition includes an offset
   copy of the 2D shape.

Get: IsDuplicateShapePresent(self: RebarShapeMultiplanarDefinition) -> bool

"""

    IsEndConnectorPresent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether a perpendicular segment is constructed
   from the end of the 2D shape.

Get: IsEndConnectorPresent(self: RebarShapeMultiplanarDefinition) -> bool

"""

    IsStartConnectorPresent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether a perpendicular segment is constructed
   from the start of the 2D shape.

Get: IsStartConnectorPresent(self: RebarShapeMultiplanarDefinition) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarShapeMultiplanarDefinition) -> bool

"""

    OutOfPlaneBendDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bend diameter to be applied to the connector segments.

Get: OutOfPlaneBendDiameter(self: RebarShapeMultiplanarDefinition) -> float

Set: OutOfPlaneBendDiameter(self: RebarShapeMultiplanarDefinition) = value
"""


