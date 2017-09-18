class FileInfo(FileSystemInfo,ISerializable):
 """
 Provides properties and instance methods for the creation,copying,deletion,moving,and opening of files,and aids in the creation of System.IO.FileStream objects. This class cannot be inherited.

 

 FileInfo(fileName: str)
 """
 def AppendText(self):
  """
  AppendText(self: FileInfo) -> StreamWriter

  

   Creates a System.IO.StreamWriter that appends text to the file represented by this instance of 

    the System.IO.FileInfo.

  

   Returns: A new StreamWriter.
  """
  pass
 def CopyTo(self,destFileName,overwrite=None):
  """
  CopyTo(self: FileInfo,destFileName: str,overwrite: bool) -> FileInfo

  

   Copies an existing file to a new file,allowing the overwriting of an existing file.

  

   destFileName: The name of the new file to copy to.

   overwrite: true to allow an existing file to be overwritten; otherwise,false.

   Returns: A new file,or an overwrite of an existing file if overwrite is true. If the file exists and 

    overwrite is false,an System.IO.IOException is thrown.

  

  CopyTo(self: FileInfo,destFileName: str) -> FileInfo

  

   Copies an existing file to a new file,disallowing the overwriting of an existing file.

  

   destFileName: The name of the new file to copy to.

   Returns: A new file with a fully qualified path.
  """
  pass
 def Create(self):
  """
  Create(self: FileInfo) -> FileStream

  

   Creates a file.

   Returns: A new file.
  """
  pass
 def CreateText(self):
  """
  CreateText(self: FileInfo) -> StreamWriter

  

   Creates a System.IO.StreamWriter that writes a new text file.

   Returns: A new StreamWriter.
  """
  pass
 def Decrypt(self):
  """
  Decrypt(self: FileInfo)

   Decrypts a file that was encrypted by the current account using the System.IO.FileInfo.Encrypt 

    method.
  """
  pass
 def Delete(self):
  """
  Delete(self: FileInfo)

   Permanently deletes a file.
  """
  pass
 def Encrypt(self):
  """
  Encrypt(self: FileInfo)

   Encrypts a file so that only the account used to encrypt the file can decrypt it.
  """
  pass
 def GetAccessControl(self,includeSections=None):
  """
  GetAccessControl(self: FileInfo,includeSections: AccessControlSections) -> FileSecurity

  

   Gets a System.Security.AccessControl.FileSecurity object that encapsulates the specified type of 

    access control list (ACL) entries for the file described by the current System.IO.FileInfo 

    object.

  

  

   includeSections: One of the System.Security.AccessControl.AccessControlSections values that specifies which group 

    of access control entries to retrieve.

  

   Returns: A System.Security.AccessControl.FileSecurity object that encapsulates the access control rules 

    for the current file.

  

  GetAccessControl(self: FileInfo) -> FileSecurity

  

   Gets a System.Security.AccessControl.FileSecurity object that encapsulates the access control 

    list (ACL) entries for the file described by the current System.IO.FileInfo object.

  

   Returns: A System.Security.AccessControl.FileSecurity object that encapsulates the access control rules 

    for the current file.
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
 def MoveTo(self,destFileName):
  """
  MoveTo(self: FileInfo,destFileName: str)

   Moves a specified file to a new location,providing the option to specify a new file name.

  

   destFileName: The path to move the file to,which can specify a different file name.
  """
  pass
 def Open(self,mode,access=None,share=None):
  """
  Open(self: FileInfo,mode: FileMode,access: FileAccess,share: FileShare) -> FileStream

  

   Opens a file in the specified mode with read,write,or read/write access and the specified 

    sharing option.

  

  

   mode: A System.IO.FileMode constant specifying the mode (for example,Open or Append) in which to open 

    the file.

  

   access: A System.IO.FileAccess constant specifying whether to open the file with Read,Write,or 

    ReadWrite file access.

  

   share: A System.IO.FileShare constant specifying the type of access other FileStream objects have to 

    this file.

  

   Returns: A System.IO.FileStream object opened with the specified mode,access,and sharing options.

  Open(self: FileInfo,mode: FileMode,access: FileAccess) -> FileStream

  

   Opens a file in the specified mode with read,write,or read/write access.

  

   mode: A System.IO.FileMode constant specifying the mode (for example,Open or Append) in which to open 

    the file.

  

   access: A System.IO.FileAccess constant specifying whether to open the file with Read,Write,or 

    ReadWrite file access.

  

   Returns: A System.IO.FileStream object opened in the specified mode and access,and unshared.

  Open(self: FileInfo,mode: FileMode) -> FileStream

  

   Opens a file in the specified mode.

  

   mode: A System.IO.FileMode constant specifying the mode (for example,Open or Append) in which to open 

    the file.

  

   Returns: A file opened in the specified mode,with read/write access and unshared.
  """
  pass
 def OpenRead(self):
  """
  OpenRead(self: FileInfo) -> FileStream

  

   Creates a read-only System.IO.FileStream.

   Returns: A new read-only System.IO.FileStream object.
  """
  pass
 def OpenText(self):
  """
  OpenText(self: FileInfo) -> StreamReader

  

   Creates a System.IO.StreamReader with UTF8 encoding that reads from an existing text file.

   Returns: A new StreamReader with UTF8 encoding.
  """
  pass
 def OpenWrite(self):
  """
  OpenWrite(self: FileInfo) -> FileStream

  

   Creates a write-only System.IO.FileStream.

   Returns: A write-only unshared System.IO.FileStream object for a new or existing file.
  """
  pass
 def Replace(self,destinationFileName,destinationBackupFileName,ignoreMetadataErrors=None):
  """
  Replace(self: FileInfo,destinationFileName: str,destinationBackupFileName: str,ignoreMetadataErrors: bool) -> FileInfo

  

   Replaces the contents of a specified file with the file described by the current 

    System.IO.FileInfo object,deleting the original file,and creating a backup of the replaced 

    file.  Also specifies whether to ignore merge errors.

  

  

   destinationFileName: The name of a file to replace with the current file.

   destinationBackupFileName: The name of a file with which to create a backup of the file described by the destFileName 

    parameter.

  

   ignoreMetadataErrors: true to ignore merge errors (such as attributes and ACLs) from the replaced file to the 

    replacement file; otherwise false.

  

   Returns: A System.IO.FileInfo object that encapsulates information about the file described by the 

    destFileName parameter.

  

  Replace(self: FileInfo,destinationFileName: str,destinationBackupFileName: str) -> FileInfo

  

   Replaces the contents of a specified file with the file described by the current 

    System.IO.FileInfo object,deleting the original file,and creating a backup of the replaced 

    file.

  

  

   destinationFileName: The name of a file to replace with the current file.

   destinationBackupFileName: The name of a file with which to create a backup of the file described by the destFileName 

    parameter.

  

   Returns: A System.IO.FileInfo object that encapsulates information about the file described by the 

    destFileName parameter.
  """
  pass
 def SetAccessControl(self,fileSecurity):
  """
  SetAccessControl(self: FileInfo,fileSecurity: FileSecurity)

   Applies access control list (ACL) entries described by a 

    System.Security.AccessControl.FileSecurity object to the file described by the current 

    System.IO.FileInfo object.

  

  

   fileSecurity: A System.Security.AccessControl.FileSecurity object that describes an access control list (ACL) 

    entry to apply to the current file.
  """
  pass
 def ToString(self):
  """
  ToString(self: FileInfo) -> str

  

   Returns the path as a string.

   Returns: A string representing the path.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,fileName):
  """ __new__(cls: type,fileName: str) """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Directory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an instance of the parent directory.



Get: Directory(self: FileInfo) -> DirectoryInfo



"""

 DirectoryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a string representing the directory's full path.



Get: DirectoryName(self: FileInfo) -> str



"""

 Exists=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether a file exists.



Get: Exists(self: FileInfo) -> bool



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines if the current file is read only.



Get: IsReadOnly(self: FileInfo) -> bool



Set: IsReadOnly(self: FileInfo)=value

"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size,in bytes,of the current file.



Get: Length(self: FileInfo) -> Int64



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the file.



Get: Name(self: FileInfo) -> str



"""


 FullPath=None
 OriginalPath=None

