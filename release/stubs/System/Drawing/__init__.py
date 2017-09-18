# encoding: utf-8
# module System.Drawing calls itself Drawing
# from System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Image(MarshalByRefObject, ISerializable, ICloneable, IDisposable):
    """ An abstract base class that provides functionality for the System.Drawing.Bitmap and System.Drawing.Imaging.Metafile descended classes. """
    def Clone(self):
        """
        Clone(self: Image) -> object
        
            Creates an exact copy of this System.Drawing.Image.
            Returns: The System.Drawing.Image this method creates, cast as an object.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Image)
            Releases all resources used by this System.Drawing.Image.
        """
        pass

    @staticmethod
    def FromFile(filename, useEmbeddedColorManagement=None):
        """
        FromFile(filename: str, useEmbeddedColorManagement: bool) -> Image
        
            Creates an System.Drawing.Image from the specified file using embedded color management 
             information in that file.
        
        
            filename: A string that contains the name of the file from which to create the System.Drawing.Image.
            useEmbeddedColorManagement: Set to true to use color management information embedded in the image file; otherwise, false.
            Returns: The System.Drawing.Image this method creates.
        FromFile(filename: str) -> Image
        
            Creates an System.Drawing.Image from the specified file.
        
            filename: A string that contains the name of the file from which to create the System.Drawing.Image.
            Returns: The System.Drawing.Image this method creates.
        """
        pass

    @staticmethod
    def FromHbitmap(hbitmap, hpalette=None):
        """
        FromHbitmap(hbitmap: IntPtr, hpalette: IntPtr) -> Bitmap
        
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
    def FromStream(stream, useEmbeddedColorManagement=None, validateImageData=None):
        """
        FromStream(stream: Stream, useEmbeddedColorManagement: bool, validateImageData: bool) -> Image
        
            Creates an System.Drawing.Image from the specified data stream, optionally using embedded color 
             management information and validating the image data.
        
        
            stream: A System.IO.Stream that contains the data for this System.Drawing.Image.
            useEmbeddedColorManagement: true to use color management information embedded in the data stream; otherwise, false.
            validateImageData: true to validate the image data; otherwise, false.
            Returns: The System.Drawing.Image this method creates.
        FromStream(stream: Stream, useEmbeddedColorManagement: bool) -> Image
        
            Creates an System.Drawing.Image from the specified data stream, optionally using embedded color 
             management information in that stream.
        
        
            stream: A System.IO.Stream that contains the data for this System.Drawing.Image.
            useEmbeddedColorManagement: true to use color management information embedded in the data stream; otherwise, false.
            Returns: The System.Drawing.Image this method creates.
        FromStream(stream: Stream) -> Image
        
            Creates an System.Drawing.Image from the specified data stream.
        
            stream: A System.IO.Stream that contains the data for this System.Drawing.Image.
            Returns: The System.Drawing.Image this method creates.
        """
        pass

    def GetBounds(self, pageUnit):
        """
        GetBounds(self: Image, pageUnit: GraphicsUnit) -> (RectangleF, GraphicsUnit)
        
            Gets the bounds of the image in the specified unit.
        
            pageUnit: One of the System.Drawing.GraphicsUnit values indicating the unit of measure for the bounding 
             rectangle.
        
            Returns: The System.Drawing.RectangleF that represents the bounds of the image, in the specified unit.
        """
        pass

    def GetEncoderParameterList(self, encoder):
        """
        GetEncoderParameterList(self: Image, encoder: Guid) -> EncoderParameters
        
            Returns information about the parameters supported by the specified image encoder.
        
            encoder: A GUID that specifies the image encoder.
            Returns: An System.Drawing.Imaging.EncoderParameters that contains an array of 
             System.Drawing.Imaging.EncoderParameter objects. Each System.Drawing.Imaging.EncoderParameter 
             contains information about one of the parameters supported by the specified image encoder.
        """
        pass

    def GetFrameCount(self, dimension):
        """
        GetFrameCount(self: Image, dimension: FrameDimension) -> int
        
            Returns the number of frames of the specified dimension.
        
            dimension: A System.Drawing.Imaging.FrameDimension that specifies the identity of the dimension type.
            Returns: The number of frames in the specified dimension.
        """
        pass

    @staticmethod
    def GetPixelFormatSize(pixfmt):
        """
        GetPixelFormatSize(pixfmt: PixelFormat) -> int
        
            Returns the color depth, in number of bits per pixel, of the specified pixel format.
        
            pixfmt: The System.Drawing.Imaging.PixelFormat member that specifies the format for which to find the 
             size.
        
            Returns: The color depth of the specified pixel format.
        """
        pass

    def GetPropertyItem(self, propid):
        """
        GetPropertyItem(self: Image, propid: int) -> PropertyItem
        
            Gets the specified property item from this System.Drawing.Image.
        
            propid: The ID of the property item to get.
            Returns: The System.Drawing.Imaging.PropertyItem this method gets.
        """
        pass

    def GetThumbnailImage(self, thumbWidth, thumbHeight, callback, callbackData):
        """ GetThumbnailImage(self: Image, thumbWidth: int, thumbHeight: int, callback: GetThumbnailImageAbort, callbackData: IntPtr) -> Image """
        pass

    @staticmethod
    def IsAlphaPixelFormat(pixfmt):
        """
        IsAlphaPixelFormat(pixfmt: PixelFormat) -> bool
        
            Returns a value that indicates whether the pixel format for this System.Drawing.Image contains 
             alpha information.
        
        
            pixfmt: The System.Drawing.Imaging.PixelFormat to test.
            Returns: true if pixfmt contains alpha information; otherwise, false.
        """
        pass

    @staticmethod
    def IsCanonicalPixelFormat(pixfmt):
        """
        IsCanonicalPixelFormat(pixfmt: PixelFormat) -> bool
        
            Returns a value that indicates whether the pixel format is 32 bits per pixel.
        
            pixfmt: The System.Drawing.Imaging.PixelFormat to test.
            Returns: true if pixfmt is canonical; otherwise, false.
        """
        pass

    @staticmethod
    def IsExtendedPixelFormat(pixfmt):
        """
        IsExtendedPixelFormat(pixfmt: PixelFormat) -> bool
        
            Returns a value that indicates whether the pixel format is 64 bits per pixel.
        
            pixfmt: The System.Drawing.Imaging.PixelFormat enumeration to test.
            Returns: true if pixfmt is extended; otherwise, false.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def RemovePropertyItem(self, propid):
        """
        RemovePropertyItem(self: Image, propid: int)
            Removes the specified property item from this System.Drawing.Image.
        
            propid: The ID of the property item to remove.
        """
        pass

    def RotateFlip(self, rotateFlipType):
        """
        RotateFlip(self: Image, rotateFlipType: RotateFlipType)
            Rotates, flips, or rotates and flips the System.Drawing.Image.
        
            rotateFlipType: A System.Drawing.RotateFlipType member that specifies the type of rotation and flip to apply to 
             the image.
        """
        pass

    def Save(self, *__args):
        """
        Save(self: Image, stream: Stream, format: ImageFormat)
            Saves this image to the specified stream in the specified format.
        
            stream: The System.IO.Stream where the image will be saved.
            format: An System.Drawing.Imaging.ImageFormat that specifies the format of the saved image.
        Save(self: Image, stream: Stream, encoder: ImageCodecInfo, encoderParams: EncoderParameters)
            Saves this image to the specified stream, with the specified encoder and image encoder 
             parameters.
        
        
            stream: The System.IO.Stream where the image will be saved.
            encoder: The System.Drawing.Imaging.ImageCodecInfo for this System.Drawing.Image.
            encoderParams: An System.Drawing.Imaging.EncoderParameters that specifies parameters used by the image encoder.
        Save(self: Image, filename: str, encoder: ImageCodecInfo, encoderParams: EncoderParameters)
            Saves this System.Drawing.Image to the specified file, with the specified encoder and 
             image-encoder parameters.
        
        
            filename: A string that contains the name of the file to which to save this System.Drawing.Image.
            encoder: The System.Drawing.Imaging.ImageCodecInfo for this System.Drawing.Image.
            encoderParams: An System.Drawing.Imaging.EncoderParameters to use for this System.Drawing.Image.
        Save(self: Image, filename: str)
            Saves this System.Drawing.Image to the specified file or stream.
        
            filename: A string that contains the name of the file to which to save this System.Drawing.Image.
        Save(self: Image, filename: str, format: ImageFormat)
            Saves this System.Drawing.Image to the specified file in the specified format.
        
            filename: A string that contains the name of the file to which to save this System.Drawing.Image.
            format: The System.Drawing.Imaging.ImageFormat for this System.Drawing.Image.
        """
        pass

    def SaveAdd(self, *__args):
        """
        SaveAdd(self: Image, image: Image, encoderParams: EncoderParameters)
            Adds a frame to the file or stream specified in a previous call to the 
             erload:System.Drawing.Image.Save method.
        
        
            image: An System.Drawing.Image that contains the frame to add.
            encoderParams: An System.Drawing.Imaging.EncoderParameters that holds parameters required by the image encoder 
             that is used by the save-add operation.
        
        SaveAdd(self: Image, encoderParams: EncoderParameters)
            Adds a frame to the file or stream specified in a previous call to the 
             erload:System.Drawing.Image.Save method. Use this method to save selected frames from a 
             multiple-frame image to another multiple-frame image.
        
        
            encoderParams: An System.Drawing.Imaging.EncoderParameters that holds parameters required by the image encoder 
             that is used by the save-add operation.
        """
        pass

    def SelectActiveFrame(self, dimension, frameIndex):
        """
        SelectActiveFrame(self: Image, dimension: FrameDimension, frameIndex: int) -> int
        
            Selects the frame specified by the dimension and index.
        
            dimension: A System.Drawing.Imaging.FrameDimension that specifies the identity of the dimension type.
            frameIndex: The index of the active frame.
            Returns: Always returns 0.
        """
        pass

    def SetPropertyItem(self, propitem):
        """
        SetPropertyItem(self: Image, propitem: PropertyItem)
            Stores a property item (piece of metadata) in this System.Drawing.Image.
        
            propitem: The System.Drawing.Imaging.PropertyItem to be stored.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets attribute flags for the pixel data of this System.Drawing.Image.

Get: Flags(self: Image) -> int

"""

    FrameDimensionsList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an array of GUIDs that represent the dimensions of frames within this System.Drawing.Image.

Get: FrameDimensionsList(self: Image) -> Array[Guid]

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height, in pixels, of this System.Drawing.Image.

Get: Height(self: Image) -> int

"""

    HorizontalResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the horizontal resolution, in pixels per inch, of this System.Drawing.Image.

Get: HorizontalResolution(self: Image) -> Single

"""

    Palette = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color palette used for this System.Drawing.Image.

Get: Palette(self: Image) -> ColorPalette

Set: Palette(self: Image) = value
"""

    PhysicalDimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width and height of this image.

Get: PhysicalDimension(self: Image) -> SizeF

"""

    PixelFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the pixel format for this System.Drawing.Image.

Get: PixelFormat(self: Image) -> PixelFormat

"""

    PropertyIdList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets IDs of the property items stored in this System.Drawing.Image.

Get: PropertyIdList(self: Image) -> Array[int]

"""

    PropertyItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all the property items (pieces of metadata) stored in this System.Drawing.Image.

Get: PropertyItems(self: Image) -> Array[PropertyItem]

"""

    RawFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file format of this System.Drawing.Image.

Get: RawFormat(self: Image) -> ImageFormat

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width and height, in pixels, of this image.

Get: Size(self: Image) -> Size

"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an object that provides additional data about the image.

Get: Tag(self: Image) -> object

Set: Tag(self: Image) = value
"""

    VerticalResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the vertical resolution, in pixels per inch, of this System.Drawing.Image.

Get: VerticalResolution(self: Image) -> Single

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width, in pixels, of this System.Drawing.Image.

Get: Width(self: Image) -> int

"""


    GetThumbnailImageAbort = None


class Bitmap(Image, ISerializable, ICloneable, IDisposable):
    """
    Encapsulates a GDI+ bitmap, which consists of the pixel data for a graphics image and its attributes. A System.Drawing.Bitmap is an object used to work with images defined by pixel data.
    
    Bitmap(filename: str)
    Bitmap(filename: str, useIcm: bool)
    Bitmap(type: Type, resource: str)
    Bitmap(stream: Stream)
    Bitmap(stream: Stream, useIcm: bool)
    Bitmap(width: int, height: int, stride: int, format: PixelFormat, scan0: IntPtr)
    Bitmap(width: int, height: int, format: PixelFormat)
    Bitmap(width: int, height: int)
    Bitmap(width: int, height: int, g: Graphics)
    Bitmap(original: Image)
    Bitmap(original: Image, width: int, height: int)
    Bitmap(original: Image, newSize: Size)
    """
    def Clone(self, rect=None, format=None):
        """
        Clone(self: Bitmap, rect: RectangleF, format: PixelFormat) -> Bitmap
        
            Creates a copy of the section of this System.Drawing.Bitmap defined with a specified 
             System.Drawing.Imaging.PixelFormat enumeration.
        
        
            rect: Defines the portion of this System.Drawing.Bitmap to copy.
            format: Specifies the System.Drawing.Imaging.PixelFormat enumeration for the destination 
             System.Drawing.Bitmap.
        
            Returns: The System.Drawing.Bitmap that this method creates.
        Clone(self: Bitmap, rect: Rectangle, format: PixelFormat) -> Bitmap
        
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
        Dispose(self: Image, disposing: bool)
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
    def FromResource(hinstance, bitmapName):
        """
        FromResource(hinstance: IntPtr, bitmapName: str) -> Bitmap
        
            Creates a System.Drawing.Bitmap from the specified Windows resource.
        
            hinstance: A handle to an instance of the executable file that contains the resource.
            bitmapName: A string that contains the name of the resource bitmap.
            Returns: The System.Drawing.Bitmap that this method creates.
        """
        pass

    def GetHbitmap(self, background=None):
        """
        GetHbitmap(self: Bitmap, background: Color) -> IntPtr
        
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

    def GetPixel(self, x, y):
        """
        GetPixel(self: Bitmap, x: int, y: int) -> Color
        
            Gets the color of the specified pixel in this System.Drawing.Bitmap.
        
            x: The x-coordinate of the pixel to retrieve.
            y: The y-coordinate of the pixel to retrieve.
            Returns: A System.Drawing.Color structure that represents the color of the specified pixel.
        """
        pass

    def LockBits(self, rect, flags, format, bitmapData=None):
        """
        LockBits(self: Bitmap, rect: Rectangle, flags: ImageLockMode, format: PixelFormat, bitmapData: BitmapData) -> BitmapData
        
            Locks a System.Drawing.Bitmap into system memory
        
            rect: A rectangle structure that specifies the portion of the System.Drawing.Bitmap to lock.
            flags: One of the System.Drawing.Imaging.ImageLockMode values that specifies the access level 
             (read/write) for the System.Drawing.Bitmap.
        
            format: One of the System.Drawing.Imaging.PixelFormat values that specifies the data format of the 
             System.Drawing.Bitmap.
        
            bitmapData: A System.Drawing.Imaging.BitmapData that contains information about the lock operation.
            Returns: A System.Drawing.Imaging.BitmapData that contains information about the lock operation.
        LockBits(self: Bitmap, rect: Rectangle, flags: ImageLockMode, format: PixelFormat) -> BitmapData
        
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

    def MakeTransparent(self, transparentColor=None):
        """
        MakeTransparent(self: Bitmap, transparentColor: Color)
            Makes the specified color transparent for this System.Drawing.Bitmap.
        
            transparentColor: The System.Drawing.Color structure that represents the color to make transparent.
        MakeTransparent(self: Bitmap)
            Makes the default transparent color transparent for this System.Drawing.Bitmap.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def SetPixel(self, x, y, color):
        """
        SetPixel(self: Bitmap, x: int, y: int, color: Color)
            Sets the color of the specified pixel in this System.Drawing.Bitmap.
        
            x: The x-coordinate of the pixel to set.
            y: The y-coordinate of the pixel to set.
            color: A System.Drawing.Color structure that represents the color to assign to the specified pixel.
        """
        pass

    def SetResolution(self, xDpi, yDpi):
        """
        SetResolution(self: Bitmap, xDpi: Single, yDpi: Single)
            Sets the resolution for this System.Drawing.Bitmap.
        
            xDpi: The horizontal resolution, in dots per inch, of the System.Drawing.Bitmap.
            yDpi: The vertical resolution, in dots per inch, of the System.Drawing.Bitmap.
        """
        pass

    def UnlockBits(self, bitmapdata):
        """
        UnlockBits(self: Bitmap, bitmapdata: BitmapData)
            Unlocks this System.Drawing.Bitmap from system memory.
        
            bitmapdata: A System.Drawing.Imaging.BitmapData that specifies information about the lock operation.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, filename: str)
        __new__(cls: type, filename: str, useIcm: bool)
        __new__(cls: type, type: Type, resource: str)
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, useIcm: bool)
        __new__(cls: type, width: int, height: int, stride: int, format: PixelFormat, scan0: IntPtr)
        __new__(cls: type, width: int, height: int, format: PixelFormat)
        __new__(cls: type, width: int, height: int)
        __new__(cls: type, width: int, height: int, g: Graphics)
        __new__(cls: type, original: Image)
        __new__(cls: type, original: Image, width: int, height: int)
        __new__(cls: type, original: Image, newSize: Size)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class BitmapSuffixInSameAssemblyAttribute(Attribute, _Attribute):
    """ BitmapSuffixInSameAssemblyAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class BitmapSuffixInSatelliteAssemblyAttribute(Attribute, _Attribute):
    """ BitmapSuffixInSatelliteAssemblyAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Brush(MarshalByRefObject, ICloneable, IDisposable):
    """ Defines objects used to fill the interiors of graphical shapes such as rectangles, ellipses, pies, polygons, and paths. """
    def Clone(self):
        """
        Clone(self: Brush) -> object
        
            When overridden in a derived class, creates an exact copy of this System.Drawing.Brush.
            Returns: The new System.Drawing.Brush that this method creates.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Brush)
            Releases all resources used by this System.Drawing.Brush object.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def SetNativeBrush(self, *args): #cannot find CLR method
        """
        SetNativeBrush(self: Brush, brush: IntPtr)
            In a derived class, sets a reference to a GDI+ brush object.
        
            brush: A pointer to the GDI+ brush object.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Brushes(object):
    """ Brushes for all the standard colors. This class cannot be inherited. """
    AliceBlue = None
    AntiqueWhite = None
    Aqua = None
    Aquamarine = None
    Azure = None
    Beige = None
    Bisque = None
    Black = None
    BlanchedAlmond = None
    Blue = None
    BlueViolet = None
    Brown = None
    BurlyWood = None
    CadetBlue = None
    Chartreuse = None
    Chocolate = None
    Coral = None
    CornflowerBlue = None
    Cornsilk = None
    Crimson = None
    Cyan = None
    DarkBlue = None
    DarkCyan = None
    DarkGoldenrod = None
    DarkGray = None
    DarkGreen = None
    DarkKhaki = None
    DarkMagenta = None
    DarkOliveGreen = None
    DarkOrange = None
    DarkOrchid = None
    DarkRed = None
    DarkSalmon = None
    DarkSeaGreen = None
    DarkSlateBlue = None
    DarkSlateGray = None
    DarkTurquoise = None
    DarkViolet = None
    DeepPink = None
    DeepSkyBlue = None
    DimGray = None
    DodgerBlue = None
    Firebrick = None
    FloralWhite = None
    ForestGreen = None
    Fuchsia = None
    Gainsboro = None
    GhostWhite = None
    Gold = None
    Goldenrod = None
    Gray = None
    Green = None
    GreenYellow = None
    Honeydew = None
    HotPink = None
    IndianRed = None
    Indigo = None
    Ivory = None
    Khaki = None
    Lavender = None
    LavenderBlush = None
    LawnGreen = None
    LemonChiffon = None
    LightBlue = None
    LightCoral = None
    LightCyan = None
    LightGoldenrodYellow = None
    LightGray = None
    LightGreen = None
    LightPink = None
    LightSalmon = None
    LightSeaGreen = None
    LightSkyBlue = None
    LightSlateGray = None
    LightSteelBlue = None
    LightYellow = None
    Lime = None
    LimeGreen = None
    Linen = None
    Magenta = None
    Maroon = None
    MediumAquamarine = None
    MediumBlue = None
    MediumOrchid = None
    MediumPurple = None
    MediumSeaGreen = None
    MediumSlateBlue = None
    MediumSpringGreen = None
    MediumTurquoise = None
    MediumVioletRed = None
    MidnightBlue = None
    MintCream = None
    MistyRose = None
    Moccasin = None
    NavajoWhite = None
    Navy = None
    OldLace = None
    Olive = None
    OliveDrab = None
    Orange = None
    OrangeRed = None
    Orchid = None
    PaleGoldenrod = None
    PaleGreen = None
    PaleTurquoise = None
    PaleVioletRed = None
    PapayaWhip = None
    PeachPuff = None
    Peru = None
    Pink = None
    Plum = None
    PowderBlue = None
    Purple = None
    Red = None
    RosyBrown = None
    RoyalBlue = None
    SaddleBrown = None
    Salmon = None
    SandyBrown = None
    SeaGreen = None
    SeaShell = None
    Sienna = None
    Silver = None
    SkyBlue = None
    SlateBlue = None
    SlateGray = None
    Snow = None
    SpringGreen = None
    SteelBlue = None
    Tan = None
    Teal = None
    Thistle = None
    Tomato = None
    Transparent = None
    Turquoise = None
    Violet = None
    Wheat = None
    White = None
    WhiteSmoke = None
    Yellow = None
    YellowGreen = None


class BufferedGraphics(object, IDisposable):
    """ Provides a graphics buffer for double buffering. """
    def Dispose(self):
        """
        Dispose(self: BufferedGraphics)
            Releases all resources used by the System.Drawing.BufferedGraphics object.
        """
        pass

    def Render(self, *__args):
        """
        Render(self: BufferedGraphics, targetDC: IntPtr)
            Writes the contents of the graphics buffer to the device context associated with the specified 
             System.IntPtr handle.
        
        
            targetDC: An System.IntPtr that points to the device context to which to write the contents of the 
             graphics buffer.
        
        Render(self: BufferedGraphics, target: Graphics)
            Writes the contents of the graphics buffer to the specified System.Drawing.Graphics object.
        
            target: A System.Drawing.Graphics object to which to write the contents of the graphics buffer.
        Render(self: BufferedGraphics)
            Writes the contents of the graphics buffer to the default device.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Graphics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Drawing.Graphics object that outputs to the graphics buffer.

Get: Graphics(self: BufferedGraphics) -> Graphics

"""



class BufferedGraphicsContext(object, IDisposable):
    """
    Provides methods for creating graphics buffers that can be used for double buffering.
    
    BufferedGraphicsContext()
    """
    def Allocate(self, *__args):
        """
        Allocate(self: BufferedGraphicsContext, targetDC: IntPtr, targetRectangle: Rectangle) -> BufferedGraphics
        
            Creates a graphics buffer of the specified size using the pixel format of the specified 
             System.Drawing.Graphics.
        
        
            targetDC: An System.IntPtr to a device context to match the pixel format of the new buffer to.
            targetRectangle: A System.Drawing.Rectangle indicating the size of the buffer to create.
            Returns: A System.Drawing.BufferedGraphics that can be used to draw to a buffer of the specified 
             dimensions.
        
        Allocate(self: BufferedGraphicsContext, targetGraphics: Graphics, targetRectangle: Rectangle) -> BufferedGraphics
        
            Creates a graphics buffer of the specified size using the pixel format of the specified 
             System.Drawing.Graphics.
        
        
            targetGraphics: The System.Drawing.Graphics to match the pixel format for the new buffer to.
            targetRectangle: A System.Drawing.Rectangle indicating the size of the buffer to create.
            Returns: A System.Drawing.BufferedGraphics that can be used to draw to a buffer of the specified 
             dimensions.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: BufferedGraphicsContext)
            Releases all resources used by the System.Drawing.BufferedGraphicsContext.
        """
        pass

    def Invalidate(self):
        """
        Invalidate(self: BufferedGraphicsContext)
            Disposes of the current graphics buffer, if a buffer has been allocated and has not yet been 
             disposed.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    MaximumBuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum size of the buffer to use.

Get: MaximumBuffer(self: BufferedGraphicsContext) -> Size

Set: MaximumBuffer(self: BufferedGraphicsContext) = value
"""



class BufferedGraphicsManager(object):
    """ Provides access to the main buffered graphics context object for the application domain. """
    Current = None


class CharacterRange(object):
    """
    Specifies a range of character positions within a string.
    
    CharacterRange(First: int, Length: int)
    """
    def Equals(self, obj):
        """
        Equals(self: CharacterRange, obj: object) -> bool
        
            Gets a value indicating whether this object is equivalent to the specified object.
        
            obj: The object to compare to for equality.
            Returns: true to indicate the specified object is an instance with the same 
             System.Drawing.CharacterRange.First and System.Drawing.CharacterRange.Length value as this 
             instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: CharacterRange) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, First, Length):
        """
        __new__[CharacterRange]() -> CharacterRange
        
        __new__(cls: type, First: int, Length: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    First = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the position in the string of the first character of this System.Drawing.CharacterRange.

Get: First(self: CharacterRange) -> int

Set: First(self: CharacterRange) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of positions in this System.Drawing.CharacterRange.

Get: Length(self: CharacterRange) -> int

Set: Length(self: CharacterRange) = value
"""



class Color(object):
    """ Represents an ARGB (alpha, red, green, blue) color. """
    def Equals(self, obj):
        """
        Equals(self: Color, obj: object) -> bool
        
            Tests whether the specified object is a System.Drawing.Color structure and is equivalent to this 
             System.Drawing.Color structure.
        
        
            obj: The object to test.
            Returns: true if obj is a System.Drawing.Color structure equivalent to this System.Drawing.Color 
             structure; otherwise, false.
        """
        pass

    @staticmethod
    def FromArgb(*__args):
        """
        FromArgb(alpha: int, baseColor: Color) -> Color
        
            Creates a System.Drawing.Color structure from the specified System.Drawing.Color structure, but 
             with the new specified alpha value. Although this method allows a 32-bit value to be passed for 
             the alpha value, the value is limited to 8 bits.
        
        
            alpha: The alpha value for the new System.Drawing.Color. Valid values are 0 through 255.
            baseColor: The System.Drawing.Color from which to create the new System.Drawing.Color.
            Returns: The System.Drawing.Color that this method creates.
        FromArgb(red: int, green: int, blue: int) -> Color
        
            Creates a System.Drawing.Color structure from the specified 8-bit color values (red, green, and 
             blue). The alpha value is implicitly 255 (fully opaque). Although this method allows a 32-bit 
             value to be passed for each color component, the value of each component is limited to 8 bits.
        
        
            red: The red component value for the new System.Drawing.Color. Valid values are 0 through 255.
            green: The green component value for the new System.Drawing.Color. Valid values are 0 through 255.
            blue: The blue component value for the new System.Drawing.Color. Valid values are 0 through 255.
            Returns: The System.Drawing.Color that this method creates.
        FromArgb(argb: int) -> Color
        
            Creates a System.Drawing.Color structure from a 32-bit ARGB value.
        
            argb: A value specifying the 32-bit ARGB value.
            Returns: The System.Drawing.Color structure that this method creates.
        FromArgb(alpha: int, red: int, green: int, blue: int) -> Color
        
            Creates a System.Drawing.Color structure from the four ARGB component (alpha, red, green, and 
             blue) values. Although this method allows a 32-bit value to be passed for each component, the 
             value of each component is limited to 8 bits.
        
        
            alpha: The alpha component. Valid values are 0 through 255.
            red: The red component. Valid values are 0 through 255.
            green: The green component. Valid values are 0 through 255.
            blue: The blue component. Valid values are 0 through 255.
            Returns: The System.Drawing.Color that this method creates.
        """
        pass

    @staticmethod
    def FromKnownColor(color):
        """
        FromKnownColor(color: KnownColor) -> Color
        
            Creates a System.Drawing.Color structure from the specified predefined color.
        
            color: An element of the System.Drawing.KnownColor enumeration.
            Returns: The System.Drawing.Color that this method creates.
        """
        pass

    @staticmethod
    def FromName(name):
        """
        FromName(name: str) -> Color
        
            Creates a System.Drawing.Color structure from the specified name of a predefined color.
        
            name: A string that is the name of a predefined color. Valid names are the same as the names of the 
             elements of the System.Drawing.KnownColor enumeration.
        
            Returns: The System.Drawing.Color that this method creates.
        """
        pass

    def GetBrightness(self):
        """
        GetBrightness(self: Color) -> Single
        
            Gets the hue-saturation-brightness (HSB) brightness value for this System.Drawing.Color 
             structure.
        
            Returns: The brightness of this System.Drawing.Color. The brightness ranges from 0.0 through 1.0, where 
             0.0 represents black and 1.0 represents white.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Color) -> int
        
            Returns a hash code for this System.Drawing.Color structure.
            Returns: An integer value that specifies the hash code for this System.Drawing.Color.
        """
        pass

    def GetHue(self):
        """
        GetHue(self: Color) -> Single
        
            Gets the hue-saturation-brightness (HSB) hue value, in degrees, for this System.Drawing.Color 
             structure.
        
            Returns: The hue, in degrees, of this System.Drawing.Color. The hue is measured in degrees, ranging from 
             0.0 through 360.0, in HSB color space.
        """
        pass

    def GetSaturation(self):
        """
        GetSaturation(self: Color) -> Single
        
            Gets the hue-saturation-brightness (HSB) saturation value for this System.Drawing.Color 
             structure.
        
            Returns: The saturation of this System.Drawing.Color. The saturation ranges from 0.0 through 1.0, where 
             0.0 is grayscale and 1.0 is the most saturated.
        """
        pass

    def ToArgb(self):
        """
        ToArgb(self: Color) -> int
        
            Gets the 32-bit ARGB value of this System.Drawing.Color structure.
            Returns: The 32-bit ARGB value of this System.Drawing.Color.
        """
        pass

    def ToKnownColor(self):
        """
        ToKnownColor(self: Color) -> KnownColor
        
            Gets the System.Drawing.KnownColor value of this System.Drawing.Color structure.
            Returns: An element of the System.Drawing.KnownColor enumeration, if the System.Drawing.Color is created 
             from a predefined color by using either the System.Drawing.Color.FromName(System.String) method 
             or the System.Drawing.Color.FromKnownColor(System.Drawing.KnownColor) method; otherwise, 0.
        """
        pass

    def ToString(self):
        """
        ToString(self: Color) -> str
        
            Converts this System.Drawing.Color structure to a human-readable string.
            Returns: A string that is the name of this System.Drawing.Color, if the System.Drawing.Color is created 
             from a predefined color by using either the System.Drawing.Color.FromName(System.String) method 
             or the System.Drawing.Color.FromKnownColor(System.Drawing.KnownColor) method; otherwise, a 
             string that consists of the ARGB component names and their values.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the alpha component value of this System.Drawing.Color structure.

Get: A(self: Color) -> Byte

"""

    B = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the blue component value of this System.Drawing.Color structure.

Get: B(self: Color) -> Byte

"""

    G = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the green component value of this System.Drawing.Color structure.

Get: G(self: Color) -> Byte

"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether this System.Drawing.Color structure is uninitialized.

Get: IsEmpty(self: Color) -> bool

"""

    IsKnownColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this System.Drawing.Color structure is a predefined color. Predefined colors are represented by the elements of the System.Drawing.KnownColor enumeration.

Get: IsKnownColor(self: Color) -> bool

"""

    IsNamedColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this System.Drawing.Color structure is a named color or a member of the System.Drawing.KnownColor enumeration.

Get: IsNamedColor(self: Color) -> bool

"""

    IsSystemColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this System.Drawing.Color structure is a system color. A system color is a color that is used in a Windows display element. System colors are represented by elements of the System.Drawing.KnownColor enumeration.

Get: IsSystemColor(self: Color) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of this System.Drawing.Color.

Get: Name(self: Color) -> str

"""

    R = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the red component value of this System.Drawing.Color structure.

