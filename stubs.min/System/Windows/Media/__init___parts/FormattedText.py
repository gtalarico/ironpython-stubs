class FormattedText(object):
 """
 Provides low-level control for drawing text in Windows Presentation Foundation (WPF) applications.
 
 FormattedText(textToFormat: str,culture: CultureInfo,flowDirection: FlowDirection,typeface: Typeface,emSize: float,foreground: Brush)
 FormattedText(textToFormat: str,culture: CultureInfo,flowDirection: FlowDirection,typeface: Typeface,emSize: float,foreground: Brush,pixelsPerDip: float)
 FormattedText(textToFormat: str,culture: CultureInfo,flowDirection: FlowDirection,typeface: Typeface,emSize: float,foreground: Brush,numberSubstitution: NumberSubstitution)
 FormattedText(textToFormat: str,culture: CultureInfo,flowDirection: FlowDirection,typeface: Typeface,emSize: float,foreground: Brush,numberSubstitution: NumberSubstitution,pixelsPerDip: float)
 FormattedText(textToFormat: str,culture: CultureInfo,flowDirection: FlowDirection,typeface: Typeface,emSize: float,foreground: Brush,numberSubstitution: NumberSubstitution,textFormattingMode: TextFormattingMode)
 FormattedText(textToFormat: str,culture: CultureInfo,flowDirection: FlowDirection,typeface: Typeface,emSize: float,foreground: Brush,numberSubstitution: NumberSubstitution,textFormattingMode: TextFormattingMode,pixelsPerDip: float)
 """
 def BuildGeometry(self,origin):
  """
  BuildGeometry(self: FormattedText,origin: Point) -> Geometry
  
   Returns a System.Windows.Media.Geometry object that represents the formatted 
    text,including all glyphs and text decorations.
  
  
   origin: The top-left origin of the resulting geometry.
   Returns: The System.Windows.Media.Geometry object representation of the formatted text.
  """
  pass
 def BuildHighlightGeometry(self,origin,startIndex=None,count=None):
  """
  BuildHighlightGeometry(self: FormattedText,origin: Point,startIndex: int,count: int) -> Geometry
  
   Returns a System.Windows.Media.Geometry object that represents the highlight 
    bounding box for a specified substring of the formatted text.
  
  
   origin: The origin of the highlight region.
   startIndex: The index of the initial character the highlight bounds should be obtained for.
   count: The number of characters the highlight bounds should contain.
   Returns: The System.Windows.Media.Geometry object that represents the highlight bounding 
    box of the formatted text substring.
  
  BuildHighlightGeometry(self: FormattedText,origin: Point) -> Geometry
  
   Returns a System.Windows.Media.Geometry object that represents the highlight 
    bounding box of the formatted text.
  
  
   origin: The origin of the highlight region.
   Returns: The System.Windows.Media.Geometry object that represents the highlight bounding 
    box of the formatted text.
  """
  pass
 def GetMaxTextWidths(self):
  """
  GetMaxTextWidths(self: FormattedText) -> Array[float]
  
   Retrieves an array of text widths. Each element in the array represents the 
    maximum text width of sequential lines of text.
  
   Returns: An array of maximum text widths,each width provided in device-independent 
    units (1/96th inch per unit).
  """
  pass
 def SetCulture(self,culture,startIndex=None,count=None):
  """
  SetCulture(self: FormattedText,culture: CultureInfo,startIndex: int,count: int)
   Sets the System.Globalization.CultureInfo for a specified subset of characters 
    in the System.Windows.Media.FormattedText object.
  
  
   culture: The System.Globalization.CultureInfo to use for text formatting.
   startIndex: The start index of initial character to apply the change to.
   count: The number of characters the change should be applied to.
  SetCulture(self: FormattedText,culture: CultureInfo)
   Sets the System.Globalization.CultureInfo for the entire set of characters in 
    the System.Windows.Media.FormattedText object.
  
  
   culture: The System.Globalization.CultureInfo to use for text formatting.
  """
  pass
 def SetFontFamily(self,fontFamily,startIndex=None,count=None):
  """
  SetFontFamily(self: FormattedText,fontFamily: FontFamily)
   Sets the font family for a System.Windows.Media.FormattedText object.
  
   fontFamily: The System.Windows.Media.FontFamily to use for text formatting.
  SetFontFamily(self: FormattedText,fontFamily: FontFamily,startIndex: int,count: int)
   Sets the font family for a specified subset of characters in the 
    System.Windows.Media.FormattedText object.
  
  
   fontFamily: The System.Windows.Media.FontFamily to use for text formatting.
   startIndex: The starting index of the initial character to apply the font family change to.
   count: The number of characters the change should apply to.
  SetFontFamily(self: FormattedText,fontFamily: str)
   Sets the font family for the entire set of characters in the 
    System.Windows.Media.FormattedText object.
  
  
   fontFamily: A string that constructs the System.Windows.Media.FontFamily to use for text 
    formatting. Fallbacks are permitted; for details,see 
    System.Windows.Media.FontFamily.
  
  SetFontFamily(self: FormattedText,fontFamily: str,startIndex: int,count: int)
   Sets the font family for a specified subset of characters in the 
    System.Windows.Media.FormattedText object.
  
  
   fontFamily: A string that constructs the System.Windows.Media.FontFamily to use for text 
    formatting. Fallbacks are permitted; for details,see 
    System.Windows.Media.FontFamily.
  
   startIndex: The starting index of the initial character to apply the font family change to.
   count: The number of characters the change should apply to.
  """
  pass
 def SetFontSize(self,emSize,startIndex=None,count=None):
  """
  SetFontSize(self: FormattedText,emSize: float,startIndex: int,count: int)
   Sets the font size for a specified subset of characters in the 
    System.Windows.Media.FormattedText object.
  
  
   emSize: The font 'em' measure size,provided in device-independent units (1/96th inch 
    per unit).
  
   startIndex: The start index of the initial character to apply the font size to.
   count: The number of characters to apply the font size to.
  SetFontSize(self: FormattedText,emSize: float)
   Sets the font size for the entire set of characters in the 
    System.Windows.Media.FormattedText object.
  
  
   emSize: The font 'em' measure size,provided in device-independent units (1/96th inch 
    per unit).
  """
  pass
 def SetFontStretch(self,stretch,startIndex=None,count=None):
  """
  SetFontStretch(self: FormattedText,stretch: FontStretch,startIndex: int,count: int)
   Sets the font stretch value for a specified subset of characters in the 
    System.Windows.Media.FormattedText object.
  
  
   stretch: The desired System.Windows.FontStretch value to use for text formatting.
   startIndex: The start index of the initial character to apply the font stretch to.
   count: The number of characters to apply the font stretch to.
  SetFontStretch(self: FormattedText,stretch: FontStretch)
   Sets the font stretch value for the entire set of characters in the 
    System.Windows.Media.FormattedText object.
  
  
   stretch: The desired System.Windows.FontStretch value to use for text formatting.
  """
  pass
 def SetFontStyle(self,style,startIndex=None,count=None):
  """
  SetFontStyle(self: FormattedText,style: FontStyle,startIndex: int,count: int)
   Sets the font style for a specified subset of characters in the 
    System.Windows.Media.FormattedText object.
  
  
   style: The System.Windows.FontStyle value to use for text formatting.
   startIndex: The start index of the initial character to apply the font style to.
   count: The number of characters to apply the font style to.
  SetFontStyle(self: FormattedText,style: FontStyle)
   Sets the font style for the entire set of characters in the 
    System.Windows.Media.FormattedText object.
  
  
   style: The System.Windows.FontStyle value to use for text formatting.
  """
  pass
 def SetFontTypeface(self,typeface,startIndex=None,count=None):
  """
  SetFontTypeface(self: FormattedText,typeface: Typeface,startIndex: int,count: int)
   Sets the font typeface for a specified subset of characters in the 
    System.Windows.Media.FormattedText object.
  
  
   typeface: The System.Windows.Media.Typeface to use for text formatting.
   startIndex: The start index of the initial character to apply the typeface to.
   count: The number of characters to apply the typeface to.
  SetFontTypeface(self: FormattedText,typeface: Typeface)
   Sets the font typeface for the entire set of characters in the 
    System.Windows.Media.FormattedText object.
  
  
   typeface: The System.Windows.Media.Typeface to use for text formatting.
  """
  pass
 def SetFontWeight(self,weight,startIndex=None,count=None):
  """
  SetFontWeight(self: FormattedText,weight: FontWeight,startIndex: int,count: int)
   Changes the System.Windows.FontWeight for specified text within a 
    System.Windows.Media.FormattedText object.
  
  
   weight: The font weight to use for text formatting.
   startIndex: The start index of the initial character to apply the font weight to.
   count: The number of characters to apply the font weight to.
  SetFontWeight(self: FormattedText,weight: FontWeight)
   Sets the font weight for the entire set of characters in the 
    System.Windows.Media.FormattedText object.
  
  
   weight: The System.Windows.FontWeight to use for text formatting.
  """
  pass
 def SetForegroundBrush(self,foregroundBrush,startIndex=None,count=None):
  """
  SetForegroundBrush(self: FormattedText,foregroundBrush: Brush,startIndex: int,count: int)
   Changes the foreground System.Windows.Media.Brush for specified text within a 
    System.Windows.Media.FormattedText object.
  
  
   foregroundBrush: The brush to use for the text foreground.
   startIndex: The start index of the initial character to apply the foreground brush to.
   count: The number of characters to apply the foreground brush to.
  SetForegroundBrush(self: FormattedText,foregroundBrush: Brush)
   Changes the foreground System.Windows.Media.Brush for an entire 
    System.Windows.Media.FormattedText object.
  
  
   foregroundBrush: The brush to use for the text foreground.
  """
  pass
 def SetMaxTextWidths(self,maxTextWidths):
  """
  SetMaxTextWidths(self: FormattedText,maxTextWidths: Array[float])
   Sets an array of maximum text widths within the 
    System.Windows.Media.FormattedText,on a per-line basis. Each element in the 
    array represents the maximum text width of sequential lines of text.
  
  
   maxTextWidths: An array of maximum text widths,each width provided in device-independent 
    units (1/96th inch per unit).
  """
  pass
 def SetNumberSubstitution(self,numberSubstitution,startIndex=None,count=None):
  """
  SetNumberSubstitution(self: FormattedText,numberSubstitution: NumberSubstitution,startIndex: int,count: int)
   Sets the number substitution behavior for specified text within a 
    System.Windows.Media.FormattedText object.
  
  
   numberSubstitution: Number substitution behavior to apply to the text; can be null,in which case 
    the default number substitution method for the text culture is used.
  
   startIndex: The start index of initial character to apply the change to.
   count: The number of characters the change should be applied to.
  SetNumberSubstitution(self: FormattedText,numberSubstitution: NumberSubstitution)
   Sets the number substitution behavior for the entire set of characters in the 
    System.Windows.Media.FormattedText object.
  
  
   numberSubstitution: Number substitution behavior to apply to the text; can be null,in which case 
    the default number substitution method for the text culture is used.
  """
  pass
 def SetTextDecorations(self,textDecorations,startIndex=None,count=None):
  """
  SetTextDecorations(self: FormattedText,textDecorations: TextDecorationCollection,startIndex: int,count: int)
   Sets the System.Windows.TextDecorationCollection for specified text within a 
    System.Windows.Media.FormattedText object.
  
  
   textDecorations: The System.Windows.TextDecorationCollection to apply to the text.
   startIndex: The start index of the initial character to apply the text decorations to.
   count: The number of characters to apply the text decorations to.
  SetTextDecorations(self: FormattedText,textDecorations: TextDecorationCollection)
   Sets the System.Windows.TextDecorationCollection for the entire set of 
    characters in the System.Windows.Media.FormattedText object.
  
  
   textDecorations: The System.Windows.TextDecorationCollection to apply to the text.
  """
  pass
 @staticmethod
 def __new__(self,textToFormat,culture,flowDirection,typeface,emSize,foreground,*__args):
  """
  __new__(cls: type,textToFormat: str,culture: CultureInfo,flowDirection: FlowDirection,typeface: Typeface,emSize: float,foreground: Brush)
  __new__(cls: type,textToFormat: str,culture: CultureInfo,flowDirection: FlowDirection,typeface: Typeface,emSize: float,foreground: Brush,pixelsPerDip: float)
  __new__(cls: type,textToFormat: str,culture: CultureInfo,flowDirection: FlowDirection,typeface: Typeface,emSize: float,foreground: Brush,numberSubstitution: NumberSubstitution)
  __new__(cls: type,textToFormat: str,culture: CultureInfo,flowDirection: FlowDirection,typeface: Typeface,emSize: float,foreground: Brush,numberSubstitution: NumberSubstitution,pixelsPerDip: float)
  __new__(cls: type,textToFormat: str,culture: CultureInfo,flowDirection: FlowDirection,typeface: Typeface,emSize: float,foreground: Brush,numberSubstitution: NumberSubstitution,textFormattingMode: TextFormattingMode)
  __new__(cls: type,textToFormat: str,culture: CultureInfo,flowDirection: FlowDirection,typeface: Typeface,emSize: float,foreground: Brush,numberSubstitution: NumberSubstitution,textFormattingMode: TextFormattingMode,pixelsPerDip: float)
  """
  pass
 Baseline=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the distance from the top of the first line to the baseline of the first line of a System.Windows.Media.FormattedText object.

