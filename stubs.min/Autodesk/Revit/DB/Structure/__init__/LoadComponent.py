class LoadComponent(object, IDisposable):
    """
    An object that represents a load combination component.
    
    LoadComponent(loadCaseOrCombinationId: ElementId, factor: float)
    """
    def Dispose(self):
        """ Dispose(self: LoadComponent) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LoadComponent, disposing: bool) """
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
    def __new__(self, loadCaseOrCombinationId, factor):
        """ __new__(cls: type, loadCaseOrCombinationId: ElementId, factor: float) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Factor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Load component factor.

Get: Factor(self: LoadComponent) -> float

Set: Factor(self: LoadComponent) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LoadComponent) -> bool

"""

    LoadCaseOrCombinationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Load case or combination id.

Get: LoadCaseOrCombinationId(self: LoadComponent) -> ElementId

Set: LoadCaseOrCombinationId(self: LoadComponent) = value
"""