Get: R(self: Color) -> Byte

"""


    AliceBlue = None
    AntiqueWhite = None
    Aqua = None
    Aquamarine = None
    Azure = None
    Beige = None
    Bisque = None
    Black = None
    BlanchedAlmond = None
    Blue = None
    BlueViolet = None
    Brown = None
    BurlyWood = None
    CadetBlue = None
    Chartreuse = None
    Chocolate = None
    Coral = None
    CornflowerBlue = None
    Cornsilk = None
    Crimson = None
    Cyan = None
    DarkBlue = None
    DarkCyan = None
    DarkGoldenrod = None
    DarkGray = None
    DarkGreen = None
    DarkKhaki = None
    DarkMagenta = None
    DarkOliveGreen = None
    DarkOrange = None
    DarkOrchid = None
    DarkRed = None
    DarkSalmon = None
    DarkSeaGreen = None
    DarkSlateBlue = None
    DarkSlateGray = None
    DarkTurquoise = None
    DarkViolet = None
    DeepPink = None
    DeepSkyBlue = None
    DimGray = None
    DodgerBlue = None
    Empty = None
    Firebrick = None
    FloralWhite = None
    ForestGreen = None
    Fuchsia = None
    Gainsboro = None
    GhostWhite = None
    Gold = None
    Goldenrod = None
    Gray = None
    Green = None
    GreenYellow = None
    Honeydew = None
    HotPink = None
    IndianRed = None
    Indigo = None
    Ivory = None
    Khaki = None
    Lavender = None
    LavenderBlush = None
    LawnGreen = None
    LemonChiffon = None
    LightBlue = None
    LightCoral = None
    LightCyan = None
    LightGoldenrodYellow = None
    LightGray = None
    LightGreen = None
    LightPink = None
    LightSalmon = None
    LightSeaGreen = None
    LightSkyBlue = None
    LightSlateGray = None
    LightSteelBlue = None
    LightYellow = None
    Lime = None
    LimeGreen = None
    Linen = None
    Magenta = None
    Maroon = None
    MediumAquamarine = None
    MediumBlue = None
    MediumOrchid = None
    MediumPurple = None
    MediumSeaGreen = None
    MediumSlateBlue = None
    MediumSpringGreen = None
    MediumTurquoise = None
    MediumVioletRed = None
    MidnightBlue = None
    MintCream = None
    MistyRose = None
    Moccasin = None
    NavajoWhite = None
    Navy = None
    OldLace = None
    Olive = None
    OliveDrab = None
    Orange = None
    OrangeRed = None
    Orchid = None
    PaleGoldenrod = None
    PaleGreen = None
    PaleTurquoise = None
    PaleVioletRed = None
    PapayaWhip = None
    PeachPuff = None
    Peru = None
    Pink = None
    Plum = None
    PowderBlue = None
    Purple = None
    Red = None
    RosyBrown = None
    RoyalBlue = None
    SaddleBrown = None
    Salmon = None
    SandyBrown = None
    SeaGreen = None
    SeaShell = None
    Sienna = None
    Silver = None
    SkyBlue = None
    SlateBlue = None
    SlateGray = None
    Snow = None
    SpringGreen = None
    SteelBlue = None
    Tan = None
    Teal = None
    Thistle = None
    Tomato = None
    Transparent = None
    Turquoise = None
    Violet = None
    Wheat = None
    White = None
    WhiteSmoke = None
    Yellow = None
    YellowGreen = None


class ColorConverter(TypeConverter):
    """
    Converts colors from one data type to another. Access this class through the System.ComponentModel.TypeDescriptor.
    
    ColorConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: ColorConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines if this converter can convert an object in the given source type to the native type 
             of the converter.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context. You can use this 
             object to get additional information about the environment from which this converter is being 
             invoked.
        
            sourceType: The type from which you want to convert.
            Returns: true if this object can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: ColorConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Returns a value indicating whether this converter can convert an object to the given destination 
             type using the context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that represents the type to which you want to convert.
            Returns: true if this converter can perform the operation; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: ColorConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the given object to the converter's native type.
        
            context: A System.ComponentModel.TypeDescriptor that provides a format context. You can use this object 
             to get additional information about the environment from which this converter is being invoked.
        
            culture: A System.Globalization.CultureInfo that specifies the culture to represent the color.
            value: The object to convert.
            Returns: An System.Object representing the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: ColorConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified object to another type.
        
            context: A formatter context. Use this object to extract additional information about the environment 
             from which this converter is being invoked. Always check whether this value is null. Also, 
             properties on the context object may return null.
        
            culture: A System.Globalization.CultureInfo that specifies the culture to represent the color.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: An System.Object representing the converted value.
        """
        pass

    def GetStandardValues(self, context=None):
        """
        GetStandardValues(self: ColorConverter, context: ITypeDescriptorContext) -> StandardValuesCollection
        
            Retrieves a collection containing a set of standard values for the data type for which this 
             validator is designed. This will return null if the data type does not support a standard set of 
             values.
        
        
            context: A formatter context. Use this object to extract additional information about the environment 
             from which this converter is being invoked. Always check whether this value is null. Also, 
             properties on the context object may return null.
        
            Returns: A collection containing null or a standard set of valid values. The default implementation 
             always returns null.
        """
        pass

    def GetStandardValuesSupported(self, context=None):
        """
        GetStandardValuesSupported(self: ColorConverter, context: ITypeDescriptorContext) -> bool
        
            Determines if this object supports a standard set of values that can be chosen from a list.
        
            context: A System.ComponentModel.TypeDescriptor through which additional context can be provided.
            Returns: true if erload:System.Drawing.ColorConverter.GetStandardValues must be called to find a common 
             set of values the object supports; otherwise, false.
        """
        pass


class ColorTranslator(object):
    """ Translates colors to and from GDI+ System.Drawing.Color structures. This class cannot be inherited. """
    @staticmethod
    def FromHtml(htmlColor):
        """
        FromHtml(htmlColor: str) -> Color
        
            Translates an HTML color representation to a GDI+ System.Drawing.Color structure.
        
            htmlColor: The string representation of the Html color to translate.
            Returns: The System.Drawing.Color structure that represents the translated HTML color or 
             System.Drawing.Color.Empty if htmlColor is null.
        """
        pass

    @staticmethod
    def FromOle(oleColor):
        """
        FromOle(oleColor: int) -> Color
        
            Translates an OLE color value to a GDI+ System.Drawing.Color structure.
        
            oleColor: The OLE color to translate.
            Returns: The System.Drawing.Color structure that represents the translated OLE color.
        """
        pass

    @staticmethod
    def FromWin32(win32Color):
        """
        FromWin32(win32Color: int) -> Color
        
            Translates a Windows color value to a GDI+ System.Drawing.Color structure.
        
            win32Color: The Windows color to translate.
            Returns: The System.Drawing.Color structure that represents the translated Windows color.
        """
        pass

    @staticmethod
    def ToHtml(c):
        """
        ToHtml(c: Color) -> str
        
            Translates the specified System.Drawing.Color structure to an HTML string color representation.
        
            c: The System.Drawing.Color structure to translate.
            Returns: The string that represents the HTML color.
        """
        pass

    @staticmethod
    def ToOle(c):
        """
        ToOle(c: Color) -> int
        
            Translates the specified System.Drawing.Color structure to an OLE color.
        
            c: The System.Drawing.Color structure to translate.
            Returns: The OLE color value.
        """
        pass

    @staticmethod
    def ToWin32(c):
        """
        ToWin32(c: Color) -> int
        
            Translates the specified System.Drawing.Color structure to a Windows color.
        
            c: The System.Drawing.Color structure to translate.
            Returns: The Windows color value.
        """
        pass


class ContentAlignment(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies alignment of content on the drawing surface.
    
    enum ContentAlignment, values: BottomCenter (512), BottomLeft (256), BottomRight (1024), MiddleCenter (32), MiddleLeft (16), MiddleRight (64), TopCenter (2), TopLeft (1), TopRight (4)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BottomCenter = None
    BottomLeft = None
    BottomRight = None
    MiddleCenter = None
    MiddleLeft = None
    MiddleRight = None
    TopCenter = None
    TopLeft = None
    TopRight = None
    value__ = None


class CopyPixelOperation(Enum, IComparable, IFormattable, IConvertible):
    """
    Determines how the source color in a copy pixel operation is combined with the destination color to result in a final color.
    
    enum CopyPixelOperation, values: Blackness (66), CaptureBlt (1073741824), DestinationInvert (5570569), MergeCopy (12583114), MergePaint (12255782), NoMirrorBitmap (-2147483648), NotSourceCopy (3342344), NotSourceErase (1114278), PatCopy (15728673), PatInvert (5898313), PatPaint (16452105), SourceAnd (8913094), SourceCopy (13369376), SourceErase (4457256), SourceInvert (6684742), SourcePaint (15597702), Whiteness (16711778)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Blackness = None
    CaptureBlt = None
    DestinationInvert = None
    MergeCopy = None
    MergePaint = None
    NoMirrorBitmap = None
    NotSourceCopy = None
    NotSourceErase = None
    PatCopy = None
    PatInvert = None
    PatPaint = None
    SourceAnd = None
    SourceCopy = None
    SourceErase = None
    SourceInvert = None
    SourcePaint = None
    value__ = None
    Whiteness = None


class Font(MarshalByRefObject, ICloneable, ISerializable, IDisposable):
    """
    Defines a particular format for text, including font face, size, and style attributes. This class cannot be inherited.
    
    Font(prototype: Font, newStyle: FontStyle)
    Font(family: FontFamily, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte, gdiVerticalFont: bool)
    Font(family: FontFamily, emSize: Single, style: FontStyle)
    Font(familyName: str, emSize: Single)
    Font(family: FontFamily, emSize: Single, style: FontStyle, unit: GraphicsUnit)
    Font(family: FontFamily, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte)
    Font(familyName: str, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte)
    Font(familyName: str, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte, gdiVerticalFont: bool)
    Font(family: FontFamily, emSize: Single, unit: GraphicsUnit)
    Font(family: FontFamily, emSize: Single)
    Font(familyName: str, emSize: Single, style: FontStyle, unit: GraphicsUnit)
    Font(familyName: str, emSize: Single, style: FontStyle)
    Font(familyName: str, emSize: Single, unit: GraphicsUnit)
    """
    def Clone(self):
        """
        Clone(self: Font) -> object
        
            Creates an exact copy of this System.Drawing.Font.
            Returns: The System.Drawing.Font this method creates, cast as an System.Object.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Font)
            Releases all resources used by this System.Drawing.Font.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Font, obj: object) -> bool
        
            Indicates whether the specified object is a System.Drawing.Font and has the same 
             System.Drawing.Font.FontFamily, System.Drawing.Font.GdiVerticalFont, 
             System.Drawing.Font.GdiCharSet, System.Drawing.Font.Style, System.Drawing.Font.Size, and 
             System.Drawing.Font.Unit property values as this System.Drawing.Font.
        
        
            obj: The object to test.
            Returns: true if the obj parameter is a System.Drawing.Font and has the same 
             System.Drawing.Font.FontFamily, System.Drawing.Font.GdiVerticalFont, 
             System.Drawing.Font.GdiCharSet, System.Drawing.Font.Style, System.Drawing.Font.Size, and 
             System.Drawing.Font.Unit property values as this System.Drawing.Font; otherwise, false.
        """
        pass

    @staticmethod
    def FromHdc(hdc):
        """
        FromHdc(hdc: IntPtr) -> Font
        
            Creates a System.Drawing.Font from the specified Windows handle to a device context.
        
            hdc: A handle to a device context.
            Returns: The System.Drawing.Font this method creates.
        """
        pass

    @staticmethod
    def FromHfont(hfont):
        """
        FromHfont(hfont: IntPtr) -> Font
        
            Creates a System.Drawing.Font from the specified Windows handle.
        
            hfont: A Windows handle to a GDI font.
            Returns: The System.Drawing.Font this method creates.
        """
        pass

    @staticmethod
    def FromLogFont(lf, hdc=None):
        """
        FromLogFont(lf: object) -> Font
        
            Creates a System.Drawing.Font from the specified GDI logical font (LOGFONT) structure.
        
            lf: An System.Object that represents the GDI�LOGFONT structure from which to create the 
             System.Drawing.Font.
        
            Returns: The System.Drawing.Font that this method creates.
        FromLogFont(lf: object, hdc: IntPtr) -> Font
        
            Creates a System.Drawing.Font from the specified GDI logical font (LOGFONT) structure.
        
            lf: An System.Object that represents the GDI�LOGFONT structure from which to create the 
             System.Drawing.Font.
        
            hdc: A handle to a device context that contains additional information about the lf structure.
            Returns: The System.Drawing.Font that this method creates.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Font) -> int
        
            Gets the hash code for this System.Drawing.Font.
            Returns: The hash code for this System.Drawing.Font.
        """
        pass

    def GetHeight(self, *__args):
        """
        GetHeight(self: Font, dpi: Single) -> Single
        
            Returns the height, in pixels, of this System.Drawing.Font when drawn to a device with the 
             specified vertical resolution.
        
        
            dpi: The vertical resolution, in dots per inch, used to calculate the height of the font.
            Returns: The height, in pixels, of this System.Drawing.Font.
        GetHeight(self: Font) -> Single
        
            Returns the line spacing, in pixels, of this font.
            Returns: The line spacing, in pixels, of this font.
        GetHeight(self: Font, graphics: Graphics) -> Single
        
            Returns the line spacing, in the current unit of a specified System.Drawing.Graphics, of this 
             font.
        
        
            graphics: A System.Drawing.Graphics that holds the vertical resolution, in dots per inch, of the display 
             device as well as settings for page unit and page scale.
        
            Returns: The line spacing, in pixels, of this font.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def ToHfont(self):
        """
        ToHfont(self: Font) -> IntPtr
        
            Returns a handle to this System.Drawing.Font.
            Returns: A Windows handle to this System.Drawing.Font.
        """
        pass

    def ToLogFont(self, logFont, graphics=None):
        """
        ToLogFont(self: Font, logFont: object, graphics: Graphics)
            Creates a GDI logical font (LOGFONT) structure from this System.Drawing.Font.
        
            logFont: An System.Object that represents the LOGFONT structure that this method creates.
            graphics: A System.Drawing.Graphics that provides additional information for the LOGFONT structure.
        ToLogFont(self: Font, logFont: object)
            Creates a GDI logical font (LOGFONT) structure from this System.Drawing.Font.
        
            logFont: An System.Object that represents the LOGFONT structure that this method creates.
        """
        pass

    def ToString(self):
        """
        ToString(self: Font) -> str
        
            Returns a human-readable string representation of this System.Drawing.Font.
            Returns: A string that represents this System.Drawing.Font.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, prototype: Font, newStyle: FontStyle)
        __new__(cls: type, family: FontFamily, emSize: Single, style: FontStyle, unit: GraphicsUnit)
        __new__(cls: type, family: FontFamily, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte)
        __new__(cls: type, family: FontFamily, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte, gdiVerticalFont: bool)
        __new__(cls: type, familyName: str, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte)
        __new__(cls: type, familyName: str, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte, gdiVerticalFont: bool)
        __new__(cls: type, family: FontFamily, emSize: Single, style: FontStyle)
        __new__(cls: type, family: FontFamily, emSize: Single, unit: GraphicsUnit)
        __new__(cls: type, family: FontFamily, emSize: Single)
        __new__(cls: type, familyName: str, emSize: Single, style: FontStyle, unit: GraphicsUnit)
        __new__(cls: type, familyName: str, emSize: Single, style: FontStyle)
        __new__(cls: type, familyName: str, emSize: Single, unit: GraphicsUnit)
        __new__(cls: type, familyName: str, emSize: Single)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Bold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Drawing.Font is bold.

Get: Bold(self: Font) -> bool

"""

    FontFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Drawing.FontFamily associated with this System.Drawing.Font.

Get: FontFamily(self: Font) -> FontFamily

"""

    GdiCharSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a byte value that specifies the GDI character set that this System.Drawing.Font uses.

Get: GdiCharSet(self: Font) -> Byte

"""

    GdiVerticalFont = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value that indicates whether this System.Drawing.Font is derived from a GDI vertical font.

Get: GdiVerticalFont(self: Font) -> bool

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the line spacing of this font.

Get: Height(self: Font) -> int

"""

    IsSystemFont = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the font is a member of System.Drawing.SystemFonts.

Get: IsSystemFont(self: Font) -> bool

"""

    Italic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this font has the italic style applied.

Get: Italic(self: Font) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the face name of this System.Drawing.Font.

Get: Name(self: Font) -> str

"""

    OriginalFontName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the font originally specified.

Get: OriginalFontName(self: Font) -> str

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the em-size of this System.Drawing.Font measured in the units specified by the System.Drawing.Font.Unit property.

Get: Size(self: Font) -> Single

"""

    SizeInPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the em-size, in points, of this System.Drawing.Font.

Get: SizeInPoints(self: Font) -> Single

"""

    Strikeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Drawing.Font specifies a horizontal line through the font.

Get: Strikeout(self: Font) -> bool

"""

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets style information for this System.Drawing.Font.

Get: Style(self: Font) -> FontStyle

"""

    SystemFontName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the system font if the System.Drawing.Font.IsSystemFont property returns true.

Get: SystemFontName(self: Font) -> str

"""

    Underline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Drawing.Font is underlined.

Get: Underline(self: Font) -> bool

"""

    Unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unit of measure for this System.Drawing.Font.

Get: Unit(self: Font) -> GraphicsUnit

"""



class FontConverter(TypeConverter):
    """
    Converts System.Drawing.Font objects from one data type to another.
    
    FontConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: FontConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether this converter can convert an object in the specified source type to the 
             native type of the converter.
        
        
            context: A formatter context. This object can be used to get additional information about the environment 
             this converter is being called from. This may be null, so you should always check. Also, 
             properties on the context object may also return null.
        
            sourceType: The type you want to convert from.
            Returns: This method returns true if this object can perform the conversion.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: FontConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object to the given destination 
             type using the context.
        
        
            context: An ITypeDescriptorContext object that provides a format context.
            destinationType: A System.Type object that represents the type you want to convert to.
            Returns: This method returns true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: FontConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the specified object to the native type of the converter.
        
            context: A formatter context. This object can be used to get additional information about the environment 
             this converter is being called from. This may be null, so you should always check. Also, 
             properties on the context object may also return null.
        
            culture: A CultureInfo object that specifies the culture used to represent the font.
            value: The object to convert.
            Returns: The converted object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: FontConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified object to another type.
        
            context: A formatter context. This object can be used to get additional information about the environment 
             this converter is being called from. This may be null, so you should always check. Also, 
             properties on the context object may also return null.
        
            culture: A System.Globalization.CultureInfo object that specifies the culture used to represent the 
             object.
        
            value: The object to convert.
            destinationType: The data type to convert the object to.
            Returns: The converted object.
        """
        pass

    def CreateInstance(self, *__args):
        """
        CreateInstance(self: FontConverter, context: ITypeDescriptorContext, propertyValues: IDictionary) -> object
        
            Creates an object of this type by using a specified set of property values for the object.
        
            context: A type descriptor through which additional context can be provided.
            propertyValues: A dictionary of new property values. The dictionary contains a series of name-value pairs, one 
             for each property returned from the erload:System.Drawing.FontConverter.GetProperties method.
        
            Returns: The newly created object, or null if the object could not be created. The default implementation 
             returns 
             null.System.Drawing.FontConverter.CreateInstance(System.ComponentModel.ITypeDescriptorContext,Sys
             tem.Collections.IDictionary) useful for creating non-changeable objects that have changeable 
             properties.
        """
        pass

    def GetCreateInstanceSupported(self, context=None):
        """
        GetCreateInstanceSupported(self: FontConverter, context: ITypeDescriptorContext) -> bool
        
            Determines whether changing a value on this object should require a call to the 
             erload:System.Drawing.FontConverter.CreateInstance method to create a new value.
        
        
            context: A type descriptor through which additional context can be provided.
            Returns: This method returns true if the CreateInstance object should be called when a change is made to 
             one or more properties of this object; otherwise, false.
        """
        pass

    def GetProperties(self, *__args):
        """
        GetProperties(self: FontConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Retrieves the set of properties for this type. By default, a type does not have any properties 
             to return.
        
        
            context: A type descriptor through which additional context can be provided.
            value: The value of the object to get the properties for.
            attributes: An array of System.Attribute objects that describe the properties.
            Returns: The set of properties that should be exposed for this data type. If no properties should be 
             exposed, this may return null. The default implementation always returns null.An easy 
             implementation of this method can call the 
             erload:System.ComponentModel.TypeConverter.GetProperties method for the correct data type.
        """
        pass

    def GetPropertiesSupported(self, context=None):
        """
        GetPropertiesSupported(self: FontConverter, context: ITypeDescriptorContext) -> bool
        
            Determines whether this object supports properties. The default is false.
        
            context: A type descriptor through which additional context can be provided.
            Returns: This method returns true if the 
             System.Drawing.FontConverter.GetPropertiesSupported(System.ComponentModel.ITypeDescriptorContext)
              method should be called to find the properties of this object; otherwise, false.
        """
        pass

    FontNameConverter = None
    FontUnitConverter = None


class FontFamily(MarshalByRefObject, IDisposable):
    """
    Defines a group of type faces having a similar basic design and certain variations in styles. This class cannot be inherited.
    
    FontFamily(name: str)
    FontFamily(name: str, fontCollection: FontCollection)
    FontFamily(genericFamily: GenericFontFamilies)
    """
    def Dispose(self):
        """
        Dispose(self: FontFamily)
            Releases all resources used by this System.Drawing.FontFamily.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: FontFamily, obj: object) -> bool
        
            Indicates whether the specified object is a System.Drawing.FontFamily and is identical to this 
             System.Drawing.FontFamily.
        
        
            obj: The object to test.
            Returns: true if obj is a System.Drawing.FontFamily and is identical to this System.Drawing.FontFamily; 
             otherwise, false.
        """
        pass

    def GetCellAscent(self, style):
        """
        GetCellAscent(self: FontFamily, style: FontStyle) -> int
        
            Returns the cell ascent, in design units, of the System.Drawing.FontFamily of the specified 
             style.
        
        
            style: A System.Drawing.FontStyle that contains style information for the font.
            Returns: The cell ascent for this System.Drawing.FontFamily that uses the specified 
             System.Drawing.FontStyle.
        """
        pass

    def GetCellDescent(self, style):
        """
        GetCellDescent(self: FontFamily, style: FontStyle) -> int
        
            Returns the cell descent, in design units, of the System.Drawing.FontFamily of the specified 
             style.
        
        
            style: A System.Drawing.FontStyle that contains style information for the font.
            Returns: The cell descent metric for this System.Drawing.FontFamily that uses the specified 
             System.Drawing.FontStyle.
        """
        pass

    def GetEmHeight(self, style):
        """
        GetEmHeight(self: FontFamily, style: FontStyle) -> int
        
            Gets the height, in font design units, of the em square for the specified style.
        
            style: The System.Drawing.FontStyle for which to get the em height.
            Returns: The height of the em square.
        """
        pass

    @staticmethod
    def GetFamilies(graphics):
        """
        GetFamilies(graphics: Graphics) -> Array[FontFamily]
        
            Returns an array that contains all the System.Drawing.FontFamily objects available for the 
             specified graphics context.
        
        
            graphics: The System.Drawing.Graphics object from which to return System.Drawing.FontFamily objects.
            Returns: An array of System.Drawing.FontFamily objects available for the specified 
             System.Drawing.Graphics object.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: FontFamily) -> int
        
            Gets a hash code for this System.Drawing.FontFamily.
            Returns: The hash code for this System.Drawing.FontFamily.
        """
        pass

    def GetLineSpacing(self, style):
        """
        GetLineSpacing(self: FontFamily, style: FontStyle) -> int
        
            Returns the line spacing, in design units, of the System.Drawing.FontFamily of the specified 
             style. The line spacing is the vertical distance between the base lines of two consecutive lines 
             of text.
        
        
            style: The System.Drawing.FontStyle to apply.
            Returns: The distance between two consecutive lines of text.
        """
        pass

    def GetName(self, language):
        """
        GetName(self: FontFamily, language: int) -> str
        
            Returns the name, in the specified language, of this System.Drawing.FontFamily.
        
            language: The language in which the name is returned.
            Returns: A System.String that represents the name, in the specified language, of this 
             System.Drawing.FontFamily.
        """
        pass

    def IsStyleAvailable(self, style):
        """
        IsStyleAvailable(self: FontFamily, style: FontStyle) -> bool
        
            Indicates whether the specified System.Drawing.FontStyle enumeration is available.
        
            style: The System.Drawing.FontStyle to test.
            Returns: true if the specified System.Drawing.FontStyle is available; otherwise, false.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def ToString(self):
        """
        ToString(self: FontFamily) -> str
        
            Converts this System.Drawing.FontFamily to a human-readable string representation.
            Returns: The string that represents this System.Drawing.FontFamily.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, fontCollection: FontCollection)
        __new__(cls: type, genericFamily: GenericFontFamilies)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of this System.Drawing.FontFamily.

Get: Name(self: FontFamily) -> str

"""


    Families = None
    GenericMonospace = None
    GenericSansSerif = None
    GenericSerif = None


class FontStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies style information applied to text.
    
    enum (flags) FontStyle, values: Bold (1), Italic (2), Regular (0), Strikeout (8), Underline (4)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Bold = None
    Italic = None
    Regular = None
    Strikeout = None
    Underline = None
    value__ = None


