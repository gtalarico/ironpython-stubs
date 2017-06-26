class FilterElement(Element, IDisposable):
    """ The base class for filter elements in the document. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def IsNameUnique(*__args):
        """
        IsNameUnique(self: FilterElement, name: str) -> bool
        
            Determines whether a potential filter element name is unique.
        
            name: The candidate name.
        IsNameUnique(aDocument: Document, name: str) -> bool
        
            Determines whether the given name could be applied to a new FilterElement,
           
             or if it could not be applied because the name is already in use.
        
        
            aDocument: The document in which the name is being tested for uniqueness.
            name: The name tested for uniqueness.
            Returns: Returns true if the name is unique, and false otherwise.
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

