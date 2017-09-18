# encoding: utf-8
# module Rhino.FileIO calls itself FileIO
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BinaryArchiveException(IOException, ISerializable, _Exception):
    """
    Thrown by BinaryArchiveReader and BinaryArchiveWriter classes when
                an IO error has occured.
    
    BinaryArchiveException(message: str)
    """
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
        """
        Dispose(self: BinaryArchiveFile)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def Open(self):
        """ Open(self: BinaryArchiveFile) -> bool """
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
    """
    Represents an entity that is capable of reading a binary archive and
                instantiating strongly-typed objects.
    """
    def AtEnd(self):
        """
        AtEnd(self: BinaryArchiveReader) -> bool
        
            true if at end of a file
        """
        pass

    def Dump3dmChunk(self, log):
        """
        Dump3dmChunk(self: BinaryArchiveReader, log: TextLog) -> UInt32
        
            Fnction for studying contents of a file.  The primary use is as an aid
                    to help dig 
             through files that have been damaged (bad disks, transmission
                    errors, etc.) If an 
             error is found, a line that begins with the word
                    "ERROR" is printed.
        
        
            log: log where information is printed to
            Returns: 0 if something went wrong, otherwise the typecode of the chunk that
                    was just 
             studied.
        """
        pass

    def Read3dmChunkVersion(self, major, minor):
        """
        Read3dmChunkVersion(self: BinaryArchiveReader) -> (int, int)
        
            A chunk version is a single byte that encodes a major.minor
                    version number.  Useful 
             when creating I/O code for 3dm chunks
                    that may change in the future.  Increment the 
             minor version 
                    number if new information is added to the end of the chunk. 
               
                  Increment the major version if the format of the chunk changes
                    in some other 
             way.
        
            Returns: true on successful read.
        """
        pass

    def Read3dmStartSection(self, version, comment):
        """
        Read3dmStartSection(self: BinaryArchiveReader) -> (bool, int, str)
            Returns: true on success
        """
        pass

    def ReadBool(self):
        """
        ReadBool(self: BinaryArchiveReader) -> bool
        
            Reads a System.Boolean from the archive.
            Returns: The value that was read.
        """
        pass

    def ReadBoolArray(self):
        """
        ReadBoolArray(self: BinaryArchiveReader) -> Array[bool]
        
            Reads an array of System.Boolean from the archive.
                    An array is returned even if the 
             input was another enumerable type.
        
            Returns: The array that was read.
        """
        pass

    def ReadBoundingBox(self):
        """
        ReadBoundingBox(self: BinaryArchiveReader) -> BoundingBox
        
            Reads a Rhino.Geometry.BoundingBox from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadByte(self):
        """
        ReadByte(self: BinaryArchiveReader) -> Byte
        
            Reads a System.Byte from the archive.
            Returns: The value that was read.
        """
        pass

    def ReadByteArray(self):
        """
        ReadByteArray(self: BinaryArchiveReader) -> Array[Byte]
        
            Reads an array of System.Byte from the archive.
                    An array is returned even if the 
             input was another enumerable type.
        
            Returns: The array that was read.
        """
        pass

    def ReadColor(self):
        """
        ReadColor(self: BinaryArchiveReader) -> Color
        
            Reads a System.Drawing.Color from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadCompressedBuffer(self):
        """
        ReadCompressedBuffer(self: BinaryArchiveReader) -> Array[Byte]
        
            Reads an array of compressed System.Byte information from the archive and uncompresses it.
             
                    An array is returned even if the input was another enumerable type.
        
            Returns: The array that was read.
        """
        pass

    def ReadDictionary(self):
        """
        ReadDictionary(self: BinaryArchiveReader) -> ArchivableDictionary
        
            Reads a complete Rhino.Collections.ArchivableDictionary from the archive.
            Returns: The newly instantiated object.
        """
        pass

    def ReadDouble(self):
        """
        ReadDouble(self: BinaryArchiveReader) -> float
        
            Reads a System.Double from the archive.
            Returns: The value that was read.
        """
        pass

    def ReadDoubleArray(self):
        """
        ReadDoubleArray(self: BinaryArchiveReader) -> Array[float]
        
            Reads an array of System.Double from the archive.
                    An array is returned even if the 
             input was another enumerable type.
        
            Returns: The array that was read.
        """
        pass

    def ReadFont(self):
        """
        ReadFont(self: BinaryArchiveReader) -> Font
        
            Reads a System.Drawing.Font from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadGeometry(self):
        """
        ReadGeometry(self: BinaryArchiveReader) -> GeometryBase
        
            Reads a Rhino.Geometry.GeometryBase-derived object from the archive.
                    The 
             Rhino.Geometry.GeometryBase class is abstract.
        
            Returns: The element that was read.
        """
        pass

    def ReadGuid(self):
        """
        ReadGuid(self: BinaryArchiveReader) -> Guid
        
            Reads a System.Guid from the archive.
            Returns: The value that was read.
        """
        pass

    def ReadGuidArray(self):
        """
        ReadGuidArray(self: BinaryArchiveReader) -> Array[Guid]
        
            Reads an array of System.Guid from the archive.
                    An array is returned even if the 
             input was another enumerable type.
        
            Returns: The array that was read.
        """
        pass

    def ReadInt(self):
        """
        ReadInt(self: BinaryArchiveReader) -> int
        
            Reads a System.Int32 from the archive.
            Returns: The value that was read.
        """
        pass

    def ReadInt64(self):
        """
        ReadInt64(self: BinaryArchiveReader) -> Int64
        
            Reads a System.Int64 from the archive.
            Returns: The value that was read.
        """
        pass

    def ReadIntArray(self):
        """
        ReadIntArray(self: BinaryArchiveReader) -> Array[int]
        
            Reads an array of System.Int32 from the archive.
                    An array is returned even if the 
             input was another enumerable type.
        
            Returns: The array that was read.
        """
        pass

    def ReadInterval(self):
        """
        ReadInterval(self: BinaryArchiveReader) -> Interval
        
            Reads a Rhino.Geometry.Interval from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadLine(self):
        """
        ReadLine(self: BinaryArchiveReader) -> Line
        
            Reads a Rhino.Geometry.Line from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadMeshingParameters(self):
        """
        ReadMeshingParameters(self: BinaryArchiveReader) -> MeshingParameters
        
            Reads a Rhino.Geometry.MeshingParameters from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadObjRef(self):
        """
        ReadObjRef(self: BinaryArchiveReader) -> ObjRef
        
            Reads a Rhino.DocObjects.ObjRef from the archive
            Returns: the element that was read
        """
        pass

    def ReadObjRefArray(self):
        """
        ReadObjRefArray(self: BinaryArchiveReader) -> Array[ObjRef]
        
            Reads an array of System.Double from the archive.
                    An array is returned even if the 
             input was another enumerable type.
        
            Returns: The array that was read.
        """
        pass

    def ReadPlane(self):
        """
        ReadPlane(self: BinaryArchiveReader) -> Plane
        
            Reads a Rhino.Geometry.Plane from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadPoint(self):
        """
        ReadPoint(self: BinaryArchiveReader) -> Point
        
            Reads a System.Drawing.Point from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadPoint2d(self):
        """
        ReadPoint2d(self: BinaryArchiveReader) -> Point2d
        
            Reads a Rhino.Geometry.Point2d from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadPoint3d(self):
        """
        ReadPoint3d(self: BinaryArchiveReader) -> Point3d
        
            Reads a Rhino.Geometry.Point3d from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadPoint3f(self):
        """
        ReadPoint3f(self: BinaryArchiveReader) -> Point3f
        
            Reads a Rhino.Geometry.Point3f from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadPoint4d(self):
        """
        ReadPoint4d(self: BinaryArchiveReader) -> Point4d
        
            Reads a Rhino.Geometry.Point4d from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadPointF(self):
        """
        ReadPointF(self: BinaryArchiveReader) -> PointF
        
            Reads a System.Drawing.PointF from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadRay3d(self):
        """
        ReadRay3d(self: BinaryArchiveReader) -> Ray3d
        
            Reads a Rhino.Geometry.Ray3d from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadRectangle(self):
        """
        ReadRectangle(self: BinaryArchiveReader) -> Rectangle
        
            Reads a System.Drawing.Rectangle from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadRectangleF(self):
        """
        ReadRectangleF(self: BinaryArchiveReader) -> RectangleF
        
            Reads a System.Drawing.RectangleF from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadSByte(self):
        """
        ReadSByte(self: BinaryArchiveReader) -> SByte
        
            Reads a System.SByte from the archive.
            Returns: The value that was read.
        """
        pass

    def ReadSByteArray(self):
        """
        ReadSByteArray(self: BinaryArchiveReader) -> Array[SByte]
        
            Reads an array of System.SByte from the archive.
                    An array is returned even if the 
             input was another enumerable type.
        
            Returns: The array that was read.
        """
        pass

    def ReadShort(self):
        """
        ReadShort(self: BinaryArchiveReader) -> Int16
        
            Reads a System.Int16 from the archive.
            Returns: The value that was read.
        """
        pass

    def ReadShortArray(self):
        """
        ReadShortArray(self: BinaryArchiveReader) -> Array[Int16]
        
            Reads an array of System.Int16 from the archive.
                    An array is returned even if the 
             input was another enumerable type.
        
            Returns: The array that was read.
        """
        pass

    def ReadSingle(self):
        """
        ReadSingle(self: BinaryArchiveReader) -> Single
        
            Reads a System.Single from the archive.
            Returns: The value that was read.
        """
        pass

    def ReadSingleArray(self):
        """
        ReadSingleArray(self: BinaryArchiveReader) -> Array[Single]
        
            Reads an array of System.Single from the archive.
                    An array is returned even if the 
             input was another enumerable type.
        
            Returns: The array that was read.
        """
        pass

    def ReadSize(self):
        """
        ReadSize(self: BinaryArchiveReader) -> Size
        
            Reads a System.Drawing.Size from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadSizeF(self):
        """
        ReadSizeF(self: BinaryArchiveReader) -> SizeF
        
            Reads a System.Drawing.SizeF from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadString(self):
        """
        ReadString(self: BinaryArchiveReader) -> str
        
            Reads a System.String from the archive.
            Returns: The value that was read.
        """
        pass

    def ReadStringArray(self):
        """
        ReadStringArray(self: BinaryArchiveReader) -> Array[str]
        
            Reads an array of System.String from the archive.
                    An array is returned even if the 
             input was another enumerable type.
        
            Returns: The array that was read.
        """
        pass

    def ReadTransform(self):
        """
        ReadTransform(self: BinaryArchiveReader) -> Transform
        
            Reads a Rhino.Geometry.Transform from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadUInt(self):
        """
        ReadUInt(self: BinaryArchiveReader) -> UInt32
        
            Reads a System.UInt32 from the archive.
            Returns: The value that was read.
        """
        pass

    def ReadUShort(self):
        """
        ReadUShort(self: BinaryArchiveReader) -> UInt16
        
            Reads a System.UInt16 from the archive.
            Returns: The value that was read.
        """
        pass

    def ReadVector2d(self):
        """
        ReadVector2d(self: BinaryArchiveReader) -> Vector2d
        
            Reads a Rhino.Geometry.Vector2d from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadVector3d(self):
        """
        ReadVector3d(self: BinaryArchiveReader) -> Vector3d
        
            Reads a Rhino.Geometry.Vector3d from the archive.
            Returns: The element that was read.
        """
        pass

    def ReadVector3f(self):
        """
        ReadVector3f(self: BinaryArchiveReader) -> Vector3f
        
            Reads a Rhino.Geometry.Vector3f from the archive.
            Returns: The element that was read.
        """
        pass

    Archive3dmVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If a 3dm archive is being read or written, then this is the
            version of the 3dm archive format (1, 2, 3, 4 or 5).
            0     a 3dm archive is not being read/written
            1     a version 1 3dm archive is being read/written
            2     a version 2 3dm archive is being read/written
            3     a version 3 3dm archive is being read/written
            4     a version 4 3dm archive is being read/written
            5     an old version 5 3dm archive is being read
            50    a version 5 3dm archive is being read/written.

Get: Archive3dmVersion(self: BinaryArchiveReader) -> int

"""

    ReadErrorOccured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether en error occurred during reading.

