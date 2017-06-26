class ExportLineweightKey(object, IDisposable):
    """
    A key used to represent an item stored in an Autodesk.Revit.DB.ExportLineweightTable.
    
    ExportLineweightKey(originalLineweight: int)
    ExportLineweightKey()
    ExportLineweightKey(other: ExportLineweightKey)
    """
    def Dispose(self):
        """ Dispose(self: ExportLineweightKey) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExportLineweightKey, disposing: bool) """
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
        __new__(cls: type, originalLineweight: int)
        __new__(cls: type)
        __new__(cls: type, other: ExportLineweightKey)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExportLineweightKey) -> bool

"""

    OriginalLineweight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The original line weight.

Get: OriginalLineweight(self: ExportLineweightKey) -> int

Set: OriginalLineweight(self: ExportLineweightKey) = value
"""


