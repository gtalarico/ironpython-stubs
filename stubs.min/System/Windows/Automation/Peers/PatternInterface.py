class PatternInterface(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the control pattern that System.Windows.Automation.Peers.AutomationPeer.GetPattern(System.Windows.Automation.Peers.PatternInterface) returns.
    
    enum PatternInterface, values: Dock (12), ExpandCollapse (6), Grid (7), GridItem (8), Invoke (0), ItemContainer (18), MultipleView (9), RangeValue (3), Scroll (4), ScrollItem (5), Selection (1), SelectionItem (11), SynchronizedInput (20), Table (13), TableItem (14), Text (17), Toggle (15), Transform (16), Value (2), VirtualizedItem (19), Window (10)
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

    Dock = None
    ExpandCollapse = None
    Grid = None
    GridItem = None
    Invoke = None
    ItemContainer = None
    MultipleView = None
    RangeValue = None
    Scroll = None
    ScrollItem = None
    Selection = None
    SelectionItem = None
    SynchronizedInput = None
    Table = None
    TableItem = None
    Text = None
    Toggle = None
    Transform = None
    Value = None
    value__ = None
    VirtualizedItem = None
    Window = None

