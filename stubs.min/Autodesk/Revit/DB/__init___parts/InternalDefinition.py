class InternalDefinition(Definition, IDisposable):
    """
    This object represents a parameter definition in Autodesk Revit.
       Every parameter has a ParamDef object which defines what kind of parameter it is, its properties, its behavior, etc.
       The ParamDef class is a base class with various derived classes representing different kinds of parameters.
       ParamDefs serve the following purposes:
       Basic properties : name, ID, the group it appears in (in the UI), whether it is read only, etc.
       Formatting and parsing : converting values to and from display strings, implemented by subclasses.
       Defining the kind of parameter : the kind of data the parameter represents: length, text, material, level, etc.
       Defining the UI for the parameter : together with the corresponding ParameterUI subclass,
       determines what kind of control will be used for the parameter in properties grids: edit box, combo box, pushbutton, etc.
    """
    def Dispose(self):
        """ Dispose(self: InternalDefinition) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: InternalDefinition, disposing: bool) """
        pass

    def SetAllowVaryBetweenGroups(self, document, allowVaryBetweenGroups):
        """
        SetAllowVaryBetweenGroups(self: InternalDefinition, document: Document, allowVaryBetweenGroups: bool) -> ICollection[ElementId]
        
            Whether or not the parameter values can vary across group members.
        
            document: The document of this parameter.
            allowVaryBetweenGroups: Whether this parameter should be allowed to vary between groups.
            Returns: The ids of elements that were updated to align the values between groups.
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

    BuiltInParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tests whether this definition identifies a built-in parameter or not.

Get: BuiltInParameter(self: InternalDefinition) -> BuiltInParameter

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the parameter.

Get: Id(self: InternalDefinition) -> ElementId

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: InternalDefinition) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The user-visible name for the parameter.

Get: Name(self: InternalDefinition) -> str

"""

    ParameterGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of a built-in parameter group to which the parameter defined by this definition belongs.

Get: ParameterGroup(self: InternalDefinition) -> BuiltInParameterGroup

Set: ParameterGroup(self: InternalDefinition) = value
"""

    ParameterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the user-visible interpretation of the parameter data.

Get: ParameterType(self: InternalDefinition) -> ParameterType

"""

    VariesAcrossGroups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not the parameter values can vary across group members.

Get: VariesAcrossGroups(self: InternalDefinition) -> bool

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the parameter is visible in the Autodesk Revit user interface.

Get: Visible(self: InternalDefinition) -> bool

"""


