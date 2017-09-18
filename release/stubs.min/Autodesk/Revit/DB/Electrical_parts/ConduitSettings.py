class ConduitSettings(Element,IDisposable):
 """ The conduit settings. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetConduitSettings(document):
  """
  GetConduitSettings(document: Document) -> ConduitSettings
  
   Gets the conduit settings of the project.
  
   document: The document.
   Returns: The conduit settings of the project.
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
 ConnectorSeparator=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The conduit connector separator string.

Get: ConnectorSeparator(self: ConduitSettings) -> str

Set: ConnectorSeparator(self: ConduitSettings)=value
"""

 FittingAnnotationSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The value of fitting annotation size.

Get: FittingAnnotationSize(self: ConduitSettings) -> float

Set: FittingAnnotationSize(self: ConduitSettings)=value
"""

 RiseDropAnnotationSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The rise drop annotation size.

Get: RiseDropAnnotationSize(self: ConduitSettings) -> float

Set: RiseDropAnnotationSize(self: ConduitSettings)=value
"""

 SizePrefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The conduit size prefix string.

Get: SizePrefix(self: ConduitSettings) -> str

Set: SizePrefix(self: ConduitSettings)=value
"""

 SizeSuffix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The conduit size suffix string.

Get: SizeSuffix(self: ConduitSettings) -> str

Set: SizeSuffix(self: ConduitSettings)=value
"""

 UseAnnotationScaleForSingleLineFittings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether use annotation scale for single line fittings or not.

Get: UseAnnotationScaleForSingleLineFittings(self: ConduitSettings) -> bool

Set: UseAnnotationScaleForSingleLineFittings(self: ConduitSettings)=value
"""


