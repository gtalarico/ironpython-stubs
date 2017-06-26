class GlyphRun(object, IResource, ISupportInitialize):
    """
    Represents a sequence of glyphs from a single face of a single font at a single size, and with a single rendering style.
    
    GlyphRun()
    GlyphRun(pixelsPerDip: Single)
    GlyphRun(glyphTypeface: GlyphTypeface, bidiLevel: int, isSideways: bool, renderingEmSize: float, pixelsPerDip: Single, glyphIndices: IList[UInt16], baselineOrigin: Point, advanceWidths: IList[float], glyphOffsets: IList[Point], characters: IList[Char], deviceFontName: str, clusterMap: IList[UInt16], caretStops: IList[bool], language: XmlLanguage)
    GlyphRun(glyphTypeface: GlyphTypeface, bidiLevel: int, isSideways: bool, renderingEmSize: float, glyphIndices: IList[UInt16], baselineOrigin: Point, advanceWidths: IList[float], glyphOffsets: IList[Point], characters: IList[Char], deviceFontName: str, clusterMap: IList[UInt16], caretStops: IList[bool], language: XmlLanguage)
    """
    def BuildGeometry(self):
        """
        BuildGeometry(self: GlyphRun) -> Geometry
        
            Retrieves the System.Windows.Media.Geometry for the System.Windows.Media.GlyphRun.
            Returns: The System.Windows.Media.Geometry corresponding to the System.Windows.Media.GlyphRun.
        """
        pass

    def ComputeAlignmentBox(self):
        """
        ComputeAlignmentBox(self: GlyphRun) -> Rect
        
            Retrieves the alignment box for the System.Windows.Media.GlyphRun.
            Returns: A System.Windows.Rect that represents the alignment box for the System.Windows.Media.GlyphRun.
        """
        pass

    def ComputeInkBoundingBox(self):
        """
        ComputeInkBoundingBox(self: GlyphRun) -> Rect
        
            Retrieves the ink bounding box for the System.Windows.Media.GlyphRun.
            Returns: A System.Windows.Rect that represents the ink bounding box the System.Windows.Media.GlyphRun.
        """
        pass

    def GetCaretCharacterHitFromDistance(self, distance, isInside):
        """
        GetCaretCharacterHitFromDistance(self: GlyphRun, distance: float) -> (CharacterHit, bool)
        
            Retrieves the System.Windows.Media.TextFormatting.CharacterHit value that represents the character hit of the caret of the System.Windows.Media.GlyphRun.
        
            distance: Offset to use for computing the caret character hit.
            Returns: A System.Windows.Media.TextFormatting.CharacterHit value that represents the character hit that is closest to the distance value. The out parameter isInside returns true if the character hit is inside the 
             System.Windows.Media.GlyphRun; otherwise, false.
        """
        pass

    def GetDistanceFromCaretCharacterHit(self, characterHit):
        """
        GetDistanceFromCaretCharacterHit(self: GlyphRun, characterHit: CharacterHit) -> float
        
            Retrieves the offset from the leading edge of the System.Windows.Media.GlyphRun to the leading or trailing edge of a caret stop containing the specified character hit.
        
            characterHit: The System.Windows.Media.TextFormatting.CharacterHit to use for computing the offset.
            Returns: A System.Double that represents the offset from the leading edge of the System.Windows.Media.GlyphRun to the leading or trailing edge of a caret stop containing the character hit.
        """
        pass

    def GetNextCaretCharacterHit(self, characterHit):
        """
        GetNextCaretCharacterHit(self: GlyphRun, characterHit: CharacterHit) -> CharacterHit
        
            Retrieves the next valid caret character hit in the logical direction in the System.Windows.Media.GlyphRun.
        
            characterHit: The System.Windows.Media.TextFormatting.CharacterHit to use for computing the next hit value.
            Returns: A System.Windows.Media.TextFormatting.CharacterHit that represents the next valid caret character hit in the logical direction. If the return value is equal to characterHit, no further navigation is 
             possible in the System.Windows.Media.GlyphRun.
        """
        pass

    def GetPreviousCaretCharacterHit(self, characterHit):
        """
        GetPreviousCaretCharacterHit(self: GlyphRun, characterHit: CharacterHit) -> CharacterHit
        
            Retrieves the previous valid caret character hit in the logical direction in the System.Windows.Media.GlyphRun.
        
            characterHit: The System.Windows.Media.TextFormatting.CharacterHit to use for computing the previous hit value.
            Returns: A System.Windows.Media.TextFormatting.CharacterHit that represents the previous valid caret character hit in the logical direction. If the return value is equal to characterHit, no further navigation is 
             possible in the System.Windows.Media.GlyphRun.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, pixelsPerDip: Single)
        __new__(cls: type, glyphTypeface: GlyphTypeface, bidiLevel: int, isSideways: bool, renderingEmSize: float, pixelsPerDip: Single, glyphIndices: IList[UInt16], baselineOrigin: Point, advanceWidths: IList[float], glyphOffsets: IList[Point], characters: IList[Char], deviceFontName: str, clusterMap: IList[UInt16], caretStops: IList[bool], language: XmlLanguage)
        __new__(cls: type, glyphTypeface: GlyphTypeface, bidiLevel: int, isSideways: bool, renderingEmSize: float, glyphIndices: IList[UInt16], baselineOrigin: Point, advanceWidths: IList[float], glyphOffsets: IList[Point], characters: IList[Char], deviceFontName: str, clusterMap: IList[UInt16], caretStops: IList[bool], language: XmlLanguage)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AdvanceWidths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the list of System.Double values that represent the advance widths corresponding to the glyph indices.

Get: AdvanceWidths(self: GlyphRun) -> IList[float]

Set: AdvanceWidths(self: GlyphRun) = value
"""

    BaselineOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the baseline origin of the System.Windows.Media.GlyphRun.

