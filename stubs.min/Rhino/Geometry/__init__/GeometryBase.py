class GeometryBase(CommonObject, IDisposable, ISerializable):
    # no doc
    def ComponentIndex(self):
        """ ComponentIndex(self: GeometryBase) -> ComponentIndex """
        pass

    def ConstructConstObject(self, *args): #cannot find CLR method
        """ ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GeometryBase) -> GeometryBase """
        pass

    def DuplicateShallow(self):
        """ DuplicateShallow(self: GeometryBase) -> GeometryBase """
        pass

    def GetBoundingBox(self, *__args):
        """
        GetBoundingBox(self: GeometryBase, plane: Plane) -> BoundingBox
        GetBoundingBox(self: GeometryBase, plane: Plane) -> (BoundingBox, Box)
        GetBoundingBox(self: GeometryBase, accurate: bool) -> BoundingBox
        GetBoundingBox(self: GeometryBase, xform: Transform) -> BoundingBox
        """
        pass

    def GetUserString(self, key):
        """ GetUserString(self: GeometryBase, key: str) -> str """
        pass

    def GetUserStrings(self):
        """ GetUserStrings(self: GeometryBase) -> NameValueCollection """
        pass

    def MakeDeformable(self):
        """ MakeDeformable(self: GeometryBase) -> bool """
        pass

    def MemoryEstimate(self):
        """ MemoryEstimate(self: GeometryBase) -> UInt32 """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """ NonConstOperation(self: CommonObject) """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """ OnSwitchToNonConst(self: GeometryBase) """
        pass

    def Rotate(self, angleRadians, rotationAxis, rotationCenter):
        """ Rotate(self: GeometryBase, angleRadians: float, rotationAxis: Vector3d, rotationCenter: Point3d) -> bool """
        pass

    def Scale(self, scaleFactor):
        """ Scale(self: GeometryBase, scaleFactor: float) -> bool """
        pass

    def SetUserString(self, key, value):
        """ SetUserString(self: GeometryBase, key: str, value: str) -> bool """
        pass

    def Transform(self, xform):
        """ Transform(self: GeometryBase, xform: Transform) -> bool """
        pass

    def Translate(self, *__args):
        """
        Translate(self: GeometryBase, x: float, y: float, z: float) -> bool
        Translate(self: GeometryBase, translationVector: Vector3d) -> bool
        """
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
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    HasBrepForm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasBrepForm(self: GeometryBase) -> bool

"""

    IsDeformable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDeformable(self: GeometryBase) -> bool

"""

    IsDocumentControlled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDocumentControlled(self: GeometryBase) -> bool

"""

    ObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectType(self: GeometryBase) -> ObjectType

"""

    UserStringCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserStringCount(self: GeometryBase) -> int

"""


