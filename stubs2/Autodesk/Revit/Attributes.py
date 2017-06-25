# encoding: utf-8
# module Autodesk.Revit.Attributes calls itself Attributes
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class JournalingAttribute(Attribute, _Attribute):
    """
    The custom journaling attribute to control the journaling behavior of the external command.
    
    JournalingAttribute(mode: JournalingMode)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, mode):
        """ __new__(cls: type, mode: JournalingMode) """
        pass

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Journaling mode.

Get: Mode(self: JournalingAttribute) -> JournalingMode

"""



class JournalingMode(Enum, IComparable, IFormattable, IConvertible):
    """
    All journaling modes supported by Revit external commands.
    
    enum JournalingMode, values: NoCommandData (1), UsingCommandData (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    NoCommandData = None
    UsingCommandData = None
    value__ = None


class RegenerationAttribute(Attribute, _Attribute):
    """
    The custom regeneration attribute to control the regeneration behavior of the external command or external application.
    
    RegenerationAttribute(option: RegenerationOption)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, option):
        """ __new__(cls: type, option: RegenerationOption) """
        pass

    Option = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Regeneration option.

Get: Option(self: RegenerationAttribute) -> RegenerationOption

"""



class RegenerationOption(Enum, IComparable, IFormattable, IConvertible):
    """
    All regeneration options supported by Revit external commands and external applications.
    
    enum RegenerationOption, values: Manual (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Manual = None
    value__ = None


class TransactionAttribute(Attribute, _Attribute):
    """
    The custom transaction attribute to control the transaction behavior of the external command.
    
    TransactionAttribute(mode: TransactionMode)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, mode):
        """ __new__(cls: type, mode: TransactionMode) """
        pass

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Transaction mode.

Get: Mode(self: TransactionAttribute) -> TransactionMode

"""



class TransactionMode(Enum, IComparable, IFormattable, IConvertible):
    """
    All transaction modes supported by Revit external commands.
    
    enum TransactionMode, values: Automatic (0), Manual (1), ReadOnly (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Automatic = None
    Manual = None
    ReadOnly = None
    value__ = None


