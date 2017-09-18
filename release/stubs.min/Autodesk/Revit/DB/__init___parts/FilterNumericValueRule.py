class FilterNumericValueRule(FilterValueRule,IDisposable):
 """ Base for all classes that use a FilterNumericRuleEvaluator to perform their comparisons """
 def Dispose(self):
  """ Dispose(self: FilterRule,A_0: bool) """
  pass
 def GetEvaluator(self):
  """
  GetEvaluator(self: FilterNumericValueRule) -> FilterNumericRuleEvaluator

  

   Gets the evaluator that implements the test for this rule.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FilterRule,disposing: bool) """
  pass
 def SetEvaluator(self,evaluator):
  """
  SetEvaluator(self: FilterNumericValueRule,evaluator: FilterNumericRuleEvaluator)

   Sets the evaluator that implements the test for this rule.
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
