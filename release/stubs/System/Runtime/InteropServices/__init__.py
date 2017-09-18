# encoding: utf-8
# module System.Runtime.InteropServices calls itself InteropServices
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class _Attribute:
    """ Exposes the System.Attribute class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _Attribute, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _Attribute, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _Attribute) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _Attribute, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AllowReversePInvokeCallsAttribute(Attribute, _Attribute):
    """
    Allows an unmanaged method to call a managed method.
    
    AllowReversePInvokeCallsAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ArrayWithOffset(object):
    """
    Encapsulates an array and an offset within the specified array.
    
    ArrayWithOffset(array: object, offset: int)
    """
    def Equals(self, obj):
        """
        Equals(self: ArrayWithOffset, obj: ArrayWithOffset) -> bool
        
            Indicates whether the specified System.Runtime.InteropServices.ArrayWithOffset object matches 
             the current instance.
        
        
            obj: An System.Runtime.InteropServices.ArrayWithOffset object to compare with this instance.
            Returns: true if the specified System.Runtime.InteropServices.ArrayWithOffset object matches the current 
             instance; otherwise, false.
        
        Equals(self: ArrayWithOffset, obj: object) -> bool
        
            Indicates whether the specified object matches the current 
             System.Runtime.InteropServices.ArrayWithOffset object.
        
        
            obj: Object to compare with this instance.
            Returns: true if the object matches this System.Runtime.InteropServices.ArrayWithOffset; otherwise, false.
        """
        pass

    def GetArray(self):
        """
        GetArray(self: ArrayWithOffset) -> object
        
            Returns the managed array referenced by this System.Runtime.InteropServices.ArrayWithOffset.
            Returns: The managed array this instance references.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ArrayWithOffset) -> int
        
            Returns a hash code for this value type.
            Returns: The hash code for this instance.
        """
        pass

    def GetOffset(self):
        """
        GetOffset(self: ArrayWithOffset) -> int
        
            Returns the offset provided when this System.Runtime.InteropServices.ArrayWithOffset was 
             constructed.
        
            Returns: The offset for this instance.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, array, offset):
        """
        __new__(cls: type, array: object, offset: int)
        __new__[ArrayWithOffset]() -> ArrayWithOffset
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass


class AssemblyRegistrationFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines a set of flags used when registering assemblies.
    
    enum (flags) AssemblyRegistrationFlags, values: None (0), SetCodeBase (1)
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

    None = None
    SetCodeBase = None
    value__ = None


class AutomationProxyAttribute(Attribute, _Attribute):
    """
    Specifies whether the type should be marshaled using the Automation marshaler or a custom proxy and stub.
    
    AutomationProxyAttribute(val: bool)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, val):
        """ __new__(cls: type, val: bool) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating the type of marshaler to use.

Get: Value(self: AutomationProxyAttribute) -> bool

"""



class BestFitMappingAttribute(Attribute, _Attribute):
    """
    Controls whether Unicode characters are converted to the closest matching ANSI characters.
    
    BestFitMappingAttribute(BestFitMapping: bool)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, BestFitMapping):
        """ __new__(cls: type, BestFitMapping: bool) """
        pass

    BestFitMapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the best-fit mapping behavior when converting Unicode characters to ANSI characters.

Get: BestFitMapping(self: BestFitMappingAttribute) -> bool

"""


    ThrowOnUnmappableChar = None


class BINDPTR(object):
    """ Use System.Runtime.InteropServices.ComTypes.BINDPTR instead. """
    lpfuncdesc = None
    lptcomp = None
    lpvardesc = None


class BIND_OPTS(object):
    """ Use System.Runtime.InteropServices.ComTypes.BIND_OPTS instead. """
    cbStruct = None
    dwTickCountDeadline = None
    grfFlags = None
    grfMode = None


class BStrWrapper(object):
    """
    Marshals data of type VT_BSTR from managed to unmanaged code. This class cannot be inherited.
    
    BStrWrapper(value: str)
    BStrWrapper(value: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, value):
        """
        __new__(cls: type, value: str)
        __new__(cls: type, value: object)
        """
        pass

    WrappedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the wrapped System.String object to marshal as type VT_BSTR.

Get: WrappedObject(self: BStrWrapper) -> str

"""



class CALLCONV(Enum, IComparable, IFormattable, IConvertible):
    """
    Use System.Runtime.InteropServices.ComTypes.CALLCONV instead.
    
    enum CALLCONV, values: CC_CDECL (1), CC_MACPASCAL (3), CC_MAX (9), CC_MPWCDECL (7), CC_MPWPASCAL (8), CC_MSCPASCAL (2), CC_PASCAL (2), CC_RESERVED (5), CC_STDCALL (4), CC_SYSCALL (6)
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

    CC_CDECL = None
    CC_MACPASCAL = None
    CC_MAX = None
    CC_MPWCDECL = None
    CC_MPWPASCAL = None
    CC_MSCPASCAL = None
    CC_PASCAL = None
    CC_RESERVED = None
    CC_STDCALL = None
    CC_SYSCALL = None
    value__ = None


class CallingConvention(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the calling convention required to call methods implemented in unmanaged code.
    
    enum CallingConvention, values: Cdecl (2), FastCall (5), StdCall (3), ThisCall (4), Winapi (1)
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

    Cdecl = None
    FastCall = None
    StdCall = None
    ThisCall = None
    value__ = None
    Winapi = None


class CharSet(Enum, IComparable, IFormattable, IConvertible):
    """
    Dictates which character set marshaled strings should use.
    
    enum CharSet, values: Ansi (2), Auto (4), None (1), Unicode (3)
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

    Ansi = None
    Auto = None
    None = None
    Unicode = None
    value__ = None


class ClassInterfaceAttribute(Attribute, _Attribute):
    """
    Indicates the type of class interface to be generated for a class exposed to COM, if an interface is generated at all.
    
    ClassInterfaceAttribute(classInterfaceType: ClassInterfaceType)
    ClassInterfaceAttribute(classInterfaceType: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, classInterfaceType):
        """
        __new__(cls: type, classInterfaceType: ClassInterfaceType)
        __new__(cls: type, classInterfaceType: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Runtime.InteropServices.ClassInterfaceType value that describes which type of interface should be generated for the class.

Get: Value(self: ClassInterfaceAttribute) -> ClassInterfaceType

"""



class ClassInterfaceType(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies the type of class interface that is generated for a class.
    
    enum ClassInterfaceType, values: AutoDispatch (1), AutoDual (2), None (0)
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

    AutoDispatch = None
    AutoDual = None
    None = None
    value__ = None


class CoClassAttribute(Attribute, _Attribute):
    """
    Specifies the class identifier of a coclass imported from a type library.
    
    CoClassAttribute(coClass: Type)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, coClass):
        """ __new__(cls: type, coClass: Type) """
        pass

    CoClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the class identifier of the original coclass.

Get: CoClass(self: CoClassAttribute) -> Type

"""



class ComAliasNameAttribute(Attribute, _Attribute):
    """
    Indicates the COM alias for a parameter or field type.
    
    ComAliasNameAttribute(alias: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, alias):
        """ __new__(cls: type, alias: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the alias for the field or parameter as found in the type library when it was imported.

Get: Value(self: ComAliasNameAttribute) -> str

"""



class ComCompatibleVersionAttribute(Attribute, _Attribute):
    """
    Indicates to a COM client that all classes in the current version of an assembly are compatible with classes in an earlier version of the assembly.
    
    ComCompatibleVersionAttribute(major: int, minor: int, build: int, revision: int)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, major, minor, build, revision):
        """ __new__(cls: type, major: int, minor: int, build: int, revision: int) """
        pass

    BuildNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the build number of the assembly.

Get: BuildNumber(self: ComCompatibleVersionAttribute) -> int

"""

    MajorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the major version number of the assembly.

Get: MajorVersion(self: ComCompatibleVersionAttribute) -> int

"""

    MinorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minor version number of the assembly.

Get: MinorVersion(self: ComCompatibleVersionAttribute) -> int

"""

    RevisionNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the revision number of the assembly.

Get: RevisionNumber(self: ComCompatibleVersionAttribute) -> int

"""



class ComConversionLossAttribute(Attribute, _Attribute):
    """
    Indicates that information was lost about a class or interface when it was imported from a type library to an assembly.
    
    ComConversionLossAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ComDefaultInterfaceAttribute(Attribute, _Attribute):
    """
    Specifies a default interface to expose to COM. This class cannot be inherited.
    
    ComDefaultInterfaceAttribute(defaultInterface: Type)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, defaultInterface):
        """ __new__(cls: type, defaultInterface: Type) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Type object that specifies the default interface to expose to COM.

Get: Value(self: ComDefaultInterfaceAttribute) -> Type

"""



class ComEventInterfaceAttribute(Attribute, _Attribute):
    """
    Identifies the source interface and the class that implements the methods of the event interface that is generated when a coclass is imported from a COM type library.
    
    ComEventInterfaceAttribute(SourceInterface: Type, EventProvider: Type)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, SourceInterface, EventProvider):
        """ __new__(cls: type, SourceInterface: Type, EventProvider: Type) """
        pass

    EventProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the class that implements the methods of the event interface.

Get: EventProvider(self: ComEventInterfaceAttribute) -> Type

"""

    SourceInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the original source interface from the type library.

Get: SourceInterface(self: ComEventInterfaceAttribute) -> Type

"""



class ComEventsHelper(object):
    """ Provides methods that enable .NET Framework delegates that handle events to be added and removed from COM objects. """
    @staticmethod
    def Combine(rcw, iid, dispid, d):
        """
        Combine(rcw: object, iid: Guid, dispid: int, d: Delegate)
            Adds a delegate to the invocation list of events originating from a COM object.
        
            rcw: The COM object that triggers the events the caller would like to respond to.
            iid: The identifier of the source interface used by the COM object to trigger events.
            dispid: The dispatch identifier of the method on the source interface.
            d: The delegate to invoke when the COM event is fired.
        """
        pass

    @staticmethod
    def Remove(rcw, iid, dispid, d):
        """
        Remove(rcw: object, iid: Guid, dispid: int, d: Delegate) -> Delegate
        
            Removes a delegate from the invocation list of events originating from a COM object.
        
            rcw: The COM object the delegate is attached to.
            iid: The identifier of the source interface used by the COM object to trigger events.
            dispid: The dispatch identifier of the method on the source interface.
            d: The delegate to remove from the invocation list.
            Returns: The delegate that was removed from the invocation list.
        """
        pass

    __all__ = [
        'Combine',
        'Remove',
    ]


class ExternalException(SystemException, ISerializable, _Exception):
    """
    The base exception type for all COM interop exceptions and structured exception handling (SEH) exceptions.
    
    ExternalException()
    ExternalException(message: str)
    ExternalException(message: str, inner: Exception)
    ExternalException(message: str, errorCode: int)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def ToString(self):
        """
        ToString(self: ExternalException) -> str
        
            Returns a string that contains the HRESULT of the error.
            Returns: A string that represents the HRESULT.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, message: str, errorCode: int)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the HRESULT of the error.

Get: ErrorCode(self: ExternalException) -> int

"""



class COMException(ExternalException, ISerializable, _Exception):
    """
    The exception that is thrown when an unrecognized HRESULT is returned from a COM method call.
    
    COMException()
    COMException(message: str)
    COMException(message: str, inner: Exception)
    COMException(message: str, errorCode: int)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def ToString(self):
        """
        ToString(self: COMException) -> str
        
            Converts the contents of the exception to a string.
            Returns: A string containing the System.Exception.HResult, System.Exception.Message, 
             System.Exception.InnerException, and System.Exception.StackTrace properties of the exception.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, message: str, errorCode: int)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class ComImportAttribute(Attribute, _Attribute):
    """
    Indicates that the attributed type was previously defined in COM.
    
    ComImportAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ComInterfaceType(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies how to expose an interface to COM.
    
    enum ComInterfaceType, values: InterfaceIsDual (0), InterfaceIsIDispatch (2), InterfaceIsIInspectable (3), InterfaceIsIUnknown (1)
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

    InterfaceIsDual = None
    InterfaceIsIDispatch = None
    InterfaceIsIInspectable = None
    InterfaceIsIUnknown = None
    value__ = None


class ComMemberType(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the type of a COM member.
    
    enum ComMemberType, values: Method (0), PropGet (1), PropSet (2)
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

    Method = None
    PropGet = None
    PropSet = None
    value__ = None


class ComRegisterFunctionAttribute(Attribute, _Attribute):
    """
    Specifies the method to call when you register an assembly for use from COM; this enables the execution of user-written code during the registration process.
    
    ComRegisterFunctionAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ComSourceInterfacesAttribute(Attribute, _Attribute):
    """
    Identifies a list of interfaces that are exposed as COM event sources for the attributed class.
    
    ComSourceInterfacesAttribute(sourceInterfaces: str)
    ComSourceInterfacesAttribute(sourceInterface: Type)
    ComSourceInterfacesAttribute(sourceInterface1: Type, sourceInterface2: Type)
    ComSourceInterfacesAttribute(sourceInterface1: Type, sourceInterface2: Type, sourceInterface3: Type)
    ComSourceInterfacesAttribute(sourceInterface1: Type, sourceInterface2: Type, sourceInterface3: Type, sourceInterface4: Type)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, sourceInterfaces: str)
        __new__(cls: type, sourceInterface: Type)
        __new__(cls: type, sourceInterface1: Type, sourceInterface2: Type)
        __new__(cls: type, sourceInterface1: Type, sourceInterface2: Type, sourceInterface3: Type)
        __new__(cls: type, sourceInterface1: Type, sourceInterface2: Type, sourceInterface3: Type, sourceInterface4: Type)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the fully qualified name of the event source interface.

Get: Value(self: ComSourceInterfacesAttribute) -> str

"""



class ComUnregisterFunctionAttribute(Attribute, _Attribute):
    """
    Specifies the method to call when you unregister an assembly for use from COM; this allows for the execution of user-written code during the unregistration process.
    
    ComUnregisterFunctionAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ComVisibleAttribute(Attribute, _Attribute):
    """
    Controls accessibility of an individual managed type or member, or of all types within an assembly, to COM.
    
    ComVisibleAttribute(visibility: bool)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, visibility):
        """ __new__(cls: type, visibility: bool) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the COM type is visible.

Get: Value(self: ComVisibleAttribute) -> bool

"""



class CONNECTDATA(object):
    """ Use System.Runtime.InteropServices.ComTypes.CONNECTDATA instead. """
    dwCookie = None
    pUnk = None


class CriticalHandle(CriticalFinalizerObject, IDisposable):
    """ Represents a wrapper class for handle resources. """
    def Close(self):
        """
        Close(self: CriticalHandle)
            Marks the handle for releasing and freeing resources.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CriticalHandle)
            Releases all resources used by the System.Runtime.InteropServices.CriticalHandle.
        """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """
        ReleaseHandle(self: CriticalHandle) -> bool
        
            When overridden in a derived class, executes the code required to free the handle.
            Returns: true if the handle is released successfully; otherwise, in the event of a catastrophic failure, 
             false. In this case, it generates a releaseHandleFailed MDA Managed Debugging Assistant.
        """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """
        SetHandle(self: CriticalHandle, handle: IntPtr)
            Sets the handle to the specified pre-existing handle.
        
            handle: The pre-existing handle to use.
        """
        pass

    def SetHandleAsInvalid(self):
        """
        SetHandleAsInvalid(self: CriticalHandle)
            Marks a handle as invalid.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, invalidHandleValue: IntPtr) """
        pass

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the handle is closed.

Get: IsClosed(self: CriticalHandle) -> bool

"""

    IsInvalid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value indicating whether the handle value is invalid.

Get: IsInvalid(self: CriticalHandle) -> bool

"""


    handle = None


class CurrencyWrapper(object):
    """
    Wraps objects the marshaler should marshal as a VT_CY.
    
    CurrencyWrapper(obj: Decimal)
    CurrencyWrapper(obj: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, obj):
        """
        __new__(cls: type, obj: Decimal)
        __new__(cls: type, obj: object)
        """
        pass

    WrappedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the wrapped object to be marshaled as type VT_CY.

Get: WrappedObject(self: CurrencyWrapper) -> Decimal

"""



class CustomQueryInterfaceMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates whether the System.Runtime.InteropServices.Marshal.GetComInterfaceForObject(System.Object,System.Type,System.Runtime.InteropServices.CustomQueryInterfaceMode) method's IUnknown::QueryInterface calls can use the System.Runtime.InteropServices.ICustomQueryInterface interface.
    
    enum CustomQueryInterfaceMode, values: Allow (1), Ignore (0)
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

    Allow = None
    Ignore = None
    value__ = None


class CustomQueryInterfaceResult(Enum, IComparable, IFormattable, IConvertible):
    """
    Provides return values for the System.Runtime.InteropServices.ICustomQueryInterface.GetInterface(System.Guid@,System.IntPtr@) method.
    
    enum CustomQueryInterfaceResult, values: Failed (2), Handled (0), NotHandled (1)
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

    Failed = None
    Handled = None
    NotHandled = None
    value__ = None


class DefaultCharSetAttribute(Attribute, _Attribute):
    """
    Specifies the value of the System.Runtime.InteropServices.CharSet enumeration. This class cannot be inherited.
    
    DefaultCharSetAttribute(charSet: CharSet)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, charSet):
        """ __new__(cls: type, charSet: CharSet) """
        pass

    CharSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default value of System.Runtime.InteropServices.CharSet for any call to System.Runtime.InteropServices.DllImportAttribute.

Get: CharSet(self: DefaultCharSetAttribute) -> CharSet

"""



class DefaultDllImportSearchPathsAttribute(Attribute, _Attribute):
    """ DefaultDllImportSearchPathsAttribute(paths: DllImportSearchPath) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, paths):
        """ __new__(cls: type, paths: DllImportSearchPath) """
        pass

    Paths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Paths(self: DefaultDllImportSearchPathsAttribute) -> DllImportSearchPath

"""



class DefaultParameterValueAttribute(Attribute, _Attribute):
    """
    Sets the default value of a parameter when called from a language that supports default parameters. This class cannot be inherited.
    
    DefaultParameterValueAttribute(value: object)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value):
        """ __new__(cls: type, value: object) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default value of a parameter.

Get: Value(self: DefaultParameterValueAttribute) -> object

"""



class DESCKIND(Enum, IComparable, IFormattable, IConvertible):
    """
    Use System.Runtime.InteropServices.ComTypes.DESCKIND instead.
    
    enum DESCKIND, values: DESCKIND_FUNCDESC (1), DESCKIND_IMPLICITAPPOBJ (4), DESCKIND_MAX (5), DESCKIND_NONE (0), DESCKIND_TYPECOMP (3), DESCKIND_VARDESC (2)
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

    DESCKIND_FUNCDESC = None
    DESCKIND_IMPLICITAPPOBJ = None
    DESCKIND_MAX = None
    DESCKIND_NONE = None
    DESCKIND_TYPECOMP = None
    DESCKIND_VARDESC = None
    value__ = None


class DispatchWrapper(object):
    """
    Wraps objects the marshaler should marshal as a VT_DISPATCH.
    
    DispatchWrapper(obj: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: object) """
        pass

    WrappedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object wrapped by the System.Runtime.InteropServices.DispatchWrapper.

Get: WrappedObject(self: DispatchWrapper) -> object

"""



class DispIdAttribute(Attribute, _Attribute):
    """
    Specifies the COM dispatch identifier (DISPID) of a method, field, or property.
    
    DispIdAttribute(dispId: int)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dispId):
        """ __new__(cls: type, dispId: int) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the DISPID for the member.

Get: Value(self: DispIdAttribute) -> int

"""



class DISPPARAMS(object):
    """ Use System.Runtime.InteropServices.ComTypes.DISPPARAMS instead. """
    cArgs = None
    cNamedArgs = None
    rgdispidNamedArgs = None
    rgvarg = None


class DllImportAttribute(Attribute, _Attribute):
    """
    Indicates that the attributed method is exposed by an unmanaged dynamic-link library (DLL) as a static entry point.
    
    DllImportAttribute(dllName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dllName):
        """ __new__(cls: type, dllName: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the DLL file that contains the entry point.

Get: Value(self: DllImportAttribute) -> str

"""


    BestFitMapping = None
    CallingConvention = None
    CharSet = None
    EntryPoint = None
    ExactSpelling = None
    PreserveSig = None
    SetLastError = None
    ThrowOnUnmappableChar = None


class DllImportSearchPath(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) DllImportSearchPath, values: ApplicationDirectory (512), AssemblyDirectory (2), LegacyBehavior (0), SafeDirectories (4096), System32 (2048), UseDllDirectoryForDependencies (256), UserDirectories (1024) """
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

    ApplicationDirectory = None
    AssemblyDirectory = None
    LegacyBehavior = None
    SafeDirectories = None
    System32 = None
    UseDllDirectoryForDependencies = None
    UserDirectories = None
    value__ = None


class ELEMDESC(object):
    """ Use System.Runtime.InteropServices.ComTypes.ELEMDESC instead. """
    desc = None
    DESCUNION = None
    tdesc = None


class ErrorWrapper(object):
    """
    Wraps objects the marshaler should marshal as a VT_ERROR.
    
    ErrorWrapper(errorCode: int)
    ErrorWrapper(errorCode: object)
    ErrorWrapper(e: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, errorCode: int)
        __new__(cls: type, errorCode: object)
        __new__(cls: type, e: Exception)
        """
        pass

    ErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error code of the wrapper.

Get: ErrorCode(self: ErrorWrapper) -> int

"""



class EXCEPINFO(object):
    """ Use System.Runtime.InteropServices.ComTypes.EXCEPINFO instead. """
    bstrDescription = None
    bstrHelpFile = None
    bstrSource = None
    dwHelpContext = None
    pfnDeferredFillIn = None
    pvReserved = None
    wCode = None
    wReserved = None


class ExporterEventKind(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the callbacks that the type library exporter makes when exporting a type library.
    
    enum ExporterEventKind, values: ERROR_REFTOINVALIDASSEMBLY (2), NOTIF_CONVERTWARNING (1), NOTIF_TYPECONVERTED (0)
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

    ERROR_REFTOINVALIDASSEMBLY = None
    NOTIF_CONVERTWARNING = None
    NOTIF_TYPECONVERTED = None
    value__ = None


class ExtensibleClassFactory(object):
    """ Enables customization of managed objects that extend from unmanaged objects during creation. """
    @staticmethod
    def RegisterObjectCreationCallback(callback):
        """
        RegisterObjectCreationCallback(callback: ObjectCreationDelegate)
            Registers a delegate that is called when an instance of a managed type, that extends from an 
             unmanaged type, needs to allocate the aggregated unmanaged object.
        
        
            callback: A delegate that is called in place of CoCreateInstance.
        """
        pass


class FieldOffsetAttribute(Attribute, _Attribute):
    """
    Indicates the physical position of fields within the unmanaged representation of a class or structure.
    
    FieldOffsetAttribute(offset: int)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, offset):
        """ __new__(cls: type, offset: int) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the offset from the beginning of the structure to the beginning of the field.

Get: Value(self: FieldOffsetAttribute) -> int

"""



class FILETIME(object):
    """ Use System.Runtime.InteropServices.ComTypes.FILETIME instead. """
    dwHighDateTime = None
    dwLowDateTime = None


class FUNCDESC(object):
    """ Use System.Runtime.InteropServices.ComTypes.FUNCDESC instead. """
    callconv = None
    cParams = None
    cParamsOpt = None
    cScodes = None
    elemdescFunc = None
    funckind = None
    invkind = None
    lprgelemdescParam = None
    lprgscode = None
    memid = None
    oVft = None
    wFuncFlags = None


class FUNCFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """
    Use System.Runtime.InteropServices.ComTypes.FUNCFLAGS instead.
    
    enum (flags) FUNCFLAGS, values: FUNCFLAG_FBINDABLE (4), FUNCFLAG_FDEFAULTBIND (32), FUNCFLAG_FDEFAULTCOLLELEM (256), FUNCFLAG_FDISPLAYBIND (16), FUNCFLAG_FHIDDEN (64), FUNCFLAG_FIMMEDIATEBIND (4096), FUNCFLAG_FNONBROWSABLE (1024), FUNCFLAG_FREPLACEABLE (2048), FUNCFLAG_FREQUESTEDIT (8), FUNCFLAG_FRESTRICTED (1), FUNCFLAG_FSOURCE (2), FUNCFLAG_FUIDEFAULT (512), FUNCFLAG_FUSESGETLASTERROR (128)
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

    FUNCFLAG_FBINDABLE = None
    FUNCFLAG_FDEFAULTBIND = None
    FUNCFLAG_FDEFAULTCOLLELEM = None
    FUNCFLAG_FDISPLAYBIND = None
    FUNCFLAG_FHIDDEN = None
    FUNCFLAG_FIMMEDIATEBIND = None
    FUNCFLAG_FNONBROWSABLE = None
    FUNCFLAG_FREPLACEABLE = None
    FUNCFLAG_FREQUESTEDIT = None
    FUNCFLAG_FRESTRICTED = None
    FUNCFLAG_FSOURCE = None
    FUNCFLAG_FUIDEFAULT = None
    FUNCFLAG_FUSESGETLASTERROR = None
    value__ = None


class FUNCKIND(Enum, IComparable, IFormattable, IConvertible):
    """
    Use System.Runtime.InteropServices.ComTypes.FUNCKIND instead.
    
    enum FUNCKIND, values: FUNC_DISPATCH (4), FUNC_NONVIRTUAL (2), FUNC_PUREVIRTUAL (1), FUNC_STATIC (3), FUNC_VIRTUAL (0)
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

    FUNC_DISPATCH = None
    FUNC_NONVIRTUAL = None
    FUNC_PUREVIRTUAL = None
    FUNC_STATIC = None
    FUNC_VIRTUAL = None
    value__ = None


class GCHandle(object):
    """ Provides a way to access a managed object from unmanaged memory. """
    def AddrOfPinnedObject(self):
        """
        AddrOfPinnedObject(self: GCHandle) -> IntPtr
        
            Retrieves the address of an object in a System.Runtime.InteropServices.GCHandleType.Pinned 
             handle.
        
            Returns: The address of the of the Pinned object as an System.IntPtr.
        """
        pass

    @staticmethod
    def Alloc(value, type=None):
        """
        Alloc(value: object, type: GCHandleType) -> GCHandle
        
            Allocates a handle of the specified type for the specified object.
        
            value: The object that uses the System.Runtime.InteropServices.GCHandle.
            type: One of the System.Runtime.InteropServices.GCHandleType values, indicating the type of 
             System.Runtime.InteropServices.GCHandle to create.
        
            Returns: A new System.Runtime.InteropServices.GCHandle of the specified type. This 
             System.Runtime.InteropServices.GCHandle must be released with 
             System.Runtime.InteropServices.GCHandle.Free when it is no longer needed.
        
        Alloc(value: object) -> GCHandle
        
            Allocates a System.Runtime.InteropServices.GCHandleType.Normal handle for the specified object.
        
            value: The object that uses the System.Runtime.InteropServices.GCHandle.
            Returns: A new System.Runtime.InteropServices.GCHandle that protects the object from garbage collection. 
             This System.Runtime.InteropServices.GCHandle must be released with 
             System.Runtime.InteropServices.GCHandle.Free when it is no longer needed.
        """
        pass

    def Equals(self, o):
        """
        Equals(self: GCHandle, o: object) -> bool
        
            Determines whether the specified System.Runtime.InteropServices.GCHandle object is equal to the 
             current System.Runtime.InteropServices.GCHandle object.
        
        
            o: The System.Runtime.InteropServices.GCHandle object to compare with the current 
             System.Runtime.InteropServices.GCHandle object.
        
            Returns: true if the specified System.Runtime.InteropServices.GCHandle object is equal to the current 
             System.Runtime.InteropServices.GCHandle object; otherwise, false.
        """
        pass

    def Free(self):
        """
        Free(self: GCHandle)
            Releases a System.Runtime.InteropServices.GCHandle.
        """
        pass

    @staticmethod
    def FromIntPtr(value):
        """
        FromIntPtr(value: IntPtr) -> GCHandle
        
            Returns a new System.Runtime.InteropServices.GCHandle object created from a handle to a managed 
             object.
        
        
            value: An System.IntPtr handle to a managed object to create a System.Runtime.InteropServices.GCHandle 
             object from.
        
            Returns: A new System.Runtime.InteropServices.GCHandle object that corresponds to the value parameter.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: GCHandle) -> int
        
            Returns an identifier for the current System.Runtime.InteropServices.GCHandle object.
            Returns: An identifier for the current System.Runtime.InteropServices.GCHandle object.
        """
        pass

    @staticmethod
    def ToIntPtr(value):
        """
        ToIntPtr(value: GCHandle) -> IntPtr
        
            Returns the internal integer representation of a System.Runtime.InteropServices.GCHandle object.
        
            value: A System.Runtime.InteropServices.GCHandle object to retrieve an internal integer representation 
             from.
        
            Returns: An System.IntPtr object that represents a System.Runtime.InteropServices.GCHandle object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsAllocated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the handle is allocated.

Get: IsAllocated(self: GCHandle) -> bool

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object this handle represents.

Get: Target(self: GCHandle) -> object

Set: Target(self: GCHandle) = value
"""



class GCHandleType(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents the types of handles the System.Runtime.InteropServices.GCHandle class can allocate.
    
    enum GCHandleType, values: Normal (2), Pinned (3), Weak (0), WeakTrackResurrection (1)
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

    Normal = None
    Pinned = None
    value__ = None
    Weak = None
    WeakTrackResurrection = None


class GuidAttribute(Attribute, _Attribute):
    """
    Supplies an explicit System.Guid when an automatic GUID is undesirable.
    
    GuidAttribute(guid: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, guid):
        """ __new__(cls: type, guid: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Guid of the class.

Get: Value(self: GuidAttribute) -> str

"""



class HandleCollector(object):
    """
    Tracks outstanding handles and forces a garbage collection when the specified threshold is reached.
    
    HandleCollector(name: str, initialThreshold: int)
    HandleCollector(name: str, initialThreshold: int, maximumThreshold: int)
    """
    def Add(self):
        """
        Add(self: HandleCollector)
            Increments the current handle count.
        """
        pass

    def Remove(self):
        """
        Remove(self: HandleCollector)
            Decrements the current handle count.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, initialThreshold, maximumThreshold=None):
        """
        __new__(cls: type, name: str, initialThreshold: int)
        __new__(cls: type, name: str, initialThreshold: int, maximumThreshold: int)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of handles collected.

Get: Count(self: HandleCollector) -> int

"""

    InitialThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies the point at which collections should begin.

Get: InitialThreshold(self: HandleCollector) -> int

"""

    MaximumThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies the point at which collections must occur.

Get: MaximumThreshold(self: HandleCollector) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of a System.Runtime.InteropServices.HandleCollector object.

Get: Name(self: HandleCollector) -> str

"""



class HandleRef(object):
    """
    Wraps a managed object holding a handle to a resource that is passed to unmanaged code using platform invoke.
    
    HandleRef(wrapper: object, handle: IntPtr)
    """
    @staticmethod
    def ToIntPtr(value):
        """
        ToIntPtr(value: HandleRef) -> IntPtr
        
            Returns the internal integer representation of a System.Runtime.InteropServices.HandleRef object.
        
            value: A System.Runtime.InteropServices.HandleRef object to retrieve an internal integer representation 
             from.
        
            Returns: An System.IntPtr object that represents a System.Runtime.InteropServices.HandleRef object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, wrapper, handle):
        """
        __new__(cls: type, wrapper: object, handle: IntPtr)
        __new__[HandleRef]() -> HandleRef
        """
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the handle to a resource.

Get: Handle(self: HandleRef) -> IntPtr

"""

    Wrapper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object holding the handle to a resource.

Get: Wrapper(self: HandleRef) -> object

"""



