class FileSystemInfo(MarshalByRefObject,ISerializable):
 """ Provides the base class for both System.IO.FileInfo and System.IO.DirectoryInfo objects. """
 def Delete(self):
  """
  Delete(self: FileSystemInfo)

   Deletes a file or directory.
  """
  pass
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: FileSystemInfo,info: SerializationInfo,context: StreamingContext)

   Sets the System.Runtime.Serialization.SerializationInfo object with the file name and additional 

    exception information.

  

  

   info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about 

    the exception being thrown.

  

   context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the 

    source or destination.
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
 def Refresh(self):
  """
  Refresh(self: FileSystemInfo)

   Refreshes the state of the object.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 Attributes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the attributes for the current file or directory.



Get: Attributes(self: FileSystemInfo) -> FileAttributes



Set: Attributes(self: FileSystemInfo)=value

"""

 CreationTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the creation time of the current file or directory.



Get: CreationTime(self: FileSystemInfo) -> DateTime



Set: CreationTime(self: FileSystemInfo)=value

"""

 CreationTimeUtc=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the creation time,in coordinated universal time (UTC),of the current file or directory.



Get: CreationTimeUtc(self: FileSystemInfo) -> DateTime



Set: CreationTimeUtc(self: FileSystemInfo)=value

"""

 Exists=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the file or directory exists.



Get: Exists(self: FileSystemInfo) -> bool



"""

 Extension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the string representing the extension part of the file.



Get: Extension(self: FileSystemInfo) -> str



"""

 FullName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the full path of the directory or file.



Get: FullName(self: FileSystemInfo) -> str



"""

 LastAccessTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the time the current file or directory was last accessed.



Get: LastAccessTime(self: FileSystemInfo) -> DateTime



Set: LastAccessTime(self: FileSystemInfo)=value

"""

 LastAccessTimeUtc=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the time,in coordinated universal time (UTC),that the current file or directory was last accessed.



Get: LastAccessTimeUtc(self: FileSystemInfo) -> DateTime



Set: LastAccessTimeUtc(self: FileSystemInfo)=value

"""

 LastWriteTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the time when the current file or directory was last written to.



Get: LastWriteTime(self: FileSystemInfo) -> DateTime



Set: LastWriteTime(self: FileSystemInfo)=value

"""

 LastWriteTimeUtc=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the time,in coordinated universal time (UTC),when the current file or directory was last written to.



Get: LastWriteTimeUtc(self: FileSystemInfo) -> DateTime



Set: LastWriteTimeUtc(self: FileSystemInfo)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """For files,gets the name of the file. For directories,gets the name of the last directory in the hierarchy if a hierarchy exists. Otherwise,the Name property gets the name of the directory.



Get: Name(self: FileSystemInfo) -> str



"""


 FullPath=None
 OriginalPath=None

