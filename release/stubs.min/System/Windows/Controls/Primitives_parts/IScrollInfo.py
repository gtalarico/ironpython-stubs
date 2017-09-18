class IScrollInfo:
 """ Represents the main scrollable region inside a System.Windows.Controls.ScrollViewer control. """
 def LineDown(self):
  """
  LineDown(self: IScrollInfo)

   Scrolls down within content by one logical unit.
  """
  pass
 def LineLeft(self):
  """
  LineLeft(self: IScrollInfo)

   Scrolls left within content by one logical unit.
  """
  pass
 def LineRight(self):
  """
  LineRight(self: IScrollInfo)

   Scrolls right within content by one logical unit.
  """
  pass
 def LineUp(self):
  """
  LineUp(self: IScrollInfo)

   Scrolls up within content by one logical unit.
  """
  pass
 def MakeVisible(self,visual,rectangle):
  """
  MakeVisible(self: IScrollInfo,visual: Visual,rectangle: Rect) -> Rect

  

   Forces content to scroll until the coordinate space of a System.Windows.Media.Visual object is 

    visible.

  

  

   visual: A System.Windows.Media.Visual that becomes visible.

   rectangle: A bounding rectangle that identifies the coordinate space to make visible.

   Returns: A System.Windows.Rect that is visible.
  """
  pass
 def MouseWheelDown(self):
  """
  MouseWheelDown(self: IScrollInfo)

   Scrolls down within content after a user clicks the wheel button on a mouse.
  """
  pass
 def MouseWheelLeft(self):
  """
  MouseWheelLeft(self: IScrollInfo)

   Scrolls left within content after a user clicks the wheel button on a mouse.
  """
  pass
 def MouseWheelRight(self):
  """
  MouseWheelRight(self: IScrollInfo)

   Scrolls right within content after a user clicks the wheel button on a mouse.
  """
  pass
 def MouseWheelUp(self):
  """
  MouseWheelUp(self: IScrollInfo)

   Scrolls up within content after a user clicks the wheel button on a mouse.
  """
  pass
 def PageDown(self):
  """
  PageDown(self: IScrollInfo)

   Scrolls down within content by one page.
  """
  pass
 def PageLeft(self):
  """
  PageLeft(self: IScrollInfo)

   Scrolls left within content by one page.
  """
  pass
 def PageRight(self):
  """
  PageRight(self: IScrollInfo)

   Scrolls right within content by one page.
  """
  pass
 def PageUp(self):
  """
  PageUp(self: IScrollInfo)

   Scrolls up within content by one page.
  """
  pass
 def SetHorizontalOffset(self,offset):
  """
  SetHorizontalOffset(self: IScrollInfo,offset: float)

   Sets the amount of horizontal offset.

  

   offset: The degree to which content is horizontally offset from the containing viewport.
  """
  pass
 def SetVerticalOffset(self,offset):
  """
  SetVerticalOffset(self: IScrollInfo,offset: float)

   Sets the amount of vertical offset.

  

   offset: The degree to which content is vertically offset from the containing viewport.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 CanHorizontallyScroll=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether scrolling on the horizontal axis is possible.



Get: CanHorizontallyScroll(self: IScrollInfo) -> bool



Set: CanHorizontallyScroll(self: IScrollInfo)=value

"""

 CanVerticallyScroll=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether scrolling on the vertical axis is possible.



Get: CanVerticallyScroll(self: IScrollInfo) -> bool



Set: CanVerticallyScroll(self: IScrollInfo)=value

"""

 ExtentHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the vertical size of the extent.



Get: ExtentHeight(self: IScrollInfo) -> float



"""

 ExtentWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the horizontal size of the extent.



Get: ExtentWidth(self: IScrollInfo) -> float



"""

 HorizontalOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the horizontal offset of the scrolled content.



Get: HorizontalOffset(self: IScrollInfo) -> float



"""

 ScrollOwner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Windows.Controls.ScrollViewer element that controls scrolling behavior.



Get: ScrollOwner(self: IScrollInfo) -> ScrollViewer



Set: ScrollOwner(self: IScrollInfo)=value

"""

 VerticalOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the vertical offset of the scrolled content.



Get: VerticalOffset(self: IScrollInfo) -> float



"""

 ViewportHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the vertical size of the viewport for this content.



Get: ViewportHeight(self: IScrollInfo) -> float



"""

 ViewportWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the horizontal size of the viewport for this content.



Get: ViewportWidth(self: IScrollInfo) -> float



"""


