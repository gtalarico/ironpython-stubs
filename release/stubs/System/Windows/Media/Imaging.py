# encoding: utf-8
# module System.Windows.Media.Imaging calls itself Imaging
# from PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BitmapCacheOption(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how a bitmap image takes advantage of memory caching.
    
    enum BitmapCacheOption, values: Default (0), None (2), OnDemand (0), OnLoad (1)
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

    Default = None
    None = None
    OnDemand = None
    OnLoad = None
    value__ = None


class BitmapCodecInfo(object):
    """ Provides information about an imaging codec. """
    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the author of the codec.

Get: Author(self: BitmapCodecInfo) -> str

"""

    ContainerFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the container format for the codec.

Get: ContainerFormat(self: BitmapCodecInfo) -> Guid

"""

    DeviceManufacturer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the device manufacturer of the codec.

Get: DeviceManufacturer(self: BitmapCodecInfo) -> str

"""

    DeviceModels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the device models of the codec.

Get: DeviceModels(self: BitmapCodecInfo) -> str

"""

    FileExtensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the file extensions associated with the codec.

Get: FileExtensions(self: BitmapCodecInfo) -> str

"""

    FriendlyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that represents the friendly name of the codec.

Get: FriendlyName(self: BitmapCodecInfo) -> str

"""

    MimeTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the Multipurpose Internet Mail Extensions (MIME) associated with the�codec.

Get: MimeTypes(self: BitmapCodecInfo) -> str

"""

    SpecificationVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the specification version of the codec.

Get: SpecificationVersion(self: BitmapCodecInfo) -> Version

"""

    SupportsAnimation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the codec supports animation.

Get: SupportsAnimation(self: BitmapCodecInfo) -> bool

"""

    SupportsLossless = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the codec supports lossless of images.

Get: SupportsLossless(self: BitmapCodecInfo) -> bool

"""

    SupportsMultipleFrames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies whether the codec supports multiple frames.

Get: SupportsMultipleFrames(self: BitmapCodecInfo) -> bool

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the version of the codec.

Get: Version(self: BitmapCodecInfo) -> Version

"""



class BitmapCreateOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies initialization options for bitmap images.
    
    enum (flags) BitmapCreateOptions, values: DelayCreation (2), IgnoreColorProfile (4), IgnoreImageCache (8), None (0), PreservePixelFormat (1)
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

    DelayCreation = None
    IgnoreColorProfile = None
    IgnoreImageCache = None
    None = None
    PreservePixelFormat = None
    value__ = None


class BitmapDecoder(DispatcherObject):
    """ Represents a container for bitmap frames. Each bitmap frame is a System.Windows.Media.Imaging.BitmapSource. This abstract class provides a base set of functionality for all derived decoder objects. """
    @staticmethod
    def Create(*__args):
        """
        Create(bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption) -> BitmapDecoder
        
            Creates a System.Windows.Media.Imaging.BitmapDecoder from a System.IO.Stream by using the 
             specified System.Windows.Media.Imaging.BitmapCreateOptions and 
             System.Windows.Media.Imaging.BitmapCacheOption.
        
        
            bitmapStream: The file stream that identifies the bitmap to decode.
            createOptions: Identifies the System.Windows.Media.Imaging.BitmapCreateOptions for this decoder.
            cacheOption: Identifies the System.Windows.Media.Imaging.BitmapCacheOption for this decoder.
            Returns: A new System.Windows.Media.Imaging.BitmapDecoder.
        Create(bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption, uriCachePolicy: RequestCachePolicy) -> BitmapDecoder
        
            Creates a System.Windows.Media.Imaging.BitmapDecoder from a System.Uri by using the specified 
             System.Windows.Media.Imaging.BitmapCreateOptions, System.Windows.Media.Imaging.BitmapCacheOption 
             and System.Net.Cache.RequestCachePolicy.
        
        
            bitmapUri: The location of the bitmap from which the System.Windows.Media.Imaging.BitmapDecoder is created.
            createOptions: The options that are used to create this System.Windows.Media.Imaging.BitmapDecoder.
            cacheOption: The cache option that is used to create this System.Windows.Media.Imaging.BitmapDecoder.
            uriCachePolicy: The caching requirements for this System.Windows.Media.Imaging.BitmapDecoder.
            Returns: A new System.Windows.Media.Imaging.BitmapDecoder.
        Create(bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption) -> BitmapDecoder
        
            Creates a System.Windows.Media.Imaging.BitmapDecoder from a System.Uri by using the specified 
             System.Windows.Media.Imaging.BitmapCreateOptions and 
             System.Windows.Media.Imaging.BitmapCacheOption.
        
        
            bitmapUri: The System.Uri of the bitmap to decode.
            createOptions: Identifies the System.Windows.Media.Imaging.BitmapCreateOptions for this decoder.
            cacheOption: Identifies the System.Windows.Media.Imaging.BitmapCacheOption for this decoder.
            Returns: A new System.Windows.Media.Imaging.BitmapDecoder.
        """
        pass

    def CreateInPlaceBitmapMetadataWriter(self):
        """
        CreateInPlaceBitmapMetadataWriter(self: BitmapDecoder) -> InPlaceBitmapMetadataWriter
        
            Creates an instance of System.Windows.Media.Imaging.InPlaceBitmapMetadataWriter, which can be 
             used to update the metadata of a bitmap.
        
            Returns: An instance of System.Windows.Media.Imaging.InPlaceBitmapMetadataWriter.
        """
        pass

    def ToString(self):
        """
        ToString(self: BitmapDecoder) -> str
        
            Converts the current value of a System.Windows.Media.Imaging.BitmapDecoder to a System.String.
            Returns: A string representation of the System.Windows.Media.Imaging.BitmapDecoder.
        """
        pass

    CodecInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets information that describes this codec.

Get: CodecInfo(self: BitmapDecoder) -> BitmapCodecInfo

"""

    ColorContexts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that represents the color profile associated with a bitmap, if one is defined.

Get: ColorContexts(self: BitmapDecoder) -> ReadOnlyCollection[ColorContext]

"""

    Frames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the content of an individual frame within a bitmap.

Get: Frames(self: BitmapDecoder) -> ReadOnlyCollection[BitmapFrame]

"""

    IsDownloading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates if the decoder is currently downloading content.

Get: IsDownloading(self: BitmapDecoder) -> bool

"""

    Metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an instance of System.Windows.Media.Imaging.BitmapMetadata that represents the global metadata associated with this bitmap, if metadata is defined.

Get: Metadata(self: BitmapDecoder) -> BitmapMetadata

"""

    Palette = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Media.Imaging.BitmapPalette associated with this decoder.

Get: Palette(self: BitmapDecoder) -> BitmapPalette

"""

    Preview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Windows.Media.Imaging.BitmapSource that represents the global preview of this bitmap, if one is defined.

Get: Preview(self: BitmapDecoder) -> BitmapSource

"""

    Thumbnail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Windows.Media.Imaging.BitmapSource that represents the thumbnail of the bitmap, if one is defined.

Get: Thumbnail(self: BitmapDecoder) -> BitmapSource

"""


    DownloadCompleted = None
    DownloadFailed = None
    DownloadProgress = None


class BitmapEncoder(DispatcherObject):
    """ Encodes a collection of System.Windows.Media.Imaging.BitmapFrame objects to an image stream. """
    @staticmethod
    def Create(containerFormat):
        """
        Create(containerFormat: Guid) -> BitmapEncoder
        
            Creates a System.Windows.Media.Imaging.BitmapEncoder from a System.Guid that identifies the 
             desired bitmap format.
        
        
            containerFormat: Identifies the desired bitmap encoding format.
            Returns: A System.Windows.Media.Imaging.BitmapEncoder that can encode to the specified containerFormat.
        """
        pass

    def Save(self, stream):
        """
        Save(self: BitmapEncoder, stream: Stream)
            Encodes a bitmap image to a specified System.IO.Stream.
        
            stream: Identifies the file stream that this bitmap is encoded to.
        """
        pass

    CodecInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets information that describes this codec.

Get: CodecInfo(self: BitmapEncoder) -> BitmapCodecInfo

"""

    ColorContexts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that represents the color profile that is associated with this encoder.

Get: ColorContexts(self: BitmapEncoder) -> ReadOnlyCollection[ColorContext]

Set: ColorContexts(self: BitmapEncoder) = value
"""

    Frames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the individual frames within an image.

Get: Frames(self: BitmapEncoder) -> IList[BitmapFrame]

Set: Frames(self: BitmapEncoder) = value
"""

    Metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the metadata that will be associated with this bitmap during encoding.

Get: Metadata(self: BitmapEncoder) -> BitmapMetadata

Set: Metadata(self: BitmapEncoder) = value
"""

    Palette = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that represents the System.Windows.Media.Imaging.BitmapPalette of an encoded bitmap.

Get: Palette(self: BitmapEncoder) -> BitmapPalette

Set: Palette(self: BitmapEncoder) = value
"""

    Preview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Windows.Media.Imaging.BitmapSource that represents the global preview of a bitmap, if there is one.

Get: Preview(self: BitmapEncoder) -> BitmapSource

Set: Preview(self: BitmapEncoder) = value
"""

    Thumbnail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Windows.Media.Imaging.BitmapSource that represents the global embedded thumbnail.

Get: Thumbnail(self: BitmapEncoder) -> BitmapSource

Set: Thumbnail(self: BitmapEncoder) = value
"""



