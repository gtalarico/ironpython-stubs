# encoding: utf-8
# module System.IO calls itself IO
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BinaryReader(object):
    """
    BinaryReader(input: Stream)
    BinaryReader(input: Stream, encoding: Encoding)
    BinaryReader(input: Stream, encoding: Encoding, leaveOpen: bool)
    """
    def Close(self):
        """ Close(self: BinaryReader) """
        pass

    def Dispose(self):
        """ Dispose(self: BinaryReader) """
        pass

    def FillBuffer(self, *args): #cannot find CLR method
        """ FillBuffer(self: BinaryReader, numBytes: int) """
        pass

    def PeekChar(self):
        """ PeekChar(self: BinaryReader) -> int """
        pass

    def Read(self, buffer=None, index=None, count=None):
        """
        Read(self: BinaryReader, buffer: Array[Byte], index: int, count: int) -> int
        Read(self: BinaryReader, buffer: Array[Char], index: int, count: int) -> int
        Read(self: BinaryReader) -> int
        """
        pass

    def Read7BitEncodedInt(self, *args): #cannot find CLR method
        """ Read7BitEncodedInt(self: BinaryReader) -> int """
        pass

    def ReadBoolean(self):
        """ ReadBoolean(self: BinaryReader) -> bool """
        pass

    def ReadByte(self):
        """ ReadByte(self: BinaryReader) -> Byte """
        pass

    def ReadBytes(self, count):
        """ ReadBytes(self: BinaryReader, count: int) -> Array[Byte] """
        pass

    def ReadChar(self):
        """ ReadChar(self: BinaryReader) -> Char """
        pass

    def ReadChars(self, count):
        """ ReadChars(self: BinaryReader, count: int) -> Array[Char] """
        pass

    def ReadDecimal(self):
        """ ReadDecimal(self: BinaryReader) -> Decimal """
        pass

    def ReadDouble(self):
        """ ReadDouble(self: BinaryReader) -> float """
        pass

    def ReadInt16(self):
        """ ReadInt16(self: BinaryReader) -> Int16 """
        pass

    def ReadInt32(self):
        """ ReadInt32(self: BinaryReader) -> int """
        pass

    def ReadInt64(self):
        """ ReadInt64(self: BinaryReader) -> Int64 """
        pass

    def ReadSByte(self):
        """ ReadSByte(self: BinaryReader) -> SByte """
        pass

    def ReadSingle(self):
        """ ReadSingle(self: BinaryReader) -> Single """
        pass

    def ReadString(self):
        """ ReadString(self: BinaryReader) -> str """
        pass

    def ReadUInt16(self):
        """ ReadUInt16(self: BinaryReader) -> UInt16 """
        pass

    def ReadUInt32(self):
        """ ReadUInt32(self: BinaryReader) -> UInt32 """
        pass

    def ReadUInt64(self):
        """ ReadUInt64(self: BinaryReader) -> UInt64 """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, input, encoding=None, leaveOpen=None):
        """
        __new__(cls: type, input: Stream)
        __new__(cls: type, input: Stream, encoding: Encoding)
        __new__(cls: type, input: Stream, encoding: Encoding, leaveOpen: bool)
        """
        pass

    BaseStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseStream(self: BinaryReader) -> Stream

"""



class BinaryWriter(object):
    """
    BinaryWriter(output: Stream)
    BinaryWriter(output: Stream, encoding: Encoding)
    BinaryWriter(output: Stream, encoding: Encoding, leaveOpen: bool)
    """
    def Close(self):
        """ Close(self: BinaryWriter) """
        pass

    def Dispose(self):
        """ Dispose(self: BinaryWriter) """
        pass

    def Flush(self):
        """ Flush(self: BinaryWriter) """
        pass

    def Seek(self, offset, origin):
        """ Seek(self: BinaryWriter, offset: int, origin: SeekOrigin) -> Int64 """
        pass

    def Write(self, *__args):
        """ Write(self: BinaryWriter, value: UInt16)Write(self: BinaryWriter, value: int)Write(self: BinaryWriter, value: Decimal)Write(self: BinaryWriter, value: Int16)Write(self: BinaryWriter, value: UInt32)Write(self: BinaryWriter, value: Single)Write(self: BinaryWriter, value: str)Write(self: BinaryWriter, value: Int64)Write(self: BinaryWriter, value: UInt64)Write(self: BinaryWriter, value: SByte)Write(self: BinaryWriter, buffer: Array[Byte])Write(self: BinaryWriter, value: bool)Write(self: BinaryWriter, value: Byte)Write(self: BinaryWriter, buffer: Array[Byte], index: int, count: int)Write(self: BinaryWriter, chars: Array[Char], index: int, count: int)Write(self: BinaryWriter, value: float)Write(self: BinaryWriter, ch: Char)Write(self: BinaryWriter, chars: Array[Char]) """
        pass

    def Write7BitEncodedInt(self, *args): #cannot find CLR method
        """ Write7BitEncodedInt(self: BinaryWriter, value: int) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, output, encoding=None, leaveOpen=None):
        """
        __new__(cls: type)
        __new__(cls: type, output: Stream)
        __new__(cls: type, output: Stream, encoding: Encoding)
        __new__(cls: type, output: Stream, encoding: Encoding, leaveOpen: bool)
        """
        pass

    BaseStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseStream(self: BinaryWriter) -> Stream

