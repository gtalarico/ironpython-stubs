class RevitCommandId(object, IDisposable):
    """ Represents a command id in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: RevitCommandId) """
        pass

    @staticmethod
    def LookupCommandId(name):
        """
        LookupCommandId(name: str) -> RevitCommandId
        
            Looks up and retrieves the Revit command id with the given id string.
        
            name: he Revit command name. Refer to the entries in the Revit journal to find the 
             string to use for a particular command.
        
            Returns: The Revit command id. Returning "null" if a command with the given name was not 
             found.
        """
        pass

    @staticmethod
    def LookupPostableCommandId(postableCommand):
        """
        LookupPostableCommandId(postableCommand: PostableCommand) -> RevitCommandId
        
            Looks up and retrieves the Revit command id with the given id string.
        
            postableCommand: The postable command.
            Returns: The Revit command id. Returning ll if a command with the given name was not 
             found.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitCommandId, disposing: bool) """
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

    CanHaveBinding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the command can be assigned a binding to an external add-in.

Get: CanHaveBinding(self: RevitCommandId) -> bool

"""

    HasBinding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether a replacement of either the Execute or CanExecute events (or both) have been applied to this command.

Get: HasBinding(self: RevitCommandId) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The command id.

Get: Id(self: RevitCommandId) -> UInt32

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RevitCommandId) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The command name.

Get: Name(self: RevitCommandId) -> str

"""


