# encoding: utf-8
# module Rhino.Display calls itself Display
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BackgroundStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Contains enumerated constants that define how the background of
                a viewport should be filled.
    
    enum BackgroundStyle, values: Environment (3), Gradient (2), SolidColor (0), WallpaperImage (1)
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

    Environment = None
    Gradient = None
    SolidColor = None
    value__ = None
    WallpaperImage = None


class BlendMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enmerated constants for display blend modes.
    
    enum BlendMode, values: DestinationAlpha (772), DestinationColor (774), One (1), OneMinusDestinationAlpha (773), OneMinusDestinationColor (775), OneMinusSourceAlpha (771), OneMinusSourceColor (769), SourceAlpha (770), SourceAlphaSaturate (776), SourceColor (768), Zero (0)
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

    DestinationAlpha = None
    DestinationColor = None
    One = None
    OneMinusDestinationAlpha = None
    OneMinusDestinationColor = None
    OneMinusSourceAlpha = None
    OneMinusSourceColor = None
    SourceAlpha = None
    SourceAlphaSaturate = None
    SourceColor = None
    value__ = None
    Zero = None


class DrawEventArgs(EventArgs):
    # no doc
    Display = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Display(self: DrawEventArgs) -> DisplayPipeline

"""

    RhinoDoc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RhinoDoc(self: DrawEventArgs) -> RhinoDoc

"""

    Viewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Viewport(self: DrawEventArgs) -> RhinoViewport

"""



class CalculateBoundingBoxEventArgs(DrawEventArgs):
    # no doc
    def IncludeBoundingBox(self, box):
        """
        IncludeBoundingBox(self: CalculateBoundingBoxEventArgs, box: BoundingBox)
            Unites a bounding box with the current display bounding box in order to ensure
                    
             dynamic objects in "box" are drawn.
        
        
            box: The box to unite.
        """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current bounding box.

Get: BoundingBox(self: CalculateBoundingBoxEventArgs) -> BoundingBox

"""



class Color4f(object, ISerializable):
    """
    Color defined by 4 floating point values.
    
    Color4f(color: Color)
    Color4f(color: Color4f)
    Color4f(red: Single, green: Single, blue: Single, alpha: Single)
    """
    def AsSystemColor(self):
        """ AsSystemColor(self: Color4f) -> Color """
        pass

    def BlendTo(self, t, col):
        """ BlendTo(self: Color4f, t: Single, col: Color4f) -> Color4f """
        pass

    def Equals(self, obj):
        """ Equals(self: Color4f, obj: object) -> bool """
        pass

    @staticmethod
    def FromArgb(a, *__args):
        """
        FromArgb(a: Single, color: Color4f) -> Color4f
        FromArgb(a: Single, r: Single, g: Single, b: Single) -> Color4f
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Color4f) -> int """
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
        __new__[Color4f]() -> Color4f
        
        __new__(cls: type, color: Color)
        __new__(cls: type, color: Color4f)
        __new__(cls: type, red: Single, green: Single, blue: Single, alpha: Single)
        """
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

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: A(self: Color4f) -> Single

"""

    B = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: B(self: Color4f) -> Single

"""

    G = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: G(self: Color4f) -> Single

"""

    R = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: R(self: Color4f) -> Single

"""


    Black = None
    Empty = None
    White = None


class ColorCMYK(object):
    """
    Represents a CMYK (Cyan, Magenta, Yellow, Key) color with double precision floating point channels. 
                CMYK colors are used primarily in printing environments as they provide a good simulation of physical ink.
    
    ColorCMYK(rgb: Color)
    ColorCMYK(cyan: float, magenta: float, yellow: float)
    ColorCMYK(cyan: float, magenta: float, yellow: float, key: float)
    ColorCMYK(alpha: float, cyan: float, magenta: float, yellow: float, key: float)
    """
    @staticmethod
    def CreateFromHSL(hsl):
        """
        CreateFromHSL(hsl: ColorHSL) -> ColorCMYK
        
            Constructs the nearest CMYK equivalent of an HSL color.
        
            hsl: Target color in HSL space.
            Returns: The CMYK equivalent of the HSL color.
        """
        pass

    @staticmethod
    def CreateFromLAB(lab):
        """
        CreateFromLAB(lab: ColorLAB) -> ColorCMYK
        
            Constructs the nearest CMYK equivalent of a LAB color.
        
            lab: Target color in LAB space.
            Returns: The CMYK equivalent of the LAB color.
        """
        pass

    @staticmethod
    def CreateFromLCH(lch):
        """
        CreateFromLCH(lch: ColorLCH) -> ColorCMYK
        
            Constructs the nearest CMYK equivalent of a LCH color.
        
            lch: Target color in LCH space.
            Returns: The CMYK equivalent of the LCH color.
        """
        pass

    @staticmethod
    def CreateFromXYZ(xyz):
        """
        CreateFromXYZ(xyz: ColorXYZ) -> ColorCMYK
        
            Constructs the nearest CMYK equivalent of an XYZ color.
        
            xyz: Target color in XYZ space.
            Returns: The CMYK equivalent of the XYZ color.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[ColorCMYK]() -> ColorCMYK
        
        __new__(cls: type, rgb: Color)
        __new__(cls: type, cyan: float, magenta: float, yellow: float)
        __new__(cls: type, cyan: float, magenta: float, yellow: float, key: float)
        __new__(cls: type, alpha: float, cyan: float, magenta: float, yellow: float, key: float)
        """
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Alpha channel value. 
            Alpha channels are limited to the 0~1 range.

Get: A(self: ColorCMYK) -> float

Set: A(self: ColorCMYK) = value
"""

    C = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Cyan channel value. 
            Cyan channels are limited to the 0~1 range.

Get: C(self: ColorCMYK) -> float

Set: C(self: ColorCMYK) = value
"""

    K = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Key channel value. 
            Key channels are limited to the 0~1 range.

Get: K(self: ColorCMYK) -> float

Set: K(self: ColorCMYK) = value
"""

    M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Magenta channel value. 
            Magenta channels are limited to the 0~1 range.

Get: M(self: ColorCMYK) -> float

Set: M(self: ColorCMYK) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Yellow channel value. 
            Yellow channels are limited to the 0~1 range.

Get: Y(self: ColorCMYK) -> float

Set: Y(self: ColorCMYK) = value
"""



class ColorHSL(object):
    """
    Represents an HSL (Hue, Saturation, Luminance) color with double precision floating point channels. 
                HSL colors are used primarily in Graphical User Interface environments as they provide a 
                very natural approach to picking colors.
    
    ColorHSL(rgb: Color)
    ColorHSL(hue: float, saturation: float, luminance: float)
    ColorHSL(alpha: float, hue: float, saturation: float, luminance: float)
    """
    @staticmethod
    def CreateFromCMYK(cmyk):
        """
        CreateFromCMYK(cmyk: ColorCMYK) -> ColorHSL
        
            Create the nearest HSL equivalent of a CMYK color.
        
            cmyk: Target color in CMYK space.
            Returns: The HSL equivalent of the CMYK color.
        """
        pass

    @staticmethod
    def CreateFromLAB(lab):
        """
        CreateFromLAB(lab: ColorLAB) -> ColorHSL
        
            Create the nearest HSL equivalent of a LAB color.
        
            lab: Target color in LAB space.
            Returns: The HSL equivalent of the LAB color.
        """
        pass

    @staticmethod
    def CreateFromLCH(lch):
        """
        CreateFromLCH(lch: ColorLCH) -> ColorHSL
        
            Create the nearest HSL equivalent of a LCH color.
        
            lch: Target color in LCH space.
            Returns: The HSL equivalent of the LCH color.
        """
        pass

    @staticmethod
    def CreateFromXYZ(xyz):
        """
        CreateFromXYZ(xyz: ColorXYZ) -> ColorHSL
        
            Create the nearest HSL equivalent of an XYZ color.
        
            xyz: Target color in XYZ space.
            Returns: The HSL equivalent of the XYZ color.
        """
        pass

    def ToArgbColor(self):
        """
        ToArgbColor(self: ColorHSL) -> Color
        
            Convert HSL color to an equivalent System.Drawing.Color.
            Returns: A .Net framework library color value.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[ColorHSL]() -> ColorHSL
        
        __new__(cls: type, rgb: Color)
        __new__(cls: type, hue: float, saturation: float, luminance: float)
        __new__(cls: type, alpha: float, hue: float, saturation: float, luminance: float)
        """
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the alpha channel value. 
            Alpha channels are limited to a 0~1 range.

Get: A(self: ColorHSL) -> float

Set: A(self: ColorHSL) = value
"""

    H = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the hue channel value. 
            Hue channels rotate between 0.0 and 1.0.

Get: H(self: ColorHSL) -> float

Set: H(self: ColorHSL) = value
"""

    L = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the luminance channel value. 
            Luminance channels are limited to a 0~1 range.

Get: L(self: ColorHSL) -> float

Set: L(self: ColorHSL) = value
"""

    S = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the saturation channel value. 
            Saturation channels are limited to a 0~1 range.

Get: S(self: ColorHSL) -> float

Set: S(self: ColorHSL) = value
"""



class ColorLAB(object):
    """
    Represents a LAB (Lightness, A, B) color with double precision floating point channels. 
                LAB colors are based on nonlinearly compressed CIE XYZ color space coordinates.  
                The A and B parameters of a LAB color represent the opponents.
    
    ColorLAB(rgb: Color)
    ColorLAB(lightness: float, a: float, b: float)
    ColorLAB(alpha: float, lightness: float, a: float, b: float)
    """
    @staticmethod
    def CreateFromCMYK(cmyk):
        """
        CreateFromCMYK(cmyk: ColorCMYK) -> ColorLAB
        
            Create the nearest LAB equivalent of a CMYK color.
        
            cmyk: Target color in CMYK space.
            Returns: The LAB equivalent of the CMYK color.
        """
        pass

    @staticmethod
    def CreateFromHSL(hsl):
        """
        CreateFromHSL(hsl: ColorHSL) -> ColorLAB
        
            Create the nearest LAB equivalent of an HSL color.
        
            hsl: Target color in HSL space.
            Returns: The LAB equivalent of the HSL color.
        """
        pass

    @staticmethod
    def CreateFromLCH(lch):
        """
        CreateFromLCH(lch: ColorLCH) -> ColorLAB
        
            Create the nearest LAB equivalent of an LCH color.
        
            lch: Target color in LCH space.
            Returns: The LAB equivalent of the LCH color.
        """
        pass

    @staticmethod
    def CreateFromXYZ(xyz):
        """
        CreateFromXYZ(xyz: ColorXYZ) -> ColorLAB
        
            Create the nearest LAB equivalent of an XYZ color.
        
            xyz: Target color in XYZ space.
            Returns: The LAB equivalent of the XYZ color.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[ColorLAB]() -> ColorLAB
        
        __new__(cls: type, rgb: Color)
        __new__(cls: type, lightness: float, a: float, b: float)
        __new__(cls: type, alpha: float, lightness: float, a: float, b: float)
        """
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Base channel. The channel is limited to 0~1.

Get: A(self: ColorLAB) -> float

Set: A(self: ColorLAB) = value
"""

    Alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Alpha channel. The channel is limited to 0~1.

Get: Alpha(self: ColorLAB) -> float

Set: Alpha(self: ColorLAB) = value
"""

    B = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Opponent channel. The channel is limited to 0~1.

Get: B(self: ColorLAB) -> float

Set: B(self: ColorLAB) = value
"""

    L = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the lightness channel. The channel is limited to 0~1.

Get: L(self: ColorLAB) -> float

Set: L(self: ColorLAB) = value
"""



class ColorLCH(object):
    """
    Represents an LCH (Lightness, A, B) color with double precision floating point channels. 
                LCH colors (also sometimes called CIELUV) are transformation of the 1931 CIE XYZ color space, 
                in order to approach perceptual uniformity. They are primarily used in computer graphics which 
                deal with colored lights.
    
    ColorLCH(rgb: Color)
    ColorLCH(lightness: float, chroma: float, hue: float)
    ColorLCH(alpha: float, lightness: float, chroma: float, hue: float)
    """
    @staticmethod
    def CreateFromCMYK(cmyk):
        """
        CreateFromCMYK(cmyk: ColorCMYK) -> ColorLCH
        
            Create the nearest LCH equivalent of a CMYK color.
        
            cmyk: Target color in CMYK space.
            Returns: The LCH equivalent of the CMYK color.
        """
        pass

    @staticmethod
    def CreateFromHSL(hsl):
        """
        CreateFromHSL(hsl: ColorHSL) -> ColorLCH
        
            Create the nearest LCH equivalent of an HSL color.
        
            hsl: Target color in HSL space.
            Returns: The LCH equivalent of the HSL color.
        """
        pass

    @staticmethod
    def CreateFromLAB(lab):
        """
        CreateFromLAB(lab: ColorLAB) -> ColorLCH
        
            Create the nearest LCH equivalent of a LAB color.
        
            lab: Target color in LAB space.
            Returns: The LCH equivalent of the LAB color.
        """
        pass

    @staticmethod
    def CreateFromXYZ(xyz):
        """
        CreateFromXYZ(xyz: ColorXYZ) -> ColorLCH
        
            Create the nearest LCH equivalent of an XYZ color.
        
            xyz: Target color in XYZ space.
            Returns: The LCH equivalent of the XYZ color.
        """
        pass

    def MakePositive(self):
        """
        MakePositive(self: ColorLCH)
            Ensure the Chromaticity of this color is positive.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[ColorLCH]() -> ColorLCH
        
        __new__(cls: type, rgb: Color)
        __new__(cls: type, lightness: float, chroma: float, hue: float)
        __new__(cls: type, alpha: float, lightness: float, chroma: float, hue: float)
        """
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Alpha channel. The Alpha channel is limited to the 0~1 range.

Get: A(self: ColorLCH) -> float

Set: A(self: ColorLCH) = value
"""

    C = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Chroma channel. Chroma is defined from -1.0 to +1.0.

Get: C(self: ColorLCH) -> float

Set: C(self: ColorLCH) = value
"""

    H = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Hue channel. The hue channel is limited to the 0~360 degree range.

Get: H(self: ColorLCH) -> float

Set: H(self: ColorLCH) = value
"""

    L = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Lightness channel.

Get: L(self: ColorLCH) -> float

Set: L(self: ColorLCH) = value
"""



class ColorXYZ(object):
    """
    Represents an XYZ (Hue, Saturation, Luminance) color with double precision floating point channels. 
                XYZ colors are based on the CIE 1931 XYZ color space standard and they mimic the natural 
                sensitivity of cones in the human retina.
    
    ColorXYZ(rgb: Color)
    ColorXYZ(x: float, y: float, z: float)
    ColorXYZ(alpha: float, x: float, y: float, z: float)
    """
    @staticmethod
    def CreateFromCMYK(cmyk):
        """
        CreateFromCMYK(cmyk: ColorCMYK) -> ColorXYZ
        
            Create the nearest XYZ equivalent of a CMYK color.
        
            cmyk: Target color in CMYK space.
            Returns: The XYZ equivalent of the CMYK color.
        """
        pass

    @staticmethod
    def CreateFromHSL(hsl):
        """
        CreateFromHSL(hsl: ColorHSL) -> ColorXYZ
        
            Create the nearest XYZ equivalent of an HSL color.
        
            hsl: Target color in HSL space.
            Returns: The XYZ equivalent of the HSL color.
        """
        pass

    @staticmethod
    def CreateFromLAB(lab):
        """
        CreateFromLAB(lab: ColorLAB) -> ColorXYZ
        
            Create the nearest XYZ equivalent of a Lab color.
        
            lab: Target color in LAB space.
            Returns: The XYZ equivalent of the LAB color.
        """
        pass

    @staticmethod
    def CreateFromLCH(lch):
        """
        CreateFromLCH(lch: ColorLCH) -> ColorXYZ
        
            Create the nearest XYZ equivalent of an LCH color.
        
            lch: Target color in LCH space.
            Returns: The XYZ equivalent of the LCH color.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[ColorXYZ]() -> ColorXYZ
        
        __new__(cls: type, rgb: Color)
        __new__(cls: type, x: float, y: float, z: float)
        __new__(cls: type, alpha: float, x: float, y: float, z: float)
        """
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or set the Alpha channel value. Channel will be limited to 0~1.

Get: A(self: ColorXYZ) -> float

Set: A(self: ColorXYZ) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or set the X channel value. Channel will be limited to 0~1.

Get: X(self: ColorXYZ) -> float

Set: X(self: ColorXYZ) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or set the Y channel value. Channel will be limited to 0~1.

Get: Y(self: ColorXYZ) -> float

Set: Y(self: ColorXYZ) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or set the Z channel value. Channel will be limited to 0~1.

Get: Z(self: ColorXYZ) -> float

Set: Z(self: ColorXYZ) = value
"""



class CullFaceMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum CullFaceMode, values: DrawBackFaces (2), DrawFrontAndBack (0), DrawFrontFaces (1) """
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

    DrawBackFaces = None
    DrawFrontAndBack = None
    DrawFrontFaces = None
    value__ = None


class CullObjectEventArgs(DrawEventArgs):
    # no doc
    CullObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CullObject(self: CullObjectEventArgs) -> bool

Set: CullObject(self: CullObjectEventArgs) = value
"""

    RhinoObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RhinoObject(self: CullObjectEventArgs) -> RhinoObject

"""



class CustomDisplay(object, IDisposable):
    """
    Provides some basic (indeed, very basic) mechanisms for drawing custom geometry in viewports.
    
    CustomDisplay(enable: bool)
    """
    def AddArc(self, arc, color=None, thickness=None):
        """
        AddArc(self: CustomDisplay, arc: Arc, color: Color, thickness: int)
            Adds a new, colored arc to the display list.
        
            arc: Arc to add.
            color: Color of arc.
            thickness: Thickness of arc.
        AddArc(self: CustomDisplay, arc: Arc, color: Color)
            Adds a new, colored arc to the display list.
        
            arc: Arc to add.
            color: Color of arc.
        AddArc(self: CustomDisplay, arc: Arc)
            Adds a new, black arc to the display list.
        
            arc: Arc to add.
        """
        pass

    def AddCircle(self, circle, color=None, thickness=None):
        """
        AddCircle(self: CustomDisplay, circle: Circle, color: Color, thickness: int)
            Adds a new, colored circle to the display list.
        
            circle: Circle to add.
            color: Color of circle.
            thickness: Thickness of circle.
        AddCircle(self: CustomDisplay, circle: Circle, color: Color)
            Adds a new, colored arc to the display list.
        
            circle: Circle to add.
            color: Color of circle.
        AddCircle(self: CustomDisplay, circle: Circle)
            Adds a new, black circle to the display list.
        
            circle: Circle to add.
        """
        pass

    def AddCurve(self, curve, color=None, thickness=None):
        """
        AddCurve(self: CustomDisplay, curve: Curve, color: Color, thickness: int)
            Adds a new, colored curve to the display list.
                    The curve will be duplicated so 
             changes to the 
                    original will not affect the display.
        
        
            curve: Curve to add.
            color: Color of curve.
            thickness: Thickness of curve.
        AddCurve(self: CustomDisplay, curve: Curve, color: Color)
            Adds a new, colored curve to the display list.
                    The curve will be duplicated so 
             changes to the 
                    original will not affect the display.
        
        
            curve: Curve to add.
            color: Color of curve.
        AddCurve(self: CustomDisplay, curve: Curve)
            Adds a new, black curve to the display list. 
                    The curve will be duplicated so 
             changes to the 
                    original will not affect the display.
        
        
            curve: Curve to add.
        """
        pass

    def AddLine(self, line, color=None, thickness=None):
        """
        AddLine(self: CustomDisplay, line: Line, color: Color, thickness: int)
            Adds a new, colored line to the display list.
        
            line: Line to add.
            color: Color of line.
            thickness: Thickness of line.
        AddLine(self: CustomDisplay, line: Line, color: Color)
            Adds a new, colored line to the display list.
        
            line: Line to add.
            color: Color of line.
        AddLine(self: CustomDisplay, line: Line)
            Adds a new, black line to the display list.
        
            line: Line to add.
        """
        pass

    def AddPoint(self, point, color=None, style=None, radius=None):
        """
        AddPoint(self: CustomDisplay, point: Point3d, color: Color, style: PointStyle, radius: int)
            Adds a new stylized point to the display list.
        
            point: Point to add.
            color: Color of point.
            style: Display style of point.
            radius: Radius of point widget.
        AddPoint(self: CustomDisplay, point: Point3d, color: Color)
            Adds a new colored point to the display list.
        
            point: Point to add.
            color: Color of point.
        AddPoint(self: CustomDisplay, point: Point3d)
            Adds a new, black point to the display list.
        
            point: Point to add.
        """
        pass

    def AddPoints(self, points, color=None, style=None, radius=None):
        """ AddPoints(self: CustomDisplay, points: IEnumerable[Point3d], color: Color, style: PointStyle, radius: int)AddPoints(self: CustomDisplay, points: IEnumerable[Point3d], color: Color)AddPoints(self: CustomDisplay, points: IEnumerable[Point3d]) """
        pass

    def AddPolygon(self, polygon, fillColor, edgeColor, drawFill, drawEdge):
        """ AddPolygon(self: CustomDisplay, polygon: IEnumerable[Point3d], fillColor: Color, edgeColor: Color, drawFill: bool, drawEdge: bool) """
        pass

    def AddText(self, text, *__args):
        """
        AddText(self: CustomDisplay, text: Text3d, color: Color)
            Adds a new 3D text object to the display list.
        
            text: Text object to add.
            color: Color of text object.
        AddText(self: CustomDisplay, text: str, plane: Plane, size: float, color: Color)
            Adds a new, colored 3D text object to the display list.
        
            text: Text to add.
            plane: Plane for text orientation.
            size: Height (in units) of font.
            color: Color of text.
        AddText(self: CustomDisplay, text: str, plane: Plane, size: float)
            Adds a new, black 3D text object to the display list.
        
            text: Text to add.
            plane: Plane for text orientation.
            size: Height (in units) of font.
        """
        pass

    def AddVector(self, anchor, span, color=None, drawAnchor=None):
        """
        AddVector(self: CustomDisplay, anchor: Point3d, span: Vector3d, color: Color, drawAnchor: bool)
            Adds a new, colored vector to the display list.
        
            anchor: Anchor point of vector.
            span: Direction and magnitude of vector.
            color: Color of vector.
            drawAnchor: Include a point at the vector anchor.
        AddVector(self: CustomDisplay, anchor: Point3d, span: Vector3d, color: Color)
            Adds a new, colored vector to the display list.
        
            anchor: Anchor point of vector.
            span: Direction and magnitude of vector.
            color: Color of vector.
        AddVector(self: CustomDisplay, anchor: Point3d, span: Vector3d)
            Adds a new, black vector to the display list.
        
            anchor: Anchor point of vector.
            span: Direction and magnitude of vector.
        """
        pass

    def Clear(self):
        """
        Clear(self: CustomDisplay)
            Clear the drawing lists.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CustomDisplay)
            Dispose this CustomDisplay instance. You must call this function in order to 
                    
             properly shut down the CustomDisplay.
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
    def __new__(self, enable):
        """ __new__(cls: type, enable: bool) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the clipping box of this CustomDisplay.

Get: ClippingBox(self: CustomDisplay) -> BoundingBox

"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Enabled state of this CustomDisplay instance. 
            If you wish to terminate this CustomDisplay, place a call to Dispose() instead.

Get: Enabled(self: CustomDisplay) -> bool

Set: Enabled(self: CustomDisplay) = value
"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this CustomDisplay instance has been disposed. 
            Once a CustomDisplay has been disposed, you can no longer use it.

Get: IsDisposed(self: CustomDisplay) -> bool

"""



class DefinedViewportProjection(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated values for parallel and perspective projections that are "standard" in Rhino.
    
    enum DefinedViewportProjection, values: Back (6), Bottom (2), Front (5), Left (3), None (0), Perspective (7), Right (4), Top (1), TwoPointPerspective (8)
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

    Back = None
    Bottom = None
    Front = None
    Left = None
    None = None
    Perspective = None
    Right = None
    Top = None
    TwoPointPerspective = None
    value__ = None


class DepthMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum DepthMode, values: AlwaysInBack (2), AlwaysInFront (1), Neutral (0) """
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

    AlwaysInBack = None
    AlwaysInFront = None
    Neutral = None
    value__ = None


class DisplayBitmap(object, IDisposable):
    """
    A bitmap resource that can be used by the display pipeline (currently only
                in OpenGL display).  Reuse DisplayBitmaps for drawing if possible; it is
                much more expensive to construct new DisplayBitmaps than it is to reuse
                existing DisplayBitmaps.
    
    DisplayBitmap(bitmap: Bitmap)
    """
    def Dispose(self):
        """
        Dispose(self: DisplayBitmap)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def GetBlendModes(self, source, destination):
        """
        GetBlendModes(self: DisplayBitmap) -> (BlendMode, BlendMode)
        
            Gets the source and destination blend modes.
        """
        pass

    @staticmethod
    def Load(path):
        """
        Load(path: str) -> DisplayBitmap
        
            Load a DisplayBitmap from and image file on disk.
        
            path: A location from which to load the file.
            Returns: The new display bitmap, or null on error.
        """
        pass

    def SetBlendFunction(self, source, destination):
        """
        SetBlendFunction(self: DisplayBitmap, source: BlendMode, destination: BlendMode)
            Sets blending function used to determine how this bitmap is blended
                    with the 
             current framebuffer color.  The default setting is SourceAlpha
                    for source and 
             OneMinusSourceAlpha for destination.  See OpenGL's
                    glBlendFunc for details.
               
                  http://www.opengl.org/sdk/docs/man/xhtml/glBlendFunc.xml
        
        
            source: The source blend mode.
            destination: The destination blend mode.
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
    def __new__(self, bitmap):
        """ __new__(cls: type, bitmap: Bitmap) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class DisplayBitmapDrawList(object):
    """ DisplayBitmapDrawList() """
    def SetPoints(self, points, *__args):
        """ SetPoints(self: DisplayBitmapDrawList, points: IEnumerable[Point3d], colors: IEnumerable[Color])SetPoints(self: DisplayBitmapDrawList, points: IEnumerable[Point3d], blendColor: Color)SetPoints(self: DisplayBitmapDrawList, points: IEnumerable[Point3d]) """
        pass

    def Sort(self, cameraDirection):
        """ Sort(self: DisplayBitmapDrawList, cameraDirection: Vector3d) -> Array[int] """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: DisplayBitmapDrawList) -> BoundingBox

"""

    MaximumCachedSortLists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum number of cached sort order index lists stored on this class.
            Default is 10, but depending on the number of points in this list you
            may get better performance by setting this value to a certain percentage
            of the point count.

Get: MaximumCachedSortLists(self: DisplayBitmapDrawList) -> int

Set: MaximumCachedSortLists(self: DisplayBitmapDrawList) = value
"""

    SortAngleTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Angle in radians used to determine if an index list is "parallel enough"
            to a viewports camera angle. Default is 0.0873 radians (5 degrees)

Get: SortAngleTolerance(self: DisplayBitmapDrawList) -> float

Set: SortAngleTolerance(self: DisplayBitmapDrawList) = value
"""



class DisplayConduit(object):
    # no doc
    def CalculateBoundingBox(self, *args): #cannot find CLR method
        """
        CalculateBoundingBox(self: DisplayConduit, e: CalculateBoundingBoxEventArgs)
            Library developers should override this function to increase the bounding box of scene so it 
             includes the
                    geometry that you plan to draw in the "Draw" virtual functions.
              
                   The default implementation does nothing.
        
        
            e: The event argument contain the current bounding box state.
        """
        pass

    def CalculateBoundingBoxZoomExtents(self, *args): #cannot find CLR method
        """
        CalculateBoundingBoxZoomExtents(self: DisplayConduit, e: CalculateBoundingBoxEventArgs)
            If you want to participate in the Zoom Extents command with your display conduit,
                    
             then you will need to override ZoomExtentsBoundingBox.  Typically you could just
                    
             call your CalculateBoundingBox override, but you may also want to spend a little
                    
             more time here and compute a tighter bounding box for your conduit geometry if
                    that 
             is needed.
                    The default implementation does nothing.
        
        
            e: The event argument contain the current bounding box state.
        """
        pass

    def DrawForeground(self, *args): #cannot find CLR method
        """
        DrawForeground(self: DisplayConduit, e: DrawEventArgs)
            Called after all non-highlighted objects have been drawn and PostDrawObjects has been called.
          
                       Depth writing and testing are turned OFF. If you want to draw with depth 
             writing/testing,
                    see PostDrawObjects.
                    The default implementation does 
             nothing.
        
        
            e: The event argument contains the current viewport and display state.
        """
        pass

    def DrawOverlay(self, *args): #cannot find CLR method
        """
        DrawOverlay(self: DisplayConduit, e: DrawEventArgs)
            If Rhino is in a feedback mode, the draw overlay call allows for temporary geometry to be drawn 
             on top of
                    everything in the scene. This is similar to the dynamic draw routine that 
             occurs with custom get point.
                    The default implementation does nothing.
        
        
            e: The event argument contains the current viewport and display state.
        """
        pass

    def ObjectCulling(self, *args): #cannot find CLR method
        """
        ObjectCulling(self: DisplayConduit, e: CullObjectEventArgs)
            The default implementation does nothing.
        """
        pass

    def PostDrawObjects(self, *args): #cannot find CLR method
        """
        PostDrawObjects(self: DisplayConduit, e: DrawEventArgs)
            Called after all non-highlighted objects have been drawn. Depth writing and testing are
                
                 still turned on. If you want to draw without depth writing/testing, see DrawForeground.
            
                     The default implementation does nothing.
        
        
            e: The event argument contains the current viewport and display state.
        """
        pass

    def PreDrawObject(self, *args): #cannot find CLR method
        """
        PreDrawObject(self: DisplayConduit, e: DrawObjectEventArgs)
            Called before every object in the scene is drawn.
        """
        pass

    def PreDrawObjects(self, *args): #cannot find CLR method
        """
        PreDrawObjects(self: DisplayConduit, e: DrawEventArgs)
            Called before objects are been drawn. Depth writing and testing are on.
                    The default 
             implementation does nothing.
        
        
            e: The event argument contain the current viewport and display state.
        """
        pass

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: DisplayConduit) -> bool

Set: Enabled(self: DisplayConduit) = value
"""



class DisplayMaterial(object, IDisposable):
    """
    DisplayMaterial()
    DisplayMaterial(other: DisplayMaterial)
    DisplayMaterial(material: Material)
    DisplayMaterial(diffuse: Color)
    DisplayMaterial(diffuse: Color, transparency: float)
    DisplayMaterial(diffuse: Color, specular: Color, ambient: Color, emission: Color, shine: float, transparency: float)
    """
    def Dispose(self):
        """ Dispose(self: DisplayMaterial) """
        pass

    def GetBitmapTexture(self, front):
        """ GetBitmapTexture(self: DisplayMaterial, front: bool) -> Texture """
        pass

    def GetBumpTexture(self, front):
        """
        GetBumpTexture(self: DisplayMaterial, front: bool) -> Texture
        
            Gets the bump texture for this display material.
            Returns: The texture, or null if no bump texture has been added to this material.
        """
        pass

    def GetEnvironmentTexture(self, front):
        """ GetEnvironmentTexture(self: DisplayMaterial, front: bool) -> Texture """
        pass

    def GetTransparencyTexture(self, front):
        """ GetTransparencyTexture(self: DisplayMaterial, front: bool) -> Texture """
        pass

    def SetBitmapTexture(self, *__args):
        """
        SetBitmapTexture(self: DisplayMaterial, texture: Texture, front: bool) -> bool
        SetBitmapTexture(self: DisplayMaterial, filename: str, front: bool) -> bool
        """
        pass

    def SetBumpTexture(self, *__args):
        """
        SetBumpTexture(self: DisplayMaterial, texture: Texture, front: bool) -> bool
        SetBumpTexture(self: DisplayMaterial, filename: str, front: bool) -> bool
        """
        pass

    def SetEnvironmentTexture(self, *__args):
        """
        SetEnvironmentTexture(self: DisplayMaterial, texture: Texture, front: bool) -> bool
        SetEnvironmentTexture(self: DisplayMaterial, filename: str, front: bool) -> bool
        """
        pass

    def SetTransparencyTexture(self, *__args):
        """
        SetTransparencyTexture(self: DisplayMaterial, texture: Texture, front: bool) -> bool
        SetTransparencyTexture(self: DisplayMaterial, filename: str, front: bool) -> bool
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
        __new__(cls: type, other: DisplayMaterial)
        __new__(cls: type, material: Material)
        __new__(cls: type, diffuse: Color)
        __new__(cls: type, diffuse: Color, transparency: float)
        __new__(cls: type, diffuse: Color, specular: Color, ambient: Color, emission: Color, shine: float, transparency: float)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Ambient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Ambient color of the Material. 
            The alpha component of the color will be ignored.

Get: Ambient(self: DisplayMaterial) -> Color

Set: Ambient(self: DisplayMaterial) = value
"""

    BackAmbient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Ambient color of the back side of the Material. 
            The alpha component of the color will be ignored.