class Graphics(MarshalByRefObject, IDisposable, IDeviceContext):
    """ Encapsulates a GDI+ drawing surface. This class cannot be inherited. """
    def AddMetafileComment(self, data):
        """
        AddMetafileComment(self: Graphics, data: Array[Byte])
            Adds a comment to the current System.Drawing.Imaging.Metafile.
        
            data: Array of bytes that contains the comment.
        """
        pass

    def BeginContainer(self, dstrect=None, srcrect=None, unit=None):
        """
        BeginContainer(self: Graphics, dstrect: Rectangle, srcrect: Rectangle, unit: GraphicsUnit) -> GraphicsContainer
        
            Saves a graphics container with the current state of this System.Drawing.Graphics and opens and 
             uses a new graphics container with the specified scale transformation.
        
        
            dstrect: System.Drawing.Rectangle structure that, together with the srcrect parameter, specifies a scale 
             transformation for the container.
        
            srcrect: System.Drawing.Rectangle structure that, together with the dstrect parameter, specifies a scale 
             transformation for the container.
        
            unit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the unit of measure for the 
             container.
        
            Returns: This method returns a System.Drawing.Drawing2D.GraphicsContainer that represents the state of 
             this System.Drawing.Graphics at the time of the method call.
        
        BeginContainer(self: Graphics, dstrect: RectangleF, srcrect: RectangleF, unit: GraphicsUnit) -> GraphicsContainer
        
            Saves a graphics container with the current state of this System.Drawing.Graphics and opens and 
             uses a new graphics container with the specified scale transformation.
        
        
            dstrect: System.Drawing.RectangleF structure that, together with the srcrect parameter, specifies a scale 
             transformation for the new graphics container.
        
            srcrect: System.Drawing.RectangleF structure that, together with the dstrect parameter, specifies a scale 
             transformation for the new graphics container.
        
            unit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the unit of measure for the 
             container.
        
            Returns: This method returns a System.Drawing.Drawing2D.GraphicsContainer that represents the state of 
             this System.Drawing.Graphics at the time of the method call.
        
        BeginContainer(self: Graphics) -> GraphicsContainer
        
            Saves a graphics container with the current state of this System.Drawing.Graphics and opens and 
             uses a new graphics container.
        
            Returns: This method returns a System.Drawing.Drawing2D.GraphicsContainer that represents the state of 
             this System.Drawing.Graphics at the time of the method call.
        """
        pass

    def Clear(self, color):
        """
        Clear(self: Graphics, color: Color)
            Clears the entire drawing surface and fills it with the specified background color.
        
            color: System.Drawing.Color structure that represents the background color of the drawing surface.
        """
        pass

    def CopyFromScreen(self, *__args):
        """
        CopyFromScreen(self: Graphics, upperLeftSource: Point, upperLeftDestination: Point, blockRegionSize: Size, copyPixelOperation: CopyPixelOperation)
            Performs a bit-block transfer of color data, corresponding to a rectangle of pixels, from the 
             screen to the drawing surface of the System.Drawing.Graphics.
        
        
            upperLeftSource: The point at the upper-left corner of the source rectangle.
            upperLeftDestination: The point at the upper-left corner of the destination rectangle.
            blockRegionSize: The size of the area to be transferred.
            copyPixelOperation: One of the System.Drawing.CopyPixelOperation values.
        CopyFromScreen(self: Graphics, sourceX: int, sourceY: int, destinationX: int, destinationY: int, blockRegionSize: Size, copyPixelOperation: CopyPixelOperation)
            Performs a bit-block transfer of the color data, corresponding to a rectangle of pixels, from 
             the screen to the drawing surface of the System.Drawing.Graphics.
        
        
            sourceX: The x-coordinate of the point at the upper-left corner of the source rectangle.
            sourceY: The y-coordinate of the point at the upper-left corner of the source rectangle
            destinationX: The x-coordinate of the point at the upper-left corner of the destination rectangle.
            destinationY: The y-coordinate of the point at the upper-left corner of the destination rectangle.
            blockRegionSize: The size of the area to be transferred.
            copyPixelOperation: One of the System.Drawing.CopyPixelOperation values.
        CopyFromScreen(self: Graphics, upperLeftSource: Point, upperLeftDestination: Point, blockRegionSize: Size)
            Performs a bit-block transfer of color data, corresponding to a rectangle of pixels, from the 
             screen to the drawing surface of the System.Drawing.Graphics.
        
        
            upperLeftSource: The point at the upper-left corner of the source rectangle.
            upperLeftDestination: The point at the upper-left corner of the destination rectangle.
            blockRegionSize: The size of the area to be transferred.
        CopyFromScreen(self: Graphics, sourceX: int, sourceY: int, destinationX: int, destinationY: int, blockRegionSize: Size)
            Performs a bit-block transfer of the color data, corresponding to a rectangle of pixels, from 
             the screen to the drawing surface of the System.Drawing.Graphics.
        
        
            sourceX: The x-coordinate of the point at the upper-left corner of the source rectangle.
            sourceY: The y-coordinate of the point at the upper-left corner of the source rectangle.
            destinationX: The x-coordinate of the point at the upper-left corner of the destination rectangle.
            destinationY: The y-coordinate of the point at the upper-left corner of the destination rectangle.
            blockRegionSize: The size of the area to be transferred.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Graphics)
            Releases all resources used by this System.Drawing.Graphics.
        """
        pass

    def DrawArc(self, pen, *__args):
        """
        DrawArc(self: Graphics, pen: Pen, x: int, y: int, width: int, height: int, startAngle: int, sweepAngle: int)
            Draws an arc representing a portion of an ellipse specified by a pair of coordinates, a width, 
             and a height.
        
        
            pen: System.Drawing.Pen that determines the color, width, and style of the arc.
            x: The x-coordinate of the upper-left corner of the rectangle that defines the ellipse.
            y: The y-coordinate of the upper-left corner of the rectangle that defines the ellipse.
            width: Width of the rectangle that defines the ellipse.
            height: Height of the rectangle that defines the ellipse.
            startAngle: Angle in degrees measured clockwise from the x-axis to the starting point of the arc.
            sweepAngle: Angle in degrees measured clockwise from the startAngle parameter to ending point of the arc.
        DrawArc(self: Graphics, pen: Pen, rect: Rectangle, startAngle: Single, sweepAngle: Single)
            Draws an arc representing a portion of an ellipse specified by a System.Drawing.Rectangle 
             structure.
        
        
            pen: System.Drawing.Pen that determines the color, width, and style of the arc.
            rect: System.Drawing.RectangleF structure that defines the boundaries of the ellipse.
            startAngle: Angle in degrees measured clockwise from the x-axis to the starting point of the arc.
            sweepAngle: Angle in degrees measured clockwise from the startAngle parameter to ending point of the arc.
        DrawArc(self: Graphics, pen: Pen, x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single)
            Draws an arc representing a portion of an ellipse specified by a pair of coordinates, a width, 
             and a height.
        
        
            pen: System.Drawing.Pen that determines the color, width, and style of the arc.
            x: The x-coordinate of the upper-left corner of the rectangle that defines the ellipse.
            y: The y-coordinate of the upper-left corner of the rectangle that defines the ellipse.
            width: Width of the rectangle that defines the ellipse.
            height: Height of the rectangle that defines the ellipse.
            startAngle: Angle in degrees measured clockwise from the x-axis to the starting point of the arc.
            sweepAngle: Angle in degrees measured clockwise from the startAngle parameter to ending point of the arc.
        DrawArc(self: Graphics, pen: Pen, rect: RectangleF, startAngle: Single, sweepAngle: Single)
            Draws an arc representing a portion of an ellipse specified by a System.Drawing.RectangleF 
             structure.
        
        
            pen: System.Drawing.Pen that determines the color, width, and style of the arc.
            rect: System.Drawing.RectangleF structure that defines the boundaries of the ellipse.
            startAngle: Angle in degrees measured clockwise from the x-axis to the starting point of the arc.
            sweepAngle: Angle in degrees measured clockwise from the startAngle parameter to ending point of the arc.
        """
        pass

    def DrawBezier(self, pen, *__args):
        """
        DrawBezier(self: Graphics, pen: Pen, pt1: Point, pt2: Point, pt3: Point, pt4: Point)
            Draws a B�zier spline defined by four System.Drawing.Point structures.
        
            pen: System.Drawing.Pen structure that determines the color, width, and style of the curve.
            pt1: System.Drawing.Point structure that represents the starting point of the curve.
            pt2: System.Drawing.Point structure that represents the first control point for the curve.
            pt3: System.Drawing.Point structure that represents the second control point for the curve.
            pt4: System.Drawing.Point structure that represents the ending point of the curve.
        DrawBezier(self: Graphics, pen: Pen, pt1: PointF, pt2: PointF, pt3: PointF, pt4: PointF)
            Draws a B�zier spline defined by four System.Drawing.PointF structures.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the curve.
            pt1: System.Drawing.PointF structure that represents the starting point of the curve.
            pt2: System.Drawing.PointF structure that represents the first control point for the curve.
            pt3: System.Drawing.PointF structure that represents the second control point for the curve.
            pt4: System.Drawing.PointF structure that represents the ending point of the curve.
        DrawBezier(self: Graphics, pen: Pen, x1: Single, y1: Single, x2: Single, y2: Single, x3: Single, y3: Single, x4: Single, y4: Single)
            Draws a B�zier spline defined by four ordered pairs of coordinates that represent points.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the curve.
            x1: The x-coordinate of the starting point of the curve.
            y1: The y-coordinate of the starting point of the curve.
            x2: The x-coordinate of the first control point of the curve.
            y2: The y-coordinate of the first control point of the curve.
            x3: The x-coordinate of the second control point of the curve.
            y3: The y-coordinate of the second control point of the curve.
            x4: The x-coordinate of the ending point of the curve.
            y4: The y-coordinate of the ending point of the curve.
        """
        pass

    def DrawBeziers(self, pen, points):
        """
        DrawBeziers(self: Graphics, pen: Pen, points: Array[Point])
            Draws a series of B�zier splines from an array of System.Drawing.Point structures.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the curve.
            points: Array of System.Drawing.Point structures that represent the points that determine the curve. The 
             number of points in the array should be a multiple of 3 plus 1, such as 4, 7, or 10.
        
        DrawBeziers(self: Graphics, pen: Pen, points: Array[PointF])
            Draws a series of B�zier splines from an array of System.Drawing.PointF structures.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the curve.
            points: Array of System.Drawing.PointF structures that represent the points that determine the curve. 
             The number of points in the array should be a multiple of 3 plus 1, such as 4, 7, or 10.
        """
        pass

    def DrawClosedCurve(self, pen, points, tension=None, fillmode=None):
        """
        DrawClosedCurve(self: Graphics, pen: Pen, points: Array[Point])
            Draws a closed cardinal spline defined by an array of System.Drawing.Point structures.
        
            pen: System.Drawing.Pen that determines the color, width, and height of the curve.
            points: Array of System.Drawing.Point structures that define the spline.
        DrawClosedCurve(self: Graphics, pen: Pen, points: Array[Point], tension: Single, fillmode: FillMode)
            Draws a closed cardinal spline defined by an array of System.Drawing.Point structures using a 
             specified tension.
        
        
            pen: System.Drawing.Pen that determines the color, width, and height of the curve.
            points: Array of System.Drawing.Point structures that define the spline.
            tension: Value greater than or equal to 0.0F that specifies the tension of the curve.
            fillmode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines how the curve is 
             filled. This parameter is required but ignored.
        
        DrawClosedCurve(self: Graphics, pen: Pen, points: Array[PointF])
            Draws a closed cardinal spline defined by an array of System.Drawing.PointF structures.
        
            pen: System.Drawing.Pen that determines the color, width, and height of the curve.
            points: Array of System.Drawing.PointF structures that define the spline.
        DrawClosedCurve(self: Graphics, pen: Pen, points: Array[PointF], tension: Single, fillmode: FillMode)
            Draws a closed cardinal spline defined by an array of System.Drawing.PointF structures using a 
             specified tension.
        
        
            pen: System.Drawing.Pen that determines the color, width, and height of the curve.
            points: Array of System.Drawing.PointF structures that define the spline.
            tension: Value greater than or equal to 0.0F that specifies the tension of the curve.
            fillmode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines how the curve is 
             filled. This parameter is required but is ignored.
        """
        pass

    def DrawCurve(self, pen, points, *__args):
        """
        DrawCurve(self: Graphics, pen: Pen, points: Array[Point])
            Draws a cardinal spline through a specified array of System.Drawing.Point structures.
        
            pen: System.Drawing.Pen that determines the color, width, and height of the curve.
            points: Array of System.Drawing.Point structures that define the spline.
        DrawCurve(self: Graphics, pen: Pen, points: Array[Point], tension: Single)
            Draws a cardinal spline through a specified array of System.Drawing.Point structures using a 
             specified tension.
        
        
            pen: System.Drawing.Pen that determines the color, width, and height of the curve.
            points: Array of System.Drawing.Point structures that define the spline.
            tension: Value greater than or equal to 0.0F that specifies the tension of the curve.
        DrawCurve(self: Graphics, pen: Pen, points: Array[Point], offset: int, numberOfSegments: int, tension: Single)
            Draws a cardinal spline through a specified array of System.Drawing.Point structures using a 
             specified tension.
        
        
            pen: System.Drawing.Pen that determines the color, width, and height of the curve.
            points: Array of System.Drawing.Point structures that define the spline.
            offset: Offset from the first element in the array of the points parameter to the starting point in the 
             curve.
        
            numberOfSegments: Number of segments after the starting point to include in the curve.
            tension: Value greater than or equal to 0.0F that specifies the tension of the curve.
        DrawCurve(self: Graphics, pen: Pen, points: Array[PointF], offset: int, numberOfSegments: int, tension: Single)
            Draws a cardinal spline through a specified array of System.Drawing.PointF structures using a 
             specified tension. The drawing begins offset from the beginning of the array.
        
        
            pen: System.Drawing.Pen that determines the color, width, and height of the curve.
            points: Array of System.Drawing.PointF structures that define the spline.
            offset: Offset from the first element in the array of the points parameter to the starting point in the 
             curve.
        
            numberOfSegments: Number of segments after the starting point to include in the curve.
            tension: Value greater than or equal to 0.0F that specifies the tension of the curve.
        DrawCurve(self: Graphics, pen: Pen, points: Array[PointF])
            Draws a cardinal spline through a specified array of System.Drawing.PointF structures.
        
            pen: System.Drawing.Pen that determines the color, width, and height of the curve.
            points: Array of System.Drawing.PointF structures that define the spline.
        DrawCurve(self: Graphics, pen: Pen, points: Array[PointF], tension: Single)
            Draws a cardinal spline through a specified array of System.Drawing.PointF structures using a 
             specified tension.
        
        
            pen: System.Drawing.Pen that determines the color, width, and height of the curve.
            points: Array of System.Drawing.PointF structures that represent the points that define the curve.
            tension: Value greater than or equal to 0.0F that specifies the tension of the curve.
        DrawCurve(self: Graphics, pen: Pen, points: Array[PointF], offset: int, numberOfSegments: int)
            Draws a cardinal spline through a specified array of System.Drawing.PointF structures. The 
             drawing begins offset from the beginning of the array.
        
        
            pen: System.Drawing.Pen that determines the color, width, and height of the curve.
            points: Array of System.Drawing.PointF structures that define the spline.
            offset: Offset from the first element in the array of the points parameter to the starting point in the 
             curve.
        
            numberOfSegments: Number of segments after the starting point to include in the curve.
        """
        pass

    def DrawEllipse(self, pen, *__args):
        """
        DrawEllipse(self: Graphics, pen: Pen, rect: Rectangle)
            Draws an ellipse specified by a bounding System.Drawing.Rectangle structure.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the ellipse.
            rect: System.Drawing.Rectangle structure that defines the boundaries of the ellipse.
        DrawEllipse(self: Graphics, pen: Pen, x: int, y: int, width: int, height: int)
            Draws an ellipse defined by a bounding rectangle specified by coordinates for the upper-left 
             corner of the rectangle, a height, and a width.
        
        
            pen: System.Drawing.Pen that determines the color, width, and style of the ellipse.
            x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.
            y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.
            width: Width of the bounding rectangle that defines the ellipse.
            height: Height of the bounding rectangle that defines the ellipse.
        DrawEllipse(self: Graphics, pen: Pen, rect: RectangleF)
            Draws an ellipse defined by a bounding System.Drawing.RectangleF.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the ellipse.
            rect: System.Drawing.RectangleF structure that defines the boundaries of the ellipse.
        DrawEllipse(self: Graphics, pen: Pen, x: Single, y: Single, width: Single, height: Single)
            Draws an ellipse defined by a bounding rectangle specified by a pair of coordinates, a height, 
             and a width.
        
        
            pen: System.Drawing.Pen that determines the color, width, and style of the ellipse.
            x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.
            y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.
            width: Width of the bounding rectangle that defines the ellipse.
            height: Height of the bounding rectangle that defines the ellipse.
        """
        pass

    def DrawIcon(self, icon, *__args):
        """
        DrawIcon(self: Graphics, icon: Icon, targetRect: Rectangle)
            Draws the image represented by the specified System.Drawing.Icon within the area specified by a 
             System.Drawing.Rectangle structure.
        
        
            icon: System.Drawing.Icon to draw.
            targetRect: System.Drawing.Rectangle structure that specifies the location and size of the resulting image 
             on the display surface. The image contained in the icon parameter is scaled to the dimensions of 
             this rectangular area.
        
        DrawIcon(self: Graphics, icon: Icon, x: int, y: int)
            Draws the image represented by the specified System.Drawing.Icon at the specified coordinates.
        
            icon: System.Drawing.Icon to draw.
            x: The x-coordinate of the upper-left corner of the drawn image.
            y: The y-coordinate of the upper-left corner of the drawn image.
        """
        pass

    def DrawIconUnstretched(self, icon, targetRect):
        """
        DrawIconUnstretched(self: Graphics, icon: Icon, targetRect: Rectangle)
            Draws the image represented by the specified System.Drawing.Icon without scaling the image.
        
            icon: System.Drawing.Icon to draw.
            targetRect: System.Drawing.Rectangle structure that specifies the location and size of the resulting image. 
             The image is not scaled to fit this rectangle, but retains its original size. If the image is 
             larger than the rectangle, it is clipped to fit inside it.
        """
        pass

    def DrawImage(self, image, *__args):
        """
        DrawImage(self: Graphics, image: Image, destPoints: Array[PointF], srcRect: RectangleF, srcUnit: GraphicsUnit, imageAttr: ImageAttributes, callback: DrawImageAbort, callbackData: int)DrawImage(self: Graphics, image: Image, destPoints: Array[Point], srcRect: Rectangle, srcUnit: GraphicsUnit)
            Draws the specified portion of the specified System.Drawing.Image at the specified location and 
             with the specified size.
        
        
            image: System.Drawing.Image to draw.
            destPoints: Array of three System.Drawing.Point structures that define a parallelogram.
            srcRect: System.Drawing.Rectangle structure that specifies the portion of the image object to draw.
            srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 
             by the srcRect parameter.
        
        DrawImage(self: Graphics, image: Image, destPoints: Array[Point], srcRect: Rectangle, srcUnit: GraphicsUnit, imageAttr: ImageAttributes)
            Draws the specified portion of the specified System.Drawing.Image at the specified location.
        
            image: System.Drawing.Image to draw.
            destPoints: Array of three System.Drawing.Point structures that define a parallelogram.
            srcRect: System.Drawing.Rectangle structure that specifies the portion of the image object to draw.
            srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 
             by the srcRect parameter.
        
            imageAttr: System.Drawing.Imaging.ImageAttributes that specifies recoloring and gamma information for the 
             image object.
        
        DrawImage(self: Graphics, image: Image, destPoints: Array[PointF], srcRect: RectangleF, srcUnit: GraphicsUnit, imageAttr: ImageAttributes, callback: DrawImageAbort)DrawImage(self: Graphics, image: Image, destRect: RectangleF, srcRect: RectangleF, srcUnit: GraphicsUnit)
            Draws the specified portion of the specified System.Drawing.Image at the specified location and 
             with the specified size.
        
        
            image: System.Drawing.Image to draw.
            destRect: System.Drawing.RectangleF structure that specifies the location and size of the drawn image. The 
             image is scaled to fit the rectangle.
        
            srcRect: System.Drawing.RectangleF structure that specifies the portion of the image object to draw.
            srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 
             by the srcRect parameter.
        
        DrawImage(self: Graphics, image: Image, destPoints: Array[PointF], srcRect: RectangleF, srcUnit: GraphicsUnit)
            Draws the specified portion of the specified System.Drawing.Image at the specified location and 
             with the specified size.
        
        
            image: System.Drawing.Image to draw.
            destPoints: Array of three System.Drawing.PointF structures that define a parallelogram.
            srcRect: System.Drawing.RectangleF structure that specifies the portion of the image object to draw.
            srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 
             by the srcRect parameter.
        
        DrawImage(self: Graphics, image: Image, destPoints: Array[PointF], srcRect: RectangleF, srcUnit: GraphicsUnit, imageAttr: ImageAttributes)
            Draws the specified portion of the specified System.Drawing.Image at the specified location and 
             with the specified size.
        
        
            image: System.Drawing.Image to draw.
            destPoints: Array of three System.Drawing.PointF structures that define a parallelogram.
            srcRect: System.Drawing.RectangleF structure that specifies the portion of the image object to draw.
            srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 
             by the srcRect parameter.
        
            imageAttr: System.Drawing.Imaging.ImageAttributes that specifies recoloring and gamma information for the 
             image object.
        
        DrawImage(self: Graphics, image: Image, destPoints: Array[Point], srcRect: Rectangle, srcUnit: GraphicsUnit, imageAttr: ImageAttributes, callback: DrawImageAbort)DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: Single, srcY: Single, srcWidth: Single, srcHeight: Single, srcUnit: GraphicsUnit, imageAttrs: ImageAttributes, callback: DrawImageAbort, callbackData: IntPtr)DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: int, srcY: int, srcWidth: int, srcHeight: int, srcUnit: GraphicsUnit)
            Draws the specified portion of the specified System.Drawing.Image at the specified location and 
             with the specified size.
        
        
            image: System.Drawing.Image to draw.
            destRect: System.Drawing.Rectangle structure that specifies the location and size of the drawn image. The 
             image is scaled to fit the rectangle.
        
            srcX: The x-coordinate of the upper-left corner of the portion of the source image to draw.
            srcY: The y-coordinate of the upper-left corner of the portion of the source image to draw.
            srcWidth: Width of the portion of the source image to draw.
            srcHeight: Height of the portion of the source image to draw.
            srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 
             to determine the source rectangle.
        
        DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: int, srcY: int, srcWidth: int, srcHeight: int, srcUnit: GraphicsUnit, imageAttr: ImageAttributes, callback: DrawImageAbort)DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: Single, srcY: Single, srcWidth: Single, srcHeight: Single, srcUnit: GraphicsUnit, imageAttrs: ImageAttributes, callback: DrawImageAbort)DrawImage(self: Graphics, image: Image, destPoints: Array[Point], srcRect: Rectangle, srcUnit: GraphicsUnit, imageAttr: ImageAttributes, callback: DrawImageAbort, callbackData: int)DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: Single, srcY: Single, srcWidth: Single, srcHeight: Single, srcUnit: GraphicsUnit)
            Draws the specified portion of the specified System.Drawing.Image at the specified location and 
             with the specified size.
        
        
            image: System.Drawing.Image to draw.
            destRect: System.Drawing.Rectangle structure that specifies the location and size of the drawn image. The 
             image is scaled to fit the rectangle.
        
            srcX: The x-coordinate of the upper-left corner of the portion of the source image to draw.
            srcY: The y-coordinate of the upper-left corner of the portion of the source image to draw.
            srcWidth: Width of the portion of the source image to draw.
            srcHeight: Height of the portion of the source image to draw.
            srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 
             to determine the source rectangle.
        
        DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: Single, srcY: Single, srcWidth: Single, srcHeight: Single, srcUnit: GraphicsUnit, imageAttrs: ImageAttributes)
            Draws the specified portion of the specified System.Drawing.Image at the specified location and 
             with the specified size.
        
        
            image: System.Drawing.Image to draw.
            destRect: System.Drawing.Rectangle structure that specifies the location and size of the drawn image. The 
             image is scaled to fit the rectangle.
        
            srcX: The x-coordinate of the upper-left corner of the portion of the source image to draw.
            srcY: The y-coordinate of the upper-left corner of the portion of the source image to draw.
            srcWidth: Width of the portion of the source image to draw.
            srcHeight: Height of the portion of the source image to draw.
            srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 
             to determine the source rectangle.
        
            imageAttrs: System.Drawing.Imaging.ImageAttributes that specifies recoloring and gamma information for the 
             image object.
        
        DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: int, srcY: int, srcWidth: int, srcHeight: int, srcUnit: GraphicsUnit, imageAttr: ImageAttributes)
            Draws the specified portion of the specified System.Drawing.Image at the specified location and 
             with the specified size.
        
        
            image: System.Drawing.Image to draw.
            destRect: System.Drawing.Rectangle structure that specifies the location and size of the drawn image. The 
             image is scaled to fit the rectangle.
        
            srcX: The x-coordinate of the upper-left corner of the portion of the source image to draw.
            srcY: The y-coordinate of the upper-left corner of the portion of the source image to draw.
            srcWidth: Width of the portion of the source image to draw.
            srcHeight: Height of the portion of the source image to draw.
            srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 
             to determine the source rectangle.
        
            imageAttr: System.Drawing.Imaging.ImageAttributes that specifies recoloring and gamma information for the 
             image object.
        
        DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: int, srcY: int, srcWidth: int, srcHeight: int, srcUnit: GraphicsUnit, imageAttrs: ImageAttributes, callback: DrawImageAbort, callbackData: IntPtr)DrawImage(self: Graphics, image: Image, point: PointF)
            Draws the specified System.Drawing.Image, using its original physical size, at the specified 
             location.
        
        
            image: System.Drawing.Image to draw.
            point: System.Drawing.PointF structure that represents the upper-left corner of the drawn image.
        DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcRect: Rectangle, srcUnit: GraphicsUnit)
            Draws the specified portion of the specified System.Drawing.Image at the specified location and 
             with the specified size.
        
        
            image: System.Drawing.Image to draw.
            destRect: System.Drawing.Rectangle structure that specifies the location and size of the drawn image. The 
             image is scaled to fit the rectangle.
        
            srcRect: System.Drawing.Rectangle structure that specifies the portion of the image object to draw.
            srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 
             by the srcRect parameter.
        
        DrawImage(self: Graphics, image: Image, x: int, y: int)
            Draws the specified image, using its original physical size, at the location specified by a 
             coordinate pair.
        
        
            image: System.Drawing.Image to draw.
            x: The x-coordinate of the upper-left corner of the drawn image.
            y: The y-coordinate of the upper-left corner of the drawn image.
        DrawImage(self: Graphics, image: Image, rect: Rectangle)
            Draws the specified System.Drawing.Image at the specified location and with the specified size.
        
            image: System.Drawing.Image to draw.
            rect: System.Drawing.Rectangle structure that specifies the location and size of the drawn image.
        DrawImage(self: Graphics, image: Image, x: int, y: int, width: int, height: int)
            Draws the specified System.Drawing.Image at the specified location and with the specified size.
        
            image: System.Drawing.Image to draw.
            x: The x-coordinate of the upper-left corner of the drawn image.
            y: The y-coordinate of the upper-left corner of the drawn image.
            width: Width of the drawn image.
            height: Height of the drawn image.
        DrawImage(self: Graphics, image: Image, x: Single, y: Single)
            Draws the specified System.Drawing.Image, using its original physical size, at the specified 
             location.
        
        
            image: System.Drawing.Image to draw.
            x: The x-coordinate of the upper-left corner of the drawn image.
            y: The y-coordinate of the upper-left corner of the drawn image.
        DrawImage(self: Graphics, image: Image, destPoints: Array[Point])
            Draws the specified System.Drawing.Image at the specified location and with the specified shape 
             and size.
        
        
            image: System.Drawing.Image to draw.
            destPoints: Array of three System.Drawing.Point structures that define a parallelogram.
        DrawImage(self: Graphics, image: Image, x: Single, y: Single, srcRect: RectangleF, srcUnit: GraphicsUnit)
            Draws a portion of an image at a specified location.
        
            image: System.Drawing.Image to draw.
            x: The x-coordinate of the upper-left corner of the drawn image.
            y: The y-coordinate of the upper-left corner of the drawn image.
            srcRect: System.Drawing.RectangleF structure that specifies the portion of the System.Drawing.Image to 
             draw.
        
            srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 
             by the srcRect parameter.
        
        DrawImage(self: Graphics, image: Image, x: int, y: int, srcRect: Rectangle, srcUnit: GraphicsUnit)
            Draws a portion of an image at a specified location.
        
            image: System.Drawing.Image to draw.
            x: The x-coordinate of the upper-left corner of the drawn image.
            y: The y-coordinate of the upper-left corner of the drawn image.
            srcRect: System.Drawing.Rectangle structure that specifies the portion of the image object to draw.
            srcUnit: Member of the System.Drawing.GraphicsUnit enumeration that specifies the units of measure used 
             by the srcRect parameter.
        
        DrawImage(self: Graphics, image: Image, destPoints: Array[PointF])
            Draws the specified System.Drawing.Image at the specified location and with the specified shape 
             and size.
        
        
            image: System.Drawing.Image to draw.
            destPoints: Array of three System.Drawing.PointF structures that define a parallelogram.
        DrawImage(self: Graphics, image: Image, rect: RectangleF)
            Draws the specified System.Drawing.Image at the specified location and with the specified size.
        
            image: System.Drawing.Image to draw.
            rect: System.Drawing.RectangleF structure that specifies the location and size of the drawn image.
        DrawImage(self: Graphics, image: Image, x: Single, y: Single, width: Single, height: Single)
            Draws the specified System.Drawing.Image at the specified location and with the specified size.
        
            image: System.Drawing.Image to draw.
            x: The x-coordinate of the upper-left corner of the drawn image.
            y: The y-coordinate of the upper-left corner of the drawn image.
            width: Width of the drawn image.
            height: Height of the drawn image.
        DrawImage(self: Graphics, image: Image, point: Point)
            Draws the specified System.Drawing.Image, using its original physical size, at the specified 
             location.
        
        
            image: System.Drawing.Image to draw.
            point: System.Drawing.Point structure that represents the location of the upper-left corner of the 
             drawn image.
        """
        pass

    def DrawImageUnscaled(self, image, *__args):
        """
        DrawImageUnscaled(self: Graphics, image: Image, rect: Rectangle)
            Draws a specified image using its original physical size at a specified location.
        
            image: System.Drawing.Image to draw.
            rect: System.Drawing.Rectangle that specifies the upper-left corner of the drawn image. The X and Y 
             properties of the rectangle specify the upper-left corner. The Width and Height properties are 
             ignored.
        
        DrawImageUnscaled(self: Graphics, image: Image, x: int, y: int, width: int, height: int)
            Draws a specified image using its original physical size at a specified location.
        
            image: System.Drawing.Image to draw.
            x: The x-coordinate of the upper-left corner of the drawn image.
            y: The y-coordinate of the upper-left corner of the drawn image.
            width: Not used.
            height: Not used.
        DrawImageUnscaled(self: Graphics, image: Image, point: Point)
            Draws a specified image using its original physical size at a specified location.
        
            image: System.Drawing.Image to draw.
            point: System.Drawing.Point structure that specifies the upper-left corner of the drawn image.
        DrawImageUnscaled(self: Graphics, image: Image, x: int, y: int)
            Draws the specified image using its original physical size at the location specified by a 
             coordinate pair.
        
        
            image: System.Drawing.Image to draw.
            x: The x-coordinate of the upper-left corner of the drawn image.
            y: The y-coordinate of the upper-left corner of the drawn image.
        """
        pass

    def DrawImageUnscaledAndClipped(self, image, rect):
        """
        DrawImageUnscaledAndClipped(self: Graphics, image: Image, rect: Rectangle)
            Draws the specified image without scaling and clips it, if necessary, to fit in the specified 
             rectangle.
        
        
            image: The System.Drawing.Image to draw.
            rect: The System.Drawing.Rectangle in which to draw the image.
        """
        pass

    def DrawLine(self, pen, *__args):
        """
        DrawLine(self: Graphics, pen: Pen, pt1: PointF, pt2: PointF)
            Draws a line connecting two System.Drawing.PointF structures.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the line.
            pt1: System.Drawing.PointF structure that represents the first point to connect.
            pt2: System.Drawing.PointF structure that represents the second point to connect.
        DrawLine(self: Graphics, pen: Pen, pt1: Point, pt2: Point)
            Draws a line connecting two System.Drawing.Point structures.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the line.
            pt1: System.Drawing.Point structure that represents the first point to connect.
            pt2: System.Drawing.Point structure that represents the second point to connect.
        DrawLine(self: Graphics, pen: Pen, x1: int, y1: int, x2: int, y2: int)
            Draws a line connecting the two points specified by the coordinate pairs.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the line.
            x1: The x-coordinate of the first point.
            y1: The y-coordinate of the first point.
            x2: The x-coordinate of the second point.
            y2: The y-coordinate of the second point.
        DrawLine(self: Graphics, pen: Pen, x1: Single, y1: Single, x2: Single, y2: Single)
            Draws a line connecting the two points specified by the coordinate pairs.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the line.
            x1: The x-coordinate of the first point.
            y1: The y-coordinate of the first point.
            x2: The x-coordinate of the second point.
            y2: The y-coordinate of the second point.
        """
        pass

    def DrawLines(self, pen, points):
        """
        DrawLines(self: Graphics, pen: Pen, points: Array[Point])
            Draws a series of line segments that connect an array of System.Drawing.Point structures.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the line segments.
            points: Array of System.Drawing.Point structures that represent the points to connect.
        DrawLines(self: Graphics, pen: Pen, points: Array[PointF])
            Draws a series of line segments that connect an array of System.Drawing.PointF structures.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the line segments.
            points: Array of System.Drawing.PointF structures that represent the points to connect.
        """
        pass

    def DrawPath(self, pen, path):
        """
        DrawPath(self: Graphics, pen: Pen, path: GraphicsPath)
            Draws a System.Drawing.Drawing2D.GraphicsPath.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the path.
            path: System.Drawing.Drawing2D.GraphicsPath to draw.
        """
        pass

    def DrawPie(self, pen, *__args):
        """
        DrawPie(self: Graphics, pen: Pen, rect: Rectangle, startAngle: Single, sweepAngle: Single)
            Draws a pie shape defined by an ellipse specified by a System.Drawing.Rectangle structure and 
             two radial lines.
        
        
            pen: System.Drawing.Pen that determines the color, width, and style of the pie shape.
            rect: System.Drawing.Rectangle structure that represents the bounding rectangle that defines the 
             ellipse from which the pie shape comes.
        
            startAngle: Angle measured in degrees clockwise from the x-axis to the first side of the pie shape.
            sweepAngle: Angle measured in degrees clockwise from the startAngle parameter to the second side of the pie 
             shape.
        
        DrawPie(self: Graphics, pen: Pen, x: int, y: int, width: int, height: int, startAngle: int, sweepAngle: int)
            Draws a pie shape defined by an ellipse specified by a coordinate pair, a width, a height, and 
             two radial lines.
        
        
            pen: System.Drawing.Pen that determines the color, width, and style of the pie shape.
            x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 
             from which the pie shape comes.
        
            y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 
             from which the pie shape comes.
        
            width: Width of the bounding rectangle that defines the ellipse from which the pie shape comes.
            height: Height of the bounding rectangle that defines the ellipse from which the pie shape comes.
            startAngle: Angle measured in degrees clockwise from the x-axis to the first side of the pie shape.
            sweepAngle: Angle measured in degrees clockwise from the startAngle parameter to the second side of the pie 
             shape.
        
        DrawPie(self: Graphics, pen: Pen, rect: RectangleF, startAngle: Single, sweepAngle: Single)
            Draws a pie shape defined by an ellipse specified by a System.Drawing.RectangleF structure and 
             two radial lines.
        
        
            pen: System.Drawing.Pen that determines the color, width, and style of the pie shape.
            rect: System.Drawing.RectangleF structure that represents the bounding rectangle that defines the 
             ellipse from which the pie shape comes.
        
            startAngle: Angle measured in degrees clockwise from the x-axis to the first side of the pie shape.
            sweepAngle: Angle measured in degrees clockwise from the startAngle parameter to the second side of the pie 
             shape.
        
        DrawPie(self: Graphics, pen: Pen, x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single)
            Draws a pie shape defined by an ellipse specified by a coordinate pair, a width, a height, and 
             two radial lines.
        
        
            pen: System.Drawing.Pen that determines the color, width, and style of the pie shape.
            x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 
             from which the pie shape comes.
        
            y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 
             from which the pie shape comes.
        
            width: Width of the bounding rectangle that defines the ellipse from which the pie shape comes.
            height: Height of the bounding rectangle that defines the ellipse from which the pie shape comes.
            startAngle: Angle measured in degrees clockwise from the x-axis to the first side of the pie shape.
            sweepAngle: Angle measured in degrees clockwise from the startAngle parameter to the second side of the pie 
             shape.
        """
        pass

    def DrawPolygon(self, pen, points):
        """
        DrawPolygon(self: Graphics, pen: Pen, points: Array[Point])
            Draws a polygon defined by an array of System.Drawing.Point structures.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the polygon.
            points: Array of System.Drawing.Point structures that represent the vertices of the polygon.
        DrawPolygon(self: Graphics, pen: Pen, points: Array[PointF])
            Draws a polygon defined by an array of System.Drawing.PointF structures.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the polygon.
            points: Array of System.Drawing.PointF structures that represent the vertices of the polygon.
        """
        pass

    def DrawRectangle(self, pen, *__args):
        """
        DrawRectangle(self: Graphics, pen: Pen, x: int, y: int, width: int, height: int)
            Draws a rectangle specified by a coordinate pair, a width, and a height.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the rectangle.
            x: The x-coordinate of the upper-left corner of the rectangle to draw.
            y: The y-coordinate of the upper-left corner of the rectangle to draw.
            width: Width of the rectangle to draw.
            height: Height of the rectangle to draw.
        DrawRectangle(self: Graphics, pen: Pen, x: Single, y: Single, width: Single, height: Single)
            Draws a rectangle specified by a coordinate pair, a width, and a height.
        
            pen: A System.Drawing.Pen that determines the color, width, and style of the rectangle.
            x: The x-coordinate of the upper-left corner of the rectangle to draw.
            y: The y-coordinate of the upper-left corner of the rectangle to draw.
            width: The width of the rectangle to draw.
            height: The height of the rectangle to draw.
        DrawRectangle(self: Graphics, pen: Pen, rect: Rectangle)
            Draws a rectangle specified by a System.Drawing.Rectangle structure.
        
            pen: A System.Drawing.Pen that determines the color, width, and style of the rectangle.
            rect: A System.Drawing.Rectangle structure that represents the rectangle to draw.
        """
        pass

    def DrawRectangles(self, pen, rects):
        """
        DrawRectangles(self: Graphics, pen: Pen, rects: Array[Rectangle])
            Draws a series of rectangles specified by System.Drawing.Rectangle structures.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the outlines of the rectangles.
            rects: Array of System.Drawing.Rectangle structures that represent the rectangles to draw.
        DrawRectangles(self: Graphics, pen: Pen, rects: Array[RectangleF])
            Draws a series of rectangles specified by System.Drawing.RectangleF structures.
        
            pen: System.Drawing.Pen that determines the color, width, and style of the outlines of the rectangles.
            rects: Array of System.Drawing.RectangleF structures that represent the rectangles to draw.
        """
        pass

    def DrawString(self, s, font, brush, *__args):
        """
        DrawString(self: Graphics, s: str, font: Font, brush: Brush, point: PointF)
            Draws the specified text string at the specified location with the specified 
             System.Drawing.Brush and System.Drawing.Font objects.
        
        
            s: String to draw.
            font: System.Drawing.Font that defines the text format of the string.
            brush: System.Drawing.Brush that determines the color and texture of the drawn text.
            point: System.Drawing.PointF structure that specifies the upper-left corner of the drawn text.
        DrawString(self: Graphics, s: str, font: Font, brush: Brush, x: Single, y: Single, format: StringFormat)
            Draws the specified text string at the specified location with the specified 
             System.Drawing.Brush and System.Drawing.Font objects using the formatting attributes of the 
             specified System.Drawing.StringFormat.
        
        
            s: String to draw.
            font: System.Drawing.Font that defines the text format of the string.
            brush: System.Drawing.Brush that determines the color and texture of the drawn text.
            x: The x-coordinate of the upper-left corner of the drawn text.
            y: The y-coordinate of the upper-left corner of the drawn text.
            format: System.Drawing.StringFormat that specifies formatting attributes, such as line spacing and 
             alignment, that are applied to the drawn text.
        
        DrawString(self: Graphics, s: str, font: Font, brush: Brush, point: PointF, format: StringFormat)
            Draws the specified text string at the specified location with the specified 
             System.Drawing.Brush and System.Drawing.Font objects using the formatting attributes of the 
             specified System.Drawing.StringFormat.
        
        
            s: String to draw.
            font: System.Drawing.Font that defines the text format of the string.
            brush: System.Drawing.Brush that determines the color and texture of the drawn text.
            point: System.Drawing.PointF structure that specifies the upper-left corner of the drawn text.
            format: System.Drawing.StringFormat that specifies formatting attributes, such as line spacing and 
             alignment, that are applied to the drawn text.
        
        DrawString(self: Graphics, s: str, font: Font, brush: Brush, x: Single, y: Single)
            Draws the specified text string at the specified location with the specified 
             System.Drawing.Brush and System.Drawing.Font objects.
        
        
            s: String to draw.
            font: System.Drawing.Font that defines the text format of the string.
            brush: System.Drawing.Brush that determines the color and texture of the drawn text.
            x: The x-coordinate of the upper-left corner of the drawn text.
            y: The y-coordinate of the upper-left corner of the drawn text.
        DrawString(self: Graphics, s: str, font: Font, brush: Brush, layoutRectangle: RectangleF)
            Draws the specified text string in the specified rectangle with the specified 
             System.Drawing.Brush and System.Drawing.Font objects.
        
        
            s: String to draw.
            font: System.Drawing.Font that defines the text format of the string.
            brush: System.Drawing.Brush that determines the color and texture of the drawn text.
            layoutRectangle: System.Drawing.RectangleF structure that specifies the location of the drawn text.
        DrawString(self: Graphics, s: str, font: Font, brush: Brush, layoutRectangle: RectangleF, format: StringFormat)
            Draws the specified text string in the specified rectangle with the specified 
             System.Drawing.Brush and System.Drawing.Font objects using the formatting attributes of the 
             specified System.Drawing.StringFormat.
        
        
            s: String to draw.
            font: System.Drawing.Font that defines the text format of the string.
            brush: System.Drawing.Brush that determines the color and texture of the drawn text.
            layoutRectangle: System.Drawing.RectangleF structure that specifies the location of the drawn text.
            format: System.Drawing.StringFormat that specifies formatting attributes, such as line spacing and 
             alignment, that are applied to the drawn text.
        """
        pass

    def EndContainer(self, container):
        """
        EndContainer(self: Graphics, container: GraphicsContainer)
            Closes the current graphics container and restores the state of this System.Drawing.Graphics to 
             the state saved by a call to the System.Drawing.Graphics.BeginContainer method.
        
        
            container: System.Drawing.Drawing2D.GraphicsContainer that represents the container this method restores.
        """
        pass

    def EnumerateMetafile(self, metafile, *__args):
        """ EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: RectangleF, srcRect: RectangleF, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: Point, srcRect: Rectangle, unit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: RectangleF, srcRect: RectangleF, unit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: RectangleF, srcRect: RectangleF, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: Point, srcRect: Rectangle, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: PointF, srcRect: RectangleF, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: PointF, srcRect: RectangleF, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: Point, srcRect: Rectangle, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: PointF, srcRect: RectangleF, unit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[Point], srcRect: Rectangle, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[PointF], srcRect: RectangleF, unit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[Point], srcRect: Rectangle, unit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[Point], srcRect: Rectangle, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[PointF], srcRect: RectangleF, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: Rectangle, srcRect: Rectangle, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: Rectangle, srcRect: Rectangle, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[PointF], srcRect: RectangleF, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: Rectangle, srcRect: Rectangle, unit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: RectangleF, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: Point, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: RectangleF, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: RectangleF, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: Point, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: PointF, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: PointF, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: Point, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: PointF, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[Point], callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[PointF], callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[Point], callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[Point], callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[PointF], callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: Rectangle, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: Rectangle, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[PointF], callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: Rectangle, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes) """
        pass

    def ExcludeClip(self, *__args):
        """
        ExcludeClip(self: Graphics, rect: Rectangle)
            Updates the clip region of this System.Drawing.Graphics to exclude the area specified by a 
             System.Drawing.Rectangle structure.
        
        
            rect: System.Drawing.Rectangle structure that specifies the rectangle to exclude from the clip region.
        ExcludeClip(self: Graphics, region: Region)
            Updates the clip region of this System.Drawing.Graphics to exclude the area specified by a 
             System.Drawing.Region.
        
        
            region: System.Drawing.Region that specifies the region to exclude from the clip region.
        """
        pass

    def FillClosedCurve(self, brush, points, fillmode=None, tension=None):
        """
        FillClosedCurve(self: Graphics, brush: Brush, points: Array[Point])
            Fills the interior of a closed cardinal spline curve defined by an array of System.Drawing.Point 
             structures.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            points: Array of System.Drawing.Point structures that define the spline.
        FillClosedCurve(self: Graphics, brush: Brush, points: Array[Point], fillmode: FillMode)
            Fills the interior of a closed cardinal spline curve defined by an array of System.Drawing.Point 
             structures using the specified fill mode.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            points: Array of System.Drawing.Point structures that define the spline.
            fillmode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines how the curve is 
             filled.
        
        FillClosedCurve(self: Graphics, brush: Brush, points: Array[Point], fillmode: FillMode, tension: Single)
            Fills the interior of a closed cardinal spline curve defined by an array of System.Drawing.Point 
             structures using the specified fill mode and tension.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            points: Array of System.Drawing.Point structures that define the spline.
            fillmode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines how the curve is 
             filled.
        
            tension: Value greater than or equal to 0.0F that specifies the tension of the curve.
        FillClosedCurve(self: Graphics, brush: Brush, points: Array[PointF])
            Fills the interior of a closed cardinal spline curve defined by an array of 
             System.Drawing.PointF structures.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            points: Array of System.Drawing.PointF structures that define the spline.
        FillClosedCurve(self: Graphics, brush: Brush, points: Array[PointF], fillmode: FillMode)
            Fills the interior of a closed cardinal spline curve defined by an array of 
             System.Drawing.PointF structures using the specified fill mode.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            points: Array of System.Drawing.PointF structures that define the spline.
            fillmode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines how the curve is 
             filled.
        
        FillClosedCurve(self: Graphics, brush: Brush, points: Array[PointF], fillmode: FillMode, tension: Single)
            Fills the interior of a closed cardinal spline curve defined by an array of 
             System.Drawing.PointF structures using the specified fill mode and tension.
        
        
            brush: A System.Drawing.Brush that determines the characteristics of the fill.
            points: Array of System.Drawing.PointF structures that define the spline.
            fillmode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines how the curve is 
             filled.
        
            tension: Value greater than or equal to 0.0F that specifies the tension of the curve.
        """
        pass

    def FillEllipse(self, brush, *__args):
        """
        FillEllipse(self: Graphics, brush: Brush, rect: Rectangle)
            Fills the interior of an ellipse defined by a bounding rectangle specified by a 
             System.Drawing.Rectangle structure.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            rect: System.Drawing.Rectangle structure that represents the bounding rectangle that defines the 
             ellipse.
        
        FillEllipse(self: Graphics, brush: Brush, x: int, y: int, width: int, height: int)
            Fills the interior of an ellipse defined by a bounding rectangle specified by a pair of 
             coordinates, a width, and a height.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.
            y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.
            width: Width of the bounding rectangle that defines the ellipse.
            height: Height of the bounding rectangle that defines the ellipse.
        FillEllipse(self: Graphics, brush: Brush, x: Single, y: Single, width: Single, height: Single)
            Fills the interior of an ellipse defined by a bounding rectangle specified by a pair of 
             coordinates, a width, and a height.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.
            y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.
            width: Width of the bounding rectangle that defines the ellipse.
            height: Height of the bounding rectangle that defines the ellipse.
        FillEllipse(self: Graphics, brush: Brush, rect: RectangleF)
            Fills the interior of an ellipse defined by a bounding rectangle specified by a 
             System.Drawing.RectangleF structure.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            rect: System.Drawing.RectangleF structure that represents the bounding rectangle that defines the 
             ellipse.
        """
        pass

    def FillPath(self, brush, path):
        """
        FillPath(self: Graphics, brush: Brush, path: GraphicsPath)
            Fills the interior of a System.Drawing.Drawing2D.GraphicsPath.
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            path: System.Drawing.Drawing2D.GraphicsPath that represents the path to fill.
        """
        pass

    def FillPie(self, brush, *__args):
        """
        FillPie(self: Graphics, brush: Brush, x: int, y: int, width: int, height: int, startAngle: int, sweepAngle: int)
            Fills the interior of a pie section defined by an ellipse specified by a pair of coordinates, a 
             width, a height, and two radial lines.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 
             from which the pie section comes.
        
            y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 
             from which the pie section comes.
        
            width: Width of the bounding rectangle that defines the ellipse from which the pie section comes.
            height: Height of the bounding rectangle that defines the ellipse from which the pie section comes.
            startAngle: Angle in degrees measured clockwise from the x-axis to the first side of the pie section.
            sweepAngle: Angle in degrees measured clockwise from the startAngle parameter to the second side of the pie 
             section.
        
        FillPie(self: Graphics, brush: Brush, x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single)
            Fills the interior of a pie section defined by an ellipse specified by a pair of coordinates, a 
             width, a height, and two radial lines.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 
             from which the pie section comes.
        
            y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse 
             from which the pie section comes.
        
            width: Width of the bounding rectangle that defines the ellipse from which the pie section comes.
            height: Height of the bounding rectangle that defines the ellipse from which the pie section comes.
            startAngle: Angle in degrees measured clockwise from the x-axis to the first side of the pie section.
            sweepAngle: Angle in degrees measured clockwise from the startAngle parameter to the second side of the pie 
             section.
        
        FillPie(self: Graphics, brush: Brush, rect: Rectangle, startAngle: Single, sweepAngle: Single)
            Fills the interior of a pie section defined by an ellipse specified by a 
             System.Drawing.RectangleF structure and two radial lines.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            rect: System.Drawing.Rectangle structure that represents the bounding rectangle that defines the 
             ellipse from which the pie section comes.
        
            startAngle: Angle in degrees measured clockwise from the x-axis to the first side of the pie section.
            sweepAngle: Angle in degrees measured clockwise from the startAngle parameter to the second side of the pie 
             section.
        """
        pass

    def FillPolygon(self, brush, points, fillMode=None):
        """
        FillPolygon(self: Graphics, brush: Brush, points: Array[PointF], fillMode: FillMode)
            Fills the interior of a polygon defined by an array of points specified by System.Drawing.PointF 
             structures using the specified fill mode.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            points: Array of System.Drawing.PointF structures that represent the vertices of the polygon to fill.
            fillMode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines the style of the 
             fill.
        
        FillPolygon(self: Graphics, brush: Brush, points: Array[Point], fillMode: FillMode)
            Fills the interior of a polygon defined by an array of points specified by System.Drawing.Point 
             structures using the specified fill mode.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            points: Array of System.Drawing.Point structures that represent the vertices of the polygon to fill.
            fillMode: Member of the System.Drawing.Drawing2D.FillMode enumeration that determines the style of the 
             fill.
        
        FillPolygon(self: Graphics, brush: Brush, points: Array[Point])
            Fills the interior of a polygon defined by an array of points specified by System.Drawing.Point 
             structures.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            points: Array of System.Drawing.Point structures that represent the vertices of the polygon to fill.
        FillPolygon(self: Graphics, brush: Brush, points: Array[PointF])
            Fills the interior of a polygon defined by an array of points specified by System.Drawing.PointF 
             structures.
        
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            points: Array of System.Drawing.PointF structures that represent the vertices of the polygon to fill.
        """
        pass

    def FillRectangle(self, brush, *__args):
        """
        FillRectangle(self: Graphics, brush: Brush, x: int, y: int, width: int, height: int)
            Fills the interior of a rectangle specified by a pair of coordinates, a width, and a height.
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            x: The x-coordinate of the upper-left corner of the rectangle to fill.
            y: The y-coordinate of the upper-left corner of the rectangle to fill.
            width: Width of the rectangle to fill.
            height: Height of the rectangle to fill.
        FillRectangle(self: Graphics, brush: Brush, rect: RectangleF)
            Fills the interior of a rectangle specified by a System.Drawing.RectangleF structure.
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            rect: System.Drawing.RectangleF structure that represents the rectangle to fill.
        FillRectangle(self: Graphics, brush: Brush, x: Single, y: Single, width: Single, height: Single)
            Fills the interior of a rectangle specified by a pair of coordinates, a width, and a height.
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            x: The x-coordinate of the upper-left corner of the rectangle to fill.
            y: The y-coordinate of the upper-left corner of the rectangle to fill.
            width: Width of the rectangle to fill.
            height: Height of the rectangle to fill.
        FillRectangle(self: Graphics, brush: Brush, rect: Rectangle)
            Fills the interior of a rectangle specified by a System.Drawing.Rectangle structure.
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            rect: System.Drawing.Rectangle structure that represents the rectangle to fill.
        """
        pass

    def FillRectangles(self, brush, rects):
        """
        FillRectangles(self: Graphics, brush: Brush, rects: Array[RectangleF])
            Fills the interiors of a series of rectangles specified by System.Drawing.RectangleF structures.
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            rects: Array of System.Drawing.RectangleF structures that represent the rectangles to fill.
        FillRectangles(self: Graphics, brush: Brush, rects: Array[Rectangle])
            Fills the interiors of a series of rectangles specified by System.Drawing.Rectangle structures.
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            rects: Array of System.Drawing.Rectangle structures that represent the rectangles to fill.
        """
        pass

    def FillRegion(self, brush, region):
        """
        FillRegion(self: Graphics, brush: Brush, region: Region)
            Fills the interior of a System.Drawing.Region.
        
            brush: System.Drawing.Brush that determines the characteristics of the fill.
            region: System.Drawing.Region that represents the area to fill.
        """
        pass

    def Flush(self, intention=None):
        """
        Flush(self: Graphics, intention: FlushIntention)
            Forces execution of all pending graphics operations with the method waiting or not waiting, as 
             specified, to return before the operations finish.
        
        
            intention: Member of the System.Drawing.Drawing2D.FlushIntention enumeration that specifies whether the 
             method returns immediately or waits for any existing operations to finish.
        
        Flush(self: Graphics)
            Forces execution of all pending graphics operations and returns immediately without waiting for 
             the operations to finish.
        """
        pass

    @staticmethod
    def FromHdc(hdc, hdevice=None):
        """
        FromHdc(hdc: IntPtr, hdevice: IntPtr) -> Graphics
        
            Creates a new System.Drawing.Graphics from the specified handle to a device context and handle 
             to a device.
        
        
            hdc: Handle to a device context.
            hdevice: Handle to a device.
            Returns: This method returns a new System.Drawing.Graphics for the specified device context and device.
        FromHdc(hdc: IntPtr) -> Graphics
        
            Creates a new System.Drawing.Graphics from the specified handle to a device context.
        
            hdc: Handle to a device context.
            Returns: This method returns a new System.Drawing.Graphics for the specified device context.
        """
        pass

    @staticmethod
    def FromHdcInternal(hdc):
        """
        FromHdcInternal(hdc: IntPtr) -> Graphics
        
            Returns a System.Drawing.Graphics for the specified device context.
        
            hdc: Handle to a device context.
            Returns: A System.Drawing.Graphics for the specified device context.
        """
        pass

    @staticmethod
    def FromHwnd(hwnd):
        """
        FromHwnd(hwnd: IntPtr) -> Graphics
        
            Creates a new System.Drawing.Graphics from the specified handle to a window.
        
            hwnd: Handle to a window.
            Returns: This method returns a new System.Drawing.Graphics for the specified window handle.
        """
        pass

    @staticmethod
    def FromHwndInternal(hwnd):
        """
        FromHwndInternal(hwnd: IntPtr) -> Graphics
        
            Creates a new System.Drawing.Graphics for the specified windows handle.
        
            hwnd: Handle to a window.
            Returns: A System.Drawing.Graphics for the specified window handle.
        """
        pass

    @staticmethod
    def FromImage(image):
        """
        FromImage(image: Image) -> Graphics
        
            Creates a new System.Drawing.Graphics from the specified System.Drawing.Image.
        
            image: System.Drawing.Image from which to create the new System.Drawing.Graphics.
            Returns: This method returns a new System.Drawing.Graphics for the specified System.Drawing.Image.
        """
        pass

    def GetContextInfo(self):
        """
        GetContextInfo(self: Graphics) -> object
        
            Gets the cumulative graphics context.
            Returns: An System.Object representing the cumulative graphics context.
        """
        pass

    @staticmethod
    def GetHalftonePalette():
        """
        GetHalftonePalette() -> IntPtr
        
            Gets a handle to the current Windows halftone palette.
            Returns: Internal pointer that specifies the handle to the palette.
        """
        pass

    def GetHdc(self):
        """
        GetHdc(self: Graphics) -> IntPtr
        
            Gets the handle to the device context associated with this System.Drawing.Graphics.
            Returns: Handle to the device context associated with this System.Drawing.Graphics.
        """
        pass

    def GetNearestColor(self, color):
        """
        GetNearestColor(self: Graphics, color: Color) -> Color
        
            Gets the nearest color to the specified System.Drawing.Color structure.
        
            color: System.Drawing.Color structure for which to find a match.
            Returns: A System.Drawing.Color structure that represents the nearest color to the one specified with the 
             color parameter.
        """
        pass

    def IntersectClip(self, *__args):
        """
        IntersectClip(self: Graphics, region: Region)
            Updates the clip region of this System.Drawing.Graphics to the intersection of the current clip 
             region and the specified System.Drawing.Region.
        
        
            region: System.Drawing.Region to intersect with the current region.
        IntersectClip(self: Graphics, rect: RectangleF)
            Updates the clip region of this System.Drawing.Graphics to the intersection of the current clip 
             region and the specified System.Drawing.RectangleF structure.
        
        
            rect: System.Drawing.RectangleF structure to intersect with the current clip region.
        IntersectClip(self: Graphics, rect: Rectangle)
            Updates the clip region of this System.Drawing.Graphics to the intersection of the current clip 
             region and the specified System.Drawing.Rectangle structure.
        
        
            rect: System.Drawing.Rectangle structure to intersect with the current clip region.
        """
        pass

    def IsVisible(self, *__args):
        """
        IsVisible(self: Graphics, x: int, y: int, width: int, height: int) -> bool
        
            Indicates whether the rectangle specified by a pair of coordinates, a width, and a height is 
             contained within the visible clip region of this System.Drawing.Graphics.
        
        
            x: The x-coordinate of the upper-left corner of the rectangle to test for visibility.
            y: The y-coordinate of the upper-left corner of the rectangle to test for visibility.
            width: Width of the rectangle to test for visibility.
            height: Height of the rectangle to test for visibility.
            Returns: true if the rectangle defined by the x, y, width, and height parameters is contained within the 
             visible clip region of this System.Drawing.Graphics; otherwise, false.
        
        IsVisible(self: Graphics, point: PointF) -> bool
        
            Indicates whether the specified System.Drawing.PointF structure is contained within the visible 
             clip region of this System.Drawing.Graphics.
        
        
            point: System.Drawing.PointF structure to test for visibility.
            Returns: true if the point specified by the point parameter is contained within the visible clip region 
             of this System.Drawing.Graphics; otherwise, false.
        
        IsVisible(self: Graphics, rect: RectangleF) -> bool
        
            Indicates whether the rectangle specified by a System.Drawing.RectangleF structure is contained 
             within the visible clip region of this System.Drawing.Graphics.
        
        
            rect: System.Drawing.RectangleF structure to test for visibility.
            Returns: true if the rectangle specified by the rect parameter is contained within the visible clip 
             region of this System.Drawing.Graphics; otherwise, false.
        
        IsVisible(self: Graphics, x: Single, y: Single, width: Single, height: Single) -> bool
        
            Indicates whether the rectangle specified by a pair of coordinates, a width, and a height is 
             contained within the visible clip region of this System.Drawing.Graphics.
        
        
            x: The x-coordinate of the upper-left corner of the rectangle to test for visibility.
            y: The y-coordinate of the upper-left corner of the rectangle to test for visibility.
            width: Width of the rectangle to test for visibility.
            height: Height of the rectangle to test for visibility.
            Returns: true if the rectangle defined by the x, y, width, and height parameters is contained within the 
             visible clip region of this System.Drawing.Graphics; otherwise, false.
        
        IsVisible(self: Graphics, x: int, y: int) -> bool
        
            Indicates whether the point specified by a pair of coordinates is contained within the visible 
             clip region of this System.Drawing.Graphics.
        
        
            x: The x-coordinate of the point to test for visibility.
            y: The y-coordinate of the point to test for visibility.
            Returns: true if the point defined by the x and y parameters is contained within the visible clip region 
             of this System.Drawing.Graphics; otherwise, false.
        
        IsVisible(self: Graphics, rect: Rectangle) -> bool
        
            Indicates whether the rectangle specified by a System.Drawing.Rectangle structure is contained 
             within the visible clip region of this System.Drawing.Graphics.
        
        
            rect: System.Drawing.Rectangle structure to test for visibility.
            Returns: true if the rectangle specified by the rect parameter is contained within the visible clip 
             region of this System.Drawing.Graphics; otherwise, false.
        
        IsVisible(self: Graphics, x: Single, y: Single) -> bool
        
            Indicates whether the point specified by a pair of coordinates is contained within the visible 
             clip region of this System.Drawing.Graphics.
        
        
            x: The x-coordinate of the point to test for visibility.
            y: The y-coordinate of the point to test for visibility.
            Returns: true if the point defined by the x and y parameters is contained within the visible clip region 
             of this System.Drawing.Graphics; otherwise, false.
        
        IsVisible(self: Graphics, point: Point) -> bool
        
            Indicates whether the specified System.Drawing.Point structure is contained within the visible 
             clip region of this System.Drawing.Graphics.
        
        
            point: System.Drawing.Point structure to test for visibility.
            Returns: true if the point specified by the point parameter is contained within the visible clip region 
             of this System.Drawing.Graphics; otherwise, false.
        """
        pass

    def MeasureCharacterRanges(self, text, font, layoutRect, stringFormat):
        """
        MeasureCharacterRanges(self: Graphics, text: str, font: Font, layoutRect: RectangleF, stringFormat: StringFormat) -> Array[Region]
        
            Gets an array of System.Drawing.Region objects, each of which bounds a range of character 
             positions within the specified string.
        
        
            text: String to measure.
            font: System.Drawing.Font that defines the text format of the string.
            layoutRect: System.Drawing.RectangleF structure that specifies the layout rectangle for the string.
            stringFormat: System.Drawing.StringFormat that represents formatting information, such as line spacing, for 
             the string.
        
            Returns: This method returns an array of System.Drawing.Region objects, each of which bounds a range of 
             character positions within the specified string.
        """
        pass

    def MeasureString(self, text, font, *__args):
        """
        MeasureString(self: Graphics, text: str, font: Font, origin: PointF, stringFormat: StringFormat) -> SizeF
        
            Measures the specified string when drawn with the specified System.Drawing.Font and formatted 
             with the specified System.Drawing.StringFormat.
        
        
            text: String to measure.
            font: System.Drawing.Font defines the text format of the string.
            origin: System.Drawing.PointF structure that represents the upper-left corner of the string.
            stringFormat: System.Drawing.StringFormat that represents formatting information, such as line spacing, for 
             the string.
        
            Returns: This method returns a System.Drawing.SizeF structure that represents the size, in the units 
             specified by the System.Drawing.Graphics.PageUnit property, of the string specified by the text 
             parameter as drawn with the font parameter and the stringFormat parameter.
        
        MeasureString(self: Graphics, text: str, font: Font, layoutArea: SizeF) -> SizeF
        
            Measures the specified string when drawn with the specified System.Drawing.Font within the 
             specified layout area.
        
        
            text: String to measure.
            font: System.Drawing.Font defines the text format of the string.
            layoutArea: System.Drawing.SizeF structure that specifies the maximum layout area for the text.
            Returns: This method returns a System.Drawing.SizeF structure that represents the size, in the units 
             specified by the System.Drawing.Graphics.PageUnit property, of the string specified by the text 
             parameter as drawn with the font parameter.
        
        MeasureString(self: Graphics, text: str, font: Font, width: int) -> SizeF
        
            Measures the specified string when drawn with the specified System.Drawing.Font.
        
            text: String to measure.
            font: System.Drawing.Font that defines the format of the string.
            width: Maximum width of the string in pixels.
            Returns: This method returns a System.Drawing.SizeF structure that represents the size, in the units 
             specified by the System.Drawing.Graphics.PageUnit property, of the string specified in the text 
             parameter as drawn with the font parameter.
        
        MeasureString(self: Graphics, text: str, font: Font, layoutArea: SizeF, stringFormat: StringFormat) -> (SizeF, int, int)
        
            Measures the specified string when drawn with the specified System.Drawing.Font and formatted 
             with the specified System.Drawing.StringFormat.
        
        
            text: String to measure.
            font: System.Drawing.Font that defines the text format of the string.
            layoutArea: System.Drawing.SizeF structure that specifies the maximum layout area for the text.
            stringFormat: System.Drawing.StringFormat that represents formatting information, such as line spacing, for 
             the string.
        
            Returns: This method returns a System.Drawing.SizeF structure that represents the size of the string, in 
             the units specified by the System.Drawing.Graphics.PageUnit property, of the text parameter as 
             drawn with the font parameter and the stringFormat parameter.
        
        MeasureString(self: Graphics, text: str, font: Font, layoutArea: SizeF, stringFormat: StringFormat) -> SizeF
        
            Measures the specified string when drawn with the specified System.Drawing.Font and formatted 
             with the specified System.Drawing.StringFormat.
        
        
            text: String to measure.
            font: System.Drawing.Font defines the text format of the string.
            layoutArea: System.Drawing.SizeF structure that specifies the maximum layout area for the text.
            stringFormat: System.Drawing.StringFormat that represents formatting information, such as line spacing, for 
             the string.
        
            Returns: This method returns a System.Drawing.SizeF structure that represents the size, in the units 
             specified by the System.Drawing.Graphics.PageUnit property, of the string specified in the text 
             parameter as drawn with the font parameter and the stringFormat parameter.
        
        MeasureString(self: Graphics, text: str, font: Font) -> SizeF
        
            Measures the specified string when drawn with the specified System.Drawing.Font.
        
            text: String to measure.
            font: System.Drawing.Font that defines the text format of the string.
            Returns: This method returns a System.Drawing.SizeF structure that represents the size, in the units 
             specified by the System.Drawing.Graphics.PageUnit property, of the string specified by the text 
             parameter as drawn with the font parameter.
        
        MeasureString(self: Graphics, text: str, font: Font, width: int, format: StringFormat) -> SizeF
        
            Measures the specified string when drawn with the specified System.Drawing.Font and formatted 
             with the specified System.Drawing.StringFormat.
        
        
            text: String to measure.
            font: System.Drawing.Font that defines the text format of the string.
            width: Maximum width of the string.
            format: System.Drawing.StringFormat that represents formatting information, such as line spacing, for 
             the string.
        
            Returns: This method returns a System.Drawing.SizeF structure that represents the size, in the units 
             specified by the System.Drawing.Graphics.PageUnit property, of the string specified in the text 
             parameter as drawn with the font parameter and the stringFormat parameter.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def MultiplyTransform(self, matrix, order=None):
        """
        MultiplyTransform(self: Graphics, matrix: Matrix, order: MatrixOrder)
            Multiplies the world transformation of this System.Drawing.Graphics and specified the 
             System.Drawing.Drawing2D.Matrix in the specified order.
        
        
            matrix: 4x4 System.Drawing.Drawing2D.Matrix that multiplies the world transformation.
            order: Member of the System.Drawing.Drawing2D.MatrixOrder enumeration that determines the order of the 
             multiplication.
        
        MultiplyTransform(self: Graphics, matrix: Matrix)
            Multiplies the world transformation of this System.Drawing.Graphics and specified the 
             System.Drawing.Drawing2D.Matrix.
        
        
            matrix: 4x4 System.Drawing.Drawing2D.Matrix that multiplies the world transformation.
        """
        pass

    def ReleaseHdc(self, hdc=None):
        """
        ReleaseHdc(self: Graphics)
            Releases a device context handle obtained by a previous call to the 
             System.Drawing.Graphics.GetHdc method of this System.Drawing.Graphics.
        
        ReleaseHdc(self: Graphics, hdc: IntPtr)
            Releases a device context handle obtained by a previous call to the 
             System.Drawing.Graphics.GetHdc method of this System.Drawing.Graphics.
        
        
            hdc: Handle to a device context obtained by a previous call to the System.Drawing.Graphics.GetHdc 
             method of this System.Drawing.Graphics.
        """
        pass

    def ReleaseHdcInternal(self, hdc):
        """
        ReleaseHdcInternal(self: Graphics, hdc: IntPtr)
            Releases a handle to a device context.
        
            hdc: Handle to a device context.
        """
        pass

    def ResetClip(self):
        """
        ResetClip(self: Graphics)
            Resets the clip region of this System.Drawing.Graphics to an infinite region.
        """
        pass

    def ResetTransform(self):
        """
        ResetTransform(self: Graphics)
            Resets the world transformation matrix of this System.Drawing.Graphics to the identity matrix.
        """
        pass

    def Restore(self, gstate):
        """
        Restore(self: Graphics, gstate: GraphicsState)
            Restores the state of this System.Drawing.Graphics to the state represented by a 
             System.Drawing.Drawing2D.GraphicsState.
        
        
            gstate: System.Drawing.Drawing2D.GraphicsState that represents the state to which to restore this 
             System.Drawing.Graphics.
        """
        pass

    def RotateTransform(self, angle, order=None):
        """
        RotateTransform(self: Graphics, angle: Single, order: MatrixOrder)
            Applies the specified rotation to the transformation matrix of this System.Drawing.Graphics in 
             the specified order.
        
        
            angle: Angle of rotation in degrees.
            order: Member of the System.Drawing.Drawing2D.MatrixOrder enumeration that specifies whether the 
             rotation is appended or prepended to the matrix transformation.
        
        RotateTransform(self: Graphics, angle: Single)
            Applies the specified rotation to the transformation matrix of this System.Drawing.Graphics.
        
            angle: Angle of rotation in degrees.
        """
        pass

    def Save(self):
        """
        Save(self: Graphics) -> GraphicsState
        
            Saves the current state of this System.Drawing.Graphics and identifies the saved state with a 
             System.Drawing.Drawing2D.GraphicsState.
        
            Returns: This method returns a System.Drawing.Drawing2D.GraphicsState that represents the saved state of 
             this System.Drawing.Graphics.
        """
        pass

    def ScaleTransform(self, sx, sy, order=None):
        """
        ScaleTransform(self: Graphics, sx: Single, sy: Single, order: MatrixOrder)
            Applies the specified scaling operation to the transformation matrix of this 
             System.Drawing.Graphics in the specified order.
        
        
            sx: Scale factor in the x direction.
            sy: Scale factor in the y direction.
            order: Member of the System.Drawing.Drawing2D.MatrixOrder enumeration that specifies whether the 
             scaling operation is prepended or appended to the transformation matrix.
        
        ScaleTransform(self: Graphics, sx: Single, sy: Single)
            Applies the specified scaling operation to the transformation matrix of this 
             System.Drawing.Graphics by prepending it to the object's transformation matrix.
        
        
            sx: Scale factor in the x direction.
            sy: Scale factor in the y direction.
        """
        pass

    def SetClip(self, *__args):
        """
        SetClip(self: Graphics, rect: RectangleF, combineMode: CombineMode)
            Sets the clipping region of this System.Drawing.Graphics to the result of the specified 
             operation combining the current clip region and the rectangle specified by a 
             System.Drawing.RectangleF structure.
        
        
            rect: System.Drawing.RectangleF structure to combine.
            combineMode: Member of the System.Drawing.Drawing2D.CombineMode enumeration that specifies the combining 
             operation to use.
        
        SetClip(self: Graphics, rect: RectangleF)
            Sets the clipping region of this System.Drawing.Graphics to the rectangle specified by a 
             System.Drawing.RectangleF structure.
        
        
            rect: System.Drawing.RectangleF structure that represents the new clip region.
        SetClip(self: Graphics, path: GraphicsPath, combineMode: CombineMode)
            Sets the clipping region of this System.Drawing.Graphics to the result of the specified 
             operation combining the current clip region and the specified 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            path: System.Drawing.Drawing2D.GraphicsPath to combine.
            combineMode: Member of the System.Drawing.Drawing2D.CombineMode enumeration that specifies the combining 
             operation to use.
        
        SetClip(self: Graphics, path: GraphicsPath)
            Sets the clipping region of this System.Drawing.Graphics to the specified 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            path: System.Drawing.Drawing2D.GraphicsPath that represents the new clip region.
        SetClip(self: Graphics, rect: Rectangle, combineMode: CombineMode)
            Sets the clipping region of this System.Drawing.Graphics to the result of the specified 
             operation combining the current clip region and the rectangle specified by a 
             System.Drawing.Rectangle structure.
        
        
            rect: System.Drawing.Rectangle structure to combine.
            combineMode: Member of the System.Drawing.Drawing2D.CombineMode enumeration that specifies the combining 
             operation to use.
        
        SetClip(self: Graphics, region: Region, combineMode: CombineMode)
            Sets the clipping region of this System.Drawing.Graphics to the result of the specified 
             operation combining the current clip region and the specified System.Drawing.Region.
        
        
            region: System.Drawing.Region to combine.
            combineMode: Member from the System.Drawing.Drawing2D.CombineMode enumeration that specifies the combining 
             operation to use.
        
        SetClip(self: Graphics, rect: Rectangle)
            Sets the clipping region of this System.Drawing.Graphics to the rectangle specified by a 
             System.Drawing.Rectangle structure.
        
        
            rect: System.Drawing.Rectangle structure that represents the new clip region.
        SetClip(self: Graphics, g: Graphics, combineMode: CombineMode)
            Sets the clipping region of this System.Drawing.Graphics to the result of the specified 
             combining operation of the current clip region and the System.Drawing.Graphics.Clip property of 
             the specified System.Drawing.Graphics.
        
        
            g: System.Drawing.Graphics that specifies the clip region to combine.
            combineMode: Member of the System.Drawing.Drawing2D.CombineMode enumeration that specifies the combining 
             operation to use.
        
        SetClip(self: Graphics, g: Graphics)
            Sets the clipping region of this System.Drawing.Graphics to the Clip property of the specified 
             System.Drawing.Graphics.
        
        
            g: System.Drawing.Graphics from which to take the new clip region.
        """
        pass

    def TransformPoints(self, destSpace, srcSpace, pts):
        """
        TransformPoints(self: Graphics, destSpace: CoordinateSpace, srcSpace: CoordinateSpace, pts: Array[Point])
            Transforms an array of points from one coordinate space to another using the current world and 
             page transformations of this System.Drawing.Graphics.
        
        
            destSpace: Member of the System.Drawing.Drawing2D.CoordinateSpace enumeration that specifies the 
             destination coordinate space.
        
            srcSpace: Member of the System.Drawing.Drawing2D.CoordinateSpace enumeration that specifies the source 
             coordinate space.
        
            pts: Array of System.Drawing.Point structures that represents the points to transformation.
        TransformPoints(self: Graphics, destSpace: CoordinateSpace, srcSpace: CoordinateSpace, pts: Array[PointF])
            Transforms an array of points from one coordinate space to another using the current world and 
             page transformations of this System.Drawing.Graphics.
        
        
            destSpace: Member of the System.Drawing.Drawing2D.CoordinateSpace enumeration that specifies the 
             destination coordinate space.
        
            srcSpace: Member of the System.Drawing.Drawing2D.CoordinateSpace enumeration that specifies the source 
             coordinate space.
        
            pts: Array of System.Drawing.PointF structures that represent the points to transform.
        """
        pass

    def TranslateClip(self, dx, dy):
        """
        TranslateClip(self: Graphics, dx: Single, dy: Single)
            Translates the clipping region of this System.Drawing.Graphics by specified amounts in the 
             horizontal and vertical directions.
        
        
            dx: The x-coordinate of the translation.
            dy: The y-coordinate of the translation.
        TranslateClip(self: Graphics, dx: int, dy: int)
            Translates the clipping region of this System.Drawing.Graphics by specified amounts in the 
             horizontal and vertical directions.
        
        
            dx: The x-coordinate of the translation.
            dy: The y-coordinate of the translation.
        """
        pass

    def TranslateTransform(self, dx, dy, order=None):
        """
        TranslateTransform(self: Graphics, dx: Single, dy: Single, order: MatrixOrder)
            Changes the origin of the coordinate system by applying the specified translation to the 
             transformation matrix of this System.Drawing.Graphics in the specified order.
        
        
            dx: The x-coordinate of the translation.
            dy: The y-coordinate of the translation.
            order: Member of the System.Drawing.Drawing2D.MatrixOrder enumeration that specifies whether the 
             translation is prepended or appended to the transformation matrix.
        
        TranslateTransform(self: Graphics, dx: Single, dy: Single)
            Changes the origin of the coordinate system by prepending the specified translation to the 
             transformation matrix of this System.Drawing.Graphics.
        
        
            dx: The x-coordinate of the translation.
            dy: The y-coordinate of the translation.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Clip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Drawing.Region that limits the drawing region of this System.Drawing.Graphics.

