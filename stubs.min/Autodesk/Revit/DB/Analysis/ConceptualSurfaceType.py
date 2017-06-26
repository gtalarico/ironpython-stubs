class ConceptualSurfaceType(Element, IDisposable):
    """
    This element represents a conceptual BIM object category to assign to faces in Mass geometries.
       There is one ConceptualSurfaceType element for each of the Mass Surface Subcategories.
       for serialization
    """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    @staticmethod
    def GetAllMassSubCategoryIds():
        """
        GetAllMassSubCategoryIds() -> IList[ElementId]
        
            Get all the mass subcategory ids for which there are ConceptualSurfaceType's.
            Returns: Returns an array of element id of mass subcategories for which there are 
             ConceptualSurfaceType's.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetByMassSubCategoryId(cda, massSubCategoryId):
        """
        GetByMassSubCategoryId(cda: Document, massSubCategoryId: ElementId) -> ConceptualSurfaceType
        
            Get the ConceptualSurfaceType by its mass subcategory id.
        
            cda: The document.
            massSubCategoryId: The mass subcategory id to get the ConceptualSurfaceType for.
            Returns: Returns ConceptualSurfaceType associated with input id or NULL.
        """
        pass

    def GetConstructionTypeIds(self):
        """
        GetConstructionTypeIds(self: ConceptualSurfaceType) -> ICollection[ElementId]
        
            The element ids of the ConceptualConstructionType's associated with this 
             ConceptualSurfaceType.
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

    DefaultConstructionTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element id of the user specified ConceptualConstructionType to be used by default on creation for mass faces of this mass subcategory.

Get: DefaultConstructionTypeId(self: ConceptualSurfaceType) -> ElementId

Set: DefaultConstructionTypeId(self: ConceptualSurfaceType) = value
"""

    MassSubCategoryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mass subcategory id of the ConceptualSurfaceType.

Get: MassSubCategoryId(self: ConceptualSurfaceType) -> ElementId

"""