Get: BackAmbient(self: DisplayMaterial) -> Color

Set: BackAmbient(self: DisplayMaterial) = value
"""

    BackDiffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Diffuse color of the back side of the Material. 
            The alpha component of the color will be ignored.

Get: BackDiffuse(self: DisplayMaterial) -> Color

Set: BackDiffuse(self: DisplayMaterial) = value
"""

    BackEmission = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Emissive color of the back side of the Material. 
            The alpha component of the color will be ignored.

Get: BackEmission(self: DisplayMaterial) -> Color

Set: BackEmission(self: DisplayMaterial) = value
"""

    BackShine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the shine factor of the back side of the material (0.0 to 1.0)

Get: BackShine(self: DisplayMaterial) -> float

Set: BackShine(self: DisplayMaterial) = value
"""

    BackSpecular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Specular color of the back side of the Material. 
            The alpha component of the color will be ignored.

Get: BackSpecular(self: DisplayMaterial) -> Color

Set: BackSpecular(self: DisplayMaterial) = value
"""

    BackTransparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the transparency of the back side material (0.0 = opaque to 1.0 = transparent)

Get: BackTransparency(self: DisplayMaterial) -> float

Set: BackTransparency(self: DisplayMaterial) = value
"""

    Diffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Diffuse color of the Material. 
            The alpha component of the color will be ignored.

Get: Diffuse(self: DisplayMaterial) -> Color

Set: Diffuse(self: DisplayMaterial) = value
"""

    Emission = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Emissive color of the Material. 
            The alpha component of the color will be ignored.

Get: Emission(self: DisplayMaterial) -> Color

Set: Emission(self: DisplayMaterial) = value
"""

    IsTwoSided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTwoSided(self: DisplayMaterial) -> bool

Set: IsTwoSided(self: DisplayMaterial) = value
"""

    Shine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the shine factor of the material (0.0 to 1.0)

Get: Shine(self: DisplayMaterial) -> float

Set: Shine(self: DisplayMaterial) = value
"""

    Specular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Specular color of the Material. 
            The alpha component of the color will be ignored.

Get: Specular(self: DisplayMaterial) -> Color

Set: Specular(self: DisplayMaterial) = value
"""

    Transparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the transparency of the material (0.0 = opaque to 1.0 = transparent)

Get: Transparency(self: DisplayMaterial) -> float

Set: Transparency(self: DisplayMaterial) = value
"""



class DisplayModeDescription(object, IDisposable, ISerializable):
    """
    Description of a how Rhino will display in a viewport. These are the modes
                that are listed under "Advanced display" in the options dialog.
    """
    @staticmethod
    def AddDisplayMode(displayMode):
        """ AddDisplayMode(displayMode: DisplayModeDescription) -> Guid """
        pass

    @staticmethod
    def DeleteDiplayMode(id):
        """ DeleteDiplayMode(id: Guid) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: DisplayModeDescription) """
        pass

    @staticmethod
    def FindByName(englishName):
        """ FindByName(englishName: str) -> DisplayModeDescription """
        pass

    @staticmethod
    def GetDisplayMode(id):
        """ GetDisplayMode(id: Guid) -> DisplayModeDescription """
        pass

    @staticmethod
    def GetDisplayModes():
        """
        GetDisplayModes() -> Array[DisplayModeDescription]
        
            Gets all display mode descriptions that Rhino currently knows about.
            Returns: Copies of all of the display mode descriptions. If you want to modify
                    these 
             descriptions, you must call UpdateDisplayMode or AddDisplayMode.
        """
        pass

    @staticmethod
    def UpdateDisplayMode(displayMode):
        """ UpdateDisplayMode(displayMode: DisplayModeDescription) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AllowObjectAssignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowObjectAssignment(self: DisplayModeDescription) -> bool

Set: AllowObjectAssignment(self: DisplayModeDescription) = value
"""

    DisplayAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayAttributes(self: DisplayModeDescription) -> DisplayPipelineAttributes

"""

    EnglishName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnglishName(self: DisplayModeDescription) -> str

Set: EnglishName(self: DisplayModeDescription) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: DisplayModeDescription) -> Guid

"""

    InMenu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InMenu(self: DisplayModeDescription) -> bool

Set: InMenu(self: DisplayModeDescription) = value
"""

    LocalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalName(self: DisplayModeDescription) -> str

"""

    PipelineLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipelineLocked(self: DisplayModeDescription) -> bool

Set: PipelineLocked(self: DisplayModeDescription) = value
"""

    ShadedPipelineRequired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadedPipelineRequired(self: DisplayModeDescription) -> bool

Set: ShadedPipelineRequired(self: DisplayModeDescription) = value
"""

    SupportsShadeCommand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportsShadeCommand(self: DisplayModeDescription) -> bool

Set: SupportsShadeCommand(self: DisplayModeDescription) = value
"""

    SupportsShading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportsShading(self: DisplayModeDescription) -> bool

Set: SupportsShading(self: DisplayModeDescription) = value
"""

    WireframePipelineRequired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WireframePipelineRequired(self: DisplayModeDescription) -> bool

