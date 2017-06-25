# encoding: utf-8
# module System
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# functions

def Action(p_object, method): # real signature unknown; restored from __doc__
    """ Action(object: object, method: IntPtr) """
    pass

def EventHandler(p_object, method): # real signature unknown; restored from __doc__
    """ EventHandler(object: object, method: IntPtr) """
    pass

def Func(*args, **kwargs): # real signature unknown
    """  """
    pass

def IComparable(*args, **kwargs): # real signature unknown
    """  """
    pass

def Nullable(*args, **kwargs): # real signature unknown
    """  """
    pass

def Tuple(*args, **kwargs): # real signature unknown
    """  """
    pass

def ValueTuple(*args, **kwargs): # real signature unknown
    """  """
    pass

def WeakReference(target): # real signature unknown; restored from __doc__
    """
    WeakReference(target: object)
    WeakReference(target: object, trackResurrection: bool)
    """
    pass

# classes

class Object:
    """ object() """
    def __delattr__(self, *args): #cannot find CLR method
        """ __delattr__(self: object, name: str) """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(self: object, formatSpec: str) -> str """
        pass

    def __getattribute__(self, *args): #cannot find CLR method
        """ __getattribute__(self: object, name: str) -> object """
        pass

    def __hash__(self, *args): #cannot find CLR method
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type, **kwargs?: dict, *args?: Array[object]) -> object
        __new__(cls: type, *args?: Array[object]) -> object
        __new__(cls: type) -> object
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __reduce__(self, *args): #cannot find CLR method
        """ helper for pickle """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setattr__(self, *args): #cannot find CLR method
        """ __setattr__(self: object, name: str, value: object) """
        pass

    def __sizeof__(self, *args): #cannot find CLR method
        """ __sizeof__(self: object) -> int """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __subclasshook__(self, *args): #cannot find CLR method
        """ __subclasshook__(*args: Array[object]) -> NotImplementedType """
        pass

    __class__ = None


class Exception(object):
    """
    Exception()
    Exception(message: str)
    Exception(message: str, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetBaseException(self):
        """ GetBaseException(self: Exception) -> Exception """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: Exception, info: SerializationInfo, context: StreamingContext) """
        pass

    def GetType(self):
        """ GetType(self: Exception) -> Type """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def ToString(self):
        """ ToString(self: Exception) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: Exception) -> IDictionary

"""

    HelpLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpLink(self: Exception) -> str

Set: HelpLink(self: Exception) = value
"""

    HResult = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HResult(self: Exception) -> int

"""

    InnerException = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerException(self: Exception) -> Exception

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: Exception) -> str

"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: Exception) -> str

Set: Source(self: Exception) = value
"""

    StackTrace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StackTrace(self: Exception) -> str

"""

    TargetSite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetSite(self: Exception) -> MethodBase

"""



class SystemException(Exception):
    """
    SystemException()
    SystemException(message: str)
    SystemException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class AccessViolationException(SystemException):
    """
    AccessViolationException()
    AccessViolationException(message: str)
    AccessViolationException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class IDisposable:
    # no doc
    def Dispose(self):
        """ Dispose(self: IDisposable) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ActivationContext(object):
    # no doc
    @staticmethod
    def CreatePartialActivationContext(identity, manifestPaths=None):
        """
        CreatePartialActivationContext(identity: ApplicationIdentity, manifestPaths: Array[str]) -> ActivationContext
        CreatePartialActivationContext(identity: ApplicationIdentity) -> ActivationContext
        """
        pass

    def Dispose(self):
        """ Dispose(self: ActivationContext) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    ApplicationManifestBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationManifestBytes(self: ActivationContext) -> Array[Byte]

"""

    DeploymentManifestBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeploymentManifestBytes(self: ActivationContext) -> Array[Byte]

"""

    Form = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Form(self: ActivationContext) -> ContextForm

"""

    Identity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identity(self: ActivationContext) -> ApplicationIdentity

"""


    ContextForm = None


class Activator(object):
    # no doc
    @staticmethod
    def CreateComInstanceFrom(assemblyName, typeName, hashValue=None, hashAlgorithm=None):
        """
        CreateComInstanceFrom(assemblyName: str, typeName: str, hashValue: Array[Byte], hashAlgorithm: AssemblyHashAlgorithm) -> ObjectHandle
        CreateComInstanceFrom(assemblyName: str, typeName: str) -> ObjectHandle
        """
        pass

    @staticmethod
    def CreateInstance(*__args):
        """
        CreateInstance(assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> ObjectHandle
        CreateInstance(domain: AppDomain, assemblyName: str, typeName: str) -> ObjectHandle
        CreateInstance[T]() -> T
        CreateInstance(assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityInfo: Evidence) -> ObjectHandle
        CreateInstance(activationContext: ActivationContext) -> ObjectHandle
        CreateInstance(activationContext: ActivationContext, activationCustomData: Array[str]) -> ObjectHandle
        CreateInstance(domain: AppDomain, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityAttributes: Evidence) -> ObjectHandle
        CreateInstance(domain: AppDomain, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> ObjectHandle
        CreateInstance(type: Type, *args: Array[object]) -> object
        CreateInstance(type: Type, args: Array[object], activationAttributes: Array[object]) -> object
        CreateInstance(type: Type, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo) -> object
        CreateInstance(type: Type, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> object
        CreateInstance(assemblyName: str, typeName: str, activationAttributes: Array[object]) -> ObjectHandle
        CreateInstance(type: Type, nonPublic: bool) -> object
        CreateInstance(type: Type) -> object
        CreateInstance(assemblyName: str, typeName: str) -> ObjectHandle
        """
        pass

    @staticmethod
    def CreateInstanceFrom(*__args):
        """
        CreateInstanceFrom(domain: AppDomain, assemblyFile: str, typeName: str) -> ObjectHandle
        CreateInstanceFrom(domain: AppDomain, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityAttributes: Evidence) -> ObjectHandle
        CreateInstanceFrom(domain: AppDomain, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> ObjectHandle
        CreateInstanceFrom(assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> ObjectHandle
        CreateInstanceFrom(assemblyFile: str, typeName: str) -> ObjectHandle
        CreateInstanceFrom(assemblyFile: str, typeName: str, activationAttributes: Array[object]) -> ObjectHandle
        CreateInstanceFrom(assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityInfo: Evidence) -> ObjectHandle
        """
        pass

    @staticmethod
    def GetObject(type, url, state=None):
        """
        GetObject(type: Type, url: str, state: object) -> object
        GetObject(type: Type, url: str) -> object
        """
        pass


class AggregateException(Exception):
    """
    AggregateException()
    AggregateException(message: str)
    AggregateException(message: str, innerException: Exception)
    AggregateException(innerExceptions: IEnumerable[Exception])
    AggregateException(*innerExceptions: Array[Exception])
    AggregateException(message: str, innerExceptions: IEnumerable[Exception])
    AggregateException(message: str, *innerExceptions: Array[Exception])
    """
    def Flatten(self):
        """ Flatten(self: AggregateException) -> AggregateException """
        pass

    def GetBaseException(self):
        """ GetBaseException(self: AggregateException) -> Exception """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: AggregateException, info: SerializationInfo, context: StreamingContext) """
        pass

    def Handle(self, predicate):
        """ Handle(self: AggregateException, predicate: Func[Exception, bool]) """
        pass

    def ToString(self):
        """ ToString(self: AggregateException) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, innerExceptions: IEnumerable[Exception])
        __new__(cls: type, *innerExceptions: Array[Exception])
        __new__(cls: type, message: str, innerExceptions: IEnumerable[Exception])
        __new__(cls: type, message: str, *innerExceptions: Array[Exception])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    InnerExceptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerExceptions(self: AggregateException) -> ReadOnlyCollection[Exception]

"""



class AppContext(object):
    # no doc
    @staticmethod
    def GetData(name):
        """ GetData(name: str) -> object """
        pass

    @staticmethod
    def SetSwitch(switchName, isEnabled):
        """ SetSwitch(switchName: str, isEnabled: bool) """
        pass

    @staticmethod
    def TryGetSwitch(switchName, isEnabled):
        """ TryGetSwitch(switchName: str) -> (bool, bool) """
        pass

    BaseDirectory = 'C:\\Program Files (x86)\\IronPython 2.7\\'
    TargetFrameworkName = '.NETFramework,Version=v4.0'
    __all__ = [
        'GetData',
        'SetSwitch',
        'TryGetSwitch',
    ]


class MarshalByRefObject(object):
    # no doc
    def CreateObjRef(self, requestedType):
        """ CreateObjRef(self: MarshalByRefObject, requestedType: Type) -> ObjRef """
        pass

    def GetLifetimeService(self):
        """ GetLifetimeService(self: MarshalByRefObject) -> object """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: MarshalByRefObject) -> object """
        pass


class _AppDomain:
    # no doc
    def AppendPrivatePath(self, path):
        """ AppendPrivatePath(self: _AppDomain, path: str) """
        pass

    def ClearPrivatePath(self):
        """ ClearPrivatePath(self: _AppDomain) """
        pass

    def ClearShadowCopyPath(self):
        """ ClearShadowCopyPath(self: _AppDomain) """
        pass

    def CreateInstance(self, assemblyName, typeName, *__args):
        """
        CreateInstance(self: _AppDomain, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityAttributes: Evidence) -> ObjectHandle
        CreateInstance(self: _AppDomain, assemblyName: str, typeName: str, activationAttributes: Array[object]) -> ObjectHandle
        CreateInstance(self: _AppDomain, assemblyName: str, typeName: str) -> ObjectHandle
        """
        pass

    def CreateInstanceFrom(self, assemblyFile, typeName, *__args):
        """
        CreateInstanceFrom(self: _AppDomain, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityAttributes: Evidence) -> ObjectHandle
        CreateInstanceFrom(self: _AppDomain, assemblyFile: str, typeName: str, activationAttributes: Array[object]) -> ObjectHandle
        CreateInstanceFrom(self: _AppDomain, assemblyFile: str, typeName: str) -> ObjectHandle
        """
        pass

    def DefineDynamicAssembly(self, name, access, *__args):
        """
        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder
        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder
        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet, isSynchronized: bool) -> AssemblyBuilder
        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder
        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, evidence: Evidence) -> AssemblyBuilder
        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str) -> AssemblyBuilder
        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess) -> AssemblyBuilder
        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder
        DefineDynamicAssembly(self: _AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, evidence: Evidence) -> AssemblyBuilder
        """
        pass

    def DoCallBack(self, theDelegate):
        """ DoCallBack(self: _AppDomain, theDelegate: CrossAppDomainDelegate) """
        pass

    def Equals(self, other):
        """ Equals(self: _AppDomain, other: object) -> bool """
        pass

    def ExecuteAssembly(self, assemblyFile, assemblySecurity=None, args=None):
        """
        ExecuteAssembly(self: _AppDomain, assemblyFile: str, assemblySecurity: Evidence, args: Array[str]) -> int
        ExecuteAssembly(self: _AppDomain, assemblyFile: str) -> int
        ExecuteAssembly(self: _AppDomain, assemblyFile: str, assemblySecurity: Evidence) -> int
        """
        pass

    def GetAssemblies(self):
        """ GetAssemblies(self: _AppDomain) -> Array[Assembly] """
        pass

    def GetData(self, name):
        """ GetData(self: _AppDomain, name: str) -> object """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: _AppDomain) -> int """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _AppDomain, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetLifetimeService(self):
        """ GetLifetimeService(self: _AppDomain) -> object """
        pass

    def GetType(self):
        """ GetType(self: _AppDomain) -> Type """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _AppDomain, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _AppDomain) -> UInt32 """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: _AppDomain) -> object """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _AppDomain, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def Load(self, *__args):
        """
        Load(self: _AppDomain, rawAssembly: Array[Byte], rawSymbolStore: Array[Byte], securityEvidence: Evidence) -> Assembly
        Load(self: _AppDomain, assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly
        Load(self: _AppDomain, assemblyString: str, assemblySecurity: Evidence) -> Assembly
        Load(self: _AppDomain, rawAssembly: Array[Byte], rawSymbolStore: Array[Byte]) -> Assembly
        Load(self: _AppDomain, assemblyRef: AssemblyName) -> Assembly
        Load(self: _AppDomain, assemblyString: str) -> Assembly
        Load(self: _AppDomain, rawAssembly: Array[Byte]) -> Assembly
        """
        pass

    def SetAppDomainPolicy(self, domainPolicy):
        """ SetAppDomainPolicy(self: _AppDomain, domainPolicy: PolicyLevel) """
        pass

    def SetCachePath(self, s):
        """ SetCachePath(self: _AppDomain, s: str) """
        pass

    def SetData(self, name, data):
        """ SetData(self: _AppDomain, name: str, data: object) """
        pass

    def SetPrincipalPolicy(self, policy):
        """ SetPrincipalPolicy(self: _AppDomain, policy: PrincipalPolicy) """
        pass

    def SetShadowCopyPath(self, s):
        """ SetShadowCopyPath(self: _AppDomain, s: str) """
        pass

    def SetThreadPrincipal(self, principal):
        """ SetThreadPrincipal(self: _AppDomain, principal: IPrincipal) """
        pass

    def ToString(self):
        """ ToString(self: _AppDomain) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BaseDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseDirectory(self: _AppDomain) -> str

"""

    DynamicDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DynamicDirectory(self: _AppDomain) -> str

"""

    Evidence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Evidence(self: _AppDomain) -> Evidence

"""

    FriendlyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FriendlyName(self: _AppDomain) -> str

"""

    RelativeSearchPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeSearchPath(self: _AppDomain) -> str

"""

    ShadowCopyFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadowCopyFiles(self: _AppDomain) -> bool

"""


    AssemblyLoad = None
    AssemblyResolve = None
    DomainUnload = None
    ProcessExit = None
    ResourceResolve = None
    TypeResolve = None
    UnhandledException = None


class AppDomain(MarshalByRefObject):
    # no doc
    def AppendPrivatePath(self, path):
        """ AppendPrivatePath(self: AppDomain, path: str) """
        pass

    def ApplyPolicy(self, assemblyName):
        """ ApplyPolicy(self: AppDomain, assemblyName: str) -> str """
        pass

    def ClearPrivatePath(self):
        """ ClearPrivatePath(self: AppDomain) """
        pass

    def ClearShadowCopyPath(self):
        """ ClearShadowCopyPath(self: AppDomain) """
        pass

    def CreateComInstanceFrom(self, *__args):
        """
        CreateComInstanceFrom(self: AppDomain, assemblyFile: str, typeName: str, hashValue: Array[Byte], hashAlgorithm: AssemblyHashAlgorithm) -> ObjectHandle
        CreateComInstanceFrom(self: AppDomain, assemblyName: str, typeName: str) -> ObjectHandle
        """
        pass

    @staticmethod
    def CreateDomain(friendlyName, securityInfo=None, *__args):
        """
        CreateDomain(friendlyName: str, securityInfo: Evidence, info: AppDomainSetup) -> AppDomain
        CreateDomain(friendlyName: str, securityInfo: Evidence, info: AppDomainSetup, grantSet: PermissionSet, *fullTrustAssemblies: Array[StrongName]) -> AppDomain
        CreateDomain(friendlyName: str, securityInfo: Evidence, appBasePath: str, appRelativeSearchPath: str, shadowCopyFiles: bool, adInit: AppDomainInitializer, adInitArgs: Array[str]) -> AppDomain
        CreateDomain(friendlyName: str, securityInfo: Evidence) -> AppDomain
        CreateDomain(friendlyName: str, securityInfo: Evidence, appBasePath: str, appRelativeSearchPath: str, shadowCopyFiles: bool) -> AppDomain
        CreateDomain(friendlyName: str) -> AppDomain
        """
        pass

    def CreateInstance(self, assemblyName, typeName, *__args):
        """
        CreateInstance(self: AppDomain, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityAttributes: Evidence) -> ObjectHandle
        CreateInstance(self: AppDomain, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> ObjectHandle
        CreateInstance(self: AppDomain, assemblyName: str, typeName: str) -> ObjectHandle
        CreateInstance(self: AppDomain, assemblyName: str, typeName: str, activationAttributes: Array[object]) -> ObjectHandle
        """
        pass

    def CreateInstanceAndUnwrap(self, assemblyName, typeName, *__args):
        """
        CreateInstanceAndUnwrap(self: AppDomain, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityAttributes: Evidence) -> object
        CreateInstanceAndUnwrap(self: AppDomain, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> object
        CreateInstanceAndUnwrap(self: AppDomain, assemblyName: str, typeName: str) -> object
        CreateInstanceAndUnwrap(self: AppDomain, assemblyName: str, typeName: str, activationAttributes: Array[object]) -> object
        """
        pass

    def CreateInstanceFrom(self, assemblyFile, typeName, *__args):
        """
        CreateInstanceFrom(self: AppDomain, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityAttributes: Evidence) -> ObjectHandle
        CreateInstanceFrom(self: AppDomain, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> ObjectHandle
        CreateInstanceFrom(self: AppDomain, assemblyFile: str, typeName: str) -> ObjectHandle
        CreateInstanceFrom(self: AppDomain, assemblyFile: str, typeName: str, activationAttributes: Array[object]) -> ObjectHandle
        """
        pass

    def CreateInstanceFromAndUnwrap(self, *__args):
        """
        CreateInstanceFromAndUnwrap(self: AppDomain, assemblyName: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object], securityAttributes: Evidence) -> object
        CreateInstanceFromAndUnwrap(self: AppDomain, assemblyFile: str, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> object
        CreateInstanceFromAndUnwrap(self: AppDomain, assemblyName: str, typeName: str) -> object
        CreateInstanceFromAndUnwrap(self: AppDomain, assemblyName: str, typeName: str, activationAttributes: Array[object]) -> object
        """
        pass

    def DefineDynamicAssembly(self, name, access, *__args):
        """
        DefineDynamicAssembly(self: AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder
        DefineDynamicAssembly(self: AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder
        DefineDynamicAssembly(self: AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder
        DefineDynamicAssembly(self: AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, isSynchronized: bool, assemblyAttributes: IEnumerable[CustomAttributeBuilder]) -> AssemblyBuilder
        DefineDynamicAssembly(self: AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet, isSynchronized: bool, assemblyAttributes: IEnumerable[CustomAttributeBuilder]) -> AssemblyBuilder
        DefineDynamicAssembly(self: AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, evidence: Evidence, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet, isSynchronized: bool) -> AssemblyBuilder
        DefineDynamicAssembly(self: AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, evidence: Evidence) -> AssemblyBuilder
        DefineDynamicAssembly(self: AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, assemblyAttributes: IEnumerable[CustomAttributeBuilder], securityContextSource: SecurityContextSource) -> AssemblyBuilder
        DefineDynamicAssembly(self: AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, assemblyAttributes: IEnumerable[CustomAttributeBuilder]) -> AssemblyBuilder
        DefineDynamicAssembly(self: AppDomain, name: AssemblyName, access: AssemblyBuilderAccess) -> AssemblyBuilder
        DefineDynamicAssembly(self: AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, requiredPermissions: PermissionSet, optionalPermissions: PermissionSet, refusedPermissions: PermissionSet) -> AssemblyBuilder
        DefineDynamicAssembly(self: AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, evidence: Evidence) -> AssemblyBuilder
        DefineDynamicAssembly(self: AppDomain, name: AssemblyName, access: AssemblyBuilderAccess, dir: str) -> AssemblyBuilder
        """
        pass

    def DoCallBack(self, callBackDelegate):
        """ DoCallBack(self: AppDomain, callBackDelegate: CrossAppDomainDelegate) """
        pass

    def ExecuteAssembly(self, assemblyFile, *__args):
        """
        ExecuteAssembly(self: AppDomain, assemblyFile: str, args: Array[str]) -> int
        ExecuteAssembly(self: AppDomain, assemblyFile: str, assemblySecurity: Evidence, args: Array[str], hashValue: Array[Byte], hashAlgorithm: AssemblyHashAlgorithm) -> int
        ExecuteAssembly(self: AppDomain, assemblyFile: str, args: Array[str], hashValue: Array[Byte], hashAlgorithm: AssemblyHashAlgorithm) -> int
        ExecuteAssembly(self: AppDomain, assemblyFile: str) -> int
        ExecuteAssembly(self: AppDomain, assemblyFile: str, assemblySecurity: Evidence) -> int
        ExecuteAssembly(self: AppDomain, assemblyFile: str, assemblySecurity: Evidence, args: Array[str]) -> int
        """
        pass

    def ExecuteAssemblyByName(self, assemblyName, *__args):
        """
        ExecuteAssemblyByName(self: AppDomain, assemblyName: str, *args: Array[str]) -> int
        ExecuteAssemblyByName(self: AppDomain, assemblyName: AssemblyName, assemblySecurity: Evidence, *args: Array[str]) -> int
        ExecuteAssemblyByName(self: AppDomain, assemblyName: AssemblyName, *args: Array[str]) -> int
        ExecuteAssemblyByName(self: AppDomain, assemblyName: str) -> int
        ExecuteAssemblyByName(self: AppDomain, assemblyName: str, assemblySecurity: Evidence) -> int
        ExecuteAssemblyByName(self: AppDomain, assemblyName: str, assemblySecurity: Evidence, *args: Array[str]) -> int
        """
        pass

    def GetAssemblies(self):
        """ GetAssemblies(self: AppDomain) -> Array[Assembly] """
        pass

    @staticmethod
    def GetCurrentThreadId():
        """ GetCurrentThreadId() -> int """
        pass

    def GetData(self, name):
        """ GetData(self: AppDomain, name: str) -> object """
        pass

    def GetType(self):
        """ GetType(self: AppDomain) -> Type """
        pass

    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: AppDomain) -> object """
        pass

    def IsCompatibilitySwitchSet(self, value):
        """ IsCompatibilitySwitchSet(self: AppDomain, value: str) -> Nullable[bool] """
        pass

    def IsDefaultAppDomain(self):
        """ IsDefaultAppDomain(self: AppDomain) -> bool """
        pass

    def IsFinalizingForUnload(self):
        """ IsFinalizingForUnload(self: AppDomain) -> bool """
        pass

    def Load(self, *__args):
        """
        Load(self: AppDomain, rawAssembly: Array[Byte], rawSymbolStore: Array[Byte], securityEvidence: Evidence) -> Assembly
        Load(self: AppDomain, assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly
        Load(self: AppDomain, assemblyString: str, assemblySecurity: Evidence) -> Assembly
        Load(self: AppDomain, rawAssembly: Array[Byte], rawSymbolStore: Array[Byte]) -> Assembly
        Load(self: AppDomain, assemblyRef: AssemblyName) -> Assembly
        Load(self: AppDomain, assemblyString: str) -> Assembly
        Load(self: AppDomain, rawAssembly: Array[Byte]) -> Assembly
        """
        pass

    def ReflectionOnlyGetAssemblies(self):
        """ ReflectionOnlyGetAssemblies(self: AppDomain) -> Array[Assembly] """
        pass

    def SetAppDomainPolicy(self, domainPolicy):
        """ SetAppDomainPolicy(self: AppDomain, domainPolicy: PolicyLevel) """
        pass

    def SetCachePath(self, path):
        """ SetCachePath(self: AppDomain, path: str) """
        pass

    def SetData(self, name, data, permission=None):
        """ SetData(self: AppDomain, name: str, data: object, permission: IPermission)SetData(self: AppDomain, name: str, data: object) """
        pass

    def SetDynamicBase(self, path):
        """ SetDynamicBase(self: AppDomain, path: str) """
        pass

    def SetPrincipalPolicy(self, policy):
        """ SetPrincipalPolicy(self: AppDomain, policy: PrincipalPolicy) """
        pass

    def SetShadowCopyFiles(self):
        """ SetShadowCopyFiles(self: AppDomain) """
        pass

    def SetShadowCopyPath(self, path):
        """ SetShadowCopyPath(self: AppDomain, path: str) """
        pass

    def SetThreadPrincipal(self, principal):
        """ SetThreadPrincipal(self: AppDomain, principal: IPrincipal) """
        pass

    def ToString(self):
        """ ToString(self: AppDomain) -> str """
        pass

    @staticmethod
    def Unload(domain):
        """ Unload(domain: AppDomain) """
        pass

    ActivationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActivationContext(self: AppDomain) -> ActivationContext

"""

    ApplicationIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationIdentity(self: AppDomain) -> ApplicationIdentity

"""

    ApplicationTrust = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationTrust(self: AppDomain) -> ApplicationTrust

"""

    BaseDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseDirectory(self: AppDomain) -> str

"""

    DomainManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DomainManager(self: AppDomain) -> AppDomainManager

"""

    DynamicDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DynamicDirectory(self: AppDomain) -> str

"""

    Evidence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Evidence(self: AppDomain) -> Evidence

"""

    FriendlyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FriendlyName(self: AppDomain) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: AppDomain) -> int

"""

    IsFullyTrusted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFullyTrusted(self: AppDomain) -> bool

"""

    IsHomogenous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHomogenous(self: AppDomain) -> bool

"""

    MonitoringSurvivedMemorySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MonitoringSurvivedMemorySize(self: AppDomain) -> Int64

"""

    MonitoringTotalAllocatedMemorySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MonitoringTotalAllocatedMemorySize(self: AppDomain) -> Int64

"""

    MonitoringTotalProcessorTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MonitoringTotalProcessorTime(self: AppDomain) -> TimeSpan

"""

    PermissionSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PermissionSet(self: AppDomain) -> PermissionSet

"""

    RelativeSearchPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeSearchPath(self: AppDomain) -> str

"""

    SetupInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SetupInformation(self: AppDomain) -> AppDomainSetup

"""

    ShadowCopyFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadowCopyFiles(self: AppDomain) -> bool

"""


    AssemblyLoad = None
    AssemblyResolve = None
    CurrentDomain = None
    DomainUnload = None
    FirstChanceException = None
    MonitoringIsEnabled = False
    ProcessExit = None
    ReflectionOnlyAssemblyResolve = None
    ResourceResolve = None
    TypeResolve = None
    UnhandledException = None


class Delegate(object):
    # no doc
    def Call(self, *args): #cannot find CLR method
        """ x.__call__(...) <==> x(...)x.__call__(...) <==> x(...) """
        pass

    def Clone(self):
        """ Clone(self: Delegate) -> object """
        pass

    @staticmethod
    def Combine(*__args):
        """
        Combine(*delegates: Array[Delegate]) -> Delegate
        Combine(a: Delegate, b: Delegate) -> Delegate
        """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: Delegate, d: Delegate) -> Delegate """
        pass

    @staticmethod
    def CreateDelegate(type, *__args):
        """
        CreateDelegate(type: Type, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
        CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
        CreateDelegate(type: Type, firstArgument: object, method: MethodInfo) -> Delegate
        CreateDelegate(type: Type, method: MethodInfo) -> Delegate
        CreateDelegate(type: Type, firstArgument: object, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
        CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool) -> Delegate
        CreateDelegate(type: Type, target: object, method: str) -> Delegate
        CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
        CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool) -> Delegate
        CreateDelegate(type: Type, target: Type, method: str) -> Delegate
        """
        pass

    def DynamicInvoke(self, args):
        """ DynamicInvoke(self: Delegate, *args: Array[object]) -> object """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        pass

    def Equals(self, obj):
        """ Equals(self: Delegate, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Delegate) -> int """
        pass

    def GetInvocationList(self):
        """ GetInvocationList(self: Delegate) -> Array[Delegate] """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: Delegate) -> MethodInfo """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: Delegate, info: SerializationInfo, context: StreamingContext) """
        pass

    def InPlaceAdd(self, *args): #cannot find CLR method
        """ InPlaceAdd(self: Delegate, other: Delegate) -> Delegate """
        pass

    def InPlaceSubtract(self, *args): #cannot find CLR method
        """ InPlaceSubtract(self: Delegate, other: Delegate) -> Delegate """
        pass

    @staticmethod
    def Remove(source, value):
        """ Remove(source: Delegate, value: Delegate) -> Delegate """
        pass

    @staticmethod
    def RemoveAll(source, value):
        """ RemoveAll(source: Delegate, value: Delegate) -> Delegate """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """ RemoveImpl(self: Delegate, d: Delegate) -> Delegate """
        pass

    def __call__(self, *args): #cannot find CLR method
        """ x.__call__(...) <==> x(...)x.__call__(...) <==> x(...) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __iadd__(self, *args): #cannot find CLR method
        """ __iadd__(self: Delegate, other: Delegate) -> Delegate """
        pass

    def __isub__(self, *args): #cannot find CLR method
        """ __isub__(self: Delegate, other: Delegate) -> Delegate """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(type: type, function: object) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Method(self: Delegate) -> MethodInfo

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Target(self: Delegate) -> object

"""



class MulticastDelegate(Delegate):
    # no doc
    def Equals(self, obj):
        """ Equals(self: MulticastDelegate, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: MulticastDelegate) -> int """
        pass

    def GetInvocationList(self):
        """ GetInvocationList(self: MulticastDelegate) -> Array[Delegate] """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: MulticastDelegate, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, target: object, method: str)
        __new__(cls: type, target: Type, method: str)
        """
        pass


class AppDomainInitializer(MulticastDelegate):
    """ AppDomainInitializer(object: object, method: IntPtr) """
    def BeginInvoke(self, args, callback, object):
        """ BeginInvoke(self: AppDomainInitializer, args: Array[str], callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: AppDomainInitializer, result: IAsyncResult) """
        pass

    def Invoke(self, args):
        """ Invoke(self: AppDomainInitializer, args: Array[str]) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class AppDomainManager(MarshalByRefObject):
    """ AppDomainManager() """
    def CheckSecuritySettings(self, state):
        """ CheckSecuritySettings(self: AppDomainManager, state: SecurityState) -> bool """
        pass

    def CreateDomain(self, friendlyName, securityInfo, appDomainInfo):
        """ CreateDomain(self: AppDomainManager, friendlyName: str, securityInfo: Evidence, appDomainInfo: AppDomainSetup) -> AppDomain """
        pass

    def CreateDomainHelper(self, *args): #cannot find CLR method
        """ CreateDomainHelper(friendlyName: str, securityInfo: Evidence, appDomainInfo: AppDomainSetup) -> AppDomain """
        pass

    def InitializeNewDomain(self, appDomainInfo):
        """ InitializeNewDomain(self: AppDomainManager, appDomainInfo: AppDomainSetup) """
        pass

    ApplicationActivator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationActivator(self: AppDomainManager) -> ApplicationActivator

"""

    EntryAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntryAssembly(self: AppDomainManager) -> Assembly

"""

    HostExecutionContextManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HostExecutionContextManager(self: AppDomainManager) -> HostExecutionContextManager

"""

    HostSecurityManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HostSecurityManager(self: AppDomainManager) -> HostSecurityManager

"""

    InitializationFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitializationFlags(self: AppDomainManager) -> AppDomainManagerInitializationOptions

Set: InitializationFlags(self: AppDomainManager) = value
"""



