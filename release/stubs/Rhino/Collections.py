# encoding: utf-8
# module Rhino.Collections calls itself Collections
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ArchivableDictionary(object, ICloneable, IDictionary[str, object], ICollection[KeyValuePair[str, object]], IEnumerable[KeyValuePair[str, object]], IEnumerable):
    """
    Represents a dictionary class that can be attached to objects and
                can be serialized (saved) at necessity.See remarks for layout.
    
    ArchivableDictionary()
    ArchivableDictionary(parentUserData: UserData)
    ArchivableDictionary(version: int)
    ArchivableDictionary(version: int, name: str)
    """
    def AddContentsFrom(self, source):
        """
        AddContentsFrom(self: ArchivableDictionary, source: ArchivableDictionary) -> bool
        
            Add the contents from the source dictionary.
        """
        pass

    def Clear(self):
        """
        Clear(self: ArchivableDictionary)
            Removes all keys and values from the dictionary.
        """
        pass

    def Clone(self):
        """
        Clone(self: ArchivableDictionary) -> ArchivableDictionary
        
            Constructs a deep copy of this object.
            Returns: The copy of this object.
        """
        pass

    def ContainsKey(self, key):
        """
        ContainsKey(self: ArchivableDictionary, key: str) -> bool
        
            Determines whether the dictionary contains the specified key.
        
            key: The key to locate.
            Returns: true if the dictionary contains an element with the specified key; otherwise, false.
        """
        pass

    def GetBool(self, key, defaultValue=None):
        """
        GetBool(self: ArchivableDictionary, key: str, defaultValue: bool) -> bool
        
            Get value as bool, will return defaultValue unless value was created using Set(string key, bool 
             value)
        
        GetBool(self: ArchivableDictionary, key: str) -> bool
        
            Get value as bool, will only succeed if value was created using Set(string key, bool value)
        """
        pass

    def GetBytes(self, key, defaultValue=None):
        """
        GetBytes(self: ArchivableDictionary, key: str, defaultValue: Array[Byte]) -> Array[Byte]
        
            Get value as byte[], will return defaultValue unless
                    value was created using 
             Set(string key, byte[] value)
        
        GetBytes(self: ArchivableDictionary, key: str) -> Array[Byte]
        
            Get value as byte[], will only succeed if value was created
                    using Set(string key, 
             byte[] value)
        """
        pass

    def GetDictionary(self, key, defaultValue=None):
        """
        GetDictionary(self: ArchivableDictionary, key: str, defaultValue: ArchivableDictionary) -> ArchivableDictionary
        
            Get value as ArchivableDictionary, will return defaultValue unless
                    value was 
             created using Set(string key, ArchivableDictionary value)
        
        GetDictionary(self: ArchivableDictionary, key: str) -> ArchivableDictionary
        
            Get value as ArchivableDictionary, will only succeed if value was created
                    using 
             Set(string key, ArchivableDictionary value)
        """
        pass

    def GetDouble(self, key, defaultValue=None):
        """
        GetDouble(self: ArchivableDictionary, key: str, defaultValue: float) -> float
        
            Get value as double, will only succeed if value was created using Set(string key, double value)
        GetDouble(self: ArchivableDictionary, key: str) -> float
        
            Get value as double, will only succeed if value was created using Set(string key, double value)
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ArchivableDictionary) -> IEnumerator[KeyValuePair[str, object]]
        
            Gets the enumerator of this dictionary.
            Returns: A System.Collections.Generic.IEnumerator, where T is an instance of 
             System.Collections.Generic.KeyValuePair, with T0 set as string, and T1 as Syste.Object.
        """
        pass

    def GetEnumValue(self, key=None):
