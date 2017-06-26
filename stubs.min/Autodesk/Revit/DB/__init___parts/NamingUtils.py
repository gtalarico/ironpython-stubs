class NamingUtils(object):
    """ A collection of utilities related to element naming. """
    @staticmethod
    def CompareNames(nameA, nameB):
        """
        CompareNames(nameA: str, nameB: str) -> int
        
            Compares two object name strings using Revit's comparison rules.
        
            nameA: The first object name to compare.
            nameB: The second object name to compare.
            Returns: An integer indicating the result of the lexical comparison between the two 
             names.
           Less than zero if nameA comes before nameB in the ordering, zero if 
             nameA and nameB are equivalent,
           and greater than zero if nameA is comes 
             after nameB in the ordering.
        """
        pass

    @staticmethod
    def IsValidName(string):
        """
        IsValidName(string: str) -> bool
        
            Identifies if the input string is valid for use as an object name in Revit.
        
            string: The name to validate.
            Returns: True if the name is valid for use as a name in Revit, false if it contains 
             prohibited characters and is invalid.
        """
        pass

    __all__ = [
        'CompareNames',
        'IsValidName',
    ]

