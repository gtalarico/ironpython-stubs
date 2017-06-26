class RoutingConditions(object, IDisposable):
    """
    RoutingConditions contain routing information that is used as input when determining if a routing criterion,
       such as minimum or maximum diameter, is met.
    
    RoutingConditions(errorLevel: RoutingPreferenceErrorLevel)
    """
    def AppendCondition(self, condition):
        """
        AppendCondition(self: RoutingConditions, condition: RoutingCondition)
            Appends a routing condition to the end of existing routing conditions. Note 
             that the first item (indexed at 0) is the condition for the primary connector.
        """
        pass

    def Clear(self):
        """
        Clear(self: RoutingConditions)
            Clear all existing conditions
        """
        pass

    def Dispose(self):
        """ Dispose(self: RoutingConditions) """
        pass

    def GetConditionAt(self, index):
        """
        GetConditionAt(self: RoutingConditions, index: int) -> RoutingCondition
        
            Gets the routing condition at the specified index position.
        
            index: The 0-based index to access the collection of available conditions. The method 
             throws the exception ArgumentOutOfRangeException if the index is out of range.
        
            Returns: The found routing condition.
        """
        pass

    def GetNumberOfConditions(self):
        """
        GetNumberOfConditions(self: RoutingConditions) -> int
        
            Gets the number of included routing conditions.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RoutingConditions, disposing: bool) """
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
    def __new__(self, errorLevel):
        """ __new__(cls: type, errorLevel: RoutingPreferenceErrorLevel) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ErrorLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The error level that the routing preference manager should post errors if the routing conditions do not meet any routing preference rule, could be None, Warning, or Error

Get: ErrorLevel(self: RoutingConditions) -> RoutingPreferenceErrorLevel

Set: ErrorLevel(self: RoutingConditions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RoutingConditions) -> bool

"""

    PreferredJunctionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The junction type (Tee or Tap) to select if defined fittings of both junction types meet all routing conditions.

Get: PreferredJunctionType(self: RoutingConditions) -> PreferredJunctionType

Set: PreferredJunctionType(self: RoutingConditions) = value
"""