# Error generating skeleton for function GetEnumValue: Method must be called on a Type for which Type.IsGenericParameter is false.

    def GetFloat(self, key, defaultValue=None):
        """
        GetFloat(self: ArchivableDictionary, key: str, defaultValue: Single) -> Single
        
            Get value as float, will return defaultValue unless value was created using Set(string key, 
             float value)
        
        GetFloat(self: ArchivableDictionary, key: str) -> Single
        
            Get value as float, will only succeed if value was created using Set(string key, float value)
        """
        pass

    def GetGuid(self, key, defaultValue=None):
        """
        GetGuid(self: ArchivableDictionary, key: str, defaultValue: Guid) -> Guid
        
            Get value as Guid, will return defaultValue unless value was created using Set(string key, Guid 
             value)
        
        GetGuid(self: ArchivableDictionary, key: str) -> Guid
        
            Get value as Guid, will only succeed if value was created using Set(string key, Guid value)
        """
        pass

    def Getint(self, key, defaultValue):
        """
        Getint(self: ArchivableDictionary, key: str, defaultValue: int) -> int
        
            Get value as int, will return defaultValue unless value was created using Set(string key, int 
             value)
        """
        pass

    def GetInteger(self, key, defaultValue=None):
        """
        GetInteger(self: ArchivableDictionary, key: str) -> int
        
            Get value as int, will only succeed if value was created using Set(string key, int value)
        GetInteger(self: ArchivableDictionary, key: str, defaultValue: int) -> int
        
            Get value as int, will return defaultValue unless value was created using Set(string key, int 
             value)
        """
        pass

    def GetPoint3d(self, key, defaultValue=None):
        """
        GetPoint3d(self: ArchivableDictionary, key: str, defaultValue: Point3d) -> Point3d
        
            Get value as Point3d, will return defaultValue unless value was created using Set(string key, 
             Point3d value)
        
        GetPoint3d(self: ArchivableDictionary, key: str) -> Point3d
        
            Get value as Point3d, will only succeed if value was created using Set(string key, Point3d value)
        """
        pass

    def GetPoint3f(self, key, defaultValue=None):
        """
        GetPoint3f(self: ArchivableDictionary, key: str, defaultValue: Point3f) -> Point3f
        
            Get value as Point3f, will return defaultValue unless value was created using Set(string key, 
             Point3f value)
        
        GetPoint3f(self: ArchivableDictionary, key: str) -> Point3f
        
            Get value as Point3f, will only succeed if value was created using Set(string key, Point3f value)
        """
        pass

    def GetString(self, key, defaultValue=None):
        """
        GetString(self: ArchivableDictionary, key: str, defaultValue: str) -> str
        
            Get value as string, will return defaultValue unless value was created using Set(string key, 
             string value)
        
        GetString(self: ArchivableDictionary, key: str) -> str
        
            Get value as string, will only succeed if value was created using Set(string key, string value)
        """
        pass

    def GetVector3d(self, key, defaultValue=None):
        """
        GetVector3d(self: ArchivableDictionary, key: str, defaultValue: Vector3d) -> Vector3d
        
            Get value as Vector3d, will return defaultValue unless value was created using Set(string key, 
             Vector3d value)
        
        GetVector3d(self: ArchivableDictionary, key: str) -> Vector3d
        
            Get value as Vector3d, will only succeed if value was created using Set(string key, Vector3d 
             value)
        """
        pass

    def Remove(self, key):
        """
        Remove(self: ArchivableDictionary, key: str) -> bool
        
            Removes the value with the specified key from the dictionary.
        
            key: The key of the element to remove.
            Returns: true if the element is successfully found and removed; otherwise, false.
                    This 
             method returns false if key is not found.
        """
        pass

    def RemoveEnumValue(self):
        """ RemoveEnumValue[T](self: ArchivableDictionary) -> bool """
        pass

    def ReplaceContentsWith(self, source):
        """
        ReplaceContentsWith(self: ArchivableDictionary, source: ArchivableDictionary) -> bool
        
            Replace the contents of the dictionary with that of the given source dictionary.
        """
        pass

    def Set(self, key, val):
        """
        Set(self: ArchivableDictionary, key: str, val: float) -> bool
        
            Sets a System.Double.
        
            key: The text key.
            val: A System.Double.
                    Because System.Double has value semantics, changes to the 
             assigning value will leave this entry unchanged.
        
            Returns: true if set operation succeeded, otherwise false.
        Set(self: ArchivableDictionary, key: str, val: Single) -> bool
        
            Sets a System.Single.
        
            key: The text key.
            val: A System.Single.
                    Because System.Single has value semantics, changes to the 
             assigning value will leave this entry unchanged.
        
            Returns: true if set operation succeeded, otherwise false.
        Set(self: ArchivableDictionary, key: str, val: Guid) -> bool
        
            Sets a System.Guid.
        
            key: The text key.
            val: A System.Guid.
                    Because System.Guid has value semantics, changes to the assigning 
             value will leave this entry unchanged.
        
            Returns: true if set operation succeeded, otherwise false.
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[bool]) -> bool
        Set(self: ArchivableDictionary, key: str, val: str) -> bool
        
            Sets a System.String.
        
            key: The text key.
            val: A System.String.
                    Because System.String is immutable, it is not possible to modify 
             the object while it is in this dictionary.
        
            Returns: true if set operation succeeded, otherwise false.
        Set(self: ArchivableDictionary, key: str, val: Int64) -> bool
        
            Sets a System.Int64.
        
            key: The text key.
            val: A System.Int64.
                    Because System.Int64 has value semantics, changes to the assigning 
             value will leave this entry unchanged.
        
            Returns: true if set operation succeeded, otherwise false.
        Set(self: ArchivableDictionary, key: str, val: Int16) -> bool
        
            Sets a System.Int16.
        
            key: The text key.
            val: A System.Int16.
                    Because System.Int16 has value semantics, changes to the assigning 
             value will leave this entry unchanged.
        
            Returns: true if set operation succeeded, otherwise false.
        Set(self: ArchivableDictionary, key: str, val: SByte) -> bool
        
            Sets a System.SByte.
        
            key: The text key.
            val: A System.SByte.
                    Because System.SByte has value semantics, changes to the assigning 
             value will leave this entry unchanged.
        
            Returns: true if set operation succeeded, otherwise false.
        Set(self: ArchivableDictionary, key: str, val: UInt16) -> bool
        
            Sets a System.UInt16.
        
            key: The text key.
            val: A System.UInt16.
                    Because System.UInt16 has value semantics, changes to the 
             assigning value will leave this entry unchanged.
        
            Returns: true if set operation succeeded, otherwise false.
        Set(self: ArchivableDictionary, key: str, val: UInt32) -> bool
        
            Sets a System.UInt32.
        
            key: The text key.
            val: A System.UInt32.
                    Because System.UInt32 has value semantics, changes to the 
             assigning value will leave this entry unchanged.
        
            Returns: true if set operation succeeded, otherwise false.
        Set(self: ArchivableDictionary, key: str, val: int) -> bool
        
            Sets a System.Int32.
        
            key: The text key.
            val: A System.Int32.
                    Because System.Int32 has value semantics, changes to the assigning 
             value will leave this entry unchanged.
        
            Returns: true if set operation succeeded, otherwise false.
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[Byte]) -> bool
        Set(self: ArchivableDictionary, key: str, val: Color) -> bool
        
            Sets a System.Drawing.Color.
        
            key: A text key.
            val: A value for that key.
                    Because System.Drawing.Color has value semantics, changes to 
             the
                    assigning value will leave this entry unchanged.
        
            Returns: true if set operation succeeded, otherwise false.
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[str]) -> bool
        Set(self: ArchivableDictionary, key: str, val: Point) -> bool
        
            Sets a System.Drawing.Point.
        
            key: A text key.
            val: A value for that key.
                    Because System.Drawing.Point has value semantics, changes to 
             the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: Rectangle) -> bool
        
            Sets a System.Drawing.Rectangle.
        
            key: A text key.
            val: A value for that key.
                    Because System.Drawing.Rectangle has value semantics, changes 
             to the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: PointF) -> bool
        
            Sets a System.Drawing.PointF.
        
            key: A text key.
            val: A value for that key.
                    Because System.Drawing.PointF has value semantics, changes to 
             the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[Guid]) -> bool
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[Int16]) -> bool
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[SByte]) -> bool
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[int]) -> bool
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[float]) -> bool
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[Single]) -> bool
        Set(self: ArchivableDictionary, key: str, val: Byte) -> bool
        
            Sets a System.Byte.
        
            key: The text key.
            val: A System.Byte.
                    Because System.Byte has value semantics, changes to the assigning 
             value will leave this entry unchanged.
        
            Returns: true if set operation succeeded, otherwise false.
        Set(self: ArchivableDictionary, key: str, val: Point4d) -> bool
        
            Sets a Rhino.Geometry.Point4d.
        
            key: A text key.
            val: A value for that key.
                    Because Rhino.Geometry.Point4d has value semantics, changes 
             to the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: Point3d) -> bool
        
            Sets a Rhino.Geometry.Point3d.
        
            key: A text key.
            val: A point for that key.
                    Because Rhino.Geometry.Point3d has value semantics, changes 
             to the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: Vector2d) -> bool
        
            Sets a Rhino.Geometry.Vector2d.
        
            key: A text key.
            val: A value for that key.
                    Because Rhino.Geometry.Vector2d has value semantics, changes 
             to the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: BoundingBox) -> bool
        
            Sets a Rhino.Geometry.BoundingBox.
        
            key: A text key.
            val: A value for that key.
                    Because Rhino.Geometry.BoundingBox has value semantics, 
             changes to the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: Vector3d) -> bool
        
            Sets a Rhino.Geometry.Vector3d.
        
            key: A text key.
            val: A value for that key.
                    Because Rhino.Geometry.Vector3d has value semantics, changes 
             to the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: Point2d) -> bool
        
            Sets a Rhino.Geometry.Point2d.
        
            key: A text key.
            val: A point for that key.
                    Because Rhino.Geometry.Point2d has value semantics, changes 
             to the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: Size) -> bool
        
            Sets a System.Drawing.Size.
        
            key: A text key.
            val: A value for that key.
                    Because System.Drawing.Size has value semantics, changes to 
             the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: RectangleF) -> bool
        
            Sets a System.Drawing.RectangleF.
        
            key: A text key.
            val: A value for that key.
                    Because System.Drawing.RectangleF has value semantics, 
             changes to the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: SizeF) -> bool
        
            Sets a System.Drawing.SizeF.
        
            key: A text key.
            val: A value for that key.
                    Because System.Drawing.SizeF has value semantics, changes to 
             the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: Interval) -> bool
        
            Sets an Rhino.Geometry.Interval.
        
            key: A text key.
            val: A value for that key.
                    Because Rhino.Geometry.Interval has value semantics, changes 
             to the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: Font) -> bool
        
            Sets a System.Drawing.Font.
        
            key: A text key.
            val: A value for that key.
                    Because System.Drawing.Font is immutable, it is not possible 
             to modify the object while it is in this dictionary.
        
        Set(self: ArchivableDictionary, key: str, val: Ray3d) -> bool
        
            Sets a Rhino.Geometry.Ray3d.
        
            key: A text key.
            val: A value for that key.
                    Because Rhino.Geometry.Ray3d has value semantics and is 
             immutable, no changes to this object are possible.
        
        Set(self: ArchivableDictionary, key: str, val: GeometryBase) -> bool
        
            Sets any class deriving from the Rhino.Geometry.GeometryBase base class.
        
            key: A text key.
            val: A geometry object for that key.
                    Because this class is a reference type and is 
             mutable, changes to this object will propagate to the object inside the dictionary.It is up to 
             the user to clone this entry when appropriate. You can use Rhino.Geometry.GeometryBase.Duplicate 
             for this.
        
        Set(self: ArchivableDictionary, key: str, val: MeshingParameters) -> bool
        
            Sets a Rhino.Geometry.MeshingParameters.
        
            key: A text key.
            val: An object for that key.
                    Because this class is a reference type and is mutable, 
             changes to this object will propagate to the object inside the dictionary.It is up to the user 
             to clone this entry when appropriate.
        
        Set(self: ArchivableDictionary, key: str, val: ObjRef) -> bool
        
            Sets a Rhino.DocObjects.ObjRef
        
            key: A text key
            val: An object for that key
                    Because this class is a reference type and is mutable, 
             changes to this object will propagate to the object inside the dictionary.It is up to the user 
             to clone this entry when appropriate.
        
        Set(self: ArchivableDictionary, key: str, val: bool) -> bool
        
            Sets a System.Boolean.
        
            key: The text key.
            val: A System.Boolean value.
                    Because System.Boolean has value semantics, changes to the 
             assigning value will leave this entry unchanged.
        
            Returns: true if set operation succeeded, otherwise false.
        Set(self: ArchivableDictionary, key: str, val: IEnumerable[ObjRef]) -> bool
        Set(self: ArchivableDictionary, key: str, val: ArchivableDictionary) -> bool
        
            Sets another Rhino.Collections.ArchivableDictionary as entry in this dictionary.
        
            key: A text key.
            val: An object for that key.
                    Because this class is a reference type and is mutable, 
             changes to this object will propagate to the object inside the dictionary.It is up to the user 
             to clone this entry when appropriate.
        
        Set(self: ArchivableDictionary, key: str, val: Plane) -> bool
        
            Sets a Rhino.Geometry.Plane.
        
            key: A text key.
            val: A plane for that key.
                    Because Rhino.Geometry.Plane has value semantics, changes to 
             the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: Transform) -> bool
        
            Sets a Rhino.Geometry.Transform.
        
            key: A text key.
            val: A transform for that key.
                    Because Rhino.Geometry.Transform has value semantics, 
             changes to the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: Line) -> bool
        
            Sets a Rhino.Geometry.Line.
        
            key: A text key.
            val: A value for that key.
                    Because Rhino.Geometry.Line has value semantics, changes to 
             the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: Vector3f) -> bool
        
            Sets a Rhino.Geometry.Vector3f.
        
            key: A text key.
            val: A value for that key.
                    Because Rhino.Geometry.Vector3f has value semantics, changes 
             to the assigning value will leave this entry unchanged.
        
        Set(self: ArchivableDictionary, key: str, val: Point3f) -> bool
        
            Sets a Rhino.Geometry.Point3f.
        
            key: A text key.
            val: A value for that key.
                    Because Rhino.Geometry.Point3f has value semantics, changes 
             to the assigning value will leave this entry unchanged.
        """
        pass

    def SetEnumValue(self, *__args):
        """
        SetEnumValue[T](self: ArchivableDictionary, key: str, enumValue: T) -> bool
        SetEnumValue[T](self: ArchivableDictionary, enumValue: T) -> bool
        """
        pass

    def TryGetBool(self, key, value):
        """
        TryGetBool(self: ArchivableDictionary, key: str) -> (bool, bool)
        
            Get value as bool, will only succeed if value was created using Set(string key, bool value)
        """
        pass

    def TryGetBytes(self, key, value):
        """
        TryGetBytes(self: ArchivableDictionary, key: str) -> (bool, Array[Byte])
        
            Get value as byte[], will only succeed if value was
                    created using Set(string key, 
             byte[] value)
        """
        pass

    def TryGetDictionary(self, key, value):
        """
        TryGetDictionary(self: ArchivableDictionary, key: str) -> (bool, ArchivableDictionary)
        
            Get value as ArchivableDictionary, will only succeed if value was
                    created using 
             Set(string key, ArchivableDictionary value)
        """
        pass

    def TryGetDouble(self, key, value):
        """
        TryGetDouble(self: ArchivableDictionary, key: str) -> (bool, float)
        
            Get value as double, will only succeed if value was created using Set(string key, double value)
        """
        pass

    def TryGetEnumValue(self, key, enumValue):