Set: WireframePipelineRequired(self: DisplayModeDescription) = value
"""



class DisplayPipeline(object):
    """
    The display pipeline calls events during specific phases of drawing
                 During the drawing of a single frame the events are called in the following order.
                 
                 [Begin Drawing of a Frame]
                 CalculateBoundingBoxCalculateClippingPanesSetupFrustumSetupLightingInitializeFrameBufferDrawBackgroundIf this is a layout and detail objects exist the channels are called in the
                   same order for each detail object (drawn as a nested viewport)PreDrawObjectsFor Each Visible Non Highlighted ObjectSetupObjectDisplayAttributesPreDrawObjectDrawObjectPostDrawObjectPostDrawObjects - depth writing/testing onDrawForeGround - depth writing/testing offFor Each Visible Highlighted ObjectSetupObjectDisplayAttributesPreDrawObjectDrawObjectPostDrawObjectPostProcessFrameBuffer (If a delegate exists that requires this)DrawOverlay (if Rhino is in a feedback mode)
                 [End of Drawing of a Frame]
                
                 NOTE: There may be multiple DrawObject calls for a single object. An example of when this could
                       happen would be with a shaded sphere. The shaded mesh is first drawn and these channels would
                       be processed; then at a later time the isocurves for the sphere would be drawn.
    """
    @staticmethod
    def CullControlPolygon():
        """
        CullControlPolygon() -> bool
        
            Returns a value indicating if only points on the side of the surface that
                    face the 
             camera are displayed.
        
            Returns: true if backfaces of surface and mesh control polygons are culled.
                    This value is 
             determined by the _CullControlPolygon command.
        """
        pass

    def Draw2dRectangle(self, rectangle, strokeColor, thickness, fillColor):
        """ Draw2dRectangle(self: DisplayPipeline, rectangle: Rectangle, strokeColor: Color, thickness: int, fillColor: Color) """
        pass

    def Draw2dText(self, text, color, *__args):
        """
        Draw2dText(self: DisplayPipeline, text: str, color: Color, worldCoordinate: Point3d, middleJustified: bool)
            Draws 2D text on the viewport.
        
            text: the string to draw.
            color: text color.
            worldCoordinate: definition point in world coordinates.
            middleJustified: if true text is centered around the definition point, otherwise it is lower-left justified.
        Draw2dText(self: DisplayPipeline, text: str, color: Color, worldCoordinate: Point3d, middleJustified: bool, height: int)
            Draws 2D text on the viewport.
        
            text: the string to draw.
            color: text color.
            worldCoordinate: definition point in world coordinates.
            middleJustified: if true text is centered around the definition point, otherwise it is lower-left justified.
            height: height in pixels (good default is 12)
        Draw2dText(self: DisplayPipeline, text: str, color: Color, worldCoordinate: Point3d, middleJustified: bool, height: int, fontface: str)
            Draws 2D text on the viewport.
        
            text: The string to draw.
            color: Text color.
            worldCoordinate: Definition point in world coordinates.
            middleJustified: If true text is centered around the definition point, otherwise it is lower-left justified.
            height: Height in pixels (good default is 12).
            fontface: Font name (good default is "Arial").
        Draw2dText(self: DisplayPipeline, text: str, color: Color, screenCoordinate: Point2d, middleJustified: bool)
            Draws 2D text on the viewport.
        
            text: the string to draw.
            color: text color.
            screenCoordinate: definition point in screen coordinates (0,0 is top-left corner)
            middleJustified: if true text is centered around the definition point, otherwise it is lower-left justified.
        Draw2dText(self: DisplayPipeline, text: str, color: Color, screenCoordinate: Point2d, middleJustified: bool, height: int)
            Draws 2D text on the viewport.
        
            text: the string to draw.
            color: text color.
            screenCoordinate: definition point in screen coordinates (0,0 is top-left corner)
            middleJustified: if true text is centered around the definition point, otherwise it is lower-left justified.
            height: height in pixels (good default is 12)
        Draw2dText(self: DisplayPipeline, text: str, color: Color, screenCoordinate: Point2d, middleJustified: bool, height: int, fontface: str)
            Draws 2D text on the viewport.
        
            text: the string to draw.
            color: text color.
            screenCoordinate: definition point in screen coordinates (0,0 is top-left corner)
            middleJustified: if true text is centered around the definition point, otherwise it is lower-left justified.
            height: height in pixels (good default is 12)
            fontface: font name (good default is "Arial")
        """
        pass

    def Draw3dText(self, text, color, *__args):
        """
        Draw3dText(self: DisplayPipeline, text: Text3d, color: Color, textPlane: Plane)
            Draws 3d text with a different plane than what is defined in the Text3d class.
        
            text: The string to draw.
            color: Text color.
            textPlane: The plane for the text object.
        Draw3dText(self: DisplayPipeline, text: Text3d, color: Color, textPlaneOrigin: Point3d)
            Draws 3d text using the Text3d plane with an adjusted origin.
        
            text: The string to draw.
            color: Text color.
            textPlaneOrigin: The origin of the plane to draw.
        Draw3dText(self: DisplayPipeline, text: str, color: Color, textPlane: Plane, height: float, fontface: str)Draw3dText(self: DisplayPipeline, text: Text3d, color: Color)
        """
        pass

    def DrawArc(self, arc, color, thickness=None):
        """
        DrawArc(self: DisplayPipeline, arc: Arc, color: Color, thickness: int)
            Draw a single arc object.
        
            arc: Arc to draw.
            color: Color to draw with.
            thickness: Thickness (in pixels) of arc.
        DrawArc(self: DisplayPipeline, arc: Arc, color: Color)
            Draw a single arc object.
        
            arc: Arc to draw.
            color: Color to draw with.
        """
        pass

    def DrawArrow(self, line, color, screenSize=None, relativeSize=None):
        """
        DrawArrow(self: DisplayPipeline, line: Line, color: Color, screenSize: float, relativeSize: float)
            Draws a single arrow object. 
                    An arrow consists of a Shaft and an Arrow head at the 
             end of the shaft.
        
        
            line: Arrow shaft.
            color: Color of arrow.
            screenSize: If screenSize != 0.0 then the size (in screen pixels) of the arrow head will be equal to 
             screenSize.
        
            relativeSize: If relativeSize != 0.0 and screensize == 0.0 the size of the arrow head will be proportional to 
             the arrow shaft length.
        
        DrawArrow(self: DisplayPipeline, line: Line, color: Color)
            Draws a single arrow object. An arrow consists of a Shaft and an Arrow head at the end of the 
             shaft.
        
        
            line: Arrow shaft.
            color: Color of arrow.
        """
        pass

    def DrawArrowHead(self, tip, direction, color, screenSize, worldSize):
        """
        DrawArrowHead(self: DisplayPipeline, tip: Point3d, direction: Vector3d, color: Color, screenSize: float, worldSize: float)
            Draws a single arrow head.
        
            tip: Point of arrow head tip.
            direction: Direction in which arrow head is pointing.
            color: Color of arrow head.
            screenSize: If screenSize != 0.0, then the size (in screen pixels) of the arrow head will be equal to the 
             screenSize.
        
            worldSize: If worldSize != 0.0 and screensize == 0.0 the size of the arrow head will be equal to the number 
             of units in worldSize.
        """
        pass

    def DrawArrows(self, lines, color):
        """
        DrawArrows(self: DisplayPipeline, lines: IEnumerable[Line], color: Color)DrawArrows(self: DisplayPipeline, lines: Array[Line], color: Color)
            Draws a collection of arrow objects. An arrow consists of a Shaft and an Arrow head at the end 
             of the shaft.
        
        
            lines: Arrow shafts.
            color: Color of arrows.
        """
        pass

    def DrawBitmap(self, bitmap, left, top, maskColor=None):
        """
        DrawBitmap(self: DisplayPipeline, bitmap: DisplayBitmap, left: int, top: int, maskColor: Color)
            Draws a bitmap in screen coordinates
        
            bitmap: bitmap to draw
            left: where top/left corner of bitmap should appear in screen coordinates
            top: where top/left corner of bitmap should appear in screen coordinates
            maskColor: mask color to apply to bitmap for transparent regions
        DrawBitmap(self: DisplayPipeline, bitmap: DisplayBitmap, left: int, top: int)
            Draws a bitmap in screen coordinates
        
            bitmap: bitmap to draw
            left: where top/left corner of bitmap should appear in screen coordinates
            top: where top/left corner of bitmap should appear in screen coordinates
        """
        pass

    def DrawBox(self, box, color, thickness=None):
        """
        DrawBox(self: DisplayPipeline, box: Box, color: Color)
            Draws the edges of a Box object.
        
            box: Box to draw.
            color: Color to draw in.
        DrawBox(self: DisplayPipeline, box: Box, color: Color, thickness: int)
            Draws the edges of a Box object.
        
            box: Box to draw.
            color: Color to draw in.
            thickness: Thickness (in pixels) of box edges.
        DrawBox(self: DisplayPipeline, box: BoundingBox, color: Color)
            Draws the edges of a BoundingBox.
        
            box: Box to draw.
            color: Color to draw in.
        DrawBox(self: DisplayPipeline, box: BoundingBox, color: Color, thickness: int)
            Draws the edges of a BoundingBox.
        
            box: Box to draw.
            color: Color to draw in.
            thickness: Thickness (in pixels) of box edges.
        """
        pass

    def DrawBoxCorners(self, box, color, size=None, thickness=None):
        """
        DrawBoxCorners(self: DisplayPipeline, box: BoundingBox, color: Color, size: float, thickness: int)
            Draws corner widgets of a world aligned boundingbox.
        
            box: Box to draw.
            color: Color to draw with.
            size: Size (in model units) of the corner widgets.
            thickness: Thickness (in pixels) of the corner widgets.
        DrawBoxCorners(self: DisplayPipeline, box: BoundingBox, color: Color, size: float)
            Draws corner widgets of a world aligned boundingbox.
        
            box: Box to draw.
            color: Color to draw with.
            size: Size (in model units) of the corner widgets.
        DrawBoxCorners(self: DisplayPipeline, box: BoundingBox, color: Color)
            Draws corner widgets of a world aligned boundingbox. 
                    Widget size will be 5% of the 
             Box diagonal.
        
        
            box: Box to draw.
            color: Color to draw with.
        """
        pass

    def DrawBrepShaded(self, brep, material):
        """
        DrawBrepShaded(self: DisplayPipeline, brep: Brep, material: DisplayMaterial)
            Draws a shaded mesh representation of a brep.
        
            brep: Brep to draw.
            material: Material to draw faces with.
        """
        pass

    def DrawBrepWires(self, brep, color, wireDensity=None):
        """
        DrawBrepWires(self: DisplayPipeline, brep: Brep, color: Color, wireDensity: int)
            Draws all the wireframe curves of a brep object.
        
            brep: Brep to draw.
            color: Color of Wireframe curves.
            wireDensity: "Density" of wireframe curves.
                    -1 = no internal wires. 0 = default internal 
             wires.>0 = custom high density.
        
        DrawBrepWires(self: DisplayPipeline, brep: Brep, color: Color)
            Draws all the wireframe curves of a brep object.
        
            brep: Brep to draw.
            color: Color of Wireframe curves.
        """
        pass

    def DrawCircle(self, circle, color, thickness=None):
        """
        DrawCircle(self: DisplayPipeline, circle: Circle, color: Color, thickness: int)
            Draw a single circle object.
        
            circle: Circle to draw.
            color: Color to draw with.
            thickness: Thickness (in pixels) of circle.
        DrawCircle(self: DisplayPipeline, circle: Circle, color: Color)
            Draw a single circle object.
        
            circle: Circle to draw.
            color: Color to draw with.
        """
        pass

    def DrawCone(self, cone, color, thickness=None):
        """
        DrawCone(self: DisplayPipeline, cone: Cone, color: Color, thickness: int)
            Draw a wireframe cone.
        
            cone: Cone to draw.
            color: Color to draw with.
            thickness: Thickness (in pixels) of Cone wires.
        DrawCone(self: DisplayPipeline, cone: Cone, color: Color)
            Draw a wireframe cone.
        
            cone: Cone to draw.
            color: Color to draw with.
        """
        pass

    def DrawConstructionPlane(self, constructionPlane):
        """ DrawConstructionPlane(self: DisplayPipeline, constructionPlane: ConstructionPlane) """
        pass

    def DrawCurvatureGraph(self, curve, color, hairScale=None, hairDensity=None, sampleDensity=None):
        """
        DrawCurvatureGraph(self: DisplayPipeline, curve: Curve, color: Color, hairScale: int, hairDensity: int, sampleDensity: int)
            Draw a typical Rhino Curvature Graph.
        
            curve: Base curve for curvature graph.
            color: Color of curvature graph.
            hairScale: 100 = true length, > 100 magnified, < 100 shortened.
            hairDensity: >= 0 larger numbers = more hairs (good default is 1).
            sampleDensity: Between 1 and 10. Higher numbers draw smoother outer curves. (good default is 2).
        DrawCurvatureGraph(self: DisplayPipeline, curve: Curve, color: Color, hairScale: int)
            Draw a typical Rhino Curvature Graph.
        
            curve: Base curve for curvature graph.
            color: Color of curvature graph.
            hairScale: 100 = true length, > 100 magnified, < 100 shortened.
        DrawCurvatureGraph(self: DisplayPipeline, curve: Curve, color: Color)
            Draw a typical Rhino Curvature Graph.
        
            curve: Base curve for curvature graph.
            color: Color of curvature graph.
        """
        pass

    def DrawCurve(self, curve, color, thickness=None):
        """
        DrawCurve(self: DisplayPipeline, curve: Curve, color: Color, thickness: int)
            Draw a single Curve object.
        
            curve: Curve to draw.
            color: Color to draw with.
            thickness: Thickness (in pixels) of curve.
        DrawCurve(self: DisplayPipeline, curve: Curve, color: Color)
            Draw a single Curve object.
        
            curve: Curve to draw.
            color: Color to draw with.
        """
        pass

    def DrawCylinder(self, cylinder, color, thickness=None):
        """
        DrawCylinder(self: DisplayPipeline, cylinder: Cylinder, color: Color, thickness: int)
            Draw a wireframe cylinder.
        
            cylinder: Cylinder to draw.
            color: Color to draw with.
            thickness: Thickness (in pixels) of cylinder wires.
        DrawCylinder(self: DisplayPipeline, cylinder: Cylinder, color: Color)
            Draw a wireframe cylinder.
        
            cylinder: Cylinder to draw.
            color: Color to draw with.
        """
        pass

    def DrawDirectionArrow(self, location, direction, color):
        """ DrawDirectionArrow(self: DisplayPipeline, location: Point3d, direction: Vector3d, color: Color) """
        pass

    def DrawDot(self, *__args):
        """
        DrawDot(self: DisplayPipeline, worldPosition: Point3d, text: str, dotColor: Color, textColor: Color)
            Draw a text dot in world coordinates.
        
            worldPosition: Location of dot in world coordinates.
            text: Text content of dot.
            dotColor: Dot background color.
            textColor: Dot foreground color.
        DrawDot(self: DisplayPipeline, worldPosition: Point3d, text: str)
            Draws a text dot in world coordinates.
        
            worldPosition: Location of dot in world coordinates.
            text: Text content of dot.
        DrawDot(self: DisplayPipeline, screenX: int, screenY: int, text: str, dotColor: Color, textColor: Color)
            Draws a text dot in screen coordinates.
        
            screenX: X coordinate (in pixels) of dot center.
            screenY: Y coordinate (in pixels) of dot center.
            text: Text content of dot.
            dotColor: Dot background color.
            textColor: Dot foreground color.
        DrawDot(self: DisplayPipeline, screenX: int, screenY: int, text: str)
            Draws a text dot in screen coordinates.
        
            screenX: X coordinate (in pixels) of dot center.
            screenY: Y coordinate (in pixels) of dot center.
            text: Text content of dot.
        """
        pass

    def DrawDottedLine(self, *__args):
        """
        DrawDottedLine(self: DisplayPipeline, from: Point3d, to: Point3d, color: Color)
            Draws a single dotted line.
        
            from: Line start point.
            to: Line end point.
            color: Color of line.
        DrawDottedLine(self: DisplayPipeline, line: Line, color: Color)
            Draws a single dotted line.
        
            line: Line to draw.
            color: Color of line.
        """
        pass

    def DrawDottedPolyline(self, points, color, close):
        """ DrawDottedPolyline(self: DisplayPipeline, points: IEnumerable[Point3d], color: Color, close: bool) """
        pass

    def DrawLine(self, *__args):
        """
        DrawLine(self: DisplayPipeline, from: Point3d, to: Point3d, color: Color)
            Draws a single line object.
        
            from: Line from point.
            to: Line to point.
            color: Color to draw line in.
        DrawLine(self: DisplayPipeline, from: Point3d, to: Point3d, color: Color, thickness: int)
            Draws a single line object.
        
            from: Line from point.
            to: Line to point.
            color: Color to draw line in.
            thickness: Thickness (in pixels) of line.
        DrawLine(self: DisplayPipeline, line: Line, color: Color)
            Draws a single line object.
        
            line: Line to draw.
            color: Color to draw line in.
        DrawLine(self: DisplayPipeline, line: Line, color: Color, thickness: int)
            Draws a single line object.
        
            line: Line to draw.
            color: Color to draw line in.
            thickness: Thickness (in pixels) of line.
        """
        pass

    def DrawLineArrow(self, line, color, thickness, size):
        """
        DrawLineArrow(self: DisplayPipeline, line: Line, color: Color, thickness: int, size: float)
            Draws an arrow made up of three line segments.
        
            line: Base line for arrow.
            color: Color of arrow.
            thickness: Thickness (in pixels) of the arrow line segments.
            size: Size (in world units) of the arrow tip lines.
        """
        pass

    def DrawLines(self, lines, color, thickness=None):
        """ DrawLines(self: DisplayPipeline, lines: IEnumerable[Line], color: Color, thickness: int)DrawLines(self: DisplayPipeline, lines: IEnumerable[Line], color: Color) """
        pass

    def DrawMarker(self, tip, direction, color, thickness=None, size=None, rotation=None):
        """
        DrawMarker(self: DisplayPipeline, tip: Point3d, direction: Vector3d, color: Color, thickness: int, size: float)
            Draws an arrow marker as a view-aligned widget.
        
            tip: Location of arrow tip point.
            direction: Direction of arrow.
            color: Color of arrow widget.
            thickness: Thickness of arrow widget lines.
            size: Size (in pixels) of the arrow shaft.
        DrawMarker(self: DisplayPipeline, tip: Point3d, direction: Vector3d, color: Color, thickness: int, size: float, rotation: float)
            Draws an arrow marker as a view-aligned widget.
        
            tip: Location of arrow tip point.
            direction: Direction of arrow.
            color: Color of arrow widget.
            thickness: Thickness of arrow widget lines.
            size: Size (in pixels) of the arrow shaft.
            rotation: Rotational angle adjustment (in radians, counter-clockwise of direction.
        DrawMarker(self: DisplayPipeline, tip: Point3d, direction: Vector3d, color: Color)
            Draws an arrow marker as a view-aligned widget.
        
            tip: Location of arrow tip point.
            direction: Direction of arrow.
            color: Color of arrow widget.
        DrawMarker(self: DisplayPipeline, tip: Point3d, direction: Vector3d, color: Color, thickness: int)
            Draws an arrow marker as a view-aligned widget.
        
            tip: Location of arrow tip point.
            direction: Direction of arrow.
            color: Color of arrow widget.
            thickness: Thickness of arrow widget lines.
        """
        pass

    def DrawMeshFalseColors(self, mesh):
        """
        DrawMeshFalseColors(self: DisplayPipeline, mesh: Mesh)
            Draws the mesh faces as false color patches. 
                    The mesh must have Vertex Colors 
             defined for this to work.
        
        
            mesh: Mesh to draw.
        """
        pass

    def DrawMeshShaded(self, mesh, material, faceIndices=None):
        """
        DrawMeshShaded(self: DisplayPipeline, mesh: Mesh, material: DisplayMaterial, faceIndices: Array[int])
            Draws the shaded faces of a given mesh.
        
            mesh: Mesh to draw.
            material: Material to draw faces with.
            faceIndices: Indices of specific faces to draw
        DrawMeshShaded(self: DisplayPipeline, mesh: Mesh, material: DisplayMaterial)
            Draws the shaded faces of a given mesh.
        
            mesh: Mesh to draw.
            material: Material to draw faces with.
        """
        pass

    def DrawMeshVertices(self, mesh, color):
        """
        DrawMeshVertices(self: DisplayPipeline, mesh: Mesh, color: Color)
            Draws all the vertices in a given mesh.
        
            mesh: Mesh for vertex drawing.
            color: Color of mesh vertices.
        """
        pass

    def DrawMeshWires(self, mesh, color, thickness=None):
        """
        DrawMeshWires(self: DisplayPipeline, mesh: Mesh, color: Color, thickness: int)
            Draws all the wires in a given mesh.
        
            mesh: Mesh for wire drawing.
            color: Color of mesh wires.
            thickness: Thickness (in pixels) of mesh wires.
        DrawMeshWires(self: DisplayPipeline, mesh: Mesh, color: Color)
            Draws all the wires in a given mesh.
        
            mesh: Mesh for wire drawing.
            color: Color of mesh wires.
        """
        pass

    def DrawObject(self, rhinoObject, xform=None):
        """
        DrawObject(self: DisplayPipeline, rhinoObject: RhinoObject, xform: Transform)
            Draws a Rhino.DocObjects.RhinoObjectRhinoObject with an applied transformation.
        
            rhinoObject: The Rhino object.
            xform: The transformation.
        DrawObject(self: DisplayPipeline, rhinoObject: RhinoObject)
        """
        pass

    def DrawParticles(self, particles, *__args):
        """ DrawParticles(self: DisplayPipeline, particles: ParticleSystem, bitmaps: Array[DisplayBitmap])DrawParticles(self: DisplayPipeline, particles: ParticleSystem, bitmap: DisplayBitmap)DrawParticles(self: DisplayPipeline, particles: ParticleSystem) """
        pass

    def DrawPoint(self, point, *__args):
        """
        DrawPoint(self: DisplayPipeline, point: Point3d, style: PointStyle, radius: int, color: Color)
            Draws a point with a given radius, style and color.
        
            point: Location of point in world coordinates.
            style: Point display style.
            radius: Point size in pixels.
            color: Color of point. If style is ControlPoint, this will be the border color.
        DrawPoint(self: DisplayPipeline, point: Point3d, color: Color)
            Draws a point with a given radius, style and color.
        
            point: Location of point in world coordinates.
            color: Color of point.
        """
        pass

    def DrawPointCloud(self, cloud, size, color=None):
        """
        DrawPointCloud(self: DisplayPipeline, cloud: PointCloud, size: int, color: Color)
            Draws a point cloud.
        
            cloud: Point cloud to draw.
            size: Size of points.
            color: Color of points in the cloud, if the cloud has a color array this setting is ignored.
        DrawPointCloud(self: DisplayPipeline, cloud: PointCloud, size: int)
            Draws a point cloud.
        
            cloud: Point cloud to draw, if the cloud has a color array, it will be used, otherwise the points will 
             be black.
        
            size: Size of points.
        """
        pass

    def DrawPoints(self, points, style, radius, color):
        """ DrawPoints(self: DisplayPipeline, points: IEnumerable[Point3d], style: PointStyle, radius: int, color: Color) """
        pass

    def DrawPolygon(self, points, color, filled):
        """ DrawPolygon(self: DisplayPipeline, points: IEnumerable[Point3d], color: Color, filled: bool) """
        pass

    def DrawPolyline(self, polyline, color, thickness=None):
        """ DrawPolyline(self: DisplayPipeline, polyline: IEnumerable[Point3d], color: Color, thickness: int)DrawPolyline(self: DisplayPipeline, polyline: IEnumerable[Point3d], color: Color) """
        pass

    def DrawSphere(self, sphere, color, thickness=None):
        """
        DrawSphere(self: DisplayPipeline, sphere: Sphere, color: Color, thickness: int)
            Draw a wireframe sphere.
        
            sphere: Sphere to draw.
            color: Color to draw with.
            thickness: Thickness (in pixels) of Sphere wires.
        DrawSphere(self: DisplayPipeline, sphere: Sphere, color: Color)
            Draw a wireframe sphere.
        
            sphere: Sphere to draw.
            color: Color to draw with.
        """
        pass

    def DrawSprite(self, bitmap, *__args):
        """ DrawSprite(self: DisplayPipeline, bitmap: DisplayBitmap, screenLocation: Point2d, size: Single)DrawSprite(self: DisplayPipeline, bitmap: DisplayBitmap, screenLocation: Point2d, size: Single, blendColor: Color)DrawSprite(self: DisplayPipeline, bitmap: DisplayBitmap, worldLocation: Point3d, size: Single, sizeInWorldSpace: bool)DrawSprite(self: DisplayPipeline, bitmap: DisplayBitmap, worldLocation: Point3d, size: Single, blendColor: Color, sizeInWorldSpace: bool) """
        pass

    def DrawSprites(self, bitmap, items, size, *__args):
        """ DrawSprites(self: DisplayPipeline, bitmap: DisplayBitmap, items: DisplayBitmapDrawList, size: Single, translation: Vector3d, sizeInWorldSpace: bool)DrawSprites(self: DisplayPipeline, bitmap: DisplayBitmap, items: DisplayBitmapDrawList, size: Single, sizeInWorldSpace: bool) """
        pass

    def DrawSurface(self, surface, wireColor, wireDensity):
        """
        DrawSurface(self: DisplayPipeline, surface: Surface, wireColor: Color, wireDensity: int)
            Draw wireframe display for a single surface.
        
            surface: Surface to draw.
            wireColor: Color to draw with.
            wireDensity: Thickness (in pixels) or wires to draw.
        """
        pass

    @staticmethod
    def DrawToBitmap(viewport, width, height):
        """
        DrawToBitmap(viewport: RhinoViewport, width: int, height: int) -> Bitmap
        
            Draw a given viewport to an off-screen bitmap.
        
            viewport: Viewport to draw.
            width: Width of target image.
            height: Height of target image.
            Returns: A bitmap containing the given view, or null on error.
        """
        pass

    def DrawTorus(self, torus, color, thickness=None):
        """
        DrawTorus(self: DisplayPipeline, torus: Torus, color: Color, thickness: int)
            Draw a wireframe torus.
        
            torus: Torus to draw.
            color: Color to draw with.
            thickness: Thickness (in pixels) of torus wires.
        DrawTorus(self: DisplayPipeline, torus: Torus, color: Color)
            Draw a wireframe torus.
        
            torus: Torus to draw.
            color: Color to draw with.
        """
        pass

    def EnableClippingPlanes(self, enable):
        """
        EnableClippingPlanes(self: DisplayPipeline, enable: bool)
            Enable or disable the Clipping Plane logic of the engine.
        
            enable: true to enable Clipping Planes, false to disable.
        """
        pass

    def EnableColorWriting(self, enable):
        """
        EnableColorWriting(self: DisplayPipeline, enable: bool)
            Enable or disable the ColorWriting behaviour of the engine.
        
            enable: true to enable ColorWriting, false to disable.
        """
        pass

    def EnableDepthTesting(self, enable):
        """
        EnableDepthTesting(self: DisplayPipeline, enable: bool)
            Enable or disable the DepthTesting behaviour of the engine. 
                    When DepthTesting is 
             disabled, objects in front will no 
                    longer occlude objects behind them.
        
        
            enable: true to enable DepthTesting, false to disable.
        """
        pass

    def EnableDepthWriting(self, enable):
        """
        EnableDepthWriting(self: DisplayPipeline, enable: bool)
            Enable or disable the DepthWriting behaviour of the engine. 
                    When DepthWriting is 
             disabled, drawn geometry does not affect the Z-Buffer.
        
        
            enable: true to enable DepthWriting, false to disable.
        """
        pass

    def EnableLighting(self, enable):
        """
        EnableLighting(self: DisplayPipeline, enable: bool)
            Enable or disable the Lighting logic of the engine.
        
            enable: true to enable Lighting, false to disable.
        """
        pass

    def InterruptDrawing(self):
        """
        InterruptDrawing(self: DisplayPipeline) -> bool
        
            Tests to see if the pipeline should stop drawing more geometry and just show what it has so far. 
             
                    If a drawing operation is taking a long time, this function will return true and 
             tell Rhino it should just 
                    finish up and show the frame buffer. This is used in 
             dynamic drawing operations.
        
            Returns: true if the pipeline should stop attempting to draw more geometry and just show the frame buffer.
        """
        pass

    def IsActive(self, rhinoObject):
        """
        IsActive(self: DisplayPipeline, rhinoObject: RhinoObject) -> bool
        
            Determines if an object can be visible in this viewport based on it's object type and display 
             attributes. 
                    This test does not check for visibility based on location of the 
             object. 
                    NOTE: Use CRhinoDisplayPipeline::IsVisible() to perform "visibility" 
            
                           tests based on location (is some part of the object in the view frustum). 
               
                        Use CRhinoDisplayPipeline::IsActive() to perform "visibility" 
                          
             tests based on object type.
        
        
            rhinoObject: Object to test.
            Returns: true if this object can be drawn in the pipeline's viewport based on it's object type and 
             display attributes.
        """
        pass

    def IsVisible(self, *__args):
        """
        IsVisible(self: DisplayPipeline, bbox: BoundingBox) -> bool
        
            Test a given box for visibility inside the view frustum under the current 
                    viewport 
             and model transformation settings.
        
        
            bbox: Box to test for visibility.
            Returns: true if at least some portion of the box is visible, false if not.
        IsVisible(self: DisplayPipeline, rhinoObject: RhinoObject) -> bool
        
            Test a given object for visibility inside the view frustum under the current viewport and model 
             
                    transformation settings. This function calls a virtual IsVisibleFinal function that 
             
                    subclassed pipelines can add extra tests to. In the base class, this test only 
             tests 
                    visibility based on the objects world coordinates location and does not pay 
             attention 
                    to the object's attributes.
                    
                    NOTE: Use 
             CRhinoDisplayPipeline::IsVisible() to perform "visibility" 
                          tests based on 
             location (is some part of the object in the view frustum). 
                          Use 
             CRhinoDisplayPipeline::IsActive() to perform "visibility" 
                          tests based on 
             object type.
        
        
            rhinoObject: Object to test.
            Returns: true if the object is visible, false if not.
        IsVisible(self: DisplayPipeline, worldCoordinate: Point3d) -> bool
        
            Test a given 3d world coordinate point for visibility inside the view 
                    frustum 
             under the current viewport and model transformation settings.
        
        
            worldCoordinate: Point to test for visibility.
            Returns: true if the point is visible, false if it is not.
        """
        pass

    def Measure2dText(self, text, definitionPoint, middleJustified, rotationRadians, height, fontFace):
        """
        Measure2dText(self: DisplayPipeline, text: str, definitionPoint: Point2d, middleJustified: bool, rotationRadians: float, height: int, fontFace: str) -> Rectangle
        
            Determines screen rectangle that would be drawn to using the Draw2dText(..) function
                   
              with the same parameters.
        
        
            text: text to measure.
            definitionPoint: either lower-left or middle of text.
            middleJustified: true=middle justified. false=lower-left justified.
            rotationRadians: text rotation in radians
            height: height in pixels (good default is 12)
            fontFace: font name (good default is "Arial")
            Returns: rectangle in the viewport's screen coordinates on success.
        """
        pass

    def PopClipTesting(self):
        """
        PopClipTesting(self: DisplayPipeline)
            Pop a ClipTesting flag off the engine's stack.
        """
        pass

    def PopCullFaceMode(self):
        """
        PopCullFaceMode(self: DisplayPipeline)
            Pop a FaceCull flag off the engine's stack.
        """
        pass

    def PopDepthTesting(self):
        """
        PopDepthTesting(self: DisplayPipeline)
            Pop a DepthTesting flag off the engine's stack.
        """
        pass

    def PopDepthWriting(self):
        """
        PopDepthWriting(self: DisplayPipeline)
            Pop a DepthWriting flag off the engine's stack.
        """
        pass

    def PopModelTransform(self):
        """
        PopModelTransform(self: DisplayPipeline)
            Pop a model transformation off the engine's model transform stack.
        """
        pass

    def PushClipTesting(self, enable):
        """
        PushClipTesting(self: DisplayPipeline, enable: bool)
            Push a ClipTesting flag on the engine's stack.
        
            enable: ClipTesting flag.
        """
        pass

    def PushCullFaceMode(self, mode):
        """
        PushCullFaceMode(self: DisplayPipeline, mode: CullFaceMode)
            Push a FaceCull flag on the engine's stack.
        
            mode: FaceCull flag.
        """
        pass

    def PushDepthTesting(self, enable):
        """
        PushDepthTesting(self: DisplayPipeline, enable: bool)
            Push a DepthTesting flag on the engine's stack.
        
            enable: DepthTesting flag.
        """
        pass

    def PushDepthWriting(self, enable):
        """
        PushDepthWriting(self: DisplayPipeline, enable: bool)
            Push a DepthWriting flag on the engine's stack.
        
            enable: DepthWriting flag.
        """
        pass

    def PushModelTransform(self, xform):
        """
        PushModelTransform(self: DisplayPipeline, xform: Transform)
            Push a model transformation on the engine's model transform stack.
        
            xform: Transformation to push.
        """
        pass

    DefaultCurveThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the curve thickness as defined by the current display mode. 
            Note: this only applies to curve objects, Brep and Mesh wires may have different settings.

Get: DefaultCurveThickness(self: DisplayPipeline) -> int

"""

    DepthMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DepthMode(self: DisplayPipeline) -> DepthMode

Set: DepthMode(self: DisplayPipeline) = value
"""

    DisplayPipelineAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayPipelineAttributes(self: DisplayPipeline) -> DisplayPipelineAttributes

"""

    DrawingGrips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the pipeline is currently in a grip drawing operation.

Get: DrawingGrips(self: DisplayPipeline) -> bool

"""

    DrawingSurfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the pipeline is currently in a surface
            drawing operation.  Surface drawing means draw the shaded triangles of a mesh
            representing the surface (mesh, extrusion, or brep).  This is useful when
            inside of a draw event or display conduit to check and see if the geometry is
            about to be drawn as a shaded set of triangles representing the geometry.
            See DrawingWires to check and see if the wireframe representation of the
            geometry is going to be drawn.

Get: DrawingSurfaces(self: DisplayPipeline) -> bool

"""

    DrawingWires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the pipeline is currently in a curve
            drawing operation. This is useful when inside of a draw event or display
            conduit to check and see if the geometry is about to be drawn is going to
            be drawing the wire representation of the geometry (mesh, extrusion, or
            brep).  See DrawingSurfaces to check and see if the shaded mesh representation
            of the geometry is going to be drawn.

Get: DrawingWires(self: DisplayPipeline) -> bool

"""

    FrameSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the framebuffer that this pipeline is drawing to.

Get: FrameSize(self: DisplayPipeline) -> Size

"""

    IsDynamicDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the viewport is in Dynamic Display state. 
            Dynamic display is the state a viewport is in when it is rapidly redrawing because of
            an operation like panning or rotating. The pipeline will drop some level of detail
            while inside a dynamic display state to keep the frame rate as high as possible.

Get: IsDynamicDisplay(self: DisplayPipeline) -> bool

"""

    IsOpenGL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this pipeline is drawing into an OpenGL context.

Get: IsOpenGL(self: DisplayPipeline) -> bool

"""

    IsPrinting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this pipeline 
            is currently drawing for printing purposes.

Get: IsPrinting(self: DisplayPipeline) -> bool

"""

    IsStereoMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this pipeline is currently using an 
            engine that is performing stereo style drawing. Stereo drawing is for 
            providing an "enhanced 3-D" effect through stereo viewing devices.

Get: IsStereoMode(self: DisplayPipeline) -> bool

"""

    ModelTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current model transformation that is applied to vertices when drawing.

Get: ModelTransform(self: DisplayPipeline) -> Transform

Set: ModelTransform(self: DisplayPipeline) = value
"""

    ModelTransformIsIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the Model Transform is an Identity transformation.

Get: ModelTransformIsIdentity(self: DisplayPipeline) -> bool

"""

    NestLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current nested viewport drawing level. 
            This is used to know if you are currently inside the drawing of a nested viewport (detail object in Rhino). 
            Nest level = 0 Drawing is occuring in a standard Rhino viewport or on the page viewport.Nest level = 1 Drawing is occuring inside a detail view object.

Get: NestLevel(self: DisplayPipeline) -> int

"""

    RenderPass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current pass that the pipeline is in for drawing a frame. 
            Typically drawing a frame requires a single pass through the DrawFrameBuffer 
            function, but some special display effects can be achieved through 
            drawing with multiple passes.

Get: RenderPass(self: DisplayPipeline) -> int

"""

    ShadingRequired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the "ShadingRequired" flag. This flag gets set inside the pipeline when a request is 
            made to draw a shaded mesh but the current render engine doesn't support shaded 
            mesh drawing...at this point the redraw mechanism will make sure everything will 
            work the next time around.

Get: ShadingRequired(self: DisplayPipeline) -> bool

Set: ShadingRequired(self: DisplayPipeline) = value
"""

    StereoProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current stereo projection if stereo mode is on.
            0 = left1 = right
            If stereo mode is not enables, this property always returns 0.

Get: StereoProjection(self: DisplayPipeline) -> int

"""

    SupportsShading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether or not this pipeline supports shaded meshes.

Get: SupportsShading(self: DisplayPipeline) -> bool

"""

    Viewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Viewport(self: DisplayPipeline) -> RhinoViewport

"""

    ZBiasMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZBiasMode(self: DisplayPipeline) -> ZBiasMode

Set: ZBiasMode(self: DisplayPipeline) = value
"""


    CalculateBoundingBox = None
    CalculateBoundingBoxZoomExtents = None
    DrawForeground = None
    DrawOverlay = None
    ObjectCulling = None
    PostDrawObjects = None
    PreDrawObject = None
    PreDrawObjects = None


class DisplayPipelineAttributes(object, IDisposable, ISerializable):
    """ Represents display pipeline settings, such as "show transparency" and "show grips". """
    def Dispose(self):
        """ Dispose(self: DisplayPipelineAttributes) """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: DisplayPipelineAttributes, info: SerializationInfo, context: StreamingContext) """
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
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CurveColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Color used for drawing curves

Get: CurveColor(self: DisplayPipelineAttributes) -> Color

Set: CurveColor(self: DisplayPipelineAttributes) = value
"""

    CurveThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Pixel thickness for curves

Get: CurveThickness(self: DisplayPipelineAttributes) -> int

Set: CurveThickness(self: DisplayPipelineAttributes) = value
"""

    DisableConduits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisableConduits(self: DisplayPipelineAttributes) -> bool

Set: DisableConduits(self: DisplayPipelineAttributes) = value
"""

    DisableTransparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisableTransparency(self: DisplayPipelineAttributes) -> bool

Set: DisableTransparency(self: DisplayPipelineAttributes) = value
"""

    EnglishName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnglishName(self: DisplayPipelineAttributes) -> str

Set: EnglishName(self: DisplayPipelineAttributes) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: DisplayPipelineAttributes) -> Guid