class BitmapSource(ImageSource, ISealable, IAnimatable, IResource, IFormattable):
    """ Represents a single, constant set of pixels at a certain size and resolution. """
    def CheckIfSiteOfOrigin(self, *args): #cannot find CLR method
        """
        CheckIfSiteOfOrigin(self: BitmapSource)
            Checks whether the bitmap source content is from a known site of origin. This method is used to 
             make sure that pixel copying operations are safe.
        """
        pass

    def Clone(self):
        """
        Clone(self: BitmapSource) -> BitmapSource
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.BitmapSource, making deep copies 
             of this object's values. When copying dependency properties, this method copies resource 
             references and data bindings (but they might no longer resolve) but not animations or their 
             current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: BitmapSource, sourceFreezable: Freezable)
            Makes this instance a deep copy of the specified System.Windows.Media.Imaging.BitmapSource. When 
             copying dependency properties, this method copies resource references and data bindings (but 
             they might no longer resolve) but not animations or their current values.
        
        
            sourceFreezable: The System.Windows.Media.Imaging.BitmapSource to clone..
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: BitmapSource) -> BitmapSource
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.BitmapSource object, making deep 
             copies of this object's current values. Resource references, data bindings, and animations are 
             not copied, but their current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: BitmapSource, sourceFreezable: Freezable)
            Makes this instance a modifiable deep copy of the specified 
             System.Windows.Media.Imaging.BitmapSource using current property values. Resource references, 
             data bindings, and animations are not copied, but their current values are.
        
        
            sourceFreezable: The System.Windows.Media.Imaging.BitmapSource to clone.
        """
        pass

    def CopyPixels(self, *__args):
        """
        CopyPixels(self: BitmapSource, sourceRect: Int32Rect, buffer: IntPtr, bufferSize: int, stride: int)
            Copies the bitmap pixel data within the specified rectangle
        
            sourceRect: The source rectangle to copy. An System.Windows.Int32Rect.Empty value specifies the entire 
             bitmap.
        
            buffer: A pointer to the buffer.
            bufferSize: The size of the buffer.
            stride: The stride of the bitmap.
        CopyPixels(self: BitmapSource, pixels: Array, stride: int, offset: int)
            Copies the bitmap pixel data into an array of pixels with the specified stride, starting at the 
             specified offset.
        
        
            pixels: The destination array.
            stride: The stride of the bitmap.
            offset: The pixel location where copying starts.
        CopyPixels(self: BitmapSource, sourceRect: Int32Rect, pixels: Array, stride: int, offset: int)
            Copies the bitmap pixel data within the specified rectangle into an array of pixels that has the 
             specified stride starting at the specified offset.
        
        
            sourceRect: The source rectangle to copy. An System.Windows.Int32Rect.Empty value specifies the entire 
             bitmap.
        
            pixels: The destination array.
            stride: The stride of the bitmap.
            offset: The pixel location where copying begins.
        """
        pass

    @staticmethod
    def Create(pixelWidth, pixelHeight, dpiX, dpiY, pixelFormat, palette, *__args):
        """
        Create(pixelWidth: int, pixelHeight: int, dpiX: float, dpiY: float, pixelFormat: PixelFormat, palette: BitmapPalette, buffer: IntPtr, bufferSize: int, stride: int) -> BitmapSource
        
            Creates a new System.Windows.Media.Imaging.BitmapSource from an array of pixels that are stored 
             in unmanaged memory.
        
        
            pixelWidth: The width of the bitmap.
            pixelHeight: The height of the bitmap.
            dpiX: The horizontal dots per inch (dpi) of the bitmap.
            dpiY: The vertical dots per inch (dpi) of the bitmap.
            pixelFormat: The pixel format of the bitmap.
            palette: The palette of the bitmap.
            buffer: A pointer to the buffer that contains the bitmap data in memory.
            bufferSize: The size of the buffer.
            stride: The stride of the bitmap.
            Returns: A System.Windows.Media.Imaging.BitmapSource that is created from the array of pixels in 
             unmanaged memory.
        
        Create(pixelWidth: int, pixelHeight: int, dpiX: float, dpiY: float, pixelFormat: PixelFormat, palette: BitmapPalette, pixels: Array, stride: int) -> BitmapSource
        
            Creates a new System.Windows.Media.Imaging.BitmapSource from an array of pixels.
        
            pixelWidth: The width of the bitmap.
            pixelHeight: The height of the bitmap.
            dpiX: The horizontal dots per inch (dpi) of the bitmap.
            dpiY: The vertical dots per inch (dpi) of the bitmap.
            pixelFormat: The pixel format of the bitmap.
            palette: The palette of the bitmap.
            pixels: An array of bytes that represents the content of a bitmap image.
            stride: The stride of the bitmap.
            Returns: The System.Windows.Media.Imaging.BitmapSource that is created from the specified array of pixels.
        """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """
        CreateInstanceCore(self: Freezable) -> Freezable
        
            When implemented in a derived class, creates a new instance of the System.Windows.Freezable 
             derived class.
        
            Returns: The new instance.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: BitmapSource, isChecking: bool) -> bool
        
            Makes an instance of System.Windows.Media.Imaging.BitmapSource or a derived class immutable.
        
            isChecking: true if this instance should actually freeze itself when this method is called; otherwise, false.
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: BitmapSource, sourceFreezable: Freezable)
            Makes this instance a clone of the specified System.Windows.Media.Imaging.BitmapSource object.
        
            sourceFreezable: The System.Windows.Media.Imaging.BitmapSource object to clone and freeze.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: BitmapSource, sourceFreezable: Freezable)
            Makes this instance a frozen clone of the specified System.Windows.Media.Imaging.BitmapSource. 
             Resource references, data bindings, and animations are not copied, but their current values are.
        
        
            sourceFreezable: The System.Windows.Media.Imaging.BitmapSource to copy and freeze.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DpiX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the horizontal dots per inch (dpi) of the image.

Get: DpiX(self: BitmapSource) -> float

"""

    DpiY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the vertical dots per inch (dpi) of the image.

Get: DpiY(self: BitmapSource) -> float

"""

    Format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the native System.Windows.Media.PixelFormat of the bitmap data.

Get: Format(self: BitmapSource) -> PixelFormat

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of the source bitmap in device-independent units (1/96th inch per unit).

Get: Height(self: BitmapSource) -> float

"""

    IsDownloading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Media.Imaging.BitmapSource content is currently downloading.

Get: IsDownloading(self: BitmapSource) -> bool

"""

    Metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the metadata that is associated with this bitmap image.

Get: Metadata(self: BitmapSource) -> ImageMetadata

"""

    Palette = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the color palette of the bitmap, if one is specified.

Get: Palette(self: BitmapSource) -> BitmapPalette

"""

    PixelHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of the bitmap in pixels.

Get: PixelHeight(self: BitmapSource) -> int

"""

    PixelWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width of the bitmap in pixels.

Get: PixelWidth(self: BitmapSource) -> int

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width of the bitmap in device-independent units (1/96th inch per unit).

Get: Width(self: BitmapSource) -> float

