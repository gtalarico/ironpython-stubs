# encoding: utf-8
# module Rhino
# from Rhino3dmIO, Version=5.1.30000.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# functions

def PersistentSettingsEventArgs(*args, **kwargs): # real signature unknown
    """  """
    pass

# classes

class IEpsilonComparable:
    # no doc
    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: IEpsilonComparable[T], other: T, epsilon: float) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEpsilonFComparable:
    # no doc
    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: IEpsilonFComparable[T], other: T, epsilon: Single) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IndexPair(object):
    """ IndexPair(i: int, j: int) """
    @staticmethod # known case of __new__
    def __new__(self, i, j):
        """
        __new__[IndexPair]() -> IndexPair
        
        __new__(cls: type, i: int, j: int)
        """
        pass

    I = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: I(self: IndexPair) -> int

Set: I(self: IndexPair) = value
"""

    J = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: J(self: IndexPair) -> int

Set: J(self: IndexPair) = value
"""



class PersistentSettings(object, ISerializable):
    """ PersistentSettings(allUserSettings: PersistentSettings) """
    def ContainsModifiedValues(self, allUserSettings):
        """ ContainsModifiedValues(self: PersistentSettings, allUserSettings: PersistentSettings) -> bool """
        pass

    def DeleteItem(self, key):
        """ DeleteItem(self: PersistentSettings, key: str) """
        pass

    @staticmethod
    def FromPlugInId(pluginId):
        """ FromPlugInId(pluginId: Guid) -> PersistentSettings """
        pass

    def GetBool(self, key, defaultValue=None):
        """
        GetBool(self: PersistentSettings, key: str, defaultValue: bool) -> bool
        GetBool(self: PersistentSettings, key: str) -> bool
        """
        pass

    def GetByte(self, key, defaultValue=None):
        """
        GetByte(self: PersistentSettings, key: str, defaultValue: Byte) -> Byte
        GetByte(self: PersistentSettings, key: str) -> Byte
        """
        pass

    def GetChar(self, key, defaultValue=None):
        """
        GetChar(self: PersistentSettings, key: str, defaultValue: Char) -> Char
        GetChar(self: PersistentSettings, key: str) -> Char
        """
        pass

    def GetColor(self, key, defaultValue=None):
        """
        GetColor(self: PersistentSettings, key: str, defaultValue: Color) -> Color
        GetColor(self: PersistentSettings, key: str) -> Color
        """
        pass

    def GetDate(self, key, defaultValue=None):
        """
        GetDate(self: PersistentSettings, key: str, defaultValue: DateTime) -> DateTime
        GetDate(self: PersistentSettings, key: str) -> DateTime
        """
        pass

    def GetDouble(self, key, defaultValue=None):
        """
        GetDouble(self: PersistentSettings, key: str, defaultValue: float) -> float
        GetDouble(self: PersistentSettings, key: str) -> float
        """
        pass

    def GetEnumValue(self, *__args):
