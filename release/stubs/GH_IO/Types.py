# encoding: utf-8
# module GH_IO.Types calls itself Types
# from GH_IO, Version=1.0.0.0, Culture=neutral, PublicKeyToken=6a29997d2e6b4f97
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_BoundingBox(object):
    """
    Represents a 3D bounding box, denoted by two points.
    
    GH_BoundingBox(nMin: GH_Point3D, nMax: GH_Point3D)
    GH_BoundingBox(Minx: float, Miny: float, Minz: float, Maxx: float, Maxy: float, Maxz: float)
    """
    def ToString(self):
        """
        ToString(self: GH_BoundingBox) -> str
        
            Converts this structure to a human-readable string.
            Returns: A string representation of the box structure.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[GH_BoundingBox]() -> GH_BoundingBox
        
        __new__(cls: type, nMin: GH_Point3D, nMax: GH_Point3D)
        __new__(cls: type, Minx: float, Miny: float, Minz: float, Maxx: float, Maxy: float, Maxz: float)
        """
        pass

    Max = None
    Min = None


class GH_Interval1D(object):
    """
    Represents two double precision floating point values.
    
    GH_Interval1D(na: float, nb: float)
    """
    def ToString(self):
        """
        ToString(self: GH_Interval1D) -> str
        
            Converts this structure to a human-readable string.
            Returns: A string representation of the Interval structure.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, na, nb):
        """
        __new__[GH_Interval1D]() -> GH_Interval1D
        
        __new__(cls: type, na: float, nb: float)
        """
        pass

    a = None
    b = None


class GH_Interval2D(object):
    """
    Represents two double precision domains.
    
    GH_Interval2D(nu: GH_Interval1D, nv: GH_Interval1D)
    GH_Interval2D(nu0: float, nu1: float, nv0: float, nv1: float)
    """
    def ToString(self):
        """
        ToString(self: GH_Interval2D) -> str
        
            Converts this structure to a human-readable string.
            Returns: A string representation of the two-dimensional Interval structure.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[GH_Interval2D]() -> GH_Interval2D
        
        __new__(cls: type, nu: GH_Interval1D, nv: GH_Interval1D)
        __new__(cls: type, nu0: float, nu1: float, nv0: float, nv1: float)
        """
        pass

    u = None
    v = None


class GH_Item(object, GH_IBinarySupport, GH_IXmlSupport):
    """
    Represents a single data item in a chunk.
    
    GH_Item(item_name: str, item_data: bool)
    GH_Item(item_name: str, item_index: int, item_data: bool)
    GH_Item(item_name: str, item_data: Byte)
    GH_Item(item_name: str, item_index: int, item_data: Byte)
    GH_Item(item_name: str, item_data: int)
    GH_Item(item_name: str, item_index: int, item_data: int)
    GH_Item(item_name: str, item_data: Int64)
    GH_Item(item_name: str, item_index: int, item_data: Int64)
    GH_Item(item_name: str, item_data: Single)
    GH_Item(item_name: str, item_index: int, item_data: Single)
    GH_Item(item_name: str, item_data: float)
    GH_Item(item_name: str, item_index: int, item_data: float)
    GH_Item(item_name: str, item_data: Decimal)
    GH_Item(item_name: str, item_index: int, item_data: Decimal)
    GH_Item(item_name: str, item_data: DateTime)
    GH_Item(item_name: str, item_index: int, item_data: DateTime)
    GH_Item(item_name: str, item_data: Guid)
    GH_Item(item_name: str, item_index: int, item_data: Guid)
    GH_Item(item_name: str, item_data: str)
    GH_Item(item_name: str, item_index: int, item_data: str)
    GH_Item(item_name: str, item_data: Array[Byte])
    GH_Item(item_name: str, item_index: int, item_data: Array[Byte])
    GH_Item(item_name: str, item_data: Array[float])
    GH_Item(item_name: str, item_index: int, item_data: Array[float])
    GH_Item(item_name: str, item_data: Point)
    GH_Item(item_name: str, item_index: int, item_data: Point)
    GH_Item(item_name: str, item_data: PointF)
    GH_Item(item_name: str, item_index: int, item_data: PointF)
    GH_Item(item_name: str, item_data: Size)
    GH_Item(item_name: str, item_index: int, item_data: Size)
    GH_Item(item_name: str, item_data: SizeF)
    GH_Item(item_name: str, item_index: int, item_data: SizeF)
    GH_Item(item_name: str, item_data: Rectangle)
    GH_Item(item_name: str, item_index: int, item_data: Rectangle)
    GH_Item(item_name: str, item_data: RectangleF)
    GH_Item(item_name: str, item_index: int, item_data: RectangleF)
    GH_Item(item_name: str, item_data: Color)
    GH_Item(item_name: str, item_index: int, item_data: Color)
    GH_Item(item_name: str, item_data: Bitmap)
    GH_Item(item_name: str, item_index: int, item_data: Bitmap)
    GH_Item(item_name: str, item_data: GH_Point2D)
    GH_Item(item_name: str, item_index: int, item_data: GH_Point2D)
    GH_Item(item_name: str, item_data: GH_Point3D)
    GH_Item(item_name: str, item_index: int, item_data: GH_Point3D)
    GH_Item(item_name: str, item_data: GH_Point4D)
    GH_Item(item_name: str, item_index: int, item_data: GH_Point4D)
    GH_Item(item_name: str, item_data: GH_Interval1D)
    GH_Item(item_name: str, item_index: int, item_data: GH_Interval1D)
    GH_Item(item_name: str, item_data: GH_Interval2D)
    GH_Item(item_name: str, item_index: int, item_data: GH_Interval2D)
    GH_Item(item_name: str, item_data: GH_Line)
    GH_Item(item_name: str, item_index: int, item_data: GH_Line)
    GH_Item(item_name: str, item_data: GH_BoundingBox)
    GH_Item(item_name: str, item_index: int, item_data: GH_BoundingBox)
    GH_Item(item_name: str, item_data: GH_Plane)
    GH_Item(item_name: str, item_index: int, item_data: GH_Plane)
    GH_Item(item_name: str, item_data: GH_Version)
    GH_Item(item_name: str, item_index: int, item_data: GH_Version)
    """
    @staticmethod
    def CreateFrom(*__args):
        """
        CreateFrom(node: XmlNode) -> GH_Item
        
            Creates a new instance of GH_Item and sets the fields from an Xml node object.
        
            node: Xml node object that defines the field data.
            Returns: The constructed and read item.
        CreateFrom(reader: BinaryReader) -> GH_Item
        
            Creates a new instance of GH_Item and sets the fields from a reader object.
        
            reader: Reader object that defines the field data.
            Returns: The constructed and read item.
        """
        pass

    def Read(self, *__args):
        """
        Read(self: GH_Item, node: XmlNode)
            Deserialize this item from an Xml node.
        
            node: Xml node to serialize from.
        Read(self: GH_Item, reader: BinaryReader)
            Deserialize this item from a binary stream.
        
            reader: Reader to deserialize with.
        """
        pass

    def ToString(self):
        """
        ToString(self: GH_Item) -> str
        
            Converts the struct into a human readable format.
        """
        pass

    def Write(self, writer):
        """
        Write(self: GH_Item, writer: XmlWriter)
            Serialize this item into an Xml stream.
        
            writer: Writer to serialize with.
        Write(self: GH_Item, writer: BinaryWriter)
            Serialize this item into a binary stream.
        
            writer: Writer to serialize with.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, item_name, *__args):
        """
        __new__(cls: type, item_name: str, item_data: bool)
        __new__(cls: type, item_name: str, item_index: int, item_data: bool)
        __new__(cls: type, item_name: str, item_data: Byte)
        __new__(cls: type, item_name: str, item_index: int, item_data: Byte)
        __new__(cls: type, item_name: str, item_data: int)
        __new__(cls: type, item_name: str, item_index: int, item_data: int)
        __new__(cls: type, item_name: str, item_data: Int64)
        __new__(cls: type, item_name: str, item_index: int, item_data: Int64)
        __new__(cls: type, item_name: str, item_data: Single)
        __new__(cls: type, item_name: str, item_index: int, item_data: Single)
        __new__(cls: type, item_name: str, item_data: float)
        __new__(cls: type, item_name: str, item_index: int, item_data: float)
        __new__(cls: type, item_name: str, item_data: Decimal)
        __new__(cls: type, item_name: str, item_index: int, item_data: Decimal)
        __new__(cls: type, item_name: str, item_data: DateTime)
        __new__(cls: type, item_name: str, item_index: int, item_data: DateTime)
        __new__(cls: type, item_name: str, item_data: Guid)
        __new__(cls: type, item_name: str, item_index: int, item_data: Guid)
        __new__(cls: type, item_name: str, item_data: str)
        __new__(cls: type, item_name: str, item_index: int, item_data: str)
        __new__(cls: type, item_name: str, item_data: Array[Byte])
        __new__(cls: type, item_name: str, item_index: int, item_data: Array[Byte])
        __new__(cls: type, item_name: str, item_data: Array[float])
        __new__(cls: type, item_name: str, item_index: int, item_data: Array[float])
        __new__(cls: type, item_name: str, item_data: Point)
        __new__(cls: type, item_name: str, item_index: int, item_data: Point)
        __new__(cls: type, item_name: str, item_data: PointF)
        __new__(cls: type, item_name: str, item_index: int, item_data: PointF)
        __new__(cls: type, item_name: str, item_data: Size)
        __new__(cls: type, item_name: str, item_index: int, item_data: Size)
        __new__(cls: type, item_name: str, item_data: SizeF)
        __new__(cls: type, item_name: str, item_index: int, item_data: SizeF)
        __new__(cls: type, item_name: str, item_data: Rectangle)
        __new__(cls: type, item_name: str, item_index: int, item_data: Rectangle)
        __new__(cls: type, item_name: str, item_data: RectangleF)
        __new__(cls: type, item_name: str, item_index: int, item_data: RectangleF)
        __new__(cls: type, item_name: str, item_data: Color)
        __new__(cls: type, item_name: str, item_index: int, item_data: Color)
        __new__(cls: type, item_name: str, item_data: Bitmap)
        __new__(cls: type, item_name: str, item_index: int, item_data: Bitmap)
        __new__(cls: type, item_name: str, item_data: GH_Point2D)
        __new__(cls: type, item_name: str, item_index: int, item_data: GH_Point2D)
        __new__(cls: type, item_name: str, item_data: GH_Point3D)
        __new__(cls: type, item_name: str, item_index: int, item_data: GH_Point3D)
        __new__(cls: type, item_name: str, item_data: GH_Point4D)
        __new__(cls: type, item_name: str, item_index: int, item_data: GH_Point4D)
        __new__(cls: type, item_name: str, item_data: GH_Interval1D)
        __new__(cls: type, item_name: str, item_index: int, item_data: GH_Interval1D)
        __new__(cls: type, item_name: str, item_data: GH_Interval2D)
        __new__(cls: type, item_name: str, item_index: int, item_data: GH_Interval2D)
        __new__(cls: type, item_name: str, item_data: GH_Line)
        __new__(cls: type, item_name: str, item_index: int, item_data: GH_Line)
        __new__(cls: type, item_name: str, item_data: GH_BoundingBox)
        __new__(cls: type, item_name: str, item_index: int, item_data: GH_BoundingBox)
        __new__(cls: type, item_name: str, item_data: GH_Plane)
        __new__(cls: type, item_name: str, item_index: int, item_data: GH_Plane)
        __new__(cls: type, item_name: str, item_data: GH_Version)
        __new__(cls: type, item_name: str, item_index: int, item_data: GH_Version)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DebuggerDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Readonly property used during Debugging.

Get: DebuggerDisplay(self: GH_Item) -> str

"""

    HasIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index existence implication. The item is considered to have an index qualifier 
            if the index value is larger than or equal to zero.

