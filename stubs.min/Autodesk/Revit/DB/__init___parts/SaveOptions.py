class SaveOptions(object, IDisposable):
    """
    This class contains options available for saving a document to disk.
    
    SaveOptions()
    """
    def Dispose(self):
        """ Dispose(self: SaveOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SaveOptions, disposing: bool) """
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

    Compact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Default is false: let the OS eliminate as much or as little dead data as it wants to.
   True: force the OS to eliminate all dead data from the file on disk.

Get: Compact(self: SaveOptions) -> bool

Set: Compact(self: SaveOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: SaveOptions) -> bool

"""

    PreviewViewId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The view id that will be used to generate the preview; this id is not saved to the document's permanent settings.

Get: PreviewViewId(self: SaveOptions) -> ElementId

Set: PreviewViewId(self: SaveOptions) = value
"""


