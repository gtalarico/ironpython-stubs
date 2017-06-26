# encoding: utf-8
# module Rhino.Display calls itself Display
# from Rhino3dmIO, Version=5.1.30000.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BackgroundStyle(Enum, IComparable, IFormattable, IConvertible):
    """ enum BackgroundStyle, values: Environment (3), Gradient (2), SolidColor (0), WallpaperImage (1) """
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


class Color4f(object, ISerializable):
    """
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
    ColorCMYK(rgb: Color)
    ColorCMYK(cyan: float, magenta: float, yellow: float)
    ColorCMYK(cyan: float, magenta: float, yellow: float, key: float)
    ColorCMYK(alpha: float, cyan: float, magenta: float, yellow: float, key: float)
    """
    @staticmethod
    def CreateFromHSL(hsl):
        """ CreateFromHSL(hsl: ColorHSL) -> ColorCMYK """
        pass

    @staticmethod
    def CreateFromLAB(lab):
        """ CreateFromLAB(lab: ColorLAB) -> ColorCMYK """
        pass

    @staticmethod
    def CreateFromLCH(lch):
        """ CreateFromLCH(lch: ColorLCH) -> ColorCMYK """
        pass

    @staticmethod
    def CreateFromXYZ(xyz):
        """ CreateFromXYZ(xyz: ColorXYZ) -> ColorCMYK """
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
    """Get: A(self: ColorCMYK) -> float

Set: A(self: ColorCMYK) = value
"""

    C = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: C(self: ColorCMYK) -> float

Set: C(self: ColorCMYK) = value
"""

    K = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: K(self: ColorCMYK) -> float

Set: K(self: ColorCMYK) = value
"""

    M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M(self: ColorCMYK) -> float

Set: M(self: ColorCMYK) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: ColorCMYK) -> float

Set: Y(self: ColorCMYK) = value
"""



class ColorHSL(object):
    """
    ColorHSL(rgb: Color)
    ColorHSL(hue: float, saturation: float, luminance: float)
    ColorHSL(alpha: float, hue: float, saturation: float, luminance: float)
    """
    @staticmethod
    def CreateFromCMYK(cmyk):
        """ CreateFromCMYK(cmyk: ColorCMYK) -> ColorHSL """
        pass

    @staticmethod
    def CreateFromLAB(lab):
        """ CreateFromLAB(lab: ColorLAB) -> ColorHSL """
        pass

    @staticmethod
    def CreateFromLCH(lch):
        """ CreateFromLCH(lch: ColorLCH) -> ColorHSL """
        pass

    @staticmethod
    def CreateFromXYZ(xyz):
        """ CreateFromXYZ(xyz: ColorXYZ) -> ColorHSL """
        pass

    def ToArgbColor(self):
        """ ToArgbColor(self: ColorHSL) -> Color """
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
    """Get: A(self: ColorHSL) -> float

Set: A(self: ColorHSL) = value
"""

    H = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: H(self: ColorHSL) -> float

Set: H(self: ColorHSL) = value
"""

    L = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: L(self: ColorHSL) -> float

Set: L(self: ColorHSL) = value
"""

    S = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: S(self: ColorHSL) -> float

Set: S(self: ColorHSL) = value
"""



class ColorLAB(object):
    """
    ColorLAB(rgb: Color)
    ColorLAB(lightness: float, a: float, b: float)
    ColorLAB(alpha: float, lightness: float, a: float, b: float)
    """
    @staticmethod
    def CreateFromCMYK(cmyk):
        """ CreateFromCMYK(cmyk: ColorCMYK) -> ColorLAB """
        pass

    @staticmethod
    def CreateFromHSL(hsl):
        """ CreateFromHSL(hsl: ColorHSL) -> ColorLAB """
        pass

    @staticmethod
    def CreateFromLCH(lch):
        """ CreateFromLCH(lch: ColorLCH) -> ColorLAB """
        pass

    @staticmethod
    def CreateFromXYZ(xyz):
        """ CreateFromXYZ(xyz: ColorXYZ) -> ColorLAB """
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
    """Get: A(self: ColorLAB) -> float

Set: A(self: ColorLAB) = value
"""

    Alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Alpha(self: ColorLAB) -> float

Set: Alpha(self: ColorLAB) = value
"""

    B = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: B(self: ColorLAB) -> float

Set: B(self: ColorLAB) = value
"""

    L = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: L(self: ColorLAB) -> float

Set: L(self: ColorLAB) = value
"""



class ColorLCH(object):
    """
    ColorLCH(rgb: Color)
    ColorLCH(lightness: float, chroma: float, hue: float)
    ColorLCH(alpha: float, lightness: float, chroma: float, hue: float)
    """
    @staticmethod
    def CreateFromCMYK(cmyk):
        """ CreateFromCMYK(cmyk: ColorCMYK) -> ColorLCH """
        pass

    @staticmethod
    def CreateFromHSL(hsl):
        """ CreateFromHSL(hsl: ColorHSL) -> ColorLCH """
        pass

    @staticmethod
    def CreateFromLAB(lab):
        """ CreateFromLAB(lab: ColorLAB) -> ColorLCH """
        pass

    @staticmethod
    def CreateFromXYZ(xyz):
        """ CreateFromXYZ(xyz: ColorXYZ) -> ColorLCH """
        pass

    def MakePositive(self):
        """ MakePositive(self: ColorLCH) """
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
    """Get: A(self: ColorLCH) -> float

Set: A(self: ColorLCH) = value
"""

    C = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: C(self: ColorLCH) -> float

Set: C(self: ColorLCH) = value
"""

    H = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: H(self: ColorLCH) -> float

Set: H(self: ColorLCH) = value
"""

    L = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: L(self: ColorLCH) -> float

Set: L(self: ColorLCH) = value
"""



class ColorXYZ(object):
    """
    ColorXYZ(rgb: Color)
    ColorXYZ(x: float, y: float, z: float)
    ColorXYZ(alpha: float, x: float, y: float, z: float)
    """
    @staticmethod
    def CreateFromCMYK(cmyk):
        """ CreateFromCMYK(cmyk: ColorCMYK) -> ColorXYZ """
        pass

    @staticmethod
    def CreateFromHSL(hsl):
        """ CreateFromHSL(hsl: ColorHSL) -> ColorXYZ """
        pass

    @staticmethod
    def CreateFromLAB(lab):
        """ CreateFromLAB(lab: ColorLAB) -> ColorXYZ """
        pass

    @staticmethod
    def CreateFromLCH(lch):
        """ CreateFromLCH(lch: ColorLCH) -> ColorXYZ """
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
    """Get: A(self: ColorXYZ) -> float

Set: A(self: ColorXYZ) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: ColorXYZ) -> float

Set: X(self: ColorXYZ) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: ColorXYZ) -> float

Set: Y(self: ColorXYZ) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: ColorXYZ) -> float

Set: Z(self: ColorXYZ) = value
"""



class DefinedViewportProjection(Enum, IComparable, IFormattable, IConvertible):
    """ enum DefinedViewportProjection, values: Back (6), Bottom (2), Front (5), Left (3), None (0), Perspective (7), Right (4), Top (1), TwoPointPerspective (8) """
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


