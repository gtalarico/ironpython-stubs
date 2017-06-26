class NumericRevisionSettings(object, IDisposable):
    """
    Contains settings that apply to Revisions with the Numeric RevisionNumberType.
    
    NumericRevisionSettings(startNumber: int, prefix: str, suffix: str)
    NumericRevisionSettings()
    NumericRevisionSettings(other: NumericRevisionSettings)
    """
    def Dispose(self):
        """ Dispose(self: NumericRevisionSettings) """
        pass

    def IsEqual(self, other):
        """
        IsEqual(self: NumericRevisionSettings, other: NumericRevisionSettings) -> bool
        
            Determines whether a specified NumericRevisionSettings is the same as 'this'.
        
            other: The specified NumericRevisionSettings with which to compare.
            Returns: True, if two NumericRevisionSettings are the same.
        """
        pass

    def IsValid(self):
        """
        IsValid(self: NumericRevisionSettings) -> bool
        
            Determines whether the NumericRevisionSettings object is in a valid state.
            Returns: True if the NumericRevisionSettings is valid.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: NumericRevisionSettings, disposing: bool) """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, startNumber: int, prefix: str, suffix: str)
        __new__(cls: type)
        __new__(cls: type, other: NumericRevisionSettings)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: NumericRevisionSettings) -> bool

"""

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The prefix string that will be prepended to the number of each revision with Numeric RevisionNumberingType.

Get: Prefix(self: NumericRevisionSettings) -> str

Set: Prefix(self: NumericRevisionSettings) = value
"""

    StartNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The start number for the sequence.

Get: StartNumber(self: NumericRevisionSettings) -> int

Set: StartNumber(self: NumericRevisionSettings) = value
"""

    Suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The suffix string that will be appended to the number of each revision with Numeric RevisionNumberingType.

Get: Suffix(self: NumericRevisionSettings) -> str

Set: Suffix(self: NumericRevisionSettings) = value
"""


