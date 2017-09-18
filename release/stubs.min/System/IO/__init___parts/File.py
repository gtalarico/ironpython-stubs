class File(object):
 """ Provides static methods for the creation,copying,deletion,moving,and opening of files,and aids in the creation of System.IO.FileStream objects. """
 @staticmethod
 def AppendAllLines(path,contents,encoding=None):
  """ AppendAllLines(path: str,contents: IEnumerable[str],encoding: Encoding)AppendAllLines(path: str,contents: IEnumerable[str]) """
  pass
 @staticmethod
 def AppendAllText(path,contents,encoding=None):
  """
  AppendAllText(path: str,contents: str,encoding: Encoding)

   Appends the specified string to the file,creating the file if it does not already exist.

  

   path: The file to append the specified string to.

   contents: The string to append to the file.

   encoding: The character encoding to use.

  AppendAllText(path: str,contents: str)

   Opens a file,appends the specified string to the file,and then closes the file. If the file 

    does not exist,this method creates a file,writes the specified string to the file,then closes 

    the file.

  

  

   path: The file to append the specified string to.

   contents: The string to append to the file.
  """
  pass
 @staticmethod
 def AppendText(path):
  """
  AppendText(path: str) -> StreamWriter

  

   Creates a System.IO.StreamWriter that appends UTF-8 encoded text to an existing file.

  

   path: The path to the file to append to.

   Returns: A StreamWriter that appends UTF-8 encoded text to an existing file.
  """
  pass
 @staticmethod
 def Copy(sourceFileName,destFileName,overwrite=None):
  """
  Copy(sourceFileName: str,destFileName: str,overwrite: bool)

   Copies an existing file to a new file. Overwriting a file of the same name is allowed.

  

   sourceFileName: The file to copy.

   destFileName: The name of the destination file. This cannot be a directory.

   overwrite: true if the destination file can be overwritten; otherwise,false.

  Copy(sourceFileName: str,destFileName: str)

   Copies an existing file to a new file. Overwriting a file of the same name is not allowed.

  

   sourceFileName: The file to copy.

   destFileName: The name of the destination file. This cannot be a directory or an existing file.
  """
  pass
 @staticmethod
 def Create(path,bufferSize=None,options=None,fileSecurity=None):
  """
  Create(path: str,bufferSize: int,options: FileOptions) -> FileStream

  

   Creates or overwrites the specified file,specifying a buffer size and a System.IO.FileOptions 

    value that describes how to create or overwrite the file.

  

  

   path: The name of the file.

   bufferSize: The number of bytes buffered for reads and writes to the file.

   options: One of the System.IO.FileOptions values that describes how to create or overwrite the file.

   Returns: A new file with the specified buffer size.

  Create(path: str,bufferSize: int,options: FileOptions,fileSecurity: FileSecurity) -> FileStream

  

   Creates or overwrites the specified file with the specified buffer size,file options,and file 

    security.

  

  

   path: The name of the file.

   bufferSize: The number of bytes buffered for reads and writes to the file.

   options: One of the System.IO.FileOptions values that describes how to create or overwrite the file.

   fileSecurity: One of the System.Security.AccessControl.FileSecurity values that determines the access control 

    and audit security for the file.

  

   Returns: A new file with the specified buffer size,file options,and file security.

  Create(path: str) -> FileStream

  

   Creates or overwrites a file in the specified path.

  

   path: The path and name of the file to create.

   Returns: A System.IO.FileStream that provides read/write access to the file specified in path.

  Create(path: str,bufferSize: int) -> FileStream

  

   Creates or overwrites the specified file.

  

   path: The name of the file.

   bufferSize: The number of bytes buffered for reads and writes to the file.

   Returns: A System.IO.FileStream with the specified buffer size that provides read/write access to the 

    file specified in path.
  """
  pass
 @staticmethod
 def CreateText(path):
  """
  CreateText(path: str) -> StreamWriter

  

   Creates or opens a file for writing UTF-8 encoded text.

  

   path: The file to be opened for writing.

   Returns: A System.IO.StreamWriter that writes to the specified file using UTF-8 encoding.
  """
  pass
 @staticmethod
 def Decrypt(path):
  """
  Decrypt(path: str)

   Decrypts a file that was encrypted by the current account using the 

    System.IO.File.Encrypt(System.String) method.

  

  

   path: A path that describes a file to decrypt.
  """
  pass
 @staticmethod
 def Delete(path):
  """
  Delete(path: str)

   Deletes the specified file.

  

   path: The name of the file to be deleted. Wildcard characters are not supported.
  """
  pass
 @staticmethod
 def Encrypt(path):
  """
  Encrypt(path: str)

   Encrypts a file so that only the account used to encrypt the file can decrypt it.

  

   path: A path that describes a file to encrypt.
  """
  pass
 @staticmethod
 def Exists(path):
  """
  Exists(path: str) -> bool

  

   Determines whether the specified file exists.

  

   path: The file to check.

   Returns: true if the caller has the required permissions and path contains the name of an existing file; 

    otherwise,false. This method also returns false if path is null,an invalid path,or a 

    zero-length string. If the caller does not have sufficient permissions to read the specified 

    file,no exception is thrown and the method returns false regardless of the existence of path.
  """
  pass
 @staticmethod
 def GetAccessControl(path,includeSections=None):
  """
  GetAccessControl(path: str,includeSections: AccessControlSections) -> FileSecurity

  

   Gets a System.Security.AccessControl.FileSecurity object that encapsulates the specified type of 

    access control list (ACL) entries for a particular file.

  

  

   path: The path to a file containing a System.Security.AccessControl.FileSecurity object that describes 

    the file's access control list (ACL) information.

  

   includeSections: One of the System.Security.AccessControl.AccessControlSections values that specifies the type of 

    access control list (ACL) information to receive.

  

   Returns: A System.Security.AccessControl.FileSecurity object that encapsulates the access control rules 

    for the file described by the path parameter.

  

  GetAccessControl(path: str) -> FileSecurity

  

   Gets a System.Security.AccessControl.FileSecurity object that encapsulates the access control 

    list (ACL) entries for a specified file.

  

  

   path: The path to a file containing a System.Security.AccessControl.FileSecurity object that describes 

    the file's access control list (ACL) information.

  

   Returns: A System.Security.AccessControl.FileSecurity object that encapsulates the access control rules 

    for the file described by the path parameter.
  """
  pass
 @staticmethod
 def GetAttributes(path):
  """
  GetAttributes(path: str) -> FileAttributes

  

   Gets the System.IO.FileAttributes of the file on the path.

  

   path: The path to the file.

   Returns: The System.IO.FileAttributes of the file on the path.
  """
  pass
 @staticmethod
 def GetCreationTime(path):
  """
  GetCreationTime(path: str) -> DateTime

  

   Returns the creation date and time of the specified file or directory.

  

   path: The file or directory for which to obtain creation date and time information.

   Returns: A System.DateTime structure set to the creation date and time for the specified file or 

    directory. This value is expressed in local time.
  """
  pass
 @staticmethod
 def GetCreationTimeUtc(path):
  """
  GetCreationTimeUtc(path: str) -> DateTime

  

   Returns the creation date and time,in coordinated universal time (UTC),of the specified file 

    or directory.

  

  

   path: The file or directory for which to obtain creation date and time information.

   Returns: A System.DateTime structure set to the creation date and time for the specified file or 

    directory. This value is expressed in UTC time.
  """
  pass
 @staticmethod
 def GetLastAccessTime(path):
  """
  GetLastAccessTime(path: str) -> DateTime

  

   Returns the date and time the specified file or directory was last accessed.

  

   path: The file or directory for which to obtain access date and time information.

   Returns: A System.DateTime structure set to the date and time that the specified file or directory was 

    last accessed. This value is expressed in local time.
  """
  pass
 @staticmethod
 def GetLastAccessTimeUtc(path):
  """
  GetLastAccessTimeUtc(path: str) -> DateTime

  

   Returns the date and time,in coordinated universal time (UTC),that the specified file or 

    directory was last accessed.

  

  

   path: The file or directory for which to obtain access date and time information.

   Returns: A System.DateTime structure set to the date and time that the specified file or directory was 

    last accessed. This value is expressed in UTC time.
  """
  pass
 @staticmethod
 def GetLastWriteTime(path):
  """
  GetLastWriteTime(path: str) -> DateTime

  

   Returns the date and time the specified file or directory was last written to.

  

   path: The file or directory for which to obtain write date and time information.

   Returns: A System.DateTime structure set to the date and time that the specified file or directory was 

    last written to. This value is expressed in local time.
  """
  pass
 @staticmethod
 def GetLastWriteTimeUtc(path):
  """
  GetLastWriteTimeUtc(path: str) -> DateTime

  

   Returns the date and time,in coordinated universal time (UTC),that the specified file or 

    directory was last written to.

  

  

   path: The file or directory for which to obtain write date and time information.

   Returns: A System.DateTime structure set to the date and time that the specified file or directory was 

    last written to. This value is expressed in UTC time.
  """
  pass
 @staticmethod
 def Move(sourceFileName,destFileName):
  """
  Move(sourceFileName: str,destFileName: str)

   Moves a specified file to a new location,providing the option to specify a new file name.

  

   sourceFileName: The name of the file to move.

   destFileName: The new path for the file.
  """
  pass
 @staticmethod
 def Open(path,mode,access=None,share=None):
  """
  Open(path: str,mode: FileMode,access: FileAccess,share: FileShare) -> FileStream

  

   Opens a System.IO.FileStream on the specified path,having the specified mode with read,write,

    or read/write access and the specified sharing option.

  

  

   path: The file to open.

   mode: A System.IO.FileMode value that specifies whether a file is created if one does not exist,and 

    determines whether the contents of existing files are retained or overwritten.

  

   access: A System.IO.FileAccess value that specifies the operations that can be performed on the file.

   share: A System.IO.FileShare value specifying the type of access other threads have to the file.

   Returns: A System.IO.FileStream on the specified path,having the specified mode with read,write,or 

    read/write access and the specified sharing option.

  

  Open(path: str,mode: FileMode,access: FileAccess) -> FileStream

  

   Opens a System.IO.FileStream on the specified path,with the specified mode and access.

  

   path: The file to open.

   mode: A System.IO.FileMode value that specifies whether a file is created if one does not exist,and 

    determines whether the contents of existing files are retained or overwritten.

  

   access: A System.IO.FileAccess value that specifies the operations that can be performed on the file.

   Returns: An unshared System.IO.FileStream that provides access to the specified file,with the specified 

    mode and access.

  

  Open(path: str,mode: FileMode) -> FileStream

  

   Opens a System.IO.FileStream on the specified path with read/write access.

  

   path: The file to open.

   mode: A System.IO.FileMode value that specifies whether a file is created if one does not exist,and 

    determines whether the contents of existing files are retained or overwritten.

  

   Returns: A System.IO.FileStream opened in the specified mode and path,with read/write access and not 

    shared.
  """
  pass
 @staticmethod
 def OpenRead(path):
  """
  OpenRead(path: str) -> FileStream

  

   Opens an existing file for reading.

  

   path: The file to be opened for reading.

   Returns: A read-only System.IO.FileStream on the specified path.
  """
  pass
 @staticmethod
 def OpenText(path):
  """
  OpenText(path: str) -> StreamReader

  

   Opens an existing UTF-8 encoded text file for reading.

  

   path: The file to be opened for reading.

   Returns: A System.IO.StreamReader on the specified path.
  """
  pass
 @staticmethod
 def OpenWrite(path):
  """
  OpenWrite(path: str) -> FileStream

  

   Opens an existing file or creates a new file for writing.

  

   path: The file to be opened for writing.

   Returns: An unshared System.IO.FileStream object on the specified path with System.IO.FileAccess.Write 

    access.
  """
  pass
 @staticmethod
 def ReadAllBytes(path):
  """
  ReadAllBytes(path: str) -> Array[Byte]

  

   Opens a binary file,reads the contents of the file into a byte array,and then closes the file.

  

   path: The file to open for reading.

   Returns: A byte array containing the contents of the file.
  """
  pass
 @staticmethod
 def ReadAllLines(path,encoding=None):
  """
  ReadAllLines(path: str,encoding: Encoding) -> Array[str]

  

   Opens a file,reads all lines of the file with the specified encoding,and then closes the file.

  

   path: The file to open for reading.

   encoding: The encoding applied to the contents of the file.

   Returns: A string array containing all lines of the file.

  ReadAllLines(path: str) -> Array[str]

  

   Opens a text file,reads all lines of the file,and then closes the file.

  

   path: The file to open for reading.

   Returns: A string array containing all lines of the file.
  """
  pass
 @staticmethod
 def ReadAllText(path,encoding=None):
  """
  ReadAllText(path: str,encoding: Encoding) -> str

  

   Opens a file,reads all lines of the file with the specified encoding,and then closes the file.

  

   path: The file to open for reading.

   encoding: The encoding applied to the contents of the file.

   Returns: A string containing all lines of the file.

  ReadAllText(path: str) -> str

  

   Opens a text file,reads all lines of the file,and then closes the file.

  

   path: The file to open for reading.

   Returns: A string containing all lines of the file.
  """
  pass
 @staticmethod
 def ReadLines(path,encoding=None):
  """
  ReadLines(path: str,encoding: Encoding) -> IEnumerable[str]

  

   Read the lines of a file that has a specified encoding.

  

   path: The file to read.

   encoding: The encoding that is applied to the contents of the file.

   Returns: All the lines of the file,or the lines that are the result of a query.

  ReadLines(path: str) -> IEnumerable[str]

  

   Reads the lines of a file.

  

   path: The file to read.

   Returns: All the lines of the file,or the lines that are the result of a query.
  """
  pass
 @staticmethod
 def Replace(sourceFileName,destinationFileName,destinationBackupFileName,ignoreMetadataErrors=None):
  """
  Replace(sourceFileName: str,destinationFileName: str,destinationBackupFileName: str,ignoreMetadataErrors: bool)

   Replaces the contents of a specified file with the contents of another file,deleting the 

    original file,and creating a backup of the replaced file and optionally ignores merge errors.

  

  

   sourceFileName: The name of a file that replaces the file specified by destinationFileName.

   destinationFileName: The name of the file being replaced.

   destinationBackupFileName: The name of the backup file.

   ignoreMetadataErrors: true to ignore merge errors (such as attributes and access control lists (ACLs)) from the 

    replaced file to the replacement file; otherwise,false.

  

  Replace(sourceFileName: str,destinationFileName: str,destinationBackupFileName: str)

   Replaces the contents of a specified file with the contents of another file,deleting the 

    original file,and creating a backup of the replaced file.

  

  

   sourceFileName: The name of a file that replaces the file specified by destinationFileName.

   destinationFileName: The name of the file being replaced.

   destinationBackupFileName: The name of the backup file.
  """
  pass
 @staticmethod
 def SetAccessControl(path,fileSecurity):
  """
  SetAccessControl(path: str,fileSecurity: FileSecurity)

   Applies access control list (ACL) entries described by a 

    System.Security.AccessControl.FileSecurity object to the specified file.

  

  

   path: A file to add or remove access control list (ACL) entries from.

   fileSecurity: A System.Security.AccessControl.FileSecurity object that describes an ACL entry to apply to the 

    file described by the path parameter.
  """
  pass
 @staticmethod
 def SetAttributes(path,fileAttributes):
  """
  SetAttributes(path: str,fileAttributes: FileAttributes)

   Sets the specified System.IO.FileAttributes of the file on the specified path.

  

   path: The path to the file.

   fileAttributes: A bitwise combination of the enumeration values.
  """
  pass
 @staticmethod
 def SetCreationTime(path,creationTime):
  """
  SetCreationTime(path: str,creationTime: DateTime)

   Sets the date and time the file was created.

  

   path: The file for which to set the creation date and time information.

   creationTime: A System.DateTime containing the value to set for the creation date and time of path. This value 

    is expressed in local time.
  """
  pass
 @staticmethod
 def SetCreationTimeUtc(path,creationTimeUtc):
  """
  SetCreationTimeUtc(path: str,creationTimeUtc: DateTime)

   Sets the date and time,in coordinated universal time (UTC),that the file was created.

  

   path: The file for which to set the creation date and time information.

   creationTimeUtc: A System.DateTime containing the value to set for the creation date and time of path. This value 

    is expressed in UTC time.
  """
  pass
 @staticmethod
 def SetLastAccessTime(path,lastAccessTime):
  """
  SetLastAccessTime(path: str,lastAccessTime: DateTime)

   Sets the date and time the specified file was last accessed.

  

   path: The file for which to set the access date and time information.

   lastAccessTime: A System.DateTime containing the value to set for the last access date and time of path. This 

    value is expressed in local time.
  """
  pass
 @staticmethod
 def SetLastAccessTimeUtc(path,lastAccessTimeUtc):
  """
  SetLastAccessTimeUtc(path: str,lastAccessTimeUtc: DateTime)

   Sets the date and time,in coordinated universal time (UTC),that the specified file was last 

    accessed.

  

  

   path: The file for which to set the access date and time information.

   lastAccessTimeUtc: A System.DateTime containing the value to set for the last access date and time of path. This 

    value is expressed in UTC time.
  """
  pass
 @staticmethod
 def SetLastWriteTime(path,lastWriteTime):
  """
  SetLastWriteTime(path: str,lastWriteTime: DateTime)

   Sets the date and time that the specified file was last written to.

  

   path: The file for which to set the date and time information.

   lastWriteTime: A System.DateTime containing the value to set for the last write date and time of path. This 

    value is expressed in local time.
  """
  pass
 @staticmethod
 def SetLastWriteTimeUtc(path,lastWriteTimeUtc):
  """
  SetLastWriteTimeUtc(path: str,lastWriteTimeUtc: DateTime)

   Sets the date and time,in coordinated universal time (UTC),that the specified file was last 

    written to.

  

  

   path: The file for which to set the date and time information.

   lastWriteTimeUtc: A System.DateTime containing the value to set for the last write date and time of path. This 

    value is expressed in UTC time.
  """
  pass
 @staticmethod
 def WriteAllBytes(path,bytes):
  """
  WriteAllBytes(path: str,bytes: Array[Byte])

   Creates a new file,writes the specified byte array to the file,and then closes the file. If 

    the target file already exists,it is overwritten.

  

  

   path: The file to write to.

   bytes: The bytes to write to the file.
  """
  pass
 @staticmethod
 def WriteAllLines(path,contents,encoding=None):
  """
  WriteAllLines(path: str,contents: IEnumerable[str])WriteAllLines(path: str,contents: IEnumerable[str],encoding: Encoding)WriteAllLines(path: str,contents: Array[str])

   Creates a new file,write the specified string array to the file,and then closes the file.

  

   path: The file to write to.

   contents: The string array to write to the file.

  WriteAllLines(path: str,contents: Array[str],encoding: Encoding)

   Creates a new file,writes the specified string array to the file by using the specified 

    encoding,and then closes the file.

  

  

   path: The file to write to.

   contents: The string array to write to the file.

   encoding: An System.Text.Encoding object that represents the character encoding applied to the string 

    array.
  """
  pass
 @staticmethod
 def WriteAllText(path,contents,encoding=None):
  """
  WriteAllText(path: str,contents: str,encoding: Encoding)

   Creates a new file,writes the specified string to the file using the specified encoding,and 

    then closes the file. If the target file already exists,it is overwritten.

  

  

   path: The file to write to.

   contents: The string to write to the file.

   encoding: The encoding to apply to the string.

  WriteAllText(path: str,contents: str)

   Creates a new file,writes the specified string to the file,and then closes the file. If the 

    target file already exists,it is overwritten.

  

  

   path: The file to write to.

   contents: The string to write to the file.
  """
  pass
 __all__=[
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

