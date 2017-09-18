class AppDomain(MarshalByRefObject,_AppDomain,IEvidenceFactory):
 """ Represents an application domain,which is an isolated environment where applications execute. This class cannot be inherited. """
 def AppendPrivatePath(self,path):
  """
  AppendPrivatePath(self: AppDomain,path: str)

   Appends the specified directory name to the private path list.

  

   path: The name of the directory to be appended to the private path.
  """
  pass
 def ApplyPolicy(self,assemblyName):
  """
  ApplyPolicy(self: AppDomain,assemblyName: str) -> str

  

   Returns the assembly display name after policy has been applied.

  

   assemblyName: The assembly display name,in the form provided by the System.Reflection.Assembly.FullName 

    property.

  

   Returns: A string containing the assembly display name after policy has been applied.
  """
  pass
 def ClearPrivatePath(self):
  """
  ClearPrivatePath(self: AppDomain)

   Resets the path that specifies the location of private assemblies to the empty string ("").
  """
  pass
 def ClearShadowCopyPath(self):
  """
  ClearShadowCopyPath(self: AppDomain)

   Resets the list of directories containing shadow copied assemblies to the empty string ("").
  """
  pass
 def CreateComInstanceFrom(self,*__args):
  """
  CreateComInstanceFrom(self: AppDomain,assemblyFile: str,typeName: str,hashValue: Array[Byte],hashAlgorithm: AssemblyHashAlgorithm) -> ObjectHandle

  

   Creates a new instance of a specified COM type. Parameters specify the name of a file that 

    contains an assembly containing the type and the name of the type.

  

  

   assemblyFile: The name of a file containing an assembly that defines the requested type.

   typeName: The name of the requested type.

   hashValue: Represents the value of the computed hash code.

   hashAlgorithm: Represents the hash algorithm used by the assembly manifest.

   Returns: An object that is a wrapper for the new instance specified by typeName. The return value needs 

    to be unwrapped to access the real object.

  

  CreateComInstanceFrom(self: AppDomain,assemblyName: str,typeName: str) -> ObjectHandle

  

   Creates a new instance of a specified COM type. Parameters specify the name of a file that 

    contains an assembly containing the type and the name of the type.

  

  

   assemblyName: The name of a file containing an assembly that defines the requested type.

   typeName: The name of the requested type.

   Returns: An object that is a wrapper for the new instance specified by typeName. The return value needs 

    to be unwrapped to access the real object.
  """
  pass
 @staticmethod
 def CreateDomain(friendlyName,securityInfo=None,*__args):
  """
  CreateDomain(friendlyName: str,securityInfo: Evidence,info: AppDomainSetup) -> AppDomain

  

   Creates a new application domain using the specified name,evidence,and application domain 

    setup information.

  

  

   friendlyName: The friendly name of the domain. This friendly name can be displayed in user interfaces to 

    identify the domain. For more information,see System.AppDomain.FriendlyName.

  

   securityInfo: Evidence that establishes the identity of the code that runs in the application domain. Pass 

    null to use the evidence of the current application domain.

  

   info: An object that contains application domain initialization information.

   Returns: The newly created application domain.

  CreateDomain(friendlyName: str,securityInfo: Evidence,info: AppDomainSetup,grantSet: PermissionSet,*fullTrustAssemblies: Array[StrongName]) -> AppDomain

  

   Creates a new application domain using the specified name,evidence,application domain setup 

    information,default permission set,and array of fully trusted assemblies.

  

  

   friendlyName: The friendly name of the domain. This friendly name can be displayed in user interfaces to 

    identify the domain. For more information,see the description of System.AppDomain.FriendlyName.

  

   securityInfo: Evidence that establishes the identity of the code that runs in the application domain. Pass 

    null to use the evidence of the current application domain.

  

   info: An object that contains application domain initialization information.

   grantSet: A default permission set that is granted to all assemblies loaded into the new application 

    domain that do not have specific grants.

  

   fullTrustAssemblies: An array of strong names representing assemblies to be considered fully trusted in the new 

    application domain.

  

   Returns: The newly created application domain.

  CreateDomain(friendlyName: str,securityInfo: Evidence,appBasePath: str,appRelativeSearchPath: str,shadowCopyFiles: bool,adInit: AppDomainInitializer,adInitArgs: Array[str]) -> AppDomain

  

   Creates a new application domain with the given name,using evidence,application base path,

    relative search path,and a parameter that specifies whether a shadow copy of an assembly is to 

    be loaded into the application domain. Specifies a callback method that is invoked when the 

    application domain is initialized,and an array of string arguments to pass the callback method.

  

  

   friendlyName: The friendly name of the domain. This friendly name can be displayed in user interfaces to 

    identify the domain. For more information,see System.AppDomain.FriendlyName.

  

   securityInfo: Evidence that establishes the identity of the code that runs in the application domain. Pass 

    null to use the evidence of the current application domain.

  

   appBasePath: The base directory that the assembly resolver uses to probe for assemblies. For more 

    information,see System.AppDomain.BaseDirectory.

  

   appRelativeSearchPath: The path relative to the base directory where the assembly resolver should probe for private 

    assemblies. For more information,see System.AppDomain.RelativeSearchPath.

  

   shadowCopyFiles: true to load a shadow copy of an assembly into the application domain.

   adInit: An System.AppDomainInitializer delegate that represents a callback method to invoke when the new 

    System.AppDomain object is initialized.

  

   adInitArgs: An array of string arguments to be passed to the callback represented by adInit,when the new 

    System.AppDomain object is initialized.

  

   Returns: The newly created application domain.

  CreateDomain(friendlyName: str,securityInfo: Evidence) -> AppDomain

  

   Creates a new application domain with the given name using the supplied evidence.

  

   friendlyName: The friendly name of the domain. This friendly name can be displayed in user interfaces to 

    identify the domain. For more information,see System.AppDomain.FriendlyName.

  

   securityInfo: Evidence that establishes the identity of the code that runs in the application domain. Pass 

    null to use the evidence of the current application domain.

  

   Returns: The newly created application domain.

  CreateDomain(friendlyName: str,securityInfo: Evidence,appBasePath: str,appRelativeSearchPath: str,shadowCopyFiles: bool) -> AppDomain

  

   Creates a new application domain with the given name,using evidence,application base path,

    relative search path,and a parameter that specifies whether a shadow copy of an assembly is to 

    be loaded into the application domain.

  

  

   friendlyName: The friendly name of the domain. This friendly name can be displayed in user interfaces to 

    identify the domain. For more information,see System.AppDomain.FriendlyName.

  

   securityInfo: Evidence that establishes the identity of the code that runs in the application domain. Pass 

    null to use the evidence of the current application domain.

  

   appBasePath: The base directory that the assembly resolver uses to probe for assemblies. For more 

    information,see System.AppDomain.BaseDirectory.

  

   appRelativeSearchPath: The path relative to the base directory where the assembly resolver should probe for private 

    assemblies. For more information,see System.AppDomain.RelativeSearchPath.

  

   shadowCopyFiles: If true,a shadow copy of an assembly is loaded into this application domain.

   Returns: The newly created application domain.

  CreateDomain(friendlyName: str) -> AppDomain

  

   Creates a new application domain with the specified name.

  

   friendlyName: The friendly name of the domain.

   Returns: The newly created application domain.
  """
  pass
 def CreateInstance(self,assemblyName,typeName,*__args):
  """
  CreateInstance(self: AppDomain,assemblyName: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object],securityAttributes: Evidence) -> ObjectHandle

  

   Creates a new instance of the specified type defined in the specified assembly. Parameters 

    specify a binder,binding flags,constructor arguments,culture-specific information used to 

    interpret arguments,activation attributes,and authorization to create the type.

  

  

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

  

  CreateInstance(self: AppDomain,assemblyName: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object]) -> ObjectHandle

  

   Creates a new instance of the specified type defined in the specified assembly. Parameters 

    specify a binder,binding flags,constructor arguments,culture-specific information used to 

    interpret arguments,and optional activation attributes.

  

  

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

  

   Returns: An object that is a wrapper for the new instance specified by typeName. The return value needs 

    to be unwrapped to access the real object.

  

  CreateInstance(self: AppDomain,assemblyName: str,typeName: str) -> ObjectHandle

  

   Creates a new instance of the specified type defined in the specified assembly.

  

   assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

   typeName: The fully qualified name of the requested type,including the namespace but not the assembly,as 

    returned by the System.Type.FullName property.

  

   Returns: An object that is a wrapper for the new instance specified by typeName. The return value needs 

    to be unwrapped to access the real object.

  

  CreateInstance(self: AppDomain,assemblyName: str,typeName: str,activationAttributes: Array[object]) -> ObjectHandle

  

   Creates a new instance of the specified type defined in the specified assembly. A parameter 

    specifies an array of activation attributes.

  

  

   assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

   typeName: The fully qualified name of the requested type,including the namespace but not the assembly,as 

    returned by the System.Type.FullName property.

  

   activationAttributes: An array of one or more attributes that can participate in activation. Typically,an array that 

    contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   Returns: An object that is a wrapper for the new instance specified by typeName. The return value needs 

    to be unwrapped to access the real object.
  """
  pass
 def CreateInstanceAndUnwrap(self,assemblyName,typeName,*__args):
  """
  CreateInstanceAndUnwrap(self: AppDomain,assemblyName: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object],securityAttributes: Evidence) -> object

  

   Creates a new instance of the specified type. Parameters specify the name of the type,and how 

    it is found and created.

  

  

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

  

   culture: A culture-specific object used to govern the coercion of types. If culture is null,the 

    CultureInfo for the current thread is used.

  

   activationAttributes: An array of one or more attributes that can participate in activation. Typically,an array that 

    contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   securityAttributes: Information used to authorize creation of typeName.

   Returns: An instance of the object specified by typeName.

  CreateInstanceAndUnwrap(self: AppDomain,assemblyName: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object]) -> object

  

   Creates a new instance of the specified type defined in the specified assembly,specifying 

    whether the case of the type name is ignored; the binding attributes and the binder that are 

    used to select the type to be created; the arguments of the constructor; the culture; and the 

    activation attributes.

  

  

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

  

   culture: A culture-specific object used to govern the coercion of types. If culture is null,the 

    CultureInfo for the current thread is used.

  

   activationAttributes: An array of one or more attributes that can participate in activation. Typically,an array that 

    contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   Returns: An instance of the object specified by typeName.

  CreateInstanceAndUnwrap(self: AppDomain,assemblyName: str,typeName: str) -> object

  

   Creates a new instance of the specified type. Parameters specify the assembly where the type is 

    defined,and the name of the type.

  

  

   assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

   typeName: The fully qualified name of the requested type,including the namespace but not the assembly,as 

    returned by the System.Type.FullName property.

  

   Returns: An instance of the object specified by typeName.

  CreateInstanceAndUnwrap(self: AppDomain,assemblyName: str,typeName: str,activationAttributes: Array[object]) -> object

  

   Creates a new instance of the specified type. Parameters specify the assembly where the type is 

    defined,the name of the type,and an array of activation attributes.

  

  

   assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

   typeName: The fully qualified name of the requested type,including the namespace but not the assembly,as 

    returned by the System.Type.FullName property.

  

   activationAttributes: An array of one or more attributes that can participate in activation. Typically,an array that 

    contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   Returns: An instance of the object specified by typeName.
  """
  pass
 def CreateInstanceFrom(self,assemblyFile,typeName,*__args):
  """
  CreateInstanceFrom(self: AppDomain,assemblyFile: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object],securityAttributes: Evidence) -> ObjectHandle

  

   Creates a new instance of the specified type defined in the specified assembly file.

  

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

  

  CreateInstanceFrom(self: AppDomain,assemblyFile: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object]) -> ObjectHandle

  

   Creates a new instance of the specified type defined in the specified assembly file.

  

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

  

   Returns: An object that is a wrapper for the new instance,or null if typeName is not found. The return 

    value needs to be unwrapped to access the real object.

  

  CreateInstanceFrom(self: AppDomain,assemblyFile: str,typeName: str) -> ObjectHandle

  

   Creates a new instance of the specified type defined in the specified assembly file.

  

   assemblyFile: The name,including the path,of a file that contains an assembly that defines the requested 

    type. The assembly is loaded using the System.Reflection.Assembly.LoadFrom(System.String)  

    method.

  

   typeName: The fully qualified name of the requested type,including the namespace but not the assembly,as 

    returned by the System.Type.FullName property.

  

   Returns: An object that is a wrapper for the new instance,or null if typeName is not found. The return 

    value needs to be unwrapped to access the real object.

  

  CreateInstanceFrom(self: AppDomain,assemblyFile: str,typeName: str,activationAttributes: Array[object]) -> ObjectHandle

  

   Creates a new instance of the specified type defined in the specified assembly file.

  

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
  """
  pass
 def CreateInstanceFromAndUnwrap(self,*__args):
  """
  CreateInstanceFromAndUnwrap(self: AppDomain,assemblyName: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object],securityAttributes: Evidence) -> object

  

   Creates a new instance of the specified type defined in the specified assembly file.

  

   assemblyName: The file name and path of the assembly that defines the requested type.

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

   Returns: The requested object,or null if typeName is not found.

  CreateInstanceFromAndUnwrap(self: AppDomain,assemblyFile: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object]) -> object

  

   Creates a new instance of the specified type defined in the specified assembly file,specifying 

    whether the case of the type name is ignored; the binding attributes and the binder that are 

    used to select the type to be created; the arguments of the constructor; the culture; and the 

    activation attributes.

  

  

   assemblyFile: The file name and path of the assembly that defines the requested type.

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

  

   Returns: The requested object,or null if typeName is not found.

  CreateInstanceFromAndUnwrap(self: AppDomain,assemblyName: str,typeName: str) -> object

  

   Creates a new instance of the specified type defined in the specified assembly file.

  

   assemblyName: The file name and path of the assembly that defines the requested type.

   typeName: The fully qualified name of the requested type,including the namespace but not the assembly,as 

    returned by the System.Type.FullName property.

  

   Returns: The requested object,or null if typeName is not found.

  CreateInstanceFromAndUnwrap(self: AppDomain,assemblyName: str,typeName: str,activationAttributes: Array[object]) -> object

  

   Creates a new instance of the specified type defined in the specified assembly file.

  

   assemblyName: The file name and path of the assembly that defines the requested type.

   typeName: The fully qualified name of the requested type,including the namespace but not the assembly 

    (see the System.Type.FullName property).

  

   activationAttributes: An array of one or more attributes that can participate in activation. Typically,an array that 

    contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   Returns: The requested object,or null if typeName is not found.
  """
  pass
 def DefineDynamicAssembly(self,name,access,*__args):
  """
  DefineDynamicAssembly(self: AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,dir: str,evidence: Evidence,requiredPermissions: PermissionSet,optionalPermissions: PermissionSet,refusedPermissions: PermissionSet) -> AssemblyBuilder

  

   Defines a dynamic assembly using the specified name,access mode,storage directory,evidence,

    and permission requests.

  

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   dir: The name of the directory where the assembly will be saved. If dir is null,the directory 

    defaults to the current directory.

  

   evidence: The evidence supplied for the dynamic assembly. The evidence is used unaltered as the final set 

    of evidence used for policy resolution.

  

   requiredPermissions: The required permissions request.

   optionalPermissions: The optional permissions request.

   refusedPermissions: The refused permissions request.

   Returns: A dynamic assembly with the specified name and features.

  DefineDynamicAssembly(self: AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,evidence: Evidence,requiredPermissions: PermissionSet,optionalPermissions: PermissionSet,refusedPermissions: PermissionSet) -> AssemblyBuilder

  

   Defines a dynamic assembly using the specified name,access mode,evidence,and permission 

    requests.

  

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   evidence: The evidence supplied for the dynamic assembly. The evidence is used unaltered as the final set 

    of evidence used for policy resolution.

  

   requiredPermissions: The required permissions request.

   optionalPermissions: The optional permissions request.

   refusedPermissions: The refused permissions request.

   Returns: A dynamic assembly with the specified name and features.

  DefineDynamicAssembly(self: AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,dir: str,requiredPermissions: PermissionSet,optionalPermissions: PermissionSet,refusedPermissions: PermissionSet) -> AssemblyBuilder

  

   Defines a dynamic assembly using the specified name,access mode,storage directory,and 

    permission requests.

  

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   dir: The name of the directory where the assembly will be saved. If dir is null,the directory 

    defaults to the current directory.

  

   requiredPermissions: The required permissions request.

   optionalPermissions: The optional permissions request.

   refusedPermissions: The refused permissions request.

   Returns: A dynamic assembly with the specified name and features.

  DefineDynamicAssembly(self: AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,dir: str,isSynchronized: bool,assemblyAttributes: IEnumerable[CustomAttributeBuilder]) -> AssemblyBuilder

  DefineDynamicAssembly(self: AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,dir: str,evidence: Evidence,requiredPermissions: PermissionSet,optionalPermissions: PermissionSet,refusedPermissions: PermissionSet,isSynchronized: bool,assemblyAttributes: IEnumerable[CustomAttributeBuilder]) -> AssemblyBuilder

  DefineDynamicAssembly(self: AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,dir: str,evidence: Evidence,requiredPermissions: PermissionSet,optionalPermissions: PermissionSet,refusedPermissions: PermissionSet,isSynchronized: bool) -> AssemblyBuilder

  

   Defines a dynamic assembly using the specified name,access mode,storage directory,evidence,

    permission requests,and synchronization option.

  

  

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

  

   Returns: A dynamic assembly with the specified name and features.

  DefineDynamicAssembly(self: AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,dir: str,evidence: Evidence) -> AssemblyBuilder

  

   Defines a dynamic assembly using the specified name,access mode,storage directory,and 

    evidence.

  

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   dir: The name of the directory where the assembly will be saved. If dir is null,the directory 

    defaults to the current directory.

  

   evidence: The evidence supplied for the dynamic assembly. The evidence is used unaltered as the final set 

    of evidence used for policy resolution.

  

   Returns: A dynamic assembly with the specified name and features.

  DefineDynamicAssembly(self: AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,assemblyAttributes: IEnumerable[CustomAttributeBuilder],securityContextSource: SecurityContextSource) -> AssemblyBuilder

  DefineDynamicAssembly(self: AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,assemblyAttributes: IEnumerable[CustomAttributeBuilder]) -> AssemblyBuilder

  DefineDynamicAssembly(self: AppDomain,name: AssemblyName,access: AssemblyBuilderAccess) -> AssemblyBuilder

  

   Defines a dynamic assembly with the specified name and access mode.

  

   name: The unique identity of the dynamic assembly.

   access: The access mode for the dynamic assembly.

   Returns: A dynamic assembly with the specified name and access mode.

  DefineDynamicAssembly(self: AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,requiredPermissions: PermissionSet,optionalPermissions: PermissionSet,refusedPermissions: PermissionSet) -> AssemblyBuilder

  

   Defines a dynamic assembly using the specified name,access mode,and permission requests.

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   requiredPermissions: The required permissions request.

   optionalPermissions: The optional permissions request.

   refusedPermissions: The refused permissions request.

   Returns: A dynamic assembly with the specified name and features.

  DefineDynamicAssembly(self: AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,evidence: Evidence) -> AssemblyBuilder

  

   Defines a dynamic assembly using the specified name,access mode,and evidence.

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   evidence: The evidence supplied for the dynamic assembly. The evidence is used unaltered as the final set 

    of evidence used for policy resolution.

  

   Returns: A dynamic assembly with the specified name and features.

  DefineDynamicAssembly(self: AppDomain,name: AssemblyName,access: AssemblyBuilderAccess,dir: str) -> AssemblyBuilder

  

   Defines a dynamic assembly using the specified name,access mode,and storage directory.

  

   name: The unique identity of the dynamic assembly.

   access: The mode in which the dynamic assembly will be accessed.

   dir: The name of the directory where the assembly will be saved. If dir is null,the directory 

    defaults to the current directory.

  

   Returns: A dynamic assembly with the specified name and features.
  """
  pass
 def DoCallBack(self,callBackDelegate):
  """
  DoCallBack(self: AppDomain,callBackDelegate: CrossAppDomainDelegate)

   Executes the code in another application domain that is identified by the specified delegate.

  

   callBackDelegate: A delegate that specifies a method to call.
  """
  pass
 def ExecuteAssembly(self,assemblyFile,*__args):
  """
  ExecuteAssembly(self: AppDomain,assemblyFile: str,args: Array[str]) -> int

  

   Executes the assembly contained in the specified file,using the specified arguments.

  

   assemblyFile: The name of the file that contains the assembly to execute.

   args: The arguments to the entry point of the assembly.

   Returns: The value that is returned by the entry point of the assembly.

  ExecuteAssembly(self: AppDomain,assemblyFile: str,assemblySecurity: Evidence,args: Array[str],hashValue: Array[Byte],hashAlgorithm: AssemblyHashAlgorithm) -> int

  

   Executes the assembly contained in the specified file,using the specified evidence,arguments,

    hash value,and hash algorithm.

  

  

   assemblyFile: The name of the file that contains the assembly to execute.

   assemblySecurity: The supplied evidence for the assembly.

   args: The arguments to the entry point of the assembly.

   hashValue: Represents the value of the computed hash code.

   hashAlgorithm: Represents the hash algorithm used by the assembly manifest.

   Returns: The value returned by the entry point of the assembly.

  ExecuteAssembly(self: AppDomain,assemblyFile: str,args: Array[str],hashValue: Array[Byte],hashAlgorithm: AssemblyHashAlgorithm) -> int

  

   Executes the assembly contained in the specified file,using the specified arguments,hash 

    value,and hash algorithm.

  

  

   assemblyFile: The name of the file that contains the assembly to execute.

   args: The arguments to the entry point of the assembly.

   hashValue: Represents the value of the computed hash code.

   hashAlgorithm: Represents the hash algorithm used by the assembly manifest.

   Returns: The value that is returned by the entry point of the assembly.

  ExecuteAssembly(self: AppDomain,assemblyFile: str) -> int

  

   Executes the assembly contained in the specified file.

  

   assemblyFile: The name of the file that contains the assembly to execute.

   Returns: The value returned by the entry point of the assembly.

  ExecuteAssembly(self: AppDomain,assemblyFile: str,assemblySecurity: Evidence) -> int

  

   Executes the assembly contained in the specified file,using the specified evidence.

  

   assemblyFile: The name of the file that contains the assembly to execute.

   assemblySecurity: Evidence for loading the assembly.

   Returns: The value returned by the entry point of the assembly.

  ExecuteAssembly(self: AppDomain,assemblyFile: str,assemblySecurity: Evidence,args: Array[str]) -> int

  

   Executes the assembly contained in the specified file,using the specified evidence and 

    arguments.

  

  

   assemblyFile: The name of the file that contains the assembly to execute.

   assemblySecurity: The supplied evidence for the assembly.

   args: The arguments to the entry point of the assembly.

   Returns: The value returned by the entry point of the assembly.
  """
  pass
 def ExecuteAssemblyByName(self,assemblyName,*__args):
  """
  ExecuteAssemblyByName(self: AppDomain,assemblyName: str,*args: Array[str]) -> int

  

   Executes the assembly given its display name,using the specified arguments.

  

   assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

   args: Command-line arguments to pass when starting the process.

   Returns: The value that is returned by the entry point of the assembly.

  ExecuteAssemblyByName(self: AppDomain,assemblyName: AssemblyName,assemblySecurity: Evidence,*args: Array[str]) -> int

  

   Executes the assembly given an System.Reflection.AssemblyName,using the specified evidence and 

    arguments.

  

  

   assemblyName: An System.Reflection.AssemblyName object representing the name of the assembly.

   assemblySecurity: Evidence for loading the assembly.

   args: Command-line arguments to pass when starting the process.

   Returns: The value returned by the entry point of the assembly.

  ExecuteAssemblyByName(self: AppDomain,assemblyName: AssemblyName,*args: Array[str]) -> int

  

   Executes the assembly given an System.Reflection.AssemblyName,using the specified arguments.

  

   assemblyName: An System.Reflection.AssemblyName object representing the name of the assembly.

   args: Command-line arguments to pass when starting the process.

   Returns: The value that is returned by the entry point of the assembly.

  ExecuteAssemblyByName(self: AppDomain,assemblyName: str) -> int

  

   Executes an assembly given its display name.

  

   assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

   Returns: The value returned by the entry point of the assembly.

  ExecuteAssemblyByName(self: AppDomain,assemblyName: str,assemblySecurity: Evidence) -> int

  

   Executes an assembly given its display name,using the specified evidence.

  

   assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

   assemblySecurity: Evidence for loading the assembly.

   Returns: The value returned by the entry point of the assembly.

  ExecuteAssemblyByName(self: AppDomain,assemblyName: str,assemblySecurity: Evidence,*args: Array[str]) -> int

  

   Executes the assembly given its display name,using the specified evidence and arguments.

  

   assemblyName: The display name of the assembly. See System.Reflection.Assembly.FullName.

   assemblySecurity: Evidence for loading the assembly.

   args: Command-line arguments to pass when starting the process.

   Returns: The value returned by the entry point of the assembly.
  """
  pass
 def GetAssemblies(self):
  """
  GetAssemblies(self: AppDomain) -> Array[Assembly]

  

   Gets the assemblies that have been loaded into the execution context of this application domain.

   Returns: An array of assemblies in this application domain.
  """
  pass
 @staticmethod
 def GetCurrentThreadId():
  """
  GetCurrentThreadId() -> int

  

   Gets the current thread identifier.

   Returns: A 32-bit signed integer that is the identifier of the current thread.
  """
  pass
 def GetData(self,name):
  """
  GetData(self: AppDomain,name: str) -> object

  

   Gets the value stored in the current application domain for the specified name.

  

   name: The name of a predefined application domain property,or the name of an application domain 

    property you have defined.

  

   Returns: The value of the name property,or null if the property does not exist.
  """
  pass
 def GetType(self):
  """
  GetType(self: AppDomain) -> Type

  

   Gets the type of the current instance.

   Returns: The type of the current instance.
  """
  pass
 def InitializeLifetimeService(self):
  """
  InitializeLifetimeService(self: AppDomain) -> object

  

   Gives the System.AppDomain an infinite lifetime by preventing a lease from being created.

   Returns: Always null.
  """
  pass
 def IsCompatibilitySwitchSet(self,value):
  """
  IsCompatibilitySwitchSet(self: AppDomain,value: str) -> Nullable[bool]

  

   Gets a nullable Boolean value that indicates whether any compatibility switches are set,and if 

    so,whether the specified compatibility switch is set.

  

  

   value: The compatibility switch to test.

   Returns: A null reference (Nothing in Visual Basic) if no compatibility switches are set; otherwise,a 

    Boolean value that indicates whether the compatibility switch that is specified by value is set.
  """
  pass
 def IsDefaultAppDomain(self):
  """
  IsDefaultAppDomain(self: AppDomain) -> bool

  

   Returns a value that indicates whether the application domain is the default application domain 

    for the process.

  

   Returns: true if the current System.AppDomain object represents the default application domain for the 

    process; otherwise,false.
  """
  pass
 def IsFinalizingForUnload(self):
  """
  IsFinalizingForUnload(self: AppDomain) -> bool

  

   Indicates whether this application domain is unloading,and the objects it contains are being 

    finalized by the common language runtime.

  

   Returns: true if this application domain is unloading and the common language runtime has started 

    invoking finalizers; otherwise,false.
  """
  pass
 def Load(self,*__args):
  """
  Load(self: AppDomain,rawAssembly: Array[Byte],rawSymbolStore: Array[Byte],securityEvidence: Evidence) -> Assembly

  

   Loads the System.Reflection.Assembly with a common object file format (COFF) based image 

    containing an emitted System.Reflection.Assembly. The raw bytes representing the symbols for the 

    System.Reflection.Assembly are also loaded.

  

  

   rawAssembly: An array of type byte that is a COFF-based image containing an emitted assembly.

   rawSymbolStore: An array of type byte containing the raw bytes representing the symbols for the assembly.

   securityEvidence: Evidence for loading the assembly.

   Returns: The loaded assembly.

  Load(self: AppDomain,assemblyRef: AssemblyName,assemblySecurity: Evidence) -> Assembly

  

   Loads an System.Reflection.Assembly given its System.Reflection.AssemblyName.

  

   assemblyRef: An object that describes the assembly to load.

   assemblySecurity: Evidence for loading the assembly.

   Returns: The loaded assembly.

  Load(self: AppDomain,assemblyString: str,assemblySecurity: Evidence) -> Assembly

  

   Loads an System.Reflection.Assembly given its display name.

  

   assemblyString: The display name of the assembly. See System.Reflection.Assembly.FullName.

   assemblySecurity: Evidence for loading the assembly.

   Returns: The loaded assembly.

  Load(self: AppDomain,rawAssembly: Array[Byte],rawSymbolStore: Array[Byte]) -> Assembly

  

   Loads the System.Reflection.Assembly with a common object file format (COFF) based image 

    containing an emitted System.Reflection.Assembly. The raw bytes representing the symbols for the 

    System.Reflection.Assembly are also loaded.

  

  

   rawAssembly: An array of type byte that is a COFF-based image containing an emitted assembly.

   rawSymbolStore: An array of type byte containing the raw bytes representing the symbols for the assembly.

   Returns: The loaded assembly.

  Load(self: AppDomain,assemblyRef: AssemblyName) -> Assembly

  

   Loads an System.Reflection.Assembly given its System.Reflection.AssemblyName.

  

   assemblyRef: An object that describes the assembly to load.

   Returns: The loaded assembly.

  Load(self: AppDomain,assemblyString: str) -> Assembly

  

   Loads an System.Reflection.Assembly given its display name.

  

   assemblyString: The display name of the assembly. See System.Reflection.Assembly.FullName.

   Returns: The loaded assembly.

  Load(self: AppDomain,rawAssembly: Array[Byte]) -> Assembly

  

   Loads the System.Reflection.Assembly with a common object file format (COFF) based image 

    containing an emitted System.Reflection.Assembly.

  

  

   rawAssembly: An array of type byte that is a COFF-based image containing an emitted assembly.

   Returns: The loaded assembly.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def ReflectionOnlyGetAssemblies(self):
  """
  ReflectionOnlyGetAssemblies(self: AppDomain) -> Array[Assembly]

  

   Returns the assemblies that have been loaded into the reflection-only context of the application 

    domain.

  

   Returns: An array of System.Reflection.Assembly objects that represent the assemblies loaded into the 

    reflection-only context of the application domain.
  """
  pass
 def SetAppDomainPolicy(self,domainPolicy):
  """
  SetAppDomainPolicy(self: AppDomain,domainPolicy: PolicyLevel)

   Establishes the security policy level for this application domain.

  

   domainPolicy: The security policy level.
  """
  pass
 def SetCachePath(self,path):
  """
  SetCachePath(self: AppDomain,path: str)

   Establishes the specified directory path as the location where assemblies are shadow copied.

  

   path: The fully qualified path to the shadow copy location.
  """
  pass
 def SetData(self,name,data,permission=None):
  """
  SetData(self: AppDomain,name: str,data: object,permission: IPermission)

   Assigns the specified value to the specified application domain property,with a specified 

    permission to demand of the caller when the property is retrieved.

  

  

   name: The name of a user-defined application domain property to create or change.

   data: The value of the property.

   permission: The permission to demand of the caller when the property is retrieved.

  SetData(self: AppDomain,name: str,data: object)

   Assigns the specified value to the specified application domain property.

  

   name: The name of a user-defined application domain property to create or change.

   data: The value of the property.
  """
  pass
 def SetDynamicBase(self,path):
  """
  SetDynamicBase(self: AppDomain,path: str)

   Establishes the specified directory path as the base directory for subdirectories where 

    dynamically generated files are stored and accessed.

  

  

   path: The fully qualified path that is the base directory for subdirectories where dynamic assemblies 

    are stored.
  """
  pass
 def SetPrincipalPolicy(self,policy):
  """
  SetPrincipalPolicy(self: AppDomain,policy: PrincipalPolicy)

   Specifies how principal and identity objects should be attached to a thread if the thread 

    attempts to bind to a principal while executing in this application domain.

  

  

   policy: One of the System.Security.Principal.PrincipalPolicy values that specifies the type of the 

    principal object to attach to threads.
  """
  pass
 def SetShadowCopyFiles(self):
  """
  SetShadowCopyFiles(self: AppDomain)

   Turns on shadow copying.
  """
  pass
 def SetShadowCopyPath(self,path):
  """
  SetShadowCopyPath(self: AppDomain,path: str)

   Establishes the specified directory path as the location of assemblies to be shadow copied.

  

   path: A list of directory names,where each name is separated by a semicolon.
  """
  pass
 def SetThreadPrincipal(self,principal):
  """
  SetThreadPrincipal(self: AppDomain,principal: IPrincipal)

   Sets the default principal object to be attached to threads if they attempt to bind to a 

    principal while executing in this application domain.

  

  

   principal: The principal object to attach to threads.
  """
  pass
 def ToString(self):
  """
  ToString(self: AppDomain) -> str

  

   Obtains a string representation that includes the friendly name of the application domain and 

    any context policies.

  

   Returns: A string formed by concatenating the literal string "Name:",the friendly name of the 

    application domain,and either string representations of the context policies or the string 

    "There are no context policies."
  """
  pass
 @staticmethod
 def Unload(domain):
  """
  Unload(domain: AppDomain)

   Unloads the specified application domain.

  

   domain: An application domain to unload.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 ActivationContext=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the activation context for the current application domain.



