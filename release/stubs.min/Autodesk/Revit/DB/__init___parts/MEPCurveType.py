class MEPCurveType(HostObjAttributes,IDisposable):
 """ The base type class for MEP curves,such as ducts,pipes,cable trays and conduits. """
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
 Cross=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The default cross fitting of the MEP curve type.

Get: Cross(self: MEPCurveType) -> FamilySymbol

Set: Cross(self: MEPCurveType)=value
"""

 Elbow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The default elbow fitting of the MEP curve type.

Get: Elbow(self: MEPCurveType) -> FamilySymbol

Set: Elbow(self: MEPCurveType)=value
"""

 MultiShapeTransition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The default multi shape transition fitting of the MEP curve type.

Get: MultiShapeTransition(self: MEPCurveType) -> FamilySymbol

Set: MultiShapeTransition(self: MEPCurveType)=value
"""

 PreferredJunctionType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The preferred junction type of the MEP curve type.

Get: PreferredJunctionType(self: MEPCurveType) -> JunctionType

Set: PreferredJunctionType(self: MEPCurveType)=value
"""

 Roughness=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The roughness of the MEP curve type.  For PipeTypes,please use Segment::Roughness

Get: Roughness(self: MEPCurveType) -> float

Set: Roughness(self: MEPCurveType)=value
"""

 RoutingPreferenceManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The RoutingPreferenceManager for the MEPCurveType

Get: RoutingPreferenceManager(self: MEPCurveType) -> RoutingPreferenceManager

"""

 Tap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The default tap fitting of the MEP curve type.

Get: Tap(self: MEPCurveType) -> FamilySymbol

Set: Tap(self: MEPCurveType)=value
"""

 Tee=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The default tee fitting of the MEP curve type.

Get: Tee(self: MEPCurveType) -> FamilySymbol

Set: Tee(self: MEPCurveType)=value
"""

 Transition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The default transition fitting of the MEP curve type.

Get: Transition(self: MEPCurveType) -> FamilySymbol

Set: Transition(self: MEPCurveType)=value
"""

 Union=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The default union fitting of the MEP curve type.

Get: Union(self: MEPCurveType) -> FamilySymbol

Set: Union(self: MEPCurveType)=value
"""


