class Leader(APIObject, IDisposable):
    """ A leader object that can be attached to annotation elements such as text notes. """
    def Dispose(self):
        """ Dispose(self: Leader, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Leader, disposing: bool)ReleaseUnmanagedResources(self: APIObject) """
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

    Anchor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Anchor point of the Leader

Get: Anchor(self: Leader) -> XYZ

"""

    Elbow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Elbow point of the Leader.

Get: Elbow(self: Leader) -> XYZ

Set: Elbow(self: Leader) = value
"""

    End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """End point of the Leader.

Get: End(self: Leader) -> XYZ

Set: End(self: Leader) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: Leader) -> bool

"""

    LeaderShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Geometric style of the leader

Get: LeaderShape(self: Leader) -> LeaderShape

"""