Get: ReadErrorOccured(self: BinaryArchiveReader) -> bool

Set: ReadErrorOccured(self: BinaryArchiveReader) = value
"""



class BinaryArchiveWriter(object):
    """ Represents an entity that is able to write data to an archive. """
    def Write3dmChunkVersion(self, major, minor):
        """
        Write3dmChunkVersion(self: BinaryArchiveWriter, major: int, minor: int)
            A chunk version is a single byte that encodes a major.minor
                    version number.  Useful 
             when creating I/O code for 3dm chunks
                    that may change in the future.  Increment the 
             minor version 
                    number if new information is added to the end of the chunk. 
               
                  Increment the major version if the format of the chunk changes
                    in some other 
             way.
        
        
            major: 0 to 15.
            minor: 0 to 16.
            Returns: true on successful read.
        """
        pass

    def WriteBool(self, value):
        """
        WriteBool(self: BinaryArchiveWriter, value: bool)
            Writes a System.Boolean value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteBoolArray(self, value):
        """ WriteBoolArray(self: BinaryArchiveWriter, value: IEnumerable[bool]) """
        pass

    def WriteBoundingBox(self, value):
        """
        WriteBoundingBox(self: BinaryArchiveWriter, value: BoundingBox)
            Writes a Rhino.Geometry.BoundingBox value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteByte(self, value):
        """
        WriteByte(self: BinaryArchiveWriter, value: Byte)
            Writes a System.Byte value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteByteArray(self, value):
        """ WriteByteArray(self: BinaryArchiveWriter, value: IEnumerable[Byte]) """
        pass

    def WriteColor(self, value):
        """
        WriteColor(self: BinaryArchiveWriter, value: Color)
            Writes a System.Drawing.Color value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteCompressedBuffer(self, value):
        """ WriteCompressedBuffer(self: BinaryArchiveWriter, value: IEnumerable[Byte]) """
        pass

    def WriteDictionary(self, dictionary):
        """
        WriteDictionary(self: BinaryArchiveWriter, dictionary: ArchivableDictionary)
            Delivers the complete content of a dictionary to the archive.
        
            dictionary: A dictionary to archive.
        """
        pass

    def WriteDouble(self, value):
        """
        WriteDouble(self: BinaryArchiveWriter, value: float)
            Writes a System.Double value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteDoubleArray(self, value):
        """ WriteDoubleArray(self: BinaryArchiveWriter, value: IEnumerable[float]) """
        pass

    def WriteFont(self, value):
        """
        WriteFont(self: BinaryArchiveWriter, value: Font)
            Writes a System.Drawing.Font value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteGeometry(self, value):
        """
        WriteGeometry(self: BinaryArchiveWriter, value: GeometryBase)
            Writes a Rhino.Geometry.GeometryBase value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteGuid(self, value):
        """
        WriteGuid(self: BinaryArchiveWriter, value: Guid)
            Writes a System.Guid value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteGuidArray(self, value):
        """ WriteGuidArray(self: BinaryArchiveWriter, value: IEnumerable[Guid]) """
        pass

    def WriteInt(self, value):
        """
        WriteInt(self: BinaryArchiveWriter, value: int)
            Writes a System.Int32 value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteInt64(self, value):
        """
        WriteInt64(self: BinaryArchiveWriter, value: Int64)
            Writes a System.Int64 value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteIntArray(self, value):
        """ WriteIntArray(self: BinaryArchiveWriter, value: IEnumerable[int]) """
        pass

    def WriteInterval(self, value):
        """
        WriteInterval(self: BinaryArchiveWriter, value: Interval)
            Writes a Rhino.Geometry.Interval value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteLine(self, value):
        """
        WriteLine(self: BinaryArchiveWriter, value: Line)
            Writes a Rhino.Geometry.Line value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteMeshingParameters(self, value):
        """
        WriteMeshingParameters(self: BinaryArchiveWriter, value: MeshingParameters)
            Writes a Rhino.Geometry.MeshingParameters value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteObjRef(self, objref):
        """
        WriteObjRef(self: BinaryArchiveWriter, objref: ObjRef)
            Writes a Rhino.DocObjects.ObjRef to the archive
            Returns: the element that was read
        """
        pass

    def WriteObjRefArray(self, objrefs):
        """ WriteObjRefArray(self: BinaryArchiveWriter, objrefs: IEnumerable[ObjRef]) """
        pass

    def WritePlane(self, value):
        """
        WritePlane(self: BinaryArchiveWriter, value: Plane)
            Writes a Rhino.Geometry.Plane value to the archive.
        
            value: A value to write.
        """
        pass

    def WritePoint(self, value):
        """
        WritePoint(self: BinaryArchiveWriter, value: Point)
            Writes a System.Drawing.Point value to the archive.
        
            value: A value to write.
        """
        pass

    def WritePoint2d(self, value):
        """
        WritePoint2d(self: BinaryArchiveWriter, value: Point2d)
            Writes a Rhino.Geometry.Point2d value to the archive.
        
            value: A value to write.
        """
        pass

    def WritePoint3d(self, value):
        """
        WritePoint3d(self: BinaryArchiveWriter, value: Point3d)
            Writes a Rhino.Geometry.Point3d value to the archive.
        
            value: A value to write.
        """
        pass

    def WritePoint3f(self, value):
        """
        WritePoint3f(self: BinaryArchiveWriter, value: Point3f)
            Writes a Rhino.Geometry.Point3f value to the archive.
        
            value: A value to write.
        """
        pass

    def WritePoint4d(self, value):
        """
        WritePoint4d(self: BinaryArchiveWriter, value: Point4d)
            Writes a Rhino.Geometry.Point4d value to the archive.
        
            value: A value to write.
        """
        pass

    def WritePointF(self, value):
        """
        WritePointF(self: BinaryArchiveWriter, value: PointF)
            Writes a System.Drawing.PointF value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteRay3d(self, value):
        """
        WriteRay3d(self: BinaryArchiveWriter, value: Ray3d)
            Writes a Rhino.Geometry.Ray3d value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteRectangle(self, value):
        """
        WriteRectangle(self: BinaryArchiveWriter, value: Rectangle)
            Writes a System.Drawing.Rectangle value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteRectangleF(self, value):
        """
        WriteRectangleF(self: BinaryArchiveWriter, value: RectangleF)
            Writes a System.Drawing.RectangleF value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteSByte(self, value):
        """
        WriteSByte(self: BinaryArchiveWriter, value: SByte)
            Writes a System.SByte value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteSByteArray(self, value):
        """ WriteSByteArray(self: BinaryArchiveWriter, value: IEnumerable[SByte]) """
        pass

    def WriteShort(self, value):
        """
        WriteShort(self: BinaryArchiveWriter, value: Int16)
            Writes a System.Int16 value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteShortArray(self, value):
        """ WriteShortArray(self: BinaryArchiveWriter, value: IEnumerable[Int16]) """
        pass

    def WriteSingle(self, value):
        """
        WriteSingle(self: BinaryArchiveWriter, value: Single)
            Writes a System.Single value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteSingleArray(self, value):
        """ WriteSingleArray(self: BinaryArchiveWriter, value: IEnumerable[Single]) """
        pass

    def WriteSize(self, value):
        """
        WriteSize(self: BinaryArchiveWriter, value: Size)
            Writes a System.Drawing.Size value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteSizeF(self, value):
        """
        WriteSizeF(self: BinaryArchiveWriter, value: SizeF)
            Writes a System.Drawing.SizeF value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteString(self, value):
        """
        WriteString(self: BinaryArchiveWriter, value: str)
            Writes a System.String value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteStringArray(self, value):
        """ WriteStringArray(self: BinaryArchiveWriter, value: IEnumerable[str]) """
        pass

    def WriteTransform(self, value):
        """
        WriteTransform(self: BinaryArchiveWriter, value: Transform)
            Writes a Rhino.Geometry.Transform value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteUInt(self, value):
        """
        WriteUInt(self: BinaryArchiveWriter, value: UInt32)
            Writes a System.UInt32 value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteUShort(self, value):
        """
        WriteUShort(self: BinaryArchiveWriter, value: UInt16)
            Writes a System.UInt16 value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteVector2d(self, value):
        """
        WriteVector2d(self: BinaryArchiveWriter, value: Vector2d)
            Writes a Rhino.Geometry.Vector2d value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteVector3d(self, value):
        """
        WriteVector3d(self: BinaryArchiveWriter, value: Vector3d)
            Writes a Rhino.Geometry.Vector3d value to the archive.
        
            value: A value to write.
        """
        pass

    def WriteVector3f(self, value):
        """
        WriteVector3f(self: BinaryArchiveWriter, value: Vector3f)
            Writes a Rhino.Geometry.Vector3f value to the archive.
        
            value: A value to write.
        """
        pass

    Archive3dmVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If a 3dm archive is being read or written, then this is the
            version of the 3dm archive format (1, 2, 3, 4 or 5).
            0     a 3dm archive is not being read/written
            1     a version 1 3dm archive is being read/written
            2     a version 2 3dm archive is being read/written
            3     a version 3 3dm archive is being read/written
            4     a version 4 3dm archive is being read/written
            5     an old version 5 3dm archive is being read
            50    a version 5 3dm archive is being read/written.

