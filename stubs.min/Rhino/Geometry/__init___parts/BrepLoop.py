class BrepLoop(GeometryBase, IDisposable, ISerializable):
    # no doc
    def ConstructConstObject(self, *args): #cannot find CLR method
        """ ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """ NonConstOperation(self: CommonObject) """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """ OnSwitchToNonConst(self: GeometryBase) """
        pass

    def To2dCurve(self):
        """ To2dCurve(self: BrepLoop) -> Curve """
        pass

    def To3dCurve(self):
        """ To3dCurve(self: BrepLoop) -> Curve """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Brep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Brep(self: BrepLoop) -> Brep

"""

    Face = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Face(self: BrepLoop) -> BrepFace

"""

    LoopIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoopIndex(self: BrepLoop) -> int

"""

    LoopType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoopType(self: BrepLoop) -> BrepLoopType

"""

    Trims = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Trims(self: BrepLoop) -> BrepTrimList

"""


