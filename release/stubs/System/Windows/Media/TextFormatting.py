# encoding: utf-8
# module System.Windows.Media.TextFormatting calls itself TextFormatting
# from PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class CharacterBufferRange(object, IEquatable[CharacterBufferRange]):
    """
    Describes a string of characters.
    
    CharacterBufferRange(characterArray: Array[Char], offsetToFirstChar: int, characterLength: int)
    CharacterBufferRange(characterString: str, offsetToFirstChar: int, characterLength: int)
    CharacterBufferRange(unsafeCharacterString: Char*, characterLength: int)
    """
    def Equals(self, *__args):
        """
        Equals(self: CharacterBufferRange, value: CharacterBufferRange) -> bool
        
            Determines whether the System.Windows.Media.TextFormatting.CharacterBufferRange object is equal 
             to the current System.Windows.Media.TextFormatting.CharacterBufferRange object.
        
        
            value: The System.Windows.Media.TextFormatting.CharacterBufferRange to compare with the current 
             System.Windows.Media.TextFormatting.CharacterBufferRange object.
        
            Returns: true if value is equal to the current System.Windows.Media.TextFormatting.CharacterBufferRange 
             object; otherwise, false. If value is not a 
             System.Windows.Media.TextFormatting.CharacterBufferRange object, false is returned.
        
        Equals(self: CharacterBufferRange, obj: object) -> bool
        
            Determines whether the specified object is equal to the current 
             System.Windows.Media.TextFormatting.CharacterBufferRange object.
        
        
            obj: The System.Object to compare with the current 
             System.Windows.Media.TextFormatting.CharacterBufferRange object.
        
            Returns: true if o is equal to the current System.Windows.Media.TextFormatting.CharacterBufferRange 
             object; otherwise, false. If o is not a System.Windows.Media.TextFormatting.CharacterBufferRange 
             object, false is returned.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: CharacterBufferRange) -> int
        
            Serves as a hash function for System.Windows.Media.TextFormatting.CharacterBufferRange. It is 
             suitable for use in hashing algorithms and data structures such as a hash table.
        
            Returns: An System.Int32 value that represents the hash code for the current object.
        """
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
        __new__(cls: type, characterArray: Array[Char], offsetToFirstChar: int, characterLength: int)
        __new__(cls: type, characterString: str, offsetToFirstChar: int, characterLength: int)
        __new__(cls: type, unsafeCharacterString: Char*, characterLength: int)
        __new__[CharacterBufferRange]() -> CharacterBufferRange
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CharacterBufferReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a reference to the character buffer of a string.

Get: CharacterBufferReference(self: CharacterBufferRange) -> CharacterBufferReference

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of characters in the text source character store.

Get: Length(self: CharacterBufferRange) -> int

"""


    Empty = None


class CharacterBufferReference(object, IEquatable[CharacterBufferReference]):
    """
    Describes a character buffer for a text run.
    
    CharacterBufferReference(characterString: str, offsetToFirstChar: int)
    CharacterBufferReference(characterArray: Array[Char], offsetToFirstChar: int)
    CharacterBufferReference(unsafeCharacterString: Char*, characterLength: int)
    """
    def Equals(self, *__args):
        """
        Equals(self: CharacterBufferReference, value: CharacterBufferReference) -> bool
        
            Determines whether the System.Windows.Media.TextFormatting.CharacterBufferReference is equal to 
             the current System.Windows.Media.TextFormatting.CharacterBufferReference object.
        
        
            value: The System.Windows.Media.TextFormatting.CharacterBufferReference to compare with the current 
             System.Windows.Media.TextFormatting.CharacterBufferReference object.
        
            Returns: true if value is equal to the current 
             System.Windows.Media.TextFormatting.CharacterBufferReference object; otherwise, false.
        
        Equals(self: CharacterBufferReference, obj: object) -> bool
        
            Determines whether the specified object is equal to the current 
             System.Windows.Media.TextFormatting.CharacterBufferReference object.
        
        
            obj: The object to compare with the current 
             System.Windows.Media.TextFormatting.CharacterBufferReference object.
        
            Returns: true if obj is equal to the current System.Windows.Media.TextFormatting.CharacterBufferReference 
             object; otherwise, false. If obj is not a 
             System.Windows.Media.TextFormatting.CharacterBufferReference object, false is returned.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: CharacterBufferReference) -> int
        
            Serves as a hash function for System.Windows.Media.TextFormatting.CharacterBufferReference. It 
             is suitable for use in hashing algorithms and data structures such as a hash table.
        
            Returns: An System.Int32 value that represents the hash code for the current object.
        """
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
        __new__(cls: type, characterArray: Array[Char], offsetToFirstChar: int)
        __new__(cls: type, characterString: str, offsetToFirstChar: int)
        __new__(cls: type, unsafeCharacterString: Char*, characterLength: int)
        __new__[CharacterBufferReference]() -> CharacterBufferReference
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class CharacterHit(object, IEquatable[CharacterHit]):
    """
    Represents information about a character hit within a glyph run.
    
    CharacterHit(firstCharacterIndex: int, trailingLength: int)
    """
    def Equals(self, obj):
        """
        Equals(self: CharacterHit, obj: object) -> bool
        
            Determines whether the specified object is equal to the current 
             System.Windows.Media.TextFormatting.CharacterBufferReference object.
        
        
            obj: The object to compare with the current 
             System.Windows.Media.TextFormatting.CharacterBufferReference object.
        
            Returns: true if obj is equal to the current System.Windows.Media.TextFormatting.CharacterBufferReference 
             object; otherwise, false. If obj is not a 
             System.Windows.Media.TextFormatting.CharacterBufferReference object, false is returned.
        
        Equals(self: CharacterHit, obj: CharacterHit) -> bool
        
            Determines whether the System.Windows.Media.TextFormatting.CharacterBufferReference is equal to 
             the current System.Windows.Media.TextFormatting.CharacterBufferReference object.
        
        
            obj: The System.Windows.Media.TextFormatting.CharacterBufferReference to compare with the current 
             System.Windows.Media.TextFormatting.CharacterBufferReference object.
        
            Returns: true if obj is equal to the current System.Windows.Media.TextFormatting.CharacterBufferReference 
             object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: CharacterHit) -> int
        
            Serves as a hash function for System.Windows.Media.TextFormatting.CharacterBufferReference. It 
             is suitable for use in hashing algorithms and data structures such as a hash table.
        
            Returns: An System.Int32 value that represents the hash code for the current object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, firstCharacterIndex, trailingLength):
        """
        __new__(cls: type, firstCharacterIndex: int, trailingLength: int)
        __new__[CharacterHit]() -> CharacterHit
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FirstCharacterIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of the first character that got hit.

Get: FirstCharacterIndex(self: CharacterHit) -> int

"""

    TrailingLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the trailing length value for the character that got hit.

