class FamilyInstance(Instance, IDisposable):
    """ This object represents a single instance of a family type, such as a single I beam. """
    def AddCoping(self, cutter):
        """
        AddCoping(self: FamilyInstance, cutter: FamilyInstance) -> bool
        
            Adds a coping (cut) to a steel beam.
        
            cutter: A steel beam or column. May not be ll or itself.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def flipFacing(self):
        """
        flipFacing(self: FamilyInstance) -> bool
        
            The orientation of family instance facing will be flipped. If it can not be 
             flipped, return false, otherwise return true.
        """
        pass

    def FlipFromToRoom(self):
        """
        FlipFromToRoom(self: FamilyInstance)
            Flips the settings of "From Room" and "To Room" for the door or window instance.
        """
        pass

    def flipHand(self):
        """
        flipHand(self: FamilyInstance) -> bool
        
            The orientation of family instance hand will be flipped. If it can not be 
             flipped, return false, otherwise return true.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCopingIds(self):
        """
        GetCopingIds(self: FamilyInstance) -> ICollection[ElementId]
        
            Lists the elements currently used as coping cutters for this element.
            Returns: The coping ElementIds
        """
        pass

    def GetFamilyPointPlacementReferences(self):
        """
        GetFamilyPointPlacementReferences(self: FamilyInstance) -> IList[FamilyPointPlacementReference]
        
            Returns the Point Placement References for the Family Instance.
        """
        pass

    def GetOriginalGeometry(self, options):
        """
        GetOriginalGeometry(self: FamilyInstance, options: Options) -> GeometryElement
        
            Returns the original geometry of the instance, before the instance is modified 
             by 
        joins, cuts, coping, extensions, or other post-processing.
        
        
            options: The options used to obtain the geometry.  Note that ComputeReferences may not
        
             be set to true.
        """
        pass

    def GetSpatialElementCalculationPoint(self):
        """
        GetSpatialElementCalculationPoint(self: FamilyInstance) -> XYZ
        
            Gets the location of the calculation point for this instance.
            Returns: A 3d point.
        """
        pass

    def GetSpatialElementFromToCalculationPoints(self):
        """
        GetSpatialElementFromToCalculationPoints(self: FamilyInstance) -> IList[XYZ]
        
            Gets the locations for the calculation points for this instance.
            Returns: A list of 3d points.
        """
        pass

    def GetSubComponentIds(self):
        """
        GetSubComponentIds(self: FamilyInstance) -> ICollection[ElementId]
        
            Gets the sub component ElementIds of the current family instance.
            Returns: The subcomponent ElementIDs
        """
        pass

    def GetSweptProfile(self):
        """
        GetSweptProfile(self: FamilyInstance) -> SweptProfile
        
            Gets the object that describes the profile that is swept along the driving 
             curve for this instance.
        
            Returns: A swept profile.
        """
        pass

    def HasModifiedGeometry(self):
        """
        HasModifiedGeometry(self: FamilyInstance) -> bool
        
            Identifies if the geometry of this FamilyInstance 
        has been modified from the 
             automatically generated default.
        """
        pass

    def HasSweptProfile(self):
        """
        HasSweptProfile(self: FamilyInstance) -> bool
        
            Indicates if this instance can be represented as a swept profile.
            Returns: True if the instance can be represented as a swept profile, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveCoping(self, cutter):
        """
        RemoveCoping(self: FamilyInstance, cutter: FamilyInstance) -> bool
        
            Removes a coping (cut) from a steel beam.
        
            cutter: A steel beam or column for which this beam currently has a coping cut. May not 
             be ll or itself.
        """
        pass

    def rotate(self):
        """
        rotate(self: FamilyInstance) -> bool
        
            The family instance will be flipped by 180 degrees. If it can not be rotated, 
             return false, otherwise return true.
        """
        pass

    def SetCopingIds(self, cutters):
        """ SetCopingIds(self: FamilyInstance, cutters: ICollection[ElementId]) -> bool """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def Split(self, param):
        """
        Split(self: FamilyInstance, param: float) -> ElementId
        
            Splits the family instance element at a point on its defining curve.
        
            param: The normalized parameter value along the element (should be greater than 0 and 
             less than 1).
        
            Returns: The newly created family instance id.
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

    CanFlipFacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to test whether the orientation of family instance facing can be flipped.

Get: CanFlipFacing(self: FamilyInstance) -> bool