class ICustomAdapter:
    """ Provides a way for clients to access the actual object, rather than the adapter object handed out by a custom marshaler. """
    def GetUnderlyingObject(self):
        """
        GetUnderlyingObject(self: ICustomAdapter) -> object
        
            Provides access to the underlying object wrapped by a custom marshaler.
            Returns: The object contained by the adapter object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ICustomFactory:
    """ Enables users to write activation code for managed objects that extend System.MarshalByRefObject. """
    def CreateInstance(self, serverType):
        """
        CreateInstance(self: ICustomFactory, serverType: Type) -> MarshalByRefObject
        
            Creates a new instance of the specified type.
        
            serverType: The type to activate.
            Returns: A System.MarshalByRefObject associated with the specified type.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ICustomMarshaler:
    """ Provides custom wrappers for handling method calls. """
    def CleanUpManagedData(self, ManagedObj):
        """
        CleanUpManagedData(self: ICustomMarshaler, ManagedObj: object)
            Performs necessary cleanup of the managed data when it is no longer needed.
        
            ManagedObj: The managed object to be destroyed.
        """
        pass

    def CleanUpNativeData(self, pNativeData):
        """
        CleanUpNativeData(self: ICustomMarshaler, pNativeData: IntPtr)
            Performs necessary cleanup of the unmanaged data when it is no longer needed.
        
            pNativeData: A pointer to the unmanaged data to be destroyed.
        """
        pass

    def GetNativeDataSize(self):
        """
        GetNativeDataSize(self: ICustomMarshaler) -> int
        
            Returns the size of the native data to be marshaled.
            Returns: The size, in bytes, of the native data.
        """
        pass

    def MarshalManagedToNative(self, ManagedObj):
        """
        MarshalManagedToNative(self: ICustomMarshaler, ManagedObj: object) -> IntPtr
        
            Converts the managed data to unmanaged data.
        
            ManagedObj: The managed object to be converted.
            Returns: A pointer to the COM view of the managed object.
        """
        pass

    def MarshalNativeToManaged(self, pNativeData):
        """
        MarshalNativeToManaged(self: ICustomMarshaler, pNativeData: IntPtr) -> object
        
            Converts the unmanaged data to managed data.
        
            pNativeData: A pointer to the unmanaged data to be wrapped.
            Returns: An object that represents the managed view of the COM data.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ICustomQueryInterface:
    """ Enables developers to provide a custom, managed implementation of the IUnknown::QueryInterface(REFIID riid, void **ppvObject) method. """
    def GetInterface(self, iid, ppv):
        """
        GetInterface(self: ICustomQueryInterface, iid: Guid) -> (CustomQueryInterfaceResult, Guid, IntPtr)
        
            Returns an interface according to a specified interface ID.
        
            iid: The GUID of the requested interface.
            Returns: One of the enumeration values that indicates whether a custom implementation of 
             IUnknown::QueryInterface was used.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDispatchImplAttribute(Attribute, _Attribute):
    """
    Indicates which IDispatch implementation the common language runtime uses when exposing dual interfaces and dispinterfaces to COM.
    
    IDispatchImplAttribute(implType: IDispatchImplType)
    IDispatchImplAttribute(implType: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, implType):
        """
        __new__(cls: type, implType: IDispatchImplType)
        __new__(cls: type, implType: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Runtime.InteropServices.IDispatchImplType value used by the class.

Get: Value(self: IDispatchImplAttribute) -> IDispatchImplType

"""



class IDispatchImplType(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates which IDispatch implementation to use for a particular class.
    
    enum IDispatchImplType, values: CompatibleImpl (2), InternalImpl (1), SystemDefinedImpl (0)
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

    CompatibleImpl = None
    InternalImpl = None
    SystemDefinedImpl = None
    value__ = None


class IDLDESC(object):
    """ Use System.Runtime.InteropServices.ComTypes.IDLDESC instead. """
    dwReserved = None
    wIDLFlags = None


class IDLFLAG(Enum, IComparable, IFormattable, IConvertible):
    """
    Use System.Runtime.InteropServices.ComTypes.IDLFLAG instead.
    
    enum (flags) IDLFLAG, values: IDLFLAG_FIN (1), IDLFLAG_FLCID (4), IDLFLAG_FOUT (2), IDLFLAG_FRETVAL (8), IDLFLAG_NONE (0)
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

    IDLFLAG_FIN = None
    IDLFLAG_FLCID = None
    IDLFLAG_FOUT = None
    IDLFLAG_FRETVAL = None
    IDLFLAG_NONE = None
    value__ = None


class IMPLTYPEFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """
    Use System.Runtime.InteropServices.ComTypes.IMPLTYPEFLAGS instead.
    
    enum (flags) IMPLTYPEFLAGS, values: IMPLTYPEFLAG_FDEFAULT (1), IMPLTYPEFLAG_FDEFAULTVTABLE (8), IMPLTYPEFLAG_FRESTRICTED (4), IMPLTYPEFLAG_FSOURCE (2)
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

    IMPLTYPEFLAG_FDEFAULT = None
    IMPLTYPEFLAG_FDEFAULTVTABLE = None
    IMPLTYPEFLAG_FRESTRICTED = None
    IMPLTYPEFLAG_FSOURCE = None
    value__ = None


class ImportedFromTypeLibAttribute(Attribute, _Attribute):
    """
    Indicates that the types defined within an assembly were originally defined in a type library.
    
    ImportedFromTypeLibAttribute(tlbFile: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, tlbFile):
        """ __new__(cls: type, tlbFile: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the original type library file.

Get: Value(self: ImportedFromTypeLibAttribute) -> str

"""



class ImporterEventKind(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the callbacks that the type library importer makes when importing a type library.
    
    enum ImporterEventKind, values: ERROR_REFTOINVALIDTYPELIB (2), NOTIF_CONVERTWARNING (1), NOTIF_TYPECONVERTED (0)
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

    ERROR_REFTOINVALIDTYPELIB = None
    NOTIF_CONVERTWARNING = None
    NOTIF_TYPECONVERTED = None
    value__ = None


class InAttribute(Attribute, _Attribute):
    """
    Indicates that data should be marshaled from the caller to the callee, but not back to the caller.
    
    InAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InterfaceTypeAttribute(Attribute, _Attribute):
    """
    Indicates whether a managed interface is dual, dispatch-only, or IUnknown -only when exposed to COM.
    
    InterfaceTypeAttribute(interfaceType: ComInterfaceType)
    InterfaceTypeAttribute(interfaceType: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, interfaceType):
        """
        __new__(cls: type, interfaceType: ComInterfaceType)
        __new__(cls: type, interfaceType: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Runtime.InteropServices.ComInterfaceType value that describes how the interface should be exposed to COM.

Get: Value(self: InterfaceTypeAttribute) -> ComInterfaceType

"""



class InvalidComObjectException(SystemException, ISerializable, _Exception):
    """
    The exception thrown when an invalid COM object is used.
    
    InvalidComObjectException()
    InvalidComObjectException(message: str)
    InvalidComObjectException(message: str, inner: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class InvalidOleVariantTypeException(SystemException, ISerializable, _Exception):
    """
    The exception thrown by the marshaler when it encounters an argument of a variant type that can not be marshaled to managed code.
    
    InvalidOleVariantTypeException()
    InvalidOleVariantTypeException(message: str)
    InvalidOleVariantTypeException(message: str, inner: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class INVOKEKIND(Enum, IComparable, IFormattable, IConvertible):
    """
    Use System.Runtime.InteropServices.ComTypes.INVOKEKIND instead.
    
    enum INVOKEKIND, values: INVOKE_FUNC (1), INVOKE_PROPERTYGET (2), INVOKE_PROPERTYPUT (4), INVOKE_PROPERTYPUTREF (8)
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

    INVOKE_FUNC = None
    INVOKE_PROPERTYGET = None
    INVOKE_PROPERTYPUT = None
    INVOKE_PROPERTYPUTREF = None
    value__ = None


class IRegistrationServices:
    """ Provides a set of services for registering and unregistering managed assemblies for use from COM. """
    def GetManagedCategoryGuid(self):
        """
        GetManagedCategoryGuid(self: IRegistrationServices) -> Guid
        
            Returns the GUID of the COM category that contains the managed classes.
            Returns: The GUID of the COM category that contains the managed classes.
        """
        pass

    def GetProgIdForType(self, type):
        """
        GetProgIdForType(self: IRegistrationServices, type: Type) -> str
        
            Retrieves the COM ProgID for a specified type.
        
            type: The type whose ProgID is being requested.
            Returns: The ProgID for the specified type.
        """
        pass

    def GetRegistrableTypesInAssembly(self, assembly):
        """
        GetRegistrableTypesInAssembly(self: IRegistrationServices, assembly: Assembly) -> Array[Type]
        
            Retrieves a list of classes in an assembly that would be registered by a call to 
             System.Runtime.InteropServices.IRegistrationServices.RegisterAssembly(System.Reflection.Assembly,
             System.Runtime.InteropServices.AssemblyRegistrationFlags).
        
        
            assembly: The assembly to search for classes.
            Returns: A System.Type array containing a list of classes in assembly.
        """
        pass

    def RegisterAssembly(self, assembly, flags):
        """
        RegisterAssembly(self: IRegistrationServices, assembly: Assembly, flags: AssemblyRegistrationFlags) -> bool
        
            Registers the classes in a managed assembly to enable creation from COM.
        
            assembly: The assembly to be registered.
            flags: An System.Runtime.InteropServices.AssemblyRegistrationFlags value indicating any special 
             settings needed when registering assembly.
        
            Returns: true if assembly contains types that were successfully registered; otherwise false if the 
             assembly contains no eligible types.
        """
        pass

    def RegisterTypeForComClients(self, type, g):
        """
        RegisterTypeForComClients(self: IRegistrationServices, type: Type, g: Guid) -> Guid
        
            Registers the specified type with COM using the specified GUID.
        
            type: The type to be registered for use from COM.
            g: GUID used to register the specified type.
        """
        pass

    def TypeRepresentsComType(self, type):
        """
        TypeRepresentsComType(self: IRegistrationServices, type: Type) -> bool
        
            Determines whether the specified type is a COM type.
        
            type: The type to determine if it is a COM type.
            Returns: true if the specified type is a COM type; otherwise false.
        """
        pass

    def TypeRequiresRegistration(self, type):
        """
        TypeRequiresRegistration(self: IRegistrationServices, type: Type) -> bool
        
            Determines whether the specified type requires registration.
        
            type: The type to check for COM registration requirements.
            Returns: true if the type must be registered for use from COM; otherwise false.
        """
        pass

    def UnregisterAssembly(self, assembly):
        """
        UnregisterAssembly(self: IRegistrationServices, assembly: Assembly) -> bool
        
            Unregisters the classes in a managed assembly.
        
            assembly: The assembly to be unregistered.
            Returns: true if assembly contains types that were successfully unregistered; otherwise false if the 
             assembly contains no eligible types.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeLibConverter:
    """ Provides a set of services that convert a managed assembly to a COM type library and vice versa. """
    def ConvertAssemblyToTypeLib(self, assembly, typeLibName, flags, notifySink):
        """
        ConvertAssemblyToTypeLib(self: ITypeLibConverter, assembly: Assembly, typeLibName: str, flags: TypeLibExporterFlags, notifySink: ITypeLibExporterNotifySink) -> object
        
            Converts an assembly to a COM type library.
        
            assembly: The assembly to convert.
            typeLibName: The file name of the resulting type library.
            flags: A System.Runtime.InteropServices.TypeLibExporterFlags value indicating any special settings.
            notifySink: The System.Runtime.InteropServices.ITypeLibExporterNotifySink interface implemented by the 
             caller.
        
            Returns: An object that implements the ITypeLib interface.
        """
        pass

    def ConvertTypeLibToAssembly(self, typeLib, asmFileName, flags, notifySink, publicKey, keyPair, *__args):
        """
        ConvertTypeLibToAssembly(self: ITypeLibConverter, typeLib: object, asmFileName: str, flags: int, notifySink: ITypeLibImporterNotifySink, publicKey: Array[Byte], keyPair: StrongNameKeyPair, unsafeInterfaces: bool) -> AssemblyBuilder
        
            Converts a COM type library to an assembly.
        
            typeLib: The object that implements the ITypeLib interface.
            asmFileName: The file name of the resulting assembly.
            flags: A System.Runtime.InteropServices.TypeLibImporterFlags value indicating any special settings.
            notifySink: System.Runtime.InteropServices.ITypeLibImporterNotifySink interface implemented by the caller.
            publicKey: A byte array containing the public key.
            keyPair: A System.Reflection.StrongNameKeyPair object containing the public and private cryptographic key 
             pair.
        
            unsafeInterfaces: If true, the interfaces require link time checks for 
             System.Security.Permissions.SecurityPermissionFlag.UnmanagedCode permission. If false, the 
             interfaces require run time checks that require a stack walk and are more expensive, but help 
             provide greater protection.
        
            Returns: An System.Reflection.Emit.AssemblyBuilder object containing the converted type library.
        ConvertTypeLibToAssembly(self: ITypeLibConverter, typeLib: object, asmFileName: str, flags: TypeLibImporterFlags, notifySink: ITypeLibImporterNotifySink, publicKey: Array[Byte], keyPair: StrongNameKeyPair, asmNamespace: str, asmVersion: Version) -> AssemblyBuilder
        
            Converts a COM type library to an assembly.
        
            typeLib: The object that implements the ITypeLib interface.
            asmFileName: The file name of the resulting assembly.
            flags: A System.Runtime.InteropServices.TypeLibImporterFlags value indicating any special settings.
            notifySink: System.Runtime.InteropServices.ITypeLibImporterNotifySink interface implemented by the caller.
            publicKey: A byte array containing the public key.
            keyPair: A System.Reflection.StrongNameKeyPair object containing the public and private cryptographic key 
             pair.
        
            asmNamespace: The namespace for the resulting assembly.
            asmVersion: The version of the resulting assembly. If null, the version of the type library is used.
            Returns: An System.Reflection.Emit.AssemblyBuilder object containing the converted type library.
        """
        pass

    def GetPrimaryInteropAssembly(self, g, major, minor, lcid, asmName, asmCodeBase):
        """
        GetPrimaryInteropAssembly(self: ITypeLibConverter, g: Guid, major: int, minor: int, lcid: int) -> (bool, str, str)
        
            Gets the name and code base of a primary interop assembly for a specified type library.
        
            g: The GUID of the type library.
            major: The major version number of the type library.
            minor: The minor version number of the type library.
            lcid: The LCID of the type library.
            Returns: true if the primary interop assembly was found in the registry; otherwise false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeLibExporterNameProvider:
    """ Provides control over the casing of names when exported to a type library. """
    def GetNames(self):
        """
        GetNames(self: ITypeLibExporterNameProvider) -> Array[str]
        
            Returns a list of names to control the casing of.
            Returns: An array of strings, where each element contains the name of a type to control casing for.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeLibExporterNotifySink:
    """ Provides a callback mechanism for the assembly converter to inform the caller of the status of the conversion, and involve the caller in the conversion process itself. """
    def ReportEvent(self, eventKind, eventCode, eventMsg):
        """
        ReportEvent(self: ITypeLibExporterNotifySink, eventKind: ExporterEventKind, eventCode: int, eventMsg: str)
            Notifies the caller that an event occured during the conversion of an assembly.
        
            eventKind: An System.Runtime.InteropServices.ExporterEventKind value indicating the type of event.
            eventCode: Indicates extra information about the event.
            eventMsg: A message generated by the event.
        """
        pass

    def ResolveRef(self, assembly):
        """
        ResolveRef(self: ITypeLibExporterNotifySink, assembly: Assembly) -> object
        
            Asks the user to resolve a reference to another assembly.
        
            assembly: The assembly to resolve.
            Returns: The type library for assembly.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeLibImporterNotifySink:
    """ Provides a callback mechanism for the type library converter to inform the caller of the status of the conversion, and involve the caller in the conversion process itself. """
    def ReportEvent(self, eventKind, eventCode, eventMsg):
        """
        ReportEvent(self: ITypeLibImporterNotifySink, eventKind: ImporterEventKind, eventCode: int, eventMsg: str)
            Notifies the caller that an event occured during the conversion of a type library.
        
            eventKind: An System.Runtime.InteropServices.ImporterEventKind value indicating the type of event.
            eventCode: Indicates extra information about the event.
            eventMsg: A message generated by the event.
        """
        pass

    def ResolveRef(self, typeLib):
        """
        ResolveRef(self: ITypeLibImporterNotifySink, typeLib: object) -> Assembly
        
            Asks the user to resolve a reference to another type library.
        
            typeLib: The object implementing the ITypeLib interface that needs to be resolved.
            Returns: The assembly corresponding to typeLib.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class LayoutKind(Enum, IComparable, IFormattable, IConvertible):
    """
    Controls the layout of an object when it is exported to unmanaged code.
    
    enum LayoutKind, values: Auto (3), Explicit (2), Sequential (0)
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

    Auto = None
    Explicit = None
    Sequential = None
    value__ = None


class LCIDConversionAttribute(Attribute, _Attribute):
    """
    Indicates that a method's unmanaged signature expects a locale identifier (LCID) parameter.
    
    LCIDConversionAttribute(lcid: int)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, lcid):
        """ __new__(cls: type, lcid: int) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the position of the LCID argument in the unmanaged signature.

Get: Value(self: LCIDConversionAttribute) -> int

"""



class LIBFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """
    Use System.Runtime.InteropServices.ComTypes.LIBFLAGS instead.
    
    enum (flags) LIBFLAGS, values: LIBFLAG_FCONTROL (2), LIBFLAG_FHASDISKIMAGE (8), LIBFLAG_FHIDDEN (4), LIBFLAG_FRESTRICTED (1)
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

    LIBFLAG_FCONTROL = None
    LIBFLAG_FHASDISKIMAGE = None
    LIBFLAG_FHIDDEN = None
    LIBFLAG_FRESTRICTED = None
    value__ = None


class ManagedToNativeComInteropStubAttribute(Attribute, _Attribute):
    """
    Provides support for user customization of interop stubs in managed-to-COM interop scenarios.
    
    ManagedToNativeComInteropStubAttribute(classType: Type, methodName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, classType, methodName):
        """ __new__(cls: type, classType: Type, methodName: str) """
        pass

    ClassType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the class that contains the required stub method.

Get: ClassType(self: ManagedToNativeComInteropStubAttribute) -> Type

"""

    MethodName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the stub method.

Get: MethodName(self: ManagedToNativeComInteropStubAttribute) -> str

"""



class Marshal(object):
    """ Provides a collection of methods for allocating unmanaged memory, copying unmanaged memory blocks, and converting managed to unmanaged types, as well as other miscellaneous methods used when interacting with unmanaged code. """
    @staticmethod
    def AddRef(pUnk):
        """
        AddRef(pUnk: IntPtr) -> int
        
            Increments the reference count on the specified interface.
        
            pUnk: The interface reference count to increment.
            Returns: The new value of the reference count on the pUnk parameter.
        """
        pass

    @staticmethod
    def AllocCoTaskMem(cb):
        """
        AllocCoTaskMem(cb: int) -> IntPtr
        
            Allocates a block of memory of specified size from the COM task memory allocator.
        
            cb: The size of the block of memory to be allocated.
            Returns: An integer representing the address of the block of memory allocated. This memory must be 
             released with System.Runtime.InteropServices.Marshal.FreeCoTaskMem(System.IntPtr).
        """
        pass

    @staticmethod
    def AllocHGlobal(cb):
        """
        AllocHGlobal(cb: int) -> IntPtr
        
            Allocates memory from the unmanaged memory of the process by using the specified number of bytes.
        
            cb: The required number of bytes in memory.
            Returns: A pointer to the newly allocated memory. This memory must be released using the 
             System.Runtime.InteropServices.Marshal.FreeHGlobal(System.IntPtr) method.
        
        AllocHGlobal(cb: IntPtr) -> IntPtr
        
            Allocates memory from the unmanaged memory of the process by using the pointer to the specified 
             number of bytes.
        
        
            cb: The required number of bytes in memory.
            Returns: A pointer to the newly allocated memory. This memory must be released using the 
             System.Runtime.InteropServices.Marshal.FreeHGlobal(System.IntPtr) method.
        """
        pass

    @staticmethod
    def AreComObjectsAvailableForCleanup():
        """
        AreComObjectsAvailableForCleanup() -> bool
        
            Indicates whether runtime callable wrappers (RCWs) from any context are available for cleanup.
            Returns: true if there are any RCWs available for cleanup; otherwise, false.
        """
        pass

    @staticmethod
    def BindToMoniker(monikerName):
        """
        BindToMoniker(monikerName: str) -> object
        
            Gets an interface pointer identified by the specified moniker.
        
            monikerName: The moniker corresponding to the desired interface pointer.
            Returns: An object containing a reference to the interface pointer identified by the monikerName 
             parameter. A moniker is a name, and in this case, the moniker is defined by an interface.
        """
        pass

    @staticmethod
    def ChangeWrapperHandleStrength(otp, fIsWeak):
        """
        ChangeWrapperHandleStrength(otp: object, fIsWeak: bool)
            Changes the strength of an object's COM Callable Wrapper (CCW) handle.
        
            otp: The object whose CCW holds a reference counted handle. The handle is strong if the reference 
             count on the CCW is greater than zero; otherwise, it is weak.
        
            fIsWeak: true to change the strength of the handle on the otp parameter to weak, regardless of its 
             reference count; false to reset the handle strength on otp to be reference counted.
        """
        pass

    @staticmethod
    def CleanupUnusedObjectsInCurrentContext():
        """
        CleanupUnusedObjectsInCurrentContext()
            Notifies the runtime to clean up all Runtime Callable Wrappers (RCWs) allocated in the current 
             context.
        """
        pass

    @staticmethod
    def Copy(source, *__args):
        """
        Copy(source: IntPtr, destination: Array[Int16], startIndex: int, length: int)
            Copies data from an unmanaged memory pointer to a managed 16-bit signed integer array.
        
            source: The memory pointer to copy from.
            destination: The array to copy to.
            startIndex: The zero-based index in the destination  array where copying should start.
            length: The number of array elements to copy.
        Copy(source: IntPtr, destination: Array[Int64], startIndex: int, length: int)
            Copies data from an unmanaged memory pointer to a managed 64-bit signed integer array.
        
            source: The memory pointer to copy from.
            destination: The array to copy to.
            startIndex: The zero-based index in the destination  array where copying should start.
            length: The number of array elements to copy.
        Copy(source: IntPtr, destination: Array[int], startIndex: int, length: int)
            Copies data from an unmanaged memory pointer to a managed 32-bit signed integer array.
        
            source: The memory pointer to copy from.
            destination: The array to copy to.
            startIndex: The zero-based index in the destination  array where copying should start.
            length: The number of array elements to copy.
        Copy(source: IntPtr, destination: Array[Char], startIndex: int, length: int)
            Copies data from an unmanaged memory pointer to a managed character array.
        
            source: The memory pointer to copy from.
            destination: The array to copy to.
            startIndex: The zero-based index in the destination  array where copying should start.
            length: The number of array elements to copy.
        Copy(source: IntPtr, destination: Array[Byte], startIndex: int, length: int)
            Copies data from an unmanaged memory pointer to a managed 8-bit unsigned integer array.
        
            source: The memory pointer to copy from.
            destination: The array to copy to.
            startIndex: The zero-based index in the destination  array where copying should start.
            length: The number of array elements to copy.
        Copy(source: IntPtr, destination: Array[IntPtr], startIndex: int, length: int)
            Copies data from an unmanaged memory pointer to a managed System.IntPtr array.
        
            source: The memory pointer to copy from.
            destination: The array to copy to.
            startIndex: The zero-based index into the destination array where copying should start.
            length: The number of array elements to copy.
        Copy(source: IntPtr, destination: Array[Single], startIndex: int, length: int)
            Copies data from an unmanaged memory pointer to a managed single-precision floating-point number 
             array.
        
        
            source: The memory pointer to copy from.
            destination: The array to copy to.
            startIndex: The zero-based index in the destination  array where copying should start.
            length: The number of array elements to copy.
        Copy(source: IntPtr, destination: Array[float], startIndex: int, length: int)
            Copies data from an unmanaged memory pointer to a managed double-precision floating-point number 
             array.
        
        
            source: The memory pointer to copy from.
            destination: The array to copy to.
            startIndex: The zero-based index in the destination  array where copying should start.
            length: The number of array elements to copy.
        Copy(source: Array[Int16], startIndex: int, destination: IntPtr, length: int)
            Copies data from a one-dimensional, managed 16-bit signed integer array to an unmanaged memory 
             pointer.
        
        
            source: The one-dimensional array to copy from.
            startIndex: The zero-based index in the source array where copying should start.
            destination: The memory pointer to copy to.
            length: The number of array elements to copy.
        Copy(source: Array[Int64], startIndex: int, destination: IntPtr, length: int)
            Copies data from a one-dimensional, managed 64-bit signed integer array to an unmanaged memory 
             pointer.
        
        
            source: The one-dimensional array to copy from.
            startIndex: The zero-based index in the source array where copying should start.
            destination: The memory pointer to copy to.
            length: The number of array elements to copy.
        Copy(source: Array[int], startIndex: int, destination: IntPtr, length: int)
            Copies data from a one-dimensional, managed 32-bit signed integer array to an unmanaged memory 
             pointer.
        
        
            source: The one-dimensional array to copy from.
            startIndex: The zero-based index in the source array where copying should start.
            destination: The memory pointer to copy to.
            length: The number of array elements to copy.
        Copy(source: Array[Char], startIndex: int, destination: IntPtr, length: int)
            Copies data from a one-dimensional, managed character array to an unmanaged memory pointer.
        
            source: The one-dimensional array to copy from.
            startIndex: The zero-based index in the source array where copying should start.
            destination: The memory pointer to copy to.
            length: The number of array elements to copy.
        Copy(source: Array[Byte], startIndex: int, destination: IntPtr, length: int)
            Copies data from a one-dimensional, managed 8-bit unsigned integer array to an unmanaged memory 
             pointer.
        
        
            source: The one-dimensional array to copy from.
            startIndex: The zero-based index in the source array where copying should start.
            destination: The memory pointer to copy to.
            length: The number of array elements to copy.
        Copy(source: Array[IntPtr], startIndex: int, destination: IntPtr, length: int)
            Copies data from a one-dimensional, managed System.IntPtr array to an unmanaged memory pointer.
        
            source: The one-dimensional array to copy from.
            startIndex: The zero-based index into the source array where copying should start.
            destination: The memory pointer to copy to.
            length: The number of array elements to copy.
        Copy(source: Array[Single], startIndex: int, destination: IntPtr, length: int)
            Copies data from a one-dimensional, managed single-precision floating-point number array to an 
             unmanaged memory pointer.
        
        
            source: The one-dimensional array to copy from.
            startIndex: The zero-based index in the source array where copying should start.
            destination: The memory pointer to copy to.
            length: The number of array elements to copy.
        Copy(source: Array[float], startIndex: int, destination: IntPtr, length: int)
            Copies data from a one-dimensional, managed double-precision floating-point number array to an 
             unmanaged memory pointer.
        
        
            source: The one-dimensional array to copy from.
            startIndex: The zero-based index in the source array where copying should start.
            destination: The memory pointer to copy to.
            length: The number of array elements to copy.
        """
        pass

    @staticmethod
    def CreateAggregatedObject(pOuter, o):
        """
        CreateAggregatedObject[T](pOuter: IntPtr, o: T) -> IntPtr
        CreateAggregatedObject(pOuter: IntPtr, o: object) -> IntPtr
        
            Aggregates a managed object with the specified COM object.
        
            pOuter: The outer IUnknown pointer.
            o: An object to aggregate.
            Returns: The inner IUnknown pointer of the managed object.
        """
        pass

    @staticmethod
    def CreateWrapperOfType(o, t=None):
        """
        CreateWrapperOfType[(T, TWrapper)](o: T) -> TWrapper
        CreateWrapperOfType(o: object, t: Type) -> object
        
            Wraps the specified COM object in an object of the specified type.
        
            o: The object to be wrapped.
            t: The type of wrapper to create.
            Returns: The newly wrapped object that is an instance of the desired type.
        """
        pass

    @staticmethod
    def DestroyStructure(ptr, structuretype=None):
        """
        DestroyStructure[T](ptr: IntPtr)DestroyStructure(ptr: IntPtr, structuretype: Type)
            Frees all substructures that the specified unmanaged memory block points to.
        
            ptr: A pointer to an unmanaged block of memory.
            structuretype: Type of a formatted class. This provides the layout information necessary to delete the buffer 
             in the ptr parameter.
        """
        pass

    @staticmethod
    def FinalReleaseComObject(o):
        """
        FinalReleaseComObject(o: object) -> int
        
            Releases all references to a Runtime Callable Wrapper (RCW) by setting its reference count to 0.
        
            o: The RCW to be released.
            Returns: The new value of the reference count of the RCW associated with the oparameter, which is 0 
             (zero) if the release is successful.
        """
        pass

    @staticmethod
    def FreeBSTR(ptr):
        """
        FreeBSTR(ptr: IntPtr)
            Frees a BSTR using the COM SysFreeString function.
        
            ptr: The address of the BSTR to be freed.
        """
        pass

    @staticmethod
    def FreeCoTaskMem(ptr):
        """
        FreeCoTaskMem(ptr: IntPtr)
            Frees a block of memory allocated by the unmanaged COM task memory allocator.
        
            ptr: The address of the memory to be freed.
        """
        pass

    @staticmethod
    def FreeHGlobal(hglobal):
        """
        FreeHGlobal(hglobal: IntPtr)
            Frees memory previously allocated from the unmanaged memory of the process.
        
            hglobal: The handle returned by the original matching call to 
             System.Runtime.InteropServices.Marshal.AllocHGlobal(System.IntPtr).
        """
        pass

    @staticmethod
    def GenerateGuidForType(type):
        """
        GenerateGuidForType(type: Type) -> Guid
        
            Returns the globally unique identifier (GUID) for the specified type, or generates a GUID using 
             the algorithm used by the Type Library Exporter (Tlbexp.exe).
        
        
            type: The type to generate a GUID for.
            Returns: An identifier for the specified type.
        """
        pass

    @staticmethod
    def GenerateProgIdForType(type):
        """
        GenerateProgIdForType(type: Type) -> str
        
            Returns a programmatic identifier (ProgID) for the specified type.
        
            type: The type to get a ProgID for.
            Returns: The ProgID of the specified type.
        """
        pass

    @staticmethod
    def GetActiveObject(progID):
        """
        GetActiveObject(progID: str) -> object
        
            Obtains a running instance of the specified object from the running object table (ROT).
        
            progID: The programmatic identifier (ProgID) of the object that was requested.
            Returns: The object that was requested; otherwise null. You can cast this object to any COM interface 
             that it supports.
        """
        pass

    @staticmethod
    def GetComInterfaceForObject(o, T=None, mode=None):
        """
        GetComInterfaceForObject(o: object, T: Type, mode: CustomQueryInterfaceMode) -> IntPtr
        
            Returns a pointer to an IUnknown interface that represents the specified interface on the 
             specified object. Custom query interface access is controlled by the specified customization 
             mode.
        
        
            o: The object that provides the interface.
            T: The type of interface that is requested.
            mode: One of the enumeration values that indicates whether to apply an IUnknown::QueryInterface 
             customization that is supplied by an System.Runtime.InteropServices.ICustomQueryInterface.
        
            Returns: The interface pointer that represents the interface for the object.
        GetComInterfaceForObject[(T, TInterface)](o: T) -> IntPtr
        GetComInterfaceForObject(o: object, T: Type) -> IntPtr
        
            Returns a pointer to an IUnknown interface that represents the specified interface on the 
             specified object. Custom query interface access is enabled by default.
        
        
            o: The object that provides the interface.
            T: The type of interface that is requested.
            Returns: The interface pointer that represents the specified interface for the object.
        """
        pass

    @staticmethod
    def GetComInterfaceForObjectInContext(o, t):
        """
        GetComInterfaceForObjectInContext(o: object, t: Type) -> IntPtr
        
            Returns an interface pointer that represents the specified interface for an object, if the 
             caller is in the same context as that object.
        
        
            o: The object that provides the interface.
            t: The type of interface that is requested.
            Returns: The interface pointer specified by t that represents the interface for the specified object, or 
             null if the caller is not in the same context as the object.
        """
        pass

    @staticmethod
    def GetComObjectData(obj, key):
        """
        GetComObjectData(obj: object, key: object) -> object
        
            Retrieves data that is referenced by the specified key from the specified COM object.
        
            obj: The COM object that contains the data that you want.
            key: The key in the internal hash table of obj to retrieve the data from.
            Returns: The data represented by the key parameter in the internal hash table of the obj parameter.
        """
        pass

    @staticmethod
    def GetComSlotForMethodInfo(m):
        """
        GetComSlotForMethodInfo(m: MemberInfo) -> int
        
            Retrieves the virtual function table (v-table or VTBL) slot for a specified 
             System.Reflection.MemberInfo type when that type is exposed to COM.
        
        
            m: An object that represents an interface method.
            Returns: The VTBL slot m identifier when it is exposed to COM.
        """
        pass

    @staticmethod
    def GetDelegateForFunctionPointer(ptr, t=None):
        """
        GetDelegateForFunctionPointer[TDelegate](ptr: IntPtr) -> TDelegate
        GetDelegateForFunctionPointer(ptr: IntPtr, t: Type) -> Delegate
        
            Converts an unmanaged function pointer to a delegate.
        
            ptr: The unmanaged function pointer to be converted.
            t: The type of the delegate to be returned.
            Returns: A delegate instance that can be cast to the appropriate delegate type.
        """
        pass

    @staticmethod
    def GetEndComSlot(t):
        """
        GetEndComSlot(t: Type) -> int
        
            Retrieves the last slot in the virtual function table (v-table or VTBL) of a type when exposed 
             to COM.
        
        
            t: A type that represents an interface or class.
            Returns: The last VTBL slot of the interface when exposed to COM. If the t parameter is a class, the 
             returned VTBL slot is the last slot in the interface that is generated from the class.
        """
        pass

    @staticmethod
    def GetExceptionCode():
        """
        GetExceptionCode() -> int
        
            Retrieves a code that identifies the type of the exception that occurred.
            Returns: The type of the exception.
        """
        pass

    @staticmethod
    def GetExceptionForHR(errorCode, errorInfo=None):
        """
        GetExceptionForHR(errorCode: int, errorInfo: IntPtr) -> Exception
        
            Converts the specified HRESULT error code to a corresponding System.Exception object, with 
             additional error information passed in an IErrorInfo interface for the exception object.
        
        
            errorCode: The HRESULT to be converted.
            errorInfo: A pointer to the IErrorInfo interface that provides more information about the error. You can 
             specify IntPtr(0) to use the current IErrorInfo interface, or IntPtr(-1) to ignore the current 
             IErrorInfo interface and construct the exception just from the error code.
        
            Returns: An object that represents the converted HRESULT and information obtained from errorInfo.
        GetExceptionForHR(errorCode: int) -> Exception
        
            Converts the specified HRESULT error code to a corresponding System.Exception object.
        
            errorCode: The HRESULT to be converted.
            Returns: An object that represents the converted HRESULT.
        """
        pass

    @staticmethod
    def GetExceptionPointers():
        """
        GetExceptionPointers() -> IntPtr
        
            Retrieves a computer-independent description of an exception, and information about the state 
             that existed for the thread when the exception occurred.
        
            Returns: A pointer to an EXCEPTION_POINTERS structure.
        """
        pass

    @staticmethod
    def GetFunctionPointerForDelegate(d):
        """
        GetFunctionPointerForDelegate[TDelegate](d: TDelegate) -> IntPtr
        GetFunctionPointerForDelegate(d: Delegate) -> IntPtr
        
            Converts a delegate into a function pointer that is callable from unmanaged code.
        
            d: The delegate to be passed to unmanaged code.
            Returns: A value that can be passed to unmanaged code, which, in turn, can use it to call the underlying 
             managed delegate.
        """
        pass

    @staticmethod
    def GetHINSTANCE(m):
        """
        GetHINSTANCE(m: Module) -> IntPtr
        
            Returns the instance handle (HINSTANCE) for the specified module.
        
            m: The module whose HINSTANCE is desired.
            Returns: The HINSTANCE for m; or -1 if the module does not have an HINSTANCE.
        """
        pass

    @staticmethod
    def GetHRForException(e):
        """
        GetHRForException(e: Exception) -> int
        
            Converts the specified exception to an HRESULT.
        
            e: The exception to convert to an HRESULT.
            Returns: The HRESULT mapped to the supplied exception.
        """
        pass

    @staticmethod
    def GetHRForLastWin32Error():
        """
        GetHRForLastWin32Error() -> int
        
            Returns the HRESULT corresponding to the last error incurred by Win32 code executed using 
             System.Runtime.InteropServices.Marshal.
        
            Returns: The HRESULT corresponding to the last Win32 error code.
        """
        pass

    @staticmethod
    def GetIDispatchForObject(o):
        """
        GetIDispatchForObject(o: object) -> IntPtr
        
            Returns an IDispatch interface from a managed object.
        
            o: The object whose IDispatch interface is requested.
            Returns: The IDispatch pointer for the o parameter.
        """
        pass

    @staticmethod
    def GetIDispatchForObjectInContext(o):
        """
        GetIDispatchForObjectInContext(o: object) -> IntPtr
        
            Returns an IDispatch interface pointer from a managed object, if the caller is in the same 
             context as that object.
        
        
            o: The object whose IDispatch interface is requested.
            Returns: The IDispatch interface pointer for the specified object, or null if the caller is not in the 
             same context as the specified object.
        """
        pass

    @staticmethod
    def GetITypeInfoForType(t):
        """
        GetITypeInfoForType(t: Type) -> IntPtr
        
            Returns a System.Runtime.InteropServices.ComTypes.ITypeInfo interface from a managed type.
        
            t: The type whose ITypeInfo interface is being requested.
            Returns: A pointer to the ITypeInfo interface for the t parameter.
        """
        pass

    @staticmethod
    def GetIUnknownForObject(o):
        """
        GetIUnknownForObject(o: object) -> IntPtr
        
            Returns an IUnknown interface from a managed object.
        
            o: The object whose IUnknown interface is requested.
            Returns: The IUnknown pointer for the o parameter.
        """
        pass

    @staticmethod
    def GetIUnknownForObjectInContext(o):
        """
        GetIUnknownForObjectInContext(o: object) -> IntPtr
        
            Returns an IUnknown interface from a managed object, if the caller is in the same context as 
             that object.
        
        
            o: The object whose IUnknown interface is requested.
            Returns: The IUnknown pointer for the specified object, or null if the caller is not in the same context 
             as the specified object.
        """
        pass

    @staticmethod
    def GetLastWin32Error():
        """
        GetLastWin32Error() -> int
        
            Returns the error code returned by the last unmanaged function that was called using platform 
             invoke that has the System.Runtime.InteropServices.DllImportAttribute.SetLastError flag set.
        
            Returns: The last error code set by a call to the Win32 SetLastError function.
        """
        pass

    @staticmethod
    def GetManagedThunkForUnmanagedMethodPtr(pfnMethodToWrap, pbSignature, cbSignature):
        """
        GetManagedThunkForUnmanagedMethodPtr(pfnMethodToWrap: IntPtr, pbSignature: IntPtr, cbSignature: int) -> IntPtr
        
            Gets a pointer to a runtime-generated function that marshals a call from managed to unmanaged 
             code.
        
        
            pfnMethodToWrap: A pointer to the method to marshal.
            pbSignature: A pointer to the method signature.
            cbSignature: The number of bytes in pbSignature.
            Returns: A pointer to the function that will marshal a call from the pfnMethodToWrap parameter to 
             unmanaged code.
        """
        pass

    @staticmethod
    def GetMethodInfoForComSlot(t, slot, memberType):
        """
        GetMethodInfoForComSlot(t: Type, slot: int, memberType: ComMemberType) -> (MemberInfo, ComMemberType)
        
            Retrieves a System.Reflection.MemberInfo object for the specified virtual function table 
             (v-table or VTBL) slot.
        
        
            t: The type for which the System.Reflection.MemberInfo is to be retrieved.
            slot: The VTBL slot.
            memberType: On successful return, one of the enumeration values that specifies the type of the member.
            Returns: The object that represents the member at the specified VTBL slot.
        """
        pass

    @staticmethod
    def GetNativeVariantForObject(obj, pDstNativeVariant):
        """
        GetNativeVariantForObject[T](obj: T, pDstNativeVariant: IntPtr)GetNativeVariantForObject(obj: object, pDstNativeVariant: IntPtr)
            Converts an object to a COM VARIANT.
        
            obj: The object for which to get a COM VARIANT.
            pDstNativeVariant: A pointer to receive the VARIANT that corresponds to the obj parameter.
        """
        pass

    @staticmethod
    def GetObjectForIUnknown(pUnk):
        """
        GetObjectForIUnknown(pUnk: IntPtr) -> object
        
            Returns an instance of a type that represents a COM object by a pointer to its IUnknown 
             interface.
        
        
            pUnk: A pointer to the IUnknown interface.
            Returns: An object that represents the specified unmanaged COM object.
        """
        pass

    @staticmethod
    def GetObjectForNativeVariant(pSrcNativeVariant):
        """
        GetObjectForNativeVariant[T](pSrcNativeVariant: IntPtr) -> T
        
            Converts a COM VARIANT to an object.
        
            pSrcNativeVariant: A pointer to a COM VARIANT.
            Returns: An object that corresponds to the pSrcNativeVariant parameter.
        GetObjectForNativeVariant(pSrcNativeVariant: IntPtr) -> object
        
            Converts a COM VARIANT to an object.
        
            pSrcNativeVariant: A pointer to a COM VARIANT.
            Returns: An object that corresponds to the pSrcNativeVariant parameter.
        """
        pass

    @staticmethod
    def GetObjectsForNativeVariants(aSrcNativeVariant, cVars):
        """
        GetObjectsForNativeVariants[T](aSrcNativeVariant: IntPtr, cVars: int) -> Array[T]
        
            Converts an array of COM VARIANTs to an array of objects.
        
            aSrcNativeVariant: A pointer to the first element of an array of COM VARIANTs.
            cVars: The count of COM VARIANTs in aSrcNativeVariant.
            Returns: An object array that corresponds to aSrcNativeVariant.
        GetObjectsForNativeVariants(aSrcNativeVariant: IntPtr, cVars: int) -> Array[object]
        
            Converts an array of COM VARIANTs to an array of objects.
        
            aSrcNativeVariant: A pointer to the first element of an array of COM VARIANTs.
            cVars: The count of COM VARIANTs in aSrcNativeVariant.
            Returns: An object array that corresponds to aSrcNativeVariant.
        """
        pass

    @staticmethod
    def GetStartComSlot(t):
        """
        GetStartComSlot(t: Type) -> int
        
            Gets the first slot in the virtual function table (v-table or VTBL) that contains user-defined 
             methods.
        
        
            t: A type that represents an interface.
            Returns: The first VTBL slot that contains user-defined methods. The first slot is 3 if the interface is 
             based on IUnknown, and 7 if the interface is based on IDispatch.
        """
        pass

    @staticmethod
    def GetThreadFromFiberCookie(cookie):
        """
        GetThreadFromFiberCookie(cookie: int) -> Thread
        
            Converts a fiber cookie into the corresponding System.Threading.Thread instance.
        
            cookie: An integer that represents a fiber cookie.
            Returns: A thread that corresponds to the cookie parameter.
        """
        pass

    @staticmethod
    def GetTypedObjectForIUnknown(pUnk, t):
        """
        GetTypedObjectForIUnknown(pUnk: IntPtr, t: Type) -> object
        
            Returns a managed object of a specified type that represents a COM object.
        
            pUnk: A pointer to the IUnknown interface of the unmanaged object.
            t: The type of the requested managed class.
            Returns: An instance of the class corresponding to the System.Type object that represents the requested 
             unmanaged COM object.
        """
        pass

    @staticmethod
    def GetTypeForITypeInfo(piTypeInfo):
        """
        GetTypeForITypeInfo(piTypeInfo: IntPtr) -> Type
        
            Converts an unmanaged ITypeInfo object into a managed System.Type object.
        
            piTypeInfo: The ITypeInfo interface to marshal.
            Returns: A managed type that represents the unmanaged ITypeInfo object.
        """
        pass

    @staticmethod
    def GetTypeFromCLSID(clsid):
        """ GetTypeFromCLSID(clsid: Guid) -> Type """
        pass

    @staticmethod
    def GetTypeInfoName(*__args):
        """
        GetTypeInfoName(typeInfo: ITypeInfo) -> str
        
            Retrieves the name of the type represented by an ITypeInfo object.
        
            typeInfo: An object that represents an ITypeInfo pointer.
            Returns: The name of the type that the typeInfo parameter points to.
        GetTypeInfoName(pTI: UCOMITypeInfo) -> str
        
            Retrieves the name of the type represented by an ITypeInfo object.
        
            pTI: An object that represents an ITypeInfo pointer.
            Returns: The name of the type that the pTI parameter points to.
        """
        pass

    @staticmethod
    def GetTypeLibGuid(*__args):
        """
        GetTypeLibGuid(typelib: ITypeLib) -> Guid
        
            Retrieves the library identifier (LIBID) of a type library.
        
            typelib: The type library whose LIBID is to be retrieved.
            Returns: The LIBID of the specified type library.
        GetTypeLibGuid(pTLB: UCOMITypeLib) -> Guid
        
            Retrieves the library identifier (LIBID) of a type library.
        
            pTLB: The type library whose LIBID is to be retrieved.
            Returns: The LIBID of the type library that the pTLB parameter points to.
        """
        pass

    @staticmethod
    def GetTypeLibGuidForAssembly(asm):
        """
        GetTypeLibGuidForAssembly(asm: Assembly) -> Guid
        
            Retrieves the library identifier (LIBID) that is assigned to a type library when it was exported 
             from the specified assembly.
        
        
            asm: The assembly from which the type library was exported.
            Returns: The LIBID that is assigned to a type library when it is exported from the specified assembly.
        """
        pass

    @staticmethod
    def GetTypeLibLcid(*__args):
        """
        GetTypeLibLcid(typelib: ITypeLib) -> int
        
            Retrieves the LCID of a type library.
        
            typelib: The type library whose LCID is to be retrieved.
            Returns: The LCID of the type library that the typelib parameter points to.
        GetTypeLibLcid(pTLB: UCOMITypeLib) -> int
        
            Retrieves the LCID of a type library.
        
            pTLB: The type library whose LCID is to be retrieved.
            Returns: The LCID of the type library that the pTLB parameter points to.
        """
        pass

    @staticmethod
    def GetTypeLibName(*__args):
        """
        GetTypeLibName(typelib: ITypeLib) -> str
        
            Retrieves the name of a type library.
        
            typelib: The type library whose name is to be retrieved.
            Returns: The name of the type library that the typelib parameter points to.
        GetTypeLibName(pTLB: UCOMITypeLib) -> str
        
            Retrieves the name of a type library.
        
            pTLB: The type library whose name is to be retrieved.
            Returns: The name of the type library that the pTLB parameter points to.
        """
        pass

    @staticmethod
    def GetTypeLibVersionForAssembly(inputAssembly, majorVersion, minorVersion):
        """
        GetTypeLibVersionForAssembly(inputAssembly: Assembly) -> (int, int)
        
            Retrieves the version number of a type library that will be exported from the specified assembly.
        
            inputAssembly: A managed assembly.
        """
        pass

    @staticmethod
    def GetUniqueObjectForIUnknown(unknown):
        """
        GetUniqueObjectForIUnknown(unknown: IntPtr) -> object
        
            Creates a unique Runtime Callable Wrapper (RCW) object for a given IUnknown interface.
        
            unknown: A managed pointer to an IUnknown interface.
            Returns: A unique RCW for the specified IUnknown interface.
        """
        pass

    @staticmethod
    def GetUnmanagedThunkForManagedMethodPtr(pfnMethodToWrap, pbSignature, cbSignature):
        """
        GetUnmanagedThunkForManagedMethodPtr(pfnMethodToWrap: IntPtr, pbSignature: IntPtr, cbSignature: int) -> IntPtr
        
            Gets a pointer to a runtime-generated function that marshals a call from unmanaged to managed 
             code.
        
        
            pfnMethodToWrap: A pointer to the method to marshal.
            pbSignature: A pointer to the method signature.
            cbSignature: The number of bytes in pbSignature.
            Returns: A pointer to a function that will marshal a call from pfnMethodToWrap to managed code.
        """
        pass

    @staticmethod
    def IsComObject(o):
        """
        IsComObject(o: object) -> bool
        
            Indicates whether a specified object represents a COM object.
        
            o: The object to check.
            Returns: true if the o parameter is a COM type; otherwise, false.
        """
        pass

    @staticmethod
    def IsTypeVisibleFromCom(t):
        """
        IsTypeVisibleFromCom(t: Type) -> bool
        
            Indicates whether a type is visible to COM clients.
        
            t: The type to check for COM visibility.
            Returns: true if the type is visible to COM; otherwise, false.
        """
        pass

    @staticmethod
    def NumParamBytes(m):
        """
        NumParamBytes(m: MethodInfo) -> int
        
            Calculates the number of bytes in unmanaged memory that are required to hold the parameters for 
             the specified method.
        
        
            m: The method to be checked.
            Returns: The number of bytes required to represent the method parameters in unmanaged memory.
        """
        pass

    @staticmethod
    def OffsetOf(*__args):
        """
        OffsetOf[T](fieldName: str) -> IntPtr
        OffsetOf(t: Type, fieldName: str) -> IntPtr
        
            Returns the field offset of the unmanaged form of the managed class.
        
            t: A value type or formatted reference type that specifies the managed class. You must apply the 
             System.Runtime.InteropServices.StructLayoutAttribute to the class.
        
            fieldName: The field within the t parameter.
            Returns: The offset, in bytes, for the fieldName parameter within the specified class that is declared by 
             platform invoke.
        """
        pass

    @staticmethod
    def Prelink(m):
        """
        Prelink(m: MethodInfo)
            Executes one-time method setup tasks without calling the method.
        
            m: The method to be checked.
        """
        pass

    @staticmethod
    def PrelinkAll(c):
        """
        PrelinkAll(c: Type)
            Performs a pre-link check for all methods on a class.
        
            c: The class whose methods are to be checked.
        """
        pass

    @staticmethod
    def PtrToStringAnsi(ptr, len=None):
        """
        PtrToStringAnsi(ptr: IntPtr, len: int) -> str
        
            Allocates a managed System.String, copies a specified number of characters from an unmanaged 
             ANSI string into it, and widens each ANSI character to Unicode.
        
        
            ptr: The address of the first character of the unmanaged string.
            len: The byte count of the input string to copy.
            Returns: A managed string that holds a copy of the native ANSI string if the value of the ptr parameter 
             is not null; otherwise, this method returns null.
        
        PtrToStringAnsi(ptr: IntPtr) -> str
        
            Copies all characters up to the first null character from an unmanaged ANSI string to a managed 
             System.String, and widens each ANSI character to Unicode.
        
        
            ptr: The address of the first character of the unmanaged string.
            Returns: A managed string that holds a copy of the unmanaged ANSI string. If ptr is null, the method 
             returns a null string.
        """
        pass

    @staticmethod
    def PtrToStringAuto(ptr, len=None):
        """
        PtrToStringAuto(ptr: IntPtr) -> str
        
            Allocates a managed System.String and copies all characters up to the first null character from 
             a string stored in unmanaged memory into it.
        
        
            ptr: For Unicode platforms, the address of the first Unicode character.-or- For ANSI plaforms, the 
             address of the first ANSI character.
        
            Returns: A managed string that holds a copy of the unmanaged string if the value of the ptr parameter is 
             not null; otherwise, this method returns null.
        
        PtrToStringAuto(ptr: IntPtr, len: int) -> str
        
            Allocates a managed System.String and copies the specified number of characters from a string 
             stored in unmanaged memory into it.
        
        
            ptr: For Unicode platforms, the address of the first Unicode character.-or- For ANSI plaforms, the 
             address of the first ANSI character.
        
            len: The number of characters to copy.
            Returns: A managed string that holds a copy of the native string if the value of the ptr parameter is not 
             null; otherwise, this method returns null.
        """
        pass

    @staticmethod
    def PtrToStringBSTR(ptr):
        """
        PtrToStringBSTR(ptr: IntPtr) -> str
        
            Allocates a managed System.String and copies a BSTR Data Type string stored in unmanaged memory 
             into it.
        
        
            ptr: The address of the first character of the unmanaged string.
            Returns: A managed string that holds a copy of the unmanaged string if the value of the ptr parameter is 
             not null; otherwise, this method returns null.
        """
        pass

    @staticmethod
    def PtrToStringUni(ptr, len=None):
        """
        PtrToStringUni(ptr: IntPtr) -> str
        
            Allocates a managed System.String and copies all characters up to the first null character from 
             an unmanaged Unicode string into it.
        
        
            ptr: The address of the first character of the unmanaged string.
            Returns: A managed string that holds a copy of the unmanaged string if the value of the ptr parameter is 
             not null; otherwise, this method returns null.
        
        PtrToStringUni(ptr: IntPtr, len: int) -> str
        
            Allocates a managed System.String and copies a specified number of characters from an unmanaged 
             Unicode string into it.
        
        
            ptr: The address of the first character of the unmanaged string.
            len: The number of Unicode characters to copy.
            Returns: A managed string that holds a copy of the unmanaged string if the value of the ptr parameter is 
             not null; otherwise, this method returns null.
        """
        pass

    @staticmethod
    def PtrToStructure(ptr, *__args):
        """
        PtrToStructure(ptr: IntPtr, structureType: Type) -> object
        
            Marshals data from an unmanaged block of memory to a newly allocated managed object of the 
             specified type.
        
        
            ptr: A pointer to an unmanaged block of memory.
            structureType: The type of object to be created. This object must represent a formatted class or a structure.
            Returns: A managed object containing the data pointed to by the ptr parameter.
        PtrToStructure[T](ptr: IntPtr) -> T
        PtrToStructure(ptr: IntPtr, structure: object)
            Marshals data from an unmanaged block of memory to a managed object.
        
            ptr: A pointer to an unmanaged block of memory.
            structure: The object to which the data is to be copied. This must be an instance of a formatted class.
        PtrToStructure[T](ptr: IntPtr, structure: T)
        """
        pass

    @staticmethod
    def QueryInterface(pUnk, iid, ppv):
        """
        QueryInterface(pUnk: IntPtr, iid: Guid) -> (int, Guid, IntPtr)
        
            Requests a pointer to a specified interface from a COM object.
        
            pUnk: The interface to be queried.
            iid: The interface identifier (IID) of the requested interface.
            Returns: An HRESULT that indicates the success or failure of the call.
        """
        pass

    @staticmethod
    def ReadByte(ptr, ofs=None):
        """
        ReadByte(ptr: IntPtr) -> Byte
        
            Reads a single byte from unmanaged memory.
        
            ptr: The address in unmanaged memory from which to read.
            Returns: The byte read from unmanaged memory.
        ReadByte(ptr: IntPtr, ofs: int) -> Byte
        
            Reads a single byte at a given offset (or index) from unmanaged memory.
        
            ptr: The base address in unmanaged memory from which to read.
            ofs: An additional byte offset, which is added to the ptr parameter before reading.
            Returns: The byte read from unmanaged memory at the given offset.
        ReadByte(ptr: object, ofs: int) -> Byte
        
            Reads a single byte at a given offset (or index) from unmanaged memory.
        
            ptr: The base address in unmanaged memory of the source object.
            ofs: An additional byte offset, which is added to the ptr parameter before reading.
            Returns: The byte read from unmanaged memory at the given offset.
        """
        pass

    @staticmethod
    def ReadInt16(ptr, ofs=None):
        """
        ReadInt16(ptr: IntPtr) -> Int16
        
            Reads a 16-bit signed integer from unmanaged memory.
        
            ptr: The address in unmanaged memory from which to read.
            Returns: The 16-bit signed integer read from unmanaged memory.
        ReadInt16(ptr: IntPtr, ofs: int) -> Int16
        
            Reads a 16-bit signed integer at a given offset from unmanaged memory.
        
            ptr: The base address in unmanaged memory from which to read.
            ofs: An additional byte offset, which is added to the ptr parameter before reading.
            Returns: The 16-bit signed integer read from unmanaged memory at the given offset.
        ReadInt16(ptr: object, ofs: int) -> Int16
        
            Reads a 16-bit signed integer at a given offset from unmanaged memory.
        
            ptr: The base address in unmanaged memory of the source object.
            ofs: An additional byte offset, which is added to the ptr parameter before reading.
            Returns: The 16-bit signed integer read from unmanaged memory at the given offset.
        """
        pass

    @staticmethod
    def ReadInt32(ptr, ofs=None):
        """
        ReadInt32(ptr: IntPtr) -> int
        
            Reads a 32-bit signed integer from unmanaged memory.
        
            ptr: The address in unmanaged memory from which to read.
            Returns: The 32-bit signed integer read from unmanaged memory.
        ReadInt32(ptr: IntPtr, ofs: int) -> int
        
            Reads a 32-bit signed integer at a given offset from unmanaged memory.
        
            ptr: The base address in unmanaged memory from which to read.
            ofs: An additional byte offset, which is added to the ptr parameter before reading.
            Returns: The 32-bit signed integer read from unmanaged memory.
        ReadInt32(ptr: object, ofs: int) -> int
        
            Reads a 32-bit signed integer at a given offset from unmanaged memory.
        
            ptr: The base address in unmanaged memory of the source object.
            ofs: An additional byte offset, which is added to the ptr parameter before reading.
            Returns: The 32-bit signed integer read from unmanaged memory at the given offset.
        """
        pass

    @staticmethod
    def ReadInt64(ptr, ofs=None):
        """
        ReadInt64(ptr: IntPtr) -> Int64
        
            Reads a 64-bit signed integer from unmanaged memory.
        
            ptr: The address in unmanaged memory from which to read.
            Returns: The 64-bit signed integer read from unmanaged memory.
        ReadInt64(ptr: IntPtr, ofs: int) -> Int64
        
            Reads a 64-bit signed integer at a given offset from unmanaged memory.
        
            ptr: The base address in unmanaged memory from which to read.
            ofs: An additional byte offset, which is added to the ptr parameter before reading.
            Returns: The 64-bit signed integer read from unmanaged memory at the given offset.
        ReadInt64(ptr: object, ofs: int) -> Int64
        
            Reads a 64-bit signed integer at a given offset from unmanaged memory.
        
            ptr: The base address in unmanaged memory of the source object.
            ofs: An additional byte offset, which is added to the ptr parameter before reading.
            Returns: The 64-bit signed integer read from unmanaged memory at the given offset.
        """
        pass

    @staticmethod
    def ReadIntPtr(ptr, ofs=None):
        """
        ReadIntPtr(ptr: IntPtr) -> IntPtr
        
            Reads a processor native-sized integer from unmanaged memory.
        
            ptr: The address in unmanaged memory from which to read.
            Returns: The integer read from unmanaged memory. A 32 bit integer is returned on 32 bit machines and a 64 
             bit integer is returned on 64 bit machines.
        
        ReadIntPtr(ptr: IntPtr, ofs: int) -> IntPtr
        
            Reads a processor native sized integer at a given offset from unmanaged memory.
        
            ptr: The base address in unmanaged memory from which to read.
            ofs: An additional byte offset, which is added to the ptr parameter before reading.
            Returns: The integer read from unmanaged memory at the given offset.
        ReadIntPtr(ptr: object, ofs: int) -> IntPtr
        
            Reads a processor native sized integer from unmanaged memory.
        
            ptr: The base address in unmanaged memory of the source object.
            ofs: An additional byte offset, which is added to the ptr parameter before reading.
            Returns: The integer read from unmanaged memory at the given offset.
        """
        pass

    @staticmethod
    def ReAllocCoTaskMem(pv, cb):
        """
        ReAllocCoTaskMem(pv: IntPtr, cb: int) -> IntPtr
        
            Resizes a block of memory previously allocated with 
             System.Runtime.InteropServices.Marshal.AllocCoTaskMem(System.Int32).
        
        
            pv: A pointer to memory allocated with 
             System.Runtime.InteropServices.Marshal.AllocCoTaskMem(System.Int32).
        
            cb: The new size of the allocated block.
            Returns: An integer representing the address of the reallocated block of memory. This memory must be 
             released with System.Runtime.InteropServices.Marshal.FreeCoTaskMem(System.IntPtr).
        """
        pass

    @staticmethod
    def ReAllocHGlobal(pv, cb):
        """
        ReAllocHGlobal(pv: IntPtr, cb: IntPtr) -> IntPtr
        
            Resizes a block of memory previously allocated with 
             System.Runtime.InteropServices.Marshal.AllocHGlobal(System.IntPtr).
        
        
            pv: A pointer to memory allocated with 
             System.Runtime.InteropServices.Marshal.AllocHGlobal(System.IntPtr).
        
            cb: The new size of the allocated block. This is not a pointer; it is the byte count you are 
             requesting, cast to type System.IntPtr. If you pass a pointer, it is treated as a size.
        
            Returns: A pointer to the reallocated memory. This memory must be released using 
             System.Runtime.InteropServices.Marshal.FreeHGlobal(System.IntPtr).
        """
        pass

    @staticmethod
    def Release(pUnk):
        """
        Release(pUnk: IntPtr) -> int
        
            Decrements the reference count on the specified interface.
        
            pUnk: The interface to release.
            Returns: The new value of the reference count on the interface specified by the pUnk parameter.
        """
        pass

    @staticmethod
    def ReleaseComObject(o):
        """
        ReleaseComObject(o: object) -> int
        
            Decrements the reference count of the specified Runtime Callable Wrapper (RCW) associated with 
             the specified COM object.
        
        
            o: The COM object to release.
            Returns: The new value of the reference count of the RCW associated with o. This value is typically zero 
             since the RCW keeps just one reference to the wrapped COM object regardless of the number of 
             managed clients calling it.
        """
        pass

    @staticmethod
    def ReleaseThreadCache():
        """
        ReleaseThreadCache()
            Releases the thread cache.
        """
        pass

    @staticmethod
    def SecureStringToBSTR(s):
        """
        SecureStringToBSTR(s: SecureString) -> IntPtr
        
            Allocates a BSTR Data Type and copies the contents of a managed System.Security.SecureString 
             object into it.
        
        
            s: The managed object to copy.
            Returns: The address, in unmanaged memory, where the s parameter was copied to, or 0 if a null object was 
             supplied.
        """
        pass

    @staticmethod
    def SecureStringToCoTaskMemAnsi(s):
        """
        SecureStringToCoTaskMemAnsi(s: SecureString) -> IntPtr
        
            Copies the contents of a managed System.Security.SecureString object to a block of memory 
             allocated from the unmanaged COM task allocator.
        
        
            s: The managed object to copy.
            Returns: The address, in unmanaged memory, where the s parameter was copied to, or 0 if a null object was 
             supplied.
        """
        pass

    @staticmethod
    def SecureStringToCoTaskMemUnicode(s):
        """
        SecureStringToCoTaskMemUnicode(s: SecureString) -> IntPtr
        
            Copies the contents of a managed System.Security.SecureString object to a block of memory 
             allocated from the unmanaged COM task allocator.
        
        
            s: The managed object to copy.
            Returns: The address, in unmanaged memory, where the s parameter was copied to, or 0 if a null object was 
             supplied.
        """
        pass

    @staticmethod
    def SecureStringToGlobalAllocAnsi(s):
        """
        SecureStringToGlobalAllocAnsi(s: SecureString) -> IntPtr
        
            Copies the contents of a managed System.Security.SecureString into unmanaged memory, converting 
             into ANSI format as it copies.
        
        
            s: The managed object to copy.
            Returns: The address, in unmanaged memory, to where the s parameter was copied, or 0 if a null object was 
             supplied.
        """
        pass

    @staticmethod
    def SecureStringToGlobalAllocUnicode(s):
        """
        SecureStringToGlobalAllocUnicode(s: SecureString) -> IntPtr
        
            Copies the contents of a managed System.Security.SecureString object into unmanaged memory.
        
            s: The managed object to copy.
            Returns: The address, in unmanaged memory, where s was copied, or 0 if s is a 
             System.Security.SecureString object whose length is 0.
        """
        pass

    @staticmethod
    def SetComObjectData(obj, key, data):
        """
        SetComObjectData(obj: object, key: object, data: object) -> bool
        
            Sets data referenced by the specified key in the specified COM object.
        
            obj: The COM object in which to store the data.
            key: The key in the internal hash table of the COM object in which to store the data.
            data: The data to set.
            Returns: true if the data was set successfully; otherwise, false.
        """
        pass

    @staticmethod
    def SizeOf(*__args):
        """
        SizeOf(t: Type) -> int
        
            Returns the size of an unmanaged type in bytes.
        
            t: The type whose size is to be returned.
            Returns: The size of the specified type in unmanaged code.
        SizeOf[T]() -> int
        SizeOf(structure: object) -> int
        
            Returns the unmanaged size of an object in bytes.
        
            structure: The object whose size is to be returned.
            Returns: The size of the specified object in unmanaged code.
        SizeOf[T](structure: T) -> int
        """
        pass

    @staticmethod
    def StringToBSTR(s):
        """
        StringToBSTR(s: str) -> IntPtr
        
            Allocates a BSTR Data Type and copies the contents of a managed System.String into it.
        
            s: The managed string to be copied.
            Returns: An unmanaged pointer to the BSTR, or 0 if s is null.
        """
        pass

    @staticmethod
    def StringToCoTaskMemAnsi(s):
        """
        StringToCoTaskMemAnsi(s: str) -> IntPtr
        
            Copies the contents of a managed System.String to a block of memory allocated from the unmanaged 
             COM task allocator.
        
        
            s: A managed string to be copied.
            Returns: An integer representing a pointer to the block of memory allocated for the string, or 0 if s is 
             null.
        """
        pass

    @staticmethod
    def StringToCoTaskMemAuto(s):
        """
        StringToCoTaskMemAuto(s: str) -> IntPtr
        
            Copies the contents of a managed System.String to a block of memory allocated from the unmanaged 
             COM task allocator.
        
        
            s: A managed string to be copied.
            Returns: The allocated memory block, or 0 if s is null.
        """
        pass

    @staticmethod
    def StringToCoTaskMemUni(s):
        """
        StringToCoTaskMemUni(s: str) -> IntPtr
        
            Copies the contents of a managed System.String to a block of memory allocated from the unmanaged 
             COM task allocator.
        
        
            s: A managed string to be copied.
            Returns: An integer representing a pointer to the block of memory allocated for the string, or 0 if s is 
             null.
        """
        pass

    @staticmethod
    def StringToHGlobalAnsi(s):
        """
        StringToHGlobalAnsi(s: str) -> IntPtr
        
            Copies the contents of a managed System.String into unmanaged memory, converting into ANSI 
             format as it copies.
        
        
            s: A managed string to be copied.
            Returns: The address, in unmanaged memory, to where s was copied, or 0 if s is null.
        """
        pass

    @staticmethod
    def StringToHGlobalAuto(s):
        """
        StringToHGlobalAuto(s: str) -> IntPtr
        
            Copies the contents of a managed System.String into unmanaged memory, converting into ANSI 
             format if required.
        
        
            s: A managed string to be copied.
            Returns: The address, in unmanaged memory, to where the string was copied, or 0 if s is null.
        """
        pass

    @staticmethod
    def StringToHGlobalUni(s):
        """
        StringToHGlobalUni(s: str) -> IntPtr
        
            Copies the contents of a managed System.String into unmanaged memory.
        
            s: A managed string to be copied.
            Returns: The address, in unmanaged memory, to where the s was copied, or 0 if s is null.
        """
        pass

    @staticmethod
    def StructureToPtr(structure, ptr, fDeleteOld):
        """
        StructureToPtr[T](structure: T, ptr: IntPtr, fDeleteOld: bool)StructureToPtr(structure: object, ptr: IntPtr, fDeleteOld: bool)
            Marshals data from a managed object to an unmanaged block of memory.
        
            structure: A managed object holding the data to be marshaled. This object must be an instance of a 
             formatted class.
        
            ptr: A pointer to an unmanaged block of memory, which must be allocated before this method is called.
            fDeleteOld: true to have the 
             System.Runtime.InteropServices.Marshal.DestroyStructure(System.IntPtr,System.Type) method called 
             on the ptr parameter before this method executes. Note that passing false can lead to a memory 
             leak.
        """
        pass

    @staticmethod
    def ThrowExceptionForHR(errorCode, errorInfo=None):
        """
        ThrowExceptionForHR(errorCode: int, errorInfo: IntPtr)
            Throws an exception with a specific failure HRESULT, based on the specified IErrorInfo Interface 
             interface.
        
        
            errorCode: The HRESULT corresponding to the desired exception.
            errorInfo: A pointer to the IErrorInfo interface that provides more information about the error. You can 
             specify IntPtr(0) to use the current IErrorInfo interface, or IntPtr(-1) to ignore the current 
             IErrorInfo interface and construct the exception just from the error code.
        
        ThrowExceptionForHR(errorCode: int)
            Throws an exception with a specific failure HRESULT value.
        
            errorCode: The HRESULT corresponding to the desired exception.
        """
        pass

    @staticmethod
    def UnsafeAddrOfPinnedArrayElement(arr, index):
        """
        UnsafeAddrOfPinnedArrayElement[T](arr: Array[T], index: int) -> IntPtr
        UnsafeAddrOfPinnedArrayElement(arr: Array, index: int) -> IntPtr
        
            Gets the address of the element at the specified index inside the specified array.
        
            arr: The array that contains the desired element.
            index: The index in the arr parameter of the desired element.
            Returns: The address of index inside arr.
        """
        pass

    @staticmethod
    def WriteByte(ptr, *__args):
        """
        WriteByte(ptr: IntPtr, val: Byte)
            Writes a single byte value to unmanaged memory.
        
            ptr: The address in unmanaged memory to write to.
            val: The value to write.
        WriteByte(ofs: int, val: Byte) -> object
        
            Writes a single byte value to unmanaged memory at a specified offset.
        
            ofs: An additional byte offset, which is added to the ptr parameter before writing.
            val: The value to write.
        WriteByte(ptr: IntPtr, ofs: int, val: Byte)
            Writes a single byte value to unmanaged memory at a specified offset.
        
            ptr: The base address in unmanaged memory to write to.
            ofs: An additional byte offset, which is added to the ptr parameter before writing.
            val: The value to write.
        """
        pass

    @staticmethod
    def WriteInt16(ptr, *__args):
        """
        WriteInt16(ptr: IntPtr, ofs: int, val: Char)
            Writes a 16-bit signed integer value to unmanaged memory at a specified offset.
        
            ptr: The base address in the native heap to write to.
            ofs: An additional byte offset, which is added to the ptr parameter before writing.
            val: The value to write.
        WriteInt16(ofs: int, val: Char) -> object
        
            Writes a 16-bit signed integer value to unmanaged memory at a specified offset.
        
            ofs: An additional byte offset, which is added to the ptr parameter before writing.
            val: The value to write.
        WriteInt16(ptr: IntPtr, val: Char)
            Writes a character as a 16-bit integer value to unmanaged memory.
        
            ptr: The address in unmanaged memory to write to.
            val: The value to write.
        WriteInt16(ptr: IntPtr, ofs: int, val: Int16)
            Writes a 16-bit signed integer value into unmanaged memory at a specified offset.
        
            ptr: The base address in unmanaged memory to write to.
            ofs: An additional byte offset, which is added to the ptr parameter before writing.
            val: The value to write.
        WriteInt16(ofs: int, val: Int16) -> object
        
            Writes a 16-bit signed integer value to unmanaged memory at a specified offset.
        
            ofs: An additional byte offset, which is added to the ptr parameter before writing.
            val: The value to write.
        WriteInt16(ptr: IntPtr, val: Int16)
            Writes a 16-bit integer value to unmanaged memory.
        
            ptr: The address in unmanaged memory to write to.
            val: The value to write.
        """
        pass

    @staticmethod
    def WriteInt32(ptr, *__args):
        """
        WriteInt32(ptr: IntPtr, val: int)
            Writes a 32-bit signed integer value to unmanaged memory.
        
            ptr: The address in unmanaged memory to write to.
            val: The value to write.
        WriteInt32(ofs: int, val: int) -> object
        
            Writes a 32-bit signed integer value to unmanaged memory at a specified offset.
        
            ofs: An additional byte offset, which is added to the ptr parameter before writing.
            val: The value to write.
        WriteInt32(ptr: IntPtr, ofs: int, val: int)
            Writes a 32-bit signed integer value into unmanaged memory at a specified offset.
        
            ptr: The base address in unmanaged memory to write to.
            ofs: An additional byte offset, which is added to the ptr parameter before writing.
            val: The value to write.
        """
        pass

    @staticmethod
    def WriteInt64(ptr, *__args):
        """
        WriteInt64(ptr: IntPtr, val: Int64)
            Writes a 64-bit signed integer value to unmanaged memory.
        
            ptr: The address in unmanaged memory to write to.
            val: The value to write.
        WriteInt64(ofs: int, val: Int64) -> object
        
            Writes a 64-bit signed integer value to unmanaged memory at a specified offset.
        
            ofs: An additional byte offset, which is added to the ptr parameter before writing.
            val: The value to write.
        WriteInt64(ptr: IntPtr, ofs: int, val: Int64)
            Writes a 64-bit signed integer value to unmanaged memory at a specified offset.
        
            ptr: The base address in unmanaged memory to write.
            ofs: An additional byte offset, which is added to the ptr parameter before writing.
            val: The value to write.
        """
        pass

    @staticmethod
    def WriteIntPtr(ptr, *__args):
        """
        WriteIntPtr(ptr: IntPtr, val: IntPtr)
            Writes a processor native sized integer value into unmanaged memory.
        
            ptr: The address in unmanaged memory to write to.
            val: The value to write.
        WriteIntPtr(ofs: int, val: IntPtr) -> object
        
            Writes a processor native sized integer value to unmanaged memory.
        
            ofs: An additional byte offset, which is added to the ptr parameter before writing.
            val: The value to write.
        WriteIntPtr(ptr: IntPtr, ofs: int, val: IntPtr)
            Writes a processor native-sized integer value to unmanaged memory at a specified offset.
        
            ptr: The base address in unmanaged memory to write to.
            ofs: An additional byte offset, which is added to the ptr parameter before writing.
            val: The value to write.
        """
        pass

    @staticmethod
    def ZeroFreeBSTR(s):
        """
        ZeroFreeBSTR(s: IntPtr)
            Frees a BSTR Data Type pointer that was allocated using the 
             System.Runtime.InteropServices.Marshal.SecureStringToBSTR(System.Security.SecureString) method.
        
        
            s: The address of the BSTR to free.
        """
        pass

    @staticmethod
    def ZeroFreeCoTaskMemAnsi(s):
        """
        ZeroFreeCoTaskMemAnsi(s: IntPtr)
            Frees an unmanaged string pointer that was allocated using the 
             System.Runtime.InteropServices.Marshal.SecureStringToCoTaskMemAnsi(System.Security.SecureString) 
             method.
        
        
            s: The address of the unmanaged string to free.
        """
        pass

    @staticmethod
    def ZeroFreeCoTaskMemUnicode(s):
        """
        ZeroFreeCoTaskMemUnicode(s: IntPtr)
            Frees an unmanaged string pointer that was allocated using the 
             System.Runtime.InteropServices.Marshal.SecureStringToCoTaskMemUnicode(System.Security.SecureStrin
             g) method.
        
        
            s: The address of the unmanaged string to free.
        """
        pass

    @staticmethod
    def ZeroFreeGlobalAllocAnsi(s):
        """
        ZeroFreeGlobalAllocAnsi(s: IntPtr)
            Frees an unmanaged string pointer that was allocated using the 
             System.Runtime.InteropServices.Marshal.SecureStringToGlobalAllocAnsi(System.Security.SecureString
             ) method.
        
        
            s: The address of the unmanaged string to free.
        """
        pass

    @staticmethod
    def ZeroFreeGlobalAllocUnicode(s):
        """
        ZeroFreeGlobalAllocUnicode(s: IntPtr)
            Frees an unmanaged string pointer that was allocated using the 
             System.Runtime.InteropServices.Marshal.SecureStringToGlobalAllocUnicode(System.Security.SecureStr
             ing) method.
        
        
            s: The address of the unmanaged string to free.
        """
        pass

    SystemDefaultCharSize = 2
    SystemMaxDBCSCharSize = 1
    __all__ = [
        'AddRef',
        'AllocCoTaskMem',
        'AllocHGlobal',
        'AreComObjectsAvailableForCleanup',
        'BindToMoniker',
        'ChangeWrapperHandleStrength',
        'CleanupUnusedObjectsInCurrentContext',
        'Copy',
        'CreateAggregatedObject',
        'CreateWrapperOfType',
        'DestroyStructure',
        'FinalReleaseComObject',
        'FreeBSTR',
        'FreeCoTaskMem',
        'FreeHGlobal',
        'GenerateGuidForType',
        'GenerateProgIdForType',
        'GetActiveObject',
        'GetComInterfaceForObject',
        'GetComInterfaceForObjectInContext',
        'GetComObjectData',
        'GetComSlotForMethodInfo',
        'GetDelegateForFunctionPointer',
        'GetEndComSlot',
        'GetExceptionCode',
        'GetExceptionForHR',
        'GetExceptionPointers',
        'GetFunctionPointerForDelegate',
        'GetHINSTANCE',
        'GetHRForException',
        'GetHRForLastWin32Error',
        'GetIDispatchForObject',
        'GetIDispatchForObjectInContext',
        'GetITypeInfoForType',
        'GetIUnknownForObject',
        'GetIUnknownForObjectInContext',
        'GetLastWin32Error',
        'GetManagedThunkForUnmanagedMethodPtr',
        'GetMethodInfoForComSlot',
        'GetNativeVariantForObject',
        'GetObjectForIUnknown',
        'GetObjectForNativeVariant',
        'GetObjectsForNativeVariants',
        'GetStartComSlot',
        'GetThreadFromFiberCookie',
        'GetTypedObjectForIUnknown',
        'GetTypeForITypeInfo',
        'GetTypeFromCLSID',
        'GetTypeInfoName',
        'GetTypeLibGuid',
        'GetTypeLibGuidForAssembly',
        'GetTypeLibLcid',
        'GetTypeLibName',
        'GetTypeLibVersionForAssembly',
        'GetUniqueObjectForIUnknown',
        'GetUnmanagedThunkForManagedMethodPtr',
        'IsComObject',
        'IsTypeVisibleFromCom',
        'NumParamBytes',
        'OffsetOf',
        'Prelink',
        'PrelinkAll',
        'PtrToStringAnsi',
        'PtrToStringAuto',
        'PtrToStringBSTR',
        'PtrToStringUni',
        'PtrToStructure',
        'QueryInterface',
        'ReadByte',
        'ReadInt16',
        'ReadInt32',
        'ReadInt64',
        'ReadIntPtr',
        'ReAllocCoTaskMem',
        'ReAllocHGlobal',
        'Release',
        'ReleaseComObject',
        'ReleaseThreadCache',
        'SecureStringToBSTR',
        'SecureStringToCoTaskMemAnsi',
        'SecureStringToCoTaskMemUnicode',
        'SecureStringToGlobalAllocAnsi',
        'SecureStringToGlobalAllocUnicode',
        'SetComObjectData',
        'SizeOf',
        'StringToBSTR',
        'StringToCoTaskMemAnsi',
        'StringToCoTaskMemAuto',
        'StringToCoTaskMemUni',
        'StringToHGlobalAnsi',
        'StringToHGlobalAuto',
        'StringToHGlobalUni',
        'StructureToPtr',
        'SystemDefaultCharSize',
        'SystemMaxDBCSCharSize',
        'ThrowExceptionForHR',
        'UnsafeAddrOfPinnedArrayElement',
        'WriteByte',
        'WriteInt16',
        'WriteInt32',
        'WriteInt64',
        'WriteIntPtr',
        'ZeroFreeBSTR',
        'ZeroFreeCoTaskMemAnsi',
        'ZeroFreeCoTaskMemUnicode',
        'ZeroFreeGlobalAllocAnsi',
        'ZeroFreeGlobalAllocUnicode',
    ]


class MarshalAsAttribute(Attribute, _Attribute):
    """
    Indicates how to marshal the data between managed and unmanaged code.
    
    MarshalAsAttribute(unmanagedType: UnmanagedType)
    MarshalAsAttribute(unmanagedType: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, unmanagedType):
        """
        __new__(cls: type, unmanagedType: UnmanagedType)
        __new__(cls: type, unmanagedType: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Runtime.InteropServices.UnmanagedType value the data is to be marshaled as.

Get: Value(self: MarshalAsAttribute) -> UnmanagedType

"""


    ArraySubType = None
    IidParameterIndex = None
    MarshalCookie = None
    MarshalType = None
    MarshalTypeRef = None
    SafeArraySubType = None
    SafeArrayUserDefinedSubType = None
    SizeConst = None
    SizeParamIndex = None


class MarshalDirectiveException(SystemException, ISerializable, _Exception):
    """
    The exception that is thrown by the marshaler when it encounters a System.Runtime.InteropServices.MarshalAsAttribute it does not support.
    
    MarshalDirectiveException()
    MarshalDirectiveException(message: str)
    MarshalDirectiveException(message: str, inner: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class ObjectCreationDelegate(MulticastDelegate, ICloneable, ISerializable):
    """
    Creates a COM object.
    
    ObjectCreationDelegate(object: object, method: IntPtr)
    """
    def BeginInvoke(self, aggregator, callback, object):
        """ BeginInvoke(self: ObjectCreationDelegate, aggregator: IntPtr, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ObjectCreationDelegate, result: IAsyncResult) -> IntPtr """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, aggregator):
        """ Invoke(self: ObjectCreationDelegate, aggregator: IntPtr) -> IntPtr """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class OptionalAttribute(Attribute, _Attribute):
    """
    Indicates that a parameter is optional.
    
    OptionalAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class OutAttribute(Attribute, _Attribute):
    """
    Indicates that data should be marshaled from callee back to caller.
    
    OutAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class PARAMDESC(object):
    """ Use System.Runtime.InteropServices.ComTypes.PARAMDESC instead. """
    lpVarValue = None
    wParamFlags = None


class PARAMFLAG(Enum, IComparable, IFormattable, IConvertible):
    """
    Use System.Runtime.InteropServices.ComTypes.PARAMFLAG instead.
    
    enum (flags) PARAMFLAG, values: PARAMFLAG_FHASCUSTDATA (64), PARAMFLAG_FHASDEFAULT (32), PARAMFLAG_FIN (1), PARAMFLAG_FLCID (4), PARAMFLAG_FOPT (16), PARAMFLAG_FOUT (2), PARAMFLAG_FRETVAL (8), PARAMFLAG_NONE (0)
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

    PARAMFLAG_FHASCUSTDATA = None
    PARAMFLAG_FHASDEFAULT = None
    PARAMFLAG_FIN = None
    PARAMFLAG_FLCID = None
    PARAMFLAG_FOPT = None
    PARAMFLAG_FOUT = None
    PARAMFLAG_FRETVAL = None
    PARAMFLAG_NONE = None
    value__ = None


class PreserveSigAttribute(Attribute, _Attribute):
    """
    Indicates that the HRESULT or retval signature transformation that takes place during COM interop calls should be suppressed.
    
    PreserveSigAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class PrimaryInteropAssemblyAttribute(Attribute, _Attribute):
    """
    Indicates that the attributed assembly is a primary interop assembly.
    
    PrimaryInteropAssemblyAttribute(major: int, minor: int)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, major, minor):
        """ __new__(cls: type, major: int, minor: int) """
        pass

    MajorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the major version number of the type library for which this assembly is the primary interop assembly.

Get: MajorVersion(self: PrimaryInteropAssemblyAttribute) -> int

"""

    MinorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minor version number of the type library for which this assembly is the primary interop assembly.

Get: MinorVersion(self: PrimaryInteropAssemblyAttribute) -> int

"""



class ProgIdAttribute(Attribute, _Attribute):
    """
    Allows the user to specify the ProgID of a class.
    
    ProgIdAttribute(progId: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, progId):
        """ __new__(cls: type, progId: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the ProgID of the class.

Get: Value(self: ProgIdAttribute) -> str

"""



class RegistrationClassContext(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the set of execution contexts in which a class object will be made available for requests to construct instances.
    
    enum (flags) RegistrationClassContext, values: DisableActivateAsActivator (32768), EnableActivateAsActivator (65536), EnableCodeDownload (8192), FromDefaultContext (131072), InProcessHandler (2), InProcessHandler16 (32), InProcessServer (1), InProcessServer16 (8), LocalServer (4), NoCodeDownload (1024), NoCustomMarshal (4096), NoFailureLog (16384), RemoteServer (16), Reserved1 (64), Reserved2 (128), Reserved3 (256), Reserved4 (512), Reserved5 (2048)
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

    DisableActivateAsActivator = None
    EnableActivateAsActivator = None
    EnableCodeDownload = None
    FromDefaultContext = None
    InProcessHandler = None
    InProcessHandler16 = None
    InProcessServer = None
    InProcessServer16 = None
    LocalServer = None
    NoCodeDownload = None
    NoCustomMarshal = None
    NoFailureLog = None
    RemoteServer = None
    Reserved1 = None
    Reserved2 = None
    Reserved3 = None
    Reserved4 = None
    Reserved5 = None
    value__ = None


class RegistrationConnectionType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the types of connections to a class object.
    
    enum (flags) RegistrationConnectionType, values: MultipleUse (1), MultiSeparate (2), SingleUse (0), Surrogate (8), Suspended (4)
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

    MultipleUse = None
    MultiSeparate = None
    SingleUse = None
    Surrogate = None
    Suspended = None
    value__ = None


class RegistrationServices(object, IRegistrationServices):
    """
    Provides a set of services for registering and unregistering managed assemblies for use from COM.
    
    RegistrationServices()
    """
    def GetManagedCategoryGuid(self):
        """
        GetManagedCategoryGuid(self: RegistrationServices) -> Guid
        
            Returns the GUID of the COM category that contains the managed classes.
            Returns: The GUID of the COM category that contains the managed classes.
        """
        pass

    def GetProgIdForType(self, type):
        """
        GetProgIdForType(self: RegistrationServices, type: Type) -> str
        
            Retrieves the COM ProgID for the specified type.
        
            type: The type corresponding to the ProgID that is being requested.
            Returns: The ProgID for the specified type.
        """
        pass

    def GetRegistrableTypesInAssembly(self, assembly):
        """
        GetRegistrableTypesInAssembly(self: RegistrationServices, assembly: Assembly) -> Array[Type]
        
            Retrieves a list of classes in an assembly that would be registered by a call to 
             System.Runtime.InteropServices.RegistrationServices.RegisterAssembly(System.Reflection.Assembly,S
             ystem.Runtime.InteropServices.AssemblyRegistrationFlags).
        
        
            assembly: The assembly to search for classes.
            Returns: A System.Type array containing a list of classes in assembly.
        """
        pass

    def RegisterAssembly(self, assembly, flags):
        """
        RegisterAssembly(self: RegistrationServices, assembly: Assembly, flags: AssemblyRegistrationFlags) -> bool
        
            Registers the classes in a managed assembly to enable creation from COM.
        
            assembly: The assembly to be registered.
            flags: An System.Runtime.InteropServices.AssemblyRegistrationFlags value indicating any special 
             settings used when registering assembly.
        
            Returns: true if assembly contains types that were successfully registered; otherwise false if the 
             assembly contains no eligible types.
        """
        pass

    def RegisterTypeForComClients(self, type, *__args):
        """
        RegisterTypeForComClients(self: RegistrationServices, type: Type, classContext: RegistrationClassContext, flags: RegistrationConnectionType) -> int
        
            Registers the specified type with COM using the specified execution context and connection type.
        
            type: The System.Type object to register for use from COM.
            classContext: One of the System.Runtime.InteropServices.RegistrationClassContext values that indicates the 
             context in which the executable code will be run.
        
            flags: One of the System.Runtime.InteropServices.RegistrationConnectionType values that specifies how 
             connections are made to the class object.
        
            Returns: An integer that represents a cookie value.
        RegisterTypeForComClients(self: RegistrationServices, type: Type, g: Guid) -> Guid
        
            Registers the specified type with COM using the specified GUID.
        
            type: The System.Type to be registered for use from COM.
            g: The System.Guid used to register the specified type.
        """
        pass

    def TypeRepresentsComType(self, type):
        """
        TypeRepresentsComType(self: RegistrationServices, type: Type) -> bool
        
            Indicates whether a type is marked with the System.Runtime.InteropServices.ComImportAttribute, 
             or derives from a type marked with the System.Runtime.InteropServices.ComImportAttribute and 
             shares the same GUID as the parent.
        
        
            type: The type to check for being a COM type.
            Returns: true if a type is marked with the System.Runtime.InteropServices.ComImportAttribute, or derives 
             from a type marked with the System.Runtime.InteropServices.ComImportAttribute and shares the 
             same GUID as the parent; otherwise false.
        """
        pass

    def TypeRequiresRegistration(self, type):
        """
        TypeRequiresRegistration(self: RegistrationServices, type: Type) -> bool
        
            Determines whether the specified type requires registration.
        
            type: The type to check for COM registration requirements.
            Returns: true if the type must be registered for use from COM; otherwise false.
        """
        pass

    def UnregisterAssembly(self, assembly):
        """
        UnregisterAssembly(self: RegistrationServices, assembly: Assembly) -> bool
        
            Unregisters the classes in a managed assembly.
        
            assembly: The assembly to be unregistered.
            Returns: true if assembly contains types that were successfully unregistered; otherwise false if the 
             assembly contains no eligible types.
        """
        pass

    def UnregisterTypeForComClients(self, cookie):
        """
        UnregisterTypeForComClients(self: RegistrationServices, cookie: int)
            Removes references to a type registered with the 
             System.Runtime.InteropServices.RegistrationServices.RegisterTypeForComClients(System.Type,System.
             Runtime.InteropServices.RegistrationClassContext,System.Runtime.InteropServices.RegistrationConne
             ctionType) method.
        
        
            cookie: The cookie value returned by a previous call to the 
             System.Runtime.InteropServices.RegistrationServices.RegisterTypeForComClients(System.Type,System.
             Runtime.InteropServices.RegistrationClassContext,System.Runtime.InteropServices.RegistrationConne
             ctionType) method overload.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class RuntimeEnvironment(object):
    """
    Provides a collection of static methods that return information about the common language runtime environment.
    
    RuntimeEnvironment()
    """
    @staticmethod
    def FromGlobalAccessCache(a):
        """
        FromGlobalAccessCache(a: Assembly) -> bool
        
            Tests whether the specified assembly is loaded in the global assembly cache.
        
            a: The assembly to test.
            Returns: true if the assembly is loaded in the global assembly cache; otherwise, false.
        """
        pass

    @staticmethod
    def GetRuntimeDirectory():
        """
        GetRuntimeDirectory() -> str
        
            Returns the directory where the common language runtime is installed.
            Returns: A string that contains the path to the directory where the common language runtime is installed.
        """
        pass

    @staticmethod
    def GetRuntimeInterfaceAsIntPtr(clsid, riid):
        """
        GetRuntimeInterfaceAsIntPtr(clsid: Guid, riid: Guid) -> IntPtr
        
            Returns the specified interface on the specified class.
        
            clsid: The identifier for the desired class.
            riid: The identifier for the desired interface.
            Returns: An unmanaged pointer to the requested interface.
        """
        pass

    @staticmethod
    def GetRuntimeInterfaceAsObject(clsid, riid):
        """
        GetRuntimeInterfaceAsObject(clsid: Guid, riid: Guid) -> object
        
            Returns an instance of a type that represents a COM object by a pointer to its IUnknown 
             interface.
        
        
            clsid: The identifier for the desired class.
            riid: The identifier for the desired interface.
            Returns: An object that represents the specified unmanaged COM object.
        """
        pass

    @staticmethod
    def GetSystemVersion():
        """
        GetSystemVersion() -> str
        
            Gets the version number of the common language runtime that is running the current process.
            Returns: A string containing the version number of the common language runtime.
        """
        pass

    SystemConfigurationFile = 'C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\config\\machine.config'


class SafeArrayRankMismatchException(SystemException, ISerializable, _Exception):
    """
    The exception thrown when the rank of an incoming SAFEARRAY does not match the rank specified in the managed signature.
    
    SafeArrayRankMismatchException()
    SafeArrayRankMismatchException(message: str)
    SafeArrayRankMismatchException(message: str, inner: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class SafeArrayTypeMismatchException(SystemException, ISerializable, _Exception):
    """
    The exception thrown when the type of the incoming SAFEARRAY does not match the type specified in the managed signature.
    
    SafeArrayTypeMismatchException()
    SafeArrayTypeMismatchException(message: str)
    SafeArrayTypeMismatchException(message: str, inner: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class SafeHandle(CriticalFinalizerObject, IDisposable):
    """ Represents a wrapper class for operating system handles. This class must be inherited. """
    def Close(self):
        """
        Close(self: SafeHandle)
            Marks the handle for releasing and freeing resources.
        """
        pass

    def DangerousAddRef(self, success):
        """
        DangerousAddRef(self: SafeHandle, success: bool) -> bool
        
            Manually increments the reference counter on System.Runtime.InteropServices.SafeHandle instances.
        
            success: true if the reference counter was successfully incremented; otherwise, false.
        """
        pass

    def DangerousGetHandle(self):
        """
        DangerousGetHandle(self: SafeHandle) -> IntPtr
        
            Returns the value of the System.Runtime.InteropServices.SafeHandle.handle field.
            Returns: An IntPtr representing the value of the System.Runtime.InteropServices.SafeHandle.handle field. 
             If the handle has been marked invalid with 
             System.Runtime.InteropServices.SafeHandle.SetHandleAsInvalid, this method still returns the 
             original handle value, which can be a stale value.
        """
        pass

    def DangerousRelease(self):
        """
        DangerousRelease(self: SafeHandle)
            Manually decrements the reference counter on a System.Runtime.InteropServices.SafeHandle 
             instance.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SafeHandle)
            Releases all resources used by the System.Runtime.InteropServices.SafeHandle class.
        """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """
        ReleaseHandle(self: SafeHandle) -> bool
        
            When overridden in a derived class, executes the code required to free the handle.
            Returns: true if the handle is released successfully; otherwise, in the event of a catastrophic failure, 
             false. In this case, it generates a releaseHandleFailed MDA Managed Debugging Assistant.
        """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """
        SetHandle(self: SafeHandle, handle: IntPtr)
            Sets the handle to the specified pre-existing handle.
        
            handle: The pre-existing handle to use.
        """
        pass

    def SetHandleAsInvalid(self):
        """
        SetHandleAsInvalid(self: SafeHandle)
            Marks a handle as no longer used.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, invalidHandleValue: IntPtr, ownsHandle: bool) """
        pass

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the handle is closed.

Get: IsClosed(self: SafeHandle) -> bool

"""

    IsInvalid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a value indicating whether the handle value is invalid.

Get: IsInvalid(self: SafeHandle) -> bool

"""


    handle = None


class SafeBuffer(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """ Provides a controlled memory buffer that can be used for reading and writing. Attempts to access memory outside the controlled buffer (underruns and overruns) raise exceptions. """
    def AcquirePointer(self, pointer):
        """
        AcquirePointer(self: SafeBuffer, pointer: Byte*) -> Byte*
        
            Obtains a pointer from a System.Runtime.InteropServices.SafeBuffer object for a block of memory.
        
            pointer: A byte pointer, passed by reference, to receive the pointer from within the 
             System.Runtime.InteropServices.SafeBuffer object. You must set this pointer to null before you 
             call this method.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SafeHandle, disposing: bool)
            Releases the unmanaged resources used by the System.Runtime.InteropServices.SafeHandle class 
             specifying whether to perform a normal dispose operation.
        
        
            disposing: true for a normal dispose operation; false to finalize the handle.
        """
        pass

    def Initialize(self, *__args):
        """
        Initialize[T](self: SafeBuffer, numElements: UInt32)Initialize(self: SafeBuffer, numElements: UInt32, sizeOfEachElement: UInt32)
            Specifies the allocation size of the memory buffer by using the specified number of elements and 
             element size. You must call this method before you use the 
             System.Runtime.InteropServices.SafeBuffer instance.
        
        
            numElements: The number of elements in the buffer.
            sizeOfEachElement: The size of each element in the buffer.
        Initialize(self: SafeBuffer, numBytes: UInt64)
            Defines the allocation size of the memory region in bytes. You must call this method before you 
             use the System.Runtime.InteropServices.SafeBuffer instance.
        
        
            numBytes: The number of bytes in the buffer.
        """
        pass

    def Read(self, byteOffset):
        """ Read[T](self: SafeBuffer, byteOffset: UInt64) -> T """
        pass

    def ReadArray(self, byteOffset, array, index, count):
        """ ReadArray[T](self: SafeBuffer, byteOffset: UInt64, array: Array[T], index: int, count: int) """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """
        ReleaseHandle(self: SafeHandle) -> bool
        
            When overridden in a derived class, executes the code required to free the handle.
            Returns: true if the handle is released successfully; otherwise, in the event of a catastrophic failure, 
             false. In this case, it generates a releaseHandleFailed MDA Managed Debugging Assistant.
        """
        pass

    def ReleasePointer(self):
        """
        ReleasePointer(self: SafeBuffer)
            Releases a pointer that was obtained by the 
             System.Runtime.InteropServices.SafeBuffer.AcquirePointer(System.Byte*@) method.
        """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """
        SetHandle(self: SafeHandle, handle: IntPtr)
            Sets the handle to the specified pre-existing handle.
        
            handle: The pre-existing handle to use.
        """
        pass

    def Write(self, byteOffset, value):
        """ Write[T](self: SafeBuffer, byteOffset: UInt64, value: T) """
        pass

    def WriteArray(self, byteOffset, array, index, count):
        """ WriteArray[T](self: SafeBuffer, byteOffset: UInt64, array: Array[T], index: int, count: int) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, ownsHandle: bool) """
        pass

    ByteLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the buffer, in bytes.

Get: ByteLength(self: SafeBuffer) -> UInt64

"""


    handle = None


class SEHException(ExternalException, ISerializable, _Exception):
    """
    Represents structured exception handling (SEH) errors.
    
    SEHException()
    SEHException(message: str)
    SEHException(message: str, inner: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def CanResume(self):
        """
        CanResume(self: SEHException) -> bool
        
            Indicates whether the exception can be recovered from, and whether the code can continue from 
             the point at which the exception was thrown.
        
            Returns: Always false, because resumable exceptions are not implemented.
        """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class SetWin32ContextInIDispatchAttribute(Attribute, _Attribute):
    """
    This attribute has been deprecated.
    
    SetWin32ContextInIDispatchAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class StandardOleMarshalObject(MarshalByRefObject, IMarshal):
    """ Replaces the standard common language runtime (CLR) free-threaded marshaler with the standard OLE STA marshaler. """
    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class STATSTG(object):
    """ Use System.Runtime.InteropServices.ComTypes.STATSTG instead. """
    atime = None
    cbSize = None
    clsid = None
    ctime = None
    grfLocksSupported = None
    grfMode = None
    grfStateBits = None
    mtime = None
    pwcsName = None
    reserved = None
    type = None


class StructLayoutAttribute(Attribute, _Attribute):
    """
    Lets you control the physical layout of the data fields of a class or structure.
    
    StructLayoutAttribute(layoutKind: LayoutKind)
    StructLayoutAttribute(layoutKind: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, layoutKind):
        """
        __new__(cls: type, layoutKind: LayoutKind)
        __new__(cls: type, layoutKind: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Runtime.InteropServices.LayoutKind value that specifies how the class or structure is arranged.

Get: Value(self: StructLayoutAttribute) -> LayoutKind

"""


    CharSet = None
    Pack = None
    Size = None


class SYSKIND(Enum, IComparable, IFormattable, IConvertible):
    """
    Use System.Runtime.InteropServices.ComTypes.SYSKIND instead.
    
    enum SYSKIND, values: SYS_MAC (2), SYS_WIN16 (0), SYS_WIN32 (1)
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

    SYS_MAC = None
    SYS_WIN16 = None
    SYS_WIN32 = None
    value__ = None


class TYPEATTR(object):
    """ Use System.Runtime.InteropServices.ComTypes.TYPEATTR instead. """
    cbAlignment = None
    cbSizeInstance = None
    cbSizeVft = None
    cFuncs = None
    cImplTypes = None
    cVars = None
    dwReserved = None
    guid = None
    idldescType = None
    lcid = None
    lpstrSchema = None
    MEMBER_ID_NIL = -1
    memidConstructor = None
    memidDestructor = None
    tdescAlias = None
    typekind = None
    wMajorVerNum = None
    wMinorVerNum = None
    wTypeFlags = None


class TYPEDESC(object):
    """ Use System.Runtime.InteropServices.ComTypes.TYPEDESC instead. """
    lpValue = None
    vt = None


class TYPEFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """
    Use System.Runtime.InteropServices.ComTypes.TYPEFLAGS instead.
    
    enum (flags) TYPEFLAGS, values: TYPEFLAG_FAGGREGATABLE (1024), TYPEFLAG_FAPPOBJECT (1), TYPEFLAG_FCANCREATE (2), TYPEFLAG_FCONTROL (32), TYPEFLAG_FDISPATCHABLE (4096), TYPEFLAG_FDUAL (64), TYPEFLAG_FHIDDEN (16), TYPEFLAG_FLICENSED (4), TYPEFLAG_FNONEXTENSIBLE (128), TYPEFLAG_FOLEAUTOMATION (256), TYPEFLAG_FPREDECLID (8), TYPEFLAG_FPROXY (16384), TYPEFLAG_FREPLACEABLE (2048), TYPEFLAG_FRESTRICTED (512), TYPEFLAG_FREVERSEBIND (8192)
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

    TYPEFLAG_FAGGREGATABLE = None
    TYPEFLAG_FAPPOBJECT = None
    TYPEFLAG_FCANCREATE = None
    TYPEFLAG_FCONTROL = None
    TYPEFLAG_FDISPATCHABLE = None
    TYPEFLAG_FDUAL = None
    TYPEFLAG_FHIDDEN = None
    TYPEFLAG_FLICENSED = None
    TYPEFLAG_FNONEXTENSIBLE = None
    TYPEFLAG_FOLEAUTOMATION = None
    TYPEFLAG_FPREDECLID = None
    TYPEFLAG_FPROXY = None
    TYPEFLAG_FREPLACEABLE = None
    TYPEFLAG_FRESTRICTED = None
    TYPEFLAG_FREVERSEBIND = None
    value__ = None


class TypeIdentifierAttribute(Attribute, _Attribute):
    """
    Provides support for type equivalence.
    
    TypeIdentifierAttribute()
    TypeIdentifierAttribute(scope: str, identifier: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, scope=None, identifier=None):
        """
        __new__(cls: type)
        __new__(cls: type, scope: str, identifier: str)
        """
        pass

    Identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the identifier parameter that was passed to the System.Runtime.InteropServices.TypeIdentifierAttribute.#ctor(System.String,System.String) constructor.

Get: Identifier(self: TypeIdentifierAttribute) -> str

"""

    Scope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the scope parameter that was passed to the System.Runtime.InteropServices.TypeIdentifierAttribute.#ctor(System.String,System.String) constructor.

Get: Scope(self: TypeIdentifierAttribute) -> str

"""



class TYPEKIND(Enum, IComparable, IFormattable, IConvertible):
    """
    Use System.Runtime.InteropServices.ComTypes.TYPEKIND instead.
    
    enum TYPEKIND, values: TKIND_ALIAS (6), TKIND_COCLASS (5), TKIND_DISPATCH (4), TKIND_ENUM (0), TKIND_INTERFACE (3), TKIND_MAX (8), TKIND_MODULE (2), TKIND_RECORD (1), TKIND_UNION (7)
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

    TKIND_ALIAS = None
    TKIND_COCLASS = None
    TKIND_DISPATCH = None
    TKIND_ENUM = None
    TKIND_INTERFACE = None
    TKIND_MAX = None
    TKIND_MODULE = None
    TKIND_RECORD = None
    TKIND_UNION = None
    value__ = None


class TYPELIBATTR(object):
    """ Use System.Runtime.InteropServices.ComTypes.TYPELIBATTR instead. """
    guid = None
    lcid = None
    syskind = None
    wLibFlags = None
    wMajorVerNum = None
    wMinorVerNum = None


class TypeLibConverter(object, ITypeLibConverter):
    """
    Provides a set of services that convert a managed assembly to a COM type library and vice versa.
    
    TypeLibConverter()
    """
    def ConvertAssemblyToTypeLib(self, assembly, strTypeLibName, flags, notifySink):
        """
        ConvertAssemblyToTypeLib(self: TypeLibConverter, assembly: Assembly, strTypeLibName: str, flags: TypeLibExporterFlags, notifySink: ITypeLibExporterNotifySink) -> object
        
            Converts an assembly to a COM type library.
        
            assembly: The assembly to convert.
            strTypeLibName: The file name of the resulting type library.
            flags: A System.Runtime.InteropServices.TypeLibExporterFlags value indicating any special settings.
            notifySink: The System.Runtime.InteropServices.ITypeLibExporterNotifySink interface implemented by the 
             caller.
        
            Returns: An object that implements the ITypeLib interface.
        """
        pass

    def ConvertTypeLibToAssembly(self, typeLib, asmFileName, flags, notifySink, publicKey, keyPair, *__args):
        """
        ConvertTypeLibToAssembly(self: TypeLibConverter, typeLib: object, asmFileName: str, flags: TypeLibImporterFlags, notifySink: ITypeLibImporterNotifySink, publicKey: Array[Byte], keyPair: StrongNameKeyPair, asmNamespace: str, asmVersion: Version) -> AssemblyBuilder
        
            Converts a COM type library to an assembly.
        
            typeLib: The object that implements the ITypeLib interface.
            asmFileName: The file name of the resulting assembly.
            flags: A System.Runtime.InteropServices.TypeLibImporterFlags value indicating any special settings.
            notifySink: System.Runtime.InteropServices.ITypeLibImporterNotifySink interface implemented by the caller.
            publicKey: A byte array containing the public key.
            keyPair: A System.Reflection.StrongNameKeyPair object containing the public and private cryptographic key 
             pair.
        
            asmNamespace: The namespace for the resulting assembly.
            asmVersion: The version of the resulting assembly. If null, the version of the type library is used.
            Returns: An System.Reflection.Emit.AssemblyBuilder object containing the converted type library.
        ConvertTypeLibToAssembly(self: TypeLibConverter, typeLib: object, asmFileName: str, flags: int, notifySink: ITypeLibImporterNotifySink, publicKey: Array[Byte], keyPair: StrongNameKeyPair, unsafeInterfaces: bool) -> AssemblyBuilder
        
            Converts a COM type library to an assembly.
        
            typeLib: The object that implements the ITypeLib interface.
            asmFileName: The file name of the resulting assembly.
            flags: A System.Runtime.InteropServices.TypeLibImporterFlags value indicating any special settings.
            notifySink: System.Runtime.InteropServices.ITypeLibImporterNotifySink interface implemented by the caller.
            publicKey: A byte array containing the public key.
            keyPair: A System.Reflection.StrongNameKeyPair object containing the public and private cryptographic key 
             pair.
        
            unsafeInterfaces: If true, the interfaces require link time checks for 
             System.Security.Permissions.SecurityPermissionFlag.UnmanagedCode permission. If false, the 
             interfaces require run time checks that require a stack walk and are more expensive, but help 
             provide greater protection.
        
            Returns: An System.Reflection.Emit.AssemblyBuilder object containing the converted type library.
        """
        pass

    def GetPrimaryInteropAssembly(self, g, major, minor, lcid, asmName, asmCodeBase):
        """
        GetPrimaryInteropAssembly(self: TypeLibConverter, g: Guid, major: int, minor: int, lcid: int) -> (bool, str, str)
        
            Gets the name and code base of a primary interop assembly for a specified type library.
        
            g: The GUID of the type library.
            major: The major version number of the type library.
            minor: The minor version number of the type library.
            lcid: The LCID of the type library.
            Returns: true if the primary interop assembly was found in the registry; otherwise false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class TypeLibExporterFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates how a type library should be produced.
    
    enum (flags) TypeLibExporterFlags, values: CallerResolvedReferences (2), ExportAs32Bit (16), ExportAs64Bit (32), None (0), OldNames (4), OnlyReferenceRegistered (1)
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

    CallerResolvedReferences = None
    ExportAs32Bit = None
    ExportAs64Bit = None
    None = None
    OldNames = None
    OnlyReferenceRegistered = None
    value__ = None


class TypeLibFuncAttribute(Attribute, _Attribute):
    """
    Contains the System.Runtime.InteropServices.FUNCFLAGS that were originally imported for this method from the COM type library.
    
    TypeLibFuncAttribute(flags: TypeLibFuncFlags)
    TypeLibFuncAttribute(flags: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, flags):
        """
        __new__(cls: type, flags: TypeLibFuncFlags)
        __new__(cls: type, flags: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Runtime.InteropServices.TypeLibFuncFlags value for this method.

Get: Value(self: TypeLibFuncAttribute) -> TypeLibFuncFlags

"""



class TypeLibFuncFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the original settings of the FUNCFLAGS in the COM type library from where this method was imported.
    
    enum (flags) TypeLibFuncFlags, values: FBindable (4), FDefaultBind (32), FDefaultCollelem (256), FDisplayBind (16), FHidden (64), FImmediateBind (4096), FNonBrowsable (1024), FReplaceable (2048), FRequestEdit (8), FRestricted (1), FSource (2), FUiDefault (512), FUsesGetLastError (128)
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

    FBindable = None
    FDefaultBind = None
    FDefaultCollelem = None
    FDisplayBind = None
    FHidden = None
    FImmediateBind = None
    FNonBrowsable = None
    FReplaceable = None
    FRequestEdit = None
    FRestricted = None
    FSource = None
    FUiDefault = None
    FUsesGetLastError = None
    value__ = None


class TypeLibImportClassAttribute(Attribute, _Attribute):
    """
    Specifies which System.Type exclusively uses an interface. This class cannot be inherited.
    
    TypeLibImportClassAttribute(importClass: Type)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, importClass):
        """ __new__(cls: type, importClass: Type) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of a System.Type object that exclusively uses an interface.

Get: Value(self: TypeLibImportClassAttribute) -> str

"""



class TypeLibImporterFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates how an assembly should be produced.
    
    enum (flags) TypeLibImporterFlags, values: ImportAsAgnostic (2048), ImportAsArm (16384), ImportAsItanium (1024), ImportAsX64 (512), ImportAsX86 (256), NoDefineVersionResource (8192), None (0), PreventClassMembers (16), PrimaryInteropAssembly (1), ReflectionOnlyLoading (4096), SafeArrayAsSystemArray (4), SerializableValueClasses (32), TransformDispRetVals (8), UnsafeInterfaces (2)
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

    ImportAsAgnostic = None
    ImportAsArm = None
    ImportAsItanium = None
    ImportAsX64 = None
    ImportAsX86 = None
    NoDefineVersionResource = None
    None = None
    PreventClassMembers = None
    PrimaryInteropAssembly = None
    ReflectionOnlyLoading = None
    SafeArrayAsSystemArray = None
    SerializableValueClasses = None
    TransformDispRetVals = None
    UnsafeInterfaces = None
    value__ = None


class TypeLibTypeAttribute(Attribute, _Attribute):
    """
    Contains the System.Runtime.InteropServices.TYPEFLAGS that were originally imported for this type from the COM type library.
    
    TypeLibTypeAttribute(flags: TypeLibTypeFlags)
    TypeLibTypeAttribute(flags: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, flags):
        """
        __new__(cls: type, flags: TypeLibTypeFlags)
        __new__(cls: type, flags: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Runtime.InteropServices.TypeLibTypeFlags value for this type.

Get: Value(self: TypeLibTypeAttribute) -> TypeLibTypeFlags

"""



class TypeLibTypeFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the original settings of the System.Runtime.InteropServices.TYPEFLAGS in the COM type library from which the type was imported.
    
    enum (flags) TypeLibTypeFlags, values: FAggregatable (1024), FAppObject (1), FCanCreate (2), FControl (32), FDispatchable (4096), FDual (64), FHidden (16), FLicensed (4), FNonExtensible (128), FOleAutomation (256), FPreDeclId (8), FReplaceable (2048), FRestricted (512), FReverseBind (8192)
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

    FAggregatable = None
    FAppObject = None
    FCanCreate = None
    FControl = None
    FDispatchable = None
    FDual = None
    FHidden = None
    FLicensed = None
    FNonExtensible = None
    FOleAutomation = None
    FPreDeclId = None
    FReplaceable = None
    FRestricted = None
    FReverseBind = None
    value__ = None


class TypeLibVarAttribute(Attribute, _Attribute):
    """
    Contains the System.Runtime.InteropServices.VARFLAGS that were originally imported for this field from the COM type library.
    
    TypeLibVarAttribute(flags: TypeLibVarFlags)
    TypeLibVarAttribute(flags: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, flags):
        """
        __new__(cls: type, flags: TypeLibVarFlags)
        __new__(cls: type, flags: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Runtime.InteropServices.TypeLibVarFlags value for this field.

Get: Value(self: TypeLibVarAttribute) -> TypeLibVarFlags

"""



class TypeLibVarFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the original settings of the System.Runtime.InteropServices.VARFLAGS in the COM type library from which the variable was imported.
    
    enum (flags) TypeLibVarFlags, values: FBindable (4), FDefaultBind (32), FDefaultCollelem (256), FDisplayBind (16), FHidden (64), FImmediateBind (4096), FNonBrowsable (1024), FReadOnly (1), FReplaceable (2048), FRequestEdit (8), FRestricted (128), FSource (2), FUiDefault (512)
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

    FBindable = None
    FDefaultBind = None
    FDefaultCollelem = None
    FDisplayBind = None
    FHidden = None
    FImmediateBind = None
    FNonBrowsable = None
    FReadOnly = None
    FReplaceable = None
    FRequestEdit = None
    FRestricted = None
    FSource = None
    FUiDefault = None
    value__ = None


class TypeLibVersionAttribute(Attribute, _Attribute):
    """
    Specifies the version number of an exported type library.
    
    TypeLibVersionAttribute(major: int, minor: int)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, major, minor):
        """ __new__(cls: type, major: int, minor: int) """
        pass

    MajorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the major version number of the type library.

Get: MajorVersion(self: TypeLibVersionAttribute) -> int

"""

    MinorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minor version number of the type library.

Get: MinorVersion(self: TypeLibVersionAttribute) -> int

"""



class UCOMIBindCtx:
    """ Use System.Runtime.InteropServices.ComTypes.BIND_OPTS instead. """
    def EnumObjectParam(self, ppenum):
        """
        EnumObjectParam(self: UCOMIBindCtx) -> UCOMIEnumString
        
            Enumerate the strings which are the keys of the internally-maintained table of contextual object 
             parameters.
        """
        pass

    def GetBindOptions(self, pbindopts):
        """
        GetBindOptions(self: UCOMIBindCtx, pbindopts: BIND_OPTS) -> BIND_OPTS
        
            Return the current binding options stored in this bind context.
        
            pbindopts: A pointer to the structure to receive the binding options.
        """
        pass

    def GetObjectParam(self, pszKey, ppunk):
        """
        GetObjectParam(self: UCOMIBindCtx, pszKey: str) -> object
        
            Lookup the given key in the internally-maintained table of contextual object parameters and 
             return the corresponding object, if one exists.
        
        
            pszKey: The name of the object to search for.
        """
        pass

    def GetRunningObjectTable(self, pprot):
        """
        GetRunningObjectTable(self: UCOMIBindCtx) -> UCOMIRunningObjectTable
        
            Return access to the Running Object Table (ROT) relevant to this binding process.
        """
        pass

    def RegisterObjectBound(self, punk):
        """
        RegisterObjectBound(self: UCOMIBindCtx, punk: object)
            Register the passed object as one of the objects that has been bound during a moniker operation 
             and which should be released when it is complete.
        
        
            punk: The object to register for release.
        """
        pass

    def RegisterObjectParam(self, pszKey, punk):
        """
        RegisterObjectParam(self: UCOMIBindCtx, pszKey: str, punk: object)
            Register the given object pointer under the specified name in the internally-maintained table of 
             object pointers.
        
        
            pszKey: The name to register punk with.
            punk: The object to register.
        """
        pass

    def ReleaseBoundObjects(self):
        """
        ReleaseBoundObjects(self: UCOMIBindCtx)
            Releases all the objects currently registered with the bind context by 
             System.Runtime.InteropServices.UCOMIBindCtx.RegisterObjectBound(System.Object).
        """
        pass

    def RevokeObjectBound(self, punk):
        """
        RevokeObjectBound(self: UCOMIBindCtx, punk: object)
            Removes the object from the set of registered objects that need to be released.
        
            punk: The object to unregister for release.
        """
        pass

    def RevokeObjectParam(self, pszKey):
        """
        RevokeObjectParam(self: UCOMIBindCtx, pszKey: str)
            Revoke the registration of the object currently found under this key in the 
             internally-maintained table of contextual object parameters, if any such key is currently 
             registered.
        
        
            pszKey: The key to unregister.
        """
        pass

    def SetBindOptions(self, pbindopts):
        """
        SetBindOptions(self: UCOMIBindCtx, pbindopts: BIND_OPTS) -> BIND_OPTS
        
            Store in the bind context a block of parameters that will apply to later UCOMIMoniker operations 
             using this bind context.
        
        
            pbindopts: The structure containing the binding options to set.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIConnectionPoint:
    """ Use System.Runtime.InteropServices.ComTypes.IConnectionPoint instead. """
    def Advise(self, pUnkSink, pdwCookie):
        """
        Advise(self: UCOMIConnectionPoint, pUnkSink: object) -> int
        
            Establishes an advisory connection between the connection point and the caller's sink object.
        
            pUnkSink: Reference to the sink to receive calls for the outgoing interface managed by this connection 
             point.
        """
        pass

    def EnumConnections(self, ppEnum):
        """
        EnumConnections(self: UCOMIConnectionPoint) -> UCOMIEnumConnections
        
            Creates an enumerator object for iteration through the connections that exist to this connection 
             point.
        """
        pass

    def GetConnectionInterface(self, pIID):
        """
        GetConnectionInterface(self: UCOMIConnectionPoint) -> Guid
        
            Returns the IID of the outgoing interface managed by this connection point.
        """
        pass

    def GetConnectionPointContainer(self, ppCPC):
        """
        GetConnectionPointContainer(self: UCOMIConnectionPoint) -> UCOMIConnectionPointContainer
        
            Retrieves the IConnectionPointContainer interface pointer to the connectable object that 
             conceptually owns this connection point.
        """
        pass

    def Unadvise(self, dwCookie):
        """
        Unadvise(self: UCOMIConnectionPoint, dwCookie: int)
            Terminates an advisory connection previously established through 
             System.Runtime.InteropServices.UCOMIConnectionPoint.Advise(System.Object,System.Int32@).
        
        
            dwCookie: The connection cookie previously returned from 
             System.Runtime.InteropServices.UCOMIConnectionPoint.Advise(System.Object,System.Int32@).
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIConnectionPointContainer:
    """ Use System.Runtime.InteropServices.ComTypes.IConnectionPointContainer instead. """
    def EnumConnectionPoints(self, ppEnum):
        """
        EnumConnectionPoints(self: UCOMIConnectionPointContainer) -> UCOMIEnumConnectionPoints
        
            Creates an enumerator of all the connection points supported in the connectable object, one 
             connection point per IID.
        """
        pass

    def FindConnectionPoint(self, riid, ppCP):
        """
        FindConnectionPoint(self: UCOMIConnectionPointContainer, riid: Guid) -> (Guid, UCOMIConnectionPoint)
        
            Asks the connectable object if it has a connection point for a particular IID, and if so, 
             returns the IConnectionPoint interface pointer to that connection point.
        
        
            riid: A reference to the outgoing interface IID whose connection point is being requested.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIEnumConnectionPoints:
    """ Use System.Runtime.InteropServices.ComTypes.IEnumConnectionPoints instead. """
    def Clone(self, ppenum):
        """
        Clone(self: UCOMIEnumConnectionPoints) -> UCOMIEnumConnectionPoints
        
            Creates another enumerator that contains the same enumeration state as the current one.
        """
        pass

    def Next(self, celt, rgelt, pceltFetched):
        """
        Next(self: UCOMIEnumConnectionPoints, celt: int) -> (int, Array[UCOMIConnectionPoint], int)
        
            Retrieves a specified number of items in the enumeration sequence.
        
            celt: The number of IConnectionPoint references to return in rgelt.
            Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def Reset(self):
        """
        Reset(self: UCOMIEnumConnectionPoints) -> int
        
            Resets the enumeration sequence to the beginning.
            Returns: An HRESULT with the value S_OK.
        """
        pass

    def Skip(self, celt):
        """
        Skip(self: UCOMIEnumConnectionPoints, celt: int) -> int
        
            Skips over a specified number of items in the enumeration sequence.
        
            celt: The number of elements to skip in the enumeration.
            Returns: S_OK if the number of elements skipped equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIEnumConnections:
    """ Use System.Runtime.InteropServices.ComTypes.IEnumConnections instead. """
    def Clone(self, ppenum):
        """
        Clone(self: UCOMIEnumConnections) -> UCOMIEnumConnections
        
            Creates another enumerator that contains the same enumeration state as the current one.
        """
        pass

    def Next(self, celt, rgelt, pceltFetched):
        """
        Next(self: UCOMIEnumConnections, celt: int) -> (int, Array[CONNECTDATA], int)
        
            Retrieves a specified number of items in the enumeration sequence.
        
            celt: The number of System.Runtime.InteropServices.CONNECTDATA structures to return in rgelt.
            Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def Reset(self):
        """
        Reset(self: UCOMIEnumConnections)
            Resets the enumeration sequence to the beginning.
        """
        pass

    def Skip(self, celt):
        """
        Skip(self: UCOMIEnumConnections, celt: int) -> int
        
            Skips over a specified number of items in the enumeration sequence.
        
            celt: The number of elements to skip in the enumeration.
            Returns: S_OK if the number of elements skipped equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIEnumMoniker:
    """ Use System.Runtime.InteropServices.ComTypes.IEnumMoniker instead. """
    def Clone(self, ppenum):
        """
        Clone(self: UCOMIEnumMoniker) -> UCOMIEnumMoniker
        
            Creates another enumerator that contains the same enumeration state as the current one.
        """
        pass

    def Next(self, celt, rgelt, pceltFetched):
        """
        Next(self: UCOMIEnumMoniker, celt: int) -> (int, Array[UCOMIMoniker], int)
        
            Retrieves a specified number of items in the enumeration sequence.
        
            celt: The number of monikers to return in rgelt.
            Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def Reset(self):
        """
        Reset(self: UCOMIEnumMoniker) -> int
        
            Resets the enumeration sequence to the beginning.
            Returns: An HRESULT with the value S_OK.
        """
        pass

    def Skip(self, celt):
        """
        Skip(self: UCOMIEnumMoniker, celt: int) -> int
        
            Skips over a specified number of items in the enumeration sequence.
        
            celt: The number of elements to skip in the enumeration.
            Returns: S_OK if the number of elements skipped equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIEnumString:
    """ Use System.Runtime.InteropServices.ComTypes.IEnumString instead. """
    def Clone(self, ppenum):
        """
        Clone(self: UCOMIEnumString) -> UCOMIEnumString
        
            Creates another enumerator that contains the same enumeration state as the current one.
        """
        pass

    def Next(self, celt, rgelt, pceltFetched):
        """
        Next(self: UCOMIEnumString, celt: int) -> (int, Array[str], int)
        
            Retrieves a specified number of items in the enumeration sequence.
        
            celt: The number of strings to return in rgelt.
            Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def Reset(self):
        """
        Reset(self: UCOMIEnumString) -> int
        
            Resets the enumeration sequence to the beginning.
            Returns: An HRESULT with the value S_OK.
        """
        pass

    def Skip(self, celt):
        """
        Skip(self: UCOMIEnumString, celt: int) -> int
        
            Skips over a specified number of items in the enumeration sequence.
        
            celt: The number of elements to skip in the enumeration.
            Returns: S_OK if the number of elements skipped equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIEnumVARIANT:
    """ Use System.Runtime.InteropServices.ComTypes.IEnumVARIANT instead. """
    def Clone(self, ppenum):
        """
        Clone(self: UCOMIEnumVARIANT, ppenum: int)
            Creates another enumerator that contains the same enumeration state as the current one.
        
            ppenum: On successful return, a reference to the newly created enumerator.
        """
        pass

    def Next(self, celt, rgvar, pceltFetched):
        """
        Next(self: UCOMIEnumVARIANT, celt: int, rgvar: int, pceltFetched: int) -> int
        
            Retrieves a specified number of items in the enumeration sequence.
        
            celt: The number of elements to return in rgelt.
            rgvar: On successful return, a reference to the enumerated elements.
            pceltFetched: On successful return, a reference to the actual number of elements enumerated in rgelt.
            Returns: S_OK if the pceltFetched parameter equals the celt parameter; otherwise, S_FALSE.
        """
        pass

    def Reset(self):
        """
        Reset(self: UCOMIEnumVARIANT) -> int
        
            Resets the enumeration sequence to the beginning.
            Returns: An HRESULT with the value S_OK.
        """
        pass

    def Skip(self, celt):
        """
        Skip(self: UCOMIEnumVARIANT, celt: int) -> int
        
            Skips over a specified number of items in the enumeration sequence.
        
            celt: The number of elements to skip in the enumeration.
            Returns: S_OK if the number of elements skipped equals celt parameter; otherwise, S_FALSE.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIMoniker:
    """ Use System.Runtime.InteropServices.ComTypes.IMoniker instead. """
    def BindToObject(self, pbc, pmkToLeft, riidResult, ppvResult):
        """
        BindToObject(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, riidResult: Guid) -> (Guid, object)
        
            Uses the moniker to bind to the object it identifies.
        
            pbc: A reference to the IBindCtx interface on the bind context object used in this binding operation.
            pmkToLeft: A reference to the moniker to the left of this moniker, if the moniker is part of a composite 
             moniker.
        
            riidResult: The interface identifier (IID) of the interface the client intends to use to communicate with 
             the object that the moniker identifies.
        """
        pass

    def BindToStorage(self, pbc, pmkToLeft, riid, ppvObj):
        """
        BindToStorage(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, riid: Guid) -> (Guid, object)
        
            Retrieves an interface pointer to the storage that contains the object identified by the moniker.
        
            pbc: A reference to the IBindCtx interface on the bind context object used during this binding 
             operation.
        
            pmkToLeft: A reference to the moniker to the left of this moniker, if the moniker is part of a composite 
             moniker.
        
            riid: The interface identifier (IID) of the storage interface requested.
        """
        pass

    def CommonPrefixWith(self, pmkOther, ppmkPrefix):
        """
        CommonPrefixWith(self: UCOMIMoniker, pmkOther: UCOMIMoniker) -> UCOMIMoniker
        
            Creates a new moniker based on the common prefix that this moniker shares with another moniker.
        
            pmkOther: A reference to the IMoniker interface on another moniker to compare with this for a common 
             prefix.
        """
        pass

    def ComposeWith(self, pmkRight, fOnlyIfNotGeneric, ppmkComposite):
        """
        ComposeWith(self: UCOMIMoniker, pmkRight: UCOMIMoniker, fOnlyIfNotGeneric: bool) -> UCOMIMoniker
        
            Combines the current moniker with another moniker, creating a new composite moniker.
        
            pmkRight: A reference to the IMoniker interface on the moniker to compose onto the end of this moniker.
            fOnlyIfNotGeneric: If true, the caller requires a nongeneric composition, so the operation proceeds only if 
             pmkRight is a moniker class that this moniker can compose with in some way other than forming a 
             generic composite. If false, the method can create a generic composite if necessary.
        """
        pass

    def Enum(self, fForward, ppenumMoniker):
        """
        Enum(self: UCOMIMoniker, fForward: bool) -> UCOMIEnumMoniker
        
            Supplies a pointer to an enumerator that can enumerate the components of a composite moniker.
        
            fForward: If true, enumerates the monikers from left to right. If false, enumerates from right to left.
        """
        pass

    def GetClassID(self, pClassID):
        """
        GetClassID(self: UCOMIMoniker) -> Guid
        
            Retrieves the class identifier (CLSID) of an object.
        """
        pass

    def GetDisplayName(self, pbc, pmkToLeft, ppszDisplayName):
        """
        GetDisplayName(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker) -> str
        
            Gets the display name, which is a user-readable representation of this moniker.
        
            pbc: A reference to the bind context to use in this operation.
            pmkToLeft: A reference to the moniker to the left of this moniker, if the moniker is part of a composite 
             moniker.
        """
        pass

    def GetSizeMax(self, pcbSize):
        """
        GetSizeMax(self: UCOMIMoniker) -> Int64
        
            Returns the size in bytes of the stream needed to save the object.
        """
        pass

    def GetTimeOfLastChange(self, pbc, pmkToLeft, pFileTime):
        """
        GetTimeOfLastChange(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker) -> FILETIME
        
            Provides a number representing the time the object identified by this moniker was last changed.
        
            pbc: A reference to the bind context to be used in this binding operation.
            pmkToLeft: A reference to the moniker to the left of this moniker, if the moniker is part of a composite 
             moniker.
        """
        pass

    def Hash(self, pdwHash):
        """
        Hash(self: UCOMIMoniker) -> int
        
            Calculates a 32-bit integer using the internal state of the moniker.
        """
        pass

    def Inverse(self, ppmk):
        """
        Inverse(self: UCOMIMoniker) -> UCOMIMoniker
        
            Provides a moniker that, when composed to the right of this moniker or one of similar structure, 
             composes to nothing.
        """
        pass

    def IsDirty(self):
        """
        IsDirty(self: UCOMIMoniker) -> int
        
            Checks the object for changes since it was last saved.
            Returns: An S_OKHRESULT value if the object has changed; otherwise, an S_FALSEHRESULT value.
        """
        pass

    def IsEqual(self, pmkOtherMoniker):
        """
        IsEqual(self: UCOMIMoniker, pmkOtherMoniker: UCOMIMoniker)
            Compares this moniker with a specified moniker and indicates whether they are identical.
        
            pmkOtherMoniker: A reference to the moniker to be used for comparison.
        """
        pass

    def IsRunning(self, pbc, pmkToLeft, pmkNewlyRunning):
        """
        IsRunning(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, pmkNewlyRunning: UCOMIMoniker)
            Determines whether the object that is identified by this moniker is currently loaded and running.
        
            pbc: A reference to the bind context to be used in this binding operation.
            pmkToLeft: A reference to the moniker to the left of this moniker if this moniker is part of a composite.
            pmkNewlyRunning: A reference to the moniker most recently added to the Running Object Table.
        """
        pass

    def IsSystemMoniker(self, pdwMksys):
        """
        IsSystemMoniker(self: UCOMIMoniker) -> int
        
            Indicates whether this moniker is of one of the system-supplied moniker classes.
        """
        pass

    def Load(self, pStm):
        """
        Load(self: UCOMIMoniker, pStm: UCOMIStream)
            Initializes an object from the stream where it was previously saved.
        
            pStm: Stream from which the object is loaded.
        """
        pass

    def ParseDisplayName(self, pbc, pmkToLeft, pszDisplayName, pchEaten, ppmkOut):
        """
        ParseDisplayName(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, pszDisplayName: str) -> (int, UCOMIMoniker)
        
            Reads as many characters of the specified display name as it understands and builds a moniker 
             corresponding to the portion read.
        
        
            pbc: A reference to the bind context to be used in this binding operation.
            pmkToLeft: A reference to the moniker that has been built out of the display name up to this point.
            pszDisplayName: A reference to the string containing the remaining display name to parse.
        """
        pass

    def Reduce(self, pbc, dwReduceHowFar, ppmkToLeft, ppmkReduced):
        """
        Reduce(self: UCOMIMoniker, pbc: UCOMIBindCtx, dwReduceHowFar: int, ppmkToLeft: UCOMIMoniker) -> (UCOMIMoniker, UCOMIMoniker)
        
            Returns a reduced moniker which is another moniker that refers to the same object as this 
             moniker but can be bound with equal or greater efficiency.
        
        
            pbc: A reference to the IBindCtx interface on the bind context to be used in this binding operation.
            dwReduceHowFar: Specifies how far this moniker should be reduced.
            ppmkToLeft: A reference to the moniker to the left of this moniker.
        """
        pass

    def RelativePathTo(self, pmkOther, ppmkRelPath):
        """
        RelativePathTo(self: UCOMIMoniker, pmkOther: UCOMIMoniker) -> UCOMIMoniker
        
            Supplies a moniker that, when appended to this moniker (or one with a similar structure), yields 
             the specified moniker.
        
        
            pmkOther: A reference to the moniker to which a relative path should be taken.
        """
        pass

    def Save(self, pStm, fClearDirty):
        """
        Save(self: UCOMIMoniker, pStm: UCOMIStream, fClearDirty: bool)
            Saves an object to the specified stream.
        
            pStm: The stream into which the object is saved.
            fClearDirty: Indicates whether to clear the modified flag after the save is complete.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIPersistFile:
    """ Use System.Runtime.InteropServices.ComTypes.IPersistFile instead. """
    def GetClassID(self, pClassID):
        """
        GetClassID(self: UCOMIPersistFile) -> Guid
        
            Retrieves the class identifier (CLSID) of an object.
        """
        pass

    def GetCurFile(self, ppszFileName):
        """
        GetCurFile(self: UCOMIPersistFile) -> str
        
            Retrieves either the absolute path to current working file of the object, or if there is no 
             current working file, the default filename prompt of the object.
        """
        pass

    def IsDirty(self):
        """
        IsDirty(self: UCOMIPersistFile) -> int
        
            Checks an object for changes since it was last saved to its current file.
            Returns: S_OK if the file has changed since it was last saved; S_FALSE if the file has not changed since 
             it was last saved.
        """
        pass

    def Load(self, pszFileName, dwMode):
        """
        Load(self: UCOMIPersistFile, pszFileName: str, dwMode: int)
            Opens the specified file and initializes an object from the file contents.
        
            pszFileName: A zero-terminated string containing the absolute path of the file to open.
            dwMode: A combination of values from the STGM enumeration to indicate the access mode in which to open 
             pszFileName.
        """
        pass

    def Save(self, pszFileName, fRemember):
        """
        Save(self: UCOMIPersistFile, pszFileName: str, fRemember: bool)
            Saves a copy of the object into the specified file.
        
            pszFileName: A zero-terminated string containing the absolute path of the file to which the object is saved.
            fRemember: Indicates whether pszFileName is to be used as the current working file.
        """
        pass

    def SaveCompleted(self, pszFileName):
        """
        SaveCompleted(self: UCOMIPersistFile, pszFileName: str)
            Notifies the object that it can write to its file.
        
            pszFileName: The absolute path of the file where the object was previously saved.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIRunningObjectTable:
    """ Use System.Runtime.InteropServices.ComTypes.IRunningObjectTable instead. """
    def EnumRunning(self, ppenumMoniker):
        """
        EnumRunning(self: UCOMIRunningObjectTable) -> UCOMIEnumMoniker
        
            Enumerates the objects currently registered as running.
        """
        pass

    def GetObject(self, pmkObjectName, ppunkObject):
        """
        GetObject(self: UCOMIRunningObjectTable, pmkObjectName: UCOMIMoniker) -> object
        
            Returns the registered object if the supplied object name is registered as running.
        
            pmkObjectName: Reference to the moniker to search for in the ROT.
        """
        pass

    def GetTimeOfLastChange(self, pmkObjectName, pfiletime):
        """
        GetTimeOfLastChange(self: UCOMIRunningObjectTable, pmkObjectName: UCOMIMoniker) -> FILETIME
        
            Searches for this moniker in the ROT and reports the recorded time of change, if present.
        
            pmkObjectName: Reference to the moniker to search for in the ROT.
        """
        pass

    def IsRunning(self, pmkObjectName):
        """
        IsRunning(self: UCOMIRunningObjectTable, pmkObjectName: UCOMIMoniker)
            Determines if the specified moniker is currently registered in the Running Object Table.
        
            pmkObjectName: Reference to the moniker to search for in the Running Object Table.
        """
        pass

    def NoteChangeTime(self, dwRegister, pfiletime):
        """
        NoteChangeTime(self: UCOMIRunningObjectTable, dwRegister: int, pfiletime: FILETIME) -> FILETIME
        
            Makes a note of the time that a particular object has changed so IMoniker::GetTimeOfLastChange 
             can report an appropriate change time.
        
        
            dwRegister: The ROT entry of the changed object.
            pfiletime: Reference to the object's last change time.
        """
        pass

    def Register(self, grfFlags, punkObject, pmkObjectName, pdwRegister):
        """
        Register(self: UCOMIRunningObjectTable, grfFlags: int, punkObject: object, pmkObjectName: UCOMIMoniker) -> int
        
            Registers that the supplied object has entered the running state.
        
            grfFlags: Specifies whether the Running Object Table's (ROT) reference to punkObject is weak or strong, 
             and controls access to the object through its entry in the ROT.
        
            punkObject: Reference to the object being registered as running.
            pmkObjectName: Reference to the moniker that identifies punkObject.
        """
        pass

    def Revoke(self, dwRegister):
        """
        Revoke(self: UCOMIRunningObjectTable, dwRegister: int)
            Unregisters the specified object from the ROT.
        
            dwRegister: The ROT entry to revoke.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIStream:
    """ Use System.Runtime.InteropServices.ComTypes.IStream instead. """
    def Clone(self, ppstm):
        """
        Clone(self: UCOMIStream) -> UCOMIStream
        
            Creates a new stream object with its own seek pointer that references the same bytes as the 
             original stream.
        """
        pass

    def Commit(self, grfCommitFlags):
        """
        Commit(self: UCOMIStream, grfCommitFlags: int)
            Ensures that any changes made to a stream object open in transacted mode are reflected in the 
             parent storage.
        
        
            grfCommitFlags: Controls how the changes for the stream object are committed.
        """
        pass

    def CopyTo(self, pstm, cb, pcbRead, pcbWritten):
        """
        CopyTo(self: UCOMIStream, pstm: UCOMIStream, cb: Int64, pcbRead: IntPtr, pcbWritten: IntPtr)
            Copies a specified number of bytes from the current seek pointer in the stream to the current 
             seek pointer in another stream.
        
        
            pstm: Reference to the destination stream.
            cb: The number of bytes to copy from the source stream.
            pcbRead: On successful return, contains the actual number of bytes read from the source.
            pcbWritten: On successful return, contains the actual number of bytes written to the destination.
        """
        pass

    def LockRegion(self, libOffset, cb, dwLockType):
        """
        LockRegion(self: UCOMIStream, libOffset: Int64, cb: Int64, dwLockType: int)
            Restricts access to a specified range of bytes in the stream.
        
            libOffset: The byte offset for the beginning of the range.
            cb: The length of the range, in bytes, to restrict.
            dwLockType: The requested restrictions on accessing the range.
        """
        pass

    def Read(self, pv, cb, pcbRead):
        """
        Read(self: UCOMIStream, cb: int, pcbRead: IntPtr) -> Array[Byte]
        
            Reads a specified number of bytes from the stream object into memory starting at the current 
             seek pointer.
        
        
            cb: The number of bytes to read from the stream object.
            pcbRead: Pointer to a ULONG variable that receives the actual number of bytes read from the stream object.
        """
        pass

    def Revert(self):
        """
        Revert(self: UCOMIStream)
            Discards all changes that have been made to a transacted stream since the last 
             System.Runtime.InteropServices.UCOMIStream.Commit(System.Int32) call.
        """
        pass

    def Seek(self, dlibMove, dwOrigin, plibNewPosition):
        """
        Seek(self: UCOMIStream, dlibMove: Int64, dwOrigin: int, plibNewPosition: IntPtr)
            Changes the seek pointer to a new location relative to the beginning of the stream, to the end 
             of the stream, or to the current seek pointer.
        
        
            dlibMove: Displacement to add to dwOrigin.
            dwOrigin: Specifies the origin of the seek. The origin can be the beginning of the file, the current seek 
             pointer, or the end of the file.
        
            plibNewPosition: On successful return, contains the offset of the seek pointer from the beginning of the stream.
        """
        pass

    def SetSize(self, libNewSize):
        """
        SetSize(self: UCOMIStream, libNewSize: Int64)
            Changes the size of the stream object.
        
            libNewSize: Specifies the new size of the stream as a number of bytes.
        """
        pass

    def Stat(self, pstatstg, grfStatFlag):
        """
        Stat(self: UCOMIStream, grfStatFlag: int) -> STATSTG
        
            Retrieves the System.Runtime.InteropServices.STATSTG structure for this stream.
        
            grfStatFlag: Specifies some of the members in the STATSTG structure that this method does not return, thus 
             saving some memory allocation operations.
        """
        pass

    def UnlockRegion(self, libOffset, cb, dwLockType):
        """
        UnlockRegion(self: UCOMIStream, libOffset: Int64, cb: Int64, dwLockType: int)
            Removes the access restriction on a range of bytes previously restricted with 
             System.Runtime.InteropServices.UCOMIStream.LockRegion(System.Int64,System.Int64,System.Int32).
        
        
            libOffset: The byte offset for the beginning of the range.
            cb: The length, in bytes, of the range to restrict.
            dwLockType: The access restrictions previously placed on the range.
        """
        pass

    def Write(self, pv, cb, pcbWritten):
        """
        Write(self: UCOMIStream, pv: Array[Byte], cb: int, pcbWritten: IntPtr)
            Writes a specified number of bytes into the stream object starting at the current seek pointer.
        
            pv: Buffer to write this stream to.
            cb: The number of bytes to write into the stream.
            pcbWritten: On successful return, contains the actual number of bytes written to the stream object. The 
             caller can set this pointer to null, in which case this method does not provide the actual 
             number of bytes written.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMITypeComp:
    """ Use System.Runtime.InteropServices.ComTypes.ITypeComp instead. """
    def Bind(self, szName, lHashVal, wFlags, ppTInfo, pDescKind, pBindPtr):
        """
        Bind(self: UCOMITypeComp, szName: str, lHashVal: int, wFlags: Int16) -> (UCOMITypeInfo, DESCKIND, BINDPTR)
        
            Maps a name to a member of a type, or binds global variables and functions contained in a type 
             library.
        
        
            szName: The name to bind.
            lHashVal: A hash value for szName computed by LHashValOfNameSys.
            wFlags: A flags word containing one or more of the invoke flags defined in the INVOKEKIND enumeration.
        """
        pass

    def BindType(self, szName, lHashVal, ppTInfo, ppTComp):
        """
        BindType(self: UCOMITypeComp, szName: str, lHashVal: int) -> (UCOMITypeInfo, UCOMITypeComp)
        
            Binds to the type descriptions contained within a type library.
        
            szName: The name to bind.
            lHashVal: A hash value for szName determined by LHashValOfNameSys.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMITypeInfo:
    """ Use System.Runtime.InteropServices.ComTypes.ITypeInfo instead. """
    def AddressOfMember(self, memid, invKind, ppv):
        """
        AddressOfMember(self: UCOMITypeInfo, memid: int, invKind: INVOKEKIND) -> IntPtr
        
            Retrieves the addresses of static functions or variables, such as those defined in a DLL.
        
            memid: Member ID of the static member's address to retrieve.
            invKind: Specifies whether the member is a property, and if so, what kind.
        """
        pass

    def CreateInstance(self, pUnkOuter, riid, ppvObj):
        """
        CreateInstance(self: UCOMITypeInfo, pUnkOuter: object, riid: Guid) -> (Guid, object)
        
            Creates a new instance of a type that describes a component class (coclass).
        
            pUnkOuter: Object which acts as the controlling IUnknown.
            riid: The IID of the interface that the caller will use to communicate with the resulting object.
        """
        pass

    def GetContainingTypeLib(self, ppTLB, pIndex):
        """
        GetContainingTypeLib(self: UCOMITypeInfo) -> (UCOMITypeLib, int)
        
            Retrieves the type library that contains this type description and its index within that type 
             library.
        """
        pass

    def GetDllEntry(self, memid, invKind, pBstrDllName, pBstrName, pwOrdinal):
        """
        GetDllEntry(self: UCOMITypeInfo, memid: int, invKind: INVOKEKIND) -> (str, str, Int16)
        
            Retrieves a description or specification of an entry point for a function in a DLL.
        
            memid: ID of the member function whose DLL entry description is to be returned.
            invKind: Specifies the kind of member identified by memid.
        """
        pass

    def GetDocumentation(self, index, strName, strDocString, dwHelpContext, strHelpFile):
        """
        GetDocumentation(self: UCOMITypeInfo, index: int) -> (str, str, int, str)
        
            Retrieves the documentation string, the complete Help file name and path, and the context ID for 
             the Help topic for a specified type description.
        
        
            index: ID of the member whose documentation is to be returned.
        """
        pass

    def GetFuncDesc(self, index, ppFuncDesc):
        """
        GetFuncDesc(self: UCOMITypeInfo, index: int) -> IntPtr
        
            Retrieves the System.Runtime.InteropServices.FUNCDESC structure that contains information about 
             a specified function.
        
        
            index: Index of the function description to return.
        """
        pass

    def GetIDsOfNames(self, rgszNames, cNames, pMemId):
        """
        GetIDsOfNames(self: UCOMITypeInfo, rgszNames: Array[str], cNames: int) -> Array[int]
        
            Maps between member names and member IDs, and parameter names and parameter IDs.
        
            rgszNames: On succesful return, an array of names to map.
            cNames: Count of names to map.
        """
        pass

    def GetImplTypeFlags(self, index, pImplTypeFlags):
        """
        GetImplTypeFlags(self: UCOMITypeInfo, index: int) -> int
        
            Retrieves the System.Runtime.InteropServices.IMPLTYPEFLAGS value for one implemented interface 
             or base interface in a type description.
        
        
            index: Index of the implemented interface or base interface.
        """
        pass

    def GetMops(self, memid, pBstrMops):
        """
        GetMops(self: UCOMITypeInfo, memid: int) -> str
        
            Retrieves marshaling information.
        
            memid: The member ID that indicates which marshaling information is needed.
        """
        pass

    def GetNames(self, memid, rgBstrNames, cMaxNames, pcNames):
        """
        GetNames(self: UCOMITypeInfo, memid: int, cMaxNames: int) -> (Array[str], int)
        
            Retrieves the variable with the specified member ID (or the name of the property or method and 
             its parameters) that correspond to the specified function ID.
        
        
            memid: The ID of the member whose name (or names) is to be returned.
            cMaxNames: Length of the rgBstrNames array.
        """
        pass

    def GetRefTypeInfo(self, hRef, ppTI):
        """
        GetRefTypeInfo(self: UCOMITypeInfo, hRef: int) -> UCOMITypeInfo
        
            If a type description references other type descriptions, it retrieves the referenced type 
             descriptions.
        
        
            hRef: Handle to the referenced type description to return.
        """
        pass

    def GetRefTypeOfImplType(self, index, href):
        """
        GetRefTypeOfImplType(self: UCOMITypeInfo, index: int) -> int
        
            If a type description describes a COM class, it retrieves the type description of the 
             implemented interface types.
        
        
            index: Index of the implemented type whose handle is returned.
        """
        pass

    def GetTypeAttr(self, ppTypeAttr):
        """
        GetTypeAttr(self: UCOMITypeInfo) -> IntPtr
        
            Retrieves a System.Runtime.InteropServices.TYPEATTR structure that contains the attributes of 
             the type description.
        """
        pass

    def GetTypeComp(self, ppTComp):
        """
        GetTypeComp(self: UCOMITypeInfo) -> UCOMITypeComp
        
            Retrieves the ITypeComp interface for the type description, which enables a client compiler to 
             bind to the type description's members.
        """
        pass

    def GetVarDesc(self, index, ppVarDesc):
        """
        GetVarDesc(self: UCOMITypeInfo, index: int) -> IntPtr
        
            Retrieves a VARDESC structure that describes the specified variable.
        
            index: Index of the variable description to return.
        """
        pass

    def Invoke(self, pvInstance, memid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: UCOMITypeInfo, pvInstance: object, memid: int, wFlags: Int16, pDispParams: DISPPARAMS) -> (DISPPARAMS, object, EXCEPINFO, int)
        
            Invokes a method, or accesses a property of an object, that implements the interface described 
             by the type description.
        
        
            pvInstance: Reference to the interface described by this type description.
            memid: Identifies the interface member.
            wFlags: Flags describing the context of the invoke call.
            pDispParams: Reference to a structure that contains an array of arguments, an array of DISPIDs for named 
             arguments, and counts of the number of elements in each array.
        """
        pass

    def ReleaseFuncDesc(self, pFuncDesc):
        """
        ReleaseFuncDesc(self: UCOMITypeInfo, pFuncDesc: IntPtr)
            Releases a System.Runtime.InteropServices.FUNCDESC previously returned by 
             System.Runtime.InteropServices.UCOMITypeInfo.GetFuncDesc(System.Int32,System.IntPtr@).
        
        
            pFuncDesc: Reference to the FUNCDESC to release.
        """
        pass

    def ReleaseTypeAttr(self, pTypeAttr):
        """
        ReleaseTypeAttr(self: UCOMITypeInfo, pTypeAttr: IntPtr)
            Releases a System.Runtime.InteropServices.TYPEATTR previously returned by 
             System.Runtime.InteropServices.UCOMITypeInfo.GetTypeAttr(System.IntPtr@).
        
        
            pTypeAttr: Reference to the TYPEATTR to release.
        """
        pass

    def ReleaseVarDesc(self, pVarDesc):
        """
        ReleaseVarDesc(self: UCOMITypeInfo, pVarDesc: IntPtr)
            Releases a VARDESC previously returned by 
             System.Runtime.InteropServices.UCOMITypeInfo.GetVarDesc(System.Int32,System.IntPtr@).
        
        
            pVarDesc: Reference to the VARDESC to release.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMITypeLib:
    """ Use System.Runtime.InteropServices.ComTypes.ITypeLib instead. """
    def FindName(self, szNameBuf, lHashVal, ppTInfo, rgMemId, pcFound):
        """
        FindName(self: UCOMITypeLib, szNameBuf: str, lHashVal: int, pcFound: Int16) -> (Array[UCOMITypeInfo], Array[int], Int16)
        
            Finds occurrences of a type description in a type library.
        
            szNameBuf: The name to search for.
            lHashVal: A hash value to speed up the search, computed by the LHashValOfNameSys function. If lHashVal is 
             0, a value is computed.
        
            pcFound: On entry, indicates how many instances to look for. For example, pcFound = 1 can be called to 
             find the first occurrence. The search stops when one instance is found.On exit, indicates the 
             number of instances that were found. If the in and out values of pcFound are identical, there 
             might be more type descriptions that contain the name.
        """
        pass

    def GetDocumentation(self, index, strName, strDocString, dwHelpContext, strHelpFile):
        """
        GetDocumentation(self: UCOMITypeLib, index: int) -> (str, str, int, str)
        
            Retrieves the library's documentation string, the complete Help file name and path, and the 
             context identifier for the library Help topic in the Help file.
        
        
            index: Index of the type description whose documentation is to be returned.
        """
        pass

    def GetLibAttr(self, ppTLibAttr):
        """
        GetLibAttr(self: UCOMITypeLib) -> IntPtr
        
            Retrieves the structure that contains the library's attributes.
        """
        pass

    def GetTypeComp(self, ppTComp):
        """
        GetTypeComp(self: UCOMITypeLib) -> UCOMITypeComp
        
            Enables a client compiler to bind to a library's types, variables, constants, and global 
             functions.
        """
        pass

    def GetTypeInfo(self, index, ppTI):
        """
        GetTypeInfo(self: UCOMITypeLib, index: int) -> UCOMITypeInfo
        
            Retrieves the specified type description in the library.
        
            index: Index of the UCOMITypeInfo interface to return.
        """
        pass

    def GetTypeInfoCount(self):
        """
        GetTypeInfoCount(self: UCOMITypeLib) -> int
        
            Returns the number of type descriptions in the type library.
            Returns: The number of type descriptions in the type library.
        """
        pass

    def GetTypeInfoOfGuid(self, guid, ppTInfo):
        """
        GetTypeInfoOfGuid(self: UCOMITypeLib, guid: Guid) -> (Guid, UCOMITypeInfo)
        
            Retrieves the type description that corresponds to the specified GUID.
        
            guid: IID of the interface of CLSID of the class whose type info is requested.
        """
        pass

    def GetTypeInfoType(self, index, pTKind):
        """
        GetTypeInfoType(self: UCOMITypeLib, index: int) -> TYPEKIND
        
            Retrieves the type of a type description.
        
            index: The index of the type description within the type library.
        """
        pass

    def IsName(self, szNameBuf, lHashVal):
        """
        IsName(self: UCOMITypeLib, szNameBuf: str, lHashVal: int) -> bool
        
            Indicates whether a passed-in string contains the name of a type or member described in the 
             library.
        
        
            szNameBuf: The string to test.
            lHashVal: The hash value of szNameBuf.
            Returns: true if szNameBuf was found in the type library; otherwise false.
        """
        pass

    def ReleaseTLibAttr(self, pTLibAttr):
        """
        ReleaseTLibAttr(self: UCOMITypeLib, pTLibAttr: IntPtr)
            Releases the System.Runtime.InteropServices.TYPELIBATTR originally obtained from 
             System.Runtime.InteropServices.UCOMITypeLib.GetLibAttr(System.IntPtr@).
        
        
            pTLibAttr: The TLIBATTR to release.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UnknownWrapper(object):
    """
    Wraps objects the marshaler should marshal as a VT_UNKNOWN.
    
    UnknownWrapper(obj: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: object) """
        pass

    WrappedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object contained by this wrapper.

Get: WrappedObject(self: UnknownWrapper) -> object

"""



class UnmanagedFunctionPointerAttribute(Attribute, _Attribute):
    """
    Controls the marshaling behavior of a delegate signature passed as an unmanaged function pointer to or from unmanaged code. This class cannot be inherited.
    
    UnmanagedFunctionPointerAttribute(callingConvention: CallingConvention)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, callingConvention):
        """ __new__(cls: type, callingConvention: CallingConvention) """
        pass

    CallingConvention = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the calling convention.

Get: CallingConvention(self: UnmanagedFunctionPointerAttribute) -> CallingConvention

"""


    BestFitMapping = None
    CharSet = None
    SetLastError = None
    ThrowOnUnmappableChar = None


class UnmanagedType(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies how to marshal parameters or fields to unmanaged code.
    
    enum UnmanagedType, values: AnsiBStr (35), AsAny (40), Bool (2), BStr (19), ByValArray (30), ByValTStr (23), Currency (15), CustomMarshaler (44), Error (45), FunctionPtr (38), HString (47), I1 (3), I2 (5), I4 (7), I8 (9), IDispatch (26), IInspectable (46), Interface (28), IUnknown (25), LPArray (42), LPStr (20), LPStruct (43), LPTStr (22), LPUTF8Str (48), LPWStr (21), R4 (11), R8 (12), SafeArray (29), Struct (27), SysInt (31), SysUInt (32), TBStr (36), U1 (4), U2 (6), U4 (8), U8 (10), VariantBool (37), VBByRefStr (34)
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

    AnsiBStr = None
    AsAny = None
    Bool = None
    BStr = None
    ByValArray = None
    ByValTStr = None
    Currency = None
    CustomMarshaler = None
    Error = None
    FunctionPtr = None
    HString = None
    I1 = None
    I2 = None
    I4 = None
    I8 = None
    IDispatch = None
    IInspectable = None
    Interface = None
    IUnknown = None
    LPArray = None
    LPStr = None
    LPStruct = None
    LPTStr = None
    LPUTF8Str = None
    LPWStr = None
    R4 = None
    R8 = None
    SafeArray = None
    Struct = None
    SysInt = None
    SysUInt = None
    TBStr = None
    U1 = None
    U2 = None
    U4 = None
    U8 = None
    value__ = None
    VariantBool = None
    VBByRefStr = None


class VARDESC(object):
    """ Use System.Runtime.InteropServices.ComTypes.VARDESC instead. """
    DESCUNION = None
    elemdescVar = None
    lpstrSchema = None
    memid = None
    varkind = None
    wVarFlags = None


class VarEnum(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates how to marshal the array elements when an array is marshaled from managed to unmanaged code as a System.Runtime.InteropServices.UnmanagedType.SafeArray.
    
    enum VarEnum, values: VT_ARRAY (8192), VT_BLOB (65), VT_BLOB_OBJECT (70), VT_BOOL (11), VT_BSTR (8), VT_BYREF (16384), VT_CARRAY (28), VT_CF (71), VT_CLSID (72), VT_CY (6), VT_DATE (7), VT_DECIMAL (14), VT_DISPATCH (9), VT_EMPTY (0), VT_ERROR (10), VT_FILETIME (64), VT_HRESULT (25), VT_I1 (16), VT_I2 (2), VT_I4 (3), VT_I8 (20), VT_INT (22), VT_LPSTR (30), VT_LPWSTR (31), VT_NULL (1), VT_PTR (26), VT_R4 (4), VT_R8 (5), VT_RECORD (36), VT_SAFEARRAY (27), VT_STORAGE (67), VT_STORED_OBJECT (69), VT_STREAM (66), VT_STREAMED_OBJECT (68), VT_UI1 (17), VT_UI2 (18), VT_UI4 (19), VT_UI8 (21), VT_UINT (23), VT_UNKNOWN (13), VT_USERDEFINED (29), VT_VARIANT (12), VT_VECTOR (4096), VT_VOID (24)
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

    value__ = None
    VT_ARRAY = None
    VT_BLOB = None
    VT_BLOB_OBJECT = None
    VT_BOOL = None
    VT_BSTR = None
    VT_BYREF = None
    VT_CARRAY = None
    VT_CF = None
    VT_CLSID = None
    VT_CY = None
    VT_DATE = None
    VT_DECIMAL = None
    VT_DISPATCH = None
    VT_EMPTY = None
    VT_ERROR = None
    VT_FILETIME = None
    VT_HRESULT = None
    VT_I1 = None
    VT_I2 = None
    VT_I4 = None
    VT_I8 = None
    VT_INT = None
    VT_LPSTR = None
    VT_LPWSTR = None
    VT_NULL = None
    VT_PTR = None
    VT_R4 = None
    VT_R8 = None
    VT_RECORD = None
    VT_SAFEARRAY = None
    VT_STORAGE = None
    VT_STORED_OBJECT = None
    VT_STREAM = None
    VT_STREAMED_OBJECT = None
    VT_UI1 = None
    VT_UI2 = None
    VT_UI4 = None
    VT_UI8 = None
    VT_UINT = None
    VT_UNKNOWN = None
    VT_USERDEFINED = None
    VT_VARIANT = None
    VT_VECTOR = None
    VT_VOID = None


class VARFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """
    Use System.Runtime.InteropServices.ComTypes.VARFLAGS instead.
    
    enum (flags) VARFLAGS, values: VARFLAG_FBINDABLE (4), VARFLAG_FDEFAULTBIND (32), VARFLAG_FDEFAULTCOLLELEM (256), VARFLAG_FDISPLAYBIND (16), VARFLAG_FHIDDEN (64), VARFLAG_FIMMEDIATEBIND (4096), VARFLAG_FNONBROWSABLE (1024), VARFLAG_FREADONLY (1), VARFLAG_FREPLACEABLE (2048), VARFLAG_FREQUESTEDIT (8), VARFLAG_FRESTRICTED (128), VARFLAG_FSOURCE (2), VARFLAG_FUIDEFAULT (512)
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

    value__ = None
    VARFLAG_FBINDABLE = None
    VARFLAG_FDEFAULTBIND = None
    VARFLAG_FDEFAULTCOLLELEM = None
    VARFLAG_FDISPLAYBIND = None
    VARFLAG_FHIDDEN = None
    VARFLAG_FIMMEDIATEBIND = None
    VARFLAG_FNONBROWSABLE = None
    VARFLAG_FREADONLY = None
    VARFLAG_FREPLACEABLE = None
    VARFLAG_FREQUESTEDIT = None
    VARFLAG_FRESTRICTED = None
    VARFLAG_FSOURCE = None
    VARFLAG_FUIDEFAULT = None


class VariantWrapper(object):
    """
    Marshals data of type VT_VARIANT | VT_BYREF from managed to unmanaged code. This class cannot be inherited.
    
    VariantWrapper(obj: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: object) """
        pass

    WrappedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object wrapped by the System.Runtime.InteropServices.VariantWrapper object.

Get: WrappedObject(self: VariantWrapper) -> object

"""



class _Activator:
    """ Exposes the System.Activator class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _Activator, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _Activator, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _Activator) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _Activator, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier for the member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _Assembly:
    """ Exposes the public members of the System.Reflection.Assembly class to unmanaged code. """
    def CreateInstance(self, typeName, ignoreCase=None, bindingAttr=None, binder=None, args=None, culture=None, activationAttributes=None):
        """
        CreateInstance(self: _Assembly, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.CreateInstance(System.String,System.Boolean,System.Reflection.BindingF
             lags,System.Reflection.Binder,System.Object[],System.Globalization.CultureInfo,System.Object[]) 
             method.
        
        
            typeName: The System.Type.FullName of the type to locate.
            ignoreCase: true to ignore the case of the type name; otherwise, false.
            bindingAttr: A bitmask that affects how the search is conducted. The value is a combination of bit flags from 
             System.Reflection.BindingFlags.
        
            binder: An object that enables the binding, coercion of argument types, invocation of members, and 
             retrieval of MemberInfo objects via reflection. If binder is null, the default binder is used.
        
            args: An array of type Object containing the arguments to be passed to the constructor. This array of 
             arguments must match in number, order, and type the parameters of the constructor to be invoked. 
             If the default constructor is desired, args must be an empty array or null.
        
            culture: An instance of CultureInfo used to govern the coercion of types. If this is null, the 
             CultureInfo for the current thread is used. (This is necessary to convert a String that 
             represents 1000 to a Double value, for example, since 1000 is represented differently by 
             different cultures.)
        
            activationAttributes: An array of type Object containing one or more activation attributes that can participate in the 
             activation. An example of an activation attribute is: 
             URLAttribute(http://hostname/appname/objectURI)
        
            Returns: An instance of Object representing the type and matching the specified criteria, or null if 
             typeName is not found.
        
        CreateInstance(self: _Assembly, typeName: str, ignoreCase: bool) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.CreateInstance(System.String,System.Boolean) method.
        
        
            typeName: The System.Type.FullName of the type to locate.
            ignoreCase: true to ignore the case of the type name; otherwise, false.
            Returns: An instance of System.Object representing the type, with culture, arguments, binder, and 
             activation attributes set to null, and System.Reflection.BindingFlags set to Public or Instance, 
             or null if typeName is not found.
        
        CreateInstance(self: _Assembly, typeName: str) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.CreateInstance(System.String) method.
        
        
            typeName: The System.Type.FullName of the type to locate.
            Returns: An instance of System.Object representing the type, with culture, arguments, binder, and 
             activation attributes set to null, and System.Reflection.BindingFlags set to Public or Instance, 
             or null if typeName is not found.
        """
        pass

    def Equals(self, other):
        """
        Equals(self: _Assembly, other: object) -> bool
        
            Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 
             method.
        
        
            other: The System.Object to compare with the current System.Object.
            Returns: true if the specified System.Object is equal to the current System.Object; otherwise, false.
        """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _Assembly, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetCustomAttributes(System.Boolean) method.
        
        
            inherit: This argument is ignored for objects of type System.Reflection.Assembly.
            Returns: An array of type Object containing the custom attributes for this assembly.
        GetCustomAttributes(self: _Assembly, attributeType: Type, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetCustomAttributes(System.Type,System.Boolean) method.
        
        
            attributeType: The System.Type for which the custom attributes are to be returned.
            inherit: This argument is ignored for objects of type System.Reflection.Assembly.
            Returns: An array of type System.Object containing the custom attributes for this assembly as specified 
             by attributeType.
        """
        pass

    def GetExportedTypes(self):
        """
        GetExportedTypes(self: _Assembly) -> Array[Type]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetExportedTypes property.
        
            Returns: An array of System.Type objects that represent the types defined in this assembly that are 
             visible outside the assembly.
        """
        pass

    def GetFile(self, name):
        """
        GetFile(self: _Assembly, name: str) -> FileStream
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetFile(System.String) method.
        
        
            name: The name of the specified file. Do not include the path to the file.
            Returns: A System.IO.FileStream for the specified file, or null if the file is not found.
        """
        pass

    def GetFiles(self, getResourceModules=None):
        """
        GetFiles(self: _Assembly, getResourceModules: bool) -> Array[FileStream]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetFiles(System.Boolean) method.
        
        
            getResourceModules: true to include resource modules; otherwise, false.
            Returns: An array of System.IO.FileStream objects.
        GetFiles(self: _Assembly) -> Array[FileStream]
        
            Provides COM objects with version-independent access to the System.Reflection.Assembly.GetFiles 
             method.
        
            Returns: An array of System.IO.FileStream objects.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: _Assembly) -> int
        
            Provides COM objects with version-independent access to the System.Object.GetHashCode method.
            Returns: A hash code for the current System.Object.
        """
        pass

    def GetLoadedModules(self, getResourceModules=None):
        """
        GetLoadedModules(self: _Assembly, getResourceModules: bool) -> Array[Module]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetLoadedModules(System.Boolean) method.
        
        
            getResourceModules: true to include resource modules; otherwise, false.
            Returns: An array of modules.
        GetLoadedModules(self: _Assembly) -> Array[Module]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetLoadedModules method.
        
            Returns: An array of modules.
        """
        pass

    def GetManifestResourceInfo(self, resourceName):
        """
        GetManifestResourceInfo(self: _Assembly, resourceName: str) -> ManifestResourceInfo
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetManifestResourceInfo(System.String) method.
        
        
            resourceName: The case-sensitive name of the resource.
            Returns: A System.Reflection.ManifestResourceInfo object populated with information about the resource's 
             topology, or null if the resource is not found.
        """
        pass

    def GetManifestResourceNames(self):
        """
        GetManifestResourceNames(self: _Assembly) -> Array[str]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetManifestResourceNames method.
        
            Returns: An array of type String containing the names of all the resources.
        """
        pass

    def GetManifestResourceStream(self, *__args):
        """
        GetManifestResourceStream(self: _Assembly, name: str) -> Stream
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetManifestResourceStream(System.String) method.
        
        
            name: The case-sensitive name of the manifest resource being requested.
            Returns: A System.IO.Stream representing this manifest resource.
        GetManifestResourceStream(self: _Assembly, type: Type, name: str) -> Stream
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetManifestResourceStream(System.Type,System.String) method.
        
        
            type: The type whose namespace is used to scope the manifest resource name.
            name: The case-sensitive name of the manifest resource being requested.
            Returns: A System.IO.Stream representing this manifest resource.
        """
        pass

    def GetModule(self, name):
        """
        GetModule(self: _Assembly, name: str) -> Module
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetModule(System.String) method.
        
        
            name: The name of the module being requested.
            Returns: The module being requested, or null if the module is not found.
        """
        pass

    def GetModules(self, getResourceModules=None):
        """
        GetModules(self: _Assembly, getResourceModules: bool) -> Array[Module]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetModules(System.Boolean) method.
        
        
            getResourceModules: true to include resource modules; otherwise, false.
            Returns: An array of modules.
        GetModules(self: _Assembly) -> Array[Module]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetModules method.
        
            Returns: An array of modules.
        """
        pass

    def GetName(self, copiedName=None):
        """
        GetName(self: _Assembly, copiedName: bool) -> AssemblyName
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetName(System.Boolean) method.
        
        
            copiedName: true to set the System.Reflection.Assembly.CodeBase to the location of the assembly after it was 
             shadow copied; false to set System.Reflection.Assembly.CodeBase to the original location.
        
            Returns: An System.Reflection.AssemblyName for this assembly.
        GetName(self: _Assembly) -> AssemblyName
        
            Provides COM objects with version-independent access to the System.Reflection.Assembly.GetName 
             method.
        
            Returns: An System.Reflection.AssemblyName for this assembly.
        """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: _Assembly, info: SerializationInfo, context: StreamingContext)
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetObjectData(System.Runtime.Serialization.SerializationInfo,System.Ru
             ntime.Serialization.StreamingContext) method.
        
        
            info: The object to be populated with serialization information.
            context: The destination context of the serialization.
        """
        pass

    def GetReferencedAssemblies(self):
        """
        GetReferencedAssemblies(self: _Assembly) -> Array[AssemblyName]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetReferencedAssemblies method.
        
            Returns: An array of type System.Reflection.AssemblyName containing all the assemblies referenced by this 
             assembly.
        """
        pass

    def GetSatelliteAssembly(self, culture, version=None):
        """
        GetSatelliteAssembly(self: _Assembly, culture: CultureInfo, version: Version) -> Assembly
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetSatelliteAssembly(System.Globalization.CultureInfo,System.Version) 
             method.
        
        
            culture: The specified culture.
            version: The version of the satellite assembly.
            Returns: The specified satellite assembly.
        GetSatelliteAssembly(self: _Assembly, culture: CultureInfo) -> Assembly
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetSatelliteAssembly(System.Globalization.CultureInfo) method.
        
        
            culture: The specified culture.
            Returns: The specified satellite assembly.
        """
        pass

    def GetType(self, name=None, throwOnError=None, ignoreCase=None):
        """
        GetType(self: _Assembly, name: str, throwOnError: bool) -> Type
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetType(System.String,System.Boolean) method.
        
        
            name: The full name of the type.
            throwOnError: true to throw an exception if the type is not found; false to return null.
            Returns: A System.Type object that represents the specified class.
        GetType(self: _Assembly, name: str, throwOnError: bool, ignoreCase: bool) -> Type
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetType(System.String,System.Boolean,System.Boolean) method.
        
        
            name: The full name of the type.
            throwOnError: true to throw an exception if the type is not found; false to return null.
            ignoreCase: true to ignore the case of the type name; otherwise, false.
            Returns: A System.Type object that represents the specified class.
        GetType(self: _Assembly) -> Type
        
            Provides COM objects with version-independent access to the System.Object.GetType method.
            Returns: A System.Type object.
        GetType(self: _Assembly, name: str) -> Type
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetType(System.String) method.
        
        
            name: The full name of the type.
            Returns: A System.Type object that represents the specified class, or null if the class is not found.
        """
        pass

    def GetTypes(self):
        """
        GetTypes(self: _Assembly) -> Array[Type]
        
            Provides COM objects with version-independent access to the System.Reflection.Assembly.GetTypes 
             method.
        
            Returns: An array of type System.Type containing objects for all the types defined in this assembly.
        """
        pass

    def IsDefined(self, attributeType, inherit):
        """
        IsDefined(self: _Assembly, attributeType: Type, inherit: bool) -> bool
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.IsDefined(System.Type,System.Boolean) method.
        
        
            attributeType: The System.Type of the custom attribute to be checked for this assembly.
            inherit: This argument is ignored for objects of this type.
            Returns: true if a custom attribute identified by the specified System.Type is defined; otherwise, false.
        """
        pass

    def LoadModule(self, moduleName, rawModule, rawSymbolStore=None):
        """
        LoadModule(self: _Assembly, moduleName: str, rawModule: Array[Byte], rawSymbolStore: Array[Byte]) -> Module
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.LoadModule(System.String,System.Byte[],System.Byte[]) method.
        
        
            moduleName: Name of the module. Must correspond to a file name in this assembly's manifest.
            rawModule: A byte array that is a COFF-based image containing an emitted module, or a resource.
            rawSymbolStore: A byte array containing the raw bytes representing the symbols for the module. Must be null if 
             this is a resource file.
        
            Returns: The loaded module.
        LoadModule(self: _Assembly, moduleName: str, rawModule: Array[Byte]) -> Module
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.LoadModule(System.String,System.Byte[]) method.
        
        
            moduleName: Name of the module. Must correspond to a file name in this assembly's manifest.
            rawModule: A byte array that is a COFF-based image containing an emitted module, or a resource.
            Returns: The loaded Module.
        """
        pass

    def ToString(self):
        """
        ToString(self: _Assembly) -> str
        
            Provides COM objects with version-independent access to the System.Reflection.Assembly.ToString 
             method.
        
            Returns: The full name of the assembly, or the class name if the full name of the assembly cannot be 
             determined.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CodeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.Assembly.CodeBase property.

Get: CodeBase(self: _Assembly) -> str

"""

    EntryPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.Assembly.EntryPoint property.

Get: EntryPoint(self: _Assembly) -> MethodInfo

"""

    EscapedCodeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.Assembly.EscapedCodeBase property.

Get: EscapedCodeBase(self: _Assembly) -> str

"""

    Evidence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.Assembly.Evidence property.

Get: Evidence(self: _Assembly) -> Evidence

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.Assembly.FullName property.

Get: FullName(self: _Assembly) -> str

"""

    GlobalAssemblyCache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.Assembly.GlobalAssemblyCache property.

Get: GlobalAssemblyCache(self: _Assembly) -> bool

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.Assembly.Location property.

Get: Location(self: _Assembly) -> str

"""


    ModuleResolve = None


class _AssemblyBuilder:
    """ Exposes the System.Reflection.Emit.AssemblyBuilder class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _AssemblyBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _AssemblyBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _AssemblyBuilder) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _AssemblyBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _AssemblyName:
    """ Exposes the System.Reflection.AssemblyName class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _AssemblyName, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _AssemblyName, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _AssemblyName) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _AssemblyName, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _ConstructorBuilder:
    """ Exposes the System.Reflection.Emit.ConstructorBuilder class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _ConstructorBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _ConstructorBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _ConstructorBuilder) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _ConstructorBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _ConstructorInfo:
    """ Exposes the public members of the System.Reflection.ConstructorInfo class to unmanaged code. """
    def Equals(self, other):
        """
        Equals(self: _ConstructorInfo, other: object) -> bool
        
            Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 
             method.
        
        
            other: The System.Object to compare with the current System.Object.
            Returns: true if the specified System.Object is equal to the current System.Object; otherwise, false.
        """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _ConstructorInfo, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.GetCustomAttributes(System.Boolean) method.
        
        
            inherit: Specifies whether to search this member's inheritance chain to find the attributes.
            Returns: An array that contains all the custom attributes, or an array with zero elements if no 
             attributes are defined.
        
        GetCustomAttributes(self: _ConstructorInfo, attributeType: Type, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Emit.MethodBuilder.GetCustomAttributes(System.Type,System.Boolean) method.
        
        
            attributeType: The type of attribute to search for. Only attributes that are assignable to this type are 
             returned.
        
            inherit: Specifies whether to search this member's inheritance chain to find the attributes.
            Returns: An array of custom attributes applied to this member, or an array with zero (0) elements if no 
             attributes have been applied.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: _ConstructorInfo) -> int
        
            Provides COM objects with version-independent access to the System.Object.GetHashCode method.
            Returns: The hash code for the current instance.
        """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _ConstructorInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: Passed-in array of names to be mapped.
            cNames: Count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: Caller-allocated array that receives the IDs corresponding to the names.
        """
        pass

    def GetMethodImplementationFlags(self):
        """
        GetMethodImplementationFlags(self: _ConstructorInfo) -> MethodImplAttributes
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MethodBase.GetMethodImplementationFlags member.
        
            Returns: The System.Reflection.MethodImplAttributes flags.
        """
        pass

    def GetParameters(self):
        """
        GetParameters(self: _ConstructorInfo) -> Array[ParameterInfo]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MethodBase.GetParameters method.
        
            Returns: An array of type System.Reflection.ParameterInfo containing information that matches the 
             signature of the method (or constructor) reflected by this instance.
        """
        pass

    def GetType(self):
        """
        GetType(self: _ConstructorInfo) -> Type
        
            Provides COM objects with version-independent access to the System.Object.GetType method.
            Returns: A System.Type object.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _ConstructorInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can then be used to get the type information 
             for an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: Receives a pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _ConstructorInfo) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _ConstructorInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: Identifies the member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: Pointer to a structure containing an array of arguments, an array of argument DISPIDs for named 
             arguments, and counts for the number of elements in the arrays.
        
            pVarResult: Pointer to the location where the result is to be stored.
            pExcepInfo: Pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def Invoke_2(self, obj, invokeAttr, binder, parameters, culture):
        """
        Invoke_2(self: _ConstructorInfo, obj: object, invokeAttr: BindingFlags, binder: Binder, parameters: Array[object], culture: CultureInfo) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MethodBase.Invoke(System.Object,System.Reflection.BindingFlags,System.Reflectio
             n.Binder,System.Object[],System.Globalization.CultureInfo) method.
        
        
            obj: The instance that created this method.
            invokeAttr: One of the BindingFlags values that specifies the type of binding.
            binder: A Binder that defines a set of properties and enables the binding, coercion of argument types, 
             and invocation of members using reflection. If binder is null, then Binder.DefaultBinding is 
             used.
        
            parameters: An array of type Object used to match the number, order, and type of the parameters for this 
             constructor, under the constraints of binder. If this constructor does not require parameters, 
             pass an array with zero elements, as in Object[] parameters = new Object[0]. Any object in this 
             array that is not explicitly initialized with a value will contain the default value for that 
             object type. For reference-type elements, this value is null. For value-type elements, this 
             value is 0, 0.0, or false, depending on the specific element type.
        
            culture: A System.Globalization.CultureInfo used to govern the coercion of types. If this is null, the 
             System.Globalization.CultureInfo for the current thread is used.
        
            Returns: An instance of the class associated with the constructor.
        """
        pass

    def Invoke_3(self, obj, parameters):
        """
        Invoke_3(self: _ConstructorInfo, obj: object, parameters: Array[object]) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MethodBase.Invoke(System.Object,System.Object[]) method.
        
        
            obj: The instance that created this method.
            parameters: An argument list for the invoked method or constructor. This is an array of objects with the 
             same number, order, and type as the parameters of the method or constructor to be invoked. If 
             there are no parameters, parameters should be null.If the method or constructor represented by 
             this instance takes a ref parameter (ByRef in Visual Basic), no special attribute is required 
             for that parameter in order to invoke the method or constructor using this function. Any object 
             in this array that is not explicitly initialized with a value will contain the default value for 
             that object type. For reference-type elements, this value is null. For value-type elements, this 
             value is 0, 0.0, or false, depending on the specific element type.
        
            Returns: An instance of the class associated with the constructor.
        """
        pass

    def Invoke_4(self, invokeAttr, binder, parameters, culture):
        """
        Invoke_4(self: _ConstructorInfo, invokeAttr: BindingFlags, binder: Binder, parameters: Array[object], culture: CultureInfo) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.ConstructorInfo.Invoke(System.Reflection.BindingFlags,System.Reflection.Binder,
             System.Object[],System.Globalization.CultureInfo) method.
        
        
            invokeAttr: One of the BindingFlags values that specifies the type of binding.
            binder: A Binder that defines a set of properties and enables the binding, coercion of argument types, 
             and invocation of members using reflection. If binder is null, then Binder.DefaultBinding is 
             used.
        
            parameters: An array of type Object used to match the number, order, and type of the parameters for this 
             constructor, under the constraints of binder. If this constructor does not require parameters, 
             pass an array with zero elements, as in Object[] parameters = new Object[0]. Any object in this 
             array that is not explicitly initialized with a value will contain the default value for that 
             object type. For reference-type elements, this value is null. For value-type elements, this 
             value is 0, 0.0, or false, depending on the specific element type.
        
            culture: A System.Globalization.CultureInfo used to govern the coercion of types. If this is null, the 
             System.Globalization.CultureInfo for the current thread is used.
        
            Returns: An instance of the class associated with the constructor.
        """
        pass

    def Invoke_5(self, parameters):
        """
        Invoke_5(self: _ConstructorInfo, parameters: Array[object]) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.ConstructorInfo.Invoke(System.Object[]) method.
        
        
            parameters: An array of values that matches the number, order, and type (under the constraints of the 
             default binder) of the parameters for this constructor. If this constructor takes no parameters, 
             then use either an array with zero elements or null, as in Object[] parameters = new Object[0]. 
             Any object in this array that is not explicitly initialized with a value will contain the 
             default value for that object type. For reference-type elements, this value is null. For 
             value-type elements, this value is 0, 0.0, or false, depending on the specific element type.
        
            Returns: An instance of the class associated with the constructor.
        """
        pass

    def IsDefined(self, attributeType, inherit):
        """
        IsDefined(self: _ConstructorInfo, attributeType: Type, inherit: bool) -> bool
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.IsDefined(System.Type,System.Boolean) member.
        
        
            attributeType: The Type object to which the custom attributes are applied.
            inherit: Specifies whether to search this member's inheritance chain to find the attributes.
            Returns: true if one or more instances of attributeType is applied to this member; otherwise false.
        """
        pass

    def ToString(self):
        """
        ToString(self: _ConstructorInfo) -> str
        
            Provides COM objects with version-independent access to the System.Object.ToString method.
            Returns: A string that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.Attributes property.

Get: Attributes(self: _ConstructorInfo) -> MethodAttributes

"""

    CallingConvention = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.CallingConvention property.

Get: CallingConvention(self: _ConstructorInfo) -> CallingConventions

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.DeclaringType property.

Get: DeclaringType(self: _ConstructorInfo) -> Type

"""

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsAbstract property.

Get: IsAbstract(self: _ConstructorInfo) -> bool

"""

    IsAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsAssembly property.

Get: IsAssembly(self: _ConstructorInfo) -> bool

"""

    IsConstructor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsConstructor property.

Get: IsConstructor(self: _ConstructorInfo) -> bool

"""

    IsFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFamily property.

Get: IsFamily(self: _ConstructorInfo) -> bool

"""

    IsFamilyAndAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFamilyAndAssembly property.

Get: IsFamilyAndAssembly(self: _ConstructorInfo) -> bool

"""

    IsFamilyOrAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFamilyOrAssembly property.

Get: IsFamilyOrAssembly(self: _ConstructorInfo) -> bool

"""

    IsFinal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFinal property.

Get: IsFinal(self: _ConstructorInfo) -> bool

"""

    IsHideBySig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsHideBySig property.

Get: IsHideBySig(self: _ConstructorInfo) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsPrivate property.

Get: IsPrivate(self: _ConstructorInfo) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsPublic property.

Get: IsPublic(self: _ConstructorInfo) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsSpecialName property.

Get: IsSpecialName(self: _ConstructorInfo) -> bool

"""

    IsStatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsStatic property.

Get: IsStatic(self: _ConstructorInfo) -> bool

"""

    IsVirtual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsVirtual property.

Get: IsVirtual(self: _ConstructorInfo) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.ConstructorInfo.MemberType property.

Get: MemberType(self: _ConstructorInfo) -> MemberTypes

"""

    MethodHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.MethodHandle property.

Get: MethodHandle(self: _ConstructorInfo) -> RuntimeMethodHandle

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.Name property.

Get: Name(self: _ConstructorInfo) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.ReflectedType property.

Get: ReflectedType(self: _ConstructorInfo) -> Type

"""



class _CustomAttributeBuilder:
    """ Exposes the System.Reflection.Emit.CustomAttributeBuilder class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _CustomAttributeBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _CustomAttributeBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _CustomAttributeBuilder) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _CustomAttributeBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _EnumBuilder:
    """ Exposes the System.Reflection.Emit.EnumBuilder class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _EnumBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An  array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _EnumBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _EnumBuilder) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _EnumBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _EventBuilder:
    """ Exposes the System.Reflection.Emit.EventBuilder class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _EventBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _EventBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _EventBuilder) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _EventBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _EventInfo:
    """ Exposes the public members of the System.Reflection.EventInfo class to unmanaged code. """
    def AddEventHandler(self, target, handler):
        """
        AddEventHandler(self: _EventInfo, target: object, handler: Delegate)
            Provides COM objects with version-independent access to the 
             System.Reflection.EventInfo.AddEventHandler(System.Object,System.Delegate) method.
        
        
            target: The event source.
            handler: A method or methods to be invoked when the event is raised by the target.
        """
        pass

    def Equals(self, other):
        """
        Equals(self: _EventInfo, other: object) -> bool
        
            Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 
             method.
        
        
            other: The System.Object to compare with the current System.Object.
            Returns: true if the specified System.Object is equal to the current System.Object; otherwise, false.
        """
        pass

    def GetAddMethod(self, nonPublic=None):
        """
        GetAddMethod(self: _EventInfo) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Reflection.EventInfo.GetAddMethod method.
        
            Returns: A System.Reflection.MethodInfo object representing the method used to add an event-handler 
             delegate to the event source.
        
        GetAddMethod(self: _EventInfo, nonPublic: bool) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Reflection.EventInfo.GetAddMethod(System.Boolean) method.
        
        
            nonPublic: true to return non-public methods; otherwise, false.
            Returns: A System.Reflection.MethodInfo object representing the method used to add an event-handler 
             delegate to the event source.
        """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _EventInfo, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.GetCustomAttributes(System.Boolean) method.
        
        
            inherit: true to search a member's inheritance chain to find the attributes; otherwise, false.
            Returns: An array that contains all the custom attributes, or an array with zero (0) elements if no 
             attributes are defined.
        
        GetCustomAttributes(self: _EventInfo, attributeType: Type, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.GetCustomAttributes(System.Type,System.Boolean) method.
        
        
            attributeType: The type of attribute to search for. Only attributes that are assignable to this type are 
             returned.
        
            inherit: true to search this member's inheritance chain to find the attributes; otherwise, false.
            Returns: An array of custom attributes applied to this member, or an array with zero (0) elements if no 
             attributes have been applied.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: _EventInfo) -> int
        
            Provides COM objects with version-independent access to the System.Object.GetHashCode method.
            Returns: The hash code for the current instance.
        """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _EventInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetRaiseMethod(self, nonPublic=None):
        """
        GetRaiseMethod(self: _EventInfo) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Reflection.EventInfo.GetRaiseMethod method.
        
            Returns: The method that is called when the event is raised.
        GetRaiseMethod(self: _EventInfo, nonPublic: bool) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Reflection.EventInfo.GetRaiseMethod(System.Boolean) method.
        
        
            nonPublic: true to return non-public methods; otherwise, false.
            Returns: The System.Reflection.MethodInfo object that was called when the event was raised.
        """
        pass

    def GetRemoveMethod(self, nonPublic=None):
        """
        GetRemoveMethod(self: _EventInfo) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Reflection.EventInfo.GetRemoveMethod method.
        
            Returns: A System.Reflection.MethodInfo object representing the method used to remove an event-handler 
             delegate from the event source.
        
        GetRemoveMethod(self: _EventInfo, nonPublic: bool) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Reflection.EventInfo.GetRemoveMethod(System.Boolean) method.
        
        
            nonPublic: true to return non-public methods; otherwise, false.
            Returns: A System.Reflection.MethodInfo object representing the method used to remove an event-handler 
             delegate from the event source.
        """
        pass

    def GetType(self):
        """
        GetType(self: _EventInfo) -> Type
        
            Provides COM objects with version-independent access to the System.Object.GetType method.
            Returns: A System.Type object.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _EventInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _EventInfo) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _EventInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier for the member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def IsDefined(self, attributeType, inherit):
        """
        IsDefined(self: _EventInfo, attributeType: Type, inherit: bool) -> bool
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.IsDefined(System.Type,System.Boolean) method.
        
        
            attributeType: The Type object to which the custom attributes are applied.
            inherit: true to search this member's inheritance chain to find the attributes; otherwise, false.
            Returns: true if one or more instance of the attributeType parameter is applied to this member; 
             otherwise, false.
        """
        pass

    def RemoveEventHandler(self, target, handler):
        """
        RemoveEventHandler(self: _EventInfo, target: object, handler: Delegate)
            Provides COM objects with version-independent access to the 
             System.Reflection.EventInfo.RemoveEventHandler(System.Object,System.Delegate) method.
        
        
            target: The event source.
            handler: The delegate to be disassociated from the events raised by target.
        """
        pass

    def ToString(self):
        """
        ToString(self: _EventInfo) -> str
        
            Provides COM objects with version-independent access to the System.Object.ToString method.
            Returns: A string that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.EventInfo.Attributes property.

Get: Attributes(self: _EventInfo) -> EventAttributes

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.DeclaringType property.

Get: DeclaringType(self: _EventInfo) -> Type

"""

    EventHandlerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.EventInfo.EventHandlerType property.

Get: EventHandlerType(self: _EventInfo) -> Type

"""

    IsMulticast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.EventInfo.IsMulticast property.

Get: IsMulticast(self: _EventInfo) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.EventInfo.IsSpecialName property.

Get: IsSpecialName(self: _EventInfo) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.EventInfo.MemberType property.

Get: MemberType(self: _EventInfo) -> MemberTypes

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.Name property.

Get: Name(self: _EventInfo) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.ReflectedType property.

Get: ReflectedType(self: _EventInfo) -> Type

"""



class _Exception:
    """ Exposes the public members of the System.Exception class to unmanaged code. """
    def Equals(self, obj):
        """
        Equals(self: _Exception, obj: object) -> bool
        
            Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 
             method.
        
        
            obj: The System.Object to compare with the current System.Object.
            Returns: true if the specified System.Object is equal to the current System.Object; otherwise, false.
        """
        pass

    def GetBaseException(self):
        """
        GetBaseException(self: _Exception) -> Exception
        
            Provides COM objects with version-independent access to the System.Exception.GetBaseException 
             method.
        
            Returns: The first exception thrown in a chain of exceptions. If the System.Exception.InnerException 
             property of the current exception is a null reference (Nothing in Visual Basic), this property 
             returns the current exception.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: _Exception) -> int
        
            Provides COM objects with version-independent access to the System.Object.GetHashCode method.
            Returns: The hash code for the current instance.
        """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: _Exception, info: SerializationInfo, context: StreamingContext)
            Provides COM objects with version-independent access to the 
             System.Exception.GetObjectData(System.Runtime.Serialization.SerializationInfo,System.Runtime.Seri
             alization.StreamingContext) method
        
        
            info: The System.Runtime.Serialization.SerializationInfo object that holds the serialized object data 
             about the exception being thrown.
        
            context: The System.Runtime.Serialization.StreamingContext structure that contains contextual information 
             about the source or destination.
        """
        pass

    def GetType(self):
        """
        GetType(self: _Exception) -> Type
        
            Provides COM objects with version-independent access to the System.Exception.GetType method.
            Returns: A System.Type object that represents the exact runtime type of the current instance.
        """
        pass

    def ToString(self):
        """
        ToString(self: _Exception) -> str
        
            Provides COM objects with version-independent access to the System.Exception.ToString method.
            Returns: A string that represents the current System.Exception object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HelpLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Exception.HelpLink property.