Get: TrailingLength(self: CharacterHit) -> int

"""



class CultureSpecificCharacterBufferRange(object):
    """
    Represents a range of characters that are associated with a culture.
    
    CultureSpecificCharacterBufferRange(culture: CultureInfo, characterBufferRange: CharacterBufferRange)
    """
    @staticmethod # known case of __new__
    def __new__(self, culture, characterBufferRange):
        """ __new__(cls: type, culture: CultureInfo, characterBufferRange: CharacterBufferRange) """
        pass

    CharacterBufferRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Media.TextFormatting.CharacterBufferRange of the System.Windows.Media.TextFormatting.CultureSpecificCharacterBufferRange.

Get: CharacterBufferRange(self: CultureSpecificCharacterBufferRange) -> CharacterBufferRange

"""

    CultureInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Globalization.CultureInfo of the System.Windows.Media.TextFormatting.CultureSpecificCharacterBufferRange.

Get: CultureInfo(self: CultureSpecificCharacterBufferRange) -> CultureInfo

"""



class IndexedGlyphRun(object):
    """ Allows text engine clients to map a text source character index to the corresponding System.Windows.Media.GlyphRun. """
    GlyphRun = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Media.GlyphRun that corresponds to the System.Windows.Media.TextFormatting.IndexedGlyphRun object.

Get: GlyphRun(self: IndexedGlyphRun) -> GlyphRun

"""

    TextSourceCharacterIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text source character index that corresponds to the beginning of the System.Windows.Media.GlyphRun.

Get: TextSourceCharacterIndex(self: IndexedGlyphRun) -> int

"""

    TextSourceLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text source character length that corresponds to the System.Windows.Media.TextFormatting.IndexedGlyphRun object.

Get: TextSourceLength(self: IndexedGlyphRun) -> int

"""



class InvertAxes(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicate the inversion of horizontal and vertical axes of the drawing surface.
    
    enum (flags) InvertAxes, values: Both (3), Horizontal (1), None (0), Vertical (2)
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

    Both = None
    Horizontal = None
    None = None
    value__ = None
    Vertical = None


class MinMaxParagraphWidth(object, IEquatable[MinMaxParagraphWidth]):
    """ Represents the smallest and largest possible paragraph width that can fully contain the specified text content. """
    def Equals(self, *__args):
        """
        Equals(self: MinMaxParagraphWidth, obj: object) -> bool
        
            Determines whether the specified object is equal to the current 
             System.Windows.Media.TextFormatting.CharacterBufferReference object.
        
        
            obj: The System.Object to compare with the current 
             System.Windows.Media.TextFormatting.CharacterBufferReference object.
        
            Returns: true if obj is equal to the current System.Windows.Media.TextFormatting.CharacterBufferReference 
             object; otherwise, false. If obj is not a 
             System.Windows.Media.TextFormatting.CharacterBufferReference object, false is returned.
        
        Equals(self: MinMaxParagraphWidth, value: MinMaxParagraphWidth) -> bool
        
            Determines whether the System.Windows.Media.TextFormatting.CharacterBufferReference is equal to 
             the current System.Windows.Media.TextFormatting.CharacterBufferReference object.
        
        
            value: The System.Windows.Media.TextFormatting.CharacterBufferReference to compare with the current 
             System.Windows.Media.TextFormatting.CharacterBufferReference object.
        
            Returns: true if value is equal to the current 
             System.Windows.Media.TextFormatting.CharacterBufferReference object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: MinMaxParagraphWidth) -> int
        
            Serves as a hash function for System.Windows.Media.TextFormatting.CharacterBufferReference. It 
             is suitable for use in hashing algorithms and data structures such as a hash table.
        
            Returns: An System.Int32 value that represents the hash code for the current object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    MaxWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the largest paragraph width possible that can fully contain the specified text content.

Get: MaxWidth(self: MinMaxParagraphWidth) -> float

"""

    MinWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the smallest paragraph width possible that can fully contain the specified text content.

Get: MinWidth(self: MinMaxParagraphWidth) -> float

"""



class TextBounds(object):
    """ Represents the bounding rectangle of a range of characters. """
    FlowDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text flow direction for the System.Windows.Media.TextFormatting.TextBounds object.

Get: FlowDirection(self: TextBounds) -> FlowDirection

"""

    Rectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the bounding rectangle for the System.Windows.Media.TextFormatting.TextBounds object.

Get: Rectangle(self: TextBounds) -> Rect

"""

    TextRunBounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a list of System.Windows.Media.TextFormatting.TextRunBounds objects.

Get: TextRunBounds(self: TextBounds) -> IList[TextRunBounds]

"""



class TextRun(object):
    """ Represents a sequence of characters that share a single property set. """
    CharacterBufferReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a reference to the text run character buffer.

Get: CharacterBufferReference(self: TextRun) -> CharacterBufferReference

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of characters in the text run.

Get: Length(self: TextRun) -> int

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the set of text properties that are shared by every character in the text run, such as typeface or foreground brush.

Get: Properties(self: TextRun) -> TextRunProperties

"""



class TextCharacters(TextRun, ITextSymbols, IShapeableTextCollector):
    """
    Represents a collection of character glyphs from distinct physical typefaces.
    
    TextCharacters(characterArray: Array[Char], offsetToFirstChar: int, length: int, textRunProperties: TextRunProperties)
    TextCharacters(characterString: str, textRunProperties: TextRunProperties)
    TextCharacters(characterString: str, offsetToFirstChar: int, length: int, textRunProperties: TextRunProperties)
    TextCharacters(unsafeCharacterString: Char*, length: int, textRunProperties: TextRunProperties)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, characterArray: Array[Char], offsetToFirstChar: int, length: int, textRunProperties: TextRunProperties)
        __new__(cls: type, characterString: str, textRunProperties: TextRunProperties)
        __new__(cls: type, characterString: str, offsetToFirstChar: int, length: int, textRunProperties: TextRunProperties)
        __new__(cls: type, unsafeCharacterString: Char*, length: int, textRunProperties: TextRunProperties)
        """
        pass

    CharacterBufferReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Media.TextFormatting.CharacterBufferReference for the System.Windows.Media.TextFormatting.TextCharacters.

Get: CharacterBufferReference(self: TextCharacters) -> CharacterBufferReference

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the text characters.

Get: Length(self: TextCharacters) -> int

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the set of properties shared by every text character.

Get: Properties(self: TextCharacters) -> TextRunProperties

"""



