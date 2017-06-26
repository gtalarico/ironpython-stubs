class StructuralConnectionSettings(Element, IDisposable):
    """ Provides access to project-wide structural connections settings. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetStructuralConnectionSettings(document):
        """
        GetStructuralConnectionSettings(document: Document) -> StructuralConnectionSettings
        
            Obtains the StructuralConnectionSettings object for the specified project 
             document.
        
        
            document: A project document.
            Returns: The StructuralConnectionSettings object.
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

    IncludeWarningControls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property controls how Structural Connection Element is generated.
   If set to true and warnings are reported for given Element, additional yellow triangle is displayed.

Get: IncludeWarningControls(self: StructuralConnectionSettings) -> bool

Set: IncludeWarningControls(self: StructuralConnectionSettings) = value
"""


