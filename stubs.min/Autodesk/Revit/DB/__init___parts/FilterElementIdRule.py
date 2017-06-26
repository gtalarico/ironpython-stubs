class FilterElementIdRule(FilterNumericValueRule,IDisposable):
 """
 A filter rule that operates on ElementId values in a Revit project.
 
 FilterElementIdRule(valueProvider: FilterableValueProvider,evaluator: FilterNumericRuleEvaluator,ruleValue: ElementId)
 """
 def Dispose(self):
  """ Dispose(self: FilterRule,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FilterRule,disposing: bool) """
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
 def __new__(self,valueProvider,evaluator,ruleValue):
  """ __new__(cls: type,valueProvider: FilterableValueProvider,evaluator: FilterNumericRuleEvaluator,ruleValue: ElementId) """
  pass
 RuleValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The user-supplied value against which values from a Revit document will be tested.

Get: RuleValue(self: FilterElementIdRule) -> ElementId

Set: RuleValue(self: FilterElementIdRule)=value
"""