"""


    Null = None
    OutStream = None


class Stream(MarshalByRefObject):
    # no doc
    def BeginRead(self, buffer, offset, count, callback, state):
        """ BeginRead(self: Stream, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult """
        pass

    def BeginWrite(self, buffer, offset, count, callback, state):
        """ BeginWrite(self: Stream, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult """
        pass

    def Close(self):
        """ Close(self: Stream) """
        pass

    def CopyTo(self, destination, bufferSize=None):
        """ CopyTo(self: Stream, destination: Stream, bufferSize: int)CopyTo(self: Stream, destination: Stream) """
        pass

    def CopyToAsync(self, destination, bufferSize=None, cancellationToken=None):
        """
        CopyToAsync(self: Stream, destination: Stream, bufferSize: int, cancellationToken: CancellationToken) -> Task
        CopyToAsync(self: Stream, destination: Stream, bufferSize: int) -> Task
        CopyToAsync(self: Stream, destination: Stream) -> Task
        """
        pass

    def CreateWaitHandle(self, *args): #cannot find CLR method
        """ CreateWaitHandle(self: Stream) -> WaitHandle """
        pass

    def Dispose(self):
        """ Dispose(self: Stream) """
        pass

    def EndRead(self, asyncResult):
        """ EndRead(self: Stream, asyncResult: IAsyncResult) -> int """
        pass

    def EndWrite(self, asyncResult):
        """ EndWrite(self: Stream, asyncResult: IAsyncResult) """
        pass

    def Flush(self):
        """ Flush(self: Stream) """
        pass

    def FlushAsync(self, cancellationToken=None):
        """
        FlushAsync(self: Stream, cancellationToken: CancellationToken) -> Task
        FlushAsync(self: Stream) -> Task
        """
        pass

    def ObjectInvariant(self, *args): #cannot find CLR method
        """ ObjectInvariant(self: Stream) """
        pass

    def Read(self, buffer, offset, count):
        """ Read(self: Stream, offset: int, count: int) -> (int, Array[Byte]) """
        pass

    def ReadAsync(self, buffer, offset, count, cancellationToken=None):
        """
        ReadAsync(self: Stream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task[int]
        ReadAsync(self: Stream, buffer: Array[Byte], offset: int, count: int) -> Task[int]
        """
        pass

    def ReadByte(self):
        """ ReadByte(self: Stream) -> int """
        pass

    def Seek(self, offset, origin):
        """ Seek(self: Stream, offset: Int64, origin: SeekOrigin) -> Int64 """
        pass

    def SetLength(self, value):
        """ SetLength(self: Stream, value: Int64) """
        pass

    @staticmethod
    def Synchronized(stream):
        """ Synchronized(stream: Stream) -> Stream """
        pass

    def Write(self, buffer, offset, count):
        """ Write(self: Stream, buffer: Array[Byte], offset: int, count: int) """
        pass

    def WriteAsync(self, buffer, offset, count, cancellationToken=None):
        """
        WriteAsync(self: Stream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task
        WriteAsync(self: Stream, buffer: Array[Byte], offset: int, count: int) -> Task
        """
        pass

    def WriteByte(self, value):
        """ WriteByte(self: Stream, value: Byte) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanRead(self: Stream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanSeek(self: Stream) -> bool

"""

    CanTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanTimeout(self: Stream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanWrite(self: Stream) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Stream) -> Int64

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: Stream) -> Int64

Set: Position(self: Stream) = value
"""

    ReadTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadTimeout(self: Stream) -> int

Set: ReadTimeout(self: Stream) = value
"""

    WriteTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WriteTimeout(self: Stream) -> int

Set: WriteTimeout(self: Stream) = value
"""


    Null = None


class BufferedStream(Stream):
    """
    BufferedStream(stream: Stream)
    BufferedStream(stream: Stream, bufferSize: int)
    """
    def BeginRead(self, buffer, offset, count, callback, state):
        """ BeginRead(self: BufferedStream, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult """
        pass

    def BeginWrite(self, buffer, offset, count, callback, state):
        """ BeginWrite(self: BufferedStream, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult """
        pass

    def Dispose(self):
        """ Dispose(self: BufferedStream, disposing: bool) """
        pass

    def EndRead(self, asyncResult):
        """ EndRead(self: BufferedStream, asyncResult: IAsyncResult) -> int """
        pass

    def EndWrite(self, asyncResult):
        """ EndWrite(self: BufferedStream, asyncResult: IAsyncResult) """
        pass

    def Flush(self):
        """ Flush(self: BufferedStream) """
        pass

    def FlushAsync(self, cancellationToken=None):
        """ FlushAsync(self: BufferedStream, cancellationToken: CancellationToken) -> Task """
        pass

    def Read(self, array, offset, count):
        """ Read(self: BufferedStream, offset: int, count: int) -> (int, Array[Byte]) """
        pass

    def ReadAsync(self, buffer, offset, count, cancellationToken=None):
        """ ReadAsync(self: BufferedStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task[int] """
        pass

    def ReadByte(self):
        """ ReadByte(self: BufferedStream) -> int """
        pass

    def Seek(self, offset, origin):
        """ Seek(self: BufferedStream, offset: Int64, origin: SeekOrigin) -> Int64 """
        pass

    def SetLength(self, value):
        """ SetLength(self: BufferedStream, value: Int64) """
        pass

    def Write(self, array, offset, count):
        """ Write(self: BufferedStream, array: Array[Byte], offset: int, count: int) """
        pass

    def WriteAsync(self, buffer, offset, count, cancellationToken=None):
        """ WriteAsync(self: BufferedStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task """
        pass

    def WriteByte(self, value):
        """ WriteByte(self: BufferedStream, value: Byte) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stream, bufferSize=None):
        """
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, bufferSize: int)
        """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanRead(self: BufferedStream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanSeek(self: BufferedStream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanWrite(self: BufferedStream) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: BufferedStream) -> Int64

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: BufferedStream) -> Int64

Set: Position(self: BufferedStream) = value
"""



class Directory(object):
    # no doc
    @staticmethod
    def CreateDirectory(path, directorySecurity=None):
        """
        CreateDirectory(path: str, directorySecurity: DirectorySecurity) -> DirectoryInfo
        CreateDirectory(path: str) -> DirectoryInfo
        """
        pass

    @staticmethod
    def Delete(path, recursive=None):
        """ Delete(path: str, recursive: bool)Delete(path: str) """
        pass

    @staticmethod
    def EnumerateDirectories(path, searchPattern=None, searchOption=None):
        """
        EnumerateDirectories(path: str, searchPattern: str, searchOption: SearchOption) -> IEnumerable[str]
        EnumerateDirectories(path: str, searchPattern: str) -> IEnumerable[str]
        EnumerateDirectories(path: str) -> IEnumerable[str]
        """
        pass

    @staticmethod
    def EnumerateFiles(path, searchPattern=None, searchOption=None):
        """
        EnumerateFiles(path: str, searchPattern: str, searchOption: SearchOption) -> IEnumerable[str]
        EnumerateFiles(path: str, searchPattern: str) -> IEnumerable[str]
        EnumerateFiles(path: str) -> IEnumerable[str]
        """
        pass

    @staticmethod
    def EnumerateFileSystemEntries(path, searchPattern=None, searchOption=None):
        """
        EnumerateFileSystemEntries(path: str, searchPattern: str, searchOption: SearchOption) -> IEnumerable[str]
        EnumerateFileSystemEntries(path: str, searchPattern: str) -> IEnumerable[str]
        EnumerateFileSystemEntries(path: str) -> IEnumerable[str]
        """
        pass

    @staticmethod
    def Exists(path):
        """ Exists(path: str) -> bool """
        pass

    @staticmethod
    def GetAccessControl(path, includeSections=None):
        """
        GetAccessControl(path: str, includeSections: AccessControlSections) -> DirectorySecurity
        GetAccessControl(path: str) -> DirectorySecurity
        """
        pass

    @staticmethod
    def GetCreationTime(path):
        """ GetCreationTime(path: str) -> DateTime """
        pass

    @staticmethod
    def GetCreationTimeUtc(path):
        """ GetCreationTimeUtc(path: str) -> DateTime """
        pass

    @staticmethod
    def GetCurrentDirectory():
        """ GetCurrentDirectory() -> str """
        pass

    @staticmethod
    def GetDirectories(path, searchPattern=None, searchOption=None):
        """
        GetDirectories(path: str, searchPattern: str, searchOption: SearchOption) -> Array[str]
        GetDirectories(path: str, searchPattern: str) -> Array[str]
        GetDirectories(path: str) -> Array[str]
        """
        pass

    @staticmethod
    def GetDirectoryRoot(path):
        """ GetDirectoryRoot(path: str) -> str """
        pass

    @staticmethod
    def GetFiles(path, searchPattern=None, searchOption=None):
        """
        GetFiles(path: str, searchPattern: str, searchOption: SearchOption) -> Array[str]
        GetFiles(path: str, searchPattern: str) -> Array[str]
        GetFiles(path: str) -> Array[str]
        """
        pass

    @staticmethod
    def GetFileSystemEntries(path, searchPattern=None, searchOption=None):
        """
        GetFileSystemEntries(path: str, searchPattern: str, searchOption: SearchOption) -> Array[str]
        GetFileSystemEntries(path: str, searchPattern: str) -> Array[str]
        GetFileSystemEntries(path: str) -> Array[str]
        """
        pass

    @staticmethod
    def GetLastAccessTime(path):
        """ GetLastAccessTime(path: str) -> DateTime """
        pass

    @staticmethod
    def GetLastAccessTimeUtc(path):
        """ GetLastAccessTimeUtc(path: str) -> DateTime """
        pass

    @staticmethod
    def GetLastWriteTime(path):
        """ GetLastWriteTime(path: str) -> DateTime """
        pass

    @staticmethod
    def GetLastWriteTimeUtc(path):
        """ GetLastWriteTimeUtc(path: str) -> DateTime """
        pass

    @staticmethod
    def GetLogicalDrives():
        """ GetLogicalDrives() -> Array[str] """
        pass

    @staticmethod
    def GetParent(path):
        """ GetParent(path: str) -> DirectoryInfo """
        pass

    @staticmethod
    def Move(sourceDirName, destDirName):
        """ Move(sourceDirName: str, destDirName: str) """
        pass

    @staticmethod
    def SetAccessControl(path, directorySecurity):
        """ SetAccessControl(path: str, directorySecurity: DirectorySecurity) """
        pass

    @staticmethod
    def SetCreationTime(path, creationTime):
        """ SetCreationTime(path: str, creationTime: DateTime) """
        pass

    @staticmethod
    def SetCreationTimeUtc(path, creationTimeUtc):
        """ SetCreationTimeUtc(path: str, creationTimeUtc: DateTime) """
        pass

    @staticmethod
    def SetCurrentDirectory(path):
        """ SetCurrentDirectory(path: str) """
        pass

    @staticmethod
    def SetLastAccessTime(path, lastAccessTime):
        """ SetLastAccessTime(path: str, lastAccessTime: DateTime) """
        pass

    @staticmethod
    def SetLastAccessTimeUtc(path, lastAccessTimeUtc):
        """ SetLastAccessTimeUtc(path: str, lastAccessTimeUtc: DateTime) """
        pass

    @staticmethod
    def SetLastWriteTime(path, lastWriteTime):
        """ SetLastWriteTime(path: str, lastWriteTime: DateTime) """
        pass

    @staticmethod
    def SetLastWriteTimeUtc(path, lastWriteTimeUtc):
        """ SetLastWriteTimeUtc(path: str, lastWriteTimeUtc: DateTime) """
        pass

    __all__ = [
        'CreateDirectory',
        'Delete',
        'EnumerateDirectories',
        'EnumerateFiles',
        'EnumerateFileSystemEntries',
        'Exists',
        'GetAccessControl',
        'GetCreationTime',
        'GetCreationTimeUtc',
        'GetCurrentDirectory',
        'GetDirectories',
        'GetDirectoryRoot',
        'GetFiles',
        'GetFileSystemEntries',
        'GetLastAccessTime',
        'GetLastAccessTimeUtc',
        'GetLastWriteTime',
        'GetLastWriteTimeUtc',
        'GetLogicalDrives',
        'GetParent',
        'Move',
        'SetAccessControl',
        'SetCreationTime',
        'SetCreationTimeUtc',
        'SetCurrentDirectory',
        'SetLastAccessTime',
        'SetLastAccessTimeUtc',
        'SetLastWriteTime',
        'SetLastWriteTimeUtc',
    ]


class FileSystemInfo(MarshalByRefObject):
    # no doc
    def Delete(self):
        """ Delete(self: FileSystemInfo) """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: FileSystemInfo, info: SerializationInfo, context: StreamingContext) """
        pass

    def Refresh(self):
        """ Refresh(self: FileSystemInfo) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: FileSystemInfo) -> FileAttributes

Set: Attributes(self: FileSystemInfo) = value
"""

    CreationTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreationTime(self: FileSystemInfo) -> DateTime

Set: CreationTime(self: FileSystemInfo) = value
"""

    CreationTimeUtc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreationTimeUtc(self: FileSystemInfo) -> DateTime

Set: CreationTimeUtc(self: FileSystemInfo) = value
"""

    Exists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exists(self: FileSystemInfo) -> bool

"""

    Extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Extension(self: FileSystemInfo) -> str

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: FileSystemInfo) -> str

"""

    LastAccessTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastAccessTime(self: FileSystemInfo) -> DateTime

Set: LastAccessTime(self: FileSystemInfo) = value
"""

    LastAccessTimeUtc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastAccessTimeUtc(self: FileSystemInfo) -> DateTime

Set: LastAccessTimeUtc(self: FileSystemInfo) = value
"""

    LastWriteTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastWriteTime(self: FileSystemInfo) -> DateTime

Set: LastWriteTime(self: FileSystemInfo) = value
"""

    LastWriteTimeUtc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastWriteTimeUtc(self: FileSystemInfo) -> DateTime

Set: LastWriteTimeUtc(self: FileSystemInfo) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: FileSystemInfo) -> str

