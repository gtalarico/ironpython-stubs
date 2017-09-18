class FilterDoubleRule(FilterNumericValueRule,IDisposable):
 """
 A filter rule that operates on double-precision numeric values in a Revit project.

 

 FilterDoubleRule(valueProvider: FilterableValueProvider,evaluator: FilterNumericRuleEvaluator,ruleValue: float,epsilon: float)
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
 def __new__(self,valueProvider,evaluator,ruleValue,epsilon):
  """ __new__(cls: type,valueProvider: FilterableValueProvider,evaluator: FilterNumericRuleEvaluator,ruleValue: float,epsilon: float) """
  pass
 Epsilon=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The tolerance within which two floating-point values may be considered equal.



Get: Epsilon(self: FilterDoubleRule) -> float



Set: Epsilon(self: FilterDoubleRule)=value

"""

 RuleValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The user-supplied value against which values from a Revit document will be tested.



Get: RuleValue(self: FilterDoubleRule) -> float



Set: RuleValue(self: FilterDoubleRule)=value

"""


