class SizeChangedInfo(object):
 """
 Report the specifics of a value change involving a System.Windows.Size. This is used as a parameter in System.Windows.UIElement.OnRenderSizeChanged(System.Windows.SizeChangedInfo) overrides.
 
 SizeChangedInfo(element: UIElement,previousSize: Size,widthChanged: bool,heightChanged: bool)
 """
 @staticmethod
 def __new__(self,element,previousSize,widthChanged,heightChanged):
  """ __new__(cls: type,element: UIElement,previousSize: Size,widthChanged: bool,heightChanged: bool) """
  pass
 HeightChanged=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this System.Windows.SizeChangedInfo  reports a size change that includes a significant change to the Height component.

Get: HeightChanged(self: SizeChangedInfo) -> bool

"""

 NewSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the new size being reported.

Get: NewSize(self: SizeChangedInfo) -> Size

"""

 PreviousSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the previous size of the size-related value being reported as changed.

Get: PreviousSize(self: SizeChangedInfo) -> Size

"""

 WidthChanged=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that declares whether the Width component of the size changed.

Get: WidthChanged(self: SizeChangedInfo) -> bool

"""


