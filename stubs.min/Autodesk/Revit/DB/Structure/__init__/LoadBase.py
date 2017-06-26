class LoadBase(Element, IDisposable):
    """ The LoadBase object is the base class for all load objects within the Autodesk Revit API. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def IsOrientToPermitted(self, orientTo):
        """
        IsOrientToPermitted(self: LoadBase, orientTo: LoadOrientTo) -> bool
        
            Indicates if the provided orientation is permitted for this load.
        
            orientTo: Load orientation to check.
            Returns: True if provided orientation type is permitted for this load, false if not.
        """
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

    HostElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The host element for the load.

Get: HostElement(self: LoadBase) -> AnalyticalModel

"""

    HostElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The host element ID for the load.

Get: HostElementId(self: LoadBase) -> ElementId

"""

    IsHosted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the Load is hosted or non-hosted.

Get: IsHosted(self: LoadBase) -> bool

"""

    IsReaction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The load is reaction option.

Get: IsReaction(self: LoadBase) -> bool

Set: IsReaction(self: LoadBase) = value
"""

    LoadCase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The load case for the load.

Get: LoadCase(self: LoadBase) -> LoadCase

"""

    LoadCaseId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The load case ID for the load.

Get: LoadCaseId(self: LoadBase) -> ElementId

Set: LoadCaseId(self: LoadBase) = value
"""

    LoadCaseName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the load case to which this load belongs.

Get: LoadCaseName(self: LoadBase) -> str

"""

    LoadCategoryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the category to which this load belongs.

Get: LoadCategoryName(self: LoadBase) -> str

"""

    LoadNatureName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A string representing the nature of the load.

Get: LoadNatureName(self: LoadBase) -> str

"""

    OrientTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The load orientation option.

Get: OrientTo(self: LoadBase) -> LoadOrientTo

Set: OrientTo(self: LoadBase) = value
"""

    WorkPlaneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the work plane which may determine the orientation of the load.

Get: WorkPlaneId(self: LoadBase) -> ElementId

"""