"""


    DecodeFailed = None
    DownloadCompleted = None
    DownloadFailed = None
    DownloadProgress = None


class BitmapFrame(BitmapSource, ISealable, IAnimatable, IResource, IFormattable, IUriContext):
    """ Represents image data returned by a decoder and accepted by encoders. """
    def CheckIfSiteOfOrigin(self, *args): #cannot find CLR method
        """
        CheckIfSiteOfOrigin(self: BitmapSource)
            Checks whether the bitmap source content is from a known site of origin. This method is used to 
             make sure that pixel copying operations are safe.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: BitmapSource, sourceFreezable: Freezable)
            Makes this instance a deep copy of the specified System.Windows.Media.Imaging.BitmapSource. When 
             copying dependency properties, this method copies resource references and data bindings (but 
             they might no longer resolve) but not animations or their current values.
        
        
            sourceFreezable: The System.Windows.Media.Imaging.BitmapSource to clone..
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: BitmapSource, sourceFreezable: Freezable)
            Makes this instance a modifiable deep copy of the specified 
             System.Windows.Media.Imaging.BitmapSource using current property values. Resource references, 
             data bindings, and animations are not copied, but their current values are.
        
        
            sourceFreezable: The System.Windows.Media.Imaging.BitmapSource to clone.
        """
        pass

    @staticmethod
    def Create(*__args):
        """
        Create(source: BitmapSource) -> BitmapFrame
        
            Creates a new System.Windows.Media.Imaging.BitmapFrame from a given 
             System.Windows.Media.Imaging.BitmapSource.
        
        
            source: The System.Windows.Media.Imaging.BitmapSource that is used to construct this 
             System.Windows.Media.Imaging.BitmapFrame.
        
            Returns: A new System.Windows.Media.Imaging.BitmapFrame.
        Create(bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption) -> BitmapFrame
        
            Creates a new System.Windows.Media.Imaging.BitmapFrame from a given System.IO.Stream with the 
             specified System.Windows.Media.Imaging.BitmapCreateOptions and 
             System.Windows.Media.Imaging.BitmapCacheOption.
        
        
            bitmapStream: The stream from which this System.Windows.Media.Imaging.BitmapFrame is constructed.
            createOptions: The options that are used to create this System.Windows.Media.Imaging.BitmapFrame.
            cacheOption: The cache option that is used to create this System.Windows.Media.Imaging.BitmapFrame.
            Returns: A new System.Windows.Media.Imaging.BitmapFrame.
        Create(source: BitmapSource, thumbnail: BitmapSource, metadata: BitmapMetadata, colorContexts: ReadOnlyCollection[ColorContext]) -> BitmapFrame
        Create(source: BitmapSource, thumbnail: BitmapSource) -> BitmapFrame
        
            Creates a new System.Windows.Media.Imaging.BitmapFrame from a given 
             System.Windows.Media.Imaging.BitmapSource with the specified thumbnail.
        
        
            source: The source from which the System.Windows.Media.Imaging.BitmapFrame is constructed.
            thumbnail: A thumbnail image of the resulting System.Windows.Media.Imaging.BitmapFrame.
            Returns: A new System.Windows.Media.Imaging.BitmapFrame.
        Create(bitmapStream: Stream) -> BitmapFrame
        
            Creates a new System.Windows.Media.Imaging.BitmapFrame from a given System.IO.Stream.
        
            bitmapStream: The System.IO.Stream that is used to construct the System.Windows.Media.Imaging.BitmapFrame.
            Returns: A new System.Windows.Media.Imaging.BitmapFrame.
        Create(bitmapUri: Uri, uriCachePolicy: RequestCachePolicy) -> BitmapFrame
        
            Creates a System.Windows.Media.Imaging.BitmapFrame from a given System.Uri with the specified 
             System.Net.Cache.RequestCachePolicy.
        
        
            bitmapUri: The location of the bitmap from which the System.Windows.Media.Imaging.BitmapFrame is created.
            uriCachePolicy: The caching requirements for this System.Windows.Media.Imaging.BitmapFrame.
            Returns: A new System.Windows.Media.Imaging.BitmapFrame.
        Create(bitmapUri: Uri) -> BitmapFrame
        
            Creates a new System.Windows.Media.Imaging.BitmapFrame from a given System.Uri.
        
            bitmapUri: The System.Uri that identifies the source of the System.Windows.Media.Imaging.BitmapFrame.
            Returns: A new System.Windows.Media.Imaging.BitmapFrame.
        Create(bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption, uriCachePolicy: RequestCachePolicy) -> BitmapFrame
        
            Creates a System.Windows.Media.Imaging.BitmapFrame from a given System.Uri with the specified 
             System.Windows.Media.Imaging.BitmapCreateOptions, 
             System.Windows.Media.Imaging.BitmapCacheOption, and System.Net.Cache.RequestCachePolicy.
        
        
            bitmapUri: The location of the bitmap from which the System.Windows.Media.Imaging.BitmapFrame is created.
            createOptions: The options that are used to create this System.Windows.Media.Imaging.BitmapFrame.
            cacheOption: The cache option that is used to create this System.Windows.Media.Imaging.BitmapFrame.
            uriCachePolicy: The caching requirements for this System.Windows.Media.Imaging.BitmapFrame.
            Returns: A new System.Windows.Media.Imaging.BitmapFrame.
        Create(bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption) -> BitmapFrame
        
            Creates a System.Windows.Media.Imaging.BitmapFrame from a given System.Uri with the specified 
             System.Windows.Media.Imaging.BitmapCreateOptions and 
             System.Windows.Media.Imaging.BitmapCacheOption.
        
        
            bitmapUri: The location of the bitmap from which the System.Windows.Media.Imaging.BitmapFrame is created.
            createOptions: The options that are used to create this System.Windows.Media.Imaging.BitmapFrame.
            cacheOption: The cache option that is used to create this System.Windows.Media.Imaging.BitmapFrame.
            Returns: A new System.Windows.Media.Imaging.BitmapFrame.
        """
        pass

    def CreateInPlaceBitmapMetadataWriter(self):
        """
        CreateInPlaceBitmapMetadataWriter(self: BitmapFrame) -> InPlaceBitmapMetadataWriter
        
            When overridden in a derived class, creates an instance of 
             System.Windows.Media.Imaging.InPlaceBitmapMetadataWriter, which can be used to associate 
             metadata with a System.Windows.Media.Imaging.BitmapFrame.
        
            Returns: An System.Windows.Media.Imaging.InPlaceBitmapMetadataWriter.
        """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """
        CreateInstanceCore(self: Freezable) -> Freezable
        
            When implemented in a derived class, creates a new instance of the System.Windows.Freezable 
             derived class.
        
            Returns: The new instance.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: BitmapSource, isChecking: bool) -> bool
        
            Makes an instance of System.Windows.Media.Imaging.BitmapSource or a derived class immutable.
        
            isChecking: true if this instance should actually freeze itself when this method is called; otherwise, false.
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: BitmapSource, sourceFreezable: Freezable)
            Makes this instance a clone of the specified System.Windows.Media.Imaging.BitmapSource object.
        
            sourceFreezable: The System.Windows.Media.Imaging.BitmapSource object to clone and freeze.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: BitmapSource, sourceFreezable: Freezable)
            Makes this instance a frozen clone of the specified System.Windows.Media.Imaging.BitmapSource. 
             Resource references, data bindings, and animations are not copied, but their current values are.
        
        
            sourceFreezable: The System.Windows.Media.Imaging.BitmapSource to copy and freeze.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BaseUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets or sets a value that represents the base System.Uri of the current context.

Get: BaseUri(self: BitmapFrame) -> Uri

Set: BaseUri(self: BitmapFrame) = value
"""

    ColorContexts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a collection of System.Windows.Media.ColorContext objects that are associated with this System.Windows.Media.Imaging.BitmapFrame.

Get: ColorContexts(self: BitmapFrame) -> ReadOnlyCollection[ColorContext]

"""

    Decoder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the decoder associated with this instance of System.Windows.Media.Imaging.BitmapFrame.

Get: Decoder(self: BitmapFrame) -> BitmapDecoder

"""

    Thumbnail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the thumbnail image associated with this System.Windows.Media.Imaging.BitmapFrame.

Get: Thumbnail(self: BitmapFrame) -> BitmapSource

"""



class BitmapImage(BitmapSource, ISealable, IAnimatable, IResource, IFormattable, ISupportInitialize, IUriContext):
    """
    Provides a specialized System.Windows.Media.Imaging.BitmapSource that is optimized for loading images using Extensible Application Markup Language (XAML).
    
    BitmapImage()
    BitmapImage(uriSource: Uri)
    BitmapImage(uriSource: Uri, uriCachePolicy: RequestCachePolicy)
    """
    def BeginInit(self):
        """
        BeginInit(self: BitmapImage)
            Signals the start of the System.Windows.Media.Imaging.BitmapImage initialization.
        """
        pass

    def CheckIfSiteOfOrigin(self, *args): #cannot find CLR method
        """
        CheckIfSiteOfOrigin(self: BitmapSource)
            Checks whether the bitmap source content is from a known site of origin. This method is used to 
             make sure that pixel copying operations are safe.
        """
        pass

    def Clone(self):
        """
        Clone(self: BitmapImage) -> BitmapImage
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.BitmapImage, making deep copies 
             of this object's values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property is false even if the source's System.Windows.Freezable.IsFrozen property is true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: BitmapImage, source: Freezable) """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: BitmapImage) -> BitmapImage
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.BitmapImage object, making deep 
             copies of this object's current values. Resource references, data bindings, and animations are 
             not copied, but their current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property is false even if the source's System.Windows.Freezable.IsFrozen property is true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: BitmapImage, source: Freezable) """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """ CreateInstanceCore(self: BitmapImage) -> Freezable """
        pass

    def EndInit(self):
        """
        EndInit(self: BitmapImage)
            Signals the end of the System.Windows.Media.Imaging.BitmapImage initialization.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: BitmapSource, isChecking: bool) -> bool
        
            Makes an instance of System.Windows.Media.Imaging.BitmapSource or a derived class immutable.
        
            isChecking: true if this instance should actually freeze itself when this method is called; otherwise, false.
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: BitmapImage, source: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: BitmapImage, source: Freezable) """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, uriSource=None, uriCachePolicy=None):
        """
        __new__(cls: type)
        __new__(cls: type, uriSource: Uri)
        __new__(cls: type, uriSource: Uri, uriCachePolicy: RequestCachePolicy)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BaseUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that represents the base System.Uri of the current System.Windows.Media.Imaging.BitmapImage context.

Get: BaseUri(self: BitmapImage) -> Uri

Set: BaseUri(self: BitmapImage) = value
"""

    CacheOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Imaging.BitmapCacheOption to use for this instance of System.Windows.Media.Imaging.BitmapImage.

Get: CacheOption(self: BitmapImage) -> BitmapCacheOption

Set: CacheOption(self: BitmapImage) = value
"""

    CreateOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Imaging.BitmapCreateOptions for a System.Windows.Media.Imaging.BitmapImage.

Get: CreateOptions(self: BitmapImage) -> BitmapCreateOptions

Set: CreateOptions(self: BitmapImage) = value
"""

    DecodePixelHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height, in pixels, that the image is decoded to.

Get: DecodePixelHeight(self: BitmapImage) -> int

Set: DecodePixelHeight(self: BitmapImage) = value
"""

    DecodePixelWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the width, in pixels, that the image is decoded to.

Get: DecodePixelWidth(self: BitmapImage) -> int

Set: DecodePixelWidth(self: BitmapImage) = value
"""

    IsDownloading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Media.Imaging.BitmapImage is currently downloading content.

Get: IsDownloading(self: BitmapImage) -> bool

