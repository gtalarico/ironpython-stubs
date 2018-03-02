# encoding: utf-8
# module Tekla.Structures.Plugins calls itself Plugins
# from Tekla.Structures.Plugins, Version=2017.0.0.0, Culture=neutral, PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AutoDirectionTypeAttribute(Attribute):
    """
    AutoDirectionTypeAttribute(Type: AutoDirectionTypeEnum)
    AutoDirectionTypeAttribute(Type: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, Type):
        """
        __new__(cls: type, Type: AutoDirectionTypeEnum)
        __new__(cls: type, Type: int)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: AutoDirectionTypeAttribute) -> AutoDirectionTypeEnum

"""



class ConnectionBase(MarshalByRefObject):
    # no doc
    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: ConnectionBase) -> object """
        pass

    def IsDefaultValue(self, Value):
        """
        IsDefaultValue(self: ConnectionBase, Value: str) -> bool
        IsDefaultValue(self: ConnectionBase, Value: float) -> bool
        IsDefaultValue(self: ConnectionBase, Value: int) -> bool
        """
        pass

    def Run(self):
        """ Run(self: ConnectionBase) -> bool """
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: ConnectionBase) -> str

Set: Code(self: ConnectionBase) = value
"""

    Identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identifier(self: ConnectionBase) -> Identifier

"""

    Positions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Positions(self: ConnectionBase) -> List[Point]

"""

    Primary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Primary(self: ConnectionBase) -> Identifier

"""

    Secondaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Secondaries(self: ConnectionBase) -> List[Identifier]

"""


    InputObjectType = None
    SeamInputType = None
    SecondaryType = None


class CustomPartBase(MarshalByRefObject):
    # no doc
    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: CustomPartBase) -> object """
        pass

    def IsDefaultValue(self, Value):
        """
        IsDefaultValue(self: CustomPartBase, Value: str) -> bool
        IsDefaultValue(self: CustomPartBase, Value: float) -> bool
        IsDefaultValue(self: CustomPartBase, Value: int) -> bool
        """
        pass

    def Run(self):
        """ Run(self: CustomPartBase) -> bool """
        pass

    Identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identifier(self: CustomPartBase) -> Identifier

"""

    Positions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Positions(self: CustomPartBase) -> List[Point]

"""



class DetailTypeAttribute(Attribute):
    """
    DetailTypeAttribute(Type: DetailTypeEnum)
    DetailTypeAttribute(Type: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, Type):
        """
        __new__(cls: type, Type: DetailTypeEnum)
        __new__(cls: type, Type: int)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: DetailTypeAttribute) -> DetailTypeEnum

"""



class DrawingPluginBase(MarshalByRefObject):
    # no doc
    def DefineInput(self):
        """ DefineInput(self: DrawingPluginBase) -> List[InputDefinition] """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: DrawingPluginBase) -> object """
        pass

    def IsDefaultValue(self, Value):
        """
        IsDefaultValue(self: DrawingPluginBase, Value: str) -> bool
        IsDefaultValue(self: DrawingPluginBase, Value: float) -> bool
        IsDefaultValue(self: DrawingPluginBase, Value: int) -> bool
        """
        pass

    def Run(self, Input):
        """ Run(self: DrawingPluginBase, Input: List[InputDefinition]) -> bool """
        pass

    InputDefinition = None
    UpdateMode = None


class InputObjectDependencyAttribute(Attribute):
    """
    InputObjectDependencyAttribute(Type: InputObjectDependency)
    InputObjectDependencyAttribute(Type: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, Type):
        """
        __new__(cls: type, Type: InputObjectDependency)
        __new__(cls: type, Type: int)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: InputObjectDependencyAttribute) -> InputObjectDependency

"""



class InputObjectTypeAttribute(Attribute):
    """
    InputObjectTypeAttribute(Type: InputObjectType)
    InputObjectTypeAttribute(Type: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, Type):
        """
        __new__(cls: type, Type: InputObjectType)
        __new__(cls: type, Type: int)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: InputObjectTypeAttribute) -> InputObjectType

"""



