# encoding: utf-8
# module Rhino.FileIO calls itself FileIO
# from Rhino3dmIO, Version=5.1.30000.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BinaryArchiveException(IOException, ISerializable, _Exception):
    """ BinaryArchiveException(message: str) """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message):
        """ __new__(cls: type, message: str) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class BinaryArchiveFile(object, IDisposable):
    """ BinaryArchiveFile(filename: str, mode: BinaryArchiveMode) """
    def Close(self):
        """ Close(self: BinaryArchiveFile) """
        pass

    def Dispose(self):
        """ Dispose(self: BinaryArchiveFile) """
        pass

    def Open(self):
        """ Open(self: BinaryArchiveFile) -> bool """
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
    def __new__(self, filename, mode):
        """ __new__(cls: type, filename: str, mode: BinaryArchiveMode) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Reader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reader(self: BinaryArchiveFile) -> BinaryArchiveReader

"""

    Writer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Writer(self: BinaryArchiveFile) -> BinaryArchiveWriter

"""



class BinaryArchiveMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum BinaryArchiveMode, values: Read (1), Read3dm (5), ReadWrite (3), Unknown (0), Write (2), Write3dm (6) """
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

    Read = None
    Read3dm = None
    ReadWrite = None
    Unknown = None
    value__ = None
    Write = None
    Write3dm = None


class BinaryArchiveReader(object):
    # no doc
    def AtEnd(self):
        """ AtEnd(self: BinaryArchiveReader) -> bool """
        pass

    def Dump3dmChunk(self, log):
        """ Dump3dmChunk(self: BinaryArchiveReader, log: TextLog) -> UInt32 """
        pass

    def Read3dmChunkVersion(self, major, minor):
        """ Read3dmChunkVersion(self: BinaryArchiveReader) -> (int, int) """
        pass

    def Read3dmStartSection(self, version, comment):
        """ Read3dmStartSection(self: BinaryArchiveReader) -> (bool, int, str) """
        pass

    def ReadBool(self):
        """ ReadBool(self: BinaryArchiveReader) -> bool """
        pass

    def ReadBoolArray(self):
        """ ReadBoolArray(self: BinaryArchiveReader) -> Array[bool] """
        pass

    def ReadBoundingBox(self):
        """ ReadBoundingBox(self: BinaryArchiveReader) -> BoundingBox """
        pass

    def ReadByte(self):
        """ ReadByte(self: BinaryArchiveReader) -> Byte """
        pass

    def ReadByteArray(self):
        """ ReadByteArray(self: BinaryArchiveReader) -> Array[Byte] """
        pass

    def ReadColor(self):
        """ ReadColor(self: BinaryArchiveReader) -> Color """
        pass

    def ReadCompressedBuffer(self):
        """ ReadCompressedBuffer(self: BinaryArchiveReader) -> Array[Byte] """
        pass

    def ReadDictionary(self):
        """ ReadDictionary(self: BinaryArchiveReader) -> ArchivableDictionary """
        pass

    def ReadDouble(self):
        """ ReadDouble(self: BinaryArchiveReader) -> float """
        pass

    def ReadDoubleArray(self):
        """ ReadDoubleArray(self: BinaryArchiveReader) -> Array[float] """
        pass

    def ReadFont(self):
        """ ReadFont(self: BinaryArchiveReader) -> Font """
        pass

    def ReadGeometry(self):
        """ ReadGeometry(self: BinaryArchiveReader) -> GeometryBase """
        pass

    def ReadGuid(self):
        """ ReadGuid(self: BinaryArchiveReader) -> Guid """
        pass

    def ReadGuidArray(self):
        """ ReadGuidArray(self: BinaryArchiveReader) -> Array[Guid] """
        pass

    def ReadInt(self):
        """ ReadInt(self: BinaryArchiveReader) -> int """
        pass

    def ReadInt64(self):
        """ ReadInt64(self: BinaryArchiveReader) -> Int64 """
        pass

    def ReadIntArray(self):
        """ ReadIntArray(self: BinaryArchiveReader) -> Array[int] """
        pass

    def ReadInterval(self):
        """ ReadInterval(self: BinaryArchiveReader) -> Interval """
        pass

    def ReadLine(self):
        """ ReadLine(self: BinaryArchiveReader) -> Line """
        pass

    def ReadMeshingParameters(self):
        """ ReadMeshingParameters(self: BinaryArchiveReader) -> MeshingParameters """
        pass

    def ReadPlane(self):
        """ ReadPlane(self: BinaryArchiveReader) -> Plane """
        pass

    def ReadPoint(self):
        """ ReadPoint(self: BinaryArchiveReader) -> Point """
        pass

    def ReadPoint2d(self):
        """ ReadPoint2d(self: BinaryArchiveReader) -> Point2d """
        pass

    def ReadPoint3d(self):
        """ ReadPoint3d(self: BinaryArchiveReader) -> Point3d """
        pass

    def ReadPoint3f(self):
        """ ReadPoint3f(self: BinaryArchiveReader) -> Point3f """
        pass

    def ReadPoint4d(self):
        """ ReadPoint4d(self: BinaryArchiveReader) -> Point4d """
        pass

    def ReadPointF(self):
        """ ReadPointF(self: BinaryArchiveReader) -> PointF """
        pass

    def ReadRay3d(self):
        """ ReadRay3d(self: BinaryArchiveReader) -> Ray3d """
        pass

    def ReadRectangle(self):
        """ ReadRectangle(self: BinaryArchiveReader) -> Rectangle """
        pass

    def ReadRectangleF(self):
        """ ReadRectangleF(self: BinaryArchiveReader) -> RectangleF """
        pass

    def ReadSByte(self):
        """ ReadSByte(self: BinaryArchiveReader) -> SByte """
        pass

    def ReadSByteArray(self):
        """ ReadSByteArray(self: BinaryArchiveReader) -> Array[SByte] """
        pass

    def ReadShort(self):
        """ ReadShort(self: BinaryArchiveReader) -> Int16 """
        pass

    def ReadShortArray(self):
        """ ReadShortArray(self: BinaryArchiveReader) -> Array[Int16] """
        pass

    def ReadSingle(self):
        """ ReadSingle(self: BinaryArchiveReader) -> Single """
        pass

    def ReadSingleArray(self):
        """ ReadSingleArray(self: BinaryArchiveReader) -> Array[Single] """
        pass

    def ReadSize(self):
        """ ReadSize(self: BinaryArchiveReader) -> Size """
        pass

    def ReadSizeF(self):
        """ ReadSizeF(self: BinaryArchiveReader) -> SizeF """
        pass

    def ReadString(self):
        """ ReadString(self: BinaryArchiveReader) -> str """
        pass

    def ReadStringArray(self):
        """ ReadStringArray(self: BinaryArchiveReader) -> Array[str] """
        pass

    def ReadTransform(self):
        """ ReadTransform(self: BinaryArchiveReader) -> Transform """
        pass

    def ReadUInt(self):
        """ ReadUInt(self: BinaryArchiveReader) -> UInt32 """
        pass

    def ReadUShort(self):
        """ ReadUShort(self: BinaryArchiveReader) -> UInt16 """
        pass

    def ReadVector2d(self):
        """ ReadVector2d(self: BinaryArchiveReader) -> Vector2d """
        pass

    def ReadVector3d(self):
        """ ReadVector3d(self: BinaryArchiveReader) -> Vector3d """
        pass

    def ReadVector3f(self):
        """ ReadVector3f(self: BinaryArchiveReader) -> Vector3f """
        pass

    Archive3dmVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Archive3dmVersion(self: BinaryArchiveReader) -> int

"""

    ReadErrorOccured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadErrorOccured(self: BinaryArchiveReader) -> bool

