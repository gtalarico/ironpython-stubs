class DriveInfo(object, ISerializable):
    """
    Provides access to information on a drive.
    
    DriveInfo(driveName: str)
    """
    @staticmethod
    def GetDrives():
        """
        GetDrives() -> Array[DriveInfo]
        
            Retrieves the drive names of all logical drives on a computer.
            Returns: An array of type System.IO.DriveInfo that represents the logical drives on a computer.
        """
        pass

    def ToString(self):
        """
        ToString(self: DriveInfo) -> str
        
            Returns a drive name as a string.
            Returns: The name of the drive.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, driveName):
        """ __new__(cls: type, driveName: str) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AvailableFreeSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the amount of available free space on a drive.

Get: AvailableFreeSpace(self: DriveInfo) -> Int64

"""

    DriveFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the file system, such as NTFS or FAT32.

Get: DriveFormat(self: DriveInfo) -> str

"""

    DriveType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the drive type.

Get: DriveType(self: DriveInfo) -> DriveType

"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether a drive is ready.

Get: IsReady(self: DriveInfo) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of a drive.

Get: Name(self: DriveInfo) -> str

"""

    RootDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the root directory of a drive.

Get: RootDirectory(self: DriveInfo) -> DirectoryInfo

"""

    TotalFreeSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total amount of free space available on a drive.

Get: TotalFreeSpace(self: DriveInfo) -> Int64

"""

    TotalSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total size of storage space on a drive.

Get: TotalSize(self: DriveInfo) -> Int64

"""

    VolumeLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the volume label of a drive.

Get: VolumeLabel(self: DriveInfo) -> str

Set: VolumeLabel(self: DriveInfo) = value
"""


