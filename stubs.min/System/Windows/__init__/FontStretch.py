class FontStretch(object, IFormattable):
    """ Describes the degree to which a font has been stretched compared to the normal aspect ratio of that font. """
    @staticmethod
    def Compare(left, right):
        """
        Compare(left: FontStretch, right: FontStretch) -> int
        
            Compares two instances of System.Windows.FontStretch objects.
        
            left: The first System.Windows.FontStretch object to compare.
            right: The second System.Windows.FontStretch object to compare.
            Returns: An System.Int32 value that represents the relationship between the two instances of System.Windows.FontStretch.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: FontStretch, obj: FontStretch) -> bool
        
            Compares a System.Windows.FontStretch object with the current System.Windows.FontStretch object.
        
            obj: The instance of the System.Windows.FontStretch object to compare for equality.
            Returns: true if two instances are equal; otherwise, false.
        Equals(self: FontStretch, obj: object) -> bool
        
            Compares a System.Object with the current System.Windows.FontStretch object.
        
            obj: The instance of the System.Object to compare for equality.
            Returns: true if two instances are equal; otherwise, false.
        """
        pass

    @staticmethod
    def FromOpenTypeStretch(stretchValue):
        """
        FromOpenTypeStretch(stretchValue: int) -> FontStretch
        
            Creates a new instance of System.Windows.FontStretch that corresponds to the OpenType usStretchClass value.
        
            stretchValue: An integer value between one and nine that corresponds to the usStretchValue definition in the OpenType specification.
            Returns: A new instance of System.Windows.FontStretch.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: FontStretch) -> int
        
            Retrieves the hash code for this object.
            Returns: An System.Int32 value representing the hash code for the object.
        """
        pass

    def ToOpenTypeStretch(self):
        """
        ToOpenTypeStretch(self: FontStretch) -> int
        
            Returns a value that represents the OpenType�usStretchClass for this System.Windows.FontStretch object.
            Returns: An integer value between 1 and 999 that corresponds to the usStretchClass definition in the OpenType specification.
        """
        pass

    def ToString(self):
        """
        ToString(self: FontStretch) -> str
        
            Creates a System.String representation of the current System.Windows.FontStretch object based on the current culture.
            Returns: A System.String value representation of the object.
        """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