"""

    Metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not supported. System.Windows.Media.Imaging.BitmapImage does not support the System.Windows.Media.Imaging.BitmapImage.Metadata property and will throw a System.NotSupportedException.

Get: Metadata(self: BitmapImage) -> ImageMetadata

"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the angle that this System.Windows.Media.Imaging.BitmapImage is rotated to.

Get: Rotation(self: BitmapImage) -> Rotation

Set: Rotation(self: BitmapImage) = value
"""

    SourceRect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rectangle that is used as the source of the System.Windows.Media.Imaging.BitmapImage.

Get: SourceRect(self: BitmapImage) -> Int32Rect

Set: SourceRect(self: BitmapImage) = value
"""

    StreamSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the stream source of the System.Windows.Media.Imaging.BitmapImage.

Get: StreamSource(self: BitmapImage) -> Stream

Set: StreamSource(self: BitmapImage) = value
"""

    UriCachePolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that represents the caching policy for images that come from an HTTP source.

Get: UriCachePolicy(self: BitmapImage) -> RequestCachePolicy

Set: UriCachePolicy(self: BitmapImage) = value
"""

    UriSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Uri source of the System.Windows.Media.Imaging.BitmapImage.

Get: UriSource(self: BitmapImage) -> Uri

Set: UriSource(self: BitmapImage) = value
"""


    CacheOptionProperty = None
    CreateOptionsProperty = None
    DecodePixelHeightProperty = None
    DecodePixelWidthProperty = None
    RotationProperty = None
    SourceRectProperty = None
    StreamSourceProperty = None
    UriCachePolicyProperty = None
    UriSourceProperty = None


class BitmapMetadata(ImageMetadata, ISealable, IEnumerable, IEnumerable[str]):
    """
    Provides support for reading and writing metadata to and from a bitmap image.
    
    BitmapMetadata(containerFormat: str)
    """
    def Clone(self):
        """
        Clone(self: BitmapMetadata) -> BitmapMetadata
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.BitmapMetadata, making deep 
             copies of this object's values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property is false even if the source's System.Windows.Freezable.IsFrozen property is true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: BitmapMetadata, sourceFreezable: Freezable)
            Makes this instance a deep copy of the specified System.Windows.Media.Imaging.BitmapMetadata.
        
            sourceFreezable: The System.Windows.Media.Imaging.BitmapMetadata to clone.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: BitmapMetadata, sourceFreezable: Freezable)
            Makes this instance a modifiable deep copy of the specified 
             System.Windows.Media.Imaging.BitmapMetadata using current property values. Resource references, 
             data bindings, and animations are not copied, but their current values are.
        
        
            sourceFreezable: The System.Windows.Media.Imaging.BitmapMetadata to clone.
        """
        pass

    def ContainsQuery(self, query):
        """
        ContainsQuery(self: BitmapMetadata, query: str) -> bool
        
            Determines whether a given query string exists within a 
             System.Windows.Media.Imaging.BitmapMetadata object.
        
        
            query: Identifies the string that is being queried in the current 
             System.Windows.Media.Imaging.BitmapMetadata object.
        
            Returns: true if the query string is found within the metadata store; otherwise, false.
        """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """
        CreateInstanceCore(self: BitmapMetadata) -> Freezable
        
            An Implementation of System.Windows.Freezable.CreateInstance.
            Returns: The new instance.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Freezable, isChecking: bool) -> bool
        
            Makes the System.Windows.Freezable object unmodifiable or tests whether it can be made 
             unmodifiable.
        
        
            isChecking: true to return an indication of whether the object can be frozen (without actually freezing it); 
             false to actually freeze the object.
        
            Returns: If isChecking is true, this method returns true if the System.Windows.Freezable can be made 
             unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this method 
             returns true if the if the specified System.Windows.Freezable is now unmodifiable, or false if 
             it cannot be made unmodifiable.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: BitmapMetadata, sourceFreezable: Freezable)
            Makes this instance a clone of the specified System.Windows.Media.Imaging.BitmapMetadata object.
        
            sourceFreezable: The System.Windows.Media.Imaging.BitmapMetadata object to clone and freeze.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: BitmapMetadata, sourceFreezable: Freezable)
            Makes this instance a frozen clone of the specified System.Windows.Media.Imaging.BitmapMetadata. 
             Resource references, data bindings, and animations are not copied, but their current values are.
        
        
            sourceFreezable: The System.Windows.Media.Imaging.BitmapMetadata to copy and freeze.
        """
        pass

    def GetQuery(self, query):
        """
        GetQuery(self: BitmapMetadata, query: str) -> object
        
            Provides access to a metadata query reader that can extract metadata from a bitmap image file.
        
            query: Identifies the string that is being queried in the current 
             System.Windows.Media.Imaging.BitmapMetadata object.
        
            Returns: The metadata at the specified query location.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def RemoveQuery(self, query):
        """
        RemoveQuery(self: BitmapMetadata, query: str)
            Removes a metadata query from an instance of System.Windows.Media.Imaging.BitmapMetadata.
        
            query: The metadata query to remove.
        """
        pass

    def SetQuery(self, query, value):
        """
        SetQuery(self: BitmapMetadata, query: str, value: object)
            Provides access to a metadata query writer that can write metadata to a bitmap image file.
        
            query: Identifies the location of the metadata to be written.
            value: The value of the metadata to be written.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[str](enumerable: IEnumerable[str], value: str) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, containerFormat):
        """ __new__(cls: type, containerFormat: str) """
        pass

    ApplicationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that identifies the name of the application that was used to construct or alter an image file.

Get: ApplicationName(self: BitmapMetadata) -> str

Set: ApplicationName(self: BitmapMetadata) = value
"""

    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that represents the author of an image.

Get: Author(self: BitmapMetadata) -> ReadOnlyCollection[str]

Set: Author(self: BitmapMetadata) = value
"""

    CameraManufacturer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that identifies the camera manufacturer that is associated with an image.

Get: CameraManufacturer(self: BitmapMetadata) -> str

Set: CameraManufacturer(self: BitmapMetadata) = value
"""

    CameraModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that identifies the camera model that was used to capture the image.

Get: CameraModel(self: BitmapMetadata) -> str

Set: CameraModel(self: BitmapMetadata) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that represents a comment that is associated with the image file.

Get: Comment(self: BitmapMetadata) -> str

Set: Comment(self: BitmapMetadata) = value
"""

    Copyright = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates copyright information that is associated with the image file.

Get: Copyright(self: BitmapMetadata) -> str

Set: Copyright(self: BitmapMetadata) = value
"""

    DateTaken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates the date that the image was taken.

Get: DateTaken(self: BitmapMetadata) -> str

Set: DateTaken(self: BitmapMetadata) = value
"""

    Format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the format of the image.

Get: Format(self: BitmapMetadata) -> str

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that determines whether the System.Windows.Media.Imaging.BitmapMetadata object is a fixed size.

Get: IsFixedSize(self: BitmapMetadata) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the metadata that is associated with an image is read-only.

Get: IsReadOnly(self: BitmapMetadata) -> bool

"""

    Keywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a collection of keywords that describe the bitmap image.

Get: Keywords(self: BitmapMetadata) -> ReadOnlyCollection[str]

Set: Keywords(self: BitmapMetadata) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the base location of the metadata that is associated with an image.

Get: Location(self: BitmapMetadata) -> str

"""

    Rating = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that identifies the image rating.

Get: Rating(self: BitmapMetadata) -> int

Set: Rating(self: BitmapMetadata) = value
"""

    Subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates the subject matter of the bitmap image.

Get: Subject(self: BitmapMetadata) -> str

Set: Subject(self: BitmapMetadata) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that identifies the title of an image file.

Get: Title(self: BitmapMetadata) -> str

Set: Title(self: BitmapMetadata) = value
"""



class BitmapMetadataBlob(object):
    """
    Provides a placeholder for metadata items that cannot be converted from C# to an underlying data type that persists�metadata. The blob is converted into an array of bytes to preserve the content.
    
    BitmapMetadataBlob(blob: Array[Byte])
    """
    def GetBlobValue(self):
        """
        GetBlobValue(self: BitmapMetadataBlob) -> Array[Byte]
        
            Returns an array of bytes that represents the value of a 
             System.Windows.Media.Imaging.BitmapMetadataBlob.
        
            Returns: An array of bytes.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, blob):
        """ __new__(cls: type, blob: Array[Byte]) """
        pass


class BitmapPalette(DispatcherObject):
    """
    Defines the available color palette for a supported image type.
    
    BitmapPalette(colors: IList[Color])
    BitmapPalette(bitmapSource: BitmapSource, maxColorCount: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, colors: IList[Color])
        __new__(cls: type, bitmapSource: BitmapSource, maxColorCount: int)
        """
        pass

    Colors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the colors defined in a palette.

Get: Colors(self: BitmapPalette) -> IList[Color]

"""



class BitmapPalettes(object):
    """ Defines several color palettes that are commonly used by bitmap images. """
    BlackAndWhite = None
    BlackAndWhiteTransparent = None
    Gray16 = None
    Gray16Transparent = None
    Gray256 = None
    Gray256Transparent = None
    Gray4 = None
    Gray4Transparent = None
    Halftone125 = None
    Halftone125Transparent = None
    Halftone216 = None
    Halftone216Transparent = None
    Halftone252 = None
    Halftone252Transparent = None
    Halftone256 = None
    Halftone256Transparent = None
    Halftone27 = None
    Halftone27Transparent = None
    Halftone64 = None
    Halftone64Transparent = None
    Halftone8 = None
    Halftone8Transparent = None
    WebPalette = None
    WebPaletteTransparent = None
    __all__ = []