Get: HelpLink(self: _Exception) -> str

Set: HelpLink(self: _Exception) = value
"""

    InnerException = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Exception.InnerException property.

Get: InnerException(self: _Exception) -> Exception

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Exception.Message property.

Get: Message(self: _Exception) -> str

"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Exception.Source property.

Get: Source(self: _Exception) -> str

Set: Source(self: _Exception) = value
"""

    StackTrace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Exception.StackTrace property.

Get: StackTrace(self: _Exception) -> str

"""

    TargetSite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Exception.TargetSite property.

Get: TargetSite(self: _Exception) -> MethodBase

"""



class _FieldBuilder:
    """ Exposes the System.Reflection.Emit.FieldBuilder class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _FieldBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _FieldBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _FieldBuilder) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _FieldBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _FieldInfo:
    """ Exposes the public members of the System.Reflection.FieldInfo class to unmanaged code. """
    def Equals(self, other):
        """
        Equals(self: _FieldInfo, other: object) -> bool
        
            Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 
             method.
        
        
            other: The System.Object to compare with the current System.Object.
            Returns: true if the specified System.Object is equal to the current System.Object; otherwise, false.
        """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _FieldInfo, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.GetCustomAttributes(System.Boolean) method.
        
        
            inherit: Specifies whether to search this member's inheritance chain to find the attributes.
            Returns: An array that contains all the custom attributes, or an array with zero elements if no 
             attributes are defined.
        
        GetCustomAttributes(self: _FieldInfo, attributeType: Type, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.GetCustomAttributes(System.Type,System.Boolean) method.
        
        
            attributeType: The type of attribute to search for. Only attributes that are assignable to this type are 
             returned.
        
            inherit: Specifies whether to search this member's inheritance chain to find the attributes.
            Returns: An array of custom attributes applied to this member, or an array with zero (0) elements if no 
             attributes have been applied.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: _FieldInfo) -> int
        
            Provides COM objects with version-independent access to the System.Object.GetHashCode method.
            Returns: The hash code for the current instance.
        """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _FieldInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: Passed-in array of names to be mapped.
            cNames: Count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: Caller-allocated array that receives the IDs corresponding to the names.
        """
        pass

    def GetType(self):
        """
        GetType(self: _FieldInfo) -> Type
        
            Provides COM objects with version-independent access to the System.Object.GetType method.
            Returns: A System.Type object.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _FieldInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can then be used to get the type information 
             for an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: Receives a pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _FieldInfo) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def GetValue(self, obj):
        """
        GetValue(self: _FieldInfo, obj: object) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.FieldInfo.GetValue(System.Object) method.
        
        
            obj: The object whose field value will be returned.
            Returns: An object containing the value of the field reflected by this instance.
        """
        pass

    def GetValueDirect(self, obj):
        """
        GetValueDirect(self: _FieldInfo, obj: TypedReference) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.FieldInfo.GetValueDirect(System.TypedReference) method.
        
        
            obj: A System.TypedReference structure that encapsulates a managed pointer to a location and a 
             runtime representation of the type that might be stored at that location.
        
            Returns: An System.Object containing a field value.
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _FieldInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: Identifies the member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: Pointer to a structure containing an array of arguments, an array of argument DISPIDs for named 
             arguments, and counts for the number of elements in the arrays.
        
            pVarResult: Pointer to the location where the result is to be stored.
            pExcepInfo: Pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def IsDefined(self, attributeType, inherit):
        """
        IsDefined(self: _FieldInfo, attributeType: Type, inherit: bool) -> bool
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.IsDefined(System.Type,System.Boolean) method.
        
        
            attributeType: The System.Type object to which the custom attributes are applied.
            inherit: Specifies whether to search this member's inheritance chain to find the attributes.
            Returns: true if one or more instance of attributeType is applied to this member; otherwise, false.
        """
        pass

    def SetValue(self, obj, value, invokeAttr=None, binder=None, culture=None):
        """
        SetValue(self: _FieldInfo, obj: object, value: object)
            Provides COM objects with version-independent access to the 
             System.Reflection.FieldInfo.SetValue(System.Object,System.Object) method.
        
        
            obj: The object whose field value will be set.
            value: The value to assign to the field.
        SetValue(self: _FieldInfo, obj: object, value: object, invokeAttr: BindingFlags, binder: Binder, culture: CultureInfo)
            Provides COM objects with version-independent access to the 
             System.Reflection.PropertyInfo.SetValue(System.Object,System.Object,System.Reflection.BindingFlag
             s,System.Reflection.Binder,System.Object[],System.Globalization.CultureInfo) method.
        
        
            obj: The object whose field value will be set.
            value: The value to assign to the field.
            invokeAttr: A field of System.Reflection.Binder that specifies the type of binding that is desired (for 
             example, Binder.CreateInstance or Binder.ExactBinding).
        
            binder: A set of properties that enables the binding, coercion of argument types, and invocation of 
             members through reflection. If binder is null, then Binder.DefaultBinding is used.
        
            culture: The software preferences of a particular culture.
        """
        pass

    def SetValueDirect(self, obj, value):
        """
        SetValueDirect(self: _FieldInfo, obj: TypedReference, value: object)
            Provides COM objects with version-independent access to the 
             System.Reflection.FieldInfo.SetValueDirect(System.TypedReference,System.Object) method.
        
        
            obj: The object whose field value will be set.
            value: The value to assign to the field.
        """
        pass

    def ToString(self):
        """
        ToString(self: _FieldInfo) -> str
        
            Provides COM objects with version-independent access to the System.Object.ToString method.
            Returns: A string that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.Attributes property.

