class ImageBackgroundSettings(BackgroundSettings, IDisposable):
    """ Represents the rendering image background settings. """
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

    BackgroundImageFit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The background image fit type.

Get: BackgroundImageFit(self: ImageBackgroundSettings) -> BackgroundImageFit

Set: BackgroundImageFit(self: ImageBackgroundSettings) = value
"""

    FilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """File path of the image for the rendering background.

Get: FilePath(self: ImageBackgroundSettings) -> str

Set: FilePath(self: ImageBackgroundSettings) = value
"""

    OffsetHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The vertical offset of the rendering image to the rendering region.

Get: OffsetHeight(self: ImageBackgroundSettings) -> float

Set: OffsetHeight(self: ImageBackgroundSettings) = value
"""

    OffsetWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The horizontal offset of the rendering image to the rendering region.

Get: OffsetWidth(self: ImageBackgroundSettings) -> float

Set: OffsetWidth(self: ImageBackgroundSettings) = value
"""


