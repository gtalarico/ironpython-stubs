class AnnotationBase(GeometryBase, IDisposable, ISerializable):
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

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: AnnotationBase) -> int

Set: Index(self: AnnotationBase) = value
"""

    NumericValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumericValue(self: AnnotationBase) -> float

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: AnnotationBase) -> Plane

Set: Plane(self: AnnotationBase) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: AnnotationBase) -> str

Set: Text(self: AnnotationBase) = value
"""

    TextFormula = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextFormula(self: AnnotationBase) -> str

Set: TextFormula(self: AnnotationBase) = value
"""

    TextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextHeight(self: AnnotationBase) -> float

Set: TextHeight(self: AnnotationBase) = value
"""


