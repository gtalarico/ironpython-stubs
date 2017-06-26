class ColorBackgroundSettings(BackgroundSettings, IDisposable):
    """ Represents the rendering color background settings. """
    def Dispose(self):
        """ Dispose(self: BackgroundSettings, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: BackgroundSettings, disposing: bool) """
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

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The color of the rendering background.

Get: Color(self: ColorBackgroundSettings) -> Color

Set: Color(self: ColorBackgroundSettings) = value
"""


