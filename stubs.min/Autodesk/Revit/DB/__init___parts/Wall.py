class Wall(HostObject, IDisposable):
    """ Represents a wall in Autodesk Revit. """
    @staticmethod
    def Create(document, *__args):
        """
        Create(document: Document, curve: Curve, wallTypeId: ElementId, levelId: ElementId, height: float, offset: float, flip: bool, structural: bool) -> Wall
        
            Creates a new rectangular profile wall within the project using the specified 
             wall type, height, and offset.
        
        
            document: The document in which the new wall is created.
            curve: An arc or line representing the base line of the wall.
            wallTypeId: Id of the wall type to be used by the new wall instead of the default type.
            levelId: Id of the level on which the wall is to be placed.
            height: The height of the wall other than the default height.
            offset: Modifies the wall's Base Offset parameter to determine its vertical placement.
            flip: Change which side of the wall is considered to be the inside and outside of the 
             wall.
        
            structural: If set, specifies that the wall is structural in nature.
            Returns: If successful a new wall object within the project.
        Create(document: Document, curve: Curve, levelId: ElementId, structural: bool) -> Wall
        
            Creates a new rectangular profile wall within the project using the default 
             wall style.
        
        
            document: The document in which the new wall is created.
            curve: An arc or line representing the base line of the wall.
            levelId: Id of the level on which the wall is to be placed.
            structural: If set, specifies that the wall is structural in nature.
            Returns: If successful a new wall object within the project.
        Create(document: Document, profile: IList[Curve], structural: bool) -> Wall
        Create(document: Document, profile: IList[Curve], wallTypeId: ElementId, levelId: ElementId, structural: bool, normal: XYZ) -> Wall
        Create(document: Document, profile: IList[Curve], wallTypeId: ElementId, levelId: ElementId, structural: bool) -> Wall
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def Flip(self):
        """
        Flip(self: Wall)
            The wall orientation will be flipped.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetStackedWallMemberIds(self):
        """
        GetStackedWallMemberIds(self: Wall) -> IList[ElementId]
        
            Get the sub walls which belongs to the wall.
            Returns: If the wall is a stacked wall, the Ids of the sub will be returned in 
             bottom-top order.
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

    CurtainGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the grid object of a curtain wall

Get: CurtainGrid(self: Wall) -> CurtainGrid

"""

    Flipped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to test whether the wall orientation is flipped.

Get: Flipped(self: Wall) -> bool

"""

    IsStackedWall = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the wall is a stacked wall.

Get: IsStackedWall(self: Wall) -> bool

"""

    IsStackedWallMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the wall is a member of a stacked wall.

Get: IsStackedWallMember(self: Wall) -> bool

"""

    Orientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The normal vector projected from the exterior side of the wall.

Get: Orientation(self: Wall) -> XYZ

"""

    StackedWallOwnerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stacked wall which contains this stacked wall member.

Get: StackedWallOwnerId(self: Wall) -> ElementId

"""

    StructuralUsage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves or changes  the wall's designated structural usage.

Get: StructuralUsage(self: Wall) -> StructuralWallUsage

Set: StructuralUsage(self: Wall) = value
"""

    WallType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves or changes the type of the wall.

Get: WallType(self: Wall) -> WallType

Set: WallType(self: Wall) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the overall thickness of the wall.

Get: Width(self: Wall) -> float

"""