# Error generating skeleton for function TryGetEnumValue: Method must be called on a Type for which Type.IsGenericParameter is false.

    def TryGetFloat(self, key, value):
        """
        TryGetFloat(self: ArchivableDictionary, key: str) -> (bool, Single)
        
            Get value as float, will only succeed if value was created using Set(string key, float value)
        """
        pass

    def TryGetGuid(self, key, value):
        """
        TryGetGuid(self: ArchivableDictionary, key: str) -> (bool, Guid)
        
            Get value as Guid, will only succeed if value was created using Set(string key, Guid value)
        """
        pass

    def TryGetInteger(self, key, value):
        """
        TryGetInteger(self: ArchivableDictionary, key: str) -> (bool, int)
        
            Get value as int, will only succeed if value was created using Set(string key, int value)
        """
        pass

    def TryGetPoint3d(self, key, value):
        """
        TryGetPoint3d(self: ArchivableDictionary, key: str) -> (bool, Point3d)
        
            Get value as Point3d, will only succeed if value was created using Set(string key, Point3d value)
        """
        pass

    def TryGetPoint3f(self, key, value):
        """
        TryGetPoint3f(self: ArchivableDictionary, key: str) -> (bool, Point3f)
        
            Get value as Point3f, will only succeed if value was created using Set(string key, Point3f value)
        """
        pass

    def TryGetString(self, key, value):
        """
        TryGetString(self: ArchivableDictionary, key: str) -> (bool, str)
        
            Get value as string, will only succeed if value was created using Set(string key, string value)
        """
        pass

    def TryGetValue(self, key, value):
        """
        TryGetValue(self: ArchivableDictionary, key: str) -> (bool, object)
        
            Gets the value associated with the specified key.
        
            key: The key of the value to get.
            Returns: true if the dictionary contains an element with the specified key; otherwise, false.
        """
        pass

    def TryGetVector3d(self, key, value):
        """
        TryGetVector3d(self: ArchivableDictionary, key: str) -> (bool, Vector3d)
        
            Get value as Vector3d, will only succeed if value was created using Set(string key, Vector3d 
             value)
        """
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
    """Gets the number of key/value pairs contained in the dictionary.

Get: Count(self: ArchivableDictionary) -> int

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all entry names or keys.

Get: Keys(self: ArchivableDictionary) -> Array[str]

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name string of this Rhino.Collections.ArchivableDictionary.

Get: Name(self: ArchivableDictionary) -> str

Set: Name(self: ArchivableDictionary) = value
"""

    ParentUserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If this dictionary is part of userdata (or is a UserDictionary), then
            this is the parent user data. null if this dictionary is not part of
            userdata

