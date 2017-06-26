class ExportFontInfo(object, IDisposable):
    """
    A value used to represent the info stored in an Autodesk.Revit.DB.ExportFontTable.
    
    ExportFontInfo(destinationFontName: str)
    ExportFontInfo()
    ExportFontInfo(other: ExportFontInfo)
    """
    def Dispose(self):
        """ Dispose(self: ExportFontInfo) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExportFontInfo, disposing: bool) """
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
        __new__(cls: type, destinationFontName: str)
        __new__(cls: type)
        __new__(cls: type, other: ExportFontInfo)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DestinationFontName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The destination font name (the name of the font in the exported format).

Get: DestinationFontName(self: ExportFontInfo) -> str

Set: DestinationFontName(self: ExportFontInfo) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExportFontInfo) -> bool

"""


