class Color(object, IFormattable, IEquatable[Color]):
    """ Describes a color in terms of alpha, red, green, and blue channels. """
    @staticmethod
    def Add(color1, color2):
        """
        Add(color1: Color, color2: Color) -> Color
        
            Adds two System.Windows.Media.Color structures.
        
            color1: The first System.Windows.Media.Color structure to add.
            color2: The second System.Windows.Media.Color structure to add.
            Returns: A new System.Windows.Media.Color structure whose color values are the results of the addition operation.
        """
        pass

    @staticmethod
    def AreClose(color1, color2):
        """
        AreClose(color1: Color, color2: Color) -> bool
        
            Compares two System.Windows.Media.Color structures for fuzzy equality.
        
            color1: The first color to compare.
            color2: The second color to compare.
            Returns: true if color1 and color2 are nearly identical; otherwise, false.
        """
        pass

    def Clamp(self):
        """
        Clamp(self: Color)
            Sets the ScRGB channels of the color to within the gamut of 0 to 1, if they are outside that range.
        """
        pass

    @staticmethod
    def Equals(*__args):
        """
        Equals(self: Color, o: object) -> bool
        
            Tests whether the specified object is a System.Windows.Media.Color structure and is equivalent to the current color.
        
            o: The object to compare to the current System.Windows.Media.Color structure.
            Returns: true if the specified object is a System.Windows.Media.Color structure and is identical to the current System.Windows.Media.Color structure; otherwise, false.
        Equals(self: Color, color: Color) -> bool
        
            Tests whether the specified System.Windows.Media.Color structure is identical to the current color.
        
            color: The System.Windows.Media.Color structure to compare to the current System.Windows.Media.Color structure.
            Returns: true if the specified System.Windows.Media.Color structure is identical to the current System.Windows.Media.Color structure; otherwise, false.
        Equals(color1: Color, color2: Color) -> bool
        
            Tests whether two System.Windows.Media.Color structures are identical.
        
            color1: The first System.Windows.Media.Color structure to compare.
            color2: The second System.Windows.Media.Color structure to compare.
            Returns: true if color1 and color2 are exactly identical; otherwise, false.
        """
        pass

    @staticmethod
    def FromArgb(a, r, g, b):
        """
        FromArgb(a: Byte, r: Byte, g: Byte, b: Byte) -> Color
        
            Creates a new System.Windows.Media.Color structure by using the specified sRGB alpha channel and color channel values.
        
            a: The alpha channel, System.Windows.Media.Color.A, of the new color.
            r: The red channel, System.Windows.Media.Color.R, of the new color.
            g: The green channel, System.Windows.Media.Color.G, of the new color.
            b: The blue channel, System.Windows.Media.Color.B, of the new color.
            Returns: A System.Windows.Media.Color structure with the specified values.
        """
        pass

    @staticmethod
    def FromAValues(a, values, profileUri):
        """
        FromAValues(a: Single, values: Array[Single], profileUri: Uri) -> Color
        
            Creates a new System.Windows.Media.Color structure by using the specified alpha channel, color channel values, and color profile.
        
            a: The alpha channel for the new color.
            values: A collection of values that specify the color channels for the new color. These values map to the profileUri.
            profileUri: The International Color Consortium (ICC) or Image Color Management (ICM) color profile for the new color.
            Returns: A System.Windows.Media.Color structure with the specified values.
        """
        pass

    @staticmethod
    def FromRgb(r, g, b):
        """
        FromRgb(r: Byte, g: Byte, b: Byte) -> Color
        
            Creates a new System.Windows.Media.Color structure by using the specified sRGB color channel values.
        
            r: The sRGB red channel, System.Windows.Media.Color.R, of the new color.
            g: The sRGB green channel, System.Windows.Media.Color.G, of the new color.
            b: The sRGB blue channel, System.Windows.Media.Color.B, of the new color.
            Returns: A System.Windows.Media.Color structure with the specified values and an alpha channel value of 1.
        """
        pass

    @staticmethod
    def FromScRgb(a, r, g, b):
        """
        FromScRgb(a: Single, r: Single, g: Single, b: Single) -> Color
        
            Creates a new System.Windows.Media.Color structure by using the specified ScRGB alpha channel and color channel values.
        
            a: The ScRGB alpha channel, System.Windows.Media.Color.ScA, of the new color.
            r: The ScRGB red channel, System.Windows.Media.Color.ScR, of the new color.
            g: The ScRGB green channel, System.Windows.Media.Color.ScG, of the new color.
            b: The ScRGB blue channel, System.Windows.Media.Color.ScB, of the new color.
            Returns: A System.Windows.Media.Color structure with the specified values.
        """
        pass

    @staticmethod
    def FromValues(values, profileUri):
        """
        FromValues(values: Array[Single], profileUri: Uri) -> Color
        
            Creates a new System.Windows.Media.Color structure by using the specified color channel values and color profile.
        
            values: A collection of values that specify the color channels for the new color. These values map to the profileUri.
            profileUri: The International Color Consortium (ICC) or Image Color Management (ICM) color profile for the new color.
            Returns: A System.Windows.Media.Color structure with the specified values and an alpha channel value of 1.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Color) -> int
        
            Gets a hash code for the current System.Windows.Media.Color structure.
            Returns: A hash code for the current System.Windows.Media.Color structure.
        """
        pass

    def GetNativeColorValues(self):
        """
        GetNativeColorValues(self: Color) -> Array[Single]
        
            Gets the color channel values of the color.
            Returns: An array of color channel values.
        """
        pass

    @staticmethod
    def Multiply(color, coefficient):
        """
        Multiply(color: Color, coefficient: Single) -> Color
        
            Multiplies the alpha, red, blue, and green channels of the specified System.Windows.Media.Color structure by the specified value.
        
            color: The System.Windows.Media.Color to be multiplied.
            coefficient: The value to multiply by.
            Returns: A new System.Windows.Media.Color structure whose color values are the results of the multiplication operation.
        """
        pass

    @staticmethod
    def Subtract(color1, color2):
        """
        Subtract(color1: Color, color2: Color) -> Color
        
            Subtracts a System.Windows.Media.Color structure from a System.Windows.Media.Color structure.
        
            color1: The System.Windows.Media.Color structure to be subtracted from.
            color2: The System.Windows.Media.Color structure to subtract from color1.
            Returns: A new System.Windows.Media.Color structure whose color values are the results of the subtraction operation.
        """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: Color, provider: IFormatProvider) -> str
        
            Creates a string representation of the color by using the ScRGB channels and the specified format provider.
        
            provider: Culture-specific formatting information.
            Returns: The string representation of the color.
        ToString(self: Color) -> str
        
            Creates a string representation of the color using the ScRGB channels.
            Returns: The string representation of the color.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(color1: Color, color2: Color) -> Color
        
            Adds two System.Windows.Media.Color structures.
        
            color1: The first System.Windows.Media.Color structure to add.
            color2: The second System.Windows.Media.Color structure to add.
            Returns: A new System.Windows.Media.Color structure whose color values are the results of the addition operation.
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(color1: Color, color2: Color) -> Color
        
            Subtracts a System.Windows.Media.Color structure from a System.Windows.Media.Color structure.
        
            color1: The System.Windows.Media.Color structure to be subtracted from.
            color2: The System.Windows.Media.Color structure to subtract from color1.
            Returns: A new System.Windows.Media.Color structure whose color values are the results of the subtraction operation.
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the sRGB alpha channel value of the color.

Get: A(self: Color) -> Byte

Set: A(self: Color) = value
"""

    B = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the sRGB blue channel value of the color.

Get: B(self: Color) -> Byte

Set: B(self: Color) = value
"""

    ColorContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the International Color Consortium (ICC) or Image Color Management (ICM) color profile of the color.

Get: ColorContext(self: Color) -> ColorContext

"""

    G = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the sRGB green channel value of the color.

Get: G(self: Color) -> Byte

Set: G(self: Color) = value
"""

    R = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the sRGB red channel value of the color.

Get: R(self: Color) -> Byte

Set: R(self: Color) = value
"""

    ScA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the ScRGB alpha channel value of the color.

Get: ScA(self: Color) -> Single

Set: ScA(self: Color) = value
"""

    ScB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the ScRGB blue channel value of the color.

Get: ScB(self: Color) -> Single

Set: ScB(self: Color) = value
"""

    ScG = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the ScRGB green channel value of the color.

Get: ScG(self: Color) -> Single

Set: ScG(self: Color) = value
"""

    ScR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the ScRGB red channel value of the color.

Get: ScR(self: Color) -> Single

Set: ScR(self: Color) = value
"""


