class TableCellCombinedParameterData(object, IDisposable):
    """ The TableCellCombinedParameterData stores the data for combined parameters """
    @staticmethod
    def Create():
        """
        Create() -> TableCellCombinedParameterData
        
            construct a TableCellCombinedParameterData
        """
        pass

    def Dispose(self):
        """ Dispose(self: TableCellCombinedParameterData) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: TableCellCombinedParameterData, disposing: bool) """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CategoryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Category id for this parameter

Get: CategoryId(self: TableCellCombinedParameterData) -> ElementId

Set: CategoryId(self: TableCellCombinedParameterData) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: TableCellCombinedParameterData) -> bool

"""

    ParamId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The parameter id

Get: ParamId(self: TableCellCombinedParameterData) -> ElementId

Set: ParamId(self: TableCellCombinedParameterData) = value
"""

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The prefix for this parameter

Get: Prefix(self: TableCellCombinedParameterData) -> str

Set: Prefix(self: TableCellCombinedParameterData) = value
"""

    SampleValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sample/example value for the parameter in text form

Get: SampleValue(self: TableCellCombinedParameterData) -> str

Set: SampleValue(self: TableCellCombinedParameterData) = value
"""

    Separator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The separator for this parameter

Get: Separator(self: TableCellCombinedParameterData) -> str

Set: Separator(self: TableCellCombinedParameterData) = value
"""

    Suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The suffix for this parameter

Get: Suffix(self: TableCellCombinedParameterData) -> str

Set: Suffix(self: TableCellCombinedParameterData) = value
"""


