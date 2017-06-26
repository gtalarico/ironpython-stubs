class InSessionViewSheetSet(object, IViewSheetSet, IDisposable):
    """ Represents the in-session ViewSheetSet. """
    def Dispose(self):
        """ Dispose(self: InSessionViewSheetSet) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: InSessionViewSheetSet, disposing: bool) """
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

    Views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The views.

Get: Views(self: InSessionViewSheetSet) -> ViewSet

Set: Views(self: InSessionViewSheetSet) = value
"""


