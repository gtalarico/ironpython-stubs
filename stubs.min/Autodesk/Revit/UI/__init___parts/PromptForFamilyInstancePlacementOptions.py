class PromptForFamilyInstancePlacementOptions(object, IDisposable):
    """
    This class contains options to control the behavior of interactive placement of family instances.
    
    PromptForFamilyInstancePlacementOptions(other: PromptForFamilyInstancePlacementOptions)
    PromptForFamilyInstancePlacementOptions()
    """
    def Dispose(self):
        """ Dispose(self: PromptForFamilyInstancePlacementOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PromptForFamilyInstancePlacementOptions, disposing: bool) """
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
    def __new__(self, other=None):
        """
        __new__(cls: type, other: PromptForFamilyInstancePlacementOptions)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    FaceBasedPlacementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The placement type to be used if prompting to place an instance of a face-based family.
   This option is ignored if placing a non-face-based family. If placing a face-based family, Default is an acceptable value, but will correspond to the first available selection in the user interface.

Get: FaceBasedPlacementType(self: PromptForFamilyInstancePlacementOptions) -> FaceBasedPlacementType

Set: FaceBasedPlacementType(self: PromptForFamilyInstancePlacementOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PromptForFamilyInstancePlacementOptions) -> bool

"""

    PlaceAirTerminalOnDuct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, when placing an air terminal, the terminal will be placed directly on the duct without fittings.
   If fase, the terminal will be placed with generated fittings.

Get: PlaceAirTerminalOnDuct(self: PromptForFamilyInstancePlacementOptions) -> bool

Set: PlaceAirTerminalOnDuct(self: PromptForFamilyInstancePlacementOptions) = value
"""

    SketchGalleryOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sketch option provided when promt to place a family instance.

Get: SketchGalleryOptions(self: PromptForFamilyInstancePlacementOptions) -> SketchGalleryOptions

Set: SketchGalleryOptions(self: PromptForFamilyInstancePlacementOptions) = value
"""


