class Size(object, IFormattable):
    """
    Implements a structure that is used to describe the System.Windows.Size of an object.
    
    Size(width: float, height: float)
    """
    @staticmethod
    def Equals(*__args):
        """
        Equals(self: Size, value: Size) -> bool
        
            Compares a value to an instance of System.Windows.Size for equality.
        
            value: The size to compare to this current instance of System.Windows.Size.
            Returns: true if the instances of System.Windows.Size are equal; otherwise, false.
        Equals(self: Size, o: object) -> bool
        
            Compares an object to an instance of System.Windows.Size for equality.
        
            o: The System.Object to compare.
            Returns: true if the sizes are equal; otherwise, false.
        Equals(size1: Size, size2: Size) -> bool
        
            Compares two instances of System.Windows.Size for equality.
        
            size1: The first instance of System.Windows.Size to compare.
            size2: The second instance of System.Windows.Size to compare.
            Returns: true if the instances of System.Windows.Size are equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Size) -> int
        
            Gets the hash code for this instance of System.Windows.Size.
            Returns: The hash code for this instance of System.Windows.Size.
        """
        pass

    @staticmethod
    def Parse(source):
        """
        Parse(source: str) -> Size
        
            Returns an instance of System.Windows.Size from a converted System.String.
        
            source: A System.String value to parse to a System.Windows.Size value.
            Returns: An instance of System.Windows.Size.
        """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: Size, provider: IFormatProvider) -> str
        
            Returns a System.String that represents this instance of System.Windows.Size.
        
            provider: An object that provides a way to control formatting.
            Returns: A System.String that represents this System.Windows.Size object.
        ToString(self: Size) -> str
        
            Returns a System.String that represents this System.Windows.Size object.
            Returns: A System.String that specifies the width followed by the height.
        """
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

    @staticmethod # known case of __new__
    def __new__(self, width, height):
        """
        __new__(cls: type, width: float, height: float)
        __new__[Size]() -> Size
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

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Size.Height of this instance of System.Windows.Size.

Get: Height(self: Size) -> float

Set: Height(self: Size) = value
"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this instance of System.Windows.Size is System.Windows.Size.Empty.

Get: IsEmpty(self: Size) -> bool

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Size.Width of this instance of System.Windows.Size.

Get: Width(self: Size) -> float

Set: Width(self: Size) = value
"""


    Empty = None

