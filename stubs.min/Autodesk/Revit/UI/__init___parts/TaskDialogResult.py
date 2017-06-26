class TaskDialogResult(Enum, IComparable, IFormattable, IConvertible):
    """
    Enum to specify the task dialog result.
    
    enum TaskDialogResult, values: Cancel (2), Close (8), CommandLink1 (1001), CommandLink2 (1002), CommandLink3 (1003), CommandLink4 (1004), No (7), None (0), Ok (1), Retry (4), Yes (6)
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

    Cancel = None
    Close = None
    CommandLink1 = None
    CommandLink2 = None
    CommandLink3 = None
    CommandLink4 = None
    No = None
    None = None
    Ok = None
    Retry = None
    value__ = None
    Yes = None