"""


    FullPath = None
    OriginalPath = None


class DirectoryInfo(FileSystemInfo):
    """ DirectoryInfo(path: str) """
    def Create(self, directorySecurity=None):
        """ Create(self: DirectoryInfo, directorySecurity: DirectorySecurity)Create(self: DirectoryInfo) """
        pass

    def CreateSubdirectory(self, path, directorySecurity=None):
        """
        CreateSubdirectory(self: DirectoryInfo, path: str, directorySecurity: DirectorySecurity) -> DirectoryInfo
        CreateSubdirectory(self: DirectoryInfo, path: str) -> DirectoryInfo
        """
        pass

    def Delete(self, recursive=None):
        """ Delete(self: DirectoryInfo, recursive: bool)Delete(self: DirectoryInfo) """
        pass

    def EnumerateDirectories(self, searchPattern=None, searchOption=None):
        """
        EnumerateDirectories(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> IEnumerable[DirectoryInfo]
        EnumerateDirectories(self: DirectoryInfo, searchPattern: str) -> IEnumerable[DirectoryInfo]
        EnumerateDirectories(self: DirectoryInfo) -> IEnumerable[DirectoryInfo]
        """
        pass

    def EnumerateFiles(self, searchPattern=None, searchOption=None):
        """
        EnumerateFiles(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> IEnumerable[FileInfo]
        EnumerateFiles(self: DirectoryInfo, searchPattern: str) -> IEnumerable[FileInfo]
        EnumerateFiles(self: DirectoryInfo) -> IEnumerable[FileInfo]
        """
        pass

    def EnumerateFileSystemInfos(self, searchPattern=None, searchOption=None):
        """
        EnumerateFileSystemInfos(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> IEnumerable[FileSystemInfo]
        EnumerateFileSystemInfos(self: DirectoryInfo, searchPattern: str) -> IEnumerable[FileSystemInfo]
        EnumerateFileSystemInfos(self: DirectoryInfo) -> IEnumerable[FileSystemInfo]
        """
        pass

    def GetAccessControl(self, includeSections=None):
        """
        GetAccessControl(self: DirectoryInfo, includeSections: AccessControlSections) -> DirectorySecurity
        GetAccessControl(self: DirectoryInfo) -> DirectorySecurity
        """
        pass

    def GetDirectories(self, searchPattern=None, searchOption=None):
        """
        GetDirectories(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> Array[DirectoryInfo]
        GetDirectories(self: DirectoryInfo, searchPattern: str) -> Array[DirectoryInfo]
        GetDirectories(self: DirectoryInfo) -> Array[DirectoryInfo]
        """
        pass

    def GetFiles(self, searchPattern=None, searchOption=None):
        """
        GetFiles(self: DirectoryInfo) -> Array[FileInfo]
        GetFiles(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> Array[FileInfo]
        GetFiles(self: DirectoryInfo, searchPattern: str) -> Array[FileInfo]
        """
        pass

    def GetFileSystemInfos(self, searchPattern=None, searchOption=None):
        """
        GetFileSystemInfos(self: DirectoryInfo) -> Array[FileSystemInfo]
        GetFileSystemInfos(self: DirectoryInfo, searchPattern: str, searchOption: SearchOption) -> Array[FileSystemInfo]
        GetFileSystemInfos(self: DirectoryInfo, searchPattern: str) -> Array[FileSystemInfo]
        """
        pass

    def MoveTo(self, destDirName):
        """ MoveTo(self: DirectoryInfo, destDirName: str) """
        pass

    def SetAccessControl(self, directorySecurity):
        """ SetAccessControl(self: DirectoryInfo, directorySecurity: DirectorySecurity) """
        pass

    def ToString(self):
        """ ToString(self: DirectoryInfo) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, path):
        """ __new__(cls: type, path: str) """
        pass

    Exists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exists(self: DirectoryInfo) -> bool

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: DirectoryInfo) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: DirectoryInfo) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: DirectoryInfo) -> DirectoryInfo

"""

    Root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Root(self: DirectoryInfo) -> DirectoryInfo

"""


    FullPath = None
    OriginalPath = None


class IOException(SystemException):
    """
    IOException()
    IOException(message: str)
    IOException(message: str, hresult: int)
    IOException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, hresult: int)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class DirectoryNotFoundException(IOException):
    """
    DirectoryNotFoundException()
    DirectoryNotFoundException(message: str)
    DirectoryNotFoundException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class DriveInfo(object):
    """ DriveInfo(driveName: str) """
    @staticmethod
    def GetDrives():
        """ GetDrives() -> Array[DriveInfo] """
        pass

    def ToString(self):
        """ ToString(self: DriveInfo) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, driveName):
        """ __new__(cls: type, driveName: str) """
        pass

    AvailableFreeSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AvailableFreeSpace(self: DriveInfo) -> Int64

"""

    DriveFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DriveFormat(self: DriveInfo) -> str

"""

    DriveType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DriveType(self: DriveInfo) -> DriveType

"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReady(self: DriveInfo) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: DriveInfo) -> str

"""

    RootDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RootDirectory(self: DriveInfo) -> DirectoryInfo

"""

    TotalFreeSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalFreeSpace(self: DriveInfo) -> Int64

"""

    TotalSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalSize(self: DriveInfo) -> Int64

"""

    VolumeLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VolumeLabel(self: DriveInfo) -> str

Set: VolumeLabel(self: DriveInfo) = value
"""



class DriveNotFoundException(IOException):
    """
    DriveNotFoundException()
    DriveNotFoundException(message: str)
    DriveNotFoundException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class DriveType(Enum):
    """ enum DriveType, values: CDRom (5), Fixed (3), Network (4), NoRootDirectory (1), Ram (6), Removable (2), Unknown (0) """
    CDRom = None
    Fixed = None
    Network = None
    NoRootDirectory = None
    Ram = None
    Removable = None
    Unknown = None
    value__ = None


class EndOfStreamException(IOException):
    """
    EndOfStreamException()
    EndOfStreamException(message: str)
    EndOfStreamException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class ErrorEventArgs(EventArgs):
    """ ErrorEventArgs(exception: Exception) """
    def GetException(self):
        """ GetException(self: ErrorEventArgs) -> Exception """
        pass

    @staticmethod # known case of __new__
    def __new__(self, exception):
        """ __new__(cls: type, exception: Exception) """
        pass


class ErrorEventHandler(MulticastDelegate):
    """ ErrorEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ErrorEventHandler, sender: object, e: ErrorEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ErrorEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ErrorEventHandler, sender: object, e: ErrorEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class File(object):
    # no doc
    @staticmethod
    def AppendAllLines(path, contents, encoding=None):
        """ AppendAllLines(path: str, contents: IEnumerable[str], encoding: Encoding)AppendAllLines(path: str, contents: IEnumerable[str]) """
        pass

    @staticmethod
    def AppendAllText(path, contents, encoding=None):
        """ AppendAllText(path: str, contents: str, encoding: Encoding)AppendAllText(path: str, contents: str) """
        pass

    @staticmethod
    def AppendText(path):
        """ AppendText(path: str) -> StreamWriter """
        pass

    @staticmethod
    def Copy(sourceFileName, destFileName, overwrite=None):
        """ Copy(sourceFileName: str, destFileName: str, overwrite: bool)Copy(sourceFileName: str, destFileName: str) """
        pass

    @staticmethod
    def Create(path, bufferSize=None, options=None, fileSecurity=None):
        """
        Create(path: str, bufferSize: int, options: FileOptions) -> FileStream
        Create(path: str, bufferSize: int, options: FileOptions, fileSecurity: FileSecurity) -> FileStream
        Create(path: str) -> FileStream
        Create(path: str, bufferSize: int) -> FileStream
        """
        pass

    @staticmethod
    def CreateText(path):
        """ CreateText(path: str) -> StreamWriter """
        pass

    @staticmethod
    def Decrypt(path):
        """ Decrypt(path: str) """
        pass

    @staticmethod
    def Delete(path):
        """ Delete(path: str) """
        pass

    @staticmethod
    def Encrypt(path):
        """ Encrypt(path: str) """
        pass

    @staticmethod
    def Exists(path):
        """ Exists(path: str) -> bool """
        pass

    @staticmethod
    def GetAccessControl(path, includeSections=None):
        """
        GetAccessControl(path: str, includeSections: AccessControlSections) -> FileSecurity
        GetAccessControl(path: str) -> FileSecurity
        """
        pass

    @staticmethod
    def GetAttributes(path):
        """ GetAttributes(path: str) -> FileAttributes """
        pass

    @staticmethod
    def GetCreationTime(path):
        """ GetCreationTime(path: str) -> DateTime """
        pass

    @staticmethod
    def GetCreationTimeUtc(path):
        """ GetCreationTimeUtc(path: str) -> DateTime """
        pass

    @staticmethod
    def GetLastAccessTime(path):
        """ GetLastAccessTime(path: str) -> DateTime """
        pass

    @staticmethod
    def GetLastAccessTimeUtc(path):
        """ GetLastAccessTimeUtc(path: str) -> DateTime """
        pass

    @staticmethod
    def GetLastWriteTime(path):
        """ GetLastWriteTime(path: str) -> DateTime """
        pass

    @staticmethod
    def GetLastWriteTimeUtc(path):
        """ GetLastWriteTimeUtc(path: str) -> DateTime """
        pass

    @staticmethod
    def Move(sourceFileName, destFileName):
        """ Move(sourceFileName: str, destFileName: str) """
        pass

    @staticmethod
    def Open(path, mode, access=None, share=None):
        """
        Open(path: str, mode: FileMode, access: FileAccess, share: FileShare) -> FileStream
        Open(path: str, mode: FileMode, access: FileAccess) -> FileStream
        Open(path: str, mode: FileMode) -> FileStream
        """
        pass

    @staticmethod
    def OpenRead(path):
        """ OpenRead(path: str) -> FileStream """
        pass

    @staticmethod
    def OpenText(path):
        """ OpenText(path: str) -> StreamReader """
        pass

    @staticmethod
    def OpenWrite(path):
        """ OpenWrite(path: str) -> FileStream """
        pass

    @staticmethod
    def ReadAllBytes(path):
        """ ReadAllBytes(path: str) -> Array[Byte] """
        pass

    @staticmethod
    def ReadAllLines(path, encoding=None):
        """
        ReadAllLines(path: str, encoding: Encoding) -> Array[str]
        ReadAllLines(path: str) -> Array[str]
        """
        pass

    @staticmethod
    def ReadAllText(path, encoding=None):
        """
        ReadAllText(path: str, encoding: Encoding) -> str
        ReadAllText(path: str) -> str
        """
        pass

    @staticmethod
    def ReadLines(path, encoding=None):
        """
        ReadLines(path: str, encoding: Encoding) -> IEnumerable[str]
        ReadLines(path: str) -> IEnumerable[str]
        """
        pass

    @staticmethod
    def Replace(sourceFileName, destinationFileName, destinationBackupFileName, ignoreMetadataErrors=None):
        """ Replace(sourceFileName: str, destinationFileName: str, destinationBackupFileName: str, ignoreMetadataErrors: bool)Replace(sourceFileName: str, destinationFileName: str, destinationBackupFileName: str) """
        pass

    @staticmethod
    def SetAccessControl(path, fileSecurity):
        """ SetAccessControl(path: str, fileSecurity: FileSecurity) """
        pass

    @staticmethod
    def SetAttributes(path, fileAttributes):
        """ SetAttributes(path: str, fileAttributes: FileAttributes) """
        pass

    @staticmethod
    def SetCreationTime(path, creationTime):
        """ SetCreationTime(path: str, creationTime: DateTime) """
        pass

    @staticmethod
    def SetCreationTimeUtc(path, creationTimeUtc):
        """ SetCreationTimeUtc(path: str, creationTimeUtc: DateTime) """
        pass

    @staticmethod
    def SetLastAccessTime(path, lastAccessTime):
        """ SetLastAccessTime(path: str, lastAccessTime: DateTime) """
        pass

    @staticmethod
    def SetLastAccessTimeUtc(path, lastAccessTimeUtc):
        """ SetLastAccessTimeUtc(path: str, lastAccessTimeUtc: DateTime) """
        pass

    @staticmethod
    def SetLastWriteTime(path, lastWriteTime):
        """ SetLastWriteTime(path: str, lastWriteTime: DateTime) """
        pass

    @staticmethod
    def SetLastWriteTimeUtc(path, lastWriteTimeUtc):
        """ SetLastWriteTimeUtc(path: str, lastWriteTimeUtc: DateTime) """
        pass

    @staticmethod
    def WriteAllBytes(path, bytes):
        """ WriteAllBytes(path: str, bytes: Array[Byte]) """
        pass

    @staticmethod
    def WriteAllLines(path, contents, encoding=None):
        """ WriteAllLines(path: str, contents: IEnumerable[str])WriteAllLines(path: str, contents: IEnumerable[str], encoding: Encoding)WriteAllLines(path: str, contents: Array[str])WriteAllLines(path: str, contents: Array[str], encoding: Encoding) """
        pass

    @staticmethod
    def WriteAllText(path, contents, encoding=None):
        """ WriteAllText(path: str, contents: str, encoding: Encoding)WriteAllText(path: str, contents: str) """
        pass

    __all__ = [
        'AppendAllLines',
        'AppendAllText',
        'AppendText',
        'Copy',
        'Create',
        'CreateText',
        'Decrypt',
        'Delete',
        'Encrypt',
        'Exists',
        'GetAccessControl',
        'GetAttributes',
        'GetCreationTime',
        'GetCreationTimeUtc',
        'GetLastAccessTime',
        'GetLastAccessTimeUtc',
        'GetLastWriteTime',
        'GetLastWriteTimeUtc',
        'Move',
        'Open',
        'OpenRead',
        'OpenText',
        'OpenWrite',
        'ReadAllBytes',
        'ReadAllLines',
        'ReadAllText',
        'ReadLines',
        'Replace',
        'SetAccessControl',
        'SetAttributes',
        'SetCreationTime',
        'SetCreationTimeUtc',
        'SetLastAccessTime',
        'SetLastAccessTimeUtc',
        'SetLastWriteTime',
        'SetLastWriteTimeUtc',
        'WriteAllBytes',
        'WriteAllLines',
        'WriteAllText',
    ]


class FileAccess(Enum):
    """ enum (flags) FileAccess, values: Read (1), ReadWrite (3), Write (2) """
    Read = None
    ReadWrite = None
    value__ = None
    Write = None


class FileAttributes(Enum):
    """ enum (flags) FileAttributes, values: Archive (32), Compressed (2048), Device (64), Directory (16), Encrypted (16384), Hidden (2), IntegrityStream (32768), Normal (128), NoScrubData (131072), NotContentIndexed (8192), Offline (4096), ReadOnly (1), ReparsePoint (1024), SparseFile (512), System (4), Temporary (256) """
    Archive = None
    Compressed = None
    Device = None
    Directory = None
    Encrypted = None
    Hidden = None
    IntegrityStream = None
    Normal = None
    NoScrubData = None
    NotContentIndexed = None
    Offline = None
    ReadOnly = None
    ReparsePoint = None
    SparseFile = None
    System = None
    Temporary = None
    value__ = None


class FileInfo(FileSystemInfo):
    """ FileInfo(fileName: str) """
    def AppendText(self):
        """ AppendText(self: FileInfo) -> StreamWriter """
        pass

    def CopyTo(self, destFileName, overwrite=None):
        """
        CopyTo(self: FileInfo, destFileName: str, overwrite: bool) -> FileInfo
        CopyTo(self: FileInfo, destFileName: str) -> FileInfo
        """
        pass

    def Create(self):
        """ Create(self: FileInfo) -> FileStream """
        pass

    def CreateText(self):
        """ CreateText(self: FileInfo) -> StreamWriter """
        pass

    def Decrypt(self):
        """ Decrypt(self: FileInfo) """
        pass

    def Delete(self):
        """ Delete(self: FileInfo) """
        pass

    def Encrypt(self):
        """ Encrypt(self: FileInfo) """
        pass

    def GetAccessControl(self, includeSections=None):
        """
        GetAccessControl(self: FileInfo, includeSections: AccessControlSections) -> FileSecurity
        GetAccessControl(self: FileInfo) -> FileSecurity
        """
        pass

    def MoveTo(self, destFileName):
        """ MoveTo(self: FileInfo, destFileName: str) """
        pass

    def Open(self, mode, access=None, share=None):
        """
        Open(self: FileInfo, mode: FileMode, access: FileAccess, share: FileShare) -> FileStream
        Open(self: FileInfo, mode: FileMode, access: FileAccess) -> FileStream
        Open(self: FileInfo, mode: FileMode) -> FileStream
        """
        pass

    def OpenRead(self):
        """ OpenRead(self: FileInfo) -> FileStream """
        pass

    def OpenText(self):
        """ OpenText(self: FileInfo) -> StreamReader """
        pass

    def OpenWrite(self):
        """ OpenWrite(self: FileInfo) -> FileStream """
        pass

    def Replace(self, destinationFileName, destinationBackupFileName, ignoreMetadataErrors=None):
        """
        Replace(self: FileInfo, destinationFileName: str, destinationBackupFileName: str, ignoreMetadataErrors: bool) -> FileInfo
        Replace(self: FileInfo, destinationFileName: str, destinationBackupFileName: str) -> FileInfo
        """
        pass

    def SetAccessControl(self, fileSecurity):
        """ SetAccessControl(self: FileInfo, fileSecurity: FileSecurity) """
        pass

    def ToString(self):
        """ ToString(self: FileInfo) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fileName):
        """ __new__(cls: type, fileName: str) """
        pass

    Directory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Directory(self: FileInfo) -> DirectoryInfo

