class WorksetFilter(object, IDisposable):
    """ A base class for a type of filter that accepts or rejects worksets based upon criteria. """
    def Dispose(self):
        """ Dispose(self: WorksetFilter) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WorksetFilter, disposing: bool) """
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

    IncludeStandaloneWorksetsOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the results of the filter only match stand-alone worksets; worksets that are not stand-alone will be rejected.

Get: IncludeStandaloneWorksetsOnly(self: WorksetFilter) -> bool

Set: IncludeStandaloneWorksetsOnly(self: WorksetFilter) = value
"""

    Inverted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the results of the filter are inverted; worksets that would normally be accepted by this filter will be rejected,
   and worksets that would normally be rejected will be accepted.

Get: Inverted(self: WorksetFilter) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: WorksetFilter) -> bool

"""


