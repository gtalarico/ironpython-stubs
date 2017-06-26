class MessageBoxImage(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the icon that is displayed by a message box.
    
    enum MessageBoxImage, values: Asterisk (64), Error (16), Exclamation (48), Hand (16), Information (64), None (0), Question (32), Stop (16), Warning (48)
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

    Asterisk = None
    Error = None
    Exclamation = None
    Hand = None
    Information = None
    None = None
    Question = None
    Stop = None
    value__ = None
    Warning = None

