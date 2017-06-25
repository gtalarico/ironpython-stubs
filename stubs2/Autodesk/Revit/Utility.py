# encoding: utf-8
# module Autodesk.Revit.Utility calls itself Utility
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AssetProperty(object, IDisposable):
    """ Represents a property of material. """
    def Dispose(self):
        """ Dispose(self: AssetProperty) """
        pass

    def GetAllConnectedProperties(self):
        """
        GetAllConnectedProperties(self: AssetProperty) -> IList[AssetProperty]
        
            Gets the list of the connected properties.
           Connected properties are the 
             detachable properties of an AssetProperty.
           e.g. diffuse property can have 
             texture as its connected property. It can also detach texture on runtime.
        
            Returns: A list of the connected properties.
        """
        pass

    def GetConnectedPropertiesNames(self):
        """
        GetConnectedPropertiesNames(self: AssetProperty) -> IList[str]
        
            Gets names of all connected properties.
            Returns: A list of the names of the connected properties.
        """
        pass

    def GetConnectedProperty(self, *__args):
        """
        GetConnectedProperty(self: AssetProperty, index: int) -> AssetProperty
        
            Gets one connected property with specified index.
            Returns: The AProperty of that index.
        GetConnectedProperty(self: AssetProperty, name: str) -> AssetProperty
        
            Gets a connected property by its name.
        
            name: Name of the property.
            Returns: The property with the specified name.
        """
        pass

    @staticmethod
    def GetTypeName(type):
        """
        GetTypeName(type: AssetPropertyType) -> str
        
            Get the name of the AssetProperty
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the object is read-only or modifiable.
   If true, the object may not be modified.  If false, the object's contents may be modified.

Get: IsReadOnly(self: AssetProperty) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: AssetProperty) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the name of the AssetProperty

Get: Name(self: AssetProperty) -> str

"""

    NumberOfConnectedProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of currently connected properties.

Get: NumberOfConnectedProperties(self: AssetProperty) -> int

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the type of the AssetProperty

Get: Type(self: AssetProperty) -> AssetPropertyType

"""



class AssetProperties(AssetProperty, IDisposable):
    """ Represents a set of asset property(s). """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of the AssetProperty(s) in the object.

Get: Size(self: AssetProperties) -> int

"""



class Asset(AssetProperties, IDisposable):
    """ Represents the properties of a material pertinent to rendering. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AssetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of the item the asset represents.

Get: AssetType(self: Asset) -> AssetType

"""

    LibraryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the library the asset belongs to.

Get: LibraryName(self: Asset) -> str

"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The title of the asset.

Get: Title(self: Asset) -> str

"""



class AssetPropertyBoolean(AssetProperty, IDisposable):
    """ Represents a property of Boolean value. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value of the property

Get: Value(self: AssetPropertyBoolean) -> bool

"""



class AssetPropertyDistance(AssetProperty, IDisposable):
    """ Represents a property of distance value. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    DisplayUnitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unit type of the property

Get: DisplayUnitType(self: AssetPropertyDistance) -> DisplayUnitType

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of the property

Get: Value(self: AssetPropertyDistance) -> float

"""



class AssetPropertyDouble(AssetProperty, IDisposable):
    """ Represents a property of double value. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value of the property

Get: Value(self: AssetPropertyDouble) -> float

"""



class AssetPropertyDoubleArray2d(AssetProperty, IDisposable):
    """ Represents a property consisting of an array of double values. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value of the property

Get: Value(self: AssetPropertyDoubleArray2d) -> DoubleArray

"""



class AssetPropertyDoubleArray3d(AssetProperty, IDisposable):
    """ Represents a property consisting of an array of double values. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value of the property

Get: Value(self: AssetPropertyDoubleArray3d) -> DoubleArray

"""



class AssetPropertyDoubleArray4d(AssetProperty, IDisposable):
    """ Represents a property consisting of an array of double values. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value of the property

Get: Value(self: AssetPropertyDoubleArray4d) -> DoubleArray

"""



class AssetPropertyDoubleMatrix44(AssetProperty, IDisposable):
    """ Represents a property consisting of an array of double values. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value of the property

Get: Value(self: AssetPropertyDoubleMatrix44) -> DoubleArray

"""



class AssetPropertyEnum(AssetProperty, IDisposable):
    """ Represents a property of enum value. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value of the property