Get: ActivationContext(self: AppDomain) -> ActivationContext



"""

 ApplicationIdentity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the identity of the application in the application domain.



Get: ApplicationIdentity(self: AppDomain) -> ApplicationIdentity



"""

 ApplicationTrust=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets information describing permissions granted to an application and whether the application has a trust level that allows it to run.



Get: ApplicationTrust(self: AppDomain) -> ApplicationTrust



"""

 BaseDirectory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the base directory that the assembly resolver uses to probe for assemblies.



Get: BaseDirectory(self: AppDomain) -> str



"""

 DomainManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the domain manager that was provided by the host when the application domain was initialized.



Get: DomainManager(self: AppDomain) -> AppDomainManager



"""

 DynamicDirectory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the directory that the assembly resolver uses to probe for dynamically created assemblies.



Get: DynamicDirectory(self: AppDomain) -> str



"""

 Evidence=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Security.Policy.Evidence associated with this application domain.



Get: Evidence(self: AppDomain) -> Evidence



"""

 FriendlyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the friendly name of this application domain.



Get: FriendlyName(self: AppDomain) -> str



"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an integer that uniquely identifies the application domain within the process.



Get: Id(self: AppDomain) -> int



"""

 IsFullyTrusted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether assemblies that are loaded into the current application domain execute with full trust.