Get: Archive3dmVersion(self: BinaryArchiveWriter) -> int

"""

    WriteErrorOccured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether an error occurred.

Get: WriteErrorOccured(self: BinaryArchiveWriter) -> bool

Set: WriteErrorOccured(self: BinaryArchiveWriter) = value
"""



class File3dm(object, IDisposable):
    """
    Represents a 3dm file, which is stored using the OpenNURBS file standard.
                The 3dm format is the main Rhinoceros storage format.Visit http://www.opennurbs.com/ for more details.
    
    File3dm()
    """
    def Audit(self, attemptRepair, repairCount, errors, warnings):
        """
        Audit(self: File3dm, attemptRepair: bool) -> (int, int, str, Array[int])
        
            Check a model to make sure it is valid and, if possible
                    and requested, attempt to 
             repair.
        
        
            attemptRepair: if true and a problem is found, the problem is repaired.
            Returns: <0 (model has serious errors),
                    0 (model is ok),
                    >0 (number of problems 
             that were found)
        """
        pass

    def Dispose(self):
        """
        Dispose(self: File3dm)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def Dump(self):
        """
        Dump(self: File3dm) -> str
        
            Prepares a text dump of the entire model.
            Returns: The text dump.
        """
        pass

    def DumpSummary(self):
        """
        DumpSummary(self: File3dm) -> str
        
            Prepares a text dump of model properties and settings.
            Returns: The text dump.
        """
        pass

    def DumpToTextLog(self, log):
        """
        DumpToTextLog(self: File3dm, log: TextLog)
            Prepares a text dump of the entire model.
        """
        pass

    def IsValid(self, errors):
        """
        IsValid(self: File3dm, errors: TextLog) -> bool
        
            Checks a model to make sure it is valid.
        
            errors: if errors are found, a description of the problem is put in this variable.
            Returns: true if the model is valid.
        IsValid(self: File3dm) -> (bool, str)
        
            Checks a model to make sure it is valid.
            Returns: true if the model is valid.
        """
        pass

    def Polish(self):
        """
        Polish(self: File3dm)
            Quickly fills in the little details, like making sure there is at least
                    one layer 
             and table indices make sense.  For a full blown check and repair,
                    call Audit(true).
        """
        pass

    @staticmethod
    def Read(path, tableTypeFilterFilter=None, objectTypeFilter=None):
        """
        Read(path: str, tableTypeFilterFilter: TableTypeFilter, objectTypeFilter: ObjectTypeFilter) -> File3dm
        Read(path: str) -> File3dm
        
            Reads a 3dm file from a specified location.
        
            path: The file to read.
            Returns: new File3dm on success, null on error.
        """
        pass

    @staticmethod
    def ReadApplicationData(path, applicationName, applicationUrl, applicationDetails):
        """
        ReadApplicationData(path: str) -> (str, str, str)
        
            Reads only the application information from an existing 3dm file.
        
            path: A location on disk or network.
        """
        pass

    @staticmethod
    def ReadArchiveVersion(path):
        """
        ReadArchiveVersion(path: str) -> int
        
            Reads only the archive 3dm version from an existing 3dm file.
        
            path: The file from which to read the archive version.
            Returns: The 3dm file archive version.
        """
        pass

    @staticmethod
    def ReadNotes(path):
        """
        ReadNotes(path: str) -> str
        
            Reads only the notes from an existing 3dm file.
        
            path: The file from which to read the notes.
            Returns: The 3dm file notes.
        """
        pass

    @staticmethod
    def ReadPreviewImage(path):
        """
        ReadPreviewImage(path: str) -> Bitmap
        
            Attempts to read the preview image out of a 3dm file.
        
            path: The location of the file.
            Returns: A bitmap, or null on failure.
        """
        pass

    @staticmethod
    def ReadRevisionHistory(path, createdBy, lastEditedBy, revision, createdOn, lastEditedOn):
        """
        ReadRevisionHistory(path: str) -> (bool, str, str, int, DateTime, DateTime)
        
            Quickly check a file for it's revision information.  This function does
                    not read 
             the entire file, just what it needs to get revision information out
        
        
            path: path to the 3dm file
            Returns: true on success
        """
        pass

    @staticmethod
    def ReadWithLog(path, *__args):
        """
        ReadWithLog(path: str) -> (File3dm, str)
        
            Read a 3dm file from a specified location and log any archive
                    reading errors.
        
            path: The file to read.
            Returns: New File3dm on success, null on error.
        ReadWithLog(path: str, tableTypeFilterFilter: TableTypeFilter, objectTypeFilter: ObjectTypeFilter) -> (File3dm, str)
        """
        pass

    def Write(self, path, *__args):
        """
        Write(self: File3dm, path: str, options: File3dmWriteOptions) -> bool
        
            Writes contents of this model to an openNURBS archive. I STRONGLY
                    suggested that 
             you call Polish() before calling Write so that your
                    file has all the "fluff" that 
             makes it complete.  If the model is
                    not valid, then Write will refuse to write it.
        
        
            path: The file name to use for writing.
            Returns: true if archive is written with no error.
                    false if errors occur.
        Write(self: File3dm, path: str, version: int) -> bool
        
            Writes contents of this model to an openNURBS archive. I STRONGLY
                    suggested that 
             you call Polish() before calling Write so that your
                    file has all the "fluff" that 
             makes it complete.  If the model is
                    not valid, then Write will refuse to write it.
        
        
            path: The file name to use for writing.
            version: Version of the openNURBS archive to write.  Must be 2, 3, 4, or 5.
                    Rhino 2.x can 
             read version 2 files.
                    Rhino 3.x can read version 2 and 3 files.
                    Rhino 
             4.x can read version 2, 3 and 4 files.
                    Rhino 5.x can read version 2, 3, 4, and 5 
             files.
                    Use version 5 when possible.
        
            Returns: true if archive is written with no error.
                    false if errors occur.
        """
        pass

    def WriteWithLog(self, path, version, errorLog):
        """
        WriteWithLog(self: File3dm, path: str, version: int) -> (bool, str)
        
            Writes contents of this model to an openNURBS archive. I STRONGLY
                    suggested that 
             you call Polish() before calling Write so that your
                    file has all the "fluff" that 
             makes it complete.  If the model is
                    not valid, then Write will refuse to write it.
        
        
            path: Version of the openNURBS archive to write.  Must be 2, 3, 4, or 5.
                    Rhino 2.x can 
             read version 2 files.
                    Rhino 3.x can read version 2 and 3 files.
                    Rhino 
             4.x can read version 2, 3 and 4 files.
                    Rhino 5.x can read version 2, 3, 4, and 5 
             files.
                    Use version 5 when possible.
        
            version: A version number.
            Returns: true if archive is written with no error.
                    false if errors occur.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ApplicationDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets details for the application that wrote this file.

