class StructuralMaterialTypeFilter(ElementSlowFilter, IDisposable):
    """
    A filter used to match family instances that have the given structural material type.
    
    StructuralMaterialTypeFilter(structuralMaterialType: StructuralMaterialType, inverted: bool)
    StructuralMaterialTypeFilter(structuralMaterialType: StructuralMaterialType)
    """
    def Dispose(self):
        """ Dispose(self: ElementFilter, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ElementFilter, disposing: bool) """
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
    def __new__(self, structuralMaterialType, inverted=None):
        """
        __new__(cls: type, structuralMaterialType: StructuralMaterialType, inverted: bool)
        __new__(cls: type, structuralMaterialType: StructuralMaterialType)
        """
        pass

    StructuralMaterialType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The structural material type.

Get: StructuralMaterialType(self: StructuralMaterialTypeFilter) -> StructuralMaterialType

"""


