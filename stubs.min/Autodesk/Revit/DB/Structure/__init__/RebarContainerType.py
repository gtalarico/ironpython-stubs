class RebarContainerType(ElementType, IDisposable):
    """ Represents a Rebar Container Type, used in the generation of Rebar Container. """
    @staticmethod
    def CreateDefaultRebarContainerType(aDoc):
        """
        CreateDefaultRebarContainerType(aDoc: Document) -> ElementId
        
            Creates a new RebarContainerType object with a default name.
        
            aDoc: The document.
            Returns: The newly created type id.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetOrCreateRebarContainerType(aDoc, name):
        """
        GetOrCreateRebarContainerType(aDoc: Document, name: str) -> ElementId
        
            Creates or returns a RebarContainerType object with a given name.
        
            aDoc: The document.
            name: Name of the type.
            Returns: The type id.
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

