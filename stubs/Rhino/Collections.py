# encoding: utf-8
# module Rhino.Collections calls itself Collections
# from Rhino3dmIO, Version=5.1.30000.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ArchivableDictionary(object, ICloneable, IDictionary[str, object], ICollection[KeyValuePair[str, object]], IEnumerable[KeyValuePair[str, object]], IEnumerable):
    """
    ArchivableDictionary()
    ArchivableDictionary(parentUserData: UserData)
    ArchivableDictionary(version: int)
    ArchivableDictionary(version: int, name: str)
    """
    def AddContentsFrom(self, source):
        """ AddContentsFrom(self: ArchivableDictionary, source: ArchivableDictionary) -> bool """
        pass

    def Clear(self):
        """ Clear(self: ArchivableDictionary) """
        pass

    def Clone(self):
        """ Clone(self: ArchivableDictionary) -> ArchivableDictionary """
        pass

    def ContainsKey(self, key):
        """ ContainsKey(self: ArchivableDictionary, key: str) -> bool """
        pass

    def GetBool(self, key, defaultValue=None):
        """
        GetBool(self: ArchivableDictionary, key: str, defaultValue: bool) -> bool
        GetBool(self: ArchivableDictionary, key: str) -> bool
        """
        pass

    def GetBytes(self, key, defaultValue=None):
        """
        GetBytes(self: ArchivableDictionary, key: str, defaultValue: Array[Byte]) -> Array[Byte]
        GetBytes(self: ArchivableDictionary, key: str) -> Array[Byte]
        """
        pass

    def GetDictionary(self, key, defaultValue=None):
        """
        GetDictionary(self: ArchivableDictionary, key: str, defaultValue: ArchivableDictionary) -> ArchivableDictionary
        GetDictionary(self: ArchivableDictionary, key: str) -> ArchivableDictionary
        """
        pass

    def GetDouble(self, key, defaultValue=None):
        """
        GetDouble(self: ArchivableDictionary, key: str, defaultValue: float) -> float
        GetDouble(self: ArchivableDictionary, key: str) -> float
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ArchivableDictionary) -> IEnumerator[KeyValuePair[str, object]] """
        pass

    def GetEnumValue(self, key=None):
