class DefaultDllImportSearchPathsAttribute(Attribute, _Attribute):
    """ DefaultDllImportSearchPathsAttribute(paths: DllImportSearchPath) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, paths):
        """ __new__(cls: type, paths: DllImportSearchPath) """
        pass

    Paths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Paths(self: DefaultDllImportSearchPathsAttribute) -> DllImportSearchPath

"""