class IConvertible:
    # no doc
    def GetTypeCode(self):
        """ GetTypeCode(self: IConvertible) -> TypeCode """
        pass

    def ToBoolean(self, provider):
        """ ToBoolean(self: IConvertible, provider: IFormatProvider) -> bool """
        pass

    def ToByte(self, provider):
        """ ToByte(self: IConvertible, provider: IFormatProvider) -> Byte """
        pass

    def ToChar(self, provider):
        """ ToChar(self: IConvertible, provider: IFormatProvider) -> Char """
        pass

    def ToDateTime(self, provider):
        """ ToDateTime(self: IConvertible, provider: IFormatProvider) -> DateTime """
        pass

    def ToDecimal(self, provider):
        """ ToDecimal(self: IConvertible, provider: IFormatProvider) -> Decimal """
        pass

    def ToDouble(self, provider):
        """ ToDouble(self: IConvertible, provider: IFormatProvider) -> float """
        pass

    def ToInt16(self, provider):
        """ ToInt16(self: IConvertible, provider: IFormatProvider) -> Int16 """
        pass

    def ToInt32(self, provider):
        """ ToInt32(self: IConvertible, provider: IFormatProvider) -> int """
        pass

    def ToInt64(self, provider):
        """ ToInt64(self: IConvertible, provider: IFormatProvider) -> Int64 """
        pass

    def ToSByte(self, provider):
        """ ToSByte(self: IConvertible, provider: IFormatProvider) -> SByte """
        pass

    def ToSingle(self, provider):
        """ ToSingle(self: IConvertible, provider: IFormatProvider) -> Single """
        pass

    def ToString(self, provider):
        """ ToString(self: IConvertible, provider: IFormatProvider) -> str """
        pass

    def ToType(self, conversionType, provider):
        """ ToType(self: IConvertible, conversionType: Type, provider: IFormatProvider) -> object """
        pass

    def ToUInt16(self, provider):
        """ ToUInt16(self: IConvertible, provider: IFormatProvider) -> UInt16 """
        pass

    def ToUInt32(self, provider):
        """ ToUInt32(self: IConvertible, provider: IFormatProvider) -> UInt32 """
        pass

    def ToUInt64(self, provider):
        """ ToUInt64(self: IConvertible, provider: IFormatProvider) -> UInt64 """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IFormattable:
    # no doc
    def ToString(self, format, formatProvider):
        """ ToString(self: IFormattable, format: str, formatProvider: IFormatProvider) -> str """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Enum(object):
    # no doc
    def CompareTo(self, target):
        """ CompareTo(self: Enum, target: object) -> int """
        pass

    def Equals(self, obj):
        """ Equals(self: Enum, obj: object) -> bool """
        pass

    @staticmethod
    def Format(enumType, value, format):
        """ Format(enumType: Type, value: object, format: str) -> str """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Enum) -> int """
        pass

    @staticmethod
    def GetName(enumType, value):
        """ GetName(enumType: Type, value: object) -> str """
        pass

    @staticmethod
    def GetNames(enumType):
        """ GetNames(enumType: Type) -> Array[str] """
        pass

    def GetTypeCode(self):
        """ GetTypeCode(self: Enum) -> TypeCode """
        pass

    @staticmethod
    def GetUnderlyingType(enumType):
        """ GetUnderlyingType(enumType: Type) -> Type """
        pass

    @staticmethod
    def GetValues(enumType):
        """ GetValues(enumType: Type) -> Array """
        pass

    def HasFlag(self, flag):
        """ HasFlag(self: Enum, flag: Enum) -> bool """
        pass

    @staticmethod
    def IsDefined(enumType, value):
        """ IsDefined(enumType: Type, value: object) -> bool """
        pass

    @staticmethod
    def Parse(enumType, value, ignoreCase=None):
        """
        Parse(enumType: Type, value: str, ignoreCase: bool) -> object
        Parse(enumType: Type, value: str) -> object
        """
        pass

    @staticmethod
    def ToObject(enumType, value):
        """
        ToObject(enumType: Type, value: UInt32) -> object
        ToObject(enumType: Type, value: UInt16) -> object
        ToObject(enumType: Type, value: UInt64) -> object
        ToObject(enumType: Type, value: Int64) -> object
        ToObject(enumType: Type, value: Byte) -> object
        ToObject(enumType: Type, value: SByte) -> object
        ToObject(enumType: Type, value: object) -> object
        ToObject(enumType: Type, value: int) -> object
        ToObject(enumType: Type, value: Int16) -> object
        """
        pass

    def ToString(self, *__args):
        """
        ToString(self: Enum, format: str) -> str
        ToString(self: Enum, provider: IFormatProvider) -> str
        ToString(self: Enum) -> str
        ToString(self: Enum, format: str, provider: IFormatProvider) -> str
        """
        pass

    @staticmethod
    def TryParse(value, *__args):
        """
        TryParse[TEnum](value: str, ignoreCase: bool) -> (bool, TEnum)
        TryParse[TEnum](value: str) -> (bool, TEnum)
        """
        pass

    def __and__(self, *args): #cannot find CLR method
        """ __and__(self: object, other: object) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(self: object) -> object """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(self: object) -> bool """
        pass

    def __or__(self, *args): #cannot find CLR method
        """ __or__(self: object, other: object) -> object """
        pass

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(self: object, other: object) -> object """
        pass

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(self: object, other: object) -> object """
        pass

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(self: object, other: object) -> object """
        pass

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(self: object, other: object) -> object """
        pass


class AppDomainManagerInitializationOptions(Enum):
    """ enum (flags) AppDomainManagerInitializationOptions, values: None (0), RegisterWithHost (1) """
    None = None
    RegisterWithHost = None
    value__ = None


class AppDomainSetup(object):
    """
    AppDomainSetup()
    AppDomainSetup(activationContext: ActivationContext)
    AppDomainSetup(activationArguments: ActivationArguments)
    """
    def GetConfigurationBytes(self):
        """ GetConfigurationBytes(self: AppDomainSetup) -> Array[Byte] """
        pass

    def SetCompatibilitySwitches(self, switches):
        """ SetCompatibilitySwitches(self: AppDomainSetup, switches: IEnumerable[str]) """
        pass

    def SetConfigurationBytes(self, value):
        """ SetConfigurationBytes(self: AppDomainSetup, value: Array[Byte]) """
        pass

    def SetNativeFunction(self, functionName, functionVersion, functionPointer):
        """ SetNativeFunction(self: AppDomainSetup, functionName: str, functionVersion: int, functionPointer: IntPtr) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, activationContext: ActivationContext)
        __new__(cls: type, activationArguments: ActivationArguments)
        """
        pass

    ActivationArguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActivationArguments(self: AppDomainSetup) -> ActivationArguments

Set: ActivationArguments(self: AppDomainSetup) = value
"""

    AppDomainInitializer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppDomainInitializer(self: AppDomainSetup) -> AppDomainInitializer

Set: AppDomainInitializer(self: AppDomainSetup) = value
"""

    AppDomainInitializerArguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppDomainInitializerArguments(self: AppDomainSetup) -> Array[str]

Set: AppDomainInitializerArguments(self: AppDomainSetup) = value
"""

    AppDomainManagerAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppDomainManagerAssembly(self: AppDomainSetup) -> str

Set: AppDomainManagerAssembly(self: AppDomainSetup) = value
"""

    AppDomainManagerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppDomainManagerType(self: AppDomainSetup) -> str

Set: AppDomainManagerType(self: AppDomainSetup) = value
"""

    ApplicationBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationBase(self: AppDomainSetup) -> str

Set: ApplicationBase(self: AppDomainSetup) = value
"""

    ApplicationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationName(self: AppDomainSetup) -> str

Set: ApplicationName(self: AppDomainSetup) = value
"""

    ApplicationTrust = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationTrust(self: AppDomainSetup) -> ApplicationTrust

Set: ApplicationTrust(self: AppDomainSetup) = value
"""

    CachePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CachePath(self: AppDomainSetup) -> str

Set: CachePath(self: AppDomainSetup) = value
"""

    ConfigurationFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConfigurationFile(self: AppDomainSetup) -> str

Set: ConfigurationFile(self: AppDomainSetup) = value
"""

    DisallowApplicationBaseProbing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisallowApplicationBaseProbing(self: AppDomainSetup) -> bool

Set: DisallowApplicationBaseProbing(self: AppDomainSetup) = value
"""

    DisallowBindingRedirects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisallowBindingRedirects(self: AppDomainSetup) -> bool

Set: DisallowBindingRedirects(self: AppDomainSetup) = value
"""

    DisallowCodeDownload = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisallowCodeDownload(self: AppDomainSetup) -> bool

Set: DisallowCodeDownload(self: AppDomainSetup) = value
"""

    DisallowPublisherPolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisallowPublisherPolicy(self: AppDomainSetup) -> bool

Set: DisallowPublisherPolicy(self: AppDomainSetup) = value
"""

    DynamicBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DynamicBase(self: AppDomainSetup) -> str

Set: DynamicBase(self: AppDomainSetup) = value
"""

    LicenseFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicenseFile(self: AppDomainSetup) -> str

Set: LicenseFile(self: AppDomainSetup) = value
"""

    LoaderOptimization = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoaderOptimization(self: AppDomainSetup) -> LoaderOptimization

Set: LoaderOptimization(self: AppDomainSetup) = value
"""

    PartialTrustVisibleAssemblies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartialTrustVisibleAssemblies(self: AppDomainSetup) -> Array[str]

Set: PartialTrustVisibleAssemblies(self: AppDomainSetup) = value
"""

    PrivateBinPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrivateBinPath(self: AppDomainSetup) -> str

Set: PrivateBinPath(self: AppDomainSetup) = value
"""

    PrivateBinPathProbe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrivateBinPathProbe(self: AppDomainSetup) -> str

Set: PrivateBinPathProbe(self: AppDomainSetup) = value
"""

    SandboxInterop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SandboxInterop(self: AppDomainSetup) -> bool

Set: SandboxInterop(self: AppDomainSetup) = value
"""

    ShadowCopyDirectories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadowCopyDirectories(self: AppDomainSetup) -> str

Set: ShadowCopyDirectories(self: AppDomainSetup) = value
"""

    ShadowCopyFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadowCopyFiles(self: AppDomainSetup) -> str

Set: ShadowCopyFiles(self: AppDomainSetup) = value
"""

    TargetFrameworkName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetFrameworkName(self: AppDomainSetup) -> str

Set: TargetFrameworkName(self: AppDomainSetup) = value
"""



class AppDomainUnloadedException(SystemException):
    """
    AppDomainUnloadedException()
    AppDomainUnloadedException(message: str)
    AppDomainUnloadedException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class ApplicationException(Exception):
    """
    ApplicationException()
    ApplicationException(message: str)
    ApplicationException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class ApplicationId(object):
    """ ApplicationId(publicKeyToken: Array[Byte], name: str, version: Version, processorArchitecture: str, culture: str) """
    def Copy(self):
        """ Copy(self: ApplicationId) -> ApplicationId """
        pass

    def Equals(self, o):
        """ Equals(self: ApplicationId, o: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ApplicationId) -> int """
        pass

    def ToString(self):
        """ ToString(self: ApplicationId) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, publicKeyToken, name, version, processorArchitecture, culture):
        """ __new__(cls: type, publicKeyToken: Array[Byte], name: str, version: Version, processorArchitecture: str, culture: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Culture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Culture(self: ApplicationId) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ApplicationId) -> str

"""

    ProcessorArchitecture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProcessorArchitecture(self: ApplicationId) -> str

"""

    PublicKeyToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PublicKeyToken(self: ApplicationId) -> Array[Byte]

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: ApplicationId) -> Version

"""



class ApplicationIdentity(object):
    """ ApplicationIdentity(applicationIdentityFullName: str) """
    def ToString(self):
        """ ToString(self: ApplicationIdentity) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, applicationIdentityFullName):
        """ __new__(cls: type, applicationIdentityFullName: str) """
        pass

    CodeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeBase(self: ApplicationIdentity) -> str

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: ApplicationIdentity) -> str

"""



class ArgIterator(object):
    """
    ArgIterator(arglist: RuntimeArgumentHandle)
    ArgIterator(arglist: RuntimeArgumentHandle, ptr: Void*)
    """
    def End(self):
        """ End(self: ArgIterator) """
        pass

    def Equals(self, o):
        """ Equals(self: ArgIterator, o: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ArgIterator) -> int """
        pass

    def GetNextArg(self, rth=None):
        """
        GetNextArg(self: ArgIterator, rth: RuntimeTypeHandle) -> TypedReference
        GetNextArg(self: ArgIterator) -> TypedReference
        """
        pass

    def GetNextArgType(self):
        """ GetNextArgType(self: ArgIterator) -> RuntimeTypeHandle """
        pass

    def GetRemainingCount(self):
        """ GetRemainingCount(self: ArgIterator) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, arglist, ptr=None):
        """
        __new__(cls: type, arglist: RuntimeArgumentHandle)
        __new__(cls: type, arglist: RuntimeArgumentHandle, ptr: Void*)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass


class ArgumentException(SystemException):
    """
    ArgumentException()
    ArgumentException(message: str)
    ArgumentException(message: str, innerException: Exception)
    ArgumentException(message: str, paramName: str, innerException: Exception)
    ArgumentException(message: str, paramName: str)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: ArgumentException, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, message: str, paramName: str, innerException: Exception)
        __new__(cls: type, message: str, paramName: str)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: ArgumentException) -> str

"""

    ParamName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamName(self: ArgumentException) -> str

"""



class ArgumentNullException(ArgumentException):
    """
    ArgumentNullException()
    ArgumentNullException(paramName: str)
    ArgumentNullException(message: str, innerException: Exception)
    ArgumentNullException(paramName: str, message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, paramName: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, paramName: str, message: str)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class ArgumentOutOfRangeException(ArgumentException):
    """
    ArgumentOutOfRangeException()
    ArgumentOutOfRangeException(paramName: str)
    ArgumentOutOfRangeException(paramName: str, message: str)
    ArgumentOutOfRangeException(message: str, innerException: Exception)
    ArgumentOutOfRangeException(paramName: str, actualValue: object, message: str)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: ArgumentOutOfRangeException, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, paramName: str)
        __new__(cls: type, paramName: str, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, paramName: str, actualValue: object, message: str)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    ActualValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActualValue(self: ArgumentOutOfRangeException) -> object

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: ArgumentOutOfRangeException) -> str

"""



class ArithmeticException(SystemException):
    """
    ArithmeticException()
    ArithmeticException(message: str)
    ArithmeticException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class ICloneable:
    # no doc
    def Clone(self):
        """ Clone(self: ICloneable) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Array(object):
    # no doc
    @staticmethod
    def AsReadOnly(array):
        """ AsReadOnly[T](array: Array[T]) -> ReadOnlyCollection[T] """
        pass

    @staticmethod
    def BinarySearch(array, *__args):
        """
        BinarySearch[T](array: Array[T], value: T, comparer: IComparer[T]) -> int
        BinarySearch[T](array: Array[T], value: T) -> int
        BinarySearch[T](array: Array[T], index: int, length: int, value: T, comparer: IComparer[T]) -> int
        BinarySearch[T](array: Array[T], index: int, length: int, value: T) -> int
        BinarySearch(array: Array, index: int, length: int, value: object) -> int
        BinarySearch(array: Array, value: object) -> int
        BinarySearch(array: Array, index: int, length: int, value: object, comparer: IComparer) -> int
        BinarySearch(array: Array, value: object, comparer: IComparer) -> int
        """
        pass

    @staticmethod
    def Clear(array, index, length):
        """ Clear(array: Array, index: int, length: int) """
        pass

    def Clone(self):
        """ Clone(self: Array) -> object """
        pass

    @staticmethod
    def ConstrainedCopy(sourceArray, sourceIndex, destinationArray, destinationIndex, length):
        """ ConstrainedCopy(sourceArray: Array, sourceIndex: int, destinationArray: Array, destinationIndex: int, length: int) """
        pass

    @staticmethod
    def ConvertAll(array, converter):
        """ ConvertAll[(TInput, TOutput)](array: Array[TInput], converter: Converter[TInput, TOutput]) -> Array[TOutput] """
        pass

    @staticmethod
    def Copy(sourceArray, *__args):
        """ Copy(sourceArray: Array, destinationArray: Array, length: Int64)Copy(sourceArray: Array, sourceIndex: Int64, destinationArray: Array, destinationIndex: Int64, length: Int64)Copy(sourceArray: Array, destinationArray: Array, length: int)Copy(sourceArray: Array, sourceIndex: int, destinationArray: Array, destinationIndex: int, length: int) """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: Array, array: Array, index: Int64)CopyTo(self: Array, array: Array, index: int) """
        pass

    @staticmethod
    def CreateInstance(elementType, *__args):
        """
        CreateInstance(elementType: Type, *lengths: Array[int]) -> Array
        CreateInstance(elementType: Type, *lengths: Array[Int64]) -> Array
        CreateInstance(elementType: Type, lengths: Array[int], lowerBounds: Array[int]) -> Array
        CreateInstance(elementType: Type, length: int) -> Array
        CreateInstance(elementType: Type, length1: int, length2: int) -> Array
        CreateInstance(elementType: Type, length1: int, length2: int, length3: int) -> Array
        """
        pass

    @staticmethod
    def Empty():
        """ Empty[T]() -> Array[T] """
        pass

    @staticmethod
    def Exists(array, match):
        """ Exists[T](array: Array[T], match: Predicate[T]) -> bool """
        pass

    @staticmethod
    def Find(array, match):
        """ Find[T](array: Array[T], match: Predicate[T]) -> T """
        pass

    @staticmethod
    def FindAll(array, match):
        """ FindAll[T](array: Array[T], match: Predicate[T]) -> Array[T] """
        pass

    @staticmethod
    def FindIndex(array, *__args):
        """
        FindIndex[T](array: Array[T], startIndex: int, count: int, match: Predicate[T]) -> int
        FindIndex[T](array: Array[T], startIndex: int, match: Predicate[T]) -> int
        FindIndex[T](array: Array[T], match: Predicate[T]) -> int
        """
        pass

    @staticmethod
    def FindLast(array, match):
        """ FindLast[T](array: Array[T], match: Predicate[T]) -> T """
        pass

    @staticmethod
    def FindLastIndex(array, *__args):
        """
        FindLastIndex[T](array: Array[T], startIndex: int, count: int, match: Predicate[T]) -> int
        FindLastIndex[T](array: Array[T], startIndex: int, match: Predicate[T]) -> int
        FindLastIndex[T](array: Array[T], match: Predicate[T]) -> int
        """
        pass

    @staticmethod
    def ForEach(array, action):
        """ ForEach[T](array: Array[T], action: Action[T]) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: Array) -> IEnumerator """
        pass

    def GetLength(self, dimension):
        """ GetLength(self: Array, dimension: int) -> int """
        pass

    def GetLongLength(self, dimension):
        """ GetLongLength(self: Array, dimension: int) -> Int64 """
        pass

    def GetLowerBound(self, dimension):
        """ GetLowerBound(self: Array, dimension: int) -> int """
        pass

    def GetUpperBound(self, dimension):
        """ GetUpperBound(self: Array, dimension: int) -> int """
        pass

    def GetValue(self, *__args):
        """
        GetValue(self: Array, index1: Int64, index2: Int64) -> object
        GetValue(self: Array, index: Int64) -> object
        GetValue(self: Array, *indices: Array[Int64]) -> object
        GetValue(self: Array, index1: Int64, index2: Int64, index3: Int64) -> object
        GetValue(self: Array, index: int) -> object
        GetValue(self: Array, *indices: Array[int]) -> object
        GetValue(self: Array, index1: int, index2: int, index3: int) -> object
        GetValue(self: Array, index1: int, index2: int) -> object
        """
        pass

    @staticmethod
    def IndexOf(array, value, startIndex=None, count=None):
        """
        IndexOf[T](array: Array[T], value: T) -> int
        IndexOf[T](array: Array[T], value: T, startIndex: int) -> int
        IndexOf[T](array: Array[T], value: T, startIndex: int, count: int) -> int
        IndexOf(array: Array, value: object) -> int
        IndexOf(array: Array, value: object, startIndex: int) -> int
        IndexOf(array: Array, value: object, startIndex: int, count: int) -> int
        """
        pass

    def Initialize(self):
        """ Initialize(self: Array) """
        pass

    @staticmethod
    def LastIndexOf(array, value, startIndex=None, count=None):
        """
        LastIndexOf[T](array: Array[T], value: T) -> int
        LastIndexOf[T](array: Array[T], value: T, startIndex: int) -> int
        LastIndexOf[T](array: Array[T], value: T, startIndex: int, count: int) -> int
        LastIndexOf(array: Array, value: object) -> int
        LastIndexOf(array: Array, value: object, startIndex: int) -> int
        LastIndexOf(array: Array, value: object, startIndex: int, count: int) -> int
        """
        pass

    @staticmethod
    def Resize(array, newSize):
        """ Resize[T](array: Array[T], newSize: int) -> Array[T] """
        pass

    @staticmethod
    def Reverse(array, index=None, length=None):
        """ Reverse(array: Array, index: int, length: int)Reverse(array: Array) """
        pass

    def SetValue(self, value, *__args):
        """ SetValue(self: Array, value: object, index1: Int64, index2: Int64)SetValue(self: Array, value: object, index: Int64)SetValue(self: Array, value: object, *indices: Array[Int64])SetValue(self: Array, value: object, index1: Int64, index2: Int64, index3: Int64)SetValue(self: Array, value: object, index1: int, index2: int)SetValue(self: Array, value: object, index: int)SetValue(self: Array, value: object, *indices: Array[int])SetValue(self: Array, value: object, index1: int, index2: int, index3: int) """
        pass

    @staticmethod
    def Sort(*__args):
        """ Sort[(TKey, TValue)](keys: Array[TKey], items: Array[TValue], index: int, length: int)Sort[T](array: Array[T], comparer: IComparer[T])Sort[(TKey, TValue)](keys: Array[TKey], items: Array[TValue])Sort[T](array: Array[T], index: int, length: int)Sort[(TKey, TValue)](keys: Array[TKey], items: Array[TValue], index: int, length: int, comparer: IComparer[TKey])Sort[T](array: Array[T], comparison: Comparison[T])Sort[(TKey, TValue)](keys: Array[TKey], items: Array[TValue], comparer: IComparer[TKey])Sort[T](array: Array[T], index: int, length: int, comparer: IComparer[T])Sort[T](array: Array[T])Sort(array: Array, index: int, length: int)Sort(keys: Array, items: Array, index: int, length: int)Sort(array: Array)Sort(keys: Array, items: Array)Sort(array: Array, index: int, length: int, comparer: IComparer)Sort(keys: Array, items: Array, index: int, length: int, comparer: IComparer)Sort(array: Array, comparer: IComparer)Sort(keys: Array, items: Array, comparer: IComparer) """
        pass

    @staticmethod
    def TrueForAll(array, match):
        """ TrueForAll[T](array: Array[T], match: Predicate[T]) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IList, value: object) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(pythonType: type, items: object) -> object
        __new__(pythonType: type, items: ICollection) -> object
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(data1: Array, data2: Array) -> Array """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        pass

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFixedSize(self: Array) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: Array) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: Array) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Array) -> int

"""

    LongLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LongLength(self: Array) -> Int64

"""

    Rank = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rank(self: Array) -> int

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: Array) -> object