Get: Clip(self: Graphics) -> Region

Set: Clip(self: Graphics) = value
"""

    ClipBounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Drawing.RectangleF structure that bounds the clipping region of this System.Drawing.Graphics.

Get: ClipBounds(self: Graphics) -> RectangleF

"""

    CompositingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies how composited images are drawn to this System.Drawing.Graphics.

Get: CompositingMode(self: Graphics) -> CompositingMode

Set: CompositingMode(self: Graphics) = value
"""

    CompositingQuality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rendering quality of composited images drawn to this System.Drawing.Graphics.

Get: CompositingQuality(self: Graphics) -> CompositingQuality

Set: CompositingQuality(self: Graphics) = value
"""

    DpiX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the horizontal resolution of this System.Drawing.Graphics.

Get: DpiX(self: Graphics) -> Single

"""

    DpiY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the vertical resolution of this System.Drawing.Graphics.

Get: DpiY(self: Graphics) -> Single

"""

    InterpolationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the interpolation mode associated with this System.Drawing.Graphics.

Get: InterpolationMode(self: Graphics) -> InterpolationMode

Set: InterpolationMode(self: Graphics) = value
"""

    IsClipEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the clipping region of this System.Drawing.Graphics is empty.

Get: IsClipEmpty(self: Graphics) -> bool

"""

    IsVisibleClipEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the visible clipping region of this System.Drawing.Graphics is empty.

