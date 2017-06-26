class CurtainGrid(APIObject, IDisposable):
    """ Represents a curtain grid element within Autodesk Revit. """
    def AddGridLine(self, isUGridLine, position, oneSegmentOnly):
        """
        AddGridLine(self: CurtainGrid, isUGridLine: bool, position: XYZ, oneSegmentOnly: bool) -> CurtainGridLine
        
            Add a grid line to the curtain grid.
        
            isUGridLine: If true, a U-direction grid line will be added. Otherwise, a V-direction grid 
             line will be added.
        
            position: The position of the grid line.
            oneSegmentOnly: If it is true, only one segment is added. Otherwise, all segments will be added 
             for the grid line.
        
            Returns: The created grid line is returned if the operation is successful. Otherwise, ll 
             is returned.
        """
        pass

    def ChangePanelType(self, panel, newSymbol):
        """
        ChangePanelType(self: CurtainGrid, panel: Element, newSymbol: ElementType) -> Element
        
            Change the type of a curtain panel.
        
            panel: The panel to be changed, it can be a type of Autodesk.Revit.DB.Panel or 
             Autodesk.Revit.DB.Wall.
        
            newSymbol: The new symbol, it may be of Autodesk.Revit.DB.PanelType or 
             Autodesk.Revit.DB.WallType when the panel is hosted in a curtain wall. 
        The 
             new symbol can only be of type Autodesk.Revit.DB.PanelType if the Panel is 
             hosted in a curtain system.
        
            Returns: If operation succeeds, the modified panel element is returned.
        """
        pass

    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def GetCell(self, uGridLineId, vGridLineId):
        """
        GetCell(self: CurtainGrid, uGridLineId: ElementId, vGridLineId: ElementId) -> CurtainCell
        
            Get the specified cell located by the intersection of the grid lines.
        
            uGridLineId: The id of a grid line in the U-direction used to locate the cell.
            vGridLineId: The id of a grid line in the V-direction used to locate the cell.
            Returns: The cell.
        """
        pass

    def GetCurtainCells(self):
        """
        GetCurtainCells(self: CurtainGrid) -> ICollection[CurtainCell]
        
            Gets the CurtainCells owned by this curtain grid.
            Returns: The CurtainCells owned by this curtain grid.
        """
        pass

    def GetMullionIds(self):
        """
        GetMullionIds(self: CurtainGrid) -> ICollection[ElementId]
        
            Gets all ElementIds of the mullions of the curtain grid.
            Returns: The mullion ElementIds
        """
        pass

    def GetPanel(self, uGridLineId, vGridLineId):
        """
        GetPanel(self: CurtainGrid, uGridLineId: ElementId, vGridLineId: ElementId) -> Panel
        
            Get the specified panel located by the intersection of the grid lines.
        
            uGridLineId: The id of a grid line in the U-direction used to locate the panel.
            vGridLineId: The id of a grid line in the V-direction used to locate the panel.
            Returns: The panel, or ll if the panel cannot be found at this intersection.
        """
        pass

    def GetPanelIds(self):
        """
        GetPanelIds(self: CurtainGrid) -> ICollection[ElementId]
        
            Gets all ElementIds of the panels of the curtain grid.
            Returns: The panel ElementIds
        """
        pass

    def GetUGridLineIds(self):
        """
        GetUGridLineIds(self: CurtainGrid) -> ICollection[ElementId]
        
            Gets all ElementIds of grid lines in the U direction.
            Returns: The U grid line ElementIds
        """
        pass

    def GetUnlockedMullionIds(self):
        """
        GetUnlockedMullionIds(self: CurtainGrid) -> ICollection[ElementId]
        
            Gets all ElementIds of the unlocked mullions of the curtain grid.
            Returns: The unlocked mullion ElementIds
        """
        pass

    def GetUnlockedPanelIds(self):
        """
        GetUnlockedPanelIds(self: CurtainGrid) -> ICollection[ElementId]
        
            Gets all ElementIds of the unlocked panels of the curtain grid.
            Returns: The unlocked panel ElementIds
        """
        pass

    def GetVGridLineIds(self):
        """
        GetVGridLineIds(self: CurtainGrid) -> ICollection[ElementId]
        
            Gets all ElementIds of grid lines in the V direction.
            Returns: The V grid line ElementIds
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: CurtainGrid) """
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

    Grid1Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The angle for the U grid line pattern of the curtain grid.

Get: Grid1Angle(self: CurtainGrid) -> float

Set: Grid1Angle(self: CurtainGrid) = value
"""

    Grid1Justification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The justification for the U grid line pattern of the curtain grid.

Get: Grid1Justification(self: CurtainGrid) -> CurtainGridAlignType

Set: Grid1Justification(self: CurtainGrid) = value
"""

    Grid1Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset for the U grid line pattern of the curtain grid.

Get: Grid1Offset(self: CurtainGrid) -> float

Set: Grid1Offset(self: CurtainGrid) = value
"""

    Grid2Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The angle for V grid line pattern of the curtain grid.

Get: Grid2Angle(self: CurtainGrid) -> float

Set: Grid2Angle(self: CurtainGrid) = value
"""

    Grid2Justification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The justification for the V grid line pattern of the curtain grid.

Get: Grid2Justification(self: CurtainGrid) -> CurtainGridAlignType

Set: Grid2Justification(self: CurtainGrid) = value
"""

    Grid2Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset for V grid line pattern of the curtain grid.

Get: Grid2Offset(self: CurtainGrid) -> float

Set: Grid2Offset(self: CurtainGrid) = value
"""

    NumPanels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of panels.

Get: NumPanels(self: CurtainGrid) -> int

"""

    NumULines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the number of grid lines in the U direction.

Get: NumULines(self: CurtainGrid) -> int

"""

    NumVLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the number of grid lines in the V direction.

Get: NumVLines(self: CurtainGrid) -> int

"""