"""



class ArraySegment(object):
    """
    ArraySegment[T](array: Array[T])
    ArraySegment[T](array: Array[T], offset: int, count: int)
    """
    def Equals(self, obj):
        """
        Equals(self: ArraySegment[T], obj: ArraySegment[T]) -> bool
        Equals(self: ArraySegment[T], obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ArraySegment[T]) -> int """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[T], item: T) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, array, offset=None, count=None):
        """
        __new__[ArraySegment`1]() -> ArraySegment[T]
        
        __new__(cls: type, array: Array[T])
        __new__(cls: type, array: Array[T], offset: int, count: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Array = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Array(self: ArraySegment[T]) -> Array[T]

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ArraySegment[T]) -> int

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: ArraySegment[T]) -> int

"""



class ArrayTypeMismatchException(SystemException):
    """
    ArrayTypeMismatchException()
    ArrayTypeMismatchException(message: str)
    ArrayTypeMismatchException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class EventArgs(object):
    """ EventArgs() """
    Empty = None


class AssemblyLoadEventArgs(EventArgs):
    """ AssemblyLoadEventArgs(loadedAssembly: Assembly) """
    @staticmethod # known case of __new__
    def __new__(self, loadedAssembly):
        """ __new__(cls: type, loadedAssembly: Assembly) """
        pass

    LoadedAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadedAssembly(self: AssemblyLoadEventArgs) -> Assembly

"""



class AssemblyLoadEventHandler(MulticastDelegate):
    """ AssemblyLoadEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: AssemblyLoadEventHandler, sender: object, args: AssemblyLoadEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: AssemblyLoadEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: AssemblyLoadEventHandler, sender: object, args: AssemblyLoadEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class AsyncCallback(MulticastDelegate):
    """ AsyncCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, ar, callback, object):
        """ BeginInvoke(self: AsyncCallback, ar: IAsyncResult, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: AsyncCallback, result: IAsyncResult) """
        pass

    def Invoke(self, ar):
        """ Invoke(self: AsyncCallback, ar: IAsyncResult) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class Attribute(object):
    # no doc
    def Equals(self, obj):
        """ Equals(self: Attribute, obj: object) -> bool """
        pass

    @staticmethod
    def GetCustomAttribute(element, attributeType, inherit=None):
        """
        GetCustomAttribute(element: Module, attributeType: Type, inherit: bool) -> Attribute
        GetCustomAttribute(element: Module, attributeType: Type) -> Attribute
        GetCustomAttribute(element: Assembly, attributeType: Type, inherit: bool) -> Attribute
        GetCustomAttribute(element: Assembly, attributeType: Type) -> Attribute
        GetCustomAttribute(element: MemberInfo, attributeType: Type, inherit: bool) -> Attribute
        GetCustomAttribute(element: MemberInfo, attributeType: Type) -> Attribute
        GetCustomAttribute(element: ParameterInfo, attributeType: Type, inherit: bool) -> Attribute
        GetCustomAttribute(element: ParameterInfo, attributeType: Type) -> Attribute
        """
        pass

    @staticmethod
    def GetCustomAttributes(element, *__args):
        """
        GetCustomAttributes(element: Module, inherit: bool) -> Array[Attribute]
        GetCustomAttributes(element: Module, attributeType: Type, inherit: bool) -> Array[Attribute]
        GetCustomAttributes(element: Module, attributeType: Type) -> Array[Attribute]
        GetCustomAttributes(element: Module) -> Array[Attribute]
        GetCustomAttributes(element: Assembly) -> Array[Attribute]
        GetCustomAttributes(element: Assembly, inherit: bool) -> Array[Attribute]
        GetCustomAttributes(element: Assembly, attributeType: Type) -> Array[Attribute]
        GetCustomAttributes(element: Assembly, attributeType: Type, inherit: bool) -> Array[Attribute]
        GetCustomAttributes(element: MemberInfo) -> Array[Attribute]
        GetCustomAttributes(element: MemberInfo, inherit: bool) -> Array[Attribute]
        GetCustomAttributes(element: MemberInfo, type: Type) -> Array[Attribute]
        GetCustomAttributes(element: MemberInfo, type: Type, inherit: bool) -> Array[Attribute]
        GetCustomAttributes(element: ParameterInfo, attributeType: Type, inherit: bool) -> Array[Attribute]
        GetCustomAttributes(element: ParameterInfo, inherit: bool) -> Array[Attribute]
        GetCustomAttributes(element: ParameterInfo) -> Array[Attribute]
        GetCustomAttributes(element: ParameterInfo, attributeType: Type) -> Array[Attribute]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Attribute) -> int """
        pass

    def IsDefaultAttribute(self):
        """ IsDefaultAttribute(self: Attribute) -> bool """
        pass

    @staticmethod
    def IsDefined(element, attributeType, inherit=None):
        """
        IsDefined(element: Module, attributeType: Type, inherit: bool) -> bool
        IsDefined(element: Module, attributeType: Type) -> bool
        IsDefined(element: Assembly, attributeType: Type, inherit: bool) -> bool
        IsDefined(element: Assembly, attributeType: Type) -> bool
        IsDefined(element: MemberInfo, attributeType: Type, inherit: bool) -> bool
        IsDefined(element: MemberInfo, attributeType: Type) -> bool
        IsDefined(element: ParameterInfo, attributeType: Type, inherit: bool) -> bool
        IsDefined(element: ParameterInfo, attributeType: Type) -> bool
        """
        pass

    def Match(self, obj):
        """ Match(self: Attribute, obj: object) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    TypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeId(self: Attribute) -> object

"""



class AttributeTargets(Enum):
    """ enum (flags) AttributeTargets, values: All (32767), Assembly (1), Class (4), Constructor (32), Delegate (4096), Enum (16), Event (512), Field (256), GenericParameter (16384), Interface (1024), Method (64), Module (2), Parameter (2048), Property (128), ReturnValue (8192), Struct (8) """
    All = None
    Assembly = None
    Class = None
    Constructor = None
    Delegate = None
    Enum = None
    Event = None
    Field = None
    GenericParameter = None
    Interface = None
    Method = None
    Module = None
    Parameter = None
    Property = None
    ReturnValue = None
    Struct = None
    value__ = None


class AttributeUsageAttribute(Attribute):
    """ AttributeUsageAttribute(validOn: AttributeTargets) """
    @staticmethod # known case of __new__
    def __new__(self, validOn):
        """ __new__(cls: type, validOn: AttributeTargets) """
        pass

    AllowMultiple = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowMultiple(self: AttributeUsageAttribute) -> bool

Set: AllowMultiple(self: AttributeUsageAttribute) = value
"""

    Inherited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Inherited(self: AttributeUsageAttribute) -> bool

Set: Inherited(self: AttributeUsageAttribute) = value
"""

    ValidOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValidOn(self: AttributeUsageAttribute) -> AttributeTargets

"""



class BadImageFormatException(SystemException):
    """
    BadImageFormatException()
    BadImageFormatException(message: str)
    BadImageFormatException(message: str, inner: Exception)
    BadImageFormatException(message: str, fileName: str)
    BadImageFormatException(message: str, fileName: str, inner: Exception)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: BadImageFormatException, info: SerializationInfo, context: StreamingContext) """
        pass

    def ToString(self):
        """ ToString(self: BadImageFormatException) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, message: str, fileName: str)
        __new__(cls: type, message: str, fileName: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: BadImageFormatException) -> str

"""

    FusionLog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FusionLog(self: BadImageFormatException) -> str

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: BadImageFormatException) -> str

"""



class Base64FormattingOptions(Enum):
    """ enum (flags) Base64FormattingOptions, values: InsertLineBreaks (1), None (0) """
    InsertLineBreaks = None
    None = None
    value__ = None


class BitConverter(object):
    # no doc
    @staticmethod
    def DoubleToInt64Bits(value):
        """ DoubleToInt64Bits(value: float) -> Int64 """
        pass

    @staticmethod
    def GetBytes(value):
        """
        GetBytes(value: UInt32) -> Array[Byte]
        GetBytes(value: UInt16) -> Array[Byte]
        GetBytes(value: UInt64) -> Array[Byte]
        GetBytes(value: float) -> Array[Byte]
        GetBytes(value: Single) -> Array[Byte]
        GetBytes(value: Char) -> Array[Byte]
        GetBytes(value: bool) -> Array[Byte]
        GetBytes(value: Int16) -> Array[Byte]
        GetBytes(value: Int64) -> Array[Byte]
        GetBytes(value: int) -> Array[Byte]
        """
        pass

    @staticmethod
    def Int64BitsToDouble(value):
        """ Int64BitsToDouble(value: Int64) -> float """
        pass

    @staticmethod
    def ToBoolean(value, startIndex):
        """ ToBoolean(value: Array[Byte], startIndex: int) -> bool """
        pass

    @staticmethod
    def ToChar(value, startIndex):
        """ ToChar(value: Array[Byte], startIndex: int) -> Char """
        pass

    @staticmethod
    def ToDouble(value, startIndex):
        """ ToDouble(value: Array[Byte], startIndex: int) -> float """
        pass

    @staticmethod
    def ToInt16(value, startIndex):
        """ ToInt16(value: Array[Byte], startIndex: int) -> Int16 """
        pass

    @staticmethod
    def ToInt32(value, startIndex):
        """ ToInt32(value: Array[Byte], startIndex: int) -> int """
        pass

    @staticmethod
    def ToInt64(value, startIndex):
        """ ToInt64(value: Array[Byte], startIndex: int) -> Int64 """
        pass

    @staticmethod
    def ToSingle(value, startIndex):
        """ ToSingle(value: Array[Byte], startIndex: int) -> Single """
        pass

    @staticmethod
    def ToString(value=None, startIndex=None, length=None):
        """
        ToString(value: Array[Byte], startIndex: int) -> str
        ToString(value: Array[Byte]) -> str
        ToString(value: Array[Byte], startIndex: int, length: int) -> str
        """
        pass

    @staticmethod
    def ToUInt16(value, startIndex):
        """ ToUInt16(value: Array[Byte], startIndex: int) -> UInt16 """
        pass

    @staticmethod
    def ToUInt32(value, startIndex):
        """ ToUInt32(value: Array[Byte], startIndex: int) -> UInt32 """
        pass

    @staticmethod
    def ToUInt64(value, startIndex):
        """ ToUInt64(value: Array[Byte], startIndex: int) -> UInt64 """
        pass

    IsLittleEndian = True
    __all__ = [
        'DoubleToInt64Bits',
        'GetBytes',
        'Int64BitsToDouble',
        'IsLittleEndian',
        'ToBoolean',
        'ToChar',
        'ToDouble',
        'ToInt16',
        'ToInt32',
        'ToInt64',
        'ToSingle',
        'ToString',
        'ToUInt16',
        'ToUInt32',
        'ToUInt64',
    ]


class Int32(object):
    # no doc
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: int) -> int """
        pass

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: int) -> int """
        pass

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: int, y: int) -> int """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __coerce__(self, *args): #cannot find CLR method
        """ __coerce__(x: int, o: object) -> object """
        pass

    def __divmod__(self, *args): #cannot find CLR method
        """
        __divmod__(x: int, y: object) -> object
        __divmod__(x: int, y: int) -> tuple
        """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __float__(self, *args): #cannot find CLR method
        """ __float__(self: int) -> float """
        pass

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//y """
        pass

    def __getnewargs__(self, *args): #cannot find CLR method
        """ __getnewargs__(self: int) -> object """
        pass

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(x: int) -> str """
        pass

    def __index__(self, *args): #cannot find CLR method
        """ __index__(self: int) -> int """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(self: int) -> int """
        pass

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: int) -> int """
        pass

    def __long__(self, *args): #cannot find CLR method
        """ __long__(self: int) -> long """
        pass

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<yx.__rshift__(y) <==> x<<y """
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, s: IList[Byte]) -> object
        __new__(cls: type, x: object) -> object
        __new__(cls: type) -> object
        __new__(o: object) -> object
        __new__(cls: type, o: Extensible[float]) -> object
        __new__(cls: type, s: str, radix: int) -> object
        """
        pass

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: int) -> bool """
        pass

    def __oct__(self, *args): #cannot find CLR method
        """ __oct__(x: int) -> str """
        pass

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: int, y: int) -> int """
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: int) -> int """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: int, y: int) -> object """
        pass

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: int, y: int) -> int """
        pass

    def __rdivmod__(self, *args): #cannot find CLR method
        """ __rdivmod__(x: int, y: int) -> object """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: int, y: int) -> object """
        pass

    def __rfloordiv__(self, *args): #cannot find CLR method
        """ __rfloordiv__(x: int, y: int) -> object """
        pass

    def __rlshift__(self, *args): #cannot find CLR method
        """ __rlshift__(x: int, y: int) -> object """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: int, y: int) -> int """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: int, y: int) -> object """
        pass

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: int, y: int) -> int """
        pass

    def __rpow__(self, *args): #cannot find CLR method
        """
        __rpow__(x: int, power: int, qmod: Nullable[int]) -> object
        __rpow__(x: int, power: int) -> object
        __rpow__(x: int, power: long, qmod: long) -> object
        __rpow__(x: int, power: float, qmod: float) -> object
        """
        pass

    def __rrshift__(self, *args): #cannot find CLR method
        """ __rrshift__(x: int, y: int) -> int """
        pass

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: int, y: int) -> object """
        pass

    def __rtruediv__(self, *args): #cannot find CLR method
        """ __rtruediv__(x: int, y: int) -> float """
        pass

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: int, y: int) -> int """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/y """
        pass

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: int) -> int """
        pass

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: int, y: int) -> int """
        pass

    denominator = None
    imag = None
    numerator = None
    real = None


class Boolean(int):
    # no doc
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: object, o: object) -> bool
        __new__(cls: object) -> object
        """
        pass


class Buffer(object):
    # no doc
    @staticmethod
    def BlockCopy(src, srcOffset, dst, dstOffset, count):
        """ BlockCopy(src: Array, srcOffset: int, dst: Array, dstOffset: int, count: int) """
        pass

    @staticmethod
    def ByteLength(array):
        """ ByteLength(array: Array) -> int """
        pass

    @staticmethod
    def GetByte(array, index):
        """ GetByte(array: Array, index: int) -> Byte """
        pass

    @staticmethod
    def MemoryCopy(source, destination, destinationSizeInBytes, sourceBytesToCopy):
        """ MemoryCopy(source: Void*, destination: Void*, destinationSizeInBytes: UInt64, sourceBytesToCopy: UInt64)MemoryCopy(source: Void*, destination: Void*, destinationSizeInBytes: Int64, sourceBytesToCopy: Int64) """
        pass

    @staticmethod
    def SetByte(array, index, value):
        """ SetByte(array: Array, index: int, value: Byte) """
        pass

    __all__ = [
        'BlockCopy',
        'ByteLength',
        'GetByte',
        'MemoryCopy',
        'SetByte',
    ]


class Byte(object):
    # no doc
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: Byte) -> int """
        pass

    def CompareTo(self, value):
        """
        CompareTo(self: Byte, value: Byte) -> int
        CompareTo(self: Byte, value: object) -> int
        """
        pass

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: Byte) -> Byte """
        pass

    def Equals(self, obj):
        """
        Equals(self: Byte, obj: Byte) -> bool
        Equals(self: Byte, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Byte) -> int """
        pass

    def GetTypeCode(self):
        """ GetTypeCode(self: Byte) -> TypeCode """
        pass

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str, provider: IFormatProvider) -> Byte
        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> Byte
        Parse(s: str) -> Byte
        Parse(s: str, style: NumberStyles) -> Byte
        """
        pass

    def ToString(self, *__args):
        """
        ToString(self: Byte, provider: IFormatProvider) -> str
        ToString(self: Byte, format: str, provider: IFormatProvider) -> str
        ToString(self: Byte) -> str
        ToString(self: Byte, format: str) -> str
        """
        pass

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, Byte)
        TryParse(s: str) -> (bool, Byte)
        """
        pass

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __and__(self, *args): #cannot find CLR method
        """
        __and__(x: Byte, y: SByte) -> Int16
        __and__(x: Byte, y: Byte) -> Byte
        """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        pass

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: Byte) -> float """
        pass

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//yx.__floordiv__(y) <==> x//y """
        pass

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(value: Byte) -> str """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: Byte) -> int """
        pass

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: Byte) -> object """
        pass

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<yx.__rshift__(y) <==> x<<y """
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%yx.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, value: object) -> object
        __new__(cls: type) -> object
        """
        pass

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: Byte) -> bool """
        pass

    def __or__(self, *args): #cannot find CLR method
        """
        __or__(x: Byte, y: SByte) -> Int16
        __or__(x: Byte, y: Byte) -> Byte
        """
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: Byte) -> Byte """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(x: SByte, y: Byte) -> object
        __radd__(x: Byte, y: Byte) -> object
        """
        pass

    def __rand__(self, *args): #cannot find CLR method
        """
        __rand__(x: SByte, y: Byte) -> Int16
        __rand__(x: Byte, y: Byte) -> Byte
        """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(x: SByte, y: Byte) -> object
        __rdiv__(x: Byte, y: Byte) -> object
        """
        pass

    def __rfloordiv__(self, *args): #cannot find CLR method
        """
        __rfloordiv__(x: SByte, y: Byte) -> object
        __rfloordiv__(x: Byte, y: Byte) -> Byte
        """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """
        __rmod__(x: SByte, y: Byte) -> Int16
        __rmod__(x: Byte, y: Byte) -> Byte
        """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(x: SByte, y: Byte) -> object
        __rmul__(x: Byte, y: Byte) -> object
        """
        pass

    def __ror__(self, *args): #cannot find CLR method
        """
        __ror__(x: SByte, y: Byte) -> Int16
        __ror__(x: Byte, y: Byte) -> Byte
        """
        pass

    def __rpow__(self, *args): #cannot find CLR method
        """
        __rpow__(x: SByte, y: Byte) -> object
        __rpow__(x: Byte, y: Byte) -> object
        """
        pass

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(x: SByte, y: Byte) -> object
        __rsub__(x: Byte, y: Byte) -> object
        """
        pass

    def __rtruediv__(self, *args): #cannot find CLR method
        """
        __rtruediv__(x: SByte, y: Byte) -> float
        __rtruediv__(x: Byte, y: Byte) -> float
        """
        pass

    def __rxor__(self, *args): #cannot find CLR method
        """
        __rxor__(x: SByte, y: Byte) -> Int16
        __rxor__(x: Byte, y: Byte) -> Byte
        """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/yx.__truediv__(y) <==> x/y """
        pass

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: Byte) -> Byte """
        pass

    def __xor__(self, *args): #cannot find CLR method
        """
        __xor__(x: Byte, y: SByte) -> Int16
        __xor__(x: Byte, y: Byte) -> Byte
        """
        pass

    denominator = None
    imag = None
    MaxValue = None
    MinValue = None
    numerator = None
    real = None


class CannotUnloadAppDomainException(SystemException):
    """
    CannotUnloadAppDomainException()
    CannotUnloadAppDomainException(message: str)
    CannotUnloadAppDomainException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class Char(object):
    # no doc
    def CompareTo(self, value):
        """
        CompareTo(self: Char, value: Char) -> int
        CompareTo(self: Char, value: object) -> int
        """
        pass

    @staticmethod
    def ConvertFromUtf32(utf32):
        """ ConvertFromUtf32(utf32: int) -> str """
        pass

    @staticmethod
    def ConvertToUtf32(*__args):
        """
        ConvertToUtf32(s: str, index: int) -> int
        ConvertToUtf32(highSurrogate: Char, lowSurrogate: Char) -> int
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Char, obj: Char) -> bool
        Equals(self: Char, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Char) -> int """
        pass

    @staticmethod
    def GetNumericValue(*__args):
        """
        GetNumericValue(s: str, index: int) -> float
        GetNumericValue(c: Char) -> float
        """
        pass

    def GetTypeCode(self):
        """ GetTypeCode(self: Char) -> TypeCode """
        pass

    @staticmethod
    def GetUnicodeCategory(*__args):
        """
        GetUnicodeCategory(s: str, index: int) -> UnicodeCategory
        GetUnicodeCategory(c: Char) -> UnicodeCategory
        """
        pass

    @staticmethod
    def IsControl(*__args):
        """
        IsControl(s: str, index: int) -> bool
        IsControl(c: Char) -> bool
        """
        pass

    @staticmethod
    def IsDigit(*__args):
        """
        IsDigit(s: str, index: int) -> bool
        IsDigit(c: Char) -> bool
        """
        pass

    @staticmethod
    def IsHighSurrogate(*__args):
        """
        IsHighSurrogate(s: str, index: int) -> bool
        IsHighSurrogate(c: Char) -> bool
        """
        pass

    @staticmethod
    def IsLetter(*__args):
        """
        IsLetter(s: str, index: int) -> bool
        IsLetter(c: Char) -> bool
        """
        pass

    @staticmethod
    def IsLetterOrDigit(*__args):
        """
        IsLetterOrDigit(s: str, index: int) -> bool
        IsLetterOrDigit(c: Char) -> bool
        """
        pass

    @staticmethod
    def IsLower(*__args):
        """
        IsLower(s: str, index: int) -> bool
        IsLower(c: Char) -> bool
        """
        pass

    @staticmethod
    def IsLowSurrogate(*__args):
        """
        IsLowSurrogate(s: str, index: int) -> bool
        IsLowSurrogate(c: Char) -> bool
        """
        pass

    @staticmethod
    def IsNumber(*__args):
        """
        IsNumber(s: str, index: int) -> bool
        IsNumber(c: Char) -> bool
        """
        pass

    @staticmethod
    def IsPunctuation(*__args):
        """
        IsPunctuation(s: str, index: int) -> bool
        IsPunctuation(c: Char) -> bool
        """
        pass

    @staticmethod
    def IsSeparator(*__args):
        """
        IsSeparator(s: str, index: int) -> bool
        IsSeparator(c: Char) -> bool
        """
        pass

    @staticmethod
    def IsSurrogate(*__args):
        """
        IsSurrogate(s: str, index: int) -> bool
        IsSurrogate(c: Char) -> bool
        """
        pass

    @staticmethod
    def IsSurrogatePair(*__args):
        """
        IsSurrogatePair(highSurrogate: Char, lowSurrogate: Char) -> bool
        IsSurrogatePair(s: str, index: int) -> bool
        """
        pass

    @staticmethod
    def IsSymbol(*__args):
        """
        IsSymbol(s: str, index: int) -> bool
        IsSymbol(c: Char) -> bool
        """
        pass

    @staticmethod
    def IsUpper(*__args):
        """
        IsUpper(s: str, index: int) -> bool
        IsUpper(c: Char) -> bool
        """
        pass

    @staticmethod
    def IsWhiteSpace(*__args):
        """
        IsWhiteSpace(s: str, index: int) -> bool
        IsWhiteSpace(c: Char) -> bool
        """
        pass

    @staticmethod
    def Parse(s):
        """ Parse(s: str) -> Char """
        pass

    @staticmethod
    def ToLower(c, culture=None):
        """
        ToLower(c: Char) -> Char
        ToLower(c: Char, culture: CultureInfo) -> Char
        """
        pass

    @staticmethod
    def ToLowerInvariant(c):
        """ ToLowerInvariant(c: Char) -> Char """
        pass

    def ToString(self, *__args):
        """
        ToString(c: Char) -> str
        ToString(self: Char, provider: IFormatProvider) -> str
        ToString(self: Char) -> str
        """
        pass

    @staticmethod
    def ToUpper(c, culture=None):
        """
        ToUpper(c: Char) -> Char
        ToUpper(c: Char, culture: CultureInfo) -> Char
        """
        pass

    @staticmethod
    def ToUpperInvariant(c):
        """ ToUpperInvariant(c: Char) -> Char """
        pass

    @staticmethod
    def TryParse(s, result):
        """ TryParse(s: str) -> (bool, Char) """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: Char, other: str) -> bool
        __contains__(self: Char, other: Char) -> bool
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    MaxValue = None
    MinValue = None


class CharEnumerator(object):
    # no doc
    def Clone(self):
        """ Clone(self: CharEnumerator) -> object """
        pass

    def Dispose(self):
        """ Dispose(self: CharEnumerator) """
        pass

    def MoveNext(self):
        """ MoveNext(self: CharEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: CharEnumerator) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Char](enumerator: IEnumerator[Char], value: Char) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: CharEnumerator) -> Char

"""



class CLSCompliantAttribute(Attribute):
    """ CLSCompliantAttribute(isCompliant: bool) """
    @staticmethod # known case of __new__
    def __new__(self, isCompliant):
        """ __new__(cls: type, isCompliant: bool) """
        pass

    IsCompliant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCompliant(self: CLSCompliantAttribute) -> bool

"""



class Comparison(MulticastDelegate):
    """ Comparison[T](object: object, method: IntPtr) """
    def BeginInvoke(self, x, y, callback, object):
        """ BeginInvoke(self: Comparison[T], x: T, y: T, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: Comparison[T], result: IAsyncResult) -> int """
        pass

    def Invoke(self, x, y):
        """ Invoke(self: Comparison[T], x: T, y: T) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class Console(object):
    # no doc
    @staticmethod
    def Beep(frequency=None, duration=None):
        """ Beep(frequency: int, duration: int)Beep() """
        pass

    @staticmethod
    def Clear():
        """ Clear() """
        pass

    @staticmethod
    def MoveBufferArea(sourceLeft, sourceTop, sourceWidth, sourceHeight, targetLeft, targetTop, sourceChar=None, sourceForeColor=None, sourceBackColor=None):
        """ MoveBufferArea(sourceLeft: int, sourceTop: int, sourceWidth: int, sourceHeight: int, targetLeft: int, targetTop: int, sourceChar: Char, sourceForeColor: ConsoleColor, sourceBackColor: ConsoleColor)MoveBufferArea(sourceLeft: int, sourceTop: int, sourceWidth: int, sourceHeight: int, targetLeft: int, targetTop: int) """
        pass

    @staticmethod
    def OpenStandardError(bufferSize=None):
        """
        OpenStandardError(bufferSize: int) -> Stream
        OpenStandardError() -> Stream
        """
        pass

    @staticmethod
    def OpenStandardInput(bufferSize=None):
        """
        OpenStandardInput(bufferSize: int) -> Stream
        OpenStandardInput() -> Stream
        """
        pass

    @staticmethod
    def OpenStandardOutput(bufferSize=None):
        """
        OpenStandardOutput(bufferSize: int) -> Stream
        OpenStandardOutput() -> Stream
        """
        pass

    @staticmethod
    def Read():
        """ Read() -> int """
        pass

    @staticmethod
    def ReadKey(intercept=None):
        """
        ReadKey(intercept: bool) -> ConsoleKeyInfo
        ReadKey() -> ConsoleKeyInfo
        """
        pass

    @staticmethod
    def ReadLine():
        """ ReadLine() -> str """
        pass

    @staticmethod
    def ResetColor():
        """ ResetColor() """
        pass

    @staticmethod
    def SetBufferSize(width, height):
        """ SetBufferSize(width: int, height: int) """
        pass

    @staticmethod
    def SetCursorPosition(left, top):
        """ SetCursorPosition(left: int, top: int) """
        pass

    @staticmethod
    def SetError(newError):
        """ SetError(newError: TextWriter) """
        pass

    @staticmethod
    def SetIn(newIn):
        """ SetIn(newIn: TextReader) """
        pass

    @staticmethod
    def SetOut(newOut):
        """ SetOut(newOut: TextWriter) """
        pass

    @staticmethod
    def SetWindowPosition(left, top):
        """ SetWindowPosition(left: int, top: int) """
        pass

    @staticmethod
    def SetWindowSize(width, height):
        """ SetWindowSize(width: int, height: int) """
        pass

    @staticmethod
    def Write(*__args):
        """ Write(value: Single)Write(value: int)Write(value: float)Write(value: Decimal)Write(value: UInt32)Write(value: object)Write(value: str)Write(value: Int64)Write(value: UInt64)Write(format: str, arg0: object, arg1: object, arg2: object)Write(format: str, arg0: object, arg1: object, arg2: object, arg3: object)Write(format: str, arg0: object)Write(format: str, arg0: object, arg1: object)Write(format: str, *arg: Array[object])Write(buffer: Array[Char])Write(buffer: Array[Char], index: int, count: int)Write(value: bool)Write(value: Char) """
        pass

    @staticmethod
    def WriteLine(*__args):
        """ WriteLine(value: object)WriteLine(value: str)WriteLine(value: Int64)WriteLine(value: UInt64)WriteLine(format: str, arg0: object)WriteLine(format: str, arg0: object, arg1: object, arg2: object, arg3: object)WriteLine(format: str, *arg: Array[object])WriteLine(format: str, arg0: object, arg1: object)WriteLine(format: str, arg0: object, arg1: object, arg2: object)WriteLine(value: UInt32)WriteLine(value: Char)WriteLine(buffer: Array[Char])WriteLine()WriteLine(value: bool)WriteLine(buffer: Array[Char], index: int, count: int)WriteLine(value: Single)WriteLine(value: int)WriteLine(value: Decimal)WriteLine(value: float) """
        pass

    BackgroundColor = None
    BufferHeight = 1000
    BufferWidth = 212
    CancelKeyPress = None
    CapsLock = False
    CursorLeft = 0
    CursorSize = 25
    CursorTop = 999
    CursorVisible = True
    Error = None
    ForegroundColor = None
    In = None
    InputEncoding = None
    IsErrorRedirected = False
    IsInputRedirected = False
    IsOutputRedirected = False
    KeyAvailable = False
    LargestWindowHeight = 53
    LargestWindowWidth = 212
    NumberLock = False
    Out = None
    OutputEncoding = None
    Title = 'cmd - ipy64  generate.py'
    TreatControlCAsInput = False
    WindowHeight = 53
    WindowLeft = 0
    WindowTop = 947
    WindowWidth = 212
    __all__ = [
        'Beep',
        'CancelKeyPress',
        'Clear',
        'MoveBufferArea',
        'OpenStandardError',
        'OpenStandardInput',
        'OpenStandardOutput',
        'Read',
        'ReadKey',
        'ReadLine',
        'ResetColor',
        'SetBufferSize',
        'SetCursorPosition',
        'SetError',
        'SetIn',
        'SetOut',
        'SetWindowPosition',
        'SetWindowSize',
        'Write',
        'WriteLine',
    ]


class ConsoleCancelEventArgs(EventArgs):
    # no doc
    Cancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cancel(self: ConsoleCancelEventArgs) -> bool

Set: Cancel(self: ConsoleCancelEventArgs) = value
"""

    SpecialKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecialKey(self: ConsoleCancelEventArgs) -> ConsoleSpecialKey

"""



class ConsoleCancelEventHandler(MulticastDelegate):
    """ ConsoleCancelEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ConsoleCancelEventHandler, sender: object, e: ConsoleCancelEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ConsoleCancelEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ConsoleCancelEventHandler, sender: object, e: ConsoleCancelEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class ConsoleColor(Enum):
    """ enum ConsoleColor, values: Black (0), Blue (9), Cyan (11), DarkBlue (1), DarkCyan (3), DarkGray (8), DarkGreen (2), DarkMagenta (5), DarkRed (4), DarkYellow (6), Gray (7), Green (10), Magenta (13), Red (12), White (15), Yellow (14) """
    Black = None
    Blue = None
    Cyan = None
    DarkBlue = None
    DarkCyan = None
    DarkGray = None
    DarkGreen = None
    DarkMagenta = None
    DarkRed = None
    DarkYellow = None
    Gray = None
    Green = None
    Magenta = None
    Red = None
    value__ = None
    White = None
    Yellow = None


class ConsoleKey(Enum):
    """ enum ConsoleKey, values: A (65), Add (107), Applications (93), Attention (246), B (66), Backspace (8), BrowserBack (166), BrowserFavorites (171), BrowserForward (167), BrowserHome (172), BrowserRefresh (168), BrowserSearch (170), BrowserStop (169), C (67), Clear (12), CrSel (247), D (68), D0 (48), D1 (49), D2 (50), D3 (51), D4 (52), D5 (53), D6 (54), D7 (55), D8 (56), D9 (57), Decimal (110), Delete (46), Divide (111), DownArrow (40), E (69), End (35), Enter (13), EraseEndOfFile (249), Escape (27), Execute (43), ExSel (248), F (70), F1 (112), F10 (121), F11 (122), F12 (123), F13 (124), F14 (125), F15 (126), F16 (127), F17 (128), F18 (129), F19 (130), F2 (113), F20 (131), F21 (132), F22 (133), F23 (134), F24 (135), F3 (114), F4 (115), F5 (116), F6 (117), F7 (118), F8 (119), F9 (120), G (71), H (72), Help (47), Home (36), I (73), Insert (45), J (74), K (75), L (76), LaunchApp1 (182), LaunchApp2 (183), LaunchMail (180), LaunchMediaSelect (181), LeftArrow (37), LeftWindows (91), M (77), MediaNext (176), MediaPlay (179), MediaPrevious (177), MediaStop (178), Multiply (106), N (78), NoName (252), NumPad0 (96), NumPad1 (97), NumPad2 (98), NumPad3 (99), NumPad4 (100), NumPad5 (101), NumPad6 (102), NumPad7 (103), NumPad8 (104), NumPad9 (105), O (79), Oem1 (186), Oem102 (226), Oem2 (191), Oem3 (192), Oem4 (219), Oem5 (220), Oem6 (221), Oem7 (222), Oem8 (223), OemClear (254), OemComma (188), OemMinus (189), OemPeriod (190), OemPlus (187), P (80), Pa1 (253), Packet (231), PageDown (34), PageUp (33), Pause (19), Play (250), Print (42), PrintScreen (44), Process (229), Q (81), R (82), RightArrow (39), RightWindows (92), S (83), Select (41), Separator (108), Sleep (95), Spacebar (32), Subtract (109), T (84), Tab (9), U (85), UpArrow (38), V (86), VolumeDown (174), VolumeMute (173), VolumeUp (175), W (87), X (88), Y (89), Z (90), Zoom (251) """
    A = None
    Add = None
    Applications = None
    Attention = None
    B = None
    Backspace = None
    BrowserBack = None
    BrowserFavorites = None
    BrowserForward = None
    BrowserHome = None
    BrowserRefresh = None
    BrowserSearch = None
    BrowserStop = None
    C = None
    Clear = None
    CrSel = None
    D = None
    D0 = None
    D1 = None
    D2 = None
    D3 = None
    D4 = None
    D5 = None
    D6 = None
    D7 = None
    D8 = None
    D9 = None
    Decimal = None
    Delete = None
    Divide = None
    DownArrow = None
    E = None
    End = None
    Enter = None
    EraseEndOfFile = None
    Escape = None
    Execute = None
    ExSel = None
    F = None
    F1 = None
    F10 = None
    F11 = None
    F12 = None
    F13 = None
    F14 = None
    F15 = None
    F16 = None
    F17 = None
    F18 = None
    F19 = None
    F2 = None
    F20 = None
    F21 = None
    F22 = None
    F23 = None
    F24 = None
    F3 = None
    F4 = None
    F5 = None
    F6 = None
    F7 = None
    F8 = None
    F9 = None
    G = None
    H = None
    Help = None
    Home = None
    I = None
    Insert = None
    J = None
    K = None
    L = None
    LaunchApp1 = None
    LaunchApp2 = None
    LaunchMail = None
    LaunchMediaSelect = None
    LeftArrow = None
    LeftWindows = None
    M = None
    MediaNext = None
    MediaPlay = None
    MediaPrevious = None
    MediaStop = None
    Multiply = None
    N = None
    NoName = None
    NumPad0 = None
    NumPad1 = None
    NumPad2 = None
    NumPad3 = None
    NumPad4 = None
    NumPad5 = None
    NumPad6 = None
    NumPad7 = None
    NumPad8 = None
    NumPad9 = None
    O = None
    Oem1 = None
    Oem102 = None
    Oem2 = None
    Oem3 = None
    Oem4 = None
    Oem5 = None
    Oem6 = None
    Oem7 = None
    Oem8 = None
    OemClear = None
    OemComma = None
    OemMinus = None
    OemPeriod = None
    OemPlus = None
    P = None
    Pa1 = None
    Packet = None
    PageDown = None
    PageUp = None
    Pause = None
    Play = None
    Print = None
    PrintScreen = None
    Process = None
    Q = None
    R = None
    RightArrow = None
    RightWindows = None
    S = None
    Select = None
    Separator = None
    Sleep = None
    Spacebar = None
    Subtract = None
    T = None
    Tab = None
    U = None
    UpArrow = None
    V = None
    value__ = None
    VolumeDown = None
    VolumeMute = None
    VolumeUp = None
    W = None
    X = None
    Y = None
    Z = None
    Zoom = None


class ConsoleKeyInfo(object):
    """ ConsoleKeyInfo(keyChar: Char, key: ConsoleKey, shift: bool, alt: bool, control: bool) """
    def Equals(self, *__args):
        """
        Equals(self: ConsoleKeyInfo, obj: ConsoleKeyInfo) -> bool
        Equals(self: ConsoleKeyInfo, value: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ConsoleKeyInfo) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, keyChar, key, shift, alt, control):
        """
        __new__[ConsoleKeyInfo]() -> ConsoleKeyInfo
        
        __new__(cls: type, keyChar: Char, key: ConsoleKey, shift: bool, alt: bool, control: bool)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: ConsoleKeyInfo) -> ConsoleKey

"""

    KeyChar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyChar(self: ConsoleKeyInfo) -> Char

"""

    Modifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Modifiers(self: ConsoleKeyInfo) -> ConsoleModifiers

"""



class ConsoleModifiers(Enum):
    """ enum (flags) ConsoleModifiers, values: Alt (1), Control (4), Shift (2) """
    Alt = None
    Control = None
    Shift = None
    value__ = None


class ConsoleSpecialKey(Enum):
    """ enum ConsoleSpecialKey, values: ControlBreak (1), ControlC (0) """
    ControlBreak = None
    ControlC = None
    value__ = None


class ContextBoundObject(MarshalByRefObject):
    # no doc

class ContextMarshalException(SystemException):
    """
    ContextMarshalException()
    ContextMarshalException(message: str)
    ContextMarshalException(message: str, inner: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class ContextStaticAttribute(Attribute):
    """ ContextStaticAttribute() """

class Convert(object):
    # no doc
    @staticmethod
    def ChangeType(value, *__args):
        """
        ChangeType(value: object, conversionType: Type) -> object
        ChangeType(value: object, conversionType: Type, provider: IFormatProvider) -> object
        ChangeType(value: object, typeCode: TypeCode) -> object
        ChangeType(value: object, typeCode: TypeCode, provider: IFormatProvider) -> object
        """
        pass

    @staticmethod
    def FromBase64CharArray(inArray, offset, length):
        """ FromBase64CharArray(inArray: Array[Char], offset: int, length: int) -> Array[Byte] """
        pass

    @staticmethod
    def FromBase64String(s):
        """ FromBase64String(s: str) -> Array[Byte] """
        pass

    @staticmethod
    def GetTypeCode(value):
        """ GetTypeCode(value: object) -> TypeCode """
        pass

    @staticmethod
    def IsDBNull(value):
        """ IsDBNull(value: object) -> bool """
        pass

    @staticmethod
    def ToBase64CharArray(inArray, offsetIn, length, outArray, offsetOut, options=None):
        """
        ToBase64CharArray(inArray: Array[Byte], offsetIn: int, length: int, outArray: Array[Char], offsetOut: int, options: Base64FormattingOptions) -> int
        ToBase64CharArray(inArray: Array[Byte], offsetIn: int, length: int, outArray: Array[Char], offsetOut: int) -> int
        """
        pass

    @staticmethod
    def ToBase64String(inArray, *__args):
        """
        ToBase64String(inArray: Array[Byte], offset: int, length: int) -> str
        ToBase64String(inArray: Array[Byte], offset: int, length: int, options: Base64FormattingOptions) -> str
        ToBase64String(inArray: Array[Byte]) -> str
        ToBase64String(inArray: Array[Byte], options: Base64FormattingOptions) -> str
        """
        pass

    @staticmethod
    def ToBoolean(value, provider=None):
        """
        ToBoolean(value: UInt64) -> bool
        ToBoolean(value: str) -> bool
        ToBoolean(value: UInt32) -> bool
        ToBoolean(value: Int64) -> bool
        ToBoolean(value: str, provider: IFormatProvider) -> bool
        ToBoolean(value: Decimal) -> bool
        ToBoolean(value: DateTime) -> bool
        ToBoolean(value: Single) -> bool
        ToBoolean(value: float) -> bool
        ToBoolean(value: bool) -> bool
        ToBoolean(value: SByte) -> bool
        ToBoolean(value: object) -> bool
        ToBoolean(value: object, provider: IFormatProvider) -> bool
        ToBoolean(value: Char) -> bool
        ToBoolean(value: UInt16) -> bool
        ToBoolean(value: int) -> bool
        ToBoolean(value: Byte) -> bool
        ToBoolean(value: Int16) -> bool
        """
        pass

    @staticmethod
    def ToByte(value, *__args):
        """
        ToByte(value: Single) -> Byte
        ToByte(value: float) -> Byte
        ToByte(value: Int64) -> Byte
        ToByte(value: UInt64) -> Byte
        ToByte(value: Decimal) -> Byte
        ToByte(value: DateTime) -> Byte
        ToByte(value: str, fromBase: int) -> Byte
        ToByte(value: str) -> Byte
        ToByte(value: str, provider: IFormatProvider) -> Byte
        ToByte(value: UInt32) -> Byte
        ToByte(value: bool) -> Byte
        ToByte(value: Byte) -> Byte
        ToByte(value: object) -> Byte
        ToByte(value: object, provider: IFormatProvider) -> Byte
        ToByte(value: Char) -> Byte
        ToByte(value: UInt16) -> Byte
        ToByte(value: int) -> Byte
        ToByte(value: SByte) -> Byte
        ToByte(value: Int16) -> Byte
        """
        pass

    @staticmethod
    def ToChar(value, provider=None):
        """
        ToChar(value: UInt64) -> Char
        ToChar(value: str) -> Char
        ToChar(value: UInt32) -> Char
        ToChar(value: Int64) -> Char
        ToChar(value: str, provider: IFormatProvider) -> Char
        ToChar(value: Decimal) -> Char
        ToChar(value: DateTime) -> Char
        ToChar(value: Single) -> Char
        ToChar(value: float) -> Char
        ToChar(value: bool) -> Char
        ToChar(value: Char) -> Char
        ToChar(value: object) -> Char
        ToChar(value: object, provider: IFormatProvider) -> Char
        ToChar(value: SByte) -> Char
        ToChar(value: UInt16) -> Char
        ToChar(value: int) -> Char
        ToChar(value: Byte) -> Char
        ToChar(value: Int16) -> Char
        """
        pass

    @staticmethod
    def ToDateTime(value, provider=None):
        """
        ToDateTime(value: Int64) -> DateTime
        ToDateTime(value: UInt64) -> DateTime
        ToDateTime(value: int) -> DateTime
        ToDateTime(value: UInt32) -> DateTime
        ToDateTime(value: bool) -> DateTime
        ToDateTime(value: float) -> DateTime
        ToDateTime(value: Decimal) -> DateTime
        ToDateTime(value: Char) -> DateTime
        ToDateTime(value: Single) -> DateTime
        ToDateTime(value: object, provider: IFormatProvider) -> DateTime
        ToDateTime(value: str) -> DateTime
        ToDateTime(value: DateTime) -> DateTime
        ToDateTime(value: object) -> DateTime
        ToDateTime(value: str, provider: IFormatProvider) -> DateTime
        ToDateTime(value: Int16) -> DateTime
        ToDateTime(value: UInt16) -> DateTime
        ToDateTime(value: SByte) -> DateTime
        ToDateTime(value: Byte) -> DateTime
        """
        pass

    @staticmethod
    def ToDecimal(value, provider=None):
        """
        ToDecimal(value: Single) -> Decimal
        ToDecimal(value: float) -> Decimal
        ToDecimal(value: Int64) -> Decimal
        ToDecimal(value: UInt64) -> Decimal
        ToDecimal(value: str) -> Decimal
        ToDecimal(value: bool) -> Decimal
        ToDecimal(value: DateTime) -> Decimal
        ToDecimal(value: str, provider: IFormatProvider) -> Decimal
        ToDecimal(value: Decimal) -> Decimal
        ToDecimal(value: SByte) -> Decimal
        ToDecimal(value: Byte) -> Decimal
        ToDecimal(value: object) -> Decimal
        ToDecimal(value: object, provider: IFormatProvider) -> Decimal
        ToDecimal(value: Char) -> Decimal
        ToDecimal(value: int) -> Decimal
        ToDecimal(value: UInt32) -> Decimal
        ToDecimal(value: Int16) -> Decimal
        ToDecimal(value: UInt16) -> Decimal
        """
        pass

    @staticmethod
    def ToDouble(value, provider=None):
        """
        ToDouble(value: Single) -> float
        ToDouble(value: float) -> float
        ToDouble(value: Int64) -> float
        ToDouble(value: UInt64) -> float
        ToDouble(value: Decimal) -> float
        ToDouble(value: bool) -> float
        ToDouble(value: DateTime) -> float
        ToDouble(value: str) -> float
        ToDouble(value: str, provider: IFormatProvider) -> float
        ToDouble(value: SByte) -> float
        ToDouble(value: Byte) -> float
        ToDouble(value: object) -> float
        ToDouble(value: object, provider: IFormatProvider) -> float
        ToDouble(value: Int16) -> float
        ToDouble(value: int) -> float
        ToDouble(value: UInt32) -> float
        ToDouble(value: Char) -> float
        ToDouble(value: UInt16) -> float
        """
        pass

    @staticmethod
    def ToInt16(value, *__args):
        """
        ToInt16(value: Single) -> Int16
        ToInt16(value: float) -> Int16
        ToInt16(value: Int64) -> Int16
        ToInt16(value: UInt64) -> Int16
        ToInt16(value: Decimal) -> Int16
        ToInt16(value: DateTime) -> Int16
        ToInt16(value: str, fromBase: int) -> Int16
        ToInt16(value: str) -> Int16
        ToInt16(value: str, provider: IFormatProvider) -> Int16
        ToInt16(value: Int16) -> Int16
        ToInt16(value: bool) -> Int16
        ToInt16(value: Char) -> Int16
        ToInt16(value: object) -> Int16
        ToInt16(value: object, provider: IFormatProvider) -> Int16
        ToInt16(value: SByte) -> Int16
        ToInt16(value: int) -> Int16
        ToInt16(value: UInt32) -> Int16
        ToInt16(value: Byte) -> Int16
        ToInt16(value: UInt16) -> Int16
        """
        pass

    @staticmethod
    def ToInt32(value, *__args):
        """
        ToInt32(value: Single) -> int
        ToInt32(value: float) -> int
        ToInt32(value: Int64) -> int
        ToInt32(value: UInt64) -> int
        ToInt32(value: Decimal) -> int
        ToInt32(value: DateTime) -> int
        ToInt32(value: str, fromBase: int) -> int
        ToInt32(value: str) -> int
        ToInt32(value: str, provider: IFormatProvider) -> int
        ToInt32(value: int) -> int
        ToInt32(value: bool) -> int
        ToInt32(value: Char) -> int
        ToInt32(value: object) -> int
        ToInt32(value: object, provider: IFormatProvider) -> int
        ToInt32(value: SByte) -> int
        ToInt32(value: UInt16) -> int
        ToInt32(value: UInt32) -> int
        ToInt32(value: Byte) -> int
        ToInt32(value: Int16) -> int
        """
        pass

    @staticmethod
    def ToInt64(value, *__args):
        """
        ToInt64(value: Single) -> Int64
        ToInt64(value: float) -> Int64
        ToInt64(value: UInt64) -> Int64
        ToInt64(value: Int64) -> Int64
        ToInt64(value: Decimal) -> Int64
        ToInt64(value: DateTime) -> Int64
        ToInt64(value: str, fromBase: int) -> Int64
        ToInt64(value: str) -> Int64
        ToInt64(value: str, provider: IFormatProvider) -> Int64
        ToInt64(value: UInt32) -> Int64
        ToInt64(value: bool) -> Int64
        ToInt64(value: Char) -> Int64
        ToInt64(value: object) -> Int64
        ToInt64(value: object, provider: IFormatProvider) -> Int64
        ToInt64(value: SByte) -> Int64
        ToInt64(value: UInt16) -> Int64
        ToInt64(value: int) -> Int64
        ToInt64(value: Byte) -> Int64
        ToInt64(value: Int16) -> Int64
        """
        pass

    @staticmethod
    def ToSByte(value, *__args):
        """
        ToSByte(value: Single) -> SByte
        ToSByte(value: float) -> SByte
        ToSByte(value: Int64) -> SByte
        ToSByte(value: UInt64) -> SByte
        ToSByte(value: Decimal) -> SByte
        ToSByte(value: DateTime) -> SByte
        ToSByte(value: str, fromBase: int) -> SByte
        ToSByte(value: str) -> SByte
        ToSByte(value: str, provider: IFormatProvider) -> SByte
        ToSByte(value: UInt32) -> SByte
        ToSByte(value: bool) -> SByte
        ToSByte(value: SByte) -> SByte
        ToSByte(value: object) -> SByte
        ToSByte(value: object, provider: IFormatProvider) -> SByte
        ToSByte(value: Char) -> SByte
        ToSByte(value: UInt16) -> SByte
        ToSByte(value: int) -> SByte
        ToSByte(value: Byte) -> SByte
        ToSByte(value: Int16) -> SByte
        """
        pass

    @staticmethod
    def ToSingle(value, provider=None):
        """
        ToSingle(value: Single) -> Single
        ToSingle(value: float) -> Single
        ToSingle(value: Int64) -> Single
        ToSingle(value: UInt64) -> Single
        ToSingle(value: Decimal) -> Single
        ToSingle(value: bool) -> Single
        ToSingle(value: DateTime) -> Single
        ToSingle(value: str) -> Single
        ToSingle(value: str, provider: IFormatProvider) -> Single
        ToSingle(value: SByte) -> Single
        ToSingle(value: Byte) -> Single
        ToSingle(value: object) -> Single
        ToSingle(value: object, provider: IFormatProvider) -> Single
        ToSingle(value: Char) -> Single
        ToSingle(value: int) -> Single
        ToSingle(value: UInt32) -> Single
        ToSingle(value: Int16) -> Single
        ToSingle(value: UInt16) -> Single
        """
        pass

    @staticmethod
    def ToString(value=None, *__args):
        """
        ToString(value: float) -> str
        ToString(value: Single, provider: IFormatProvider) -> str
        ToString(value: Decimal) -> str
        ToString(value: float, provider: IFormatProvider) -> str
        ToString(value: Single) -> str
        ToString(value: Int64, provider: IFormatProvider) -> str
        ToString(value: Int64) -> str
        ToString(value: UInt64, provider: IFormatProvider) -> str
        ToString(value: UInt64) -> str
        ToString(value: Int16, toBase: int) -> str
        ToString(value: Byte, toBase: int) -> str
        ToString(value: Int64, toBase: int) -> str
        ToString(value: int, toBase: int) -> str
        ToString(value: str, provider: IFormatProvider) -> str
        ToString(value: DateTime) -> str
        ToString(value: Decimal, provider: IFormatProvider) -> str
        ToString(value: str) -> str
        ToString(value: DateTime, provider: IFormatProvider) -> str
        ToString(value: SByte) -> str
        ToString(value: Char, provider: IFormatProvider) -> str
        ToString(value: Byte) -> str
        ToString(value: SByte, provider: IFormatProvider) -> str
        ToString(value: Char) -> str
        ToString(value: object, provider: IFormatProvider) -> str
        ToString(value: object) -> str
        ToString(value: bool, provider: IFormatProvider) -> str
        ToString(value: bool) -> str
        ToString(value: int, provider: IFormatProvider) -> str
        ToString(value: int) -> str
        ToString(value: UInt32, provider: IFormatProvider) -> str
        ToString(value: UInt32) -> str
        ToString(value: UInt16, provider: IFormatProvider) -> str
        ToString(value: Int16) -> str
        ToString(value: Byte, provider: IFormatProvider) -> str
        ToString(value: UInt16) -> str
        ToString(value: Int16, provider: IFormatProvider) -> str
        """
        pass

    @staticmethod
    def ToUInt16(value, *__args):
        """
        ToUInt16(value: Single) -> UInt16
        ToUInt16(value: float) -> UInt16
        ToUInt16(value: Int64) -> UInt16
        ToUInt16(value: UInt64) -> UInt16
        ToUInt16(value: Decimal) -> UInt16
        ToUInt16(value: DateTime) -> UInt16
        ToUInt16(value: str, fromBase: int) -> UInt16
        ToUInt16(value: str) -> UInt16
        ToUInt16(value: str, provider: IFormatProvider) -> UInt16
        ToUInt16(value: UInt32) -> UInt16
        ToUInt16(value: bool) -> UInt16
        ToUInt16(value: Char) -> UInt16
        ToUInt16(value: object) -> UInt16
        ToUInt16(value: object, provider: IFormatProvider) -> UInt16
        ToUInt16(value: SByte) -> UInt16
        ToUInt16(value: int) -> UInt16
        ToUInt16(value: UInt16) -> UInt16
        ToUInt16(value: Byte) -> UInt16
        ToUInt16(value: Int16) -> UInt16
        """
        pass

    @staticmethod
    def ToUInt32(value, *__args):
        """
        ToUInt32(value: Single) -> UInt32
        ToUInt32(value: float) -> UInt32
        ToUInt32(value: Int64) -> UInt32
        ToUInt32(value: UInt64) -> UInt32
        ToUInt32(value: Decimal) -> UInt32
        ToUInt32(value: DateTime) -> UInt32
        ToUInt32(value: str, fromBase: int) -> UInt32
        ToUInt32(value: str) -> UInt32
        ToUInt32(value: str, provider: IFormatProvider) -> UInt32
        ToUInt32(value: UInt32) -> UInt32
        ToUInt32(value: bool) -> UInt32
        ToUInt32(value: Char) -> UInt32
        ToUInt32(value: object) -> UInt32
        ToUInt32(value: object, provider: IFormatProvider) -> UInt32
        ToUInt32(value: SByte) -> UInt32
        ToUInt32(value: UInt16) -> UInt32
        ToUInt32(value: int) -> UInt32
        ToUInt32(value: Byte) -> UInt32
        ToUInt32(value: Int16) -> UInt32
        """
        pass

    @staticmethod
    def ToUInt64(value, *__args):
        """
        ToUInt64(value: Single) -> UInt64
        ToUInt64(value: float) -> UInt64
        ToUInt64(value: Int64) -> UInt64
        ToUInt64(value: UInt64) -> UInt64
        ToUInt64(value: Decimal) -> UInt64
        ToUInt64(value: DateTime) -> UInt64
        ToUInt64(value: str, fromBase: int) -> UInt64
        ToUInt64(value: str) -> UInt64
        ToUInt64(value: str, provider: IFormatProvider) -> UInt64
        ToUInt64(value: UInt32) -> UInt64
        ToUInt64(value: bool) -> UInt64
        ToUInt64(value: Char) -> UInt64
        ToUInt64(value: object) -> UInt64
        ToUInt64(value: object, provider: IFormatProvider) -> UInt64
        ToUInt64(value: SByte) -> UInt64
        ToUInt64(value: UInt16) -> UInt64
        ToUInt64(value: int) -> UInt64
        ToUInt64(value: Byte) -> UInt64
        ToUInt64(value: Int16) -> UInt64
        """
        pass

    DBNull = None
    __all__ = [
        'ChangeType',
        'DBNull',
        'FromBase64CharArray',
        'FromBase64String',
        'GetTypeCode',
        'IsDBNull',
        'ToBase64CharArray',
        'ToBase64String',
        'ToBoolean',
        'ToByte',
        'ToChar',
        'ToDateTime',
        'ToDecimal',
        'ToDouble',
        'ToInt16',
        'ToInt32',
        'ToInt64',
        'ToSByte',
        'ToSingle',
        'ToString',
        'ToUInt16',
        'ToUInt32',
        'ToUInt64',
    ]


class Converter(MulticastDelegate):
    """ Converter[TInput, TOutput](object: object, method: IntPtr) """
    def BeginInvoke(self, input, callback, object):
        """ BeginInvoke(self: Converter[TInput, TOutput], input: TInput, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: Converter[TInput, TOutput], result: IAsyncResult) -> TOutput """
        pass

    def Invoke(self, input):
        """ Invoke(self: Converter[TInput, TOutput], input: TInput) -> TOutput """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class CrossAppDomainDelegate(MulticastDelegate):
    """ CrossAppDomainDelegate(object: object, method: IntPtr) """
    def BeginInvoke(self, callback, object):
        """ BeginInvoke(self: CrossAppDomainDelegate, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: CrossAppDomainDelegate, result: IAsyncResult) """
        pass

    def Invoke(self):
        """ Invoke(self: CrossAppDomainDelegate) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class DataMisalignedException(SystemException):
    """
    DataMisalignedException()
    DataMisalignedException(message: str)
    DataMisalignedException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        """
        pass


class DateTime(object):
    """
    DateTime(ticks: Int64)
    DateTime(ticks: Int64, kind: DateTimeKind)
    DateTime(year: int, month: int, day: int)
    DateTime(year: int, month: int, day: int, calendar: Calendar)
    DateTime(year: int, month: int, day: int, hour: int, minute: int, second: int)
    DateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, kind: DateTimeKind)
    DateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, calendar: Calendar)
    DateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int)
    DateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, kind: DateTimeKind)
    DateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: Calendar)
    DateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: Calendar, kind: DateTimeKind)
    """
    def Add(self, value):
        """ Add(self: DateTime, value: TimeSpan) -> DateTime """
        pass

    def AddDays(self, value):
        """ AddDays(self: DateTime, value: float) -> DateTime """
        pass

    def AddHours(self, value):
        """ AddHours(self: DateTime, value: float) -> DateTime """
        pass

    def AddMilliseconds(self, value):
        """ AddMilliseconds(self: DateTime, value: float) -> DateTime """
        pass

    def AddMinutes(self, value):
        """ AddMinutes(self: DateTime, value: float) -> DateTime """
        pass

    def AddMonths(self, months):
        """ AddMonths(self: DateTime, months: int) -> DateTime """
        pass

    def AddSeconds(self, value):
        """ AddSeconds(self: DateTime, value: float) -> DateTime """
        pass

    def AddTicks(self, value):
        """ AddTicks(self: DateTime, value: Int64) -> DateTime """
        pass

    def AddYears(self, value):
        """ AddYears(self: DateTime, value: int) -> DateTime """
        pass

    @staticmethod
    def Compare(t1, t2):
        """ Compare(t1: DateTime, t2: DateTime) -> int """
        pass

    def CompareTo(self, value):
        """
        CompareTo(self: DateTime, value: DateTime) -> int
        CompareTo(self: DateTime, value: object) -> int
        """
        pass

    @staticmethod
    def DaysInMonth(year, month):
        """ DaysInMonth(year: int, month: int) -> int """
        pass

    def Equals(self, *__args):
        """
        Equals(t1: DateTime, t2: DateTime) -> bool
        Equals(self: DateTime, value: DateTime) -> bool
        Equals(self: DateTime, value: object) -> bool
        """
        pass

    @staticmethod
    def FromBinary(dateData):
        """ FromBinary(dateData: Int64) -> DateTime """
        pass

    @staticmethod
    def FromFileTime(fileTime):
        """ FromFileTime(fileTime: Int64) -> DateTime """
        pass

    @staticmethod
    def FromFileTimeUtc(fileTime):
        """ FromFileTimeUtc(fileTime: Int64) -> DateTime """
        pass

    @staticmethod
    def FromOADate(d):
        """ FromOADate(d: float) -> DateTime """
        pass

    def GetDateTimeFormats(self, *__args):
        """
        GetDateTimeFormats(self: DateTime, format: Char) -> Array[str]
        GetDateTimeFormats(self: DateTime, format: Char, provider: IFormatProvider) -> Array[str]
        GetDateTimeFormats(self: DateTime) -> Array[str]
        GetDateTimeFormats(self: DateTime, provider: IFormatProvider) -> Array[str]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DateTime) -> int """
        pass

    def GetTypeCode(self):
        """ GetTypeCode(self: DateTime) -> TypeCode """
        pass

    def IsDaylightSavingTime(self):
        """ IsDaylightSavingTime(self: DateTime) -> bool """
        pass

    @staticmethod
    def IsLeapYear(year):
        """ IsLeapYear(year: int) -> bool """
        pass

    @staticmethod
    def Parse(s, provider=None, styles=None):
        """
        Parse(s: str, provider: IFormatProvider, styles: DateTimeStyles) -> DateTime
        Parse(s: str, provider: IFormatProvider) -> DateTime
        Parse(s: str) -> DateTime
        """
        pass

    @staticmethod
    def ParseExact(s, *__args):
        """
        ParseExact(s: str, formats: Array[str], provider: IFormatProvider, style: DateTimeStyles) -> DateTime
        ParseExact(s: str, format: str, provider: IFormatProvider, style: DateTimeStyles) -> DateTime
        ParseExact(s: str, format: str, provider: IFormatProvider) -> DateTime
        """
        pass

    @staticmethod
    def SpecifyKind(value, kind):
        """ SpecifyKind(value: DateTime, kind: DateTimeKind) -> DateTime """
        pass

    def Subtract(self, value):
        """
        Subtract(self: DateTime, value: TimeSpan) -> DateTime
        Subtract(self: DateTime, value: DateTime) -> TimeSpan
        """
        pass

    def ToBinary(self):
        """ ToBinary(self: DateTime) -> Int64 """
        pass

    def ToFileTime(self):
        """ ToFileTime(self: DateTime) -> Int64 """
        pass

    def ToFileTimeUtc(self):
        """ ToFileTimeUtc(self: DateTime) -> Int64 """
        pass

    def ToLocalTime(self):
        """ ToLocalTime(self: DateTime) -> DateTime """
        pass

    def ToLongDateString(self):
        """ ToLongDateString(self: DateTime) -> str """
        pass

    def ToLongTimeString(self):
        """ ToLongTimeString(self: DateTime) -> str """
        pass

    def ToOADate(self):
        """ ToOADate(self: DateTime) -> float """
        pass

    def ToShortDateString(self):
        """ ToShortDateString(self: DateTime) -> str """
        pass

    def ToShortTimeString(self):
        """ ToShortTimeString(self: DateTime) -> str """
        pass

    def ToString(self, *__args):
        """
        ToString(self: DateTime, provider: IFormatProvider) -> str
        ToString(self: DateTime, format: str, provider: IFormatProvider) -> str
        ToString(self: DateTime) -> str
        ToString(self: DateTime, format: str) -> str
        """
        pass

    def ToUniversalTime(self):
        """ ToUniversalTime(self: DateTime) -> DateTime """
        pass

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str, provider: IFormatProvider, styles: DateTimeStyles) -> (bool, DateTime)
        TryParse(s: str) -> (bool, DateTime)
        """
        pass

    @staticmethod
    def TryParseExact(s, *__args):
        """
        TryParseExact(s: str, formats: Array[str], provider: IFormatProvider, style: DateTimeStyles) -> (bool, DateTime)
        TryParseExact(s: str, format: str, provider: IFormatProvider, style: DateTimeStyles) -> (bool, DateTime)
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[DateTime]() -> DateTime
        
        __new__(cls: type, ticks: Int64)
        __new__(cls: type, ticks: Int64, kind: DateTimeKind)
        __new__(cls: type, year: int, month: int, day: int)
        __new__(cls: type, year: int, month: int, day: int, calendar: Calendar)
        __new__(cls: type, year: int, month: int, day: int, hour: int, minute: int, second: int)
        __new__(cls: type, year: int, month: int, day: int, hour: int, minute: int, second: int, kind: DateTimeKind)
        __new__(cls: type, year: int, month: int, day: int, hour: int, minute: int, second: int, calendar: Calendar)
        __new__(cls: type, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int)
        __new__(cls: type, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, kind: DateTimeKind)
        __new__(cls: type, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: Calendar)
        __new__(cls: type, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: Calendar, kind: DateTimeKind)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(d1: DateTime, d2: DateTime) -> TimeSpan """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: DateTime) -> DateTime

"""

    Day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Day(self: DateTime) -> int

"""

    DayOfWeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DayOfWeek(self: DateTime) -> DayOfWeek

"""

    DayOfYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DayOfYear(self: DateTime) -> int

"""

    Hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hour(self: DateTime) -> int

"""

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: DateTime) -> DateTimeKind

"""

    Millisecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Millisecond(self: DateTime) -> int

"""

    Minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Minute(self: DateTime) -> int

"""

    Month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Month(self: DateTime) -> int

"""

    Second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Second(self: DateTime) -> int

"""

    Ticks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ticks(self: DateTime) -> Int64

"""

    TimeOfDay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeOfDay(self: DateTime) -> TimeSpan

"""

    Year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Year(self: DateTime) -> int

"""


    MaxValue = None
    MinValue = None
    Now = None
    Today = None
    UtcNow = None


class DateTimeKind(Enum):
    """ enum DateTimeKind, values: Local (2), Unspecified (0), Utc (1) """
    Local = None
    Unspecified = None
    Utc = None
    value__ = None


class DateTimeOffset(object):
    """
    DateTimeOffset(ticks: Int64, offset: TimeSpan)
    DateTimeOffset(dateTime: DateTime)
    DateTimeOffset(dateTime: DateTime, offset: TimeSpan)
    DateTimeOffset(year: int, month: int, day: int, hour: int, minute: int, second: int, offset: TimeSpan)
    DateTimeOffset(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, offset: TimeSpan)
    DateTimeOffset(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: Calendar, offset: TimeSpan)
    """
    def Add(self, timeSpan):
        """ Add(self: DateTimeOffset, timeSpan: TimeSpan) -> DateTimeOffset """
        pass

    def AddDays(self, days):
        """ AddDays(self: DateTimeOffset, days: float) -> DateTimeOffset """
        pass

    def AddHours(self, hours):
        """ AddHours(self: DateTimeOffset, hours: float) -> DateTimeOffset """
        pass

    def AddMilliseconds(self, milliseconds):
        """ AddMilliseconds(self: DateTimeOffset, milliseconds: float) -> DateTimeOffset """
        pass

    def AddMinutes(self, minutes):
        """ AddMinutes(self: DateTimeOffset, minutes: float) -> DateTimeOffset """
        pass

    def AddMonths(self, months):
        """ AddMonths(self: DateTimeOffset, months: int) -> DateTimeOffset """
        pass

    def AddSeconds(self, seconds):
        """ AddSeconds(self: DateTimeOffset, seconds: float) -> DateTimeOffset """
        pass

    def AddTicks(self, ticks):
        """ AddTicks(self: DateTimeOffset, ticks: Int64) -> DateTimeOffset """
        pass

    def AddYears(self, years):
        """ AddYears(self: DateTimeOffset, years: int) -> DateTimeOffset """
        pass

    @staticmethod
    def Compare(first, second):
        """ Compare(first: DateTimeOffset, second: DateTimeOffset) -> int """
        pass

    def CompareTo(self, other):
        """ CompareTo(self: DateTimeOffset, other: DateTimeOffset) -> int """
        pass

    def Equals(self, *__args):
        """
        Equals(first: DateTimeOffset, second: DateTimeOffset) -> bool
        Equals(self: DateTimeOffset, other: DateTimeOffset) -> bool
        Equals(self: DateTimeOffset, obj: object) -> bool
        """
        pass

    def EqualsExact(self, other):
        """ EqualsExact(self: DateTimeOffset, other: DateTimeOffset) -> bool """
        pass

    @staticmethod
    def FromFileTime(fileTime):
        """ FromFileTime(fileTime: Int64) -> DateTimeOffset """
        pass

    @staticmethod
    def FromUnixTimeMilliseconds(milliseconds):
        """ FromUnixTimeMilliseconds(milliseconds: Int64) -> DateTimeOffset """
        pass

    @staticmethod
    def FromUnixTimeSeconds(seconds):
        """ FromUnixTimeSeconds(seconds: Int64) -> DateTimeOffset """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DateTimeOffset) -> int """
        pass

    @staticmethod
    def Parse(input, formatProvider=None, styles=None):
        """
        Parse(input: str, formatProvider: IFormatProvider, styles: DateTimeStyles) -> DateTimeOffset
        Parse(input: str, formatProvider: IFormatProvider) -> DateTimeOffset
        Parse(input: str) -> DateTimeOffset
        """
        pass

    @staticmethod
    def ParseExact(input, *__args):
        """
        ParseExact(input: str, formats: Array[str], formatProvider: IFormatProvider, styles: DateTimeStyles) -> DateTimeOffset
        ParseExact(input: str, format: str, formatProvider: IFormatProvider, styles: DateTimeStyles) -> DateTimeOffset
        ParseExact(input: str, format: str, formatProvider: IFormatProvider) -> DateTimeOffset
        """
        pass

    def Subtract(self, value):
        """
        Subtract(self: DateTimeOffset, value: TimeSpan) -> DateTimeOffset
        Subtract(self: DateTimeOffset, value: DateTimeOffset) -> TimeSpan
        """
        pass

    def ToFileTime(self):
        """ ToFileTime(self: DateTimeOffset) -> Int64 """
        pass

    def ToLocalTime(self):
        """ ToLocalTime(self: DateTimeOffset) -> DateTimeOffset """
        pass

    def ToOffset(self, offset):
        """ ToOffset(self: DateTimeOffset, offset: TimeSpan) -> DateTimeOffset """
        pass

    def ToString(self, *__args):
        """
        ToString(self: DateTimeOffset, formatProvider: IFormatProvider) -> str
        ToString(self: DateTimeOffset, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: DateTimeOffset) -> str
        ToString(self: DateTimeOffset, format: str) -> str
        """
        pass

    def ToUniversalTime(self):
        """ ToUniversalTime(self: DateTimeOffset) -> DateTimeOffset """
        pass

    def ToUnixTimeMilliseconds(self):
        """ ToUnixTimeMilliseconds(self: DateTimeOffset) -> Int64 """
        pass

    def ToUnixTimeSeconds(self):
        """ ToUnixTimeSeconds(self: DateTimeOffset) -> Int64 """
        pass

    @staticmethod
    def TryParse(input, *__args):
        """
        TryParse(input: str, formatProvider: IFormatProvider, styles: DateTimeStyles) -> (bool, DateTimeOffset)
        TryParse(input: str) -> (bool, DateTimeOffset)
        """
        pass

    @staticmethod
    def TryParseExact(input, *__args):
        """
        TryParseExact(input: str, formats: Array[str], formatProvider: IFormatProvider, styles: DateTimeStyles) -> (bool, DateTimeOffset)
        TryParseExact(input: str, format: str, formatProvider: IFormatProvider, styles: DateTimeStyles) -> (bool, DateTimeOffset)
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[DateTimeOffset]() -> DateTimeOffset
        
        __new__(cls: type, ticks: Int64, offset: TimeSpan)
        __new__(cls: type, dateTime: DateTime)
        __new__(cls: type, dateTime: DateTime, offset: TimeSpan)
        __new__(cls: type, year: int, month: int, day: int, hour: int, minute: int, second: int, offset: TimeSpan)
        __new__(cls: type, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, offset: TimeSpan)
        __new__(cls: type, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: Calendar, offset: TimeSpan)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(left: DateTimeOffset, right: DateTimeOffset) -> TimeSpan """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: DateTimeOffset) -> DateTime

"""

    DateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateTime(self: DateTimeOffset) -> DateTime

"""

    Day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Day(self: DateTimeOffset) -> int

"""

    DayOfWeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DayOfWeek(self: DateTimeOffset) -> DayOfWeek

"""

    DayOfYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DayOfYear(self: DateTimeOffset) -> int

"""

    Hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hour(self: DateTimeOffset) -> int

"""

    LocalDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalDateTime(self: DateTimeOffset) -> DateTime

"""

    Millisecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Millisecond(self: DateTimeOffset) -> int

"""

    Minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Minute(self: DateTimeOffset) -> int

"""

    Month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Month(self: DateTimeOffset) -> int

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: DateTimeOffset) -> TimeSpan

"""

    Second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Second(self: DateTimeOffset) -> int

"""

    Ticks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ticks(self: DateTimeOffset) -> Int64

"""

    TimeOfDay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeOfDay(self: DateTimeOffset) -> TimeSpan

"""

    UtcDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UtcDateTime(self: DateTimeOffset) -> DateTime

"""

    UtcTicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UtcTicks(self: DateTimeOffset) -> Int64

"""

    Year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Year(self: DateTimeOffset) -> int

"""


    MaxValue = None
    MinValue = None
    Now = None
    UtcNow = None


class DayOfWeek(Enum):
    """ enum DayOfWeek, values: Friday (5), Monday (1), Saturday (6), Sunday (0), Thursday (4), Tuesday (2), Wednesday (3) """
    Friday = None
    Monday = None
    Saturday = None
    Sunday = None
    Thursday = None
    Tuesday = None
    value__ = None
    Wednesday = None


class DBNull(object):
    # no doc
    def GetObjectData(self, info, context):
        """ GetObjectData(self: DBNull, info: SerializationInfo, context: StreamingContext) """
        pass

    def GetTypeCode(self):
        """ GetTypeCode(self: DBNull) -> TypeCode """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: DBNull, provider: IFormatProvider) -> str
        ToString(self: DBNull) -> str
        """
        pass

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(value: DBNull) -> bool """
        pass

    Value = None


class Decimal(object):
    """
    Decimal(value: int)
    Decimal(value: UInt32)
    Decimal(value: Int64)
    Decimal(value: UInt64)
    Decimal(value: Single)
    Decimal(value: float)
    Decimal(bits: Array[int])
    Decimal(lo: int, mid: int, hi: int, isNegative: bool, scale: Byte)
    """
    @staticmethod
    def Add(d1, d2):
        """ Add(d1: Decimal, d2: Decimal) -> Decimal """
        pass

    @staticmethod
    def Ceiling(d):
        """ Ceiling(d: Decimal) -> Decimal """
        pass

    @staticmethod
    def Compare(d1, d2):
        """ Compare(d1: Decimal, d2: Decimal) -> int """
        pass

    def CompareTo(self, value):
        """
        CompareTo(self: Decimal, value: Decimal) -> int
        CompareTo(self: Decimal, value: object) -> int
        """
        pass

    @staticmethod
    def Divide(d1, d2):
        """ Divide(d1: Decimal, d2: Decimal) -> Decimal """
        pass

    def Equals(self, *__args):
        """
        Equals(d1: Decimal, d2: Decimal) -> bool
        Equals(self: Decimal, value: Decimal) -> bool
        Equals(self: Decimal, value: object) -> bool
        """
        pass

    @staticmethod
    def Floor(d):
        """ Floor(d: Decimal) -> Decimal """
        pass

    @staticmethod
    def FromOACurrency(cy):
        """ FromOACurrency(cy: Int64) -> Decimal """
        pass

    @staticmethod
    def GetBits(d):
        """ GetBits(d: Decimal) -> Array[int] """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Decimal) -> int """
        pass

    def GetTypeCode(self):
        """ GetTypeCode(self: Decimal) -> TypeCode """
        pass

    @staticmethod
    def Multiply(d1, d2):
        """ Multiply(d1: Decimal, d2: Decimal) -> Decimal """
        pass

    @staticmethod
    def Negate(d):
        """ Negate(d: Decimal) -> Decimal """
        pass

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str, provider: IFormatProvider) -> Decimal
        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> Decimal
        Parse(s: str) -> Decimal
        Parse(s: str, style: NumberStyles) -> Decimal
        """
        pass

    @staticmethod
    def Remainder(d1, d2):
        """ Remainder(d1: Decimal, d2: Decimal) -> Decimal """
        pass

    @staticmethod
    def Round(d, *__args):
        """
        Round(d: Decimal, mode: MidpointRounding) -> Decimal
        Round(d: Decimal, decimals: int, mode: MidpointRounding) -> Decimal
        Round(d: Decimal) -> Decimal
        Round(d: Decimal, decimals: int) -> Decimal
        """
        pass

    @staticmethod
    def Subtract(d1, d2):
        """ Subtract(d1: Decimal, d2: Decimal) -> Decimal """
        pass

    @staticmethod
    def ToByte(value):
        """ ToByte(value: Decimal) -> Byte """
        pass

    @staticmethod
    def ToDouble(d):
        """ ToDouble(d: Decimal) -> float """
        pass

    @staticmethod
    def ToInt16(value):
        """ ToInt16(value: Decimal) -> Int16 """
        pass

    @staticmethod
    def ToInt32(d):
        """ ToInt32(d: Decimal) -> int """
        pass

    @staticmethod
    def ToInt64(d):
        """ ToInt64(d: Decimal) -> Int64 """
        pass

    @staticmethod
    def ToOACurrency(value):
        """ ToOACurrency(value: Decimal) -> Int64 """
        pass

    @staticmethod
    def ToSByte(value):
        """ ToSByte(value: Decimal) -> SByte """
        pass

    @staticmethod
    def ToSingle(d):
        """ ToSingle(d: Decimal) -> Single """
        pass

    def ToString(self, *__args):
        """
        ToString(self: Decimal, provider: IFormatProvider) -> str
        ToString(self: Decimal, format: str, provider: IFormatProvider) -> str
        ToString(self: Decimal) -> str
        ToString(self: Decimal, format: str) -> str
        """
        pass

    @staticmethod
    def ToUInt16(value):
        """ ToUInt16(value: Decimal) -> UInt16 """
        pass

    @staticmethod
    def ToUInt32(d):
        """ ToUInt32(d: Decimal) -> UInt32 """
        pass

    @staticmethod
    def ToUInt64(d):
        """ ToUInt64(d: Decimal) -> UInt64 """
        pass

    @staticmethod
    def Truncate(d):
        """ Truncate(d: Decimal) -> Decimal """
        pass

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, Decimal)
        TryParse(s: str) -> (bool, Decimal)
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __complex__(self, *args): #cannot find CLR method
        """ __complex__(value: Decimal) -> float """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __float__(self, *args): #cannot find CLR method
        """ __complex__(value: Decimal) -> float """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(value: Decimal) -> int """
        pass

    def __long__(self, *args): #cannot find CLR method
        """ __int__(value: Decimal) -> int """
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Decimal]() -> Decimal
        
        __new__(cls: type, value: int)
        __new__(cls: type, value: UInt32)
        __new__(cls: type, value: Int64)
        __new__(cls: type, value: UInt64)
        __new__(cls: type, value: Single)
        __new__(cls: type, value: float)
        __new__(cls: type, bits: Array[int])
        __new__(cls: type, lo: int, mid: int, hi: int, isNegative: bool, scale: Byte)
        """
        pass

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: Decimal) -> bool """
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(d: Decimal) -> Decimal """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(d1: Decimal, d2: Decimal) -> Decimal """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(d1: Decimal, d2: Decimal) -> Decimal """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(d1: Decimal, d2: Decimal) -> Decimal """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(d1: Decimal, d2: Decimal) -> Decimal """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(d1: Decimal, d2: Decimal) -> Decimal """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    MaxValue = None
    MinusOne = None
    MinValue = None
    One = None
    Zero = None


class DivideByZeroException(ArithmeticException):
    """
    DivideByZeroException()
    DivideByZeroException(message: str)
    DivideByZeroException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class TypeLoadException(SystemException):
    """
    TypeLoadException()
    TypeLoadException(message: str)
    TypeLoadException(message: str, inner: Exception)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: TypeLoadException, info: SerializationInfo, context: StreamingContext) """
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

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: TypeLoadException) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: TypeLoadException) -> str

"""



class DllNotFoundException(TypeLoadException):
    """
    DllNotFoundException()
    DllNotFoundException(message: str)
    DllNotFoundException(message: str, inner: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class Double(object):
    # no doc
    def as_integer_ratio(self, *args): #cannot find CLR method
        """ as_integer_ratio(self: float) -> tuple """
        pass

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: float) -> float """
        pass

    def fromhex(self, *args): #cannot find CLR method
        """ fromhex(cls: type, self: str) -> object """
        pass

    def hex(self, *args): #cannot find CLR method
        """ hex(self: float) -> str """
        pass

    def is_integer(self, *args): #cannot find CLR method
        """ is_integer(self: float) -> bool """
        pass

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __coerce__(self, *args): #cannot find CLR method
        """ __coerce__(x: float, o: object) -> tuple """
        pass

    def __divmod__(self, *args): #cannot find CLR method
        """ __divmod__(x: float, y: float) -> object """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __float__(self, *args): #cannot find CLR method
        """ __float__(self: float) -> float """
        pass

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//y """
        pass

    def __getformat__(self, *args): #cannot find CLR method
        """ __getformat__(typestr: str) -> str """
        pass

    def __getnewargs__(self, *args): #cannot find CLR method
        """ __getnewargs__(self: float) -> object """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(d: float) -> object """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __long__(self, *args): #cannot find CLR method
        """ __long__(self: float) -> long """
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, s: IList[Byte]) -> object
        __new__(cls: type, x: object) -> object
        __new__(cls: type) -> object
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: float) -> bool """
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: float) -> float """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: float, y: float) -> float """
        pass

    def __rdivmod__(self, *args): #cannot find CLR method
        """ __rdivmod__(x: float, y: float) -> object """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: float, y: float) -> float """
        pass

    def __rfloordiv__(self, *args): #cannot find CLR method
        """ __rfloordiv__(x: float, y: float) -> float """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: float, y: float) -> float """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: float, y: float) -> float """
        pass

    def __rpow__(self, *args): #cannot find CLR method
        """ __rpow__(x: float, y: float) -> float """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: float, y: float) -> float """
        pass

    def __rtruediv__(self, *args): #cannot find CLR method
        """ __rtruediv__(x: float, y: float) -> float """
        pass

    def __setformat__(self, *args): #cannot find CLR method
        """ __setformat__(typestr: str, fmt: str) """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/y """
        pass

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: float) -> object """
        pass

    imag = None
    real = None


class DuplicateWaitObjectException(ArgumentException):
    """
    DuplicateWaitObjectException()
    DuplicateWaitObjectException(parameterName: str)
    DuplicateWaitObjectException(parameterName: str, message: str)
    DuplicateWaitObjectException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, parameterName: str)
        __new__(cls: type, parameterName: str, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class EntryPointNotFoundException(TypeLoadException):
    """
    EntryPointNotFoundException()
    EntryPointNotFoundException(message: str)
    EntryPointNotFoundException(message: str, inner: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class Environment(object):
    # no doc
    @staticmethod
    def Exit(exitCode):
        """ Exit(exitCode: int) """
        pass

    @staticmethod
    def ExpandEnvironmentVariables(name):
        """ ExpandEnvironmentVariables(name: str) -> str """
        pass

    @staticmethod
    def FailFast(message, exception=None):
        """ FailFast(message: str, exception: Exception)FailFast(message: str) """
        pass

    @staticmethod
    def GetCommandLineArgs():
        """ GetCommandLineArgs() -> Array[str] """
        pass

    @staticmethod
    def GetEnvironmentVariable(variable, target=None):
        """
        GetEnvironmentVariable(variable: str, target: EnvironmentVariableTarget) -> str
        GetEnvironmentVariable(variable: str) -> str
        """
        pass

    @staticmethod
    def GetEnvironmentVariables(target=None):
        """
        GetEnvironmentVariables(target: EnvironmentVariableTarget) -> IDictionary
        GetEnvironmentVariables() -> IDictionary
        """
        pass

    @staticmethod
    def GetFolderPath(folder, option=None):
        """
        GetFolderPath(folder: SpecialFolder, option: SpecialFolderOption) -> str
        GetFolderPath(folder: SpecialFolder) -> str
        """
        pass

    @staticmethod
    def GetLogicalDrives():
        """ GetLogicalDrives() -> Array[str] """
        pass

    @staticmethod
    def SetEnvironmentVariable(variable, value, target=None):
        """ SetEnvironmentVariable(variable: str, value: str, target: EnvironmentVariableTarget)SetEnvironmentVariable(variable: str, value: str) """
        pass

    CommandLine = 'ipy64  generate.py'
    CurrentDirectory = 'C:\\Dropbox\\Shared\\dev\\repos\\revit-autocomplete-for-vscode'
    CurrentManagedThreadId = 1
    ExitCode = 0
    HasShutdownStarted = False
    Is64BitOperatingSystem = True
    Is64BitProcess = True
    MachineName = 'XPS-GUI'
    NewLine = '\r\n'
    OSVersion = None
    ProcessorCount = 4
    SpecialFolder = None
    SpecialFolderOption = None
    StackTrace = '   at System.Environment.GetStackTrace(Exception e, Boolean needFileInfo)\r\n   at System.Environment.get_StackTrace()\r\n   at Microsoft.Scripting.Interpreter.FuncCallInstruction`1.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run3[T0,T1,T2,TRet](T0 arg0, T1 arg1, T2 arg2)\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute2[T0,T1,TRet](CallSite site, T0 arg0, T1 arg1)\r\n   at Microsoft.Scripting.Interpreter.FuncCallInstruction`5.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run3[T0,T1,T2,TRet](T0 arg0, T1 arg1, T2 arg2)\r\n   at IronPython.Runtime.Types.BuiltinFunction.Call0(CodeContext context, SiteLocalStorage`1 storage, Object instance)\r\n   at IronPython.Runtime.Types.ReflectedProperty.CallGetter(CodeContext context, PythonType owner, SiteLocalStorage`1 storage, Object instance)\r\n   at IronPython.Runtime.Types.ReflectedProperty.TryGetValue(CodeContext context, Object instance, PythonType owner, Object& value)\r\n   at IronPython.Runtime.Binding.MetaPythonType.FastGetBinderHelper.SlotAccessDelegate.Target(CodeContext context, Object self, Object& result)\r\n   at IronPython.Runtime.Types.TypeGetBase.RunDelegates(Object self, CodeContext context)\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute2[T0,T1,TRet](CallSite site, T0 arg0, T1 arg1)\r\n   at IronPython.Runtime.Types.PythonType.TryGetBoundAttr(CodeContext context, Object o, String name, Object& ret)\r\n   at IronPython.Runtime.Operations.PythonOps.GetBoundAttr(CodeContext context, Object o, String name)\r\n   at redo_class$264(Closure , PythonFunction , Object , Object , Object , Object , Object , Object , Object , Object )\r\n   at CallSite.Target(Closure , CallSite , CodeContext , Object , Object , Object , Object , Object , Object , Object , Object )\r\n   at lambda_method(Closure , Object[] , StrongBox`1[] , InterpretedFrame )\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run4[T0,T1,T2,T3,TRet](T0 arg0, T1 arg1, T2 arg2, T3 arg3)\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute5[T0,T1,T2,T3,T4,TRet](CallSite site, T0 arg0, T1 arg1, T2 arg2, T3 arg3, T4 arg4)\r\n   at IronPython.Runtime.Method.MethodBinding`2.SelfTarget(CallSite site, CodeContext context, Object target, T0 arg0, T1 arg1)\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute4[T0,T1,T2,T3,TRet](CallSite site, T0 arg0, T1 arg1, T2 arg2, T3 arg3)\r\n   at Microsoft.Scripting.Interpreter.FuncCallInstruction`7.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run5[T0,T1,T2,T3,T4,TRet](T0 arg0, T1 arg1, T2 arg2, T3 arg3, T4 arg4)\r\n   at IronPython.Compiler.Ast.CallExpression.Invoke2Instruction.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run5[T0,T1,T2,T3,T4,TRet](T0 arg0, T1 arg1, T2 arg2, T3 arg3, T4 arg4)\r\n   at Microsoft.Scripting.Interpreter.FuncCallInstruction`7.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run7[T0,T1,T2,T3,T4,T5,T6,TRet](T0 arg0, T1 arg1, T2 arg2, T3 arg3, T4 arg4, T5 arg5, T6 arg6)\r\n   at Microsoft.Scripting.Interpreter.DynamicInstruction`7.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run6[T0,T1,T2,T3,T4,T5,TRet](T0 arg0, T1 arg1, T2 arg2, T3 arg3, T4 arg4, T5 arg5)\r\n   at Microsoft.Scripting.Interpreter.FuncCallInstruction`8.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run7[T0,T1,T2,T3,T4,T5,T6,TRet](T0 arg0, T1 arg1, T2 arg2, T3 arg3, T4 arg4, T5 arg5, T6 arg6)\r\n   at Microsoft.Scripting.Interpreter.DynamicInstruction`7.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run1[T0,TRet](T0 arg0)\r\n   at IronPython.Compiler.RuntimeScriptCode.InvokeTarget(Scope scope)\r\n   at IronPython.Hosting.PythonCommandLine.RunFileWorker(String fileName)\r\n   at IronPython.Hosting.PythonCommandLine.RunFile(String fileName)\r\n   at Microsoft.Scripting.Hosting.Shell.CommandLine.Run()\r\n   at IronPython.Hosting.PythonCommandLine.Run()\r\n   at Microsoft.Scripting.Hosting.Shell.CommandLine.Run(ScriptEngine engine, IConsole console, ConsoleOptions options)\r\n   at Microsoft.Scripting.Hosting.Shell.ConsoleHost.RunCommandLine()\r\n   at Microsoft.Scripting.Hosting.Shell.ConsoleHost.ExecuteInternal()\r\n   at Microsoft.Scripting.Hosting.Shell.ConsoleHost.Run(String[] args)\r\n   at PythonConsoleHost.Main(String[] args)'
    SystemDirectory = 'C:\\WINDOWS\\system32'
    SystemPageSize = 4096
    TickCount = 150421921
    UserDomainName = 'XPS-GUI'
    UserInteractive = True
    UserName = 'gtalarico'
    Version = None
    WorkingSet = None
    __all__ = [
        'Exit',
        'ExpandEnvironmentVariables',
        'FailFast',
        'GetCommandLineArgs',
        'GetEnvironmentVariable',
        'GetEnvironmentVariables',
        'GetFolderPath',
        'GetLogicalDrives',
        'SetEnvironmentVariable',
        'SpecialFolder',
        'SpecialFolderOption',
    ]


