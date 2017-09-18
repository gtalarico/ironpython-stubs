# encoding: utf-8
# module System.Drawing.Text calls itself Text
# from System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class FontCollection(object, IDisposable):
    """ Provides a base class for installed and private font collections. """
    def Dispose(self):
        """
        Dispose(self: FontCollection)
            Releases all resources used by this System.Drawing.Text.FontCollection.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Families = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the array of System.Drawing.FontFamily objects associated with this System.Drawing.Text.FontCollection.

Get: Families(self: FontCollection) -> Array[FontFamily]

"""



class GenericFontFamilies(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies a generic System.Drawing.FontFamily object.
    
    enum GenericFontFamilies, values: Monospace (2), SansSerif (1), Serif (0)
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

    Monospace = None
    SansSerif = None
    Serif = None
    value__ = None


class HotkeyPrefix(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of display for hot-key prefixes that relate to text.
    
    enum HotkeyPrefix, values: Hide (2), None (0), Show (1)
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

    Hide = None
    None = None
    Show = None
    value__ = None


class InstalledFontCollection(FontCollection, IDisposable):
    """
    Represents the fonts installed on the system. This class cannot be inherited.
    
    InstalledFontCollection()
    """
    def Dispose(self):
        """
        Dispose(self: FontCollection, disposing: bool)
            Releases the unmanaged resources used by the System.Drawing.Text.FontCollection and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
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


class PrivateFontCollection(FontCollection, IDisposable):
    """
    Provides a collection of font families built from font files that are provided by the client application.
    
    PrivateFontCollection()
    """
    def AddFontFile(self, filename):
        """
        AddFontFile(self: PrivateFontCollection, filename: str)
            Adds a font from the specified file to this System.Drawing.Text.PrivateFontCollection.
        
            filename: A System.String that contains the file name of the font to add.
        """
        pass

    def AddMemoryFont(self, memory, length):
        """
        AddMemoryFont(self: PrivateFontCollection, memory: IntPtr, length: int)
            Adds a font contained in system memory to this System.Drawing.Text.PrivateFontCollection.
        
            memory: The memory address of the font to add.
            length: The memory length of the font to add.
        """
        pass

    def Dispose(self):
        """ Dispose(self: PrivateFontCollection, disposing: bool) """
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


class TextRenderingHint(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the quality of text rendering.
    
    enum TextRenderingHint, values: AntiAlias (4), AntiAliasGridFit (3), ClearTypeGridFit (5), SingleBitPerPixel (2), SingleBitPerPixelGridFit (1), SystemDefault (0)
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

    AntiAlias = None
    AntiAliasGridFit = None
    ClearTypeGridFit = None
    SingleBitPerPixel = None
    SingleBitPerPixelGridFit = None
    SystemDefault = None
    value__ = None


