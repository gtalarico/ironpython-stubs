class PrimarySizeCriterion(RoutingCriterionBase,IDisposable):
 """
 This class contains a size criterion for a RoutingPreferenceRule.
 
 PrimarySizeCriterion(minimumSize: float,maximumSize: float)
 """
 @staticmethod
 def All():
  """
  All() -> PrimarySizeCriterion
  
   Creates a criterion with a range of all sizes.
   Returns: The new criterion.
  """
  pass
 def Dispose(self):
  """ Dispose(self: RoutingCriterionBase,A_0: bool) """
  pass
 @staticmethod
 def None():
  """
  None() -> PrimarySizeCriterion
  
   Creates a criterion with a range of no sizes.
   Returns: The new criterion.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: RoutingCriterionBase,disposing: bool) """
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
 def __new__(self,minimumSize,maximumSize):
  """ __new__(cls: type,minimumSize: float,maximumSize: float) """
  pass
 MaximumSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The maximum size of this criterion.

Get: MaximumSize(self: PrimarySizeCriterion) -> float

Set: MaximumSize(self: PrimarySizeCriterion)=value
"""

 MinimumSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The minimum size of this criterion.

Get: MinimumSize(self: PrimarySizeCriterion) -> float

Set: MinimumSize(self: PrimarySizeCriterion)=value
"""