class EnvironmentVariableTarget(Enum):
    """ enum EnvironmentVariableTarget, values: Machine (2), Process (0), User (1) """
    Machine = None
    Process = None
    User = None
    value__ = None


class ExecutionEngineException(SystemException):
    """
    ExecutionEngineException()
    ExecutionEngineException(message: str)
    ExecutionEngineException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        """
        pass


class MemberAccessException(SystemException):
    """
    MemberAccessException()
    MemberAccessException(message: str)
    MemberAccessException(message: str, inner: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class FieldAccessException(MemberAccessException):
    """
    FieldAccessException()
    FieldAccessException(message: str)
    FieldAccessException(message: str, inner: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class UriParser(object):
    # no doc
    def GetComponents(self, *args): #cannot find CLR method
        """ GetComponents(self: UriParser, uri: Uri, components: UriComponents, format: UriFormat) -> str """
        pass

    def InitializeAndValidate(self, *args): #cannot find CLR method
        """ InitializeAndValidate(self: UriParser, uri: Uri) -> UriFormatException """
        pass

    def IsBaseOf(self, *args): #cannot find CLR method
        """ IsBaseOf(self: UriParser, baseUri: Uri, relativeUri: Uri) -> bool """
        pass

    @staticmethod
    def IsKnownScheme(schemeName):
        """ IsKnownScheme(schemeName: str) -> bool """
        pass

    def IsWellFormedOriginalString(self, *args): #cannot find CLR method
        """ IsWellFormedOriginalString(self: UriParser, uri: Uri) -> bool """
        pass

    def OnNewUri(self, *args): #cannot find CLR method
        """ OnNewUri(self: UriParser) -> UriParser """
        pass

    def OnRegister(self, *args): #cannot find CLR method
        """ OnRegister(self: UriParser, schemeName: str, defaultPort: int) """
        pass

    @staticmethod
    def Register(uriParser, schemeName, defaultPort):
        """ Register(uriParser: UriParser, schemeName: str, defaultPort: int) """
        pass

    def Resolve(self, *args): #cannot find CLR method
        """ Resolve(self: UriParser, baseUri: Uri, relativeUri: Uri) -> (str, UriFormatException) """
        pass


class FileStyleUriParser(UriParser):
    """ FileStyleUriParser() """

class FlagsAttribute(Attribute):
    """ FlagsAttribute() """

class FormatException(SystemException):
    """
    FormatException()
    FormatException(message: str)
    FormatException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class FormattableString(object):
    # no doc
    def GetArgument(self, index):
        """ GetArgument(self: FormattableString, index: int) -> object """
        pass

    def GetArguments(self):
        """ GetArguments(self: FormattableString) -> Array[object] """
        pass

    @staticmethod
    def Invariant(formattable):
        """ Invariant(formattable: FormattableString) -> str """
        pass

    def ToString(self, formatProvider=None):
        """
        ToString(self: FormattableString) -> str
        ToString(self: FormattableString, formatProvider: IFormatProvider) -> str
        """
        pass

    ArgumentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArgumentCount(self: FormattableString) -> int

"""

    Format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Format(self: FormattableString) -> str

"""



class FtpStyleUriParser(UriParser):
    """ FtpStyleUriParser() """

class GC(object):
    # no doc
    @staticmethod
    def AddMemoryPressure(bytesAllocated):
        """ AddMemoryPressure(bytesAllocated: Int64) """
        pass

    @staticmethod
    def CancelFullGCNotification():
        """ CancelFullGCNotification() """
        pass

    @staticmethod
    def Collect(generation=None, mode=None, blocking=None, compacting=None):
        """ Collect(generation: int, mode: GCCollectionMode, blocking: bool)Collect(generation: int, mode: GCCollectionMode, blocking: bool, compacting: bool)Collect(generation: int, mode: GCCollectionMode)Collect(generation: int)Collect() """
        pass

    @staticmethod
    def CollectionCount(generation):
        """ CollectionCount(generation: int) -> int """
        pass

    @staticmethod
    def EndNoGCRegion():
        """ EndNoGCRegion() """
        pass

    @staticmethod
    def GetGeneration(*__args):
        """
        GetGeneration(wo: WeakReference) -> int
        GetGeneration(obj: object) -> int
        """
        pass

    @staticmethod
    def GetTotalMemory(forceFullCollection):
        """ GetTotalMemory(forceFullCollection: bool) -> Int64 """
        pass

    @staticmethod
    def KeepAlive(obj):
        """ KeepAlive(obj: object) """
        pass

    @staticmethod
    def RegisterForFullGCNotification(maxGenerationThreshold, largeObjectHeapThreshold):
        """ RegisterForFullGCNotification(maxGenerationThreshold: int, largeObjectHeapThreshold: int) """
        pass

    @staticmethod
    def RemoveMemoryPressure(bytesAllocated):
        """ RemoveMemoryPressure(bytesAllocated: Int64) """
        pass

    @staticmethod
    def ReRegisterForFinalize(obj):
        """ ReRegisterForFinalize(obj: object) """
        pass

    @staticmethod
    def SuppressFinalize(obj):
        """ SuppressFinalize(obj: object) """
        pass

    @staticmethod
    def TryStartNoGCRegion(totalSize, *__args):
        """
        TryStartNoGCRegion(totalSize: Int64, disallowFullBlockingGC: bool) -> bool
        TryStartNoGCRegion(totalSize: Int64, lohSize: Int64, disallowFullBlockingGC: bool) -> bool
        TryStartNoGCRegion(totalSize: Int64) -> bool
        TryStartNoGCRegion(totalSize: Int64, lohSize: Int64) -> bool
        """
        pass

    @staticmethod
    def WaitForFullGCApproach(millisecondsTimeout=None):
        """
        WaitForFullGCApproach(millisecondsTimeout: int) -> GCNotificationStatus
        WaitForFullGCApproach() -> GCNotificationStatus
        """
        pass

    @staticmethod
    def WaitForFullGCComplete(millisecondsTimeout=None):
        """
        WaitForFullGCComplete(millisecondsTimeout: int) -> GCNotificationStatus
        WaitForFullGCComplete() -> GCNotificationStatus
        """
        pass

    @staticmethod
    def WaitForPendingFinalizers():
        """ WaitForPendingFinalizers() """
        pass

    MaxGeneration = 2
    __all__ = [
        'AddMemoryPressure',
        'CancelFullGCNotification',
        'Collect',
        'CollectionCount',
        'EndNoGCRegion',
        'GetGeneration',
        'GetTotalMemory',
        'KeepAlive',
        'RegisterForFullGCNotification',
        'RemoveMemoryPressure',
        'ReRegisterForFinalize',
        'SuppressFinalize',
        'TryStartNoGCRegion',
        'WaitForFullGCApproach',
        'WaitForFullGCComplete',
        'WaitForPendingFinalizers',
    ]


class GCCollectionMode(Enum):
    """ enum GCCollectionMode, values: Default (0), Forced (1), Optimized (2) """
    Default = None
    Forced = None
    Optimized = None
    value__ = None


class GCNotificationStatus(Enum):
    """ enum GCNotificationStatus, values: Canceled (2), Failed (1), NotApplicable (4), Succeeded (0), Timeout (3) """
    Canceled = None
    Failed = None
    NotApplicable = None
    Succeeded = None
    Timeout = None
    value__ = None


class GenericUriParser(UriParser):
    """ GenericUriParser(options: GenericUriParserOptions) """
    @staticmethod # known case of __new__
    def __new__(self, options):
        """ __new__(cls: type, options: GenericUriParserOptions) """
        pass


class GenericUriParserOptions(Enum):
    """ enum (flags) GenericUriParserOptions, values: AllowEmptyAuthority (2), Default (0), DontCompressPath (128), DontConvertPathBackslashes (64), DontUnescapePathDotsAndSlashes (256), GenericAuthority (1), Idn (512), IriParsing (1024), NoFragment (32), NoPort (8), NoQuery (16), NoUserInfo (4) """
    AllowEmptyAuthority = None
    Default = None
    DontCompressPath = None
    DontConvertPathBackslashes = None
    DontUnescapePathDotsAndSlashes = None
    GenericAuthority = None
    Idn = None
    IriParsing = None
    NoFragment = None
    NoPort = None
    NoQuery = None
    NoUserInfo = None
    value__ = None


class GopherStyleUriParser(UriParser):
    """ GopherStyleUriParser() """

class Guid(object):
    """
    Guid(b: Array[Byte])
    Guid(a: UInt32, b: UInt16, c: UInt16, d: Byte, e: Byte, f: Byte, g: Byte, h: Byte, i: Byte, j: Byte, k: Byte)
    Guid(a: int, b: Int16, c: Int16, d: Array[Byte])
    Guid(a: int, b: Int16, c: Int16, d: Byte, e: Byte, f: Byte, g: Byte, h: Byte, i: Byte, j: Byte, k: Byte)
    Guid(g: str)
    """
    def CompareTo(self, value):
        """
        CompareTo(self: Guid, value: Guid) -> int
        CompareTo(self: Guid, value: object) -> int
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Guid, g: Guid) -> bool
        Equals(self: Guid, o: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Guid) -> int """
        pass

    @staticmethod
    def NewGuid():
        """ NewGuid() -> Guid """
        pass

    @staticmethod
    def Parse(input):
        """ Parse(input: str) -> Guid """
        pass

    @staticmethod
    def ParseExact(input, format):
        """ ParseExact(input: str, format: str) -> Guid """
        pass

    def ToByteArray(self):
        """ ToByteArray(self: Guid) -> Array[Byte] """
        pass

    def ToString(self, format=None, provider=None):
        """
        ToString(self: Guid, format: str, provider: IFormatProvider) -> str
        ToString(self: Guid, format: str) -> str
        ToString(self: Guid) -> str
        """
        pass

    @staticmethod
    def TryParse(input, result):
        """ TryParse(input: str) -> (bool, Guid) """
        pass

    @staticmethod
    def TryParseExact(input, format, result):
        """ TryParseExact(input: str, format: str) -> (bool, Guid) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[Guid]() -> Guid
        
        __new__(cls: type, b: Array[Byte])
        __new__(cls: type, a: UInt32, b: UInt16, c: UInt16, d: Byte, e: Byte, f: Byte, g: Byte, h: Byte, i: Byte, j: Byte, k: Byte)
        __new__(cls: type, a: int, b: Int16, c: Int16, d: Array[Byte])
        __new__(cls: type, a: int, b: Int16, c: Int16, d: Byte, e: Byte, f: Byte, g: Byte, h: Byte, i: Byte, j: Byte, k: Byte)
        __new__(cls: type, g: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Empty = None


class HttpStyleUriParser(UriParser):
    """ HttpStyleUriParser() """

class IAppDomainSetup:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ApplicationBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationBase(self: IAppDomainSetup) -> str

Set: ApplicationBase(self: IAppDomainSetup) = value
"""

    ApplicationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationName(self: IAppDomainSetup) -> str

Set: ApplicationName(self: IAppDomainSetup) = value
"""

    CachePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CachePath(self: IAppDomainSetup) -> str

Set: CachePath(self: IAppDomainSetup) = value
"""

    ConfigurationFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConfigurationFile(self: IAppDomainSetup) -> str

Set: ConfigurationFile(self: IAppDomainSetup) = value
"""

    DynamicBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DynamicBase(self: IAppDomainSetup) -> str

Set: DynamicBase(self: IAppDomainSetup) = value
"""

    LicenseFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicenseFile(self: IAppDomainSetup) -> str

Set: LicenseFile(self: IAppDomainSetup) = value
"""

    PrivateBinPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrivateBinPath(self: IAppDomainSetup) -> str

Set: PrivateBinPath(self: IAppDomainSetup) = value
"""

    PrivateBinPathProbe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrivateBinPathProbe(self: IAppDomainSetup) -> str

Set: PrivateBinPathProbe(self: IAppDomainSetup) = value
"""

    ShadowCopyDirectories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadowCopyDirectories(self: IAppDomainSetup) -> str

Set: ShadowCopyDirectories(self: IAppDomainSetup) = value
"""

    ShadowCopyFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadowCopyFiles(self: IAppDomainSetup) -> str

Set: ShadowCopyFiles(self: IAppDomainSetup) = value
"""



class IAsyncResult:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AsyncState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AsyncState(self: IAsyncResult) -> object

"""

    AsyncWaitHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AsyncWaitHandle(self: IAsyncResult) -> WaitHandle

"""

    CompletedSynchronously = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CompletedSynchronously(self: IAsyncResult) -> bool

"""

    IsCompleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCompleted(self: IAsyncResult) -> bool

"""



class ICustomFormatter:
    # no doc
    def Format(self, format, arg, formatProvider):
        """ Format(self: ICustomFormatter, format: str, arg: object, formatProvider: IFormatProvider) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEquatable:
    # no doc
    def Equals(self, other):
        """ Equals(self: IEquatable[T], other: T) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IFormatProvider:
    # no doc
    def GetFormat(self, formatType):
        """ GetFormat(self: IFormatProvider, formatType: Type) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IndexOutOfRangeException(SystemException):
    """
    IndexOutOfRangeException()
    IndexOutOfRangeException(message: str)
    IndexOutOfRangeException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        """
        pass


class InsufficientExecutionStackException(SystemException):
    """
    InsufficientExecutionStackException()
    InsufficientExecutionStackException(message: str)
    InsufficientExecutionStackException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        """
        pass


class OutOfMemoryException(SystemException):
    """
    OutOfMemoryException()
    OutOfMemoryException(message: str)
    OutOfMemoryException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class InsufficientMemoryException(OutOfMemoryException):
    """
    InsufficientMemoryException()
    InsufficientMemoryException(message: str)
    InsufficientMemoryException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        """
        pass


class Int16(object):
    # no doc
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: Int16) -> int """
        pass

    def CompareTo(self, value):
        """
        CompareTo(self: Int16, value: Int16) -> int
        CompareTo(self: Int16, value: object) -> int
        """
        pass

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: Int16) -> Int16 """
        pass

    def Equals(self, obj):
        """
        Equals(self: Int16, obj: Int16) -> bool
        Equals(self: Int16, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Int16) -> int """
        pass

    def GetTypeCode(self):
        """ GetTypeCode(self: Int16) -> TypeCode """
        pass

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str, provider: IFormatProvider) -> Int16
        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> Int16
        Parse(s: str) -> Int16
        Parse(s: str, style: NumberStyles) -> Int16
        """
        pass

    def ToString(self, *__args):
        """
        ToString(self: Int16, format: str) -> str
        ToString(self: Int16, format: str, provider: IFormatProvider) -> str
        ToString(self: Int16) -> str
        ToString(self: Int16, provider: IFormatProvider) -> str
        """
        pass

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, Int16)
        TryParse(s: str) -> (bool, Int16)
        """
        pass

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: Int16, y: Int16) -> Int16 """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: Int16) -> float """
        pass

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//y """
        pass

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(value: Int16) -> str """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: Int16) -> int """
        pass

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: Int16) -> Int16 """
        pass

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<yx.__rshift__(y) <==> x<<y """
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, value: object) -> object
        __new__(cls: type) -> object
        """
        pass

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: Int16) -> bool """
        pass

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: Int16, y: Int16) -> Int16 """
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: Int16) -> Int16 """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: Int16, y: Int16) -> object """
        pass

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: Int16, y: Int16) -> Int16 """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: Int16, y: Int16) -> object """
        pass

    def __rfloordiv__(self, *args): #cannot find CLR method
        """ __rfloordiv__(x: Int16, y: Int16) -> object """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: Int16, y: Int16) -> Int16 """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: Int16, y: Int16) -> object """
        pass

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: Int16, y: Int16) -> Int16 """
        pass

    def __rpow__(self, *args): #cannot find CLR method
        """ __rpow__(x: Int16, y: Int16) -> object """
        pass

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: Int16, y: Int16) -> object """
        pass

    def __rtruediv__(self, *args): #cannot find CLR method
        """ __rtruediv__(x: Int16, y: Int16) -> float """
        pass

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: Int16, y: Int16) -> Int16 """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/y """
        pass

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: Int16) -> Int16 """
        pass

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: Int16, y: Int16) -> Int16 """
        pass

    denominator = None
    imag = None
    MaxValue = None
    MinValue = None
    numerator = None
    real = None


class Int64(object):
    # no doc
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: Int64) -> int """
        pass

    def CompareTo(self, value):
        """
        CompareTo(self: Int64, value: Int64) -> int
        CompareTo(self: Int64, value: object) -> int
        """
        pass

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: Int64) -> Int64 """
        pass

    def Equals(self, obj):
        """
        Equals(self: Int64, obj: Int64) -> bool
        Equals(self: Int64, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Int64) -> int """
        pass

    def GetTypeCode(self):
        """ GetTypeCode(self: Int64) -> TypeCode """
        pass

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str, provider: IFormatProvider) -> Int64
        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> Int64
        Parse(s: str) -> Int64
        Parse(s: str, style: NumberStyles) -> Int64
        """
        pass

    def ToString(self, *__args):
        """
        ToString(self: Int64, format: str) -> str
        ToString(self: Int64, format: str, provider: IFormatProvider) -> str
        ToString(self: Int64) -> str
        ToString(self: Int64, provider: IFormatProvider) -> str
        """
        pass

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, Int64)
        TryParse(s: str) -> (bool, Int64)
        """
        pass

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: Int64, y: Int64) -> Int64 """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: Int64) -> float """
        pass

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//y """
        pass

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(value: Int64) -> str """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: Int64) -> int """
        pass

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: Int64) -> Int64 """
        pass

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<y """
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, value: object) -> object
        __new__(cls: type) -> object
        """
        pass

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: Int64) -> bool """
        pass

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: Int64, y: Int64) -> Int64 """
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: Int64) -> Int64 """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: Int64, y: Int64) -> object """
        pass

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: Int64, y: Int64) -> Int64 """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: Int64, y: Int64) -> object """
        pass

    def __rfloordiv__(self, *args): #cannot find CLR method
        """ __rfloordiv__(x: Int64, y: Int64) -> object """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: Int64, y: Int64) -> Int64 """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: Int64, y: Int64) -> object """
        pass

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: Int64, y: Int64) -> Int64 """
        pass

    def __rpow__(self, *args): #cannot find CLR method
        """ __rpow__(x: Int64, y: Int64) -> object """
        pass

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: Int64, y: Int64) -> object """
        pass

    def __rtruediv__(self, *args): #cannot find CLR method
        """ __rtruediv__(x: Int64, y: Int64) -> float """
        pass

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: Int64, y: Int64) -> Int64 """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/y """
        pass

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: Int64) -> Int64 """
        pass

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: Int64, y: Int64) -> Int64 """
        pass

    denominator = None
    imag = None
    MaxValue = None
    MinValue = None
    numerator = None
    real = None


class IntPtr(object):
    """
    IntPtr(value: int)
    IntPtr(value: Int64)
    IntPtr(value: Void*)
    """
    @staticmethod
    def Add(pointer, offset):
        """ Add(pointer: IntPtr, offset: int) -> IntPtr """
        pass

    def Equals(self, obj):
        """ Equals(self: IntPtr, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: IntPtr) -> int """
        pass

    @staticmethod
    def Subtract(pointer, offset):
        """ Subtract(pointer: IntPtr, offset: int) -> IntPtr """
        pass

    def ToInt32(self):
        """ ToInt32(self: IntPtr) -> int """
        pass

    def ToInt64(self):
        """ ToInt64(self: IntPtr) -> Int64 """
        pass

    def ToPointer(self):
        """ ToPointer(self: IntPtr) -> Void* """
        pass

    def ToString(self, format=None):
        """
        ToString(self: IntPtr, format: str) -> str
        ToString(self: IntPtr) -> str
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(value: IntPtr) -> int """
        pass

    def __long__(self, *args): #cannot find CLR method
        """ __int__(value: IntPtr) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value):
        """
        __new__[IntPtr]() -> IntPtr
        
        __new__(cls: type, value: int)
        __new__(cls: type, value: Int64)
        __new__(cls: type, value: Void*)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    Size = 8
    Zero = None


class InvalidCastException(SystemException):
    """
    InvalidCastException()
    InvalidCastException(message: str)
    InvalidCastException(message: str, innerException: Exception)
    InvalidCastException(message: str, errorCode: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, message: str, errorCode: int)
        """
        pass


class InvalidOperationException(SystemException):
    """
    InvalidOperationException()
    InvalidOperationException(message: str)
    InvalidOperationException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class InvalidProgramException(SystemException):
    """
    InvalidProgramException()
    InvalidProgramException(message: str)
    InvalidProgramException(message: str, inner: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        """
        pass


