class _AppDomain:
 """ Exposes the public members of the System.AppDomain class to unmanaged code. """
 def AppendPrivatePath(self,path):
  """
  AppendPrivatePath(self: _AppDomain,path: str)

   Provides COM objects with version-independent access to the 

    System.AppDomain.AppendPrivatePath(System.String) method.

  

  

   path: The name of the directory to be appended to the private path.
  """
  pass
 def ClearPrivatePath(self):
  """
  ClearPrivatePath(self: _AppDomain)

   Provides COM objects with version-independent access to the System.AppDomain.ClearPrivatePath 

    method.
  """
  pass
 def ClearShadowCopyPath(self):
  """
  ClearShadowCopyPath(self: _AppDomain)

   Provides COM objects with version-independent access to the System.AppDomain.ClearShadowCopyPath 

    method.
  """
  pass
 def CreateInstance(self,assemblyName,typeName,*__args):
  """
  CreateInstance(self: _AppDomain,assemblyName: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object],securityAttributes: Evidence) -> ObjectHandle

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.CreateInstance(System.String,System.String,System.Boolean,System.Reflection.Bind

    ingFlags,System.Reflection.Binder,System.Object[],System.Globalization.CultureInfo,System.Object[

    ],System.Security.Policy.Evidence) method overload.

  

  

   assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

   typeName: The fully qualified name of the requested type,including the namespace but not the assembly,as 

    returned by the System.Type.FullName property.

  

   ignoreCase: A Boolean value specifying whether to perform a case-sensitive search or not.

   bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If 

    bindingAttr is zero,a case-sensitive search for public constructors is conducted.

  

   binder: An object that enables the binding,coercion of argument types,invocation of members,and 

    retrieval of System.Reflection.MemberInfo objects using reflection. If binder is null,the 

    default binder is used.

  

   args: The arguments to pass to the constructor. This array of arguments must match in number,order,

    and type the parameters of the constructor to invoke. If the default constructor is preferred,

    args must be an empty array or null.

  

   culture: Culture-specific information that governs the coercion of args to the formal types declared for 

    the typeName constructor. If culture is null,the System.Globalization.CultureInfo for the 

    current thread is used.

  

   activationAttributes: An array of one or more attributes that can participate in activation. Typically,an array that 

    contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   securityAttributes: Information used to authorize creation of typeName.

   Returns: An object that is a wrapper for the new instance specified by typeName. The return value needs 

    to be unwrapped to access the real object.

  

  CreateInstance(self: _AppDomain,assemblyName: str,typeName: str,activationAttributes: Array[object]) -> ObjectHandle

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.CreateInstance(System.String,System.String,System.Object[]) method overload.

  

  

   assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

   typeName: The fully qualified name of the requested type,including the namespace but not the assembly,as 

    returned by the System.Type.FullName property.

  

   activationAttributes: An array of one or more attributes that can participate in activation. Typically,an array that 

    contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   Returns: An object that is a wrapper for the new instance specified by typeName. The return value needs 

    to be unwrapped to access the real object.

  

  CreateInstance(self: _AppDomain,assemblyName: str,typeName: str) -> ObjectHandle

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.CreateInstance(System.String,System.String) method.

  

  

   assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

   typeName: The fully qualified name of the requested type,including the namespace but not the assembly,as 

    returned by the System.Type.FullName property.

  

   Returns: An object that is a wrapper for the new instance specified by typeName. The return value needs 

    to be unwrapped to access the real object.
  """
  pass
 def CreateInstanceFrom(self,assemblyFile,typeName,*__args):
  """
  CreateInstanceFrom(self: _AppDomain,assemblyFile: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object],securityAttributes: Evidence) -> ObjectHandle

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.CreateInstanceFrom(System.String,System.String,System.Boolean,System.Reflection.

    BindingFlags,System.Reflection.Binder,System.Object[],System.Globalization.CultureInfo,System.Obj

    ect[],System.Security.Policy.Evidence) method overload.

  

  

   assemblyFile: The name,including the path,of a file that contains an assembly that defines the requested 

    type. The assembly is loaded using the System.Reflection.Assembly.LoadFrom(System.String)  

    method.

  

   typeName: The fully qualified name of the requested type,including the namespace but not the assembly,as 

    returned by the System.Type.FullName property.

  

   ignoreCase: A Boolean value specifying whether to perform a case-sensitive search or not.

   bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If 

    bindingAttr is zero,a case-sensitive search for public constructors is conducted.

  

   binder: An object that enables the binding,coercion of argument types,invocation of members,and 

    retrieval of System.Reflection.MemberInfo objects through reflection. If binder is null,the 

    default binder is used.

  

   args: The arguments to pass to the constructor. This array of arguments must match in number,order,

    and type the parameters of the constructor to invoke. If the default constructor is preferred,

    args must be an empty array or null.

  

   culture: Culture-specific information that governs the coercion of args to the formal types declared for 

    the typeName constructor. If culture is null,the System.Globalization.CultureInfo for the 

    current thread is used.

  

   activationAttributes: An array of one or more attributes that can participate in activation. Typically,an array that 

    contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   securityAttributes: Information used to authorize creation of typeName.

   Returns: An object that is a wrapper for the new instance,or null if typeName is not found. The return 

    value needs to be unwrapped to access the real object.

  

  CreateInstanceFrom(self: _AppDomain,assemblyFile: str,typeName: str,activationAttributes: Array[object]) -> ObjectHandle

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.CreateInstanceFrom(System.String,System.String,System.Object[]) method 

    overload.

  

  

   assemblyFile: The name,including the path,of a file that contains an assembly that defines the requested 

    type. The assembly is loaded using the System.Reflection.Assembly.LoadFrom(System.String)  

    method.

  

   typeName: The fully qualified name of the requested type,including the namespace but not the assembly,as 

    returned by the System.Type.FullName property.

  

   activationAttributes: An array of one or more attributes that can participate in activation. Typically,an array that 

    contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   Returns: An object that is a wrapper for the new instance,or null if typeName is not found. The return 

    value needs to be unwrapped to access the real object.

  

  CreateInstanceFrom(self: _AppDomain,assemblyFile: str,typeName: str) -> ObjectHandle

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.CreateInstanceFrom(System.String,System.String) method overload.

  

  

   assemblyFile: The name,including the path,of a file that contains an assembly that defines the requested 

    type. The assembly is loaded using the System.Reflection.Assembly.LoadFrom(System.String)  

    method.

  

   typeName: The fully qualified name of the requested type,including the namespace but not the assembly,as 

    returned by the System.Type.FullName property.

  

   Returns: An object that is a wrapper for the new instance,or null if typeName is not found. The return 

    value needs to be unwrapped to access the real object.
  """
  pass
 def DefineDynamicAssembly(self,name,access,*__args):
  """
  DefineDynamicAssembly(self: _AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,evidence: Evidence,requiredPermissions: PermissionSet,optionalPermissions: PermissionSet,refusedPermissions: PermissionSet) -> AssemblyBuilder

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.Asse

    mblyBuilderAccess,System.Security.Policy.Evidence,System.Security.PermissionSet,System.Security.P

    ermissionSet,System.Security.PermissionSet) method overload.

  

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   evidence: The evidence supplied for the dynamic assembly. The evidence is used unaltered as the final set 

    of evidence used for policy resolution.

  

   requiredPermissions: The required permissions request.

   optionalPermissions: The optional permissions request.

   refusedPermissions: The refused permissions request.

   Returns: Represents the dynamic assembly created.

  DefineDynamicAssembly(self: _AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,dir: str,requiredPermissions: PermissionSet,optionalPermissions: PermissionSet,refusedPermissions: PermissionSet) -> AssemblyBuilder

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.Asse

    mblyBuilderAccess,System.String,System.Security.PermissionSet,System.Security.PermissionSet,Syste

    m.Security.PermissionSet) method overload.

  

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   dir: The name of the directory where the assembly will be saved. If dir is null,the directory 

    defaults to the current directory.

  

   requiredPermissions: The required permissions request.

   optionalPermissions: The optional permissions request.

   refusedPermissions: The refused permissions request.

   Returns: Represents the dynamic assembly created.

  DefineDynamicAssembly(self: _AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,dir: str,evidence: Evidence,requiredPermissions: PermissionSet,optionalPermissions: PermissionSet,refusedPermissions: PermissionSet,isSynchronized: bool) -> AssemblyBuilder

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.Asse

    mblyBuilderAccess,System.String,System.Security.Policy.Evidence,System.Security.PermissionSet,Sys

    tem.Security.PermissionSet,System.Security.PermissionSet,System.Boolean) method overload.

  

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   dir: The name of the directory where the dynamic assembly will be saved. If dir is null,the 

    directory defaults to the current directory.

  

   evidence: The evidence supplied for the dynamic assembly. The evidence is used unaltered as the final set 

    of evidence used for policy resolution.

  

   requiredPermissions: The required permissions request.

   optionalPermissions: The optional permissions request.

   refusedPermissions: The refused permissions request.

   isSynchronized: true to synchronize the creation of modules,types,and members in the dynamic assembly; 

    otherwise,false.

  

   Returns: Represents the dynamic assembly created.

  DefineDynamicAssembly(self: _AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,dir: str,evidence: Evidence,requiredPermissions: PermissionSet,optionalPermissions: PermissionSet,refusedPermissions: PermissionSet) -> AssemblyBuilder

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.Asse

    mblyBuilderAccess,System.String,System.Security.Policy.Evidence,System.Security.PermissionSet,Sys

    tem.Security.PermissionSet,System.Security.PermissionSet) method overload.

  

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   dir: The name of the directory where the assembly will be saved. If dir is null,the directory 

    defaults to the current directory.

  

   evidence: The evidence supplied for the dynamic assembly. The evidence is used unaltered as the final set 

    of evidence used for policy resolution.

  

   requiredPermissions: The required permissions request.

   optionalPermissions: The optional permissions request.

   refusedPermissions: The refused permissions request.

   Returns: Represents the dynamic assembly created.

  DefineDynamicAssembly(self: _AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,dir: str,evidence: Evidence) -> AssemblyBuilder

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.Asse

    mblyBuilderAccess,System.String,System.Security.Policy.Evidence) method overload.

  

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   dir: The name of the directory where the assembly will be saved. If dir is null,the directory 

    defaults to the current directory.

  

   evidence: The evidence supplied for the dynamic assembly. The evidence is used unaltered as the final set 

    of evidence used for policy resolution.

  

   Returns: Represents the dynamic assembly created.

  DefineDynamicAssembly(self: _AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,dir: str) -> AssemblyBuilder

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.Asse

    mblyBuilderAccess,System.String) method overload.

  

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   dir: The name of the directory where the assembly will be saved. If dir is null,the directory 

    defaults to the current directory.

  

   Returns: Represents the dynamic assembly created.

  DefineDynamicAssembly(self: _AppDomain,name: AssemblyName,access: AssemblyBuilderAccess) -> AssemblyBuilder

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.Asse

    mblyBuilderAccess) method overload.

  

  

   name: The unique identity of the dynamic assembly.

   access: The access mode for the dynamic assembly.

   Returns: Represents the dynamic assembly created.

  DefineDynamicAssembly(self: _AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,requiredPermissions: PermissionSet,optionalPermissions: PermissionSet,refusedPermissions: PermissionSet) -> AssemblyBuilder

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.Asse

    mblyBuilderAccess,System.Security.PermissionSet,System.Security.PermissionSet,System.Security.Per

    missionSet) method overload.

  

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   requiredPermissions: The required permissions request.

   optionalPermissions: The optional permissions request.

   refusedPermissions: The refused permissions request.

   Returns: Represents the dynamic assembly created.

  DefineDynamicAssembly(self: _AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,evidence: Evidence) -> AssemblyBuilder

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.DefineDynamicAssembly(System.Reflection.AssemblyName,System.Reflection.Emit.Asse

    mblyBuilderAccess,System.Security.Policy.Evidence) method overload.

  

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   evidence: The evidence supplied for the dynamic assembly. The evidence is used unaltered as the final set 

    of evidence used for policy resolution.

  

   Returns: Represents the dynamic assembly created.
  """
  pass
 def DoCallBack(self,theDelegate):
  """
  DoCallBack(self: _AppDomain,theDelegate: CrossAppDomainDelegate)

   Provides COM objects with version-independent access to the 

    System.AppDomain.DoCallBack(System.CrossAppDomainDelegate) method.

  

  

   theDelegate: A delegate that specifies a method to call.
  """
  pass
 def Equals(self,other):
  """
  Equals(self: _AppDomain,other: object) -> bool

  

   Provides COM objects with version-independent access to the inherited 

    System.Object.Equals(System.Object) method.

  

  

   other: The System.Object to compare to the current System.Object.

   Returns: true if the specified System.Object is equal to the current System.Object; otherwise,false.
  """
  pass
 def ExecuteAssembly(self,assemblyFile,assemblySecurity=None,args=None):
  """
  ExecuteAssembly(self: _AppDomain,assemblyFile: str,assemblySecurity: Evidence,args: Array[str]) -> int

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.ExecuteAssembly(System.String,System.Security.Policy.Evidence,System.String[]) 

    method overload.

  

  

   assemblyFile: The name of the file that contains the assembly to execute.

   assemblySecurity: The supplied evidence for the assembly.

   args: The arguments to the entry point of the assembly.

   Returns: The value returned by the entry point of the assembly.

  ExecuteAssembly(self: _AppDomain,assemblyFile: str) -> int

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.ExecuteAssembly(System.String) method overload.

  

  

   assemblyFile: The name of the file that contains the assembly to execute.

   Returns: The value returned by the entry point of the assembly.

  ExecuteAssembly(self: _AppDomain,assemblyFile: str,assemblySecurity: Evidence) -> int

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.ExecuteAssembly(System.String,System.Security.Policy.Evidence) method overload.

  

  

   assemblyFile: The name of the file that contains the assembly to execute.

   assemblySecurity: Evidence for loading the assembly.

   Returns: The value returned by the entry point of the assembly.
  """
  pass
 def GetAssemblies(self):
  """
  GetAssemblies(self: _AppDomain) -> Array[Assembly]

  

   Provides COM objects with version-independent access to the System.AppDomain.GetAssemblies 

    method.

  

   Returns: An array of assemblies in this application domain.
  """
  pass
 def GetData(self,name):
  """
  GetData(self: _AppDomain,name: str) -> object

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.GetData(System.String) method.

  

  

   name: The name of a predefined application domain property,or the name of an application domain 

    property you have defined.

  

   Returns: The value of the name property.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: _AppDomain) -> int

  

   Provides COM objects with version-independent access to the inherited System.Object.GetHashCode 

    method.

  

   Returns: A hash code for the current System.Object.
  """
  pass
 def GetIDsOfNames(self,riid,rgszNames,cNames,lcid,rgDispId):
  """
  GetIDsOfNames(self: _AppDomain,riid: Guid,rgszNames: IntPtr,cNames: UInt32,lcid: UInt32,rgDispId: IntPtr) -> Guid

  

   Maps a set of names to a corresponding set of dispatch identifiers.

  

   riid: Reserved for future use. Must be IID_NULL.

   rgszNames: Passed-in array of names to be mapped.

   cNames: Count of the names to be mapped.

   lcid: The locale context in which to interpret the names.

   rgDispId: Caller-allocated array which receives the IDs corresponding to the names.
  """
  pass
 def GetLifetimeService(self):
  """
  GetLifetimeService(self: _AppDomain) -> object

  

   Provides COM objects with version-independent access to the inherited 

    System.MarshalByRefObject.GetLifetimeService method.

  

   Returns: An object of type System.Runtime.Remoting.Lifetime.ILease used to control the lifetime policy 

    for this instance.
  """
  pass
 def GetType(self):
  """
  GetType(self: _AppDomain) -> Type

  

   Provides COM objects with version-independent access to the System.AppDomain.GetType method.

   Returns: A System.Type representing the type of the current instance.
  """
  pass
 def GetTypeInfo(self,iTInfo,lcid,ppTInfo):
  """
  GetTypeInfo(self: _AppDomain,iTInfo: UInt32,lcid: UInt32,ppTInfo: IntPtr)

   Retrieves the type information for an object,which can then be used to get the type information 

    for an interface.

  

  

   iTInfo: The type information to return.

   lcid: The locale identifier for the type information.

   ppTInfo: Receives a pointer to the requested type information object.
  """
  pass
 def GetTypeInfoCount(self,pcTInfo):
  """
  GetTypeInfoCount(self: _AppDomain) -> UInt32

  

   Retrieves the number of type information interfaces that an object provides (either 0 or 1).
  """
  pass
 def InitializeLifetimeService(self):
  """
  InitializeLifetimeService(self: _AppDomain) -> object

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.InitializeLifetimeService method.

  

   Returns: Always null.
  """
  pass
 def Invoke(self,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr):
  """
  Invoke(self: _AppDomain,dispIdMember: UInt32,riid: Guid,lcid: UInt32,wFlags: Int16,pDispParams: IntPtr,pVarResult: IntPtr,pExcepInfo: IntPtr,puArgErr: IntPtr) -> Guid

  

   Provides access to properties and methods exposed by an object.

  

   dispIdMember: Identifies the member.

   riid: Reserved for future use. Must be IID_NULL.

   lcid: The locale context in which to interpret arguments.

   wFlags: Flags describing the context of the call.

   pDispParams: Pointer to a structure containing an array of arguments,an array of argument DISPIDs for named 

    arguments,and counts for the number of elements in the arrays.

  

   pVarResult: Pointer to the location where the result is to be stored.

   pExcepInfo: Pointer to a structure that contains exception information.

   puArgErr: The index of the first argument that has an error.
  """
  pass
 def Load(self,*__args):
  """
  Load(self: _AppDomain,rawAssembly: Array[Byte],rawSymbolStore: Array[Byte],securityEvidence: Evidence) -> Assembly

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.Load(System.Byte[],System.Byte[],System.Security.Policy.Evidence) method 

    overload.

  

  

   rawAssembly: An array of type byte that is a COFF-based image containing an emitted assembly.

   rawSymbolStore: An array of type byte containing the raw bytes representing the symbols for the assembly.

   securityEvidence: Evidence for loading the assembly.

   Returns: The loaded assembly.

  Load(self: _AppDomain,assemblyRef: AssemblyName,assemblySecurity: Evidence) -> Assembly

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.Load(System.Reflection.AssemblyName,System.Security.Policy.Evidence) method 

    overload.

  

  

   assemblyRef: An object that describes the assembly to load.

   assemblySecurity: Evidence for loading the assembly.

   Returns: The loaded assembly.

  Load(self: _AppDomain,assemblyString: str,assemblySecurity: Evidence) -> Assembly

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.Load(System.String,System.Security.Policy.Evidence) method overload.

  

  

   assemblyString: The display name of the assembly. See System.Reflection.Assembly.FullName.

   assemblySecurity: Evidence for loading the assembly.

   Returns: The loaded assembly.

  Load(self: _AppDomain,rawAssembly: Array[Byte],rawSymbolStore: Array[Byte]) -> Assembly

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.Load(System.Byte[],System.Byte[]) method overload.

  

  

   rawAssembly: An array of type byte that is a COFF-based image containing an emitted assembly.

   rawSymbolStore: An array of type byte containing the raw bytes representing the symbols for the assembly.

   Returns: The loaded assembly.

  Load(self: _AppDomain,assemblyRef: AssemblyName) -> Assembly

  

   Provides COM objects with version-independent access to the 

    System.AppDomain.Load(System.Reflection.AssemblyName) method overload.

  

  

   assemblyRef: An object that describes the assembly to load.

   Returns: The loaded assembly.

  Load(self: _AppDomain,assemblyString: str) -> Assembly

  

   Provides COM objects with version-independent access to the System.AppDomain.Load(System.String) 

    method overload.

  

  

   assemblyString: The display name of the assembly. See System.Reflection.Assembly.FullName.

   Returns: The loaded assembly.

  Load(self: _AppDomain,rawAssembly: Array[Byte]) -> Assembly

  

   Provides COM objects with version-independent access to the System.AppDomain.Load(System.Byte[]) 

    method overload.

  

  

   rawAssembly: An array of type byte that is a COFF-based image containing an emitted assembly.

   Returns: The loaded assembly.
  """
  pass
 def SetAppDomainPolicy(self,domainPolicy):
  """
  SetAppDomainPolicy(self: _AppDomain,domainPolicy: PolicyLevel)

   Provides COM objects with version-independent access to the 

    System.AppDomain.SetAppDomainPolicy(System.Security.Policy.PolicyLevel) method.

  

  

   domainPolicy: The security policy level.
  """
  pass
 def SetCachePath(self,s):
  """
  SetCachePath(self: _AppDomain,s: str)

   Provides COM objects with version-independent access to the 

    System.AppDomain.SetCachePath(System.String) method.

  

  

   s: The fully qualified path to the shadow copy location.
  """
  pass
 def SetData(self,name,data):
  """
  SetData(self: _AppDomain,name: str,data: object)

   Provides COM objects with version-independent access to the 

    System.AppDomain.SetData(System.String,System.Object) method.

  

  

   name: The name of a user-defined application domain property to create or change.

   data: The value of the property.
  """
  pass
 def SetPrincipalPolicy(self,policy):
  """
  SetPrincipalPolicy(self: _AppDomain,policy: PrincipalPolicy)

   Provides COM objects with version-independent access to the 

    System.AppDomain.SetPrincipalPolicy(System.Security.Principal.PrincipalPolicy) method.

  

  

   policy: One of the System.Security.Principal.PrincipalPolicy values that specifies the type of the 

    principal object to attach to threads.
  """
  pass
 def SetShadowCopyPath(self,s):
  """
  SetShadowCopyPath(self: _AppDomain,s: str)

   Provides COM objects with version-independent access to the 

    System.AppDomain.SetShadowCopyPath(System.String) method.

  

  

   s: A list of directory names,where each name is separated by a semicolon.
  """
  pass
 def SetThreadPrincipal(self,principal):
  """
  SetThreadPrincipal(self: _AppDomain,principal: IPrincipal)

   Provides COM objects with version-independent access to the 

    System.AppDomain.SetThreadPrincipal(System.Security.Principal.IPrincipal) method.

  

  

   principal: The principal object to attach to threads.
  """
  pass
 def ToString(self):
  """
  ToString(self: _AppDomain) -> str

  

   Provides COM objects with version-independent access to the System.AppDomain.ToString method.

   Returns: A string formed by concatenating the literal string "Name:",the friendly name of the 

    application domain,and either string representations of the context policies or the string 

    "There are no context policies."
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 BaseDirectory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.AppDomain.BaseDirectory property.



Get: BaseDirectory(self: _AppDomain) -> str



"""

 DynamicDirectory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.AppDomain.DynamicDirectory property.



Get: DynamicDirectory(self: _AppDomain) -> str



"""

 Evidence=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.AppDomain.Evidence property.



Get: Evidence(self: _AppDomain) -> Evidence



"""

 FriendlyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.AppDomain.FriendlyName property.



Get: FriendlyName(self: _AppDomain) -> str



"""

 RelativeSearchPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.AppDomain.RelativeSearchPath property.



Get: RelativeSearchPath(self: _AppDomain) -> str



"""

 ShadowCopyFiles=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.AppDomain.ShadowCopyFiles property.



Get: ShadowCopyFiles(self: _AppDomain) -> bool



"""


 AssemblyLoad=None
 AssemblyResolve=None
 DomainUnload=None
 ProcessExit=None
 ResourceResolve=None
 TypeResolve=None
 UnhandledException=None

