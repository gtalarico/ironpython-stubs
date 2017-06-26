class MEPSystemType(ElementType, IDisposable):
    """ A system type in the Autodesk Revit MEP product. """
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

    Abbreviation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the abbreviation, the short name, for the system type

Get: Abbreviation(self: MEPSystemType) -> str

Set: Abbreviation(self: MEPSystemType) = value
"""

    CalculationLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the calculation level for the system type.

Get: CalculationLevel(self: MEPSystemType) -> SystemCalculationLevel

Set: CalculationLevel(self: MEPSystemType) = value
"""

    LineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the color that should override the line color for all components in the system.

Get: LineColor(self: MEPSystemType) -> Color

Set: LineColor(self: MEPSystemType) = value
"""

    LinePatternId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the line pattern color that should override the line color for all components in the system.

Get: LinePatternId(self: MEPSystemType) -> ElementId

Set: LinePatternId(self: MEPSystemType) = value
"""

    LineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the weight that should override the line weight for all components in the system.

Get: LineWeight(self: MEPSystemType) -> int

Set: LineWeight(self: MEPSystemType) = value
"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the material id that should override the material for all components in the system.

Get: MaterialId(self: MEPSystemType) -> ElementId

Set: MaterialId(self: MEPSystemType) = value
"""

    SystemClassification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the classification for the system type

Get: SystemClassification(self: MEPSystemType) -> MEPSystemClassification

"""


