class ExternalDefinitionCreationOptions(object, IDisposable):
    """
    An option class used for creating a new shared parameter definition, including options such as name, type, visibility,
       Guid description and modifiable flag.
    
    ExternalDefinitionCreationOptions(name: str, type: ParameterType)
    """
    def Dispose(self):
        """ Dispose(self: ExternalDefinitionCreationOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExternalDefinitionCreationOptions, disposing: bool) """
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
    def __new__(self, name, type):
        """ __new__(cls: type, name: str, type: ParameterType) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The description of the parameter definition to be created. The description will be used as tooltip in the
   Revit UI including in the properties palette.
   The default is an empty string.

Get: Description(self: ExternalDefinitionCreationOptions) -> str

Set: Description(self: ExternalDefinitionCreationOptions) = value
"""

    GUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GUID to use for this parameter definition.
   If not explicitly set, a random GUID is used.

Get: GUID(self: ExternalDefinitionCreationOptions) -> Guid

Set: GUID(self: ExternalDefinitionCreationOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExternalDefinitionCreationOptions) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the parameter definition to be created.

Get: Name(self: ExternalDefinitionCreationOptions) -> str

Set: Name(self: ExternalDefinitionCreationOptions) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the parameter definition to be created.

Get: Type(self: ExternalDefinitionCreationOptions) -> ParameterType

Set: Type(self: ExternalDefinitionCreationOptions) = value
"""

    UserModifiable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property indicates whether this parameter can be modified by UI user or not.
   True if the parameter will be modifiable by the user in the user interface, false if the parameter will display as read-only.
   The default is true.

Get: UserModifiable(self: ExternalDefinitionCreationOptions) -> bool

Set: UserModifiable(self: ExternalDefinitionCreationOptions) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the parameter is visible to the user, false if it is hidden and accessible only via the API.
   The default is true.

Get: Visible(self: ExternalDefinitionCreationOptions) -> bool

Set: Visible(self: ExternalDefinitionCreationOptions) = value
"""