class TextCollapsedRange(object):
    """ Represents the range of characters and its width measurement for collapsed text within a line. """
    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of characters for the collapsed text.

Get: Length(self: TextCollapsedRange) -> int

"""

    TextSourceCharacterIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index to the first character in the System.Windows.Media.TextFormatting.TextSource that represents collapsed text characters.

Get: TextSourceCharacterIndex(self: TextCollapsedRange) -> int

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total width of collapsed text characters.

Get: Width(self: TextCollapsedRange) -> float

"""



class TextCollapsingProperties(object):
    """ Represents the characteristics of collapsed text. """
    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the style of the collapsed text.

Get: Style(self: TextCollapsingProperties) -> TextCollapsingStyle

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text run that is used as the collapsed text symbol.

Get: Symbol(self: TextCollapsingProperties) -> TextRun

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width of the range of collapsed text.

Get: Width(self: TextCollapsingProperties) -> float

"""



class TextCollapsingStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the style of collapsed text.
    
    enum TextCollapsingStyle, values: TrailingCharacter (0), TrailingWord (1)
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

    TrailingCharacter = None
    TrailingWord = None
    value__ = None


class TextEmbeddedObject(TextRun):
    """ Defines a type of text content in which measuring, hit testing and drawing of the entire content is done in whole. """
    def ComputeBoundingBox(self, rightToLeft, sideways):
        """
        ComputeBoundingBox(self: TextEmbeddedObject, rightToLeft: bool, sideways: bool) -> Rect
        
            Gets the computed bounding box of the text object.
        
            rightToLeft: A System.Boolean value that determines if the text object is drawn from right to left.
            sideways: A System.Boolean value that determines if the text object is drawn with its side parallel to the 
             baseline.
        
            Returns: A System.Windows.Rect value that represents the bounding box size of the text object.
        """
        pass

    def Draw(self, drawingContext, origin, rightToLeft, sideways):
        """
        Draw(self: TextEmbeddedObject, drawingContext: DrawingContext, origin: Point, rightToLeft: bool, sideways: bool)
            Draws the text object.
        
            drawingContext: The System.Windows.Media.DrawingContext to use for rendering the text object.
            origin: The System.Windows.Point value that represents the origin where the text object is drawn.
            rightToLeft: A System.Boolean value that determines if the text object is drawn from right to left.
            sideways: A System.Boolean value that determines if the text object is drawn with its side parallel to the 
             baseline.
        """
        pass

    def Format(self, remainingParagraphWidth):
        """
        Format(self: TextEmbeddedObject, remainingParagraphWidth: float) -> TextEmbeddedObjectMetrics
        
            Get text object measurement metrics that will fit within the specified remaining width of the 
             paragraph.
        
        
            remainingParagraphWidth: A System.Double that represents the remaining paragraph width.
            Returns: A System.Windows.Media.TextFormatting.TextEmbeddedObjectMetrics value that represents the text 
             object metrics.
        """
        pass

    BreakAfter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the line breaking condition after the text object.

Get: BreakAfter(self: TextEmbeddedObject) -> LineBreakCondition

"""

    BreakBefore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the line breaking condition before the text object.

Get: BreakBefore(self: TextEmbeddedObject) -> LineBreakCondition

"""

    HasFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether the text object has a fixed size regardless of where it is placed within a line.

Get: HasFixedSize(self: TextEmbeddedObject) -> bool

"""



class TextEmbeddedObjectMetrics(object):
    """
    Specifies properties for a System.Windows.Media.TextFormatting.TextEmbeddedObject.
    
    TextEmbeddedObjectMetrics(width: float, height: float, baseline: float)
    """
    @staticmethod # known case of __new__
    def __new__(self, width, height, baseline):
        """ __new__(cls: type, width: float, height: float, baseline: float) """
        pass

    Baseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the baseline of the text object.

Get: Baseline(self: TextEmbeddedObjectMetrics) -> float

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of the text object.

Get: Height(self: TextEmbeddedObjectMetrics) -> float

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width of the text object.

Get: Width(self: TextEmbeddedObjectMetrics) -> float

"""



class TextEndOfLine(TextRun):
    """
    Defines a specialized text run that is used to mark the end of a line.
    
    TextEndOfLine(length: int)
    TextEndOfLine(length: int, textRunProperties: TextRunProperties)
    """
    @staticmethod # known case of __new__
    def __new__(self, length, textRunProperties=None):
        """
        __new__(cls: type, length: int)
        __new__(cls: type, length: int, textRunProperties: TextRunProperties)
        """
        pass

    CharacterBufferReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a reference to the System.Windows.Media.TextFormatting.TextEndOfLine character buffer.

Get: CharacterBufferReference(self: TextEndOfLine) -> CharacterBufferReference

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the character length of the System.Windows.Media.TextFormatting.TextEndOfLine character buffer.

Get: Length(self: TextEndOfLine) -> int

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the set of properties shared by every text character of the System.Windows.Media.TextFormatting.TextEndOfLine character buffer.

Get: Properties(self: TextEndOfLine) -> TextRunProperties

"""



class TextEndOfParagraph(TextEndOfLine):
    """
    Defines a specialized text run that is used to mark the end of a paragraph.
    
    TextEndOfParagraph(length: int)
    TextEndOfParagraph(length: int, textRunProperties: TextRunProperties)
    """
    @staticmethod # known case of __new__
    def __new__(self, length, textRunProperties=None):
        """
        __new__(cls: type, length: int)
        __new__(cls: type, length: int, textRunProperties: TextRunProperties)
        """
        pass


class TextEndOfSegment(TextRun):
    """
    Defines a specialized text run that is used to mark the end of a segment.
    
    TextEndOfSegment(length: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, length):
        """ __new__(cls: type, length: int) """
        pass

    CharacterBufferReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a reference to the System.Windows.Media.TextFormatting.TextEndOfSegment character buffer.

Get: CharacterBufferReference(self: TextEndOfSegment) -> CharacterBufferReference

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the character length of the System.Windows.Media.TextFormatting.TextEndOfSegment character buffer.

Get: Length(self: TextEndOfSegment) -> int

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the set of properties shared by every text character of the System.Windows.Media.TextFormatting.TextEndOfSegment character buffer.

Get: Properties(self: TextEndOfSegment) -> TextRunProperties

"""



