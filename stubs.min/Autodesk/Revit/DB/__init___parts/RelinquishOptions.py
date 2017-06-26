class RelinquishOptions(object, IDisposable):
    """
    Options to control behavior of relinquishing ownership of elements and worksets.
    
    RelinquishOptions(relinquishEverything: bool)
    """
    def Dispose(self):
        """ Dispose(self: RelinquishOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RelinquishOptions, disposing: bool) """
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
    def __new__(self, relinquishEverything):
        """ __new__(cls: type, relinquishEverything: bool) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CheckedOutElements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True means all elements checked out by the current user should be relinquished.
   False means none of these are relinquished.

Get: CheckedOutElements(self: RelinquishOptions) -> bool

Set: CheckedOutElements(self: RelinquishOptions) = value
"""

    FamilyWorksets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True means all family worksets owned by the current user should be relinquished.
   False means none of these are relinquished.

Get: FamilyWorksets(self: RelinquishOptions) -> bool

Set: FamilyWorksets(self: RelinquishOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RelinquishOptions) -> bool

"""

    StandardWorksets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True means all project standards worksets owned by the current user should be relinquished.
   False means none of these are relinquished.

Get: StandardWorksets(self: RelinquishOptions) -> bool

Set: StandardWorksets(self: RelinquishOptions) = value
"""

    UserWorksets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True means all user-created worksets owned by the current user should be relinquished.
   False means none of these are relinquished.

Get: UserWorksets(self: RelinquishOptions) -> bool

Set: UserWorksets(self: RelinquishOptions) = value
"""

    ViewWorksets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True means all view worksets owned by the current user should be relinquished.
   False means none of these are relinquished.

Get: ViewWorksets(self: RelinquishOptions) -> bool

Set: ViewWorksets(self: RelinquishOptions) = value
"""


