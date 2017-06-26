class CableTraySettings(Element, IDisposable):
    """ The cable tray settings. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetCableTraySettings(document):
        """
        GetCableTraySettings(document: Document) -> CableTraySettings
        
            Gets the cable tray settings of the project.
        
            document: The document.
            Returns: The cable tray settings of the project.
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

    ConnectorSeparator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The cable tray connector separator string.

Get: ConnectorSeparator(self: CableTraySettings) -> str

Set: ConnectorSeparator(self: CableTraySettings) = value
"""

    FittingAnnotationSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of fitting annotation size.

Get: FittingAnnotationSize(self: CableTraySettings) -> float

Set: FittingAnnotationSize(self: CableTraySettings) = value
"""

    RiseDropAnnotationSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rise drop annotation size.

Get: RiseDropAnnotationSize(self: CableTraySettings) -> float

Set: RiseDropAnnotationSize(self: CableTraySettings) = value
"""

    SizeSeparator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The cable tray size separator string.

Get: SizeSeparator(self: CableTraySettings) -> str

Set: SizeSeparator(self: CableTraySettings) = value
"""

    SizeSuffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The cable tray size suffix string.

Get: SizeSuffix(self: CableTraySettings) -> str

Set: SizeSuffix(self: CableTraySettings) = value
"""

    UseAnnotationScaleForSingleLineFittings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether use annotation scale for single line fittings or not.

Get: UseAnnotationScaleForSingleLineFittings(self: CableTraySettings) -> bool

Set: UseAnnotationScaleForSingleLineFittings(self: CableTraySettings) = value
"""


