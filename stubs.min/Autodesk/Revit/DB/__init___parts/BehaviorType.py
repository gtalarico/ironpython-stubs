class BehaviorType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the behavior type for MEP Components.
    
    enum BehaviorType, values: BaseObject (1024), Bend (2), Branch (4), BreakInto (32), Coupling (2097152), ElectricalBaseObject (65536), EndCap (2048), Flange (8192), Flat_Tap (1048576), Flex (262144), Hanger (524288), Inline (16), Intersection (8), Invalid (0), MechanicalCoupling (16384), Normal (1), OrientToCenterLine (128), OrientToFace (256), OrientToObject (64), Oval_CentreLine_Tap (8388608), Round_CentreLine_Tap (4194304), Straight (131072), SystemMember (512), Valve (4096), VerticalBend (32768)
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

    BaseObject = None
    Bend = None
    Branch = None
    BreakInto = None
    Coupling = None
    ElectricalBaseObject = None
    EndCap = None
    Flange = None
    Flat_Tap = None
    Flex = None
    Hanger = None
    Inline = None
    Intersection = None
    Invalid = None
    MechanicalCoupling = None
    Normal = None
    OrientToCenterLine = None
    OrientToFace = None
    OrientToObject = None
    Oval_CentreLine_Tap = None
    Round_CentreLine_Tap = None
    Straight = None
    SystemMember = None
    value__ = None
    Valve = None
    VerticalBend = None

