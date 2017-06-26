class InsulationLiningBase(MEPCurve, IDisposable):
    """ Acts as the base class for duct insulation, pipe insulation and duct lining elements. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetInsulationIds(document, elemId):
        """
        GetInsulationIds(document: Document, elemId: ElementId) -> ICollection[ElementId]
        
            Returns the ids of the insulation elements associated to a given element.
        
            document: The document.
            elemId: The element.
            Returns: A collection of the ids of the insulation elements.
        """
        pass

    @staticmethod
    def GetLiningIds(document, elemId):
        """
        GetLiningIds(document: Document, elemId: ElementId) -> ICollection[ElementId]
        
            Returns the ids of the lining elements associated to a given element.
        
            document: The document.
            elemId: The element.
            Returns: A collection of the ids of the lining elements.
        """
        pass

    @staticmethod
    def IsValidThickness(thickness):
        """
        IsValidThickness(thickness: float) -> bool
        
            Identifies if the given thickness value is valid for assignment to insulation 
             or lining elements.
        
        
            thickness: Thickness of the insulation and lining elements.
            Returns: True if the thickness is valid, false otherwise.
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

    HostElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the host element for the insulation or lining element.

Get: HostElementId(self: InsulationLiningBase) -> ElementId

"""

    Thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Thickness of the insulation or lining element.

Get: Thickness(self: InsulationLiningBase) -> float

Set: Thickness(self: InsulationLiningBase) = value
"""


