class FormatValueOptions(object, IDisposable):
    """
    Options for formatting numbers with units into strings.
    
    FormatValueOptions()
    """
    def Dispose(self):
        """ Dispose(self: FormatValueOptions) """
        pass

    def GetFormatOptions(self):
        """
        GetFormatOptions(self: FormatValueOptions) -> FormatOptions
        
            Gets the FormatOptions to optionally override the default settings in the Units 
             class.
        
            Returns: A copy of the FormatOptions.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FormatValueOptions, disposing: bool) """
        pass

    def SetFormatOptions(self, formatOptions):
        """
        SetFormatOptions(self: FormatValueOptions, formatOptions: FormatOptions)
            Sets the FormatOptions to optionally override the default settings in the Units 
             class.
        
        
            formatOptions: The FormatOptions.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AppendUnitSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if a unit symbol should be appended regardless of the settings in the FormatOptions.

Get: AppendUnitSymbol(self: FormatValueOptions) -> bool

Set: AppendUnitSymbol(self: FormatValueOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FormatValueOptions) -> bool

"""


