class CableTray(CableTrayConduitBase, IDisposable):
    """ This class represents a cable tray in Autodesk Revit. """
    @staticmethod
    def Create(document, cabletrayType, startPoint, endPoint, levelId):
        """
        Create(document: Document, cabletrayType: ElementId, startPoint: XYZ, endPoint: XYZ, levelId: ElementId) -> CableTray
        
            Creates a new instance of cable tray.
        
            document: The document.
            cabletrayType: The cable tray type.  This must be a cable tray type accepted by 
             isValidCableTrayType().
           If the input cable tray type is InvalidElementId, 
             the default cable tray type from the document will be used.
        
            startPoint: The start point of the cable tray location line.
            endPoint: The end point of the cable tray location line.
            levelId: The element id of the level which this cable tray based.
           If the input level 
             id is invalidElementId = -1, the nearest level will be used.
        
            Returns: The newly created cable tray.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetShapeType(self):
        """
        GetShapeType(self: CableTray) -> CableTrayShape
        
            Returns the shape type for the cable tray.
            Returns: The shape type.
        """
        pass

    @staticmethod
    def IsValidCableTrayType(document, cabletrayType):
        """
        IsValidCableTrayType(document: Document, cabletrayType: ElementId) -> bool
        
            Identifies if a cable tray type is valid.
        
            document: The document.
            cabletrayType: The cable tray type.
            Returns: True if the cable tray type is valid, false otherwise.
        """
        pass

    def IsValidRungSpace(self, rungSpace):
        """
        IsValidRungSpace(self: CableTray, rungSpace: float) -> bool
        
            Identifies if the input rung space is valid.
        
            rungSpace: The rung space to check.
            Returns: True if the value is acceptable, false otherwise.
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

    CurveNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The up-direction vector of the cable tray.

Get: CurveNormal(self: CableTray) -> XYZ

Set: CurveNormal(self: CableTray) = value
"""

    RungSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance between two rungs for the ladder cable tray.

Get: RungSpace(self: CableTray) -> float

Set: RungSpace(self: CableTray) = value
"""


