class DirectoryInfo(FileSystemInfo,ISerializable):
 """
 Exposes instance methods for creating,moving,and enumerating through directories and subdirectories. This class cannot be inherited.

 

 DirectoryInfo(path: str)
 """
 def Create(self,directorySecurity=None):
  """
  Create(self: DirectoryInfo,directorySecurity: DirectorySecurity)

   Creates a directory using a System.Security.AccessControl.DirectorySecurity object.

  

   directorySecurity: The access control to apply to the directory.

  Create(self: DirectoryInfo)

   Creates a directory.
  """
  pass
 def CreateSubdirectory(self,path,directorySecurity=None):
  """
  CreateSubdirectory(self: DirectoryInfo,path: str,directorySecurity: DirectorySecurity) -> DirectoryInfo

  

   Creates a subdirectory or subdirectories on the specified path with the specified security. The 

    specified path can be relative to this instance of the System.IO.DirectoryInfo class.

  

  

   path: The specified path. This cannot be a different disk volume or Universal Naming Convention (UNC) 

    name.

  

   directorySecurity: The security to apply.

   Returns: The last directory specified in path.

  CreateSubdirectory(self: DirectoryInfo,path: str) -> DirectoryInfo

  

   Creates a subdirectory or subdirectories on the specified path. The specified path can be 

    relative to this instance of the System.IO.DirectoryInfo class.

  

  

   path: The specified path. This cannot be a different disk volume or Universal Naming Convention (UNC) 

    name.

  

   Returns: The last directory specified in path.
  """
  pass
 def Delete(self,recursive=None):
  """
  Delete(self: DirectoryInfo,recursive: bool)

   Deletes this instance of a System.IO.DirectoryInfo,specifying whether to delete subdirectories 

    and files.

  

  

   recursive: true to delete this directory,its subdirectories,and all files; otherwise,false.

  Delete(self: DirectoryInfo)

   Deletes this System.IO.DirectoryInfo if it is empty.
  """
  pass
 def EnumerateDirectories(self,searchPattern=None,searchOption=None):
  """
  EnumerateDirectories(self: DirectoryInfo,searchPattern: str,searchOption: SearchOption) -> IEnumerable[DirectoryInfo]

  

   Returns an enumerable collection of directory information that matches a specified search 

    pattern and search subdirectory option.

  

  

   searchPattern: The search string. The default pattern is "*",which returns all directories.

   searchOption: One of the enumeration values that specifies whether the search operation should include only 

    the current directory or all subdirectories. The default value is 

    System.IO.SearchOption.TopDirectoryOnly.

  

   Returns: An enumerable collection of directories that matches searchPattern and searchOption.

  EnumerateDirectories(self: DirectoryInfo,searchPattern: str) -> IEnumerable[DirectoryInfo]

  

   Returns an enumerable collection of directory information that matches a specified search 

    pattern.

  

  

   searchPattern: The search string. The default pattern is "*",which returns all directories.

   Returns: An enumerable collection of directories that matches searchPattern.

  EnumerateDirectories(self: DirectoryInfo) -> IEnumerable[DirectoryInfo]

  

   Returns an enumerable collection of directory information in the current directory.

   Returns: An enumerable collection of directories in the current directory.
  """
  pass
 def EnumerateFiles(self,searchPattern=None,searchOption=None):
  """
  EnumerateFiles(self: DirectoryInfo,searchPattern: str,searchOption: SearchOption) -> IEnumerable[FileInfo]

  

   Returns an enumerable collection of file information that matches a specified search pattern and 

    search subdirectory option.

  

  

   searchPattern: The search string. The default pattern is "*",which returns all files.

   searchOption: One of the enumeration values that specifies whether the search operation should include only 

    the current directory or all subdirectories. The default value is 

    System.IO.SearchOption.TopDirectoryOnly.

  

   Returns: An enumerable collection of files that matches searchPattern and searchOption.

  EnumerateFiles(self: DirectoryInfo,searchPattern: str) -> IEnumerable[FileInfo]

  

   Returns an enumerable collection of file information that matches a search pattern.

  

   searchPattern: The search string. The default pattern is "*",which returns all files.

   Returns: An enumerable collection of files that matches searchPattern.

  EnumerateFiles(self: DirectoryInfo) -> IEnumerable[FileInfo]

  

   Returns an enumerable collection of file information in the current directory.

   Returns: An enumerable collection of the files in the current directory.
  """
  pass
 def EnumerateFileSystemInfos(self,searchPattern=None,searchOption=None):
  """
  EnumerateFileSystemInfos(self: DirectoryInfo,searchPattern: str,searchOption: SearchOption) -> IEnumerable[FileSystemInfo]

  

   Returns an enumerable collection of file system information that matches a specified search 

    pattern and search subdirectory option.

  

  

   searchPattern: The search string. The default pattern is "*",which returns all files or directories.

   searchOption: One of the enumeration values that specifies whether the search operation should include only 

    the current directory or all subdirectories. The default value is 

    System.IO.SearchOption.TopDirectoryOnly.

  

   Returns: An enumerable collection of file system information objects that matches searchPattern and 

    searchOption.

  

  EnumerateFileSystemInfos(self: DirectoryInfo,searchPattern: str) -> IEnumerable[FileSystemInfo]

  

   Returns an enumerable collection of file system information that matches a specified search 

    pattern.

  

  

   searchPattern: The search string. The default pattern is "*",which returns all files and directories.

   Returns: An enumerable collection of file system information objects that matches searchPattern.

  EnumerateFileSystemInfos(self: DirectoryInfo) -> IEnumerable[FileSystemInfo]

  

   Returns an enumerable collection of file system information in the current directory.

   Returns: An enumerable collection of file system information in the current directory.
  """
  pass
 def GetAccessControl(self,includeSections=None):
  """
  GetAccessControl(self: DirectoryInfo,includeSections: AccessControlSections) -> DirectorySecurity

  

   Gets a System.Security.AccessControl.DirectorySecurity object that encapsulates the specified 

    type of access control list (ACL) entries for the directory described by the current 

    System.IO.DirectoryInfo object.

  

  

   includeSections: One of the System.Security.AccessControl.AccessControlSections values that specifies the type of 

    access control list (ACL) information to receive.

  

   Returns: A System.Security.AccessControl.DirectorySecurity object that encapsulates the access control 

    rules for the file described by the path parameter.ExceptionsException 

    typeConditionSystem.SystemExceptionThe directory could not be found or 

    modified.System.UnauthorizedAccessExceptionThe current process does not have access to open the 

    directory.System.IO.IOExceptionAn I/O error occurred while opening the 

    directory.System.PlatformNotSupportedExceptionThe current operating system is not Microsoft 

    Windows 2000 or later.System.UnauthorizedAccessExceptionThe directory is read-only.-or- This 

    operation is not supported on the current platform.-or- The caller does not have the required 

    permission.

  

  GetAccessControl(self: DirectoryInfo) -> DirectorySecurity

  

   Gets a System.Security.AccessControl.DirectorySecurity object that encapsulates the access 

    control list (ACL) entries for the directory described by the current System.IO.DirectoryInfo 

    object.

  

   Returns: A System.Security.AccessControl.DirectorySecurity object that encapsulates the access control 

    rules for the directory.
  """
  pass
 def GetDirectories(self,searchPattern=None,searchOption=None):
  """
  GetDirectories(self: DirectoryInfo,searchPattern: str,searchOption: SearchOption) -> Array[DirectoryInfo]

  

   Returns an array of directories in the current System.IO.DirectoryInfo matching the given search 

    criteria and using a value to determine whether to search subdirectories.

  

  

   searchPattern: The search string. For example,"System*" can be used to search for all directories that begin 

    with the word "System".

  

   searchOption: One of the enumeration values that specifies whether the search operation should include only 

    the current directory or all subdirectories.

  

   Returns: An array of type DirectoryInfo matching searchPattern.

  GetDirectories(self: DirectoryInfo,searchPattern: str) -> Array[DirectoryInfo]

  

   Returns an array of directories in the current System.IO.DirectoryInfo matching the given search 

    criteria.

  

  

   searchPattern: The search string. For example,"System*" can be used to search for all directories that begin 

    with the word "System".

  

   Returns: An array of type DirectoryInfo matching searchPattern.

  GetDirectories(self: DirectoryInfo) -> Array[DirectoryInfo]

  

   Returns the subdirectories of the current directory.

   Returns: An array of System.IO.DirectoryInfo objects.
  """
  pass
 def GetFiles(self,searchPattern=None,searchOption=None):
  """
  GetFiles(self: DirectoryInfo) -> Array[FileInfo]

  

   Returns a file list from the current directory.

   Returns: An array of type System.IO.FileInfo.

  GetFiles(self: DirectoryInfo,searchPattern: str,searchOption: SearchOption) -> Array[FileInfo]

  

   Returns a file list from the current directory matching the given search pattern and using a 

    value to determine whether to search subdirectories.

  

  

   searchPattern: The search string. For example,"System*" can be used to search for all directories that begin 

    with the word "System".

  

   searchOption: One of the enumeration values that specifies whether the search operation should include only 

    the current directory or all subdirectories.

  

   Returns: An array of type System.IO.FileInfo.

  GetFiles(self: DirectoryInfo,searchPattern: str) -> Array[FileInfo]

  

   Returns a file list from the current directory matching the given search pattern.

  

   searchPattern: The search string,such as "*.txt".

   Returns: An array of type System.IO.FileInfo.
  """
  pass
 def GetFileSystemInfos(self,searchPattern=None,searchOption=None):
  """
  GetFileSystemInfos(self: DirectoryInfo) -> Array[FileSystemInfo]

  

   Returns an array of strongly typed System.IO.FileSystemInfo entries representing all the files 

    and subdirectories in a directory.

  

   Returns: An array of strongly typed System.IO.FileSystemInfo entries.

  GetFileSystemInfos(self: DirectoryInfo,searchPattern: str,searchOption: SearchOption) -> Array[FileSystemInfo]

  

   Retrieves an array of System.IO.FileSystemInfo objects that represent the files and 

    subdirectories matching the specified search criteria.

  

  

   searchPattern: The search string. The default pattern is "*",which returns all files and directories.

   searchOption: One of the enumeration values that specifies whether the search operation should include only 

    the current directory or all subdirectories. The default value is 

    System.IO.SearchOption.TopDirectoryOnly.

  

   Returns: An array of file system entries that match the search criteria.

  GetFileSystemInfos(self: DirectoryInfo,searchPattern: str) -> Array[FileSystemInfo]

  

   Retrieves an array of strongly typed System.IO.FileSystemInfo objects representing the files and 

    subdirectories that match the specified search criteria.

  

  

   searchPattern: The search string. For example,"System*" can be used to search for all directories that begin 

    with the word "System".

  

   Returns: An array of strongly typed FileSystemInfo objects matching the search criteria.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def MoveTo(self,destDirName):
  """
  MoveTo(self: DirectoryInfo,destDirName: str)

   Moves a System.IO.DirectoryInfo instance and its contents to a new path.

  

   destDirName: The name and path to which to move this directory. The destination cannot be another disk volume 

    or a directory with the identical name. It can be an existing directory to which you want to add 

    this directory as a subdirectory.
  """
  pass
 def SetAccessControl(self,directorySecurity):
  """
  SetAccessControl(self: DirectoryInfo,directorySecurity: DirectorySecurity)

   Applies access control list (ACL) entries described by a 

    System.Security.AccessControl.DirectorySecurity object to the directory described by the current 

    System.IO.DirectoryInfo object.

  

  

   directorySecurity: An object that describes an ACL entry to apply to the directory described by the path parameter.
  """
  pass
 def ToString(self):
  """
  ToString(self: DirectoryInfo) -> str

  

   Returns the original path that was passed by the user.

   Returns: Returns the original path that was passed by the user.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,path):
  """ __new__(cls: type,path: str) """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Exists=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the directory exists.



Get: Exists(self: DirectoryInfo) -> bool



"""

 FullName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FullName(self: DirectoryInfo) -> str



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of this System.IO.DirectoryInfo instance.



Get: Name(self: DirectoryInfo) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent directory of a specified subdirectory.



Get: Parent(self: DirectoryInfo) -> DirectoryInfo



"""

 Root=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the root portion of a path.



Get: Root(self: DirectoryInfo) -> DirectoryInfo



"""


 FullPath=None
 OriginalPath=None

