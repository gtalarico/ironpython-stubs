class TraceEventType(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies the type of event that has caused the trace.
    
    enum TraceEventType, values: Critical (1), Error (2), Information (8), Resume (2048), Start (256), Stop (512), Suspend (1024), Transfer (4096), Verbose (16), Warning (4)
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

    Critical = None
    Error = None
    Information = None
    Resume = None
    Start = None
    Stop = None
    Suspend = None
    Transfer = None
    value__ = None
    Verbose = None
    Warning = None