Get: HasIndex(self: GH_Item) -> bool

"""

    HasName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name validity of this item. 
            The item is considered to have an invalid name if string.IsNullOrEmpty(name)

Get: HasName(self: GH_Item) -> bool

"""

    HasType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type set validity of this item. 
            The item is considered to have a type if type != GH_Types.unset

Get: HasType(self: GH_Item) -> bool

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the index of an item. 
            Typically, indices are set at construction and do not change. 
            If you change indices after construction, you could corrupt an archive.

Get: Index(self: GH_Item) -> int

Set: Index(self: GH_Item) = value
"""

    InternalData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the internal data of this item. 
            No type casting is performed.

Get: InternalData(self: GH_Item) -> object

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of this item. 
            Typically, names are set at construction and do not change. 
            If you change names after construction, you could corrupt an archive.

Get: Name(self: GH_Item) -> str

Set: Name(self: GH_Item) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of this item. 
            Type flags are set during construction and cannot be altered.

Get: Type(self: GH_Item) -> GH_Types

"""

    _bool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Boolean.
            If the data is not stored as a Boolean, a conversion exception might be thrown.

Get: _bool(self: GH_Item) -> bool

"""

    _boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a BoundingBox.
            If the data is not stored as a BoundingBox, a conversion exception might be thrown.

Get: _boundingbox(self: GH_Item) -> GH_BoundingBox

"""

    _byte = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Byte.
            If the data is not stored as a Byte, a conversion exception might be thrown.

