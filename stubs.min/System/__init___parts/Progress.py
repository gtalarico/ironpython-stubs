class Progress(object, IProgress[T]):
    """
    Progress[T]()
    Progress[T](handler: Action[T])
    """
    def OnReport(self, *args): #cannot find CLR method
        """ OnReport(self: Progress[T], value: T) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, handler=None):
        """
        __new__(cls: type)
        __new__(cls: type, handler: Action[T])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ProgressChanged = None

