class RebarCoverType(ElementType, IDisposable):
    """ A named value for a clear cover distance. """
    @staticmethod
    def Create(doc, name, coverDistance):
        """
        Create(doc: Document, name: str, coverDistance: float) -> RebarCoverType
        
            Creates a new CoverType in the document.
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

    CoverDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A distance that can be used as a concrete cover value in a document.

Get: CoverDistance(self: RebarCoverType) -> float

Set: CoverDistance(self: RebarCoverType) = value
"""


