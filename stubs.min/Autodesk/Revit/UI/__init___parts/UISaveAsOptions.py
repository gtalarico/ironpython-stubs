class UISaveAsOptions(object, IDisposable):
    """
    This class contains UI options available for saving a document to disk with a new filename.
    
    UISaveAsOptions()
    """
    def Dispose(self):
        """ Dispose(self: UISaveAsOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: UISaveAsOptions, disposing: bool) """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: UISaveAsOptions) -> bool

"""

    ShowOverwriteWarning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if UI should show an overwrite warning dialog.

Get: ShowOverwriteWarning(self: UISaveAsOptions) -> bool

Set: ShowOverwriteWarning(self: UISaveAsOptions) = value
"""


