class MassZone(Element, IDisposable):
    """ MassZones are created from the MassEnergyAnalyticalModel.  They are conceptual representations of individually heated and cooled sub-volumes of a building. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCoincidentReferenceFromAdjacentZone(self, referenceToZoneFace):
        """
        GetCoincidentReferenceFromAdjacentZone(self: MassZone, referenceToZoneFace: Reference) -> Reference
        
            This method is used to get a Reference from an adjacent MassZone that is 
             coincident to a Reference of this MassZone.
        
        
            referenceToZoneFace: Reference to face of MassZone.
            Returns: Reference to coincident face of adjacent MassZone or ll if there is no adjacent 
             MassZone face Reference.
        """
        pass

    def GetEquivalentReferenceFromMassOrLevel(self, referenceToZoneFace):
        """
        GetEquivalentReferenceFromMassOrLevel(self: MassZone, referenceToZoneFace: Reference) -> Reference
        
            Returns a Reference to a face of a MassEnergyAnalyticalModel element or
           an 
             element Reference to a MassLevelData element.
           This Reference represents 
             what the MassZone face was "cut from" when making the MassZone for the level.
        
        
            referenceToZoneFace: Reference to a face of the zone to get an equivalent reference for.
            Returns: Reference to MassEnergyAnalyticalModel or MassLevelData.  Should only be ll if 
             there is an error
           in the MassEnergyAnalyticalModel data or the input is not 
             a
        """
        pass

    def GetMassDataElementIdForZoneFaceReference(self, referenceOfZone):
        """
        GetMassDataElementIdForZoneFaceReference(self: MassZone, referenceOfZone: Reference) -> ElementId
        
            MassZone faces come from faces of MassEnergyAnalyticalModel, and those faces 
             have MassSurfaceData
           or MassLevelData elements associated with them.
        
        
            referenceOfZone: Reference to face of the MassZone to get data element for.
            Returns: Id of MassSurfaceData or MassLevelData element.
        """
        pass

    def GetReferencesToEnergyAnalysisFaces(self):
        """
        GetReferencesToEnergyAnalysisFaces(self: MassZone) -> IList[Reference]
        
            Used to get References to all the faces of the MassZone that are used for 
             Energy Analysis.
        
            Returns: Array of References to faces of MassZone.
        """
        pass

    def IsEmpty(self):
        """
        IsEmpty(self: MassZone) -> bool
        
            Indicates if MassZone has no geometry.  Such zones should not be shown to the 
             user.
        
            Returns: Returns True if MassZone has no geometry.
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

    ConditionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The gbXMLConditionType of the MassZone.

Get: ConditionType(self: MassZone) -> gbXMLConditionType

Set: ConditionType(self: MassZone) = value
"""

    CutByLowerLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the relationship between the MassZone and its lower level.

Get: CutByLowerLevel(self: MassZone) -> MassZoneLevelCutState

"""

    CutByUpperLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the relationship between the MassZone and its upper level.

Get: CutByUpperLevel(self: MassZone) -> MassZoneLevelCutState

"""

    FloorArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The floor area of the MassZone.

Get: FloorArea(self: MassZone) -> float

"""

    IsZoneOccupiable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A MassZone must have a level as its bottom to be occupiable;
   If it does not, it is still a MassZone, but it is not occupiable

Get: IsZoneOccupiable(self: MassZone) -> bool

"""

    LowerLevelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The bottom level defining the MassZone.

Get: LowerLevelId(self: MassZone) -> ElementId

"""

    MassEnergyAnalyticalModelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the MassEnergyAnalyticalModel that the MassZone is derived from.

Get: MassEnergyAnalyticalModelId(self: MassZone) -> ElementId

"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The visualization material for the MassZone.
   Will be InvalidElementId if material is by category or the material type is by MassZoneMaterialTypeMaterialBySurfaceType.

Get: MaterialId(self: MassZone) -> ElementId

Set: MaterialId(self: MassZone) = value
"""

    MaterialType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates how the material of MassZone faces is determined.

Get: MaterialType(self: MassZone) -> MassZoneMaterialType

Set: MaterialType(self: MassZone) = value
"""

    SpaceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The gbXMLSpaceType of the MassZone.

Get: SpaceType(self: MassZone) -> gbXMLSpaceType

Set: SpaceType(self: MassZone) = value
"""

    UpperLevelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The upper level defining the MassZone.

Get: UpperLevelId(self: MassZone) -> ElementId

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The volume of the MassZone.

Get: Volume(self: MassZone) -> float

"""


