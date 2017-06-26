class FontFamily(object):
    """
    Represents a family of related fonts.
    
    FontFamily(familyName: str)
    FontFamily(baseUri: Uri, familyName: str)
    FontFamily()
    """
    def Equals(self, o):
        """
        Equals(self: FontFamily, o: object) -> bool
        
            Gets a value that indicates whether the current font family object and the specified font family object are the same.
        
            o: The System.Windows.Media.FontFamily object to compare.
            Returns: true if o is equal to the current System.Windows.Media.FontFamily object; otherwise, false. If o is not a System.Windows.Media.FontFamily object, false is returned.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: FontFamily) -> int
        
            Serves as a hash function for System.Windows.Media.FontFamily. It is suitable for use in hashing algorithms and data structures such as a hash table.
            Returns: An System.Int32 value that represents the hash code for the current object.
        """
        pass

    def GetTypefaces(self):
        """
        GetTypefaces(self: FontFamily) -> ICollection[Typeface]
        
            Returns a collection of System.Windows.Media.Typeface objects that represent the type faces in the default system font location.
            Returns: An System.Collections.Generic.ICollection of System.Windows.Media.Typeface objects.
        """
        pass

    def ToString(self):
        """
        ToString(self: FontFamily) -> str
        
            Returns the value of the System.Windows.Media.FontFamily.Source property.
            Returns: The source location of the System.Windows.Media.FontFamily object, including the directory or uniform resource identifier (URI) location reference.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, familyName: str)
        __new__(cls: type, baseUri: Uri, familyName: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Baseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the distance between the baseline and the character cell top.

Get: Baseline(self: FontFamily) -> float

Set: Baseline(self: FontFamily) = value
"""

    BaseUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the base uniform resource identifier (URI) that is used to resolve a font family name.

Get: BaseUri(self: FontFamily) -> Uri

"""

    FamilyMaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of System.Windows.Media.FontFamilyMap objects.

Get: FamilyMaps(self: FontFamily) -> FontFamilyMapCollection

"""

    FamilyNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of strings and System.Globalization.CultureInfo values that represent the font family names of the System.Windows.Media.FontFamily object.

Get: FamilyNames(self: FontFamily) -> LanguageSpecificStringDictionary

"""

    FamilyTypefaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of typefaces for the System.Windows.Media.FontFamily object.

Get: FamilyTypefaces(self: FontFamily) -> FamilyTypefaceCollection

"""

    LineSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the line spacing value for the System.Windows.Media.FontFamily object. The line spacing is the recommended baseline-to-baseline distance for the text in this font relative to the em size.

Get: LineSpacing(self: FontFamily) -> float

Set: LineSpacing(self: FontFamily) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the font family name that is used to construct the System.Windows.Media.FontFamily object.

Get: Source(self: FontFamily) -> str

"""


