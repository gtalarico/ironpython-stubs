class ConstructionType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumeration specifies the available analytical construction types
       like external walls, windows etc. for use in the detailed analytical
       energy model.
    
    enum ConstructionType, values: Ceiling (4), Door (6), ExteriorWall (0), ExteriorWindow (7), Floor (5), InteriorWall (1), InteriorWindow (8), Roof (3), Skylight (9), Slab (2)
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

    Ceiling = None
    Door = None
    ExteriorWall = None
    ExteriorWindow = None
    Floor = None
    InteriorWall = None
    InteriorWindow = None
    Roof = None
    Skylight = None
    Slab = None
    value__ = None