Get: Baseline(self: FormattedText) -> float

"""

 Extent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the distance from the topmost drawn pixel of the first line to the bottommost drawn pixel of the last line.

Get: Extent(self: FormattedText) -> float

"""

 FlowDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.FlowDirection of a System.Windows.Media.FormattedText object.

Get: FlowDirection(self: FormattedText) -> FlowDirection

Set: FlowDirection(self: FormattedText)=value
"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the distance from the top of the first line to the bottom of the last line of the System.Windows.Media.FormattedText object.

Get: Height(self: FormattedText) -> float

"""

 LineHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the line height,or line spacing,between lines of text.

Get: LineHeight(self: FormattedText) -> float

Set: LineHeight(self: FormattedText)=value
"""

 MaxLineCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum number of lines to display. Text exceeding the System.Windows.Media.FormattedText.MaxLineCount  will not be displayed.

Get: MaxLineCount(self: FormattedText) -> int

Set: MaxLineCount(self: FormattedText)=value
"""

 MaxTextHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum height of a text column.

Get: MaxTextHeight(self: FormattedText) -> float

Set: MaxTextHeight(self: FormattedText)=value
"""

 MaxTextWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum text width (length) for a line of text.

Get: MaxTextWidth(self: FormattedText) -> float

Set: MaxTextWidth(self: FormattedText)=value
"""

 MinWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the smallest possible text width that can fully contain the specified text content.

Get: MinWidth(self: FormattedText) -> float

"""

 OverhangAfter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the distance from the bottom of the last line of text to the bottommost drawn pixel.