class TextFormatter(object, IDisposable):
    """ Provides services for formatting text and breaking text lines using a custom text layout client. """
    @staticmethod
    def Create(textFormattingMode=None):
        """
        Create() -> TextFormatter
        
            Creates a new instance of the System.Windows.Media.TextFormatting.TextFormatter class. This is a 
             static method.
        
            Returns: A new instance of System.Windows.Media.TextFormatting.TextFormatter.
        Create(textFormattingMode: TextFormattingMode) -> TextFormatter
        
            Creates a new instance of the System.Windows.Media.TextFormatting.TextFormatter class with the 
             specified formatting mode. This is a static method.
        
        
            textFormattingMode: The System.Windows.Media.TextFormattingMode that specifies the text layout for the 
             System.Windows.Media.TextFormatting.TextFormatter.
        
            Returns: A new instance of System.Windows.Media.TextFormatting.TextFormatter.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: TextFormatter)
            Releases all managed and unmanaged resources used by the 
             System.Windows.Media.TextFormatting.TextFormatter object.
        """
        pass

    def FormatLine(self, textSource, firstCharIndex, paragraphWidth, paragraphProperties, previousLineBreak, textRunCache=None):
        """
        FormatLine(self: TextFormatter, textSource: TextSource, firstCharIndex: int, paragraphWidth: float, paragraphProperties: TextParagraphProperties, previousLineBreak: TextLineBreak, textRunCache: TextRunCache) -> TextLine
        
            Creates a System.Windows.Media.TextFormatting.TextLine that is used for formatting and 
             displaying document content.
        
        
            textSource: A System.Windows.Media.TextFormatting.TextSource object that represents the text source for the 
             line.
        
            firstCharIndex: An System.Int32 value that specifies the character index of the starting character in the line.
            paragraphWidth: A System.Double value that specifies the width of the paragraph that the line fills.
            paragraphProperties: A System.Windows.Media.TextFormatting.TextParagraphProperties object that represents paragraph 
             properties, such as flow direction, alignment, or indentation.
        
            previousLineBreak: A System.Windows.Media.TextFormatting.TextLineBreak object that specifies the text formatter 
             state, in terms of where the previous line in the paragraph was broken by the text formatting 
             process.
        
            textRunCache: A System.Windows.Media.TextFormatting.TextRunCache object that represents the caching mechanism 
             for the layout of text.
        
            Returns: A System.Windows.Media.TextFormatting.TextLine value that represents a line of text that can be 
             displayed.
        
        FormatLine(self: TextFormatter, textSource: TextSource, firstCharIndex: int, paragraphWidth: float, paragraphProperties: TextParagraphProperties, previousLineBreak: TextLineBreak) -> TextLine
        
            Creates a System.Windows.Media.TextFormatting.TextLine that is used for formatting and 
             displaying document content.
        
        
            textSource: A System.Windows.Media.TextFormatting.TextSource value that represents the text source for the 
             line.
        
            firstCharIndex: An System.Int32 value that specifies the character index of the starting character in the line.
            paragraphWidth: A System.Double value that specifies the width of the paragraph that the line fills.
            paragraphProperties: A System.Windows.Media.TextFormatting.TextParagraphProperties value that represents paragraph 
             properties, such as flow direction, alignment, or indentation.
        
            previousLineBreak: A System.Windows.Media.TextFormatting.TextLineBreak value that specifies the text formatter 
             state, in terms of where the previous line in the paragraph was broken by the text formatting 
             process.
        
            Returns: A System.Windows.Media.TextFormatting.TextLine value that represents a line of text that can be 
             displayed.
        """
        pass

    def FormatMinMaxParagraphWidth(self, textSource, firstCharIndex, paragraphProperties, textRunCache=None):
        """
        FormatMinMaxParagraphWidth(self: TextFormatter, textSource: TextSource, firstCharIndex: int, paragraphProperties: TextParagraphProperties, textRunCache: TextRunCache) -> MinMaxParagraphWidth
        
            Returns a value that represents the smallest and largest possible paragraph width that can fully 
             contain the specified text content.
        
        
            textSource: A System.Windows.Media.TextFormatting.TextSource object that represents the text source for the 
             line.
        
            firstCharIndex: An System.Int32 value that specifies the character index of the starting character in the line.
            paragraphProperties: A System.Windows.Media.TextFormatting.TextParagraphProperties object that represents paragraph 
             properties, such as flow direction, alignment, or indentation.
        
            textRunCache: A System.Windows.Media.TextFormatting.TextRunCache object that represents the caching mechanism 
             for the layout of text.
        
            Returns: A System.Windows.Media.TextFormatting.MinMaxParagraphWidth value that represents the smallest 
             and largest possible paragraph width that can fully contain the specified text content.
        
        FormatMinMaxParagraphWidth(self: TextFormatter, textSource: TextSource, firstCharIndex: int, paragraphProperties: TextParagraphProperties) -> MinMaxParagraphWidth
        
            Returns a value that represents the smallest and largest possible paragraph width that can fully 
             contain the specified text content.
        
        
            textSource: A System.Windows.Media.TextFormatting.TextSource object that represents the text source for the 
             line.
        
            firstCharIndex: An System.Int32 value that specifies the character index of the starting character in the line.
            paragraphProperties: A System.Windows.Media.TextFormatting.TextParagraphProperties object that represents paragraph 
             properties, such as flow direction, alignment, or indentation.
        
            Returns: A System.Windows.Media.TextFormatting.MinMaxParagraphWidth value that represents the smallest 
             and largest possible paragraph width that can fully contain the specified text content.
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


class TextHidden(TextRun):
    """
    Defines a specialized text run that is used to mark a range of hidden characters.
    
    TextHidden(length: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, length):
        """ __new__(cls: type, length: int) """
        pass

    CharacterBufferReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a reference to the System.Windows.Media.TextFormatting.TextHidden character buffer.

Get: CharacterBufferReference(self: TextHidden) -> CharacterBufferReference

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the character length of the System.Windows.Media.TextFormatting.TextHidden character buffer.

Get: Length(self: TextHidden) -> int

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the set of properties shared by every text character of the System.Windows.Media.TextFormatting.TextHidden character buffer.

Get: Properties(self: TextHidden) -> TextRunProperties

