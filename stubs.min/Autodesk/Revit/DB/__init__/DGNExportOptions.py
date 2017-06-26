class DGNExportOptions(BaseExportOptions, IDisposable):
    """
    The export options used by exporting DGN format file.
    
    DGNExportOptions(option: DGNExportOptions)
    DGNExportOptions()
    """
    def Dispose(self):
        """ Dispose(self: BaseExportOptions, A_0: bool) """
        pass

    def GetExportLineweightTable(self):
        """
        GetExportLineweightTable(self: DGNExportOptions) -> ExportLineweightTable
        
            Gets a copy of the line weight table.
            Returns: The line weight table.
        """
        pass

    @staticmethod
    def GetPredefinedOptions(document, setup):
        """
        GetPredefinedOptions(document: Document, setup: str) -> DGNExportOptions
        
            Returns an instance DGNExportOptions containing settings from a predefined 
             export setup.
        
        
            document: A Revit project document to retrieve the setup from.
            setup: The name of a predefined export setup from the specified document.
            Returns: An instance of predefined DGNExportOptions, or ll if the name was not found.
        """
        pass

    @staticmethod
    def GetPredefinedSetupNames(document):
        """
        GetPredefinedSetupNames(document: Document) -> IList[str]
        
            Returns a list of names of predefined setups of DGN export options.
        
            document: A Revit document to retrieve names from.
            Returns: An array of strings representing names of predefined setups.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: BaseExportOptions, disposing: bool) """
        pass

    def SetExportLineweightTable(self, lineweightTable):
        """
        SetExportLineweightTable(self: DGNExportOptions, lineweightTable: ExportLineweightTable)
            Sets the line weight table to use during export.
        
            lineweightTable: The line weight table to be set.
        """
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
        __new__(cls: type, option: DGNExportOptions)
        __new__(cls: type)
        """
        pass

    FileVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The DGN file version.
   Default value of fileVersion is DGNFileFormat.Default.

Get: FileVersion(self: DGNExportOptions) -> DGNFileFormat

Set: FileVersion(self: DGNExportOptions) = value
"""

    MasterUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The master units.
   Default value of masterUnits is true.

Get: MasterUnits(self: DGNExportOptions) -> bool

Set: MasterUnits(self: DGNExportOptions) = value
"""

    MergedViews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to merge all views in one file (via XRefs).
   Default value of mergedViews is false.

Get: MergedViews(self: DGNExportOptions) -> bool

Set: MergedViews(self: DGNExportOptions) = value
"""

    SeedName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the DGN seed.
   Default value of seedName is empty.

Get: SeedName(self: DGNExportOptions) -> str

Set: SeedName(self: DGNExportOptions) = value
"""


