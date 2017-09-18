class Image(MarshalByRefObject,ISerializable,ICloneable,IDisposable):
 """ An abstract base class that provides functionality for the System.Drawing.Bitmap and System.Drawing.Imaging.Metafile descended classes. """
 def Clone(self):
  """
  Clone(self: Image) -> object

  

   Creates an exact copy of this System.Drawing.Image.

   Returns: The System.Drawing.Image this method creates,cast as an object.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Image)

   Releases all resources used by this System.Drawing.Image.
  """
  pass
 @staticmethod
 def FromFile(filename,useEmbeddedColorManagement=None):
  """
  FromFile(filename: str,useEmbeddedColorManagement: bool) -> Image

  

   Creates an System.Drawing.Image from the specified file using embedded color management 

    information in that file.

  

  

   filename: A string that contains the name of the file from which to create the System.Drawing.Image.

   useEmbeddedColorManagement: Set to true to use color management information embedded in the image file; otherwise,false.

   Returns: The System.Drawing.Image this method creates.

  FromFile(filename: str) -> Image

  

   Creates an System.Drawing.Image from the specified file.

  

   filename: A string that contains the name of the file from which to create the System.Drawing.Image.

   Returns: The System.Drawing.Image this method creates.
  """
  pass
 @staticmethod
 def FromHbitmap(hbitmap,hpalette=None):
  """
  FromHbitmap(hbitmap: IntPtr,hpalette: IntPtr) -> Bitmap

  

   Creates a System.Drawing.Bitmap from a handle to a GDI bitmap and a handle to a GDI palette.

  

   hbitmap: The GDI bitmap handle from which to create the System.Drawing.Bitmap.

   hpalette: A handle to a GDI palette used to define the bitmap colors if the bitmap specified in the 

    hBitmap parameter is not a device-independent bitmap (DIB).

  

   Returns: The System.Drawing.Bitmap this method creates.

  FromHbitmap(hbitmap: IntPtr) -> Bitmap

  

   Creates a System.Drawing.Bitmap from a handle to a GDI bitmap.

  

   hbitmap: The GDI bitmap handle from which to create the System.Drawing.Bitmap.

   Returns: The System.Drawing.Bitmap this method creates.
  """
  pass
 @staticmethod
 def FromStream(stream,useEmbeddedColorManagement=None,validateImageData=None):
  """
  FromStream(stream: Stream,useEmbeddedColorManagement: bool,validateImageData: bool) -> Image

  

   Creates an System.Drawing.Image from the specified data stream,optionally using embedded color 

    management information and validating the image data.

  

  

   stream: A System.IO.Stream that contains the data for this System.Drawing.Image.

   useEmbeddedColorManagement: true to use color management information embedded in the data stream; otherwise,false.

   validateImageData: true to validate the image data; otherwise,false.

   Returns: The System.Drawing.Image this method creates.

  FromStream(stream: Stream,useEmbeddedColorManagement: bool) -> Image

  

   Creates an System.Drawing.Image from the specified data stream,optionally using embedded color 

    management information in that stream.

  

  

   stream: A System.IO.Stream that contains the data for this System.Drawing.Image.

   useEmbeddedColorManagement: true to use color management information embedded in the data stream; otherwise,false.

   Returns: The System.Drawing.Image this method creates.

  FromStream(stream: Stream) -> Image

  

   Creates an System.Drawing.Image from the specified data stream.

  

   stream: A System.IO.Stream that contains the data for this System.Drawing.Image.

   Returns: The System.Drawing.Image this method creates.
  """
  pass
 def GetBounds(self,pageUnit):
  """
  GetBounds(self: Image,pageUnit: GraphicsUnit) -> (RectangleF,GraphicsUnit)

  

   Gets the bounds of the image in the specified unit.

  

   pageUnit: One of the System.Drawing.GraphicsUnit values indicating the unit of measure for the bounding 

    rectangle.

  

   Returns: The System.Drawing.RectangleF that represents the bounds of the image,in the specified unit.
  """
  pass
 def GetEncoderParameterList(self,encoder):
  """
  GetEncoderParameterList(self: Image,encoder: Guid) -> EncoderParameters

  

   Returns information about the parameters supported by the specified image encoder.

  

   encoder: A GUID that specifies the image encoder.

   Returns: An System.Drawing.Imaging.EncoderParameters that contains an array of 

    System.Drawing.Imaging.EncoderParameter objects. Each System.Drawing.Imaging.EncoderParameter 

    contains information about one of the parameters supported by the specified image encoder.
  """
  pass
 def GetFrameCount(self,dimension):
  """
  GetFrameCount(self: Image,dimension: FrameDimension) -> int

  

   Returns the number of frames of the specified dimension.

  

   dimension: A System.Drawing.Imaging.FrameDimension that specifies the identity of the dimension type.

   Returns: The number of frames in the specified dimension.
  """
  pass
 @staticmethod
 def GetPixelFormatSize(pixfmt):
  """
  GetPixelFormatSize(pixfmt: PixelFormat) -> int

  

   Returns the color depth,in number of bits per pixel,of the specified pixel format.

  

   pixfmt: The System.Drawing.Imaging.PixelFormat member that specifies the format for which to find the 

    size.

  

   Returns: The color depth of the specified pixel format.
  """
  pass
 def GetPropertyItem(self,propid):
  """
  GetPropertyItem(self: Image,propid: int) -> PropertyItem

  

   Gets the specified property item from this System.Drawing.Image.

  

   propid: The ID of the property item to get.

   Returns: The System.Drawing.Imaging.PropertyItem this method gets.
  """
  pass
 def GetThumbnailImage(self,thumbWidth,thumbHeight,callback,callbackData):
  """ GetThumbnailImage(self: Image,thumbWidth: int,thumbHeight: int,callback: GetThumbnailImageAbort,callbackData: IntPtr) -> Image """
  pass
 @staticmethod
 def IsAlphaPixelFormat(pixfmt):
  """
  IsAlphaPixelFormat(pixfmt: PixelFormat) -> bool

  

   Returns a value that indicates whether the pixel format for this System.Drawing.Image contains 

    alpha information.

  

  

   pixfmt: The System.Drawing.Imaging.PixelFormat to test.

   Returns: true if pixfmt contains alpha information; otherwise,false.
  """
  pass
 @staticmethod
 def IsCanonicalPixelFormat(pixfmt):
  """
  IsCanonicalPixelFormat(pixfmt: PixelFormat) -> bool

  

   Returns a value that indicates whether the pixel format is 32 bits per pixel.

  

   pixfmt: The System.Drawing.Imaging.PixelFormat to test.

   Returns: true if pixfmt is canonical; otherwise,false.
  """
  pass
 @staticmethod
 def IsExtendedPixelFormat(pixfmt):
  """
  IsExtendedPixelFormat(pixfmt: PixelFormat) -> bool

  

   Returns a value that indicates whether the pixel format is 64 bits per pixel.

  

   pixfmt: The System.Drawing.Imaging.PixelFormat enumeration to test.

   Returns: true if pixfmt is extended; otherwise,false.
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
 def RemovePropertyItem(self,propid):
  """
  RemovePropertyItem(self: Image,propid: int)

   Removes the specified property item from this System.Drawing.Image.

  

   propid: The ID of the property item to remove.
  """
  pass
 def RotateFlip(self,rotateFlipType):
  """
  RotateFlip(self: Image,rotateFlipType: RotateFlipType)

   Rotates,flips,or rotates and flips the System.Drawing.Image.

  

   rotateFlipType: A System.Drawing.RotateFlipType member that specifies the type of rotation and flip to apply to 

    the image.
  """
  pass
 def Save(self,*__args):
  """
  Save(self: Image,stream: Stream,format: ImageFormat)

   Saves this image to the specified stream in the specified format.

  

   stream: The System.IO.Stream where the image will be saved.

   format: An System.Drawing.Imaging.ImageFormat that specifies the format of the saved image.

  Save(self: Image,stream: Stream,encoder: ImageCodecInfo,encoderParams: EncoderParameters)

   Saves this image to the specified stream,with the specified encoder and image encoder 

    parameters.

  

  

   stream: The System.IO.Stream where the image will be saved.

   encoder: The System.Drawing.Imaging.ImageCodecInfo for this System.Drawing.Image.

   encoderParams: An System.Drawing.Imaging.EncoderParameters that specifies parameters used by the image encoder.

  Save(self: Image,filename: str,encoder: ImageCodecInfo,encoderParams: EncoderParameters)

   Saves this System.Drawing.Image to the specified file,with the specified encoder and 

    image-encoder parameters.

  

  

   filename: A string that contains the name of the file to which to save this System.Drawing.Image.

   encoder: The System.Drawing.Imaging.ImageCodecInfo for this System.Drawing.Image.

   encoderParams: An System.Drawing.Imaging.EncoderParameters to use for this System.Drawing.Image.

  Save(self: Image,filename: str)

   Saves this System.Drawing.Image to the specified file or stream.

  

   filename: A string that contains the name of the file to which to save this System.Drawing.Image.

  Save(self: Image,filename: str,format: ImageFormat)

   Saves this System.Drawing.Image to the specified file in the specified format.

  

   filename: A string that contains the name of the file to which to save this System.Drawing.Image.

   format: The System.Drawing.Imaging.ImageFormat for this System.Drawing.Image.
  """
  pass
 def SaveAdd(self,*__args):
  """
  SaveAdd(self: Image,image: Image,encoderParams: EncoderParameters)

   Adds a frame to the file or stream specified in a previous call to the 

    erload:System.Drawing.Image.Save method.

  

  

   image: An System.Drawing.Image that contains the frame to add.

   encoderParams: An System.Drawing.Imaging.EncoderParameters that holds parameters required by the image encoder 

    that is used by the save-add operation.

  

  SaveAdd(self: Image,encoderParams: EncoderParameters)

   Adds a frame to the file or stream specified in a previous call to the 

    erload:System.Drawing.Image.Save method. Use this method to save selected frames from a 

    multiple-frame image to another multiple-frame image.

  

  

   encoderParams: An System.Drawing.Imaging.EncoderParameters that holds parameters required by the image encoder 

    that is used by the save-add operation.
  """
  pass
 def SelectActiveFrame(self,dimension,frameIndex):
  """
  SelectActiveFrame(self: Image,dimension: FrameDimension,frameIndex: int) -> int

  

   Selects the frame specified by the dimension and index.

  

   dimension: A System.Drawing.Imaging.FrameDimension that specifies the identity of the dimension type.

   frameIndex: The index of the active frame.

   Returns: Always returns 0.
  """
  pass
 def SetPropertyItem(self,propitem):
  """
  SetPropertyItem(self: Image,propitem: PropertyItem)

   Stores a property item (piece of metadata) in this System.Drawing.Image.

  

   propitem: The System.Drawing.Imaging.PropertyItem to be stored.
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
 def __reduce_ex__(self,*args):
  pass
 Flags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets attribute flags for the pixel data of this System.Drawing.Image.



