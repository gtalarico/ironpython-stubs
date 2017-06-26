class AnalyticalModelColumn(AnalyticalModelStick,IDisposable):
 """ An element that represents the structural analytical model column. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
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
 BaseExtension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The base extension option.

Get: BaseExtension(self: AnalyticalModelColumn) -> StickElementExtension

Set: BaseExtension(self: AnalyticalModelColumn)=value
"""

 BaseExtensionMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The bottom extension method option.

Get: BaseExtensionMethod(self: AnalyticalModelColumn) -> AnalyticalAlignmentMethod

Set: BaseExtensionMethod(self: AnalyticalModelColumn)=value
"""

 BaseExtensionPlaneId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The bottom extension plane ID option.

Get: BaseExtensionPlaneId(self: AnalyticalModelColumn) -> ElementId

Set: BaseExtensionPlaneId(self: AnalyticalModelColumn)=value
"""

 TopExtension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The top extension option.

Get: TopExtension(self: AnalyticalModelColumn) -> StickElementExtension

Set: TopExtension(self: AnalyticalModelColumn)=value
"""

 TopExtensionMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The top extension method option.

Get: TopExtensionMethod(self: AnalyticalModelColumn) -> AnalyticalAlignmentMethod

Set: TopExtensionMethod(self: AnalyticalModelColumn)=value
"""

 TopExtensionPlaneId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The top extension plane ID option.

Get: TopExtensionPlaneId(self: AnalyticalModelColumn) -> ElementId

Set: TopExtensionPlaneId(self: AnalyticalModelColumn)=value
"""


