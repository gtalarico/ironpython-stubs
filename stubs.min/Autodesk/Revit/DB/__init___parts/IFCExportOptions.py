class IFCExportOptions(object, IDisposable):
    """
    IFC Export options.
    
    IFCExportOptions(from: IFCExportOptions)
    IFCExportOptions()
    """
    def AddOption(self, name, value):
        """
        AddOption(self: IFCExportOptions, name: str, value: str)
            Adds a new named option to the options structure.
        
            name: The option name.
            value: The option value.
        """
        pass

    def Assign(self, sourceOptions):
        """
        Assign(self: IFCExportOptions, sourceOptions: IFCExportOptions)
            Assigns the values of the IFCExportOptions to this options object.
        
            sourceOptions: The source IFCExportOptions.
        """
        pass

    def Dispose(self):
        """ Dispose(self: IFCExportOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: IFCExportOptions, disposing: bool) """
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
    def __new__(self, from=None):
        """
        __new__(cls: type, from: IFCExportOptions)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ExportBaseQuantities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Option to export IFC standard quantities currently supported by Revit.

Get: ExportBaseQuantities(self: IFCExportOptions) -> bool

Set: ExportBaseQuantities(self: IFCExportOptions) = value
"""

    FamilyMappingFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Path to a file containing family mapping.

Get: FamilyMappingFile(self: IFCExportOptions) -> str

Set: FamilyMappingFile(self: IFCExportOptions) = value
"""

    FileVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """IFC file version.

Get: FileVersion(self: IFCExportOptions) -> IFCVersion

Set: FileVersion(self: IFCExportOptions) = value
"""

    FilterViewId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the view whose visibility settings will govern the contents in the exported IFC file.

Get: FilterViewId(self: IFCExportOptions) -> ElementId

Set: FilterViewId(self: IFCExportOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: IFCExportOptions) -> bool

"""

    SpaceBoundaryLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Level of space boundaries exported in IFC file.

Get: SpaceBoundaryLevel(self: IFCExportOptions) -> int

Set: SpaceBoundaryLevel(self: IFCExportOptions) = value
"""

    WallAndColumnSplitting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Option to allow division of multi-level walls and columns by levels.

Get: WallAndColumnSplitting(self: IFCExportOptions) -> bool

Set: WallAndColumnSplitting(self: IFCExportOptions) = value
"""