Get: ApplicationDetails(self: File3dm) -> str

Set: ApplicationDetails(self: File3dm) = value
"""

    ApplicationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the application that wrote this file.

Get: ApplicationName(self: File3dm) -> str

Set: ApplicationName(self: File3dm) = value
"""

    ApplicationUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a URL for the application that wrote this file.

Get: ApplicationUrl(self: File3dm) -> str

Set: ApplicationUrl(self: File3dm) = value
"""

    Created = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the DateTime that this file was originally created. If the
            value is not set in the 3dm file, then DateTime.MinValue is returned

Get: Created(self: File3dm) -> DateTime

"""

    CreatedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a string that names the user who created the file.

Get: CreatedBy(self: File3dm) -> str

"""

    DimStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dimension Styles in this file

Get: DimStyles(self: File3dm) -> IList[DimensionStyle]

"""

    HatchPatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Hatch patterns in this file

Get: HatchPatterns(self: File3dm) -> IList[HatchPattern]

"""

    HistoryRecords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """History records stored in this file

Get: HistoryRecords(self: File3dm) -> File3dmHistoryRecordTable

"""

    InstanceDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Instance definitions in this file

Get: InstanceDefinitions(self: File3dm) -> IList[InstanceDefinitionGeometry]

"""

    LastEdited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the DateTime that this file was last edited. If the
            value is not set in the 3dm file, then DateTime.MinValue is returned

Get: LastEdited(self: File3dm) -> DateTime

"""

    LastEditedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a string that names the user who last edited the file.

Get: LastEditedBy(self: File3dm) -> str

"""

    Layers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Layers in this file.

Get: Layers(self: File3dm) -> IList[Layer]

"""

    Linetypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Linetypes in this file.

Get: Linetypes(self: File3dm) -> IList[Linetype]

"""

    Materials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Materials in this file.

Get: Materials(self: File3dm) -> IList[Material]

"""

    NamedViews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Named view list

Get: NamedViews(self: File3dm) -> IList[ViewInfo]

"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the model notes.

Get: Notes(self: File3dm) -> File3dmNotes

Set: Notes(self: File3dm) = value
"""

    Objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets access to the Rhino.FileIO.File3dmObjectTable class associated with this file,
            which contains all objects.

Get: Objects(self: File3dm) -> File3dmObjectTable

"""

    PlugInData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Custom plug-in data in this file.  This data is not attached to any geometry or attributes

Get: PlugInData(self: File3dm) -> File3dmPlugInDataTable

"""

    Revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the revision number.

Get: Revision(self: File3dm) -> int

Set: Revision(self: File3dm) = value
"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Settings include tolerance, and unit system, and defaults used
            for creating views and objects.

Get: Settings(self: File3dm) -> File3dmSettings

