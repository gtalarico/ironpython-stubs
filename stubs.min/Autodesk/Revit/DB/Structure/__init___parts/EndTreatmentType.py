class EndTreatmentType(ElementType, IDisposable):
    """ An end treatment type object that is used to hold information about the end treatment applied to bars that are connected to a coupler. """
    @staticmethod
    def Create(doc, strTreatment=None):
        """
        Create(doc: Document) -> EndTreatmentType
        
            Creates a new EndTreatmentType in a document.
        Create(doc: Document, strTreatment: str) -> EndTreatmentType
        
            Creates a new EndTreatmentType in a document and adds the input string to the 
             endTreatment parameter.
        """
        pass

    @staticmethod
    def CreateDefaultEndTreatmentType(ADoc):
        """
        CreateDefaultEndTreatmentType(ADoc: Document) -> ElementId
        
            Creates a new EndTreatmentType object with a default name.
        
            ADoc: The document.
            Returns: The newly created type id.
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

    EndTreatment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """String describing the end treatment

Get: EndTreatment(self: EndTreatmentType) -> str

Set: EndTreatment(self: EndTreatmentType) = value
"""


