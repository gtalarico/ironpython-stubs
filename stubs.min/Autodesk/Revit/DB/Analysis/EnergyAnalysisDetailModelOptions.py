class EnergyAnalysisDetailModelOptions(object, IDisposable):
    """
    Options that govern the calculations for the generation of the energy analysis detail model.
    
    EnergyAnalysisDetailModelOptions()
    """
    def Dispose(self):
        """ Dispose(self: EnergyAnalysisDetailModelOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: EnergyAnalysisDetailModelOptions, disposing: bool) """
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

    EnergyModelType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """It indicates whether the energy model is based on rooms/spaces or building elements.

Get: EnergyModelType(self: EnergyAnalysisDetailModelOptions) -> EnergyModelType

Set: EnergyModelType(self: EnergyAnalysisDetailModelOptions) = value
"""

    ExportMullions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if to specify the setting for exporting mullions.

Get: ExportMullions(self: EnergyAnalysisDetailModelOptions) -> bool

Set: ExportMullions(self: EnergyAnalysisDetailModelOptions) = value
"""

    IncludeShadingSurfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if to set and get the setting for if shading surfaces should be included.

Get: IncludeShadingSurfaces(self: EnergyAnalysisDetailModelOptions) -> bool

Set: IncludeShadingSurfaces(self: EnergyAnalysisDetailModelOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: EnergyAnalysisDetailModelOptions) -> bool

"""

    SimplifyCurtainSystems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if to specify the setting for simplified curtain systems.

Get: SimplifyCurtainSystems(self: EnergyAnalysisDetailModelOptions) -> bool

Set: SimplifyCurtainSystems(self: EnergyAnalysisDetailModelOptions) = value
"""

    Tier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Level of computation for energy analysis model.

Get: Tier(self: EnergyAnalysisDetailModelOptions) -> EnergyAnalysisDetailModelTier

Set: Tier(self: EnergyAnalysisDetailModelOptions) = value
"""


