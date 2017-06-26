class ParameterFilterElement(FilterElement, IDisposable):
    """
    Admits elements that satisfy two conditions:
       The element's category must be one of a certain set of allowed categories.The element must pass a series of filter rules.
    """
    @staticmethod
    def AllRuleParametersApplicable(*__args):
        """
        AllRuleParametersApplicable(self: ParameterFilterElement, rules: IList[FilterRule]) -> bool
        AllRuleParametersApplicable(aDocument: Document, categories: ICollection[ElementId], rules: IList[FilterRule]) -> bool
        """
        pass

    def ClearRules(self):
        """
        ClearRules(self: ParameterFilterElement)
            Removes all rules from this filter.
        """
        pass

    @staticmethod
    def Create(aDocument, name, categories, rules=None):
        """
        Create(aDocument: Document, name: str, categories: ICollection[ElementId]) -> ParameterFilterElement
        Create(aDocument: Document, name: str, categories: ICollection[ElementId], rules: IList[FilterRule]) -> ParameterFilterElement
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetCategories(self):
        """
        GetCategories(self: ParameterFilterElement) -> ICollection[ElementId]
        
            Gets the categories admitted by this filter.
        """
        pass

    @staticmethod
    def GetRuleParameter(rule):
        """
        GetRuleParameter(rule: FilterRule) -> ElementId
        
            Returns the parameter for a given filter rule.
        
            rule: The rule to query.
            Returns: The identifier of the rule's parameter.
        """
        pass

    def GetRuleParameters(self):
        """
        GetRuleParameters(self: ParameterFilterElement) -> IList[ElementId]
        
            Retrieves a list of the parameters associated with each rule in the filter.
           
             The order of the resulting array corresponds to the order in which the 
             associated
           filter rules are applied.
        
            Returns: An array of parameter identifiers.
        """
        pass

    def GetRules(self):
        """
        GetRules(self: ParameterFilterElement) -> IList[FilterRule]
        
            Returns the rules of this filter, in the order in which they are applied.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def SetCategories(self, categories):
        """ SetCategories(self: ParameterFilterElement, categories: ICollection[ElementId]) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetRules(self, rules):
        """ SetRules(self: ParameterFilterElement, rules: IList[FilterRule]) """
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