Set: ReadErrorOccured(self: BinaryArchiveReader) = value
"""



class BinaryArchiveWriter(object):
    # no doc
    def Write3dmChunkVersion(self, major, minor):
        """ Write3dmChunkVersion(self: BinaryArchiveWriter, major: int, minor: int) """
        pass

    def WriteBool(self, value):
        """ WriteBool(self: BinaryArchiveWriter, value: bool) """
        pass

    def WriteBoolArray(self, value):
        """ WriteBoolArray(self: BinaryArchiveWriter, value: IEnumerable[bool]) """
        pass

    def WriteBoundingBox(self, value):
        """ WriteBoundingBox(self: BinaryArchiveWriter, value: BoundingBox) """
        pass

    def WriteByte(self, value):
        """ WriteByte(self: BinaryArchiveWriter, value: Byte) """
        pass

    def WriteByteArray(self, value):
        """ WriteByteArray(self: BinaryArchiveWriter, value: IEnumerable[Byte]) """
        pass

    def WriteColor(self, value):
        """ WriteColor(self: BinaryArchiveWriter, value: Color) """
        pass

    def WriteCompressedBuffer(self, value):
        """ WriteCompressedBuffer(self: BinaryArchiveWriter, value: IEnumerable[Byte]) """
        pass

    def WriteDictionary(self, dictionary):
        """ WriteDictionary(self: BinaryArchiveWriter, dictionary: ArchivableDictionary) """
        pass

    def WriteDouble(self, value):
        """ WriteDouble(self: BinaryArchiveWriter, value: float) """
        pass

    def WriteDoubleArray(self, value):
        """ WriteDoubleArray(self: BinaryArchiveWriter, value: IEnumerable[float]) """
        pass

    def WriteFont(self, value):
        """ WriteFont(self: BinaryArchiveWriter, value: Font) """
        pass

    def WriteGeometry(self, value):
        """ WriteGeometry(self: BinaryArchiveWriter, value: GeometryBase) """
        pass

    def WriteGuid(self, value):
        """ WriteGuid(self: BinaryArchiveWriter, value: Guid) """
        pass

    def WriteGuidArray(self, value):
        """ WriteGuidArray(self: BinaryArchiveWriter, value: IEnumerable[Guid]) """
        pass

    def WriteInt(self, value):
        """ WriteInt(self: BinaryArchiveWriter, value: int) """
        pass

    def WriteInt64(self, value):
        """ WriteInt64(self: BinaryArchiveWriter, value: Int64) """
        pass

    def WriteIntArray(self, value):
        """ WriteIntArray(self: BinaryArchiveWriter, value: IEnumerable[int]) """
        pass

    def WriteInterval(self, value):
        """ WriteInterval(self: BinaryArchiveWriter, value: Interval) """
        pass

    def WriteLine(self, value):
        """ WriteLine(self: BinaryArchiveWriter, value: Line) """
        pass

    def WriteMeshingParameters(self, value):
        """ WriteMeshingParameters(self: BinaryArchiveWriter, value: MeshingParameters) """
        pass

    def WritePlane(self, value):
        """ WritePlane(self: BinaryArchiveWriter, value: Plane) """
        pass

    def WritePoint(self, value):
        """ WritePoint(self: BinaryArchiveWriter, value: Point) """
        pass

    def WritePoint2d(self, value):
        """ WritePoint2d(self: BinaryArchiveWriter, value: Point2d) """
        pass

    def WritePoint3d(self, value):
        """ WritePoint3d(self: BinaryArchiveWriter, value: Point3d) """
        pass

    def WritePoint3f(self, value):
        """ WritePoint3f(self: BinaryArchiveWriter, value: Point3f) """
        pass

    def WritePoint4d(self, value):
        """ WritePoint4d(self: BinaryArchiveWriter, value: Point4d) """
        pass

    def WritePointF(self, value):
        """ WritePointF(self: BinaryArchiveWriter, value: PointF) """
        pass

    def WriteRay3d(self, value):
        """ WriteRay3d(self: BinaryArchiveWriter, value: Ray3d) """
        pass

    def WriteRectangle(self, value):
        """ WriteRectangle(self: BinaryArchiveWriter, value: Rectangle) """
        pass

    def WriteRectangleF(self, value):
        """ WriteRectangleF(self: BinaryArchiveWriter, value: RectangleF) """
        pass

    def WriteSByte(self, value):
        """ WriteSByte(self: BinaryArchiveWriter, value: SByte) """
        pass

    def WriteSByteArray(self, value):
        """ WriteSByteArray(self: BinaryArchiveWriter, value: IEnumerable[SByte]) """
        pass

    def WriteShort(self, value):
        """ WriteShort(self: BinaryArchiveWriter, value: Int16) """
        pass

    def WriteShortArray(self, value):
        """ WriteShortArray(self: BinaryArchiveWriter, value: IEnumerable[Int16]) """
        pass

    def WriteSingle(self, value):
        """ WriteSingle(self: BinaryArchiveWriter, value: Single) """
        pass

    def WriteSingleArray(self, value):
        """ WriteSingleArray(self: BinaryArchiveWriter, value: IEnumerable[Single]) """
        pass

    def WriteSize(self, value):
        """ WriteSize(self: BinaryArchiveWriter, value: Size) """
        pass

    def WriteSizeF(self, value):
        """ WriteSizeF(self: BinaryArchiveWriter, value: SizeF) """
        pass

    def WriteString(self, value):
        """ WriteString(self: BinaryArchiveWriter, value: str) """
        pass

    def WriteStringArray(self, value):
        """ WriteStringArray(self: BinaryArchiveWriter, value: IEnumerable[str]) """
        pass

    def WriteTransform(self, value):
        """ WriteTransform(self: BinaryArchiveWriter, value: Transform) """
        pass

    def WriteUInt(self, value):
        """ WriteUInt(self: BinaryArchiveWriter, value: UInt32) """
        pass

    def WriteUShort(self, value):
        """ WriteUShort(self: BinaryArchiveWriter, value: UInt16) """
        pass

    def WriteVector2d(self, value):
        """ WriteVector2d(self: BinaryArchiveWriter, value: Vector2d) """
        pass

    def WriteVector3d(self, value):
        """ WriteVector3d(self: BinaryArchiveWriter, value: Vector3d) """
        pass

    def WriteVector3f(self, value):
        """ WriteVector3f(self: BinaryArchiveWriter, value: Vector3f) """
        pass

    Archive3dmVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Archive3dmVersion(self: BinaryArchiveWriter) -> int

"""

    WriteErrorOccured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WriteErrorOccured(self: BinaryArchiveWriter) -> bool

