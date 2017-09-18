class Directory(object):
 """ Exposes static methods for creating,moving,and enumerating through directories and subdirectories. This class cannot be inherited. """
 @staticmethod
 def CreateDirectory(path,directorySecurity=None):
  """
  CreateDirectory(path: str,directorySecurity: DirectorySecurity) -> DirectoryInfo

  

   Creates all the directories in the specified path,applying the specified Windows security.

  

   path: The directory to create.

   directorySecurity: The access control to apply to the directory.

   Returns: A System.IO.DirectoryInfo object representing the newly created directory.

  CreateDirectory(path: str) -> DirectoryInfo

  

   Creates all directories and subdirectories in the specified path.

  

   path: The directory path to create.

   Returns: A System.IO.DirectoryInfo as specified by path.
  """
  pass
 @staticmethod
 def Delete(path,recursive=None):
  """
  Delete(path: str,recursive: bool)

   Deletes the specified directory and,if indicated,any subdirectories and files in the directory.

  

   path: The name of the directory to remove.

   recursive: true to remove directories,subdirectories,and files in path; otherwise,false.

  Delete(path: str)

   Deletes an empty directory from a specified path.

  

   path: The name of the empty directory to remove. This directory must be writable or empty.
  """
  pass
 @staticmethod
 def EnumerateDirectories(path,searchPattern=None,searchOption=None):
  """
  EnumerateDirectories(path: str,searchPattern: str,searchOption: SearchOption) -> IEnumerable[str]

  

   Returns an enumerable collection of directory names that match a search pattern in a specified 

    path,and optionally searches subdirectories.

  

  

   path: The directory to search.

   searchPattern: The search string to match against the names of directories in path.

   searchOption: One of the values of the System.IO.SearchOption enumeration that specifies whether the search 

    operation should include only the current directory or should include all subdirectories.The 

    default value is System.IO.SearchOption.TopDirectoryOnly.

  

   Returns: An enumerable collection of directory names in the directory specified by path and that match 

    searchPattern and searchOption.

  

  EnumerateDirectories(path: str,searchPattern: str) -> IEnumerable[str]

  

   Returns an enumerable collection of directory names that match a search pattern in a specified 

    path.

  

  

   path: The directory to search.

   searchPattern: The search string to match against the names of directories in path.

   Returns: An enumerable collection of directory names in the directory specified by path and that match 

    searchPattern.

  

  EnumerateDirectories(path: str) -> IEnumerable[str]

  

   Returns an enumerable collection of directory names in a specified path.

  

   path: The directory to search.

   Returns: An enumerable collection of directory names in the directory specified by path.
  """
  pass
 @staticmethod
 def EnumerateFiles(path,searchPattern=None,searchOption=None):
  """
  EnumerateFiles(path: str,searchPattern: str,searchOption: SearchOption) -> IEnumerable[str]

  

   Returns an enumerable collection of file names that match a search pattern in a specified path,

    and optionally searches subdirectories.

  

  

   path: The directory to search.

   searchPattern: The search string to match against the names of directories in path.

   searchOption: One of the values of the System.IO.SearchOption enumeration that specifies whether the search 

    operation should include only the current directory or should include all subdirectories.The 

    default value is System.IO.SearchOption.TopDirectoryOnly.

  

   Returns: An enumerable collection of file names in the directory specified by path and that match 

    searchPattern and searchOption.

  

  EnumerateFiles(path: str,searchPattern: str) -> IEnumerable[str]

  

   Returns an enumerable collection of file names that match a search pattern in a specified path.

  

   path: The directory to search.

   searchPattern: The search string to match against the names of directories in path.

   Returns: An enumerable collection of file names in the directory specified by path and that match 

    searchPattern.

  

  EnumerateFiles(path: str) -> IEnumerable[str]

  

   Returns an enumerable collection of file names in a specified path.

  

   path: The directory to search.

   Returns: An enumerable collection of file names in the directory specified by path.
  """
  pass
 @staticmethod
 def EnumerateFileSystemEntries(path,searchPattern=None,searchOption=None):
  """
  EnumerateFileSystemEntries(path: str,searchPattern: str,searchOption: SearchOption) -> IEnumerable[str]

  

   Returns an enumerable collection of file names and directory names that match a search pattern 

    in a specified path,and optionally searches subdirectories.

  

  

   path: The directory to search.

   searchPattern: The search string to match against the names of directories in path.

   searchOption: One of the values of the System.IO.SearchOption enumeration that specifies whether the search 

    operation should include only the current directory or should include all subdirectories.The 

    default value is System.IO.SearchOption.TopDirectoryOnly.

  

   Returns: An enumerable collection of file-system entries in the directory specified by path and that 

    match searchPattern and searchOption.

  

  EnumerateFileSystemEntries(path: str,searchPattern: str) -> IEnumerable[str]

  

   Returns an enumerable collection of file-system entries that match a search pattern in a 

    specified path.

  

  

   path: The directory to search.

   searchPattern: The search string to match against the names of directories in path.

   Returns: An enumerable collection of file-system entries in the directory specified by path and that 

    match searchPattern.

  

  EnumerateFileSystemEntries(path: str) -> IEnumerable[str]

  

   Returns an enumerable collection of file-system entries in a specified path.

  

   path: The directory to search.

   Returns: An enumerable collection of file-system entries in the directory specified by path.
  """
  pass
 @staticmethod
 def Exists(path):
  """
  Exists(path: str) -> bool

  

   Determines whether the given path refers to an existing directory on disk.

  

   path: The path to test.

   Returns: true if path refers to an existing directory; otherwise,false.
  """
  pass
 @staticmethod
 def GetAccessControl(path,includeSections=None):
  """
  GetAccessControl(path: str,includeSections: AccessControlSections) -> DirectorySecurity

  

   Gets a System.Security.AccessControl.DirectorySecurity object that encapsulates the specified 

    type of access control list (ACL) entries for a specified directory.

  

  

   path: The path to a directory containing a System.Security.AccessControl.DirectorySecurity object that 

    describes the file's access control list (ACL) information.

  

   includeSections: One of the System.Security.AccessControl.AccessControlSections values that specifies the type of 

    access control list (ACL) information to receive.

  

   Returns: A System.Security.AccessControl.DirectorySecurity object that encapsulates the access control 

    rules for the file described by the path parameter.

  

  GetAccessControl(path: str) -> DirectorySecurity

  

   Gets a System.Security.AccessControl.DirectorySecurity object that encapsulates the access 

    control list (ACL) entries for a specified directory.

  

  

   path: The path to a directory containing a System.Security.AccessControl.DirectorySecurity object that 

    describes the file's access control list (ACL) information.

  

   Returns: A System.Security.AccessControl.DirectorySecurity object that encapsulates the access control 

    rules for the file described by the path parameter.
  """
  pass
 @staticmethod
 def GetCreationTime(path):
  """
  GetCreationTime(path: str) -> DateTime

  

   Gets the creation date and time of a directory.

  

   path: The path of the directory.

   Returns: A System.DateTime structure set to the creation date and time for the specified directory. This 

    value is expressed in local time.
  """
  pass
 @staticmethod
 def GetCreationTimeUtc(path):
  """
  GetCreationTimeUtc(path: str) -> DateTime

  

   Gets the creation date and time,in Coordinated Universal Time (UTC) format,of a directory.

  

   path: The path of the directory.

   Returns: A System.DateTime structure set to the creation date and time for the specified directory. This 

    value is expressed in UTC time.
  """
  pass
 @staticmethod
 def GetCurrentDirectory():
  """
  GetCurrentDirectory() -> str

  

   Gets the current working directory of the application.

   Returns: A string that contains the path of the current working directory,and does not end with a 

    backslash (\).
  """
  pass
 @staticmethod
 def GetDirectories(path,searchPattern=None,searchOption=None):
  """
  GetDirectories(path: str,searchPattern: str,searchOption: SearchOption) -> Array[str]

  

   Gets the names of the directories (including their paths) that match the specified search 

    pattern in the current directory,and optionally searches subdirectories.

  

  

   path: The path to search.

   searchPattern: The search string to match against the names of files in path. The parameter cannot end in two 

    periods ("..") or contain two periods ("..") followed by System.IO.Path.DirectorySeparatorChar 

    or System.IO.Path.AltDirectorySeparatorChar,nor can it contain any of the characters in 

    System.IO.Path.InvalidPathChars.

  

   searchOption: One of the System.IO.SearchOption values that specifies whether the search operation should 

    include all subdirectories or only the current directory.

  

   Returns: A String array of directories that match the search pattern.

  GetDirectories(path: str,searchPattern: str) -> Array[str]

  

   Gets an array of directories (including their paths) that match the specified search pattern in 

    the current directory.

  

  

   path: The path to search.

   searchPattern: The search string to match against the names of files in path. The parameter cannot end in two 

    periods ("..") or contain two periods ("..") followed by System.IO.Path.DirectorySeparatorChar 

    or System.IO.Path.AltDirectorySeparatorChar,nor can it contain any of the characters in 

    System.IO.Path.InvalidPathChars.

  

   Returns: A String array of directories that match the search pattern.

  GetDirectories(path: str) -> Array[str]

  

   Gets the names of subdirectories (including their paths) in the specified directory.

  

   path: The path for which an array of subdirectory names is returned.

   Returns: An array of the names of subdirectories in path.
  """
  pass
 @staticmethod
 def GetDirectoryRoot(path):
  """
  GetDirectoryRoot(path: str) -> str

  

   Returns the volume information,root information,or both for the specified path.

  

   path: The path of a file or directory.

   Returns: A string containing the volume information,root information,or both for the specified path.
  """
  pass
 @staticmethod
 def GetFiles(path,searchPattern=None,searchOption=None):
  """
  GetFiles(path: str,searchPattern: str,searchOption: SearchOption) -> Array[str]

  

   Returns the names of files (including their paths) that match the specified search pattern in 

    the specified directory,using a value to determine whether to search subdirectories.

  

  

   path: The directory to search.

   searchPattern: The search string to match against the names of files in path. The parameter cannot end in two 

    periods ("..") or contain two periods ("..") followed by System.IO.Path.DirectorySeparatorChar 

    or System.IO.Path.AltDirectorySeparatorChar,nor can it contain any of the characters in 

    System.IO.Path.InvalidPathChars.

  

   searchOption: One of the System.IO.SearchOption values that specifies whether the search operation should 

    include all subdirectories or only the current directory.

  

   Returns: A String array containing the names of files in the specified directory that match the specified 

    search pattern. File names include the full path.

  

  GetFiles(path: str,searchPattern: str) -> Array[str]

  

   Returns the names of files (including their paths) that match the specified search pattern in 

    the specified directory.

  

  

   path: The directory to search.

   searchPattern: The search string to match against the names of files in path. The parameter cannot end in two 

    periods ("..") or contain two periods ("..") followed by System.IO.Path.DirectorySeparatorChar 

    or System.IO.Path.AltDirectorySeparatorChar,nor can it contain any of the characters in 

    System.IO.Path.InvalidPathChars.

  

   Returns: A String array containing the names of files in the specified directory that match the specified 

    search pattern. File names include the full path.

  

  GetFiles(path: str) -> Array[str]

  

   Returns the names of files (including their paths) in the specified directory.

  

   path: The directory from which to retrieve the files.

   Returns: A String array of file names in the specified directory.
  """
  pass
 @staticmethod
 def GetFileSystemEntries(path,searchPattern=None,searchOption=None):
  """
  GetFileSystemEntries(path: str,searchPattern: str,searchOption: SearchOption) -> Array[str]

  

   Gets an array of all the file names and directory names that match a search pattern in a 

    specified path,and optionally searches subdirectories.

  

  

   path: The directory to search.

   searchPattern: The string used to search for all files or directories that match its search pattern. The 

    default pattern is for all files and directories: "*"

  

   searchOption: The option that specifies whether the search operation should include only the current directory 

    or should include all subdirectories.The default value is 

    System.IO.SearchOption.TopDirectoryOnly.

  

   Returns: An array of file system entries that match the search criteria.

  GetFileSystemEntries(path: str,searchPattern: str) -> Array[str]

  

   Returns an array of file system entries that match the specified search criteria.

  

   path: The path to be searched.

   searchPattern: The search string to match against the names of files in path. The searchPattern parameter 

    cannot end in two periods ("..") or contain two periods ("..") followed by 

    System.IO.Path.DirectorySeparatorChar or System.IO.Path.AltDirectorySeparatorChar,nor can it 

    contain any of the characters in System.IO.Path.InvalidPathChars.

  

   Returns: An array of file system entries that match the search criteria.

  GetFileSystemEntries(path: str) -> Array[str]

  

   Returns the names of all files and subdirectories in the specified directory.

  

   path: The directory for which file and subdirectory names are returned.

   Returns: An array that contains the names of files and subdirectories in the specified directory.
  """
  pass
 @staticmethod
 def GetLastAccessTime(path):
  """
  GetLastAccessTime(path: str) -> DateTime

  

   Returns the date and time the specified file or directory was last accessed.

  

   path: The file or directory for which to obtain access date and time information.

   Returns: A System.DateTime structure set to the date and time the specified file or directory was last 

    accessed. This value is expressed in local time.
  """
  pass
 @staticmethod
 def GetLastAccessTimeUtc(path):
  """
  GetLastAccessTimeUtc(path: str) -> DateTime

  

   Returns the date and time,in Coordinated Universal Time (UTC) format,that the specified file 

    or directory was last accessed.

  

  

   path: The file or directory for which to obtain access date and time information.

   Returns: A System.DateTime structure set to the date and time the specified file or directory was last 

    accessed. This value is expressed in UTC time.
  """
  pass
 @staticmethod
 def GetLastWriteTime(path):
  """
  GetLastWriteTime(path: str) -> DateTime

  

   Returns the date and time the specified file or directory was last written to.

  

   path: The file or directory for which to obtain modification date and time information.

   Returns: A System.DateTime structure set to the date and time the specified file or directory was last 

    written to. This value is expressed in local time.
  """
  pass
 @staticmethod
 def GetLastWriteTimeUtc(path):
  """
  GetLastWriteTimeUtc(path: str) -> DateTime

  

   Returns the date and time,in Coordinated Universal Time (UTC) format,that the specified file 

    or directory was last written to.

  

  

   path: The file or directory for which to obtain modification date and time information.

   Returns: A System.DateTime structure set to the date and time the specified file or directory was last 

    written to. This value is expressed in UTC time.
  """
  pass
 @staticmethod
 def GetLogicalDrives():
  """
  GetLogicalDrives() -> Array[str]

  

   Retrieves the names of the logical drives on this computer in the form "<drive letter>:\".

   Returns: The logical drives on this computer.
  """
  pass
 @staticmethod
 def GetParent(path):
  """
  GetParent(path: str) -> DirectoryInfo

  

   Retrieves the parent directory of the specified path,including both absolute and relative paths.

  

   path: The path for which to retrieve the parent directory.

   Returns: The parent directory,or null if path is the root directory,including the root of a UNC server 

    or share name.
  """
  pass
 @staticmethod
 def Move(sourceDirName,destDirName):
  """
  Move(sourceDirName: str,destDirName: str)

   Moves a file or a directory and its contents to a new location.

  

   sourceDirName: The path of the file or directory to move.

   destDirName: The path to the new location for sourceDirName. If sourceDirName is a file,then destDirName 

    must also be a file name.
  """
  pass
 @staticmethod
 def SetAccessControl(path,directorySecurity):
  """
  SetAccessControl(path: str,directorySecurity: DirectorySecurity)

   Applies access control list (ACL) entries described by a 

    System.Security.AccessControl.DirectorySecurity object to the specified directory.

  

  

   path: A directory to add or remove access control list (ACL) entries from.

   directorySecurity: A System.Security.AccessControl.DirectorySecurity object that describes an ACL entry to apply to 

    the directory described by the path parameter.
  """
  pass
 @staticmethod
 def SetCreationTime(path,creationTime):
  """
  SetCreationTime(path: str,creationTime: DateTime)

   Sets the creation date and time for the specified file or directory.

  

   path: The file or directory for which to set the creation date and time information.

   creationTime: A System.DateTime containing the value to set for the creation date and time of path. This value 

    is expressed in local time.
  """
  pass
 @staticmethod
 def SetCreationTimeUtc(path,creationTimeUtc):
  """
  SetCreationTimeUtc(path: str,creationTimeUtc: DateTime)

   Sets the creation date and time,in Coordinated Universal Time (UTC) format,for the specified 

    file or directory.

  

  

   path: The file or directory for which to set the creation date and time information.

   creationTimeUtc: A System.DateTime containing the value to set for the creation date and time of path. This value 

    is expressed in UTC time.
  """
  pass
 @staticmethod
 def SetCurrentDirectory(path):
  """
  SetCurrentDirectory(path: str)

   Sets the application's current working directory to the specified directory.

  

   path: The path to which the current working directory is set.
  """
  pass
 @staticmethod
 def SetLastAccessTime(path,lastAccessTime):
  """
  SetLastAccessTime(path: str,lastAccessTime: DateTime)

   Sets the date and time the specified file or directory was last accessed.

  

   path: The file or directory for which to set the access date and time information.

   lastAccessTime: A System.DateTime containing the value to set for the access date and time of path. This value 

    is expressed in local time.
  """
  pass
 @staticmethod
 def SetLastAccessTimeUtc(path,lastAccessTimeUtc):
  """
  SetLastAccessTimeUtc(path: str,lastAccessTimeUtc: DateTime)

   Sets the date and time,in Coordinated Universal Time (UTC) format,that the specified file or 

    directory was last accessed.

  

  

   path: The file or directory for which to set the access date and time information.

   lastAccessTimeUtc: A System.DateTime containing the value to set for the access date and time of path. This value 

    is expressed in UTC time.
  """
  pass
 @staticmethod
 def SetLastWriteTime(path,lastWriteTime):
  """
  SetLastWriteTime(path: str,lastWriteTime: DateTime)

   Sets the date and time a directory was last written to.

  

   path: The path of the directory.

   lastWriteTime: The date and time the directory was last written to. This value is expressed in local time.
  """
  pass
 @staticmethod
 def SetLastWriteTimeUtc(path,lastWriteTimeUtc):
  """
  SetLastWriteTimeUtc(path: str,lastWriteTimeUtc: DateTime)

   Sets the date and time,in Coordinated Universal Time (UTC) format,that a directory was last 

    written to.

  

  

   path: The path of the directory.

   lastWriteTimeUtc: The date and time the directory was last written to. This value is expressed in UTC time.
  """
  pass
 __all__=[
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

