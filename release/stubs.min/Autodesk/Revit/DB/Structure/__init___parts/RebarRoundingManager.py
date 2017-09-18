class RebarRoundingManager(ReinforcementRoundingManager,IDisposable):
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



Get: ApplicableReinforcementRoundingSource(self: RebarRoundingManager) -> ReinforcementRoundingSource



"""

 ApplicableSegmentLengthRounding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The applicable rounding for shared parameters used by rebar.



Get: ApplicableSegmentLengthRounding(self: RebarRoundingManager) -> float



"""

 ApplicableSegmentLengthRoundingMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The applicable rounding method for shared parameters used by rebar.



Get: ApplicableSegmentLengthRoundingMethod(self: RebarRoundingManager) -> RoundingMethod



"""

 ApplicableTotalLengthRounding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The applicable rounding for Bar Length and Total Bar Length parameters.



Get: ApplicableTotalLengthRounding(self: RebarRoundingManager) -> float



"""

 ApplicableTotalLengthRoundingMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The applicable rounding method for Bar Length and Total Bar Length parameters.



Get: ApplicableTotalLengthRoundingMethod(self: RebarRoundingManager) -> RoundingMethod



"""

 SegmentLengthRounding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The rounding for shared parameters used by rebar.



Get: SegmentLengthRounding(self: RebarRoundingManager) -> float



Set: SegmentLengthRounding(self: RebarRoundingManager)=value

"""

 SegmentLengthRoundingMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies the segment length rounding method



Get: SegmentLengthRoundingMethod(self: RebarRoundingManager) -> RoundingMethod



Set: SegmentLengthRoundingMethod(self: RebarRoundingManager)=value

"""

 TotalLengthRounding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The rounding for Bar Length and Total Bar Length parameters.



Get: TotalLengthRounding(self: RebarRoundingManager) -> float



Set: TotalLengthRounding(self: RebarRoundingManager)=value

"""

 TotalLengthRoundingMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies the total length rounding method



Get: TotalLengthRoundingMethod(self: RebarRoundingManager) -> RoundingMethod



Set: TotalLengthRoundingMethod(self: RebarRoundingManager)=value

"""


