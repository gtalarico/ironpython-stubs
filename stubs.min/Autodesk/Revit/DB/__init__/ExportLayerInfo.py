class ExportLayerInfo(object, IDisposable):
    """
    A value used to represent the info stored in the Autodesk.Revit.DB.ExportLayerTable.
    
    ExportLayerInfo()
    """
    def AddCutLayerModifier(self, layerModifier):
        """
        AddCutLayerModifier(self: ExportLayerInfo, layerModifier: LayerModifier)
            Adds a cut layer modifier to the layer info.
        
            layerModifier: The cut layer modifier.
        """
        pass

    def AddLayerModifier(self, layerModifier):
        """
        AddLayerModifier(self: ExportLayerInfo, layerModifier: LayerModifier)
            Adds a project layer modifier to the layer info.
        
            layerModifier: The project layer modifier.
        """
        pass

    def ClearCutLayerModifiers(self):
        """
        ClearCutLayerModifiers(self: ExportLayerInfo)
            Clears all the cut layer modifiers stored in the layer info.
        """
        pass

    def ClearLayerModifiers(self):
        """
        ClearLayerModifiers(self: ExportLayerInfo)
            Clears all the project layer modifiers stored in the layer info.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ExportLayerInfo) """
        pass

    def GetCutLayerModifiers(self):
        """
        GetCutLayerModifiers(self: ExportLayerInfo) -> IList[LayerModifier]
        
            Gets all the cut layer modifiers from the layer info.
            Returns: The cut layer modifier array.
        """
        pass

    def GetLayerModifiers(self):
        """
        GetLayerModifiers(self: ExportLayerInfo) -> IList[LayerModifier]
        
            Gets all the project layer modifiers from the layer info.
            Returns: The project layer modifier array.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExportLayerInfo, disposing: bool) """
        pass

    def RemoveCutLayerModifier(self, layerModifier):
        """
        RemoveCutLayerModifier(self: ExportLayerInfo, layerModifier: LayerModifier)
            Removes a cut layer modifier from the layer info.
        
            layerModifier: The cut layer modifier.
        """
        pass

    def RemoveLayerModifier(self, layerModifier):
        """
        RemoveLayerModifier(self: ExportLayerInfo, layerModifier: LayerModifier)
            Removes a project layer modifier from the layer info.
        
            layerModifier: The project layer modifier.
        """
        pass

    def SetCutLayerModifiers(self, cutLayermodifiers):
        """ SetCutLayerModifiers(self: ExportLayerInfo, cutLayermodifiers: IList[LayerModifier]) """
        pass

    def SetLayerModifiers(self, layermodifiers):
        """ SetLayerModifiers(self: ExportLayerInfo, layermodifiers: IList[LayerModifier]) """
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

    CategoryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The category type which this layer belongs to.

Get: CategoryType(self: ExportLayerInfo) -> LayerCategoryType

Set: CategoryType(self: ExportLayerInfo) = value
"""

    ColorName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The color name stored in value.
   For IFC export, the naming is to match the "colornumber" setting -- really, this stores a string
   that generates the colorNumber (for formats that don't use the color but need a second entry.)

Get: ColorName(self: ExportLayerInfo) -> str

Set: ColorName(self: ExportLayerInfo) = value
"""

    ColorNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The color number stored in value.

Get: ColorNumber(self: ExportLayerInfo) -> int

Set: ColorNumber(self: ExportLayerInfo) = value
"""

    CutColorNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The cut color number stored in value.

Get: CutColorNumber(self: ExportLayerInfo) -> int

Set: CutColorNumber(self: ExportLayerInfo) = value
"""

    CutLayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The cut layer name stored in value.

Get: CutLayerName(self: ExportLayerInfo) -> str

Set: CutLayerName(self: ExportLayerInfo) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExportLayerInfo) -> bool

"""

    LayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The layer name stored in value.

Get: LayerName(self: ExportLayerInfo) -> str

Set: LayerName(self: ExportLayerInfo) = value
"""