Get: IsVisibleClipEmpty(self: Graphics) -> bool

"""

    PageScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the scaling between world units and page units for this System.Drawing.Graphics.

Get: PageScale(self: Graphics) -> Single

Set: PageScale(self: Graphics) = value
"""

    PageUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the unit of measure used for page coordinates in this System.Drawing.Graphics.

Get: PageUnit(self: Graphics) -> GraphicsUnit

Set: PageUnit(self: Graphics) = value
"""

    PixelOffsetMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or set a value specifying how pixels are offset during rendering of this System.Drawing.Graphics.

Get: PixelOffsetMode(self: Graphics) -> PixelOffsetMode

Set: PixelOffsetMode(self: Graphics) = value
"""

    RenderingOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rendering origin of this System.Drawing.Graphics for dithering and for hatch brushes.

Get: RenderingOrigin(self: Graphics) -> Point

Set: RenderingOrigin(self: Graphics) = value
"""

    SmoothingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rendering quality for this System.Drawing.Graphics.

Get: SmoothingMode(self: Graphics) -> SmoothingMode

Set: SmoothingMode(self: Graphics) = value
"""

    TextContrast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the gamma correction value for rendering text.

Get: TextContrast(self: Graphics) -> int

Set: TextContrast(self: Graphics) = value
"""

    TextRenderingHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rendering mode for text associated with this System.Drawing.Graphics.

Get: TextRenderingHint(self: Graphics) -> TextRenderingHint

Set: TextRenderingHint(self: Graphics) = value
"""

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a copy of the geometric world transformation for this System.Drawing.Graphics.

Get: Transform(self: Graphics) -> Matrix

Set: Transform(self: Graphics) = value
"""

    VisibleClipBounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the bounding rectangle of the visible clipping region of this System.Drawing.Graphics.

Get: VisibleClipBounds(self: Graphics) -> RectangleF

"""


    DrawImageAbort = None
    EnumerateMetafileProc = None


