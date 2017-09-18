class _Assembly:
 """ Exposes the public members of the System.Reflection.Assembly class to unmanaged code. """
 def CreateInstance(self,typeName,ignoreCase=None,bindingAttr=None,binder=None,args=None,culture=None,activationAttributes=None):
  """
  CreateInstance(self: _Assembly,typeName: str,ignoreCase: bool,bindingAttr: BindingFlags,binder: Binder,args: Array[object],culture: CultureInfo,activationAttributes: Array[object]) -> object

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.CreateInstance(System.String,System.Boolean,System.Reflection.BindingF

    lags,System.Reflection.Binder,System.Object[],System.Globalization.CultureInfo,System.Object[]) 

    method.

  

  

   typeName: The System.Type.FullName of the type to locate.

   ignoreCase: true to ignore the case of the type name; otherwise,false.

   bindingAttr: A bitmask that affects how the search is conducted. The value is a combination of bit flags from 

    System.Reflection.BindingFlags.

  

   binder: An object that enables the binding,coercion of argument types,invocation of members,and 

    retrieval of MemberInfo objects via reflection. If binder is null,the default binder is used.

  

   args: An array of type Object containing the arguments to be passed to the constructor. This array of 

    arguments must match in number,order,and type the parameters of the constructor to be invoked. 

    If the default constructor is desired,args must be an empty array or null.

  

   culture: An instance of CultureInfo used to govern the coercion of types. If this is null,the 

    CultureInfo for the current thread is used. (This is necessary to convert a String that 

    represents 1000 to a Double value,for example,since 1000 is represented differently by 

    different cultures.)

  

   activationAttributes: An array of type Object containing one or more activation attributes that can participate in the 

    activation. An example of an activation attribute is: 

    URLAttribute(http://hostname/appname/objectURI)

  

   Returns: An instance of Object representing the type and matching the specified criteria,or null if 

    typeName is not found.

  

  CreateInstance(self: _Assembly,typeName: str,ignoreCase: bool) -> object

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.CreateInstance(System.String,System.Boolean) method.

  

  

   typeName: The System.Type.FullName of the type to locate.

   ignoreCase: true to ignore the case of the type name; otherwise,false.

   Returns: An instance of System.Object representing the type,with culture,arguments,binder,and 

    activation attributes set to null,and System.Reflection.BindingFlags set to Public or Instance,

    or null if typeName is not found.

  

  CreateInstance(self: _Assembly,typeName: str) -> object

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.CreateInstance(System.String) method.

  

  

   typeName: The System.Type.FullName of the type to locate.

   Returns: An instance of System.Object representing the type,with culture,arguments,binder,and 

    activation attributes set to null,and System.Reflection.BindingFlags set to Public or Instance,

    or null if typeName is not found.
  """
  pass
 def Equals(self,other):
  """
  Equals(self: _Assembly,other: object) -> bool

  

   Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 

    method.

  

  

   other: The System.Object to compare with the current System.Object.

   Returns: true if the specified System.Object is equal to the current System.Object; otherwise,false.
  """
  pass
 def GetCustomAttributes(self,*__args):
  """
  GetCustomAttributes(self: _Assembly,inherit: bool) -> Array[object]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetCustomAttributes(System.Boolean) method.

  

  

   inherit: This argument is ignored for objects of type System.Reflection.Assembly.

   Returns: An array of type Object containing the custom attributes for this assembly.

  GetCustomAttributes(self: _Assembly,attributeType: Type,inherit: bool) -> Array[object]

  

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
 def GetFile(self,name):
  """
  GetFile(self: _Assembly,name: str) -> FileStream

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetFile(System.String) method.

  

  

   name: The name of the specified file. Do not include the path to the file.

   Returns: A System.IO.FileStream for the specified file,or null if the file is not found.
  """
  pass
 def GetFiles(self,getResourceModules=None):
  """
  GetFiles(self: _Assembly,getResourceModules: bool) -> Array[FileStream]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetFiles(System.Boolean) method.

  

  

   getResourceModules: true to include resource modules; otherwise,false.

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
 def GetLoadedModules(self,getResourceModules=None):
  """
  GetLoadedModules(self: _Assembly,getResourceModules: bool) -> Array[Module]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetLoadedModules(System.Boolean) method.

  

  

   getResourceModules: true to include resource modules; otherwise,false.

   Returns: An array of modules.

  GetLoadedModules(self: _Assembly) -> Array[Module]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetLoadedModules method.

  

   Returns: An array of modules.
  """
  pass
 def GetManifestResourceInfo(self,resourceName):
  """
  GetManifestResourceInfo(self: _Assembly,resourceName: str) -> ManifestResourceInfo

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetManifestResourceInfo(System.String) method.

  

  

   resourceName: The case-sensitive name of the resource.

   Returns: A System.Reflection.ManifestResourceInfo object populated with information about the resource's 

    topology,or null if the resource is not found.
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
 def GetManifestResourceStream(self,*__args):
  """
  GetManifestResourceStream(self: _Assembly,name: str) -> Stream

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetManifestResourceStream(System.String) method.

  

  

   name: The case-sensitive name of the manifest resource being requested.

   Returns: A System.IO.Stream representing this manifest resource.

  GetManifestResourceStream(self: _Assembly,type: Type,name: str) -> Stream

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetManifestResourceStream(System.Type,System.String) method.

  

  

   type: The type whose namespace is used to scope the manifest resource name.

   name: The case-sensitive name of the manifest resource being requested.

   Returns: A System.IO.Stream representing this manifest resource.
  """
  pass
 def GetModule(self,name):
  """
  GetModule(self: _Assembly,name: str) -> Module

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetModule(System.String) method.

  

  

   name: The name of the module being requested.

   Returns: The module being requested,or null if the module is not found.
  """
  pass
 def GetModules(self,getResourceModules=None):
  """
  GetModules(self: _Assembly,getResourceModules: bool) -> Array[Module]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetModules(System.Boolean) method.

  

  

   getResourceModules: true to include resource modules; otherwise,false.

   Returns: An array of modules.

  GetModules(self: _Assembly) -> Array[Module]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetModules method.

  

   Returns: An array of modules.
  """
  pass
 def GetName(self,copiedName=None):
  """
  GetName(self: _Assembly,copiedName: bool) -> AssemblyName

  

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
 def GetObjectData(self,info,context):
  """
  GetObjectData(self: _Assembly,info: SerializationInfo,context: StreamingContext)

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
 def GetSatelliteAssembly(self,culture,version=None):
  """
  GetSatelliteAssembly(self: _Assembly,culture: CultureInfo,version: Version) -> Assembly

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetSatelliteAssembly(System.Globalization.CultureInfo,System.Version) 

    method.

  

  

   culture: The specified culture.

   version: The version of the satellite assembly.

   Returns: The specified satellite assembly.

  GetSatelliteAssembly(self: _Assembly,culture: CultureInfo) -> Assembly

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetSatelliteAssembly(System.Globalization.CultureInfo) method.

  

  

   culture: The specified culture.

   Returns: The specified satellite assembly.
  """
  pass
 def GetType(self,name=None,throwOnError=None,ignoreCase=None):
  """
  GetType(self: _Assembly,name: str,throwOnError: bool) -> Type

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetType(System.String,System.Boolean) method.

  

  

   name: The full name of the type.

   throwOnError: true to throw an exception if the type is not found; false to return null.

   Returns: A System.Type object that represents the specified class.

  GetType(self: _Assembly,name: str,throwOnError: bool,ignoreCase: bool) -> Type

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetType(System.String,System.Boolean,System.Boolean) method.

  

  

   name: The full name of the type.

   throwOnError: true to throw an exception if the type is not found; false to return null.

   ignoreCase: true to ignore the case of the type name; otherwise,false.

   Returns: A System.Type object that represents the specified class.

  GetType(self: _Assembly) -> Type

  

   Provides COM objects with version-independent access to the System.Object.GetType method.

   Returns: A System.Type object.

  GetType(self: _Assembly,name: str) -> Type

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetType(System.String) method.

  

  

   name: The full name of the type.

   Returns: A System.Type object that represents the specified class,or null if the class is not found.
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
 def IsDefined(self,attributeType,inherit):
  """
  IsDefined(self: _Assembly,attributeType: Type,inherit: bool) -> bool

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.IsDefined(System.Type,System.Boolean) method.

  

  

   attributeType: The System.Type of the custom attribute to be checked for this assembly.

   inherit: This argument is ignored for objects of this type.

   Returns: true if a custom attribute identified by the specified System.Type is defined; otherwise,false.
  """
  pass
 def LoadModule(self,moduleName,rawModule,rawSymbolStore=None):
  """
  LoadModule(self: _Assembly,moduleName: str,rawModule: Array[Byte],rawSymbolStore: Array[Byte]) -> Module

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.LoadModule(System.String,System.Byte[],System.Byte[]) method.

  

  

   moduleName: Name of the module. Must correspond to a file name in this assembly's manifest.

   rawModule: A byte array that is a COFF-based image containing an emitted module,or a resource.

   rawSymbolStore: A byte array containing the raw bytes representing the symbols for the module. Must be null if 

    this is a resource file.

  

   Returns: The loaded module.

  LoadModule(self: _Assembly,moduleName: str,rawModule: Array[Byte]) -> Module

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.LoadModule(System.String,System.Byte[]) method.

  

  

   moduleName: Name of the module. Must correspond to a file name in this assembly's manifest.

   rawModule: A byte array that is a COFF-based image containing an emitted module,or a resource.

   Returns: The loaded Module.
  """
  pass
 def ToString(self):
  """
  ToString(self: _Assembly) -> str

  

   Provides COM objects with version-independent access to the System.Reflection.Assembly.ToString 

    method.

  

   Returns: The full name of the assembly,or the class name if the full name of the assembly cannot be 

    determined.
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
 CodeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.Assembly.CodeBase property.



Get: CodeBase(self: _Assembly) -> str



"""

 EntryPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.Assembly.EntryPoint property.



Get: EntryPoint(self: _Assembly) -> MethodInfo



"""

 EscapedCodeBase=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.Assembly.EscapedCodeBase property.



Get: EscapedCodeBase(self: _Assembly) -> str



"""

 Evidence=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.Assembly.Evidence property.



Get: Evidence(self: _Assembly) -> Evidence



"""

 FullName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.Assembly.FullName property.



Get: FullName(self: _Assembly) -> str



"""

 GlobalAssemblyCache=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.Assembly.GlobalAssemblyCache property.



Get: GlobalAssemblyCache(self: _Assembly) -> bool



"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.Assembly.Location property.



Get: Location(self: _Assembly) -> str



"""


 ModuleResolve=None

