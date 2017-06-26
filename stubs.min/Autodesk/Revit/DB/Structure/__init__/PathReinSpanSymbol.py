class PathReinSpanSymbol(IndependentTag, IDisposable):
    """ Represents a Path Reinforcement Span Symbol element in Autodesk Revit. """
    @staticmethod
    def Create(document, viewId, hostId, point, symbolId):
        """
        Create(document: Document, viewId: ElementId, hostId: LinkElementId, point: XYZ, symbolId: ElementId) -> PathReinSpanSymbol
        
            Creates a new instance of PathReinSpanSymbol in the project.
        
            document: The document.
            viewId: The id of the view in which the symbol should appear.
            hostId: The ElementId of PathReinforcement (either in the document, or linked from 
             another document).
        
            point: The span symbol's head position.
            symbolId: The family symbol id of this element.
            Returns: A reference to newly created span symbol.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
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