class BitmapSizeOptions(object):
    """ Defines size-related attributes of a cached bitmap image. A bitmap is scaled based on values that are defined by this class. """
    @staticmethod
    def FromEmptyOptions():
        """
        FromEmptyOptions() -> BitmapSizeOptions
        
            Initializes a new instance of System.Windows.Media.Imaging.BitmapSizeOptions with empty sizing 
             properties.
        
            Returns: An instance of System.Windows.Media.Imaging.BitmapSizeOptions.
        """
        pass

    @staticmethod
    def FromHeight(pixelHeight):
        """
        FromHeight(pixelHeight: int) -> BitmapSizeOptions
        
            Initializes an instance of System.Windows.Media.Imaging.BitmapSizeOptions that preserves the 
             aspect ratio of the source bitmap and specifies an initial 
             System.Windows.Media.Imaging.BitmapSizeOptions.PixelHeight.
        
        
            pixelHeight: The height, in pixels, of the resulting bitmap.
            Returns: An instance of System.Windows.Media.Imaging.BitmapSizeOptions.
        """
        pass

    @staticmethod
    def FromRotation(rotation):
        """
        FromRotation(rotation: Rotation) -> BitmapSizeOptions
        
            Initializes an instance of System.Windows.Media.Imaging.BitmapSizeOptions that preserves the 
             aspect ratio of the source bitmap and specifies an initial System.Windows.Media.Imaging.Rotation 
             to apply.
        
        
            rotation: The initial rotation value to apply. Only 90 degree increments are supported.
            Returns: A new instance of System.Windows.Media.Imaging.BitmapSizeOptions.
        """
        pass

    @staticmethod
    def FromWidth(pixelWidth):
        """
        FromWidth(pixelWidth: int) -> BitmapSizeOptions
        
            Initializes an instance of System.Windows.Media.Imaging.BitmapSizeOptions that preserves the 
             aspect ratio of the source bitmap and specifies an initial 
             System.Windows.Media.Imaging.BitmapSizeOptions.PixelWidth.
        
        
            pixelWidth: The width, in pixels, of the resulting bitmap.
            Returns: An instance of System.Windows.Media.Imaging.BitmapSizeOptions.
        """
        pass

    @staticmethod
    def FromWidthAndHeight(pixelWidth, pixelHeight):
        """
        FromWidthAndHeight(pixelWidth: int, pixelHeight: int) -> BitmapSizeOptions
        
            Initializes an instance of System.Windows.Media.Imaging.BitmapSizeOptions that does not preserve 
             the original bitmap aspect ratio.
        
        
            pixelWidth: The width, in pixels, of the resulting bitmap.
            pixelHeight: The height, in pixels, of the resulting bitmap.
            Returns: A new instance of System.Windows.Media.Imaging.BitmapSizeOptions.
        """
        pass

    PixelHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height, in pixels, of the bitmap image.

Get: PixelHeight(self: BitmapSizeOptions) -> int

"""

    PixelWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width, in pixels, of the bitmap image.

Get: PixelWidth(self: BitmapSizeOptions) -> int

"""

    PreservesAspectRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that determines whether the aspect ratio of the original bitmap image is preserved.

Get: PreservesAspectRatio(self: BitmapSizeOptions) -> bool

"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that represents the rotation angle that is applied to a bitmap.

Get: Rotation(self: BitmapSizeOptions) -> Rotation

"""



class BmpBitmapDecoder(BitmapDecoder):
    """
    Defines a decoder for bitmap (BMP) encoded images.
    
    BmpBitmapDecoder(bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    BmpBitmapDecoder(bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
        __new__(cls: type, bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
        """
        pass


class BmpBitmapEncoder(BitmapEncoder):
    """
    Defines an encoder that is used to encode bitmap (BMP) format images.
    
    BmpBitmapEncoder()
    """

class CachedBitmap(BitmapSource, ISealable, IAnimatable, IResource, IFormattable):
    """
    Provides caching functionality for a System.Windows.Media.Imaging.BitmapSource.
    
    CachedBitmap(source: BitmapSource, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    """
    def CheckIfSiteOfOrigin(self, *args): #cannot find CLR method
        """
        CheckIfSiteOfOrigin(self: BitmapSource)
            Checks whether the bitmap source content is from a known site of origin. This method is used to 
             make sure that pixel copying operations are safe.
        """
        pass

    def Clone(self):
        """
        Clone(self: CachedBitmap) -> CachedBitmap
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.CachedBitmap, making deep copies 
             of this object's values. When copying dependency properties, this method copies resource 
             references and data bindings (but they might no longer resolve) but not animations or their 
             current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: CachedBitmap, sourceFreezable: Freezable) """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: CachedBitmap) -> CachedBitmap
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.CachedBitmap object, making deep 
             copies of this object's current values. Resource references, data bindings, and animations are 
             not copied, but their current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: CachedBitmap, sourceFreezable: Freezable) """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """ CreateInstanceCore(self: CachedBitmap) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: BitmapSource, isChecking: bool) -> bool
        
            Makes an instance of System.Windows.Media.Imaging.BitmapSource or a derived class immutable.
        
            isChecking: true if this instance should actually freeze itself when this method is called; otherwise, false.
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: CachedBitmap, sourceFreezable: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: CachedBitmap, sourceFreezable: Freezable) """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, source, createOptions, cacheOption):
        """ __new__(cls: type, source: BitmapSource, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class ColorConvertedBitmap(BitmapSource, ISealable, IAnimatable, IResource, IFormattable, ISupportInitialize):
    """
    Changes the color space of a System.Windows.Media.Imaging.BitmapSource.
    
    ColorConvertedBitmap()
    ColorConvertedBitmap(source: BitmapSource, sourceColorContext: ColorContext, destinationColorContext: ColorContext, format: PixelFormat)
    """
    def BeginInit(self):
        """
        BeginInit(self: ColorConvertedBitmap)
            Signals the start of the System.Windows.Media.Imaging.ColorConvertedBitmap initialization.
        """
        pass

    def CheckIfSiteOfOrigin(self, *args): #cannot find CLR method
        """
        CheckIfSiteOfOrigin(self: BitmapSource)
            Checks whether the bitmap source content is from a known site of origin. This method is used to 
             make sure that pixel copying operations are safe.
        """
        pass

    def Clone(self):
        """
        Clone(self: ColorConvertedBitmap) -> ColorConvertedBitmap
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.ColorConvertedBitmap, making 
             deep copies of this object's values. When copying dependency properties, this method copies 
             resource references and data bindings (but they might no longer resolve) but not animations or 
             their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: ColorConvertedBitmap, source: Freezable) """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: ColorConvertedBitmap) -> ColorConvertedBitmap
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.ColorConvertedBitmap object, 
             making deep copies of this object's current values. Resource references, data bindings, and 
             animations are not copied, but their current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: ColorConvertedBitmap, source: Freezable) """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """ CreateInstanceCore(self: ColorConvertedBitmap) -> Freezable """
        pass

    def EndInit(self):
        """
        EndInit(self: ColorConvertedBitmap)
            Signals the end of the System.Windows.Media.Imaging.ColorConvertedBitmap initialization.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: BitmapSource, isChecking: bool) -> bool
        
            Makes an instance of System.Windows.Media.Imaging.BitmapSource or a derived class immutable.
        
            isChecking: true if this instance should actually freeze itself when this method is called; otherwise, false.
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: ColorConvertedBitmap, source: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: ColorConvertedBitmap, source: Freezable) """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, source=None, sourceColorContext=None, destinationColorContext=None, format=None):
        """
        __new__(cls: type)
        __new__(cls: type, source: BitmapSource, sourceColorContext: ColorContext, destinationColorContext: ColorContext, format: PixelFormat)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DestinationColorContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that identifies the color profile, as defined by the System.Windows.Media.ColorContext class, of the converted bitmap.

Get: DestinationColorContext(self: ColorConvertedBitmap) -> ColorContext

Set: DestinationColorContext(self: ColorConvertedBitmap) = value
"""

    DestinationFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that represents the System.Windows.Media.PixelFormat of the converted bitmap.

Get: DestinationFormat(self: ColorConvertedBitmap) -> PixelFormat

Set: DestinationFormat(self: ColorConvertedBitmap) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that identifies the source bitmap that is converted.

Get: Source(self: ColorConvertedBitmap) -> BitmapSource

Set: Source(self: ColorConvertedBitmap) = value
"""

    SourceColorContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that identifies the color profile of the source bitmap.

Get: SourceColorContext(self: ColorConvertedBitmap) -> ColorContext

Set: SourceColorContext(self: ColorConvertedBitmap) = value
"""


    DestinationColorContextProperty = None
    DestinationFormatProperty = None
    SourceColorContextProperty = None
    SourceProperty = None


