class ReinforcementRoundingManager(object, IDisposable):
    """ A base class providing access to reinforcement rounding overrides for structural elements. """
    def Dispose(self):
        """ Dispose(self: ReinforcementRoundingManager) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ReinforcementRoundingManager, disposing: bool) """
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

    Element = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The owner of the reinforcement rounding overrides.

Get: Element(self: ReinforcementRoundingManager) -> Element

"""

    IsActiveOnElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines whether reinforcement rounding is activated for the particular element.

Get: IsActiveOnElement(self: ReinforcementRoundingManager) -> bool

Set: IsActiveOnElement(self: ReinforcementRoundingManager) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ReinforcementRoundingManager) -> bool

"""

    LengthDisplayUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length units used when displaying the reinforcement rounding values.

Get: LengthDisplayUnit(self: ReinforcementRoundingManager) -> DisplayUnitType

"""


