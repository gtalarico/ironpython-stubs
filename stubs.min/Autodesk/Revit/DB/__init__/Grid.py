class Grid(DatumPlane, IDisposable):
    """ Represents a single grid line within Autodesk Revit. """
    @staticmethod
    def Create(document, *__args):
        """
        Create(document: Document, line: Line) -> Grid
        
            Creates a new grid line.
        
            document: The document in which the new instance is created.
            line: A line object which represents the location of the grid line.
            Returns: The newly created grid line.
        Create(document: Document, arc: Arc) -> Grid
        
            Creates a new radial grid line.
        
            document: The document in which the new instance is created.
            arc: An arc object that represents the location of the new grid line.
            Returns: The newly created grid line.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetExtents(self):
        """
        GetExtents(self: Grid) -> Outline
        
            Gets the extents of the grid in the model.
            Returns: The extents are the 3D bounding box surrounding the grid.  The Z coordinates of 
             the box are used by
           Revit to determine if the grid should be displayed in a 
             corresponding view plan (if the grid is linear). The
           extents are not used 
             for arc grids.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetVerticalExtents(self, bottom, top):
        """
        SetVerticalExtents(self: Grid, bottom: float, top: float)
            Adjusts the grid to extend through only the vertical range between bottom and 
             top.
        
        
            bottom: The bottom range of the grid extents.  It must be a valid number and below the 
             top range.
        
            top: The top range of the grid extents.  It must be a valid number and above the 
             bottom range.
        """
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

    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves an object that represents the geometry of the grid line.

Get: Curve(self: Grid) -> Curve

"""

    IsCurved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the grid line is curved or straight.

Get: IsCurved(self: Grid) -> bool

"""


