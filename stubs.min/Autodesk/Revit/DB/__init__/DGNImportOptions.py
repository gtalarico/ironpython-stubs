class DGNImportOptions(BaseImportOptions, IDisposable):
    """
    The import options used to import DGN format files.
    
    DGNImportOptions(option: DGNImportOptions)
    DGNImportOptions()
    """
    def Dispose(self):
        """ Dispose(self: BaseImportOptions, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: BaseImportOptions, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, option=None):
        """
        __new__(cls: type, option: DGNImportOptions)
        __new__(cls: type)
        """
        pass

    DGNModelViewName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The model view name to be imported.
   Need user give a model view name to specify which model view need to be imported into Revit

Get: DGNModelViewName(self: DGNImportOptions) -> str

Set: DGNModelViewName(self: DGNImportOptions) = value
"""

    IgnoreUnsupportedElementWarning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, ignore warning messages about unsupported elements in the DGN file.
   If false, the import process is aborted if imported dgn files have unsupported elements.

Get: IgnoreUnsupportedElementWarning(self: DGNImportOptions) -> bool

Set: IgnoreUnsupportedElementWarning(self: DGNImportOptions) = value
"""