class InvalidTimeZoneException(Exception):
    """
    InvalidTimeZoneException(message: str)
    InvalidTimeZoneException(message: str, innerException: Exception)
    InvalidTimeZoneException()
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type)
        """
        pass


class IObservable:
    # no doc
    def Subscribe(self, observer):
        """ Subscribe(self: IObservable[T], observer: IObserver[T]) -> IDisposable """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IObserver:
    # no doc
    def OnCompleted(self):
        """ OnCompleted(self: IObserver[T]) """
        pass

    def OnError(self, error):
        """ OnError(self: IObserver[T], error: Exception) """
        pass

    def OnNext(self, value):
        """ OnNext(self: IObserver[T], value: T) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IProgress:
    # no doc
    def Report(self, value):
        """ Report(self: IProgress[T], value: T) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IServiceProvider:
    # no doc
    def GetService(self, serviceType):
        """ GetService(self: IServiceProvider, serviceType: Type) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Lazy(object):
    """
    Lazy[T](valueFactory: Func[T], mode: LazyThreadSafetyMode)
    Lazy[T]()
    Lazy[T](valueFactory: Func[T])
    Lazy[T](isThreadSafe: bool)
    Lazy[T](mode: LazyThreadSafetyMode)
    Lazy[T](valueFactory: Func[T], isThreadSafe: bool)
    """
    def ToString(self):
        """ ToString(self: Lazy[T]) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, valueFactory: Func[T])
        __new__(cls: type, isThreadSafe: bool)
        __new__(cls: type, mode: LazyThreadSafetyMode)
        __new__(cls: type, valueFactory: Func[T], isThreadSafe: bool)
        __new__(cls: type, valueFactory: Func[T], mode: LazyThreadSafetyMode)
        """
        pass

    IsValueCreated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValueCreated(self: Lazy[T]) -> bool

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: Lazy[T]) -> T

"""



