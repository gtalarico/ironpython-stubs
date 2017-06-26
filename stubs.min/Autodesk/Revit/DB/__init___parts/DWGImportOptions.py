class DWGImportOptions(BaseImportOptions, IDisposable):
    """
    The import options used by importing DWG or DXF format file.
    
    DWGImportOptions(option: DWGImportOptions)
    DWGImportOptions()
    """
    def Dispose(self):
        """ Dispose(self: BaseImportOptions, A_0: bool) """
        pass

    def GetLineWeights(self):
        """
        GetLineWeights(self: DWGImportOptions) -> IList[int]
        
            Gets array of line weights.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: BaseImportOptions, disposing: bool) """
        pass

    def SetLineWeights(self, lineWeight):
        """ SetLineWeights(self: DWGImportOptions, lineWeight: IList[int]) """
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
        __new__(cls: type, option: DWGImportOptions)
        __new__(cls: type)
        """
        pass