# Error generating skeleton for function GetEnumValue: Method must be called on a Type for which Type.IsGenericParameter is false.

    def GetInteger(self, key, defaultValue=None):
        """
        GetInteger(self: PersistentSettings, key: str, defaultValue: int) -> int
        GetInteger(self: PersistentSettings, key: str) -> int
        """
        pass

    def GetPoint(self, key, defaultValue=None):
        """
        GetPoint(self: PersistentSettings, key: str, defaultValue: Point) -> Point
        GetPoint(self: PersistentSettings, key: str) -> Point
        """
        pass

    def GetPoint3d(self, key, defaultValue=None):
        """
        GetPoint3d(self: PersistentSettings, key: str, defaultValue: Point3d) -> Point3d
        GetPoint3d(self: PersistentSettings, key: str) -> Point3d
        """
        pass

    def GetRectangle(self, key, defaultValue=None):
        """
        GetRectangle(self: PersistentSettings, key: str, defaultValue: Rectangle) -> Rectangle
        GetRectangle(self: PersistentSettings, key: str) -> Rectangle
        """
        pass

    def GetSize(self, key, defaultValue=None):
        """
        GetSize(self: PersistentSettings, key: str, defaultValue: Size) -> Size
        GetSize(self: PersistentSettings, key: str) -> Size
        """
        pass

    def GetString(self, key, defaultValue=None):
        """
        GetString(self: PersistentSettings, key: str, defaultValue: str) -> str
        GetString(self: PersistentSettings, key: str) -> str
        """
        pass

    def GetStringList(self, key, defaultValue=None):
        """
        GetStringList(self: PersistentSettings, key: str, defaultValue: Array[str]) -> Array[str]
        GetStringList(self: PersistentSettings, key: str) -> Array[str]
        """
        pass

    def GetUnsignedInteger(self, key, defaultValue=None):
        """
        GetUnsignedInteger(self: PersistentSettings, key: str, defaultValue: UInt32) -> UInt32
        GetUnsignedInteger(self: PersistentSettings, key: str) -> UInt32
        """
        pass

    def GetValidator(self, key):
        """ GetValidator(self: PersistentSettings, key: str) -> EventHandler[PersistentSettingsEventArgs] """
        pass

    def RegisterSettingsValidator(self, key, validator):
        """ RegisterSettingsValidator(self: PersistentSettings, key: str, validator: EventHandler[PersistentSettingsEventArgs]) """
        pass

    def SetBool(self, key, value):
        """ SetBool(self: PersistentSettings, key: str, value: bool) """
        pass

    def SetByte(self, key, value):
        """ SetByte(self: PersistentSettings, key: str, value: Byte) """
        pass

    def SetChar(self, key, value):
        """ SetChar(self: PersistentSettings, key: str, value: Char) """
        pass

    def SetColor(self, key, value):
        """ SetColor(self: PersistentSettings, key: str, value: Color) """
        pass

    def SetDate(self, key, value):
        """ SetDate(self: PersistentSettings, key: str, value: DateTime) """
        pass

    def SetDefault(self, key, value):
        """ SetDefault(self: PersistentSettings, key: str, value: Rectangle)SetDefault(self: PersistentSettings, key: str, value: Color)SetDefault(self: PersistentSettings, key: str, value: DateTime)SetDefault(self: PersistentSettings, key: str, value: Point3d)SetDefault(self: PersistentSettings, key: str, value: Point)SetDefault(self: PersistentSettings, key: str, value: Size)SetDefault(self: PersistentSettings, key: str, value: Array[str])SetDefault(self: PersistentSettings, key: str, value: int)SetDefault(self: PersistentSettings, key: str, value: Byte)SetDefault(self: PersistentSettings, key: str, value: bool)SetDefault(self: PersistentSettings, key: str, value: str)SetDefault(self: PersistentSettings, key: str, value: Char)SetDefault(self: PersistentSettings, key: str, value: float) """
        pass

    def SetDouble(self, key, value):
        """ SetDouble(self: PersistentSettings, key: str, value: float) """
        pass

    def SetEnumValue(self, *__args):
        """ SetEnumValue[T](self: PersistentSettings, key: str, enumValue: T)SetEnumValue[T](self: PersistentSettings, enumValue: T) """
        pass

    def SetInteger(self, key, value):
        """ SetInteger(self: PersistentSettings, key: str, value: int) """
        pass

    def SetPoint(self, key, value):
        """ SetPoint(self: PersistentSettings, key: str, value: Point) """
        pass

    def SetPoint3d(self, key, value):
        """ SetPoint3d(self: PersistentSettings, key: str, value: Point3d) """
        pass

    def SetRectangle(self, key, value):
        """ SetRectangle(self: PersistentSettings, key: str, value: Rectangle) """
        pass

    def SetSize(self, key, value):
        """ SetSize(self: PersistentSettings, key: str, value: Size) """
        pass

    def SetString(self, key, value):
        """ SetString(self: PersistentSettings, key: str, value: str) """
        pass

    def SetStringList(self, key, value):
        """ SetStringList(self: PersistentSettings, key: str, value: Array[str]) """
        pass

    def SetUnsignedInteger(self, key, value):
        """ SetUnsignedInteger(self: PersistentSettings, key: str, value: UInt32) """
        pass

    def TryGetBool(self, key, value):
        """ TryGetBool(self: PersistentSettings, key: str) -> (bool, bool) """
        pass

    def TryGetByte(self, key, value):
        """ TryGetByte(self: PersistentSettings, key: str) -> (bool, Byte) """
        pass

    def TryGetChar(self, key, value):
        """ TryGetChar(self: PersistentSettings, key: str) -> (bool, Char) """
        pass

    def TryGetColor(self, key, value):
        """ TryGetColor(self: PersistentSettings, key: str) -> (bool, Color) """
        pass

    def TryGetDate(self, key, value):
        """ TryGetDate(self: PersistentSettings, key: str) -> (bool, DateTime) """
        pass

    def TryGetDefault(self, key, value):
        """
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, Color)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, DateTime)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, Array[str])
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, Rectangle)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, Size)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, Point3d)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, int)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, Byte)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, bool)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, str)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, Char)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, float)
        """
        pass

    def TryGetDouble(self, key, value):
        """ TryGetDouble(self: PersistentSettings, key: str) -> (bool, float) """
        pass

    def TryGetEnumValue(self, *__args):