Get: Attributes(self: _FieldInfo) -> FieldAttributes

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.DeclaringType property.

Get: DeclaringType(self: _FieldInfo) -> Type

"""

    FieldHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.FieldHandle property.

Get: FieldHandle(self: _FieldInfo) -> RuntimeFieldHandle

"""

    FieldType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.FieldType property.

Get: FieldType(self: _FieldInfo) -> Type

"""

    IsAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsAssembly property.

Get: IsAssembly(self: _FieldInfo) -> bool

"""

    IsFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsFamily property.

Get: IsFamily(self: _FieldInfo) -> bool

"""

    IsFamilyAndAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsFamilyAndAssembly property.

Get: IsFamilyAndAssembly(self: _FieldInfo) -> bool

"""

    IsFamilyOrAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsFamilyOrAssembly property.

Get: IsFamilyOrAssembly(self: _FieldInfo) -> bool

"""

    IsInitOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsInitOnly property.

Get: IsInitOnly(self: _FieldInfo) -> bool

"""

    IsLiteral = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsLiteral property.

Get: IsLiteral(self: _FieldInfo) -> bool

"""

    IsNotSerialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsNotSerialized property.

Get: IsNotSerialized(self: _FieldInfo) -> bool

"""

    IsPinvokeImpl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsPinvokeImpl property.

