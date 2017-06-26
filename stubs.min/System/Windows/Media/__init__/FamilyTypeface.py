class FamilyTypeface(object, IDeviceFont, ITypefaceMetrics):
    """
    Specifies the details of a single typeface supported by a System.Windows.Media.FontFamily.
    
    FamilyTypeface()
    """
    def Equals(self, *__args):
        """
        Equals(self: FamilyTypeface, o: object) -> bool
        
            Compares two font family typefaces for equality.
        
            o: The System.Object value that represents the typeface to compare.
            Returns: true if typeface is not null and has the same properties as this typeface; otherwise, false.
        Equals(self: FamilyTypeface, typeface: FamilyTypeface) -> bool
        
            Compares two font family typefaces for equality.
        
            typeface: The System.Windows.Media.FamilyTypeface value to compare.
            Returns: true if typeface is not null and has the same properties as this font family typeface; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: FamilyTypeface) -> int
        
            Serves as a hash function for a System.Windows.Media.FamilyTypeface object. The System.Windows.Media.FamilyTypeface.GetHashCode method is suitable for use in hashing algorithms and data structures like a 
             hash table.
        
            Returns: A value of type System.Int32.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AdjustedFaceNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of localized face names adjusted by the font differentiator.

Get: AdjustedFaceNames(self: FamilyTypeface) -> IDictionary[XmlLanguage, str]

"""

    CapsHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the distance from baseline to top of an English capital, relative to em size.

Get: CapsHeight(self: FamilyTypeface) -> float

Set: CapsHeight(self: FamilyTypeface) = value
"""

    DeviceFontCharacterMetrics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of character metrics for a device font family typeface.

Get: DeviceFontCharacterMetrics(self: FamilyTypeface) -> CharacterMetricsDictionary

"""

    DeviceFontName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name or unique identifier for a device font family typeface.

Get: DeviceFontName(self: FamilyTypeface) -> str

Set: DeviceFontName(self: FamilyTypeface) = value
"""

    Stretch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the designed stretch of the font family typeface.

Get: Stretch(self: FamilyTypeface) -> FontStretch

Set: Stretch(self: FamilyTypeface) = value
"""

    StrikethroughPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the position of the strikethrough value relative to the baseline. The value is also relative to em size.

Get: StrikethroughPosition(self: FamilyTypeface) -> float

Set: StrikethroughPosition(self: FamilyTypeface) = value
"""

    StrikethroughThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the thickness of the strikethrough relative to em size.

Get: StrikethroughThickness(self: FamilyTypeface) -> float

Set: StrikethroughThickness(self: FamilyTypeface) = value
"""

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the style of the font family typeface design.

Get: Style(self: FamilyTypeface) -> FontStyle

Set: Style(self: FamilyTypeface) = value
"""

    UnderlinePosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the position of underline value relative to the baseline. The value is also relative to em size.

Get: UnderlinePosition(self: FamilyTypeface) -> float

Set: UnderlinePosition(self: FamilyTypeface) = value
"""

    UnderlineThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the thickness of underline relative to em size.

Get: UnderlineThickness(self: FamilyTypeface) -> float

Set: UnderlineThickness(self: FamilyTypeface) = value
"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the designed weight of this font family typeface.

Get: Weight(self: FamilyTypeface) -> FontWeight

Set: Weight(self: FamilyTypeface) = value
"""

    XHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Western x-height relative to em size.

Get: XHeight(self: FamilyTypeface) -> float

Set: XHeight(self: FamilyTypeface) = value
"""