# Error generating skeleton for function TryGetEnumValue: Method must be called on a Type for which Type.IsGenericParameter is false.

    def TryGetInteger(self, key, value):
        """ TryGetInteger(self: PersistentSettings, key: str) -> (bool, int) """
        pass

    def TryGetPoint(self, key, value):
        """ TryGetPoint(self: PersistentSettings, key: str) -> (bool, Point) """
        pass

    def TryGetPoint3d(self, key, value):
        """ TryGetPoint3d(self: PersistentSettings, key: str) -> (bool, Point3d) """
        pass

    def TryGetRectangle(self, key, value):
        """ TryGetRectangle(self: PersistentSettings, key: str) -> (bool, Rectangle) """
        pass

    def TryGetSize(self, key, value):
        """ TryGetSize(self: PersistentSettings, key: str) -> (bool, Size) """
        pass

    def TryGetString(self, key, value):
        """ TryGetString(self: PersistentSettings, key: str) -> (bool, str) """
        pass

    def TryGetStringList(self, key, value):
        """ TryGetStringList(self: PersistentSettings, key: str) -> (bool, Array[str]) """
        pass

    def TryGetUnsignedInteger(self, key, value):
        """ TryGetUnsignedInteger(self: PersistentSettings, key: str) -> (bool, UInt32) """
        pass

    def __delitem__(self, *args): #cannot find CLR method
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, allUserSettings):
        """
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, allUserSettings: PersistentSettings)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    StringListRootKey = '%root%'


class RhinoMath(object):
    # no doc
    @staticmethod
    def Clamp(value, bound1, bound2):
        """
        Clamp(value: float, bound1: float, bound2: float) -> float
        Clamp(value: int, bound1: int, bound2: int) -> int
        """
        pass

    @staticmethod
    def CRC32(currentRemainder, *__args):
        """
        CRC32(currentRemainder: UInt32, value: int) -> UInt32
        CRC32(currentRemainder: UInt32, value: float) -> UInt32
        CRC32(currentRemainder: UInt32, buffer: Array[Byte]) -> UInt32
        """
        pass

    @staticmethod
    def EpsilonEquals(x, y, epsilon):
        """
        EpsilonEquals(x: Single, y: Single, epsilon: Single) -> bool
        EpsilonEquals(x: float, y: float, epsilon: float) -> bool
        """
        pass

    @staticmethod
    def IsValidDouble(x):
        """ IsValidDouble(x: float) -> bool """
        pass

    @staticmethod
    def IsValidSingle(x):
        """ IsValidSingle(x: Single) -> bool """
        pass

    @staticmethod
    def ToDegrees(radians):
        """ ToDegrees(radians: float) -> float """
        pass

    @staticmethod
    def ToRadians(degrees):
        """ ToRadians(degrees: float) -> float """
        pass

    @staticmethod
    def UnitScale(from, to):
        """ UnitScale(from: UnitSystem, to: UnitSystem) -> float """
        pass

    DefaultAngleTolerance = 0.017453292519943295
    SqrtEpsilon = 1.4901161193849999e-08
    UnsetSingle = None
    UnsetValue = -1.2343210123432101e+308
    ZeroTolerance = 9.9999999999999998e-13
    __all__ = [
        'Clamp',
        'CRC32',
        'DefaultAngleTolerance',
        'EpsilonEquals',
        'IsValidDouble',
        'IsValidSingle',
        'SqrtEpsilon',
        'ToDegrees',
        'ToRadians',
        'UnitScale',
        'UnsetSingle',
        'UnsetValue',
        'ZeroTolerance',
    ]


class UnitSystem(Enum, IComparable, IFormattable, IConvertible):
    """ enum UnitSystem, values: Angstroms (12), Astronomical (23), Centimeters (3), CustomUnitSystem (11), Decimeters (14), Dekameters (15), Feet (9), Gigameters (18), Hectometers (16), Inches (8), Kilometers (5), Lightyears (24), Megameters (17), Meters (4), Microinches (6), Microns (1), Miles (10), Millimeters (2), Mils (7), Nanometers (13), NauticalMile (22), None (0), Parsecs (25), PrinterPica (21), PrinterPoint (20), Yards (19) """
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

    Angstroms = None
    Astronomical = None
    Centimeters = None
    CustomUnitSystem = None
    Decimeters = None
    Dekameters = None
    Feet = None
    Gigameters = None
    Hectometers = None
    Inches = None
    Kilometers = None
    Lightyears = None
    Megameters = None
    Meters = None
    Microinches = None
    Microns = None
    Miles = None
    Millimeters = None
    Mils = None
    Nanometers = None
    NauticalMile = None
    None = None
    Parsecs = None
    PrinterPica = None
    PrinterPoint = None
    value__ = None
    Yards = None


# variables with complex values