"""

    IgnoreHighlights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IgnoreHighlights(self: DisplayPipelineAttributes) -> bool

Set: IgnoreHighlights(self: DisplayPipelineAttributes) = value
"""

    LocalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalName(self: DisplayPipelineAttributes) -> str

"""

    LockedObjectsDrawBehindOthers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Locked object are drawn behind other objects

Get: LockedObjectsDrawBehindOthers(self: DisplayPipelineAttributes) -> bool

Set: LockedObjectsDrawBehindOthers(self: DisplayPipelineAttributes) = value
"""

    MeshSpecificAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MeshSpecificAttributes(self: DisplayPipelineAttributes) -> MeshDisplayAttributes

"""

    ObjectColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectColor(self: DisplayPipelineAttributes) -> Color

Set: ObjectColor(self: DisplayPipelineAttributes) = value
"""

    ShadingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Draw shaded meshes and surfaces

Get: ShadingEnabled(self: DisplayPipelineAttributes) -> bool

Set: ShadingEnabled(self: DisplayPipelineAttributes) = value
"""

    ShowCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Draw curves

Get: ShowCurves(self: DisplayPipelineAttributes) -> bool

Set: ShowCurves(self: DisplayPipelineAttributes) = value
"""

    ShowGrips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowGrips(self: DisplayPipelineAttributes) -> bool

Set: ShowGrips(self: DisplayPipelineAttributes) = value
"""

    ViewSpecificAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewSpecificAttributes(self: DisplayPipelineAttributes) -> ViewDisplayAttributes

"""

    XrayAllObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XrayAllObjects(self: DisplayPipelineAttributes) -> bool

Set: XrayAllObjects(self: DisplayPipelineAttributes) = value
"""


    MeshDisplayAttributes = None
    ViewDisplayAttributes = None


class DrawForegroundEventArgs(DrawEventArgs):
    # no doc
    DrawWorldAxes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawWorldAxes(self: DrawForegroundEventArgs) -> bool

Set: DrawWorldAxes(self: DrawForegroundEventArgs) = value
"""

    WorldAxesDrawn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WorldAxesDrawn(self: DrawForegroundEventArgs) -> bool

Set: WorldAxesDrawn(self: DrawForegroundEventArgs) = value
"""



class DrawFrameStages(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) DrawFrameStages, values: All (4294836223), CalculateBoundingBox (8), CalculateClippingPlanes (16), DrawBackground (64), DrawForeGround (1024), DrawMiddleGround (896), DrawObject (256), DrawOverlay (2048), InitializeFrameBuffer (1), MeshingParameters (8192), ObjectBasedChannel (114948), ObjectCulling (4), ObjectDisplayAttributes (16384), PostDrawObjects (512), PostObjectDraw (65536), PostProcessFrameBuffer (4096), PreDrawObjects (128), PreObjectDraw (32768), SetupFrustum (2), SetupLighting (32), ViewExtents (131072) """
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

    All = None
    CalculateBoundingBox = None
    CalculateClippingPlanes = None
    DrawBackground = None
    DrawForeGround = None
    DrawMiddleGround = None
    DrawObject = None
    DrawOverlay = None
    InitializeFrameBuffer = None
    MeshingParameters = None
    ObjectBasedChannel = None
    ObjectCulling = None
    ObjectDisplayAttributes = None
    PostDrawObjects = None
    PostObjectDraw = None
    PostProcessFrameBuffer = None
    PreDrawObjects = None
    PreObjectDraw = None
    SetupFrustum = None
    SetupLighting = None
    value__ = None
    ViewExtents = None


class DrawObjectEventArgs(DrawEventArgs):
    # no doc
    DrawObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawObject(self: DrawObjectEventArgs) -> bool

Set: DrawObject(self: DrawObjectEventArgs) = value
"""

    RhinoObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RhinoObject(self: DrawObjectEventArgs) -> RhinoObject

"""



class PageViewSpaceChangeEventArgs(EventArgs):
    # no doc
    NewActiveDetailId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the detail object was set active.  Note, if this id is
            equal to Guid.Empty, then the active detail object is the page
            view itself.

Get: NewActiveDetailId(self: PageViewSpaceChangeEventArgs) -> Guid

"""

    OldActiveDetailId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the previously active detail object. Note, if this id
            is equal to Guid.Empty, then the active detail object was the
            page view itself.

Get: OldActiveDetailId(self: PageViewSpaceChangeEventArgs) -> Guid

"""

    PageView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The page view on which a different detail object was set active.

Get: PageView(self: PageViewSpaceChangeEventArgs) -> RhinoPageView

