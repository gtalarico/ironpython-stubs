class WorksharingDisplayGraphicSettings(object, IDisposable):
    """
    Represents the graphical settings that can be assigned to elements in the worksharing
       display modes.
    
    WorksharingDisplayGraphicSettings(shouldApply: bool, lineColor: Color)
    """
    def Dispose(self):
        """ Dispose(self: WorksharingDisplayGraphicSettings) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WorksharingDisplayGraphicSettings, disposing: bool) """
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
    def __new__(self, shouldApply, lineColor):
        """ __new__(cls: type, shouldApply: bool, lineColor: Color) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    FillColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fill color that will be applied to elements when these settings are
   applied.  Note that this is automatically set by increasing the luma of
   the specified line color by 65%.

Get: FillColor(self: WorksharingDisplayGraphicSettings) -> Color

"""

    IsApplied = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether this set of graphic overrides will be applied.

Get: IsApplied(self: WorksharingDisplayGraphicSettings) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: WorksharingDisplayGraphicSettings) -> bool

"""

    LineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The line color that will be applied to elements when these settings are
   applied.

Get: LineColor(self: WorksharingDisplayGraphicSettings) -> Color

"""


