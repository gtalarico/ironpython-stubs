class FilterIntegerRule(FilterNumericValueRule, IDisposable):
    """
    A filter rule that operates on integer values in a Revit project.
    
    FilterIntegerRule(valueProvider: FilterableValueProvider, evaluator: FilterNumericRuleEvaluator, ruleValue: int)
    """
    def Dispose(self):
        """ Dispose(self: FilterRule, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FilterRule, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, valueProvider, evaluator, ruleValue):
        """ __new__(cls: type, valueProvider: FilterableValueProvider, evaluator: FilterNumericRuleEvaluator, ruleValue: int) """
        pass

    RuleValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The user-supplied value against which values from a Revit document will be tested.

Get: RuleValue(self: FilterIntegerRule) -> int

Set: RuleValue(self: FilterIntegerRule) = value
"""


