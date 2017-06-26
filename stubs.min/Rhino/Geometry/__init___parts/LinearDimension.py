class LinearDimension(AnnotationBase,IDisposable,ISerializable):
 """
 LinearDimension()
 LinearDimension(dimensionPlane: Plane,extensionLine1End: Point2d,extensionLine2End: Point2d,pointOnDimensionLine: Point2d)
 """
 def ConstructConstObject(self,*args):
  """ ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int) """
  pass
 def Dispose(self):
  """ Dispose(self: CommonObject,disposing: bool) """
  pass
 def NonConstOperation(self,*args):
  """ NonConstOperation(self: CommonObject) """
  pass
 def OnSwitchToNonConst(self,*args):
  """ OnSwitchToNonConst(self: GeometryBase) """
  pass
 def SetLocations(self,extensionLine1End,extensionLine2End,pointOnDimensionLine):
  """ SetLocations(self: LinearDimension,extensionLine1End: Point2d,extensionLine2End: Point2d,pointOnDimensionLine: Point2d) """
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
 @staticmethod
 def __new__(self,dimensionPlane=None,extensionLine1End=None,extensionLine2End=None,pointOnDimensionLine=None):
  """
  __new__(cls: type)
  __new__(cls: type,dimensionPlane: Plane,extensionLine1End: Point2d,extensionLine2End: Point2d,pointOnDimensionLine: Point2d)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 Aligned=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Aligned(self: LinearDimension) -> bool

Set: Aligned(self: LinearDimension)=value
"""

 Arrowhead1End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Arrowhead1End(self: LinearDimension) -> Point2d

"""

 Arrowhead2End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Arrowhead2End(self: LinearDimension) -> Point2d

"""

 DimensionStyleIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DimensionStyleIndex(self: LinearDimension) -> int

Set: DimensionStyleIndex(self: LinearDimension)=value
"""

 DistanceBetweenArrowTips=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DistanceBetweenArrowTips(self: LinearDimension) -> float

"""

 ExtensionLine1End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExtensionLine1End(self: LinearDimension) -> Point2d

"""

 ExtensionLine2End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExtensionLine2End(self: LinearDimension) -> Point2d

"""

 TextPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TextPosition(self: LinearDimension) -> Point2d

Set: TextPosition(self: LinearDimension)=value
"""