"""

    DirectoryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectoryName(self: FileInfo) -> str

"""

    Exists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exists(self: FileInfo) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: FileInfo) -> bool

Set: IsReadOnly(self: FileInfo) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: FileInfo) -> Int64

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: FileInfo) -> str

"""


    FullPath = None
    OriginalPath = None


class FileLoadException(IOException):
    """
    FileLoadException()
    FileLoadException(message: str)
    FileLoadException(message: str, inner: Exception)
    FileLoadException(message: str, fileName: str)
    FileLoadException(message: str, fileName: str, inner: Exception)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: FileLoadException, info: SerializationInfo, context: StreamingContext) """
        pass

    def ToString(self):
        """ ToString(self: FileLoadException) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, message: str, fileName: str)
        __new__(cls: type, message: str, fileName: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: FileLoadException) -> str

"""

    FusionLog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FusionLog(self: FileLoadException) -> str

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: FileLoadException) -> str

"""



class FileMode(Enum):
    """ enum FileMode, values: Append (6), Create (2), CreateNew (1), Open (3), OpenOrCreate (4), Truncate (5) """
    Append = None
    Create = None
    CreateNew = None
    Open = None
    OpenOrCreate = None
    Truncate = None
    value__ = None


class FileNotFoundException(IOException):
    """
    FileNotFoundException()
    FileNotFoundException(message: str)
    FileNotFoundException(message: str, innerException: Exception)
    FileNotFoundException(message: str, fileName: str)
    FileNotFoundException(message: str, fileName: str, innerException: Exception)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: FileNotFoundException, info: SerializationInfo, context: StreamingContext) """
        pass

    def ToString(self):
        """ ToString(self: FileNotFoundException) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, message: str, fileName: str)
        __new__(cls: type, message: str, fileName: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: FileNotFoundException) -> str

"""

    FusionLog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FusionLog(self: FileNotFoundException) -> str

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: FileNotFoundException) -> str

