class StructuralConnectionApprovalType(ElementType, IDisposable):
    """ A type element that represents a connection approval type. """
    @staticmethod
    def Create(doc, name):
        """
        Create(doc: Document, name: str) -> StructuralConnectionApprovalType
        
            Creates a new StructuralConnectionApprovalType.
        
            name: A name for the new approval type. It must be unique within the document.
            Returns: Created connection approval type.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    @staticmethod
    def GetAllStructuralConnectionApprovalTypes(cda, ids):
        """ GetAllStructuralConnectionApprovalTypes(cda: Document) -> ICollection[ElementId] """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def IsValidApprovalTypeName(doc, name):
        """
        IsValidApprovalTypeName(doc: Document, name: str) -> bool
        
            Verifies if the provided approval name is unique in the document.
            Returns: True if approval type name is unique.
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