Set: WriteErrorOccured(self: BinaryArchiveWriter) = value
"""



class File3dm(object, IDisposable):
    """ File3dm() """
    def Audit(self, attemptRepair, repairCount, errors, warnings):
        """ Audit(self: File3dm, attemptRepair: bool) -> (int, int, str, Array[int]) """
        pass

    def Dispose(self):
        """ Dispose(self: File3dm) """
        pass

    def Dump(self):
        """ Dump(self: File3dm) -> str """
        pass

    def DumpSummary(self):
        """ DumpSummary(self: File3dm) -> str """
        pass

    def DumpToTextLog(self, log):
        """ DumpToTextLog(self: File3dm, log: TextLog) """
        pass

    def IsValid(self, errors):
        """
        IsValid(self: File3dm, errors: TextLog) -> bool
        IsValid(self: File3dm) -> (bool, str)
        """
        pass

    def Polish(self):
        """ Polish(self: File3dm) """
        pass

    @staticmethod
    def Read(path, tableTypeFilterFilter=None, objectTypeFilter=None, objectReadCallback=None):
        """
        Read(path: str, tableTypeFilterFilter: TableTypeFilter, objectTypeFilter: ObjectTypeFilter, objectReadCallback: Func[GeometryBase, ObjectAttributes, bool]) -> File3dm
        Read(path: str, tableTypeFilterFilter: TableTypeFilter, objectTypeFilter: ObjectTypeFilter) -> File3dm
        Read(path: str) -> File3dm
        """
        pass

    @staticmethod
    def ReadApplicationData(path, applicationName, applicationUrl, applicationDetails):
        """ ReadApplicationData(path: str) -> (str, str, str) """
        pass

    @staticmethod
    def ReadArchiveVersion(path):
        """ ReadArchiveVersion(path: str) -> int """
        pass

    @staticmethod
    def ReadNotes(path):
        """ ReadNotes(path: str) -> str """
        pass

    @staticmethod
    def ReadRevisionHistory(path, createdBy, lastEditedBy, revision, createdOn, lastEditedOn):
        """ ReadRevisionHistory(path: str) -> (bool, str, str, int, DateTime, DateTime) """
        pass

    @staticmethod
    def ReadWithLog(path, *__args):
        """
        ReadWithLog(path: str) -> (File3dm, str)
        ReadWithLog(path: str, tableTypeFilterFilter: TableTypeFilter, objectTypeFilter: ObjectTypeFilter) -> (File3dm, str)
        """
        pass

    def Write(self, path, *__args):
        """
        Write(self: File3dm, path: str, options: File3dmWriteOptions) -> bool
        Write(self: File3dm, path: str, version: int) -> bool
        """
        pass

    def WriteWithLog(self, path, version, errorLog):
        """ WriteWithLog(self: File3dm, path: str, version: int) -> (bool, str) """
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

    ApplicationDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationDetails(self: File3dm) -> str

Set: ApplicationDetails(self: File3dm) = value
"""

    ApplicationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationName(self: File3dm) -> str

Set: ApplicationName(self: File3dm) = value
"""

    ApplicationUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationUrl(self: File3dm) -> str

Set: ApplicationUrl(self: File3dm) = value
"""

    Created = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Created(self: File3dm) -> DateTime

"""

    CreatedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedBy(self: File3dm) -> str

"""

    DimStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimStyles(self: File3dm) -> IList[DimensionStyle]

"""

    HatchPatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchPatterns(self: File3dm) -> IList[HatchPattern]

"""

    HistoryRecords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HistoryRecords(self: File3dm) -> File3dmHistoryRecordTable

"""

    InstanceDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InstanceDefinitions(self: File3dm) -> IList[InstanceDefinitionGeometry]

"""

    LastEdited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastEdited(self: File3dm) -> DateTime

"""

    LastEditedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastEditedBy(self: File3dm) -> str

"""

    Layers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layers(self: File3dm) -> IList[Layer]

"""

    Linetypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linetypes(self: File3dm) -> IList[Linetype]

"""

    Materials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Materials(self: File3dm) -> IList[Material]

"""

    NamedViews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NamedViews(self: File3dm) -> IList[ViewInfo]

"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notes(self: File3dm) -> File3dmNotes

Set: Notes(self: File3dm) = value
"""

    Objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Objects(self: File3dm) -> File3dmObjectTable

"""

    PlugInData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlugInData(self: File3dm) -> File3dmPlugInDataTable

"""

    Revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Revision(self: File3dm) -> int

Set: Revision(self: File3dm) = value
"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settings(self: File3dm) -> File3dmSettings

"""

    StartSectionComments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartSectionComments(self: File3dm) -> str

Set: StartSectionComments(self: File3dm) = value
"""

    Views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Views(self: File3dm) -> IList[ViewInfo]

"""


    ObjectTypeFilter = None
    TableTypeFilter = None


class File3dmHistoryRecordTable(object):
    # no doc
    def Clear(self):
        """ Clear(self: File3dmHistoryRecordTable) """
        pass

    def Dump(self):
        """ Dump(self: File3dmHistoryRecordTable) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: File3dmHistoryRecordTable) -> int

"""



class File3dmNotes(object):
    """ File3dmNotes() """
    IsHtml = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHtml(self: File3dmNotes) -> bool

Set: IsHtml(self: File3dmNotes) = value
"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVisible(self: File3dmNotes) -> bool

Set: IsVisible(self: File3dmNotes) = value
"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notes(self: File3dmNotes) -> str

Set: Notes(self: File3dmNotes) = value
"""

    WindowRectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowRectangle(self: File3dmNotes) -> Rectangle

Set: WindowRectangle(self: File3dmNotes) = value
"""



class File3dmObject(object):
    # no doc
    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: File3dmObject) -> ObjectAttributes

"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: File3dmObject) -> GeometryBase

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: File3dmObject) -> str

Set: Name(self: File3dmObject) = value
"""



