class PixelFormatChannelMask(object):
    """ Defines the bit mask and shift for a specific pixel formats """
    @staticmethod
    def Equals(*__args):
        """
        Equals(self: PixelFormatChannelMask, obj: object) -> bool
        
            Determines whether the specified object is equal to the current object.
        
            obj: The System.Object to compare with the current mask.
            Returns: true if the System.Windows.Media.PixelFormatChannelMask is equal to obj; otherwise, false.
        Equals(left: PixelFormatChannelMask, right: PixelFormatChannelMask) -> bool
        
            Determines if two pixel format channel masks are equal.
        
            left: The first mask to compare.
            right: The second mask to compare.
            Returns: true if the masks are equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PixelFormatChannelMask) -> int
        
            Retrieves a hash code for the mask.
            Returns: A mask's hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the bitmask for a color channel. The value will never be greater then 0xffffffff

Get: Mask(self: PixelFormatChannelMask) -> IList[Byte]

"""


