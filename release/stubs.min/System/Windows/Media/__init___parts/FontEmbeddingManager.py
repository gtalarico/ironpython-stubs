class FontEmbeddingManager(object):
 """
 Provides functionality for physical and composite font embedding.
 
 FontEmbeddingManager()
 """
 def GetUsedGlyphs(self,glyphTypeface):
  """
  GetUsedGlyphs(self: FontEmbeddingManager,glyphTypeface: Uri) -> ICollection[UInt16]
  
   Retrieves the list of glyphs used by the glyph typeface.
  
   glyphTypeface: A System.Uri value that represents the location of the glyph typeface 
    containing the glyphs.
  
   Returns: A collection of System.UInt16 values that represent the glyphs.
  """
  pass
 def RecordUsage(self,glyphRun):
  """
  RecordUsage(self: FontEmbeddingManager,glyphRun: GlyphRun)
   Initiates the collection of usage information about the glyph typeface and 
    indices used by a specified System.Windows.Media.GlyphRun.
  
  
   glyphRun: The System.Windows.Media.GlyphRun whose usage information is collected.
  """
  pass
 GlyphTypefaceUris=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the collection of glyph typefaces used by the System.Windows.Media.GlyphRun specified in the System.Windows.Media.FontEmbeddingManager.RecordUsage(System.Windows.Media.GlyphRun) method.

Get: GlyphTypefaceUris(self: FontEmbeddingManager) -> ICollection[Uri]

"""


