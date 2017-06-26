class ViewSection(View, IDisposable):
    """ ViewSection covers sections, details, elevations, and callouts, all in their reference and non-reference variations. """
    @staticmethod
    def CreateCallout(document, parentViewId, viewFamilyTypeId, point1, point2):
        """
        CreateCallout(document: Document, parentViewId: ElementId, viewFamilyTypeId: ElementId, point1: XYZ, point2: XYZ) -> View
        
            Creates a new callout view.
        
            document: The document to which the new callout will be added.
            parentViewId: The view in which the callout appears.
           Callouts can be created in 
             FloorPlan, CeilingPlan, StructuralPlan, Section, Elevation,
           and Detail 
             views.
        
            viewFamilyTypeId: The id of the ViewFamilyType which will be used by the new callout ViewSection.
             
           Detail ViewFamilyTypes can be used in all parent views except for 
             CeilingPlan and Drafting views.
           FloorPlan, CeilingPlan, StructuralPlan, 
             Section, and Elevation ViewFamilyTypes may be
           be used in parent views that 
             also use a type with the same ViewFamily enum value.
           For example, in 
             StructuralPlan parent views both StructuralPlan and Detail ViewFamilyTypes are 
             allowed.
        
            point1: Determines the extents of the callout symbol in the parent view.
            point2: Determine the extents of the callout symbol in the parent view.
            Returns: The new callout view.  The view will be either a ViewSection, ViewPlan or 
             ViewDetail.
        """
        pass

    @staticmethod
    def CreateDetail(document, viewFamilyTypeId, sectionBox):
        """
        CreateDetail(document: Document, viewFamilyTypeId: ElementId, sectionBox: BoundingBoxXYZ) -> ViewSection
        
            Returns a new detail ViewSection.
        
            document: The document to which the new detail ViewSection will be added.
            viewFamilyTypeId: The id of the ViewFamilyType which will be used by the new detail ViewSection.  
             The type needs to be a Detail ViewFamily.
        
            sectionBox: The BoundingBoxXYZ which specifies the new ViewSection's view direction and 
             extents.
        
            Returns: The new detail ViewSection.
        """
        pass

    @staticmethod
    def CreateReferenceCallout(document, parentViewId, viewIdToReference, point1, point2):
        """
        CreateReferenceCallout(document: Document, parentViewId: ElementId, viewIdToReference: ElementId, point1: XYZ, point2: XYZ)
            Creates a new reference callout.
        
            document: The document to which the new reference callout will be added.
            parentViewId: The view in which the callout symbol appears.
           Callouts can be created in 
             FloorPlan, CeilingPlan, StructuralPlan, Section, Elevation,
           Drafting, and 
             Detail views.
        
            viewIdToReference: The view which will be referenced.  The ViewFamilyType of the referenced view 
             will be used
           by the new reference callout.
           Only cropped views can be 
             referenced, unless the referenced view is a Drafting view.
           Drafting views 
             can always be referenced regardless of the parent view type.
           Elevation 
             views can be referenced from Elevation and Drafting parent views.
           Section 
             views can be referenced from Section and Drafting parent views.
           Detail 
             views can be referenced from all parent views except for in FloorPlan, 
             CeilingPlan and
           StructuralPlan parent views where only 
             horizontally-oriented Detail views can be referenced.
           FloorPlan, 
             CeilingPlan and StructuralPlan views can be referenced from FloorPlan, 
             CeilingPlan
           and StructuralPlan parent views.
        
            point1: One corner of the callout symbol in the parent view.
            point2: The other diagonally opposed corner of the callout symbol in the parent view.
        """
        pass

    @staticmethod
    def CreateReferenceSection(document, parentViewId, viewIdToReference, headPoint, tailPoint):
        """
        CreateReferenceSection(document: Document, parentViewId: ElementId, viewIdToReference: ElementId, headPoint: XYZ, tailPoint: XYZ)
            Creates a new reference section.
        
            document: The document to which the reference section will be added.
            parentViewId: The view in which the new reference section marker will appear.
           Reference 
             sections can be created in FloorPlan, CeilingPlan, StructuralPlan, Section, 
             Elevation,
           Drafting, and Detail views.
        
            viewIdToReference: Detail, Drafting and Section views can be referenced.
           The ViewFamilyType of 
             the referenced view will be used by the new reference section.
        
            headPoint: Determines the location of the section marker's head in the parent view.
            tailPoint: Determines the location of the section marker's tail in the parent view.
        """
        pass

    @staticmethod
    def CreateSection(document, viewFamilyTypeId, sectionBox):
        """
        CreateSection(document: Document, viewFamilyTypeId: ElementId, sectionBox: BoundingBoxXYZ) -> ViewSection
        
            Returns a new section ViewSection.
        
            document: The document to which the new section ViewSection will be added.
            viewFamilyTypeId: The id of the ViewFamilyType which will be used by the new section ViewSection. 
              The type needs to be a Section ViewFamily.
        
            sectionBox: The BoundingBoxXYZ which specifies the new ViewSection's view direction and 
             extents.
        
            Returns: The new section ViewSection.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: View, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def IsParentViewValidForCallout(document, parentViewId):
        """
        IsParentViewValidForCallout(document: Document, parentViewId: ElementId) -> bool
        
            This validator checks that the parent view is appropriate for callout views.
        
            document: The document which contains the ViewFamilyType and parent view.
            parentViewId: The view in which the new callout will appear.
           Callouts can be created in 
             FloorPlan, CeilingPlan, StructuralPlan, Section, Elevation,
           and Detail 
             views.
        
            Returns: True if the ViewFamilyType can be used for callout views in the parent view, 
             false otherwise.
        """
        pass

    @staticmethod
    def IsViewFamilyTypeValidForCallout(document, viewFamilyTypeId, parentViewId):
        """
        IsViewFamilyTypeValidForCallout(document: Document, viewFamilyTypeId: ElementId, parentViewId: ElementId) -> bool
        
            This validator checks that the ViewFamilyType is appropriate for callout views 
             in the
           input parent view.
        
        
            document: The document which contains the ViewFamilyType and parent view.
            viewFamilyTypeId: The id of the ViewFamilyType which will be used by the new callout ViewSection.
             
           Detail ViewFamilyTypes can be used in all parent views except for 
             CeilingPlan and Drafting views.
           FloorPlan, CeilingPlan, StructuralPlan, 
             Section, Elevation, and Detail ViewFamilyTypes may be
           be used in parent 
             views that also use a type with the same ViewFamily enum value.
           For 
             example, in StructuralPlan views both StructuralPlan and Detail ViewFamilyTypes 
             are allowed.
        
            parentViewId: The view in which the new callout will appear.
           Callouts can be created in 
             FloorPlan, CeilingPlan, StructuralPlan, Section, Elevation,
           and Detail 
             views.
        
            Returns: True if the ViewFamilyType can be used for callout views in the parent view, 
             false otherwise.
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

