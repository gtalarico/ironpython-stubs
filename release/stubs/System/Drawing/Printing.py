# encoding: utf-8
# module System.Drawing.Printing calls itself Printing
# from System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Duplex(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the printer's duplex setting.
    
    enum Duplex, values: Default (-1), Horizontal (3), Simplex (1), Vertical (2)
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

    Default = None
    Horizontal = None
    Simplex = None
    value__ = None
    Vertical = None


class InvalidPrinterException(SystemException, ISerializable, _Exception):
    """
    Represents the exception that is thrown when you try to access a printer using printer settings that are not valid.
    
    InvalidPrinterException(settings: PrinterSettings)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: InvalidPrinterException, info: SerializationInfo, context: StreamingContext)
            Overridden. Sets the System.Runtime.Serialization.SerializationInfo with information about the 
             exception.
        
        
            info: The System.Runtime.Serialization.SerializationInfo that holds the serialized object data about 
             the exception being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext that contains contextual information about the 
             source or destination.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, settings):
        """
        __new__(cls: type, settings: PrinterSettings)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class Margins(object, ICloneable):
    """
    Specifies the dimensions of the margins of a printed page.
    
    Margins(left: int, right: int, top: int, bottom: int)
    Margins()
    """
    def Clone(self):
        """
        Clone(self: Margins) -> object
        
            Retrieves a duplicate of this object, member by member.
            Returns: A duplicate of this object.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Margins, obj: object) -> bool
        
            Compares this System.Drawing.Printing.Margins to the specified System.Object to determine 
             whether they have the same dimensions.
        
        
            obj: The object to which to compare this System.Drawing.Printing.Margins.
            Returns: true if the specified object is a System.Drawing.Printing.Margins and has the same 
             System.Drawing.Printing.Margins.Top, System.Drawing.Printing.Margins.Bottom, 
             System.Drawing.Printing.Margins.Right and System.Drawing.Printing.Margins.Left values as this 
             System.Drawing.Printing.Margins; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Margins) -> int
        
            Calculates and retrieves a hash code based on the width of the left, right, top, and bottom 
             margins.
        
            Returns: A hash code based on the left, right, top, and bottom margins.
        """
        pass

    def ToString(self):
        """
        ToString(self: Margins) -> str
        
            Converts the System.Drawing.Printing.Margins to a string.
            Returns: A System.String representation of the System.Drawing.Printing.Margins.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, left=None, right=None, top=None, bottom=None):
        """
        __new__(cls: type)
        __new__(cls: type, left: int, right: int, top: int, bottom: int)
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

    Bottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the bottom margin, in hundredths of an inch.

Get: Bottom(self: Margins) -> int

Set: Bottom(self: Margins) = value
"""

    Left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the left margin width, in hundredths of an inch.

Get: Left(self: Margins) -> int

Set: Left(self: Margins) = value
"""

    Right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the right margin width, in hundredths of an inch.

Get: Right(self: Margins) -> int

Set: Right(self: Margins) = value
"""

    Top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the top margin width, in hundredths of an inch.

Get: Top(self: Margins) -> int

Set: Top(self: Margins) = value
"""



class MarginsConverter(ExpandableObjectConverter):
    """
    Provides a System.Drawing.Printing.MarginsConverter for System.Drawing.Printing.Margins.
    
    MarginsConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: MarginsConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Returns whether this converter can convert an object of the specified source type to the native 
             type of the converter using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type from which you want to convert.
            Returns: true if an object can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: MarginsConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Returns whether this converter can convert an object to the given destination type using the 
             context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that represents the type to which you want to convert.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: MarginsConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the specified object to the converter's native type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo that provides the language to convert to.
            value: The System.Object to convert.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: MarginsConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the given value object to the specified destination type using the specified context 
             and arguments.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo that provides the language to convert to.
            value: The System.Object to convert.
            destinationType: The System.Type to which to convert the value.
            Returns: An System.Object that represents the converted value.
        """
        pass

    def CreateInstance(self, *__args):
        """
        CreateInstance(self: MarginsConverter, context: ITypeDescriptorContext, propertyValues: IDictionary) -> object
        
            Creates an System.Object given a set of property values for the object.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            propertyValues: An System.Collections.IDictionary of new property values.
            Returns: An System.Object representing the specified System.Collections.IDictionary, or null if the 
             object cannot be created.
        """
        pass

    def GetCreateInstanceSupported(self, context=None):
        """
        GetCreateInstanceSupported(self: MarginsConverter, context: ITypeDescriptorContext) -> bool
        
            Returns whether changing a value on this object requires a call to the 
             System.Drawing.Printing.MarginsConverter.CreateInstance(System.ComponentModel.ITypeDescriptorCont
             ext,System.Collections.IDictionary) method to create a new value, using the specified context.
        
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            Returns: true if changing a property on this object requires a call to 
             System.Drawing.Printing.MarginsConverter.CreateInstance(System.ComponentModel.ITypeDescriptorCont
             ext,System.Collections.IDictionary) to create a new value; otherwise, false. This method always 
             returns true.
        """
        pass


class PageSettings(object, ICloneable):
    """
    Specifies settings that apply to a single, printed page.
    
    PageSettings()
    PageSettings(printerSettings: PrinterSettings)
    """
    def Clone(self):
        """
        Clone(self: PageSettings) -> object
        
            Creates a copy of this System.Drawing.Printing.PageSettings.
            Returns: A copy of this object.
        """
        pass

    def CopyToHdevmode(self, hdevmode):
        """
        CopyToHdevmode(self: PageSettings, hdevmode: IntPtr)
            Copies the relevant information from the System.Drawing.Printing.PageSettings to the specified 
             DEVMODE structure.
        
        
            hdevmode: The handle to a Win32 DEVMODE structure.
        """
        pass

    def SetHdevmode(self, hdevmode):
        """
        SetHdevmode(self: PageSettings, hdevmode: IntPtr)
            Copies relevant information to the System.Drawing.Printing.PageSettings from the specified 
             DEVMODE structure.
        
        
            hdevmode: The handle to a Win32 DEVMODE structure.
        """
        pass

    def ToString(self):
        """
        ToString(self: PageSettings) -> str
        
            Converts the System.Drawing.Printing.PageSettings to string form.
            Returns: A string showing the various property settings for the System.Drawing.Printing.PageSettings.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, printerSettings=None):
        """
        __new__(cls: type)
        __new__(cls: type, printerSettings: PrinterSettings)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the page, taking into account the page orientation specified by the System.Drawing.Printing.PageSettings.Landscape property.