"""



class TextLine(object, ITextMetrics, IDisposable):
    """ Provides an abstract class for supporting formatting services to a line of text. """
    def Collapse(self, collapsingPropertiesList):
        """
        Collapse(self: TextLine, *collapsingPropertiesList: Array[TextCollapsingProperties]) -> TextLine
        
            Create a collapsed line based on collapsed text properties.
        
            collapsingPropertiesList: A list of System.Windows.Media.TextFormatting.TextCollapsingProperties objects that represent 
             the collapsed text properties.
        
            Returns: A System.Windows.Media.TextFormatting.TextLine value that represents a collapsed line that can 
             be displayed.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: TextLine)
            Releases all managed and unmanaged resources used by the 
             System.Windows.Media.TextFormatting.TextFormatter object.
        """
        pass

    def Draw(self, drawingContext, origin, inversion):
        """
        Draw(self: TextLine, drawingContext: DrawingContext, origin: Point, inversion: InvertAxes)
            Renders the System.Windows.Media.TextFormatting.TextLine object based upon the specified 
             System.Windows.Media.DrawingContext.
        
        
            drawingContext: The System.Windows.Media.DrawingContext object onto which the 
             System.Windows.Media.TextFormatting.TextLine is rendered.
        
            origin: A System.Windows.Point value that represents the drawing origin.
            inversion: An enumerated System.Windows.Media.TextFormatting.InvertAxes value that indicates the inversion 
             of the horizontal and vertical axes of the drawing surface.
        """
        pass

    def GetBackspaceCaretCharacterHit(self, characterHit):
        """
        GetBackspaceCaretCharacterHit(self: TextLine, characterHit: CharacterHit) -> CharacterHit
        
            Gets the previous character hit after backspacing.
        
            characterHit: The current System.Windows.Media.TextFormatting.CharacterHit object.
            Returns: The System.Windows.Media.TextFormatting.CharacterHit object after backspacing.
        """
        pass

    def GetCharacterHitFromDistance(self, distance):
        """
        GetCharacterHitFromDistance(self: TextLine, distance: float) -> CharacterHit
        
            Gets the character hit corresponding to the specified distance from the beginning of the line.
        
            distance: A System.Double value that represents the distance from the beginning of the line.
            Returns: The System.Windows.Media.TextFormatting.CharacterHit object at the specified distance from the 
             beginning of the line.
        """
        pass

    def GetDistanceFromCharacterHit(self, characterHit):
        """
        GetDistanceFromCharacterHit(self: TextLine, characterHit: CharacterHit) -> float
        
            Gets the distance from the beginning of the line to the specified character hit.
        
            characterHit: The System.Windows.Media.TextFormatting.CharacterHit object whose distance you want to query.
            Returns: A System.Double that represents the distance from the beginning of the line.
        """
        pass

    def GetIndexedGlyphRuns(self):
        """
        GetIndexedGlyphRuns(self: TextLine) -> IEnumerable[IndexedGlyphRun]
        
            Gets an enumerator for enumerating System.Windows.Media.TextFormatting.IndexedGlyphRun objects 
             in the System.Windows.Media.TextFormatting.TextLine.
        
            Returns: An enumerator that allows you to enumerate each 
             System.Windows.Media.TextFormatting.IndexedGlyphRun object in the 
             System.Windows.Media.TextFormatting.TextLine.
        """
        pass

    def GetNextCaretCharacterHit(self, characterHit):
        """
        GetNextCaretCharacterHit(self: TextLine, characterHit: CharacterHit) -> CharacterHit
        
            Gets the next character hit for caret navigation.
        
            characterHit: The current System.Windows.Media.TextFormatting.CharacterHit object.
            Returns: The next System.Windows.Media.TextFormatting.CharacterHit object based on caret navigation.
        """
        pass

    def GetPreviousCaretCharacterHit(self, characterHit):
        """
        GetPreviousCaretCharacterHit(self: TextLine, characterHit: CharacterHit) -> CharacterHit
        
            Gets the previous character hit for caret navigation.
        
            characterHit: The current System.Windows.Media.TextFormatting.CharacterHit object.
            Returns: The previous System.Windows.Media.TextFormatting.CharacterHit object based on caret navigation.
        """
        pass

    def GetTextBounds(self, firstTextSourceCharacterIndex, textLength):
        """
        GetTextBounds(self: TextLine, firstTextSourceCharacterIndex: int, textLength: int) -> IList[TextBounds]
        
            Gets an array of bounding rectangles that represent the range of characters within a text line.
        
            firstTextSourceCharacterIndex: An System.Int32 value that represents the index of first character of specified range.
            textLength: An System.Int32 value that represents the number of characters of the specified range.
            Returns: A list of System.Windows.Media.TextFormatting.TextBounds objects representing the bounding 
             rectangle.
        """
        pass

    def GetTextCollapsedRanges(self):
        """
        GetTextCollapsedRanges(self: TextLine) -> IList[TextCollapsedRange]
        
            Gets a collection of collapsed text ranges after a line has been collapsed.
            Returns: A list of System.Windows.Media.TextFormatting.TextCollapsedRange objects that represent the 
             collapsed text.
        """
        pass

    def GetTextLineBreak(self):
        """
        GetTextLineBreak(self: TextLine) -> TextLineBreak
        
            Gets the state of the line when broken by line breaking process.
            Returns: A System.Windows.Media.TextFormatting.TextLineBreak value that represents the line break.
        """
        pass

    def GetTextRunSpans(self):
        """
        GetTextRunSpans(self: TextLine) -> IList[TextSpan[TextRun]]
        
            Gets a collection of System.Windows.Media.TextFormatting.TextRun objects in a text span that are 
             contained within a line.
        
            Returns: Gets a list of System.Windows.Media.TextFormatting.TextRun objects contained within a text span.
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
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, pixelsPerDip: float)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Baseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the distance from the top to the baseline of the current System.Windows.Media.TextFormatting.TextLine object.

Get: Baseline(self: TextLine) -> float

"""

    DependentLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of characters following the last character of the line that may trigger reformatting of the current line.

Get: DependentLength(self: TextLine) -> int

"""

    Extent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the distance from the top-most to bottom-most black pixel in a line.

Get: Extent(self: TextLine) -> float

"""

    HasCollapsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the line is collapsed.

Get: HasCollapsed(self: TextLine) -> bool

"""

    HasOverflowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether content of the line overflows the specified paragraph width.

Get: HasOverflowed(self: TextLine) -> bool

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of a line of text.

Get: Height(self: TextLine) -> float

"""

    IsTruncated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether the text line is truncated in the middle of a word.

Get: IsTruncated(self: TextLine) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total number of System.Windows.Media.TextFormatting.TextSource positions of the current line.

Get: Length(self: TextLine) -> int

"""

    MarkerBaseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the distance from the edge of the line's highest point to the baseline marker of the line.

Get: MarkerBaseline(self: TextLine) -> float

"""

    MarkerHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of a marker for a list item.

Get: MarkerHeight(self: TextLine) -> float

"""

    NewlineLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of newline characters at the end of a line.

Get: NewlineLength(self: TextLine) -> int

"""

    OverhangAfter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the distance that black pixels extend beyond the bottom alignment edge of a line.

Get: OverhangAfter(self: TextLine) -> float

"""

    OverhangLeading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the distance that black pixels extend prior to the left leading alignment edge of the line.

Get: OverhangLeading(self: TextLine) -> float