# Error generating skeleton for function GetEnumValue: Method must be called on a Type for which Type.IsGenericParameter is false.

    def GetFloat(self, key, defaultValue=None):
        """
        GetFloat(self: ArchivableDictionary, key: str, defaultValue: Single) -> Single
        GetFloat(self: ArchivableDictionary, key: str) -> Single
        """
        pass

    def GetGuid(self, key, defaultValue=None):
        """
        GetGuid(self: ArchivableDictionary, key: str, defaultValue: Guid) -> Guid
        GetGuid(self: ArchivableDictionary, key: str) -> Guid
        """
        pass

    def Getint(self, key, defaultValue):
        """ Getint(self: ArchivableDictionary, key: str, defaultValue: int) -> int """
        pass

    def GetInteger(self, key, defaultValue=None):
        """
        GetInteger(self: ArchivableDictionary, key: str) -> int
        GetInteger(self: ArchivableDictionary, key: str, defaultValue: int) -> int
        """
        pass

    def GetPoint3d(self, key, defaultValue=None):
        """
        GetPoint3d(self: ArchivableDictionary, key: str, defaultValue: Point3d) -> Point3d
        GetPoint3d(self: ArchivableDictionary, key: str) -> Point3d
        """
        pass

    def GetPoint3f(self, key, defaultValue=None):
        """
        GetPoint3f(self: ArchivableDictionary, key: str, defaultValue: Point3f) -> Point3f
        GetPoint3f(self: ArchivableDictionary, key: str) -> Point3f
        """
        pass

    def GetString(self, key, defaultValue=None):
        """
        GetString(self: ArchivableDictionary, key: str, defaultValue: str) -> str
        GetString(self: ArchivableDictionary, key: str) -> str
        """
        pass

    def GetVector3d(self, key, defaultValue=None):
        """
        GetVector3d(self: ArchivableDictionary, key: str, defaultValue: Vector3d) -> Vector3d
        GetVector3d(self: ArchivableDictionary, key: str) -> Vector3d
        """
        pass

    def Remove(self, key):
        """ Remove(self: ArchivableDictionary, key: str) -> bool """
        pass

    def RemoveEnumValue(self):
        """ RemoveEnumValue[T](self: ArchivableDictionary) -> bool """
        pass

    def ReplaceContentsWith(self, source):
        """ ReplaceContentsWith(self: ArchivableDictionary, source: ArchivableDictionary) -> bool """
        pass

    def Set(self, key, val):
        """
        Set(self: ArchivableDictionary, key: str, val: Point2d) -> bool
        Set(self: ArchivableDictionary, key: str, val: Interval) -> bool
        Set(self: ArchivableDictionary, key: str, val: Point3d) -> bool
        Set(self: ArchivableDictionary, key: str, val: Vector2d) -> bool
        Set(self: ArchivableDictionary, key: str, val: Point4d) -> bool
        Set(self: ArchivableDictionary, key: str, val: Font) -> bool
        Set(self: ArchivableDictionary, key: str, val: Rectangle) -> bool
        Set(self: ArchivableDictionary, key: str, val: PointF) -> bool
        Set(self: ArchivableDictionary, key: str, val: RectangleF) -> bool
        Set(self: ArchivableDictionary, key: str, val: SizeF) -> bool
        Set(self: ArchivableDictionary, key: str, val: Size) -> bool
        Set(self: ArchivableDictionary, key: str, val: Vector3f) -> bool
        Set(self: ArchivableDictionary, key: str, val: Point3f) -> bool
        Set(self: ArchivableDictionary, key: str, val: ArchivableDictionary) -> bool
        Set(self: ArchivableDictionary, key: str, val: GeometryBase) -> bool
        Set(self: ArchivableDictionary, key: str, val: MeshingParameters) -> bool
        Set(self: ArchivableDictionary, key: str, val: Line) -> bool
        Set(self: ArchivableDictionary, key: str, val: BoundingBox) -> bool
        Set(self: ArchivableDictionary, key: str, val: Vector3d) -> bool
        Set(self: ArchivableDictionary, key: str, val: Ray3d) -> bool
        Set(self: ArchivableDictionary, key: str, val: Plane) -> bool
        Set(self: ArchivableDictionary, key: str, val: Transform) -> bool
        Set(self: ArchivableDictionary, key: str, val: Point) -> bool
        Set(self: ArchivableDictionary, key: str, val: Int64) -> bool
        Set(self: ArchivableDictionary, key: str, val: UInt32) -> bool
        Set(self: ArchivableDictionary, key: str, val: Single) -> bool
        Set(self: ArchivableDictionary, key: str, val: Guid) -> bool
        Set(self: ArchivableDictionary, key: str, val: float) -> bool
        Set(self: ArchivableDictionary, key: str, val: int) -> bool
        Set(self: ArchivableDictionary, key: str, val: Byte) -> bool
        Set(self: ArchivableDictionary, key: str, val: bool) -> bool
        Set(self: ArchivableDictionary, key: str, val: SByte) -> bool
        Set(self: ArchivableDictionary, key: str, val: UInt16) -> bool
        Set(self: ArchivableDictionary, key: str, val: Int16) -> bool
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[float]) -> bool
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[Single]) -> bool
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[Guid]) -> bool
        Set(self: ArchivableDictionary, key: str, val: Color) -> bool
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[str]) -> bool
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[int]) -> bool
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[bool]) -> bool
        Set(self: ArchivableDictionary, key: str, val: str) -> bool
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[Byte]) -> bool
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[Int16]) -> bool
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[SByte]) -> bool
        """
        pass

    def SetEnumValue(self, *__args):
        """
        SetEnumValue[T](self: ArchivableDictionary, key: str, enumValue: T) -> bool
        SetEnumValue[T](self: ArchivableDictionary, enumValue: T) -> bool
        """
        pass

    def TryGetBool(self, key, value):
        """ TryGetBool(self: ArchivableDictionary, key: str) -> (bool, bool) """
        pass

    def TryGetBytes(self, key, value):
        """ TryGetBytes(self: ArchivableDictionary, key: str) -> (bool, Array[Byte]) """
        pass

    def TryGetDictionary(self, key, value):
        """ TryGetDictionary(self: ArchivableDictionary, key: str) -> (bool, ArchivableDictionary) """
        pass

    def TryGetDouble(self, key, value):
        """ TryGetDouble(self: ArchivableDictionary, key: str) -> (bool, float) """
        pass

    def TryGetEnumValue(self, key, enumValue):
