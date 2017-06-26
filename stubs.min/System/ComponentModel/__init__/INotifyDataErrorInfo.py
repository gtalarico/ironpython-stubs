class INotifyDataErrorInfo:
    # no doc
    def GetErrors(self, propertyName):
        """ GetErrors(self: INotifyDataErrorInfo, propertyName: str) -> IEnumerable """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    HasErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasErrors(self: INotifyDataErrorInfo) -> bool

"""


    ErrorsChanged = None

