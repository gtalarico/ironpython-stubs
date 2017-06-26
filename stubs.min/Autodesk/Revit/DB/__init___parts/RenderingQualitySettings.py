class RenderingQualitySettings(object, IDisposable):
    """ Represents the quality settings of rendering. """
    def Dispose(self):
        """ Dispose(self: RenderingQualitySettings) """
        pass

    def IsCustomQuality(self):
        """
        IsCustomQuality(self: RenderingQualitySettings) -> bool
        
            Checks if the current rendering quality is custom or not.
            Returns: True if the current rendering quality is custom, false otherwise.
        """
        pass

    def IsValidRenderLevel(self, value):
        """
        IsValidRenderLevel(self: RenderingQualitySettings, value: int) -> bool
        
            Validate the render level is between 1 and 40
        
            value: The render level value to validate.
            Returns: True if the render level value is in the proper range, false otherwise.
        """
        pass

    def IsValidRenderTime(self, value):
        """
        IsValidRenderTime(self: RenderingQualitySettings, value: int) -> bool
        
            Validate the render time is between 1 and 32768.
        
            value: The render time value to validate.
            Returns: True if the value is in the proper range, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RenderingQualitySettings, disposing: bool) """
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

Get: IsValidObject(self: RenderingQualitySettings) -> bool

"""

    LightAndMaterialAccuracyMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A value that controls light and material accuracy mode.

Get: LightAndMaterialAccuracyMode(self: RenderingQualitySettings) -> LightAndMaterialAccuracyMode

Set: LightAndMaterialAccuracyMode(self: RenderingQualitySettings) = value
"""

    RenderDuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A value that controls render duration.

Get: RenderDuration(self: RenderingQualitySettings) -> RenderDuration

Set: RenderDuration(self: RenderingQualitySettings) = value
"""

    RenderingQuality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The quality applied for rendering.

Get: RenderingQuality(self: RenderingQualitySettings) -> RenderingQuality

Set: RenderingQuality(self: RenderingQualitySettings) = value
"""

    RenderLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The render target level as a numerical value between 1 and 40.

Get: RenderLevel(self: RenderingQualitySettings) -> int

Set: RenderLevel(self: RenderingQualitySettings) = value
"""

    RenderTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The render target time as a numerical value between 1 and 32768.

Get: RenderTime(self: RenderingQualitySettings) -> int

Set: RenderTime(self: RenderingQualitySettings) = value
"""


