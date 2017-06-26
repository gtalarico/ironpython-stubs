class gbXMLExportComplexity(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumeration specifies the level of detail of the exported analytical energy model in gbXML.
       Complex means that Curtain Walls and Curtain Systems are exported as several openings, panel by panel;
       a curtain wall with 50 panels gets exported as 50 openings. Simple means that one "huge" opening with
       the total opening area equal to the 50 panels is exported. This is more appropriate for most energy analysis.
       Mullions mean that Mullions in Curtain Walls and Systems are exported as shading surfaces. A "simplified"
       analytical shading surface is produced from a mullion based on its centerline, thickness and offset.
    
    enum gbXMLExportComplexity, values: Complex (2), ComplexWithMullionsAndShadingSurfaces (4), ComplexWithShadingSurfaces (3), Simple (0), SimpleWithShadingSurfaces (1)
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

    Complex = None
    ComplexWithMullionsAndShadingSurfaces = None
    ComplexWithShadingSurfaces = None
    Simple = None
    SimpleWithShadingSurfaces = None
    value__ = None