Get: Bounds(self: PageSettings) -> Rectangle

"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the page should be printed in color.

Get: Color(self: PageSettings) -> bool

Set: Color(self: PageSettings) = value
"""

    HardMarginX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the x-coordinate, in hundredths of an inch, of the hard margin at the left of the page.

Get: HardMarginX(self: PageSettings) -> Single

"""

    HardMarginY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the y-coordinate, in hundredths of an inch, of the hard margin at the top of the page.

Get: HardMarginY(self: PageSettings) -> Single

"""

    Landscape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the page is printed in landscape or portrait orientation.

Get: Landscape(self: PageSettings) -> bool

Set: Landscape(self: PageSettings) = value
"""

    Margins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the margins for this page.

Get: Margins(self: PageSettings) -> Margins

Set: Margins(self: PageSettings) = value
"""

    PaperSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the paper size for the page.

Get: PaperSize(self: PageSettings) -> PaperSize

Set: PaperSize(self: PageSettings) = value
"""

    PaperSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the page's paper source; for example, the printer's upper tray.

Get: PaperSource(self: PageSettings) -> PaperSource

Set: PaperSource(self: PageSettings) = value
"""

    PrintableArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the bounds of the printable area of the page for the printer.

Get: PrintableArea(self: PageSettings) -> RectangleF

"""

    PrinterResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the printer resolution for the page.

Get: PrinterResolution(self: PageSettings) -> PrinterResolution

Set: PrinterResolution(self: PageSettings) = value
"""

    PrinterSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the printer settings associated with the page.

Get: PrinterSettings(self: PageSettings) -> PrinterSettings

Set: PrinterSettings(self: PageSettings) = value
"""



