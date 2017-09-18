class TextNode(RenderNode,IDisposable):
 """ This is a class representing a text annotation object in a model-exporting process. """
 def Dispose(self):
  """ Dispose(self: RenderNode,A_0: bool) """
  pass
 def GetFormattedText(self):
  """
  GetFormattedText(self: TextNode) -> FormattedText
  
   Returns an Autodesk.Revit.DB.FormattedText object that contains text and 
    associated formatting of this TextNode.
  
   Returns: The object that contains the text and associated formatting of of the text in 
    this text note.
  """
  pass
 def GetFormattedTextRuns(self):
  """
  GetFormattedTextRuns(self: TextNode) -> IList[FormattedTextRun]
  
   Returns a list of separated runs of formatted text.
   Returns: A collection of instances of Autodesk.Revit.DB.FormattedTextRun.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RenderNode,disposing: bool) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 BaseDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Direction of the base line of the text object in model space.

Get: BaseDirection(self: TextNode) -> XYZ

"""

 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The color of the text.

Get: Color(self: TextNode) -> Color

"""

 FontHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Height [ft] of the text font,in model space.

Get: FontHeight(self: TextNode) -> float

"""

 FontName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the text font.

Get: FontName(self: TextNode) -> str

"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Height [ft] of the area of the text content in model space.

Get: Height(self: TextNode) -> float

"""

 HorizontalAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates default horizontal alignment of the text.

Get: HorizontalAlignment(self: TextNode) -> HorizontalTextAlignment

"""

 IsBold=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the default formatting is set to bold text.

Get: IsBold(self: TextNode) -> bool

"""

 IsForRightToLeftReading=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the text uses Right-To-Left reading order.

Get: IsForRightToLeftReading(self: TextNode) -> bool

"""

 IsItalic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the default formatting is set to italic text.

Get: IsItalic(self: TextNode) -> bool

"""

 IsKeptReadable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates text behavior inside a rotated text object.

Get: IsKeptReadable(self: TextNode) -> bool

"""

 IsTransparent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the text background is transparent or opaque.

Get: IsTransparent(self: TextNode) -> bool

"""

 IsUnderlined=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the default formatting is set to underlined text.

Get: IsUnderlined(self: TextNode) -> bool

"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Position of the text in model coordinates.

Get: Position(self: TextNode) -> XYZ

"""

 TabSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The size [ft] of the interval between tab stops,in model space.

Get: TabSize(self: TextNode) -> float

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The content of the text annotation as a plain string stripped of all formatting.

Get: Text(self: TextNode) -> str

"""

 TextSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Height [ft] of the text in model space.

Get: TextSize(self: TextNode) -> float

"""

 UpDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Direction along the vertical axis of letters of the text object in model space.

Get: UpDirection(self: TextNode) -> XYZ

"""

 VerticalAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates default vertical alignment of the text.

Get: VerticalAlignment(self: TextNode) -> VerticalTextAlignment

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Width [ft] of the area of the text content in model space.

Get: Width(self: TextNode) -> float

"""

 WidthScale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Scale applied to the width of the text.

Get: WidthScale(self: TextNode) -> float

"""