"""



class PointStyle(Enum, IComparable, IFormattable, IConvertible):
    """ enum PointStyle, values: ActivePoint (2), ControlPoint (1), Simple (0), X (3) """
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

    ActivePoint = None
    ControlPoint = None
    Simple = None
    value__ = None
    X = None


class RhinoView(object):
    """
    A RhinoView represents a single "window" display of a document. A view could
                contain one or many RhinoViewports (many in the case of Layout views with detail viewports).
                Standard Rhino modeling views have one viewport.
    """
    def CaptureToBitmap(self, *__args):
        """
        CaptureToBitmap(self: RhinoView, mode: DisplayModeDescription) -> Bitmap
        
            Capture View contents to a bitmap using a display mode description to define
                    how 
             drawing is performed.
        
        
            mode: The display mode.
            Returns: A new bitmap.
        CaptureToBitmap(self: RhinoView, size: Size, mode: DisplayModeDescription) -> Bitmap
        
            Capture View contents to a bitmap using a display mode description to define
                    how 
             drawing is performed.
        
        
            size: The width and height of the returned bitmap.
            mode: The display mode.
            Returns: A new bitmap.
        CaptureToBitmap(self: RhinoView, attributes: DisplayPipelineAttributes) -> Bitmap
        
            Captures view contents to a bitmap using display attributes to define how
                    drawing 
             is performed.
        
        
            attributes: The specific display mode attributes.
            Returns: A new bitmap.
        CaptureToBitmap(self: RhinoView, size: Size, attributes: DisplayPipelineAttributes) -> Bitmap
        
            Capture View contents to a bitmap using display attributes to define how
                    drawing is 
             performed.
        
        
            size: The width and height of the returned bitmap.
            attributes: The specific display mode attributes.
            Returns: A new bitmap.
        CaptureToBitmap(self: RhinoView, size: Size) -> Bitmap
        
            Capture View contents to a bitmap.
        
            size: Size of Bitmap to capture to.
            Returns: The bitmap of the specified part of the view.
        CaptureToBitmap(self: RhinoView) -> Bitmap
        
            Capture View contents to a bitmap.
            Returns: The bitmap of the complete view.
        CaptureToBitmap(self: RhinoView, grid: bool, worldAxes: bool, cplaneAxes: bool) -> Bitmap
        
            Captures the view contents to a bitmap allowing for visibility of grid and axes.
        
            grid: true if the construction plane grid should be visible.
            worldAxes: true if the world axis should be visible.
            cplaneAxes: true if the construction plane close the the grid should be visible.
            Returns: A new bitmap.
        CaptureToBitmap(self: RhinoView, size: Size, grid: bool, worldAxes: bool, cplaneAxes: bool) -> Bitmap
        
            Captures a part of the view contents to a bitmap allowing for visibility of grid and axes.
        
            size: The width and height of the returned bitmap.
            grid: true if the construction plane grid should be visible.
            worldAxes: true if the world axis should be visible.
            cplaneAxes: true if the construction plane close the the grid should be visible.
            Returns: A new bitmap.
        """
        pass

    def ClientToScreen(self, clientPoint):
        """
        ClientToScreen(self: RhinoView, clientPoint: Point2d) -> Point2d
        ClientToScreen(self: RhinoView, clientPoint: Point) -> Point
        """
        pass

    def Close(self):
        """
        Close(self: RhinoView) -> bool
        
            Remove this View from Rhino. DO NOT attempt to use this instance of this
                    class 
             after calling Close.
        
            Returns: true on success
        """
        pass

    def CreateShadedPreviewImage(self, imagePath, size, ignoreHighlights, drawConstructionPlane, useGhostedShading):
        """
        CreateShadedPreviewImage(self: RhinoView, imagePath: str, size: Size, ignoreHighlights: bool, drawConstructionPlane: bool, useGhostedShading: bool) -> bool
        
            Creates a bitmap preview image of model.
        
            imagePath: [in] The name of the bitmap file to create.  The extension of the imagePath controls
                   
              the format of the bitmap file created (bmp, tga, jpg, pcx, png, tif).
        
            size: [in] The width and height of the bitmap in pixels.
            ignoreHighlights: true if highlighted elements should be drawn normally.
            drawConstructionPlane: true if the CPlane should be drawn.
            useGhostedShading: true if ghosted shading (partially transparent shading) should be used.
            Returns: true if successful.
        """
        pass

    def CreateWireframePreviewImage(self, imagePath, size, ignoreHighlights, drawConstructionPlane):
        """
        CreateWireframePreviewImage(self: RhinoView, imagePath: str, size: Size, ignoreHighlights: bool, drawConstructionPlane: bool) -> bool
        
            Creates a bitmap preview image of model.
        
            imagePath: [in] The name of the bitmap file to create.  The extension of the imagePath controls
                   
              the format of the bitmap file created (bmp, tga, jpg, pcx, png, tif).
        
            size: [in] The width and height of the bitmap in pixels.
            ignoreHighlights: true if highlighted elements should be drawn normally.
            drawConstructionPlane: true if the CPlane should be drawn.
            Returns: true if successful.
        """
        pass

    def Redraw(self):
        """
        Redraw(self: RhinoView)
            Redraws this view.
        """
        pass

    def ScreenToClient(self, screenPoint):
        """
        ScreenToClient(self: RhinoView, screenPoint: Point2d) -> Point2d
        ScreenToClient(self: RhinoView, screenPoint: Point) -> Point
        
            Converts a point in screen coordinates to client coordinates for this view.
        
            screenPoint: The 2D screen point.
            Returns: A 2D point in client coordinates.
        """
        pass

    def SpeedTest(self, frameCount, freezeDrawList, direction, angleDeltaRadians):
        """ SpeedTest(self: RhinoView, frameCount: int, freezeDrawList: bool, direction: int, angleDeltaRadians: float) -> float """
        pass

    ActiveViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ActiveViewport is the same as the MainViewport for standard RhinoViews. In
            a RhinoPageView, the active viewport may be the RhinoViewport of a child detail object.
            Most of the time, you will use ActiveViewport unless you explicitly need to work with
            the main viewport.

Get: ActiveViewport(self: RhinoView) -> RhinoViewport

"""

    ActiveViewportID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns viewport ID for the active viewport. Faster than ActiveViewport function when
            working with page views.

Get: ActiveViewportID(self: RhinoView) -> Guid

"""

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size and location of the view including its nonclient elements, in pixels, relative to the parent control.

Get: Bounds(self: RhinoView) -> Rectangle

"""

    ClientRectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rectangle that represents the client area of the view.

Get: ClientRectangle(self: RhinoView) -> Rectangle

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: RhinoView) -> RhinoDoc

"""

    Floating = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Floating state of RhinoView.
            if true, then the view will be in a floating frame window. Otherwise
            the view will be embeded in the main frame.

Get: Floating(self: RhinoView) -> bool

Set: Floating(self: RhinoView) = value
"""

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the window handle that this view is bound to.

Get: Handle(self: RhinoView) -> IntPtr

"""

    MainViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A RhinoView contains a "main viewport" that fills the entire view client window.
            RhinoPageViews may also contain nested child RhinoViewports for implementing
            detail viewports.
            The MainViewport will always return this RhinoView's m_vp.

Get: MainViewport(self: RhinoView) -> RhinoViewport

"""

    Maximized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Maximized(self: RhinoView) -> bool

Set: Maximized(self: RhinoView) = value
"""

    ScreenRectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rectangle that represents the client area of the view in screen coordinates.

Get: ScreenRectangle(self: RhinoView) -> Rectangle

"""

    TitleVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Visibility of the viewport title window.

Get: TitleVisible(self: RhinoView) -> bool

Set: TitleVisible(self: RhinoView) = value
"""


    Create = None
    Destroy = None
    Rename = None
    SetActive = None


class RhinoPageView(RhinoView):
    # no doc
    def AddDetailView(self, title, corner0, corner1, initialProjection):
        """
        AddDetailView(self: RhinoPageView, title: str, corner0: Point2d, corner1: Point2d, initialProjection: DefinedViewportProjection) -> DetailViewObject
        
            Creates a detail view object that is displayed on this page and adds it to the doc.
        
            title: The detail view title.
            corner0: Corners of the detail view in world coordinates.
            corner1: Corners of the detail view in world coordinates.
            initialProjection: The defined initial projection type.
            Returns: Newly created detail view on success. null on error.
        """
        pass

    def GetDetailViews(self):
        """
        GetDetailViews(self: RhinoPageView) -> Array[DetailViewObject]
        
            Gets a list of the detail view objects associated with this layout.
            Returns: A detail view object array. This can be null, but not empty.
        """
        pass

    def SetActiveDetail(self, *__args):
        """
        SetActiveDetail(self: RhinoPageView, detailName: str, compareCase: bool) -> bool
        SetActiveDetail(self: RhinoPageView, detailId: Guid) -> bool
        """
        pass

    def SetPageAsActive(self):
        """ SetPageAsActive(self: RhinoPageView) """
        pass

    ActiveViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ActiveViewport is the same as the MainViewport for standard RhinoViews. In
            a RhinoPageView, the active viewport may be the RhinoViewport of a child detail object.
            Most of the time, you will use ActiveViewport unless you explicitly need to work with
            the main viewport.

Get: ActiveViewport(self: RhinoPageView) -> RhinoViewport

"""

    ActiveViewportID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns viewport ID for the active viewport. Faster than ActiveViewport function when
            working with page views.

Get: ActiveViewportID(self: RhinoPageView) -> Guid

"""

    PageHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Height of the page in the document's PageUnitSystem

Get: PageHeight(self: RhinoPageView) -> float

Set: PageHeight(self: RhinoPageView) = value
"""

    PageIsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if the page is active instead of any detail views. This occurs
            when the MainViewport.Id == ActiveViewportID.

Get: PageIsActive(self: RhinoPageView) -> bool

"""

    PageName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Same as the MainViewport.Name.

Get: PageName(self: RhinoPageView) -> str

Set: PageName(self: RhinoPageView) = value
"""

    PageNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the runtime page number and updates the page number for all
            of the other pages. The first page has a value of 0

Get: PageNumber(self: RhinoPageView) -> int

Set: PageNumber(self: RhinoPageView) = value
"""

    PageWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Width of the page in the document's PageUnitSystem

Get: PageWidth(self: RhinoPageView) -> float

Set: PageWidth(self: RhinoPageView) = value
"""


    PageViewSpaceChange = None