Get: OverhangAfter(self: FormattedText) -> float

"""

 OverhangLeading=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the maximum distance from the leading alignment point to the leading drawn pixel of a line.

Get: OverhangLeading(self: FormattedText) -> float

"""

 OverhangTrailing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the maximum distance from the trailing inked pixel to the trailing alignment point of a line.

Get: OverhangTrailing(self: FormattedText) -> float

"""

 PixelsPerDip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PixelsPerDip(self: FormattedText) -> float

Set: PixelsPerDip(self: FormattedText)=value
"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the string of text to be displayed.

Get: Text(self: FormattedText) -> str

"""

 TextAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the alignment of text within a System.Windows.Media.FormattedText object.

Get: TextAlignment(self: FormattedText) -> TextAlignment

Set: TextAlignment(self: FormattedText)=value
"""

 Trimming=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the means by which the omission of text is indicated.

Get: Trimming(self: FormattedText) -> TextTrimming

Set: Trimming(self: FormattedText)=value
"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the width between the leading and trailing alignment points of a line,excluding any trailing white-space characters.

Get: Width(self: FormattedText) -> float

"""

 WidthIncludingTrailingWhitespace=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the width between the leading and trailing alignment points of a line,including any trailing white-space characters.

Get: WidthIncludingTrailingWhitespace(self: FormattedText) -> float

"""


