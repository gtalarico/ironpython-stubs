class ParameterFilterUtilities(object):
    """
    Contains static utility functions for enumerating the categories and parameters that
       are available for use by ParameterFilterElement objects.
    """
    @staticmethod
    def GetAllFilterableCategories():
        """
        GetAllFilterableCategories() -> ICollection[ElementId]
        
            Returns the set of categories that may be used in a ParameterFilterElement.
            Returns: The set of all filterable categories.
        """
        pass

    @staticmethod
    def GetFilterableParametersInCommon(aDoc, categories):
        """ GetFilterableParametersInCommon(aDoc: Document, categories: ICollection[ElementId]) -> ICollection[ElementId] """
        pass

    @staticmethod
    def GetInapplicableParameters(aDoc, categories, parameters):
        """ GetInapplicableParameters(aDoc: Document, categories: ICollection[ElementId], parameters: IList[ElementId]) -> IList[ElementId] """
        pass

    @staticmethod
    def IsParameterApplicable(element, parameter):
        """
        IsParameterApplicable(element: Element, parameter: ElementId) -> bool
        
            Used to determine whether the element supports the given parameter.
        
            element: The element to query for support of the given parameter.
            parameter: The parameter for which to query support.
            Returns: True if the element supports the given parameter, false otherwise.
        """
        pass

    @staticmethod
    def RemoveUnfilterableCategories(categories):
        """ RemoveUnfilterableCategories(categories: ICollection[ElementId]) -> ICollection[ElementId] """
        pass

    __all__ = [
        'GetAllFilterableCategories',
        'GetFilterableParametersInCommon',
        'GetInapplicableParameters',
        'IsParameterApplicable',
        'RemoveUnfilterableCategories',
    ]