Get: Value(self: AssetPropertyEnum) -> int

"""



class AssetPropertyFloat(AssetProperty, IDisposable):
    """ Represents a property of float value. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value of the property

Get: Value(self: AssetPropertyFloat) -> Single

"""



class AssetPropertyFloatArray(AssetProperty, IDisposable):
    """ Represents a property consisting of an array of float values. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def GetValue(self):
        """
        GetValue(self: AssetPropertyFloatArray) -> IList[Single]
        
            Get the value of the property.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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


class AssetPropertyInt64(AssetProperty, IDisposable):
    """ Represents a property of Int64 value. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value of the property.

Get: Value(self: AssetPropertyInt64) -> Int64

"""



class AssetPropertyInteger(AssetProperty, IDisposable):
    """ Represents a property of integer value. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value of the property

Get: Value(self: AssetPropertyInteger) -> int

"""



class AssetPropertyList(AssetProperty, IDisposable):
    """ Represents a list of AssetProperty(s). """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def GetValue(self):
        """
        GetValue(self: AssetPropertyList) -> IList[AssetProperty]
        
            Gets collection of properties stored in this property list.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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


class AssetPropertyReference(AssetProperty, IDisposable):
    """ A reference property of material. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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


class AssetPropertyString(AssetProperty, IDisposable):
    """ Represents a property of string value. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value of the property

Get: Value(self: AssetPropertyString) -> str

"""



class AssetPropertyTime(AssetProperty, IDisposable):
    """ Represents a property of DateTime value. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value of the property

Get: Value(self: AssetPropertyTime) -> DateTime

"""



class AssetPropertyType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing AssetProperty Types in Revit.
    
    enum AssetPropertyType, values: APT_Asset (15), APT_Boolean (2), APT_Distance (14), APT_Double (6), APT_Double44 (10), APT_DoubleArray2d (7), APT_DoubleArray3d (8), APT_DoubleArray4d (9), APT_Enum (3), APT_Float (5), APT_FloatArray (20), APT_Int64 (17), APT_Integer (4), APT_List (19), APT_Properties (1), APT_Reference (16), APT_String (11), APT_Time (12), APT_UInt64 (18), APT_Unknown (0)
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

    APT_Asset = None
    APT_Boolean = None
    APT_Distance = None
    APT_Double = None
    APT_Double44 = None
    APT_DoubleArray2d = None
    APT_DoubleArray3d = None
    APT_DoubleArray4d = None
    APT_Enum = None
    APT_Float = None
    APT_FloatArray = None
    APT_Int64 = None
    APT_Integer = None
    APT_List = None
    APT_Properties = None
    APT_Reference = None
    APT_String = None
    APT_Time = None
    APT_UInt64 = None
    APT_Unknown = None
    value__ = None


class AssetPropertyUInt64(AssetProperty, IDisposable):
    """ Represents a property of UInt64 value. """
    def Dispose(self):
        """ Dispose(self: AssetProperty, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetProperty, disposing: bool) """
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

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value of the property.

Get: Value(self: AssetPropertyUInt64) -> UInt64

"""



class AssetSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains assets.
    
    AssetSet()
    """
    def Clear(self):
        """
        Clear(self: AssetSet)
            Removes every asset from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: AssetSet, item: Asset) -> bool
        
            Tests for the existence of a asset within the set.
        
            item: The asset to be searched for.
            Returns: The Contains method returns True if the asset is within the set, otherwise 
             False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: AssetSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: AssetSet, item: Asset) -> int
        
            Removes a specified asset from the set.
        
            item: The asset to be erased.
            Returns: The number of assets that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: AssetSet) -> AssetSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: AssetSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: AssetSet, item: Asset) -> bool
        
            Insert the specified asset into the set.
        
            item: The asset to be inserted into the set.
            Returns: Returns whether the asset was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: AssetSet) -> AssetSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: AssetSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of assets that are in the set.

Get: Size(self: AssetSet) -> int

"""



class AssetSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a asset set.
    
    AssetSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: AssetSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: AssetSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssetSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: AssetSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: AssetSetIterator) -> object

"""



class AssetType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated to list Asset Types in Revit.
    
    enum AssetType, values: Appearance (4), Content (5)
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

    Appearance = None
    Content = None
    value__ = None


