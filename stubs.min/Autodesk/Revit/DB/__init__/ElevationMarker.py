class ElevationMarker(Element, IDisposable):
    """ ElevationMarkers either host elevation ViewSection views or view references. """
    def CreateElevation(self, document, viewPlanId, index):
        """
        CreateElevation(self: ElevationMarker, document: Document, viewPlanId: ElementId, index: int) -> ViewSection
        
            Creates a new elevation ViewSection on the ElevationMarker at the desired index.
        
            document: The document to which the new elevation ViewSection will be added.
            viewPlanId: The id of a ViewPlan in which the ElevationMarker is visible.  The new 
             elevation ViewSection will derive its extents
           and inherit settings from the 
             ViewPlan.
        
            index: The index on the ElevationMarker where the new elevation ViewSection will be 
             placed.
           The index on the ElevationMarker must be valid and unused.
           View 
             direction is determined by the index.
        
            Returns: The new elevation ViewSection.
        """
        pass

    @staticmethod
    def CreateElevationMarker(document, viewFamilyTypeId, origin, initialViewScale):
        """
        CreateElevationMarker(document: Document, viewFamilyTypeId: ElementId, origin: XYZ, initialViewScale: int) -> ElevationMarker
        
            Creates a new ElevationMarker.
        
            document: The document to which the new ElevationMarker will be added.
            viewFamilyTypeId: This ViewFamilyType will be used by all elevations hosted on the new 
             ElevationMarker.
        
            origin: The desired origin for the ElevationMarker.
            initialViewScale: This view scale will be automatically applied to new elevations created on the 
             ElevationMarker.
           The scale is the ratio of true model size to paper size.
        
            Returns: The new ElevationMarker.
        """
        pass

    def CreateReferenceElevation(self, document, index, viewIdToReference):
        """
        CreateReferenceElevation(self: ElevationMarker, document: Document, index: int, viewIdToReference: ElementId)
            Creates a reference elevation on the ElevationMarker at the desired index.
        
            document: The document to which the new reference elevation will be added.
            index: The index on the ElevationMarker where the reference elevation will be placed.
            viewIdToReference: The view which will be referenced.
        """
        pass

    @staticmethod
    def CreateReferenceElevationMarker(document, viewFamilyTypeId, origin, viewPlanId):
        """
        CreateReferenceElevationMarker(document: Document, viewFamilyTypeId: ElementId, origin: XYZ, viewPlanId: ElementId) -> ElevationMarker
        
            Creates a new ElevationMarker.
        
            document: The document to which the new ElevationMarker will be added.
            viewFamilyTypeId: This ViewFamilyType will be used by all elevations hosted on the new 
             ElevationMarker.
        
            origin: The desired origin for the ElevationMarker.
            viewPlanId: The ViewPlan in which the reference ElevationMarker will appear.  Reference 
             ElevationMarkers only appear in one view.
        
            Returns: The new ElevationMarker.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetViewId(self, index):
        """
        GetViewId(self: ElevationMarker, index: int) -> ElementId
        
            Returns the ViewSection id for the index of the ElevationMarker.
        
            index: The index of the ElevationMarker for which a ViewSection id will be returned.
            Returns: ViewSection id of the view at the ElevationMarker index, invalid element id 
             otherwise.
        """
        pass

    def HasElevations(self):
        """
        HasElevations(self: ElevationMarker) -> bool
        
            Returns true if the ElevationMarker has at least one elevation view, false 
             otherwise.
        
            Returns: True if the ElevationMarker has at least one elevation view, false otherwise.
        """
        pass

    def IsAvailableIndex(self, index):
        """
        IsAvailableIndex(self: ElevationMarker, index: int) -> bool
        
            Returns true if a new elevation ViewSection can be placed at %index%, returns 
             false otherwise.
        
        
            index: The index of the ElevationMarker which will be checked.
            Returns: True if an elevation can be created at %index%, false otherwise.
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

    CurrentViewCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current number of views hosted by this ElevationMarker.

Get: CurrentViewCount(self: ElevationMarker) -> int

"""

    IsReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if this is a reference ElevationMarker.
   Only reference elevations can be hosted by reference ElevationMarkers.

Get: IsReference(self: ElevationMarker) -> bool

"""

    MaximumViewCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum number of views that can be hosted by this ElevationMarker.

Get: MaximumViewCount(self: ElevationMarker) -> int

"""