Get: ParentUserData(self: ArchivableDictionary) -> UserData

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all values in this dictionary.

Get: Values(self: ArchivableDictionary) -> Array[object]

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the version of this Rhino.Collections.ArchivableDictionary.

Get: Version(self: ArchivableDictionary) -> int

Set: Version(self: ArchivableDictionary) = value
"""



class CurveList(RhinoList[Curve], IList[Curve], ICollection[Curve], IEnumerable[Curve], IEnumerable, IList, ICollection):
    """
    Represents a list of curves.
    
    CurveList()
    CurveList(initialCapacity: int)
    CurveList(collection: IEnumerable[Curve])
    """
    def Add(self, *__args):
        """
        Add(self: CurveList, polyline: IEnumerable[Point3d])Add(self: CurveList, ellipse: Ellipse)
            Adds an ellipse to this list.
        
            ellipse: An ellipse that will be the model of the new internal curve.
        Add(self: CurveList, arc: Arc)
            Adds an arc to this list.
        
            arc: An arc value that will be the model of the new internal curve.
        Add(self: CurveList, line: Line)
            Adds a line to this list.
        
            line: A line value that will be the model of the new internal curve.
        Add(self: CurveList, circle: Circle)
            Adds a circle to this list.
        
            circle: A circle value that will be the model of the new internal curve.
        """
        pass

    def Insert(self, index, *__args):
        """
        Insert(self: CurveList, index: int, polyline: IEnumerable[Point3d])Insert(self: CurveList, index: int, ellipse: Ellipse)
            Inserts an ellipse at a given index of this list.
        
            index: A 0-based position in the list.
            ellipse: The ellipse value from which to construct the new curve.
        Insert(self: CurveList, index: int, arc: Arc)
            Inserts an arc at a given index of this list.
        
            index: A 0-based position in the list.
            arc: The arc value from which to construct the new curve.
        Insert(self: CurveList, index: int, line: Line)
            Inserts a line at a given index of this list.
        
            index: A 0-based position in the list.
            line: The line value from which to construct the new curve.
        Insert(self: CurveList, index: int, circle: Circle)
            Inserts a line at a given index of this list.
        
            index: A 0-based position in the list.
            circle: The circle value from which to construct the new curve.
        """
        pass

    def Transform(self, xform):
        """
        Transform(self: CurveList, xform: Transform) -> bool
        
            Transform all the curves in this list. If at least a single transform failed 
                    this 
             function returns false.
        
        
            xform: Transformation to apply to all curves.
        """
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
    Represents a list of Rhino.Geometry.Point3d.
    
    Point3dList()
    Point3dList(initialCapacity: int)
    Point3dList(collection: IEnumerable[Point3d])
    Point3dList(*initialPoints: Array[Point3d])
    """
    def Add(self, *__args):
        """
        Add(self: Point3dList, x: float, y: float, z: float)
            Adds a Point3d to the end of the list with given x,y,z coordinates.
        
            x: The X coordinate.
            y: The Y coordinate.
            z: The Z coordinate.
        """
        pass

    def ClosestIndex(self, testPoint):
        """
        ClosestIndex(self: Point3dList, testPoint: Point3d) -> int
        
            Finds the index of the point that is closest to a test point in this list.
        
            testPoint: point to compare against.
            Returns: index of closest point in the list on success. -1 on error.
        """
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
        """
        SetAllX(self: Point3dList, xValue: float)
            Set all the X values for the points to a single value
        """
        pass

    def SetAllY(self, yValue):
        """
        SetAllY(self: Point3dList, yValue: float)
            Set all the Y values for the points to a single value
        """
        pass

    def SetAllZ(self, zValue):
        """
        SetAllZ(self: Point3dList, zValue: float)
            Set all the Z values for the points to a single value
        """
        pass

    def Transform(self, xform):
        """
        Transform(self: Point3dList, xform: Transform)
            Applies a transform to all the points in the list.
        
            xform: Transform to apply.
        """
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
    """Even though this is a property, it is not a "fast" calculation. Every point is
            evaluated in order to get the bounding box of the list.

Get: BoundingBox(self: Point3dList) -> BoundingBox

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns an indexer with all X coordinates in this list.

Get: X(self: Point3dList) -> XAccess

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns an indexer with all Y coordinates in this list.

Get: Y(self: Point3dList) -> YAccess

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns an indexer with all Z coordinates in this list.

Get: Z(self: Point3dList) -> ZAccess

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
        """
        Add(self: RhinoList[T], item: T)
            Adds an object to the end of the List.
        
            item: Item to append.
        """
        pass

    def AddRange(self, collection):
        """
        AddRange(self: RhinoList[T], collection: IEnumerable)
            Adds the elements of the specified collection to the end of the List.
        
            collection: The collection whose elements should be added to the end of the List. 
                    The 
             collection itself cannot be a null reference (Nothing in Visual Basic), 
                    but it can 
             contain elements that are a null reference (Nothing in Visual Basic). 
                    Objects in 
             collection which cannot be represented as T will throw exceptions.
        
        AddRange(self: RhinoList[T], collection: IEnumerable[T])
            Adds the elements of the specified collection to the end of the List.
        
            collection: The collection whose elements should be added to the end of the List. 
                    The 
             collection itself cannot be a null reference (Nothing in Visual Basic), 
                    but it can 
             contain elements that are a null reference (Nothing in Visual Basic), 
                    if type T is 
             a reference type.
        """
        pass

    def AsReadOnly(self):
        """
        AsReadOnly(self: RhinoList[T]) -> ReadOnlyCollection[T]
        
            Constructs a read-only wrapper of this class.
            Returns: A wrapper.
        """
        pass

    def BinarySearch(self, *__args):
        """
        BinarySearch(self: RhinoList[T], index: int, count: int, item: T, comparer: IComparer[T]) -> int
        
            Searches the entire sorted List for an element using the specified 
                    comparer and 
             returns the zero-based index of the element.
        
        
            index: The zero-based starting index of the range to search.
            count: The length of the range to search.
            item: The object to locate. The value can be a null reference 
                    (Nothing in Visual Basic) 
             for reference types.
        
            comparer: The IComparer(T) implementation to use when comparing elements.
                    Or a null reference 
             (Nothing in Visual Basic) to use the default comparer 
                    Comparer(T)::Default.
        
            Returns: The zero-based index of item in the sorted List, if item is found; 
                    otherwise, a 
             negative number that is the bitwise complement of the index 
                    of the next element 
             that is larger than item or, if there is no larger element, 
                    the bitwise complement 
             of Count.
        
        BinarySearch(self: RhinoList[T], item: T, comparer: IComparer[T]) -> int
        
            Searches the entire sorted List for an element using the specified 
                    comparer and 
             returns the zero-based index of the element.
        
        
            item: The object to locate. The value can be a null reference 
                    (Nothing in Visual Basic) 
             for reference types.
        
            comparer: The IComparer(T) implementation to use when comparing elements.
                    Or a null reference 
             (Nothing in Visual Basic) to use the default comparer 
                    Comparer(T)::Default.
        
            Returns: The zero-based index of item in the sorted List, if item is found; 
                    otherwise, a 
             negative number that is the bitwise complement of the index 
                    of the next element 
             that is larger than item or, if there is no larger element, 
                    the bitwise complement 
             of Count.
        
        BinarySearch(self: RhinoList[T], item: T) -> int
        
            Searches the entire sorted List for an element using the default comparer 
                    and 
             returns the zero-based index of the element.
        
        
            item: The object to locate. The value can be a null reference 
                    (Nothing in Visual Basic) 
             for reference types.
        
            Returns: The zero-based index of item in the sorted List, if item is found; 
                    otherwise, a 
             negative number that is the bitwise complement of the index 
                    of the next element 
             that is larger than item or, if there is no larger element, 
                    the bitwise complement 
             of Count.
        """
        pass

    def Clear(self):
        """
        Clear(self: RhinoList[T])
            Removes all elements from the List.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: RhinoList[T], item: T) -> bool
        
            Determines whether an element is in the List.
        
            item: The object to locate in the List. 
                    The value can be a null reference (Nothing in 
             Visual Basic) for reference types.
        
            Returns: true if item is found in the List; otherwise, false.
        """
        pass

    def ConvertAll(self, converter):
        """ ConvertAll[TOutput](self: RhinoList[T], converter: Converter[T, TOutput]) -> RhinoList[TOutput] """
        pass

    def CopyTo(self, *__args):
        """ CopyTo(self: RhinoList[T], index: int, array: Array[T], arrayIndex: int, count: int)CopyTo(self: RhinoList[T], array: Array[T], arrayIndex: int)CopyTo(self: RhinoList[T], array: Array[T]) """
        pass

    def Exists(self, match):
        """
        Exists(self: RhinoList[T], match: Predicate[T]) -> bool
        
            Determines whether the List contains elements that match the 
                    conditions defined by 
             the specified predicate.
        
        
            match: The Predicate(T) delegate that defines the conditions of the elements to search for.
            Returns: true if the List contains one or more elements that match the 
                    conditions defined 
             by the specified predicate; otherwise, false.
        """
        pass

    def Find(self, match):
        """
        Find(self: RhinoList[T], match: Predicate[T]) -> T
        
            Searches for an element that matches the conditions defined by the 
                    specified 
             predicate, and returns the first occurrence within the entire List.
        
        
            match: The Predicate(T) delegate that defines the conditions of the element to search for.
            Returns: The first element that matches the conditions defined by the specified predicate, 
                    
             if found; otherwise, the default value for type T.
        """
        pass

    def FindAll(self, match):
        """
        FindAll(self: RhinoList[T], match: Predicate[T]) -> RhinoList[T]
        
            Retrieves all the elements that match the conditions defined by the specified predicate.
        
            match: The Predicate(T) delegate that defines the conditions of the elements to search for.
            Returns: A ON_List(T) containing all the elements that match the conditions 
                    defined by the 
             specified predicate, if found; otherwise, an empty ON_List(T).
        """
        pass

    def FindIndex(self, *__args):
        """
        FindIndex(self: RhinoList[T], startIndex: int, count: int, match: Predicate[T]) -> int
        
            Searches for an element that matches the conditions defined by the specified predicate, 
               
                  and returns the zero-based index of the first occurrence within the range of elements 
            
                     in the List that extends from the specified index to the last element.
        
        
            startIndex: The zero-based starting index of the search.
            count: The number of elements in the section to search.
            match: The Predicate(T) delegate that defines the conditions of the element to search for.
            Returns: The zero-based index of the first occurrence of an element that 
                    matches the 
             conditions defined by match, if found; otherwise, -1.
        
        FindIndex(self: RhinoList[T], startIndex: int, match: Predicate[T]) -> int
        
            Searches for an element that matches the conditions defined by the 
                    specified 
             predicate, and returns the zero-based index of the first 
                    occurrence within the 
             entire List.
        
        
            startIndex: The zero-based starting index of the search.
            match: The Predicate(T) delegate that defines the conditions of the element to search for.
            Returns: The zero-based index of the first occurrence of an element that 
                    matches the 
             conditions defined by match, if found; otherwise, -1.
        
        FindIndex(self: RhinoList[T], match: Predicate[T]) -> int
        
            Searches for an element that matches the conditions defined by the 
                    specified 
             predicate, and returns the zero-based index of the first 
                    occurrence within the 
             entire List.
        
        
            match: The Predicate(T) delegate that defines the conditions of the element to search for.
            Returns: The zero-based index of the first occurrence of an element that 
                    matches the 
             conditions defined by match, if found; otherwise, -1.
        """
        pass

    def FindLast(self, match):
        """
        FindLast(self: RhinoList[T], match: Predicate[T]) -> T
        
            Searches for an element that matches the conditions defined by the 
                    specified 
             predicate, and returns the last occurrence within the entire List.
        
        
            match: The Predicate(T) delegate that defines the conditions of the element to search for.
            Returns: The last element that matches the conditions defined by the specified predicate, 
                    
             if found; otherwise, the default value for type T.
        """
        pass

    def FindLastIndex(self, *__args):
        """
        FindLastIndex(self: RhinoList[T], startIndex: int, count: int, match: Predicate[T]) -> int
        
            Searches for an element that matches the conditions defined by the 
                    specified 
             predicate, and returns the zero-based index of the last 
                    occurrence within the 
             entire List.
        
        
            startIndex: The zero-based starting index of the backward search.
            count: The number of elements in the section to search.
            match: The Predicate(T) delegate that defines the conditions of the element to search for.
            Returns: The zero-based index of the last occurrence of an element that matches 
                    the 
             conditions defined by match, if found; otherwise, -1.
        
        FindLastIndex(self: RhinoList[T], startIndex: int, match: Predicate[T]) -> int
        
            Searches for an element that matches the conditions defined by the 
                    specified 
             predicate, and returns the zero-based index of the last 
                    occurrence within the 
             entire List.
        
        
            startIndex: The zero-based starting index of the backward search.
            match: The Predicate(T) delegate that defines the conditions of the element to search for.
            Returns: The zero-based index of the last occurrence of an element that matches 
                    the 
             conditions defined by match, if found; otherwise, -1.
        
        FindLastIndex(self: RhinoList[T], match: Predicate[T]) -> int
        
            Searches for an element that matches the conditions defined by the 
                    specified 
             predicate, and returns the zero-based index of the last 
                    occurrence within the 
             entire List.
        
        
            match: The Predicate(T) delegate that defines the conditions of the element to search for.
            Returns: The zero-based index of the last occurrence of an element that matches 
                    the 
             conditions defined by match, if found; otherwise, -1.
        """
        pass

    def ForEach(self, action):
        """
        ForEach(self: RhinoList[T], action: Action[T])
            Performs the specified action on each element of the List.
        
            action: The Action(T) delegate to perform on each element of the List.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: RhinoList[T]) -> IEnumerator[T]
        
            Constructs an enumerator that is capable of iterating over all items in this list.
            Returns: The new enumerator.
        """
        pass

    def GetRange(self, index, count):
        """
        GetRange(self: RhinoList[T], index: int, count: int) -> RhinoList[T]
        
            Constructs a shallow copy of a range of elements in the source List.
        
            index: The zero-based List index at which the range starts.
            count: The number of elements in the range.
            Returns: A shallow copy of a range of elements in the source List.
        """
        pass

    def IndexOf(self, item, index=None, count=None):
        """
        IndexOf(self: RhinoList[T], item: T, index: int, count: int) -> int
        
            Searches for the specified object and returns the zero-based index of the first 
                    
             occurrence within the range of elements in the List that starts at the specified 
                    
             index and contains the specified number of elements.
        
        
            item: The object to locate in the List. 
                    The value can be a null reference (Nothing in 
             Visual Basic) 
                    for reference types.
        
            index: The zero-based starting index of the search.
            count: The number of elements in the section to search.
            Returns: The zero-based index of the first occurrence of item within 
                    the entire List, if 
             found; otherwise, -1.
        
        IndexOf(self: RhinoList[T], item: T, index: int) -> int
        
            Searches for the specified object and returns the zero-based index of 
                    the first 
             occurrence within the range of elements in the List that 
                    extends from the 
             specified index to the last element.
        
        
            item: The object to locate in the List. 
                    The value can be a null reference (Nothing in 
             Visual Basic) 
                    for reference types.
        
            index: The zero-based starting index of the search.
            Returns: The zero-based index of the first occurrence of item within 
                    the entire List, if 
             found; otherwise, -1.
        
        IndexOf(self: RhinoList[T], item: T) -> int
        
            Searches for the specified object and returns the zero-based index of the 
                    first 
             occurrence within the entire List.
        
        
            item: The object to locate in the List. 
                    The value can be a null reference (Nothing in 
             Visual Basic) 
                    for reference types.
        
            Returns: The zero-based index of the first occurrence of item within 
                    the entire List, if 
             found; otherwise, -1.
        """
        pass

    def Insert(self, index, item):
        """
        Insert(self: RhinoList[T], index: int, item: T)
            Inserts an element into the List at the specified index.
        
            index: The zero-based index at which item should be inserted.
            item: The object to insert. The value can be a null reference 
                    (Nothing in Visual Basic) 
             for reference types.
        """
        pass

    def InsertRange(self, index, collection):
        """
        InsertRange(self: RhinoList[T], index: int, collection: IEnumerable[T])
            Inserts the elements of a collection into the List at the specified index.
        
            index: The zero-based index at which the new elements should be inserted.
            collection: The collection whose elements should be inserted into the List. 
                    The collection 
             itself cannot be a null reference (Nothing in Visual Basic), 
                    but it can contain 
             elements that are a null reference (Nothing in Visual Basic), 
                    if type T is a 
             reference type.
        """
        pass

    def LastIndexOf(self, item, index=None, count=None):
        """
        LastIndexOf(self: RhinoList[T], item: T, index: int, count: int) -> int
        
            Searches for the specified object and returns the zero-based index of the 
                    last 
             occurrence within the range of elements in the List that contains 
                    the specified 
             number of elements and ends at the specified index.
        
        
            item: The object to locate in the List. 
                    The value can be a null reference (Nothing in 
             Visual Basic) for reference types.
        
            index: The zero-based starting index of the backward search.
            count: The number of elements in the section to search.
            Returns: The zero-based index of the last occurrence of item within 
                    the entire the List, if 
             found; otherwise, -1.
        
        LastIndexOf(self: RhinoList[T], item: T, index: int) -> int
        
            Searches for the specified object and returns the zero-based index 
                    of the last 
             occurrence within the range of elements in the List 
                    that extends from the first 
             element to the specified index.
        
        
            item: The object to locate in the List. 
                    The value can be a null reference (Nothing in 
             Visual Basic) for reference types.
        
            index: The zero-based starting index of the backward search.
            Returns: The zero-based index of the last occurrence of item within 
                    the entire the List, if 
             found; otherwise, -1.
        
        LastIndexOf(self: RhinoList[T], item: T) -> int
        
            Searches for the specified object and returns the zero-based 
                    index of the last 
             occurrence within the entire List.
        
        
            item: The object to locate in the List. 
                    The value can be a null reference (Nothing in 
             Visual Basic) for reference types.
        
            Returns: The zero-based index of the last occurrence of item within 
                    the entire the List, if 
             found; otherwise, -1.
        """
        pass

    def RemapIndex(self, index):
        """
        RemapIndex(self: RhinoList[T], index: int) -> int
        
            Remap an index in the infinite range onto the List index range.
        
            index: Index to remap.
            Returns: Remapped index.
        """
        pass

    def Remove(self, item):
        """
        Remove(self: RhinoList[T], item: T) -> bool
        
            Removes the first occurrence of a specific object from the List.
        
            item: The object to remove from the List. 
                    The value can be a null reference (Nothing in 
             Visual Basic) for reference types.
        
            Returns: true if item is successfully removed; otherwise, false. 
                    This method also returns 
             false if item was not found in the List.
        """
        pass

    def RemoveAll(self, match):
        """
        RemoveAll(self: RhinoList[T], match: Predicate[T]) -> int
        
            Removes the all the elements that match the conditions defined by the specified predicate.
        
            match: The Predicate(T) delegate that defines the conditions of the elements to remove.
            Returns: The number of elements removed from the List.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: RhinoList[T], index: int)
            Removes the element at the specified index of the List.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def RemoveNulls(self):
        """
        RemoveNulls(self: RhinoList[T]) -> int
        
            Removes all elements from the List that are null references (Nothing in Visual Basic). 
                
                 This function will not do anything if T is not a Reference type.
        
            Returns: The number of nulls removed from the List.
        """
        pass

    def RemoveRange(self, index, count):
        """
        RemoveRange(self: RhinoList[T], index: int, count: int)
            Removes a range of elements from the List.
        
            index: The zero-based starting index of the range of elements to remove.
            count: The number of elements to remove.
        """
        pass

    def Reverse(self, index=None, count=None):
        """
        Reverse(self: RhinoList[T], index: int, count: int)
            Reverses the order of the elements in the specified range.
        
            index: The zero-based starting index of the range to reverse.
            count: The number of elements in the range to reverse.
        Reverse(self: RhinoList[T])
            Reverses the order of the elements in the entire List.
        """
        pass

    def Sort(self, *__args):
        """
        Sort(self: RhinoList[T], index: int, count: int, comparer: IComparer[T])
            Sorts the elements in a range of elements in list using the specified comparer.
        
            index: The zero-based starting index of the range to sort.
            count: The length of the range to sort.
            comparer: The IComparer(T) implementation to use when comparing 
                    elements, or a null 
             reference (Nothing in Visual Basic) to use the default 
                    comparer 
             Comparer(T).Default.
        
        Sort(self: RhinoList[T], keys: Array[float])
            Sort this list based on a list of numeric keys of equal length. 
                    The keys array 
             will not be altered.
        
        
            keys: Numeric keys to sort with.
        Sort(self: RhinoList[T], keys: Array[int])
            Sort this list based on a list of numeric keys of equal length. 
                    The keys array 
             will not be altered.
        
        
            keys: Numeric keys to sort with.
        Sort(self: RhinoList[T])
            Sorts the elements in the entire List using the default comparer.
        Sort(self: RhinoList[T], comparer: IComparer[T])
            Sorts the elements in the entire list using the specified System.Comparison(T)
        
            comparer: The IComparer(T) implementation to use when comparing elements, 
                    or a null 
             reference (Nothing in Visual Basic) to use the default comparer Comparer(T).Default.
        
        Sort(self: RhinoList[T], comparison: Comparison[T])
            Sorts the elements in the entire list using the specified comparer.
        
            comparison: The System.Comparison(T) to use when comparing elements.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: RhinoList[T]) -> Array[T]
        
            Constructs an array that contains all items in this list.
            Returns: An array containing all items in this list.
        """
        pass

    def TrimExcess(self):
        """
        TrimExcess(self: RhinoList[T])
            Sets the capacity to the actual number of elements in the List, 
                    if that number is 
             less than a threshold value.
        """
        pass

    def TrueForAll(self, match):
        """
        TrueForAll(self: RhinoList[T], match: Predicate[T]) -> bool
        
            Determines whether every element in the List matches the conditions defined by the specified 
             predicate.
        
        
            match: The Predicate(T) delegate that defines the conditions to check against the elements.
            Returns: true if every element in the List matches the conditions defined by 
                    the specified 
             predicate; otherwise, false. If the list has no elements, the return value is true.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[T], item: T) -> bool
        
            Determines whether the System.Collections.Generic.ICollection contains a specific value.
        
            item: The object to locate in the System.Collections.Generic.ICollection.
            Returns: true if item is found in the System.Collections.Generic.ICollection; otherwise, false.
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
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
    """Gets or sets the total number of elements the internal data structure can hold without resizing.

