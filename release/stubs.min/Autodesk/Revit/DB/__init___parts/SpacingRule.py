class SpacingRule(APIObject,IDisposable):
 """
 A rule for specifying a set of equidistant,

 parallel gridlines within a region.
 """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: SpacingRule) """
  pass
 def SetLayoutFixedDistance(self,distance,just,gridlinesRotation,offset):
  """
  SetLayoutFixedDistance(self: SpacingRule,distance: float,just: SpacingRuleJustification,gridlinesRotation: float,offset: float)

   Set the Layout property to FixedDistance.
  """
  pass
 def SetLayoutFixedNumber(self,number,just,gridlinesRotation,offset):
  """
  SetLayoutFixedNumber(self: SpacingRule,number: int,just: SpacingRuleJustification,gridlinesRotation: float,offset: float)

   Set the Layout property to FixedNumber.
  """
  pass
 def SetLayoutMaximumSpacing(self,distance,just,gridlinesRotation,offset):
  """
  SetLayoutMaximumSpacing(self: SpacingRule,distance: float,just: SpacingRuleJustification,gridlinesRotation: float,offset: float)

   Set the Layout property to MaximumSpacing.
  """
  pass
 def SetLayoutMinimumSpacing(self,distance,just,gridlinesRotation,offset):
  """
  SetLayoutMinimumSpacing(self: SpacingRule,distance: float,just: SpacingRuleJustification,gridlinesRotation: float,offset: float)

   Set the Layout property to MinimumSpacing.
  """
  pass
 def SetLayoutNone(self):
  """
  SetLayoutNone(self: SpacingRule)

   Set the Layout property to None.
  """
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
 BeltMeasurement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """On a curved surface,BeltMeasurement specifies where the

grid's distances are measured.



Get: BeltMeasurement(self: SpacingRule) -> float



Set: BeltMeasurement(self: SpacingRule)=value

"""

 Distance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The exact distance between layout

lines.



Get: Distance(self: SpacingRule) -> float



Set: Distance(self: SpacingRule)=value

"""

 GridlinesRotation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """An additional rotation to be applied

to this set of grid lines.



Get: GridlinesRotation(self: SpacingRule) -> float



Set: GridlinesRotation(self: SpacingRule)=value

"""

 HasBeltMeasurement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if the gridlines are not parallel due to surface

curvature,and the BeltMeasurement property therefore

applies.



Get: HasBeltMeasurement(self: SpacingRule) -> bool



"""

 Justification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The justification of the lines within

the region.



Get: Justification(self: SpacingRule) -> SpacingRuleJustification



Set: Justification(self: SpacingRule)=value

"""

 Layout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A choice of several gridline layout rules.



Get: Layout(self: SpacingRule) -> SpacingRuleLayout



"""

 Number=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The exact number of lines in the

region.



Get: Number(self: SpacingRule) -> int



Set: Number(self: SpacingRule)=value

"""

 Offset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """An additional offset applied to the first

gridline.



Get: Offset(self: SpacingRule) -> float



Set: Offset(self: SpacingRule)=value

"""


