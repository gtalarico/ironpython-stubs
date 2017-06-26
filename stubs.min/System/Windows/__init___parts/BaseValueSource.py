class BaseValueSource(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies the property system source of a particular dependency property value.
    
    enum BaseValueSource, values: Default (1), DefaultStyle (3), DefaultStyleTrigger (4), ImplicitStyleReference (8), Inherited (2), Local (11), ParentTemplate (9), ParentTemplateTrigger (10), Style (5), StyleTrigger (7), TemplateTrigger (6), Unknown (0)
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

    Default = None
    DefaultStyle = None
    DefaultStyleTrigger = None
    ImplicitStyleReference = None
    Inherited = None
    Local = None
    ParentTemplate = None
    ParentTemplateTrigger = None
    Style = None
    StyleTrigger = None
    TemplateTrigger = None
    Unknown = None
    value__ = None