"""

    StartSectionComments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the start section comments, which are the comments with which the 3dm file begins.

Get: StartSectionComments(self: File3dm) -> str

Set: StartSectionComments(self: File3dm) = value
"""

    Views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Views that represent the RhinoViews which are displayed when Rhino loads this file

Get: Views(self: File3dm) -> IList[ViewInfo]

"""


    ObjectTypeFilter = None
    TableTypeFilter = None


class File3dmHistoryRecordTable(object):
    """ Table of custom data provided by plug-ins """
    def Clear(self):
        """
        Clear(self: File3dmHistoryRecordTable)
            Remove all entries from this table
        """
        pass

    def Dump(self):
        """
        Dump(self: File3dmHistoryRecordTable) -> str
        
            Prepares a text dump of table.
            Returns: A string containing the dump.
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of history records in this table.

Get: Count(self: File3dmHistoryRecordTable) -> int

"""



class File3dmNotes(object):
    """
    Represents the notes information stored in a 3dm file.
    
    File3dmNotes()
    """
    IsHtml = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text format. If the format is HTML, true; false otherwise.

Get: IsHtml(self: File3dmNotes) -> bool

Set: IsHtml(self: File3dmNotes) = value
"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the notes visibility. If the notes are visible, true; false otherwise.

Get: IsVisible(self: File3dmNotes) -> bool

Set: IsVisible(self: File3dmNotes) = value
"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text content of the notes.

Get: Notes(self: File3dmNotes) -> str

Set: Notes(self: File3dmNotes) = value
"""

    WindowRectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the position of the Notes when they were saved.

Get: WindowRectangle(self: File3dmNotes) -> Rectangle

Set: WindowRectangle(self: File3dmNotes) = value
"""



class File3dmObject(object):
    """ Used to store geometry table object definition and attributes in a File3dm. """
    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the attributes that are linked with this document object.

Get: Attributes(self: File3dmObject) -> ObjectAttributes

"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the geometry that is linked with this document object.

Get: Geometry(self: File3dmObject) -> GeometryBase

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Name of the object. Equivalent to this.Attributes.Name.

Get: Name(self: File3dmObject) -> str

Set: Name(self: File3dmObject) = value
"""



