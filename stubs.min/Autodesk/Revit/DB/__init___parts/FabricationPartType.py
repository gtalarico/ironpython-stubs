class FabricationPartType(ElementType, IDisposable):
    """ Represents a fabrication component type in the Autodesk Revit MEP product. """
    @staticmethod
    def Create(document, button, condition):
        """
        Create(document: Document, button: FabricationServiceButton, condition: int) -> FabricationPartType
        
            Creates a fabrication part type element based on a specific fabrication servic 
             button and condition.
        
        
            document: The document.
            button: The fabrication service button.
            condition: The condition index.
            Returns: The created fabrication part type element.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def Lookup(document, button, condition):
        """
        Lookup(document: Document, button: FabricationServiceButton, condition: int) -> ElementId
        
            Looks up an existing fabrication part type based on a specfic fabrication 
             service button and condition.
        
        
            document: The document.
            button: The fabrication service button.
            condition: The condition index.
            Returns: Identifier of the fabrication part type element or invalidElementId if no 
             fabrication part type exist for the
           specific fabrication service button and 
             condition
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