class RhinoViewport(object, IDisposable):
    """
    Displays geometry with a given projection. In standard modeling views there
                is a one to one relationship between RhinoView and RhinoViewports. In a page
                layout, there may be multiple RhinoViewports for a single layout.
    
    RhinoViewport()
    RhinoViewport(other: RhinoViewport)
    """
    def ChangeToParallelProjection(self, symmetricFrustum):
        """
        ChangeToParallelProjection(self: RhinoViewport, symmetricFrustum: bool) -> bool
        
            Use this function to change projections of valid viewports from persective to parallel.
                
                 It will make common additional adjustments to the frustum so the resulting views are
               
                  similar. The camera location and direction will not be changed.
        
        
            symmetricFrustum: true if you want the resulting frustum to be symmetric.
            Returns: If the current projection is parallel and bSymmetricFrustum, FrustumIsLeftRightSymmetric()
             
                    and FrustumIsTopBottomSymmetric() are all equal, then no changes are made and true is 
             returned.
        """
        pass

    def ChangeToPerspectiveProjection(self, *__args):
        """
        ChangeToPerspectiveProjection(self: RhinoViewport, targetDistance: float, symmetricFrustum: bool, lensLength: float) -> bool
        
            Use this function to change projections of valid viewports from parallel to perspective.
               
                  It will make common additional adjustments to the frustum and camera location so the
              
                   resulting views are similar. The camera direction and target point are not be changed.
        
        
            targetDistance: If RhinoMath.UnsetValue this parameter is ignored. Otherwise it must be > 0 and indicates
              
                   which plane in the current view frustum should be perserved.
        
            symmetricFrustum: true if you want the resulting frustum to be symmetric.
            lensLength: (pass 50.0 when in doubt) 35 mm lens length to use when changing from parallel to perspective
          
                       projections. If the current projection is perspective or lens_length is <= 0.0, then
         
                        this parameter is ignored.
        
            Returns: If the current projection is perspective and bSymmetricFrustum, FrustumIsLeftRightSymmetric()
          
                       and FrustumIsTopBottomSymmetric() are all equal, then no changes are made and true is 
             returned.
        
        ChangeToPerspectiveProjection(self: RhinoViewport, symmetricFrustum: bool, lensLength: float) -> bool
        
            Use this function to change projections of valid viewports from parallel to perspective.
               
                  It will make common additional adjustments to the frustum and camera location so the
              
                   resulting views are similar. The camera direction and target point are not be changed.
        
        
            symmetricFrustum: true if you want the resulting frustum to be symmetric.
            lensLength: (pass 50.0 when in doubt) 35 mm lens length to use when changing from parallel to perspective
          
                       projections. If the current projection is perspective or lens_length is <= 0.0, then
         
                        this parameter is ignored.
        
            Returns: If the current projection is perspective and bSymmetricFrustum, FrustumIsLeftRightSymmetric()
          
                       and FrustumIsTopBottomSymmetric() are all equal, then no changes are made and true is 
             returned.
        """
        pass

    def ClearTraceImage(self):
        """
        ClearTraceImage(self: RhinoViewport)
            Remove trace image (background bitmap) for this viewport if one exists.
        """
        pass

    def ClientToScreen(self, clientPoint):
        """
        ClientToScreen(self: RhinoViewport, clientPoint: Point) -> Point
        ClientToScreen(self: RhinoViewport, clientPoint: Point2d) -> Point
        """
        pass

    def ClientToWorld(self, clientPoint):
        """
        ClientToWorld(self: RhinoViewport, clientPoint: Point2d) -> Line
        ClientToWorld(self: RhinoViewport, clientPoint: Point) -> Line
        """
        pass

    def ConstructionPlane(self):
        """
        ConstructionPlane(self: RhinoViewport) -> Plane
        
            Simple plane information for this viewport's construction plane. If you want
                    
             detailed construction lpane information, use GetConstructionPlane.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RhinoViewport) """
        pass

    def GetCameraAngle(self, halfDiagonalAngle, halfVerticalAngle, halfHorizontalAngle):
        """ GetCameraAngle(self: RhinoViewport) -> (bool, float, float, float) """
        pass

    def GetCameraExtents(self, points):
        """ GetCameraExtents(self: RhinoViewport, points: IEnumerable[Point3d]) -> BoundingBox """
        pass

    def GetCameraFrame(self, frame):
        """
        GetCameraFrame(self: RhinoViewport) -> (bool, Plane)
        
            Gets the camera plane.
            Returns: true if current camera orientation is valid.
        """
        pass

    def GetConstructionPlane(self):
        """ GetConstructionPlane(self: RhinoViewport) -> ConstructionPlane """
        pass

    def GetDepth(self, *__args):
        """
        GetDepth(self: RhinoViewport, sphere: Sphere) -> (bool, float, float)
        
            Gets near and far clipping distances of a sphere.
        
            sphere: The sphere.
            Returns: true if the sphere intersects the view frustum and near_dist/far_dist were set.
                    
             false if the sphere does not intesect the view frustum.
        
        GetDepth(self: RhinoViewport, bbox: BoundingBox) -> (bool, float, float)
        
            Gets near and far clipping distances of a bounding box.
        
            bbox: The bounding box.
            Returns: true if the bounding box intersects the view frustum and near_dist/far_dist were set.
                  
               false if the bounding box does not intesect the view frustum.
        
        GetDepth(self: RhinoViewport, point: Point3d) -> (bool, float)
        
            Gets clipping distance of a point.
        
            point: A 3D point.
            Returns: true if the point is ing the view frustum and near_dist/far_dist were set.
                    false if 
             the bounding box does not intesect the view frustum.
        """
        pass

    def GetFarRect(self):
        """
        GetFarRect(self: RhinoViewport) -> Array[Point3d]
        
            Get corners of far clipping plane rectangle.
            Returns: [left_bottom, right_bottom, left_top, right_top] points on success
                    null on failure.
        """
        pass

    def GetFrustum(self, left, right, bottom, top, nearDistance, farDistance):
        """
        GetFrustum(self: RhinoViewport) -> (bool, float, float, float, float, float, float)
        
            Gets the view frustum.
            Returns: true if operation succeeded.
        """
        pass

    def GetFrustumBottomPlane(self, plane):
        """
        GetFrustumBottomPlane(self: RhinoViewport) -> (bool, Plane)
        
            Get bottom world frustum clipping plane.
            Returns: true if camera and frustum are valid and plane was set.
        """
        pass

    def GetFrustumBoundingBox(self):
        """ GetFrustumBoundingBox(self: RhinoViewport) -> BoundingBox """
        pass

    def GetFrustumCenter(self, center):
        """
        GetFrustumCenter(self: RhinoViewport) -> (bool, Point3d)
        
            Returns world coordinates of frustum's center.
            Returns: true if the center was successfully computed.
        """
        pass

    def GetFrustumFarPlane(self, plane):
        """
        GetFrustumFarPlane(self: RhinoViewport) -> (bool, Plane)
        
            Get far clipping plane.
            Returns: true if camera and frustum are valid.
        """
        pass

    def GetFrustumLeftPlane(self, plane):
        """
        GetFrustumLeftPlane(self: RhinoViewport) -> (bool, Plane)
        
            Get left world frustum clipping plane.
            Returns: true if camera and frustum are valid and plane was set.
        """
        pass

    def GetFrustumLine(self, screenX, screenY, worldLine):
        """
        GetFrustumLine(self: RhinoViewport, screenX: float, screenY: float) -> (bool, Line)
        
            Gets the world coordinate line in the view frustum that projects to a point on the screen.
        
            screenX: (screenx,screeny) = screen location.
            screenY: (screenx,screeny) = screen location.
            Returns: true if successful.
                    false if view projection or frustum is invalid.
        """
        pass

    def GetFrustumNearPlane(self, plane):
        """
        GetFrustumNearPlane(self: RhinoViewport) -> (bool, Plane)
        
            Get near clipping plane.
            Returns: true if camera and frustum are valid.
        """
        pass

    def GetFrustumRightPlane(self, plane):
        """
        GetFrustumRightPlane(self: RhinoViewport) -> (bool, Plane)
        
            Get right world frustum clipping plane.
            Returns: true if camera and frustum are valid and plane was set.
        """
        pass

    def GetFrustumTopPlane(self, plane):
        """
        GetFrustumTopPlane(self: RhinoViewport) -> (bool, Plane)
        
            Get top world frustum clipping plane.
            Returns: true if camera and frustum are valid and plane was set.
        """
        pass

    def GetNearRect(self):
        """
        GetNearRect(self: RhinoViewport) -> Array[Point3d]
        
            Get corners of near clipping plane rectangle.
            Returns: [left_bottom, right_bottom, left_top, right_top] points on success
                    null on failure.
        """
        pass

    def GetPickTransform(self, *__args):
        """
        GetPickTransform(self: RhinoViewport, clientRectangle: Rectangle) -> Transform
        
            Takes a rectangle in screen coordinates and returns a transformation
                    that maps the 
             3d frustum defined by the rectangle to a -1/+1 clipping
                    coordinate box.
        
        
            clientRectangle: The client rectangle.
            Returns: A transformation matrix.
        GetPickTransform(self: RhinoViewport, clientPoint: Point) -> Transform
        
            Takes a rectangle in screen coordinates and returns a transformation
                    that maps the 
             3d frustum defined by the rectangle to a -1/+1 clipping
                    coordinate box. This takes 
             a single point and inflates it by
                    
             Rhino.ApplicationSettings.ModelAidSettings.MousePickBoxRadius to define
                    the screen 
             rectangle.
        
        
            clientPoint: The client point.
            Returns: A transformation matrix.
        GetPickTransform(self: RhinoViewport, clientX: int, clientY: int) -> Transform
        
            Takes a rectangle in screen coordinates and returns a transformation
                    that maps the 
             3d frustum defined by the rectangle to a -1/+1 clipping
                    coordinate box. This takes 
             a single point and inflates it by
                    
             Rhino.ApplicationSettings.ModelAidSettings.MousePickBoxRadius to define
                    the screen 
             rectangle.
        
        
            clientX: The client point X coordinate.
            clientY: The client point Y coordinate.
            Returns: A transformation matrix.
        """
        pass

    def GetScreenPort(self, portLeft, portRight, portBottom, portTop, portNear, portFar):
        """
        GetScreenPort(self: RhinoViewport) -> (bool, int, int, int, int, int, int)
        
            Location of viewport in pixels.  These are provided so you can set the port you are using
              
                   and get the appropriate transformations to and from screen space.
        
            Returns: true if the operation is successful.
        """
        pass

    def GetTransform(self, sourceSystem, destinationSystem):
        """
        GetTransform(self: RhinoViewport, sourceSystem: CoordinateSystem, destinationSystem: CoordinateSystem) -> Transform
        
            Gets a transform from origin coordinate system to a target coordinate system.
        
            sourceSystem: The origin coordinate system.
            destinationSystem: The target coordinate system.
            Returns: 4x4 transformation matrix (acts on the left)
                    Identity matrix is returned if this 
             function fails.
        """
        pass

    def GetWorldToScreenScale(self, pointInFrustum, pixelsPerUnit):
        """
        GetWorldToScreenScale(self: RhinoViewport, pointInFrustum: Point3d) -> (bool, float)
        
            Gets the world to screen size scaling factor at a point in frustum.
        
            pointInFrustum: A point in frustum.
            Returns: true if the operation is successful.
        """
        pass

    def IsVisible(self, *__args):
        """
        IsVisible(self: RhinoViewport, point: Point3d) -> bool
        
            Deterines if a world coordinate point is visible in the viewing frustum.
        
            point: A point that is tested for visibility.
            Returns: true if the point is visible; otherwise false.
        IsVisible(self: RhinoViewport, bbox: BoundingBox) -> bool
        
            Returns true if some portion of a world coordinate bounding box is
                    potentially 
             visible in the viewing frustum.
        
        
            bbox: A bounding box that is tested for visibility.
            Returns: true if the box is potentially visible; otherwise false.
        """
        pass

    def KeyboardDolly(self, leftRight, amount):
        """
        KeyboardDolly(self: RhinoViewport, leftRight: bool, amount: float) -> bool
        
            Emulates the keyboard arrow key in terms of interaction.
        
            leftRight: left/right dolly if true, up/down dolly if false.
            amount: The dolly amount.
            Returns: true if operation succeeded; otherwise false.
        """
        pass

    def KeyboardDollyInOut(self, amount):
        """
        KeyboardDollyInOut(self: RhinoViewport, amount: float) -> bool
        
            Emulates the keyboard arrow key in terms of interaction.
        
            amount: The dolly amount.
            Returns: true if operation succeeded; otherwise false.
        """
        pass

    def KeyboardRotate(self, leftRight, angleRadians):
        """
        KeyboardRotate(self: RhinoViewport, leftRight: bool, angleRadians: float) -> bool
        
            Emulates the keyboard arrow key in terms of interaction.
        
            leftRight: left/right rotate if true, up/down rotate if false.
            angleRadians: If less than 0, rotation is to left or down.
                    If greater than 0, rotation is to 
             right or up.
        
            Returns: true if operation succeeded; otherwise false.
        """
        pass

    def Magnify(self, magnificationFactor, mode, fixedScreenPoint=None):
        """
        Magnify(self: RhinoViewport, magnificationFactor: float, mode: bool, fixedScreenPoint: Point) -> bool
        
            Zooms or dollies in order to scale the viewport projection of observed objects.
        
            magnificationFactor: The scale factor.
            mode: false = perform a "dolly" magnification by moving the camera towards/away from
                    the 
             target so that the amount of the screen subtended by an object changes.
                    true = 
             perform a "zoom" magnification by adjusting the "lens" angle
        
            fixedScreenPoint: A point in the sceen that should remain fixed.
            Returns: true if operation succeeded; otherwise false.
        Magnify(self: RhinoViewport, magnificationFactor: float, mode: bool) -> bool
        
            Zooms or dollies in order to scale the viewport projection of observed objects.
        
            magnificationFactor: The scale factor.
            mode: false = perform a "dolly" magnification by moving the camera towards/away from
                    the 
             target so that the amount of the screen subtended by an object changes.
                    true = 
             perform a "zoom" magnification by adjusting the "lens" angle
        
            Returns: true if operation succeeded; otherwise false.
        """
        pass

    def MouseDollyZoom(self, mousePreviousPoint, mouseCurrentPoint):
        """ MouseDollyZoom(self: RhinoViewport, mousePreviousPoint: Point, mouseCurrentPoint: Point) -> bool """
        pass

    def MouseInOutDolly(self, mousePreviousPoint, mouseCurrentPoint):
        """ MouseInOutDolly(self: RhinoViewport, mousePreviousPoint: Point, mouseCurrentPoint: Point) -> bool """
        pass

    def MouseMagnify(self, mousePreviousPoint, mouseCurrentPoint):
        """ MouseMagnify(self: RhinoViewport, mousePreviousPoint: Point, mouseCurrentPoint: Point) -> bool """
        pass

    def MouseRotateAroundTarget(self, mousePreviousPoint, mouseCurrentPoint):
        """
        MouseRotateAroundTarget(self: RhinoViewport, mousePreviousPoint: Point, mouseCurrentPoint: Point) -> bool
        
            Rotates the viewport around target.
        
            mousePreviousPoint: The mouse previous point.
            mouseCurrentPoint: The mouse current point.
        """
        pass

    def MouseRotateCamera(self, mousePreviousPoint, mouseCurrentPoint):
        """
        MouseRotateCamera(self: RhinoViewport, mousePreviousPoint: Point, mouseCurrentPoint: Point) -> bool
        
            Rotates the view around the camera location.
        
            mousePreviousPoint: The mouse previous point.
            mouseCurrentPoint: The mouse current point.
        """
        pass

    def MouseTilt(self, mousePreviousPoint, mouseCurrentPoint):
        """ MouseTilt(self: RhinoViewport, mousePreviousPoint: Point, mouseCurrentPoint: Point) -> bool """
        pass

    def NextConstructionPlane(self):
        """
        NextConstructionPlane(self: RhinoViewport) -> bool
        
            Sets the construction plane to the plane that was
                    active before the last call to 
             PreviousConstructionPlane.
        
            Returns: true if successful.
        """
        pass

    def NextViewProjection(self):
        """
        NextViewProjection(self: RhinoViewport) -> bool
        
            Sets the view projection and target to the settings that 
                    were active before the 
             last call to PrevView.
        
            Returns: true if the view stack was popped.
        """
        pass

    def PopConstructionPlane(self):
        """
        PopConstructionPlane(self: RhinoViewport) -> bool
        
            Sets the construction plane to the plane that was
                    active before the last call to 
             PushConstructionPlane.
        
            Returns: true if a construction plane was popped.
        """
        pass

    def PopViewProjection(self):
        """
        PopViewProjection(self: RhinoViewport) -> bool
        
            Sets the view projection and target to the settings at the top of
                    the view stack 
             and removes those settings from the view stack.
        
            Returns: true if there were settings that could be popped from the stack.
        """
        pass

    def PreviousConstructionPlane(self):
        """
        PreviousConstructionPlane(self: RhinoViewport) -> bool
        
            Sets the construction plane to the plane that was
                    active before the last call to 
             NextConstructionPlane
                    or SetConstructionPlane.
        
            Returns: true if successful.
        """
        pass

    def PreviousViewProjection(self):
        """
        PreviousViewProjection(self: RhinoViewport) -> bool
        
            Sets the view projection and target to the settings that
                    were active before the 
             last call to NextViewProjection.
        
            Returns: true if the view stack was popped.
        """
        pass

    def PushConstructionPlane(self, cplane):
        """
        PushConstructionPlane(self: RhinoViewport, cplane: ConstructionPlane)
            Pushes the current construction plane on the viewport's
                    construction plane stack 
             and sets the construction plane
                    to cplane.
        
        
            cplane: The constuction plane to push.
        """
        pass

    def PushViewInfo(self, viewinfo, includeTraceImage):
        """ PushViewInfo(self: RhinoViewport, viewinfo: ViewInfo, includeTraceImage: bool) -> bool """
        pass

    def PushViewProjection(self):
        """
        PushViewProjection(self: RhinoViewport)
            Appends the current view projection and target to the viewport's view stack.
        """
        pass

    def Rotate(self, angleRadians, rotationAxis, rotationCenter):
        """
        Rotate(self: RhinoViewport, angleRadians: float, rotationAxis: Vector3d, rotationCenter: Point3d) -> bool
        
            Rotates about the specified axis. A positive rotation angle results
                    in a 
             counter-clockwise rotation about the axis (right hand rule).
        
        
            angleRadians: angle of rotation in radians.
            rotationAxis: direction of the axis of rotation.
            rotationCenter: point on the axis of rotation.
            Returns: true if geometry successfully rotated.
        """
        pass

    def ScreenToClient(self, screenPoint):
        """ ScreenToClient(self: RhinoViewport, screenPoint: Point) -> Point """
        pass

    def SetCameraDirection(self, cameraDirection, updateTargetLocation):
        """
        SetCameraDirection(self: RhinoViewport, cameraDirection: Vector3d, updateTargetLocation: bool)
            Set viewport camera direction. By default the target location is changed so that
                    
             the vector from the camera location to the target is parallel to the camera direction.
        
        
            cameraDirection: new camera direction.
            updateTargetLocation: if true, the target location is changed so that the vector from the camera
                    location 
             to the target is parallel to the camera direction.
                    If false, the target location is 
             not changed.
                    See the remarks section of RhinoViewport.SetTarget for important 
             details.
        """
        pass

    def SetCameraLocation(self, cameraLocation, updateTargetLocation):
        """
        SetCameraLocation(self: RhinoViewport, cameraLocation: Point3d, updateTargetLocation: bool)
            Set viewport camera location. By default the target location is changed so that
                     
             the vector from the camera location to the target is parallel to the camera direction
                  
                vector.
        
        
            cameraLocation: new camera location.
            updateTargetLocation: if true, the target location is changed so that the vector from the camera
                    location 
             to the target is parallel to the camera direction vector.  
                    If false, the target 
             location is not changed. See the remarks section of
                    RhinoViewport.SetTarget for 
             important details.
        """
        pass

    def SetCameraLocations(self, targetLocation, cameraLocation):
        """
        SetCameraLocations(self: RhinoViewport, targetLocation: Point3d, cameraLocation: Point3d)
            Set viewport camera location and target location. The camera direction vector is
                    
             changed so that it is parallel to the vector from the camera location to
                    the target 
             location.
        
        
            targetLocation: new target location.
            cameraLocation: new camera location.
        """
        pass

    def SetCameraTarget(self, targetLocation, updateCameraLocation):
        """
        SetCameraTarget(self: RhinoViewport, targetLocation: Point3d, updateCameraLocation: bool)
            Set viewport target point. By default the camera location
                    is translated so that the 
             camera direction vector is parallel
                    to the vector from the camera location to the 
             target location.
        
        
            targetLocation: new target location.
            updateCameraLocation: if true, the camera location is translated so that the camera direction
                    vector is 
             parallel to the vector from the camera location to the target
                    location.
                   
              If false, the camera location is not changed.
        """
        pass

    def SetClippingPlanes(self, box):
        """
        SetClippingPlanes(self: RhinoViewport, box: BoundingBox)
            Sets optimal clipping planes to view objects in a world coordinate 3d bounding box.
        
            box: The bounding box
        """
        pass

    def SetConstructionPlane(self, *__args):
        """
        SetConstructionPlane(self: RhinoViewport, cplane: ConstructionPlane)
            Sets the construction plane to cplane.
        
            cplane: The constuction plane to set.
        SetConstructionPlane(self: RhinoViewport, plane: Plane)
        """
        pass

    def SetProjection(self, projection, viewName, updateConstructionPlane):
        """
        SetProjection(self: RhinoViewport, projection: DefinedViewportProjection, viewName: str, updateConstructionPlane: bool) -> bool
        
            Set viewport to a defined projection.
        
            projection: The "standard" projection type.
            viewName: If not null or empty, the name is set.
            updateConstructionPlane: If true, the construction plane is set to the viewport plane.
            Returns: true if successful.
        """
        pass

    def SetToPlanView(self, planeOrigin, planeXaxis, planeYaxis, setConstructionPlane):
        """ SetToPlanView(self: RhinoViewport, planeOrigin: Point3d, planeXaxis: Vector3d, planeYaxis: Vector3d, setConstructionPlane: bool) -> bool """
        pass

    def SetTraceImage(self, bitmapFileName, plane, width, height, grayscale, filtered):
        """
        SetTraceImage(self: RhinoViewport, bitmapFileName: str, plane: Plane, width: float, height: float, grayscale: bool, filtered: bool) -> bool
        
            Set trace image (background bitmap) for this viewport.
        
            bitmapFileName: The bitmap file name.
            plane: A picture plane.
            width: The picture width.
            height: The picture height.
            grayscale: true if the picture should be in grayscale.
            filtered: true if image should be filtered (bilinear) before displayed.
            Returns: true if successful.
        """
        pass

    def SetViewProjection(self, projection, updateTargetLocation):
        """
        SetViewProjection(self: RhinoViewport, projection: ViewportInfo, updateTargetLocation: bool) -> bool
        
            Sets the viewport camera projection.
        
            projection: The "standard" projection type.
            updateTargetLocation: if true, the target location is changed so that the vector from the camera location to the 
             target
                    is parallel to the camera direction vector.  If false, the target location 
             is not changed.
        
            Returns: true on success.
        """
        pass

    def SetWallpaper(self, imageFilename, grayscale, visible=None):
        """
        SetWallpaper(self: RhinoViewport, imageFilename: str, grayscale: bool, visible: bool) -> bool
        SetWallpaper(self: RhinoViewport, imageFilename: str, grayscale: bool) -> bool
        """
        pass

    def WorldToClient(self, worldPoint):
        """
        WorldToClient(self: RhinoViewport, worldPoint: Point3d) -> Point2d
        
            Convert a point from world coordinates in the viewport to a 2d screen
                    point in the 
             local coordinates of the viewport (X/Y of point is relative
                    to top left corner of 
             viewport on screen)
        
        
            worldPoint: The 3D point in world coordinates.
            Returns: The 2D point on the screen.
        """
        pass

    def ZoomBoundingBox(self, box):
        """
        ZoomBoundingBox(self: RhinoViewport, box: BoundingBox) -> bool
        
            Zooms the viewport to the given bounding box.
        
            box: The bouding box to zoom.
            Returns: true if operation succeeded; otherwise false.
        """
        pass

    def ZoomExtents(self):
        """
        ZoomExtents(self: RhinoViewport) -> bool
        
            Dollies the camera location and so that the view frustum contains all of the
                    
             selected document objects that can be seen in view. If the projection is
                    
             perspective, the camera angle is not changed.
        
            Returns: true if successful.
        """
        pass

    def ZoomExtentsSelected(self):
        """
        ZoomExtentsSelected(self: RhinoViewport) -> bool
        
            Dollies the camera location and so that the view frustum contains all of the
                    
             selected document objects that can be seen in view. If the projection is
                    
             perspective, the camera angle is not changed.
        
            Returns: true if successful.
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
    def __new__(self, other=None):
        """
        __new__(cls: type)
        __new__(cls: type, other: RhinoViewport)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size and location of the viewport, in pixels, relative to the parent view.

