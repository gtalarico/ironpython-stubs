# encoding: utf-8
# module Microsoft.Win32 calls itself Win32
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class IntranetZoneCredentialPolicy(object, ICredentialPolicy):
    """
    Defines a credential policy to be used for resource requests that are made using System.Net.WebRequest and its derived classes.
    
    IntranetZoneCredentialPolicy()
    """
    def ShouldSendCredential(self, challengeUri, request, credential, authModule):
        """
        ShouldSendCredential(self: IntranetZoneCredentialPolicy, challengeUri: Uri, request: WebRequest, credential: NetworkCredential, authModule: IAuthenticationModule) -> bool
        
            Returns a System.Boolean that indicates whether the client's credentials are sent with a request 
             for a resource that was made using System.Net.WebRequest.
        
        
            challengeUri: The System.Uri that will receive the request.
            request: The System.Net.WebRequest that represents the resource being requested.
            credential: The System.Net.NetworkCredential that will be sent with the request if this method returns true.
            authModule: The System.Net.IAuthenticationModule that will conduct the authentication, if authentication is 
             required.
        
            Returns: true if the requested resource is in the same domain as the client making the request; 
             otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class PowerModeChangedEventArgs(EventArgs):
    """
    Provides data for the Microsoft.Win32.SystemEvents.PowerModeChanged event.
    
    PowerModeChangedEventArgs(mode: PowerModes)
    """
    @staticmethod # known case of __new__
    def __new__(self, mode):
        """ __new__(cls: type, mode: PowerModes) """
        pass

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an identifier that indicates the type of the power mode event that has occurred.

Get: Mode(self: PowerModeChangedEventArgs) -> PowerModes

"""



class PowerModeChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the Microsoft.Win32.SystemEvents.PowerModeChanged event.
    
    PowerModeChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: PowerModeChangedEventHandler, sender: object, e: PowerModeChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: PowerModeChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PowerModeChangedEventHandler, sender: object, e: PowerModeChangedEventArgs) """
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


class PowerModes(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers for power mode events reported by the operating system.
    
    enum PowerModes, values: Resume (1), StatusChange (2), Suspend (3)
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

    Resume = None
    StatusChange = None
    Suspend = None
    value__ = None


class Registry(object):
    """ Provides Microsoft.Win32.RegistryKey objects that represent the root keys in the Windows registry, and static methods to access key/value pairs. """
    @staticmethod
    def GetValue(keyName, valueName, defaultValue):
        """
        GetValue(keyName: str, valueName: str, defaultValue: object) -> object
        
            Retrieves the value associated with the specified name, in the specified registry key. If the 
             name is not found in the specified key, returns a default value that you provide, or null if the 
             specified key does not exist.
        
        
            keyName: The full registry path of the key, beginning with a valid registry root, such as 
             "HKEY_CURRENT_USER".
        
            valueName: The name of the name/value pair.
            defaultValue: The value to return if valueName does not exist.
            Returns: null if the subkey specified by keyName does not exist; otherwise, the value associated with 
             valueName, or defaultValue if valueName is not found.
        """
        pass

    @staticmethod
    def SetValue(keyName, valueName, value, valueKind=None):
        """
        SetValue(keyName: str, valueName: str, value: object, valueKind: RegistryValueKind)
            Sets the name/value pair on the specified registry key, using the specified registry data type. 
             If the specified key does not exist, it is created.
        
        
            keyName: The full registry path of the key, beginning with a valid registry root, such as 
             "HKEY_CURRENT_USER".
        
            valueName: The name of the name/value pair.
            value: The value to be stored.
            valueKind: The registry data type to use when storing the data.
        SetValue(keyName: str, valueName: str, value: object)
            Sets the specified name/value pair on the specified registry key. If the specified key does not 
             exist, it is created.
        
        
            keyName: The full registry path of the key, beginning with a valid registry root, such as 
             "HKEY_CURRENT_USER".
        
            valueName: The name of the name/value pair.
            value: The value to be stored.
        """
        pass

    ClassesRoot = None
    CurrentConfig = None
    CurrentUser = None
    DynData = None
    LocalMachine = None
    PerformanceData = None
    Users = None
    __all__ = [
        'ClassesRoot',
        'CurrentConfig',
        'CurrentUser',
        'DynData',
        'GetValue',
        'LocalMachine',
        'PerformanceData',
        'SetValue',
        'Users',
    ]


class RegistryHive(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents the possible values for a top-level node on a foreign machine.
    
    enum RegistryHive, values: ClassesRoot (-2147483648), CurrentConfig (-2147483643), CurrentUser (-2147483647), DynData (-2147483642), LocalMachine (-2147483646), PerformanceData (-2147483644), Users (-2147483645)
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

    ClassesRoot = None
    CurrentConfig = None
    CurrentUser = None
    DynData = None
    LocalMachine = None
    PerformanceData = None
    Users = None
    value__ = None


class RegistryKey(MarshalByRefObject, IDisposable):
    """ Represents a key-level node in the Windows registry. This class is a registry encapsulation. """
    def Close(self):
        """
        Close(self: RegistryKey)
            Closes the key and flushes it to disk if its contents have been modified.
        """
        pass

    def CreateSubKey(self, subkey, *__args):
        """
        CreateSubKey(self: RegistryKey, subkey: str, writable: bool, options: RegistryOptions) -> RegistryKey
        CreateSubKey(self: RegistryKey, subkey: str, permissionCheck: RegistryKeyPermissionCheck, registrySecurity: RegistrySecurity) -> RegistryKey
        
            Creates a new subkey or opens an existing subkey for write access, using the specified 
             permission check option and registry security.
        
        
            subkey: The name or path of the subkey to create or open. This string is not case-sensitive.
            permissionCheck: One of the enumeration values that specifies whether the key is opened for read or read/write 
             access.
        
            registrySecurity: The access control security for the new key.
            Returns: The newly created subkey, or null if the operation failed. If a zero-length string is specified 
             for subkey, the current Microsoft.Win32.RegistryKey object is returned.
        
        CreateSubKey(self: RegistryKey, subkey: str, permissionCheck: RegistryKeyPermissionCheck, registryOptions: RegistryOptions, registrySecurity: RegistrySecurity) -> RegistryKey
        
            Creates a subkey or opens a subkey for write access, using the specified permission check 
             option, registry option, and registry security.
        
        
            subkey: The name or path of the subkey to create or open.
            permissionCheck: One of the enumeration values that specifies whether the key is opened for read or read/write 
             access.
        
            registryOptions: The registry option to use.
            registrySecurity: The access control security for the new subkey.
            Returns: The newly created subkey, or null if the operation failed.
        CreateSubKey(self: RegistryKey, subkey: str, writable: bool) -> RegistryKey
        CreateSubKey(self: RegistryKey, subkey: str) -> RegistryKey
        
            Creates a new subkey or opens an existing subkey for write access.
        
            subkey: The name or path of the subkey to create or open. This string is not case-sensitive.
            Returns: The newly created subkey, or null if the operation failed. If a zero-length string is specified 
             for subkey, the current Microsoft.Win32.RegistryKey object is returned.
        
        CreateSubKey(self: RegistryKey, subkey: str, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey
        
            Creates a new subkey or opens an existing subkey for write access, using the specified 
             permission check option.
        
        
            subkey: The name or path of the subkey to create or open. This string is not case-sensitive.
            permissionCheck: One of the enumeration values that specifies whether the key is opened for read or read/write 
             access.
        
            Returns: The newly created subkey, or null if the operation failed. If a zero-length string is specified 
             for subkey, the current Microsoft.Win32.RegistryKey object is returned.
        
        CreateSubKey(self: RegistryKey, subkey: str, permissionCheck: RegistryKeyPermissionCheck, options: RegistryOptions) -> RegistryKey
        
            Creates a subkey or opens a subkey for write access, using the specified permission check and 
             registry options.
        
        
            subkey: The name or path of the subkey to create or open.
            permissionCheck: One of the enumeration values that specifies whether the key is opened for read or read/write 
             access.
        
            options: The registry option to use; for example, that creates a volatile key.
            Returns: The newly created subkey, or null if the operation failed.
        """
        pass

    def DeleteSubKey(self, subkey, throwOnMissingSubKey=None):
        """
        DeleteSubKey(self: RegistryKey, subkey: str, throwOnMissingSubKey: bool)
            Deletes the specified subkey, and specifies whether an exception is raised if the subkey is not 
             found.
        
        
            subkey: The name of the subkey to delete. This string is not case-sensitive.
            throwOnMissingSubKey: Indicates whether an exception should be raised if the specified subkey cannot be found. If this 
             argument is true and the specified subkey does not exist, an exception is raised. If this 
             argument is false and the specified subkey does not exist, no action is taken.
        
        DeleteSubKey(self: RegistryKey, subkey: str)
            Deletes the specified subkey.
        
            subkey: The name of the subkey to delete. This string is not case-sensitive.
        """
        pass

    def DeleteSubKeyTree(self, subkey, throwOnMissingSubKey=None):
        """
        DeleteSubKeyTree(self: RegistryKey, subkey: str, throwOnMissingSubKey: bool)
            Deletes the specified subkey and any child subkeys recursively, and specifies whether an 
             exception is raised if the subkey is not found.
        
        
            subkey: The name of the subkey to delete. This string is not case-sensitive.
            throwOnMissingSubKey: Indicates whether an exception should be raised if the specified subkey cannot be found. If this 
             argument is true and the specified subkey does not exist, an exception is raised. If this 
             argument is false and the specified subkey does not exist, no action is taken.
        
        DeleteSubKeyTree(self: RegistryKey, subkey: str)
            Deletes a subkey and any child subkeys recursively.
        
            subkey: The subkey to delete. This string is not case-sensitive.
        """
        pass

    def DeleteValue(self, name, throwOnMissingValue=None):
        """
        DeleteValue(self: RegistryKey, name: str, throwOnMissingValue: bool)
            Deletes the specified value from this key, and specifies whether an exception is raised if the 
             value is not found.
        
        
            name: The name of the value to delete.
            throwOnMissingValue: Indicates whether an exception should be raised if the specified value cannot be found. If this 
             argument is true and the specified value does not exist, an exception is raised. If this 
             argument is false and the specified value does not exist, no action is taken.
        
        DeleteValue(self: RegistryKey, name: str)
            Deletes the specified value from this key.
        
            name: The name of the value to delete.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: RegistryKey)
            Releases all resources used by the current instance of the Microsoft.Win32.RegistryKey class.
        """
        pass

    def Flush(self):
        """
        Flush(self: RegistryKey)
            Writes all the attributes of the specified open registry key into the registry.
        """
        pass

    @staticmethod
    def FromHandle(handle, view=None):
        """
        FromHandle(handle: SafeRegistryHandle, view: RegistryView) -> RegistryKey
        
            Creates a registry key from a specified handle and registry view setting.
        
            handle: The handle to the registry key.
            view: The registry view to use.
            Returns: A registry key.
        FromHandle(handle: SafeRegistryHandle) -> RegistryKey
        
            Creates a registry key from a specified handle.
        
            handle: The handle to the registry key.
            Returns: A registry key.
        """
        pass

    def GetAccessControl(self, includeSections=None):
        """
        GetAccessControl(self: RegistryKey, includeSections: AccessControlSections) -> RegistrySecurity
        
            Returns the specified sections of the access control security for the current registry key.
        
            includeSections: A bitwise combination of enumeration values that specifies the type of security information to 
             get.
        
            Returns: An object that describes the access control permissions on the registry key represented by the 
             current Microsoft.Win32.RegistryKey.
        
        GetAccessControl(self: RegistryKey) -> RegistrySecurity
        
            Returns the access control security for the current registry key.
            Returns: An object that describes the access control permissions on the registry key represented by the 
             current Microsoft.Win32.RegistryKey.
        """
        pass

    def GetSubKeyNames(self):
        """
        GetSubKeyNames(self: RegistryKey) -> Array[str]
        
            Retrieves an array of strings that contains all the subkey names.
            Returns: An array of strings that contains the names of the subkeys for the current key.
        """
        pass

    def GetValue(self, name, defaultValue=None, options=None):
        """
        GetValue(self: RegistryKey, name: str, defaultValue: object, options: RegistryValueOptions) -> object
        
            Retrieves the value associated with the specified name and retrieval options. If the name is not 
             found, returns the default value that you provide.
        
        
            name: The name of the value to retrieve. This string is not case-sensitive.
            defaultValue: The value to return if name does not exist.
            options: One of the enumeration values that specifies optional processing of the retrieved value.
            Returns: The value associated with name, processed according to the specified options, or defaultValue if 
             name is not found.
        
        GetValue(self: RegistryKey, name: str, defaultValue: object) -> object
        
            Retrieves the value associated with the specified name. If the name is not found, returns the 
             default value that you provide.
        
        
            name: The name of the value to retrieve. This string is not case-sensitive.
            defaultValue: The value to return if name does not exist.
            Returns: The value associated with name, with any embedded environment variables left unexpanded, or 
             defaultValue if name is not found.
        
        GetValue(self: RegistryKey, name: str) -> object
        
            Retrieves the value associated with the specified name. Returns null if the name/value pair does 
             not exist in the registry.
        
        
            name: The name of the value to retrieve. This string is not case-sensitive.
            Returns: The value associated with name, or null if name is not found.
        """
        pass

    def GetValueKind(self, name):
        """
        GetValueKind(self: RegistryKey, name: str) -> RegistryValueKind
        
            Retrieves the registry data type of the value associated with the specified name.
        
            name: The name of the value whose registry data type is to be retrieved. This string is not 
             case-sensitive.
        
            Returns: The registry data type of the value associated with name.
        """
        pass

    def GetValueNames(self):
        """
        GetValueNames(self: RegistryKey) -> Array[str]
        
            Retrieves an array of strings that contains all the value names associated with this key.
            Returns: An array of strings that contains the value names for the current key.
        """
        pass

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

    @staticmethod
    def OpenBaseKey(hKey, view):
        """
        OpenBaseKey(hKey: RegistryHive, view: RegistryView) -> RegistryKey
        
            Opens a new Microsoft.Win32.RegistryKey that represents the requested key on the local machine 
             with the specified view.
        
        
            hKey: The HKEY to open.
            view: The registry view to use.
            Returns: The requested registry key.
        """
        pass

    @staticmethod
    def OpenRemoteBaseKey(hKey, machineName, view=None):
        """
        OpenRemoteBaseKey(hKey: RegistryHive, machineName: str, view: RegistryView) -> RegistryKey
        
            Opens a new registry key that represents the requested key on a remote machine with the 
             specified view.
        
        
            hKey: The HKEY to open from the Microsoft.Win32.RegistryHive enumeration..
            machineName: The remote machine.
            view: The registry view to use.
            Returns: The requested registry key.
        OpenRemoteBaseKey(hKey: RegistryHive, machineName: str) -> RegistryKey
        
            Opens a new Microsoft.Win32.RegistryKey that represents the requested key on a remote machine.
        
            hKey: The HKEY to open, from the Microsoft.Win32.RegistryHive enumeration.
            machineName: The remote machine.
            Returns: The requested registry key.
        """
        pass

    def OpenSubKey(self, name, *__args):
        """
        OpenSubKey(self: RegistryKey, name: str, permissionCheck: RegistryKeyPermissionCheck, rights: RegistryRights) -> RegistryKey
        
            Retrieves the specified subkey for read or read/write access, requesting the specified access 
             rights.
        
        
            name: The name or path of the subkey to create or open.
            permissionCheck: One of the enumeration values that specifies whether the key is opened for read or read/write 
             access.
        
            rights: A bitwise combination of enumeration values that specifies the desired security access.
            Returns: The subkey requested, or null if the operation failed.
        OpenSubKey(self: RegistryKey, name: str) -> RegistryKey
        
            Retrieves a subkey as read-only.
        
            name: The name or path of the subkey to open as read-only.
            Returns: The subkey requested, or null if the operation failed.
        OpenSubKey(self: RegistryKey, name: str, rights: RegistryRights) -> RegistryKey
        OpenSubKey(self: RegistryKey, name: str, writable: bool) -> RegistryKey
        
            Retrieves a specified subkey, and specifies whether write access is to be applied to the key.
        
            name: Name or path of the subkey to open.
            writable: Set to true if you need write access to the key.
            Returns: The subkey requested, or null if the operation failed.
        OpenSubKey(self: RegistryKey, name: str, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey
        
            Retrieves the specified subkey for read or read/write access.
        
            name: The name or path of the subkey to create or open.
            permissionCheck: One of the enumeration values that specifies whether the key is opened for read or read/write 
             access.
        
            Returns: The subkey requested, or null if the operation failed.
        """
        pass

    def SetAccessControl(self, registrySecurity):
        """
        SetAccessControl(self: RegistryKey, registrySecurity: RegistrySecurity)
            Applies Windows access control security to an existing registry key.
        
            registrySecurity: The access control security to apply to the current subkey.
        """
        pass

    def SetValue(self, name, value, valueKind=None):
        """
        SetValue(self: RegistryKey, name: str, value: object, valueKind: RegistryValueKind)
            Sets the value of a name/value pair in the registry key, using the specified registry data type.
        
            name: The name of the value to be stored.
            value: The data to be stored.
            valueKind: The registry data type to use when storing the data.
        SetValue(self: RegistryKey, name: str, value: object)
            Sets the specified name/value pair.
        
            name: The name of the value to store.
            value: The data to be stored.
        """
        pass

    def ToString(self):
        """
        ToString(self: RegistryKey) -> str
        
            Retrieves a string representation of this key.
            Returns: A string representing the key. If the specified key is invalid (cannot be found) then null is 
             returned.
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

    def __str__(self, *args): #cannot find CLR method
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Microsoft.Win32.SafeHandles.SafeRegistryHandle object that represents the registry key that the current Microsoft.Win32.RegistryKey object encapsulates.

Get: Handle(self: RegistryKey) -> SafeRegistryHandle

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the name of the key.

Get: Name(self: RegistryKey) -> str

"""

    SubKeyCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the count of subkeys of the current key.

Get: SubKeyCount(self: RegistryKey) -> int

"""

    ValueCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the count of values in the key.

Get: ValueCount(self: RegistryKey) -> int

"""

    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the view that was used to create the registry key.

Get: View(self: RegistryKey) -> RegistryView

"""



class RegistryKeyPermissionCheck(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies whether security checks are performed when opening registry keys and accessing their name/value pairs.
    
    enum RegistryKeyPermissionCheck, values: Default (0), ReadSubTree (1), ReadWriteSubTree (2)
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

    Default = None
    ReadSubTree = None
    ReadWriteSubTree = None
    value__ = None


class RegistryOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies options to use when creating a registry key.
    
    enum (flags) RegistryOptions, values: None (0), Volatile (1)
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
    value__ = None
    Volatile = None


class RegistryValueKind(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the data types to use when storing values in the registry, or identifies the data type of a value in the registry.
    
    enum RegistryValueKind, values: Binary (3), DWord (4), ExpandString (2), MultiString (7), None (-1), QWord (11), String (1), Unknown (0)
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

    Binary = None
    DWord = None
    ExpandString = None
    MultiString = None
    None = None
    QWord = None
    String = None
    Unknown = None
    value__ = None


class RegistryValueOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies optional behavior when retrieving name/value pairs from a registry key.
    
    enum (flags) RegistryValueOptions, values: DoNotExpandEnvironmentNames (1), None (0)
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

    DoNotExpandEnvironmentNames = None
    None = None
    value__ = None


class RegistryView(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies which registry view to target on a 64-bit operating system.
    
    enum RegistryView, values: Default (0), Registry32 (512), Registry64 (256)
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

    Default = None
    Registry32 = None
    Registry64 = None
    value__ = None


class SessionEndedEventArgs(EventArgs):
    """
    Provides data for the Microsoft.Win32.SystemEvents.SessionEnded event.
    
    SessionEndedEventArgs(reason: SessionEndReasons)
    """
    @staticmethod # known case of __new__
    def __new__(self, reason):
        """ __new__(cls: type, reason: SessionEndReasons) """
        pass

    Reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an identifier that indicates how the session ended.

Get: Reason(self: SessionEndedEventArgs) -> SessionEndReasons

"""



class SessionEndedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the Microsoft.Win32.SystemEvents.SessionEnded event.
    
    SessionEndedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: SessionEndedEventHandler, sender: object, e: SessionEndedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: SessionEndedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SessionEndedEventHandler, sender: object, e: SessionEndedEventArgs) """
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


class SessionEndingEventArgs(EventArgs):
    """
    Provides data for the Microsoft.Win32.SystemEvents.SessionEnding event.
    
    SessionEndingEventArgs(reason: SessionEndReasons)
    """
    @staticmethod # known case of __new__
    def __new__(self, reason):
        """ __new__(cls: type, reason: SessionEndReasons) """
        pass

    Cancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to cancel the user request to end the session.

Get: Cancel(self: SessionEndingEventArgs) -> bool

Set: Cancel(self: SessionEndingEventArgs) = value
"""

    Reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the reason the session is ending.

Get: Reason(self: SessionEndingEventArgs) -> SessionEndReasons

"""



class SessionEndingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the Microsoft.Win32.SystemEvents.SessionEnding event from the operating system.
    
    SessionEndingEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: SessionEndingEventHandler, sender: object, e: SessionEndingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: SessionEndingEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SessionEndingEventHandler, sender: object, e: SessionEndingEventArgs) """
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


class SessionEndReasons(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers that represent how the current logon session is ending.
    
    enum SessionEndReasons, values: Logoff (1), SystemShutdown (2)
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

    Logoff = None
    SystemShutdown = None
    value__ = None


class SessionSwitchEventArgs(EventArgs):
    """
    Provides data for the Microsoft.Win32.SystemEvents.SessionSwitch event.
    
    SessionSwitchEventArgs(reason: SessionSwitchReason)
    """
    @staticmethod # known case of __new__
    def __new__(self, reason):
        """ __new__(cls: type, reason: SessionSwitchReason) """
        pass

    Reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an identifier that indicates the type of session change event.

Get: Reason(self: SessionSwitchEventArgs) -> SessionSwitchReason

"""



class SessionSwitchEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the Microsoft.Win32.SystemEvents.SessionSwitch event.
    
    SessionSwitchEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: SessionSwitchEventHandler, sender: object, e: SessionSwitchEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: SessionSwitchEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SessionSwitchEventHandler, sender: object, e: SessionSwitchEventArgs) """
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


class SessionSwitchReason(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers used to represent the type of a session switch event.
    
    enum SessionSwitchReason, values: ConsoleConnect (1), ConsoleDisconnect (2), RemoteConnect (3), RemoteDisconnect (4), SessionLock (7), SessionLogoff (6), SessionLogon (5), SessionRemoteControl (9), SessionUnlock (8)
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

    ConsoleConnect = None
    ConsoleDisconnect = None
    RemoteConnect = None
    RemoteDisconnect = None
    SessionLock = None
    SessionLogoff = None
    SessionLogon = None
    SessionRemoteControl = None
    SessionUnlock = None
    value__ = None


class SystemEvents(object):
    """ Provides access to system event notifications. This class cannot be inherited. """
    @staticmethod
    def CreateTimer(interval):
        """
        CreateTimer(interval: int) -> IntPtr
        
            Creates a new window timer associated with the system events window.
        
            interval: Specifies the interval between timer notifications, in milliseconds.
            Returns: The ID of the new timer.
        """
        pass

    @staticmethod
    def InvokeOnEventsThread(method):
        """
        InvokeOnEventsThread(method: Delegate)
            Invokes the specified delegate using the thread that listens for system events.
        
            method: A delegate to invoke using the thread that listens for system events.
        """
        pass

    @staticmethod
    def KillTimer(timerId):
        """
        KillTimer(timerId: IntPtr)
            Terminates the timer specified by the given id.
        
            timerId: The ID of the timer to terminate.
        """
        pass

    DisplaySettingsChanged = None
    DisplaySettingsChanging = None
    EventsThreadShutdown = None
    InstalledFontsChanged = None
    LowMemory = None
    PaletteChanged = None
    PowerModeChanged = None
    SessionEnded = None
    SessionEnding = None
    SessionSwitch = None
    TimeChanged = None
    TimerElapsed = None
    UserPreferenceChanged = None
    UserPreferenceChanging = None


class TimerElapsedEventArgs(EventArgs):
    """
    Provides data for the Microsoft.Win32.SystemEvents.TimerElapsed event.
    
    TimerElapsedEventArgs(timerId: IntPtr)
    """
    @staticmethod # known case of __new__
    def __new__(self, timerId):
        """ __new__(cls: type, timerId: IntPtr) """
        pass

    TimerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the ID number for the timer.

Get: TimerId(self: TimerElapsedEventArgs) -> IntPtr

"""



class TimerElapsedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the Microsoft.Win32.SystemEvents.TimerElapsed event.
    
    TimerElapsedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: TimerElapsedEventHandler, sender: object, e: TimerElapsedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: TimerElapsedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: TimerElapsedEventHandler, sender: object, e: TimerElapsedEventArgs) """
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


class UserPreferenceCategory(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers that represent categories of user preferences.
    
    enum UserPreferenceCategory, values: Accessibility (1), Color (2), Desktop (3), General (4), Icon (5), Keyboard (6), Locale (13), Menu (7), Mouse (8), Policy (9), Power (10), Screensaver (11), VisualStyle (14), Window (12)
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

    Accessibility = None
    Color = None
    Desktop = None
    General = None
    Icon = None
    Keyboard = None
    Locale = None
    Menu = None
    Mouse = None
    Policy = None
    Power = None
    Screensaver = None
    value__ = None
    VisualStyle = None
    Window = None


class UserPreferenceChangedEventArgs(EventArgs):
    """
    Provides data for the Microsoft.Win32.SystemEvents.UserPreferenceChanged event.
    
    UserPreferenceChangedEventArgs(category: UserPreferenceCategory)
    """
    @staticmethod # known case of __new__
    def __new__(self, category):
        """ __new__(cls: type, category: UserPreferenceCategory) """
        pass

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the category of user preferences that has changed.

Get: Category(self: UserPreferenceChangedEventArgs) -> UserPreferenceCategory

"""



class UserPreferenceChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the Microsoft.Win32.SystemEvents.UserPreferenceChanged event.
    
    UserPreferenceChangedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: UserPreferenceChangedEventHandler, sender: object, e: UserPreferenceChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: UserPreferenceChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: UserPreferenceChangedEventHandler, sender: object, e: UserPreferenceChangedEventArgs) """
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


class UserPreferenceChangingEventArgs(EventArgs):
    """
    Provides data for the Microsoft.Win32.SystemEvents.UserPreferenceChanging event.
    
    UserPreferenceChangingEventArgs(category: UserPreferenceCategory)
    """
    @staticmethod # known case of __new__
    def __new__(self, category):
        """ __new__(cls: type, category: UserPreferenceCategory) """
        pass

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the category of user preferences that is changing.

Get: Category(self: UserPreferenceChangingEventArgs) -> UserPreferenceCategory

"""



class UserPreferenceChangingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the Microsoft.Win32.SystemEvents.UserPreferenceChanging event.
    
    UserPreferenceChangingEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: UserPreferenceChangingEventHandler, sender: object, e: UserPreferenceChangingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: UserPreferenceChangingEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: UserPreferenceChangingEventHandler, sender: object, e: UserPreferenceChangingEventArgs) """
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


# variables with complex values

