class SharedParameterElement(ParameterElement, IDisposable):
    """ An element that stores the definition of a shared parameter which is loaded into the document. """
    @staticmethod
    def Create(document, sharedParameterDefinition):
        """
        Create(document: Document, sharedParameterDefinition: ExternalDefinition) -> SharedParameterElement
        
            Creates a new shared parameter element in the document representing the 
             parameter stored in the input ExternalDefinition.
        
        
            document: The document.
            sharedParameterDefinition: Shared parameter definition.
            Returns: The newly created shared parameter instance.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def Lookup(document, guidValue):
        """
        Lookup(document: Document, guidValue: Guid) -> SharedParameterElement
        
            Finds the shared parameter element that corresponds to the given Guid.
        
            document: The document.
            guidValue: Shared parameter Guid.
            Returns: The retrieved shared parameter instance, or ll if the matching element is not 
             found.
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

    GuidValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Guid that identifies this shared parameter.

Get: GuidValue(self: SharedParameterElement) -> Guid

"""


