class RevitLinkOptions(object, IDisposable):
    """
    This class contains the options in use when creating
       or loading a Revit link.
    
    RevitLinkOptions(relative: bool)
    RevitLinkOptions(relative: bool, config: WorksetConfiguration)
    RevitLinkOptions(other: RevitLinkOptions)
    """
    def Dispose(self):
        """ Dispose(self: RevitLinkOptions) """
        pass

    def GetWorksetConfiguration(self):
        """
        GetWorksetConfiguration(self: RevitLinkOptions) -> WorksetConfiguration
        
            Gets the set of worksets to open when creating the link.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitLinkOptions, disposing: bool) """
        pass

    def SetWorksetConfiguration(self, config):
        """
        SetWorksetConfiguration(self: RevitLinkOptions, config: WorksetConfiguration)
            Sets the set of worksets to open when creating the link.
        """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, relative: bool)
        __new__(cls: type, relative: bool, config: WorksetConfiguration)
        __new__(cls: type, other: RevitLinkOptions)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsRelative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of path to use when creating the link. If true, Revit will
   store a relative path for the link. If false, Revit will store an absolute
   path.

   If the link is to a Revit Server location, isRelative must be false.

Get: IsRelative(self: RevitLinkOptions) -> bool

Set: IsRelative(self: RevitLinkOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RevitLinkOptions) -> bool

"""


