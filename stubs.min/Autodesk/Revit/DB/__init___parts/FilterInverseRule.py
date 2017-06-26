class FilterInverseRule(FilterRule,IDisposable):
 """
 A filter rule that inverts the boolean values returned by the rule it contains.
 
 FilterInverseRule(innerRule: FilterRule)
 """
 def Dispose(self):
  """ Dispose(self: FilterRule,A_0: bool) """
  pass
 def GetInnerRule(self):
  """
  GetInnerRule(self: FilterInverseRule) -> FilterRule
  
   Gets the rule being inverted.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FilterRule,disposing: bool) """
  pass
 def SetInnerRule(self,innerRule):
  """
  SetInnerRule(self: FilterInverseRule,innerRule: FilterRule)
   Gets the rule being inverted.
  
   innerRule: The rule to invert.
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
 @staticmethod
 def __new__(self,innerRule):
  """ __new__(cls: type,innerRule: FilterRule) """
  pass
