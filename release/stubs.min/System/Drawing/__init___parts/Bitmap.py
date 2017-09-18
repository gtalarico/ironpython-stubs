class Bitmap(Image,ISerializable,ICloneable,IDisposable):
 """
 Encapsulates a GDI+ bitmap,which consists of the pixel data for a graphics image and its attributes. A System.Drawing.Bitmap is an object used to work with images defined by pixel data.

 

 Bitmap(filename: str)

 Bitmap(filename: str,useIcm: bool)

 Bitmap(type: Type,resource: str)

 Bitmap(stream: Stream)

 Bitmap(stream: Stream,useIcm: bool)

 Bitmap(width: int,height: int,stride: int,format: PixelFormat,scan0: IntPtr)

 Bitmap(width: int,height: int,format: PixelFormat)

 Bitmap(width: int,height: int)

 Bitmap(width: int,height: int,g: Graphics)

 Bitmap(original: Image)

 Bitmap(original: Image,width: int,height: int)

 Bitmap(original: Image,newSize: Size)
 """
 def Clone(self,rect=None,format=None):
  """
  Clone(self: Bitmap,rect: RectangleF,format: PixelFormat) -> Bitmap

  

   Creates a copy of the section of this System.Drawing.Bitmap defined with a specified 

    System.Drawing.Imaging.PixelFormat enumeration.

  

  

   rect: Defines the portion of this System.Drawing.Bitmap to copy.

   format: Specifies the System.Drawing.Imaging.PixelFormat enumeration for the destination 

    System.Drawing.Bitmap.

  

   Returns: The System.Drawing.Bitmap that this method creates.

  Clone(self: Bitmap,rect: Rectangle,format: PixelFormat) -> Bitmap

  

   Creates a copy of the section of this System.Drawing.Bitmap defined by System.Drawing.Rectangle 

    structure and with a specified System.Drawing.Imaging.PixelFormat enumeration.

  

  

   rect: Defines the portion of this System.Drawing.Bitmap to copy. Coordinates are relative to this 

    System.Drawing.Bitmap.

  

   format: The pixel format for the new System.Drawing.Bitmap. This must specify a value that begins with 

    Format.

  

   Returns: The new System.Drawing.Bitmap that this method creates.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Image,disposing: bool)

   Releases the unmanaged resources used by the System.Drawing.Image and optionally releases the 

    managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 @staticmethod
 def FromHicon(hicon):
  """
  FromHicon(hicon: IntPtr) -> Bitmap

  

   Creates a System.Drawing.Bitmap from a Windows handle to an icon.

  

   hicon: A handle to an icon.

   Returns: The System.Drawing.Bitmap that this method creates.
  """
  pass
 @staticmethod
 def FromResource(hinstance,bitmapName):
  """
  FromResource(hinstance: IntPtr,bitmapName: str) -> Bitmap

  

   Creates a System.Drawing.Bitmap from the specified Windows resource.

  

   hinstance: A handle to an instance of the executable file that contains the resource.

   bitmapName: A string that contains the name of the resource bitmap.

   Returns: The System.Drawing.Bitmap that this method creates.
  """
  pass
 def GetHbitmap(self,background=None):
  """
  GetHbitmap(self: Bitmap,background: Color) -> IntPtr

  

   Creates a GDI bitmap object from this System.Drawing.Bitmap.

  

   background: A System.Drawing.Color structure that specifies the background color. This parameter is ignored 

    if the bitmap is totally opaque.

  

   Returns: A handle to the GDI bitmap object that this method creates.

  GetHbitmap(self: Bitmap) -> IntPtr

  

   Creates a GDI bitmap object from this System.Drawing.Bitmap.

   Returns: A handle to the GDI bitmap object that this method creates.
  """
  pass
 def GetHicon(self):
  """
  GetHicon(self: Bitmap) -> IntPtr

  

   Returns the handle to an icon.

   Returns: A Windows handle to an icon with the same image as the System.Drawing.Bitmap.
  """
  pass
 def GetPixel(self,x,y):
  """
  GetPixel(self: Bitmap,x: int,y: int) -> Color

  

   Gets the color of the specified pixel in this System.Drawing.Bitmap.

  

   x: The x-coordinate of the pixel to retrieve.

   y: The y-coordinate of the pixel to retrieve.

   Returns: A System.Drawing.Color structure that represents the color of the specified pixel.
  """
  pass
 def LockBits(self,rect,flags,format,bitmapData=None):
  """
  LockBits(self: Bitmap,rect: Rectangle,flags: ImageLockMode,format: PixelFormat,bitmapData: BitmapData) -> BitmapData

  

   Locks a System.Drawing.Bitmap into system memory

  

   rect: A rectangle structure that specifies the portion of the System.Drawing.Bitmap to lock.

   flags: One of the System.Drawing.Imaging.ImageLockMode values that specifies the access level 

    (read/write) for the System.Drawing.Bitmap.

  

   format: One of the System.Drawing.Imaging.PixelFormat values that specifies the data format of the 

    System.Drawing.Bitmap.

  

   bitmapData: A System.Drawing.Imaging.BitmapData that contains information about the lock operation.

   Returns: A System.Drawing.Imaging.BitmapData that contains information about the lock operation.

  LockBits(self: Bitmap,rect: Rectangle,flags: ImageLockMode,format: PixelFormat) -> BitmapData

  

   Locks a System.Drawing.Bitmap into system memory.

  

   rect: A System.Drawing.Rectangle structure that specifies the portion of the System.Drawing.Bitmap to 

    lock.

  

   flags: An System.Drawing.Imaging.ImageLockMode enumeration that specifies the access level (read/write) 

    for the System.Drawing.Bitmap.

  

   format: A System.Drawing.Imaging.PixelFormat enumeration that specifies the data format of this 

    System.Drawing.Bitmap.

  

   Returns: A System.Drawing.Imaging.BitmapData that contains information about this lock operation.
  """
  pass
 def MakeTransparent(self,transparentColor=None):
  """
  MakeTransparent(self: Bitmap,transparentColor: Color)

   Makes the specified color transparent for this System.Drawing.Bitmap.

  

   transparentColor: The System.Drawing.Color structure that represents the color to make transparent.

  MakeTransparent(self: Bitmap)

   Makes the default transparent color transparent for this System.Drawing.Bitmap.
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
 def SetPixel(self,x,y,color):
  """
  SetPixel(self: Bitmap,x: int,y: int,color: Color)

   Sets the color of the specified pixel in this System.Drawing.Bitmap.

  

   x: The x-coordinate of the pixel to set.

   y: The y-coordinate of the pixel to set.

   color: A System.Drawing.Color structure that represents the color to assign to the specified pixel.
  """
  pass
 def SetResolution(self,xDpi,yDpi):
  """
  SetResolution(self: Bitmap,xDpi: Single,yDpi: Single)

   Sets the resolution for this System.Drawing.Bitmap.

  

   xDpi: The horizontal resolution,in dots per inch,of the System.Drawing.Bitmap.

   yDpi: The vertical resolution,in dots per inch,of the System.Drawing.Bitmap.
  """
  pass
 def UnlockBits(self,bitmapdata):
  """
  UnlockBits(self: Bitmap,bitmapdata: BitmapData)

   Unlocks this System.Drawing.Bitmap from system memory.

  

   bitmapdata: A System.Drawing.Imaging.BitmapData that specifies information about the lock operation.
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
  __new__(cls: type,filename: str)

  __new__(cls: type,filename: str,useIcm: bool)

  __new__(cls: type,type: Type,resource: str)

  __new__(cls: type,stream: Stream)

  __new__(cls: type,stream: Stream,useIcm: bool)

  __new__(cls: type,width: int,height: int,stride: int,format: PixelFormat,scan0: IntPtr)

  __new__(cls: type,width: int,height: int,format: PixelFormat)

  __new__(cls: type,width: int,height: int)

  __new__(cls: type,width: int,height: int,g: Graphics)

  __new__(cls: type,original: Image)

  __new__(cls: type,original: Image,width: int,height: int)

  __new__(cls: type,original: Image,newSize: Size)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