Get: _byte(self: GH_Item) -> Byte

"""

    _bytearray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Byte array.
            If the data is not stored as a Byte array, a conversion exception might be thrown.

Get: _bytearray(self: GH_Item) -> Array[Byte]

"""

    _date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a DateTime.
            If the data is not stored as a DateTime, a conversion exception might be thrown.

Get: _date(self: GH_Item) -> DateTime

"""

    _decimal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Decimal.
            If the data is not stored as a Decimal, a conversion exception might be thrown.

Get: _decimal(self: GH_Item) -> Decimal

"""

    _double = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Double.
            If the data is not stored as a Double, a conversion exception might be thrown.

Get: _double(self: GH_Item) -> float

"""

    _doublearray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Byte array.
            If the data is not stored as a Byte array, a conversion exception might be thrown.

Get: _doublearray(self: GH_Item) -> Array[float]

"""

    _drawing_bitmap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Bitmap.
            If the data is not stored as a Bitmap, a conversion exception might be thrown.

Get: _drawing_bitmap(self: GH_Item) -> Bitmap

"""

    _drawing_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Color.
            If the data is not stored as a Color, a conversion exception might be thrown.

Get: _drawing_color(self: GH_Item) -> Color

"""

    _drawing_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Point.
            If the data is not stored as a Point, a conversion exception might be thrown.

