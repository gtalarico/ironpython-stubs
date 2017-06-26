class ToolboxItemFilterAttribute(Attribute, _Attribute):
    """
    Specifies the filter string and filter type to use for a toolbox item.
    
    ToolboxItemFilterAttribute(filterString: str)
    ToolboxItemFilterAttribute(filterString: str, filterType: ToolboxItemFilterType)
    """
    def Equals(self, obj):
        """
        Equals(self: ToolboxItemFilterAttribute, obj: object) -> bool
        
            obj: The object to compare.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ToolboxItemFilterAttribute) -> int """
        pass

    def Match(self, obj):
        """
        Match(self: ToolboxItemFilterAttribute, obj: object) -> bool
        
            Indicates whether the specified object has a matching filter string.
        
            obj: The object to test for a matching filter string.
            Returns: true if the specified object has a matching filter string; otherwise, false.
        """
        pass

    def ToString(self):
        """ ToString(self: ToolboxItemFilterAttribute) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, filterString, filterType=None):
        """
        __new__(cls: type, filterString: str)
        __new__(cls: type, filterString: str, filterType: ToolboxItemFilterType)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FilterString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the filter string for the toolbox item.

Get: FilterString(self: ToolboxItemFilterAttribute) -> str

"""

    FilterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the filter.

Get: FilterType(self: ToolboxItemFilterAttribute) -> ToolboxItemFilterType

"""

    TypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type ID for the attribute.

Get: TypeId(self: ToolboxItemFilterAttribute) -> object

"""


