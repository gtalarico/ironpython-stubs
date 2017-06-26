class Conduit(CableTrayConduitBase, IDisposable):
    """ This class represents a conduit in Autodesk Revit. """
    @staticmethod
    def Create(document, conduitType, startPoint, endPoint, levelId):
        """
        Create(document: Document, conduitType: ElementId, startPoint: XYZ, endPoint: XYZ, levelId: ElementId) -> Conduit
        
            Creates a new instance of conduit.
        
            document: The document.
            conduitType: The conduit type.  This must be a conduit type accepted by 
             isValidConduitType().
           If the input conduit type is InvalidElementId, the 
             default conduit type from the document will be used.
        
            startPoint: The start point of the conduit location line.
            endPoint: The end point of the conduit location line.
            levelId: The element id of the level which this conduit based.
           If the input level id 
             is invalidElementId = -1, the nearest level will be used.
        
            Returns: The newly created conduit.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def IsValidConduitType(document, conduitType):
        """
        IsValidConduitType(document: Document, conduitType: ElementId) -> bool
        
            Identifies if a conduit type is valid.
        
            document: The document.
            conduitType: The conduit type.
            Returns: True if the conduit type is valid, false otherwise.
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

