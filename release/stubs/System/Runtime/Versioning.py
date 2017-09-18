# encoding: utf-8
# module System.Runtime.Versioning calls itself Versioning
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class CompatibilitySwitch(object):
    # no doc
    @staticmethod
    def GetValue(compatibilitySwitchName):
        """ GetValue(compatibilitySwitchName: str) -> str """
        pass

    @staticmethod
    def IsEnabled(compatibilitySwitchName):
        """ IsEnabled(compatibilitySwitchName: str) -> bool """
        pass

    __all__ = [
        'GetValue',
        'IsEnabled',
    ]


class ComponentGuaranteesAttribute(Attribute, _Attribute):
    """
    Defines the compatibility guarantee of a component, type, or type member that may span multiple versions.
    
    ComponentGuaranteesAttribute(guarantees: ComponentGuaranteesOptions)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, guarantees):
        """ __new__(cls: type, guarantees: ComponentGuaranteesOptions) """
        pass

    Guarantees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates the guaranteed level of compatibility of a library, type, or type member that spans multiple versions.

Get: Guarantees(self: ComponentGuaranteesAttribute) -> ComponentGuaranteesOptions

"""



class ComponentGuaranteesOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the compatibility guarantee of a component, type, or type member that may span multiple versions.
    
    enum (flags) ComponentGuaranteesOptions, values: Exchange (1), None (0), SideBySide (4), Stable (2)
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

    Exchange = None
    None = None
    SideBySide = None
    Stable = None
    value__ = None


class FrameworkName(object, IEquatable[FrameworkName]):
    """
    Represents the name of a version of the .NET Framework.
    
    FrameworkName(identifier: str, version: Version)
    FrameworkName(identifier: str, version: Version, profile: str)
    FrameworkName(frameworkName: str)
    """
    def Equals(self, *__args):
        """
        Equals(self: FrameworkName, other: FrameworkName) -> bool
        
            Returns a value that indicates whether this System.Runtime.Versioning.FrameworkName instance 
             represents the same .NET Framework version as a specified 
             System.Runtime.Versioning.FrameworkName instance.
        
        
            other: The object to compare to the current instance.
            Returns: true if every component of the current System.Runtime.Versioning.FrameworkName object matches 
             the corresponding component of other; otherwise, false.
        
        Equals(self: FrameworkName, obj: object) -> bool
        
            Returns a value that indicates whether this System.Runtime.Versioning.FrameworkName instance 
             represents the same .NET Framework version as a specified object.
        
        
            obj: The object to compare to the current instance.
            Returns: true if every component of the current System.Runtime.Versioning.FrameworkName object matches 
             the corresponding component of obj; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: FrameworkName) -> int
        
            Returns the hash code for the System.Runtime.Versioning.FrameworkName object.
            Returns: A 32-bit signed integer that represents the hash code of this instance.
        """
        pass

    def ToString(self):
        """
        ToString(self: FrameworkName) -> str
        
            Returns the string representation of this System.Runtime.Versioning.FrameworkName object.
            Returns: A string that represents this System.Runtime.Versioning.FrameworkName object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, identifier: str, version: Version)
        __new__(cls: type, identifier: str, version: Version, profile: str)
        __new__(cls: type, frameworkName: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the full name of this System.Runtime.Versioning.FrameworkName object.

Get: FullName(self: FrameworkName) -> str

"""

    Identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the identifier of this System.Runtime.Versioning.FrameworkName object.

Get: Identifier(self: FrameworkName) -> str

"""

    Profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the profile name of this System.Runtime.Versioning.FrameworkName object.

Get: Profile(self: FrameworkName) -> str

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the version of this System.Runtime.Versioning.FrameworkName object.

Get: Version(self: FrameworkName) -> Version

"""



class ResourceConsumptionAttribute(Attribute, _Attribute):
    """
    Specifies the resource consumed by the member of a class. This class cannot be inherited.
    
    ResourceConsumptionAttribute(resourceScope: ResourceScope)
    ResourceConsumptionAttribute(resourceScope: ResourceScope, consumptionScope: ResourceScope)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, resourceScope, consumptionScope=None):
        """
        __new__(cls: type, resourceScope: ResourceScope)
        __new__(cls: type, resourceScope: ResourceScope, consumptionScope: ResourceScope)
        """
        pass

    ConsumptionScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the consumption scope for this member.

Get: ConsumptionScope(self: ResourceConsumptionAttribute) -> ResourceScope

"""

    ResourceScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the resource scope for the consumed resource.

Get: ResourceScope(self: ResourceConsumptionAttribute) -> ResourceScope

"""



class ResourceExposureAttribute(Attribute, _Attribute):
    """
    Specifies the resource exposure for a member of a class. This class cannot be inherited.
    
    ResourceExposureAttribute(exposureLevel: ResourceScope)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, exposureLevel):
        """ __new__(cls: type, exposureLevel: ResourceScope) """
        pass

    ResourceExposureLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the resource exposure scope.

Get: ResourceExposureLevel(self: ResourceExposureAttribute) -> ResourceScope

"""



class ResourceScope(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies the scope of a sharable resource.
    
    enum (flags) ResourceScope, values: AppDomain (4), Assembly (32), Library (8), Machine (1), None (0), Private (16), Process (2)
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

    AppDomain = None
    Assembly = None
    Library = None
    Machine = None
    None = None
    Private = None
    Process = None
    value__ = None


class TargetFrameworkAttribute(Attribute, _Attribute):
    """
    Identifies the version of the .NET Framework that a particular assembly was compiled against.
    
    TargetFrameworkAttribute(frameworkName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, frameworkName):
        """ __new__(cls: type, frameworkName: str) """
        pass

    FrameworkDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the display name of the .NET Framework version against which an assembly was built.

Get: FrameworkDisplayName(self: TargetFrameworkAttribute) -> str

Set: FrameworkDisplayName(self: TargetFrameworkAttribute) = value
"""

    FrameworkName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the .NET Framework version against which a particular assembly was compiled.

Get: FrameworkName(self: TargetFrameworkAttribute) -> str

"""



class VersioningHelper(object):
    """ Provides methods to aid developers in writing version-safe code. This class cannot be inherited. """
    @staticmethod
    def MakeVersionSafeName(name, from, to, type=None):
        """
        MakeVersionSafeName(name: str, from: ResourceScope, to: ResourceScope) -> str
        
            Returns a version-safe name based on the specified resource name and the intended resource 
             consumption source.
        
        
            name: The name of the resource.
            from: The scope of the resource.
            to: The desired resource consumption scope.
            Returns: A version-safe name.
        MakeVersionSafeName(name: str, from: ResourceScope, to: ResourceScope, type: Type) -> str
        
            Returns a version-safe name based on the specified resource name, the intended resource 
             consumption scope, and the type using the resource.
        
        
            name: The name of the resource.
            from: The beginning of the scope range.
            to: The end of the scope range.
            type: The System.Type of the resource.
            Returns: A version-safe name.
        """
        pass

    __all__ = [
        'MakeVersionSafeName',
    ]