class PluginAttribute(Attribute):
    """ PluginAttribute(name: str) """
    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PluginAttribute) -> str

"""



class PluginBase(MarshalByRefObject):
    # no doc
    def DefineInput(self):
        """ DefineInput(self: PluginBase) -> List[InputDefinition] """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: PluginBase) -> object """
        pass

    def IsDefaultValue(self, Value):
        """
        IsDefaultValue(self: PluginBase, Value: str) -> bool
        IsDefaultValue(self: PluginBase, Value: float) -> bool
        IsDefaultValue(self: PluginBase, Value: int) -> bool
        """
        pass

    def Run(self, Input):
        """ Run(self: PluginBase, Input: List[InputDefinition]) -> bool """
        pass

    Identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identifier(self: PluginBase) -> Identifier

"""


    CoordinateSystemType = None
    InputDefinition = None
    InputObjectDependency = None


class PluginCoordinateSystemAttribute(Attribute):
    """
    PluginCoordinateSystemAttribute(Type: CoordinateSystemType)
    PluginCoordinateSystemAttribute(Type: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, Type):
        """
        __new__(cls: type, Type: CoordinateSystemType)
        __new__(cls: type, Type: int)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: PluginCoordinateSystemAttribute) -> CoordinateSystemType

"""



class PluginDescriptionAttribute(Attribute):
    """ PluginDescriptionAttribute(language: str, description: str) """
    @staticmethod # known case of __new__
    def __new__(self, language, description):
        """ __new__(cls: type, language: str, description: str) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: PluginDescriptionAttribute) -> str

"""

    Language = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Language(self: PluginDescriptionAttribute) -> str

"""



class PluginNameAttribute(Attribute):
    """ PluginNameAttribute(language: str, name: str) """
    @staticmethod # known case of __new__
    def __new__(self, language, name):
        """ __new__(cls: type, language: str, name: str) """
        pass

    Language = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Language(self: PluginNameAttribute) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PluginNameAttribute) -> str

"""



class PluginUserInterfaceAttribute(Attribute):
    """ PluginUserInterfaceAttribute(description: str) """
    @staticmethod # known case of __new__
    def __new__(self, description):
        """ __new__(cls: type, description: str) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: PluginUserInterfaceAttribute) -> str

"""



class PositionTypeAttribute(Attribute):
    """
    PositionTypeAttribute(Type: PositionTypeEnum)
    PositionTypeAttribute(Type: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, Type):
        """
        __new__(cls: type, Type: PositionTypeEnum)
        __new__(cls: type, Type: int)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: PositionTypeAttribute) -> PositionTypeEnum

"""



class SeamInputTypeAttribute(Attribute):
    """
    SeamInputTypeAttribute(Type: SeamInputType)
    SeamInputTypeAttribute(Type: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, Type):
        """
        __new__(cls: type, Type: SeamInputType)
        __new__(cls: type, Type: int)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: SeamInputTypeAttribute) -> SeamInputType

"""



class SecondaryTypeAttribute(Attribute):
    """
    SecondaryTypeAttribute(Type: SecondaryType)
    SecondaryTypeAttribute(Type: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, Type):
        """
        __new__(cls: type, Type: SecondaryType)
        __new__(cls: type, Type: int)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: SecondaryTypeAttribute) -> SecondaryType

"""



class StructuresFieldAttribute(Attribute):
    """ StructuresFieldAttribute(attributeName: str) """
    @staticmethod # known case of __new__
    def __new__(self, attributeName):
        """ __new__(cls: type, attributeName: str) """
        pass

    AttributeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttributeName(self: StructuresFieldAttribute) -> str

"""



class UpdateModeAttribute(Attribute):
    """
    UpdateModeAttribute(Type: UpdateMode)
    UpdateModeAttribute(Type: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, Type):
        """
        __new__(cls: type, Type: UpdateMode)
        __new__(cls: type, Type: int)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: UpdateModeAttribute) -> UpdateMode

"""



