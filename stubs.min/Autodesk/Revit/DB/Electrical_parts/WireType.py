class WireType(ElementType,IDisposable):
 """ Represents a specific wire type. """
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
 Conduit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The conduit type of the wire type.

Get: Conduit(self: WireType) -> WireConduitType

Set: Conduit(self: WireType)=value
"""

 Insulation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The insulation type.

Get: Insulation(self: WireType) -> InsulationType

Set: Insulation(self: WireType)=value
"""

 IsInUse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the wire type is in use.

Get: IsInUse(self: WireType) -> bool

"""

 MaxSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The max size of the wire type.

Get: MaxSize(self: WireType) -> WireSize

Set: MaxSize(self: WireType)=value
"""

 NeutralMultiplier=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The neutral multiplier type of the wire type.

Get: NeutralMultiplier(self: WireType) -> float

Set: NeutralMultiplier(self: WireType)=value
"""

 NeutralRequired=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether or not the neutral point is required.

Get: NeutralRequired(self: WireType) -> bool

Set: NeutralRequired(self: WireType)=value
"""

 NeutralSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The maximum neutral size of the wire type.

Get: NeutralSize(self: WireType) -> NeutralMode

Set: NeutralSize(self: WireType)=value
"""

 TemperatureRating=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The temperature rating type of the wire type.

Get: TemperatureRating(self: WireType) -> TemperatureRatingType

Set: TemperatureRating(self: WireType)=value
"""

 WireMaterial=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The material type of the wire type.

Get: WireMaterial(self: WireType) -> WireMaterialType

Set: WireMaterial(self: WireType)=value
"""


