class FillPattern(object, IDisposable):
    """
    Represents a fill pattern object.
    
    FillPattern(name: str, target: FillPatternTarget, orientation: FillPatternHostOrientation, angle: float, spacing1: float, spacing2: float)
    FillPattern(name: str, target: FillPatternTarget, orientation: FillPatternHostOrientation, angle: float, spacing1: float)
    FillPattern(name: str, target: FillPatternTarget, orientation: FillPatternHostOrientation)
    FillPattern()
    FillPattern(other: FillPattern)
    """
    def Dispose(self):
        """ Dispose(self: FillPattern) """
        pass

    def ExpandDots(self):
        """
        ExpandDots(self: FillPattern) -> bool
        
            Corrects pattern dots to make them be drawn properly for Revit.
            Returns: Indicates whether any dots were in fact expanded.
        """
        pass

    def GetFillGrid(self, gridIdx):
        """
        GetFillGrid(self: FillPattern, gridIdx: int) -> FillGrid
        
            Gets the specified fill grid.
        
            gridIdx: The index of the fill grid.
            Returns: The fill grid.
        """
        pass

    def GetFillGrids(self):
        """
        GetFillGrids(self: FillPattern) -> IList[FillGrid]
        
            Gets all fill grids in this fill pattern
            Returns: The fill grids.
        """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: FillPattern, other: FillPattern) -> bool
        
            Check if the contents in two fill patterns are equal.
        
            other: The fill pattern to be compared.
            Returns: True for equal, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FillPattern, disposing: bool) """
        pass

    def SetFillGrid(self, gridIdx, fillGrid):
        """
        SetFillGrid(self: FillPattern, gridIdx: int, fillGrid: FillGrid)
            Sets the fill grid.
        
            gridIdx: The index of the fill grid.
            fillGrid: The fill grid to be used.
        """
        pass

    def SetFillGrids(self, fillGrids):
        """ SetFillGrids(self: FillPattern, fillGrids: IList[FillGrid]) """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str, target: FillPatternTarget, orientation: FillPatternHostOrientation, angle: float, spacing1: float, spacing2: float)
        __new__(cls: type, name: str, target: FillPatternTarget, orientation: FillPatternHostOrientation, angle: float, spacing1: float)
        __new__(cls: type, name: str, target: FillPatternTarget, orientation: FillPatternHostOrientation)
        __new__(cls: type)
        __new__(cls: type, other: FillPattern)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    GridCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count of the fill grids in this fill pattern.

Get: GridCount(self: FillPattern) -> int

"""

    HostOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Orientation to host layer.

Get: HostOrientation(self: FillPattern) -> FillPatternHostOrientation

Set: HostOrientation(self: FillPattern) = value
"""

    IsSolidFill = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Check if the fill pattern is a solid fill pattern.

Get: IsSolidFill(self: FillPattern) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FillPattern) -> bool

"""

    LengthPerArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets length of all lines that placed on unit area.

Get: LengthPerArea(self: FillPattern) -> float

"""

    LinesPerLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of solid lines that placed in unit length.

Get: LinesPerLength(self: FillPattern) -> float

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the fill pattern.

Get: Name(self: FillPattern) -> str

Set: Name(self: FillPattern) = value
"""

    StrokesPerArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of strokes that placed on unit area.

Get: StrokesPerArea(self: FillPattern) -> float

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Target of this fill pattern applied to.

Get: Target(self: FillPattern) -> FillPatternTarget

Set: Target(self: FillPattern) = value
"""