Get: _drawing_point(self: GH_Item) -> Point

"""

    _drawing_pointf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a PointF.
            If the data is not stored as a PointF, a conversion exception might be thrown.

Get: _drawing_pointf(self: GH_Item) -> PointF

"""

    _drawing_rectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Rectangle.
            If the data is not stored as a Rectangle, a conversion exception might be thrown.

Get: _drawing_rectangle(self: GH_Item) -> Rectangle

"""

    _drawing_rectanglef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a RectangleF.
            If the data is not stored as a RectangleF, a conversion exception might be thrown.

Get: _drawing_rectanglef(self: GH_Item) -> RectangleF

"""

    _drawing_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Size.
            If the data is not stored as a Size, a conversion exception might be thrown.

Get: _drawing_size(self: GH_Item) -> Size

"""

    _drawing_sizef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a SizeF.
            If the data is not stored as a SizeF, a conversion exception might be thrown.

Get: _drawing_sizef(self: GH_Item) -> SizeF

"""

    _guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Guid.
            If the data is not stored as a Guid, a conversion exception might be thrown.

Get: _guid(self: GH_Item) -> Guid

"""

    _int32 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to an Int32.
            If the data is not stored as an Int32, a conversion exception might be thrown.

Get: _int32(self: GH_Item) -> int

"""

    _int64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to an Int64.
            If the data is not stored as an Int64, a conversion exception might be thrown.

