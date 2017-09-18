class _PropertyInfo:
 """ Exposes the public members of the System.Reflection.PropertyInfo class to unmanaged code. """
 def Equals(self,other):
  """
  Equals(self: _PropertyInfo,other: object) -> bool

  

   Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 

    method.

  

  

   other: The System.Object to compare with the current System.Object.

   Returns: true if the specified System.Object is equal to the current System.Object; otherwise,false.
  """
  pass
 def GetAccessors(self,nonPublic=None):
  """
  GetAccessors(self: _PropertyInfo) -> Array[MethodInfo]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.PropertyInfo.GetAccessors method.

  

   Returns: An array of System.Reflection.MethodInfo objects that reflect the public get,set,and other 

    accessors of the property reflected by the current instance,if accessors are found; otherwise,

    this method returns an array with zero (0) elements.

  

  GetAccessors(self: _PropertyInfo,nonPublic: bool) -> Array[MethodInfo]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.PropertyInfo.GetAccessors(System.Boolean) method.

  

  

   nonPublic: true to include non-public methods in the returned MethodInfo array; otherwise,false.

   Returns: An array of System.Reflection.MethodInfo objects whose elements reflect the get,set,and other 

    accessors of the property reflected by the current instance. If the nonPublic parameter is true,

    this array contains public and non-public get,set,and other accessors. If nonPublic is false,

    this array contains only public get,set,and other accessors. If no accessors with the 

    specified visibility are found,this method returns an array with zero (0) elements.
  """
  pass
 def GetCustomAttributes(self,*__args):
  """
  GetCustomAttributes(self: _PropertyInfo,inherit: bool) -> Array[object]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MemberInfo.GetCustomAttributes(System.Boolean) method.

  

  

   inherit: true to search this member's inheritance chain to find the attributes; otherwise false.

   Returns: An array that contains all the custom attributes,or an array with zero elements if no 

    attributes are defined.

  

  GetCustomAttributes(self: _PropertyInfo,attributeType: Type,inherit: bool) -> Array[object]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MemberInfo.GetCustomAttributes(System.Type,System.Boolean) method.

  

  

   attributeType: The type of attribute to search for. Only attributes that are assignable to this type are 

    returned.

  

   inherit: true to search this member's inheritance chain to find the attributes; otherwise false.

   Returns: An array of custom attributes applied to this member,or an array with zero (0) elements if no 

    attributes have been applied.
  """
  pass
 def GetGetMethod(self,nonPublic=None):
  """
  GetGetMethod(self: _PropertyInfo) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Reflection.PropertyInfo.GetGetMethod method.

  

   Returns: A System.Reflection.MethodInfo object representing the public get accessor for this property,or 

    null if the get accessor is non-public or does not exist.

  

  GetGetMethod(self: _PropertyInfo,nonPublic: bool) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Reflection.PropertyInfo.GetGetMethod(System.Boolean) method.

  

  

   nonPublic: true to return a non-public get accessor; otherwise,false.

   Returns: A System.Reflection.MethodInfo object representing the get accessor for this property,if the 

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
 def GetIDsOfNames(self,riid,rgszNames,cNames,lcid,rgDispId):
  """
  GetIDsOfNames(self: _PropertyInfo,riid: Guid,rgszNames: IntPtr,cNames: UInt32,lcid: UInt32,rgDispId: IntPtr) -> Guid

  

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
 def GetSetMethod(self,nonPublic=None):
  """
  GetSetMethod(self: _PropertyInfo) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Reflection.PropertyInfo.GetSetMethod method.

  

   Returns: The System.Reflection.MethodInfo object representing the Set method for this property if the set 

    accessor is public,or null if the set accessor is not public.

  

  GetSetMethod(self: _PropertyInfo,nonPublic: bool) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Reflection.PropertyInfo.GetSetMethod(System.Boolean) method.

  

  

   nonPublic: true to return a non-public accessor; otherwise,false.

   Returns: One of the values in the following table.Value Meaning A System.Reflection.MethodInfo object 

    representing the Set method for this property. The set accessor is public.-or- The nonPublic 

    parameter is true and the set accessor is non-public. nullThe nonPublic parameter is true,but 

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
 def GetTypeInfo(self,iTInfo,lcid,ppTInfo):
  """
  GetTypeInfo(self: _PropertyInfo,iTInfo: UInt32,lcid: UInt32,ppTInfo: IntPtr)

   Retrieves the type information for an object,which can be used to get the type information for 

    an interface.

  

  

   iTInfo: The type information to return.

   lcid: The locale identifier for the type information.

   ppTInfo: A pointer to the requested type information object.
  """
  pass
 def GetTypeInfoCount(self,pcTInfo):
  """
  GetTypeInfoCount(self: _PropertyInfo) -> UInt32

  

   Retrieves the number of type information interfaces that an object provides (either 0 or 1).
  """
  pass
 def GetValue(self,obj,*__args):
  """
  GetValue(self: _PropertyInfo,obj: object,invokeAttr: BindingFlags,binder: Binder,index: Array[object],culture: CultureInfo) -> object

  

   Provides COM objects with version-independent access to the 

    System.Reflection.PropertyInfo.GetValue(System.Object,System.Reflection.BindingFlags,System.Refle

    ction.Binder,System.Object[],System.Globalization.CultureInfo) method.

  

  

   obj: The object whose property value will be returned.

   invokeAttr: The invocation attribute. This must be a bit flag from BindingFlags: InvokeMethod,

    CreateInstance,Static,GetField,SetField,GetProperty,or SetProperty. A suitable invocation 

    attribute must be specified. If a static member will be invoked,the Static flag of BindingFlags 

    must be set.

  

   binder: An object that enables the binding,coercion of argument types,invocation of members,and 

    retrieval of MemberInfo objects through reflection. If binder is null,the default binder is 

    used.

  

   index: Optional index values for indexed properties. This value should be null for non-indexed 

    properties.

  

   culture: The CultureInfo object that represents the culture for which the resource will be localized. 

    Note that if the resource is not localized for this culture,the CultureInfo.Parent method will 

    be called successively in search of a match. If this value is null,the CultureInfo is obtained 

    from the CultureInfo.CurrentUICulture property.

  

   Returns: The property value for the obj parameter.

  GetValue(self: _PropertyInfo,obj: object,index: Array[object]) -> object

  

   Provides COM objects with version-independent access to the 

    System.Reflection.PropertyInfo.GetValue(System.Object,System.Object[]) method.

  

  

   obj: The object whose property value will be returned.

   index: Optional index values for indexed properties. This value should be null for non-indexed 

    properties.

  

   Returns: The property value for the obj parameter.
  """
  pass
 def Invoke(self,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr):
  """
  Invoke(self: _PropertyInfo,dispIdMember: UInt32,riid: Guid,lcid: UInt32,wFlags: Int16,pDispParams: IntPtr,pVarResult: IntPtr,pExcepInfo: IntPtr,puArgErr: IntPtr) -> Guid

  

   Provides access to properties and methods exposed by an object.

  

   dispIdMember: An identifier of a member.

   riid: Reserved for future use. Must be IID_NULL.

   lcid: The locale context in which to interpret arguments.

   wFlags: Flags describing the context of the call.

   pDispParams: A pointer to a structure containing an array of arguments,an array of argument DISPIDs for 

    named arguments,and counts for the number of elements in the arrays.

  

   pVarResult: A pointer to the location where the result will be stored.

   pExcepInfo: A pointer to a structure that contains exception information.

   puArgErr: The index of the first argument that has an error.
  """
  pass
 def IsDefined(self,attributeType,inherit):
  """
  IsDefined(self: _PropertyInfo,attributeType: Type,inherit: bool) -> bool

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MemberInfo.IsDefined(System.Type,System.Boolean) method.

  

  

   attributeType: The System.Type object to which the custom attributes are applied.

   inherit: true to search this member's inheritance chain to find the attributes; otherwise false.

   Returns: true if one or more instances of the attributeType parameter are applied to this member; 

    otherwise,false.
  """
  pass
 def SetValue(self,obj,value,*__args):
  """
  SetValue(self: _PropertyInfo,obj: object,value: object,invokeAttr: BindingFlags,binder: Binder,index: Array[object],culture: CultureInfo)

   Provides COM objects with version-independent access to the 

    System.Reflection.FieldInfo.SetValue(System.Object,System.Object,System.Reflection.BindingFlags,S

    ystem.Reflection.Binder,System.Globalization.CultureInfo) method.

  

  

   obj: The object whose property value will be returned.

   value: The new value for this property.

   invokeAttr: The invocation attribute. This must be a bit flag from System.Reflection.BindingFlags: 

    InvokeMethod,CreateInstance,Static,GetField,SetField,GetProperty,or SetProperty. A 

    suitable invocation attribute must be specified. If a static member will be invoked,the Static 

    flag of BindingFlags must be set.

  

   binder: An object that enables the binding,coercion of argument types,invocation of members,and 

    retrieval of System.Reflection.MemberInfo objects through reflection. If binder is null,the 

    default binder is used.

  

   index: Optional index values for indexed properties. This value should be null for non-indexed 

    properties.

  

   culture: The System.Globalization.CultureInfo object that represents the culture for which the resource 

    will be localized. Note that if the resource is not localized for this culture,the 

    CultureInfo.Parent method will be called successively in search of a match. If this value is 

    null,the CultureInfo is obtained from the CultureInfo.CurrentUICulture property.

  

  SetValue(self: _PropertyInfo,obj: object,value: object,index: Array[object])

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
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 Attributes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.PropertyInfo.Attributes property.



Get: Attributes(self: _PropertyInfo) -> PropertyAttributes



"""

 CanRead=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.PropertyInfo.CanRead property.



Get: CanRead(self: _PropertyInfo) -> bool



"""

 CanWrite=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.PropertyInfo.CanWrite property.



Get: CanWrite(self: _PropertyInfo) -> bool



"""

 DeclaringType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.DeclaringType property.



Get: DeclaringType(self: _PropertyInfo) -> Type



"""

 IsSpecialName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.PropertyInfo.IsSpecialName property.



Get: IsSpecialName(self: _PropertyInfo) -> bool



"""

 MemberType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.PropertyInfo.MemberType property.



Get: MemberType(self: _PropertyInfo) -> MemberTypes



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.Name property.



Get: Name(self: _PropertyInfo) -> str



"""

 PropertyType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.PropertyInfo.PropertyType property.



Get: PropertyType(self: _PropertyInfo) -> Type



"""

 ReflectedType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.ReflectedType property.



Get: ReflectedType(self: _PropertyInfo) -> Type



"""


