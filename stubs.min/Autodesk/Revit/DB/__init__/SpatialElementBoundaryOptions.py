class SpatialElementBoundaryOptions(object, IDisposable):
    """
    Options that can be passed to a SpatialElementBoundaryCalculator to influence the results of the calculation.
    
    SpatialElementBoundaryOptions()
    """
    def Dispose(self):
        """ Dispose(self: SpatialElementBoundaryOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SpatialElementBoundaryOptions, disposing: bool) """
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

Get: IsValidObject(self: SpatialElementBoundaryOptions) -> bool

"""

    SpatialElementBoundaryLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The boundary of spatial element for geometry calculation.

Get: SpatialElementBoundaryLocation(self: SpatialElementBoundaryOptions) -> SpatialElementBoundaryLocation

Set: SpatialElementBoundaryLocation(self: SpatialElementBoundaryOptions) = value
"""

    StoreFreeBoundaryFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether to include the free boundary faces in the result.

Get: StoreFreeBoundaryFaces(self: SpatialElementBoundaryOptions) -> bool

Set: StoreFreeBoundaryFaces(self: SpatialElementBoundaryOptions) = value
"""