Get: Flags(self: Image) -> int



"""

 FrameDimensionsList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an array of GUIDs that represent the dimensions of frames within this System.Drawing.Image.



Get: FrameDimensionsList(self: Image) -> Array[Guid]



"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the height,in pixels,of this System.Drawing.Image.



Get: Height(self: Image) -> int



"""

 HorizontalResolution=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the horizontal resolution,in pixels per inch,of this System.Drawing.Image.



Get: HorizontalResolution(self: Image) -> Single



"""

 Palette=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color palette used for this System.Drawing.Image.



Get: Palette(self: Image) -> ColorPalette



Set: Palette(self: Image)=value

"""

 PhysicalDimension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the width and height of this image.



Get: PhysicalDimension(self: Image) -> SizeF



"""

 PixelFormat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the pixel format for this System.Drawing.Image.



Get: PixelFormat(self: Image) -> PixelFormat



"""

 PropertyIdList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets IDs of the property items stored in this System.Drawing.Image.



Get: PropertyIdList(self: Image) -> Array[int]



"""

 PropertyItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets all the property items (pieces of metadata) stored in this System.Drawing.Image.



Get: PropertyItems(self: Image) -> Array[PropertyItem]



"""

 RawFormat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the file format of this System.Drawing.Image.



Get: RawFormat(self: Image) -> ImageFormat



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the width and height,in pixels,of this image.



Get: Size(self: Image) -> Size



"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object that provides additional data about the image.



Get: Tag(self: Image) -> object



Set: Tag(self: Image)=value

"""

 VerticalResolution=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the vertical resolution,in pixels per inch,of this System.Drawing.Image.



Get: VerticalResolution(self: Image) -> Single



"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the width,in pixels,of this System.Drawing.Image.



Get: Width(self: Image) -> int



"""


 GetThumbnailImageAbort=None

