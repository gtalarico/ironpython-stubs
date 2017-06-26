class Definition(object):
    """ The Definition object is a base object for all type of parameter definitions within the Autodesk Revit API. """
    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The user visible name for the parameter.

Get: Name(self: Definition) -> str

"""

    ParameterGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the group ID of the parameter definition.

Get: ParameterGroup(self: Definition) -> BuiltInParameterGroup

"""

    ParameterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the user visible interpretation of the parameter data.

Get: ParameterType(self: Definition) -> ParameterType

"""

    UnitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the UnitType of the parameter definition.

Get: UnitType(self: Definition) -> UnitType

"""


