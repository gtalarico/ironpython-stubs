class FilterStringRule(FilterValueRule, IDisposable):
    """
    A filter rule that operates on string values in a Revit project.
    
    FilterStringRule(valueProvider: FilterableValueProvider, evaluator: FilterStringRuleEvaluator, ruleString: str, caseSensitive: bool)
    """
    def Dispose(self):
        """ Dispose(self: FilterRule, A_0: bool) """
        pass

    def GetEvaluator(self):
        """
        GetEvaluator(self: FilterStringRule) -> FilterStringRuleEvaluator
        
            Gets the evaluator that implements the test for this rule.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FilterRule, disposing: bool) """
        pass

    def SetEvaluator(self, evaluator):
        """
        SetEvaluator(self: FilterStringRule, evaluator: FilterStringRuleEvaluator)
            Sets the evaluator that implements the test for this rule.
        """
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
    def __new__(self, valueProvider, evaluator, ruleString, caseSensitive):
        """ __new__(cls: type, valueProvider: FilterableValueProvider, evaluator: FilterStringRuleEvaluator, ruleString: str, caseSensitive: bool) """
        pass

    RuleString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The user-supplied string against which strings from a Revit document will be tested.

Get: RuleString(self: FilterStringRule) -> str

Set: RuleString(self: FilterStringRule) = value
"""


