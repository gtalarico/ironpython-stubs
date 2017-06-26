class GlyphTypeface(object,ITypefaceMetrics,ISupportInitialize):
 """
 Specifies a physical font face that corresponds to a font file on the disk.
 
 GlyphTypeface()
 GlyphTypeface(typefaceSource: Uri)
 GlyphTypeface(typefaceSource: Uri,styleSimulations: StyleSimulations)
 """
 def ComputeSubset(self,glyphs):
  """ ComputeSubset(self: GlyphTypeface,glyphs: ICollection[UInt16]) -> Array[Byte] """
  pass
 def Equals(self,o):
  """
  Equals(self: GlyphTypeface,o: object) -> bool
  
   Determines whether the specified object is equal to the current 
    System.Windows.Media.GlyphTypeface object.
  
  
   o: The System.Object to compare with the current 
    System.Windows.Media.GlyphTypeface object.
  
   Returns: true if o is a System.Windows.Media.GlyphTypeface and is equal to the current 
    System.Windows.Media.GlyphTypeface; otherwise,false.
  """
  pass
 def GetFontStream(self):
  """
  GetFontStream(self: GlyphTypeface) -> Stream
  
   Returns the font file stream represented by the 
    System.Windows.Media.GlyphTypeface object.
  
   Returns: A System.IO.Stream value that represents the font file.
  """
  pass
 def GetGlyphOutline(self,glyphIndex,renderingEmSize,hintingEmSize):
  """
  GetGlyphOutline(self: GlyphTypeface,glyphIndex: UInt16,renderingEmSize: float,hintingEmSize: float) -> Geometry
  
   Returns a System.Windows.Media.Geometry value describing the path for a single 
    glyph in the font.
  
  
   glyphIndex: The index of the glyph to get the outline for.
   renderingEmSize: The font size in drawing surface units.
   hintingEmSize: The size to hint for in points.
   Returns: A System.Windows.Media.Geometry value that represents the path of the glyph.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: GlyphTypeface) -> int
  
   Serves as a hash function for System.Windows.Media.GlyphTypeface.
   Returns: A hash code for the current object.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,typefaceSource=None,styleSimulations=None):
  """
  __new__(cls: type)
  __new__(cls: type,typefaceSource: Uri)
  __new__(cls: type,typefaceSource: Uri,styleSimulations: StyleSimulations)
  """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 AdvanceHeights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the advance heights for the glyphs represented by the System.Windows.Media.GlyphTypeface object.

Get: AdvanceHeights(self: GlyphTypeface) -> IDictionary[UInt16,float]

"""

 AdvanceWidths=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the advance widths for the glyphs represented by the System.Windows.Media.GlyphTypeface object.

Get: AdvanceWidths(self: GlyphTypeface) -> IDictionary[UInt16,float]

"""

 Baseline=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the baseline value for the System.Windows.Media.GlyphTypeface.

Get: Baseline(self: GlyphTypeface) -> float

"""

 BottomSideBearings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the distance from bottom edge of the black box to the bottom end of the advance vector for the glyphs represented by the System.Windows.Media.GlyphTypeface object.

Get: BottomSideBearings(self: GlyphTypeface) -> IDictionary[UInt16,float]

"""

 CapsHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the distance from the baseline to the top of an English capital,relative to em size,for the System.Windows.Media.GlyphTypeface object.

Get: CapsHeight(self: GlyphTypeface) -> float

"""

 CharacterToGlyphMap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the nominal mapping of a Unicode code point to a glyph index as defined by the font 'CMAP' table.

Get: CharacterToGlyphMap(self: GlyphTypeface) -> IDictionary[int,UInt16]

"""

 Copyrights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the copyright information for the System.Windows.Media.GlyphTypeface object.

Get: Copyrights(self: GlyphTypeface) -> IDictionary[CultureInfo,str]

"""

 Descriptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the description information for the System.Windows.Media.GlyphTypeface object.

Get: Descriptions(self: GlyphTypeface) -> IDictionary[CultureInfo,str]

"""

 DesignerNames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the designer information for the System.Windows.Media.GlyphTypeface object.

Get: DesignerNames(self: GlyphTypeface) -> IDictionary[CultureInfo,str]

"""

 DesignerUrls=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the designer URL information for the System.Windows.Media.GlyphTypeface object.

Get: DesignerUrls(self: GlyphTypeface) -> IDictionary[CultureInfo,str]

"""

 DistancesFromHorizontalBaselineToBlackBoxBottom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the offset value from the horizontal Western baseline to the bottom of the glyph black box for the glyphs represented by the System.Windows.Media.GlyphTypeface object.

Get: DistancesFromHorizontalBaselineToBlackBoxBottom(self: GlyphTypeface) -> IDictionary[UInt16,float]

"""

 EmbeddingRights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the font embedding permission for the System.Windows.Media.GlyphTypeface object.

Get: EmbeddingRights(self: GlyphTypeface) -> FontEmbeddingRight