class LdapStyleUriParser(UriParser):
    """ LdapStyleUriParser() """

class LoaderOptimization(Enum):
    """ enum LoaderOptimization, values: DisallowBindings (4), DomainMask (3), MultiDomain (2), MultiDomainHost (3), NotSpecified (0), SingleDomain (1) """
    DisallowBindings = None
    DomainMask = None
    MultiDomain = None
    MultiDomainHost = None
    NotSpecified = None
    SingleDomain = None
    value__ = None


class LoaderOptimizationAttribute(Attribute):
    """
    LoaderOptimizationAttribute(value: Byte)
    LoaderOptimizationAttribute(value: LoaderOptimization)
    """
    @staticmethod # known case of __new__
    def __new__(self, value):
        """
        __new__(cls: type, value: Byte)
        __new__(cls: type, value: LoaderOptimization)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: LoaderOptimizationAttribute) -> LoaderOptimization

"""



class LocalDataStoreSlot(object):
    # no doc

class Math(object):
    # no doc
    @staticmethod
    def Abs(value):
        """
        Abs(value: Single) -> Single
        Abs(value: float) -> float
        Abs(value: Decimal) -> Decimal
        Abs(value: Int64) -> Int64
        Abs(value: SByte) -> SByte
        Abs(value: Int16) -> Int16
        Abs(value: int) -> int
        """
        pass

    @staticmethod
    def Acos(d):
        """ Acos(d: float) -> float """
        pass

    @staticmethod
    def Asin(d):
        """ Asin(d: float) -> float """
        pass

    @staticmethod
    def Atan(d):
        """ Atan(d: float) -> float """
        pass

    @staticmethod
    def Atan2(y, x):
        """ Atan2(y: float, x: float) -> float """
        pass

    @staticmethod
    def BigMul(a, b):
        """ BigMul(a: int, b: int) -> Int64 """
        pass

    @staticmethod
    def Ceiling(*__args):
        """
        Ceiling(a: float) -> float
        Ceiling(d: Decimal) -> Decimal
        """
        pass

    @staticmethod
    def Cos(d):
        """ Cos(d: float) -> float """
        pass

    @staticmethod
    def Cosh(value):
        """ Cosh(value: float) -> float """
        pass

    @staticmethod
    def DivRem(a, b, result):
        """
        DivRem(a: Int64, b: Int64) -> (Int64, Int64)
        DivRem(a: int, b: int) -> (int, int)
        """
        pass

    @staticmethod
    def Exp(d):
        """ Exp(d: float) -> float """
        pass

    @staticmethod
    def Floor(d):
        """
        Floor(d: float) -> float
        Floor(d: Decimal) -> Decimal
        """
        pass

    @staticmethod
    def IEEERemainder(x, y):
        """ IEEERemainder(x: float, y: float) -> float """
        pass

    @staticmethod
    def Log(*__args):
        """
        Log(a: float, newBase: float) -> float
        Log(d: float) -> float
        """
        pass

    @staticmethod
    def Log10(d):
        """ Log10(d: float) -> float """
        pass

    @staticmethod
    def Max(val1, val2):
        """
        Max(val1: UInt64, val2: UInt64) -> UInt64
        Max(val1: Int64, val2: Int64) -> Int64
        Max(val1: Single, val2: Single) -> Single
        Max(val1: Decimal, val2: Decimal) -> Decimal
        Max(val1: float, val2: float) -> float
        Max(val1: UInt32, val2: UInt32) -> UInt32
        Max(val1: Byte, val2: Byte) -> Byte
        Max(val1: SByte, val2: SByte) -> SByte
        Max(val1: Int16, val2: Int16) -> Int16
        Max(val1: int, val2: int) -> int
        Max(val1: UInt16, val2: UInt16) -> UInt16
        """
        pass

    @staticmethod
    def Min(val1, val2):
        """
        Min(val1: UInt64, val2: UInt64) -> UInt64
        Min(val1: Int64, val2: Int64) -> Int64
        Min(val1: Single, val2: Single) -> Single
        Min(val1: Decimal, val2: Decimal) -> Decimal
        Min(val1: float, val2: float) -> float
        Min(val1: UInt32, val2: UInt32) -> UInt32
        Min(val1: Byte, val2: Byte) -> Byte
        Min(val1: SByte, val2: SByte) -> SByte
        Min(val1: Int16, val2: Int16) -> Int16
        Min(val1: int, val2: int) -> int
        Min(val1: UInt16, val2: UInt16) -> UInt16
        """
        pass

    @staticmethod
    def Pow(x, y):
        """ Pow(x: float, y: float) -> float """
        pass

    @staticmethod
    def Round(*__args):
        """
        Round(d: Decimal, decimals: int) -> Decimal
        Round(d: Decimal) -> Decimal
        Round(d: Decimal, decimals: int, mode: MidpointRounding) -> Decimal
        Round(d: Decimal, mode: MidpointRounding) -> Decimal
        Round(value: float, digits: int) -> float
        Round(a: float) -> float
        Round(value: float, digits: int, mode: MidpointRounding) -> float
        Round(value: float, mode: MidpointRounding) -> float
        """
        pass

    @staticmethod
    def Sign(value):
        """
        Sign(value: Single) -> int
        Sign(value: float) -> int
        Sign(value: Decimal) -> int
        Sign(value: Int64) -> int
        Sign(value: SByte) -> int
        Sign(value: Int16) -> int
        Sign(value: int) -> int
        """
        pass

    @staticmethod
    def Sin(a):
        """ Sin(a: float) -> float """
        pass

    @staticmethod
    def Sinh(value):
        """ Sinh(value: float) -> float """
        pass

    @staticmethod
    def Sqrt(d):
        """ Sqrt(d: float) -> float """
        pass

    @staticmethod
    def Tan(a):
        """ Tan(a: float) -> float """
        pass

    @staticmethod
    def Tanh(value):
        """ Tanh(value: float) -> float """
        pass

    @staticmethod
    def Truncate(d):
        """
        Truncate(d: float) -> float
        Truncate(d: Decimal) -> Decimal
        """
        pass

    E = 2.718281828459045
    PI = 3.141592653589793
    __all__ = [
        'Abs',
        'Acos',
        'Asin',
        'Atan',
        'Atan2',
        'BigMul',
        'Ceiling',
        'Cos',
        'Cosh',
        'DivRem',
        'E',
        'Exp',
        'Floor',
        'IEEERemainder',
        'Log',
        'Log10',
        'Max',
        'Min',
        'PI',
        'Pow',
        'Round',
        'Sign',
        'Sin',
        'Sinh',
        'Sqrt',
        'Tan',
        'Tanh',
        'Truncate',
    ]


class MethodAccessException(MemberAccessException):
    """
    MethodAccessException()
    MethodAccessException(message: str)
    MethodAccessException(message: str, inner: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class MidpointRounding(Enum):
    """ enum MidpointRounding, values: AwayFromZero (1), ToEven (0) """
    AwayFromZero = None
    ToEven = None
    value__ = None


class MissingMemberException(MemberAccessException):
    """
    MissingMemberException()
    MissingMemberException(message: str)
    MissingMemberException(message: str, inner: Exception)
    MissingMemberException(className: str, memberName: str)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: MissingMemberException, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, className: str, memberName: str)
        """
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: MissingMemberException) -> str

"""


    ClassName = None
    MemberName = None
    Signature = None


class MissingFieldException(MissingMemberException):
    """
    MissingFieldException()
    MissingFieldException(message: str)
    MissingFieldException(message: str, inner: Exception)
    MissingFieldException(className: str, fieldName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, className: str, fieldName: str)
        """
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: MissingFieldException) -> str

"""


    ClassName = None
    MemberName = None
    Signature = None


class MissingMethodException(MissingMemberException):
    """
    MissingMethodException()
    MissingMethodException(message: str)
    MissingMethodException(message: str, inner: Exception)
    MissingMethodException(className: str, methodName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, className: str, methodName: str)
        """
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: MissingMethodException) -> str

"""


    ClassName = None
    MemberName = None
    Signature = None


class ModuleHandle(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: ModuleHandle, handle: ModuleHandle) -> bool
        Equals(self: ModuleHandle, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ModuleHandle) -> int """
        pass

    def GetRuntimeFieldHandleFromMetadataToken(self, fieldToken):
        """ GetRuntimeFieldHandleFromMetadataToken(self: ModuleHandle, fieldToken: int) -> RuntimeFieldHandle """
        pass

    def GetRuntimeMethodHandleFromMetadataToken(self, methodToken):
        """ GetRuntimeMethodHandleFromMetadataToken(self: ModuleHandle, methodToken: int) -> RuntimeMethodHandle """
        pass

    def GetRuntimeTypeHandleFromMetadataToken(self, typeToken):
        """ GetRuntimeTypeHandleFromMetadataToken(self: ModuleHandle, typeToken: int) -> RuntimeTypeHandle """
        pass

    def ResolveFieldHandle(self, fieldToken, typeInstantiationContext=None, methodInstantiationContext=None):
        """
        ResolveFieldHandle(self: ModuleHandle, fieldToken: int, typeInstantiationContext: Array[RuntimeTypeHandle], methodInstantiationContext: Array[RuntimeTypeHandle]) -> RuntimeFieldHandle
        ResolveFieldHandle(self: ModuleHandle, fieldToken: int) -> RuntimeFieldHandle
        """
        pass

    def ResolveMethodHandle(self, methodToken, typeInstantiationContext=None, methodInstantiationContext=None):
        """
        ResolveMethodHandle(self: ModuleHandle, methodToken: int, typeInstantiationContext: Array[RuntimeTypeHandle], methodInstantiationContext: Array[RuntimeTypeHandle]) -> RuntimeMethodHandle
        ResolveMethodHandle(self: ModuleHandle, methodToken: int) -> RuntimeMethodHandle
        """
        pass

    def ResolveTypeHandle(self, typeToken, typeInstantiationContext=None, methodInstantiationContext=None):
        """
        ResolveTypeHandle(self: ModuleHandle, typeToken: int, typeInstantiationContext: Array[RuntimeTypeHandle], methodInstantiationContext: Array[RuntimeTypeHandle]) -> RuntimeTypeHandle
        ResolveTypeHandle(self: ModuleHandle, typeToken: int) -> RuntimeTypeHandle
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    MDStreamVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MDStreamVersion(self: ModuleHandle) -> int

"""


    EmptyHandle = None


class MTAThreadAttribute(Attribute):
    """ MTAThreadAttribute() """

class MulticastNotSupportedException(SystemException):
    """
    MulticastNotSupportedException()
    MulticastNotSupportedException(message: str)
    MulticastNotSupportedException(message: str, inner: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        """
        pass


class NetPipeStyleUriParser(UriParser):
    """ NetPipeStyleUriParser() """

class NetTcpStyleUriParser(UriParser):
    """ NetTcpStyleUriParser() """

class NewsStyleUriParser(UriParser):
    """ NewsStyleUriParser() """

class NonSerializedAttribute(Attribute):
    """ NonSerializedAttribute() """

class NotFiniteNumberException(ArithmeticException):
    """
    NotFiniteNumberException()
    NotFiniteNumberException(offendingNumber: float)
    NotFiniteNumberException(message: str)
    NotFiniteNumberException(message: str, offendingNumber: float)
    NotFiniteNumberException(message: str, innerException: Exception)
    NotFiniteNumberException(message: str, offendingNumber: float, innerException: Exception)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: NotFiniteNumberException, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, offendingNumber: float)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, offendingNumber: float)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, message: str, offendingNumber: float, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    OffendingNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffendingNumber(self: NotFiniteNumberException) -> float

"""



class NotImplementedException(SystemException):
    """
    NotImplementedException()
    NotImplementedException(message: str)
    NotImplementedException(message: str, inner: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class NotSupportedException(SystemException):
    """
    NotSupportedException()
    NotSupportedException(message: str)
    NotSupportedException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class NullReferenceException(SystemException):
    """
    NullReferenceException()
    NullReferenceException(message: str)
    NullReferenceException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class ObjectDisposedException(InvalidOperationException):
    """
    ObjectDisposedException(objectName: str)
    ObjectDisposedException(objectName: str, message: str)
    ObjectDisposedException(message: str, innerException: Exception)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: ObjectDisposedException, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, objectName: str)
        __new__(cls: type, objectName: str, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: ObjectDisposedException) -> str

"""

    ObjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectName(self: ObjectDisposedException) -> str

"""



class ObsoleteAttribute(Attribute):
    """
    ObsoleteAttribute()
    ObsoleteAttribute(message: str)
    ObsoleteAttribute(message: str, error: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, error=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, error: bool)
        """
        pass

    IsError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsError(self: ObsoleteAttribute) -> bool

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: ObsoleteAttribute) -> str

"""



class OperatingSystem(object):
    """ OperatingSystem(platform: PlatformID, version: Version) """
    def Clone(self):
        """ Clone(self: OperatingSystem) -> object """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: OperatingSystem, info: SerializationInfo, context: StreamingContext) """
        pass

    def ToString(self):
        """ ToString(self: OperatingSystem) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, platform, version):
        """ __new__(cls: type, platform: PlatformID, version: Version) """
        pass

    Platform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Platform(self: OperatingSystem) -> PlatformID

"""

    ServicePack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ServicePack(self: OperatingSystem) -> str

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: OperatingSystem) -> Version

"""

    VersionString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VersionString(self: OperatingSystem) -> str

"""



class OperationCanceledException(SystemException):
    """
    OperationCanceledException()
    OperationCanceledException(message: str)
    OperationCanceledException(message: str, innerException: Exception)
    OperationCanceledException(token: CancellationToken)
    OperationCanceledException(message: str, token: CancellationToken)
    OperationCanceledException(message: str, innerException: Exception, token: CancellationToken)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, token: CancellationToken)
        __new__(cls: type, message: str, token: CancellationToken)
        __new__(cls: type, message: str, innerException: Exception, token: CancellationToken)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    CancellationToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CancellationToken(self: OperationCanceledException) -> CancellationToken

"""



class OverflowException(ArithmeticException):
    """
    OverflowException()
    OverflowException(message: str)
    OverflowException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class ParamArrayAttribute(Attribute):
    """ ParamArrayAttribute() """

class PlatformID(Enum):
    """ enum PlatformID, values: MacOSX (6), Unix (4), Win32NT (2), Win32S (0), Win32Windows (1), WinCE (3), Xbox (5) """
    MacOSX = None
    Unix = None
    value__ = None
    Win32NT = None
    Win32S = None
    Win32Windows = None
    WinCE = None
    Xbox = None


class PlatformNotSupportedException(NotSupportedException):
    """
    PlatformNotSupportedException()
    PlatformNotSupportedException(message: str)
    PlatformNotSupportedException(message: str, inner: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class Predicate(MulticastDelegate):
    """ Predicate[T](object: object, method: IntPtr) """
    def BeginInvoke(self, obj, callback, object):
        """ BeginInvoke(self: Predicate[T], obj: T, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: Predicate[T], result: IAsyncResult) -> bool """
        pass

    def Invoke(self, obj):
        """ Invoke(self: Predicate[T], obj: T) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class Progress(object):
    """
    Progress[T]()
    Progress[T](handler: Action[T])
    """
    def OnReport(self, *args): #cannot find CLR method
        """ OnReport(self: Progress[T], value: T) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, handler=None):
        """
        __new__(cls: type)
        __new__(cls: type, handler: Action[T])
        """
        pass

    ProgressChanged = None


class Random(object):
    """
    Random()
    Random(Seed: int)
    """
    def Next(self, *__args):
        """
        Next(self: Random, maxValue: int) -> int
        Next(self: Random, minValue: int, maxValue: int) -> int
        Next(self: Random) -> int
        """
        pass

    def NextBytes(self, buffer):
        """ NextBytes(self: Random, buffer: Array[Byte]) """
        pass

    def NextDouble(self):
        """ NextDouble(self: Random) -> float """
        pass

    def Sample(self, *args): #cannot find CLR method
        """ Sample(self: Random) -> float """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Seed=None):
        """
        __new__(cls: type)
        __new__(cls: type, Seed: int)
        """
        pass


class RankException(SystemException):
    """
    RankException()
    RankException(message: str)
    RankException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class ResolveEventArgs(EventArgs):
    """
    ResolveEventArgs(name: str)
    ResolveEventArgs(name: str, requestingAssembly: Assembly)
    """
    @staticmethod # known case of __new__
    def __new__(self, name, requestingAssembly=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, requestingAssembly: Assembly)
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ResolveEventArgs) -> str

"""

    RequestingAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RequestingAssembly(self: ResolveEventArgs) -> Assembly

"""



class ResolveEventHandler(MulticastDelegate):
    """ ResolveEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: ResolveEventHandler, sender: object, args: ResolveEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ResolveEventHandler, result: IAsyncResult) -> Assembly """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: ResolveEventHandler, sender: object, args: ResolveEventArgs) -> Assembly """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class RuntimeArgumentHandle(object):
    # no doc

class RuntimeFieldHandle(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RuntimeFieldHandle, handle: RuntimeFieldHandle) -> bool
        Equals(self: RuntimeFieldHandle, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RuntimeFieldHandle) -> int """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: RuntimeFieldHandle, info: SerializationInfo, context: StreamingContext) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: RuntimeFieldHandle) -> IntPtr

"""



class RuntimeMethodHandle(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RuntimeMethodHandle, handle: RuntimeMethodHandle) -> bool
        Equals(self: RuntimeMethodHandle, obj: object) -> bool
        """
        pass

    def GetFunctionPointer(self):
        """ GetFunctionPointer(self: RuntimeMethodHandle) -> IntPtr """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RuntimeMethodHandle) -> int """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: RuntimeMethodHandle, info: SerializationInfo, context: StreamingContext) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: RuntimeMethodHandle) -> IntPtr

"""



class RuntimeTypeHandle(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RuntimeTypeHandle, obj: object) -> bool
        Equals(self: RuntimeTypeHandle, handle: RuntimeTypeHandle) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RuntimeTypeHandle) -> int """
        pass

    def GetModuleHandle(self):
        """ GetModuleHandle(self: RuntimeTypeHandle) -> ModuleHandle """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: RuntimeTypeHandle, info: SerializationInfo, context: StreamingContext) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: RuntimeTypeHandle) -> IntPtr

"""



