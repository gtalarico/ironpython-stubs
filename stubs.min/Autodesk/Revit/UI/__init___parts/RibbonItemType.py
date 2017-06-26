class RibbonItemType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the toolbar item styles.
    
    enum RibbonItemType, values: ComboBox (6), ComboBoxMember (5), PulldownButton (1), PushButton (0), RadioButtonGroup (4), SplitButton (2), TextBox (7), ToggleButton (3)
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

    ComboBox = None
    ComboBoxMember = None
    PulldownButton = None
    PushButton = None
    RadioButtonGroup = None
    SplitButton = None
    TextBox = None
    ToggleButton = None
    value__ = None

