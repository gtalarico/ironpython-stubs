class MultiSegmentGrid(Element, IDisposable):
    """
    This element acts as a multi-segmented Grid. The individual grids associated to
       the MultiSegmentGrid behave as a single unit and all share the same text. They inherit
       their type (GridType) from the MultiSegmentGrid.
    """
    @staticmethod
    def AreGridsInSameMultiSegmentGrid(grid1, grid2):
        """
        AreGridsInSameMultiSegmentGrid(grid1: Grid, grid2: Grid) -> bool
        
            Determine whether two Grids are members of the same GridChain.
        
            grid1: A Grid.
            grid2: A Grid.
            Returns: Returns true if both of the specified Grids are associated to the same 
             MultiSegmentGrid,
           i.e. getMultiSegementGridId returns the same valid 
             element id for both Grids.
        """
        pass

    @staticmethod
    def Create(document, typeId, curveLoop, sketchPlaneId):
        """
        Create(document: Document, typeId: ElementId, curveLoop: CurveLoop, sketchPlaneId: ElementId) -> ElementId
        
            Create a MultiSegmentGrid element from the specified curve loop.
        
            document: The document in which to create the MultiSegmentGrid.
            typeId: Element id of a GridType element.
            curveLoop: An open curve loop consisting of lines and arcs.
            sketchPlaneId: Element id of a SketchPlane for the curves elements that will be created from 
             the curveLoop.
        
            Returns: The element id of the new MultiSegmentGrid element.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetGridIds(self):
        """
        GetGridIds(self: MultiSegmentGrid) -> ICollection[ElementId]
        
            Get the element ids of the Grids that make up this MultiSegmentGrid.
            Returns: Element ids of Grids that make up this MultiSegmentGrid.
        """
        pass

    @staticmethod
    def GetMultiSegementGridId(grid):
        """
        GetMultiSegementGridId(grid: Grid) -> ElementId
        
            Retrieve the element id of the MultiSegmentGrid of which the specified Grid is 
             a member.
        
        
            grid: A Grid.
            Returns: The element id of the associated GridChain. If the Grid is not associated to a 
             GridChain,
           this will return invalidElementId.
        """
        pass

    @staticmethod
    def IsValidCurveLoop(curveLoop):
        """
        IsValidCurveLoop(curveLoop: CurveLoop) -> bool
        
            Identifies whether the specified curve loop is valid for creation of a 
             MultiSegmentGrid.
        
        
            curveLoop: The curve loop.
            Returns: True if the curve loop is an open curve loop consisting of lines and arcs, and 
             false otherwise.
        """
        pass

    @staticmethod
    def IsValidSketchPlaneId(document, elemId):
        """
        IsValidSketchPlaneId(document: Document, elemId: ElementId) -> bool
        
            Identifies whether provided element id corresponds to a SketchPlane that is 
             valid for GridChain creation.
        
        
            document: The document.
            elemId: Element id.
            Returns: True if elemId is the element id of a horizontal SketchPlane.
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

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name shared by grids in this MultiSegmentGrid

Get: Text(self: MultiSegmentGrid) -> str

Set: Text(self: MultiSegmentGrid) = value
"""