Get: _int64(self: GH_Item) -> Int64

"""

    _interval1d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to an Interval1D.
            If the data is not stored as an Interval1D, a conversion exception might be thrown.

Get: _interval1d(self: GH_Item) -> GH_Interval1D

"""

    _interval2d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to an Interval2D.
            If the data is not stored as an Interval2D, a conversion exception might be thrown.

Get: _interval2d(self: GH_Item) -> GH_Interval2D

"""

    _line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Line.
            If the data is not stored as a Line, a conversion exception might be thrown.

Get: _line(self: GH_Item) -> GH_Line

"""

    _plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Plane.
            If the data is not stored as a Plane, a conversion exception might be thrown.

Get: _plane(self: GH_Item) -> GH_Plane

"""

    _point2d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Point2D.
            If the data is not stored as a Point2D, a conversion exception might be thrown.

Get: _point2d(self: GH_Item) -> GH_Point2D

"""

    _point3d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Point3D.
            If the data is not stored as a Point3D, a conversion exception might be thrown.

Get: _point3d(self: GH_Item) -> GH_Point3D

"""

    _point4d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Point4D.
            If the data is not stored as a Point4D, a conversion exception might be thrown.

Get: _point4d(self: GH_Item) -> GH_Point4D

"""

    _single = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Single.
            If the data is not stored as a Single, a conversion exception might be thrown.

Get: _single(self: GH_Item) -> Single

"""

    _string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a String.
            If the data is not stored as a String, a conversion exception might be thrown.

Get: _string(self: GH_Item) -> str

"""

    _version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the internal data of this item cast to a Version.
            If the data is not stored as a Version, a conversion exception might be thrown.

Get: _version(self: GH_Item) -> GH_Version

"""



class GH_Line(object):
    """
    Represents a 3D line segment, denoted by start and endpoints.
    
    GH_Line(nA: GH_Point3D, nB: GH_Point3D)
    GH_Line(Ax: float, Ay: float, Az: float, Bx: float, By: float, Bz: float)
    """
    def ToString(self):
        """
        ToString(self: GH_Line) -> str
        
            Converts this structure to a human-readable string.
            Returns: A string representation of the line structure.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[GH_Line]() -> GH_Line
        
        __new__(cls: type, nA: GH_Point3D, nB: GH_Point3D)
        __new__(cls: type, Ax: float, Ay: float, Az: float, Bx: float, By: float, Bz: float)
        """
        pass

    A = None
    B = None


class GH_Plane(object):
    """
    Represents a 3D plane system, defined by origin point and {X,Y} axis directions.
    
    GH_Plane(nOrigin: GH_Point3D, nXAxis: GH_Point3D, nYAxis: GH_Point3D)
    GH_Plane(Ox: float, Oy: float, Oz: float, Xx: float, Xy: float, Xz: float, Yx: float, Yy: float, Yz: float)
    """
    def ToString(self):
        """
        ToString(self: GH_Plane) -> str
        
            Converts this structure to a human-readable string.
            Returns: A string representation of the plane structure.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[GH_Plane]() -> GH_Plane
        
        __new__(cls: type, nOrigin: GH_Point3D, nXAxis: GH_Point3D, nYAxis: GH_Point3D)
        __new__(cls: type, Ox: float, Oy: float, Oz: float, Xx: float, Xy: float, Xz: float, Yx: float, Yy: float, Yz: float)
        """
        pass

    Origin = None
    XAxis = None
    YAxis = None


class GH_Point2D(object):
    """
    Represents a 2D point coordinate with double precision floating point components.
    
    GH_Point2D(nx: float, ny: float)
    """
    def ToString(self):
        """
        ToString(self: GH_Point2D) -> str
        
            Converts this structure to a human-readable string.
            Returns: A string representation of the two-dimenionsional point structure.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, nx, ny):
        """
        __new__[GH_Point2D]() -> GH_Point2D
        
        __new__(cls: type, nx: float, ny: float)
        """
        pass

    x = None
    y = None