class SByte(object):
    # no doc
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: SByte) -> int """
        pass

    def CompareTo(self, *__args):
        """
        CompareTo(self: SByte, value: SByte) -> int
        CompareTo(self: SByte, obj: object) -> int
        """
        pass

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: SByte) -> SByte """
        pass

    def Equals(self, obj):
        """
        Equals(self: SByte, obj: SByte) -> bool
        Equals(self: SByte, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: SByte) -> int """
        pass

    def GetTypeCode(self):
        """ GetTypeCode(self: SByte) -> TypeCode """
        pass

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str, provider: IFormatProvider) -> SByte
        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> SByte
        Parse(s: str) -> SByte
        Parse(s: str, style: NumberStyles) -> SByte
        """
        pass

    def ToString(self, *__args):
        """
        ToString(self: SByte, format: str) -> str
        ToString(self: SByte, format: str, provider: IFormatProvider) -> str
        ToString(self: SByte) -> str
        ToString(self: SByte, provider: IFormatProvider) -> str
        """
        pass

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, SByte)
        TryParse(s: str) -> (bool, SByte)
        """
        pass

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: SByte, y: SByte) -> SByte """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: SByte) -> float """
        pass

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//y """
        pass

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(value: SByte) -> str """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: SByte) -> int """
        pass

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: SByte) -> SByte """
        pass

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<yx.__rshift__(y) <==> x<<y """
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, value: object) -> object
        __new__(cls: type) -> object
        """
        pass

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: SByte) -> bool """
        pass

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: SByte, y: SByte) -> SByte """
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: SByte) -> SByte """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: SByte, y: SByte) -> object """
        pass

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: SByte, y: SByte) -> SByte """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: SByte, y: SByte) -> object """
        pass

    def __rfloordiv__(self, *args): #cannot find CLR method
        """ __rfloordiv__(x: SByte, y: SByte) -> object """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: SByte, y: SByte) -> SByte """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: SByte, y: SByte) -> object """
        pass

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: SByte, y: SByte) -> SByte """
        pass

    def __rpow__(self, *args): #cannot find CLR method
        """ __rpow__(x: SByte, y: SByte) -> object """
        pass

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: SByte, y: SByte) -> object """
        pass

    def __rtruediv__(self, *args): #cannot find CLR method
        """ __rtruediv__(x: SByte, y: SByte) -> float """
        pass

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: SByte, y: SByte) -> SByte """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/y """
        pass

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: SByte) -> SByte """
        pass

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: SByte, y: SByte) -> SByte """
        pass

    denominator = None
    imag = None
    MaxValue = None
    MinValue = None
    numerator = None
    real = None


class SerializableAttribute(Attribute):
    """ SerializableAttribute() """

class Single(object):
    # no doc
    def CompareTo(self, value):
        """
        CompareTo(self: Single, value: Single) -> int
        CompareTo(self: Single, value: object) -> int
        """
        pass

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: Single) -> Single """
        pass

    def Equals(self, obj):
        """
        Equals(self: Single, obj: Single) -> bool
        Equals(self: Single, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Single) -> int """
        pass

    def GetTypeCode(self):
        """ GetTypeCode(self: Single) -> TypeCode """
        pass

    @staticmethod
    def IsInfinity(f):
        """ IsInfinity(f: Single) -> bool """
        pass

    @staticmethod
    def IsNaN(f):
        """ IsNaN(f: Single) -> bool """
        pass

    @staticmethod
    def IsNegativeInfinity(f):
        """ IsNegativeInfinity(f: Single) -> bool """
        pass

    @staticmethod
    def IsPositiveInfinity(f):
        """ IsPositiveInfinity(f: Single) -> bool """
        pass

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str, provider: IFormatProvider) -> Single
        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> Single
        Parse(s: str) -> Single
        Parse(s: str, style: NumberStyles) -> Single
        """
        pass

    def ToString(self, *__args):
        """
        ToString(self: Single, format: str) -> str
        ToString(self: Single, format: str, provider: IFormatProvider) -> str
        ToString(self: Single) -> str
        ToString(self: Single, provider: IFormatProvider) -> str
        """
        pass

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, Single)
        TryParse(s: str) -> (bool, Single)
        """
        pass

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: Single) -> float """
        pass

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: Single) -> int """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, s: IList[Byte]) -> object
        __new__(cls: type, x: object) -> object
        __new__(cls: type) -> object
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: Single) -> bool """
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: Single) -> Single """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: Single, y: Single) -> Single """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: Single, y: Single) -> Single """
        pass

    def __rfloordiv__(self, *args): #cannot find CLR method
        """ __rfloordiv__(x: Single, y: Single) -> Single """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: Single, y: Single) -> Single """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: Single, y: Single) -> Single """
        pass

    def __rpow__(self, *args): #cannot find CLR method
        """ __rpow__(x: Single, y: Single) -> Single """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: Single, y: Single) -> Single """
        pass

    def __rtruediv__(self, *args): #cannot find CLR method
        """ __rtruediv__(x: Single, y: Single) -> Single """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/y """
        pass

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: Single) -> object """
        pass

    Epsilon = None
    imag = None
    MaxValue = None
    MinValue = None
    NaN = None
    NegativeInfinity = None
    PositiveInfinity = None
    real = None


class StackOverflowException(SystemException):
    """
    StackOverflowException()
    StackOverflowException(message: str)
    StackOverflowException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        """
        pass


class STAThreadAttribute(Attribute):
    """ STAThreadAttribute() """

class String(object):
    """
    str(value: Char*)
    str(value: Char*, startIndex: int, length: int)
    str(value: SByte*)
    str(value: SByte*, startIndex: int, length: int)
    str(value: SByte*, startIndex: int, length: int, enc: Encoding)
    str(value: Array[Char], startIndex: int, length: int)
    str(value: Array[Char])
    str(c: Char, count: int)
    """
    def capitalize(self, *args): #cannot find CLR method
        """ capitalize(self: str) -> str """
        pass

    def center(self, *args): #cannot find CLR method
        """
        center(self: str, width: int, fillchar: Char) -> str
        center(self: str, width: int) -> str
        """
        pass

    def count(self, *args): #cannot find CLR method
        """
        count(self: str, ssub: str, start: int, end: int) -> int
        count(self: str, sub: str, start: int) -> int
        count(self: str, sub: str) -> int
        """
        pass

    def decode(self, *args): #cannot find CLR method
        """
        decode(s: str, encoding: object, errors: str) -> str
        decode(s: str) -> str
        """
        pass

    def encode(self, *args): #cannot find CLR method
        """ encode(s: str, encoding: object, errors: str) -> str """
        pass

    def endswith(self, *args): #cannot find CLR method
        """
        endswith(self: str, suffix: object, start: int, end: int) -> bool
        endswith(self: str, suffix: object, start: int) -> bool
        endswith(self: str, suffix: object) -> bool
        """
        pass

    def expandtabs(self, *args): #cannot find CLR method
        """
        expandtabs(self: str, tabsize: int) -> str
        expandtabs(self: str) -> str
        """
        pass

    def find(self, *args): #cannot find CLR method
        """
        find(self: str, sub: str, start: int, end: int) -> int
        find(self: str, sub: str, start: long, end: long) -> int
        find(self: str, sub: str, start: object, end: object) -> int
        find(self: str, sub: str) -> int
        find(self: str, sub: str, start: int) -> int
        find(self: str, sub: str, start: long) -> int
        """
        pass

    def format(self, *args): #cannot find CLR method
        """
        format(format_string: str, **kwargs: dict, *args: Array[object]) -> str
        format(format_string: str, *args: Array[object]) -> str
        """
        pass

    def index(self, *args): #cannot find CLR method
        """
        index(self: str, sub: str, start: int, end: int) -> int
        index(self: str, sub: str, start: object, end: object) -> int
        index(self: str, sub: str) -> int
        index(self: str, sub: str, start: int) -> int
        """
        pass

    def isalnum(self, *args): #cannot find CLR method
        """ isalnum(self: str) -> bool """
        pass

    def isalpha(self, *args): #cannot find CLR method
        """ isalpha(self: str) -> bool """
        pass

    def isdecimal(self, *args): #cannot find CLR method
        """ isdecimal(self: str) -> bool """
        pass

    def isdigit(self, *args): #cannot find CLR method
        """ isdigit(self: str) -> bool """
        pass

    def islower(self, *args): #cannot find CLR method
        """ islower(self: str) -> bool """
        pass

    def isnumeric(self, *args): #cannot find CLR method
        """ isnumeric(self: str) -> bool """
        pass

    def isspace(self, *args): #cannot find CLR method
        """ isspace(self: str) -> bool """
        pass

    def istitle(self, *args): #cannot find CLR method
        """ istitle(self: str) -> bool """
        pass

    def isunicode(self, *args): #cannot find CLR method
        """ isunicode(self: str) -> bool """
        pass

    def isupper(self, *args): #cannot find CLR method
        """ isupper(self: str) -> bool """
        pass

    def join(self, *args): #cannot find CLR method
        """
        join(self: str, sequence: list) -> str
        join(self: str, sequence: object) -> str
        """
        pass

    def ljust(self, *args): #cannot find CLR method
        """
        ljust(self: str, width: int, fillchar: Char) -> str
        ljust(self: str, width: int) -> str
        """
        pass

    def lower(self, *args): #cannot find CLR method
        """ lower(self: str) -> str """
        pass

    def lstrip(self, *args): #cannot find CLR method
        """
        lstrip(self: str, chars: str) -> str
        lstrip(self: str) -> str
        """
        pass

    def partition(self, *args): #cannot find CLR method
        """ partition(self: str, sep: str) -> tuple (of str) """
        pass

    def replace(self, *args): #cannot find CLR method
        """ replace(self: str, old: object, new_: object, maxsplit: int) -> str """
        pass

    def rfind(self, *args): #cannot find CLR method
        """
        rfind(self: str, sub: str, start: int, end: int) -> int
        rfind(self: str, sub: str, start: long, end: long) -> int
        rfind(self: str, sub: str, start: object, end: object) -> int
        rfind(self: str, sub: str) -> int
        rfind(self: str, sub: str, start: int) -> int
        rfind(self: str, sub: str, start: long) -> int
        """
        pass

    def rindex(self, *args): #cannot find CLR method
        """
        rindex(self: str, sub: str, start: int, end: int) -> int
        rindex(self: str, sub: str, start: object, end: object) -> int
        rindex(self: str, sub: str) -> int
        rindex(self: str, sub: str, start: int) -> int
        """
        pass

    def rjust(self, *args): #cannot find CLR method
        """
        rjust(self: str, width: int, fillchar: Char) -> str
        rjust(self: str, width: int) -> str
        """
        pass

    def rpartition(self, *args): #cannot find CLR method
        """ rpartition(self: str, sep: str) -> tuple (of str) """
        pass

    def rsplit(self, *args): #cannot find CLR method
        """
        rsplit(self: str, sep: str, maxsplit: int) -> list
        rsplit(self: str, sep: str) -> list
        rsplit(self: str) -> list
        """
        pass

    def rstrip(self, *args): #cannot find CLR method
        """
        rstrip(self: str, chars: str) -> str
        rstrip(self: str) -> str
        """
        pass

    def split(self, *args): #cannot find CLR method
        """
        split(self: str, sep: str, maxsplit: int) -> list
        split(self: str, sep: str) -> list
        split(self: str) -> list
        """
        pass

    def splitlines(self, *args): #cannot find CLR method
        """
        splitlines(self: str, keepends: bool) -> list
        splitlines(self: str) -> list
        """
        pass

    def startswith(self, *args): #cannot find CLR method
        """
        startswith(self: str, prefix: object, start: int, end: int) -> bool
        startswith(self: str, prefix: object, start: int) -> bool
        startswith(self: str, prefix: object) -> bool
        """
        pass

    def strip(self, *args): #cannot find CLR method
        """
        strip(self: str, chars: str) -> str
        strip(self: str) -> str
        """
        pass

    def swapcase(self, *args): #cannot find CLR method
        """ swapcase(self: str) -> str """
        pass

    def title(self, *args): #cannot find CLR method
        """ title(self: str) -> str """
        pass

    def translate(self, *args): #cannot find CLR method
        """
        translate(self: str, table: str, deletechars: str) -> str
        translate(self: str, table: str) -> str
        translate(self: str, table: dict) -> str
        """
        pass

    def upper(self, *args): #cannot find CLR method
        """ upper(self: str) -> str """
        pass

    def zfill(self, *args): #cannot find CLR method
        """ zfill(self: str, width: int) -> str """
        pass

    def _formatter_field_name_split(self, *args): #cannot find CLR method
        """ _formatter_field_name_split(self: str) -> tuple """
        pass

    def _formatter_parser(self, *args): #cannot find CLR method
        """ _formatter_parser(self: str) -> IEnumerable[tuple] """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(s: str, item: Char) -> bool
        __contains__(s: str, item: str) -> bool
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __getnewargs__(self, *args): #cannot find CLR method
        """ __getnewargs__(self: str) -> object """
        pass

    def __getslice__(self, *args): #cannot find CLR method
        """ __getslice__(self: str, x: int, y: int) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, object: float) -> object
        __new__(cls: type, object: bool) -> object
        __new__(cls: type, object: int) -> object
        __new__(cls: type, string: object, encoding: str, errors: str) -> object
        __new__(cls: type, object: Single) -> object
        __new__(cls: type, object: Extensible[float]) -> object
        __new__(cls: type, object: Extensible[long]) -> object
        __new__(cls: type, object: str) -> object
        __new__(cls: type, object: object) -> object
        __new__(cls: type) -> object
        __new__(cls: type, object: long) -> object
        __new__(cls: type, object: Char) -> object
        __new__(cls: type, object: ExtensibleString) -> object
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(self: Char, other: str) -> str
        __radd__(self: str, other: str) -> str
        """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(other: object, self: str) -> object """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(count: object, self: str) -> object
        __rmul__(count: Index, self: str) -> object
        __rmul__(other: int, self: str) -> str
        """
        pass


class StringComparer(object):
    # no doc
    def Compare(self, x, y):
        """
        Compare(self: StringComparer, x: str, y: str) -> int
        Compare(self: StringComparer, x: object, y: object) -> int
        """
        pass

    @staticmethod
    def Create(culture, ignoreCase):
        """ Create(culture: CultureInfo, ignoreCase: bool) -> StringComparer """
        pass

    def Equals(self, *__args):
        """
        Equals(self: StringComparer, x: str, y: str) -> bool
        Equals(self: StringComparer, x: object, y: object) -> bool
        """
        pass

    def GetHashCode(self, obj=None):
        """
        GetHashCode(self: StringComparer, obj: str) -> int
        GetHashCode(self: StringComparer, obj: object) -> int
        """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    CurrentCulture = None
    CurrentCultureIgnoreCase = None
    InvariantCulture = None
    InvariantCultureIgnoreCase = None
    Ordinal = None
    OrdinalIgnoreCase = None


class StringComparison(Enum):
    """ enum StringComparison, values: CurrentCulture (0), CurrentCultureIgnoreCase (1), InvariantCulture (2), InvariantCultureIgnoreCase (3), Ordinal (4), OrdinalIgnoreCase (5) """
    CurrentCulture = None
    CurrentCultureIgnoreCase = None
    InvariantCulture = None
    InvariantCultureIgnoreCase = None
    Ordinal = None
    OrdinalIgnoreCase = None
    value__ = None


class StringSplitOptions(Enum):
    """ enum (flags) StringSplitOptions, values: None (0), RemoveEmptyEntries (1) """
    None = None
    RemoveEmptyEntries = None
    value__ = None


class ThreadStaticAttribute(Attribute):
    """ ThreadStaticAttribute() """

class TimeoutException(SystemException):
    """
    TimeoutException()
    TimeoutException(message: str)
    TimeoutException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class TimeSpan(object):
    """
    TimeSpan(ticks: Int64)
    TimeSpan(hours: int, minutes: int, seconds: int)
    TimeSpan(days: int, hours: int, minutes: int, seconds: int)
    TimeSpan(days: int, hours: int, minutes: int, seconds: int, milliseconds: int)
    """
    def Add(self, ts):
        """ Add(self: TimeSpan, ts: TimeSpan) -> TimeSpan """
        pass

    @staticmethod
    def Compare(t1, t2):
        """ Compare(t1: TimeSpan, t2: TimeSpan) -> int """
        pass

    def CompareTo(self, value):
        """
        CompareTo(self: TimeSpan, value: TimeSpan) -> int
        CompareTo(self: TimeSpan, value: object) -> int
        """
        pass

    def Duration(self):
        """ Duration(self: TimeSpan) -> TimeSpan """
        pass

    def Equals(self, *__args):
        """
        Equals(t1: TimeSpan, t2: TimeSpan) -> bool
        Equals(self: TimeSpan, obj: TimeSpan) -> bool
        Equals(self: TimeSpan, value: object) -> bool
        """
        pass

    @staticmethod
    def FromDays(value):
        """ FromDays(value: float) -> TimeSpan """
        pass

    @staticmethod
    def FromHours(value):
        """ FromHours(value: float) -> TimeSpan """
        pass

    @staticmethod
    def FromMilliseconds(value):
        """ FromMilliseconds(value: float) -> TimeSpan """
        pass

    @staticmethod
    def FromMinutes(value):
        """ FromMinutes(value: float) -> TimeSpan """
        pass

    @staticmethod
    def FromSeconds(value):
        """ FromSeconds(value: float) -> TimeSpan """
        pass

    @staticmethod
    def FromTicks(value):
        """ FromTicks(value: Int64) -> TimeSpan """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: TimeSpan) -> int """
        pass

    def Negate(self):
        """ Negate(self: TimeSpan) -> TimeSpan """
        pass

    @staticmethod
    def Parse(*__args):
        """
        Parse(input: str, formatProvider: IFormatProvider) -> TimeSpan
        Parse(s: str) -> TimeSpan
        """
        pass

    @staticmethod
    def ParseExact(input, *__args):
        """
        ParseExact(input: str, format: str, formatProvider: IFormatProvider, styles: TimeSpanStyles) -> TimeSpan
        ParseExact(input: str, formats: Array[str], formatProvider: IFormatProvider, styles: TimeSpanStyles) -> TimeSpan
        ParseExact(input: str, format: str, formatProvider: IFormatProvider) -> TimeSpan
        ParseExact(input: str, formats: Array[str], formatProvider: IFormatProvider) -> TimeSpan
        """
        pass

    def Subtract(self, ts):
        """ Subtract(self: TimeSpan, ts: TimeSpan) -> TimeSpan """
        pass

    def ToString(self, format=None, formatProvider=None):
        """
        ToString(self: TimeSpan, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: TimeSpan, format: str) -> str
        ToString(self: TimeSpan) -> str
        """
        pass

    @staticmethod
    def TryParse(*__args):
        """
        TryParse(input: str, formatProvider: IFormatProvider) -> (bool, TimeSpan)
        TryParse(s: str) -> (bool, TimeSpan)
        """
        pass

    @staticmethod
    def TryParseExact(input, *__args):
        """
        TryParseExact(input: str, format: str, formatProvider: IFormatProvider, styles: TimeSpanStyles) -> (bool, TimeSpan)
        TryParseExact(input: str, formats: Array[str], formatProvider: IFormatProvider, styles: TimeSpanStyles) -> (bool, TimeSpan)
        TryParseExact(input: str, format: str, formatProvider: IFormatProvider) -> (bool, TimeSpan)
        TryParseExact(input: str, formats: Array[str], formatProvider: IFormatProvider) -> (bool, TimeSpan)
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[TimeSpan]() -> TimeSpan
        
        __new__(cls: type, ticks: Int64)
        __new__(cls: type, hours: int, minutes: int, seconds: int)
        __new__(cls: type, days: int, hours: int, minutes: int, seconds: int)
        __new__(cls: type, days: int, hours: int, minutes: int, seconds: int, milliseconds: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(t: TimeSpan) -> TimeSpan """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(t1: TimeSpan, t2: TimeSpan) -> TimeSpan """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(t1: TimeSpan, t2: TimeSpan) -> TimeSpan """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    Days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Days(self: TimeSpan) -> int

"""

    Hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hours(self: TimeSpan) -> int

"""

    Milliseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Milliseconds(self: TimeSpan) -> int

"""

    Minutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Minutes(self: TimeSpan) -> int

"""

    Seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Seconds(self: TimeSpan) -> int

"""

    Ticks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ticks(self: TimeSpan) -> Int64

"""

    TotalDays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalDays(self: TimeSpan) -> float

"""

    TotalHours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalHours(self: TimeSpan) -> float

"""

    TotalMilliseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalMilliseconds(self: TimeSpan) -> float

"""

    TotalMinutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalMinutes(self: TimeSpan) -> float

"""

    TotalSeconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalSeconds(self: TimeSpan) -> float

"""


    MaxValue = None
    MinValue = None
    TicksPerDay = None
    TicksPerHour = None
    TicksPerMillisecond = None
    TicksPerMinute = None
    TicksPerSecond = None
    Zero = None


class TimeZone(object):
    # no doc
    def GetDaylightChanges(self, year):
        """ GetDaylightChanges(self: TimeZone, year: int) -> DaylightTime """
        pass

    def GetUtcOffset(self, time):
        """ GetUtcOffset(self: TimeZone, time: DateTime) -> TimeSpan """
        pass

    def IsDaylightSavingTime(self, time, daylightTimes=None):
        """
        IsDaylightSavingTime(time: DateTime, daylightTimes: DaylightTime) -> bool
        IsDaylightSavingTime(self: TimeZone, time: DateTime) -> bool
        """
        pass

    def ToLocalTime(self, time):
        """ ToLocalTime(self: TimeZone, time: DateTime) -> DateTime """
        pass

    def ToUniversalTime(self, time):
        """ ToUniversalTime(self: TimeZone, time: DateTime) -> DateTime """
        pass

    DaylightName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DaylightName(self: TimeZone) -> str

"""

    StandardName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StandardName(self: TimeZone) -> str

"""


    CurrentTimeZone = None


class TimeZoneInfo(object):
    # no doc
    @staticmethod
    def ClearCachedData():
        """ ClearCachedData() """
        pass

    @staticmethod
    def ConvertTime(*__args):
        """
        ConvertTime(dateTime: DateTime, sourceTimeZone: TimeZoneInfo, destinationTimeZone: TimeZoneInfo) -> DateTime
        ConvertTime(dateTime: DateTime, destinationTimeZone: TimeZoneInfo) -> DateTime
        ConvertTime(dateTimeOffset: DateTimeOffset, destinationTimeZone: TimeZoneInfo) -> DateTimeOffset
        """
        pass

    @staticmethod
    def ConvertTimeBySystemTimeZoneId(*__args):
        """
        ConvertTimeBySystemTimeZoneId(dateTime: DateTime, sourceTimeZoneId: str, destinationTimeZoneId: str) -> DateTime
        ConvertTimeBySystemTimeZoneId(dateTime: DateTime, destinationTimeZoneId: str) -> DateTime
        ConvertTimeBySystemTimeZoneId(dateTimeOffset: DateTimeOffset, destinationTimeZoneId: str) -> DateTimeOffset
        """
        pass

    @staticmethod
    def ConvertTimeFromUtc(dateTime, destinationTimeZone):
        """ ConvertTimeFromUtc(dateTime: DateTime, destinationTimeZone: TimeZoneInfo) -> DateTime """
        pass

    @staticmethod
    def ConvertTimeToUtc(dateTime, sourceTimeZone=None):
        """
        ConvertTimeToUtc(dateTime: DateTime, sourceTimeZone: TimeZoneInfo) -> DateTime
        ConvertTimeToUtc(dateTime: DateTime) -> DateTime
        """
        pass

    @staticmethod
    def CreateCustomTimeZone(id, baseUtcOffset, displayName, standardDisplayName, daylightDisplayName=None, adjustmentRules=None, disableDaylightSavingTime=None):
        """
        CreateCustomTimeZone(id: str, baseUtcOffset: TimeSpan, displayName: str, standardDisplayName: str, daylightDisplayName: str, adjustmentRules: Array[AdjustmentRule], disableDaylightSavingTime: bool) -> TimeZoneInfo
        CreateCustomTimeZone(id: str, baseUtcOffset: TimeSpan, displayName: str, standardDisplayName: str, daylightDisplayName: str, adjustmentRules: Array[AdjustmentRule]) -> TimeZoneInfo
        CreateCustomTimeZone(id: str, baseUtcOffset: TimeSpan, displayName: str, standardDisplayName: str) -> TimeZoneInfo
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: TimeZoneInfo, obj: object) -> bool
        Equals(self: TimeZoneInfo, other: TimeZoneInfo) -> bool
        """
        pass

    @staticmethod
    def FindSystemTimeZoneById(id):
        """ FindSystemTimeZoneById(id: str) -> TimeZoneInfo """
        pass

    @staticmethod
    def FromSerializedString(source):
        """ FromSerializedString(source: str) -> TimeZoneInfo """
        pass

    def GetAdjustmentRules(self):
        """ GetAdjustmentRules(self: TimeZoneInfo) -> Array[AdjustmentRule] """
        pass

    def GetAmbiguousTimeOffsets(self, *__args):
        """
        GetAmbiguousTimeOffsets(self: TimeZoneInfo, dateTime: DateTime) -> Array[TimeSpan]
        GetAmbiguousTimeOffsets(self: TimeZoneInfo, dateTimeOffset: DateTimeOffset) -> Array[TimeSpan]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: TimeZoneInfo) -> int """
        pass

    @staticmethod
    def GetSystemTimeZones():
        """ GetSystemTimeZones() -> ReadOnlyCollection[TimeZoneInfo] """
        pass

    def GetUtcOffset(self, *__args):
        """
        GetUtcOffset(self: TimeZoneInfo, dateTime: DateTime) -> TimeSpan
        GetUtcOffset(self: TimeZoneInfo, dateTimeOffset: DateTimeOffset) -> TimeSpan
        """
        pass

    def HasSameRules(self, other):
        """ HasSameRules(self: TimeZoneInfo, other: TimeZoneInfo) -> bool """
        pass

    def IsAmbiguousTime(self, *__args):
        """
        IsAmbiguousTime(self: TimeZoneInfo, dateTime: DateTime) -> bool
        IsAmbiguousTime(self: TimeZoneInfo, dateTimeOffset: DateTimeOffset) -> bool
        """
        pass

    def IsDaylightSavingTime(self, *__args):
        """
        IsDaylightSavingTime(self: TimeZoneInfo, dateTime: DateTime) -> bool
        IsDaylightSavingTime(self: TimeZoneInfo, dateTimeOffset: DateTimeOffset) -> bool
        """
        pass

    def IsInvalidTime(self, dateTime):
        """ IsInvalidTime(self: TimeZoneInfo, dateTime: DateTime) -> bool """
        pass

    def ToSerializedString(self):
        """ ToSerializedString(self: TimeZoneInfo) -> str """
        pass

    def ToString(self):
        """ ToString(self: TimeZoneInfo) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    BaseUtcOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseUtcOffset(self: TimeZoneInfo) -> TimeSpan

"""

    DaylightName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DaylightName(self: TimeZoneInfo) -> str

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: TimeZoneInfo) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: TimeZoneInfo) -> str

"""

    StandardName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StandardName(self: TimeZoneInfo) -> str

"""

    SupportsDaylightSavingTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportsDaylightSavingTime(self: TimeZoneInfo) -> bool

