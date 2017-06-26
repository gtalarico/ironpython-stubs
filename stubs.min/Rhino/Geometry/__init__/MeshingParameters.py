class MeshingParameters(object, IDisposable):
    """ MeshingParameters() """
    def Dispose(self):
        """ Dispose(self: MeshingParameters) """
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

    ComputeCurvature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComputeCurvature(self: MeshingParameters) -> bool

Set: ComputeCurvature(self: MeshingParameters) = value
"""

    GridAmplification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridAmplification(self: MeshingParameters) -> float

Set: GridAmplification(self: MeshingParameters) = value
"""

    GridAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridAngle(self: MeshingParameters) -> float

Set: GridAngle(self: MeshingParameters) = value
"""

    GridAspectRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridAspectRatio(self: MeshingParameters) -> float

Set: GridAspectRatio(self: MeshingParameters) = value
"""

    GridMaxCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridMaxCount(self: MeshingParameters) -> int

Set: GridMaxCount(self: MeshingParameters) = value
"""

    GridMinCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridMinCount(self: MeshingParameters) -> int

Set: GridMinCount(self: MeshingParameters) = value
"""

    JaggedSeams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JaggedSeams(self: MeshingParameters) -> bool

Set: JaggedSeams(self: MeshingParameters) = value
"""

    MaximumEdgeLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumEdgeLength(self: MeshingParameters) -> float

Set: MaximumEdgeLength(self: MeshingParameters) = value
"""

    MinimumEdgeLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumEdgeLength(self: MeshingParameters) -> float

Set: MinimumEdgeLength(self: MeshingParameters) = value
"""

    MinimumTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumTolerance(self: MeshingParameters) -> float

Set: MinimumTolerance(self: MeshingParameters) = value
"""

    RefineAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefineAngle(self: MeshingParameters) -> float

Set: RefineAngle(self: MeshingParameters) = value
"""

    RefineGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefineGrid(self: MeshingParameters) -> bool

Set: RefineGrid(self: MeshingParameters) = value
"""

    RelativeTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeTolerance(self: MeshingParameters) -> float

Set: RelativeTolerance(self: MeshingParameters) = value
"""

    SimplePlanes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SimplePlanes(self: MeshingParameters) -> bool

Set: SimplePlanes(self: MeshingParameters) = value
"""

    Tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tolerance(self: MeshingParameters) -> float

Set: Tolerance(self: MeshingParameters) = value
"""


