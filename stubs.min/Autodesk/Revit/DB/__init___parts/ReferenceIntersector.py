class ReferenceIntersector(object, IDisposable):
    """
    A class used to find and return elements that intersect a ray created from an origin point and direction.
    
    ReferenceIntersector(filter: ElementFilter, targetType: FindReferenceTarget, view3d: View3D)
    ReferenceIntersector(targetElementIds: ICollection[ElementId], targetType: FindReferenceTarget, view3d: View3D)
    ReferenceIntersector(targetElementId: ElementId, targetType: FindReferenceTarget, view3d: View3D)
    ReferenceIntersector(view3d: View3D)
    """
    def Dispose(self):
        """ Dispose(self: ReferenceIntersector) """
        pass

    def Find(self, origin, direction):
        """
        Find(self: ReferenceIntersector, origin: XYZ, direction: XYZ) -> IList[ReferenceWithContext]
        
            Projects a ray from the origin along the given direction, and returns all 
             references from intersected elements which match the ReferenceIntersector's 
             criteria.
        
        
            origin: The origin of the ray.
            direction: The direction of the ray.
            Returns: A collection containing the intersected references.
        """
        pass

    def FindNearest(self, origin, direction):
        """
        FindNearest(self: ReferenceIntersector, origin: XYZ, direction: XYZ) -> ReferenceWithContext
        
            Projects a ray from the origin along the given direction, and returns the 
             nearest reference from intersected elements which match the 
             ReferenceIntersector's criteria.
        
        
            origin: The origin of the ray.
            direction: The direction of the ray.
            Returns: The intersected reference nearest to the ray origin, ll if none is found
        """
        pass

    def GetFilter(self):
        """
        GetFilter(self: ReferenceIntersector) -> ElementFilter
        
            Gets the ElementFilter used in intersection testing.
            Returns: The ElementFilter, or ll if no filter is set.
        """
        pass

    def GetTargetElementIds(self):
        """
        GetTargetElementIds(self: ReferenceIntersector) -> ICollection[ElementId]
        
            Gets the set of ElementIds to test from in intersection testing.
            Returns: The target ElementIds.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ReferenceIntersector, disposing: bool) """
        pass

    def SetFilter(self, filter):
        """
        SetFilter(self: ReferenceIntersector, filter: ElementFilter)
            Sets the ElementFilter used in intersection testing.
        
            filter: The ElementFilter.  Pass ll to remove the existing filter.
        """
        pass

    def SetTargetElementIds(self, elementIds):
        """ SetTargetElementIds(self: ReferenceIntersector, elementIds: ICollection[ElementId]) """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, filter: ElementFilter, targetType: FindReferenceTarget, view3d: View3D)
        __new__(cls: type, targetElementIds: ICollection[ElementId], targetType: FindReferenceTarget, view3d: View3D)
        __new__(cls: type, targetElementId: ElementId, targetType: FindReferenceTarget, view3d: View3D)
        __new__(cls: type, view3d: View3D)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    FindReferencesInRevitLinks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if references inside Revit Links should be found.

Get: FindReferencesInRevitLinks(self: ReferenceIntersector) -> bool

Set: FindReferencesInRevitLinks(self: ReferenceIntersector) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ReferenceIntersector) -> bool

"""

    TargetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of reference to find.

Get: TargetType(self: ReferenceIntersector) -> FindReferenceTarget

Set: TargetType(self: ReferenceIntersector) = value
"""

    ViewId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the 3D view used for evaluation.

Get: ViewId(self: ReferenceIntersector) -> ElementId

Set: ViewId(self: ReferenceIntersector) = value
"""


