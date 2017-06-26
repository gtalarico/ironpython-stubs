class ElectricalDemandFactorRule(Enum, IComparable, IFormattable, IConvertible):
    """
    This enum describes the different demand factor rule types available to the application.
       Within a demand factor a rule will be referenced and the user will have to enter values
       corresponding to that rule.
    
    enum ElectricalDemandFactorRule, values: Constant (0), LoadTable (2), LoadTablePerPortion (4), QuantityTable (1), QuantityTablePerPortion (3)
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

    Constant = None
    LoadTable = None
    LoadTablePerPortion = None
    QuantityTable = None
    QuantityTablePerPortion = None
    value__ = None

