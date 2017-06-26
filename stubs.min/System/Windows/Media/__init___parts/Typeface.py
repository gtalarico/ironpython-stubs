class Typeface(object):
    """
    Represents a combination of System.Windows.Media.FontFamily, System.Windows.FontWeight, System.Windows.FontStyle, and System.Windows.FontStretch.
    
    Typeface(typefaceName: str)
    Typeface(fontFamily: FontFamily, style: FontStyle, weight: FontWeight, stretch: FontStretch)
    Typeface(fontFamily: FontFamily, style: FontStyle, weight: FontWeight, stretch: FontStretch, fallbackFontFamily: FontFamily)
    """
    def Equals(self, o):
        """
        Equals(self: Typeface, o: object) -> bool
        
            Gets a value that indicates whether the current typeface and the specified typeface have the same System.Windows.Media.Typeface.FontFamily, System.Windows.Media.Typeface.Style, 
             System.Windows.Media.Typeface.Weight, System.Windows.Media.Typeface.Stretch, and fallback font values.
        
        
            o: The System.Windows.Media.Typeface to compare.
            Returns: true if o is equal to the current System.Windows.Media.Typeface object; otherwise, false. If o is not a System.Windows.Media.Typeface object, false is returned.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Typeface) -> int
        
            Serves as a hash function for System.Windows.Media.Typeface. It is suitable for use in hashing algorithms and data structures such as a hash table.
            Returns: An System.Int32 value that represents the hash code for the current object.
        """
        pass

    def TryGetGlyphTypeface(self, glyphTypeface):
        """
        TryGetGlyphTypeface(self: Typeface) -> (bool, GlyphTypeface)
        
            Retrieves the System.Windows.Media.GlyphTypeface that corresponds to the System.Windows.Media.Typeface.
            Returns: true if the out parameter is set to a System.Windows.Media.GlyphTypeface value; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, typefaceName: str)
        __new__(cls: type, fontFamily: FontFamily, style: FontStyle, weight: FontWeight, stretch: FontStretch)
        __new__(cls: type, fontFamily: FontFamily, style: FontStyle, weight: FontWeight, stretch: FontStretch, fallbackFontFamily: FontFamily)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    CapsHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the distance from the baseline to the top of an English capital letter for the typeface.

Get: CapsHeight(self: Typeface) -> float

"""

    FaceNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of culture-specific names for the System.Windows.Media.Typeface.

Get: FaceNames(self: Typeface) -> LanguageSpecificStringDictionary

"""

    FontFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the font family from which the typeface was constructed.

Get: FontFamily(self: Typeface) -> FontFamily

"""

    IsBoldSimulated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether to simulate a bold weight for the glyphs represented by the System.Windows.Media.Typeface.

Get: IsBoldSimulated(self: Typeface) -> bool

"""

    IsObliqueSimulated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether to simulate an italic style for the glyphs represented by the System.Windows.Media.Typeface.

Get: IsObliqueSimulated(self: Typeface) -> bool

"""

    Stretch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stretch value for the System.Windows.Media.Typeface. The stretch value determines whether a typeface is expanded or condensed when it is displayed.

Get: Stretch(self: Typeface) -> FontStretch

"""

    StrikethroughPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the distance from the baseline to the strikethrough for the typeface.

Get: StrikethroughPosition(self: Typeface) -> float

"""

    StrikethroughThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the thickness of the strikethrough relative to the font em size.

Get: StrikethroughThickness(self: Typeface) -> float

"""

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the style of the System.Windows.Media.Typeface.

Get: Style(self: Typeface) -> FontStyle

"""

    UnderlinePosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the distance of the underline from the baseline for the typeface.

Get: UnderlinePosition(self: Typeface) -> float

"""

    UnderlineThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the thickness of the underline relative to the font em size for the typeface.

Get: UnderlineThickness(self: Typeface) -> float

"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the relative weight of the typeface.

Get: Weight(self: Typeface) -> FontWeight

"""

    XHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the distance from the baseline to the top of an English lowercase letter for a typeface. The distance excludes ascenders.

Get: XHeight(self: Typeface) -> float

"""