"""

    OverhangTrailing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the distance that black pixels extend following the right trailing alignment edge of the line.

Get: OverhangTrailing(self: TextLine) -> float

"""

    PixelsPerDip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PixelsPerDip(self: TextLine) -> float

Set: PixelsPerDip(self: TextLine) = value
"""

    Start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the distance from the start of a paragraph to the starting point of a line.

Get: Start(self: TextLine) -> float

"""

    TextBaseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the distance from the top to the baseline of the line of text.

Get: TextBaseline(self: TextLine) -> float

"""

    TextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of the text and any other content in the line.

Get: TextHeight(self: TextLine) -> float

"""

    TrailingWhitespaceLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of whitespace code points beyond the last non-blank character in a line.

Get: TrailingWhitespaceLength(self: TextLine) -> int

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width of a line of text, excluding trailing whitespace characters.

Get: Width(self: TextLine) -> float

"""

    WidthIncludingTrailingWhitespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width of a line of text, including trailing whitespace characters.

Get: WidthIncludingTrailingWhitespace(self: TextLine) -> float

"""



class TextLineBreak(object, IDisposable):
    """ Specifies text properties and state at the point where text is broken by the line breaking process. """
    def Clone(self):
        """
        Clone(self: TextLineBreak) -> TextLineBreak
        
            Clone a new instance of the System.Windows.Media.TextFormatting.TextLineBreak object.
            Returns: A new instance of System.Windows.Media.TextFormatting.TextLineBreak.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: TextLineBreak)
            Releases the resources used by the System.Windows.Media.TextFormatting.TextLineBreak class.
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


class TextMarkerProperties(object):
    """ Represents an abstract class for defining text markers. """
    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the distance from the start of the line to the end of the text marker symbol.

Get: Offset(self: TextMarkerProperties) -> float

"""

    TextSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Media.TextFormatting.TextSource that represents the source of the text runs for the marker symbol.

Get: TextSource(self: TextMarkerProperties) -> TextSource

"""



class TextModifier(TextRun):
    """ Represents a specialized text run that can be used to modify properties of text runs within its scope. """
    def ModifyProperties(self, properties):
        """
        ModifyProperties(self: TextModifier, properties: TextRunProperties) -> TextRunProperties
        
            Retrieves the System.Windows.Media.TextFormatting.TextRunProperties for a text run.
        
            properties: The System.Windows.Media.TextFormatting.TextRunProperties for a text run, or the return value of 
             System.Windows.Media.TextFormatting.TextModifier.ModifyProperties(System.Windows.Media.TextFormat
             ting.TextRunProperties) for a nested text modifier.
        
            Returns: The actual System.Windows.Media.TextFormatting.TextRunProperties to be used by the 
             System.Windows.Media.TextFormatting.TextFormatter, subject to further modification by 
             System.Windows.Media.TextFormatting.TextModifier objects at outer scopes.
        """
        pass

    CharacterBufferReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Media.TextFormatting.CharacterBufferReference for the System.Windows.Media.TextFormatting.TextModifier.

Get: CharacterBufferReference(self: TextModifier) -> CharacterBufferReference

"""

    FlowDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.FlowDirection for the System.Windows.Media.TextFormatting.TextModifier.

Get: FlowDirection(self: TextModifier) -> FlowDirection

"""

    HasDirectionalEmbedding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Media.TextFormatting.TextModifier supports System.Windows.FlowDirection for the current scope of text.

Get: HasDirectionalEmbedding(self: TextModifier) -> bool

"""



class TextParagraphProperties(object):
    """ Provides a set of properties, such as flow direction, alignment, or indentation, that can be applied to a paragraph. This is an abstract class. """
    AlwaysCollapsible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a formatted line can always be collapsed.

Get: AlwaysCollapsible(self: TextParagraphProperties) -> bool

"""

    DefaultIncrementalTab = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default incremental tab distance.

Get: DefaultIncrementalTab(self: TextParagraphProperties) -> float

"""

    DefaultTextRunProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default text run properties, such as typeface or foreground brush.

Get: DefaultTextRunProperties(self: TextParagraphProperties) -> TextRunProperties

"""

    FirstLineInParagraph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the text run is the first line of the paragraph.

Get: FirstLineInParagraph(self: TextParagraphProperties) -> bool

"""

    FlowDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies whether the primary text advance direction shall be left-to-right, or right-to-left.

Get: FlowDirection(self: TextParagraphProperties) -> FlowDirection

"""

    Indent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of line indentation.

Get: Indent(self: TextParagraphProperties) -> float

"""

    LineHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the height of a line of text.

Get: LineHeight(self: TextParagraphProperties) -> float

"""

    ParagraphIndent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of the paragraph indentation.

Get: ParagraphIndent(self: TextParagraphProperties) -> float

"""

    Tabs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of tab definitions.

Get: Tabs(self: TextParagraphProperties) -> IList[TextTabProperties]

"""

    TextAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that describes how an inline content of a block is aligned.

Get: TextAlignment(self: TextParagraphProperties) -> TextAlignment

"""

    TextDecorations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of System.Windows.TextDecoration objects.

Get: TextDecorations(self: TextParagraphProperties) -> TextDecorationCollection

"""

    TextMarkerProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies marker characteristics of the first line in the paragraph.

Get: TextMarkerProperties(self: TextParagraphProperties) -> TextMarkerProperties

"""

    TextWrapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that controls whether text wraps when it reaches the flow edge of its containing block box.

Get: TextWrapping(self: TextParagraphProperties) -> TextWrapping

"""



class TextRunBounds(object):
    """ Represents the bounding rectangle of a text run. """
    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the character length of bounded text run.

Get: Length(self: TextRunBounds) -> int

"""

    Rectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the bounding rectangle for the text run.

Get: Rectangle(self: TextRunBounds) -> Rect

"""

    TextRun = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Media.TextFormatting.TextRun object that represents the text run.

Get: TextRun(self: TextRunBounds) -> TextRun

"""

    TextSourceCharacterIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the character index of the first character in the bounded text run.

Get: TextSourceCharacterIndex(self: TextRunBounds) -> int