Get: IsFullyTrusted(self: AppDomain) -> bool



"""

 IsHomogenous=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the current application domain has a set of permissions that is granted to all assemblies that are loaded into the application domain.



Get: IsHomogenous(self: AppDomain) -> bool



"""

 MonitoringSurvivedMemorySize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of bytes that survived the last full,blocking collection and that are known to be referenced by the current application domain.



Get: MonitoringSurvivedMemorySize(self: AppDomain) -> Int64



"""

 MonitoringTotalAllocatedMemorySize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total size,in bytes,of all memory allocations that have been made by the application domain since it was created,without subtracting memory that has been collected.



Get: MonitoringTotalAllocatedMemorySize(self: AppDomain) -> Int64



"""

 MonitoringTotalProcessorTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the total processor time that has been used by all threads while executing in the current application domain,since the process started.



Get: MonitoringTotalProcessorTime(self: AppDomain) -> TimeSpan



"""

 PermissionSet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the permission set of a sandboxed application domain.



Get: PermissionSet(self: AppDomain) -> PermissionSet



"""

 RelativeSearchPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the path under the base directory where the assembly resolver should probe for private assemblies.



Get: RelativeSearchPath(self: AppDomain) -> str



"""

 SetupInformation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the application domain configuration information for this instance.



Get: SetupInformation(self: AppDomain) -> AppDomainSetup



"""

 ShadowCopyFiles=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an indication whether the application domain is configured to shadow copy files.



Get: ShadowCopyFiles(self: AppDomain) -> bool



"""


 AssemblyLoad=None
 AssemblyResolve=None
 CurrentDomain=None
 DomainUnload=None
 FirstChanceException=None
 MonitoringIsEnabled=False
 ProcessExit=None
 ReflectionOnlyAssemblyResolve=None
 ResourceResolve=None
 TypeResolve=None
 UnhandledException=None

