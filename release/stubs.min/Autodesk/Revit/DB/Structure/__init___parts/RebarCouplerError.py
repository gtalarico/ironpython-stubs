class RebarCouplerError(Enum,IComparable,IFormattable,IConvertible):
 """
 Error states for the Rebar Coupler

 

 enum RebarCouplerError,values: BarSegementsAreNotParallel (6),BarSegmentsAreNotOnSameLine (7),BarSegmentSmallerThanEngagement (13),BarsNotTouching (3),CurvesOtherThanLine (12),DifferentLayout (2),InconsistentShape (8),IncorrectEndTreatmentCoupler (5),IncorrectEndTreatmentHook (4),IncorrectInputData (1),InvalidDiameter (9),ValidationSuccessfuly (0),VaryingDistanceBetweenDistributionsBars (14)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 BarSegementsAreNotParallel=None
 BarSegmentsAreNotOnSameLine=None
 BarSegmentSmallerThanEngagement=None
 BarsNotTouching=None
 CurvesOtherThanLine=None
 DifferentLayout=None
 InconsistentShape=None
 IncorrectEndTreatmentCoupler=None
 IncorrectEndTreatmentHook=None
 IncorrectInputData=None
 InvalidDiameter=None
 ValidationSuccessfuly=None
 value__=None
 VaryingDistanceBetweenDistributionsBars=None

