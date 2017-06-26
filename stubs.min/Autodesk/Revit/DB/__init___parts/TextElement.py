class TextElement(Element,IDisposable):
 """ Base class representing text elements in Revit. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetMaximumAllowedWidth(cdda=None,typeId=None):
  """
  GetMaximumAllowedWidth(self: TextElement) -> float
  
   Returns the maximum width the text element can be assigned.
   Returns: The maximum allowed width in paper space [ft].
  GetMaximumAllowedWidth(cdda: Document,typeId: ElementId) -> float
  
   Returns the maximum width the text element can be created with.
  
   cdda: A document containing the new text element's type
   typeId: Id of the text type
   Returns: The maximum allowed width in paper space [ft].
  """
  pass
 @staticmethod
 def GetMinimumAllowedWidth(cdda=None,typeId=None):
  """
  GetMinimumAllowedWidth(self: TextElement) -> float
  
   Returns the minimum width the text element can be assigned.
   Returns: The minimum allowed width in paper space [ft].
  GetMinimumAllowedWidth(cdda: Document,typeId: ElementId) -> float
  
   Returns the minimum width a text element can be created with.
  
   cdda: A document containing the new text element's type
   typeId: Id of the text type
   Returns: The minimum allowed width in paper space [ft].
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
 """Direction of the base line of the text element.

Get: BaseDirection(self: TextElement) -> XYZ

"""

 Coord=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Position of the text (in model coordinates.)

Get: Coord(self: TextElement) -> XYZ

Set: Coord(self: TextElement)=value
"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Height of the area of the text content.

Get: Height(self: TextElement) -> float

"""

 HorizontalAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Horizontal alignment of the text content within the text area of the element.

Get: HorizontalAlignment(self: TextElement) -> HorizontalTextAlignment

Set: HorizontalAlignment(self: TextElement)=value
"""

 IsTextWrappingActive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A flag identifying whether text-wrapping is currently active in this text element or not.

Get: IsTextWrappingActive(self: TextElement) -> bool

"""

 KeepRotatedTextReadable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A flag to control how text behaves inside a rotated text element.

Get: KeepRotatedTextReadable(self: TextElement) -> bool

Set: KeepRotatedTextReadable(self: TextElement)=value
"""

 Symbol=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the type of the TextElement object.

Get: Symbol(self: TextElement) -> TextElementType

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The content of the element as a plain string stripped of all formating.

Get: Text(self: TextElement) -> str

Set: Text(self: TextElement)=value
"""

 UpDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Direction along the vertical axis of letters of the text note.

Get: UpDirection(self: TextElement) -> XYZ

"""

 VerticalAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Vertical alignment of the text content within the text area of the element.

Get: VerticalAlignment(self: TextElement) -> VerticalTextAlignment

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Width of the area of the text content.

Get: Width(self: TextElement) -> float

Set: Width(self: TextElement)=value
"""