# Error generating skeleton for function TryGetEnumValue: Method must be called on a Type for which Type.IsGenericParameter is false.

    def TryGetFloat(self, key, value):
        """ TryGetFloat(self: ArchivableDictionary, key: str) -> (bool, Single) """
        pass

    def TryGetGuid(self, key, value):
        """ TryGetGuid(self: ArchivableDictionary, key: str) -> (bool, Guid) """
        pass

    def TryGetInteger(self, key, value):
        """ TryGetInteger(self: ArchivableDictionary, key: str) -> (bool, int) """
        pass

    def TryGetPoint3d(self, key, value):
        """ TryGetPoint3d(self: ArchivableDictionary, key: str) -> (bool, Point3d) """
        pass

    def TryGetPoint3f(self, key, value):
        """ TryGetPoint3f(self: ArchivableDictionary, key: str) -> (bool, Point3f) """
        pass

    def TryGetString(self, key, value):
        """ TryGetString(self: ArchivableDictionary, key: str) -> (bool, str) """
        pass

    def TryGetValue(self, key, value):
        """ TryGetValue(self: ArchivableDictionary, key: str) -> (bool, object) """
        pass

    def TryGetVector3d(self, key, value):
        """ TryGetVector3d(self: ArchivableDictionary, key: str) -> (bool, Vector3d) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary[str, object], key: str) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, parentUserData: UserData)
        __new__(cls: type, version: int)
        __new__(cls: type, version: int, name: str)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ArchivableDictionary) -> int

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keys(self: ArchivableDictionary) -> Array[str]

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ArchivableDictionary) -> str

Set: Name(self: ArchivableDictionary) = value
"""

    ParentUserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentUserData(self: ArchivableDictionary) -> UserData

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: ArchivableDictionary) -> Array[object]

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: ArchivableDictionary) -> int

Set: Version(self: ArchivableDictionary) = value
"""



class CurveList(RhinoList[Curve], IList[Curve], ICollection[Curve], IEnumerable[Curve], IEnumerable, IList, ICollection):
    """
    CurveList()
    CurveList(initialCapacity: int)
    CurveList(collection: IEnumerable[Curve])
    """
    def Add(self, *__args):
        """ Add(self: CurveList, polyline: IEnumerable[Point3d])Add(self: CurveList, ellipse: Ellipse)Add(self: CurveList, arc: Arc)Add(self: CurveList, line: Line)Add(self: CurveList, circle: Circle) """
        pass

    def Insert(self, index, *__args):
        """ Insert(self: CurveList, index: int, polyline: IEnumerable[Point3d])Insert(self: CurveList, index: int, ellipse: Ellipse)Insert(self: CurveList, index: int, arc: Arc)Insert(self: CurveList, index: int, line: Line)Insert(self: CurveList, index: int, circle: Circle) """
        pass

    def Transform(self, xform):
        """ Transform(self: CurveList, xform: Transform) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, initialCapacity: int)
        __new__(cls: type, collection: IEnumerable[Curve])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class Point3dList(RhinoList[Point3d], IList[Point3d], ICollection[Point3d], IEnumerable[Point3d], IEnumerable, IList, ICollection):
    """
    Point3dList()
    Point3dList(initialCapacity: int)
    Point3dList(collection: IEnumerable[Point3d])
    Point3dList(*initialPoints: Array[Point3d])
    """
    def Add(self, *__args):
        """ Add(self: Point3dList, x: float, y: float, z: float) """
        pass

    def ClosestIndex(self, testPoint):
        """ ClosestIndex(self: Point3dList, testPoint: Point3d) -> int """
        pass

    @staticmethod
    def ClosestIndexInList(list, testPoint):
        """ ClosestIndexInList(list: IList[Point3d], testPoint: Point3d) -> int """
        pass

    @staticmethod
    def ClosestPointInList(list, testPoint):
        """ ClosestPointInList(list: IList[Point3d], testPoint: Point3d) -> Point3d """
        pass

    def SetAllX(self, xValue):
        """ SetAllX(self: Point3dList, xValue: float) """
        pass

    def SetAllY(self, yValue):
        """ SetAllY(self: Point3dList, yValue: float) """
        pass

    def SetAllZ(self, zValue):
        """ SetAllZ(self: Point3dList, zValue: float) """
        pass

    def Transform(self, xform):
        """ Transform(self: Point3dList, xform: Transform) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, initialCapacity: int)
        __new__(cls: type, collection: IEnumerable[Point3d])
        __new__(cls: type, *initialPoints: Array[Point3d])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: Point3dList) -> BoundingBox

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Point3dList) -> XAccess

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Point3dList) -> YAccess

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: Point3dList) -> ZAccess

"""


    XAccess = None
    YAccess = None
    ZAccess = None


