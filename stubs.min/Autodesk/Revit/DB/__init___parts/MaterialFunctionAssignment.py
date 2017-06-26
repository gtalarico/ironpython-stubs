class MaterialFunctionAssignment(Enum, IComparable, IFormattable, IConvertible):
    """
    Used in class CompoundStructure to specify the function of a layer.
    
    enum MaterialFunctionAssignment, values: Finish1 (4), Finish2 (5), Insulation (3), Membrane (100), None (0), StructuralDeck (200), Structure (1), Substrate (2)
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

    Finish1 = None
    Finish2 = None
    Insulation = None
    Membrane = None
    None = None
    StructuralDeck = None
    Structure = None
    Substrate = None
    value__ = None

