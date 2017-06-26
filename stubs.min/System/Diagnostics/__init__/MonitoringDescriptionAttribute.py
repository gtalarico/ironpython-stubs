class MonitoringDescriptionAttribute(DescriptionAttribute, _Attribute):
    """
    Specifies a description for a property or event.
    
    MonitoringDescriptionAttribute(description: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, description):
        """ __new__(cls: type, description: str) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets description text associated with the item monitored.

Get: Description(self: MonitoringDescriptionAttribute) -> str

"""

    DescriptionValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the string stored as the description.

"""