"""



class TextRunCache(object):
    """
    Provides caching services to the System.Windows.Media.TextFormatting.TextFormatter object in order to improve performance.
    
    TextRunCache()
    """
    def Change(self, textSourceCharacterIndex, addition, removal):
        """
        Change(self: TextRunCache, textSourceCharacterIndex: int, addition: int, removal: int)
            Notifies the text engine client of a change to the cache when text content or text run 
             properties of System.Windows.Media.TextFormatting.TextRun are added, removed, or replaced.
        
        
            textSourceCharacterIndex: Specifies the System.Windows.Media.TextFormatting.TextSource character index position of the 
             start of the change.
        
            addition: Indicates the number of System.Windows.Media.TextFormatting.TextSource characters to be added.
            removal: Indicates the number of System.Windows.Media.TextFormatting.TextSource characters to be removed.
        """
        pass

    def Invalidate(self):
        """
        Invalidate(self: TextRunCache)
            Signals the text engine client to invalidate the entire contents of the 
             System.Windows.Media.TextFormatting.TextFormatter cache.
        """
        pass


class TextRunProperties(object):
    """ Provides a set of properties, such as typeface or foreground brush, that can be applied to a System.Windows.Media.TextFormatting.TextRun object. This is an abstract class. """
    BackgroundBrush = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brush that is used to paint the background color of the text run.

Get: BackgroundBrush(self: TextRunProperties) -> Brush

"""

    BaselineAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the baseline style for a text that is positioned on the vertical axis.

Get: BaselineAlignment(self: TextRunProperties) -> BaselineAlignment

"""

    CultureInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the culture information for the text run.

Get: CultureInfo(self: TextRunProperties) -> CultureInfo

"""

    FontHintingEmSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text size in points, which is then used for font hinting.

Get: FontHintingEmSize(self: TextRunProperties) -> float

"""

    FontRenderingEmSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text size in points for the text run.

Get: FontRenderingEmSize(self: TextRunProperties) -> float

"""

    ForegroundBrush = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brush that is used to paint the foreground color of the text run.

Get: ForegroundBrush(self: TextRunProperties) -> Brush

"""

    NumberSubstitution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number substitution settings, which determines who numbers in text are displayed in different cultures.

Get: NumberSubstitution(self: TextRunProperties) -> NumberSubstitution

"""

    PixelsPerDip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PixelsPerDip(self: TextRunProperties) -> float

Set: PixelsPerDip(self: TextRunProperties) = value
"""

    TextDecorations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of  System.Windows.TextDecoration objects used for the text run.

Get: TextDecorations(self: TextRunProperties) -> TextDecorationCollection

"""

    TextEffects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of System.Windows.Media.TextEffect objects used for the text run.

Get: TextEffects(self: TextRunProperties) -> TextEffectCollection

"""

    Typeface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the typeface for the text run.

Get: Typeface(self: TextRunProperties) -> Typeface

"""

    TypographyProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the typography properties for the text run.

Get: TypographyProperties(self: TextRunProperties) -> TextRunTypographyProperties

"""



class TextRunTypographyProperties(object):
    """ Provides an abstract class for supporting typography properties for System.Windows.Media.TextFormatting.TextRun objects. """
    def OnPropertiesChanged(self, *args): #cannot find CLR method
        """
        OnPropertiesChanged(self: TextRunTypographyProperties)
            Corrects internal state for a System.Windows.Media.TextFormatting.TextRunTypographyProperties 
             derived class whenever any System.Windows.Media.TextFormatting.TextRunTypographyProperties 
             property changes its value.
        """
        pass

    AnnotationAlternates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of an alternate annotation form.

Get: AnnotationAlternates(self: TextRunTypographyProperties) -> int

"""

    Capitals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the capital form of the selected font.

Get: Capitals(self: TextRunTypographyProperties) -> FontCapitals

"""

    CapitalSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether inter-glyph spacing for all-capital text is globally adjusted to improve readability.

Get: CapitalSpacing(self: TextRunTypographyProperties) -> bool

"""

    CaseSensitiveForms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether glyphs adjust their vertical position to better align with uppercase glyphs.

Get: CaseSensitiveForms(self: TextRunTypographyProperties) -> bool

"""

    ContextualAlternates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether custom glyph forms can be used based upon the context of the text being rendered.

Get: ContextualAlternates(self: TextRunTypographyProperties) -> bool

"""

    ContextualLigatures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether contextual ligatures are enabled.

Get: ContextualLigatures(self: TextRunTypographyProperties) -> bool

"""

    ContextualSwashes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies the index of a contextual swashes form.

Get: ContextualSwashes(self: TextRunTypographyProperties) -> int

"""

    DiscretionaryLigatures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether discretionary ligatures are enabled.

Get: DiscretionaryLigatures(self: TextRunTypographyProperties) -> bool

"""

    EastAsianExpertForms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the standard Japanese font forms have been replaced with the corresponding preferred typographic forms.

Get: EastAsianExpertForms(self: TextRunTypographyProperties) -> bool

"""

    EastAsianLanguage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the version of glyphs to be used for a specific writing system or language.

Get: EastAsianLanguage(self: TextRunTypographyProperties) -> FontEastAsianLanguage

"""

    EastAsianWidths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the proportional width to be used for Latin characters in an East Asian font.

Get: EastAsianWidths(self: TextRunTypographyProperties) -> FontEastAsianWidths

"""

    Fraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the fraction style.

Get: Fraction(self: TextRunTypographyProperties) -> FontFraction

"""

    HistoricalForms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether historical forms are enabled.

Get: HistoricalForms(self: TextRunTypographyProperties) -> bool

"""

    HistoricalLigatures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether historical ligatures are enabled.

Get: HistoricalLigatures(self: TextRunTypographyProperties) -> bool

"""

    Kerning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether kerning is enabled.

Get: Kerning(self: TextRunTypographyProperties) -> bool

"""

    MathematicalGreek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether standard typographic font forms of Greek glyphs have been replaced with corresponding font forms commonly used in mathematical notation.

Get: MathematicalGreek(self: TextRunTypographyProperties) -> bool

"""

    NumeralAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the alignment of widths when using numerals.

Get: NumeralAlignment(self: TextRunTypographyProperties) -> FontNumeralAlignment

"""

    NumeralStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the set of glyphs that are used to render numeric alternate font forms.

Get: NumeralStyle(self: TextRunTypographyProperties) -> FontNumeralStyle

"""

    SlashedZero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a nominal zero font form should be replaced with a slashed zero.

Get: SlashedZero(self: TextRunTypographyProperties) -> bool

"""

    StandardLigatures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether standard ligatures are enabled.

Get: StandardLigatures(self: TextRunTypographyProperties) -> bool

"""

    StandardSwashes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of a standard swashes form.

Get: StandardSwashes(self: TextRunTypographyProperties) -> int

"""

    StylisticAlternates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of a stylistic alternates form.

Get: StylisticAlternates(self: TextRunTypographyProperties) -> int

"""

    StylisticSet1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet1(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet10(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet11 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet11(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet12 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet12(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet13 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet13(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet14 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet14(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet15 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet15(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet16(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet17 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet17(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet18 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet18(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet19 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet19(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet2(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet20 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet20(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet3(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet4(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet5(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet6(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet7(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet8(self: TextRunTypographyProperties) -> bool

"""

    StylisticSet9 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a stylistic set of a font form is enabled.

