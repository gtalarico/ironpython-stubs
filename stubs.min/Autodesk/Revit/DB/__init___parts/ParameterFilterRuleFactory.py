class ParameterFilterRuleFactory(object, IDisposable):
    """ Contains functions that create appropriate FilterRule objects based on the parameters given. """
    @staticmethod
    def CreateBeginsWithRule(parameter, value, caseSensitive):
        """
        CreateBeginsWithRule(parameter: ElementId, value: str, caseSensitive: bool) -> FilterRule
        
            Creates a filter rule that determines whether strings from the document
           
             begin with a certain string value.
        
        
            parameter: A string-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied string value for which values from the document will be 
             searched.
        
            caseSensitive: If true, the string comparison will be case-sensitive.
        """
        pass

    @staticmethod
    def CreateContainsRule(parameter, value, caseSensitive):
        """
        CreateContainsRule(parameter: ElementId, value: str, caseSensitive: bool) -> FilterRule
        
            Creates a filter rule that determines whether strings from the document contain
             
           a certain string value.
        
        
            parameter: A string-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied string value for which values from the document will be 
             searched.
        
            caseSensitive: If true, the string comparison will be case-sensitive.
        """
        pass

    @staticmethod
    def CreateEndsWithRule(parameter, value, caseSensitive):
        """
        CreateEndsWithRule(parameter: ElementId, value: str, caseSensitive: bool) -> FilterRule
        
            Creates a filter rule that determines whether strings from the document
           end 
             with a certain string value.
        
        
            parameter: A string-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied string value for which values from the document will be 
             searched.
        
            caseSensitive: If true, the string comparison will be case-sensitive.
        """
        pass

    @staticmethod
    def CreateEqualsRule(parameter, value, *__args):
        """
        CreateEqualsRule(parameter: ElementId, value: float, epsilon: float) -> FilterRule
        
            Creates a filter rule that determines whether double-precision values
           from 
             the document equal a certain value.
        
        
            parameter: A double-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
            epsilon: Defines the tolerance within which two values may be considered equal.
        CreateEqualsRule(parameter: ElementId, value: str, caseSensitive: bool) -> FilterRule
        
            Creates a filter rule that determines whether strings from the document
           
             equal a certain value.
        
        
            parameter: A string-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied string value against which values from the document will be 
             compared.
        
            caseSensitive: If true, the string comparison will be case-sensitive.
        CreateEqualsRule(parameter: ElementId, value: ElementId) -> FilterRule
        
            Creates a filter rule that determines whether ElementId values
           from the 
             document equal a certain value.
        
        
            parameter: An ElementId-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
        CreateEqualsRule(parameter: ElementId, value: int) -> FilterRule
        
            Creates a filter rule that determines whether integer values
           from the 
             document equal a certain value.
        
        
            parameter: An integer-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
        """
        pass

    @staticmethod
    def CreateGreaterOrEqualRule(parameter, value, *__args):
        """
        CreateGreaterOrEqualRule(parameter: ElementId, value: float, epsilon: float) -> FilterRule
        
            Creates a filter rule that determines whether double-precision values
           from 
             the document are greater than or equal to a certain value.
        
        
            parameter: A double-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
            epsilon: Defines the tolerance within which two values may be considered equal.
        CreateGreaterOrEqualRule(parameter: ElementId, value: str, caseSensitive: bool) -> FilterRule
        
            Creates a filter rule that determines whether strings from the document
           are 
             greater than or equal to a certain value.
        
        
            parameter: A string-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied string value against which values from the document will be 
             compared.
        
            caseSensitive: If true, the string comparison will be case-sensitive.
        CreateGreaterOrEqualRule(parameter: ElementId, value: ElementId) -> FilterRule
        
            Creates a filter rule that determines whether ElementId values
           from the 
             document are greater than or equal to a certain value.
        
        
            parameter: An ElementId-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
        CreateGreaterOrEqualRule(parameter: ElementId, value: int) -> FilterRule
        
            Creates a filter rule that determines whether integer values
           from the 
             document are greater than or equal to a certain value.
        
        
            parameter: An integer-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
        """
        pass

    @staticmethod
    def CreateGreaterRule(parameter, value, *__args):
        """
        CreateGreaterRule(parameter: ElementId, value: float, epsilon: float) -> FilterRule
        
            Creates a filter rule that determines whether double-precision values
           from 
             the document are greater than a certain value.
        
        
            parameter: A double-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
            epsilon: Defines the tolerance within which two values may be considered equal.
        CreateGreaterRule(parameter: ElementId, value: str, caseSensitive: bool) -> FilterRule
        
            Creates a filter rule that determines whether strings from the document
           are 
             greater than a certain value.
        
        
            parameter: A string-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied string value against which values from the document will be 
             compared.
        
            caseSensitive: If true, the string comparison will be case-sensitive.
        CreateGreaterRule(parameter: ElementId, value: ElementId) -> FilterRule
        
            Creates a filter rule that determines whether ElementId values
           from the 
             document are greater than a certain value.
        
        
            parameter: An ElementId-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
        CreateGreaterRule(parameter: ElementId, value: int) -> FilterRule
        
            Creates a filter rule that determines whether integer values
           from the 
             document are greater than a certain value.
        
        
            parameter: An integer-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
        """
        pass

    @staticmethod
    def CreateIsAssociatedWithGlobalParameterRule(parameter, value):
        """
        CreateIsAssociatedWithGlobalParameterRule(parameter: ElementId, value: ElementId) -> FilterRule
        
            Creates a filter rule that determines whether a parameter is associated
           
             with a certain global parameter.
        
        
            parameter: A parameter that can be associated with an existing global parameter of a 
             compatible type.
        
            value: The global parameter used to test the association.
        """
        pass

    @staticmethod
    def CreateIsNotAssociatedWithGlobalParameterRule(parameter, value):
        """
        CreateIsNotAssociatedWithGlobalParameterRule(parameter: ElementId, value: ElementId) -> FilterRule
        
            Creates a filter rule that determines whether a parameter is not associated
           
             with a certain global parameter.
        
        
            parameter: A parameter that can be associated with an existing global parameter of a 
             compatible type.
        
            value: The global parameter used to test the association.
        """
        pass

    @staticmethod
    def CreateLessOrEqualRule(parameter, value, *__args):
        """
        CreateLessOrEqualRule(parameter: ElementId, value: float, epsilon: float) -> FilterRule
        
            Creates a filter rule that determines whether double-precision values
           from 
             the document are less than or equal to a certain value.
        
        
            parameter: A double-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
            epsilon: Defines the tolerance within which two values may be considered equal.
        CreateLessOrEqualRule(parameter: ElementId, value: str, caseSensitive: bool) -> FilterRule
        
            Creates a filter rule that determines whether strings from the document
           are 
             less than or equal to a certain value.
        
        
            parameter: A string-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied string value against which values from the document will be 
             compared.
        
            caseSensitive: If true, the string comparison will be case-sensitive.
        CreateLessOrEqualRule(parameter: ElementId, value: ElementId) -> FilterRule
        
            Creates a filter rule that determines whether ElementId values
           from the 
             document are less than or equal to a certain value.
        
        
            parameter: An ElementId-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
        CreateLessOrEqualRule(parameter: ElementId, value: int) -> FilterRule
        
            Creates a filter rule that determines whether integer values
           from the 
             document are less than or equal to a certain value.
        
        
            parameter: An integer-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
        """
        pass

    @staticmethod
    def CreateLessRule(parameter, value, *__args):
        """
        CreateLessRule(parameter: ElementId, value: float, epsilon: float) -> FilterRule
        
            Creates a filter rule that determines whether double-precision values
           from 
             the document are less than a certain value.
        
        
            parameter: A double-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
            epsilon: Defines the tolerance within which two values may be considered equal.
        CreateLessRule(parameter: ElementId, value: str, caseSensitive: bool) -> FilterRule
        
            Creates a filter rule that determines whether strings from the document
           are 
             less than a certain value.
        
        
            parameter: A string-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied string value against which values from the document will be 
             compared.
        
            caseSensitive: If true, the string comparison will be case-sensitive.
        CreateLessRule(parameter: ElementId, value: ElementId) -> FilterRule
        
            Creates a filter rule that determines whether ElementId values
           from the 
             document are less than a certain value.
        
        
            parameter: An ElementId-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
        CreateLessRule(parameter: ElementId, value: int) -> FilterRule
        
            Creates a filter rule that determines whether integer values
           from the 
             document are less than a certain value.
        
        
            parameter: An integer-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
        """
        pass

    @staticmethod
    def CreateNotBeginsWithRule(parameter, value, caseSensitive):
        """
        CreateNotBeginsWithRule(parameter: ElementId, value: str, caseSensitive: bool) -> FilterRule
        
            Creates a filter rule that determines whether strings from the document
           do 
             not begin with a certain string value.
        
        
            parameter: A string-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied string value for which values from the document will be 
             searched.
        
            caseSensitive: If true, the string comparison will be case-sensitive.
        """
        pass

    @staticmethod
    def CreateNotContainsRule(parameter, value, caseSensitive):
        """
        CreateNotContainsRule(parameter: ElementId, value: str, caseSensitive: bool) -> FilterRule
        
            Creates a filter rule that determines whether strings from the document do not
        
                contain a certain string value.
        
        
            parameter: A string-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied string value for which values from the document will be 
             searched.
        
            caseSensitive: If true, the string comparison will be case-sensitive.
        """
        pass

    @staticmethod
    def CreateNotEndsWithRule(parameter, value, caseSensitive):
        """
        CreateNotEndsWithRule(parameter: ElementId, value: str, caseSensitive: bool) -> FilterRule
        
            Creates a filter rule that determines whether strings from the document
           do 
             not end with a certain string value.
        
        
            parameter: A string-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied string value for which values from the document will be 
             searched.
        
            caseSensitive: If true, the string comparison will be case-sensitive.
        """
        pass

    @staticmethod
    def CreateNotEqualsRule(parameter, value, *__args):
        """
        CreateNotEqualsRule(parameter: ElementId, value: float, epsilon: float) -> FilterRule
        
            Creates a filter rule that determines whether double-precision values
           from 
             the document do not equal a certain value.
        
        
            parameter: A double-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
            epsilon: Defines the tolerance within which two values may be considered equal.
        CreateNotEqualsRule(parameter: ElementId, value: str, caseSensitive: bool) -> FilterRule
        
            Creates a filter rule that determines whether strings from the document
           do 
             not equal a certain value.
        
        
            parameter: A string-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied string value against which values from the document will be 
             compared.
        
            caseSensitive: If true, the string comparison will be case-sensitive.
        CreateNotEqualsRule(parameter: ElementId, value: ElementId) -> FilterRule
        
            Creates a filter rule that determines whether ElementId values
           from the 
             document do not equal a certain value.
        
        
            parameter: An ElementId-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
        CreateNotEqualsRule(parameter: ElementId, value: int) -> FilterRule
        
            Creates a filter rule that determines whether integer values
           from the 
             document do not equal a certain value.
        
        
            parameter: An integer-typed parameter used to get values from the document for a given 
             element.
        
            value: The user-supplied value against which values from the document will be compared.
        """
        pass

    @staticmethod
    def CreateSharedParameterApplicableRule(parameterName):
        """
        CreateSharedParameterApplicableRule(parameterName: str) -> FilterRule
        
            Creates a filter rule that tests elements for support of a shared parameter.
        
            parameterName: The name of the parameter that elements must support to satisfy this rule.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ParameterFilterRuleFactory) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ParameterFilterRuleFactory, disposing: bool) """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ParameterFilterRuleFactory) -> bool

"""