class File3dmObjectTable(object, IEnumerable[File3dmObject], IEnumerable, IRhinoTable[File3dmObject]):
    # no doc
    def AddArc(self, arc, attributes=None):
        """
        AddArc(self: File3dmObjectTable, arc: Arc, attributes: ObjectAttributes) -> Guid
        AddArc(self: File3dmObjectTable, arc: Arc) -> Guid
        """
        pass

    def AddBrep(self, brep, attributes=None):
        """
        AddBrep(self: File3dmObjectTable, brep: Brep, attributes: ObjectAttributes) -> Guid
        AddBrep(self: File3dmObjectTable, brep: Brep) -> Guid
        """
        pass

    def AddCircle(self, circle, attributes=None):
        """
        AddCircle(self: File3dmObjectTable, circle: Circle, attributes: ObjectAttributes) -> Guid
        AddCircle(self: File3dmObjectTable, circle: Circle) -> Guid
        """
        pass

    def AddClippingPlane(self, plane, uMagnitude, vMagnitude, *__args):
        """
        AddClippingPlane(self: File3dmObjectTable, plane: Plane, uMagnitude: float, vMagnitude: float, clippedViewportIds: IEnumerable[Guid], attributes: ObjectAttributes) -> Guid
        AddClippingPlane(self: File3dmObjectTable, plane: Plane, uMagnitude: float, vMagnitude: float, clippedViewportIds: IEnumerable[Guid]) -> Guid
        AddClippingPlane(self: File3dmObjectTable, plane: Plane, uMagnitude: float, vMagnitude: float, clippedViewportId: Guid) -> Guid
        """
        pass

    def AddCurve(self, curve, attributes=None):
        """
        AddCurve(self: File3dmObjectTable, curve: Curve, attributes: ObjectAttributes) -> Guid
        AddCurve(self: File3dmObjectTable, curve: Curve) -> Guid
        """
        pass

    def AddEllipse(self, ellipse, attributes=None):
        """
        AddEllipse(self: File3dmObjectTable, ellipse: Ellipse, attributes: ObjectAttributes) -> Guid
        AddEllipse(self: File3dmObjectTable, ellipse: Ellipse) -> Guid
        """
        pass

    def AddExtrusion(self, extrusion, attributes=None):
        """
        AddExtrusion(self: File3dmObjectTable, extrusion: Extrusion, attributes: ObjectAttributes) -> Guid
        AddExtrusion(self: File3dmObjectTable, extrusion: Extrusion) -> Guid
        """
        pass

    def AddHatch(self, hatch, attributes=None):
        """
        AddHatch(self: File3dmObjectTable, hatch: Hatch, attributes: ObjectAttributes) -> Guid
        AddHatch(self: File3dmObjectTable, hatch: Hatch) -> Guid
        """
        pass

    def AddLeader(self, *__args):
        """
        AddLeader(self: File3dmObjectTable, text: str, plane: Plane, points: IEnumerable[Point2d], attributes: ObjectAttributes) -> Guid
        AddLeader(self: File3dmObjectTable, text: str, plane: Plane, points: IEnumerable[Point2d]) -> Guid
        AddLeader(self: File3dmObjectTable, plane: Plane, points: IEnumerable[Point2d]) -> Guid
        AddLeader(self: File3dmObjectTable, plane: Plane, points: IEnumerable[Point2d], attributes: ObjectAttributes) -> Guid
        """
        pass

    def AddLine(self, *__args):
        """
        AddLine(self: File3dmObjectTable, line: Line) -> Guid
        AddLine(self: File3dmObjectTable, line: Line, attributes: ObjectAttributes) -> Guid
        AddLine(self: File3dmObjectTable, from: Point3d, to: Point3d) -> Guid
        AddLine(self: File3dmObjectTable, from: Point3d, to: Point3d, attributes: ObjectAttributes) -> Guid
        """
        pass

    def AddLinearDimension(self, dimension, attributes=None):
        """
        AddLinearDimension(self: File3dmObjectTable, dimension: LinearDimension, attributes: ObjectAttributes) -> Guid
        AddLinearDimension(self: File3dmObjectTable, dimension: LinearDimension) -> Guid
        """
        pass

    def AddMesh(self, mesh, attributes=None):
        """
        AddMesh(self: File3dmObjectTable, mesh: Mesh, attributes: ObjectAttributes) -> Guid
        AddMesh(self: File3dmObjectTable, mesh: Mesh) -> Guid
        """
        pass

    def AddPoint(self, *__args):
        """
        AddPoint(self: File3dmObjectTable, point: Point3f) -> Guid
        AddPoint(self: File3dmObjectTable, point: Point3f, attributes: ObjectAttributes) -> Guid
        AddPoint(self: File3dmObjectTable, point: Point3d, attributes: ObjectAttributes) -> Guid
        AddPoint(self: File3dmObjectTable, x: float, y: float, z: float) -> Guid
        AddPoint(self: File3dmObjectTable, point: Point3d) -> Guid
        """
        pass

    def AddPointCloud(self, *__args):
        """
        AddPointCloud(self: File3dmObjectTable, points: IEnumerable[Point3d]) -> Guid
        AddPointCloud(self: File3dmObjectTable, points: IEnumerable[Point3d], attributes: ObjectAttributes) -> Guid
        AddPointCloud(self: File3dmObjectTable, cloud: PointCloud) -> Guid
        AddPointCloud(self: File3dmObjectTable, cloud: PointCloud, attributes: ObjectAttributes) -> Guid
        """
        pass

    def AddPoints(self, points, attributes=None):
        """
        AddPoints(self: File3dmObjectTable, points: IEnumerable[Point3f]) -> Array[Guid]
        AddPoints(self: File3dmObjectTable, points: IEnumerable[Point3f], attributes: ObjectAttributes) -> Array[Guid]
        AddPoints(self: File3dmObjectTable, points: IEnumerable[Point3d]) -> Array[Guid]
        AddPoints(self: File3dmObjectTable, points: IEnumerable[Point3d], attributes: ObjectAttributes) -> Array[Guid]
        """
        pass

    def AddPolyline(self, points, attributes=None):
        """
        AddPolyline(self: File3dmObjectTable, points: IEnumerable[Point3d], attributes: ObjectAttributes) -> Guid
        AddPolyline(self: File3dmObjectTable, points: IEnumerable[Point3d]) -> Guid
        """
        pass

    def AddSphere(self, sphere, attributes=None):
        """
        AddSphere(self: File3dmObjectTable, sphere: Sphere, attributes: ObjectAttributes) -> Guid
        AddSphere(self: File3dmObjectTable, sphere: Sphere) -> Guid
        """
        pass

    def AddSurface(self, surface, attributes=None):
        """
        AddSurface(self: File3dmObjectTable, surface: Surface, attributes: ObjectAttributes) -> Guid
        AddSurface(self: File3dmObjectTable, surface: Surface) -> Guid
        """
        pass

    def AddText(self, text, plane, height, fontName, bold, italic, *__args):
        """
        AddText(self: File3dmObjectTable, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool, justification: TextJustification, attributes: ObjectAttributes) -> Guid
        AddText(self: File3dmObjectTable, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool, attributes: ObjectAttributes) -> Guid
        AddText(self: File3dmObjectTable, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool) -> Guid
        AddText(self: File3dmObjectTable, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool, justification: TextJustification) -> Guid
        """
        pass

    def AddTextDot(self, *__args):
        """
        AddTextDot(self: File3dmObjectTable, dot: TextDot) -> Guid
        AddTextDot(self: File3dmObjectTable, dot: TextDot, attributes: ObjectAttributes) -> Guid
        AddTextDot(self: File3dmObjectTable, text: str, location: Point3d) -> Guid
        AddTextDot(self: File3dmObjectTable, text: str, location: Point3d, attributes: ObjectAttributes) -> Guid
        """
        pass

    def Delete(self, *__args):
        """
        Delete(self: File3dmObjectTable, objectIds: IEnumerable[Guid]) -> int
        Delete(self: File3dmObjectTable, objectId: Guid) -> bool
        Delete(self: File3dmObjectTable, obj: File3dmObject) -> bool
        """
        pass

    def Dump(self):
        """ Dump(self: File3dmObjectTable) -> str """
        pass

    def FindByLayer(self, layer):
        """ FindByLayer(self: File3dmObjectTable, layer: str) -> Array[File3dmObject] """
        pass

    def GetBoundingBox(self):
        """ GetBoundingBox(self: File3dmObjectTable) -> BoundingBox """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: File3dmObjectTable) -> IEnumerator[File3dmObject] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[File3dmObject](enumerable: IEnumerable[File3dmObject], value: File3dmObject) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: File3dmObjectTable) -> int