class CroppedBitmap(BitmapSource, ISealable, IAnimatable, IResource, IFormattable, ISupportInitialize):
    """
    Crops a System.Windows.Media.Imaging.BitmapSource.
    
    CroppedBitmap()
    CroppedBitmap(source: BitmapSource, sourceRect: Int32Rect)
    """
    def BeginInit(self):
        """
        BeginInit(self: CroppedBitmap)
            Signals the start of the System.Windows.Media.Imaging.CroppedBitmap initialization.
        """
        pass

    def CheckIfSiteOfOrigin(self, *args): #cannot find CLR method
        """
        CheckIfSiteOfOrigin(self: BitmapSource)
            Checks whether the bitmap source content is from a known site of origin. This method is used to 
             make sure that pixel copying operations are safe.
        """
        pass

    def Clone(self):
        """
        Clone(self: CroppedBitmap) -> CroppedBitmap
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.CroppedBitmap, making deep 
             copies of this object's values. When copying dependency properties, this method copies resource 
             references and data bindings (but they might no longer resolve) but not animations or their 
             current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: CroppedBitmap, source: Freezable) """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: CroppedBitmap) -> CroppedBitmap
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.CroppedBitmap object, making 
             deep copies of this object's current values. Resource references, data bindings, and animations 
             are not copied, but their current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: CroppedBitmap, source: Freezable) """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """ CreateInstanceCore(self: CroppedBitmap) -> Freezable """
        pass

    def EndInit(self):
        """
        EndInit(self: CroppedBitmap)
            Signals the end of the System.Windows.Media.Imaging.CroppedBitmap initialization.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: BitmapSource, isChecking: bool) -> bool
        
            Makes an instance of System.Windows.Media.Imaging.BitmapSource or a derived class immutable.
        
            isChecking: true if this instance should actually freeze itself when this method is called; otherwise, false.
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: CroppedBitmap, source: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: CroppedBitmap, source: Freezable) """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, source=None, sourceRect=None):
        """
        __new__(cls: type)
        __new__(cls: type, source: BitmapSource, sourceRect: Int32Rect)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the source for the bitmap.

Get: Source(self: CroppedBitmap) -> BitmapSource

Set: Source(self: CroppedBitmap) = value
"""

    SourceRect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rectangular area that the bitmap is cropped to.

Get: SourceRect(self: CroppedBitmap) -> Int32Rect

Set: SourceRect(self: CroppedBitmap) = value
"""


    SourceProperty = None
    SourceRectProperty = None


class DownloadProgressEventArgs(EventArgs):
    """ Provides data for the System.Windows.Media.Imaging.BitmapSource.DownloadProgress and System.Windows.Media.Imaging.BitmapDecoder.DownloadProgress events. """
    Progress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that represents the download progress of a bitmap, expressed as a percentage.

Get: Progress(self: DownloadProgressEventArgs) -> int

"""



class FormatConvertedBitmap(BitmapSource, ISealable, IAnimatable, IResource, IFormattable, ISupportInitialize):
    """
    Provides pixel format conversion functionality for a System.Windows.Media.Imaging.BitmapSource.
    
    FormatConvertedBitmap()
    FormatConvertedBitmap(source: BitmapSource, destinationFormat: PixelFormat, destinationPalette: BitmapPalette, alphaThreshold: float)
    """
    def BeginInit(self):
        """
        BeginInit(self: FormatConvertedBitmap)
            Signals the start of the System.Windows.Media.Imaging.FormatConvertedBitmap initialization.
        """
        pass

    def CheckIfSiteOfOrigin(self, *args): #cannot find CLR method
        """
        CheckIfSiteOfOrigin(self: BitmapSource)
            Checks whether the bitmap source content is from a known site of origin. This method is used to 
             make sure that pixel copying operations are safe.
        """
        pass

    def Clone(self):
        """
        Clone(self: FormatConvertedBitmap) -> FormatConvertedBitmap
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.FormatConvertedBitmap, making 
             deep copies of this object's values. When copying dependency properties, this method copies 
             resource references and data bindings (but they might no longer resolve) but not animations or 
             their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: FormatConvertedBitmap, source: Freezable) """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: FormatConvertedBitmap) -> FormatConvertedBitmap
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.FormatConvertedBitmap object, 
             making deep copies of this object's current values. Resource references, data bindings, and 
             animations are not copied, but their current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: FormatConvertedBitmap, source: Freezable) """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """ CreateInstanceCore(self: FormatConvertedBitmap) -> Freezable """
        pass

    def EndInit(self):
        """
        EndInit(self: FormatConvertedBitmap)
            Signals the end of the System.Windows.Media.Imaging.FormatConvertedBitmap initialization.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: BitmapSource, isChecking: bool) -> bool
        
            Makes an instance of System.Windows.Media.Imaging.BitmapSource or a derived class immutable.
        
            isChecking: true if this instance should actually freeze itself when this method is called; otherwise, false.
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: FormatConvertedBitmap, source: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: FormatConvertedBitmap, source: Freezable) """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, source=None, destinationFormat=None, destinationPalette=None, alphaThreshold=None):
        """
        __new__(cls: type)
        __new__(cls: type, source: BitmapSource, destinationFormat: PixelFormat, destinationPalette: BitmapPalette, alphaThreshold: float)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AlphaThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the alpha channel threshold of a bitmap when converting to palletized formats that recognizes an alpha color.

Get: AlphaThreshold(self: FormatConvertedBitmap) -> float

Set: AlphaThreshold(self: FormatConvertedBitmap) = value
"""

    DestinationFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the pixel format to convert the bitmap to.

Get: DestinationFormat(self: FormatConvertedBitmap) -> PixelFormat

Set: DestinationFormat(self: FormatConvertedBitmap) = value
"""

    DestinationPalette = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the palette to apply to the bitmap if the format is indexed.

Get: DestinationPalette(self: FormatConvertedBitmap) -> BitmapPalette

Set: DestinationPalette(self: FormatConvertedBitmap) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the source for the bitmap.

Get: Source(self: FormatConvertedBitmap) -> BitmapSource

Set: Source(self: FormatConvertedBitmap) = value
"""


    AlphaThresholdProperty = None
    DestinationFormatProperty = None
    DestinationPaletteProperty = None
    SourceProperty = None


class GifBitmapDecoder(BitmapDecoder):
    """
    Defines a decoder for Graphics Interchange Format (GIF) encoded images.
    
    GifBitmapDecoder(bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    GifBitmapDecoder(bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
        __new__(cls: type, bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
        """
        pass


class GifBitmapEncoder(BitmapEncoder):
    """
    Defines an encoder that is used to encode Graphics Interchange Format (GIF) images.
    
    GifBitmapEncoder()
    """

class IconBitmapDecoder(BitmapDecoder):
    """
    Defines a specialized decoder for icon (.ico) encoded images.
    
    IconBitmapDecoder(bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    IconBitmapDecoder(bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
        __new__(cls: type, bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
        """
        pass


class InPlaceBitmapMetadataWriter(BitmapMetadata, ISealable, IEnumerable, IEnumerable[str]):
    """ Enables in-place updates to existing blocks of System.Windows.Media.Imaging.BitmapMetadata. """
    def Clone(self):
        """
        Clone(self: InPlaceBitmapMetadataWriter) -> InPlaceBitmapMetadataWriter
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.InPlaceBitmapMetadataWriter, 
             making deep copies of this object's values. When copying dependency properties, this method 
             copies resource references and data bindings (but they might no longer resolve) but not 
             animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: InPlaceBitmapMetadataWriter, sourceFreezable: Freezable) """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: InPlaceBitmapMetadataWriter, sourceFreezable: Freezable) """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """ CreateInstanceCore(self: InPlaceBitmapMetadataWriter) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Freezable, isChecking: bool) -> bool
        
            Makes the System.Windows.Freezable object unmodifiable or tests whether it can be made 
             unmodifiable.
        
        
            isChecking: true to return an indication of whether the object can be frozen (without actually freezing it); 
             false to actually freeze the object.
        
            Returns: If isChecking is true, this method returns true if the System.Windows.Freezable can be made 
             unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this method 
             returns true if the if the specified System.Windows.Freezable is now unmodifiable, or false if 
             it cannot be made unmodifiable.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: InPlaceBitmapMetadataWriter, sourceFreezable: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: InPlaceBitmapMetadataWriter, sourceFreezable: Freezable) """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def TrySave(self):
        """
        TrySave(self: InPlaceBitmapMetadataWriter) -> bool
        
            Gets a value that indicates whether image metadata can be saved successfully.
            Returns: true if bitmap�metadata can be written successfully; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class JpegBitmapDecoder(BitmapDecoder):
    """
    Defines a decoder for Joint Photographics Experts Group (JPEG) encoded images.
    
    JpegBitmapDecoder(bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    JpegBitmapDecoder(bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
        __new__(cls: type, bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
        """
        pass


class JpegBitmapEncoder(BitmapEncoder):
    """
    Defines an encoder that is used to encode Joint Photographics Experts Group (JPEG) format images.
    
    JpegBitmapEncoder()
    """
    FlipHorizontal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether a Joint Photographics Experts Group (JPEG) image should be flipped horizontally during encoding.

Get: FlipHorizontal(self: JpegBitmapEncoder) -> bool

Set: FlipHorizontal(self: JpegBitmapEncoder) = value
"""

    FlipVertical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether a Joint Photographics Experts Group (JPEG) image should be flipped vertically during encoding.

Get: FlipVertical(self: JpegBitmapEncoder) -> bool

Set: FlipVertical(self: JpegBitmapEncoder) = value
"""

    QualityLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates the quality level of the resulting Joint Photographics Experts Group (JPEG) image.

Get: QualityLevel(self: JpegBitmapEncoder) -> int

Set: QualityLevel(self: JpegBitmapEncoder) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that represents the degree to which a Joint Photographics Experts Group (JPEG) image is rotated.