Get: IsPinvokeImpl(self: _FieldInfo) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsPrivate property.

Get: IsPrivate(self: _FieldInfo) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsPublic property.

Get: IsPublic(self: _FieldInfo) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsSpecialName property.

Get: IsSpecialName(self: _FieldInfo) -> bool

"""

    IsStatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsStatic property.

Get: IsStatic(self: _FieldInfo) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.MemberType property.

Get: MemberType(self: _FieldInfo) -> MemberTypes

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.Name property.

Get: Name(self: _FieldInfo) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.ReflectedType property.

Get: ReflectedType(self: _FieldInfo) -> Type

"""



class _ILGenerator:
    """ Exposes the System.Reflection.Emit.ILGenerator class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _ILGenerator, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: A count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _ILGenerator, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _ILGenerator) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _ILGenerator, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _LocalBuilder:
    """ Exposes the System.Reflection.Emit.LocalBuilder class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _LocalBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _LocalBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _LocalBuilder) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _LocalBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result is to be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _MemberInfo:
    """ Exposes the public members of the System.Reflection.MemberInfo class to unmanaged code. """
    def Equals(self, other):
        """
        Equals(self: _MemberInfo, other: object) -> bool
        
            Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 
             method.
        
        
            other: The System.Object to compare with the current System.Object.
            Returns: true if the specified System.Object is equal to the current System.Object; otherwise, false.
        """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _MemberInfo, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.GetCustomAttributes(System.Boolean) method.
        
        
            inherit: true to search this member's inheritance chain to find the attributes; otherwise, false.
            Returns: An array that contains all the custom attributes, or an array with zero (0) elements if no 
             attributes are defined.
        
        GetCustomAttributes(self: _MemberInfo, attributeType: Type, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetCustomAttributes(System.Type,System.Boolean) method.
        
        
            attributeType: The type of attribute to search for. Only attributes that are assignable to this type are 
             returned.
        
            inherit: true to search this member's inheritance chain to find the attributes; otherwise, false.
            Returns: An array of custom attributes applied to this member, or an array with zero (0) elements if no 
             attributes have been applied.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: _MemberInfo) -> int
        
            Provides COM objects with version-independent access to the System.Object.GetHashCode method.
            Returns: The hash code for the current instance.
        """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _MemberInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An  array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetType(self):
        """
        GetType(self: _MemberInfo) -> Type
        
            Provides COM objects with version-independent access to the System.Type.GetType method.
            Returns: A System.Type object.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _MemberInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _MemberInfo) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _MemberInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier for the member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def IsDefined(self, attributeType, inherit):
        """
        IsDefined(self: _MemberInfo, attributeType: Type, inherit: bool) -> bool
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.IsDefined(System.Type,System.Boolean) method.
        
        
            attributeType: The System.Type object to which the custom attributes are applied.
            inherit: true to search this member's inheritance chain to find the attributes; otherwise, false.
            Returns: true if one or more instance of the attributeType parameter is applied to this member; 
             otherwise, false.
        """
        pass

    def ToString(self):
        """
        ToString(self: _MemberInfo) -> str
        
            Provides COM objects with version-independent access to the System.Object.ToString method.
            Returns: A string that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.DeclaringType property.

Get: DeclaringType(self: _MemberInfo) -> Type

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.MemberType property.

Get: MemberType(self: _MemberInfo) -> MemberTypes

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.Name property.

Get: Name(self: _MemberInfo) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.ReflectedType property.

Get: ReflectedType(self: _MemberInfo) -> Type

"""



