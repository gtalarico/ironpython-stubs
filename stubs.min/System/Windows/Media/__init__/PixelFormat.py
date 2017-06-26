class PixelFormat(object, IEquatable[PixelFormat]):
    """ Defines a pixel format for images and pixel-based surfaces. """
    def Equals(self, *__args):
        """
        Equals(self: PixelFormat, pixelFormat: PixelFormat) -> bool
        
            Determines whether the pixel format equals the given System.Windows.Media.PixelFormat.
        
            pixelFormat: The pixel format to compare.
            Returns: true if the pixel formats are equal; otherwise, false.
        Equals(left: PixelFormat, right: PixelFormat) -> bool
        
            Determines whether the specified System.Windows.Media.PixelFormat instances are considered equal.
        
            left: The first System.Windows.Media.PixelFormat objects to compare for equality.
            right: The second System.Windows.Media.PixelFormat object to compare for equality.
            Returns: true if the two parameters are equal; otherwise, false.
        Equals(self: PixelFormat, obj: object) -> bool
        
            Determines whether the specified object is equal to the current object.
        
            obj: The Object to compare with the current Object.
            Returns: true if the System.Windows.Media.PixelFormat is equal to obj; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PixelFormat) -> int
        
            Creates a hash code from this pixel format's System.Windows.Media.PixelFormat.Masks value.
            Returns: The pixel format's hash code.
        """
        pass

    def ToString(self):
        """
        ToString(self: PixelFormat) -> str
        
            Creates a string representation of this System.Windows.Media.PixelFormat.
            Returns: A System.String containing a representation of the System.Windows.Media.PixelFormat.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BitsPerPixel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of bits-per-pixel (bpp) for this System.Windows.Media.PixelFormat.

Get: BitsPerPixel(self: PixelFormat) -> int

"""

    Masks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of bit masks associated with the System.Windows.Media.PixelFormat.

Get: Masks(self: PixelFormat) -> IList[PixelFormatChannelMask]

"""