"""



class File3dmPlugInData(object):
    # no doc
    PlugInId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlugInId(self: File3dmPlugInData) -> Guid

"""



class File3dmPlugInDataTable(object, IEnumerable[File3dmPlugInData], IEnumerable, IRhinoTable[File3dmPlugInData]):
    # no doc
    def Clear(self):
        """ Clear(self: File3dmPlugInDataTable) """
        pass

    def Dump(self):
        """ Dump(self: File3dmPlugInDataTable) -> str """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: File3dmPlugInDataTable) -> IEnumerator[File3dmPlugInData] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[File3dmPlugInData](enumerable: IEnumerable[File3dmPlugInData], value: File3dmPlugInData) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: File3dmPlugInDataTable) -> int

"""



class File3dmSettings(object):
    # no doc
    ModelAbsoluteTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelAbsoluteTolerance(self: File3dmSettings) -> float

Set: ModelAbsoluteTolerance(self: File3dmSettings) = value
"""

    ModelAngleToleranceDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelAngleToleranceDegrees(self: File3dmSettings) -> float

Set: ModelAngleToleranceDegrees(self: File3dmSettings) = value
"""

    ModelAngleToleranceRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelAngleToleranceRadians(self: File3dmSettings) -> float

Set: ModelAngleToleranceRadians(self: File3dmSettings) = value
"""

    ModelBasepoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelBasepoint(self: File3dmSettings) -> Point3d

Set: ModelBasepoint(self: File3dmSettings) = value
"""

    ModelRelativeTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelRelativeTolerance(self: File3dmSettings) -> float

Set: ModelRelativeTolerance(self: File3dmSettings) = value
"""

    ModelUnitSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelUnitSystem(self: File3dmSettings) -> UnitSystem

Set: ModelUnitSystem(self: File3dmSettings) = value
"""

    ModelUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelUrl(self: File3dmSettings) -> str

Set: ModelUrl(self: File3dmSettings) = value
"""

    PageAbsoluteTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageAbsoluteTolerance(self: File3dmSettings) -> float

Set: PageAbsoluteTolerance(self: File3dmSettings) = value
"""

    PageAngleToleranceDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageAngleToleranceDegrees(self: File3dmSettings) -> float

Set: PageAngleToleranceDegrees(self: File3dmSettings) = value
"""

    PageAngleToleranceRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageAngleToleranceRadians(self: File3dmSettings) -> float

Set: PageAngleToleranceRadians(self: File3dmSettings) = value
"""

    PageRelativeTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageRelativeTolerance(self: File3dmSettings) -> float

Set: PageRelativeTolerance(self: File3dmSettings) = value
"""

    PageUnitSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageUnitSystem(self: File3dmSettings) -> UnitSystem

