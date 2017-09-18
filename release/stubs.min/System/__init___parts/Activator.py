class Activator(object,_Activator):
 """ Contains methods to create types of objects locally or remotely,or obtain references to existing remote objects. This class cannot be inherited. """
 @staticmethod
 def CreateComInstanceFrom(assemblyName,typeName,hashValue=None,hashAlgorithm=None):
  """
  CreateComInstanceFrom(assemblyName: str,typeName: str,hashValue: Array[Byte],hashAlgorithm: AssemblyHashAlgorithm) -> ObjectHandle

  

   Creates an instance of the COM object whose name is specified,using the named assembly file and 

    the default constructor.

  

  

   assemblyName: The name of a file that contains an assembly where the type named typeName is sought.

   typeName: The name of the preferred type.

   hashValue: The value of the computed hash code.

   hashAlgorithm: The hash algorithm used for hashing files and generating the strong name.

   Returns: A handle that must be unwrapped to access the newly created instance.

  CreateComInstanceFrom(assemblyName: str,typeName: str) -> ObjectHandle

  

   Creates an instance of the COM object whose name is specified,using the named assembly file and 

    the constructor that best matches the specified parameters.

  

  

   assemblyName: The name of a file that contains an assembly where the type named typeName is sought.

   typeName: The name of the preferred type.

   Returns: A handle that must be unwrapped to access the newly created instance.
  """
  pass
 @staticmethod
 def CreateInstance(*__args):
  """
  CreateInstance(assemblyName: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object]) -> ObjectHandle

  

   Creates an instance of the type whose name is specified,using the named assembly and the 

    constructor that best matches the specified parameters.

  

  

   assemblyName: The name of the assembly where the type named typeName is sought. If assemblyName is null,the 

    executing assembly is searched.

  

   typeName: The name of the preferred type.

   ignoreCase: true to specify that the search for typeName is not case-sensitive; false to specify that the 

    search is case-sensitive.

  

   bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If 

    bindingAttr is zero,a case-sensitive search for public constructors is conducted.

  

   binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If 

    binder is null,the default binder is used.

  

   args: An array of arguments that match in number,order,and type the parameters of the constructor to 

    invoke. If args is an empty array or null,the constructor that takes no parameters (the default 

    constructor) is invoked.

  

   culture: Culture-specific information that governs the coercion of args to the formal types declared for 

    the typeName constructor. If culture is null,the System.Globalization.CultureInfo for the 

    current thread is used.

  

   activationAttributes: An array of one or more attributes that can participate in activation. This is typically an 

    array that contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   Returns: A handle that must be unwrapped to access the newly created instance.

  CreateInstance(domain: AppDomain,assemblyName: str,typeName: str) -> ObjectHandle

  

   Creates an instance of the type whose name is specified in the specified remote domain,using 

    the named assembly and default constructor.

  

  

   domain: The remote domain where the type named typeName is created.

   assemblyName: The name of the assembly where the type named typeName is sought. If assemblyName is null,the 

    executing assembly is searched.

  

   typeName: The name of the preferred type.

   Returns: A handle that must be unwrapped to access the newly created instance.

  CreateInstance[T]() -> T

  CreateInstance(assemblyName: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object],securityInfo: Evidence) -> ObjectHandle

  

   Creates an instance of the type whose name is specified,using the named assembly and the 

    constructor that best matches the specified parameters.

  

  

   assemblyName: The name of the assembly where the type named typeName is sought. If assemblyName is null,the 

    executing assembly is searched.

  

   typeName: The name of the preferred type.

   ignoreCase: true to specify that the search for typeName is not case-sensitive; false to specify that the 

    search is case-sensitive.

  

   bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If 

    bindingAttr is zero,a case-sensitive search for public constructors is conducted.

  

   binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If 

    binder is null,the default binder is used.

  

   args: An array of arguments that match in number,order,and type the parameters of the constructor to 

    invoke. If args is an empty array or null,the constructor that takes no parameters (the default 

    constructor) is invoked.

  

   culture: Culture-specific information that governs the coercion of args to the formal types declared for 

    the typeName constructor. If culture is null,the System.Globalization.CultureInfo for the 

    current thread is used.

  

   activationAttributes: An array of one or more attributes that can participate in activation. This is typically an 

    array that contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   securityInfo: Information used to make security policy decisions and grant code permissions.

   Returns: A handle that must be unwrapped to access the newly created instance.

  CreateInstance(activationContext: ActivationContext) -> ObjectHandle

  

   Creates an instance of the type designated by the specified System.ActivationContext object.

  

   activationContext: An activation context object that specifies the object to create.

   Returns: A handle that must be unwrapped to access the newly created object.

  CreateInstance(activationContext: ActivationContext,activationCustomData: Array[str]) -> ObjectHandle

  

   Creates an instance of the type that is designated by the specified System.ActivationContext 

    object and activated with the specified custom activation data.

  

  

   activationContext: An activation context object that specifies the object to create.

   activationCustomData: An array of Unicode strings that contain custom activation data.

   Returns: A handle that must be unwrapped to access the newly created object.

  CreateInstance(domain: AppDomain,assemblyName: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object],securityAttributes: Evidence) -> ObjectHandle

  

   Creates an instance of the type whose name is specified in the specified remote domain,using 

    the named assembly and the constructor that best matches the specified parameters.

  

  

   domain: The domain where the type named typeName is created.

   assemblyName: The name of the assembly where the type named typeName is sought. If assemblyName is null,the 

    executing assembly is searched.

  

   typeName: The name of the preferred type.

   ignoreCase: true to specify that the search for typeName is not case-sensitive; false to specify that the 

    search is case-sensitive.

  

   bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If 

    bindingAttr is zero,a case-sensitive search for public constructors is conducted.

  

   binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If 

    binder is null,the default binder is used.

  

   args: An array of arguments that match in number,order,and type the parameters of the constructor to 

    invoke. If args is an empty array or null,the constructor that takes no parameters (the default 

    constructor) is invoked.

  

   culture: Culture-specific information that governs the coercion of args to the formal types declared for 

    the typeName constructor. If culture is null,the System.Globalization.CultureInfo for the 

    current thread is used.

  

   activationAttributes: An array of one or more attributes that can participate in activation. This is typically an 

    array that contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   securityAttributes: Information used to make security policy decisions and grant code permissions.

   Returns: A handle that must be unwrapped to access the newly created instance.

  CreateInstance(domain: AppDomain,assemblyName: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object]) -> ObjectHandle

  

   Creates an instance of the type whose name is specified in the specified remote domain,using 

    the named assembly and the constructor that best matches the specified parameters.

  

  

   domain: The domain where the type named typeName is created.

   assemblyName: The name of the assembly where the type named typeName is sought. If assemblyName is null,the 

    executing assembly is searched.

  

   typeName: The name of the preferred type.

   ignoreCase: true to specify that the search for typeName is not case-sensitive; false to specify that the 

    search is case-sensitive.

  

   bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If 

    bindingAttr is zero,a case-sensitive search for public constructors is conducted.

  

   binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If 

    binder is null,the default binder is used.

  

   args: An array of arguments that match in number,order,and type the parameters of the constructor to 

    invoke. If args is an empty array or null,the constructor that takes no parameters (the default 

    constructor) is invoked.

  

   culture: Culture-specific information that governs the coercion of args to the formal types declared for 

    the typeName constructor. If culture is null,the System.Globalization.CultureInfo for the 

    current thread is used.

  

   activationAttributes: An array of one or more attributes that can participate in activation. This is typically an 

    array that contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   Returns: A handle that must be unwrapped to access the newly created instance.

  CreateInstance(type: Type,*args: Array[object]) -> object

  

   Creates an instance of the specified type using the constructor that best matches the specified 

    parameters.

  

  

   type: The type of object to create.

   args: An array of arguments that match in number,order,and type the parameters of the constructor to 

    invoke. If args is an empty array or null,the constructor that takes no parameters (the default 

    constructor) is invoked.

  

   Returns: A reference to the newly created object.

  CreateInstance(type: Type,args: Array[object],activationAttributes: Array[object]) -> object

  

   Creates an instance of the specified type using the constructor that best matches the specified 

    parameters.

  

  

   type: The type of object to create.

   args: An array of arguments that match in number,order,and type the parameters of the constructor to 

    invoke. If args is an empty array or null,the constructor that takes no parameters (the default 

    constructor) is invoked.

  

   activationAttributes: An array of one or more attributes that can participate in activation. This is typically an 

    array that contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   Returns: A reference to the newly created object.

  CreateInstance(type: Type,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo) -> object

  

   Creates an instance of the specified type using the constructor that best matches the specified 

    parameters.

  

  

   type: The type of object to create.

   bindingAttr: A combination of zero or more bit flags that affect the search for the type constructor. If 

    bindingAttr is zero,a case-sensitive search for public constructors is conducted.

  

   binder: An object that uses bindingAttr and args to seek and identify the type constructor. If binder is 

    null,the default binder is used.

  

   args: An array of arguments that match in number,order,and type the parameters of the constructor to 

    invoke. If args is an empty array or null,the constructor that takes no parameters (the default 

    constructor) is invoked.

  

   culture: Culture-specific information that governs the coercion of args to the formal types declared for 

    the type constructor. If culture is null,the System.Globalization.CultureInfo for the current 

    thread is used.

  

   Returns: A reference to the newly created object.

  CreateInstance(type: Type,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object]) -> object

  

   Creates an instance of the specified type using the constructor that best matches the specified 

    parameters.

  

  

   type: The type of object to create.

   bindingAttr: A combination of zero or more bit flags that affect the search for the type constructor. If 

    bindingAttr is zero,a case-sensitive search for public constructors is conducted.

  

   binder: An object that uses bindingAttr and args to seek and identify the type constructor. If binder is 

    null,the default binder is used.

  

   args: An array of arguments that match in number,order,and type the parameters of the constructor to 

    invoke. If args is an empty array or null,the constructor that takes no parameters (the default 

    constructor) is invoked.

  

   culture: Culture-specific information that governs the coercion of args to the formal types declared for 

    the type constructor. If culture is null,the System.Globalization.CultureInfo for the current 

    thread is used.

  

   activationAttributes: An array of one or more attributes that can participate in activation. This is typically an 

    array that contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   Returns: A reference to the newly created object.

  CreateInstance(assemblyName: str,typeName: str,activationAttributes: Array[object]) -> ObjectHandle

  

   Creates an instance of the type whose name is specified,using the named assembly and default 

    constructor.

  

  

   assemblyName: The name of the assembly where the type named typeName is sought. If assemblyName is null,the 

    executing assembly is searched.

  

   typeName: The name of the preferred type.

   activationAttributes: An array of one or more attributes that can participate in activation. This is typically an 

    array that contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   Returns: A handle that must be unwrapped to access the newly created instance.

  CreateInstance(type: Type,nonPublic: bool) -> object

  

   Creates an instance of the specified type using that type's default constructor.

  

   type: The type of object to create.

   nonPublic: true if a public or nonpublic default constructor can match; false if only a public default 

    constructor can match.

  

   Returns: A reference to the newly created object.

  CreateInstance(type: Type) -> object

  

   Creates an instance of the specified type using that type's default constructor.

  

   type: The type of object to create.

   Returns: A reference to the newly created object.

  CreateInstance(assemblyName: str,typeName: str) -> ObjectHandle

  

   Creates an instance of the type whose name is specified,using the named assembly and default 

    constructor.

  

  

   assemblyName: The name of the assembly where the type named typeName is sought. If assemblyName is null,the 

    executing assembly is searched.

  

   typeName: The name of the preferred type.

   Returns: A handle that must be unwrapped to access the newly created instance.
  """
  pass
 @staticmethod
 def CreateInstanceFrom(*__args):
  """
  CreateInstanceFrom(domain: AppDomain,assemblyFile: str,typeName: str) -> ObjectHandle

  

   Creates an instance of the type whose name is specified in the specified remote domain,using 

    the named assembly file and default constructor.

  

  

   domain: The remote domain where the type named typeName is created.

   assemblyFile: The name of a file that contains an assembly where the type named typeName is sought.

   typeName: The name of the preferred type.

   Returns: A handle that must be unwrapped to access the newly created instance.

  CreateInstanceFrom(domain: AppDomain,assemblyFile: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object],securityAttributes: Evidence) -> ObjectHandle

  

   Creates an instance of the type whose name is specified in the specified remote domain,using 

    the named assembly file and the constructor that best matches the specified parameters.

  

  

   domain: The remote domain where the type named typeName is created.

   assemblyFile: The name of a file that contains an assembly where the type named typeName is sought.

   typeName: The name of the preferred type.

   ignoreCase: true to specify that the search for typeName is not case-sensitive; false to specify that the 

    search is case-sensitive.

  

   bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If 

    bindingAttr is zero,a case-sensitive search for public constructors is conducted.

  

   binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If 

    binder is null,the default binder is used.

  

   args: An array of arguments that match in number,order,and type the parameters of the constructor to 

    invoke. If args is an empty array or null,the constructor that takes no parameters (the default 

    constructor) is invoked.

  

   culture: Culture-specific information that governs the coercion of args to the formal types declared for 

    the typeName constructor. If culture is null,the System.Globalization.CultureInfo for the 

    current thread is used.

  

   activationAttributes: An array of one or more attributes that can participate in activation. This is typically an 

    array that contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   securityAttributes: Information used to make security policy decisions and grant code permissions.

   Returns: A handle that must be unwrapped to access the newly created instance.

  CreateInstanceFrom(domain: AppDomain,assemblyFile: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object]) -> ObjectHandle

  

   Creates an instance of the type whose name is specified in the specified remote domain,using 

    the named assembly file and the constructor that best matches the specified parameters.

  

  

   domain: The remote domain where the type named typeName is created.

   assemblyFile: The name of a file that contains an assembly where the type named typeName is sought.

   typeName: The name of the preferred type.

   ignoreCase: true to specify that the search for typeName is not case-sensitive; false to specify that the 

    search is case-sensitive.

  

   bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If 

    bindingAttr is zero,a case-sensitive search for public constructors is conducted.

  

   binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If 

    binder is null,the default binder is used.

  

   args: An array of arguments that match in number,order,and type the parameters of the constructor to 

    invoke. If args is an empty array or null,the constructor that takes no parameters (the default 

    constructor) is invoked.

  

   culture: Culture-specific information that governs the coercion of args to the formal types declared for 

    the typeName constructor. If culture is null,the System.Globalization.CultureInfo for the 

    current thread is used.

  

   activationAttributes: An array of one or more attributes that can participate in activation. This is typically an 

    array that contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   Returns: A handle that must be unwrapped to access the newly created instance.

  CreateInstanceFrom(assemblyFile: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object]) -> ObjectHandle

  

   Creates an instance of the type whose name is specified,using the named assembly file and the 

    constructor that best matches the specified parameters.

  

  

   assemblyFile: The name of a file that contains an assembly where the type named typeName is sought.

   typeName: The name of the preferred type.

   ignoreCase: true to specify that the search for typeName is not case-sensitive; false to specify that the 

    search is case-sensitive.

  

   bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If 

    bindingAttr is zero,a case-sensitive search for public constructors is conducted.

  

   binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If 

    binder is null,the default binder is used.

  

   args: An array of arguments that match in number,order,and type the parameters of the constructor to 

    invoke. If args is an empty array or null,the constructor that takes no parameters (the default 

    constructor) is invoked.

  

   culture: Culture-specific information that governs the coercion of args to the formal types declared for 

    the typeName constructor. If culture is null,the System.Globalization.CultureInfo for the 

    current thread is used.

  

   activationAttributes: An array of one or more attributes that can participate in activation. This is typically an 

    array that contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   Returns: A handle that must be unwrapped to access the newly created instance.

  CreateInstanceFrom(assemblyFile: str,typeName: str) -> ObjectHandle

  

   Creates an instance of the type whose name is specified,using the named assembly file and 

    default constructor.

  

  

   assemblyFile: The name of a file that contains an assembly where the type named typeName is sought.

   typeName: The name of the preferred type.

   Returns: A handle that must be unwrapped to access the newly created instance.

  CreateInstanceFrom(assemblyFile: str,typeName: str,activationAttributes: Array[object]) -> ObjectHandle

  

   Creates an instance of the type whose name is specified,using the named assembly file and 

    default constructor.

  

  

   assemblyFile: The name of a file that contains an assembly where the type named typeName is sought.

   typeName: The name of the preferred type.

   activationAttributes: An array of one or more attributes that can participate in activation. This is typically an 

    array that contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   Returns: A handle that must be unwrapped to access the newly created instance.

  CreateInstanceFrom(assemblyFile: str,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object],securityInfo: Evidence) -> ObjectHandle

  

   Creates an instance of the type whose name is specified,using the named assembly file and the 

    constructor that best matches the specified parameters.

  

  

   assemblyFile: The name of a file that contains an assembly where the type named typeName is sought.

   typeName: The name of the preferred type.

   ignoreCase: true to specify that the search for typeName is not case-sensitive; false to specify that the 

    search is case-sensitive.

  

   bindingAttr: A combination of zero or more bit flags that affect the search for the typeName constructor. If 

    bindingAttr is zero,a case-sensitive search for public constructors is conducted.

  

   binder: An object that uses bindingAttr and args to seek and identify the typeName constructor. If 

    binder is null,the default binder is used.

  

   args: An array of arguments that match in number,order,and type the parameters of the constructor to 

    invoke. If args is an empty array or null,the constructor that takes no parameters (the default 

    constructor) is invoked.

  

   culture: Culture-specific information that governs the coercion of args to the formal types declared for 

    the typeName constructor. If culture is null,the System.Globalization.CultureInfo for the 

    current thread is used.

  

   activationAttributes: An array of one or more attributes that can participate in activation. This is typically an 

    array that contains a single System.Runtime.Remoting.Activation.UrlAttribute object. The 

    System.Runtime.Remoting.Activation.UrlAttribute specifies the URL that is required to activate a 

    remote object.

  

   securityInfo: Information used to make security policy decisions and grant code permissions.

   Returns: A handle that must be unwrapped to access the newly created instance.
  """
  pass
 @staticmethod
 def GetObject(type,url,state=None):
  """
  GetObject(type: Type,url: str,state: object) -> object

  

   Creates a proxy for the well-known object indicated by the specified type,URL,and channel data.

  

   type: The type of the well-known object to which you want to connect.

   url: The URL of the well-known object.

   state: Channel-specific data or null.

   Returns: A proxy that points to an endpoint served by the requested well-known object.

  GetObject(type: Type,url: str) -> object

  

   Creates a proxy for the well-known object indicated by the specified type and URL.

  

   type: The type of the well-known object to which you want to connect.

   url: The URL of the well-known object.

   Returns: A proxy that points to an endpoint served by the requested well-known object.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