Get: Capacity(self: RhinoList[T]) -> int

Set: Capacity(self: RhinoList[T]) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements actually contained in the List.

Get: Count(self: RhinoList[T]) -> int

"""

    First = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the first item in the list. This is synonymous to calling List[0].

Get: First(self: RhinoList[T]) -> T

Set: First(self: RhinoList[T]) = value
"""

    Last = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the last item in the list. This is synonymous to calling List[Count-1].

Get: Last(self: RhinoList[T]) -> T

Set: Last(self: RhinoList[T]) = value
"""

    NullCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of null references (Nothing in Visual Basic) in this list. 
            If T is a ValueType, this property always return zero.

Get: NullCount(self: RhinoList[T]) -> int

"""



class TransformObjectList(object, IDisposable):
    """
    Used by the TransformCommand and GetTransform classes.
    
    TransformObjectList()
    """
    def Add(self, *__args):
        """
        Add(self: TransformObjectList, objref: ObjRef)
            Add an ObjRef to this list. Use this to add Polyedges so the references are properly counted
        Add(self: TransformObjectList, rhinoObject: RhinoObject)
            Add a RhinoObject to this list
        """
        pass

    def Clear(self):
        """
        Clear(self: TransformObjectList)
            Remove all elements from this list
        """
        pass

    def Dispose(self):
        """ Dispose(self: TransformObjectList) """
        pass

    def GetBoundingBox(self, regularObjects, grips):
        """
        GetBoundingBox(self: TransformObjectList, regularObjects: bool, grips: bool) -> BoundingBox
        
            Gets the bounding box of all of the objects that this list contains.
        
            regularObjects: true if any object except grips should be included; otherwise false.
            grips: true if grips should be included; otherwise false.
            Returns: Unset BoundingBox if this list is empty.
        """
        pass

    def UpdateDisplayFeedbackTransform(self, xform):
        """ UpdateDisplayFeedbackTransform(self: TransformObjectList, xform: Transform) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of elements in this list

Get: Count(self: TransformObjectList) -> int

"""

    DisplayFeedbackEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayFeedbackEnabled(self: TransformObjectList) -> bool

Set: DisplayFeedbackEnabled(self: TransformObjectList) = value
"""



