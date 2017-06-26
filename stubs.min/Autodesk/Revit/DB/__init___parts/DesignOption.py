class DesignOption(Element, IDisposable):
    """ An element that represents a design alternative. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    @staticmethod
    def GetActiveDesignOptionId(document):
        """
        GetActiveDesignOptionId(document: Document) -> ElementId
        
            Gets the active design option id for the current design option set.
        
            document: The document.
            Returns: The active design option id. It can be invalid id if there is no active design 
             option in the model.
        """
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

    IsPrimary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether this is a primary design option.

Get: IsPrimary(self: DesignOption) -> bool

"""