class RhinoList(object, IList[T], ICollection[T], IEnumerable[T], IEnumerable, IList, ICollection):
    """
    RhinoList[T]()
    RhinoList[T](initialCapacity: int)
    RhinoList[T](amount: int, defaultValue: T)
    RhinoList[T](collection: IEnumerable[T])
    RhinoList[T](list: RhinoList[T])
    """
    def Add(self, item):
        """ Add(self: RhinoList[T], item: T) """
        pass

    def AddRange(self, collection):
        """ AddRange(self: RhinoList[T], collection: IEnumerable)AddRange(self: RhinoList[T], collection: IEnumerable[T]) """
        pass

    def AsReadOnly(self):
        """ AsReadOnly(self: RhinoList[T]) -> ReadOnlyCollection[T] """
        pass

    def BinarySearch(self, *__args):
        """
        BinarySearch(self: RhinoList[T], index: int, count: int, item: T, comparer: IComparer[T]) -> int
        BinarySearch(self: RhinoList[T], item: T, comparer: IComparer[T]) -> int
        BinarySearch(self: RhinoList[T], item: T) -> int
        """
        pass

    def Clear(self):
        """ Clear(self: RhinoList[T]) """
        pass

    def Contains(self, item):
        """ Contains(self: RhinoList[T], item: T) -> bool """
        pass

    def ConvertAll(self, converter):
        """ ConvertAll[TOutput](self: RhinoList[T], converter: Converter[T, TOutput]) -> RhinoList[TOutput] """
        pass

    def CopyTo(self, *__args):
        """ CopyTo(self: RhinoList[T], index: int, array: Array[T], arrayIndex: int, count: int)CopyTo(self: RhinoList[T], array: Array[T], arrayIndex: int)CopyTo(self: RhinoList[T], array: Array[T]) """
        pass

    def Exists(self, match):
        """ Exists(self: RhinoList[T], match: Predicate[T]) -> bool """
        pass

    def Find(self, match):
        """ Find(self: RhinoList[T], match: Predicate[T]) -> T """
        pass

    def FindAll(self, match):
        """ FindAll(self: RhinoList[T], match: Predicate[T]) -> RhinoList[T] """
        pass

    def FindIndex(self, *__args):
        """
        FindIndex(self: RhinoList[T], startIndex: int, count: int, match: Predicate[T]) -> int
        FindIndex(self: RhinoList[T], startIndex: int, match: Predicate[T]) -> int
        FindIndex(self: RhinoList[T], match: Predicate[T]) -> int
        """
        pass

    def FindLast(self, match):
        """ FindLast(self: RhinoList[T], match: Predicate[T]) -> T """
        pass

    def FindLastIndex(self, *__args):
        """
        FindLastIndex(self: RhinoList[T], startIndex: int, count: int, match: Predicate[T]) -> int
        FindLastIndex(self: RhinoList[T], startIndex: int, match: Predicate[T]) -> int
        FindLastIndex(self: RhinoList[T], match: Predicate[T]) -> int
        """
        pass

    def ForEach(self, action):
        """ ForEach(self: RhinoList[T], action: Action[T]) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: RhinoList[T]) -> IEnumerator[T] """
        pass

    def GetRange(self, index, count):
        """ GetRange(self: RhinoList[T], index: int, count: int) -> RhinoList[T] """
        pass

    def IndexOf(self, item, index=None, count=None):
        """
        IndexOf(self: RhinoList[T], item: T, index: int, count: int) -> int
        IndexOf(self: RhinoList[T], item: T, index: int) -> int
        IndexOf(self: RhinoList[T], item: T) -> int
        """
        pass

    def Insert(self, index, item):
        """ Insert(self: RhinoList[T], index: int, item: T) """
        pass

    def InsertRange(self, index, collection):
        """ InsertRange(self: RhinoList[T], index: int, collection: IEnumerable[T]) """
        pass

    def LastIndexOf(self, item, index=None, count=None):
        """
        LastIndexOf(self: RhinoList[T], item: T, index: int, count: int) -> int
        LastIndexOf(self: RhinoList[T], item: T, index: int) -> int
        LastIndexOf(self: RhinoList[T], item: T) -> int
        """
        pass

    def RemapIndex(self, index):
        """ RemapIndex(self: RhinoList[T], index: int) -> int """
        pass

    def Remove(self, item):
        """ Remove(self: RhinoList[T], item: T) -> bool """
        pass

    def RemoveAll(self, match):
        """ RemoveAll(self: RhinoList[T], match: Predicate[T]) -> int """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: RhinoList[T], index: int) """
        pass

    def RemoveNulls(self):
        """ RemoveNulls(self: RhinoList[T]) -> int """
        pass

    def RemoveRange(self, index, count):
        """ RemoveRange(self: RhinoList[T], index: int, count: int) """
        pass

    def Reverse(self, index=None, count=None):
        """ Reverse(self: RhinoList[T], index: int, count: int)Reverse(self: RhinoList[T]) """
        pass

    def Sort(self, *__args):
        """ Sort(self: RhinoList[T], index: int, count: int, comparer: IComparer[T])Sort(self: RhinoList[T], keys: Array[float])Sort(self: RhinoList[T], keys: Array[int])Sort(self: RhinoList[T])Sort(self: RhinoList[T], comparer: IComparer[T])Sort(self: RhinoList[T], comparison: Comparison[T]) """
        pass

    def ToArray(self):
        """ ToArray(self: RhinoList[T]) -> Array[T] """
        pass

    def TrimExcess(self):
        """ TrimExcess(self: RhinoList[T]) """
        pass

    def TrueForAll(self, match):
        """ TrueForAll(self: RhinoList[T], match: Predicate[T]) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[T], item: T) -> bool
        
            Determines whether the System.Collections.Generic.ICollection contains a 
             specific value.
        
        
            item: The object to locate in the System.Collections.Generic.ICollection.
            Returns: true if item is found in the System.Collections.Generic.ICollection; otherwise, 
             false.
        
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, 
             false.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, initialCapacity: int)
        __new__(cls: type, amount: int, defaultValue: T)
        __new__(cls: type, collection: IEnumerable[T])
        __new__(cls: type, list: RhinoList[T])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: RhinoList[T]) -> int

Set: Capacity(self: RhinoList[T]) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: RhinoList[T]) -> int

"""

    First = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: First(self: RhinoList[T]) -> T

Set: First(self: RhinoList[T]) = value
"""

    Last = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Last(self: RhinoList[T]) -> T

Set: Last(self: RhinoList[T]) = value
"""

    NullCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NullCount(self: RhinoList[T]) -> int

"""