Get: StylisticSet9(self: TextRunTypographyProperties) -> bool

"""

    Variants = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates a variation of the standard typographic form to be used.

Get: Variants(self: TextRunTypographyProperties) -> FontVariants

"""



class TextSimpleMarkerProperties(TextMarkerProperties):
    """
    Provides for a generic implementation of text marker properties.
    
    TextSimpleMarkerProperties(style: TextMarkerStyle, offset: float, autoNumberingIndex: int, textParagraphProperties: TextParagraphProperties)
    """
    @staticmethod # known case of __new__
    def __new__(self, style, offset, autoNumberingIndex, textParagraphProperties):
        """ __new__(cls: type, style: TextMarkerStyle, offset: float, autoNumberingIndex: int, textParagraphProperties: TextParagraphProperties) """
        pass

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the distance from the start of the line to the end of the text marker symbol.

Get: Offset(self: TextSimpleMarkerProperties) -> float

"""

    TextSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the source of the text runs used for the text marker.

Get: TextSource(self: TextSimpleMarkerProperties) -> TextSource

"""



class TextSource(object):
    """ Provides an abstract class for specifying character data and formatting properties to be used by the System.Windows.Media.TextFormatting.TextFormatter object. """
    def GetPrecedingText(self, textSourceCharacterIndexLimit):
        """
        GetPrecedingText(self: TextSource, textSourceCharacterIndexLimit: int) -> TextSpan[CultureSpecificCharacterBufferRange]
        
            Retrieves the text span immediately before the specified 
             System.Windows.Media.TextFormatting.TextSource position.
        
        
            textSourceCharacterIndexLimit: An System.Int32 value that specifies the character index position where text retrieval stops.
            Returns: A System.Windows.Media.TextFormatting.CultureSpecificCharacterBufferRange value that represents 
             the text span immediately before textSourceCharacterIndexLimit.
        """
        pass

    def GetTextEffectCharacterIndexFromTextSourceCharacterIndex(self, textSourceCharacterIndex):
        """
        GetTextEffectCharacterIndexFromTextSourceCharacterIndex(self: TextSource, textSourceCharacterIndex: int) -> int
        
            Retrieves a value that maps a System.Windows.Media.TextFormatting.TextSource character index to 
             a System.Windows.Media.TextEffect character index.
        
        
            textSourceCharacterIndex: An System.Int32 value that specifies the System.Windows.Media.TextFormatting.TextSource 
             character index to map.
        
            Returns: An System.Int32 value that represents the System.Windows.Media.TextEffect character index.
        """
        pass

    def GetTextRun(self, textSourceCharacterIndex):
        """
        GetTextRun(self: TextSource, textSourceCharacterIndex: int) -> TextRun
        
            Retrieves a System.Windows.Media.TextFormatting.TextRun starting at a specified 
             System.Windows.Media.TextFormatting.TextSource position.
        
        
            textSourceCharacterIndex: Specifies the character index position in the System.Windows.Media.TextFormatting.TextSource 
             where the System.Windows.Media.TextFormatting.TextRun is retrieved.
        
            Returns: A value that represents a System.Windows.Media.TextFormatting.TextRun, or an object derived from 
             System.Windows.Media.TextFormatting.TextRun.
        """
        pass

    PixelsPerDip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PixelsPerDip(self: TextSource) -> float

Set: PixelsPerDip(self: TextSource) = value
"""



class TextSpan(object):
    """ TextSpan[T](length: int, value: T) """
    @staticmethod # known case of __new__
    def __new__(self, length, value):
        """ __new__(cls: type, length: int, value: T) """
        pass

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of characters in the text span.

Get: Length(self: TextSpan[T]) -> int

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object associated with the text span.

Get: Value(self: TextSpan[T]) -> T

"""



class TextTabAlignment(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes how text is aligned at a tab location.
    
    enum TextTabAlignment, values: Center (1), Character (3), Left (0), Right (2)
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

    Center = None
    Character = None
    Left = None
    Right = None
    value__ = None


class TextTabProperties(object):
    """
    Specifies properties of user-defined tabs.
    
    TextTabProperties(alignment: TextTabAlignment, location: float, tabLeader: int, aligningChar: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, alignment, location, tabLeader, aligningChar):
        """ __new__(cls: type, alignment: TextTabAlignment, location: float, tabLeader: int, aligningChar: int) """
        pass

    AligningCharacter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of the specific character in the text that is aligned at the specified tab location.

Get: AligningCharacter(self: TextTabProperties) -> int

"""

    Alignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the alignment style of the text at the tab location.

Get: Alignment(self: TextTabProperties) -> TextTabAlignment

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index value of the tab location.

Get: Location(self: TextTabProperties) -> float

"""

    TabLeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of the character that is used to display the tab leader.

Get: TabLeader(self: TextTabProperties) -> int

"""



class TextTrailingCharacterEllipsis(TextCollapsingProperties):
    """
    Defines collapsed text properties for collapsing a whole line toward the end at character granularity, and with ellipsis being the collapsed text symbol.
    
    TextTrailingCharacterEllipsis(width: float, textRunProperties: TextRunProperties)
    """
    @staticmethod # known case of __new__
    def __new__(self, width, textRunProperties):
        """ __new__(cls: type, width: float, textRunProperties: TextRunProperties) """
        pass

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the style of collapsed text.

Get: Style(self: TextTrailingCharacterEllipsis) -> TextCollapsingStyle

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text run that is used as the collapsed text symbol.

Get: Symbol(self: TextTrailingCharacterEllipsis) -> TextRun

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width for which the specified collapsed text range is constrained to.

Get: Width(self: TextTrailingCharacterEllipsis) -> float

"""



class TextTrailingWordEllipsis(TextCollapsingProperties):
    """
    Defines collapsed text properties for collapsing a whole line toward the end at word granularity, and with ellipsis being the collapsed text symbol.
    
    TextTrailingWordEllipsis(width: float, textRunProperties: TextRunProperties)
    """
    @staticmethod # known case of __new__
    def __new__(self, width, textRunProperties):
        """ __new__(cls: type, width: float, textRunProperties: TextRunProperties) """
        pass

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the style of collapsed text.

Get: Style(self: TextTrailingWordEllipsis) -> TextCollapsingStyle

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text run that is used as the collapsed text symbol.

Get: Symbol(self: TextTrailingWordEllipsis) -> TextRun

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the width for which the specified collapsed text range is constrained to.

Get: Width(self: TextTrailingWordEllipsis) -> float

"""



