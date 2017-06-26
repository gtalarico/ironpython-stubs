class LightingSource(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates the lighting scheme type in rendering settings.
    
    enum LightingSource, values: ExteriorArtificial (23), ExteriorSun (21), ExteriorSunAndArtificial (22), InteriorArtificial (26), InteriorSun (24), InteriorSunAndArtificial (25)
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

    ExteriorArtificial = None
    ExteriorSun = None
    ExteriorSunAndArtificial = None
    InteriorArtificial = None
    InteriorSun = None
    InteriorSunAndArtificial = None
    value__ = None