"""

 FaceNames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the face name for the System.Windows.Media.GlyphTypeface object.

Get: FaceNames(self: GlyphTypeface) -> IDictionary[CultureInfo,str]

"""

 FamilyNames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the family name for the System.Windows.Media.GlyphTypeface object.

Get: FamilyNames(self: GlyphTypeface) -> IDictionary[CultureInfo,str]

"""

 FontUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the URI�for the System.Windows.Media.GlyphTypeface�object.

Get: FontUri(self: GlyphTypeface) -> Uri

Set: FontUri(self: GlyphTypeface)=value
"""

 GlyphCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of glyphs for the System.Windows.Media.GlyphTypeface object.

Get: GlyphCount(self: GlyphTypeface) -> int

"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the height of the character cell relative to the em size.

Get: Height(self: GlyphTypeface) -> float

"""

 LeftSideBearings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the distance from the leading end of the advance vector to the left edge of the black box for the glyphs represented by the System.Windows.Media.GlyphTypeface object.

Get: LeftSideBearings(self: GlyphTypeface) -> IDictionary[UInt16,float]

"""

 LicenseDescriptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the font license description information for the System.Windows.Media.GlyphTypeface object.

Get: LicenseDescriptions(self: GlyphTypeface) -> IDictionary[CultureInfo,str]

"""

 ManufacturerNames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the font manufacturer information for the System.Windows.Media.GlyphTypeface object.

Get: ManufacturerNames(self: GlyphTypeface) -> IDictionary[CultureInfo,str]

"""

 RightSideBearings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the distance from the right edge of the black box to the right end of the advance vector for the glyphs represented by the System.Windows.Media.GlyphTypeface object.

Get: RightSideBearings(self: GlyphTypeface) -> IDictionary[UInt16,float]

"""

 SampleTexts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the sample text information for the System.Windows.Media.GlyphTypeface object.

Get: SampleTexts(self: GlyphTypeface) -> IDictionary[CultureInfo,str]

"""

 Stretch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.FontStretch value for the System.Windows.Media.GlyphTypeface object.

Get: Stretch(self: GlyphTypeface) -> FontStretch

"""

 StrikethroughPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates the distance from the baseline to the strikethrough for the typeface.

Get: StrikethroughPosition(self: GlyphTypeface) -> float

"""

 StrikethroughThickness=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates the thickness of the strikethrough relative to the font em size.

Get: StrikethroughThickness(self: GlyphTypeface) -> float

"""

 Style=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the style for the System.Windows.Media.GlyphTypeface object.

Get: Style(self: GlyphTypeface) -> FontStyle

"""

 StyleSimulations=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.StyleSimulations for the System.Windows.Media.GlyphTypeface object.

Get: StyleSimulations(self: GlyphTypeface) -> StyleSimulations

Set: StyleSimulations(self: GlyphTypeface)=value
"""

 Symbol=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.Windows.Media.GlyphTypeface font conforms to Unicode encoding.

Get: Symbol(self: GlyphTypeface) -> bool

"""

 TopSideBearings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the distance from the top end of the vertical advance vector to the top edge of the black box for the glyphs represented by the System.Windows.Media.GlyphTypeface object.

Get: TopSideBearings(self: GlyphTypeface) -> IDictionary[UInt16,float]

"""

 Trademarks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the trademark notice information for the System.Windows.Media.GlyphTypeface object.

Get: Trademarks(self: GlyphTypeface) -> IDictionary[CultureInfo,str]

"""

 UnderlinePosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the position of the underline in the System.Windows.Media.GlyphTypeface.

Get: UnderlinePosition(self: GlyphTypeface) -> float

"""

 UnderlineThickness=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the thickness of the underline relative to em size.

Get: UnderlineThickness(self: GlyphTypeface) -> float

"""

 VendorUrls=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the vendor URL information for the System.Windows.Media.GlyphTypeface object.

Get: VendorUrls(self: GlyphTypeface) -> IDictionary[CultureInfo,str]

"""

 Version=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the font face version interpreted from the font's 'NAME' table.

Get: Version(self: GlyphTypeface) -> float

"""

 VersionStrings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the version string information for the System.Windows.Media.GlyphTypeface object interpreted from the font's 'NAME' table.

Get: VersionStrings(self: GlyphTypeface) -> IDictionary[CultureInfo,str]

"""

 Weight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the designed weight of the font represented by the System.Windows.Media.GlyphTypeface object.

Get: Weight(self: GlyphTypeface) -> FontWeight

"""

 Win32FaceNames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Win32 face name for the font represented by the  System.Windows.Media.GlyphTypeface object.

Get: Win32FaceNames(self: GlyphTypeface) -> IDictionary[CultureInfo,str]

"""

 Win32FamilyNames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Win32 family name for the font represented by the  System.Windows.Media.GlyphTypeface object.

Get: Win32FamilyNames(self: GlyphTypeface) -> IDictionary[CultureInfo,str]

"""

 XHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Western x-height relative to em size for the font represented by the System.Windows.Media.GlyphTypeface object.

Get: XHeight(self: GlyphTypeface) -> float

"""