class GraphicsUnit(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the unit of measure for the given data.
    
    enum GraphicsUnit, values: Display (1), Document (5), Inch (4), Millimeter (6), Pixel (2), Point (3), World (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Display = None
    Document = None
    Inch = None
    Millimeter = None
    Pixel = None
    Point = None
    value__ = None
    World = None


class Icon(MarshalByRefObject, ISerializable, ICloneable, IDisposable):
    """
    Represents a Windows icon, which is a small bitmap image that is used to represent an object. Icons can be thought of as transparent bitmaps, although their size is determined by the system.
    
    Icon(original: Icon, size: Size)
    Icon(original: Icon, width: int, height: int)
    Icon(type: Type, resource: str)
    Icon(stream: Stream)
    Icon(stream: Stream, width: int, height: int)
    Icon(fileName: str)
    Icon(fileName: str, size: Size)
    Icon(fileName: str, width: int, height: int)
    Icon(stream: Stream, size: Size)
    """
    def Clone(self):
        """
        Clone(self: Icon) -> object
        
            Clones the System.Drawing.Icon, creating a duplicate image.
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

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def Save(self, outputStream):
        """
        Save(self: Icon, outputStream: Stream)
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

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, fileName: str)
        __new__(cls: type, fileName: str, size: Size)
        __new__(cls: type, fileName: str, width: int, height: int)
        __new__(cls: type, original: Icon, size: Size)
        __new__(cls: type, original: Icon, width: int, height: int)
        __new__(cls: type, type: Type, resource: str)
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, size: Size)
        __new__(cls: type, stream: Stream, width: int, height: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Windows handle for this System.Drawing.Icon. This is not a copy of the handle; do not free it.

Get: Handle(self: Icon) -> IntPtr

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of this System.Drawing.Icon.

Get: Height(self: Icon) -> int

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of this System.Drawing.Icon.

Get: Size(self: Icon) -> Size

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width of this System.Drawing.Icon.

Get: Width(self: Icon) -> int

"""



class IconConverter(ExpandableObjectConverter):
    """
    Converts an System.Drawing.Icon object from one data type to another. Access this class through the System.ComponentModel.TypeDescriptor object.
    
    IconConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: IconConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether this System.Drawing.IconConverter can convert an instance of a specified type 
             to an System.Drawing.Icon, using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that specifies the type you want to convert from.
            Returns: This method returns true if this System.Drawing.IconConverter can perform the conversion; 
             otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: IconConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether this System.Drawing.IconConverter can convert an System.Drawing.Icon to an 
             instance of a specified type, using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that specifies the type you want to convert to.
            Returns: This method returns true if this System.Drawing.IconConverter can perform the conversion; 
             otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: IconConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts a specified object to an System.Drawing.Icon.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo that holds information about a specific culture.
            value: The System.Object to be converted.
            Returns: If this method succeeds, it returns the System.Drawing.Icon that it created by converting the 
             specified object. Otherwise, it throws an exception.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: IconConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts an System.Drawing.Icon (or an object that can be cast to an System.Drawing.Icon) to a 
             specified type.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo object that specifies formatting conventions used by a 
             particular culture.
        
            value: The object to convert. This object should be of type icon or some type that can be cast to 
             System.Drawing.Icon.
        
            destinationType: The type to convert the icon to.
            Returns: This method returns the converted object.
        """
        pass


class IDeviceContext(IDisposable):
    """ Defines methods for obtaining and releasing an existing handle to a Windows device context. """
    def GetHdc(self):
        """
        GetHdc(self: IDeviceContext) -> IntPtr
        
            Returns the handle to a Windows device context.
            Returns: An System.IntPtr representing the handle of a device context.
        """
        pass

    def ReleaseHdc(self):
        """
        ReleaseHdc(self: IDeviceContext)
            Releases the handle of a Windows device context.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ImageAnimator(object):
    """ Animates an image that has time-based frames. """
    @staticmethod
    def Animate(image, onFrameChangedHandler):
        """
        Animate(image: Image, onFrameChangedHandler: EventHandler)
            Displays a multiple-frame image as an animation.
        
            image: The System.Drawing.Image object to animate.
            onFrameChangedHandler: An EventHandler object that specifies the method that is called when the animation frame changes.
        """
        pass

    @staticmethod
    def CanAnimate(image):
        """
        CanAnimate(image: Image) -> bool
        
            Returns a Boolean value indicating whether the specified image contains time-based frames.
        
            image: The System.Drawing.Image object to test.
            Returns: This method returns true if the specified image contains time-based frames; otherwise, false.
        """
        pass

    @staticmethod
    def StopAnimate(image, onFrameChangedHandler):
        """
        StopAnimate(image: Image, onFrameChangedHandler: EventHandler)
            Terminates a running animation.
        
            image: The System.Drawing.Image object to stop animating.
            onFrameChangedHandler: An EventHandler object that specifies the method that is called when the animation frame changes.
        """
        pass

    @staticmethod
    def UpdateFrames(image=None):
        """
        UpdateFrames()
            Advances the frame in all images currently being animated. The new frame is drawn the next time 
             the image is rendered.
        
        UpdateFrames(image: Image)
            Advances the frame in the specified image. The new frame is drawn the next time the image is 
             rendered. This method applies only to images with time-based frames.
        
        
            image: The System.Drawing.Image object for which to update frames.
        """
        pass


class ImageConverter(TypeConverter):
    """
    System.Drawing.ImageConverter  is a class that can be used to convert System.Drawing.Image objects from one data type to another. Access this class through the System.ComponentModel.TypeDescriptor object.
    
    ImageConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: ImageConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether this System.Drawing.ImageConverter can convert an instance of a specified 
             type to an System.Drawing.Image, using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that specifies the type you want to convert from.
            Returns: This method returns true if this System.Drawing.ImageConverter can perform the conversion; 
             otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: ImageConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether this System.Drawing.ImageConverter can convert an System.Drawing.Image to an 
             instance of a specified type, using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that specifies the type you want to convert to.
            Returns: This method returns true if this System.Drawing.ImageConverter can perform the conversion; 
             otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: ImageConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts a specified object to an System.Drawing.Image.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo that holds information about a specific culture.
            value: The System.Object to be converted.
            Returns: If this method succeeds, it returns the System.Drawing.Image that it created by converting the 
             specified object. Otherwise, it throws an exception.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: ImageConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts an System.Drawing.Image (or an object that can be cast to an System.Drawing.Image) to 
             the specified type.
        
        
            context: A formatter context. This object can be used to get more information about the environment this 
             converter is being called from. This may be null, so you should always check. Also, properties 
             on the context object may also return null.
        
            culture: A System.Globalization.CultureInfo object that specifies formatting conventions used by a 
             particular culture.
        
            value: The System.Drawing.Image to convert.
            destinationType: The System.Type to convert the System.Drawing.Image to.
            Returns: This method returns the converted object.
        """
        pass

    def GetProperties(self, *__args):
        """
        GetProperties(self: ImageConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Gets the set of properties for this type.
        
            context: A type descriptor through which additional context can be provided.
            value: The value of the object to get the properties for.
            attributes: An array of System.Attribute objects that describe the properties.
            Returns: The set of properties that should be exposed for this data type. If no properties should be 
             exposed, this can return null. The default implementation always returns null.
        """
        pass

    def GetPropertiesSupported(self, context=None):
        """
        GetPropertiesSupported(self: ImageConverter, context: ITypeDescriptorContext) -> bool
        
            Indicates whether this object supports properties. By default, this is false.
        
            context: A type descriptor through which additional context can be provided.
            Returns: This method returns true if the erload:System.Drawing.ImageConverter.GetProperties method should 
             be called to find the properties of this object.
        """
        pass


class ImageFormatConverter(TypeConverter):
    """
    System.Drawing.ImageFormatConverter is a class that can be used to convert System.Drawing.Imaging.ImageFormat objects from one data type to another. Access this class through the System.ComponentModel.TypeDescriptor object.
    
    ImageFormatConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: ImageFormatConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Indicates whether this converter can convert an object in the specified source type to the 
             native type of the converter.
        
        
            context: A formatter context. This object can be used to get more information about the environment this 
             converter is being called from. This may be null, so you should always check. Also, properties 
             on the context object may also return null.
        
            sourceType: The type you want to convert from.
            Returns: This method returns true if this object can perform the conversion.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: ImageFormatConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object to the specified 
             destination type using the context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that specifies the context for this type 
             conversion.
        
            destinationType: The System.Type that represents the type to which you want to convert this 
             System.Drawing.Imaging.ImageFormat object.
        
            Returns: This method returns true if this object can perform the conversion.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: ImageFormatConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the specified object to an System.Drawing.Imaging.ImageFormat object.
        
            context: A formatter context. This object can be used to get more information about the environment this 
             converter is being called from. This may be null, so you should always check. Also, properties 
             on the context object may also return null.
        
            culture: A System.Globalization.CultureInfo object that specifies formatting conventions for a particular 
             culture.
        
            value: The object to convert.
            Returns: The converted object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: ImageFormatConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified object to the specified type.
        
            context: A formatter context. This object can be used to get more information about the environment this 
             converter is being called from. This may be null, so you should always check. Also, properties 
             on the context object may also return null.
        
            culture: A System.Globalization.CultureInfo object that specifies formatting conventions for a particular 
             culture.
        
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object.
        """
        pass

    def GetStandardValues(self, context=None):
        """
        GetStandardValues(self: ImageFormatConverter, context: ITypeDescriptorContext) -> StandardValuesCollection
        
            Gets a collection that contains a set of standard values for the data type this validator is 
             designed for. Returns null if the data type does not support a standard set of values.
        
        
            context: A formatter context. This object can be used to get more information about the environment this 
             converter is being called from. This may be null, so you should always check. Also, properties 
             on the context object may also return null.
        
            Returns: A collection that contains a standard set of valid values, or null. The default implementation 
             always returns null.
        """
        pass

    def GetStandardValuesSupported(self, context=None):
        """
        GetStandardValuesSupported(self: ImageFormatConverter, context: ITypeDescriptorContext) -> bool
        
            Indicates whether this object supports a standard set of values that can be picked from a list.
        
            context: A type descriptor through which additional context can be provided.
            Returns: This method returns true if the erload:System.Drawing.ImageFormatConverter.GetStandardValues 
             method should be called to find a common set of values the object supports.
        """
        pass


class KnownColor(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the known system colors.
    
    enum KnownColor, values: ActiveBorder (1), ActiveCaption (2), ActiveCaptionText (3), AliceBlue (28), AntiqueWhite (29), AppWorkspace (4), Aqua (30), Aquamarine (31), Azure (32), Beige (33), Bisque (34), Black (35), BlanchedAlmond (36), Blue (37), BlueViolet (38), Brown (39), BurlyWood (40), ButtonFace (168), ButtonHighlight (169), ButtonShadow (170), CadetBlue (41), Chartreuse (42), Chocolate (43), Control (5), ControlDark (6), ControlDarkDark (7), ControlLight (8), ControlLightLight (9), ControlText (10), Coral (44), CornflowerBlue (45), Cornsilk (46), Crimson (47), Cyan (48), DarkBlue (49), DarkCyan (50), DarkGoldenrod (51), DarkGray (52), DarkGreen (53), DarkKhaki (54), DarkMagenta (55), DarkOliveGreen (56), DarkOrange (57), DarkOrchid (58), DarkRed (59), DarkSalmon (60), DarkSeaGreen (61), DarkSlateBlue (62), DarkSlateGray (63), DarkTurquoise (64), DarkViolet (65), DeepPink (66), DeepSkyBlue (67), Desktop (11), DimGray (68), DodgerBlue (69), Firebrick (70), FloralWhite (71), ForestGreen (72), Fuchsia (73), Gainsboro (74), GhostWhite (75), Gold (76), Goldenrod (77), GradientActiveCaption (171), GradientInactiveCaption (172), Gray (78), GrayText (12), Green (79), GreenYellow (80), Highlight (13), HighlightText (14), Honeydew (81), HotPink (82), HotTrack (15), InactiveBorder (16), InactiveCaption (17), InactiveCaptionText (18), IndianRed (83), Indigo (84), Info (19), InfoText (20), Ivory (85), Khaki (86), Lavender (87), LavenderBlush (88), LawnGreen (89), LemonChiffon (90), LightBlue (91), LightCoral (92), LightCyan (93), LightGoldenrodYellow (94), LightGray (95), LightGreen (96), LightPink (97), LightSalmon (98), LightSeaGreen (99), LightSkyBlue (100), LightSlateGray (101), LightSteelBlue (102), LightYellow (103), Lime (104), LimeGreen (105), Linen (106), Magenta (107), Maroon (108), MediumAquamarine (109), MediumBlue (110), MediumOrchid (111), MediumPurple (112), MediumSeaGreen (113), MediumSlateBlue (114), MediumSpringGreen (115), MediumTurquoise (116), MediumVioletRed (117), Menu (21), MenuBar (173), MenuHighlight (174), MenuText (22), MidnightBlue (118), MintCream (119), MistyRose (120), Moccasin (121), NavajoWhite (122), Navy (123), OldLace (124), Olive (125), OliveDrab (126), Orange (127), OrangeRed (128), Orchid (129), PaleGoldenrod (130), PaleGreen (131), PaleTurquoise (132), PaleVioletRed (133), PapayaWhip (134), PeachPuff (135), Peru (136), Pink (137), Plum (138), PowderBlue (139), Purple (140), Red (141), RosyBrown (142), RoyalBlue (143), SaddleBrown (144), Salmon (145), SandyBrown (146), ScrollBar (23), SeaGreen (147), SeaShell (148), Sienna (149), Silver (150), SkyBlue (151), SlateBlue (152), SlateGray (153), Snow (154), SpringGreen (155), SteelBlue (156), Tan (157), Teal (158), Thistle (159), Tomato (160), Transparent (27), Turquoise (161), Violet (162), Wheat (163), White (164), WhiteSmoke (165), Window (24), WindowFrame (25), WindowText (26), Yellow (166), YellowGreen (167)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ActiveBorder = None
    ActiveCaption = None
    ActiveCaptionText = None
    AliceBlue = None
    AntiqueWhite = None
    AppWorkspace = None
    Aqua = None
    Aquamarine = None
    Azure = None
    Beige = None
    Bisque = None
    Black = None
    BlanchedAlmond = None
    Blue = None
    BlueViolet = None
    Brown = None
    BurlyWood = None
    ButtonFace = None
    ButtonHighlight = None
    ButtonShadow = None
    CadetBlue = None
    Chartreuse = None
    Chocolate = None
    Control = None
    ControlDark = None
    ControlDarkDark = None
    ControlLight = None
    ControlLightLight = None
    ControlText = None
    Coral = None
    CornflowerBlue = None
    Cornsilk = None
    Crimson = None
    Cyan = None
    DarkBlue = None
    DarkCyan = None
    DarkGoldenrod = None
    DarkGray = None
    DarkGreen = None
    DarkKhaki = None
    DarkMagenta = None
    DarkOliveGreen = None
    DarkOrange = None
    DarkOrchid = None
    DarkRed = None
    DarkSalmon = None
    DarkSeaGreen = None
    DarkSlateBlue = None
    DarkSlateGray = None
    DarkTurquoise = None
    DarkViolet = None
    DeepPink = None
    DeepSkyBlue = None
    Desktop = None
    DimGray = None
    DodgerBlue = None
    Firebrick = None
    FloralWhite = None
    ForestGreen = None
    Fuchsia = None
    Gainsboro = None
    GhostWhite = None
    Gold = None
    Goldenrod = None
    GradientActiveCaption = None
    GradientInactiveCaption = None
    Gray = None
    GrayText = None
    Green = None
    GreenYellow = None
    Highlight = None
    HighlightText = None
    Honeydew = None
    HotPink = None
    HotTrack = None
    InactiveBorder = None
    InactiveCaption = None
    InactiveCaptionText = None
    IndianRed = None
    Indigo = None
    Info = None
    InfoText = None
    Ivory = None
    Khaki = None
    Lavender = None
    LavenderBlush = None
    LawnGreen = None
    LemonChiffon = None
    LightBlue = None
    LightCoral = None
    LightCyan = None
    LightGoldenrodYellow = None
    LightGray = None
    LightGreen = None
    LightPink = None
    LightSalmon = None
    LightSeaGreen = None
    LightSkyBlue = None
    LightSlateGray = None
    LightSteelBlue = None
    LightYellow = None
    Lime = None
    LimeGreen = None
    Linen = None
    Magenta = None
    Maroon = None
    MediumAquamarine = None
    MediumBlue = None
    MediumOrchid = None
    MediumPurple = None
    MediumSeaGreen = None
    MediumSlateBlue = None
    MediumSpringGreen = None
    MediumTurquoise = None
    MediumVioletRed = None
    Menu = None
    MenuBar = None
    MenuHighlight = None
    MenuText = None
    MidnightBlue = None
    MintCream = None
    MistyRose = None
    Moccasin = None
    NavajoWhite = None
    Navy = None
    OldLace = None
    Olive = None
    OliveDrab = None
    Orange = None
    OrangeRed = None
    Orchid = None
    PaleGoldenrod = None
    PaleGreen = None
    PaleTurquoise = None
    PaleVioletRed = None
    PapayaWhip = None
    PeachPuff = None
    Peru = None
    Pink = None
    Plum = None
    PowderBlue = None
    Purple = None
    Red = None
    RosyBrown = None
    RoyalBlue = None
    SaddleBrown = None
    Salmon = None
    SandyBrown = None
    ScrollBar = None
    SeaGreen = None
    SeaShell = None
    Sienna = None
    Silver = None
    SkyBlue = None
    SlateBlue = None
    SlateGray = None
    Snow = None
    SpringGreen = None
    SteelBlue = None
    Tan = None
    Teal = None
    Thistle = None
    Tomato = None
    Transparent = None
    Turquoise = None
    value__ = None
    Violet = None
    Wheat = None
    White = None
    WhiteSmoke = None
    Window = None
    WindowFrame = None
    WindowText = None
    Yellow = None
    YellowGreen = None


class Pen(MarshalByRefObject, ISystemColorTracker, ICloneable, IDisposable):
    """
    Defines an object used to draw lines and curves. This class cannot be inherited.
    
    Pen(color: Color)
    Pen(color: Color, width: Single)
    Pen(brush: Brush)
    Pen(brush: Brush, width: Single)
    """
    def Clone(self):
        """
        Clone(self: Pen) -> object
        
            Creates an exact copy of this System.Drawing.Pen.
            Returns: An System.Object that can be cast to a System.Drawing.Pen.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Pen)
            Releases all resources used by this System.Drawing.Pen.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def MultiplyTransform(self, matrix, order=None):
        """
        MultiplyTransform(self: Pen, matrix: Matrix, order: MatrixOrder)
            Multiplies the transformation matrix for this System.Drawing.Pen by the specified 
             System.Drawing.Drawing2D.Matrix in the specified order.
        
        
            matrix: The System.Drawing.Drawing2D.Matrix by which to multiply the transformation matrix.
            order: The order in which to perform the multiplication operation.
        MultiplyTransform(self: Pen, matrix: Matrix)
            Multiplies the transformation matrix for this System.Drawing.Pen by the specified 
             System.Drawing.Drawing2D.Matrix.
        
        
            matrix: The System.Drawing.Drawing2D.Matrix object by which to multiply the transformation matrix.
        """
        pass

    def ResetTransform(self):
        """
        ResetTransform(self: Pen)
            Resets the geometric transformation matrix for this System.Drawing.Pen to identity.
        """
        pass

    def RotateTransform(self, angle, order=None):
        """
        RotateTransform(self: Pen, angle: Single, order: MatrixOrder)
            Rotates the local geometric transformation by the specified angle in the specified order.
        
            angle: The angle of rotation.
            order: A System.Drawing.Drawing2D.MatrixOrder that specifies whether to append or prepend the rotation 
             matrix.
        
        RotateTransform(self: Pen, angle: Single)
            Rotates the local geometric transformation by the specified angle. This method prepends the 
             rotation to the transformation.
        
        
            angle: The angle of rotation.
        """
        pass

    def ScaleTransform(self, sx, sy, order=None):
        """
        ScaleTransform(self: Pen, sx: Single, sy: Single, order: MatrixOrder)
            Scales the local geometric transformation by the specified factors in the specified order.
        
            sx: The factor by which to scale the transformation in the x-axis direction.
            sy: The factor by which to scale the transformation in the y-axis direction.
            order: A System.Drawing.Drawing2D.MatrixOrder that specifies whether to append or prepend the scaling 
             matrix.
        
        ScaleTransform(self: Pen, sx: Single, sy: Single)
            Scales the local geometric transformation by the specified factors. This method prepends the 
             scaling matrix to the transformation.
        
        
            sx: The factor by which to scale the transformation in the x-axis direction.
            sy: The factor by which to scale the transformation in the y-axis direction.
        """
        pass

    def SetLineCap(self, startCap, endCap, dashCap):
        """
        SetLineCap(self: Pen, startCap: LineCap, endCap: LineCap, dashCap: DashCap)
            Sets the values that determine the style of cap used to end lines drawn by this 
             System.Drawing.Pen.
        
        
            startCap: A System.Drawing.Drawing2D.LineCap that represents the cap style to use at the beginning of 
             lines drawn with this System.Drawing.Pen.
        
            endCap: A System.Drawing.Drawing2D.LineCap that represents the cap style to use at the end of lines 
             drawn with this System.Drawing.Pen.
        
            dashCap: A System.Drawing.Drawing2D.LineCap that represents the cap style to use at the beginning or end 
             of dashed lines drawn with this System.Drawing.Pen.
        """
        pass

    def TranslateTransform(self, dx, dy, order=None):
        """
        TranslateTransform(self: Pen, dx: Single, dy: Single, order: MatrixOrder)
            Translates the local geometric transformation by the specified dimensions in the specified order.
        
            dx: The value of the translation in x.
            dy: The value of the translation in y.
            order: The order (prepend or append) in which to apply the translation.
        TranslateTransform(self: Pen, dx: Single, dy: Single)
            Translates the local geometric transformation by the specified dimensions. This method prepends 
             the translation to the transformation.
        
        
            dx: The value of the translation in x.
            dy: The value of the translation in y.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, color: Color)
        __new__(cls: type, color: Color, width: Single)
        __new__(cls: type, brush: Brush)
        __new__(cls: type, brush: Brush, width: Single)
        """
        pass

    Alignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the alignment for this System.Drawing.Pen.

Get: Alignment(self: Pen) -> PenAlignment

Set: Alignment(self: Pen) = value
"""

    Brush = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Drawing.Brush that determines attributes of this System.Drawing.Pen.

Get: Brush(self: Pen) -> Brush

Set: Brush(self: Pen) = value
"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of this System.Drawing.Pen.

Get: Color(self: Pen) -> Color

Set: Color(self: Pen) = value
"""

    CompoundArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of values that specifies a compound pen. A compound pen draws a compound line made up of parallel lines and spaces.

Get: CompoundArray(self: Pen) -> Array[Single]

Set: CompoundArray(self: Pen) = value
"""

    CustomEndCap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a custom cap to use at the end of lines drawn with this System.Drawing.Pen.

Get: CustomEndCap(self: Pen) -> CustomLineCap

Set: CustomEndCap(self: Pen) = value
"""

    CustomStartCap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a custom cap to use at the beginning of lines drawn with this System.Drawing.Pen.

Get: CustomStartCap(self: Pen) -> CustomLineCap

Set: CustomStartCap(self: Pen) = value
"""

    DashCap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the cap style used at the end of the dashes that make up dashed lines drawn with this System.Drawing.Pen.

Get: DashCap(self: Pen) -> DashCap

Set: DashCap(self: Pen) = value
"""

    DashOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the distance from the start of a line to the beginning of a dash pattern.

Get: DashOffset(self: Pen) -> Single

Set: DashOffset(self: Pen) = value
"""

    DashPattern = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of custom dashes and spaces.

Get: DashPattern(self: Pen) -> Array[Single]

Set: DashPattern(self: Pen) = value
"""

    DashStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the style used for dashed lines drawn with this System.Drawing.Pen.

Get: DashStyle(self: Pen) -> DashStyle

Set: DashStyle(self: Pen) = value
"""

    EndCap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the cap style used at the end of lines drawn with this System.Drawing.Pen.

Get: EndCap(self: Pen) -> LineCap

Set: EndCap(self: Pen) = value
"""

    LineJoin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the join style for the ends of two consecutive lines drawn with this System.Drawing.Pen.

Get: LineJoin(self: Pen) -> LineJoin

Set: LineJoin(self: Pen) = value
"""

    MiterLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the limit of the thickness of the join on a mitered corner.

Get: MiterLimit(self: Pen) -> Single

Set: MiterLimit(self: Pen) = value
"""

    PenType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the style of lines drawn with this System.Drawing.Pen.

Get: PenType(self: Pen) -> PenType

"""

    StartCap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the cap style used at the beginning of lines drawn with this System.Drawing.Pen.

Get: StartCap(self: Pen) -> LineCap

Set: StartCap(self: Pen) = value
"""

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a copy of the geometric transformation for this System.Drawing.Pen.

Get: Transform(self: Pen) -> Matrix

Set: Transform(self: Pen) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the width of this System.Drawing.Pen, in units of the System.Drawing.Graphics object used for drawing.

Get: Width(self: Pen) -> Single

Set: Width(self: Pen) = value
"""



class Pens(object):
    """ Pens for all the standard colors. This class cannot be inherited. """
    AliceBlue = None
    AntiqueWhite = None
    Aqua = None
    Aquamarine = None
    Azure = None
    Beige = None
    Bisque = None
    Black = None
    BlanchedAlmond = None
    Blue = None
    BlueViolet = None
    Brown = None
    BurlyWood = None
    CadetBlue = None
    Chartreuse = None
    Chocolate = None
    Coral = None
    CornflowerBlue = None
    Cornsilk = None
    Crimson = None
    Cyan = None
    DarkBlue = None
    DarkCyan = None
    DarkGoldenrod = None
    DarkGray = None
    DarkGreen = None
    DarkKhaki = None
    DarkMagenta = None
    DarkOliveGreen = None
    DarkOrange = None
    DarkOrchid = None
    DarkRed = None
    DarkSalmon = None
    DarkSeaGreen = None
    DarkSlateBlue = None
    DarkSlateGray = None
    DarkTurquoise = None
    DarkViolet = None
    DeepPink = None
    DeepSkyBlue = None
    DimGray = None
    DodgerBlue = None
    Firebrick = None
    FloralWhite = None
    ForestGreen = None
    Fuchsia = None
    Gainsboro = None
    GhostWhite = None
    Gold = None
    Goldenrod = None
    Gray = None
    Green = None
    GreenYellow = None
    Honeydew = None
    HotPink = None
    IndianRed = None
    Indigo = None
    Ivory = None
    Khaki = None
    Lavender = None
    LavenderBlush = None
    LawnGreen = None
    LemonChiffon = None
    LightBlue = None
    LightCoral = None
    LightCyan = None
    LightGoldenrodYellow = None
    LightGray = None
    LightGreen = None
    LightPink = None
    LightSalmon = None
    LightSeaGreen = None
    LightSkyBlue = None
    LightSlateGray = None
    LightSteelBlue = None
    LightYellow = None
    Lime = None
    LimeGreen = None
    Linen = None
    Magenta = None
    Maroon = None
    MediumAquamarine = None
    MediumBlue = None
    MediumOrchid = None
    MediumPurple = None
    MediumSeaGreen = None
    MediumSlateBlue = None
    MediumSpringGreen = None
    MediumTurquoise = None
    MediumVioletRed = None
    MidnightBlue = None
    MintCream = None
    MistyRose = None
    Moccasin = None
    NavajoWhite = None
    Navy = None
    OldLace = None
    Olive = None
    OliveDrab = None
    Orange = None
    OrangeRed = None
    Orchid = None
    PaleGoldenrod = None
    PaleGreen = None
    PaleTurquoise = None
    PaleVioletRed = None
    PapayaWhip = None
    PeachPuff = None
    Peru = None
    Pink = None
    Plum = None
    PowderBlue = None
    Purple = None
    Red = None
    RosyBrown = None
    RoyalBlue = None
    SaddleBrown = None
    Salmon = None
    SandyBrown = None
    SeaGreen = None
    SeaShell = None
    Sienna = None
    Silver = None
    SkyBlue = None
    SlateBlue = None
    SlateGray = None
    Snow = None
    SpringGreen = None
    SteelBlue = None
    Tan = None
    Teal = None
    Thistle = None
    Tomato = None
    Transparent = None
    Turquoise = None
    Violet = None
    Wheat = None
    White = None
    WhiteSmoke = None
    Yellow = None
    YellowGreen = None


class Point(object):
    """
    Represents an ordered pair of integer x- and y-coordinates that defines a point in a two-dimensional plane.
    
    Point(x: int, y: int)
    Point(sz: Size)
    Point(dw: int)
    """
    @staticmethod
    def Add(pt, sz):
        """
        Add(pt: Point, sz: Size) -> Point
        
            Adds the specified System.Drawing.Size to the specified System.Drawing.Point.
        
            pt: The System.Drawing.Point to add.
            sz: The System.Drawing.Size to add
            Returns: The System.Drawing.Point that is the result of the addition operation.
        """
        pass

    @staticmethod
    def Ceiling(value):
        """
        Ceiling(value: PointF) -> Point
        
            Converts the specified System.Drawing.PointF to a System.Drawing.Point by rounding the values of 
             the System.Drawing.PointF to the next higher integer values.
        
        
            value: The System.Drawing.PointF to convert.
            Returns: The System.Drawing.Point this method converts to.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Point, obj: object) -> bool
        
            Specifies whether this System.Drawing.Point contains the same coordinates as the specified 
             System.Object.
        
        
            obj: The System.Object to test.
            Returns: true if obj is a System.Drawing.Point and has the same coordinates as this System.Drawing.Point.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Point) -> int
        
            Returns a hash code for this System.Drawing.Point.
            Returns: An integer value that specifies a hash value for this System.Drawing.Point.
        """
        pass

    def Offset(self, *__args):
        """
        Offset(self: Point, p: Point)
            Translates this System.Drawing.Point by the specified System.Drawing.Point.
        
            p: The System.Drawing.Point used offset this System.Drawing.Point.
        Offset(self: Point, dx: int, dy: int)
            Translates this System.Drawing.Point by the specified amount.
        
            dx: The amount to offset the x-coordinate.
            dy: The amount to offset the y-coordinate.
        """
        pass

    @staticmethod
    def Round(value):
        """
        Round(value: PointF) -> Point
        
            Converts the specified System.Drawing.PointF to a System.Drawing.Point object by rounding the 
             System.Drawing.Point values to the nearest integer.
        
        
            value: The System.Drawing.PointF to convert.
            Returns: The System.Drawing.Point this method converts to.
        """
        pass

    @staticmethod
    def Subtract(pt, sz):
        """
        Subtract(pt: Point, sz: Size) -> Point
        
            Returns the result of subtracting specified System.Drawing.Size from the specified 
             System.Drawing.Point.
        
        
            pt: The System.Drawing.Point to be subtracted from.
            sz: The System.Drawing.Size to subtract from the System.Drawing.Point.
            Returns: The System.Drawing.Point that is the result of the subtraction operation.
        """
        pass

    def ToString(self):
        """
        ToString(self: Point) -> str
        
            Converts this System.Drawing.Point to a human-readable string.
            Returns: A string that represents this System.Drawing.Point.
        """
        pass

    @staticmethod
    def Truncate(value):
        """
        Truncate(value: PointF) -> Point
        
            Converts the specified System.Drawing.PointF to a System.Drawing.Point by truncating the values 
             of the System.Drawing.Point.
        
        
            value: The System.Drawing.PointF to convert.
            Returns: The System.Drawing.Point this method converts to.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Point]() -> Point
        
        __new__(cls: type, x: int, y: int)
        __new__(cls: type, sz: Size)
        __new__(cls: type, dw: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this System.Drawing.Point is empty.

Get: IsEmpty(self: Point) -> bool

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate of this System.Drawing.Point.

Get: X(self: Point) -> int

Set: X(self: Point) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate of this System.Drawing.Point.

Get: Y(self: Point) -> int

Set: Y(self: Point) = value
"""


    Empty = None


class PointConverter(TypeConverter):
    """
    Converts a System.Drawing.Point object from one data type to another.
    
    PointConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: PointConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines if this converter can convert an object in the given source type to the native type 
             of the converter.
        
        
            context: A formatter context. This object can be used to get additional information about the environment 
             this converter is being called from. This may be null, so you should always check. Also, 
             properties on the context object may also return null.
        
            sourceType: The type you want to convert from.
            Returns: true if this object can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: PointConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object to the given destination 
             type using the context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext object that provides a format context.
            destinationType: A System.Type object that represents the type you want to convert to.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: PointConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the specified object to a System.Drawing.Point object.
        
            context: A formatter context. This object can be used to get additional information about the environment 
             this converter is being called from. This may be null, so you should always check. Also, 
             properties on the context object may also return null.
        
            culture: An object that contains culture specific information, such as the language, calendar, and 
             cultural conventions associated with a specific culture. It is based on the RFC 1766 standard.
        
            value: The object to convert.
            Returns: The converted object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: PointConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified object to the specified type.
        
            context: A formatter context. This object can be used to get additional information about the environment 
             this converter is being called from. This may be null, so you should always check. Also, 
             properties on the context object may also return null.
        
            culture: An object that contains culture specific information, such as the language, calendar, and 
             cultural conventions associated with a specific culture. It is based on the RFC 1766 standard.
        
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object.
        """
        pass

    def CreateInstance(self, *__args):
        """
        CreateInstance(self: PointConverter, context: ITypeDescriptorContext, propertyValues: IDictionary) -> object
        
            Creates an instance of this type given a set of property values for the object.
        
            context: A type descriptor through which additional context can be provided.
            propertyValues: A dictionary of new property values. The dictionary contains a series of name-value pairs, one 
             for each property returned from 
             System.Drawing.PointConverter.GetProperties(System.ComponentModel.ITypeDescriptorContext,System.O
             bject,System.Attribute[]).
        
            Returns: The newly created object, or null if the object could not be created. The default implementation 
             returns null.
        """
        pass

    def GetCreateInstanceSupported(self, context=None):
        """
        GetCreateInstanceSupported(self: PointConverter, context: ITypeDescriptorContext) -> bool
        
            Determines if changing a value on this object should require a call to 
             System.Drawing.PointConverter.CreateInstance(System.ComponentModel.ITypeDescriptorContext,System.
             Collections.IDictionary) to create a new value.
        
        
            context: A System.ComponentModel.TypeDescriptor through which additional context can be provided.
            Returns: true if the 
             System.Drawing.PointConverter.CreateInstance(System.ComponentModel.ITypeDescriptorContext,System.
             Collections.IDictionary) method should be called when a change is made to one or more properties 
             of this object; otherwise, false.
        """
        pass

    def GetProperties(self, *__args):
        """
        GetProperties(self: PointConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Retrieves the set of properties for this type. By default, a type does not return any properties.
        
            context: A type descriptor through which additional context can be provided.
            value: The value of the object to get the properties for.
            attributes: An array of System.Attribute objects that describe the properties.
            Returns: The set of properties that are exposed for this data type. If no properties are exposed, this 
             method might return null. The default implementation always returns null.
        """
        pass

    def GetPropertiesSupported(self, context=None):
        """
        GetPropertiesSupported(self: PointConverter, context: ITypeDescriptorContext) -> bool
        
            Determines if this object supports properties. By default, this is false.
        
            context: A System.ComponentModel.TypeDescriptor through which additional context can be provided.
            Returns: true if 
             System.Drawing.PointConverter.GetProperties(System.ComponentModel.ITypeDescriptorContext,System.O
             bject,System.Attribute[]) should be called to find the properties of this object; otherwise, 
             false.
        """
        pass


class PointF(object):
    """
    Represents an ordered pair of floating-point x- and y-coordinates that defines a point in a two-dimensional plane.
    
    PointF(x: Single, y: Single)
    """
    @staticmethod
    def Add(pt, sz):
        """
        Add(pt: PointF, sz: SizeF) -> PointF
        
            Translates a given System.Drawing.PointF by a specified System.Drawing.SizeF.
        
            pt: The System.Drawing.PointF to translate.
            sz: The System.Drawing.SizeF that specifies the numbers to add to the coordinates of pt.
            Returns: The translated System.Drawing.PointF.
        Add(pt: PointF, sz: Size) -> PointF
        
            Translates a given System.Drawing.PointF by the specified System.Drawing.Size.
        
            pt: The System.Drawing.PointF to translate.
            sz: The System.Drawing.Size that specifies the numbers to add to the coordinates of pt.
            Returns: The translated System.Drawing.PointF.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PointF, obj: object) -> bool
        
            Specifies whether this System.Drawing.PointF contains the same coordinates as the specified 
             System.Object.
        
        
            obj: The System.Object to test.
            Returns: This method returns true if obj is a System.Drawing.PointF and has the same coordinates as this 
             System.Drawing.Point.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PointF) -> int
        
            Returns a hash code for this System.Drawing.PointF structure.
            Returns: An integer value that specifies a hash value for this System.Drawing.PointF structure.
        """
        pass

    @staticmethod
    def Subtract(pt, sz):
        """
        Subtract(pt: PointF, sz: SizeF) -> PointF
        
            Translates a System.Drawing.PointF by the negative of a specified size.
        
            pt: The System.Drawing.PointF to translate.
            sz: The System.Drawing.SizeF that specifies the numbers to subtract from the coordinates of pt.
            Returns: The translated System.Drawing.PointF.
        Subtract(pt: PointF, sz: Size) -> PointF
        
            Translates a System.Drawing.PointF by the negative of a specified size.
        
            pt: The System.Drawing.PointF to translate.
            sz: The System.Drawing.Size that specifies the numbers to subtract from the coordinates of pt.
            Returns: The translated System.Drawing.PointF.
        """
        pass

    def ToString(self):
        """
        ToString(self: PointF) -> str
        
            Converts this System.Drawing.PointF to a human readable string.
            Returns: A string that represents this System.Drawing.PointF.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, x, y):
        """
        __new__[PointF]() -> PointF
        
        __new__(cls: type, x: Single, y: Single)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this System.Drawing.PointF is empty.

Get: IsEmpty(self: PointF) -> bool

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate of this System.Drawing.PointF.

Get: X(self: PointF) -> Single

Set: X(self: PointF) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate of this System.Drawing.PointF.

Get: Y(self: PointF) -> Single

Set: Y(self: PointF) = value
"""


    Empty = None


class Rectangle(object):
    """
    Stores a set of four integers that represent the location and size of a rectangle
    
    Rectangle(x: int, y: int, width: int, height: int)
    Rectangle(location: Point, size: Size)
    """
    @staticmethod
    def Ceiling(value):
        """
        Ceiling(value: RectangleF) -> Rectangle
        
            Converts the specified System.Drawing.RectangleF structure to a System.Drawing.Rectangle 
             structure by rounding the System.Drawing.RectangleF values to the next higher integer values.
        
        
            value: The System.Drawing.RectangleF structure to be converted.
            Returns: Returns a System.Drawing.Rectangle.
        """
        pass

    def Contains(self, *__args):
        """
        Contains(self: Rectangle, rect: Rectangle) -> bool
        
            Determines if the rectangular region represented by rect is entirely contained within this 
             System.Drawing.Rectangle structure.
        
        
            rect: The System.Drawing.Rectangle to test.
            Returns: This method returns true if the rectangular region represented by rect is entirely contained 
             within this System.Drawing.Rectangle structure; otherwise false.
        
        Contains(self: Rectangle, pt: Point) -> bool
        
            Determines if the specified point is contained within this System.Drawing.Rectangle structure.
        
            pt: The System.Drawing.Point to test.
            Returns: This method returns true if the point represented by pt is contained within this 
             System.Drawing.Rectangle structure; otherwise false.
        
        Contains(self: Rectangle, x: int, y: int) -> bool
        
            Determines if the specified point is contained within this System.Drawing.Rectangle structure.
        
            x: The x-coordinate of the point to test.
            y: The y-coordinate of the point to test.
            Returns: This method returns true if the point defined by x and y is contained within this 
             System.Drawing.Rectangle structure; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Rectangle, obj: object) -> bool
        
            Tests whether obj is a System.Drawing.Rectangle structure with the same location and size of 
             this System.Drawing.Rectangle structure.
        
        
            obj: The System.Object to test.
            Returns: This method returns true if obj is a System.Drawing.Rectangle structure and its 
             System.Drawing.Rectangle.X, System.Drawing.Rectangle.Y, System.Drawing.Rectangle.Width, and 
             System.Drawing.Rectangle.Height properties are equal to the corresponding properties of this 
             System.Drawing.Rectangle structure; otherwise, false.
        """
        pass

    @staticmethod
    def FromLTRB(left, top, right, bottom):
        """
        FromLTRB(left: int, top: int, right: int, bottom: int) -> Rectangle
        
            Creates a System.Drawing.Rectangle structure with the specified edge locations.
        
            left: The x-coordinate of the upper-left corner of this System.Drawing.Rectangle structure.
            top: The y-coordinate of the upper-left corner of this System.Drawing.Rectangle structure.
            right: The x-coordinate of the lower-right corner of this System.Drawing.Rectangle structure.
            bottom: The y-coordinate of the lower-right corner of this System.Drawing.Rectangle structure.
            Returns: The new System.Drawing.Rectangle that this method creates.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Rectangle) -> int
        
            Returns the hash code for this System.Drawing.Rectangle structure. For information about the use 
             of hash codes, see System.Object.GetHashCode .
        
            Returns: An integer that represents the hash code for this rectangle.
        """
        pass

    def Inflate(self, *__args):
        """
        Inflate(rect: Rectangle, x: int, y: int) -> Rectangle
        
            Creates and returns an enlarged copy of the specified System.Drawing.Rectangle structure. The 
             copy is enlarged by the specified amount. The original System.Drawing.Rectangle structure 
             remains unmodified.
        
        
            rect: The System.Drawing.Rectangle with which to start. This rectangle is not modified.
            x: The amount to inflate this System.Drawing.Rectangle horizontally.
            y: The amount to inflate this System.Drawing.Rectangle vertically.
            Returns: The enlarged System.Drawing.Rectangle.
        Inflate(self: Rectangle, size: Size)
            Enlarges this System.Drawing.Rectangle by the specified amount.
        
            size: The amount to inflate this rectangle.
        Inflate(self: Rectangle, width: int, height: int)
            Enlarges this System.Drawing.Rectangle by the specified amount.
        
            width: The amount to inflate this System.Drawing.Rectangle horizontally.
            height: The amount to inflate this System.Drawing.Rectangle vertically.
        """
        pass

    def Intersect(self, *__args):
        """
        Intersect(a: Rectangle, b: Rectangle) -> Rectangle
        
            Returns a third System.Drawing.Rectangle structure that represents the intersection of two other 
             System.Drawing.Rectangle structures. If there is no intersection, an empty 
             System.Drawing.Rectangle is returned.
        
        
            a: A rectangle to intersect.
            b: A rectangle to intersect.
            Returns: A System.Drawing.Rectangle that represents the intersection of a and b.
        Intersect(self: Rectangle, rect: Rectangle)
            Replaces this System.Drawing.Rectangle with the intersection of itself and the specified 
             System.Drawing.Rectangle.
        
        
            rect: The System.Drawing.Rectangle with which to intersect.
        """
        pass

    def IntersectsWith(self, rect):
        """
        IntersectsWith(self: Rectangle, rect: Rectangle) -> bool
        
            Determines if this rectangle intersects with rect.
        
            rect: The rectangle to test.
            Returns: This method returns true if there is any intersection, otherwise false.
        """
        pass

    def Offset(self, *__args):
        """
        Offset(self: Rectangle, x: int, y: int)
            Adjusts the location of this rectangle by the specified amount.
        
            x: The horizontal offset.
            y: The vertical offset.
        Offset(self: Rectangle, pos: Point)
            Adjusts the location of this rectangle by the specified amount.
        
            pos: Amount to offset the location.
        """
        pass

    @staticmethod
    def Round(value):
        """
        Round(value: RectangleF) -> Rectangle
        
            Converts the specified System.Drawing.RectangleF to a System.Drawing.Rectangle by rounding the 
             System.Drawing.RectangleF values to the nearest integer values.
        
        
            value: The System.Drawing.RectangleF to be converted.
            Returns: A System.Drawing.Rectangle.
        """
        pass

    def ToString(self):
        """
        ToString(self: Rectangle) -> str
        
            Converts the attributes of this System.Drawing.Rectangle to a human-readable string.
            Returns: A string that contains the position, width, and height of this System.Drawing.Rectangle 
             structure � for example, {X=20, Y=20, Width=100, Height=50}
        """
        pass

    @staticmethod
    def Truncate(value):
        """
        Truncate(value: RectangleF) -> Rectangle
        
            Converts the specified System.Drawing.RectangleF to a System.Drawing.Rectangle by truncating the 
             System.Drawing.RectangleF values.
        
        
            value: The System.Drawing.RectangleF to be converted.
            Returns: A System.Drawing.Rectangle.
        """
        pass

    @staticmethod
    def Union(a, b):
        """
        Union(a: Rectangle, b: Rectangle) -> Rectangle
        
            Gets a System.Drawing.Rectangle structure that contains the union of two 
             System.Drawing.Rectangle structures.
        
        
            a: A rectangle to union.
            b: A rectangle to union.
            Returns: A System.Drawing.Rectangle structure that bounds the union of the two System.Drawing.Rectangle 
             structures.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Rectangle]() -> Rectangle
        
        __new__(cls: type, x: int, y: int, width: int, height: int)
        __new__(cls: type, location: Point, size: Size)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Bottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the y-coordinate that is the sum of the System.Drawing.Rectangle.Y and System.Drawing.Rectangle.Height property values of this System.Drawing.Rectangle structure.

Get: Bottom(self: Rectangle) -> int

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height of this System.Drawing.Rectangle structure.

Get: Height(self: Rectangle) -> int

Set: Height(self: Rectangle) = value
"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tests whether all numeric properties of this System.Drawing.Rectangle have values of zero.

Get: IsEmpty(self: Rectangle) -> bool

"""

    Left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the x-coordinate of the left edge of this System.Drawing.Rectangle structure.

Get: Left(self: Rectangle) -> int

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the coordinates of the upper-left corner of this System.Drawing.Rectangle structure.

Get: Location(self: Rectangle) -> Point

Set: Location(self: Rectangle) = value
"""

    Right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the x-coordinate that is the sum of System.Drawing.Rectangle.X and System.Drawing.Rectangle.Width property values of this System.Drawing.Rectangle structure.

Get: Right(self: Rectangle) -> int

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size of this System.Drawing.Rectangle.

Get: Size(self: Rectangle) -> Size

Set: Size(self: Rectangle) = value
"""

    Top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the y-coordinate of the top edge of this System.Drawing.Rectangle structure.

Get: Top(self: Rectangle) -> int

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the width of this System.Drawing.Rectangle structure.

Get: Width(self: Rectangle) -> int

Set: Width(self: Rectangle) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate of the upper-left corner of this System.Drawing.Rectangle structure.

Get: X(self: Rectangle) -> int

Set: X(self: Rectangle) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate of the upper-left corner of this System.Drawing.Rectangle structure.

Get: Y(self: Rectangle) -> int

Set: Y(self: Rectangle) = value
"""


    Empty = None


class RectangleConverter(TypeConverter):
    """
    Converts rectangles from one data type to another. Access this class through the System.ComponentModel.TypeDescriptor.
    
    RectangleConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: RectangleConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines if this converter can convert an object in the given source type to the native type 
             of the converter.
        
        
            context: A formatter context. This object can be used to get additional information about the environment 
             this converter is being called from. This may be null, so you should always check. Also, 
             properties on the context object may also return null.
        
            sourceType: The type you want to convert from.
            Returns: This method returns true if this object can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: RectangleConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object to the given destination 
             type using the context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext object that provides a format context. This can 
             be null, so you should always check. Also, properties on the context object can also return 
             null.
        
            destinationType: A System.Type object that represents the type you want to convert to.
            Returns: This method returns true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: RectangleConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the given object to a System.Drawing.Rectangle object.
        
            context: A System.ComponentModel.ITypeDescriptorContext that can be used to get additional information 
             about the environment this converter is being called from. This may be null, so you should 
             always check. Also, properties on the context object may also return null.
        
            culture: An System.Globalization.CultureInfo that contains culture specific information, such as the 
             language, calendar, and cultural conventions associated with a specific culture. It is based on 
             the RFC 1766 standard.
        
            value: The object to convert.
            Returns: The converted object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: RectangleConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified object to the specified type.
        
            context: A System.ComponentModel.ITypeDescriptorContext that can be used to get additional information 
             about the environment this converter is being called from. This may be null, so you should 
             always check. Also, properties on the context object may also return null.
        
            culture: An System.Globalization.CultureInfo that contains culture specific information, such as the 
             language, calendar, and cultural conventions associated with a specific culture. It is based on 
             the RFC 1766 standard.
        
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object.
        """
        pass

    def CreateInstance(self, *__args):
        """
        CreateInstance(self: RectangleConverter, context: ITypeDescriptorContext, propertyValues: IDictionary) -> object
        
            Creates an instance of this type given a set of property values for the object. This is useful 
             for objects that are immutable but still want to provide changeable properties.
        
        
            context: A System.ComponentModel.ITypeDescriptorContext through which additional context can be provided.
            propertyValues: A dictionary of new property values. The dictionary contains a series of name-value pairs, one 
             for each property returned from a call to the 
             System.Drawing.RectangleConverter.GetProperties(System.ComponentModel.ITypeDescriptorContext,Syst
             em.Object,System.Attribute[]) method.
        
            Returns: The newly created object, or null if the object could not be created. The default implementation 
             returns null.
        """
        pass

    def GetCreateInstanceSupported(self, context=None):
        """
        GetCreateInstanceSupported(self: RectangleConverter, context: ITypeDescriptorContext) -> bool
        
            Determines if changing a value on this object should require a call to 
             System.Drawing.RectangleConverter.CreateInstance(System.ComponentModel.ITypeDescriptorContext,Sys
             tem.Collections.IDictionary) to create a new value.
        
        
            context: A type descriptor through which additional context can be provided.
            Returns: This method returns true if 
             System.Drawing.RectangleConverter.CreateInstance(System.ComponentModel.ITypeDescriptorContext,Sys
             tem.Collections.IDictionary) should be called when a change is made to one or more properties of 
             this object; otherwise, false.
        """
        pass

    def GetProperties(self, *__args):
        """
        GetProperties(self: RectangleConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Retrieves the set of properties for this type. By default, a type does not return any properties.
        
            context: A System.ComponentModel.ITypeDescriptorContext through which additional context can be provided.
            value: The value of the object to get the properties for.
            attributes: An array of System.Attribute objects that describe the properties.
            Returns: The set of properties that should be exposed for this data type. If no properties should be 
             exposed, this may return null. The default implementation always returns null.
        """
        pass

    def GetPropertiesSupported(self, context=None):
        """
        GetPropertiesSupported(self: RectangleConverter, context: ITypeDescriptorContext) -> bool
        
            Determines if this object supports properties. By default, this is false.
        
            context: A System.ComponentModel.ITypeDescriptorContext through which additional context can be provided.
            Returns: This method returns true if 
             System.Drawing.RectangleConverter.GetProperties(System.ComponentModel.ITypeDescriptorContext,Syst
             em.Object,System.Attribute[]) should be called to find the properties of this object; otherwise, 
             false.
        """
        pass


