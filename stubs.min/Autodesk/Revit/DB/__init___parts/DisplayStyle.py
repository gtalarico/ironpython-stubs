class DisplayStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Display type of the view.
    
    enum DisplayStyle, values: FlatColors (7), HLR (2), Raytrace (9), Realistic (6), RealisticWithEdges (8), Rendering (5), Shading (3), ShadingWithEdges (4), Undefined (0), Wireframe (1)
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

    FlatColors = None
    HLR = None
    Raytrace = None
    Realistic = None
    RealisticWithEdges = None
    Rendering = None
    Shading = None
    ShadingWithEdges = None
    Undefined = None
    value__ = None
    Wireframe = None

