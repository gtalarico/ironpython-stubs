class ConsoleColor(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies constants that define foreground and background colors for the console.
    
    enum ConsoleColor, values: Black (0), Blue (9), Cyan (11), DarkBlue (1), DarkCyan (3), DarkGray (8), DarkGreen (2), DarkMagenta (5), DarkRed (4), DarkYellow (6), Gray (7), Green (10), Magenta (13), Red (12), White (15), Yellow (14)
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

    Black = None
    Blue = None
    Cyan = None
    DarkBlue = None
    DarkCyan = None
    DarkGray = None
    DarkGreen = None
    DarkMagenta = None
    DarkRed = None
    DarkYellow = None
    Gray = None
    Green = None
    Magenta = None
    Red = None
    value__ = None
    White = None
    Yellow = None