class RectangleF(object):
    """
    Stores a set of four floating-point numbers that represent the location and size of a rectangle. For more advanced region functions, use a System.Drawing.Region object.
    
    RectangleF(x: Single, y: Single, width: Single, height: Single)
    RectangleF(location: PointF, size: SizeF)
    """
    def Contains(self, *__args):
        """
        Contains(self: RectangleF, rect: RectangleF) -> bool
        
            Determines if the rectangular region represented by rect is entirely contained within this 
             System.Drawing.RectangleF structure.
        
        
            rect: The System.Drawing.RectangleF to test.
            Returns: This method returns true if the rectangular region represented by rect is entirely contained 
             within the rectangular region represented by this System.Drawing.RectangleF; otherwise false.
        
        Contains(self: RectangleF, pt: PointF) -> bool
        
            Determines if the specified point is contained within this System.Drawing.RectangleF structure.
        
            pt: The System.Drawing.PointF to test.
            Returns: This method returns true if the point represented by the pt parameter is contained within this 
             System.Drawing.RectangleF structure; otherwise false.
        
        Contains(self: RectangleF, x: Single, y: Single) -> bool
        
            Determines if the specified point is contained within this System.Drawing.RectangleF structure.
        
            x: The x-coordinate of the point to test.
            y: The y-coordinate of the point to test.
            Returns: This method returns true if the point defined by x and y is contained within this 
             System.Drawing.RectangleF structure; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: RectangleF, obj: object) -> bool
        
            Tests whether obj is a System.Drawing.RectangleF with the same location and size of this 
             System.Drawing.RectangleF.
        
        
            obj: The System.Object to test.
            Returns: This method returns true if obj is a System.Drawing.RectangleF and its X, Y, Width, and Height 
             properties are equal to the corresponding properties of this System.Drawing.RectangleF; 
             otherwise, false.
        """
        pass

    @staticmethod
    def FromLTRB(left, top, right, bottom):
        """
        FromLTRB(left: Single, top: Single, right: Single, bottom: Single) -> RectangleF
        
            Creates a System.Drawing.RectangleF structure with upper-left corner and lower-right corner at 
             the specified locations.
        
        
            left: The x-coordinate of the upper-left corner of the rectangular region.
            top: The y-coordinate of the upper-left corner of the rectangular region.
            right: The x-coordinate of the lower-right corner of the rectangular region.
            bottom: The y-coordinate of the lower-right corner of the rectangular region.
            Returns: The new System.Drawing.RectangleF that this method creates.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: RectangleF) -> int
        
            Gets the hash code for this System.Drawing.RectangleF structure. For information about the use 
             of hash codes, see Object.GetHashCode.
        
            Returns: The hash code for this System.Drawing.RectangleF.
        """
        pass

    def Inflate(self, *__args):
        """
        Inflate(rect: RectangleF, x: Single, y: Single) -> RectangleF
        
            Creates and returns an enlarged copy of the specified System.Drawing.RectangleF structure. The 
             copy is enlarged by the specified amount and the original rectangle remains unmodified.
        
        
            rect: The System.Drawing.RectangleF to be copied. This rectangle is not modified.
            x: The amount to enlarge the copy of the rectangle horizontally.
            y: The amount to enlarge the copy of the rectangle vertically.
            Returns: The enlarged System.Drawing.RectangleF.
        Inflate(self: RectangleF, size: SizeF)
            Enlarges this System.Drawing.RectangleF by the specified amount.
        
            size: The amount to inflate this rectangle.
        Inflate(self: RectangleF, x: Single, y: Single)
            Enlarges this System.Drawing.RectangleF structure by the specified amount.
        
            x: The amount to inflate this System.Drawing.RectangleF structure horizontally.
            y: The amount to inflate this System.Drawing.RectangleF structure vertically.
        """
        pass

    def Intersect(self, *__args):
        """
        Intersect(a: RectangleF, b: RectangleF) -> RectangleF
        
            Returns a System.Drawing.RectangleF structure that represents the intersection of two 
             rectangles. If there is no intersection, and empty System.Drawing.RectangleF is returned.
        
        
            a: A rectangle to intersect.
            b: A rectangle to intersect.
            Returns: A third System.Drawing.RectangleF structure the size of which represents the overlapped area of 
             the two specified rectangles.
        
        Intersect(self: RectangleF, rect: RectangleF)
            Replaces this System.Drawing.RectangleF structure with the intersection of itself and the 
             specified System.Drawing.RectangleF structure.
        
        
            rect: The rectangle to intersect.
        """
        pass

    def IntersectsWith(self, rect):
        """
        IntersectsWith(self: RectangleF, rect: RectangleF) -> bool
        
            Determines if this rectangle intersects with rect.
        
            rect: The rectangle to test.
            Returns: This method returns true if there is any intersection.
        """
        pass

    def Offset(self, *__args):
        """
        Offset(self: RectangleF, x: Single, y: Single)
            Adjusts the location of this rectangle by the specified amount.
        
            x: The amount to offset the location horizontally.
            y: The amount to offset the location vertically.
        Offset(self: RectangleF, pos: PointF)
            Adjusts the location of this rectangle by the specified amount.
        
            pos: The amount to offset the location.
        """
        pass

    def ToString(self):
        """
        ToString(self: RectangleF) -> str
        
            Converts the Location and System.Drawing.Size of this System.Drawing.RectangleF to a 
             human-readable string.
        
            Returns: A string that contains the position, width, and height of this System.Drawing.RectangleF 
             structure. For example, "{X=20, Y=20, Width=100, Height=50}".
        """
        pass

    @staticmethod
    def Union(a, b):
        """
        Union(a: RectangleF, b: RectangleF) -> RectangleF
        
            Creates the smallest possible third rectangle that can contain both of two rectangles that form 
             a union.
        
        
            a: A rectangle to union.
            b: A rectangle to union.
            Returns: A third System.Drawing.RectangleF structure that contains both of the two rectangles that form 
             the union.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[RectangleF]() -> RectangleF
        
        __new__(cls: type, x: Single, y: Single, width: Single, height: Single)
        __new__(cls: type, location: PointF, size: SizeF)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Bottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the y-coordinate that is the sum of System.Drawing.RectangleF.Y and System.Drawing.RectangleF.Height of this System.Drawing.RectangleF structure.

Get: Bottom(self: RectangleF) -> Single

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height of this System.Drawing.RectangleF structure.

Get: Height(self: RectangleF) -> Single

Set: Height(self: RectangleF) = value
"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tests whether the System.Drawing.RectangleF.Width or System.Drawing.RectangleF.Height property of this System.Drawing.RectangleF has a value of zero.

Get: IsEmpty(self: RectangleF) -> bool

"""

    Left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the x-coordinate of the left edge of this System.Drawing.RectangleF structure.

Get: Left(self: RectangleF) -> Single

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the coordinates of the upper-left corner of this System.Drawing.RectangleF structure.

Get: Location(self: RectangleF) -> PointF

Set: Location(self: RectangleF) = value
"""

    Right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the x-coordinate that is the sum of System.Drawing.RectangleF.X and System.Drawing.RectangleF.Width of this System.Drawing.RectangleF structure.

Get: Right(self: RectangleF) -> Single

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size of this System.Drawing.RectangleF.

Get: Size(self: RectangleF) -> SizeF

Set: Size(self: RectangleF) = value
"""

    Top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the y-coordinate of the top edge of this System.Drawing.RectangleF structure.

Get: Top(self: RectangleF) -> Single

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the width of this System.Drawing.RectangleF structure.

Get: Width(self: RectangleF) -> Single

Set: Width(self: RectangleF) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate of the upper-left corner of this System.Drawing.RectangleF structure.

Get: X(self: RectangleF) -> Single

Set: X(self: RectangleF) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate of the upper-left corner of this System.Drawing.RectangleF structure.

Get: Y(self: RectangleF) -> Single

Set: Y(self: RectangleF) = value
"""


    Empty = None


class Region(MarshalByRefObject, IDisposable):
    """
    Describes the interior of a graphics shape composed of rectangles and paths. This class cannot be inherited.
    
    Region()
    Region(rect: Rectangle)
    Region(path: GraphicsPath)
    Region(rect: RectangleF)
    Region(rgnData: RegionData)
    """
    def Clone(self):
        """
        Clone(self: Region) -> Region
        
            Creates an exact copy of this System.Drawing.Region.
            Returns: The System.Drawing.Region that this method creates.
        """
        pass

    def Complement(self, *__args):
        """
        Complement(self: Region, path: GraphicsPath)
            Updates this System.Drawing.Region to contain the portion of the specified 
             System.Drawing.Drawing2D.GraphicsPath that does not intersect with this System.Drawing.Region.
        
        
            path: The System.Drawing.Drawing2D.GraphicsPath to complement this System.Drawing.Region.
        Complement(self: Region, region: Region)
            Updates this System.Drawing.Region to contain the portion of the specified System.Drawing.Region 
             that does not intersect with this System.Drawing.Region.
        
        
            region: The System.Drawing.Region object to complement this System.Drawing.Region object.
        Complement(self: Region, rect: RectangleF)
            Updates this System.Drawing.Region to contain the portion of the specified 
             System.Drawing.RectangleF structure that does not intersect with this System.Drawing.Region.
        
        
            rect: The System.Drawing.RectangleF structure to complement this System.Drawing.Region.
        Complement(self: Region, rect: Rectangle)
            Updates this System.Drawing.Region to contain the portion of the specified 
             System.Drawing.Rectangle structure that does not intersect with this System.Drawing.Region.
        
        
            rect: The System.Drawing.Rectangle structure to complement this System.Drawing.Region.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Region)
            Releases all resources used by this System.Drawing.Region.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Region, region: Region, g: Graphics) -> bool
        
            Tests whether the specified System.Drawing.Region is identical to this System.Drawing.Region on 
             the specified drawing surface.
        
        
            region: The System.Drawing.Region to test.
            g: A System.Drawing.Graphics that represents a drawing surface.
            Returns: true if the interior of region is identical to the interior of this region when the 
             transformation associated with the g parameter is applied; otherwise, false.
        """
        pass

    def Exclude(self, *__args):
        """
        Exclude(self: Region, path: GraphicsPath)
            Updates this System.Drawing.Region to contain only the portion of its interior that does not 
             intersect with the specified System.Drawing.Drawing2D.GraphicsPath.
        
        
            path: The System.Drawing.Drawing2D.GraphicsPath to exclude from this System.Drawing.Region.
        Exclude(self: Region, region: Region)
            Updates this System.Drawing.Region to contain only the portion of its interior that does not 
             intersect with the specified System.Drawing.Region.
        
        
            region: The System.Drawing.Region to exclude from this System.Drawing.Region.
        Exclude(self: Region, rect: Rectangle)
            Updates this System.Drawing.Region to contain only the portion of its interior that does not 
             intersect with the specified System.Drawing.Rectangle structure.
        
        
            rect: The System.Drawing.Rectangle structure to exclude from this System.Drawing.Region.
        Exclude(self: Region, rect: RectangleF)
            Updates this System.Drawing.Region to contain only the portion of its interior that does not 
             intersect with the specified System.Drawing.RectangleF structure.
        
        
            rect: The System.Drawing.RectangleF structure to exclude from this System.Drawing.Region.
        """
        pass

    @staticmethod
    def FromHrgn(hrgn):
        """
        FromHrgn(hrgn: IntPtr) -> Region
        
            Initializes a new System.Drawing.Region from a handle to the specified existing GDI region.
        
            hrgn: A handle to an existing System.Drawing.Region.
            Returns: The new System.Drawing.Region.
        """
        pass

    def GetBounds(self, g):
        """
        GetBounds(self: Region, g: Graphics) -> RectangleF
        
            Gets a System.Drawing.RectangleF structure that represents a rectangle that bounds this 
             System.Drawing.Region on the drawing surface of a System.Drawing.Graphics object.
        
        
            g: The System.Drawing.Graphics on which this System.Drawing.Region is drawn.
            Returns: A System.Drawing.RectangleF structure that represents the bounding rectangle for this 
             System.Drawing.Region on the specified drawing surface.
        """
        pass

    def GetHrgn(self, g):
        """
        GetHrgn(self: Region, g: Graphics) -> IntPtr
        
            Returns a Windows handle to this System.Drawing.Region in the specified graphics context.
        
            g: The System.Drawing.Graphics on which this System.Drawing.Region is drawn.
            Returns: A Windows handle to this System.Drawing.Region.
        """
        pass

    def GetRegionData(self):
        """
        GetRegionData(self: Region) -> RegionData
        
            Returns a System.Drawing.Drawing2D.RegionData that represents the information that describes 
             this System.Drawing.Region.
        
            Returns: A System.Drawing.Drawing2D.RegionData that represents the information that describes this 
             System.Drawing.Region.
        """
        pass

    def GetRegionScans(self, matrix):
        """
        GetRegionScans(self: Region, matrix: Matrix) -> Array[RectangleF]
        
            Returns an array of System.Drawing.RectangleF structures that approximate this 
             System.Drawing.Region after the specified matrix transformation is applied.
        
        
            matrix: A System.Drawing.Drawing2D.Matrix that represents a geometric transformation to apply to the 
             region.
        
            Returns: An array of System.Drawing.RectangleF structures that approximate this System.Drawing.Region 
             after the specified matrix transformation is applied.
        """
        pass

    def Intersect(self, *__args):
        """
        Intersect(self: Region, rect: Rectangle)
            Updates this System.Drawing.Region to the intersection of itself with the specified 
             System.Drawing.Rectangle structure.
        
        
            rect: The System.Drawing.Rectangle structure to intersect with this System.Drawing.Region.
        Intersect(self: Region, path: GraphicsPath)
            Updates this System.Drawing.Region to the intersection of itself with the specified 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            path: The System.Drawing.Drawing2D.GraphicsPath to intersect with this System.Drawing.Region.
        Intersect(self: Region, region: Region)
            Updates this System.Drawing.Region to the intersection of itself with the specified 
             System.Drawing.Region.
        
        
            region: The System.Drawing.Region to intersect with this System.Drawing.Region.
        Intersect(self: Region, rect: RectangleF)
            Updates this System.Drawing.Region to the intersection of itself with the specified 
             System.Drawing.RectangleF structure.
        
        
            rect: The System.Drawing.RectangleF structure to intersect with this System.Drawing.Region.
        """
        pass

    def IsEmpty(self, g):
        """
        IsEmpty(self: Region, g: Graphics) -> bool
        
            Tests whether this System.Drawing.Region has an empty interior on the specified drawing surface.
        
            g: A System.Drawing.Graphics that represents a drawing surface.
            Returns: true if the interior of this System.Drawing.Region is empty when the transformation associated 
             with g is applied; otherwise, false.
        """
        pass

    def IsInfinite(self, g):
        """
        IsInfinite(self: Region, g: Graphics) -> bool
        
            Tests whether this System.Drawing.Region has an infinite interior on the specified drawing 
             surface.
        
        
            g: A System.Drawing.Graphics that represents a drawing surface.
            Returns: true if the interior of this System.Drawing.Region is infinite when the transformation 
             associated with g is applied; otherwise, false.
        """
        pass

    def IsVisible(self, *__args):
        """
        IsVisible(self: Region, point: Point, g: Graphics) -> bool
        
            Tests whether the specified System.Drawing.Point structure is contained within this 
             System.Drawing.Region when drawn using the specified System.Drawing.Graphics.
        
        
            point: The System.Drawing.Point structure to test.
            g: A System.Drawing.Graphics that represents a graphics context.
            Returns: true when point is contained within this System.Drawing.Region; otherwise, false.
        IsVisible(self: Region, point: Point) -> bool
        
            Tests whether the specified System.Drawing.Point structure is contained within this 
             System.Drawing.Region.
        
        
            point: The System.Drawing.Point structure to test.
            Returns: true when point is contained within this System.Drawing.Region; otherwise, false.
        IsVisible(self: Region, x: int, y: int, g: Graphics) -> bool
        
            Tests whether the specified point is contained within this System.Drawing.Region object when 
             drawn using the specified System.Drawing.Graphics object.
        
        
            x: The x-coordinate of the point to test.
            y: The y-coordinate of the point to test.
            g: A System.Drawing.Graphics that represents a graphics context.
            Returns: true when the specified point is contained within this System.Drawing.Region; otherwise, false.
        IsVisible(self: Region, x: int, y: int, width: int, height: int) -> bool
        
            Tests whether any portion of the specified rectangle is contained within this 
             System.Drawing.Region.
        
        
            x: The x-coordinate of the upper-left corner of the rectangle to test.
            y: The y-coordinate of the upper-left corner of the rectangle to test.
            width: The width of the rectangle to test.
            height: The height of the rectangle to test.
            Returns: true when any portion of the specified rectangle is contained within this System.Drawing.Region; 
             otherwise, false.
        
        IsVisible(self: Region, rect: Rectangle, g: Graphics) -> bool
        
            Tests whether any portion of the specified System.Drawing.Rectangle structure is contained 
             within this System.Drawing.Region when drawn using the specified System.Drawing.Graphics.
        
        
            rect: The System.Drawing.Rectangle structure to test.
            g: A System.Drawing.Graphics that represents a graphics context.
            Returns: true when any portion of the rect is contained within this System.Drawing.Region; otherwise, 
             false.
        
        IsVisible(self: Region, x: int, y: int, width: int, height: int, g: Graphics) -> bool
        
            Tests whether any portion of the specified rectangle is contained within this 
             System.Drawing.Region when drawn using the specified System.Drawing.Graphics.
        
        
            x: The x-coordinate of the upper-left corner of the rectangle to test.
            y: The y-coordinate of the upper-left corner of the rectangle to test.
            width: The width of the rectangle to test.
            height: The height of the rectangle to test.
            g: A System.Drawing.Graphics that represents a graphics context.
            Returns: true when any portion of the specified rectangle is contained within this System.Drawing.Region; 
             otherwise, false.
        
        IsVisible(self: Region, rect: Rectangle) -> bool
        
            Tests whether any portion of the specified System.Drawing.Rectangle structure is contained 
             within this System.Drawing.Region.
        
        
            rect: The System.Drawing.Rectangle structure to test.
            Returns: This method returns true when any portion of rect is contained within this 
             System.Drawing.Region; otherwise, false.
        
        IsVisible(self: Region, rect: RectangleF, g: Graphics) -> bool
        
            Tests whether any portion of the specified System.Drawing.RectangleF structure is contained 
             within this System.Drawing.Region when drawn using the specified System.Drawing.Graphics.
        
        
            rect: The System.Drawing.RectangleF structure to test.
            g: A System.Drawing.Graphics that represents a graphics context.
            Returns: true when rect is contained within this System.Drawing.Region; otherwise, false.
        IsVisible(self: Region, x: Single, y: Single, g: Graphics) -> bool
        
            Tests whether the specified point is contained within this System.Drawing.Region when drawn 
             using the specified System.Drawing.Graphics.
        
        
            x: The x-coordinate of the point to test.
            y: The y-coordinate of the point to test.
            g: A System.Drawing.Graphics that represents a graphics context.
            Returns: true when the specified point is contained within this System.Drawing.Region; otherwise, false.
        IsVisible(self: Region, point: PointF) -> bool
        
            Tests whether the specified System.Drawing.PointF structure is contained within this 
             System.Drawing.Region.
        
        
            point: The System.Drawing.PointF structure to test.
            Returns: true when point is contained within this System.Drawing.Region; otherwise, false.
        IsVisible(self: Region, x: Single, y: Single) -> bool
        
            Tests whether the specified point is contained within this System.Drawing.Region.
        
            x: The x-coordinate of the point to test.
            y: The y-coordinate of the point to test.
            Returns: true when the specified point is contained within this System.Drawing.Region; otherwise, false.
        IsVisible(self: Region, point: PointF, g: Graphics) -> bool
        
            Tests whether the specified System.Drawing.PointF structure is contained within this 
             System.Drawing.Region when drawn using the specified System.Drawing.Graphics.
        
        
            point: The System.Drawing.PointF structure to test.
            g: A System.Drawing.Graphics that represents a graphics context.
            Returns: true when point is contained within this System.Drawing.Region; otherwise, false.
        IsVisible(self: Region, x: Single, y: Single, width: Single, height: Single, g: Graphics) -> bool
        
            Tests whether any portion of the specified rectangle is contained within this 
             System.Drawing.Region when drawn using the specified System.Drawing.Graphics.
        
        
            x: The x-coordinate of the upper-left corner of the rectangle to test.
            y: The y-coordinate of the upper-left corner of the rectangle to test.
            width: The width of the rectangle to test.
            height: The height of the rectangle to test.
            g: A System.Drawing.Graphics that represents a graphics context.
            Returns: true when any portion of the specified rectangle is contained within this System.Drawing.Region; 
             otherwise, false.
        
        IsVisible(self: Region, rect: RectangleF) -> bool
        
            Tests whether any portion of the specified System.Drawing.RectangleF structure is contained 
             within this System.Drawing.Region.
        
        
            rect: The System.Drawing.RectangleF structure to test.
            Returns: true when any portion of rect is contained within this System.Drawing.Region; otherwise, false.
        IsVisible(self: Region, x: Single, y: Single, width: Single, height: Single) -> bool
        
            Tests whether any portion of the specified rectangle is contained within this 
             System.Drawing.Region.
        
        
            x: The x-coordinate of the upper-left corner of the rectangle to test.
            y: The y-coordinate of the upper-left corner of the rectangle to test.
            width: The width of the rectangle to test.
            height: The height of the rectangle to test.
            Returns: true when any portion of the specified rectangle is contained within this System.Drawing.Region 
             object; otherwise, false.
        """
        pass

    def MakeEmpty(self):
        """
        MakeEmpty(self: Region)
            Initializes this System.Drawing.Region to an empty interior.
        """
        pass

    def MakeInfinite(self):
        """
        MakeInfinite(self: Region)
            Initializes this System.Drawing.Region object to an infinite interior.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def ReleaseHrgn(self, regionHandle):
        """
        ReleaseHrgn(self: Region, regionHandle: IntPtr)
            Releases the handle of the System.Drawing.Region.
        
            regionHandle: The handle to the System.Drawing.Region.
        """
        pass

    def Transform(self, matrix):
        """
        Transform(self: Region, matrix: Matrix)
            Transforms this System.Drawing.Region by the specified System.Drawing.Drawing2D.Matrix.
        
            matrix: The System.Drawing.Drawing2D.Matrix by which to transform this System.Drawing.Region.
        """
        pass

    def Translate(self, dx, dy):
        """
        Translate(self: Region, dx: int, dy: int)
            Offsets the coordinates of this System.Drawing.Region by the specified amount.
        
            dx: The amount to offset this System.Drawing.Region horizontally.
            dy: The amount to offset this System.Drawing.Region vertically.
        Translate(self: Region, dx: Single, dy: Single)
            Offsets the coordinates of this System.Drawing.Region by the specified amount.
        
            dx: The amount to offset this System.Drawing.Region horizontally.
            dy: The amount to offset this System.Drawing.Region vertically.
        """
        pass

    def Union(self, *__args):
        """
        Union(self: Region, path: GraphicsPath)
            Updates this System.Drawing.Region to the union of itself and the specified 
             System.Drawing.Drawing2D.GraphicsPath.
        
        
            path: The System.Drawing.Drawing2D.GraphicsPath to unite with this System.Drawing.Region.
        Union(self: Region, region: Region)
            Updates this System.Drawing.Region to the union of itself and the specified 
             System.Drawing.Region.
        
        
            region: The System.Drawing.Region to unite with this System.Drawing.Region.
        Union(self: Region, rect: Rectangle)
            Updates this System.Drawing.Region to the union of itself and the specified 
             System.Drawing.Rectangle structure.
        
        
            rect: The System.Drawing.Rectangle structure to unite with this System.Drawing.Region.
        Union(self: Region, rect: RectangleF)
            Updates this System.Drawing.Region to the union of itself and the specified 
             System.Drawing.RectangleF structure.
        
        
            rect: The System.Drawing.RectangleF structure to unite with this System.Drawing.Region.
        """
        pass

    def Xor(self, *__args):
        """
        Xor(self: Region, path: GraphicsPath)
            Updates this System.Drawing.Region to the union minus the intersection of itself with the 
             specified System.Drawing.Drawing2D.GraphicsPath.
        
        
            path: The System.Drawing.Drawing2D.GraphicsPath to erload:System.Drawing.Region.Xor with this 
             System.Drawing.Region.
        
        Xor(self: Region, region: Region)
            Updates this System.Drawing.Region to the union minus the intersection of itself with the 
             specified System.Drawing.Region.
        
        
            region: The System.Drawing.Region to erload:System.Drawing.Region.Xor with this System.Drawing.Region.
        Xor(self: Region, rect: RectangleF)
            Updates this System.Drawing.Region to the union minus the intersection of itself with the 
             specified System.Drawing.RectangleF structure.
        
        
            rect: The System.Drawing.RectangleF structure to 
             System.Drawing.Region.Xor(System.Drawing.Drawing2D.GraphicsPath) with this 
             System.Drawing.Region.
        
        Xor(self: Region, rect: Rectangle)
            Updates this System.Drawing.Region to the union minus the intersection of itself with the 
             specified System.Drawing.Rectangle structure.
        
        
            rect: The System.Drawing.Rectangle structure to erload:System.Drawing.Region.Xor with this 
             System.Drawing.Region.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, rect: RectangleF)
        __new__(cls: type, rect: Rectangle)
        __new__(cls: type, path: GraphicsPath)
        __new__(cls: type, rgnData: RegionData)
        """
        pass


class RotateFlipType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how much an image is rotated and the axis used to flip the image.
    
    enum RotateFlipType, values: Rotate180FlipNone (2), Rotate180FlipX (6), Rotate180FlipXY (0), Rotate180FlipY (4), Rotate270FlipNone (3), Rotate270FlipX (7), Rotate270FlipXY (1), Rotate270FlipY (5), Rotate90FlipNone (1), Rotate90FlipX (5), Rotate90FlipXY (3), Rotate90FlipY (7), RotateNoneFlipNone (0), RotateNoneFlipX (4), RotateNoneFlipXY (2), RotateNoneFlipY (6)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Rotate180FlipNone = None
    Rotate180FlipX = None
    Rotate180FlipXY = None
    Rotate180FlipY = None
    Rotate270FlipNone = None
    Rotate270FlipX = None
    Rotate270FlipXY = None
    Rotate270FlipY = None
    Rotate90FlipNone = None
    Rotate90FlipX = None
    Rotate90FlipXY = None
    Rotate90FlipY = None
    RotateNoneFlipNone = None
    RotateNoneFlipX = None
    RotateNoneFlipXY = None
    RotateNoneFlipY = None
    value__ = None


class Size(object):
    """
    Stores an ordered pair of integers, which specify a System.Drawing.Size.Height and System.Drawing.Size.Width.
    
    Size(pt: Point)
    Size(width: int, height: int)
    """
    @staticmethod
    def Add(sz1, sz2):
        """
        Add(sz1: Size, sz2: Size) -> Size
        
            Adds the width and height of one System.Drawing.Size structure to the width and height of 
             another System.Drawing.Size structure.
        
        
            sz1: The first System.Drawing.Size structure to add.
            sz2: The second System.Drawing.Size structure to add.
            Returns: A System.Drawing.Size structure that is the result of the addition operation.
        """
        pass

    @staticmethod
    def Ceiling(value):
        """
        Ceiling(value: SizeF) -> Size
        
            Converts the specified System.Drawing.SizeF structure to a System.Drawing.Size structure by 
             rounding the values of the System.Drawing.Size structure to the next higher integer values.
        
        
            value: The System.Drawing.SizeF structure to convert.
            Returns: The System.Drawing.Size structure this method converts to.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Size, obj: object) -> bool
        
            Tests to see whether the specified object is a System.Drawing.Size structure with the same 
             dimensions as this System.Drawing.Size structure.
        
        
            obj: The System.Object to test.
            Returns: true if obj is a System.Drawing.Size and has the same width and height as this 
             System.Drawing.Size; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Size) -> int
        
            Returns a hash code for this System.Drawing.Size structure.
            Returns: An integer value that specifies a hash value for this System.Drawing.Size structure.
        """
        pass

    @staticmethod
    def Round(value):
        """
        Round(value: SizeF) -> Size
        
            Converts the specified System.Drawing.SizeF structure to a System.Drawing.Size structure by 
             rounding the values of the System.Drawing.SizeF structure to the nearest integer values.
        
        
            value: The System.Drawing.SizeF structure to convert.
            Returns: The System.Drawing.Size structure this method converts to.
        """
        pass

    @staticmethod
    def Subtract(sz1, sz2):
        """
        Subtract(sz1: Size, sz2: Size) -> Size
        
            Subtracts the width and height of one System.Drawing.Size structure from the width and height of 
             another System.Drawing.Size structure.
        
        
            sz1: The System.Drawing.Size structure on the left side of the subtraction operator.
            sz2: The System.Drawing.Size structure on the right side of the subtraction operator.
            Returns: A System.Drawing.Size structure that is a result of the subtraction operation.
        """
        pass

    def ToString(self):
        """
        ToString(self: Size) -> str
        
            Creates a human-readable string that represents this System.Drawing.Size structure.
            Returns: A string that represents this System.Drawing.Size.
        """
        pass

    @staticmethod
    def Truncate(value):
        """
        Truncate(value: SizeF) -> Size
        
            Converts the specified System.Drawing.SizeF structure to a System.Drawing.Size structure by 
             truncating the values of the System.Drawing.SizeF structure to the next lower integer values.
        
        
            value: The System.Drawing.SizeF structure to convert.
            Returns: The System.Drawing.Size structure this method converts to.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Size]() -> Size
        
        __new__(cls: type, pt: Point)
        __new__(cls: type, width: int, height: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(sz1: Size, sz2: Size) -> Size
        
            Adds the width and height of one System.Drawing.Size structure to the width and height of 
             another System.Drawing.Size structure.
        
        
            sz1: The first System.Drawing.Size to add.
            sz2: The second System.Drawing.Size to add.
            Returns: A System.Drawing.Size structure that is the result of the addition operation.
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(sz1: Size, sz2: Size) -> Size
        
            Subtracts the width and height of one System.Drawing.Size structure from the width and height of 
             another System.Drawing.Size structure.
        
        
            sz1: The System.Drawing.Size structure on the left side of the subtraction operator.
            sz2: The System.Drawing.Size structure on the right side of the subtraction operator.
            Returns: A System.Drawing.Size structure that is the result of the subtraction operation.
        """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the vertical component of this System.Drawing.Size structure.

Get: Height(self: Size) -> int

Set: Height(self: Size) = value
"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tests whether this System.Drawing.Size structure has width and height of 0.

Get: IsEmpty(self: Size) -> bool

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the horizontal component of this System.Drawing.Size structure.

Get: Width(self: Size) -> int