class File3dmObjectTable(object, IEnumerable[File3dmObject], IEnumerable, IRhinoTable[File3dmObject]):
    """
    Represents a simple object table for a file that is open externally.
                This class mimics Rhino.DocObjects.Tables.ObjectTable while providing external eccess to the file.
    """
    def AddArc(self, arc, attributes=None):
        """
        AddArc(self: File3dmObjectTable, arc: Arc, attributes: ObjectAttributes) -> Guid
        
            Adds a curve object to the document representing an arc.
        
            arc: An arc to add.
            attributes: attributes to apply to arc.
            Returns: A unique identifier for the object.
        AddArc(self: File3dmObjectTable, arc: Arc) -> Guid
        
            Adds a curve object to the document representing an arc.
        
            arc: An arc.
            Returns: A unique identifier for the object.
        """
        pass

    def AddBrep(self, brep, attributes=None):
        """
        AddBrep(self: File3dmObjectTable, brep: Brep, attributes: ObjectAttributes) -> Guid
        
            Adds a brep object to Rhino.
        
            brep: A duplicate of this brep is added to Rhino.
            attributes: Attributes to apply to brep.
            Returns: A unique identifier for the object.
        AddBrep(self: File3dmObjectTable, brep: Brep) -> Guid
        
            Adds a brep object to Rhino.
        
            brep: A duplicate of this brep is added to Rhino.
            Returns: A unique identifier for the object.
        """
        pass

    def AddCircle(self, circle, attributes=None):
        """
        AddCircle(self: File3dmObjectTable, circle: Circle, attributes: ObjectAttributes) -> Guid
        
            Adds a curve object to the document representing a circle.
        
            circle: A circle to add.
            attributes: attributes to apply to circle.
            Returns: A unique identifier for the object.
        AddCircle(self: File3dmObjectTable, circle: Circle) -> Guid
        
            Adds a curve object to the document representing a circle.
        
            circle: A circle to add.
            Returns: A unique identifier for the object.
        """
        pass

    def AddClippingPlane(self, plane, uMagnitude, vMagnitude, *__args):
        """
        AddClippingPlane(self: File3dmObjectTable, plane: Plane, uMagnitude: float, vMagnitude: float, clippedViewportIds: IEnumerable[Guid], attributes: ObjectAttributes) -> Guid
        AddClippingPlane(self: File3dmObjectTable, plane: Plane, uMagnitude: float, vMagnitude: float, clippedViewportIds: IEnumerable[Guid]) -> Guid
        AddClippingPlane(self: File3dmObjectTable, plane: Plane, uMagnitude: float, vMagnitude: float, clippedViewportId: Guid) -> Guid
        
            Adds a clipping plane object to Rhino.
        
            plane: A plane.
            uMagnitude: The size in U direction.
            vMagnitude: The size in V direction.
            clippedViewportId: The viewport id that the new clipping plane will clip.
            Returns: A unique identifier for the object.
        """
        pass

    def AddCurve(self, curve, attributes=None):
        """
        AddCurve(self: File3dmObjectTable, curve: Curve, attributes: ObjectAttributes) -> Guid
        
            Adds a curve object to the table.
        
            curve: A duplicate of this curve is added to Rhino.
            attributes: Attributes to apply to curve.
            Returns: A unique identifier for the object.
        AddCurve(self: File3dmObjectTable, curve: Curve) -> Guid
        
            Adds a curve object to the table.
        
            curve: A curve to add.
            Returns: A unique identifier for the object.
        """
        pass

    def AddEllipse(self, ellipse, attributes=None):
        """
        AddEllipse(self: File3dmObjectTable, ellipse: Ellipse, attributes: ObjectAttributes) -> Guid
        
            Adds a curve object to the document representing an ellipse.
        
            ellipse: An ellipse to add.
            attributes: attributes to apply to ellipse.
            Returns: A unique identifier for the object.
        AddEllipse(self: File3dmObjectTable, ellipse: Ellipse) -> Guid
        
            Adds a curve object to the document representing an ellipse.
        
            ellipse: An ellipse to add.
            Returns: A unique identifier for the object.
        """
        pass

    def AddExtrusion(self, extrusion, attributes=None):
        """
        AddExtrusion(self: File3dmObjectTable, extrusion: Extrusion, attributes: ObjectAttributes) -> Guid
        
            Adds an extrusion object to Rhino.
        
            extrusion: A duplicate of this extrusion is added to Rhino.
            attributes: Attributes to link to the object.
            Returns: A unique identifier for the object.
        AddExtrusion(self: File3dmObjectTable, extrusion: Extrusion) -> Guid
        
            Adds an extrusion object to Rhino.
        
            extrusion: A duplicate of this extrusion is added to Rhino.
            Returns: A unique identifier for the object.
        """
        pass

    def AddHatch(self, hatch, attributes=None):
        """
        AddHatch(self: File3dmObjectTable, hatch: Hatch, attributes: ObjectAttributes) -> Guid
        
            Adds a hatch to the document.
        
            hatch: A hatch.
            attributes: Attributes to apply to brep.
            Returns: A unique identifier for the hatch, or System.Guid.Empty on failure.
        AddHatch(self: File3dmObjectTable, hatch: Hatch) -> Guid
        
            Adds a hatch to the document.
        
            hatch: A hatch.
            Returns: A unique identifier for the hatch, or System.Guid.Empty on failure.
        """
        pass

    def AddLeader(self, *__args):
        """
        AddLeader(self: File3dmObjectTable, text: str, plane: Plane, points: IEnumerable[Point2d]) -> Guid
        AddLeader(self: File3dmObjectTable, text: str, points: IEnumerable[Point3d]) -> Guid
        AddLeader(self: File3dmObjectTable, points: IEnumerable[Point3d]) -> Guid
        AddLeader(self: File3dmObjectTable, plane: Plane, points: IEnumerable[Point2d]) -> Guid
        AddLeader(self: File3dmObjectTable, plane: Plane, points: IEnumerable[Point2d], attributes: ObjectAttributes) -> Guid
        AddLeader(self: File3dmObjectTable, text: str, plane: Plane, points: IEnumerable[Point2d], attributes: ObjectAttributes) -> Guid
        """
        pass

    def AddLine(self, *__args):
        """
        AddLine(self: File3dmObjectTable, line: Line) -> Guid
        
            Adds a line object to Rhino.
            Returns: A unique identifier for the object.
        AddLine(self: File3dmObjectTable, line: Line, attributes: ObjectAttributes) -> Guid
        
            Adds a line object to Rhino.
        
            line: A line.
            attributes: Attributes to apply to line.
            Returns: A unique identifier for the object.
        AddLine(self: File3dmObjectTable, from: Point3d, to: Point3d) -> Guid
        
            Adds a line object to Rhino.
        
            from: A line start point.
            to: A line end point.
            Returns: A unique identifier of new rhino object.
        AddLine(self: File3dmObjectTable, from: Point3d, to: Point3d, attributes: ObjectAttributes) -> Guid
        
            Adds a line object to Rhino.
        
            from: The start point of the line.
            to: The end point of the line.
            attributes: Attributes to apply to line.
            Returns: A unique identifier for the object.
        """
        pass

    def AddLinearDimension(self, dimension, attributes=None):
        """
        AddLinearDimension(self: File3dmObjectTable, dimension: LinearDimension, attributes: ObjectAttributes) -> Guid
        
            Adds a linear dimension to the 3dm file object table.
        
            dimension: A dimension.
            attributes: Attributes to apply to dimension.
            Returns: A unique identifier for the object.
        AddLinearDimension(self: File3dmObjectTable, dimension: LinearDimension) -> Guid
        
            Adds a linear dimension to the 3dm file object table.
        
            dimension: A dimension.
            Returns: A unique identifier for the object.
        """
        pass

    def AddMesh(self, mesh, attributes=None):
        """
        AddMesh(self: File3dmObjectTable, mesh: Mesh, attributes: ObjectAttributes) -> Guid
        
            Adds a mesh object to Rhino.
        
            mesh: A duplicate of this mesh is added to Rhino.
            attributes: Attributes to link to the object.
            Returns: A unique identifier for the object.
        AddMesh(self: File3dmObjectTable, mesh: Mesh) -> Guid
        
            Adds a mesh object to Rhino.
        
            mesh: A duplicate of this mesh is added to Rhino.
            Returns: A unique identifier for the object.
        """
        pass

    def AddPoint(self, *__args):
        """
        AddPoint(self: File3dmObjectTable, point: Point3f) -> Guid
        
            Adds a point object to the document.
        
            point: location of point.
            Returns: A unique identifier for the object.
        AddPoint(self: File3dmObjectTable, point: Point3f, attributes: ObjectAttributes) -> Guid
        
            Adds a point object to the document.
        
            point: location of point.
            attributes: attributes to apply to point.
            Returns: A unique identifier for the object.
        AddPoint(self: File3dmObjectTable, point: Point3d, attributes: ObjectAttributes) -> Guid
        
            Adds a point object to the document.
        
            point: A location for point.
            attributes: attributes to apply to point.
            Returns: A unique identifier for the object.
        AddPoint(self: File3dmObjectTable, x: float, y: float, z: float) -> Guid
        
            Adds a point object to the table.
        
            x: X component of point coordinate.
            y: Y component of point coordinate.
            z: Z component of point coordinate.
            Returns: id of new object.
        AddPoint(self: File3dmObjectTable, point: Point3d) -> Guid
        
            Adds a point object to the table.
        
            point: A location for point.
            Returns: Id of new object.
        """
        pass

    def AddPointCloud(self, *__args):
        """
        AddPointCloud(self: File3dmObjectTable, points: IEnumerable[Point3d]) -> Guid
        AddPointCloud(self: File3dmObjectTable, points: IEnumerable[Point3d], attributes: ObjectAttributes) -> Guid
        AddPointCloud(self: File3dmObjectTable, cloud: PointCloud) -> Guid
        
            Adds a point cloud object to the document.
        
            cloud: PointCloud to add.
            Returns: A unique identifier for the object.
        AddPointCloud(self: File3dmObjectTable, cloud: PointCloud, attributes: ObjectAttributes) -> Guid
        
            Adds a point cloud object to the document.
        
            cloud: PointCloud to add.
            attributes: attributes to apply to point cloud.
            Returns: A unique identifier for the object.
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
        
            Adds a surface object to the document representing a sphere.
        
            sphere: A sphere to add.
            attributes: Attributes to link with the sphere.
            Returns: A unique identifier for the object.
        AddSphere(self: File3dmObjectTable, sphere: Sphere) -> Guid
        
            Adds a surface object to the document representing a sphere.
        
            sphere: A sphere to add.
            Returns: A unique identifier for the object.
        """
        pass

    def AddSurface(self, surface, attributes=None):
        """
        AddSurface(self: File3dmObjectTable, surface: Surface, attributes: ObjectAttributes) -> Guid
        
            Adds a surface object to Rhino.
        
            surface: A duplicate of this surface is added to Rhino.
            attributes: Attributes to link to the object.
            Returns: A unique identifier for the object.
        AddSurface(self: File3dmObjectTable, surface: Surface) -> Guid
        
            Adds a surface object to Rhino.
        
            surface: A duplicate of this surface is added to Rhino.
            Returns: A unique identifier for the object.
        """
        pass

    def AddText(self, *__args):
        """
        AddText(self: File3dmObjectTable, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool, justification: TextJustification) -> Guid
        
            Adds an annotation text object to the document.
        
            text: Text string.
            plane: Plane of text.
            height: Height of text.
            fontName: Name of FontFace.
            bold: Bold flag.
            italic: Italic flag.
            justification: The justification of the text.
            Returns: The Guid of the newly added object or Guid.Empty on failure.
        AddText(self: File3dmObjectTable, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool, justification: TextJustification, attributes: ObjectAttributes) -> Guid
        
            Adds an annotation text object to the document.
        
            text: Text string.
            plane: Plane of text.
            height: Height of text.
            fontName: Name of FontFace.
            bold: Bold flag.
            italic: Italic flag.
            justification: The justification of the text.
            attributes: Attributes to link to the object.
            Returns: The Guid of the newly added object or Guid.Empty on failure.
        AddText(self: File3dmObjectTable, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool, attributes: ObjectAttributes) -> Guid
        
            Adds an annotation text object to the document.
        
            text: Text string.
            plane: Plane of text.
            height: Height of text.
            fontName: Name of FontFace.
            bold: Bold flag.
            italic: Italic flag.
            attributes: Object Attributes.
            Returns: The Guid of the newly added object or Guid.Empty on failure.
        AddText(self: File3dmObjectTable, text3d: Text3d) -> Guid
        
            Adds an annotation text object to the document.
        
            text3d: The text object to add.
            Returns: The Guid of the newly added object or Guid.Empty on failure.
        AddText(self: File3dmObjectTable, text3d: Text3d, attributes: ObjectAttributes) -> Guid
        
            Adds an annotation text object to the document.
        
            text3d: The text object to add.
            attributes: Attributes to link to the object.
            Returns: The Guid of the newly added object or Guid.Empty on failure.
        AddText(self: File3dmObjectTable, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool) -> Guid
        
            Adds an annotation text object to the document.
        
            text: Text string.
            plane: Plane of text.
            height: Height of text.
            fontName: Name of FontFace.
            bold: Bold flag.
            italic: Italic flag.
            Returns: The Guid of the newly added object or Guid.Empty on failure.
        """
        pass

    def AddTextDot(self, *__args):
        """
        AddTextDot(self: File3dmObjectTable, dot: TextDot) -> Guid
        
            Adds a text dot object to Rhino.
        
            dot: The text dot.
            Returns: A unique identifier for the object.
        AddTextDot(self: File3dmObjectTable, dot: TextDot, attributes: ObjectAttributes) -> Guid
        
            Adds a text dot object to Rhino.
        
            dot: The text dot.
            attributes: Attributes to link with curve.
            Returns: A unique identifier for the object.
        AddTextDot(self: File3dmObjectTable, text: str, location: Point3d) -> Guid
        
            Adds a text dot object to the table.
        
            text: The text.
            location: The location.
            Returns: A unique identifier for the object.
        AddTextDot(self: File3dmObjectTable, text: str, location: Point3d, attributes: ObjectAttributes) -> Guid
        
            Adds a text dot object to the table.
        
            text: The text.
            location: The location.
            attributes: Attributes to link with curve.
            Returns: A unique identifier for the object.
        """
        pass

    def Delete(self, *__args):
        """
        Delete(self: File3dmObjectTable, objectIds: IEnumerable[Guid]) -> int
        Delete(self: File3dmObjectTable, objectId: Guid) -> bool
        
            Deletes object from document.
        
            objectId: Id of the object to delete.
            Returns: true on success, false on failure.
        Delete(self: File3dmObjectTable, obj: File3dmObject) -> bool
        
            Deletes object from document.
        
            obj: The object to delete.
            Returns: true on success, false on failure.
        """
        pass

    def Dump(self):
        """
        Dump(self: File3dmObjectTable) -> str
        
            Prepares a text dump of object table.
            Returns: A string containing the dump.
        """
        pass

    def FindByLayer(self, layer):
        """
        FindByLayer(self: File3dmObjectTable, layer: str) -> Array[File3dmObject]
        
            Finds all File3dmObject that are in a given layer.
        
            layer: Layer to search.
            Returns: Array of objects that belong to the specified group or null if no objects could be found.
        """
        pass

    def GetBoundingBox(self):
        """
        GetBoundingBox(self: File3dmObjectTable) -> BoundingBox
        
            Gets the bounding box containing every object in this table.
            Returns: The computed bounding box.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: File3dmObjectTable) -> IEnumerator[File3dmObject]
        
            Gets the enumerator that visits any Rhino.FileIO.File3dmObject in this table.
            Returns: The enumerator.
        """
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
    """Gets the number of File3dmObjects in this table.

Get: Count(self: File3dmObjectTable) -> int

"""



