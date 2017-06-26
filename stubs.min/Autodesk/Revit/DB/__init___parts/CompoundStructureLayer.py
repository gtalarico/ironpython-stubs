class CompoundStructureLayer(object, IDisposable):
    """
    Describes a single layer in a CompoundStructure.
    
    CompoundStructureLayer(width: float, function: MaterialFunctionAssignment, materialId: ElementId)
    CompoundStructureLayer(cs: CompoundStructureLayer)
    CompoundStructureLayer()
    """
    def Dispose(self):
        """ Dispose(self: CompoundStructureLayer) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: CompoundStructureLayer, disposing: bool) """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, width: float, function: MaterialFunctionAssignment, materialId: ElementId)
        __new__(cls: type, cs: CompoundStructureLayer)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DeckEmbeddingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Embedding type for structural deck - only for a layer whose function is StructuralDeck.

Get: DeckEmbeddingType(self: CompoundStructureLayer) -> StructDeckEmbeddingType

Set: DeckEmbeddingType(self: CompoundStructureLayer) = value
"""

    DeckProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the structural deck profile - only for a layer whose function is StructuralDeck.

Get: DeckProfileId(self: CompoundStructureLayer) -> ElementId

Set: DeckProfileId(self: CompoundStructureLayer) = value
"""

    Function = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The function of the layer.

Get: Function(self: CompoundStructureLayer) -> MaterialFunctionAssignment

Set: Function(self: CompoundStructureLayer) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: CompoundStructureLayer) -> bool

"""

    LayerCapFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the layer participates in wrapping at end caps and/or inserts.

Get: LayerCapFlag(self: CompoundStructureLayer) -> bool

Set: LayerCapFlag(self: CompoundStructureLayer) = value
"""

    LayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the layer - note that this may be different from the index in the array of layers in a CompoundStructure.

Get: LayerId(self: CompoundStructureLayer) -> int

"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the material assigned to this layer.

Get: MaterialId(self: CompoundStructureLayer) -> ElementId

Set: MaterialId(self: CompoundStructureLayer) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Width of the layer.

Get: Width(self: CompoundStructureLayer) -> float

Set: Width(self: CompoundStructureLayer) = value
"""