class GH_Point3D(object):
    """
    Represents a 3D point coordinate with double precision floating point components.
    
    GH_Point3D(nx: float, ny: float, nz: float)
    """
    def ToString(self):
        """
        ToString(self: GH_Point3D) -> str
        
            Converts this structure to a human-readable string.
            Returns: A string representation of the three-dimenionsional point structure.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, nx, ny, nz):
        """
        __new__[GH_Point3D]() -> GH_Point3D
        
        __new__(cls: type, nx: float, ny: float, nz: float)
        """
        pass

    x = None
    y = None
    z = None


class GH_Point4D(object):
    """
    Represents a 4D point coordinate with double precision floating point components.
    
    GH_Point4D(nx: float, ny: float, nz: float, nw: float)
    """
    def ToString(self):
        """
        ToString(self: GH_Point4D) -> str
        
            Converts this structure to a human-readable string.
            Returns: A string representation of the four-dimenionsional point structure.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, nx, ny, nz, nw):
        """
        __new__[GH_Point4D]() -> GH_Point4D
        
        __new__(cls: type, nx: float, ny: float, nz: float, nw: float)
        """
        pass

    w = None
    x = None
    y = None
    z = None


class GH_Types(Enum, IComparable, IFormattable, IConvertible):
    """
    Contains flags for all data types currently supported by GH_IO.dll
    
    enum GH_Types, values: gh_bool (1), gh_boundingbox (71), gh_byte (2), gh_bytearray (20), gh_date (8), gh_decimal (7), gh_double (6), gh_doublearray (21), gh_drawing_bitmap (37), gh_drawing_color (36), gh_drawing_point (30), gh_drawing_pointf (31), gh_drawing_rectangle (34), gh_drawing_rectanglef (35), gh_drawing_size (32), gh_drawing_sizef (33), gh_guid (9), gh_int32 (3), gh_int64 (4), gh_interval1d (60), gh_interval2d (61), gh_line (70), gh_plane (72), gh_point2d (50), gh_point3d (51), gh_point4d (52), gh_single (5), gh_string (10), gh_version (80), unset (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    gh_bool = None
    gh_boundingbox = None
    gh_byte = None
    gh_bytearray = None
    gh_date = None
    gh_decimal = None
    gh_double = None
    gh_doublearray = None
    gh_drawing_bitmap = None
    gh_drawing_color = None
    gh_drawing_point = None
    gh_drawing_pointf = None
    gh_drawing_rectangle = None
    gh_drawing_rectanglef = None
    gh_drawing_size = None
    gh_drawing_sizef = None
    gh_guid = None
    gh_int32 = None
    gh_int64 = None
    gh_interval1d = None
    gh_interval2d = None
    gh_line = None
    gh_plane = None
    gh_point2d = None
    gh_point3d = None
    gh_point4d = None
    gh_single = None
    gh_string = None
    gh_version = None
    unset = None
    value__ = None


class GH_Version(object):
    """
    Basic version type. Contains Major, Minor and Revision fields.
    
    GH_Version(v_major: int, v_minor: int, v_revision: int)
    GH_Version(other: GH_Version)
    """
    def Equals(self, obj):
        """
        Equals(self: GH_Version, obj: object) -> bool
        
            Performs value equality comparison.
        
            obj: Object to compare with. 
                    If obj is a null reference or not a GH_Version instance, 
             false is returned.
        
            Returns: True if obj is a GH_Version instance which is equal to this one.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: GH_Version) -> int
        
            Returns the hash code for this instance.
            Returns: A hash code for the current version object.
        """
        pass

    def ToString(self):
        """
        ToString(self: GH_Version) -> str
        
            Default formatter for Version data: M.m.RRRR 
                    Revision section is padded with 
             zeroes until it is at least 4 digits long.
        
            Returns: A string represtation of the Version structure.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[GH_Version]() -> GH_Version
        
        __new__(cls: type, v_major: int, v_minor: int, v_revision: int)
        __new__(cls: type, other: GH_Version)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    major = None
    minor = None
    revision = None


