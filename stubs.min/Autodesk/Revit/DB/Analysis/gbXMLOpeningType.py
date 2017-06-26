class gbXMLOpeningType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumeration corresponds to the openingType attribute in gbXML
       and identifies the type of opening defined.
    
    enum gbXMLOpeningType, values: FixedSkylight (2), FixedWindow (0), NonSlidingDoor (5), NoOfOpeningTypes (7), OpeningAir (6), OperableSkylight (3), OperableWindow (1), SlidingDoor (4)
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

    FixedSkylight = None
    FixedWindow = None
    NonSlidingDoor = None
    NoOfOpeningTypes = None
    OpeningAir = None
    OperableSkylight = None
    OperableWindow = None
    SlidingDoor = None
    value__ = None