Set: Width(self: Size) = value
"""


    Empty = None


class SizeConverter(TypeConverter):
    """
    The System.Drawing.SizeConverter class is used to convert from one data type to another. Access this class through the System.ComponentModel.TypeDescriptor object.
    
    SizeConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: SizeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether this converter can convert an object in the specified source type to the 
             native type of the converter.
        
        
            context: A System.ComponentModel.ITypeDescriptorContext that can be used to get additional information 
             about the environment this converter is being called from. This may be null, so you should 
             always check. Also, properties on the context object may also return null.
        
            sourceType: The type you want to convert from.
            Returns: This method returns true if this object can perform the conversion.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: SizeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Gets a value indicating whether this converter can convert an object to the given destination 
             type using the context.
        
        
            context: A System.ComponentModel.ITypeDescriptorContext that can be used to get additional information 
             about the environment this converter is being called from. This can be null, so always check. 
             Also, properties on the context object can return null.
        
            destinationType: A System.Type that represents the type you want to convert to.
            Returns: This method returns true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: SizeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the specified object to the converter's native type.
        
            context: A System.ComponentModel.ITypeDescriptorContext that can be used to get additional information 
             about the environment this converter is being called from. This may be null, so you should 
             always check. Also, properties on the context object may also return null.
        
            culture: An System.Globalization.CultureInfo object that contains culture specific information, such as 
             the language, calendar, and cultural conventions associated with a specific culture. It is based 
             on the RFC 1766 standard.
        
            value: The object to convert.
            Returns: The converted object.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: SizeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified object to the specified type.
        
            context: A System.ComponentModel.ITypeDescriptorContext that can be used to get additional information 
             about the environment this converter is being called from. This may be null, so you should 
             always check. Also, properties on the context object may also return null.
        
            culture: An System.Globalization.CultureInfo object that contains culture specific information, such as 
             the language, calendar, and cultural conventions associated with a specific culture. It is based 
             on the RFC 1766 standard.
        
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: The converted object.
        """
        pass

    def CreateInstance(self, *__args):
        """
        CreateInstance(self: SizeConverter, context: ITypeDescriptorContext, propertyValues: IDictionary) -> object
        
            Creates an object of this type by using a specified set of property values for the object. This 
             is useful for creating non-changeable objects that have changeable properties.
        
        
            context: A System.ComponentModel.TypeDescriptor through which additional context can be provided.
            propertyValues: A dictionary of new property values. The dictionary contains a series of name-value pairs, one 
             for each property returned from the 
             System.Drawing.SizeConverter.GetProperties(System.ComponentModel.ITypeDescriptorContext,System.Ob
             ject,System.Attribute[]) method.
        
            Returns: The newly created object, or null if the object could not be created. The default implementation 
             returns null.
        """
        pass

    def GetCreateInstanceSupported(self, context=None):
        """
        GetCreateInstanceSupported(self: SizeConverter, context: ITypeDescriptorContext) -> bool
        
            Determines whether changing a value on this object should require a call to the 
             System.Drawing.SizeConverter.CreateInstance(System.ComponentModel.ITypeDescriptorContext,System.C
             ollections.IDictionary) method to create a new value.
        
        
            context: A System.ComponentModel.TypeDescriptor through which additional context can be provided.
            Returns: true if the 
             System.Drawing.SizeConverter.CreateInstance(System.ComponentModel.ITypeDescriptorContext,System.C
             ollections.IDictionary) object should be called when a change is made to one or more properties 
             of this object.
        """
        pass

    def GetProperties(self, *__args):
        """
        GetProperties(self: SizeConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Retrieves the set of properties for this type. By default, a type does not have any properties 
             to return.
        
        
            context: A System.ComponentModel.TypeDescriptor through which additional context can be provided.
            value: The value of the object to get the properties for.
            attributes: An array of System.Attribute objects that describe the properties.
            Returns: The set of properties that should be exposed for this data type. If no properties should be 
             exposed, this may return null. The default implementation always returns null.
        """
        pass

    def GetPropertiesSupported(self, context=None):
        """
        GetPropertiesSupported(self: SizeConverter, context: ITypeDescriptorContext) -> bool
        
            Determines whether this object supports properties. By default, this is false.
        
            context: A System.ComponentModel.TypeDescriptor through which additional context can be provided.
            Returns: true if the 
             System.Drawing.SizeConverter.GetProperties(System.ComponentModel.ITypeDescriptorContext,System.Ob
             ject,System.Attribute[]) method should be called to find the properties of this object.
        """
        pass


class SizeF(object):
    """
    Stores an ordered pair of floating-point numbers, typically the width and height of a rectangle.
    
    SizeF(size: SizeF)
    SizeF(pt: PointF)
    SizeF(width: Single, height: Single)
    """
    @staticmethod
    def Add(sz1, sz2):
        """
        Add(sz1: SizeF, sz2: SizeF) -> SizeF
        
            Adds the width and height of one System.Drawing.SizeF structure to the width and height of 
             another System.Drawing.SizeF structure.
        
        
            sz1: The first System.Drawing.SizeF structure to add.
            sz2: The second System.Drawing.SizeF structure to add.
            Returns: A System.Drawing.SizeF structure that is the result of the addition operation.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: SizeF, obj: object) -> bool
        
            Tests to see whether the specified object is a System.Drawing.SizeF structure with the same 
             dimensions as this System.Drawing.SizeF structure.
        
        
            obj: The System.Object to test.
            Returns: This method returns true if obj is a System.Drawing.SizeF and has the same width and height as 
             this System.Drawing.SizeF; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: SizeF) -> int
        
            Returns a hash code for this System.Drawing.Size structure.
            Returns: An integer value that specifies a hash value for this System.Drawing.Size structure.
        """
        pass

    @staticmethod
    def Subtract(sz1, sz2):
        """
        Subtract(sz1: SizeF, sz2: SizeF) -> SizeF
        
            Subtracts the width and height of one System.Drawing.SizeF structure from the width and height 
             of another System.Drawing.SizeF structure.
        
        
            sz1: The System.Drawing.SizeF structure on the left side of the subtraction operator.
            sz2: The System.Drawing.SizeF structure on the right side of the subtraction operator.
            Returns: A System.Drawing.SizeF structure that is a result of the subtraction operation.
        """
        pass

    def ToPointF(self):
        """
        ToPointF(self: SizeF) -> PointF
        
            Converts a System.Drawing.SizeF structure to a System.Drawing.PointF structure.
            Returns: Returns a System.Drawing.PointF structure.
        """
        pass

    def ToSize(self):
        """
        ToSize(self: SizeF) -> Size
        
            Converts a System.Drawing.SizeF structure to a System.Drawing.Size structure.
            Returns: Returns a System.Drawing.Size structure.
        """
        pass

    def ToString(self):
        """
        ToString(self: SizeF) -> str
        
            Creates a human-readable string that represents this System.Drawing.SizeF structure.
            Returns: A string that represents this System.Drawing.SizeF structure.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[SizeF]() -> SizeF
        
        __new__(cls: type, size: SizeF)
        __new__(cls: type, pt: PointF)
        __new__(cls: type, width: Single, height: Single)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(sz1: SizeF, sz2: SizeF) -> SizeF
        
            Adds the width and height of one System.Drawing.SizeF structure to the width and height of 
             another System.Drawing.SizeF structure.
        
        
            sz1: The first System.Drawing.SizeF structure to add.
            sz2: The second System.Drawing.SizeF structure to add.
            Returns: A System.Drawing.Size structure that is the result of the addition operation.
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(sz1: SizeF, sz2: SizeF) -> SizeF
        
            Subtracts the width and height of one System.Drawing.SizeF structure from the width and height 
             of another System.Drawing.SizeF structure.
        
        
            sz1: The System.Drawing.SizeF structure on the left side of the subtraction operator.
            sz2: The System.Drawing.SizeF structure on the right side of the subtraction operator.
            Returns: A System.Drawing.SizeF that is the result of the subtraction operation.
        """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the vertical component of this System.Drawing.SizeF structure.

Get: Height(self: SizeF) -> Single

Set: Height(self: SizeF) = value
"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Drawing.SizeF structure has zero width and height.

Get: IsEmpty(self: SizeF) -> bool

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the horizontal component of this System.Drawing.SizeF structure.

Get: Width(self: SizeF) -> Single

Set: Width(self: SizeF) = value
"""


    Empty = None


class SizeFConverter(TypeConverter):
    """
    Converts System.Drawing.SizeF objects from one type to another.
    
    SizeFConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: SizeFConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Returns a value indicating whether the converter can convert from the type specified to the 
             System.Drawing.SizeF type, using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext through which additional context can be supplied.
            sourceType: A System.Type the represents the type you wish to convert from.
            Returns: true to indicate the conversion can be performed; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: SizeFConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Returns a value indicating whether the System.Drawing.SizeFConverter can convert a 
             System.Drawing.SizeF to the specified type.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext through which additional context can be supplied.
            destinationType: A System.Type that represents the type you want to convert from.
            Returns: true if this converter can perform the conversion otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: SizeFConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The System.Globalization.CultureInfo to use as the current culture.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: SizeFConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo. If null is passed, the current culture is assumed.
            value: The System.Object to convert.
            destinationType: The System.Type to convert the value parameter to.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def CreateInstance(self, *__args):
        """
        CreateInstance(self: SizeFConverter, context: ITypeDescriptorContext, propertyValues: IDictionary) -> object
        
            Creates an instance of a System.Drawing.SizeF with the specified property values using the 
             specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext through which additional context can be supplied.
            propertyValues: An System.Collections.IDictionary containing property names and values.
            Returns: An System.Object representing the new System.Drawing.SizeF, or null if the object cannot be 
             created.
        """
        pass

    def GetCreateInstanceSupported(self, context=None):
        """
        GetCreateInstanceSupported(self: SizeFConverter, context: ITypeDescriptorContext) -> bool
        
            Returns a value indicating whether changing a value on this object requires a call to the 
             erload:System.Drawing.SizeFConverter.CreateInstance method to create a new value.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context. This may be null.
            Returns: Always returns true.
        """
        pass

    def GetProperties(self, *__args):
        """
        GetProperties(self: SizeFConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        
            Retrieves a set of properties for the System.Drawing.SizeF type using the specified context and 
             attributes.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext through which additional context can be supplied.
            value: The System.Object to return properties for.
            attributes: An array of System.Attribute objects that describe the properties.
            Returns: A System.ComponentModel.PropertyDescriptorCollection containing the properties.
        """
        pass

    def GetPropertiesSupported(self, context=None):
        """
        GetPropertiesSupported(self: SizeFConverter, context: ITypeDescriptorContext) -> bool
        
            Returns whether the System.Drawing.SizeF type supports properties.
        
            context: An System.ComponentModel.ITypeDescriptorContext through which additional context can be supplied.
            Returns: Always returns true.
        """
        pass


class SolidBrush(Brush, ICloneable, IDisposable, ISystemColorTracker):
    """
    Defines a brush of a single color. Brushes are used to fill graphics shapes, such as rectangles, ellipses, pies, polygons, and paths. This class cannot be inherited.
    
    SolidBrush(color: Color)
    """
    def Clone(self):
        """
        Clone(self: SolidBrush) -> object
        
            Creates an exact copy of this System.Drawing.SolidBrush object.
            Returns: The System.Drawing.SolidBrush object that this method creates.
        """
        pass

    def Dispose(self):
        """ Dispose(self: SolidBrush, disposing: bool) """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def SetNativeBrush(self, *args): #cannot find CLR method
        """
        SetNativeBrush(self: Brush, brush: IntPtr)
            In a derived class, sets a reference to a GDI+ brush object.
        
            brush: A pointer to the GDI+ brush object.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, color):
        """ __new__(cls: type, color: Color) """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of this System.Drawing.SolidBrush object.

Get: Color(self: SolidBrush) -> Color

Set: Color(self: SolidBrush) = value
"""



class StringAlignment(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the alignment of a text string relative to its layout rectangle.
    
    enum StringAlignment, values: Center (1), Far (2), Near (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Center = None
    Far = None
    Near = None
    value__ = None


class StringDigitSubstitute(Enum, IComparable, IFormattable, IConvertible):
    """
    The System.Drawing.StringDigitSubstitute enumeration specifies how to substitute digits in a string according to a user's locale or language.
    
    enum StringDigitSubstitute, values: National (2), None (1), Traditional (3), User (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    National = None
    None = None
    Traditional = None
    User = None
    value__ = None


class StringFormat(MarshalByRefObject, ICloneable, IDisposable):
    """
    Encapsulates text layout information (such as alignment, orientation and tab stops) display manipulations (such as ellipsis insertion and national digit substitution) and OpenType features. This class cannot be inherited.
    
    StringFormat()
    StringFormat(options: StringFormatFlags)
    StringFormat(options: StringFormatFlags, language: int)
    StringFormat(format: StringFormat)
    """
    def Clone(self):
        """
        Clone(self: StringFormat) -> object
        
            Creates an exact copy of this System.Drawing.StringFormat object.
            Returns: The System.Drawing.StringFormat object this method creates.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: StringFormat)
            Releases all resources used by this System.Drawing.StringFormat object.
        """
        pass

    def GetTabStops(self, firstTabOffset):
        """
        GetTabStops(self: StringFormat) -> (Array[Single], Single)
        
            Gets the tab stops for this System.Drawing.StringFormat object.
            Returns: An array of distances (in number of spaces) between tab stops.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def SetDigitSubstitution(self, language, substitute):
        """
        SetDigitSubstitution(self: StringFormat, language: int, substitute: StringDigitSubstitute)
            Specifies the language and method to be used when local digits are substituted for western 
             digits.
        
        
            language: A National Language Support (NLS) language identifier that identifies the language that will be 
             used when local digits are substituted for western digits. You can pass the 
             System.Globalization.CultureInfo.LCID property of a System.Globalization.CultureInfo object as 
             the NLS language identifier. For example, suppose you create a System.Globalization.CultureInfo 
             object by passing the string "ar-EG" to a System.Globalization.CultureInfo constructor. If you 
             pass the System.Globalization.CultureInfo.LCID property of that System.Globalization.CultureInfo 
             object along with System.Drawing.StringDigitSubstitute.Traditional to the 
             System.Drawing.StringFormat.SetDigitSubstitution(System.Int32,System.Drawing.StringDigitSubstitut
             e) method, then Arabic-Indic digits will be substituted for western digits at display time.
        
            substitute: An element of the System.Drawing.StringDigitSubstitute enumeration that specifies how digits are 
             displayed.
        """
        pass

    def SetMeasurableCharacterRanges(self, ranges):
        """
        SetMeasurableCharacterRanges(self: StringFormat, ranges: Array[CharacterRange])
            Specifies an array of System.Drawing.CharacterRange structures that represent the ranges of 
             characters measured by a call to the 
             System.Drawing.Graphics.MeasureCharacterRanges(System.String,System.Drawing.Font,System.Drawing.R
             ectangleF,System.Drawing.StringFormat) method.
        
        
            ranges: An array of System.Drawing.CharacterRange structures that specifies the ranges of characters 
             measured by a call to the 
             System.Drawing.Graphics.MeasureCharacterRanges(System.String,System.Drawing.Font,System.Drawing.R
             ectangleF,System.Drawing.StringFormat) method.
        """
        pass

    def SetTabStops(self, firstTabOffset, tabStops):
        """
        SetTabStops(self: StringFormat, firstTabOffset: Single, tabStops: Array[Single])
            Sets tab stops for this System.Drawing.StringFormat object.
        
            firstTabOffset: The number of spaces between the beginning of a line of text and the first tab stop.
            tabStops: An array of distances between tab stops in the units specified by the 
             System.Drawing.Graphics.PageUnit property.
        """
        pass

    def ToString(self):
        """
        ToString(self: StringFormat) -> str
        
            Converts this System.Drawing.StringFormat object to a human-readable string.
            Returns: A string representation of this System.Drawing.StringFormat object.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, options: StringFormatFlags)
        __new__(cls: type, options: StringFormatFlags, language: int)
        __new__(cls: type, format: StringFormat)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Alignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets horizontal alignment of the string..

Get: Alignment(self: StringFormat) -> StringAlignment

Set: Alignment(self: StringFormat) = value
"""

    DigitSubstitutionLanguage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the language that is used when local digits are substituted for western digits.

Get: DigitSubstitutionLanguage(self: StringFormat) -> int

"""

    DigitSubstitutionMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the method to be used for digit substitution.

Get: DigitSubstitutionMethod(self: StringFormat) -> StringDigitSubstitute

"""

    FormatFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Drawing.StringFormatFlags enumeration that contains formatting information.

Get: FormatFlags(self: StringFormat) -> StringFormatFlags

Set: FormatFlags(self: StringFormat) = value
"""

    HotkeyPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Drawing.Text.HotkeyPrefix object for this System.Drawing.StringFormat object.

Get: HotkeyPrefix(self: StringFormat) -> HotkeyPrefix

Set: HotkeyPrefix(self: StringFormat) = value
"""

    LineAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the vertical alignment of the string.

Get: LineAlignment(self: StringFormat) -> StringAlignment

Set: LineAlignment(self: StringFormat) = value
"""

    Trimming = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Drawing.StringTrimming enumeration for this System.Drawing.StringFormat object.

Get: Trimming(self: StringFormat) -> StringTrimming

Set: Trimming(self: StringFormat) = value
"""


    GenericDefault = None
    GenericTypographic = None


class StringFormatFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the display and layout information for text strings.
    
    enum (flags) StringFormatFlags, values: DirectionRightToLeft (1), DirectionVertical (2), DisplayFormatControl (32), FitBlackBox (4), LineLimit (8192), MeasureTrailingSpaces (2048), NoClip (16384), NoFontFallback (1024), NoWrap (4096)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DirectionRightToLeft = None
    DirectionVertical = None
    DisplayFormatControl = None
    FitBlackBox = None
    LineLimit = None
    MeasureTrailingSpaces = None
    NoClip = None
    NoFontFallback = None
    NoWrap = None
    value__ = None


class StringTrimming(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how to trim characters from a string that does not completely fit into a layout shape.
    
    enum StringTrimming, values: Character (1), EllipsisCharacter (3), EllipsisPath (5), EllipsisWord (4), None (0), Word (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Character = None
    EllipsisCharacter = None
    EllipsisPath = None
    EllipsisWord = None
    None = None
    value__ = None
    Word = None


class StringUnit(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the units of measure for a text string.
    
    enum StringUnit, values: Display (1), Document (5), Em (32), Inch (4), Millimeter (6), Pixel (2), Point (3), World (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Display = None
    Document = None
    Em = None
    Inch = None
    Millimeter = None
    Pixel = None
    Point = None
    value__ = None
    World = None


class SystemBrushes(object):
    """ Each property of the System.Drawing.SystemBrushes class is a System.Drawing.SolidBrush that is the color of a Windows display element. """
    @staticmethod
    def FromSystemColor(c):
        """
        FromSystemColor(c: Color) -> Brush
        
            Creates a System.Drawing.Brush from the specified System.Drawing.Color structure.
        
            c: The System.Drawing.Color structure from which to create the System.Drawing.Brush.
            Returns: The System.Drawing.Brush this method creates.
        """
        pass

    ActiveBorder = None
    ActiveCaption = None
    ActiveCaptionText = None
    AppWorkspace = None
    ButtonFace = None
    ButtonHighlight = None
    ButtonShadow = None
    Control = None
    ControlDark = None
    ControlDarkDark = None
    ControlLight = None
    ControlLightLight = None
    ControlText = None
    Desktop = None
    GradientActiveCaption = None
    GradientInactiveCaption = None
    GrayText = None
    Highlight = None
    HighlightText = None
    HotTrack = None
    InactiveBorder = None
    InactiveCaption = None
    InactiveCaptionText = None
    Info = None
    InfoText = None
    Menu = None
    MenuBar = None
    MenuHighlight = None
    MenuText = None
    ScrollBar = None
    Window = None
    WindowFrame = None
    WindowText = None


class SystemColors(object):
    """ Each property of the System.Drawing.SystemColors class is a System.Drawing.Color structure that is the color of a Windows display element. """
    ActiveBorder = None
    ActiveCaption = None
    ActiveCaptionText = None
    AppWorkspace = None
    ButtonFace = None
    ButtonHighlight = None
    ButtonShadow = None
    Control = None
    ControlDark = None
    ControlDarkDark = None
    ControlLight = None
    ControlLightLight = None
    ControlText = None
    Desktop = None
    GradientActiveCaption = None
    GradientInactiveCaption = None
    GrayText = None
    Highlight = None
    HighlightText = None
    HotTrack = None
    InactiveBorder = None
    InactiveCaption = None
    InactiveCaptionText = None
    Info = None
    InfoText = None
    Menu = None
    MenuBar = None
    MenuHighlight = None
    MenuText = None
    ScrollBar = None
    Window = None
    WindowFrame = None
    WindowText = None


class SystemFonts(object):
    """ Specifies the fonts used to display text in Windows display elements. """
    @staticmethod
    def GetFontByName(systemFontName):
        """
        GetFontByName(systemFontName: str) -> Font
        
            Returns a font object that corresponds to the specified system font name.
        
            systemFontName: The name of the system font you need a font object for.
            Returns: A System.Drawing.Font if the specified name matches a value in System.Drawing.SystemFonts; 
             otherwise, null.
        """
        pass

    CaptionFont = None
    DefaultFont = None
    DialogFont = None
    IconTitleFont = None
    MenuFont = None
    MessageBoxFont = None
    SmallCaptionFont = None
    StatusFont = None


class SystemIcons(object):
    """ Each property of the System.Drawing.SystemIcons class is an System.Drawing.Icon object for Windows system-wide icons. This class cannot be inherited. """
    Application = None
    Asterisk = None
    Error = None
    Exclamation = None
    Hand = None
    Information = None
    Question = None
    Shield = None
    Warning = None
    WinLogo = None


class SystemPens(object):
    """ Each property of the System.Drawing.SystemPens class is a System.Drawing.Pen that is the color of a Windows display element and that has a width of 1 pixel. """
    @staticmethod
    def FromSystemColor(c):
        """
        FromSystemColor(c: Color) -> Pen
        
            Creates a System.Drawing.Pen from the specified System.Drawing.Color.
        
            c: The System.Drawing.Color for the new System.Drawing.Pen.
            Returns: The System.Drawing.Pen this method creates.
        """
        pass

    ActiveBorder = None
    ActiveCaption = None
    ActiveCaptionText = None
    AppWorkspace = None
    ButtonFace = None
    ButtonHighlight = None
    ButtonShadow = None
    Control = None
    ControlDark = None
    ControlDarkDark = None
    ControlLight = None
    ControlLightLight = None
    ControlText = None
    Desktop = None
    GradientActiveCaption = None
    GradientInactiveCaption = None
    GrayText = None
    Highlight = None
    HighlightText = None
    HotTrack = None
    InactiveBorder = None
    InactiveCaption = None
    InactiveCaptionText = None
    Info = None
    InfoText = None
    Menu = None
    MenuBar = None
    MenuHighlight = None
    MenuText = None
    ScrollBar = None
    Window = None
    WindowFrame = None
    WindowText = None


class TextureBrush(Brush, ICloneable, IDisposable):
    """
    Each property of the System.Drawing.TextureBrush class is a System.Drawing.Brush object that uses an image to fill the interior of a shape. This class cannot be inherited.
    
    TextureBrush(bitmap: Image)
    TextureBrush(image: Image, wrapMode: WrapMode)
    TextureBrush(image: Image, wrapMode: WrapMode, dstRect: RectangleF)
    TextureBrush(image: Image, wrapMode: WrapMode, dstRect: Rectangle)
    TextureBrush(image: Image, dstRect: RectangleF)
    TextureBrush(image: Image, dstRect: RectangleF, imageAttr: ImageAttributes)
    TextureBrush(image: Image, dstRect: Rectangle)
    TextureBrush(image: Image, dstRect: Rectangle, imageAttr: ImageAttributes)
    """
    def Clone(self):
        """
        Clone(self: TextureBrush) -> object
        
            Creates an exact copy of this System.Drawing.TextureBrush object.
            Returns: The System.Drawing.TextureBrush object this method creates, cast as an System.Object object.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Brush, disposing: bool)
            Releases the unmanaged resources used by the System.Drawing.Brush and optionally releases the 
             managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def MultiplyTransform(self, matrix, order=None):
        """
        MultiplyTransform(self: TextureBrush, matrix: Matrix, order: MatrixOrder)
            Multiplies the System.Drawing.Drawing2D.Matrix object that represents the local geometric 
             transformation of this System.Drawing.TextureBrush object by the specified 
             System.Drawing.Drawing2D.Matrix object in the specified order.
        
        
            matrix: The System.Drawing.Drawing2D.Matrix object by which to multiply the geometric transformation.
            order: A System.Drawing.Drawing2D.MatrixOrder enumeration that specifies the order in which to multiply 
             the two matrices.
        
        MultiplyTransform(self: TextureBrush, matrix: Matrix)
            Multiplies the System.Drawing.Drawing2D.Matrix object that represents the local geometric 
             transformation of this System.Drawing.TextureBrush object by the specified 
             System.Drawing.Drawing2D.Matrix object by prepending the specified 
             System.Drawing.Drawing2D.Matrix object.
        
        
            matrix: The System.Drawing.Drawing2D.Matrix object by which to multiply the geometric transformation.
        """
        pass

    def ResetTransform(self):
        """
        ResetTransform(self: TextureBrush)
            Resets the Transform property of this System.Drawing.TextureBrush object to identity.
        """
        pass

    def RotateTransform(self, angle, order=None):
        """
        RotateTransform(self: TextureBrush, angle: Single, order: MatrixOrder)
            Rotates the local geometric transformation of this System.Drawing.TextureBrush object by the 
             specified amount in the specified order.
        
        
            angle: The angle of rotation.
            order: A System.Drawing.Drawing2D.MatrixOrder enumeration that specifies whether to append or prepend 
             the rotation matrix.
        
        RotateTransform(self: TextureBrush, angle: Single)
            Rotates the local geometric transformation of this System.Drawing.TextureBrush object by the 
             specified amount. This method prepends the rotation to the transformation.
        
        
            angle: The angle of rotation.
        """
        pass

    def ScaleTransform(self, sx, sy, order=None):
        """
        ScaleTransform(self: TextureBrush, sx: Single, sy: Single, order: MatrixOrder)
            Scales the local geometric transformation of this System.Drawing.TextureBrush object by the 
             specified amounts in the specified order.
        
        
            sx: The amount by which to scale the transformation in the x direction.
            sy: The amount by which to scale the transformation in the y direction.
            order: A System.Drawing.Drawing2D.MatrixOrder enumeration that specifies whether to append or prepend 
             the scaling matrix.
        
        ScaleTransform(self: TextureBrush, sx: Single, sy: Single)
            Scales the local geometric transformation of this System.Drawing.TextureBrush object by the 
             specified amounts. This method prepends the scaling matrix to the transformation.
        
        
            sx: The amount by which to scale the transformation in the x direction.
            sy: The amount by which to scale the transformation in the y direction.
        """
        pass

    def SetNativeBrush(self, *args): #cannot find CLR method
        """
        SetNativeBrush(self: Brush, brush: IntPtr)
            In a derived class, sets a reference to a GDI+ brush object.
        
            brush: A pointer to the GDI+ brush object.
        """
        pass

    def TranslateTransform(self, dx, dy, order=None):
        """
        TranslateTransform(self: TextureBrush, dx: Single, dy: Single, order: MatrixOrder)
            Translates the local geometric transformation of this System.Drawing.TextureBrush object by the 
             specified dimensions in the specified order.
        
        
            dx: The dimension by which to translate the transformation in the x direction.
            dy: The dimension by which to translate the transformation in the y direction.
            order: The order (prepend or append) in which to apply the translation.
        TranslateTransform(self: TextureBrush, dx: Single, dy: Single)
            Translates the local geometric transformation of this System.Drawing.TextureBrush object by the 
             specified dimensions. This method prepends the translation to the transformation.
        
        
            dx: The dimension by which to translate the transformation in the x direction.
            dy: The dimension by which to translate the transformation in the y direction.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, bitmap: Image)
        __new__(cls: type, image: Image, wrapMode: WrapMode)
        __new__(cls: type, image: Image, wrapMode: WrapMode, dstRect: RectangleF)
        __new__(cls: type, image: Image, wrapMode: WrapMode, dstRect: Rectangle)
        __new__(cls: type, image: Image, dstRect: RectangleF)
        __new__(cls: type, image: Image, dstRect: RectangleF, imageAttr: ImageAttributes)
        __new__(cls: type, image: Image, dstRect: Rectangle)
        __new__(cls: type, image: Image, dstRect: Rectangle, imageAttr: ImageAttributes)
        """
        pass

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Drawing.Image object associated with this System.Drawing.TextureBrush object.

Get: Image(self: TextureBrush) -> Image

"""

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a copy of the System.Drawing.Drawing2D.Matrix object that defines a local geometric transformation for the image associated with this System.Drawing.TextureBrush object.

Get: Transform(self: TextureBrush) -> Matrix

Set: Transform(self: TextureBrush) = value
"""

    WrapMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Drawing.Drawing2D.WrapMode enumeration that indicates the wrap mode for this System.Drawing.TextureBrush object.

Get: WrapMode(self: TextureBrush) -> WrapMode

Set: WrapMode(self: TextureBrush) = value
"""



class ToolboxBitmapAttribute(Attribute, _Attribute):
    """
    Allows you to specify an icon to represent a control in a container, such as the Microsoft Visual Studio Form Designer.
    
    ToolboxBitmapAttribute(imageFile: str)
    ToolboxBitmapAttribute(t: Type)
    ToolboxBitmapAttribute(t: Type, name: str)
    """
    def Equals(self, value):
        """
        Equals(self: ToolboxBitmapAttribute, value: object) -> bool
        
            Indicates whether the specified object is a System.Drawing.ToolboxBitmapAttribute object and is 
             identical to this System.Drawing.ToolboxBitmapAttribute object.
        
        
            value: The System.Object to test.
            Returns: This method returns true if value is both a System.Drawing.ToolboxBitmapAttribute object and is 
             identical to this System.Drawing.ToolboxBitmapAttribute object.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ToolboxBitmapAttribute) -> int
        
            Gets a hash code for this System.Drawing.ToolboxBitmapAttribute object.
            Returns: The hash code for this System.Drawing.ToolboxBitmapAttribute object.
        """
        pass

    def GetImage(self, *__args):
        """
        GetImage(self: ToolboxBitmapAttribute, type: Type, large: bool) -> Image
        
            Gets the small or large System.Drawing.Image associated with this 
             System.Drawing.ToolboxBitmapAttribute object.
        
        
            type: If this System.Drawing.ToolboxBitmapAttribute object does not already have a small image, this 
             method searches for a bitmap resource in the assembly that defines the type specified by the 
             component type. For example, if you pass typeof(ControlA) to the type parameter, then this 
             method searches the assembly that defines ControlA.
        
            large: Specifies whether this method returns a large image (true) or a small image (false). The small 
             image is 16 by 16, and the large image is 32 by 32.
        
            Returns: An System.Drawing.Image associated with this System.Drawing.ToolboxBitmapAttribute object.
        GetImage(self: ToolboxBitmapAttribute, type: Type, imgName: str, large: bool) -> Image
        
            Gets the small or large System.Drawing.Image associated with this 
             System.Drawing.ToolboxBitmapAttribute object.
        
        
            type: If this System.Drawing.ToolboxBitmapAttribute object does not already have a small image, this 
             method searches for an embedded bitmap resource in the assembly that defines the type specified 
             by the component type. For example, if you pass typeof(ControlA) to the type parameter, then 
             this method searches the assembly that defines ControlA.
        
            imgName: The name of the embedded bitmap resource.
            large: Specifies whether this method returns a large image (true) or a small image (false). The small 
             image is 16 by 16, and the large image is 32 by 32.
        
            Returns: An System.Drawing.Image associated with this System.Drawing.ToolboxBitmapAttribute object.
        GetImage(self: ToolboxBitmapAttribute, type: Type) -> Image
        
            Gets the small System.Drawing.Image associated with this System.Drawing.ToolboxBitmapAttribute 
             object.
        
        
            type: If this System.Drawing.ToolboxBitmapAttribute object does not already have a small image, this 
             method searches for a bitmap resource in the assembly that defines the type specified by the 
             type parameter. For example, if you pass typeof(ControlA) to the type parameter, then this 
             method searches the assembly that defines ControlA.
        
            Returns: The small System.Drawing.Image associated with this System.Drawing.ToolboxBitmapAttribute object.
        GetImage(self: ToolboxBitmapAttribute, component: object) -> Image
        
            Gets the small System.Drawing.Image associated with this System.Drawing.ToolboxBitmapAttribute 
             object.
        
        
            component: If this System.Drawing.ToolboxBitmapAttribute object does not already have a small image, this 
             method searches for a bitmap resource in the assembly that defines the type of the object 
             specified by the component parameter. For example, if you pass an object of type ControlA to the 
             component parameter, then this method searches the assembly that defines ControlA.
        
            Returns: The small System.Drawing.Image associated with this System.Drawing.ToolboxBitmapAttribute object.
        GetImage(self: ToolboxBitmapAttribute, component: object, large: bool) -> Image
        
            Gets the small or large System.Drawing.Image associated with this 
             System.Drawing.ToolboxBitmapAttribute object.
        
        
            component: If this System.Drawing.ToolboxBitmapAttribute object does not already have a small image, this 
             method searches for a bitmap resource in the assembly that defines the type of the object 
             specified by the component parameter. For example, if you pass an object of type ControlA to the 
             component parameter, then this method searches the assembly that defines ControlA.
        
            large: Specifies whether this method returns a large image (true) or a small image (false). The small 
             image is 16 by 16, and the large image is 32 by 32.
        
            Returns: An System.Drawing.Image object associated with this System.Drawing.ToolboxBitmapAttribute object.
        """
        pass

    @staticmethod
    def GetImageFromResource(t, imageName, large):
        """
        GetImageFromResource(t: Type, imageName: str, large: bool) -> Image
        
            Returns an System.Drawing.Image object based on a bitmap resource that is embedded in an 
             assembly.
        
        
            t: This method searches for an embedded bitmap resource in the assembly that defines the type 
             specified by the t parameter. For example, if you pass typeof(ControlA) to the t parameter, then 
             this method searches the assembly that defines ControlA.
        
            imageName: The name of the embedded bitmap resource.
            large: Specifies whether this method returns a large image (true)or a small image (false). The small 
             image is 16 by 16, and the large image is 32 x 32.
        
            Returns: An System.Drawing.Image object based on the retrieved bitmap.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, imageFile: str)
        __new__(cls: type, t: Type)
        __new__(cls: type, t: Type, name: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Default = None


# variables with complex values

