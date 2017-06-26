class ReinforcementAbbreviationTag(object, IDisposable):
    """
    This class is used to access the Area or Path Reinforcement abbreviation tag data.
       It stores abbreviation tag value and abbreviation type.
    
    ReinforcementAbbreviationTag(typeTag: ReinforcementAbbreviationTagType, abbreviationTag: str)
    """
    def Dispose(self):
        """ Dispose(self: ReinforcementAbbreviationTag) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ReinforcementAbbreviationTag, disposing: bool) """
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
    def __new__(self, typeTag, abbreviationTag):
        """ __new__(cls: type, typeTag: ReinforcementAbbreviationTagType, abbreviationTag: str) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AbbreviationTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The abbreviation tag value.

Get: AbbreviationTag(self: ReinforcementAbbreviationTag) -> str

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ReinforcementAbbreviationTag) -> bool

"""

    TypeTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The abbreviation tag type.

Get: TypeTag(self: ReinforcementAbbreviationTag) -> ReinforcementAbbreviationTagType

"""


