class ImportExportFileFormat(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes formats supported by import / export.
    
    enum ImportExportFileFormat, values: Civil3D (10), DGN (9), DWF (2), DWFX (4), DWG (1), DXF (12), FBX (7), GBXML (6), IFC (14), Image (8), Inventor (11), NWC (15), SAT (13)
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

    Civil3D = None
    DGN = None
    DWF = None
    DWFX = None
    DWG = None
    DXF = None
    FBX = None
    GBXML = None
    IFC = None
    Image = None
    Inventor = None
    NWC = None
    SAT = None
    value__ = None