"""

    CanFlipHand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to test whether the orientation of family instance hand can be flipped.

Get: CanFlipHand(self: FamilyInstance) -> bool

"""

    CanFlipWorkPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the instance can flip its work plane.

Get: CanFlipWorkPlane(self: FamilyInstance) -> bool

"""

    CanRotate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to test whether the family instance can be rotated by 180 degrees.

Get: CanRotate(self: FamilyInstance) -> bool

"""

    CanSplit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies whether a particular family instance can be split at a point on it's defining curve (by Autodesk.Revit.DB.FamilyInstance.Split(System.Double)).

Get: CanSplit(self: FamilyInstance) -> bool

"""

    ExtensionUtility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to check whether the instance can be extended and return the interface for extension operation.

Get: ExtensionUtility(self: FamilyInstance) -> IExtension

"""

    FacingFlipped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to test whether the orientation of family instance facing is flipped.

Get: FacingFlipped(self: FamilyInstance) -> bool

"""

    FacingOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to get the orientation of family instance facing.

Get: FacingOrientation(self: FamilyInstance) -> XYZ

"""

    HandFlipped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to test whether the orientation of family instance hand is flipped.

Get: HandFlipped(self: FamilyInstance) -> bool

"""

    HandOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to get the orientation of family instance hand.

Get: HandOrientation(self: FamilyInstance) -> XYZ

"""

    HasSpatialElementCalculationPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if this instance has a single SpatialElementCalculationPoint used as the search point for Revit to identify if the instance is inside a room or space.

Get: HasSpatialElementCalculationPoint(self: FamilyInstance) -> bool

"""

    HasSpatialElementFromToCalculationPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if this instance has a pair of SpatialElementCalculationPoints used as the search points for Revit to identify if the instance lies between up to two rooms or spaces.

Get: HasSpatialElementFromToCalculationPoints(self: FamilyInstance) -> bool

"""

    Host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If the instance is contained within another element, this property returns the containing
element. An instance that is face hosted will return the element containing the face.

Get: Host(self: FamilyInstance) -> Element

"""

    HostFace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to get the reference to the host face of family instance.

Get: HostFace(self: FamilyInstance) -> Reference

"""

    HostParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If the instance is hosted by a wall, this property returns the parameter value of the insertion
point of the instance along the wall's location curve, as long as the family of the instance isn't work plane based.

Get: HostParameter(self: FamilyInstance) -> float

"""

    Invisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to test whether the family instance is invisible.

Get: Invisible(self: FamilyInstance) -> bool

"""

    IsSlantedColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the family instance is a slanted column.

Get: IsSlantedColumn(self: FamilyInstance) -> bool

"""

    IsWorkPlaneFlipped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the instance's work plane is flipped.

Get: IsWorkPlaneFlipped(self: FamilyInstance) -> bool

Set: IsWorkPlaneFlipped(self: FamilyInstance) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is used to find the physical location of an instance within project.

Get: Location(self: FamilyInstance) -> Location

"""

    MEPModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the MEP model for the family instance.

Get: MEPModel(self: FamilyInstance) -> MEPModel

"""

    Mirrored = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to test whether the family instance is mirrored. (only one axis is flipped)

Get: Mirrored(self: FamilyInstance) -> bool

"""

    StructuralMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the material that defines the instance's structural analysis properties.

Get: StructuralMaterialId(self: FamilyInstance) -> ElementId

Set: StructuralMaterialId(self: FamilyInstance) = value
"""

    StructuralMaterialType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property returns the physical material from which the instance is made.

Get: StructuralMaterialType(self: FamilyInstance) -> StructuralMaterialType

"""

    StructuralType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides the primary structural type of the instance, such as beam or column etc.

Get: StructuralType(self: FamilyInstance) -> StructuralType

"""

    StructuralUsage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides the primary structural usage of the instance, such as brace, girder etc.

Get: StructuralUsage(self: FamilyInstance) -> StructuralInstanceUsage

Set: StructuralUsage(self: FamilyInstance) = value
"""

    SuperComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to get the super component of current family instance.

Get: SuperComponent(self: FamilyInstance) -> Element

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns or changes the FamilySymbol object that represents the type of the instance.

Get: Symbol(self: FamilyInstance) -> FamilySymbol

Set: Symbol(self: FamilyInstance) = value
"""