class _MethodBase:
    """ Exposes the public members of the System.Reflection.MethodBase class to unmanaged code. """
    def Equals(self, other):
        """
        Equals(self: _MethodBase, other: object) -> bool
        
            Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 
             method.
        
        
            other: The System.Object to compare with the current System.Object.
            Returns: true if the specified System.Object is equal to the current System.Object; otherwise, false.
        """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _MethodBase, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.GetCustomAttributes(System.Boolean) method.
        
        
            inherit: true to search this member's inheritance chain to find the attributes; otherwise, false.
            Returns: An array that contains all the custom attributes, or an array with zero (0) elements if no 
             attributes are defined.
        
        GetCustomAttributes(self: _MethodBase, attributeType: Type, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.GetCustomAttributes(System.Type,System.Boolean) method.
        
        
            attributeType: The type of attribute to search for. Only attributes that are assignable to this type are 
             returned.
        
            inherit: true to search this member's inheritance chain to find the attributes; otherwise, false.
            Returns: An array of custom attributes applied to this member, or an array with zero (0) elements if no 
             attributes have been applied.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: _MethodBase) -> int
        
            Provides COM objects with version-independent access to the System.Object.GetHashCode method.
            Returns: The hash code for the current instance.
        """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _MethodBase, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetMethodImplementationFlags(self):
        """
        GetMethodImplementationFlags(self: _MethodBase) -> MethodImplAttributes
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MethodBase.GetMethodImplementationFlags method.
        
            Returns: One of the System.Reflection.MethodImplAttributes values.
        """
        pass

    def GetParameters(self):
        """
        GetParameters(self: _MethodBase) -> Array[ParameterInfo]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MethodBase.GetParameters method.
        
            Returns: An array of type System.Reflection.ParameterInfo containing information that matches the 
             signature of the method (or constructor) reflected by this instance.
        """
        pass

    def GetType(self):
        """
        GetType(self: _MethodBase) -> Type
        
            Provides COM objects with version-independent access to the System.Type.GetType method.
            Returns: A System.Type object.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _MethodBase, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _MethodBase) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, *__args):
        """
        Invoke(self: _MethodBase, obj: object, parameters: Array[object]) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MethodBase.Invoke(System.Object,System.Object[]) method.
        
        
            obj: The instance that created this method.
            parameters: An argument list for the invoked method or constructor. This is an array of objects with the 
             same number, order, and type as the parameters of the method or constructor to be invoked. If 
             there are no parameters, parameters should be null.If the method or constructor represented by 
             this instance takes a ref parameter (ByRef in Visual Basic), no special attribute is required 
             for that parameter to invoke the method or constructor using this function. Any object in this 
             array that is not explicitly initialized with a value will contain the default value for that 
             object type. For reference type elements, this value is null. For value type elements, this 
             value is 0, 0.0, or false, depending on the specific element type.
        
            Returns: An instance of the class associated with the constructor.
        Invoke(self: _MethodBase, obj: object, invokeAttr: BindingFlags, binder: Binder, parameters: Array[object], culture: CultureInfo) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MethodBase.Invoke(System.Object,System.Reflection.BindingFlags,System.Reflectio
             n.Binder,System.Object[],System.Globalization.CultureInfo) method.
        
        
            obj: The instance that created this method.
            invokeAttr: One of the BindingFlags values that specifies the type of binding.
            binder: A Binder that defines a set of properties and enables the binding, coercion of argument types, 
             and invocation of members using reflection. If binder is null, then Binder.DefaultBinding is 
             used.
        
            parameters: An array of type Object used to match the number, order, and type of the parameters for this 
             constructor, under the constraints of binder. If this constructor does not require parameters, 
             pass an array with zero elements, as in Object[] parameters = new Object[0]. Any object in this 
             array that is not explicitly initialized with a value will contain the default value for that 
             object type. For reference type elements, this value is null. For value type elements, this 
             value is 0, 0.0, or false, depending on the specific element type.
        
            culture: A System.Globalization.CultureInfo object used to govern the coercion of types. If this is null, 
             the System.Globalization.CultureInfo for the current thread is used.
        
            Returns: An instance of the class associated with the constructor.
        Invoke(self: _MethodBase, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier for the member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def IsDefined(self, attributeType, inherit):
        """
        IsDefined(self: _MethodBase, attributeType: Type, inherit: bool) -> bool
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.IsDefined(System.Type,System.Boolean) method.
        
        
            attributeType: The Type object to which the custom attributes are applied.
            inherit: true to search this member's inheritance chain to find the attributes; otherwise, false.
            Returns: true if one or more instance of the attributeType parameter is applied to this member; 
             otherwise, false.
        """
        pass

    def ToString(self):
        """
        ToString(self: _MethodBase) -> str
        
            Provides COM objects with version-independent access to the System.Object.ToString method.
            Returns: A string that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.Attributes property.