Get: BaselineOrigin(self: GlyphRun) -> Point

Set: BaselineOrigin(self: GlyphRun) = value
"""

    BidiLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the bidirectional nesting level of the System.Windows.Media.GlyphRun.

Get: BidiLevel(self: GlyphRun) -> int

Set: BidiLevel(self: GlyphRun) = value
"""

    CaretStops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the list of System.Boolean values that determine whether there are caret stops for every UTF16 code point in the Unicode representing the System.Windows.Media.GlyphRun.

Get: CaretStops(self: GlyphRun) -> IList[bool]

Set: CaretStops(self: GlyphRun) = value
"""

    Characters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the list of UTF16 code points that represent the Unicode content of the System.Windows.Media.GlyphRun.

Get: Characters(self: GlyphRun) -> IList[Char]

Set: Characters(self: GlyphRun) = value
"""

    ClusterMap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the list of System.UInt16 values that maps characters in the System.Windows.Media.GlyphRun to glyph indices.

Get: ClusterMap(self: GlyphRun) -> IList[UInt16]

Set: ClusterMap(self: GlyphRun) = value
"""

    DeviceFontName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the specific device font for which the System.Windows.Media.GlyphRun has been optimized.

Get: DeviceFontName(self: GlyphRun) -> str

Set: DeviceFontName(self: GlyphRun) = value
"""

    FontRenderingEmSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the em size used for rendering the System.Windows.Media.GlyphRun.

Get: FontRenderingEmSize(self: GlyphRun) -> float

Set: FontRenderingEmSize(self: GlyphRun) = value
"""

    GlyphIndices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of System.UInt16 values that represent the glyph indices in the rendering physical font.

Get: GlyphIndices(self: GlyphRun) -> IList[UInt16]

Set: GlyphIndices(self: GlyphRun) = value
"""

    GlyphOffsets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of System.Windows.Point values representing the offsets of the glyphs in the System.Windows.Media.GlyphRun.

Get: GlyphOffsets(self: GlyphRun) -> IList[Point]

Set: GlyphOffsets(self: GlyphRun) = value
"""

    GlyphTypeface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.GlyphTypeface for the System.Windows.Media.GlyphRun.

Get: GlyphTypeface(self: GlyphRun) -> GlyphTypeface

Set: GlyphTypeface(self: GlyphRun) = value
"""

    IsHitTestable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether there are any valid caret character hits within the System.Windows.Media.GlyphRun.

Get: IsHitTestable(self: GlyphRun) -> bool

"""

    IsSideways = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to rotate glyphs.

Get: IsSideways(self: GlyphRun) -> bool

Set: IsSideways(self: GlyphRun) = value
"""

    Language = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Markup.XmlLanguage for the System.Windows.Media.GlyphRun.

Get: Language(self: GlyphRun) -> XmlLanguage

Set: Language(self: GlyphRun) = value
"""

    PixelsPerDip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PixelsPerDip(self: GlyphRun) -> Single

Set: PixelsPerDip(self: GlyphRun) = value
"""


