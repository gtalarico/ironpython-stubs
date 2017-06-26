class ElectricalSystemType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the possible electrical system types for a connector object.
    
    enum ElectricalSystemType, values: Communication (14), Controls (13), Data (5), FireAlarm (11), NurseCall (12), PowerBalanced (30), PowerCircuit (6), PowerUnBalanced (31), Security (10), Telephone (9), UndefinedSystemType (0)
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

    Communication = None
    Controls = None
    Data = None
    FireAlarm = None
    NurseCall = None
    PowerBalanced = None
    PowerCircuit = None
    PowerUnBalanced = None
    Security = None
    Telephone = None
    UndefinedSystemType = None
    value__ = None