Set: PageUnitSystem(self: File3dmSettings) = value
"""



class File3dmTypeCodes(object):
    # no doc
    TCODE_ANALYSIS_MESH = None
    TCODE_ANGULAR_DIMENSION = None
    TCODE_ANNOTATION = None
    TCODE_ANNOTATION_LEADER = None
    TCODE_ANNOTATION_SETTINGS = None
    TCODE_ANONYMOUS_CHUNK = None
    TCODE_BITMAPPREVIEW = None
    TCODE_BITMAP_RECORD = None
    TCODE_BITMAP_TABLE = None
    TCODE_BUMPMAP = None
    TCODE_COMMENTBLOCK = None
    TCODE_COMPRESSED_MESH_GEOMETRY = None
    TCODE_CPLANE = None
    TCODE_CRC = None
    TCODE_CURRENTLAYER = None
    TCODE_DICTIONARY = None
    TCODE_DICTIONARY_END = None
    TCODE_DICTIONARY_ENTRY = None
    TCODE_DICTIONARY_ID = None
    TCODE_DIMSTYLE_RECORD = None
    TCODE_DIMSTYLE_TABLE = None
    TCODE_DISPLAY = None
    TCODE_DISP_AM_RESOLUTION = None
    TCODE_DISP_CPLINES = None
    TCODE_DISP_MAXLENGTH = None
    TCODE_ENDOFFILE = None
    TCODE_ENDOFFILE_GOO = None
    TCODE_ENDOFTABLE = None
    TCODE_FONT_RECORD = None
    TCODE_FONT_TABLE = None
    TCODE_GEOMETRY = None
    TCODE_GROUP_RECORD = None
    TCODE_GROUP_TABLE = None
    TCODE_HATCHPATTERN_RECORD = None
    TCODE_HATCHPATTERN_TABLE = None
    TCODE_HIDE_TRACE = None
    TCODE_HISTORYRECORD_RECORD = None
    TCODE_HISTORYRECORD_TABLE = None
    TCODE_INSTANCE_DEFINITION_RECORD = None
    TCODE_INSTANCE_DEFINITION_TABLE = None
    TCODE_INTERFACE = None
    TCODE_LAYER = None
    TCODE_LAYERINDEX = None
    TCODE_LAYERLOCKED = None
    TCODE_LAYERMATERIALINDEX = None
    TCODE_LAYERNAME = None
    TCODE_LAYERON = None
    TCODE_LAYERPICKABLE = None
    TCODE_LAYERREF = None
    TCODE_LAYERRENDERABLE = None
    TCODE_LAYERSNAPABLE = None
    TCODE_LAYERSTATE = None
    TCODE_LAYERTABLE = None
    TCODE_LAYERTHAWED = None
    TCODE_LAYERVISIBLE = None
    TCODE_LAYER_OBSELETE_1 = None
    TCODE_LAYER_OBSELETE_2 = None
    TCODE_LAYER_OBSELETE_3 = None
    TCODE_LAYER_RECORD = None
    TCODE_LAYER_TABLE = None
    TCODE_LEGACY_ASM = None
    TCODE_LEGACY_ASMSTUFF = None
    TCODE_LEGACY_BND = None
    TCODE_LEGACY_BNDSTUFF = None
    TCODE_LEGACY_CRV = None
    TCODE_LEGACY_CRVSTUFF = None
    TCODE_LEGACY_FAC = None
    TCODE_LEGACY_FACSTUFF = None
    TCODE_LEGACY_GEOMETRY = None
    TCODE_LEGACY_PNT = None
    TCODE_LEGACY_PNTSTUFF = None
    TCODE_LEGACY_PRT = None
    TCODE_LEGACY_PRTSTUFF = None
    TCODE_LEGACY_SHL = None
    TCODE_LEGACY_SHLSTUFF = None
    TCODE_LEGACY_SPL = None
    TCODE_LEGACY_SPLSTUFF = None
    TCODE_LEGACY_SRF = None
    TCODE_LEGACY_SRFSTUFF = None
    TCODE_LEGACY_TOL_ANGLE = None
    TCODE_LEGACY_TOL_FIT = None
    TCODE_LEGACY_TRM = None
    TCODE_LEGACY_TRMSTUFF = None
    TCODE_LIGHT_RECORD = None
    TCODE_LIGHT_RECORD_ATTRIBUTES = None
    TCODE_LIGHT_RECORD_ATTRIBUTES_USERDATA = None
    TCODE_LIGHT_RECORD_END = None
    TCODE_LIGHT_TABLE = None
    TCODE_LINEAR_DIMENSION = None
    TCODE_LINETYPE_RECORD = None
    TCODE_LINETYPE_TABLE = None
    TCODE_MATERIAL_RECORD = None
    TCODE_MATERIAL_TABLE = None
    TCODE_MAXIMIZED_VIEWPORT = None
    TCODE_MESH_OBJECT = None
    TCODE_NAME = None
    TCODE_NAMED_CPLANE = None
    TCODE_NAMED_VIEW = None
    TCODE_NEAR_CLIP_PLANE = None
    TCODE_NOTES = None
    TCODE_OBJECT_RECORD = None
    TCODE_OBJECT_RECORD_ATTRIBUTES = None
    TCODE_OBJECT_RECORD_ATTRIBUTES_USERDATA = None
    TCODE_OBJECT_RECORD_END = None
    TCODE_OBJECT_RECORD_HISTORY = None
    TCODE_OBJECT_RECORD_HISTORY_DATA = None
    TCODE_OBJECT_RECORD_HISTORY_HEADER = None
    TCODE_OBJECT_RECORD_TYPE = None
    TCODE_OBJECT_TABLE = None
    TCODE_OBSOLETE_LAYERSET_RECORD = None
    TCODE_OBSOLETE_LAYERSET_TABLE = None
    TCODE_OLD_FULLMESH = None
    TCODE_OLD_MESH_UV = None
    TCODE_OLD_MESH_VERTEX_NORMALS = None
    TCODE_OLD_RH_TRIMESH = None
    TCODE_OPENNURBS_CLASS = None
    TCODE_OPENNURBS_CLASS_DATA = None
    TCODE_OPENNURBS_CLASS_END = None
    TCODE_OPENNURBS_CLASS_USERDATA = None
    TCODE_OPENNURBS_CLASS_USERDATA_HEADER = None
    TCODE_OPENNURBS_CLASS_UUID = None
    TCODE_OPENNURBS_OBJECT = None
    TCODE_PROPERTIES_APPLICATION = None
    TCODE_PROPERTIES_COMPRESSED_PREVIEWIMAGE = None
    TCODE_PROPERTIES_NOTES = None
    TCODE_PROPERTIES_OPENNURBS_VERSION = None
    TCODE_PROPERTIES_PREVIEWIMAGE = None
    TCODE_PROPERTIES_REVISIONHISTORY = None
    TCODE_PROPERTIES_TABLE = None
    TCODE_RADIAL_DIMENSION = None
    TCODE_RENDER = None
    TCODE_RENDERMESHPARAMS = None
    TCODE_RENDER_MATERIAL_ID = None
    TCODE_RGB = None
    TCODE_RGBDISPLAY = None
    TCODE_RHINOIO_OBJECT_BREP = None
    TCODE_RHINOIO_OBJECT_DATA = None
    TCODE_RHINOIO_OBJECT_END = None
    TCODE_RHINOIO_OBJECT_NURBS_CURVE = None
    TCODE_RHINOIO_OBJECT_NURBS_SURFACE = None
    TCODE_RH_POINT = None
    TCODE_RH_SPOTLIGHT = None
    TCODE_SETTINGS_ANALYSISMESH = None
    TCODE_SETTINGS_ANNOTATION = None
    TCODE_SETTINGS_ATTRIBUTES = None
    TCODE_SETTINGS_CURRENT_COLOR = None
    TCODE_SETTINGS_CURRENT_DIMSTYLE_INDEX = None
    TCODE_SETTINGS_CURRENT_FONT_INDEX = None
    TCODE_SETTINGS_CURRENT_LAYER_INDEX = None
    TCODE_SETTINGS_CURRENT_MATERIAL_INDEX = None
    TCODE_SETTINGS_CURRENT_WIRE_DENSITY = None
    TCODE_SETTINGS_GRID_DEFAULTS = None
    TCODE_SETTINGS_MODEL_URL = None
    TCODE_SETTINGS_NAMED_CPLANE_LIST = None
    TCODE_SETTINGS_NAMED_VIEW_LIST = None
    TCODE_SETTINGS_PLUGINLIST = None
    TCODE_SETTINGS_RENDER = None
    TCODE_SETTINGS_RENDERMESH = None
    TCODE_SETTINGS_TABLE = None
    TCODE_SETTINGS_UNITSANDTOLS = None
    TCODE_SETTINGS_VIEW_LIST = None
    TCODE_SETTINGS__NEVER__USE__THIS = None
    TCODE_SHORT = None
    TCODE_SHOWGRID = None
    TCODE_SHOWGRIDAXES = None
    TCODE_SHOWWORLDAXES = None
    TCODE_SNAPSIZE = None
    TCODE_STUFF = None
    TCODE_SUMMARY = None
    TCODE_TABLE = None
    TCODE_TABLEREC = None
    TCODE_TEXTUREMAP = None
    TCODE_TEXTURE_MAPPING_RECORD = None
    TCODE_TEXTURE_MAPPING_TABLE = None
    TCODE_TEXT_BLOCK = None
    TCODE_TOLERANCE = None
    TCODE_TRANSPARENCY = None
    TCODE_UNIT_AND_TOLERANCES = None
    TCODE_USER = None
    TCODE_USER_RECORD = None
    TCODE_USER_TABLE = None
    TCODE_USER_TABLE_UUID = None
    TCODE_VIEW = None
    TCODE_VIEWPORT = None
    TCODE_VIEWPORT_DISPLAY_MODE = None
    TCODE_VIEWPORT_POSITION = None
    TCODE_VIEWPORT_TRACEINFO = None
    TCODE_VIEWPORT_WALLPAPER = None
    TCODE_VIEW_ATTRIBUTES = None
    TCODE_VIEW_CPLANE = None
    TCODE_VIEW_DISPLAYMODE = None
    TCODE_VIEW_NAME = None
    TCODE_VIEW_POSITION = None
    TCODE_VIEW_RECORD = None
    TCODE_VIEW_SHOWCONAXES = None
    TCODE_VIEW_SHOWCONGRID = None
    TCODE_VIEW_SHOWWORLDAXES = None
    TCODE_VIEW_TARGET = None
    TCODE_VIEW_TRACEIMAGE = None
    TCODE_VIEW_VIEWPORT = None
    TCODE_VIEW_VIEWPORT_USERDATA = None
    TCODE_VIEW_WALLPAPER = None
    TCODE_VIEW_WALLPAPER_V3 = None
    TCODE_XDATA = None
    __all__ = [
        'TCODE_ANALYSIS_MESH',
        'TCODE_ANGULAR_DIMENSION',
        'TCODE_ANNOTATION',
        'TCODE_ANNOTATION_LEADER',
        'TCODE_ANNOTATION_SETTINGS',
        'TCODE_ANONYMOUS_CHUNK',
        'TCODE_BITMAP_RECORD',
        'TCODE_BITMAP_TABLE',
        'TCODE_BITMAPPREVIEW',
        'TCODE_BUMPMAP',
        'TCODE_COMMENTBLOCK',
        'TCODE_COMPRESSED_MESH_GEOMETRY',
        'TCODE_CPLANE',
        'TCODE_CRC',
        'TCODE_CURRENTLAYER',
        'TCODE_DICTIONARY',
        'TCODE_DICTIONARY_END',
        'TCODE_DICTIONARY_ENTRY',
        'TCODE_DICTIONARY_ID',
        'TCODE_DIMSTYLE_RECORD',
        'TCODE_DIMSTYLE_TABLE',
        'TCODE_DISP_AM_RESOLUTION',
        'TCODE_DISP_CPLINES',
        'TCODE_DISP_MAXLENGTH',
        'TCODE_DISPLAY',
        'TCODE_ENDOFFILE',
        'TCODE_ENDOFFILE_GOO',
        'TCODE_ENDOFTABLE',
        'TCODE_FONT_RECORD',
        'TCODE_FONT_TABLE',
        'TCODE_GEOMETRY',
        'TCODE_GROUP_RECORD',
        'TCODE_GROUP_TABLE',
        'TCODE_HATCHPATTERN_RECORD',
        'TCODE_HATCHPATTERN_TABLE',
        'TCODE_HIDE_TRACE',
        'TCODE_HISTORYRECORD_RECORD',
        'TCODE_HISTORYRECORD_TABLE',
        'TCODE_INSTANCE_DEFINITION_RECORD',
        'TCODE_INSTANCE_DEFINITION_TABLE',
        'TCODE_INTERFACE',
        'TCODE_LAYER',
        'TCODE_LAYER_OBSELETE_1',
        'TCODE_LAYER_OBSELETE_2',
        'TCODE_LAYER_OBSELETE_3',
        'TCODE_LAYER_RECORD',
        'TCODE_LAYER_TABLE',
        'TCODE_LAYERINDEX',
        'TCODE_LAYERLOCKED',
        'TCODE_LAYERMATERIALINDEX',
        'TCODE_LAYERNAME',
        'TCODE_LAYERON',
        'TCODE_LAYERPICKABLE',
        'TCODE_LAYERREF',
        'TCODE_LAYERRENDERABLE',
        'TCODE_LAYERSNAPABLE',
        'TCODE_LAYERSTATE',
        'TCODE_LAYERTABLE',
        'TCODE_LAYERTHAWED',
        'TCODE_LAYERVISIBLE',
        'TCODE_LEGACY_ASM',
        'TCODE_LEGACY_ASMSTUFF',
        'TCODE_LEGACY_BND',
        'TCODE_LEGACY_BNDSTUFF',
        'TCODE_LEGACY_CRV',
        'TCODE_LEGACY_CRVSTUFF',
        'TCODE_LEGACY_FAC',
        'TCODE_LEGACY_FACSTUFF',
        'TCODE_LEGACY_GEOMETRY',
        'TCODE_LEGACY_PNT',
        'TCODE_LEGACY_PNTSTUFF',
        'TCODE_LEGACY_PRT',
        'TCODE_LEGACY_PRTSTUFF',
        'TCODE_LEGACY_SHL',
        'TCODE_LEGACY_SHLSTUFF',
        'TCODE_LEGACY_SPL',
        'TCODE_LEGACY_SPLSTUFF',
        'TCODE_LEGACY_SRF',
        'TCODE_LEGACY_SRFSTUFF',
        'TCODE_LEGACY_TOL_ANGLE',
        'TCODE_LEGACY_TOL_FIT',
        'TCODE_LEGACY_TRM',
        'TCODE_LEGACY_TRMSTUFF',
        'TCODE_LIGHT_RECORD',
        'TCODE_LIGHT_RECORD_ATTRIBUTES',
        'TCODE_LIGHT_RECORD_ATTRIBUTES_USERDATA',
        'TCODE_LIGHT_RECORD_END',
        'TCODE_LIGHT_TABLE',
        'TCODE_LINEAR_DIMENSION',
        'TCODE_LINETYPE_RECORD',
        'TCODE_LINETYPE_TABLE',
        'TCODE_MATERIAL_RECORD',
        'TCODE_MATERIAL_TABLE',
        'TCODE_MAXIMIZED_VIEWPORT',
        'TCODE_MESH_OBJECT',
        'TCODE_NAME',
        'TCODE_NAMED_CPLANE',
        'TCODE_NAMED_VIEW',
        'TCODE_NEAR_CLIP_PLANE',
        'TCODE_NOTES',
        'TCODE_OBJECT_RECORD',
        'TCODE_OBJECT_RECORD_ATTRIBUTES',
        'TCODE_OBJECT_RECORD_ATTRIBUTES_USERDATA',
        'TCODE_OBJECT_RECORD_END',
        'TCODE_OBJECT_RECORD_HISTORY',
        'TCODE_OBJECT_RECORD_HISTORY_DATA',
        'TCODE_OBJECT_RECORD_HISTORY_HEADER',
        'TCODE_OBJECT_RECORD_TYPE',
        'TCODE_OBJECT_TABLE',
        'TCODE_OBSOLETE_LAYERSET_RECORD',
        'TCODE_OBSOLETE_LAYERSET_TABLE',
        'TCODE_OLD_FULLMESH',
        'TCODE_OLD_MESH_UV',
        'TCODE_OLD_MESH_VERTEX_NORMALS',
        'TCODE_OLD_RH_TRIMESH',
        'TCODE_OPENNURBS_CLASS',
        'TCODE_OPENNURBS_CLASS_DATA',
        'TCODE_OPENNURBS_CLASS_END',
        'TCODE_OPENNURBS_CLASS_USERDATA',
        'TCODE_OPENNURBS_CLASS_USERDATA_HEADER',
        'TCODE_OPENNURBS_CLASS_UUID',
        'TCODE_OPENNURBS_OBJECT',
        'TCODE_PROPERTIES_APPLICATION',
        'TCODE_PROPERTIES_COMPRESSED_PREVIEWIMAGE',
        'TCODE_PROPERTIES_NOTES',
        'TCODE_PROPERTIES_OPENNURBS_VERSION',
        'TCODE_PROPERTIES_PREVIEWIMAGE',
        'TCODE_PROPERTIES_REVISIONHISTORY',
        'TCODE_PROPERTIES_TABLE',
        'TCODE_RADIAL_DIMENSION',
        'TCODE_RENDER',
        'TCODE_RENDER_MATERIAL_ID',
        'TCODE_RENDERMESHPARAMS',
        'TCODE_RGB',
        'TCODE_RGBDISPLAY',
        'TCODE_RH_POINT',
        'TCODE_RH_SPOTLIGHT',
        'TCODE_RHINOIO_OBJECT_BREP',
        'TCODE_RHINOIO_OBJECT_DATA',
        'TCODE_RHINOIO_OBJECT_END',
        'TCODE_RHINOIO_OBJECT_NURBS_CURVE',
        'TCODE_RHINOIO_OBJECT_NURBS_SURFACE',
        'TCODE_SETTINGS__NEVER__USE__THIS',
        'TCODE_SETTINGS_ANALYSISMESH',
        'TCODE_SETTINGS_ANNOTATION',
        'TCODE_SETTINGS_ATTRIBUTES',
        'TCODE_SETTINGS_CURRENT_COLOR',
        'TCODE_SETTINGS_CURRENT_DIMSTYLE_INDEX',
        'TCODE_SETTINGS_CURRENT_FONT_INDEX',
        'TCODE_SETTINGS_CURRENT_LAYER_INDEX',
        'TCODE_SETTINGS_CURRENT_MATERIAL_INDEX',
        'TCODE_SETTINGS_CURRENT_WIRE_DENSITY',
        'TCODE_SETTINGS_GRID_DEFAULTS',
        'TCODE_SETTINGS_MODEL_URL',
        'TCODE_SETTINGS_NAMED_CPLANE_LIST',
        'TCODE_SETTINGS_NAMED_VIEW_LIST',
        'TCODE_SETTINGS_PLUGINLIST',
        'TCODE_SETTINGS_RENDER',
        'TCODE_SETTINGS_RENDERMESH',
        'TCODE_SETTINGS_TABLE',
        'TCODE_SETTINGS_UNITSANDTOLS',
        'TCODE_SETTINGS_VIEW_LIST',
        'TCODE_SHORT',
        'TCODE_SHOWGRID',
        'TCODE_SHOWGRIDAXES',
        'TCODE_SHOWWORLDAXES',
        'TCODE_SNAPSIZE',
        'TCODE_STUFF',
        'TCODE_SUMMARY',
        'TCODE_TABLE',
        'TCODE_TABLEREC',
        'TCODE_TEXT_BLOCK',
        'TCODE_TEXTURE_MAPPING_RECORD',
        'TCODE_TEXTURE_MAPPING_TABLE',
        'TCODE_TEXTUREMAP',
        'TCODE_TOLERANCE',
        'TCODE_TRANSPARENCY',
        'TCODE_UNIT_AND_TOLERANCES',
        'TCODE_USER',
        'TCODE_USER_RECORD',
        'TCODE_USER_TABLE',
        'TCODE_USER_TABLE_UUID',
        'TCODE_VIEW',
        'TCODE_VIEW_ATTRIBUTES',
        'TCODE_VIEW_CPLANE',
        'TCODE_VIEW_DISPLAYMODE',
        'TCODE_VIEW_NAME',
        'TCODE_VIEW_POSITION',
        'TCODE_VIEW_RECORD',
        'TCODE_VIEW_SHOWCONAXES',
        'TCODE_VIEW_SHOWCONGRID',
        'TCODE_VIEW_SHOWWORLDAXES',
        'TCODE_VIEW_TARGET',
        'TCODE_VIEW_TRACEIMAGE',
        'TCODE_VIEW_VIEWPORT',
        'TCODE_VIEW_VIEWPORT_USERDATA',
        'TCODE_VIEW_WALLPAPER',
        'TCODE_VIEW_WALLPAPER_V3',
        'TCODE_VIEWPORT',
        'TCODE_VIEWPORT_DISPLAY_MODE',
        'TCODE_VIEWPORT_POSITION',
        'TCODE_VIEWPORT_TRACEINFO',
        'TCODE_VIEWPORT_WALLPAPER',
        'TCODE_XDATA',
    ]


class File3dmWriteOptions(object):
    """ File3dmWriteOptions() """
    SaveAnalysisMeshes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SaveAnalysisMeshes(self: File3dmWriteOptions) -> bool

Set: SaveAnalysisMeshes(self: File3dmWriteOptions) = value
"""

    SaveRenderMeshes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SaveRenderMeshes(self: File3dmWriteOptions) -> bool

