class ChangePriority(Enum, IComparable, IFormattable, IConvertible):
    """
    Enum used to specify the priority of an Updater during execution.
    
    enum ChangePriority, values: Annotations (16), Connections (10), DetailComponents (15), DoorsOpeningsWindows (5), FloorsRoofsStructuralWalls (2), FreeStandingComponents (9), GridsLevelsReferencePlanes (0), InteriorWalls (4), Masses (1), MEPAccessoriesFittingsSegmentsWires (12), MEPCalculations (8), MEPFixtures (6), MEPSystems (13), Rebar (11), RoomsSpacesZones (7), Structure (3), Views (14)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Annotations = None
    Connections = None
    DetailComponents = None
    DoorsOpeningsWindows = None
    FloorsRoofsStructuralWalls = None
    FreeStandingComponents = None
    GridsLevelsReferencePlanes = None
    InteriorWalls = None
    Masses = None
    MEPAccessoriesFittingsSegmentsWires = None
    MEPCalculations = None
    MEPFixtures = None
    MEPSystems = None
    Rebar = None
    RoomsSpacesZones = None
    Structure = None
    value__ = None
    Views = None

