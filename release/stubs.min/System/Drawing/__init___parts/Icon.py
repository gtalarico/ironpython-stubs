class Icon(MarshalByRefObject,ISerializable,ICloneable,IDisposable):
 """
 Represents a Windows icon,which is a small bitmap image that is used to represent an object. Icons can be thought of as transparent bitmaps,although their size is determined by the system.

 

 Icon(original: Icon,size: Size)

 Icon(original: Icon,width: int,height: int)

 Icon(type: Type,resource: str)

 Icon(stream: Stream)

 Icon(stream: Stream,width: int,height: int)

 Icon(fileName: str)

 Icon(fileName: str,size: Size)

 Icon(fileName: str,width: int,height: int)

 Icon(stream: Stream,size: Size)
 """
 def Clone(self):
  """
  Clone(self: Icon) -> object

  

   Clones the System.Drawing.Icon,creating a duplicate image.

   Returns: An object that can be cast to an System.Drawing.Icon.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Icon)

   Releases all resources used by this System.Drawing.Icon.
  """
  pass
 @staticmethod
 def ExtractAssociatedIcon(filePath):
  """
  ExtractAssociatedIcon(filePath: str) -> Icon

  

   Returns an icon representation of an image that is contained in the specified file.

  

   filePath: The path to the file that contains an image.

   Returns: The System.Drawing.Icon representation of the image that is contained in the specified file.
  """
  pass
 @staticmethod
 def FromHandle(handle):
  """
  FromHandle(handle: IntPtr) -> Icon

  

   Creates a GDI+ System.Drawing.Icon from the specified Windows handle to an icon (HICON).

  

   handle: A Windows handle to an icon.

   Returns: The System.Drawing.Icon this method creates.
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
 def Save(self,outputStream):
  """
  Save(self: Icon,outputStream: Stream)

   Saves this System.Drawing.Icon to the specified output System.IO.Stream.

  

   outputStream: The System.IO.Stream to save to.
  """
  pass
 def ToBitmap(self):
  """
  ToBitmap(self: Icon) -> Bitmap

  

   Converts this System.Drawing.Icon to a GDI+ System.Drawing.Bitmap.

   Returns: A System.Drawing.Bitmap that represents the converted System.Drawing.Icon.
  """
  pass
 def ToString(self):
  """
  ToString(self: Icon) -> str

  

   Gets a human-readable string that describes the System.Drawing.Icon.

   Returns: A string that describes the System.Drawing.Icon.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,fileName: str)

  __new__(cls: type,fileName: str,size: Size)

  __new__(cls: type,fileName: str,width: int,height: int)

  __new__(cls: type,original: Icon,size: Size)

  __new__(cls: type,original: Icon,width: int,height: int)

  __new__(cls: type,type: Type,resource: str)

  __new__(cls: type,stream: Stream)

  __new__(cls: type,stream: Stream,size: Size)

  __new__(cls: type,stream: Stream,width: int,height: int)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Handle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Windows handle for this System.Drawing.Icon. This is not a copy of the handle; do not free it.



Get: Handle(self: Icon) -> IntPtr



"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the height of this System.Drawing.Icon.



Get: Height(self: Icon) -> int



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size of this System.Drawing.Icon.



Get: Size(self: Icon) -> Size



"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the width of this System.Drawing.Icon.



Get: Width(self: Icon) -> int



"""


