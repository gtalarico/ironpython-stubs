class FormatUtils(object):
    """ A utility class for formatting numbers with units. """
    @staticmethod
    def Format(document, unitType, value):
        """
        Format(document: Document, unitType: UnitType, value: float) -> str
        
            Formats a number with units into a string based on the units formatting 
             settings for a document.
        
        
            document: The document whose Units object will be used for the units formatting settings.
            unitType: The unit type of the value to format.
            value: The value to format, in Revit's internal units.
            Returns: The formatted string.
        """
        pass

    __all__ = [
        'Format',
    ]

