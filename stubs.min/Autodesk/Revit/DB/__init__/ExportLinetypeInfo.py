class ExportLinetypeInfo(object, IDisposable):
    """
    A value used to represent the info stored in the Autodesk.Revit.DB.ExportLinetypeTable.
    
    ExportLinetypeInfo(destinationLinetypeName: str)
    ExportLinetypeInfo()
    ExportLinetypeInfo(other: ExportLinetypeInfo)
    """
    def Dispose(self):
        """ Dispose(self: ExportLinetypeInfo) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExportLinetypeInfo, disposing: bool) """
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
        __new__(cls: type, destinationLinetypeName: str)
        __new__(cls: type)
        __new__(cls: type, other: ExportLinetypeInfo)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DestinationLinetypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The destination linetype name (the name of the linetype in the exported format).

Get: DestinationLinetypeName(self: ExportLinetypeInfo) -> str

Set: DestinationLinetypeName(self: ExportLinetypeInfo) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExportLinetypeInfo) -> bool

"""