class File3dmPlugInData(object):
    """ Custom data in the file supplied by a plug-in """
    PlugInId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Plug-in this data is associated with

Get: PlugInId(self: File3dmPlugInData) -> Guid

"""



class File3dmPlugInDataTable(object, IEnumerable[File3dmPlugInData], IEnumerable, IRhinoTable[File3dmPlugInData]):
    """ Table of custom data provided by plug-ins """
    def Clear(self):
        """
        Clear(self: File3dmPlugInDataTable)
            Remove all entries from this table
        """
        pass

    def Dump(self):
        """
        Dump(self: File3dmPlugInDataTable) -> str
        
            Prepares a text dump of table.
            Returns: A string containing the dump.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: File3dmPlugInDataTable) -> IEnumerator[File3dmPlugInData]
        
            Gets the enumerator that visits any Rhino.FileIO.File3dmPlugInData in this table.
            Returns: The enumerator.
        """
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
    """Gets the number of File3dmPlugInData in this table.

Get: Count(self: File3dmPlugInDataTable) -> int

"""



class File3dmSettings(object):
    """ Contains settings used within the whole 3dm file. """
    ModelAbsoluteTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the model space absolute tolerance.

Get: ModelAbsoluteTolerance(self: File3dmSettings) -> float

Set: ModelAbsoluteTolerance(self: File3dmSettings) = value
"""

    ModelAngleToleranceDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the model space angle tolerance.

Get: ModelAngleToleranceDegrees(self: File3dmSettings) -> float

Set: ModelAngleToleranceDegrees(self: File3dmSettings) = value
"""

    ModelAngleToleranceRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the model space angle tolerance.

Get: ModelAngleToleranceRadians(self: File3dmSettings) -> float

Set: ModelAngleToleranceRadians(self: File3dmSettings) = value
"""

    ModelBasepoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the model basepoint that is used when the file is read as an instance definition.
            This point is mapped to the origin in the instance definition.

Get: ModelBasepoint(self: File3dmSettings) -> Point3d

Set: ModelBasepoint(self: File3dmSettings) = value
"""

    ModelRelativeTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the model space relative tolerance.

Get: ModelRelativeTolerance(self: File3dmSettings) -> float

Set: ModelRelativeTolerance(self: File3dmSettings) = value
"""

    ModelUnitSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the model unit system, using Rhino.UnitSystem enumeration.

Get: ModelUnitSystem(self: File3dmSettings) -> UnitSystem

Set: ModelUnitSystem(self: File3dmSettings) = value
"""

    ModelUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Uniform Resource Locator (URL) direction for the model.

Get: ModelUrl(self: File3dmSettings) -> str

Set: ModelUrl(self: File3dmSettings) = value
"""

    PageAbsoluteTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the page space absolute tolerance.

Get: PageAbsoluteTolerance(self: File3dmSettings) -> float

Set: PageAbsoluteTolerance(self: File3dmSettings) = value
"""

    PageAngleToleranceDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the page space angle tolerance.

Get: PageAngleToleranceDegrees(self: File3dmSettings) -> float

Set: PageAngleToleranceDegrees(self: File3dmSettings) = value
"""

    PageAngleToleranceRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the page space angle tolerance.

Get: PageAngleToleranceRadians(self: File3dmSettings) -> float

Set: PageAngleToleranceRadians(self: File3dmSettings) = value
"""

    PageRelativeTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the page space relative tolerance.

Get: PageRelativeTolerance(self: File3dmSettings) -> float

Set: PageRelativeTolerance(self: File3dmSettings) = value
"""

    PageUnitSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the page unit system, using Rhino.UnitSystem enumeration.

Get: PageUnitSystem(self: File3dmSettings) -> UnitSystem

Set: PageUnitSystem(self: File3dmSettings) = value
"""



class File3dmTypeCodes(object):
    """
    Typecode format 4 bytes long
                
                x xxxxxxxxxxxxxxx,x xxx xxxx xxxx x x xx
                | |               | |               | |  |
                |        |        |                 |
                |        |        |         |       +---  "stuff" bit
                |        |        |         |
                |        |        |         +-- specific codes
                |        |        |
                |        |        +-- RESERVED - DO NOT USE (should be 0) (will be used to control CRC on/off)
                |        |
                |        +-- category:_000 0000 0000 0001  Legacy geometry    TCODE_LEGACY_GEOMETRY
                |                     _000 0000 0000 0010  openNURBS object   TCODE_OPENNURBS_OBJECT
                |                     _000 0000 0000 0100  -- RESERVED - DO NOT USE (should be 0 in any typecode) -- 
                |                     _000 0000 0000 1000  -- RESERVED - DO NOT USE (should be 0 in any typecode) --                     
                |                     _000 0000 0001 0000  Geometry           TCODE_GEOMETRY
                |                     _000 0000 0010 0000  Annotation
                |                     _000 0000 0100 0000  Display Attributes TCODE_DISPLAY
                |                     _000 0000 1000 0000  Rendering          TCODE_RENDER     
                |                     _000 0001 0000 0000                         
                |                     _000 0010 0000 0000  Interface          TCODE_INTERFACE 
                |                     _000 0100 0000 0000  -- RESERVED - DO NOT USE (should be 0 in any typecode) --
                |                     _000 1000 0000 0000  Tolerances         TCODE_TOLERANCE
                |                     _001 0000 0000 0000  Tables             TCODE_TABLE    
                |                     _010 0000 0000 0000  Table record       TCODE_TABLEREC
                |                     _100 0000 0000 0000  User information   TCODE_USER
                | 
                +-- format: 0 - data size in header  - data block follows    TCODE_SHORT
                            1 - data in header - no data block follows
    """
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
    """
    Options used by File3dm.Write
    
    File3dmWriteOptions()
    """
    SaveAnalysisMeshes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Include analysis meshes in the file. Default is true

Get: SaveAnalysisMeshes(self: File3dmWriteOptions) -> bool

Set: SaveAnalysisMeshes(self: File3dmWriteOptions) = value
"""

    SaveRenderMeshes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Include Render meshes in the file. Default is true

