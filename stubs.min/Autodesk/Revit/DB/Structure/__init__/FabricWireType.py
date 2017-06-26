class FabricWireType(ElementType, IDisposable):
    """ A Fabric Wire Type object that is used in the generation of Fabric Wire. """
    @staticmethod
    def CreateDefaultFabricWireType(ADoc):
        """
        CreateDefaultFabricWireType(ADoc: Document) -> ElementId
        
            Creates a new FabricWireType object with a default name.
        
            ADoc: The document.
            Returns: The newly created type id.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    BendDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the bending diameter of the wire.

Get: BendDiameter(self: FabricWireType) -> float

Set: BendDiameter(self: FabricWireType) = value
"""

    WireDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the diameter of the wire.

Get: WireDiameter(self: FabricWireType) -> float

Set: WireDiameter(self: FabricWireType) = value
"""