"""



class FileOptions(Enum):
    """ enum (flags) FileOptions, values: Asynchronous (1073741824), DeleteOnClose (67108864), Encrypted (16384), None (0), RandomAccess (268435456), SequentialScan (134217728), WriteThrough (-2147483648) """
    Asynchronous = None
    DeleteOnClose = None
    Encrypted = None
    None = None
    RandomAccess = None
    SequentialScan = None
    value__ = None
    WriteThrough = None


class FileShare(Enum):
    """ enum (flags) FileShare, values: Delete (4), Inheritable (16), None (0), Read (1), ReadWrite (3), Write (2) """
    Delete = None
    Inheritable = None
    None = None
    Read = None
    ReadWrite = None
    value__ = None
    Write = None


class FileStream(Stream):
    """
    FileStream(path: str, mode: FileMode)
    FileStream(path: str, mode: FileMode, access: FileAccess)
    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare)
    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int)
    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, options: FileOptions)
    FileStream(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, useAsync: bool)
    FileStream(path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions, fileSecurity: FileSecurity)
    FileStream(path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions)
    FileStream(handle: IntPtr, access: FileAccess)
    FileStream(handle: IntPtr, access: FileAccess, ownsHandle: bool)
    FileStream(handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int)
    FileStream(handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int, isAsync: bool)
    FileStream(handle: SafeFileHandle, access: FileAccess)
    FileStream(handle: SafeFileHandle, access: FileAccess, bufferSize: int)
    FileStream(handle: SafeFileHandle, access: FileAccess, bufferSize: int, isAsync: bool)
    """
    def BeginRead(self, array, offset, numBytes, userCallback, stateObject):
        """ BeginRead(self: FileStream, array: Array[Byte], offset: int, numBytes: int, userCallback: AsyncCallback, stateObject: object) -> IAsyncResult """
        pass

    def BeginWrite(self, array, offset, numBytes, userCallback, stateObject):
        """ BeginWrite(self: FileStream, array: Array[Byte], offset: int, numBytes: int, userCallback: AsyncCallback, stateObject: object) -> IAsyncResult """
        pass

    def Dispose(self):
        """ Dispose(self: FileStream, disposing: bool) """
        pass

    def EndRead(self, asyncResult):
        """ EndRead(self: FileStream, asyncResult: IAsyncResult) -> int """
        pass

    def EndWrite(self, asyncResult):
        """ EndWrite(self: FileStream, asyncResult: IAsyncResult) """
        pass

    def Flush(self, flushToDisk=None):
        """ Flush(self: FileStream, flushToDisk: bool)Flush(self: FileStream) """
        pass

    def FlushAsync(self, cancellationToken=None):
        """ FlushAsync(self: FileStream, cancellationToken: CancellationToken) -> Task """
        pass

    def GetAccessControl(self):
        """ GetAccessControl(self: FileStream) -> FileSecurity """
        pass

    def Lock(self, position, length):
        """ Lock(self: FileStream, position: Int64, length: Int64) """
        pass

    def Read(self, array, offset, count):
        """ Read(self: FileStream, offset: int, count: int) -> (int, Array[Byte]) """
        pass

    def ReadAsync(self, buffer, offset, count, cancellationToken=None):
        """ ReadAsync(self: FileStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task[int] """
        pass

    def ReadByte(self):
        """ ReadByte(self: FileStream) -> int """
        pass

    def Seek(self, offset, origin):
        """ Seek(self: FileStream, offset: Int64, origin: SeekOrigin) -> Int64 """
        pass

    def SetAccessControl(self, fileSecurity):
        """ SetAccessControl(self: FileStream, fileSecurity: FileSecurity) """
        pass

    def SetLength(self, value):
        """ SetLength(self: FileStream, value: Int64) """
        pass

    def Unlock(self, position, length):
        """ Unlock(self: FileStream, position: Int64, length: Int64) """
        pass

    def Write(self, array, offset, count):
        """ Write(self: FileStream, array: Array[Byte], offset: int, count: int) """
        pass

    def WriteAsync(self, buffer, offset, count, cancellationToken=None):
        """ WriteAsync(self: FileStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task """
        pass

    def WriteByte(self, value):
        """ WriteByte(self: FileStream, value: Byte) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, path: str, mode: FileMode)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, options: FileOptions)
        __new__(cls: type, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, useAsync: bool)
        __new__(cls: type, path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions, fileSecurity: FileSecurity)
        __new__(cls: type, path: str, mode: FileMode, rights: FileSystemRights, share: FileShare, bufferSize: int, options: FileOptions)
        __new__(cls: type, handle: IntPtr, access: FileAccess)
        __new__(cls: type, handle: IntPtr, access: FileAccess, ownsHandle: bool)
        __new__(cls: type, handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int)
        __new__(cls: type, handle: IntPtr, access: FileAccess, ownsHandle: bool, bufferSize: int, isAsync: bool)
        __new__(cls: type, handle: SafeFileHandle, access: FileAccess)
        __new__(cls: type, handle: SafeFileHandle, access: FileAccess, bufferSize: int)
        __new__(cls: type, handle: SafeFileHandle, access: FileAccess, bufferSize: int, isAsync: bool)
        """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanRead(self: FileStream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanSeek(self: FileStream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanWrite(self: FileStream) -> bool

"""

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handle(self: FileStream) -> IntPtr

"""

    IsAsync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAsync(self: FileStream) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: FileStream) -> Int64

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: FileStream) -> str

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: FileStream) -> Int64

Set: Position(self: FileStream) = value
"""

    SafeFileHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SafeFileHandle(self: FileStream) -> SafeFileHandle

"""



class FileSystemEventArgs(EventArgs):
    """ FileSystemEventArgs(changeType: WatcherChangeTypes, directory: str, name: str) """
    @staticmethod # known case of __new__
    def __new__(self, changeType, directory, name):
        """ __new__(cls: type, changeType: WatcherChangeTypes, directory: str, name: str) """
        pass

    ChangeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChangeType(self: FileSystemEventArgs) -> WatcherChangeTypes

"""

    FullPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullPath(self: FileSystemEventArgs) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: FileSystemEventArgs) -> str

"""



class FileSystemEventHandler(MulticastDelegate):
    """ FileSystemEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: FileSystemEventHandler, sender: object, e: FileSystemEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FileSystemEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: FileSystemEventHandler, sender: object, e: FileSystemEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FileSystemWatcher(Component):
    """
    FileSystemWatcher()
    FileSystemWatcher(path: str)
    FileSystemWatcher(path: str, filter: str)
    """
    def BeginInit(self):
        """ BeginInit(self: FileSystemWatcher) """
        pass

    def Dispose(self):
        """ Dispose(self: FileSystemWatcher, disposing: bool) """
        pass

    def EndInit(self):
        """ EndInit(self: FileSystemWatcher) """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """ OnChanged(self: FileSystemWatcher, e: FileSystemEventArgs) """
        pass

    def OnCreated(self, *args): #cannot find CLR method
        """ OnCreated(self: FileSystemWatcher, e: FileSystemEventArgs) """
        pass

    def OnDeleted(self, *args): #cannot find CLR method
        """ OnDeleted(self: FileSystemWatcher, e: FileSystemEventArgs) """
        pass

    def OnError(self, *args): #cannot find CLR method
        """ OnError(self: FileSystemWatcher, e: ErrorEventArgs) """
        pass

    def OnRenamed(self, *args): #cannot find CLR method
        """ OnRenamed(self: FileSystemWatcher, e: RenamedEventArgs) """
        pass

    def WaitForChanged(self, changeType, timeout=None):
        """
        WaitForChanged(self: FileSystemWatcher, changeType: WatcherChangeTypes, timeout: int) -> WaitForChangedResult
        WaitForChanged(self: FileSystemWatcher, changeType: WatcherChangeTypes) -> WaitForChangedResult
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, path=None, filter=None):
        """
        __new__(cls: type)
        __new__(cls: type, path: str)
        __new__(cls: type, path: str, filter: str)
        """
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    EnableRaisingEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnableRaisingEvents(self: FileSystemWatcher) -> bool

Set: EnableRaisingEvents(self: FileSystemWatcher) = value
"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: FileSystemWatcher) -> str

Set: Filter(self: FileSystemWatcher) = value
"""

    IncludeSubdirectories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeSubdirectories(self: FileSystemWatcher) -> bool

Set: IncludeSubdirectories(self: FileSystemWatcher) = value
"""

    InternalBufferSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalBufferSize(self: FileSystemWatcher) -> int

Set: InternalBufferSize(self: FileSystemWatcher) = value
"""

    NotifyFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NotifyFilter(self: FileSystemWatcher) -> NotifyFilters

Set: NotifyFilter(self: FileSystemWatcher) = value
"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: FileSystemWatcher) -> str

Set: Path(self: FileSystemWatcher) = value
"""

    Site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Site(self: FileSystemWatcher) -> ISite

Set: Site(self: FileSystemWatcher) = value
"""

    SynchronizingObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SynchronizingObject(self: FileSystemWatcher) -> ISynchronizeInvoke