Get: Attributes(self: _MethodBase) -> MethodAttributes

"""

    CallingConvention = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.CallingConvention property.

Get: CallingConvention(self: _MethodBase) -> CallingConventions

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.DeclaringType property.

Get: DeclaringType(self: _MethodBase) -> Type

"""

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsAbstract property.

Get: IsAbstract(self: _MethodBase) -> bool

"""

    IsAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsAssembly property.

Get: IsAssembly(self: _MethodBase) -> bool

"""

    IsConstructor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsConstructor property.

Get: IsConstructor(self: _MethodBase) -> bool

"""

    IsFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFamily property.

Get: IsFamily(self: _MethodBase) -> bool

"""

    IsFamilyAndAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFamilyAndAssembly property.

Get: IsFamilyAndAssembly(self: _MethodBase) -> bool

"""

    IsFamilyOrAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFamilyOrAssembly property.

Get: IsFamilyOrAssembly(self: _MethodBase) -> bool

"""

    IsFinal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFinal property.

Get: IsFinal(self: _MethodBase) -> bool

"""

    IsHideBySig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsHideBySig property.

Get: IsHideBySig(self: _MethodBase) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsPrivate property.

Get: IsPrivate(self: _MethodBase) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsPublic property.

Get: IsPublic(self: _MethodBase) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsSpecialName property.

Get: IsSpecialName(self: _MethodBase) -> bool

"""

    IsStatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsStatic property.

Get: IsStatic(self: _MethodBase) -> bool

"""

    IsVirtual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsVirtual property.

Get: IsVirtual(self: _MethodBase) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.MemberType property.

Get: MemberType(self: _MethodBase) -> MemberTypes

"""

    MethodHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.MethodHandle property.

Get: MethodHandle(self: _MethodBase) -> RuntimeMethodHandle

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.Name property.

Get: Name(self: _MethodBase) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.ReflectedType property.

Get: ReflectedType(self: _MethodBase) -> Type

"""



class _MethodBuilder:
    """ Exposes the System.Reflection.Emit.MethodBuilder class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _MethodBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _MethodBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _MethodBuilder) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _MethodBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _MethodInfo:
    """ Exposes the public members of the System.Reflection.MethodInfo class to unmanaged code. """
    def Equals(self, other):
        """
        Equals(self: _MethodInfo, other: object) -> bool
        
            Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 
             method.
        
        
            other: The System.Object to compare with the current System.Object.
            Returns: true if the specified System.Object is equal to the current System.Object; otherwise, false.
        """
        pass

    def GetBaseDefinition(self):
        """
        GetBaseDefinition(self: _MethodInfo) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MethodInfo.GetBaseDefinition method.
        
            Returns: A System.Reflection.MethodInfo object for the first implementation of this method.
        """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _MethodInfo, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.GetCustomAttributes(System.Boolean) method.
        
        
            inherit: true to search this member's inheritance chain to find the attributes; otherwise, false.
            Returns: An array that contains all the custom attributes, or an array with zero (0) elements if no 
             attributes are defined.
        
        GetCustomAttributes(self: _MethodInfo, attributeType: Type, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.GetCustomAttributes(System.Type,System.Boolean) method.
        
        
            attributeType: The type of attribute to search for. Only attributes that are assignable to this type are 
             returned.
        
            inherit: true to search this member's inheritance chain to find the attributes; otherwise, false.
            Returns: An array of custom attributes applied to this member, or an array with zero (0) elements if no 
             attributes have been applied.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: _MethodInfo) -> int
        
            Provides COM objects with version-independent access to the System.Object.GetHashCode method.
            Returns: The hash code for the current instance.
        """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _MethodInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetMethodImplementationFlags(self):
        """
        GetMethodImplementationFlags(self: _MethodInfo) -> MethodImplAttributes
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MethodBase.GetMethodImplementationFlags method.
        
            Returns: One of the System.Reflection.MethodImplAttributes values.
        """
        pass

    def GetParameters(self):
        """
        GetParameters(self: _MethodInfo) -> Array[ParameterInfo]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MethodBase.GetParameters method.
        
            Returns: An array of type System.Reflection.ParameterInfo containing information that matches the 
             signature of the method (or constructor) reflected by this instance.
        """
        pass

    def GetType(self):
        """
        GetType(self: _MethodInfo) -> Type
        
            Provides COM objects with version-independent access to the System.Type.GetType method.
            Returns: A System.Type object.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _MethodInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _MethodInfo) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, *__args):
        """
        Invoke(self: _MethodInfo, obj: object, parameters: Array[object]) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MethodBase.Invoke(System.Object,System.Object[]) method.
        
        
            obj: The instance that created this method.
            parameters: An argument list for the invoked method or constructor. This is an array of objects with the 
             same number, order, and type as the parameters of the method or constructor to be invoked. If 
             there are no parameters, parameters should be null.If the method or constructor represented by 
             this instance takes a ref parameter (ByRef in Visual Basic), no special attribute is required 
             for that parameter to invoke the method or constructor using this function. Any object in this 
             array that is not explicitly initialized with a value will contain the default value for that 
             object type. For reference type elements, this value is null. For value type elements, this 
             value is 0, 0.0, or false, depending on the specific element type.
        
            Returns: An instance of the class associated with the constructor.
        Invoke(self: _MethodInfo, obj: object, invokeAttr: BindingFlags, binder: Binder, parameters: Array[object], culture: CultureInfo) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MethodBase.Invoke(System.Object,System.Reflection.BindingFlags,System.Reflectio
             n.Binder,System.Object[],System.Globalization.CultureInfo) method.
        
        
            obj: The instance that created this method.
            invokeAttr: One of the BindingFlags values that specifies the type of binding.
            binder: A Binder that defines a set of properties and enables the binding, coercion of argument types, 
             and invocation of members using reflection. If binder is null, then Binder.DefaultBinding is 
             used.
        
            parameters: An array of type Object used to match the number, order, and type of the parameters for this 
             constructor, under the constraints of binder. If this constructor does not require parameters, 
             pass an array with zero elements, as in Object[] parameters = new Object[0]. Any object in this 
             array that is not explicitly initialized with a value will contain the default value for that 
             object type. For reference type elements, this value is null. For value type elements, this 
             value is 0, 0.0, or false, depending on the specific element type.
        
            culture: A System.Globalization.CultureInfo object used to govern the coercion of types. If this is null, 
             the System.Globalization.CultureInfo for the current thread is used.
        
            Returns: An instance of the class associated with the constructor.
        Invoke(self: _MethodInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier for the member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def IsDefined(self, attributeType, inherit):
        """
        IsDefined(self: _MethodInfo, attributeType: Type, inherit: bool) -> bool
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.IsDefined(System.Type,System.Boolean) method.
        
        
            attributeType: The Type object to which the custom attributes are applied.
            inherit: true to search this member's inheritance chain to find the attributes; otherwise, false.
            Returns: true if one or more instance of the attributeType parameter is applied to this member; 
             otherwise, false.
        """
        pass

    def ToString(self):
        """
        ToString(self: _MethodInfo) -> str
        
            Provides COM objects with version-independent access to the System.Object.ToString method.
            Returns: A string that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.Attributes property.

Get: Attributes(self: _MethodInfo) -> MethodAttributes

"""

    CallingConvention = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.CallingConvention property.

Get: CallingConvention(self: _MethodInfo) -> CallingConventions

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.DeclaringType property.

Get: DeclaringType(self: _MethodInfo) -> Type

"""

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsAbstract property.

Get: IsAbstract(self: _MethodInfo) -> bool

"""

    IsAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsAssembly property.

Get: IsAssembly(self: _MethodInfo) -> bool

"""

    IsConstructor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsConstructor property.

Get: IsConstructor(self: _MethodInfo) -> bool

"""

    IsFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFamily property.

Get: IsFamily(self: _MethodInfo) -> bool

"""

    IsFamilyAndAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFamilyAndAssembly property.

Get: IsFamilyAndAssembly(self: _MethodInfo) -> bool

"""

    IsFamilyOrAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFamilyOrAssembly property.

Get: IsFamilyOrAssembly(self: _MethodInfo) -> bool

"""

    IsFinal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFinal property.

Get: IsFinal(self: _MethodInfo) -> bool

"""

    IsHideBySig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsHideBySig property.

Get: IsHideBySig(self: _MethodInfo) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsPrivate property.

Get: IsPrivate(self: _MethodInfo) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsPublic property.

Get: IsPublic(self: _MethodInfo) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsSpecialName property.

Get: IsSpecialName(self: _MethodInfo) -> bool

"""

    IsStatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsStatic property.

Get: IsStatic(self: _MethodInfo) -> bool

"""

    IsVirtual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsVirtual property.

Get: IsVirtual(self: _MethodInfo) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.MemberType property.

Get: MemberType(self: _MethodInfo) -> MemberTypes

"""

    MethodHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodBase.MethodHandle property.

Get: MethodHandle(self: _MethodInfo) -> RuntimeMethodHandle

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.Name property.

Get: Name(self: _MethodInfo) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.ReflectedType property.

Get: ReflectedType(self: _MethodInfo) -> Type

"""

    ReturnType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodInfo.ReturnType property.

Get: ReturnType(self: _MethodInfo) -> Type

"""

    ReturnTypeCustomAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MethodInfo.ReturnTypeCustomAttributes property.

Get: ReturnTypeCustomAttributes(self: _MethodInfo) -> ICustomAttributeProvider

"""



class _MethodRental:
    """ Exposes the System.Reflection.Emit.MethodRental class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _MethodRental, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _MethodRental, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _MethodRental) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _MethodRental, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _Module:
    """ Exposes the System.Reflection.Module class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _Module, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _Module, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _Module) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _Module, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _ModuleBuilder:
    """ Exposes the System.Reflection.Emit.ModuleBuilder class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _ModuleBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _ModuleBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _ModuleBuilder) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _ModuleBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _ParameterBuilder:
    """ Exposes the System.Reflection.Emit.ParameterBuilder class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _ParameterBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _ParameterBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _ParameterBuilder) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _ParameterBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _ParameterInfo:
    """ Exposes the System.Reflection.ParameterInfo class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _ParameterInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _ParameterInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _ParameterInfo) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _ParameterInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _PropertyBuilder:
    """ Exposes the System.Reflection.Emit.PropertyBuilder class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _PropertyBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _PropertyBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _PropertyBuilder) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _PropertyBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _PropertyInfo:
    """ Exposes the public members of the System.Reflection.PropertyInfo class to unmanaged code. """
    def Equals(self, other):
        """
        Equals(self: _PropertyInfo, other: object) -> bool
        
            Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 
             method.
        
        
            other: The System.Object to compare with the current System.Object.
            Returns: true if the specified System.Object is equal to the current System.Object; otherwise, false.
        """
        pass

    def GetAccessors(self, nonPublic=None):
        """
        GetAccessors(self: _PropertyInfo) -> Array[MethodInfo]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.PropertyInfo.GetAccessors method.
        
            Returns: An array of System.Reflection.MethodInfo objects that reflect the public get, set, and other 
             accessors of the property reflected by the current instance, if accessors are found; otherwise, 
             this method returns an array with zero (0) elements.
        
        GetAccessors(self: _PropertyInfo, nonPublic: bool) -> Array[MethodInfo]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.PropertyInfo.GetAccessors(System.Boolean) method.
        
        
            nonPublic: true to include non-public methods in the returned MethodInfo array; otherwise, false.
            Returns: An array of System.Reflection.MethodInfo objects whose elements reflect the get, set, and other 
             accessors of the property reflected by the current instance. If the nonPublic parameter is true, 
             this array contains public and non-public get, set, and other accessors. If nonPublic is false, 
             this array contains only public get, set, and other accessors. If no accessors with the 
             specified visibility are found, this method returns an array with zero (0) elements.
        """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _PropertyInfo, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.GetCustomAttributes(System.Boolean) method.
        
        
            inherit: true to search this member's inheritance chain to find the attributes; otherwise false.
            Returns: An array that contains all the custom attributes, or an array with zero elements if no 
             attributes are defined.
        
        GetCustomAttributes(self: _PropertyInfo, attributeType: Type, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.GetCustomAttributes(System.Type,System.Boolean) method.
        
        
            attributeType: The type of attribute to search for. Only attributes that are assignable to this type are 
             returned.
        
            inherit: true to search this member's inheritance chain to find the attributes; otherwise false.
            Returns: An array of custom attributes applied to this member, or an array with zero (0) elements if no 
             attributes have been applied.
        """
        pass

    def GetGetMethod(self, nonPublic=None):
        """
        GetGetMethod(self: _PropertyInfo) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Reflection.PropertyInfo.GetGetMethod method.
        
            Returns: A System.Reflection.MethodInfo object representing the public get accessor for this property, or 
             null if the get accessor is non-public or does not exist.
        
        GetGetMethod(self: _PropertyInfo, nonPublic: bool) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Reflection.PropertyInfo.GetGetMethod(System.Boolean) method.
        
        
            nonPublic: true to return a non-public get accessor; otherwise, false.
            Returns: A System.Reflection.MethodInfo object representing the get accessor for this property, if the 
             nonPublic parameter is true. Or null if nonPublic is false and the get accessor is non-public, 
             or if nonPublic is true but no get accessors exist.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: _PropertyInfo) -> int
        
            Provides COM objects with version-independent access to the System.Object.GetHashCode method.
            Returns: The hash code for the current instance.
        """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _PropertyInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetIndexParameters(self):
        """
        GetIndexParameters(self: _PropertyInfo) -> Array[ParameterInfo]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.PropertyInfo.GetIndexParameters method.
        
            Returns: An array of type System.Reflection.ParameterInfo containing the parameters for the indexes.
        """
        pass

    def GetSetMethod(self, nonPublic=None):
        """
        GetSetMethod(self: _PropertyInfo) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Reflection.PropertyInfo.GetSetMethod method.
        
            Returns: The System.Reflection.MethodInfo object representing the Set method for this property if the set 
             accessor is public, or null if the set accessor is not public.
        
        GetSetMethod(self: _PropertyInfo, nonPublic: bool) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Reflection.PropertyInfo.GetSetMethod(System.Boolean) method.
        
        
            nonPublic: true to return a non-public accessor; otherwise, false.
            Returns: One of the values in the following table.Value Meaning A System.Reflection.MethodInfo object 
             representing the Set method for this property. The set accessor is public.-or- The nonPublic 
             parameter is true and the set accessor is non-public. nullThe nonPublic parameter is true, but 
             the property is read-only.-or- The nonPublic parameter is false and the set accessor is 
             non-public.-or- There is no set accessor.
        """
        pass

    def GetType(self):
        """
        GetType(self: _PropertyInfo) -> Type
        
            Provides COM objects with version-independent access to the System.Object.GetType method.
            Returns: A System.Type object.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _PropertyInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _PropertyInfo) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def GetValue(self, obj, *__args):
        """
        GetValue(self: _PropertyInfo, obj: object, invokeAttr: BindingFlags, binder: Binder, index: Array[object], culture: CultureInfo) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.PropertyInfo.GetValue(System.Object,System.Reflection.BindingFlags,System.Refle
             ction.Binder,System.Object[],System.Globalization.CultureInfo) method.
        
        
            obj: The object whose property value will be returned.
            invokeAttr: The invocation attribute. This must be a bit flag from BindingFlags: InvokeMethod, 
             CreateInstance, Static, GetField, SetField, GetProperty, or SetProperty. A suitable invocation 
             attribute must be specified. If a static member will be invoked, the Static flag of BindingFlags 
             must be set.
        
            binder: An object that enables the binding, coercion of argument types, invocation of members, and 
             retrieval of MemberInfo objects through reflection. If binder is null, the default binder is 
             used.
        
            index: Optional index values for indexed properties. This value should be null for non-indexed 
             properties.
        
            culture: The CultureInfo object that represents the culture for which the resource will be localized. 
             Note that if the resource is not localized for this culture, the CultureInfo.Parent method will 
             be called successively in search of a match. If this value is null, the CultureInfo is obtained 
             from the CultureInfo.CurrentUICulture property.
        
            Returns: The property value for the obj parameter.
        GetValue(self: _PropertyInfo, obj: object, index: Array[object]) -> object
        
            Provides COM objects with version-independent access to the 
             System.Reflection.PropertyInfo.GetValue(System.Object,System.Object[]) method.
        
        
            obj: The object whose property value will be returned.
            index: Optional index values for indexed properties. This value should be null for non-indexed 
             properties.
        
            Returns: The property value for the obj parameter.
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _PropertyInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def IsDefined(self, attributeType, inherit):
        """
        IsDefined(self: _PropertyInfo, attributeType: Type, inherit: bool) -> bool
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.IsDefined(System.Type,System.Boolean) method.
        
        
            attributeType: The System.Type object to which the custom attributes are applied.
            inherit: true to search this member's inheritance chain to find the attributes; otherwise false.
            Returns: true if one or more instances of the attributeType parameter are applied to this member; 
             otherwise, false.
        """
        pass

    def SetValue(self, obj, value, *__args):
        """
        SetValue(self: _PropertyInfo, obj: object, value: object, invokeAttr: BindingFlags, binder: Binder, index: Array[object], culture: CultureInfo)
            Provides COM objects with version-independent access to the 
             System.Reflection.FieldInfo.SetValue(System.Object,System.Object,System.Reflection.BindingFlags,S
             ystem.Reflection.Binder,System.Globalization.CultureInfo) method.
        
        
            obj: The object whose property value will be returned.
            value: The new value for this property.
            invokeAttr: The invocation attribute. This must be a bit flag from System.Reflection.BindingFlags: 
             InvokeMethod, CreateInstance, Static, GetField, SetField, GetProperty, or SetProperty. A 
             suitable invocation attribute must be specified. If a static member will be invoked, the Static 
             flag of BindingFlags must be set.
        
            binder: An object that enables the binding, coercion of argument types, invocation of members, and 
             retrieval of System.Reflection.MemberInfo objects through reflection. If binder is null, the 
             default binder is used.
        
            index: Optional index values for indexed properties. This value should be null for non-indexed 
             properties.
        
            culture: The System.Globalization.CultureInfo object that represents the culture for which the resource 
             will be localized. Note that if the resource is not localized for this culture, the 
             CultureInfo.Parent method will be called successively in search of a match. If this value is 
             null, the CultureInfo is obtained from the CultureInfo.CurrentUICulture property.
        
        SetValue(self: _PropertyInfo, obj: object, value: object, index: Array[object])
            Provides COM objects with version-independent access to the 
             System.Reflection.PropertyInfo.SetValue(System.Object,System.Object,System.Object[]) method.
        
        
            obj: The object whose property value will be set.
            value: The new value for this property.
            index: Optional index values for indexed properties. This value should be null for non-indexed 
             properties.
        """
        pass

    def ToString(self):
        """
        ToString(self: _PropertyInfo) -> str
        
            Provides COM objects with version-independent access to the System.Object.ToString method.
            Returns: A string that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.PropertyInfo.Attributes property.

Get: Attributes(self: _PropertyInfo) -> PropertyAttributes

"""

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.PropertyInfo.CanRead property.

Get: CanRead(self: _PropertyInfo) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.PropertyInfo.CanWrite property.

Get: CanWrite(self: _PropertyInfo) -> bool

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.DeclaringType property.

Get: DeclaringType(self: _PropertyInfo) -> Type

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.PropertyInfo.IsSpecialName property.

Get: IsSpecialName(self: _PropertyInfo) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.PropertyInfo.MemberType property.

Get: MemberType(self: _PropertyInfo) -> MemberTypes

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.Name property.

Get: Name(self: _PropertyInfo) -> str

"""

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.PropertyInfo.PropertyType property.

Get: PropertyType(self: _PropertyInfo) -> Type

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.ReflectedType property.

Get: ReflectedType(self: _PropertyInfo) -> Type

"""



