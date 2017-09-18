class FabricRoundingManager(ReinforcementRoundingManager,IDisposable):
 """ Provides access to element reinforcement roundings overrides. """
 def Dispose(self):
  """ Dispose(self: ReinforcementRoundingManager,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ReinforcementRoundingManager,disposing: bool) """
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
 ApplicableReinforcementRoundingSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies the source of the rounding settings for this element.

Get: ApplicableReinforcementRoundingSource(self: FabricRoundingManager) -> ReinforcementRoundingSource

"""

 ApplicableSegmentLengthRounding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The applicable rounding for fabric segments.

Get: ApplicableSegmentLengthRounding(self: FabricRoundingManager) -> float

"""

 ApplicableSegmentLengthRoundingMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The applicable rounding method for fabric segments.

Get: ApplicableSegmentLengthRoundingMethod(self: FabricRoundingManager) -> RoundingMethod

"""

 ApplicableTotalLengthRounding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The applicable rounding for Cut Overall Length and Cut Overall Width parameters.

Get: ApplicableTotalLengthRounding(self: FabricRoundingManager) -> float

"""

 ApplicableTotalLengthRoundingMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The applicable rounding method for Cut Overall Length and Cut Overall Width parameters.

Get: ApplicableTotalLengthRoundingMethod(self: FabricRoundingManager) -> RoundingMethod

"""

 SegmentLengthRounding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The rounding for fabric segments.

Get: SegmentLengthRounding(self: FabricRoundingManager) -> float

Set: SegmentLengthRounding(self: FabricRoundingManager)=value
"""

 SegmentLengthRoundingMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies the segment length rounding method

Get: SegmentLengthRoundingMethod(self: FabricRoundingManager) -> RoundingMethod

Set: SegmentLengthRoundingMethod(self: FabricRoundingManager)=value
"""

 TotalLengthRounding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The rounding for Cut Overall Length and Cut Overall Width parameters.

Get: TotalLengthRounding(self: FabricRoundingManager) -> float

Set: TotalLengthRounding(self: FabricRoundingManager)=value
"""

 TotalLengthRoundingMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies the total length rounding method

Get: TotalLengthRoundingMethod(self: FabricRoundingManager) -> RoundingMethod

Set: TotalLengthRoundingMethod(self: FabricRoundingManager)=value
"""