Get: Rotation(self: JpegBitmapEncoder) -> Rotation

Set: Rotation(self: JpegBitmapEncoder) = value
"""



class LateBoundBitmapDecoder(BitmapDecoder):
    """ Defines a decoder that requires delayed bitmap creation such as asynchronous image downloads. """
    CodecInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets information that describes this codec.

Get: CodecInfo(self: LateBoundBitmapDecoder) -> BitmapCodecInfo

"""

    ColorContexts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that represents the color profile that is associated with a bitmap, if one is defined.

Get: ColorContexts(self: LateBoundBitmapDecoder) -> ReadOnlyCollection[ColorContext]

"""

    Decoder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the underlying decoder that is associated with this late-bound decoder.

Get: Decoder(self: LateBoundBitmapDecoder) -> BitmapDecoder

"""

    Frames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the content of an individual frame within a bitmap.

Get: Frames(self: LateBoundBitmapDecoder) -> ReadOnlyCollection[BitmapFrame]

"""

    IsDownloading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the decoder is currently downloading content.

Get: IsDownloading(self: LateBoundBitmapDecoder) -> bool

"""

    Palette = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Media.Imaging.BitmapPalette that is associated with this decoder.

Get: Palette(self: LateBoundBitmapDecoder) -> BitmapPalette

"""

    Preview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Windows.Media.Imaging.BitmapSource that represents the global preview of this bitmap, if one is defined.

Get: Preview(self: LateBoundBitmapDecoder) -> BitmapSource

"""

    Thumbnail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Windows.Media.Imaging.BitmapSource that represents the thumbnail of the bitmap, if one is defined.

Get: Thumbnail(self: LateBoundBitmapDecoder) -> BitmapSource

"""



class PngBitmapDecoder(BitmapDecoder):
    """
    Defines a decoder for Portable Network Graphics (PNG) encoded images.
    
    PngBitmapDecoder(bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    PngBitmapDecoder(bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
        __new__(cls: type, bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
        """
        pass


class PngBitmapEncoder(BitmapEncoder):
    """
    Defines an encoder that is used to encode Portable Network Graphics (PNG) format images.
    
    PngBitmapEncoder()
    """
    Interlace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the Portable Network Graphics (PNG) bitmap should interlace.

Get: Interlace(self: PngBitmapEncoder) -> PngInterlaceOption

Set: Interlace(self: PngBitmapEncoder) = value
"""



class PngInterlaceOption(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies whether a Portable Network Graphics (PNG) format image is interlaced during encoding.
    
    enum PngInterlaceOption, values: Default (0), Off (2), On (1)
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

    Default = None
    Off = None
    On = None
    value__ = None


class RenderTargetBitmap(BitmapSource, ISealable, IAnimatable, IResource, IFormattable):
    """
    Converts a System.Windows.Media.Visual object into a bitmap.
    
    RenderTargetBitmap(pixelWidth: int, pixelHeight: int, dpiX: float, dpiY: float, pixelFormat: PixelFormat)
    """
    def CheckIfSiteOfOrigin(self, *args): #cannot find CLR method
        """
        CheckIfSiteOfOrigin(self: BitmapSource)
            Checks whether the bitmap source content is from a known site of origin. This method is used to 
             make sure that pixel copying operations are safe.
        """
        pass

    def Clear(self):
        """
        Clear(self: RenderTargetBitmap)
            Clears the render target and sets all pixels to transparent black.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: RenderTargetBitmap, sourceFreezable: Freezable) """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: RenderTargetBitmap, sourceFreezable: Freezable) """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """ CreateInstanceCore(self: RenderTargetBitmap) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: BitmapSource, isChecking: bool) -> bool
        
            Makes an instance of System.Windows.Media.Imaging.BitmapSource or a derived class immutable.
        
            isChecking: true if this instance should actually freeze itself when this method is called; otherwise, false.
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: RenderTargetBitmap, sourceFreezable: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: RenderTargetBitmap, sourceFreezable: Freezable) """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def Render(self, visual):
        """
        Render(self: RenderTargetBitmap, visual: Visual)
            Renders the System.Windows.Media.Visual object.
        
            visual: The System.Windows.Media.Visual object to be used as a bitmap.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pixelWidth, pixelHeight, dpiX, dpiY, pixelFormat):
        """ __new__(cls: type, pixelWidth: int, pixelHeight: int, dpiX: float, dpiY: float, pixelFormat: PixelFormat) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class Rotation(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the rotation to apply to a bitmap image.
    
    enum Rotation, values: Rotate0 (0), Rotate180 (2), Rotate270 (3), Rotate90 (1)
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

    Rotate0 = None
    Rotate180 = None
    Rotate270 = None
    Rotate90 = None
    value__ = None


class TiffBitmapDecoder(BitmapDecoder):
    """
    Defines a decoder for Tagged Image File Format (TIFF) encoded images.
    
    TiffBitmapDecoder(bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    TiffBitmapDecoder(bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
        __new__(cls: type, bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
        """
        pass


class TiffBitmapEncoder(BitmapEncoder):
    """
    Defines an encoder that is used to encode Tagged Image File Format (TIFF) format images.
    
    TiffBitmapEncoder()
    """
    Compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates the type of compression that is used by this Tagged Image File Format (TIFF) image.

Get: Compression(self: TiffBitmapEncoder) -> TiffCompressOption

Set: Compression(self: TiffBitmapEncoder) = value
"""



class TiffCompressOption(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the possible compression schemes for Tagged Image File Format (TIFF)�bitmap images.
    
    enum TiffCompressOption, values: Ccitt3 (2), Ccitt4 (3), Default (0), Lzw (4), None (1), Rle (5), Zip (6)
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

    Ccitt3 = None
    Ccitt4 = None
    Default = None
    Lzw = None
    None = None
    Rle = None
    value__ = None
    Zip = None


class TransformedBitmap(BitmapSource, ISealable, IAnimatable, IResource, IFormattable, ISupportInitialize):
    """
    Scales and rotates a System.Windows.Media.Imaging.BitmapSource.
    
    TransformedBitmap()
    TransformedBitmap(source: BitmapSource, newTransform: Transform)
    """
    def BeginInit(self):
        """
        BeginInit(self: TransformedBitmap)
            Signals the start of the System.Windows.Media.Imaging.TransformedBitmap initialization.
        """
        pass

    def CheckIfSiteOfOrigin(self, *args): #cannot find CLR method
        """
        CheckIfSiteOfOrigin(self: BitmapSource)
            Checks whether the bitmap source content is from a known site of origin. This method is used to 
             make sure that pixel copying operations are safe.
        """
        pass

    def Clone(self):
        """
        Clone(self: TransformedBitmap) -> TransformedBitmap
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.TransformedBitmap, making deep 
             copies of this object's values. When copying dependency properties, this method copies resource 
             references and data bindings (but they might no longer resolve) but not animations or their 
             current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: TransformedBitmap, source: Freezable) """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: TransformedBitmap) -> TransformedBitmap
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.TransformedBitmap object, making 
             deep copies of this object's current values. Resource references, data bindings, and animations 
             are not copied, but their current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: TransformedBitmap, source: Freezable) """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """ CreateInstanceCore(self: TransformedBitmap) -> Freezable """
        pass

    def EndInit(self):
        """
        EndInit(self: TransformedBitmap)
            Signals the end of the System.Windows.Media.Imaging.BitmapImage initialization.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: BitmapSource, isChecking: bool) -> bool
        
            Makes an instance of System.Windows.Media.Imaging.BitmapSource or a derived class immutable.
        
            isChecking: true if this instance should actually freeze itself when this method is called; otherwise, false.
            Returns: If isChecking is true, this method returns true if this 
             System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be 
             made unmodifiable. If isChecking is false, this method returns true if the if this 
             System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made 
             unmodifiable, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: TransformedBitmap, source: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: TransformedBitmap, source: Freezable) """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, source=None, newTransform=None):
        """
        __new__(cls: type)
        __new__(cls: type, source: BitmapSource, newTransform: Transform)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the source for the bitmap.

Get: Source(self: TransformedBitmap) -> BitmapSource

Set: Source(self: TransformedBitmap) = value
"""

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Transform, which specifies the scale or rotation of the bitmap.

Get: Transform(self: TransformedBitmap) -> Transform

Set: Transform(self: TransformedBitmap) = value
"""


    SourceProperty = None
    TransformProperty = None


class WmpBitmapDecoder(BitmapDecoder):
    """
    Defines a decoder for Microsoft Windows Media Photo encoded images.
    
    WmpBitmapDecoder(bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    WmpBitmapDecoder(bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, bitmapUri: Uri, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
        __new__(cls: type, bitmapStream: Stream, createOptions: BitmapCreateOptions, cacheOption: BitmapCacheOption)
        """
        pass


class WmpBitmapEncoder(BitmapEncoder):
    """
    Defines an encoder that is used to encode Microsoft Windows Media Photo images.
    
    WmpBitmapEncoder()
    """
    AlphaDataDiscardLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the level of alpha frequency data to discard during a compressed domain transcode.

Get: AlphaDataDiscardLevel(self: WmpBitmapEncoder) -> Byte

Set: AlphaDataDiscardLevel(self: WmpBitmapEncoder) = value
"""

    AlphaQualityLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the compression quality for a planar alpha channel.

Get: AlphaQualityLevel(self: WmpBitmapEncoder) -> Byte

Set: AlphaQualityLevel(self: WmpBitmapEncoder) = value
"""

    CompressedDomainTranscode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether compressed domain operations can be used. Compressed domain operations are transformation operations that are done without decoding the image data.