Get: Bounds(self: RhinoViewport) -> Rectangle

"""

    Camera35mmLensLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Camera35mmLensLength(self: RhinoViewport) -> float

Set: Camera35mmLensLength(self: RhinoViewport) = value
"""

    CameraDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CameraDirection(self: RhinoViewport) -> Vector3d

"""

    CameraLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CameraLocation(self: RhinoViewport) -> Point3d

"""

    CameraTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Viewport target point.

Get: CameraTarget(self: RhinoViewport) -> Point3d

"""

    CameraUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CameraUp(self: RhinoViewport) -> Vector3d

Set: CameraUp(self: RhinoViewport) = value
"""

    CameraX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the "unit to the right" vector.

Get: CameraX(self: RhinoViewport) -> Vector3d

"""

    CameraY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the "unit up" vector.

Get: CameraY(self: RhinoViewport) -> Vector3d

"""

    CameraZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unit vector in CameraDirection.

Get: CameraZ(self: RhinoViewport) -> Vector3d

"""

    ChangeCounter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of change counter is incremented every time the view projection
            or construction plane changes. The user can the mouse and nestable view 
            manipulation commands to change a view at any time. The value of change
            counter can be used to detect these changes in code that is sensitive to
            the view projection.

Get: ChangeCounter(self: RhinoViewport) -> UInt32

"""

    ConstructionAxesVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConstructionAxesVisible(self: RhinoViewport) -> bool

Set: ConstructionAxesVisible(self: RhinoViewport) = value
"""

    ConstructionGridVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConstructionGridVisible(self: RhinoViewport) -> bool

Set: ConstructionGridVisible(self: RhinoViewport) = value
"""

    DisplayMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayMode(self: RhinoViewport) -> DisplayModeDescription

Set: DisplayMode(self: RhinoViewport) = value
"""

    FrustumAspect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width/height ratio of the frustum.

Get: FrustumAspect(self: RhinoViewport) -> float

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unique id for this viewport.

Get: Id(self: RhinoViewport) -> Guid

"""

    IsParallelProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsParallelProjection(self: RhinoViewport) -> bool

"""

    IsPerspectiveProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPerspectiveProjection(self: RhinoViewport) -> bool

"""

    IsPlanView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if construction plane z axis is parallel to camera direction.

Get: IsPlanView(self: RhinoViewport) -> bool

"""

    IsTwoPointPerspectiveProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTwoPointPerspectiveProjection(self: RhinoViewport) -> bool

"""

    IsValidCamera = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidCamera(self: RhinoViewport) -> bool

"""

    IsValidFrustum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidFrustum(self: RhinoViewport) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name associated with this viewport.

Get: Name(self: RhinoViewport) -> str

Set: Name(self: RhinoViewport) = value
"""

    ParentView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent view, if there is one
            
            Every RhinoView has an associated RhinoViewport that does all the 3d display work.
            Those associated viewports return the RhinoView as their parent view. However,
            RhinoViewports are used in other image creating contexts that do not have a parent
            RhinoView.  If you call ParentView, you MUST check for NULL return values.

Get: ParentView(self: RhinoViewport) -> RhinoView

"""

    ScreenPortAspect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """screen port's width/height.

Get: ScreenPortAspect(self: RhinoViewport) -> float

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height and width of the viewport (in pixels)

Get: Size(self: RhinoViewport) -> Size

Set: Size(self: RhinoViewport) = value
"""

    ViewportType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportType(self: RhinoViewport) -> ViewportType

"""

    WallpaperFilename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WallpaperFilename(self: RhinoViewport) -> str

"""

    WallpaperGrayscale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WallpaperGrayscale(self: RhinoViewport) -> bool

"""

    WallpaperVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WallpaperVisible(self: RhinoViewport) -> bool

"""

    WorldAxesVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WorldAxesVisible(self: RhinoViewport) -> bool

Set: WorldAxesVisible(self: RhinoViewport) = value
"""



class Text3d(object, IDisposable):
    """
    3D aligned text with font settings.
    
    Text3d(text: str)
    Text3d(text: str, plane: Plane, height: float)
    """
    def Dispose(self):
        """
        Dispose(self: Text3d)
            Actively reclaims unmanaged resources that this instance uses.
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
    def __new__(self, text, plane=None, height=None):
        """
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, plane: Plane, height: float)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Bold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether this Text3d object will be drawn in Bold.

Get: Bold(self: Text3d) -> bool

Set: Bold(self: Text3d) = value
"""

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the boundingbox for this Text3d object.

Get: BoundingBox(self: Text3d) -> BoundingBox

"""

    FontFace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the FontFace name.

Get: FontFace(self: Text3d) -> str

Set: FontFace(self: Text3d) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height (in units) of this Text3d object. 
            The height should be a positive number larger than zero.

Get: Height(self: Text3d) -> float

Set: Height(self: Text3d) = value
"""

    Italic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether this Text3d object will be drawn in Italics.

Get: Italic(self: Text3d) -> bool

Set: Italic(self: Text3d) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text string for this Text3d object.

Get: Text(self: Text3d) -> str

Set: Text(self: Text3d) = value
"""

    TextPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the 3D aligned plane for this Text3d object.

Get: TextPlane(self: Text3d) -> Plane

Set: TextPlane(self: Text3d) = value
"""



class ViewEventArgs(EventArgs):
    # no doc
    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: View(self: ViewEventArgs) -> RhinoView

"""



class ViewportType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ViewportType, values: DetailViewport (2), PageViewMainViewport (1), StandardModelingViewport (0) """
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

    DetailViewport = None
    PageViewMainViewport = None
    StandardModelingViewport = None
    value__ = None


class VisualAnalysisMode(object):
    """
    Represents a base class for visual analysis modes.
                This class is abstract.
    """
    def DrawBrepObject(self, *args): #cannot find CLR method
        """
        DrawBrepObject(self: VisualAnalysisMode, brep: BrepObject, pipeline: DisplayPipeline)
            Draws one brep. Override this method to add your custom behavior.
                    The default 
             implementation does nothing.
        
        
            brep: A brep object.
            pipeline: The current display pipeline.
        """
        pass

    def DrawCurveObject(self, *args): #cannot find CLR method
        """
        DrawCurveObject(self: VisualAnalysisMode, curve: CurveObject, pipeline: DisplayPipeline)
            If Style==Wireframe, then the default decomposes the curve object into
                    nurbs curve 
             segments and calls the virtual DrawNurbsCurve for each segment.
        
        
            curve: A document curve object.
            pipeline: The drawing pipeline.
        """
        pass

    def DrawMesh(self, *args): #cannot find CLR method
        """
        DrawMesh(self: VisualAnalysisMode, obj: RhinoObject, mesh: Mesh, pipeline: DisplayPipeline)
            Draws a mesh.
                    The default implementation does nothing.
        
            obj: A Rhino object corresponding to the surface.
            mesh: The mesh geometry.
            pipeline: The current display pipeline.
        """
        pass

    def DrawMeshObject(self, *args): #cannot find CLR method
        """
        DrawMeshObject(self: VisualAnalysisMode, mesh: MeshObject, pipeline: DisplayPipeline)
            Draws one mesh. Override this method to add your custom behavior.
                    The default 
             implementation does nothing.
        
        
            mesh: A mesh object.
            pipeline: The current display pipeline.
        """
        pass

    def DrawNurbsCurve(self, *args): #cannot find CLR method
        """
        DrawNurbsCurve(self: VisualAnalysisMode, obj: RhinoObject, curve: NurbsCurve, pipeline: DisplayPipeline)
            Draws a NURBS curve. This is a good function to override for
                    analysis modes like 
             curvature hair display.
                    The default implementation does nothing.
        
        
            obj: A Rhino object corresponding to the curve.
            curve: The curve geometry.
            pipeline: The current display pipeline.
        """
        pass

    def DrawNurbsSurface(self, *args): #cannot find CLR method
        """
        DrawNurbsSurface(self: VisualAnalysisMode, obj: RhinoObject, surface: NurbsSurface, pipeline: DisplayPipeline)
            Draws a NURBS surface. This is a good function to override
                    to display 
             object-related meshes.
                    The default implementation does nothing.
        
        
            obj: A Rhino object corresponding to the surface.
            surface: The surface geometry.
            pipeline: The current display pipeline.
        """
        pass

    def DrawPointCloudObject(self, *args): #cannot find CLR method
        """
        DrawPointCloudObject(self: VisualAnalysisMode, pointCloud: PointCloudObject, pipeline: DisplayPipeline)
            Draws one point cloud. Override this method to add your custom behavior.
                    The 
             default implementation does nothing.
        
        
            pointCloud: A point cloud object.
            pipeline: The current display pipeline.
        """
        pass

    def DrawPointObject(self, *args): #cannot find CLR method
        """
        DrawPointObject(self: VisualAnalysisMode, point: PointObject, pipeline: DisplayPipeline)
            Draws one point. Override this method to add your custom behavior.
                    The default 
             implementation does nothing.
        
        
            point: A point object.
            pipeline: The current display pipeline.
        """
        pass

    def EnableUserInterface(self, on):
        """
        EnableUserInterface(self: VisualAnalysisMode, on: bool)
            Turns the analysis mode's user interface on and off. For Rhino's built
                    in modes 
             this opens or closes the modeless dialog that controls the
                    analysis mode's display 
             settings.
        
        
            on: true if the inferface should be shown; false if it should be concealed.
        """
        pass

    @staticmethod
    def Find(*__args):
        """
        Find(t: Type) -> VisualAnalysisMode
        
            Finds a visual analysis mode by type.
        
            t: A visual analysis mode type.
            Returns: A visual analysis mode on success, or null on error.
        Find(id: Guid) -> VisualAnalysisMode
        
            Finds a visual analysis mode by guid.
        
            id: The globally unique identifier to search for.
            Returns: The found visual analysis mode, or null if it was not found, or on error.
        """
        pass

    def ObjectSupportsAnalysisMode(self, obj):
        """
        ObjectSupportsAnalysisMode(self: VisualAnalysisMode, obj: RhinoObject) -> bool
        
            Gets a value indicating if this visual analysis mode can be used on a given Rhino object.
        
            obj: The object to be tested.
            Returns: true if this mode can indeed be used on the object; otherwise false.
        """
        pass

    @staticmethod
    def Register(customAnalysisModeType):
        """
        Register(customAnalysisModeType: Type) -> VisualAnalysisMode
        
            Registers a custom visual analysis mode for use in Rhino.  It is OK to call
                    
             register multiple times for a single custom analysis mode type, since subsequent
                    
             register calls will notice that the type has already been registered.
        
        
            customAnalysisModeType: Must be a type that is a subclass of VisualAnalysisMode.
            Returns: An instance of registered analysis mode on success.
        """
        pass

    def SetUpDisplayAttributes(self, *args): #cannot find CLR method
        """
        SetUpDisplayAttributes(self: VisualAnalysisMode, obj: RhinoObject, attributes: DisplayPipelineAttributes)
            If an analysis mode needs to modify display attributes, this is the place
                    to do it. 
              In particular, Style==Texture, then this function must be
                    overridden.
        
        
            obj: The object for which to set up attributes.
            attributes: The linked attributes.
        """
        pass

    def UpdateVertexColors(self, *args): #cannot find CLR method
        """
        UpdateVertexColors(self: VisualAnalysisMode, obj: RhinoObject, meshes: Array[Mesh])
            If Style==falseColor, then this virtual function must be overridden.
                    Rhino calls 
             this function when it is time for to set the false colors
                    on the analysis mesh 
             vertices.  For breps, there is one mesh per face.
                    For mesh objects there is a 
             single mesh.
        
        
            obj: The object for which to update vertex colors.
            meshes: An array of meshes that should be updated.
        """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual analysis mode GUID.
            The Guid is specified with the System.Runtime.InteropServices.GuidAttributeGuidAttribute
            applied to the class.

Get: Id(self: VisualAnalysisMode) -> Guid

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the analysis mode. It is used by the _What command and the object
            properties details window to describe the object.

Get: Name(self: VisualAnalysisMode) -> str

"""

    ShowIsoCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets true if this visual analysis mode will show isocuves on shaded surface
            objects.  Often a mode's user interface will provide a way to change this
            setting.
            The default is false.

Get: ShowIsoCurves(self: VisualAnalysisMode) -> bool

"""

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual analysis mode style.

Get: Style(self: VisualAnalysisMode) -> AnalysisStyle

"""


    AnalysisStyle = None
    RhinoCurvatureColorAnalyisModeId = None
    RhinoCurvatureGraphAnalysisModeId = None
    RhinoDraftAngleAnalysisModeId = None
    RhinoEdgeAnalysisModeId = None
    RhinoEmapAnalysisModeId = None
    RhinoThicknessAnalysisModeId = None
    RhinoZebraStripeAnalysisModeId = None


class ZBiasMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum ZBiasMode, values: AwayFromCamera (2), Neutral (0), TowardsCamera (1) """
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

    AwayFromCamera = None
    Neutral = None
    TowardsCamera = None
    value__ = None


class ZBufferCapture(object, IDisposable):
    """
    Provides functionality for getting the zbuffer values from a viewport
                and a given display mode
    
    ZBufferCapture(viewport: RhinoViewport)
    """
    def Dispose(self):
        """
        Dispose(self: ZBufferCapture)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def GrayscaleDib(self):
        """ GrayscaleDib(self: ZBufferCapture) -> Bitmap """
        pass

    def HitCount(self):
        """ HitCount(self: ZBufferCapture) -> int """
        pass

    def MaxZ(self):
        """ MaxZ(self: ZBufferCapture) -> Single """
        pass

    def MinZ(self):
        """ MinZ(self: ZBufferCapture) -> Single """
        pass

    def SetDisplayMode(self, modeId):
        """ SetDisplayMode(self: ZBufferCapture, modeId: Guid) """
        pass

    def ShowAnnotations(self, on):
        """ ShowAnnotations(self: ZBufferCapture, on: bool) """
        pass

    def ShowCurves(self, on):
        """ ShowCurves(self: ZBufferCapture, on: bool) """
        pass

    def ShowIsocurves(self, on):
        """ ShowIsocurves(self: ZBufferCapture, on: bool) """
        pass

    def ShowLights(self, on):
        """ ShowLights(self: ZBufferCapture, on: bool) """
        pass

    def ShowMeshWires(self, on):
        """ ShowMeshWires(self: ZBufferCapture, on: bool) """
        pass

    def ShowPoints(self, on):
        """ ShowPoints(self: ZBufferCapture, on: bool) """
        pass

    def ShowText(self, on):
        """ ShowText(self: ZBufferCapture, on: bool) """
        pass

    def WorldPointAt(self, x, y):
        """ WorldPointAt(self: ZBufferCapture, x: int, y: int) -> Point3d """
        pass

    def ZValueAt(self, x, y):
        """ ZValueAt(self: ZBufferCapture, x: int, y: int) -> Single """
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
    def __new__(self, viewport):
        """ __new__(cls: type, viewport: RhinoViewport) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