class _SignatureHelper:
    """ Exposes the System.Reflection.Emit.SignatureHelper class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _SignatureHelper, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _SignatureHelper, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _SignatureHelper) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _SignatureHelper, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _Thread:
    """ Exposes the System.Threading.Thread class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _Thread, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _Thread, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _Thread) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _Thread, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _Type:
    """ Exposes the public members of the System.Type class to the unmanaged code. """
    def Equals(self, *__args):
        """
        Equals(self: _Type, o: Type) -> bool
        
            Provides COM objects with version-independent access to the System.Type.Equals(System.Type) 
             method.
        
        
            o: The System.Type whose underlying system type is to be compared with the underlying system type 
             of the current System.Type.
        
            Returns: true if the underlying system type of o is the same as the underlying system type of the current 
             System.Type; otherwise, false.
        
        Equals(self: _Type, other: object) -> bool
        
            Provides COM objects with version-independent access to the System.Type.Equals(System.Object) 
             method.
        
        
            other: The System.Object whose underlying system type is to be compared with the underlying system type 
             of the current System.Type.
        
            Returns: true if the underlying system type of o is the same as the underlying system type of the current 
             System.Type; otherwise, false.
        """
        pass

    def FindInterfaces(self, filter, filterCriteria):
        """
        FindInterfaces(self: _Type, filter: TypeFilter, filterCriteria: object) -> Array[Type]
        
            Provides COM objects with version-independent access to the 
             System.Type.FindInterfaces(System.Reflection.TypeFilter,System.Object) method.
        
        
            filter: The System.Reflection.TypeFilter delegate that compares the interfaces against filterCriteria.
            filterCriteria: The search criteria that determines whether an interface should be included in the returned 
             array.
        
            Returns: An array of System.Type objects representing a filtered list of the interfaces implemented or 
             inherited by the current System.Type.-or- An empty array of type System.Type, if no interfaces 
             matching the filter are implemented or inherited by the current System.Type.
        """
        pass

    def FindMembers(self, memberType, bindingAttr, filter, filterCriteria):
        """
        FindMembers(self: _Type, memberType: MemberTypes, bindingAttr: BindingFlags, filter: MemberFilter, filterCriteria: object) -> Array[MemberInfo]
        
            Provides COM objects with version-independent access to the 
             System.Type.FindMembers(System.Reflection.MemberTypes,System.Reflection.BindingFlags,System.Refle
             ction.MemberFilter,System.Object) method.
        
        
            memberType: A MemberTypes object indicating the type of member to search for.
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            filter: The delegate that does the comparisons, returning true if the member currently being inspected 
             matches the filterCriteria and false otherwise. You can use the FilterAttribute, FilterName, and 
             FilterNameIgnoreCase delegates supplied by this class. The first uses the fields of 
             FieldAttributes, MethodAttributes, and MethodImplAttributes as search criteria, and the other 
             two delegates use String objects as the search criteria.
        
            filterCriteria: The search criteria that determines whether a member is returned in the array of MemberInfo 
             objects.The fields of FieldAttributes, MethodAttributes, and MethodImplAttributes can be used in 
             conjunction with the FilterAttribute delegate supplied by this class.
        
            Returns: A filtered array of System.Reflection.MemberInfo objects of the specified member type.-or- An 
             empty array of type System.Reflection.MemberInfo, if the current System.Type does not have 
             members of type memberType that match the filter criteria.
        """
        pass

    def GetArrayRank(self):
        """
        GetArrayRank(self: _Type) -> int
        
            Provides COM objects with version-independent access to the System.Type.GetArrayRank method.
            Returns: An System.Int32 containing the number of dimensions in the current System.Type.
        """
        pass

    def GetConstructor(self, *__args):
        """
        GetConstructor(self: _Type, types: Array[Type]) -> ConstructorInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetConstructor(System.Type[]) method.
        
        
            types: An array of System.Type objects representing the number, order, and type of the parameters for 
             the desired constructor.-or- An empty array of System.Type objects, to get a constructor that 
             takes no parameters. Such an empty array is provided by the static field System.Type.EmptyTypes.
        
            Returns: A System.Reflection.ConstructorInfo object representing the public instance constructor whose 
             parameters match the types in the parameter type array, if found; otherwise, null.
        
        GetConstructor(self: _Type, bindingAttr: BindingFlags, binder: Binder, types: Array[Type], modifiers: Array[ParameterModifier]) -> ConstructorInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetConstructor(System.Reflection.BindingFlags,System.Reflection.Binder,System.Type[],
             System.Reflection.ParameterModifier[]) method.
        
        
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            binder: A System.Reflection.Binder object that defines a set of properties and enables binding, which 
             can involve selection of an overloaded method, coercion of argument types, and invocation of a 
             member through reflection.-or- null, to use the System.Type.DefaultBinder.
        
            types: An array of System.Type objects representing the number, order, and type of the parameters for 
             the constructor to get.-or- An empty array of the type System.Type (that is, Type[] types = new 
             Type[0]) to get a constructor that takes no parameters.-or- System.Type.EmptyTypes.
        
            modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 
             with the corresponding element in the parameter type array. The default binder does not process 
             this parameter.
        
            Returns: A System.Reflection.ConstructorInfo object representing the constructor that matches the 
             specified requirements, if found; otherwise, null.
        
        GetConstructor(self: _Type, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> ConstructorInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetConstructor(System.Reflection.BindingFlags,System.Reflection.Binder,System.Reflect
             ion.CallingConventions,System.Type[],System.Reflection.ParameterModifier[]) method.
        
        
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            binder: A System.Reflection.Binder object that defines a set of properties and enables binding, which 
             can involve selection of an overloaded method, coercion of argument types, and invocation of a 
             member through reflection.-or- null, to use the System.Type.DefaultBinder.
        
            callConvention: The System.Reflection.CallingConventions object that specifies the set of rules to use regarding 
             the order and layout of arguments, how the return value is passed, what registers are used for 
             arguments, and the stack is cleaned up.
        
            types: An array of System.Type objects representing the number, order, and type of the parameters for 
             the constructor to get.-or- An empty array of the type System.Type (that is, Type[] types = new 
             Type[0]) to get a constructor that takes no parameters.
        
            modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 
             with the corresponding element in the types array. The default binder does not process this 
             parameter.
        
            Returns: A System.Reflection.ConstructorInfo object representing the constructor that matches the 
             specified requirements, if found; otherwise, null.
        """
        pass

    def GetConstructors(self, bindingAttr=None):
        """
        GetConstructors(self: _Type) -> Array[ConstructorInfo]
        
            Provides COM objects with version-independent access to the System.Type.GetConstructors method.
            Returns: An array of System.Reflection.ConstructorInfo objects representing all the public instance 
             constructors defined for the current System.Type, but not including the type initializer (static 
             constructor). If no public instance constructors are defined for the current System.Type, or if 
             the current System.Type represents a type parameter of a generic type or method definition, an 
             empty array of type System.Reflection.ConstructorInfo is returned.
        
        GetConstructors(self: _Type, bindingAttr: BindingFlags) -> Array[ConstructorInfo]
        
            Provides COM objects with version-independent access to the 
             System.Type.GetConstructors(System.Reflection.BindingFlags) method.
        
        
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            Returns: An array of System.Reflection.ConstructorInfo objects representing all constructors defined for 
             the current System.Type that match the specified binding constraints, including the type 
             initializer if it is defined. Returns an empty array of type System.Reflection.ConstructorInfo 
             if no constructors are defined for the current System.Type, if none of the defined constructors 
             match the binding constraints, or if the current System.Type represents a type parameter of a 
             generic type or method definition.
        """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _Type, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.Assembly.GetCustomAttributes(System.Boolean) method.
        
        
            inherit: Specifies whether to search this member's inheritance chain to find the attributes.
            Returns: An array of custom attributes applied to this member, or an array with zero (0) elements if no 
             attributes have been applied.
        
        GetCustomAttributes(self: _Type, attributeType: Type, inherit: bool) -> Array[object]
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.GetCustomAttributes(System.Type,System.Boolean) method.
        
        
            attributeType: The type of attribute to search for. Only attributes that are assignable to this type are 
             returned.
        
            inherit: Specifies whether to search this member's inheritance chain to find the attributes.
            Returns: An array of custom attributes applied to this member, or an array with zero (0) elements if no 
             attributes have been applied.
        """
        pass

    def GetDefaultMembers(self):
        """
        GetDefaultMembers(self: _Type) -> Array[MemberInfo]
        
            Provides COM objects with version-independent access to the System.Type.GetDefaultMembers method.
            Returns: An array of System.Reflection.MemberInfo objects representing all default members of the current 
             System.Type.-or- An empty array of type System.Reflection.MemberInfo, if the current System.Type 
             does not have default members.
        """
        pass

    def GetElementType(self):
        """
        GetElementType(self: _Type) -> Type
        
            Provides COM objects with version-independent access to the System.Type.GetElementType method.
            Returns: The System.Type of the object encompassed or referred to by the current array, pointer or 
             reference type.-or- null if the current System.Type is not an array or a pointer, or is not 
             passed by reference, or represents a generic type or a type parameter of a generic type or 
             method definition.
        """
        pass

    def GetEvent(self, name, bindingAttr=None):
        """
        GetEvent(self: _Type, name: str) -> EventInfo
        
            Provides COM objects with version-independent access to the System.Type.GetEvent(System.String) 
             method.
        
        
            name: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            Returns: An array of System.Reflection.EventInfo objects representing all events that are declared or 
             inherited by the current System.Type that match the specified binding constraints.-or- An empty 
             array of type System.Reflection.EventInfo, if the current System.Type does not have events, or 
             if none of the events match the binding constraints.
        
        GetEvent(self: _Type, name: str, bindingAttr: BindingFlags) -> EventInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetEvent(System.String,System.Reflection.BindingFlags) method.
        
        
            name: The System.String containing the name of an event that is declared or inherited by the current 
             System.Type.
        
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            Returns: The System.Reflection.EventInfo object representing the specified event that is declared or 
             inherited by the current System.Type, if found; otherwise, null.
        """
        pass

    def GetEvents(self, bindingAttr=None):
        """
        GetEvents(self: _Type, bindingAttr: BindingFlags) -> Array[EventInfo]
        
            Provides COM objects with version-independent access to the 
             System.Type.GetEvents(System.Reflection.BindingFlags) method.
        
        
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            Returns: An array of System.Reflection.EventInfo objects representing all events that are declared or 
             inherited by the current System.Type that match the specified binding constraints.-or- An empty 
             array of type System.Reflection.EventInfo, if the current System.Type does not have events, or 
             if none of the events match the binding constraints.
        
        GetEvents(self: _Type) -> Array[EventInfo]
        
            Provides COM objects with version-independent access to the System.Type.GetEvents method.
            Returns: An array of System.Reflection.EventInfo objects representing all the public events that are 
             declared or inherited by the current System.Type.-or- An empty array of type 
             System.Reflection.EventInfo, if the current System.Type does not have public events.
        """
        pass

    def GetField(self, name, bindingAttr=None):
        """
        GetField(self: _Type, name: str) -> FieldInfo
        
            Provides COM objects with version-independent access to the System.Type.GetField(System.String) 
             method.
        
        
            name: The System.String containing the name of the data field to get.
            Returns: A System.Reflection.FieldInfo object representing the public field with the specified name, if 
             found; otherwise, null.
        
        GetField(self: _Type, name: str, bindingAttr: BindingFlags) -> FieldInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetField(System.String,System.Reflection.BindingFlags) method.
        
        
            name: The System.String containing the name of the data field to get.
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            Returns: A System.Reflection.FieldInfo object representing the field that matches the specified 
             requirements, if found; otherwise, null.
        """
        pass

    def GetFields(self, bindingAttr=None):
        """
        GetFields(self: _Type) -> Array[FieldInfo]
        
            Provides COM objects with version-independent access to the System.Type.GetFields method.
            Returns: An array of System.Reflection.FieldInfo objects representing all the public fields defined for 
             the current System.Type.-or- An empty array of type System.Reflection.FieldInfo, if no public 
             fields are defined for the current System.Type.
        
        GetFields(self: _Type, bindingAttr: BindingFlags) -> Array[FieldInfo]
        
            Provides COM objects with version-independent access to the 
             System.Type.GetFields(System.Reflection.BindingFlags) method.
        
        
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            Returns: An array of System.Reflection.FieldInfo objects representing all fields defined for the current 
             System.Type that match the specified binding constraints.-or- An empty array of type 
             System.Reflection.FieldInfo, if no fields are defined for the current System.Type, or if none of 
             the defined fields match the binding constraints.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: _Type) -> int
        
            Provides COM objects with version-independent access to the System.Type.GetHashCode method.
            Returns: An System.Int32 containing the hash code for this instance.
        """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _Type, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: Passed-in array of names to be mapped.
            cNames: Count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: Caller-allocated array that receives the IDs corresponding to the names.
        """
        pass

    def GetInterface(self, name, ignoreCase=None):
        """
        GetInterface(self: _Type, name: str) -> Type
        
            Provides COM objects with version-independent access to the 
             System.Type.GetInterface(System.String) method.
        
        
            name: The System.String containing the name of the interface to get. For generic interfaces, this is 
             the mangled name.
        
            Returns: A System.Type object representing the interface with the specified name, implemented or 
             inherited by the current System.Type, if found; otherwise, null.
        
        GetInterface(self: _Type, name: str, ignoreCase: bool) -> Type
        
            Provides COM objects with version-independent access to the 
             System.Type.GetInterface(System.String,System.Boolean) method.
        
        
            name: The System.String containing the name of the interface to get. For generic interfaces, this is 
             the mangled name.
        
            ignoreCase: true to perform a case-insensitive search for name.-or- false to perform a case-sensitive search 
             for name.
        
            Returns: A System.Type object representing the interface with the specified name, implemented or 
             inherited by the current System.Type, if found; otherwise, null.
        """
        pass

    def GetInterfaceMap(self, interfaceType):
        """
        GetInterfaceMap(self: _Type, interfaceType: Type) -> InterfaceMapping
        
            Provides COM objects with version-independent access to the 
             System.Type.GetInterfaceMap(System.Type) method.
        
        
            interfaceType: The System.Type of the interface of which to retrieve a mapping.
            Returns: An System.Reflection.InterfaceMapping object representing the interface mapping for 
             interfaceType.
        """
        pass

    def GetInterfaces(self):
        """
        GetInterfaces(self: _Type) -> Array[Type]
        
            Provides COM objects with version-independent access to the System.Type.GetInterfaces method.
            Returns: An array of System.Type objects representing all the interfaces implemented or inherited by the 
             current System.Type.-or- An empty array of type System.Type, if no interfaces are implemented or 
             inherited by the current System.Type.
        """
        pass

    def GetMember(self, name, *__args):
        """
        GetMember(self: _Type, name: str) -> Array[MemberInfo]
        
            Provides COM objects with version-independent access to the System.Type.GetMember(System.String) 
             method.
        
        
            name: The System.String containing the name of the public members to get.
            Returns: An array of System.Reflection.MemberInfo objects representing the public members with the 
             specified name, if found; otherwise, an empty array.
        
        GetMember(self: _Type, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]
        
            Provides COM objects with version-independent access to the 
             System.Type.GetMember(System.String,System.Reflection.BindingFlags) method.
        
        
            name: The System.String containing the name of the members to get.
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return an empty array.
        
            Returns: An array of System.Reflection.MemberInfo objects representing the public members with the 
             specified name, if found; otherwise, an empty array.
        
        GetMember(self: _Type, name: str, type: MemberTypes, bindingAttr: BindingFlags) -> Array[MemberInfo]
        
            Provides COM objects with version-independent access to the 
             System.Type.GetMember(System.String,System.Reflection.MemberTypes,System.Reflection.BindingFlags)
              method.
        
        
            name: The System.String containing the name of the members to get.
            type: The System.Reflection.MemberTypes value to search for.
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return an empty array.
        
            Returns: An array of System.Reflection.MemberInfo objects representing the public members with the 
             specified name, if found; otherwise, an empty array.
        """
        pass

    def GetMembers(self, bindingAttr=None):
        """
        GetMembers(self: _Type) -> Array[MemberInfo]
        
            Provides COM objects with version-independent access to the System.Type.GetMembers method.
            Returns: An array of System.Reflection.MemberInfo objects representing all the public members of the 
             current System.Type.-or- An empty array of type System.Reflection.MemberInfo, if the current 
             System.Type does not have public members.
        
        GetMembers(self: _Type, bindingAttr: BindingFlags) -> Array[MemberInfo]
        
            Provides COM objects with version-independent access to the 
             System.Type.GetMembers(System.Reflection.BindingFlags) method.
        
        
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            Returns: An array of System.Reflection.MemberInfo objects representing all members defined for the 
             current System.Type that match the specified binding constraints.-or- An empty array of type 
             System.Reflection.MemberInfo, if no members are defined for the current System.Type, or if none 
             of the defined members match the binding constraints.
        """
        pass

    def GetMethod(self, name, *__args):
        """
        GetMethod(self: _Type, name: str, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetMethod(System.String,System.Type[],System.Reflection.ParameterModifier[]) method.
        
        
            name: The System.String containing the name of the public method to get.
            types: An array of System.Type objects representing the number, order, and type of the parameters for 
             the method to get.-or- An empty array of the type System.Type (that is, Type[] types = new 
             Type[0]) to get a method that takes no parameters.
        
            modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 
             with the corresponding element in the types array. The default binder does not process this 
             parameter.
        
            Returns: A System.Reflection.MethodInfo object representing the public method that matches the specified 
             requirements, if found; otherwise, null.
        
        GetMethod(self: _Type, name: str, types: Array[Type]) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetMethod(System.String,System.Type[]) method.
        
        
            name: The System.String containing the name of the public method to get.
            types: An array of System.Type objects representing the number, order, and type of the parameters for 
             the method to get.-or- An empty array of the type System.Type (that is, Type[] types = new 
             Type[0]) to get a method that takes no parameters.
        
            Returns: A System.Reflection.MethodInfo object representing the public method whose parameters match the 
             specified argument types, if found; otherwise, null.
        
        GetMethod(self: _Type, name: str) -> MethodInfo
        
            Provides COM objects with version-independent access to the System.Type.GetMethod(System.String) 
             method.
        
        
            name: The System.String containing the name of the public method to get.
            Returns: A System.Reflection.MethodInfo object representing the public method with the specified name, if 
             found; otherwise, null.
        
        GetMethod(self: _Type, name: str, bindingAttr: BindingFlags, binder: Binder, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetMethod(System.String,System.Reflection.BindingFlags,System.Reflection.Binder,Syste
             m.Type[],System.Reflection.ParameterModifier[]) method.
        
        
            name: The System.String containing the name of the method to get.
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            binder: A System.Reflection.Binder object that defines a set of properties and enables binding, which 
             can involve selection of an overloaded method, coercion of argument types, and invocation of a 
             member through reflection.-or- null, to use the System.Type.DefaultBinder.
        
            types: An array of System.Type objects representing the number, order, and type of the parameters for 
             the method to get.-or- An empty array of the type System.Type (that is, Type[] types = new 
             Type[0]) to get a method that takes no parameters.
        
            modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 
             with the corresponding element in the types array. The default binder does not process this 
             parameter.
        
            Returns: A System.Reflection.MethodInfo object representing the method that matches the specified 
             requirements, if found; otherwise, null.
        
        GetMethod(self: _Type, name: str, bindingAttr: BindingFlags) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetMethod(System.String,System.Reflection.BindingFlags) method.
        
        
            name: The System.String containing the name of the method to get.
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            Returns: A System.Reflection.MethodInfo object representing the method that matches the specified 
             requirements, if found; otherwise, null.
        
        GetMethod(self: _Type, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetMethod(System.String,System.Reflection.BindingFlags,System.Reflection.Binder,Syste
             m.Reflection.CallingConventions,System.Type[],System.Reflection.ParameterModifier[]) method.
        
        
            name: The System.String containing the name of the method to get.
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            binder: A System.Reflection.Binder object that defines a set of properties and enables binding, which 
             can involve selection of an overloaded method, coercion of argument types, and invocation of a 
             member through reflection.-or- null, to use the System.Type.DefaultBinder.
        
            callConvention: The System.Reflection.CallingConventions object that specifies the set of rules to use regarding 
             the order and layout of arguments, how the return value is passed, what registers are used for 
             arguments, and how the stack is cleaned up.
        
            types: An array of System.Type objects representing the number, order, and type of the parameters for 
             the method to get.-or- An empty array of the type System.Type (that is, Type[] types = new 
             Type[0]) to get a method that takes no parameters.
        
            modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 
             with the corresponding element in the types array. The default binder does not process this 
             parameter.
        
            Returns: A System.Reflection.MethodInfo object representing the method that matches the specified 
             requirements, if found; otherwise, null.
        """
        pass

    def GetMethods(self, bindingAttr=None):
        """
        GetMethods(self: _Type) -> Array[MethodInfo]
        
            Provides COM objects with version-independent access to the System.Type.GetMethods method.
            Returns: An array of System.Reflection.MethodInfo objects representing all the public methods defined for 
             the current System.Type.-or- An empty array of type System.Reflection.MethodInfo, if no public 
             methods are defined for the current System.Type.
        
        GetMethods(self: _Type, bindingAttr: BindingFlags) -> Array[MethodInfo]
        
            Provides COM objects with version-independent access to the 
             System.Type.GetMethods(System.Reflection.BindingFlags) method.
        
        
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            Returns: An array of System.Reflection.MethodInfo objects representing all methods defined for the 
             current System.Type that match the specified binding constraints.-or- An empty array of type 
             System.Reflection.MethodInfo, if no methods are defined for the current System.Type, or if none 
             of the defined methods match the binding constraints.
        """
        pass

    def GetNestedType(self, name, bindingAttr=None):
        """
        GetNestedType(self: _Type, name: str) -> Type
        
            Provides COM objects with version-independent access to the 
             System.Type.GetNestedType(System.String) method.
        
        
            name: The string containing the name of the nested type to get.
            Returns: A System.Type object representing the public nested type with the specified name, if found; 
             otherwise, null.
        
        GetNestedType(self: _Type, name: str, bindingAttr: BindingFlags) -> Type
        
            Provides COM objects with version-independent access to the 
             System.Type.GetNestedType(System.String,System.Reflection.BindingFlags) method.
        
        
            name: The string containing the name of the nested type to get.
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            Returns: A System.Type object representing the nested type that matches the specified requirements, if 
             found; otherwise, null.
        """
        pass

    def GetNestedTypes(self, bindingAttr=None):
        """
        GetNestedTypes(self: _Type) -> Array[Type]
        
            Provides COM objects with version-independent access to the System.Type.GetNestedTypes method.
            Returns: An array of System.Type objects representing all the types nested within the current 
             System.Type.-or- An empty array of type System.Type, if no types are nested within the current 
             System.Type.
        
        GetNestedTypes(self: _Type, bindingAttr: BindingFlags) -> Array[Type]
        
            Provides COM objects with version-independent access to the 
             System.Type.GetNestedTypes(System.Reflection.BindingFlags) method, and searches for the types 
             nested within the current System.Type, using the specified binding constraints.
        
        
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            Returns: An array of System.Type objects representing all the types nested within the current System.Type 
             that match the specified binding constraints.-or- An empty array of type System.Type, if no 
             types are nested within the current System.Type, or if none of the nested types match the 
             binding constraints.
        """
        pass

    def GetProperties(self, bindingAttr=None):
        """
        GetProperties(self: _Type) -> Array[PropertyInfo]
        
            Provides COM objects with version-independent access to the System.Type.GetProperties method.
            Returns: An array of System.Reflection.PropertyInfo objects representing all public properties of the 
             current System.Type.-or- An empty array of type System.Reflection.PropertyInfo, if the current 
             System.Type does not have public properties.
        
        GetProperties(self: _Type, bindingAttr: BindingFlags) -> Array[PropertyInfo]
        
            Provides COM objects with version-independent access to the 
             System.Type.GetProperties(System.Reflection.BindingFlags) method.
        
        
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            Returns: An array of System.Reflection.PropertyInfo objects representing all properties of the current 
             System.Type that match the specified binding constraints.-or- An empty array of type 
             System.Reflection.PropertyInfo, if the current System.Type does not have properties, or if none 
             of the properties match the binding constraints.
        """
        pass

    def GetProperty(self, name, *__args):
        """
        GetProperty(self: _Type, name: str, types: Array[Type]) -> PropertyInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetProperty(System.String,System.Type[]) method.
        
        
            name: The System.String containing the name of the public property to get.
            types: An array of System.Type objects representing the number, order, and type of the parameters for 
             the indexed property to get.-or- An empty array of the type System.Type (that is, Type[] types = 
             new Type[0]) to get a property that is not indexed.
        
            Returns: A System.Reflection.PropertyInfo object representing the public property whose parameters match 
             the specified argument types, if found; otherwise, null.
        
        GetProperty(self: _Type, name: str, returnType: Type) -> PropertyInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetProperty(System.String,System.Type) method.
        
        
            name: The System.String containing the name of the public property to get.
            returnType: The return type of the property.
            Returns: A System.Reflection.PropertyInfo object representing the public property with the specified 
             name, if found; otherwise, null.
        
        GetProperty(self: _Type, name: str) -> PropertyInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetProperty(System.String) method.
        
        
            name: The System.String containing the name of the public property to get.
            Returns: A System.Reflection.PropertyInfo object representing the public property with the specified 
             name, if found; otherwise, null.
        
        GetProperty(self: _Type, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetProperty(System.String,System.Type,System.Type[]) method.
        
        
            name: The System.String containing the name of the public property to get.
            returnType: The return type of the property.
            types: An array of System.Type objects representing the number, order, and type of the parameters for 
             the indexed property to get.-or- An empty array of the type System.Type (that is, Type[] types = 
             new Type[0]) to get a property that is not indexed.
        
            Returns: A System.Reflection.PropertyInfo object representing the public property whose parameters match 
             the specified argument types, if found; otherwise, null.
        
        GetProperty(self: _Type, name: str, bindingAttr: BindingFlags) -> PropertyInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetProperty(System.String,System.Reflection.BindingFlags) method.
        
        
            name: The System.String containing the name of the property to get.
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            Returns: A System.Reflection.PropertyInfo object representing the property that matches the specified 
             requirements, if found; otherwise, null.
        
        GetProperty(self: _Type, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetProperty(System.String,System.Reflection.BindingFlags,System.Reflection.Binder,Sys
             tem.Type,System.Type[],System.Reflection.ParameterModifier[]) method.
        
        
            name: The System.String containing the name of the property to get.
            bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted.-or- Zero, to return null.
        
            binder: A System.Reflection.Binder object that defines a set of properties and enables binding, which 
             can involve selection of an overloaded method, coercion of argument types, and invocation of a 
             member through reflection.-or- null, to use the System.Type.DefaultBinder.
        
            returnType: The return type of the property.
            types: An array of System.Type objects representing the number, order, and type of the parameters for 
             the indexed property to get.-or- An empty array of the type System.Type (that is, Type[] types = 
             new Type[0]) to get a property that is not indexed.
        
            modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 
             with the corresponding element in the types array. The default binder does not process this 
             parameter.
        
            Returns: A System.Reflection.PropertyInfo object representing the property that matches the specified 
             requirements, if found; otherwise, null.
        
        GetProperty(self: _Type, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo
        
            Provides COM objects with version-independent access to the 
             System.Type.GetProperty(System.String,System.Type,System.Type[],System.Reflection.ParameterModifi
             er[]) method.
        
        
            name: The System.String containing the name of the public property to get.
            returnType: The return type of the property.
            types: An array of System.Type objects representing the number, order, and type of the parameters for 
             the indexed property to get.-or- An empty array of the type System.Type (that is, Type[] types = 
             new Type[0]) to get a property that is not indexed.
        
            modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 
             with the corresponding element in the types array. The default binder does not process this 
             parameter.
        
            Returns: A System.Reflection.PropertyInfo object representing the public property that matches the 
             specified requirements, if found; otherwise, null.
        """
        pass

    def GetType(self):
        """
        GetType(self: _Type) -> Type
        
            Provides COM objects with version-independent access to the System.Type.GetType method.
            Returns: The current System.Type.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _Type, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can then be used to get the type information 
             for an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: Receives a pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _Type) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _Type, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: Identifies the member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: Pointer to a structure containing an array of arguments, an array of argument DISPIDs for named 
             arguments, and counts for the number of elements in the arrays.
        
            pVarResult: Pointer to the location where the result is to be stored.
            pExcepInfo: Pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def InvokeMember(self, name, invokeAttr, binder, target, args, *__args):
        """
        InvokeMember(self: _Type, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object]) -> object
        
            Provides COM objects with version-independent access to the 
             System.Type.InvokeMember(System.String,System.Reflection.BindingFlags,System.Reflection.Binder,Sy
             stem.Object,System.Object[]) method.
        
        
            name: The System.String containing the name of the constructor, method, property, or field member to 
             invoke.-or- An empty string ("") to invoke the default member. -or-For IDispatch members, a 
             string representing the DispID, for example "[DispID=3]".
        
            invokeAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted. The access can be one of the BindingFlags such as Public, NonPublic, Private, 
             InvokeMethod, GetField, and so on. The type of lookup need not be specified. If the type of 
             lookup is omitted, BindingFlags.Public | BindingFlags.Instance will apply.
        
            binder: A System.Reflection.Binder object that defines a set of properties and enables binding, which 
             can involve selection of an overloaded method, coercion of argument types, and invocation of a 
             member through reflection.-or- null, to use the System.Type.DefaultBinder.
        
            target: The System.Object on which to invoke the specified member.
            args: An array containing the arguments to pass to the member to invoke.
            Returns: An System.Object representing the return value of the invoked member.
        InvokeMember(self: _Type, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object], culture: CultureInfo) -> object
        
            Provides COM objects with version-independent access to the 
             System.Type.InvokeMember(System.String,System.Reflection.BindingFlags,System.Reflection.Binder,Sy
             stem.Object,System.Object[],System.Globalization.CultureInfo) method.
        
        
            name: The System.String containing the name of the constructor, method, property, or field member to 
             invoke.-or- An empty string ("") to invoke the default member. -or-For IDispatch members, a 
             string representing the DispID, for example "[DispID=3]".
        
            invokeAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted. The access can be one of the BindingFlags such as Public, NonPublic, Private, 
             InvokeMethod, GetField, and so on. The type of lookup need not be specified. If the type of 
             lookup is omitted, BindingFlags.Public | BindingFlags.Instance will apply.
        
            binder: A System.Reflection.Binder object that defines a set of properties and enables binding, which 
             can involve selection of an overloaded method, coercion of argument types, and invocation of a 
             member through reflection.-or- null, to use the System.Type.DefaultBinder.
        
            target: The System.Object on which to invoke the specified member.
            args: An array containing the arguments to pass to the member to invoke.
            culture: The System.Globalization.CultureInfo object representing the globalization locale to use, which 
             may be necessary for locale-specific conversions, such as converting a numeric String to a 
             Double.-or- null to use the current thread's System.Globalization.CultureInfo.
        
            Returns: An System.Object representing the return value of the invoked member.
        InvokeMember(self: _Type, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object], modifiers: Array[ParameterModifier], culture: CultureInfo, namedParameters: Array[str]) -> object
        
            Provides COM objects with version-independent access to the 
             System.Type.InvokeMember(System.String,System.Reflection.BindingFlags,System.Reflection.Binder,Sy
             stem.Object,System.Object[],System.Reflection.ParameterModifier[],System.Globalization.CultureInf
             o,System.String[]) method.
        
        
            name: The System.String containing the name of the constructor, method, property, or field member to 
             invoke.-or- An empty string ("") to invoke the default member. -or-For IDispatch members, a 
             string representing the DispID, for example "[DispID=3]".
        
            invokeAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 
             conducted. The access can be one of the BindingFlags such as Public, NonPublic, Private, 
             InvokeMethod, GetField, and so on. The type of lookup need not be specified. If the type of 
             lookup is omitted, BindingFlags.Public | BindingFlags.Instance will apply.
        
            binder: A System.Reflection.Binder object that defines a set of properties and enables binding, which 
             can involve selection of an overloaded method, coercion of argument types, and invocation of a 
             member through reflection.-or- null, to use the System.Type.DefaultBinder.
        
            target: The System.Object on which to invoke the specified member.
            args: An array containing the arguments to pass to the member to invoke.
            modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 
             with the corresponding element in the args array. A parameter's associated attributes are stored 
             in the member's signature. The default binder does not process this parameter.
        
            culture: The System.Globalization.CultureInfo object representing the globalization locale to use, which 
             may be necessary for locale-specific conversions, such as converting a numeric String to a 
             Double.-or- null to use the current thread's System.Globalization.CultureInfo.
        
            namedParameters: An array containing the names of the parameters to which the values in the args array are passed.
            Returns: An System.Object representing the return value of the invoked member.
        """
        pass

    def IsAssignableFrom(self, c):
        """
        IsAssignableFrom(self: _Type, c: Type) -> bool
        
            Provides COM objects with version-independent access to the 
             System.Type.IsAssignableFrom(System.Type) method.
        
        
            c: The System.Type to compare with the current System.Type.
            Returns: true if c and the current System.Type represent the same type, or if the current System.Type is 
             in the inheritance hierarchy of c, or if the current System.Type is an interface that c 
             implements, or if c is a generic type parameter and the current System.Type represents one of 
             the constraints of c. false if none of these conditions are the case, or if c is null.
        """
        pass

    def IsDefined(self, attributeType, inherit):
        """
        IsDefined(self: _Type, attributeType: Type, inherit: bool) -> bool
        
            Provides COM objects with version-independent access to the 
             System.Reflection.MemberInfo.IsDefined(System.Type,System.Boolean) method.
        
        
            attributeType: The Type object to which the custom attributes are applied.
            inherit: Specifies whether to search this member's inheritance chain to find the attributes.
            Returns: true if one or more instance of attributeType is applied to this member; otherwise, false.
        """
        pass

    def IsInstanceOfType(self, o):
        """
        IsInstanceOfType(self: _Type, o: object) -> bool
        
            Provides COM objects with version-independent access to the 
             System.Type.IsInstanceOfType(System.Object) method.
        
        
            o: The object to compare with the current System.Type.
            Returns: true if the current System.Type is in the inheritance hierarchy of the object represented by o, 
             or if the current System.Type is an interface that o supports. false if neither of these 
             conditions is the case, or if o is null, or if the current System.Type is an open generic type 
             (that is, System.Type.ContainsGenericParameters returns true).
        """
        pass

    def IsSubclassOf(self, c):
        """
        IsSubclassOf(self: _Type, c: Type) -> bool
        
            Provides COM objects with version-independent access to the 
             System.Type.IsSubclassOf(System.Type) method.
        
        
            c: The System.Type to compare with the current System.Type.
            Returns: true if the System.Type represented by the c parameter and the current System.Type represent 
             classes, and the class represented by the current System.Type derives from the class represented 
             by c; otherwise, false. This method also returns false if c and the current System.Type 
             represent the same class.
        """
        pass

    def ToString(self):
        """
        ToString(self: _Type) -> str
        
            Provides COM objects with version-independent access to the System.Type.ToString method.
            Returns: A System.String representing the name of the current System.Type.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Assembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.Assembly property.

Get: Assembly(self: _Type) -> Assembly

"""

    AssemblyQualifiedName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.AssemblyQualifiedName property.

Get: AssemblyQualifiedName(self: _Type) -> str

"""

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.Attributes property.

Get: Attributes(self: _Type) -> TypeAttributes

"""

    BaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.BaseType property.

Get: BaseType(self: _Type) -> Type

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.DeclaringType property.

Get: DeclaringType(self: _Type) -> Type

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.FullName property.

Get: FullName(self: _Type) -> str

"""

    GUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.GUID property.

Get: GUID(self: _Type) -> Guid

"""

    HasElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.HasElementType property.

Get: HasElementType(self: _Type) -> bool

"""

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsAbstract property.

Get: IsAbstract(self: _Type) -> bool

"""

    IsAnsiClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsAnsiClass property.

Get: IsAnsiClass(self: _Type) -> bool

"""

    IsArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsArray property.

Get: IsArray(self: _Type) -> bool

"""

    IsAutoClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsAutoClass property.

Get: IsAutoClass(self: _Type) -> bool

"""

    IsAutoLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsAutoLayout property.

Get: IsAutoLayout(self: _Type) -> bool

"""

    IsByRef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsByRef property.

Get: IsByRef(self: _Type) -> bool

"""

    IsClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsClass property.

Get: IsClass(self: _Type) -> bool

"""

    IsCOMObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsCOMObject property.

Get: IsCOMObject(self: _Type) -> bool

"""

    IsContextful = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsContextful property.

Get: IsContextful(self: _Type) -> bool

"""

    IsEnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsEnum property.

Get: IsEnum(self: _Type) -> bool

"""

    IsExplicitLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsExplicitLayout property.

Get: IsExplicitLayout(self: _Type) -> bool

"""

    IsImport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsImport property.

Get: IsImport(self: _Type) -> bool

"""

    IsInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsInterface property.

Get: IsInterface(self: _Type) -> bool

"""

    IsLayoutSequential = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsLayoutSequential property.

Get: IsLayoutSequential(self: _Type) -> bool

"""

    IsMarshalByRef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsMarshalByRef property.

Get: IsMarshalByRef(self: _Type) -> bool

"""

    IsNestedAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsNestedAssembly property.

Get: IsNestedAssembly(self: _Type) -> bool

"""

    IsNestedFamANDAssem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsNestedFamANDAssem property.

Get: IsNestedFamANDAssem(self: _Type) -> bool

"""

    IsNestedFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsNestedFamily property.

Get: IsNestedFamily(self: _Type) -> bool

"""

    IsNestedFamORAssem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsNestedFamORAssem property.

Get: IsNestedFamORAssem(self: _Type) -> bool

"""

    IsNestedPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsNestedPrivate property.

Get: IsNestedPrivate(self: _Type) -> bool

"""

    IsNestedPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsNestedPublic property.

Get: IsNestedPublic(self: _Type) -> bool

"""

    IsNotPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsNotPublic property.

Get: IsNotPublic(self: _Type) -> bool

"""

    IsPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsPointer property.

Get: IsPointer(self: _Type) -> bool

"""

    IsPrimitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsPrimitive property.

Get: IsPrimitive(self: _Type) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsPublic property.

Get: IsPublic(self: _Type) -> bool

"""

    IsSealed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsSealed property.

Get: IsSealed(self: _Type) -> bool

"""

    IsSerializable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsSerializable property.

Get: IsSerializable(self: _Type) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsSpecialName property.

Get: IsSpecialName(self: _Type) -> bool

"""

    IsUnicodeClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsUnicodeClass property.

Get: IsUnicodeClass(self: _Type) -> bool

"""

    IsValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.IsValueType property.

Get: IsValueType(self: _Type) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.MemberType property.

Get: MemberType(self: _Type) -> MemberTypes

"""

    Module = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.Module property.

Get: Module(self: _Type) -> Module

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.Name property.

Get: Name(self: _Type) -> str

"""

    Namespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.Namespace property.

Get: Namespace(self: _Type) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.ReflectedType property.

Get: ReflectedType(self: _Type) -> Type

"""

    TypeHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.TypeHandle property.

Get: TypeHandle(self: _Type) -> RuntimeTypeHandle

"""

    TypeInitializer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.TypeInitializer property.

Get: TypeInitializer(self: _Type) -> ConstructorInfo

"""

    UnderlyingSystemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides COM objects with version-independent access to the System.Type.UnderlyingSystemType property.

Get: UnderlyingSystemType(self: _Type) -> Type

"""



class _TypeBuilder:
    """ Exposes the System.Reflection.Emit.TypeBuilder class to unmanaged code. """
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """
        GetIDsOfNames(self: _TypeBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid
        
            Maps a set of names to a corresponding set of dispatch identifiers.
        
            riid: Reserved for future use. Must be IID_NULL.
            rgszNames: An array of names to be mapped.
            cNames: The count of the names to be mapped.
            lcid: The locale context in which to interpret the names.
            rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
        """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """
        GetTypeInfo(self: _TypeBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr)
            Retrieves the type information for an object, which can be used to get the type information for 
             an interface.
        
        
            iTInfo: The type information to return.
            lcid: The locale identifier for the type information.
            ppTInfo: A pointer to the requested type information object.
        """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """
        GetTypeInfoCount(self: _TypeBuilder) -> UInt32
        
            Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """
        Invoke(self: _TypeBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        
            Provides access to properties and methods exposed by an object.
        
            dispIdMember: An identifier of a member.
            riid: Reserved for future use. Must be IID_NULL.
            lcid: The locale context in which to interpret arguments.
            wFlags: Flags describing the context of the call.
            pDispParams: A pointer to a structure containing an array of arguments, an array of argument DISPIDs for 
             named arguments, and counts for the number of elements in the arrays.
        
            pVarResult: A pointer to the location where the result will be stored.
            pExcepInfo: A pointer to a structure that contains exception information.
            puArgErr: The index of the first argument that has an error.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


# variables with complex values