class PaperKind(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the standard paper sizes.
    
    enum PaperKind, values: A2 (66), A3 (8), A3Extra (63), A3ExtraTransverse (68), A3Rotated (76), A3Transverse (67), A4 (9), A4Extra (53), A4Plus (60), A4Rotated (77), A4Small (10), A4Transverse (55), A5 (11), A5Extra (64), A5Rotated (78), A5Transverse (61), A6 (70), A6Rotated (83), APlus (57), B4 (12), B4Envelope (33), B4JisRotated (79), B5 (13), B5Envelope (34), B5Extra (65), B5JisRotated (80), B5Transverse (62), B6Envelope (35), B6Jis (88), B6JisRotated (89), BPlus (58), C3Envelope (29), C4Envelope (30), C5Envelope (28), C65Envelope (32), C6Envelope (31), CSheet (24), Custom (0), DLEnvelope (27), DSheet (25), ESheet (26), Executive (7), Folio (14), GermanLegalFanfold (41), GermanStandardFanfold (40), InviteEnvelope (47), IsoB4 (42), ItalyEnvelope (36), JapaneseDoublePostcard (69), JapaneseDoublePostcardRotated (82), JapaneseEnvelopeChouNumber3 (73), JapaneseEnvelopeChouNumber3Rotated (86), JapaneseEnvelopeChouNumber4 (74), JapaneseEnvelopeChouNumber4Rotated (87), JapaneseEnvelopeKakuNumber2 (71), JapaneseEnvelopeKakuNumber2Rotated (84), JapaneseEnvelopeKakuNumber3 (72), JapaneseEnvelopeKakuNumber3Rotated (85), JapaneseEnvelopeYouNumber4 (91), JapaneseEnvelopeYouNumber4Rotated (92), JapanesePostcard (43), JapanesePostcardRotated (81), Ledger (4), Legal (5), LegalExtra (51), Letter (1), LetterExtra (50), LetterExtraTransverse (56), LetterPlus (59), LetterRotated (75), LetterSmall (2), LetterTransverse (54), MonarchEnvelope (37), Note (18), Number10Envelope (20), Number11Envelope (21), Number12Envelope (22), Number14Envelope (23), Number9Envelope (19), PersonalEnvelope (38), Prc16K (93), Prc16KRotated (106), Prc32K (94), Prc32KBig (95), Prc32KBigRotated (108), Prc32KRotated (107), PrcEnvelopeNumber1 (96), PrcEnvelopeNumber10 (105), PrcEnvelopeNumber10Rotated (118), PrcEnvelopeNumber1Rotated (109), PrcEnvelopeNumber2 (97), PrcEnvelopeNumber2Rotated (110), PrcEnvelopeNumber3 (98), PrcEnvelopeNumber3Rotated (111), PrcEnvelopeNumber4 (99), PrcEnvelopeNumber4Rotated (112), PrcEnvelopeNumber5 (100), PrcEnvelopeNumber5Rotated (113), PrcEnvelopeNumber6 (101), PrcEnvelopeNumber6Rotated (114), PrcEnvelopeNumber7 (102), PrcEnvelopeNumber7Rotated (115), PrcEnvelopeNumber8 (103), PrcEnvelopeNumber8Rotated (116), PrcEnvelopeNumber9 (104), PrcEnvelopeNumber9Rotated (117), Quarto (15), Standard10x11 (45), Standard10x14 (16), Standard11x17 (17), Standard12x11 (90), Standard15x11 (46), Standard9x11 (44), Statement (6), Tabloid (3), TabloidExtra (52), USStandardFanfold (39)
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

    A2 = None
    A3 = None
    A3Extra = None
    A3ExtraTransverse = None
    A3Rotated = None
    A3Transverse = None
    A4 = None
    A4Extra = None
    A4Plus = None
    A4Rotated = None
    A4Small = None
    A4Transverse = None
    A5 = None
    A5Extra = None
    A5Rotated = None
    A5Transverse = None
    A6 = None
    A6Rotated = None
    APlus = None
    B4 = None
    B4Envelope = None
    B4JisRotated = None
    B5 = None
    B5Envelope = None
    B5Extra = None
    B5JisRotated = None
    B5Transverse = None
    B6Envelope = None
    B6Jis = None
    B6JisRotated = None
    BPlus = None
    C3Envelope = None
    C4Envelope = None
    C5Envelope = None
    C65Envelope = None
    C6Envelope = None
    CSheet = None
    Custom = None
    DLEnvelope = None
    DSheet = None
    ESheet = None
    Executive = None
    Folio = None
    GermanLegalFanfold = None
    GermanStandardFanfold = None
    InviteEnvelope = None
    IsoB4 = None
    ItalyEnvelope = None
    JapaneseDoublePostcard = None
    JapaneseDoublePostcardRotated = None
    JapaneseEnvelopeChouNumber3 = None
    JapaneseEnvelopeChouNumber3Rotated = None
    JapaneseEnvelopeChouNumber4 = None
    JapaneseEnvelopeChouNumber4Rotated = None
    JapaneseEnvelopeKakuNumber2 = None
    JapaneseEnvelopeKakuNumber2Rotated = None
    JapaneseEnvelopeKakuNumber3 = None
    JapaneseEnvelopeKakuNumber3Rotated = None
    JapaneseEnvelopeYouNumber4 = None
    JapaneseEnvelopeYouNumber4Rotated = None
    JapanesePostcard = None
    JapanesePostcardRotated = None
    Ledger = None
    Legal = None
    LegalExtra = None
    Letter = None
    LetterExtra = None
    LetterExtraTransverse = None
    LetterPlus = None
    LetterRotated = None
    LetterSmall = None
    LetterTransverse = None
    MonarchEnvelope = None
    Note = None
    Number10Envelope = None
    Number11Envelope = None
    Number12Envelope = None
    Number14Envelope = None
    Number9Envelope = None
    PersonalEnvelope = None
    Prc16K = None
    Prc16KRotated = None
    Prc32K = None
    Prc32KBig = None
    Prc32KBigRotated = None
    Prc32KRotated = None
    PrcEnvelopeNumber1 = None
    PrcEnvelopeNumber10 = None
    PrcEnvelopeNumber10Rotated = None
    PrcEnvelopeNumber1Rotated = None
    PrcEnvelopeNumber2 = None
    PrcEnvelopeNumber2Rotated = None
    PrcEnvelopeNumber3 = None
    PrcEnvelopeNumber3Rotated = None
    PrcEnvelopeNumber4 = None
    PrcEnvelopeNumber4Rotated = None
    PrcEnvelopeNumber5 = None
    PrcEnvelopeNumber5Rotated = None
    PrcEnvelopeNumber6 = None
    PrcEnvelopeNumber6Rotated = None
    PrcEnvelopeNumber7 = None
    PrcEnvelopeNumber7Rotated = None
    PrcEnvelopeNumber8 = None
    PrcEnvelopeNumber8Rotated = None
    PrcEnvelopeNumber9 = None
    PrcEnvelopeNumber9Rotated = None
    Quarto = None
    Standard10x11 = None
    Standard10x14 = None
    Standard11x17 = None
    Standard12x11 = None
    Standard15x11 = None
    Standard9x11 = None
    Statement = None
    Tabloid = None
    TabloidExtra = None
    USStandardFanfold = None
    value__ = None


class PaperSize(object):
    """
    Specifies the size of a piece of paper.
    
    PaperSize()
    PaperSize(name: str, width: int, height: int)
    """
    def ToString(self):
        """
        ToString(self: PaperSize) -> str
        
            Provides information about the System.Drawing.Printing.PaperSize in string form.
            Returns: A string.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name=None, width=None, height=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str, width: int, height: int)
        """
        pass

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height of the paper, in hundredths of an inch.

Get: Height(self: PaperSize) -> int

Set: Height(self: PaperSize) = value
"""

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of paper.

Get: Kind(self: PaperSize) -> PaperKind

"""

    PaperName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the type of paper.

Get: PaperName(self: PaperSize) -> str

Set: PaperName(self: PaperSize) = value
"""

    RawKind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an integer representing one of the System.Drawing.Printing.PaperSize values or a custom value.

Get: RawKind(self: PaperSize) -> int

Set: RawKind(self: PaperSize) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the width of the paper, in hundredths of an inch.

Get: Width(self: PaperSize) -> int

Set: Width(self: PaperSize) = value
"""



class PaperSource(object):
    """
    Specifies the paper tray from which the printer gets paper.
    
    PaperSource()
    """
    def ToString(self):
        """
        ToString(self: PaperSource) -> str
        
            Provides information about the System.Drawing.Printing.PaperSource in string form.
            Returns: A string.
        """
        pass

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the paper source.

Get: Kind(self: PaperSource) -> PaperSourceKind

"""

    RawKind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the integer representing one of the System.Drawing.Printing.PaperSourceKind values or a custom value.

Get: RawKind(self: PaperSource) -> int

Set: RawKind(self: PaperSource) = value
"""

    SourceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the paper source.

Get: SourceName(self: PaperSource) -> str

Set: SourceName(self: PaperSource) = value
"""



class PaperSourceKind(Enum, IComparable, IFormattable, IConvertible):
    """
    Standard paper sources.
    
    enum PaperSourceKind, values: AutomaticFeed (7), Cassette (14), Custom (257), Envelope (5), FormSource (15), LargeCapacity (11), LargeFormat (10), Lower (2), Manual (4), ManualFeed (6), Middle (3), SmallFormat (9), TractorFeed (8), Upper (1)
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

    AutomaticFeed = None
    Cassette = None
    Custom = None
    Envelope = None
    FormSource = None
    LargeCapacity = None
    LargeFormat = None
    Lower = None
    Manual = None
    ManualFeed = None
    Middle = None
    SmallFormat = None
    TractorFeed = None
    Upper = None
    value__ = None


class PreviewPageInfo(object):
    """
    Specifies print preview information for a single page. This class cannot be inherited.
    
    PreviewPageInfo(image: Image, physicalSize: Size)
    """
    @staticmethod # known case of __new__
    def __new__(self, image, physicalSize):
        """ __new__(cls: type, image: Image, physicalSize: Size) """
        pass

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the image of the printed page.

Get: Image(self: PreviewPageInfo) -> Image

"""

    PhysicalSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the printed page, in hundredths of an inch.

Get: PhysicalSize(self: PreviewPageInfo) -> Size

"""



class PrintController(object):
    """ Controls how a document is printed, when printing from a Windows Forms application. """
    def OnEndPage(self, document, e):
        """
        OnEndPage(self: PrintController, document: PrintDocument, e: PrintPageEventArgs)
            When overridden in a derived class, completes the control sequence that determines when and how 
             to print a page of a document.
        
        
            document: A System.Drawing.Printing.PrintDocument that represents the document currently being printed.
            e: A System.Drawing.Printing.PrintPageEventArgs that contains the event data.
        """
        pass

    def OnEndPrint(self, document, e):
        """
        OnEndPrint(self: PrintController, document: PrintDocument, e: PrintEventArgs)
            When overridden in a derived class, completes the control sequence that determines when and how 
             to print a document.
        
        
            document: A System.Drawing.Printing.PrintDocument that represents the document currently being printed.
            e: A System.Drawing.Printing.PrintEventArgs that contains the event data.
        """
        pass

    def OnStartPage(self, document, e):
        """
        OnStartPage(self: PrintController, document: PrintDocument, e: PrintPageEventArgs) -> Graphics
        
            When overridden in a derived class, begins the control sequence that determines when and how to 
             print a page of a document.
        
        
            document: A System.Drawing.Printing.PrintDocument that represents the document currently being printed.
            e: A System.Drawing.Printing.PrintPageEventArgs that contains the event data.
            Returns: A System.Drawing.Graphics that represents a page from a System.Drawing.Printing.PrintDocument.
        """
        pass

    def OnStartPrint(self, document, e):
        """
        OnStartPrint(self: PrintController, document: PrintDocument, e: PrintEventArgs)
            When overridden in a derived class, begins the control sequence that determines when and how to 
             print a document.
        
        
            document: A System.Drawing.Printing.PrintDocument that represents the document currently being printed.
            e: A System.Drawing.Printing.PrintEventArgs that contains the event data.
        """
        pass

    IsPreview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Drawing.Printing.PrintController is used for print preview.

Get: IsPreview(self: PrintController) -> bool

"""



class PreviewPrintController(PrintController):
    """
    Specifies a print controller that displays a document on a screen as a series of images.
    
    PreviewPrintController()
    """
    def GetPreviewPageInfo(self):
        """
        GetPreviewPageInfo(self: PreviewPrintController) -> Array[PreviewPageInfo]
        
            Captures the pages of a document as a series of images.
            Returns: An array of type System.Drawing.Printing.PreviewPageInfo that contains the pages of a 
             System.Drawing.Printing.PrintDocument as a series of images.
        """
        pass

    def OnEndPage(self, document, e):
        """
        OnEndPage(self: PreviewPrintController, document: PrintDocument, e: PrintPageEventArgs)
            Completes the control sequence that determines when and how to preview a page in a print 
             document.
        
        
            document: A System.Drawing.Printing.PrintDocument that represents the document being previewed.
            e: A System.Drawing.Printing.PrintPageEventArgs that contains data about how to preview a page in 
             the print document.
        """
        pass

    def OnEndPrint(self, document, e):
        """
        OnEndPrint(self: PreviewPrintController, document: PrintDocument, e: PrintEventArgs)
            Completes the control sequence that determines when and how to preview a print document.
        
            document: A System.Drawing.Printing.PrintDocument that represents the document being previewed.
            e: A System.Drawing.Printing.PrintEventArgs that contains data about how to preview the print 
             document.
        """
        pass

    def OnStartPage(self, document, e):
        """
        OnStartPage(self: PreviewPrintController, document: PrintDocument, e: PrintPageEventArgs) -> Graphics
        
            Begins the control sequence that determines when and how to preview a page in a print document.
        
            document: A System.Drawing.Printing.PrintDocument that represents the document being previewed.
            e: A System.Drawing.Printing.PrintPageEventArgs that contains data about how to preview a page in 
             the print document. Initially, the System.Drawing.Printing.PrintPageEventArgs.Graphics property 
             of this parameter will be null. The value returned from this method will be used to set this 
             property.
        
            Returns: A System.Drawing.Graphics that represents a page from a System.Drawing.Printing.PrintDocument.
        """
        pass

    def OnStartPrint(self, document, e):
        """
        OnStartPrint(self: PreviewPrintController, document: PrintDocument, e: PrintEventArgs)
            Begins the control sequence that determines when and how to preview a print document.
        
            document: A System.Drawing.Printing.PrintDocument that represents the document being previewed.
            e: A System.Drawing.Printing.PrintEventArgs that contains data about how to print the document.
        """
        pass

    IsPreview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this controller is used for print preview.

Get: IsPreview(self: PreviewPrintController) -> bool

"""

    UseAntiAlias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to use anti-aliasing when displaying the print preview.

Get: UseAntiAlias(self: PreviewPrintController) -> bool

Set: UseAntiAlias(self: PreviewPrintController) = value
"""



class PrintAction(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of print operation occurring.
    
    enum PrintAction, values: PrintToFile (0), PrintToPreview (1), PrintToPrinter (2)
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

    PrintToFile = None
    PrintToPreview = None
    PrintToPrinter = None
    value__ = None


class PrintDocument(Component, IComponent, IDisposable):
    """
    Defines a reusable object that sends output to a printer, when printing from a Windows Forms application.
    
    PrintDocument()
    """
    def Dispose(self):
        """
        Dispose(self: Component, disposing: bool)
            Releases the unmanaged resources used by the System.ComponentModel.Component and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def OnBeginPrint(self, *args): #cannot find CLR method
        """
        OnBeginPrint(self: PrintDocument, e: PrintEventArgs)
            Raises the System.Drawing.Printing.PrintDocument.BeginPrint event. It is called after the 
             System.Drawing.Printing.PrintDocument.Print method is called and before the first page of the 
             document prints.
        
        
            e: A System.Drawing.Printing.PrintEventArgs that contains the event data.
        """
        pass

    def OnEndPrint(self, *args): #cannot find CLR method
        """
        OnEndPrint(self: PrintDocument, e: PrintEventArgs)
            Raises the System.Drawing.Printing.PrintDocument.EndPrint event. It is called when the last page 
             of the document has printed.
        
        
            e: A System.Drawing.Printing.PrintEventArgs that contains the event data.
        """
        pass

    def OnPrintPage(self, *args): #cannot find CLR method
        """
        OnPrintPage(self: PrintDocument, e: PrintPageEventArgs)
            Raises the System.Drawing.Printing.PrintDocument.PrintPage event. It is called before a page 
             prints.
        
        
            e: A System.Drawing.Printing.PrintPageEventArgs that contains the event data.
        """
        pass

    def OnQueryPageSettings(self, *args): #cannot find CLR method
        """
        OnQueryPageSettings(self: PrintDocument, e: QueryPageSettingsEventArgs)
            Raises the System.Drawing.Printing.PrintDocument.QueryPageSettings event. It is called 
             immediately before each System.Drawing.Printing.PrintDocument.PrintPage event.
        
        
            e: A System.Drawing.Printing.QueryPageSettingsEventArgs that contains the event data.
        """
        pass

    def Print(self):
        """
        Print(self: PrintDocument)
            Starts the document's printing process.
        """
        pass

    def ToString(self):
        """
        ToString(self: PrintDocument) -> str
        
            Provides information about the print document, in string form.
            Returns: A string.
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

    def __str__(self, *args): #cannot find CLR method
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    DefaultPageSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets page settings that are used as defaults for all pages to be printed.

Get: DefaultPageSettings(self: PrintDocument) -> PageSettings

Set: DefaultPageSettings(self: PrintDocument) = value
"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    DocumentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the document name to display (for example, in a print status dialog box or printer queue) while printing the document.

Get: DocumentName(self: PrintDocument) -> str

Set: DocumentName(self: PrintDocument) = value
"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    OriginAtMargins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the position of a graphics object associated with a page is located just inside the user-specified margins or at the top-left corner of the printable area of the page.

Get: OriginAtMargins(self: PrintDocument) -> bool

Set: OriginAtMargins(self: PrintDocument) = value
"""

    PrintController = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the print controller that guides the printing process.

Get: PrintController(self: PrintDocument) -> PrintController

Set: PrintController(self: PrintDocument) = value
"""

    PrinterSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the printer that prints the document.

Get: PrinterSettings(self: PrintDocument) -> PrinterSettings

Set: PrinterSettings(self: PrintDocument) = value
"""


    BeginPrint = None
    EndPrint = None
    PrintPage = None
    QueryPageSettings = None


class PrinterResolution(object):
    """
    Represents the resolution supported by a printer.
    
    PrinterResolution()
    """
    def ToString(self):
        """
        ToString(self: PrinterResolution) -> str
        
            This member overrides the System.Object.ToString method.
            Returns: A System.String that contains information about the System.Drawing.Printing.PrinterResolution.
        """
        pass

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the printer resolution.

Get: Kind(self: PrinterResolution) -> PrinterResolutionKind

Set: Kind(self: PrinterResolution) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the horizontal printer resolution, in dots per inch.

Get: X(self: PrinterResolution) -> int

Set: X(self: PrinterResolution) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the vertical printer resolution, in dots per inch.

Get: Y(self: PrinterResolution) -> int

Set: Y(self: PrinterResolution) = value
"""



class PrinterResolutionKind(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies a printer resolution.
    
    enum PrinterResolutionKind, values: Custom (0), Draft (-1), High (-4), Low (-2), Medium (-3)
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

    Custom = None
    Draft = None
    High = None
    Low = None
    Medium = None
    value__ = None


class PrinterSettings(object, ICloneable):
    """
    Specifies information about how a document is printed, including the printer that prints it, when printing from a Windows Forms application.
    
    PrinterSettings()
    """
    def Clone(self):
        """
        Clone(self: PrinterSettings) -> object
        
            Creates a copy of this System.Drawing.Printing.PrinterSettings.
            Returns: A copy of this object.
        """
        pass

    def CreateMeasurementGraphics(self, *__args):
        """
        CreateMeasurementGraphics(self: PrinterSettings, pageSettings: PageSettings) -> Graphics
        
            Returns a System.Drawing.Graphics that contains printer information associated with the 
             specified System.Drawing.Printing.PageSettings.
        
        
            pageSettings: The System.Drawing.Printing.PageSettings to retrieve a graphics object for.
            Returns: A System.Drawing.Graphics that contains printer information from the 
             System.Drawing.Printing.PageSettings.
        
        CreateMeasurementGraphics(self: PrinterSettings, pageSettings: PageSettings, honorOriginAtMargins: bool) -> Graphics
        
            Creates a System.Drawing.Graphics associated with the specified page settings and optionally 
             specifying the origin at the margins.
        
        
            pageSettings: The System.Drawing.Printing.PageSettings to retrieve a System.Drawing.Graphics object for.
            honorOriginAtMargins: true to specify the origin at the margins; otherwise, false.
            Returns: A System.Drawing.Graphics that contains printer information from the 
             System.Drawing.Printing.PageSettings.
        
        CreateMeasurementGraphics(self: PrinterSettings) -> Graphics
        
            Returns a System.Drawing.Graphics that contains printer information that is useful when creating 
             a System.Drawing.Printing.PrintDocument.
        
            Returns: A System.Drawing.Graphics that contains information from a printer.
        CreateMeasurementGraphics(self: PrinterSettings, honorOriginAtMargins: bool) -> Graphics
        
            Returns a System.Drawing.Graphics that contains printer information, optionally specifying the 
             origin at the margins.
        
        
            honorOriginAtMargins: true to indicate the origin at the margins; otherwise, false.
            Returns: A System.Drawing.Graphics that contains printer information from the 
             System.Drawing.Printing.PageSettings.
        """
        pass

    def GetHdevmode(self, pageSettings=None):
        """
        GetHdevmode(self: PrinterSettings, pageSettings: PageSettings) -> IntPtr
        
            Creates a handle to a DEVMODE structure that corresponds to the printer and the page settings 
             specified through the pageSettings parameter.
        
        
            pageSettings: The System.Drawing.Printing.PageSettings object that the DEVMODE structure's handle corresponds 
             to.
        
            Returns: A handle to a DEVMODE structure.
        GetHdevmode(self: PrinterSettings) -> IntPtr
        
            Creates a handle to a DEVMODE structure that corresponds to the printer settings.
            Returns: A handle to a DEVMODE structure.
        """
        pass

    def GetHdevnames(self):
        """
        GetHdevnames(self: PrinterSettings) -> IntPtr
        
            Creates a handle to a DEVNAMES structure that corresponds to the printer settings.
            Returns: A handle to a DEVNAMES structure.
        """
        pass

    def IsDirectPrintingSupported(self, *__args):
        """
        IsDirectPrintingSupported(self: PrinterSettings, image: Image) -> bool
        
            Gets a value indicating whether the printer supports printing the specified image file.
        
            image: The image to print.
            Returns: true if the printer supports printing the specified image; otherwise, false.
        IsDirectPrintingSupported(self: PrinterSettings, imageFormat: ImageFormat) -> bool
        
            Returns a value indicating whether the printer supports printing the specified image format.
        
            imageFormat: An System.Drawing.Imaging.ImageFormat to print.
            Returns: true if the printer supports printing the specified image format; otherwise, false.
        """
        pass

    def SetHdevmode(self, hdevmode):
        """
        SetHdevmode(self: PrinterSettings, hdevmode: IntPtr)
            Copies the relevant information out of the given handle and into the 
             System.Drawing.Printing.PrinterSettings.
        
        
            hdevmode: The handle to a Win32 DEVMODE structure.
        """
        pass

    def SetHdevnames(self, hdevnames):
        """
        SetHdevnames(self: PrinterSettings, hdevnames: IntPtr)
            Copies the relevant information out of the given handle and into the 
             System.Drawing.Printing.PrinterSettings.
        
        
            hdevnames: The handle to a Win32 DEVNAMES structure.
        """
        pass

    def ToString(self):
        """
        ToString(self: PrinterSettings) -> str
        
            Provides information about the System.Drawing.Printing.PrinterSettings in string form.
            Returns: A string.
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

    def __str__(self, *args): #cannot find CLR method
        pass

    CanDuplex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the printer supports double-sided printing.

Get: CanDuplex(self: PrinterSettings) -> bool

"""

    Collate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the printed document is collated.

Get: Collate(self: PrinterSettings) -> bool

Set: Collate(self: PrinterSettings) = value
"""

    Copies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of copies of the document to print.

Get: Copies(self: PrinterSettings) -> Int16

Set: Copies(self: PrinterSettings) = value
"""

    DefaultPageSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default page settings for this printer.

Get: DefaultPageSettings(self: PrinterSettings) -> PageSettings

"""

    Duplex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the printer setting for double-sided printing.

Get: Duplex(self: PrinterSettings) -> Duplex

Set: Duplex(self: PrinterSettings) = value
"""

    FromPage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the page number of the first page to print.

Get: FromPage(self: PrinterSettings) -> int

Set: FromPage(self: PrinterSettings) = value
"""

    IsDefaultPrinter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Drawing.Printing.PrinterSettings.PrinterName property designates the default printer, except when the user explicitly sets System.Drawing.Printing.PrinterSettings.PrinterName.

Get: IsDefaultPrinter(self: PrinterSettings) -> bool

"""

    IsPlotter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the printer is a plotter.

Get: IsPlotter(self: PrinterSettings) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Drawing.Printing.PrinterSettings.PrinterName property designates a valid printer.

Get: IsValid(self: PrinterSettings) -> bool

"""

    LandscapeAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the angle, in degrees, that the portrait orientation is rotated to produce the landscape orientation.

Get: LandscapeAngle(self: PrinterSettings) -> int

"""

    MaximumCopies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum number of copies that the printer enables the user to print at a time.

Get: MaximumCopies(self: PrinterSettings) -> int

"""

    MaximumPage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum System.Drawing.Printing.PrinterSettings.FromPage or System.Drawing.Printing.PrinterSettings.ToPage that can be selected in a System.Windows.Forms.PrintDialog.

Get: MaximumPage(self: PrinterSettings) -> int

Set: MaximumPage(self: PrinterSettings) = value
"""

    MinimumPage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the minimum System.Drawing.Printing.PrinterSettings.FromPage or System.Drawing.Printing.PrinterSettings.ToPage that can be selected in a System.Windows.Forms.PrintDialog.

Get: MinimumPage(self: PrinterSettings) -> int

Set: MinimumPage(self: PrinterSettings) = value
"""

    PaperSizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the paper sizes that are supported by this printer.

Get: PaperSizes(self: PrinterSettings) -> PaperSizeCollection

"""

    PaperSources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the paper source trays that are available on the printer.

Get: PaperSources(self: PrinterSettings) -> PaperSourceCollection

"""

    PrinterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the printer to use.

Get: PrinterName(self: PrinterSettings) -> str

Set: PrinterName(self: PrinterSettings) = value
"""

    PrinterResolutions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all the resolutions that are supported by this printer.

Get: PrinterResolutions(self: PrinterSettings) -> PrinterResolutionCollection

"""

    PrintFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the file name, when printing to a file.

Get: PrintFileName(self: PrinterSettings) -> str

Set: PrintFileName(self: PrinterSettings) = value
"""

    PrintRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the page numbers that the user has specified to be printed.

Get: PrintRange(self: PrinterSettings) -> PrintRange

Set: PrintRange(self: PrinterSettings) = value
"""

    PrintToFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the printing output is sent to a file instead of a port.

Get: PrintToFile(self: PrinterSettings) -> bool

Set: PrintToFile(self: PrinterSettings) = value
"""

    SupportsColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this printer supports color printing.

Get: SupportsColor(self: PrinterSettings) -> bool

"""

    ToPage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of the last page to print.

Get: ToPage(self: PrinterSettings) -> int

Set: ToPage(self: PrinterSettings) = value
"""


    InstalledPrinters = None
    PaperSizeCollection = None
    PaperSourceCollection = None
    PrinterResolutionCollection = None
    StringCollection = None


class PrinterUnit(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies several of the units of measure used for printing.
    
    enum PrinterUnit, values: Display (0), HundredthsOfAMillimeter (2), TenthsOfAMillimeter (3), ThousandthsOfAnInch (1)
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

    Display = None
    HundredthsOfAMillimeter = None
    TenthsOfAMillimeter = None
    ThousandthsOfAnInch = None
    value__ = None


class PrinterUnitConvert(object):
    """ Specifies a series of conversion methods that are useful when interoperating with the Win32 printing API. This class cannot be inherited. """
    @staticmethod
    def Convert(value, fromUnit, toUnit):
        """
        Convert(value: Size, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> Size
        
            Converts a System.Drawing.Size from one System.Drawing.Printing.PrinterUnit type to another 
             System.Drawing.Printing.PrinterUnit type.
        
        
            value: The System.Drawing.Size being converted.
            fromUnit: The unit to convert from.
            toUnit: The unit to convert to.
            Returns: A System.Drawing.Size that represents the converted System.Drawing.Printing.PrinterUnit.
        Convert(value: Rectangle, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> Rectangle
        
            Converts a System.Drawing.Rectangle from one System.Drawing.Printing.PrinterUnit type to another 
             System.Drawing.Printing.PrinterUnit type.
        
        
            value: The System.Drawing.Rectangle being converted.
            fromUnit: The unit to convert from.
            toUnit: The unit to convert to.
            Returns: A System.Drawing.Rectangle that represents the converted System.Drawing.Printing.PrinterUnit.
        Convert(value: Margins, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> Margins
        
            Converts a System.Drawing.Printing.Margins from one System.Drawing.Printing.PrinterUnit type to 
             another System.Drawing.Printing.PrinterUnit type.
        
        
            value: The System.Drawing.Printing.Margins being converted.
            fromUnit: The unit to convert from.
            toUnit: The unit to convert to.
            Returns: A System.Drawing.Printing.Margins that represents the converted 
             System.Drawing.Printing.PrinterUnit.
        
        Convert(value: float, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> float
        
            Converts a double-precision floating-point number from one System.Drawing.Printing.PrinterUnit 
             type to another System.Drawing.Printing.PrinterUnit type.
        
        
            value: The System.Drawing.Point being converted.
            fromUnit: The unit to convert from.
            toUnit: The unit to convert to.
            Returns: A double-precision floating-point number that represents the converted 
             System.Drawing.Printing.PrinterUnit.
        
        Convert(value: int, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> int
        
            Converts a 32-bit signed integer from one System.Drawing.Printing.PrinterUnit type to another 
             System.Drawing.Printing.PrinterUnit type.
        
        
            value: The value being converted.
            fromUnit: The unit to convert from.
            toUnit: The unit to convert to.
            Returns: A 32-bit signed integer that represents the converted System.Drawing.Printing.PrinterUnit.
        Convert(value: Point, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> Point
        
            Converts a System.Drawing.Point from one System.Drawing.Printing.PrinterUnit type to another 
             System.Drawing.Printing.PrinterUnit type.
        
        
            value: The System.Drawing.Point being converted.
            fromUnit: The unit to convert from.
            toUnit: The unit to convert to.
            Returns: A System.Drawing.Point that represents the converted System.Drawing.Printing.PrinterUnit.
        """
        pass


class PrintEventArgs(CancelEventArgs):
    """
    Provides data for the System.Drawing.Printing.PrintDocument.BeginPrint and System.Drawing.Printing.PrintDocument.EndPrint events.
    
    PrintEventArgs()
    """
    PrintAction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns System.Drawing.Printing.PrintAction.PrintToFile in all cases.

Get: PrintAction(self: PrintEventArgs) -> PrintAction

"""



class PrintEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Drawing.Printing.PrintDocument.BeginPrint or System.Drawing.Printing.PrintDocument.EndPrint event of a System.Drawing.Printing.PrintDocument.
    
    PrintEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: PrintEventHandler, sender: object, e: PrintEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PrintEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PrintEventHandler, sender: object, e: PrintEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class PrintingPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    """
    Controls access to printers. This class cannot be inherited.
    
    PrintingPermission(state: PermissionState)
    PrintingPermission(printingLevel: PrintingPermissionLevel)
    """
    def Copy(self):
        """
        Copy(self: PrintingPermission) -> IPermission
        
            Creates and returns an identical copy of the current permission object.
            Returns: A copy of the current permission object.
        """
        pass

    def FromXml(self, esd):
        """
        FromXml(self: PrintingPermission, esd: SecurityElement)
            Reconstructs a security object with a specified state from an XML encoding.
        
            esd: The XML encoding to use to reconstruct the security object.
        """
        pass

    def Intersect(self, target):
        """
        Intersect(self: PrintingPermission, target: IPermission) -> IPermission
        
            Creates and returns a permission that is the intersection of the current permission object and a 
             target permission object.
        
        
            target: A permission object of the same type as the current permission object.
            Returns: A new permission object that represents the intersection of the current object and the specified 
             target. This object is null if the intersection is empty.
        """
        pass

    def IsSubsetOf(self, target):
        """
        IsSubsetOf(self: PrintingPermission, target: IPermission) -> bool
        
            Determines whether the current permission object is a subset of the specified permission.
        
            target: A permission object that is to be tested for the subset relationship. This object must be of the 
             same type as the current permission object.
        
            Returns: true if the current permission object is a subset of target; otherwise, false.
        """
        pass

    def IsUnrestricted(self):
        """
        IsUnrestricted(self: PrintingPermission) -> bool
        
            Gets a value indicating whether the permission is unrestricted.
            Returns: true if permission is unrestricted; otherwise, false.
        """
        pass

    def ToXml(self):
        """
        ToXml(self: PrintingPermission) -> SecurityElement
        
            Creates an XML encoding of the security object and its current state.
            Returns: An XML encoding of the security object, including any state information.
        """
        pass

    def Union(self, target):
        """
        Union(self: PrintingPermission, target: IPermission) -> IPermission
        
            Creates a permission that combines the permission object and the target permission object.
        
            target: A permission object of the same type as the current permission object.
            Returns: A new permission object that represents the union of the current permission object and the 
             specified permission object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, printingLevel: PrintingPermissionLevel)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the code's level of printing access.

Get: Level(self: PrintingPermission) -> PrintingPermissionLevel

Set: Level(self: PrintingPermission) = value
"""



class PrintingPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """
    Allows declarative printing permission checks.
    
    PrintingPermissionAttribute(action: SecurityAction)
    """
    def CreatePermission(self):
        """
        CreatePermission(self: PrintingPermissionAttribute) -> IPermission
        
            Creates the permission based on the requested access levels, which are set through the 
             System.Drawing.Printing.PrintingPermissionAttribute.Level property on the attribute.
        
            Returns: An System.Security.IPermission that represents the created permission.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, action):
        """ __new__(cls: type, action: SecurityAction) """
        pass

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of printing allowed.

Get: Level(self: PrintingPermissionAttribute) -> PrintingPermissionLevel

Set: Level(self: PrintingPermissionAttribute) = value
"""



class PrintingPermissionLevel(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of printing that code is allowed to do.
    
    enum PrintingPermissionLevel, values: AllPrinting (3), DefaultPrinting (2), NoPrinting (0), SafePrinting (1)
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

    AllPrinting = None
    DefaultPrinting = None
    NoPrinting = None
    SafePrinting = None
    value__ = None


class PrintPageEventArgs(EventArgs):
    """
    Provides data for the System.Drawing.Printing.PrintDocument.PrintPage event.
    
    PrintPageEventArgs(graphics: Graphics, marginBounds: Rectangle, pageBounds: Rectangle, pageSettings: PageSettings)
    """
    @staticmethod # known case of __new__
    def __new__(self, graphics, marginBounds, pageBounds, pageSettings):
        """ __new__(cls: type, graphics: Graphics, marginBounds: Rectangle, pageBounds: Rectangle, pageSettings: PageSettings) """
        pass

    Cancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the print job should be canceled.

Get: Cancel(self: PrintPageEventArgs) -> bool

Set: Cancel(self: PrintPageEventArgs) = value
"""

    Graphics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Drawing.Graphics used to paint the page.

Get: Graphics(self: PrintPageEventArgs) -> Graphics

"""

    HasMorePages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether an additional page should be printed.

Get: HasMorePages(self: PrintPageEventArgs) -> bool

Set: HasMorePages(self: PrintPageEventArgs) = value
"""

    MarginBounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rectangular area that represents the portion of the page inside the margins.

Get: MarginBounds(self: PrintPageEventArgs) -> Rectangle

"""

    PageBounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rectangular area that represents the total area of the page.

Get: PageBounds(self: PrintPageEventArgs) -> Rectangle

"""

    PageSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the page settings for the current page.

Get: PageSettings(self: PrintPageEventArgs) -> PageSettings

"""



class PrintPageEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Drawing.Printing.PrintDocument.PrintPage event of a System.Drawing.Printing.PrintDocument.
    
    PrintPageEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: PrintPageEventHandler, sender: object, e: PrintPageEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PrintPageEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PrintPageEventHandler, sender: object, e: PrintPageEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class PrintRange(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the part of the document to print.
    
    enum PrintRange, values: AllPages (0), CurrentPage (4194304), Selection (1), SomePages (2)
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

    AllPages = None
    CurrentPage = None
    Selection = None
    SomePages = None
    value__ = None


class QueryPageSettingsEventArgs(PrintEventArgs):
    """
    Provides data for the System.Drawing.Printing.PrintDocument.QueryPageSettings event.
    
    QueryPageSettingsEventArgs(pageSettings: PageSettings)
    """
    @staticmethod # known case of __new__
    def __new__(self, pageSettings):
        """ __new__(cls: type, pageSettings: PageSettings) """
        pass

    PageSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the page settings for the page to be printed.

Get: PageSettings(self: QueryPageSettingsEventArgs) -> PageSettings

Set: PageSettings(self: QueryPageSettingsEventArgs) = value
"""



class QueryPageSettingsEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that handles the System.Drawing.Printing.PrintDocument.QueryPageSettings event of a System.Drawing.Printing.PrintDocument.
    
    QueryPageSettingsEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: QueryPageSettingsEventHandler, sender: object, e: QueryPageSettingsEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: QueryPageSettingsEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: QueryPageSettingsEventHandler, sender: object, e: QueryPageSettingsEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class StandardPrintController(PrintController):
    """
    Specifies a print controller that sends information to a printer.
    
    StandardPrintController()
    """
    def OnEndPage(self, document, e):
        """
        OnEndPage(self: StandardPrintController, document: PrintDocument, e: PrintPageEventArgs)
            Completes the control sequence that determines when and how to print a page of a document.
        
            document: A System.Drawing.Printing.PrintDocument that represents the document being printed.
            e: A System.Drawing.Printing.PrintPageEventArgs that contains data about how to print a page in the 
             document.
        """
        pass

    def OnEndPrint(self, document, e):
        """
        OnEndPrint(self: StandardPrintController, document: PrintDocument, e: PrintEventArgs)
            Completes the control sequence that determines when and how to print a document.
        
            document: A System.Drawing.Printing.PrintDocument that represents the document being printed.
            e: A System.Drawing.Printing.PrintEventArgs that contains data about how to print the document.
        """
        pass

    def OnStartPage(self, document, e):
        """
        OnStartPage(self: StandardPrintController, document: PrintDocument, e: PrintPageEventArgs) -> Graphics
        
            Begins the control sequence that determines when and how to print a page in a document.
        
            document: A System.Drawing.Printing.PrintDocument that represents the document being printed.
            e: A System.Drawing.Printing.PrintPageEventArgs that contains data about how to print a page in the 
             document. Initially, the System.Drawing.Printing.PrintPageEventArgs.Graphics property of this 
             parameter will be null. The value returned from the 
             System.Drawing.Printing.StandardPrintController.OnStartPage(System.Drawing.Printing.PrintDocument
             ,System.Drawing.Printing.PrintPageEventArgs) method will be used to set this property.
        
            Returns: A System.Drawing.Graphics object that represents a page from a 
             System.Drawing.Printing.PrintDocument.
        """
        pass

    def OnStartPrint(self, document, e):
        """
        OnStartPrint(self: StandardPrintController, document: PrintDocument, e: PrintEventArgs)
            Begins the control sequence that determines when and how to print a document.
        
            document: A System.Drawing.Printing.PrintDocument that represents the document being printed.
            e: A System.Drawing.Printing.PrintEventArgs that contains data about how to print the document.
        """
        pass