"""


    AdjustmentRule = None
    Local = None
    TransitionTime = None
    Utc = None


class TimeZoneNotFoundException(Exception):
    """
    TimeZoneNotFoundException(message: str)
    TimeZoneNotFoundException(message: str, innerException: Exception)
    TimeZoneNotFoundException()
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type)
        """
        pass


class TupleExtensions(object):
    # no doc
    @staticmethod
    def Deconstruct(value, item1, item2=None, item3=None, item4=None, item5=None, item6=None, item7=None, item8=None, item9=None, item10=None, item11=None, item12=None, item13=None, item14=None, item15=None, item16=None, item17=None, item18=None, item19=None, item20=None, item21=None):
        """
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15]]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15)
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16]]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16)
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14)
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12)
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13)
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20]]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20)
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20, T21]]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21)
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19]]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19)
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17]]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17)
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18]]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18)
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11)
        Deconstruct[(T1, T2, T3, T4)](value: Tuple[T1, T2, T3, T4]) -> (T1, T2, T3, T4)
        Deconstruct[(T1, T2, T3, T4, T5)](value: Tuple[T1, T2, T3, T4, T5]) -> (T1, T2, T3, T4, T5)
        Deconstruct[(T1, T2, T3)](value: Tuple[T1, T2, T3]) -> (T1, T2, T3)
        Deconstruct[T1](value: Tuple[T1]) -> T1
        Deconstruct[(T1, T2)](value: Tuple[T1, T2]) -> (T1, T2)
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9)
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10]]) -> (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10)
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7, T8)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]) -> (T1, T2, T3, T4, T5, T6, T7, T8)
        Deconstruct[(T1, T2, T3, T4, T5, T6)](value: Tuple[T1, T2, T3, T4, T5, T6]) -> (T1, T2, T3, T4, T5, T6)
        Deconstruct[(T1, T2, T3, T4, T5, T6, T7)](value: Tuple[T1, T2, T3, T4, T5, T6, T7]) -> (T1, T2, T3, T4, T5, T6, T7)
        """
        pass

    @staticmethod
    def ToTuple(value):
        """
        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15]]]
        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16]]]
        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14]]
        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12]]
        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13]]
        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19, T20]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20]]]
        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19, T20, T21]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20, T21]]]
        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19]]]
        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17]]]
        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18]]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18]]]
        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11]]
        ToTuple[(T1, T2, T3, T4)](value: ValueTuple[T1, T2, T3, T4]) -> Tuple[T1, T2, T3, T4]
        ToTuple[(T1, T2, T3, T4, T5)](value: ValueTuple[T1, T2, T3, T4, T5]) -> Tuple[T1, T2, T3, T4, T5]
        ToTuple[(T1, T2, T3)](value: ValueTuple[T1, T2, T3]) -> Tuple[T1, T2, T3]
        ToTuple[T1](value: ValueTuple[T1]) -> Tuple[T1]
        ToTuple[(T1, T2)](value: ValueTuple[T1, T2]) -> Tuple[T1, T2]
        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9]]
        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10]]
        ToTuple[(T1, T2, T3, T4, T5, T6, T7, T8)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8]]) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]
        ToTuple[(T1, T2, T3, T4, T5, T6)](value: ValueTuple[T1, T2, T3, T4, T5, T6]) -> Tuple[T1, T2, T3, T4, T5, T6]
        ToTuple[(T1, T2, T3, T4, T5, T6, T7)](value: ValueTuple[T1, T2, T3, T4, T5, T6, T7]) -> Tuple[T1, T2, T3, T4, T5, T6, T7]
        """
        pass

    @staticmethod
    def ToValueTuple(value):
        """
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15]]]
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16]]]
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14]]
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12]]
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13]]
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19, T20]]]
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19, T20, T21]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19, T20, T21]]]
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18, T19]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18, T19]]]
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17]]]
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14, Tuple[T15, T16, T17, T18]]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14, ValueTuple[T15, T16, T17, T18]]]
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11]]
        ToValueTuple[(T1, T2, T3, T4)](value: Tuple[T1, T2, T3, T4]) -> ValueTuple[T1, T2, T3, T4]
        ToValueTuple[(T1, T2, T3, T4, T5)](value: Tuple[T1, T2, T3, T4, T5]) -> ValueTuple[T1, T2, T3, T4, T5]
        ToValueTuple[(T1, T2, T3)](value: Tuple[T1, T2, T3]) -> ValueTuple[T1, T2, T3]
        ToValueTuple[T1](value: Tuple[T1]) -> ValueTuple[T1]
        ToValueTuple[(T1, T2)](value: Tuple[T1, T2]) -> ValueTuple[T1, T2]
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9]]
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10]]
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7, T8)](value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8]]
        ToValueTuple[(T1, T2, T3, T4, T5, T6)](value: Tuple[T1, T2, T3, T4, T5, T6]) -> ValueTuple[T1, T2, T3, T4, T5, T6]
        ToValueTuple[(T1, T2, T3, T4, T5, T6, T7)](value: Tuple[T1, T2, T3, T4, T5, T6, T7]) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7]
        """
        pass

    __all__ = [
        'Deconstruct',
        'ToTuple',
        'ToValueTuple',
    ]


class Type(MemberInfo):
    # no doc
    def Equals(self, o):
        """
        Equals(self: Type, o: Type) -> bool
        Equals(self: Type, o: object) -> bool
        """
        pass

    def FilterAttribute(self, *args): #cannot find CLR method
        """ MemberFilter(object: object, method: IntPtr) """
        pass

    def FilterName(self, *args): #cannot find CLR method
        """ MemberFilter(object: object, method: IntPtr) """
        pass

    def FilterNameIgnoreCase(self, *args): #cannot find CLR method
        """ MemberFilter(object: object, method: IntPtr) """
        pass

    def FindInterfaces(self, filter, filterCriteria):
        """ FindInterfaces(self: Type, filter: TypeFilter, filterCriteria: object) -> Array[Type] """
        pass

    def FindMembers(self, memberType, bindingAttr, filter, filterCriteria):
        """ FindMembers(self: Type, memberType: MemberTypes, bindingAttr: BindingFlags, filter: MemberFilter, filterCriteria: object) -> Array[MemberInfo] """
        pass

    def GetArrayRank(self):
        """ GetArrayRank(self: Type) -> int """
        pass

    def GetAttributeFlagsImpl(self, *args): #cannot find CLR method
        """ GetAttributeFlagsImpl(self: Type) -> TypeAttributes """
        pass

    def GetConstructor(self, *__args):
        """
        GetConstructor(self: Type, types: Array[Type]) -> ConstructorInfo
        GetConstructor(self: Type, bindingAttr: BindingFlags, binder: Binder, types: Array[Type], modifiers: Array[ParameterModifier]) -> ConstructorInfo
        GetConstructor(self: Type, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> ConstructorInfo
        """
        pass

    def GetConstructorImpl(self, *args): #cannot find CLR method
        """ GetConstructorImpl(self: Type, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> ConstructorInfo """
        pass

    def GetConstructors(self, bindingAttr=None):
        """
        GetConstructors(self: Type) -> Array[ConstructorInfo]
        GetConstructors(self: Type, bindingAttr: BindingFlags) -> Array[ConstructorInfo]
        """
        pass

    def GetDefaultMembers(self):
        """ GetDefaultMembers(self: Type) -> Array[MemberInfo] """
        pass

    def GetElementType(self):
        """ GetElementType(self: Type) -> Type """
        pass

    def GetEnumName(self, value):
        """ GetEnumName(self: Type, value: object) -> str """
        pass

    def GetEnumNames(self):
        """ GetEnumNames(self: Type) -> Array[str] """
        pass

    def GetEnumUnderlyingType(self):
        """ GetEnumUnderlyingType(self: Type) -> Type """
        pass

    def GetEnumValues(self):
        """ GetEnumValues(self: Type) -> Array """
        pass

    def GetEvent(self, name, bindingAttr=None):
        """
        GetEvent(self: Type, name: str, bindingAttr: BindingFlags) -> EventInfo
        GetEvent(self: Type, name: str) -> EventInfo
        """
        pass

    def GetEvents(self, bindingAttr=None):
        """
        GetEvents(self: Type, bindingAttr: BindingFlags) -> Array[EventInfo]
        GetEvents(self: Type) -> Array[EventInfo]
        """
        pass

    def GetField(self, name, bindingAttr=None):
        """
        GetField(self: Type, name: str) -> FieldInfo
        GetField(self: Type, name: str, bindingAttr: BindingFlags) -> FieldInfo
        """
        pass

    def GetFields(self, bindingAttr=None):
        """
        GetFields(self: Type, bindingAttr: BindingFlags) -> Array[FieldInfo]
        GetFields(self: Type) -> Array[FieldInfo]
        """
        pass

    def GetGenericArguments(self):
        """ GetGenericArguments(self: Type) -> Array[Type] """
        pass

    def GetGenericParameterConstraints(self):
        """ GetGenericParameterConstraints(self: Type) -> Array[Type] """
        pass

    def GetGenericTypeDefinition(self):
        """ GetGenericTypeDefinition(self: Type) -> Type """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Type) -> int """
        pass

    def GetInterface(self, name, ignoreCase=None):
        """
        GetInterface(self: Type, name: str, ignoreCase: bool) -> Type
        GetInterface(self: Type, name: str) -> Type
        """
        pass

    def GetInterfaceMap(self, interfaceType):
        """ GetInterfaceMap(self: Type, interfaceType: Type) -> InterfaceMapping """
        pass

    def GetInterfaces(self):
        """ GetInterfaces(self: Type) -> Array[Type] """
        pass

    def GetMember(self, name, *__args):
        """
        GetMember(self: Type, name: str, type: MemberTypes, bindingAttr: BindingFlags) -> Array[MemberInfo]
        GetMember(self: Type, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]
        GetMember(self: Type, name: str) -> Array[MemberInfo]
        """
        pass

    def GetMembers(self, bindingAttr=None):
        """
        GetMembers(self: Type, bindingAttr: BindingFlags) -> Array[MemberInfo]
        GetMembers(self: Type) -> Array[MemberInfo]
        """
        pass

    def GetMethod(self, name, *__args):
        """
        GetMethod(self: Type, name: str, types: Array[Type]) -> MethodInfo
        GetMethod(self: Type, name: str, bindingAttr: BindingFlags) -> MethodInfo
        GetMethod(self: Type, name: str) -> MethodInfo
        GetMethod(self: Type, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        GetMethod(self: Type, name: str, bindingAttr: BindingFlags, binder: Binder, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        GetMethod(self: Type, name: str, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: Type, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo """
        pass

    def GetMethods(self, bindingAttr=None):
        """
        GetMethods(self: Type) -> Array[MethodInfo]
        GetMethods(self: Type, bindingAttr: BindingFlags) -> Array[MethodInfo]
        """
        pass

    def GetNestedType(self, name, bindingAttr=None):
        """
        GetNestedType(self: Type, name: str, bindingAttr: BindingFlags) -> Type
        GetNestedType(self: Type, name: str) -> Type
        """
        pass

    def GetNestedTypes(self, bindingAttr=None):
        """
        GetNestedTypes(self: Type, bindingAttr: BindingFlags) -> Array[Type]
        GetNestedTypes(self: Type) -> Array[Type]
        """
        pass

    def GetProperties(self, bindingAttr=None):
        """
        GetProperties(self: Type) -> Array[PropertyInfo]
        GetProperties(self: Type, bindingAttr: BindingFlags) -> Array[PropertyInfo]
        """
        pass

    def GetProperty(self, name, *__args):
        """
        GetProperty(self: Type, name: str, types: Array[Type]) -> PropertyInfo
        GetProperty(self: Type, name: str, returnType: Type) -> PropertyInfo
        GetProperty(self: Type, name: str) -> PropertyInfo
        GetProperty(self: Type, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo
        GetProperty(self: Type, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo
        GetProperty(self: Type, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo
        GetProperty(self: Type, name: str, bindingAttr: BindingFlags) -> PropertyInfo
        """
        pass

    def GetPropertyImpl(self, *args): #cannot find CLR method
        """ GetPropertyImpl(self: Type, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo """
        pass

    def GetType(self, typeName=None, *__args):
        """
        GetType(typeName: str, assemblyResolver: Func[AssemblyName, Assembly], typeResolver: Func[Assembly, str, bool, Type], throwOnError: bool) -> Type
        GetType(typeName: str, assemblyResolver: Func[AssemblyName, Assembly], typeResolver: Func[Assembly, str, bool, Type], throwOnError: bool, ignoreCase: bool) -> Type
        GetType(self: Type) -> Type
        GetType(typeName: str, assemblyResolver: Func[AssemblyName, Assembly], typeResolver: Func[Assembly, str, bool, Type]) -> Type
        GetType(typeName: str, throwOnError: bool, ignoreCase: bool) -> Type
        GetType(typeName: str, throwOnError: bool) -> Type
        GetType(typeName: str) -> Type
        """
        pass

    @staticmethod
    def GetTypeArray(args):
        """ GetTypeArray(args: Array[object]) -> Array[Type] """
        pass

    @staticmethod
    def GetTypeCode(type):
        """ GetTypeCode(type: Type) -> TypeCode """
        pass

    def GetTypeCodeImpl(self, *args): #cannot find CLR method
        """ GetTypeCodeImpl(self: Type) -> TypeCode """
        pass

    @staticmethod
    def GetTypeFromCLSID(clsid, *__args):
        """
        GetTypeFromCLSID(clsid: Guid, server: str) -> Type
        GetTypeFromCLSID(clsid: Guid, server: str, throwOnError: bool) -> Type
        GetTypeFromCLSID(clsid: Guid) -> Type
        GetTypeFromCLSID(clsid: Guid, throwOnError: bool) -> Type
        """
        pass

    @staticmethod
    def GetTypeFromHandle(handle):
        """ GetTypeFromHandle(handle: RuntimeTypeHandle) -> Type """
        pass

    @staticmethod
    def GetTypeFromProgID(progID, *__args):
        """
        GetTypeFromProgID(progID: str, server: str) -> Type
        GetTypeFromProgID(progID: str, server: str, throwOnError: bool) -> Type
        GetTypeFromProgID(progID: str) -> Type
        GetTypeFromProgID(progID: str, throwOnError: bool) -> Type
        """
        pass

    @staticmethod
    def GetTypeHandle(o):
        """ GetTypeHandle(o: object) -> RuntimeTypeHandle """
        pass

    def HasElementTypeImpl(self, *args): #cannot find CLR method
        """ HasElementTypeImpl(self: Type) -> bool """
        pass

    def InvokeMember(self, name, invokeAttr, binder, target, args, *__args):
        """
        InvokeMember(self: Type, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object]) -> object
        InvokeMember(self: Type, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object], culture: CultureInfo) -> object
        InvokeMember(self: Type, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object], modifiers: Array[ParameterModifier], culture: CultureInfo, namedParameters: Array[str]) -> object
        """
        pass

    def IsArrayImpl(self, *args): #cannot find CLR method
        """ IsArrayImpl(self: Type) -> bool """
        pass

    def IsAssignableFrom(self, c):
        """ IsAssignableFrom(self: Type, c: Type) -> bool """
        pass

    def IsByRefImpl(self, *args): #cannot find CLR method
        """ IsByRefImpl(self: Type) -> bool """
        pass

    def IsCOMObjectImpl(self, *args): #cannot find CLR method
        """ IsCOMObjectImpl(self: Type) -> bool """
        pass

    def IsContextfulImpl(self, *args): #cannot find CLR method
        """ IsContextfulImpl(self: Type) -> bool """
        pass

    def IsEnumDefined(self, value):
        """ IsEnumDefined(self: Type, value: object) -> bool """
        pass

    def IsEquivalentTo(self, other):
        """ IsEquivalentTo(self: Type, other: Type) -> bool """
        pass

    def IsInstanceOfType(self, o):
        """ IsInstanceOfType(self: Type, o: object) -> bool """
        pass

    def IsMarshalByRefImpl(self, *args): #cannot find CLR method
        """ IsMarshalByRefImpl(self: Type) -> bool """
        pass

    def IsPointerImpl(self, *args): #cannot find CLR method
        """ IsPointerImpl(self: Type) -> bool """
        pass

    def IsPrimitiveImpl(self, *args): #cannot find CLR method
        """ IsPrimitiveImpl(self: Type) -> bool """
        pass

    def IsSubclassOf(self, c):
        """ IsSubclassOf(self: Type, c: Type) -> bool """
        pass

    def IsValueTypeImpl(self, *args): #cannot find CLR method
        """ IsValueTypeImpl(self: Type) -> bool """
        pass

    def MakeArrayType(self, rank=None):
        """
        MakeArrayType(self: Type, rank: int) -> Type
        MakeArrayType(self: Type) -> Type
        """
        pass

    def MakeByRefType(self):
        """ MakeByRefType(self: Type) -> Type """
        pass

    def MakeGenericType(self, typeArguments):
        """ MakeGenericType(self: Type, *typeArguments: Array[Type]) -> Type """
        pass

    def MakePointerType(self):
        """ MakePointerType(self: Type) -> Type """
        pass

    @staticmethod
    def ReflectionOnlyGetType(typeName, throwIfNotFound, ignoreCase):
        """ ReflectionOnlyGetType(typeName: str, throwIfNotFound: bool, ignoreCase: bool) -> Type """
        pass

    def ToString(self):
        """ ToString(self: Type) -> str """
        pass

    Assembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Assembly(self: Type) -> Assembly

"""

    AssemblyQualifiedName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyQualifiedName(self: Type) -> str

"""

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: Type) -> TypeAttributes

"""

    BaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseType(self: Type) -> Type

"""

    ContainsGenericParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContainsGenericParameters(self: Type) -> bool

"""

    DeclaringMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaringMethod(self: Type) -> MethodBase

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaringType(self: Type) -> Type

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: Type) -> str

"""

    GenericParameterAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GenericParameterAttributes(self: Type) -> GenericParameterAttributes

"""

    GenericParameterPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GenericParameterPosition(self: Type) -> int

"""

    GenericTypeArguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GenericTypeArguments(self: Type) -> Array[Type]

"""

    GUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GUID(self: Type) -> Guid

"""

    HasElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasElementType(self: Type) -> bool

"""

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAbstract(self: Type) -> bool

"""

    IsAnsiClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAnsiClass(self: Type) -> bool

"""

    IsArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsArray(self: Type) -> bool

"""

    IsAutoClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAutoClass(self: Type) -> bool

"""

    IsAutoLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAutoLayout(self: Type) -> bool

"""

    IsByRef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsByRef(self: Type) -> bool

"""

    IsClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClass(self: Type) -> bool

"""

    IsCOMObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCOMObject(self: Type) -> bool

"""

    IsConstructedGenericType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConstructedGenericType(self: Type) -> bool

"""

    IsContextful = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsContextful(self: Type) -> bool

"""

    IsEnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnum(self: Type) -> bool

"""

    IsExplicitLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsExplicitLayout(self: Type) -> bool

"""

    IsGenericParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGenericParameter(self: Type) -> bool

"""

    IsGenericType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGenericType(self: Type) -> bool

"""

    IsGenericTypeDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGenericTypeDefinition(self: Type) -> bool

"""

    IsImport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsImport(self: Type) -> bool

"""

    IsInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInterface(self: Type) -> bool

"""

    IsLayoutSequential = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLayoutSequential(self: Type) -> bool

"""

    IsMarshalByRef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMarshalByRef(self: Type) -> bool

"""

    IsNested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNested(self: Type) -> bool

"""

    IsNestedAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNestedAssembly(self: Type) -> bool

"""

    IsNestedFamANDAssem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNestedFamANDAssem(self: Type) -> bool

"""

    IsNestedFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNestedFamily(self: Type) -> bool

"""

    IsNestedFamORAssem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNestedFamORAssem(self: Type) -> bool

"""

    IsNestedPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNestedPrivate(self: Type) -> bool

"""

    IsNestedPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNestedPublic(self: Type) -> bool

"""

    IsNotPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNotPublic(self: Type) -> bool

"""

    IsPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPointer(self: Type) -> bool

"""

    IsPrimitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrimitive(self: Type) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: Type) -> bool

"""

    IsSealed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSealed(self: Type) -> bool

"""

    IsSecurityCritical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSecurityCritical(self: Type) -> bool

"""

    IsSecuritySafeCritical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSecuritySafeCritical(self: Type) -> bool

"""

    IsSecurityTransparent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSecurityTransparent(self: Type) -> bool

"""

    IsSerializable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSerializable(self: Type) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpecialName(self: Type) -> bool

"""

    IsUnicodeClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUnicodeClass(self: Type) -> bool

"""

    IsValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValueType(self: Type) -> bool

"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVisible(self: Type) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: Type) -> MemberTypes

"""

    Module = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Module(self: Type) -> Module

"""

    Namespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Namespace(self: Type) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReflectedType(self: Type) -> Type

"""

    StructLayoutAttribute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructLayoutAttribute(self: Type) -> StructLayoutAttribute

"""

    TypeHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeHandle(self: Type) -> RuntimeTypeHandle

"""

    TypeInitializer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeInitializer(self: Type) -> ConstructorInfo

"""

    UnderlyingSystemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnderlyingSystemType(self: Type) -> Type

"""


    DefaultBinder = None
    Delimiter = None
    EmptyTypes = None
    Missing = None


class TypeAccessException(TypeLoadException):
    """
    TypeAccessException()
    TypeAccessException(message: str)
    TypeAccessException(message: str, inner: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class TypeCode(Enum):
    """ enum TypeCode, values: Boolean (3), Byte (6), Char (4), DateTime (16), DBNull (2), Decimal (15), Double (14), Empty (0), Int16 (7), Int32 (9), Int64 (11), Object (1), SByte (5), Single (13), String (18), UInt16 (8), UInt32 (10), UInt64 (12) """
    Boolean = None
    Byte = None
    Char = None
    DateTime = None
    DBNull = None
    Decimal = None
    Double = None
    Empty = None
    Int16 = None
    Int32 = None
    Int64 = None
    Object = None
    SByte = None
    Single = None
    String = None
    UInt16 = None
    UInt32 = None
    UInt64 = None
    value__ = None


class TypedReference(object):
    # no doc
    def Equals(self, o):
        """ Equals(self: TypedReference, o: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: TypedReference) -> int """
        pass

    @staticmethod
    def GetTargetType(value):
        """ GetTargetType(value: TypedReference) -> Type """
        pass

    @staticmethod
    def MakeTypedReference(target, flds):
        """ MakeTypedReference(target: object, flds: Array[FieldInfo]) -> TypedReference """
        pass

    @staticmethod
    def SetTypedReference(target, value):
        """ SetTypedReference(target: TypedReference, value: object) """
        pass

    @staticmethod
    def TargetTypeToken(value):
        """ TargetTypeToken(value: TypedReference) -> RuntimeTypeHandle """
        pass

    @staticmethod
    def ToObject(value):
        """ ToObject(value: TypedReference) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass


class TypeInitializationException(SystemException):
    """ TypeInitializationException(fullTypeName: str, innerException: Exception) """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: TypeInitializationException, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fullTypeName, innerException):
        """ __new__(cls: type, fullTypeName: str, innerException: Exception) """
        pass

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: TypeInitializationException) -> str

"""



class TypeUnloadedException(SystemException):
    """
    TypeUnloadedException()
    TypeUnloadedException(message: str)
    TypeUnloadedException(message: str, innerException: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class UInt16(object):
    # no doc
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: UInt16) -> int """
        pass

    def CompareTo(self, value):
        """
        CompareTo(self: UInt16, value: UInt16) -> int
        CompareTo(self: UInt16, value: object) -> int
        """
        pass

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: UInt16) -> UInt16 """
        pass

    def Equals(self, obj):
        """
        Equals(self: UInt16, obj: UInt16) -> bool
        Equals(self: UInt16, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: UInt16) -> int """
        pass

    def GetTypeCode(self):
        """ GetTypeCode(self: UInt16) -> TypeCode """
        pass

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str, provider: IFormatProvider) -> UInt16
        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> UInt16
        Parse(s: str) -> UInt16
        Parse(s: str, style: NumberStyles) -> UInt16
        """
        pass

    def ToString(self, *__args):
        """
        ToString(self: UInt16, format: str) -> str
        ToString(self: UInt16, format: str, provider: IFormatProvider) -> str
        ToString(self: UInt16) -> str
        ToString(self: UInt16, provider: IFormatProvider) -> str
        """
        pass

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, UInt16)
        TryParse(s: str) -> (bool, UInt16)
        """
        pass

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __and__(self, *args): #cannot find CLR method
        """
        __and__(x: UInt16, y: Int16) -> int
        __and__(x: UInt16, y: UInt16) -> UInt16
        """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        pass

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: UInt16) -> float """
        pass

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//yx.__floordiv__(y) <==> x//y """
        pass

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(value: UInt16) -> str """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: UInt16) -> int """
        pass

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: UInt16) -> object """
        pass

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<yx.__rshift__(y) <==> x<<y """
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%yx.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, value: object) -> object
        __new__(cls: type) -> object
        """
        pass

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: UInt16) -> bool """
        pass

    def __or__(self, *args): #cannot find CLR method
        """
        __or__(x: UInt16, y: Int16) -> int
        __or__(x: UInt16, y: UInt16) -> UInt16
        """
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: UInt16) -> UInt16 """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(x: Int16, y: UInt16) -> object
        __radd__(x: UInt16, y: UInt16) -> object
        """
        pass

    def __rand__(self, *args): #cannot find CLR method
        """
        __rand__(x: Int16, y: UInt16) -> int
        __rand__(x: UInt16, y: UInt16) -> UInt16
        """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(x: Int16, y: UInt16) -> object
        __rdiv__(x: UInt16, y: UInt16) -> object
        """
        pass

    def __rfloordiv__(self, *args): #cannot find CLR method
        """
        __rfloordiv__(x: Int16, y: UInt16) -> object
        __rfloordiv__(x: UInt16, y: UInt16) -> UInt16
        """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """
        __rmod__(x: Int16, y: UInt16) -> int
        __rmod__(x: UInt16, y: UInt16) -> UInt16
        """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(x: Int16, y: UInt16) -> object
        __rmul__(x: UInt16, y: UInt16) -> object
        """
        pass

    def __ror__(self, *args): #cannot find CLR method
        """
        __ror__(x: Int16, y: UInt16) -> int
        __ror__(x: UInt16, y: UInt16) -> UInt16
        """
        pass

    def __rpow__(self, *args): #cannot find CLR method
        """
        __rpow__(x: Int16, y: UInt16) -> object
        __rpow__(x: UInt16, y: UInt16) -> object
        """
        pass

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(x: Int16, y: UInt16) -> object
        __rsub__(x: UInt16, y: UInt16) -> object
        """
        pass

    def __rtruediv__(self, *args): #cannot find CLR method
        """
        __rtruediv__(x: Int16, y: UInt16) -> float
        __rtruediv__(x: UInt16, y: UInt16) -> float
        """
        pass

    def __rxor__(self, *args): #cannot find CLR method
        """
        __rxor__(x: Int16, y: UInt16) -> int
        __rxor__(x: UInt16, y: UInt16) -> UInt16
        """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/yx.__truediv__(y) <==> x/y """
        pass

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: UInt16) -> UInt16 """
        pass

    def __xor__(self, *args): #cannot find CLR method
        """
        __xor__(x: UInt16, y: Int16) -> int
        __xor__(x: UInt16, y: UInt16) -> UInt16
        """
        pass

    denominator = None
    imag = None
    MaxValue = None
    MinValue = None
    numerator = None
    real = None


class UInt32(object):
    # no doc
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: UInt32) -> int """
        pass

    def CompareTo(self, value):
        """
        CompareTo(self: UInt32, value: UInt32) -> int
        CompareTo(self: UInt32, value: object) -> int
        """
        pass

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: UInt32) -> UInt32 """
        pass

    def Equals(self, obj):
        """
        Equals(self: UInt32, obj: UInt32) -> bool
        Equals(self: UInt32, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: UInt32) -> int """
        pass

    def GetTypeCode(self):
        """ GetTypeCode(self: UInt32) -> TypeCode """
        pass

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str, provider: IFormatProvider) -> UInt32
        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> UInt32
        Parse(s: str) -> UInt32
        Parse(s: str, style: NumberStyles) -> UInt32
        """
        pass

    def ToString(self, *__args):
        """
        ToString(self: UInt32, format: str) -> str
        ToString(self: UInt32, format: str, provider: IFormatProvider) -> str
        ToString(self: UInt32) -> str
        ToString(self: UInt32, provider: IFormatProvider) -> str
        """
        pass

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, UInt32)
        TryParse(s: str) -> (bool, UInt32)
        """
        pass

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __and__(self, *args): #cannot find CLR method
        """
        __and__(x: UInt32, y: int) -> Int64
        __and__(x: UInt32, y: UInt32) -> UInt32
        """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        pass

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: UInt32) -> float """
        pass

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//yx.__floordiv__(y) <==> x//y """
        pass

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(value: UInt32) -> str """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: UInt32) -> int """
        pass

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: UInt32) -> object """
        pass

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<y """
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%yx.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, value: object) -> object
        __new__(cls: type) -> object
        """
        pass

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: UInt32) -> bool """
        pass

    def __or__(self, *args): #cannot find CLR method
        """
        __or__(x: UInt32, y: int) -> Int64
        __or__(x: UInt32, y: UInt32) -> UInt32
        """
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: UInt32) -> UInt32 """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(x: int, y: UInt32) -> object
        __radd__(x: UInt32, y: UInt32) -> object
        """
        pass

    def __rand__(self, *args): #cannot find CLR method
        """
        __rand__(x: int, y: UInt32) -> Int64
        __rand__(x: UInt32, y: UInt32) -> UInt32
        """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(x: int, y: UInt32) -> object
        __rdiv__(x: UInt32, y: UInt32) -> object
        """
        pass

    def __rfloordiv__(self, *args): #cannot find CLR method
        """
        __rfloordiv__(x: int, y: UInt32) -> object
        __rfloordiv__(x: UInt32, y: UInt32) -> UInt32
        """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """
        __rmod__(x: int, y: UInt32) -> Int64
        __rmod__(x: UInt32, y: UInt32) -> UInt32
        """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(x: int, y: UInt32) -> object
        __rmul__(x: UInt32, y: UInt32) -> object
        """
        pass

    def __ror__(self, *args): #cannot find CLR method
        """
        __ror__(x: int, y: UInt32) -> Int64
        __ror__(x: UInt32, y: UInt32) -> UInt32
        """
        pass

    def __rpow__(self, *args): #cannot find CLR method
        """
        __rpow__(x: int, y: UInt32) -> object
        __rpow__(x: UInt32, y: UInt32) -> object
        """
        pass

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(x: int, y: UInt32) -> object
        __rsub__(x: UInt32, y: UInt32) -> object
        """
        pass

    def __rtruediv__(self, *args): #cannot find CLR method
        """
        __rtruediv__(x: int, y: UInt32) -> float
        __rtruediv__(x: UInt32, y: UInt32) -> float
        """
        pass

    def __rxor__(self, *args): #cannot find CLR method
        """
        __rxor__(x: int, y: UInt32) -> Int64
        __rxor__(x: UInt32, y: UInt32) -> UInt32
        """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/yx.__truediv__(y) <==> x/y """
        pass

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: UInt32) -> UInt32 """
        pass

    def __xor__(self, *args): #cannot find CLR method
        """
        __xor__(x: UInt32, y: int) -> Int64
        __xor__(x: UInt32, y: UInt32) -> UInt32
        """
        pass

    denominator = None
    imag = None
    MaxValue = None
    MinValue = None
    numerator = None
    real = None


class UInt64(object):
    # no doc
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: UInt64) -> int """
        pass

    def CompareTo(self, value):
        """
        CompareTo(self: UInt64, value: UInt64) -> int
        CompareTo(self: UInt64, value: object) -> int
        """
        pass

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: UInt64) -> UInt64 """
        pass

    def Equals(self, obj):
        """
        Equals(self: UInt64, obj: UInt64) -> bool
        Equals(self: UInt64, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: UInt64) -> int """
        pass

    def GetTypeCode(self):
        """ GetTypeCode(self: UInt64) -> TypeCode """
        pass

    @staticmethod
    def Parse(s, *__args):
        """
        Parse(s: str, provider: IFormatProvider) -> UInt64
        Parse(s: str, style: NumberStyles, provider: IFormatProvider) -> UInt64
        Parse(s: str) -> UInt64
        Parse(s: str, style: NumberStyles) -> UInt64
        """
        pass

    def ToString(self, *__args):
        """
        ToString(self: UInt64, format: str) -> str
        ToString(self: UInt64, format: str, provider: IFormatProvider) -> str
        ToString(self: UInt64) -> str
        ToString(self: UInt64, provider: IFormatProvider) -> str
        """
        pass

    @staticmethod
    def TryParse(s, *__args):
        """
        TryParse(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, UInt64)
        TryParse(s: str) -> (bool, UInt64)
        """
        pass

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __and__(self, *args): #cannot find CLR method
        """
        __and__(x: UInt64, y: Int64) -> long
        __and__(x: UInt64, y: UInt64) -> UInt64
        """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        pass

    def __float__(self, *args): #cannot find CLR method
        """ __float__(x: UInt64) -> float """
        pass

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//yx.__floordiv__(y) <==> x//y """
        pass

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(value: UInt64) -> str """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: UInt64) -> int """
        pass

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: UInt64) -> object """
        pass

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<y """
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%yx.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, value: object) -> object
        __new__(cls: type) -> object
        """
        pass

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: UInt64) -> bool """
        pass

    def __or__(self, *args): #cannot find CLR method
        """
        __or__(x: UInt64, y: Int64) -> long
        __or__(x: UInt64, y: UInt64) -> UInt64
        """
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: UInt64) -> UInt64 """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(x: Int64, y: UInt64) -> object
        __radd__(x: UInt64, y: UInt64) -> object
        """
        pass

    def __rand__(self, *args): #cannot find CLR method
        """
        __rand__(x: Int64, y: UInt64) -> long
        __rand__(x: UInt64, y: UInt64) -> UInt64
        """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(x: Int64, y: UInt64) -> object
        __rdiv__(x: UInt64, y: UInt64) -> object
        """
        pass

    def __rfloordiv__(self, *args): #cannot find CLR method
        """
        __rfloordiv__(x: Int64, y: UInt64) -> object
        __rfloordiv__(x: UInt64, y: UInt64) -> UInt64
        """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """
        __rmod__(x: Int64, y: UInt64) -> long
        __rmod__(x: UInt64, y: UInt64) -> UInt64
        """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(x: Int64, y: UInt64) -> object
        __rmul__(x: UInt64, y: UInt64) -> object
        """
        pass

    def __ror__(self, *args): #cannot find CLR method
        """
        __ror__(x: Int64, y: UInt64) -> long
        __ror__(x: UInt64, y: UInt64) -> UInt64
        """
        pass

    def __rpow__(self, *args): #cannot find CLR method
        """
        __rpow__(x: Int64, y: UInt64) -> object
        __rpow__(x: UInt64, y: UInt64) -> object
        """
        pass

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(x: Int64, y: UInt64) -> object
        __rsub__(x: UInt64, y: UInt64) -> object
        """
        pass

    def __rtruediv__(self, *args): #cannot find CLR method
        """
        __rtruediv__(x: Int64, y: UInt64) -> float
        __rtruediv__(x: UInt64, y: UInt64) -> float
        """
        pass

    def __rxor__(self, *args): #cannot find CLR method
        """
        __rxor__(x: Int64, y: UInt64) -> long
        __rxor__(x: UInt64, y: UInt64) -> UInt64
        """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/yx.__truediv__(y) <==> x/y """
        pass

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: UInt64) -> UInt64 """
        pass

    def __xor__(self, *args): #cannot find CLR method
        """
        __xor__(x: UInt64, y: Int64) -> long
        __xor__(x: UInt64, y: UInt64) -> UInt64
        """
        pass

    denominator = None
    imag = None
    MaxValue = None
    MinValue = None
    numerator = None
    real = None


class UIntPtr(object):
    """
    UIntPtr(value: UInt32)
    UIntPtr(value: UInt64)
    UIntPtr(value: Void*)
    """
    @staticmethod
    def Add(pointer, offset):
        """ Add(pointer: UIntPtr, offset: int) -> UIntPtr """
        pass

    def Equals(self, obj):
        """ Equals(self: UIntPtr, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: UIntPtr) -> int """
        pass

    @staticmethod
    def Subtract(pointer, offset):
        """ Subtract(pointer: UIntPtr, offset: int) -> UIntPtr """
        pass

    def ToPointer(self):
        """ ToPointer(self: UIntPtr) -> Void* """
        pass

    def ToString(self):
        """ ToString(self: UIntPtr) -> str """
        pass

    def ToUInt32(self):
        """ ToUInt32(self: UIntPtr) -> UInt32 """
        pass

    def ToUInt64(self):
        """ ToUInt64(self: UIntPtr) -> UInt64 """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value):
        """
        __new__[UIntPtr]() -> UIntPtr
        
        __new__(cls: type, value: UInt32)
        __new__(cls: type, value: UInt64)
        __new__(cls: type, value: Void*)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    Size = 8
    Zero = None


class UnauthorizedAccessException(SystemException):
    """
    UnauthorizedAccessException()
    UnauthorizedAccessException(message: str)
    UnauthorizedAccessException(message: str, inner: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass


class UnhandledExceptionEventArgs(EventArgs):
    """ UnhandledExceptionEventArgs(exception: object, isTerminating: bool) """
    @staticmethod # known case of __new__
    def __new__(self, exception, isTerminating):
        """ __new__(cls: type, exception: object, isTerminating: bool) """
        pass

    ExceptionObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExceptionObject(self: UnhandledExceptionEventArgs) -> object

"""

    IsTerminating = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTerminating(self: UnhandledExceptionEventArgs) -> bool

"""



class UnhandledExceptionEventHandler(MulticastDelegate):
    """ UnhandledExceptionEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: UnhandledExceptionEventHandler, sender: object, e: UnhandledExceptionEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: UnhandledExceptionEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: UnhandledExceptionEventHandler, sender: object, e: UnhandledExceptionEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class Uri(object):
    """
    Uri(uriString: str)
    Uri(uriString: str, dontEscape: bool)
    Uri(baseUri: Uri, relativeUri: str, dontEscape: bool)
    Uri(uriString: str, uriKind: UriKind)
    Uri(baseUri: Uri, relativeUri: str)
    Uri(baseUri: Uri, relativeUri: Uri)
    """
    def Canonicalize(self, *args): #cannot find CLR method
        """ Canonicalize(self: Uri) """
        pass

    @staticmethod
    def CheckHostName(name):
        """ CheckHostName(name: str) -> UriHostNameType """
        pass

    @staticmethod
    def CheckSchemeName(schemeName):
        """ CheckSchemeName(schemeName: str) -> bool """
        pass

    def CheckSecurity(self, *args): #cannot find CLR method
        """ CheckSecurity(self: Uri) """
        pass

    @staticmethod
    def Compare(uri1, uri2, partsToCompare, compareFormat, comparisonType):
        """ Compare(uri1: Uri, uri2: Uri, partsToCompare: UriComponents, compareFormat: UriFormat, comparisonType: StringComparison) -> int """
        pass

    def Equals(self, comparand):
        """ Equals(self: Uri, comparand: object) -> bool """
        pass

    def Escape(self, *args): #cannot find CLR method
        """ Escape(self: Uri) """
        pass

    @staticmethod
    def EscapeDataString(stringToEscape):
        """ EscapeDataString(stringToEscape: str) -> str """
        pass

    def EscapeString(self, *args): #cannot find CLR method
        """ EscapeString(str: str) -> str """
        pass

    @staticmethod
    def EscapeUriString(stringToEscape):
        """ EscapeUriString(stringToEscape: str) -> str """
        pass

    @staticmethod
    def FromHex(digit):
        """ FromHex(digit: Char) -> int """
        pass

    def GetComponents(self, components, format):
        """ GetComponents(self: Uri, components: UriComponents, format: UriFormat) -> str """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Uri) -> int """
        pass

    def GetLeftPart(self, part):
        """ GetLeftPart(self: Uri, part: UriPartial) -> str """
        pass

    def GetObjectData(self, *args): #cannot find CLR method
        """ GetObjectData(self: Uri, serializationInfo: SerializationInfo, streamingContext: StreamingContext) """
        pass

    @staticmethod
    def HexEscape(character):
        """ HexEscape(character: Char) -> str """
        pass

    @staticmethod
    def HexUnescape(pattern, index):
        """ HexUnescape(pattern: str, index: int) -> (Char, int) """
        pass

    def IsBadFileSystemCharacter(self, *args): #cannot find CLR method
        """ IsBadFileSystemCharacter(self: Uri, character: Char) -> bool """
        pass

    def IsBaseOf(self, uri):
        """ IsBaseOf(self: Uri, uri: Uri) -> bool """
        pass

    def IsExcludedCharacter(self, *args): #cannot find CLR method
        """ IsExcludedCharacter(character: Char) -> bool """
        pass

    @staticmethod
    def IsHexDigit(character):
        """ IsHexDigit(character: Char) -> bool """
        pass

    @staticmethod
    def IsHexEncoding(pattern, index):
        """ IsHexEncoding(pattern: str, index: int) -> bool """
        pass

    def IsReservedCharacter(self, *args): #cannot find CLR method
        """ IsReservedCharacter(self: Uri, character: Char) -> bool """
        pass

    def IsWellFormedOriginalString(self):
        """ IsWellFormedOriginalString(self: Uri) -> bool """
        pass

    @staticmethod
    def IsWellFormedUriString(uriString, uriKind):
        """ IsWellFormedUriString(uriString: str, uriKind: UriKind) -> bool """
        pass

    def MakeRelative(self, toUri):
        """ MakeRelative(self: Uri, toUri: Uri) -> str """
        pass

    def MakeRelativeUri(self, uri):
        """ MakeRelativeUri(self: Uri, uri: Uri) -> Uri """
        pass

    def Parse(self, *args): #cannot find CLR method
        """ Parse(self: Uri) """
        pass

    def ToString(self):
        """ ToString(self: Uri) -> str """
        pass

    @staticmethod
    def TryCreate(*__args):
        """
        TryCreate(baseUri: Uri, relativeUri: Uri) -> (bool, Uri)
        TryCreate(baseUri: Uri, relativeUri: str) -> (bool, Uri)
        TryCreate(uriString: str, uriKind: UriKind) -> (bool, Uri)
        """
        pass

    def Unescape(self, *args): #cannot find CLR method
        """ Unescape(self: Uri, path: str) -> str """
        pass

    @staticmethod
    def UnescapeDataString(stringToUnescape):
        """ UnescapeDataString(stringToUnescape: str) -> str """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, uriString: str)
        __new__(cls: type, uriString: str, dontEscape: bool)
        __new__(cls: type, baseUri: Uri, relativeUri: str, dontEscape: bool)
        __new__(cls: type, uriString: str, uriKind: UriKind)
        __new__(cls: type, baseUri: Uri, relativeUri: str)
        __new__(cls: type, baseUri: Uri, relativeUri: Uri)
        __new__(cls: type, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    AbsolutePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AbsolutePath(self: Uri) -> str

"""

    AbsoluteUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AbsoluteUri(self: Uri) -> str

"""

    Authority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Authority(self: Uri) -> str

"""

    DnsSafeHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DnsSafeHost(self: Uri) -> str

"""

    Fragment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fragment(self: Uri) -> str

"""

    Host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Host(self: Uri) -> str

"""

    HostNameType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HostNameType(self: Uri) -> UriHostNameType

"""

    IdnHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdnHost(self: Uri) -> str

"""

    IsAbsoluteUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAbsoluteUri(self: Uri) -> bool

"""

    IsDefaultPort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDefaultPort(self: Uri) -> bool

"""

    IsFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFile(self: Uri) -> bool

"""

    IsLoopback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLoopback(self: Uri) -> bool

"""

    IsUnc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUnc(self: Uri) -> bool

"""

    LocalPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalPath(self: Uri) -> str

"""

    OriginalString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalString(self: Uri) -> str

"""

    PathAndQuery = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PathAndQuery(self: Uri) -> str

"""

    Port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Port(self: Uri) -> int

"""

    Query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Query(self: Uri) -> str

"""

    Scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scheme(self: Uri) -> str

"""

    Segments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Segments(self: Uri) -> Array[str]

"""

    UserEscaped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserEscaped(self: Uri) -> bool

"""

    UserInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserInfo(self: Uri) -> str

"""


    SchemeDelimiter = '://'
    UriSchemeFile = 'file'
    UriSchemeFtp = 'ftp'
    UriSchemeGopher = 'gopher'
    UriSchemeHttp = 'http'
    UriSchemeHttps = 'https'
    UriSchemeMailto = 'mailto'
    UriSchemeNetPipe = 'net.pipe'
    UriSchemeNetTcp = 'net.tcp'
    UriSchemeNews = 'news'
    UriSchemeNntp = 'nntp'


class UriBuilder(object):
    """
    UriBuilder()
    UriBuilder(uri: str)
    UriBuilder(uri: Uri)
    UriBuilder(schemeName: str, hostName: str)
    UriBuilder(scheme: str, host: str, portNumber: int)
    UriBuilder(scheme: str, host: str, port: int, pathValue: str)
    UriBuilder(scheme: str, host: str, port: int, path: str, extraValue: str)
    """
    def Equals(self, rparam):
        """ Equals(self: UriBuilder, rparam: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: UriBuilder) -> int """
        pass

    def ToString(self):
        """ ToString(self: UriBuilder) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, uri: str)
        __new__(cls: type, uri: Uri)
        __new__(cls: type, schemeName: str, hostName: str)
        __new__(cls: type, scheme: str, host: str, portNumber: int)
        __new__(cls: type, scheme: str, host: str, port: int, pathValue: str)
        __new__(cls: type, scheme: str, host: str, port: int, path: str, extraValue: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Fragment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fragment(self: UriBuilder) -> str

Set: Fragment(self: UriBuilder) = value
"""

    Host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Host(self: UriBuilder) -> str

Set: Host(self: UriBuilder) = value
"""

    Password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Password(self: UriBuilder) -> str

Set: Password(self: UriBuilder) = value
"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: UriBuilder) -> str

Set: Path(self: UriBuilder) = value
"""

    Port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Port(self: UriBuilder) -> int

Set: Port(self: UriBuilder) = value
"""

    Query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Query(self: UriBuilder) -> str

Set: Query(self: UriBuilder) = value
"""

    Scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scheme(self: UriBuilder) -> str

Set: Scheme(self: UriBuilder) = value
"""

    Uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Uri(self: UriBuilder) -> Uri

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: UriBuilder) -> str

Set: UserName(self: UriBuilder) = value
"""



class UriComponents(Enum):
    """ enum (flags) UriComponents, values: AbsoluteUri (127), Fragment (64), Host (4), HostAndPort (132), HttpRequestUrl (61), KeepDelimiter (1073741824), NormalizedHost (256), Path (16), PathAndQuery (48), Port (8), Query (32), Scheme (1), SchemeAndServer (13), SerializationInfoString (-2147483648), StrongAuthority (134), StrongPort (128), UserInfo (2) """
    AbsoluteUri = None
    Fragment = None
    Host = None
    HostAndPort = None
    HttpRequestUrl = None
    KeepDelimiter = None
    NormalizedHost = None
    Path = None
    PathAndQuery = None
    Port = None
    Query = None
    Scheme = None
    SchemeAndServer = None
    SerializationInfoString = None
    StrongAuthority = None
    StrongPort = None
    UserInfo = None
    value__ = None


class UriFormat(Enum):
    """ enum UriFormat, values: SafeUnescaped (3), Unescaped (2), UriEscaped (1) """
    SafeUnescaped = None
    Unescaped = None
    UriEscaped = None
    value__ = None


class UriFormatException(FormatException):
    """
    UriFormatException()
    UriFormatException(textString: str)
    UriFormatException(textString: str, e: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, textString=None, e=None):
        """
        __new__(cls: type)
        __new__(cls: type, textString: str)
        __new__(cls: type, textString: str, e: Exception)
        __new__(cls: type, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
        """
        pass


class UriHostNameType(Enum):
    """ enum UriHostNameType, values: Basic (1), Dns (2), IPv4 (3), IPv6 (4), Unknown (0) """
    Basic = None
    Dns = None
    IPv4 = None
    IPv6 = None
    Unknown = None
    value__ = None


class UriIdnScope(Enum):
    """ enum UriIdnScope, values: All (2), AllExceptIntranet (1), None (0) """
    All = None
    AllExceptIntranet = None
    None = None
    value__ = None


class UriKind(Enum):
    """ enum UriKind, values: Absolute (1), Relative (2), RelativeOrAbsolute (0) """
    Absolute = None
    Relative = None
    RelativeOrAbsolute = None
    value__ = None


class UriPartial(Enum):
    """ enum UriPartial, values: Authority (1), Path (2), Query (3), Scheme (0) """
    Authority = None
    Path = None
    Query = None
    Scheme = None
    value__ = None


class UriTypeConverter(TypeConverter):
    """ UriTypeConverter() """
    def CanConvertFrom(self, *__args):
        """ CanConvertFrom(self: UriTypeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool """
        pass

    def CanConvertTo(self, *__args):
        """ CanConvertTo(self: UriTypeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool """
        pass

    def ConvertFrom(self, *__args):
        """ ConvertFrom(self: UriTypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object """
        pass

    def ConvertTo(self, *__args):
        """ ConvertTo(self: UriTypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object """
        pass

    def IsValid(self, *__args):
        """ IsValid(self: UriTypeConverter, context: ITypeDescriptorContext, value: object) -> bool """
        pass


class ValueType(object):
    # no doc
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass


class Version(object):
    """
    Version(major: int, minor: int, build: int, revision: int)
    Version(major: int, minor: int, build: int)
    Version(major: int, minor: int)
    Version(version: str)
    Version()
    """
    def Clone(self):
        """ Clone(self: Version) -> object """
        pass

    def CompareTo(self, *__args):
        """
        CompareTo(self: Version, value: Version) -> int
        CompareTo(self: Version, version: object) -> int
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Version, obj: Version) -> bool
        Equals(self: Version, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Version) -> int """
        pass

    @staticmethod
    def Parse(input):
        """ Parse(input: str) -> Version """
        pass

    def ToString(self, fieldCount=None):
        """
        ToString(self: Version, fieldCount: int) -> str
        ToString(self: Version) -> str
        """
        pass

    @staticmethod
    def TryParse(input, result):
        """ TryParse(input: str) -> (bool, Version) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, major: int, minor: int, build: int, revision: int)
        __new__(cls: type, major: int, minor: int, build: int)
        __new__(cls: type, major: int, minor: int)
        __new__(cls: type, version: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Build = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Build(self: Version) -> int

"""

    Major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Major(self: Version) -> int

"""

    MajorRevision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorRevision(self: Version) -> Int16

"""

    Minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Minor(self: Version) -> int

"""

    MinorRevision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorRevision(self: Version) -> Int16

"""

    Revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Revision(self: Version) -> int

"""



class Void(object):
    # no doc

# variables with complex values