Set: SynchronizingObject(self: FileSystemWatcher) = value
"""


    Changed = None
    Created = None
    Deleted = None
    Error = None
    Renamed = None


class InternalBufferOverflowException(SystemException):
    """
    InternalBufferOverflowException()
    InternalBufferOverflowException(message: str)
    InternalBufferOverflowException(message: str, inner: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class InvalidDataException(SystemException):
    """
    InvalidDataException()
    InvalidDataException(message: str)
    InvalidDataException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        """
        pass


class IODescriptionAttribute(DescriptionAttribute):
    """ IODescriptionAttribute(description: str) """
    @staticmethod # known case of __new__
    def __new__(self, description):
        """ __new__(cls: type, description: str) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: IODescriptionAttribute) -> str

"""

    DescriptionValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class MemoryStream(Stream):
    """
    MemoryStream()
    MemoryStream(capacity: int)
    MemoryStream(buffer: Array[Byte])
    MemoryStream(buffer: Array[Byte], writable: bool)
    MemoryStream(buffer: Array[Byte], index: int, count: int)
    MemoryStream(buffer: Array[Byte], index: int, count: int, writable: bool)
    MemoryStream(buffer: Array[Byte], index: int, count: int, writable: bool, publiclyVisible: bool)
    """
    def CopyToAsync(self, destination, bufferSize=None, cancellationToken=None):
        """ CopyToAsync(self: MemoryStream, destination: Stream, bufferSize: int, cancellationToken: CancellationToken) -> Task """
        pass

    def Dispose(self):
        """ Dispose(self: MemoryStream, disposing: bool) """
        pass

    def Flush(self):
        """ Flush(self: MemoryStream) """
        pass

    def FlushAsync(self, cancellationToken=None):
        """ FlushAsync(self: MemoryStream, cancellationToken: CancellationToken) -> Task """
        pass

    def GetBuffer(self):
        """ GetBuffer(self: MemoryStream) -> Array[Byte] """
        pass

    def Read(self, buffer, offset, count):
        """ Read(self: MemoryStream, offset: int, count: int) -> (int, Array[Byte]) """
        pass

    def ReadAsync(self, buffer, offset, count, cancellationToken=None):
        """ ReadAsync(self: MemoryStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task[int] """
        pass

    def ReadByte(self):
        """ ReadByte(self: MemoryStream) -> int """
        pass

    def Seek(self, offset, loc):
        """ Seek(self: MemoryStream, offset: Int64, loc: SeekOrigin) -> Int64 """
        pass

    def SetLength(self, value):
        """ SetLength(self: MemoryStream, value: Int64) """
        pass

    def ToArray(self):
        """ ToArray(self: MemoryStream) -> Array[Byte] """
        pass

    def TryGetBuffer(self, buffer):
        """ TryGetBuffer(self: MemoryStream) -> (bool, ArraySegment[Byte]) """
        pass

    def Write(self, buffer, offset, count):
        """ Write(self: MemoryStream, buffer: Array[Byte], offset: int, count: int) """
        pass

    def WriteAsync(self, buffer, offset, count, cancellationToken=None):
        """ WriteAsync(self: MemoryStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task """
        pass

    def WriteByte(self, value):
        """ WriteByte(self: MemoryStream, value: Byte) """
        pass

    def WriteTo(self, stream):
        """ WriteTo(self: MemoryStream, stream: Stream) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, buffer: Array[Byte])
        __new__(cls: type, buffer: Array[Byte], writable: bool)
        __new__(cls: type, buffer: Array[Byte], index: int, count: int)
        __new__(cls: type, buffer: Array[Byte], index: int, count: int, writable: bool)
        __new__(cls: type, buffer: Array[Byte], index: int, count: int, writable: bool, publiclyVisible: bool)
        """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanRead(self: MemoryStream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanSeek(self: MemoryStream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanWrite(self: MemoryStream) -> bool

"""

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: MemoryStream) -> int

Set: Capacity(self: MemoryStream) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: MemoryStream) -> Int64

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: MemoryStream) -> Int64

Set: Position(self: MemoryStream) = value
"""



class NotifyFilters(Enum):
    """ enum (flags) NotifyFilters, values: Attributes (4), CreationTime (64), DirectoryName (2), FileName (1), LastAccess (32), LastWrite (16), Security (256), Size (8) """
    Attributes = None
    CreationTime = None
    DirectoryName = None
    FileName = None
    LastAccess = None
    LastWrite = None
    Security = None
    Size = None
    value__ = None


class Path(object):
    # no doc
    @staticmethod
    def ChangeExtension(path, extension):
        """ ChangeExtension(path: str, extension: str) -> str """
        pass

    @staticmethod
    def Combine(*__args):
        """
        Combine(path1: str, path2: str, path3: str, path4: str) -> str
        Combine(*paths: Array[str]) -> str
        Combine(path1: str, path2: str) -> str
        Combine(path1: str, path2: str, path3: str) -> str
        """
        pass

    @staticmethod
    def GetDirectoryName(path):
        """ GetDirectoryName(path: str) -> str """
        pass

    @staticmethod
    def GetExtension(path):
        """ GetExtension(path: str) -> str """
        pass

    @staticmethod
    def GetFileName(path):
        """ GetFileName(path: str) -> str """
        pass

    @staticmethod
    def GetFileNameWithoutExtension(path):
        """ GetFileNameWithoutExtension(path: str) -> str """
        pass

    @staticmethod
    def GetFullPath(path):
        """ GetFullPath(path: str) -> str """
        pass

    @staticmethod
    def GetInvalidFileNameChars():
        """ GetInvalidFileNameChars() -> Array[Char] """
        pass

    @staticmethod
    def GetInvalidPathChars():
        """ GetInvalidPathChars() -> Array[Char] """
        pass

    @staticmethod
    def GetPathRoot(path):
        """ GetPathRoot(path: str) -> str """
        pass

    @staticmethod
    def GetRandomFileName():
        """ GetRandomFileName() -> str """
        pass

    @staticmethod
    def GetTempFileName():
        """ GetTempFileName() -> str """
        pass

    @staticmethod
    def GetTempPath():
        """ GetTempPath() -> str """
        pass

    @staticmethod
    def HasExtension(path):
        """ HasExtension(path: str) -> bool """
        pass

    @staticmethod
    def IsPathRooted(path):
        """ IsPathRooted(path: str) -> bool """
        pass

    AltDirectorySeparatorChar = None
    DirectorySeparatorChar = None
    InvalidPathChars = None
    PathSeparator = None
    VolumeSeparatorChar = None
    __all__ = [
        'AltDirectorySeparatorChar',
        'ChangeExtension',
        'Combine',
        'DirectorySeparatorChar',
        'GetDirectoryName',
        'GetExtension',
        'GetFileName',
        'GetFileNameWithoutExtension',
        'GetFullPath',
        'GetInvalidFileNameChars',
        'GetInvalidPathChars',
        'GetPathRoot',
        'GetRandomFileName',
        'GetTempFileName',
        'GetTempPath',
        'HasExtension',
        'InvalidPathChars',
        'IsPathRooted',
        'PathSeparator',
        'VolumeSeparatorChar',
    ]


class PathTooLongException(IOException):
    """
    PathTooLongException()
    PathTooLongException(message: str)
    PathTooLongException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class RenamedEventArgs(FileSystemEventArgs):
    """ RenamedEventArgs(changeType: WatcherChangeTypes, directory: str, name: str, oldName: str) """
    @staticmethod # known case of __new__
    def __new__(self, changeType, directory, name, oldName):
        """ __new__(cls: type, changeType: WatcherChangeTypes, directory: str, name: str, oldName: str) """
        pass

    OldFullPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldFullPath(self: RenamedEventArgs) -> str

"""

    OldName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldName(self: RenamedEventArgs) -> str

"""



class RenamedEventHandler(MulticastDelegate):
    """ RenamedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: RenamedEventHandler, sender: object, e: RenamedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: RenamedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: RenamedEventHandler, sender: object, e: RenamedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class SearchOption(Enum):
    """ enum SearchOption, values: AllDirectories (1), TopDirectoryOnly (0) """
    AllDirectories = None
    TopDirectoryOnly = None
    value__ = None


class SeekOrigin(Enum):
    """ enum SeekOrigin, values: Begin (0), Current (1), End (2) """
    Begin = None
    Current = None
    End = None
    value__ = None


class TextReader(MarshalByRefObject):
    # no doc
    def Close(self):
        """ Close(self: TextReader) """
        pass

    def Dispose(self):
        """ Dispose(self: TextReader) """
        pass

    def Peek(self):
        """ Peek(self: TextReader) -> int """
        pass

    def Read(self, buffer=None, index=None, count=None):
        """
        Read(self: TextReader, index: int, count: int) -> (int, Array[Char])
        Read(self: TextReader) -> int
        """
        pass

    def ReadAsync(self, buffer, index, count):
        """ ReadAsync(self: TextReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        pass

    def ReadBlock(self, buffer, index, count):
        """ ReadBlock(self: TextReader, index: int, count: int) -> (int, Array[Char]) """
        pass

    def ReadBlockAsync(self, buffer, index, count):
        """ ReadBlockAsync(self: TextReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        pass

    def ReadLine(self):
        """ ReadLine(self: TextReader) -> str """
        pass

    def ReadLineAsync(self):
        """ ReadLineAsync(self: TextReader) -> Task[str] """
        pass

    def ReadToEnd(self):
        """ ReadToEnd(self: TextReader) -> str """
        pass

    def ReadToEndAsync(self):
        """ ReadToEndAsync(self: TextReader) -> Task[str] """
        pass

    @staticmethod
    def Synchronized(reader):
        """ Synchronized(reader: TextReader) -> TextReader """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Null = None


class StreamReader(TextReader):
    """
    StreamReader(stream: Stream)
    StreamReader(stream: Stream, detectEncodingFromByteOrderMarks: bool)
    StreamReader(stream: Stream, encoding: Encoding)
    StreamReader(stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)
    StreamReader(stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)
    StreamReader(stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int, leaveOpen: bool)
    StreamReader(path: str)
    StreamReader(path: str, detectEncodingFromByteOrderMarks: bool)
    StreamReader(path: str, encoding: Encoding)
    StreamReader(path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)
    StreamReader(path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)
    """
    def Close(self):
        """ Close(self: StreamReader) """
        pass

    def DiscardBufferedData(self):
        """ DiscardBufferedData(self: StreamReader) """
        pass

    def Dispose(self):
        """ Dispose(self: StreamReader, disposing: bool) """
        pass

    def Peek(self):
        """ Peek(self: StreamReader) -> int """
        pass

    def Read(self, buffer=None, index=None, count=None):
        """
        Read(self: StreamReader, index: int, count: int) -> (int, Array[Char])
        Read(self: StreamReader) -> int
        """
        pass

    def ReadAsync(self, buffer, index, count):
        """ ReadAsync(self: StreamReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        pass

    def ReadBlock(self, buffer, index, count):
        """ ReadBlock(self: StreamReader, index: int, count: int) -> (int, Array[Char]) """
        pass

    def ReadBlockAsync(self, buffer, index, count):
        """ ReadBlockAsync(self: StreamReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        pass

    def ReadLine(self):
        """ ReadLine(self: StreamReader) -> str """
        pass

    def ReadLineAsync(self):
        """ ReadLineAsync(self: StreamReader) -> Task[str] """
        pass

    def ReadToEnd(self):
        """ ReadToEnd(self: StreamReader) -> str """
        pass

    def ReadToEndAsync(self):
        """ ReadToEndAsync(self: StreamReader) -> Task[str] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, detectEncodingFromByteOrderMarks: bool)
        __new__(cls: type, stream: Stream, encoding: Encoding)
        __new__(cls: type, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)
        __new__(cls: type, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)
        __new__(cls: type, stream: Stream, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int, leaveOpen: bool)
        __new__(cls: type, path: str)
        __new__(cls: type, path: str, detectEncodingFromByteOrderMarks: bool)
        __new__(cls: type, path: str, encoding: Encoding)
        __new__(cls: type, path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool)
        __new__(cls: type, path: str, encoding: Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int)
        """
        pass

    BaseStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseStream(self: StreamReader) -> Stream

"""

    CurrentEncoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentEncoding(self: StreamReader) -> Encoding

"""

    EndOfStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndOfStream(self: StreamReader) -> bool

"""


    Null = None


class TextWriter(MarshalByRefObject):
    # no doc
    def Close(self):
        """ Close(self: TextWriter) """
        pass

    def Dispose(self):
        """ Dispose(self: TextWriter) """
        pass

    def Flush(self):
        """ Flush(self: TextWriter) """
        pass

    def FlushAsync(self):
        """ FlushAsync(self: TextWriter) -> Task """
        pass

    @staticmethod
    def Synchronized(writer):
        """ Synchronized(writer: TextWriter) -> TextWriter """
        pass

    def Write(self, *__args):
        """ Write(self: TextWriter, value: str)Write(self: TextWriter, value: object)Write(self: TextWriter, value: float)Write(self: TextWriter, value: Decimal)Write(self: TextWriter, format: str, arg0: object, arg1: object, arg2: object)Write(self: TextWriter, format: str, *arg: Array[object])Write(self: TextWriter, format: str, arg0: object)Write(self: TextWriter, format: str, arg0: object, arg1: object)Write(self: TextWriter, value: Single)Write(self: TextWriter, buffer: Array[Char], index: int, count: int)Write(self: TextWriter, value: bool)Write(self: TextWriter, value: Char)Write(self: TextWriter, buffer: Array[Char])Write(self: TextWriter, value: Int64)Write(self: TextWriter, value: UInt64)Write(self: TextWriter, value: int)Write(self: TextWriter, value: UInt32) """
        pass

    def WriteAsync(self, *__args):
        """
        WriteAsync(self: TextWriter, buffer: Array[Char]) -> Task
        WriteAsync(self: TextWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteAsync(self: TextWriter, value: Char) -> Task
        WriteAsync(self: TextWriter, value: str) -> Task
        """
        pass

    def WriteLine(self, *__args):
        """ WriteLine(self: TextWriter, value: Decimal)WriteLine(self: TextWriter, value: str)WriteLine(self: TextWriter, value: Single)WriteLine(self: TextWriter, value: float)WriteLine(self: TextWriter, value: object)WriteLine(self: TextWriter, format: str, arg0: object, arg1: object, arg2: object)WriteLine(self: TextWriter, format: str, *arg: Array[object])WriteLine(self: TextWriter, format: str, arg0: object)WriteLine(self: TextWriter, format: str, arg0: object, arg1: object)WriteLine(self: TextWriter, buffer: Array[Char])WriteLine(self: TextWriter, buffer: Array[Char], index: int, count: int)WriteLine(self: TextWriter)WriteLine(self: TextWriter, value: Char)WriteLine(self: TextWriter, value: bool)WriteLine(self: TextWriter, value: Int64)WriteLine(self: TextWriter, value: UInt64)WriteLine(self: TextWriter, value: int)WriteLine(self: TextWriter, value: UInt32) """
        pass

    def WriteLineAsync(self, *__args):
        """
        WriteLineAsync(self: TextWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteLineAsync(self: TextWriter) -> Task
        WriteLineAsync(self: TextWriter, buffer: Array[Char]) -> Task
        WriteLineAsync(self: TextWriter, value: Char) -> Task
        WriteLineAsync(self: TextWriter, value: str) -> Task
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, formatProvider: IFormatProvider)
        """
        pass

    Encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Encoding(self: TextWriter) -> Encoding

"""

    FormatProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FormatProvider(self: TextWriter) -> IFormatProvider

"""

    NewLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewLine(self: TextWriter) -> str

Set: NewLine(self: TextWriter) = value
"""


    CoreNewLine = None
    Null = None


class StreamWriter(TextWriter):
    """
    StreamWriter(stream: Stream)
    StreamWriter(stream: Stream, encoding: Encoding)
    StreamWriter(stream: Stream, encoding: Encoding, bufferSize: int, leaveOpen: bool)
    StreamWriter(path: str, append: bool, encoding: Encoding)
    StreamWriter(stream: Stream, encoding: Encoding, bufferSize: int)
    StreamWriter(path: str)
    StreamWriter(path: str, append: bool)
    StreamWriter(path: str, append: bool, encoding: Encoding, bufferSize: int)
    """
    def Close(self):
        """ Close(self: StreamWriter) """
        pass

    def Dispose(self):
        """ Dispose(self: StreamWriter, disposing: bool) """
        pass

    def Flush(self):
        """ Flush(self: StreamWriter) """
        pass

    def FlushAsync(self):
        """ FlushAsync(self: StreamWriter) -> Task """
        pass

    def Write(self, *__args):
        """ Write(self: StreamWriter, buffer: Array[Char])Write(self: StreamWriter, value: str)Write(self: StreamWriter, buffer: Array[Char], index: int, count: int)Write(self: StreamWriter, value: Char) """
        pass

    def WriteAsync(self, *__args):
        """
        WriteAsync(self: StreamWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteAsync(self: StreamWriter, value: str) -> Task
        WriteAsync(self: StreamWriter, value: Char) -> Task
        """
        pass

    def WriteLineAsync(self, *__args):
        """
        WriteLineAsync(self: StreamWriter, value: str) -> Task
        WriteLineAsync(self: StreamWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteLineAsync(self: StreamWriter) -> Task
        WriteLineAsync(self: StreamWriter, value: Char) -> Task
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, encoding: Encoding)
        __new__(cls: type, stream: Stream, encoding: Encoding, bufferSize: int)
        __new__(cls: type, stream: Stream, encoding: Encoding, bufferSize: int, leaveOpen: bool)
        __new__(cls: type, path: str)
        __new__(cls: type, path: str, append: bool)
        __new__(cls: type, path: str, append: bool, encoding: Encoding)
        __new__(cls: type, path: str, append: bool, encoding: Encoding, bufferSize: int)
        """
        pass

    AutoFlush = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoFlush(self: StreamWriter) -> bool

Set: AutoFlush(self: StreamWriter) = value
"""

    BaseStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseStream(self: StreamWriter) -> Stream

"""

    Encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Encoding(self: StreamWriter) -> Encoding

"""


    CoreNewLine = None
    Null = None


class StringReader(TextReader):
    """ StringReader(s: str) """
    def Close(self):
        """ Close(self: StringReader) """
        pass

    def Dispose(self):
        """ Dispose(self: StringReader, disposing: bool) """
        pass

    def Peek(self):
        """ Peek(self: StringReader) -> int """
        pass

    def Read(self, buffer=None, index=None, count=None):
        """
        Read(self: StringReader, index: int, count: int) -> (int, Array[Char])
        Read(self: StringReader) -> int
        """
        pass

    def ReadAsync(self, buffer, index, count):
        """ ReadAsync(self: StringReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        pass

    def ReadBlockAsync(self, buffer, index, count):
        """ ReadBlockAsync(self: StringReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        pass

    def ReadLine(self):
        """ ReadLine(self: StringReader) -> str """
        pass

    def ReadLineAsync(self):
        """ ReadLineAsync(self: StringReader) -> Task[str] """
        pass

    def ReadToEnd(self):
        """ ReadToEnd(self: StringReader) -> str """
        pass

    def ReadToEndAsync(self):
        """ ReadToEndAsync(self: StringReader) -> Task[str] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, s):
        """ __new__(cls: type, s: str) """
        pass


class StringWriter(TextWriter):
    """
    StringWriter()
    StringWriter(formatProvider: IFormatProvider)
    StringWriter(sb: StringBuilder)
    StringWriter(sb: StringBuilder, formatProvider: IFormatProvider)
    """
    def Close(self):
        """ Close(self: StringWriter) """
        pass

    def Dispose(self):
        """ Dispose(self: StringWriter, disposing: bool) """
        pass

    def FlushAsync(self):
        """ FlushAsync(self: StringWriter) -> Task """
        pass

    def GetStringBuilder(self):
        """ GetStringBuilder(self: StringWriter) -> StringBuilder """
        pass

    def ToString(self):
        """ ToString(self: StringWriter) -> str """
        pass

    def Write(self, *__args):
        """ Write(self: StringWriter, value: str)Write(self: StringWriter, buffer: Array[Char], index: int, count: int)Write(self: StringWriter, value: Char) """
        pass

    def WriteAsync(self, *__args):
        """
        WriteAsync(self: StringWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteAsync(self: StringWriter, value: str) -> Task
        WriteAsync(self: StringWriter, value: Char) -> Task
        """
        pass

    def WriteLineAsync(self, *__args):
        """
        WriteLineAsync(self: StringWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteLineAsync(self: StringWriter, value: str) -> Task
        WriteLineAsync(self: StringWriter, value: Char) -> Task
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, formatProvider: IFormatProvider)
        __new__(cls: type, sb: StringBuilder)
        __new__(cls: type, sb: StringBuilder, formatProvider: IFormatProvider)
        """
        pass

    Encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Encoding(self: StringWriter) -> Encoding

"""


    CoreNewLine = None


class UnmanagedMemoryAccessor(object):
    """
    UnmanagedMemoryAccessor(buffer: SafeBuffer, offset: Int64, capacity: Int64)
    UnmanagedMemoryAccessor(buffer: SafeBuffer, offset: Int64, capacity: Int64, access: FileAccess)
    """
    def Dispose(self):
        """ Dispose(self: UnmanagedMemoryAccessor) """
        pass

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: UnmanagedMemoryAccessor, buffer: SafeBuffer, offset: Int64, capacity: Int64, access: FileAccess) """
        pass

    def Read(self, position, structure):
        """ Read[T](self: UnmanagedMemoryAccessor, position: Int64) -> T """
        pass

    def ReadArray(self, position, array, offset, count):
        """ ReadArray[T](self: UnmanagedMemoryAccessor, position: Int64, array: Array[T], offset: int, count: int) -> int """
        pass

    def ReadBoolean(self, position):
        """ ReadBoolean(self: UnmanagedMemoryAccessor, position: Int64) -> bool """
        pass

    def ReadByte(self, position):
        """ ReadByte(self: UnmanagedMemoryAccessor, position: Int64) -> Byte """
        pass

    def ReadChar(self, position):
        """ ReadChar(self: UnmanagedMemoryAccessor, position: Int64) -> Char """
        pass

    def ReadDecimal(self, position):
        """ ReadDecimal(self: UnmanagedMemoryAccessor, position: Int64) -> Decimal """
        pass

    def ReadDouble(self, position):
        """ ReadDouble(self: UnmanagedMemoryAccessor, position: Int64) -> float """
        pass

    def ReadInt16(self, position):
        """ ReadInt16(self: UnmanagedMemoryAccessor, position: Int64) -> Int16 """
        pass

    def ReadInt32(self, position):
        """ ReadInt32(self: UnmanagedMemoryAccessor, position: Int64) -> int """
        pass

    def ReadInt64(self, position):
        """ ReadInt64(self: UnmanagedMemoryAccessor, position: Int64) -> Int64 """
        pass

    def ReadSByte(self, position):
        """ ReadSByte(self: UnmanagedMemoryAccessor, position: Int64) -> SByte """
        pass

    def ReadSingle(self, position):
        """ ReadSingle(self: UnmanagedMemoryAccessor, position: Int64) -> Single """
        pass

    def ReadUInt16(self, position):
        """ ReadUInt16(self: UnmanagedMemoryAccessor, position: Int64) -> UInt16 """
        pass

    def ReadUInt32(self, position):
        """ ReadUInt32(self: UnmanagedMemoryAccessor, position: Int64) -> UInt32 """
        pass

    def ReadUInt64(self, position):
        """ ReadUInt64(self: UnmanagedMemoryAccessor, position: Int64) -> UInt64 """
        pass

    def Write(self, position, *__args):
        """
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: SByte)Write(self: UnmanagedMemoryAccessor, position: Int64, value: float)Write(self: UnmanagedMemoryAccessor, position: Int64, value: Single)Write(self: UnmanagedMemoryAccessor, position: Int64, value: UInt16)Write[T](self: UnmanagedMemoryAccessor, position: Int64, structure: T) -> T
        Write(self: UnmanagedMemoryAccessor, position: Int64, value: UInt64)Write(self: UnmanagedMemoryAccessor, position: Int64, value: UInt32)Write(self: UnmanagedMemoryAccessor, position: Int64, value: Char)Write(self: UnmanagedMemoryAccessor, position: Int64, value: Byte)Write(self: UnmanagedMemoryAccessor, position: Int64, value: bool)Write(self: UnmanagedMemoryAccessor, position: Int64, value: Int16)Write(self: UnmanagedMemoryAccessor, position: Int64, value: Decimal)Write(self: UnmanagedMemoryAccessor, position: Int64, value: Int64)Write(self: UnmanagedMemoryAccessor, position: Int64, value: int)
        """
        pass

    def WriteArray(self, position, array, offset, count):
        """ WriteArray[T](self: UnmanagedMemoryAccessor, position: Int64, array: Array[T], offset: int, count: int) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, buffer, offset, capacity, access=None):
        """
        __new__(cls: type)
        __new__(cls: type, buffer: SafeBuffer, offset: Int64, capacity: Int64)
        __new__(cls: type, buffer: SafeBuffer, offset: Int64, capacity: Int64, access: FileAccess)
        """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanRead(self: UnmanagedMemoryAccessor) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanWrite(self: UnmanagedMemoryAccessor) -> bool

"""

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: UnmanagedMemoryAccessor) -> Int64

"""

    IsOpen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class UnmanagedMemoryStream(Stream):
    """
    UnmanagedMemoryStream(buffer: SafeBuffer, offset: Int64, length: Int64)
    UnmanagedMemoryStream(buffer: SafeBuffer, offset: Int64, length: Int64, access: FileAccess)
    UnmanagedMemoryStream(pointer: Byte*, length: Int64)
    UnmanagedMemoryStream(pointer: Byte*, length: Int64, capacity: Int64, access: FileAccess)
    """
    def Dispose(self):
        """ Dispose(self: UnmanagedMemoryStream, disposing: bool) """
        pass

    def Flush(self):
        """ Flush(self: UnmanagedMemoryStream) """
        pass

    def FlushAsync(self, cancellationToken=None):
        """ FlushAsync(self: UnmanagedMemoryStream, cancellationToken: CancellationToken) -> Task """
        pass

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: UnmanagedMemoryStream, buffer: SafeBuffer, offset: Int64, length: Int64, access: FileAccess)Initialize(self: UnmanagedMemoryStream, pointer: Byte*, length: Int64, capacity: Int64, access: FileAccess) """
        pass

    def Read(self, buffer, offset, count):
        """ Read(self: UnmanagedMemoryStream, offset: int, count: int) -> (int, Array[Byte]) """
        pass

    def ReadAsync(self, buffer, offset, count, cancellationToken=None):
        """ ReadAsync(self: UnmanagedMemoryStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task[int] """
        pass

    def ReadByte(self):
        """ ReadByte(self: UnmanagedMemoryStream) -> int """
        pass

    def Seek(self, offset, loc):
        """ Seek(self: UnmanagedMemoryStream, offset: Int64, loc: SeekOrigin) -> Int64 """
        pass

    def SetLength(self, value):
        """ SetLength(self: UnmanagedMemoryStream, value: Int64) """
        pass

    def Write(self, buffer, offset, count):
        """ Write(self: UnmanagedMemoryStream, buffer: Array[Byte], offset: int, count: int) """
        pass

    def WriteAsync(self, buffer, offset, count, cancellationToken=None):
        """ WriteAsync(self: UnmanagedMemoryStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task """
        pass

    def WriteByte(self, value):
        """ WriteByte(self: UnmanagedMemoryStream, value: Byte) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, buffer: SafeBuffer, offset: Int64, length: Int64)
        __new__(cls: type, buffer: SafeBuffer, offset: Int64, length: Int64, access: FileAccess)
        __new__(cls: type, pointer: Byte*, length: Int64)
        __new__(cls: type, pointer: Byte*, length: Int64, capacity: Int64, access: FileAccess)
        """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanRead(self: UnmanagedMemoryStream) -> bool

"""

    CanSeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanSeek(self: UnmanagedMemoryStream) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanWrite(self: UnmanagedMemoryStream) -> bool

"""

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: UnmanagedMemoryStream) -> Int64

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: UnmanagedMemoryStream) -> Int64

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: UnmanagedMemoryStream) -> Int64

Set: Position(self: UnmanagedMemoryStream) = value
"""

    PositionPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PositionPointer(self: UnmanagedMemoryStream) -> Byte*

Set: PositionPointer(self: UnmanagedMemoryStream) = value
"""



class WaitForChangedResult(object):
    # no doc
    ChangeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChangeType(self: WaitForChangedResult) -> WatcherChangeTypes

Set: ChangeType(self: WaitForChangedResult) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: WaitForChangedResult) -> str

Set: Name(self: WaitForChangedResult) = value
"""

    OldName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldName(self: WaitForChangedResult) -> str

Set: OldName(self: WaitForChangedResult) = value
"""

    TimedOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimedOut(self: WaitForChangedResult) -> bool

Set: TimedOut(self: WaitForChangedResult) = value
"""



class WatcherChangeTypes(Enum):
    """ enum (flags) WatcherChangeTypes, values: All (15), Changed (4), Created (1), Deleted (2), Renamed (8) """
    All = None
    Changed = None
    Created = None
    Deleted = None
    Renamed = None
    value__ = None


# variables with complex values

