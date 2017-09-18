class TypeDescriptionProvider(object):
 """ Provides supplemental metadata to the System.ComponentModel.TypeDescriptor. """
 def CreateInstance(self,provider,objectType,argTypes,args):
  """
  CreateInstance(self: TypeDescriptionProvider,provider: IServiceProvider,objectType: Type,argTypes: Array[Type],args: Array[object]) -> object

  

   Creates an object that can substitute for another data type.

  

   provider: An optional service provider.

   objectType: The type of object to create. This parameter is never null.

   argTypes: An optional array of types that represent the parameter types to be passed to the object's 

    constructor. This array can be null or of zero length.

  

   args: An optional array of parameter values to pass to the object's constructor.

   Returns: The substitute System.Object.
  """
  pass
 def GetCache(self,instance):
  """
  GetCache(self: TypeDescriptionProvider,instance: object) -> IDictionary

  

   Gets a per-object cache,accessed as an System.Collections.IDictionary of key/value pairs.

  

   instance: The object for which to get the cache.

   Returns: An System.Collections.IDictionary if the provided object supports caching; otherwise,null.
  """
  pass
 def GetExtendedTypeDescriptor(self,instance):
  """
  GetExtendedTypeDescriptor(self: TypeDescriptionProvider,instance: object) -> ICustomTypeDescriptor

  

   Gets an extended custom type descriptor for the given object.

  

   instance: The object for which to get the extended type descriptor.

   Returns: An System.ComponentModel.ICustomTypeDescriptor that can provide extended metadata for the object.
  """
  pass
 def GetExtenderProviders(self,*args):
  """
  GetExtenderProviders(self: TypeDescriptionProvider,instance: object) -> Array[IExtenderProvider]

  

   Gets the extender providers for the specified object.

  

   instance: The object to get extender providers for.

   Returns: An array of extender providers for instance.
  """
  pass
 def GetFullComponentName(self,component):
  """
  GetFullComponentName(self: TypeDescriptionProvider,component: object) -> str

  

   Gets the name of the specified component,or null if the component has no name.

  

   component: The specified component.

   Returns: The name of the specified component.
  """
  pass
 def GetReflectionType(self,*__args):
  """
  GetReflectionType(self: TypeDescriptionProvider,objectType: Type,instance: object) -> Type

  

   Performs normal reflection against the given object with the given type.

  

   objectType: The type of object for which to retrieve the System.Reflection.IReflect.

   instance: An instance of the type. Can be null.

   Returns: A System.Type.

  GetReflectionType(self: TypeDescriptionProvider,instance: object) -> Type

  

   Performs normal reflection against the given object.

  

   instance: An instance of the type (should not be null).

   Returns: A System.Type.

  GetReflectionType(self: TypeDescriptionProvider,objectType: Type) -> Type

  

   Performs normal reflection against a type.

  

   objectType: The type of object for which to retrieve the System.Reflection.IReflect.

   Returns: A System.Type.
  """
  pass
 def GetRuntimeType(self,reflectionType):
  """
  GetRuntimeType(self: TypeDescriptionProvider,reflectionType: Type) -> Type

  

   Converts a reflection type into a runtime type.

  

   reflectionType: The type to convert to its runtime equivalent.

   Returns: A System.Type that represents the runtime equivalent of reflectionType.
  """
  pass
 def GetTypeDescriptor(self,*__args):
  """
  GetTypeDescriptor(self: TypeDescriptionProvider,objectType: Type,instance: object) -> ICustomTypeDescriptor

  

   Gets a custom type descriptor for the given type and object.

  

   objectType: The type of object for which to retrieve the type descriptor.

   instance: An instance of the type. Can be null if no instance was passed to the 

    System.ComponentModel.TypeDescriptor.

  

   Returns: An System.ComponentModel.ICustomTypeDescriptor that can provide metadata for the type.

  GetTypeDescriptor(self: TypeDescriptionProvider,instance: object) -> ICustomTypeDescriptor

  

   Gets a custom type descriptor for the given object.

  

   instance: An instance of the type. Can be null if no instance was passed to the 

    System.ComponentModel.TypeDescriptor.

  

   Returns: An System.ComponentModel.ICustomTypeDescriptor that can provide metadata for the type.

  GetTypeDescriptor(self: TypeDescriptionProvider,objectType: Type) -> ICustomTypeDescriptor

  

   Gets a custom type descriptor for the given type.

  

   objectType: The type of object for which to retrieve the type descriptor.

   Returns: An System.ComponentModel.ICustomTypeDescriptor that can provide metadata for the type.
  """
  pass
 def IsSupportedType(self,type):
  """
  IsSupportedType(self: TypeDescriptionProvider,type: Type) -> bool

  

   Gets a value that indicates whether the specified type is compatible with the type description 

    and its chain of type description providers.

  

  

   type: The type to test for compatibility.

   Returns: true if type is compatible with the type description and its chain of type description 

    providers; otherwise,false.
  """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type)

  __new__(cls: type,parent: TypeDescriptionProvider)
  """
  pass
