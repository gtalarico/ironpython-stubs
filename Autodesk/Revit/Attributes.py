# encoding: utf-8
# module Autodesk.Revit.Attributes calls itself Attributes
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class JournalingAttribute(Attribute):
    """
    The custom journaling attribute to control the journaling behavior of the external command.
    
    JournalingAttribute(mode: JournalingMode)
    """
    @staticmethod # known case of __new__
    def __new__(self, mode):
        """ __new__(cls: type, mode: JournalingMode) """
        pass

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Journaling mode.

Get: Mode(self: JournalingAttribute) -> JournalingMode

"""



class JournalingMode(Enum):
    """
    All journaling modes supported by Revit external commands.
    
    enum JournalingMode, values: NoCommandData (1), UsingCommandData (0)
    """
    NoCommandData = None
    UsingCommandData = None
    value__ = None


class RegenerationAttribute(Attribute):
    """
    The custom regeneration attribute to control the regeneration behavior of the external command or external application.
    
    RegenerationAttribute(option: RegenerationOption)
    """
    @staticmethod # known case of __new__
    def __new__(self, option):
        """ __new__(cls: type, option: RegenerationOption) """
        pass

    Option = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Regeneration option.

Get: Option(self: RegenerationAttribute) -> RegenerationOption

"""



class RegenerationOption(Enum):
    """
    All regeneration options supported by Revit external commands and external applications.
    
    enum RegenerationOption, values: Manual (0)
    """
    Manual = None
    value__ = None


class TransactionAttribute(Attribute):
    """
    The custom transaction attribute to control the transaction behavior of the external command.
    
    TransactionAttribute(mode: TransactionMode)
    """
    @staticmethod # known case of __new__
    def __new__(self, mode):
        """ __new__(cls: type, mode: TransactionMode) """
        pass

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Transaction mode.

Get: Mode(self: TransactionAttribute) -> TransactionMode

"""



class TransactionMode(Enum):
    """
    All transaction modes supported by Revit external commands.
    
    enum TransactionMode, values: Automatic (0), Manual (1), ReadOnly (2)
    """
    Automatic = None
    Manual = None
    ReadOnly = None
    value__ = None