Set: SaveRenderMeshes(self: File3dmWriteOptions) = value
"""

    SaveUserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SaveUserData(self: File3dmWriteOptions) -> bool

Set: SaveUserData(self: File3dmWriteOptions) = value
"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: File3dmWriteOptions) -> int

Set: Version(self: File3dmWriteOptions) = value
"""



class FileType(object):
    """ FileType(extension: str, description: str) """
    @staticmethod # known case of __new__
    def __new__(self, extension, description):
        """ __new__(cls: type, extension: str, description: str) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: FileType) -> str

"""

    Extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Extension(self: FileType) -> str

"""



class SerializationOptions(object):
    """ SerializationOptions() """
    RhinoVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RhinoVersion(self: SerializationOptions) -> int

Set: RhinoVersion(self: SerializationOptions) = value
"""

    WriteUserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WriteUserData(self: SerializationOptions) -> bool

Set: WriteUserData(self: SerializationOptions) = value
"""



class TextLog(object, IDisposable):
    """
    TextLog()
    TextLog(filename: str)
    """
    def Dispose(self):
        """ Dispose(self: TextLog) """
        pass

    def PopIndent(self):
        """ PopIndent(self: TextLog) """
        pass

    def Print(self, *__args):
        """ Print(self: TextLog, format: str, arg0: object, arg1: object)Print(self: TextLog, format: str, arg0: object)Print(self: TextLog, text: str) """
        pass

    def PrintWrappedText(self, text, lineLength):
        """ PrintWrappedText(self: TextLog, text: str, lineLength: int) """
        pass

    def PushIndent(self):
        """ PushIndent(self: TextLog) """
        pass

    def ToString(self):
        """ ToString(self: TextLog) -> str """
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
    def __new__(self, filename=None):
        """
        __new__(cls: type)
        __new__(cls: type, filename: str)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IndentSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IndentSize(self: TextLog) -> int

Set: IndentSize(self: TextLog) = value
"""



