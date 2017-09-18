# encoding: utf-8
# module System.Security.Authentication.ExtendedProtection calls itself ExtendedProtection
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ChannelBinding(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """ The System.Security.Authentication.ExtendedProtection.ChannelBinding class encapsulates a pointer to the opaque data used to bind an authenticated transaction to a secure channel. """
    def Dispose(self):
        """
        Dispose(self: SafeHandle, disposing: bool)
            Releases the unmanaged resources used by the System.Runtime.InteropServices.SafeHandle class 
             specifying whether to perform a normal dispose operation.
        
        
            disposing: true for a normal dispose operation; false to finalize the handle.
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
        """
        __new__(cls: type)
        __new__(cls: type, ownsHandle: bool)
        """
        pass

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The System.Security.Authentication.ExtendedProtection.ChannelBinding.Size property gets the size, in bytes, of the channel binding token associated with the System.Security.Authentication.ExtendedProtection.ChannelBinding instance.

Get: Size(self: ChannelBinding) -> int

"""


    handle = None


class ChannelBindingKind(Enum, IComparable, IFormattable, IConvertible):
    """
    The System.Security.Authentication.ExtendedProtection.ChannelBindingKind enumeration represents the kinds of channel bindings that can be queried from secure channels.
    
    enum ChannelBindingKind, values: Endpoint (26), Unique (25), Unknown (0)
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

    Endpoint = None
    Unique = None
    Unknown = None
    value__ = None


class ExtendedProtectionPolicy(object, ISerializable):
    """
    The System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy class represents the extended protection policy used by the server to validate incoming client connections.
    
    ExtendedProtectionPolicy(policyEnforcement: PolicyEnforcement, protectionScenario: ProtectionScenario, customServiceNames: ServiceNameCollection)
    ExtendedProtectionPolicy(policyEnforcement: PolicyEnforcement, protectionScenario: ProtectionScenario, customServiceNames: ICollection)
    ExtendedProtectionPolicy(policyEnforcement: PolicyEnforcement, customChannelBinding: ChannelBinding)
    ExtendedProtectionPolicy(policyEnforcement: PolicyEnforcement)
    """
    def ToString(self):
        """
        ToString(self: ExtendedProtectionPolicy) -> str
        
            Gets a string representation for the extended protection policy instance.
            Returns: A System.String instance that contains the representation of the 
             System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy instance.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, policyEnforcement, *__args):
        """
        __new__(cls: type, policyEnforcement: PolicyEnforcement, protectionScenario: ProtectionScenario, customServiceNames: ServiceNameCollection)
        __new__(cls: type, policyEnforcement: PolicyEnforcement, protectionScenario: ProtectionScenario, customServiceNames: ICollection)
        __new__(cls: type, policyEnforcement: PolicyEnforcement, customChannelBinding: ChannelBinding)
        __new__(cls: type, policyEnforcement: PolicyEnforcement)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CustomChannelBinding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a custom channel binding token (CBT) to use for validation.

Get: CustomChannelBinding(self: ExtendedProtectionPolicy) -> ChannelBinding

"""

    CustomServiceNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the custom Service Provider Name (SPN) list used to match against a client's SPN.

Get: CustomServiceNames(self: ExtendedProtectionPolicy) -> ServiceNameCollection

"""

    PolicyEnforcement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets when the extended protection policy should be enforced.

Get: PolicyEnforcement(self: ExtendedProtectionPolicy) -> PolicyEnforcement

"""

    ProtectionScenario = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the kind of protection enforced by the extended protection policy.

Get: ProtectionScenario(self: ExtendedProtectionPolicy) -> ProtectionScenario

"""


    OSSupportsExtendedProtection = True


class ExtendedProtectionPolicyTypeConverter(TypeConverter):
    """
    The System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicyTypeConverter class represents the type converter for extended protection policy used by the server to validate incoming client connections.
    
    ExtendedProtectionPolicyTypeConverter()
    """
    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: ExtendedProtectionPolicyTypeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Returns whether this converter can convert the object to the specified type.
        
            context: The object to convert.
            destinationType: A System.Type that represents the type you want to convert to.
            Returns: true if this converter can perform the conversion; otherwise false.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: ExtendedProtectionPolicyTypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Convert the object to the specified type
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: A System.Globalization.CultureInfo object. If null is passed, the current culture is assumed.
            value: The System.Object to convert. This should be a 
             System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy object.
        
            destinationType: The System.Type to convert the value parameter to.
            Returns: An System.Object that represents the converted value parameter.
        """
        pass


class PolicyEnforcement(Enum, IComparable, IFormattable, IConvertible):
    """
    The System.Security.Authentication.ExtendedProtection.PolicyEnforcement enumeration specifies when the System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy should be enforced.
    
    enum PolicyEnforcement, values: Always (2), Never (0), WhenSupported (1)
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

    Always = None
    Never = None
    value__ = None
    WhenSupported = None


class ProtectionScenario(Enum, IComparable, IFormattable, IConvertible):
    """
    The System.Security.Authentication.ExtendedProtection.ProtectionScenario enumeration specifies the protection scenario enforced by the policy.
    
    enum ProtectionScenario, values: TransportSelected (0), TrustedProxy (1)
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

    TransportSelected = None
    TrustedProxy = None
    value__ = None


class ServiceNameCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """
    The System.Security.Authentication.ExtendedProtection.ServiceNameCollection class is a read-only collection of service principal names.
    
    ServiceNameCollection(items: ICollection)
    """
    def Contains(self, searchServiceName):
        """ Contains(self: ServiceNameCollection, searchServiceName: str) -> bool """
        pass

    def Merge(self, *__args):
        """
        Merge(self: ServiceNameCollection, serviceNames: IEnumerable) -> ServiceNameCollection
        
            Merges the current System.Security.Authentication.ExtendedProtection.ServiceNameCollection with 
             the specified values to create a new 
             System.Security.Authentication.ExtendedProtection.ServiceNameCollection containing the union.
        
        
            serviceNames: An instance of the System.Collections.IEnumerable class that contains the specified values of 
             service names to be merged.
        
            Returns: A new System.Security.Authentication.ExtendedProtection.ServiceNameCollection instance that 
             contains the union of the existing 
             System.Security.Authentication.ExtendedProtection.ServiceNameCollection instance merged with the 
             specified values.
        
        Merge(self: ServiceNameCollection, serviceName: str) -> ServiceNameCollection
        
            Merges the current System.Security.Authentication.ExtendedProtection.ServiceNameCollection with 
             the specified values to create a new 
             System.Security.Authentication.ExtendedProtection.ServiceNameCollection containing the union.
        
        
            serviceName: A string that contains the specified values of service names to be used to initialize the class.
            Returns: A new System.Security.Authentication.ExtendedProtection.ServiceNameCollection instance that 
             contains the union of the existing 
             System.Security.Authentication.ExtendedProtection.ServiceNameCollection instance merged with the 
             specified values.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, items):
        """ __new__(cls: type, items: ICollection) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance.

"""



class TokenBinding(object):
    # no doc
    def GetRawTokenBindingId(self):
        """ GetRawTokenBindingId(self: TokenBinding) -> Array[Byte] """
        pass

    BindingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BindingType(self: TokenBinding) -> TokenBindingType

"""



class TokenBindingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum TokenBindingType, values: Provided (0), Referred (1) """
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

    Provided = None
    Referred = None
    value__ = None


# variables with complex values