Get: SaveRenderMeshes(self: File3dmWriteOptions) -> bool

Set: SaveRenderMeshes(self: File3dmWriteOptions) = value
"""

    SaveUserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Include custom user data in the file. Default is true

Get: SaveUserData(self: File3dmWriteOptions) -> bool

Set: SaveUserData(self: File3dmWriteOptions) = value
"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """File version. Default is 5

Get: Version(self: File3dmWriteOptions) -> int

Set: Version(self: File3dmWriteOptions) = value
"""



class FileReadOptions(object, IDisposable):
    """ FileReadOptions() """
    def Dispose(self):
        """ Dispose(self: FileReadOptions) """
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

    BatchMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true means you cannot ask questions during reading. (no dialogs, no "getters", etc.)

Get: BatchMode(self: FileReadOptions) -> bool

Set: BatchMode(self: FileReadOptions) = value
"""

    ImportMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true means we are merging whatever is being read into an existing document.
             This means you need to consider things like:
            
            If the information being read is in a different unit system, it should be
            scaled if UseScaleGeometry is true.
            
            There can be existing layers, fonts, materials, dimension styles, hatch
            patterns, and so on with the same name as items being read from the file.

Get: ImportMode(self: FileReadOptions) -> bool

Set: ImportMode(self: FileReadOptions) = value
"""

    ImportReferenceMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true means we are reading information for a work session reference model
            or a linked instance definition.

Get: ImportReferenceMode(self: FileReadOptions) -> bool

Set: ImportReferenceMode(self: FileReadOptions) = value
"""

    InsertMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true means we are reading information that will be used to create an
            instance definition or some other type of "inserting" that is supported
            by Rhino's "Insert" command.

Get: InsertMode(self: FileReadOptions) -> bool

Set: InsertMode(self: FileReadOptions) = value
"""

    NewMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true means we are reading template information in something like
            a OnFileNew event.

Get: NewMode(self: FileReadOptions) -> bool

Set: NewMode(self: FileReadOptions) = value
"""

    OpenMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true means we are reading the information into an empty document.  This
            means you need to consider things like:
            Setting the unit system (if the file has a unit system)Creating a default layer if one is not there.Setting up appropriate views when you're finished reading.

Get: OpenMode(self: FileReadOptions) -> bool

Set: OpenMode(self: FileReadOptions) = value
"""

    ScaleGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true: If ImportMode is true and the geometry in the file being read has
            a unit system different from the model's unit system, then apply the unit
            conversion scale to the file's geometry before adding it to the model.
            
            false: Do not scale. Once case where this happens is when an instance
            definition is read from a file and the model space instance references
            have been scaled. In case the instance definition geometry cannot be
            scaled or the net result is that the size of the instance reference
            object is scaled by the square of the scale factor.

Get: ScaleGeometry(self: FileReadOptions) -> bool

Set: ScaleGeometry(self: FileReadOptions) = value
"""

    UseScaleGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If this parameter is true, then no questions are asked when unit conversion
            scaling is optional and the setting specified by ScaleGeometry is used.

Get: UseScaleGeometry(self: FileReadOptions) -> bool

Set: UseScaleGeometry(self: FileReadOptions) = value
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



class FileWriteOptions(object, IDisposable):
    """ FileWriteOptions() """
    def Dispose(self):
        """ Dispose(self: FileWriteOptions) """
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

    ApplyTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyTransform(self: FileWriteOptions) -> bool

Set: ApplyTransform(self: FileWriteOptions) = value
"""

    FileVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileVersion(self: FileWriteOptions) -> int

Set: FileVersion(self: FileWriteOptions) = value
"""

    IncludeBitmapTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeBitmapTable(self: FileWriteOptions) -> bool

Set: IncludeBitmapTable(self: FileWriteOptions) = value
"""

    IncludeHistory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeHistory(self: FileWriteOptions) -> bool

Set: IncludeHistory(self: FileWriteOptions) = value
"""

    IncludePreviewImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludePreviewImage(self: FileWriteOptions) -> bool

Set: IncludePreviewImage(self: FileWriteOptions) = value
"""

    IncludeRenderMeshes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeRenderMeshes(self: FileWriteOptions) -> bool

Set: IncludeRenderMeshes(self: FileWriteOptions) = value
"""

    SuppressDialogBoxes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuppressDialogBoxes(self: FileWriteOptions) -> bool

Set: SuppressDialogBoxes(self: FileWriteOptions) = value
"""

    WriteAsTemplate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WriteAsTemplate(self: FileWriteOptions) -> bool

Set: WriteAsTemplate(self: FileWriteOptions) = value
"""

    WriteGeometryOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WriteGeometryOnly(self: FileWriteOptions) -> bool

Set: WriteGeometryOnly(self: FileWriteOptions) = value
"""

    WriteSelectedObjectsOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WriteSelectedObjectsOnly(self: FileWriteOptions) -> bool

Set: WriteSelectedObjectsOnly(self: FileWriteOptions) = value
"""

    WriteUserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WriteUserData(self: FileWriteOptions) -> bool

Set: WriteUserData(self: FileWriteOptions) = value
"""

    Xform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Xform(self: FileWriteOptions) -> Transform

Set: Xform(self: FileWriteOptions) = value
"""



class SerializationOptions(object):
    """
    Contains options for serializing -or storing- data,
                such as Rhino version and user data.
    
    SerializationOptions()
    """
    RhinoVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating the Rhino version.

Get: RhinoVersion(self: SerializationOptions) -> int

Set: RhinoVersion(self: SerializationOptions) = value
"""

    WriteUserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to write user data.

Get: WriteUserData(self: SerializationOptions) -> bool

Set: WriteUserData(self: SerializationOptions) = value
"""



class TextLog(object, IDisposable):
    """
    Used for collecting text data
    
    TextLog()
    TextLog(filename: str)
    """
    def Dispose(self):
        """
        Dispose(self: TextLog)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def PopIndent(self):
        """
        PopIndent(self: TextLog)
            Decrease the indentation level
        """
        pass

    def Print(self, *__args):
        """
        Print(self: TextLog, format: str, arg0: object, arg1: object)
            Send formatted text to the textlog
        Print(self: TextLog, format: str, arg0: object)
            Send formatted text to the textlog
        Print(self: TextLog, text: str)
            Send text to the textlog
        """
        pass

    def PrintWrappedText(self, text, lineLength):
        """
        PrintWrappedText(self: TextLog, text: str, lineLength: int)
            Send text wrapped at a set line length
        """
        pass

    def PushIndent(self):
        """
        PushIndent(self: TextLog)
            Increase the indentation level
        """
        pass

    def ToString(self):
        """
        ToString(self: TextLog) -> str
        
            If the TextLog was constructed using the empty constructor, then the text
                    
             information is stored in a runtime string.  The contents of this string
                    is 
             retrieved using ToString for this case
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
    """0: one tab per indent. >0: number of spaces per indent

Get: IndentSize(self: TextLog) -> int

Set: IndentSize(self: TextLog) = value
"""