Get: CompressedDomainTranscode(self: WmpBitmapEncoder) -> bool

Set: CompressedDomainTranscode(self: WmpBitmapEncoder) = value
"""

    FlipHorizontal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to flip the image horizontally.

Get: FlipHorizontal(self: WmpBitmapEncoder) -> bool

Set: FlipHorizontal(self: WmpBitmapEncoder) = value
"""

    FlipVertical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to flip the image vertically.

Get: FlipVertical(self: WmpBitmapEncoder) -> bool

Set: FlipVertical(self: WmpBitmapEncoder) = value
"""

    FrequencyOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to encoding in frequency order.

Get: FrequencyOrder(self: WmpBitmapEncoder) -> bool

Set: FrequencyOrder(self: WmpBitmapEncoder) = value
"""

    HorizontalTileSlices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of horizontal divisions to use during compression encoding. A single division creates two horizontal regions.

Get: HorizontalTileSlices(self: WmpBitmapEncoder) -> Int16

Set: HorizontalTileSlices(self: WmpBitmapEncoder) = value
"""

    IgnoreOverlap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to ignore region overlap pixels in subregion compressed domain encoding. This feature is not currently implemented.

Get: IgnoreOverlap(self: WmpBitmapEncoder) -> bool

Set: IgnoreOverlap(self: WmpBitmapEncoder) = value
"""

    ImageDataDiscardLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the level of image data to discard during a compressed domain transcode.

Get: ImageDataDiscardLevel(self: WmpBitmapEncoder) -> Byte

Set: ImageDataDiscardLevel(self: WmpBitmapEncoder) = value
"""

    ImageQualityLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the image quality level.

Get: ImageQualityLevel(self: WmpBitmapEncoder) -> Single

Set: ImageQualityLevel(self: WmpBitmapEncoder) = value
"""

    InterleavedAlpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to encode the alpha channel data as an additional interleaved channel.

Get: InterleavedAlpha(self: WmpBitmapEncoder) -> bool

Set: InterleavedAlpha(self: WmpBitmapEncoder) = value
"""

    Lossless = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether to encode using lossless compression.

Get: Lossless(self: WmpBitmapEncoder) -> bool

Set: Lossless(self: WmpBitmapEncoder) = value
"""

    OverlapLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the overlap processing level.

Get: OverlapLevel(self: WmpBitmapEncoder) -> Byte

Set: OverlapLevel(self: WmpBitmapEncoder) = value
"""

    QualityLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the compression quality for the main image.

Get: QualityLevel(self: WmpBitmapEncoder) -> Byte

Set: QualityLevel(self: WmpBitmapEncoder) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Imaging.Rotation of the image.

Get: Rotation(self: WmpBitmapEncoder) -> Rotation

Set: Rotation(self: WmpBitmapEncoder) = value
"""

    SubsamplingLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the sub-sampling level for RGB image encoding.

Get: SubsamplingLevel(self: WmpBitmapEncoder) -> Byte

Set: SubsamplingLevel(self: WmpBitmapEncoder) = value
"""

    UseCodecOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates codec options are to be used.

Get: UseCodecOptions(self: WmpBitmapEncoder) -> bool

Set: UseCodecOptions(self: WmpBitmapEncoder) = value
"""

    VerticalTileSlices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of vertical divisions to use during compression encoding. A single division creates two vertical regions.

Get: VerticalTileSlices(self: WmpBitmapEncoder) -> Int16

Set: VerticalTileSlices(self: WmpBitmapEncoder) = value
"""



class WriteableBitmap(BitmapSource, ISealable, IAnimatable, IResource, IFormattable):
    """
    Provides a System.Windows.Media.Imaging.BitmapSource that can be written to and updated.
    
    WriteableBitmap(source: BitmapSource)
    WriteableBitmap(pixelWidth: int, pixelHeight: int, dpiX: float, dpiY: float, pixelFormat: PixelFormat, palette: BitmapPalette)
    """
    def AddDirtyRect(self, dirtyRect):
        """
        AddDirtyRect(self: WriteableBitmap, dirtyRect: Int32Rect)
            Specifies the area of the bitmap that changed.
        
            dirtyRect: An System.Windows.Int32Rect representing the area that changed. Dimensions are in pixels.
        """
        pass

    def CheckIfSiteOfOrigin(self, *args): #cannot find CLR method
        """
        CheckIfSiteOfOrigin(self: BitmapSource)
            Checks whether the bitmap source content is from a known site of origin. This method is used to 
             make sure that pixel copying operations are safe.
        """
        pass

    def Clone(self):
        """
        Clone(self: WriteableBitmap) -> WriteableBitmap
        
            Creates a modifiable clone of this System.Windows.Media.Imaging.WriteableBitmap, making deep 
             copies of this object's values. When copying dependency properties, this method copies resource 
             references and data bindings (but they might no longer resolve) but not animations or their 
             current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: WriteableBitmap, sourceFreezable: Freezable) """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: WriteableBitmap) -> WriteableBitmap
        
            Creates a modifiable clone of this System.Windows.Media.Animation.ByteAnimationUsingKeyFrames 
             object, making deep copies of this object's current values. Resource references, data bindings, 
             and animations are not copied, but their current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 
             property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: WriteableBitmap, sourceFreezable: Freezable) """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """ CreateInstanceCore(self: WriteableBitmap) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """ FreezeCore(self: WriteableBitmap, isChecking: bool) -> bool """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: WriteableBitmap, sourceFreezable: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: WriteableBitmap, sourceFreezable: Freezable) """
        pass

    def Lock(self):
        """
        Lock(self: WriteableBitmap)
            Reserves the back buffer for updates.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 
             intended to be used directly from your code.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a 
             System.Windows.DependencyObjectType data member that has just been set.
        
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr
             gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 
             dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 
             System.Windows.Freezable must call this method at the beginning of any API that reads data 
             members that are not dependency properties.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for 
             the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def TryLock(self, timeout):
        """
        TryLock(self: WriteableBitmap, timeout: Duration) -> bool
        
            Attempts to lock the bitmap, waiting for no longer than the specified length of time.
        
            timeout: A System.Windows.Duration that represents the length of time to wait. A value of 0 returns 
             immediately. A value of System.Windows.Duration.Forever blocks indefinitely.
        
            Returns: true if the lock was acquired; otherwise, false.
        """
        pass

    def Unlock(self):
        """
        Unlock(self: WriteableBitmap)
            Releases the back buffer to make it available for display.
        """
        pass

    def WritePixels(self, sourceRect, *__args):
        """
        WritePixels(self: WriteableBitmap, sourceRect: Int32Rect, buffer: IntPtr, bufferSize: int, stride: int)
            Updates the pixels in the specified region of the bitmap.
        
            sourceRect: The rectangle of the System.Windows.Media.Imaging.WriteableBitmap to update.
            buffer: The input buffer used to update the bitmap.
            bufferSize: The size of the input buffer.
            stride: The stride of the update region in buffer.
        WritePixels(self: WriteableBitmap, sourceRect: Int32Rect, pixels: Array, stride: int, offset: int)
            Updates the pixels in the specified region of the bitmap.
        
            sourceRect: The rectangle of the System.Windows.Media.Imaging.WriteableBitmap to update.
            pixels: The pixel array used to update the bitmap.
            stride: The stride of the update region in pixels.
            offset: The input buffer offset.
        WritePixels(self: WriteableBitmap, sourceRect: Int32Rect, sourceBuffer: IntPtr, sourceBufferSize: int, sourceBufferStride: int, destinationX: int, destinationY: int)
            Updates the pixels in the specified region of the bitmap.
        
            sourceRect: The rectangle in sourceBuffer to copy.
            sourceBuffer: The input buffer used to update the bitmap.
            sourceBufferSize: The size of the input buffer.
            sourceBufferStride: The stride of the input buffer, in bytes.
            destinationX: The destination x-coordinate of the left-most pixel in the back buffer.
            destinationY: The destination y-coordinate of the top-most pixel in the back buffer.
        WritePixels(self: WriteableBitmap, sourceRect: Int32Rect, sourceBuffer: Array, sourceBufferStride: int, destinationX: int, destinationY: int)
            Updates the pixels in the specified region of the bitmap.
        
            sourceRect: The rectangle in sourceBuffer to copy.
            sourceBuffer: The input buffer used to update the bitmap.
            sourceBufferStride: The stride of the input buffer, in bytes.
            destinationX: The destination x-coordinate of the left-most pixel in the back buffer.
            destinationY: The destination y-coordinate of the top-most pixel in the back buffer.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 
             its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 
             should call this method at the end of any API that modifies class members that are not stored as 
             dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 
             valid threading context. System.Windows.Freezable inheritors should call this method at the 
             beginning of any API that writes to data members that are not dependency properties.
        """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, source: BitmapSource)
        __new__(cls: type, pixelWidth: int, pixelHeight: int, dpiX: float, dpiY: float, pixelFormat: PixelFormat, palette: BitmapPalette)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BackBuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a pointer to the back buffer.

Get: BackBuffer(self: WriteableBitmap) -> IntPtr

"""

    BackBufferStride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating the number of bytes in a single row of pixel data.

Get: BackBufferStride(self: WriteableBitmap) -> int

"""



