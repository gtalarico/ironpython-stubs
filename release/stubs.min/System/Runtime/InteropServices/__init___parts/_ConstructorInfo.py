class _ConstructorInfo:
 """ Exposes the public members of the System.Reflection.ConstructorInfo class to unmanaged code. """
 def Equals(self,other):
  """
  Equals(self: _ConstructorInfo,other: object) -> bool

  

   Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 

    method.

  

  

   other: The System.Object to compare with the current System.Object.

   Returns: true if the specified System.Object is equal to the current System.Object; otherwise,false.
  """
  pass
 def GetCustomAttributes(self,*__args):
  """
  GetCustomAttributes(self: _ConstructorInfo,inherit: bool) -> Array[object]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MemberInfo.GetCustomAttributes(System.Boolean) method.

  

  

   inherit: Specifies whether to search this member's inheritance chain to find the attributes.

   Returns: An array that contains all the custom attributes,or an array with zero elements if no 

    attributes are defined.

  

  GetCustomAttributes(self: _ConstructorInfo,attributeType: Type,inherit: bool) -> Array[object]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Emit.MethodBuilder.GetCustomAttributes(System.Type,System.Boolean) method.

  

  

   attributeType: The type of attribute to search for. Only attributes that are assignable to this type are 

    returned.

  

   inherit: Specifies whether to search this member's inheritance chain to find the attributes.

   Returns: An array of custom attributes applied to this member,or an array with zero (0) elements if no 

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
 def GetIDsOfNames(self,riid,rgszNames,cNames,lcid,rgDispId):
  """
  GetIDsOfNames(self: _ConstructorInfo,riid: Guid,rgszNames: IntPtr,cNames: UInt32,lcid: UInt32,rgDispId: IntPtr) -> Guid

  

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
 def GetTypeInfo(self,iTInfo,lcid,ppTInfo):
  """
  GetTypeInfo(self: _ConstructorInfo,iTInfo: UInt32,lcid: UInt32,ppTInfo: IntPtr)

   Retrieves the type information for an object,which can then be used to get the type information 

    for an interface.

  

  

   iTInfo: The type information to return.

   lcid: The locale identifier for the type information.

   ppTInfo: Receives a pointer to the requested type information object.
  """
  pass
 def GetTypeInfoCount(self,pcTInfo):
  """
  GetTypeInfoCount(self: _ConstructorInfo) -> UInt32

  

   Retrieves the number of type information interfaces that an object provides (either 0 or 1).
  """
  pass
 def Invoke(self,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr):
  """
  Invoke(self: _ConstructorInfo,dispIdMember: UInt32,riid: Guid,lcid: UInt32,wFlags: Int16,pDispParams: IntPtr,pVarResult: IntPtr,pExcepInfo: IntPtr,puArgErr: IntPtr) -> Guid

  

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
 def Invoke_2(self,obj,invokeAttr,binder,parameters,culture):
  """
  Invoke_2(self: _ConstructorInfo,obj: object,invokeAttr: BindingFlags,binder: Binder,parameters: Array[object],culture: CultureInfo) -> object

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MethodBase.Invoke(System.Object,System.Reflection.BindingFlags,System.Reflectio

    n.Binder,System.Object[],System.Globalization.CultureInfo) method.

  

  

   obj: The instance that created this method.

   invokeAttr: One of the BindingFlags values that specifies the type of binding.

   binder: A Binder that defines a set of properties and enables the binding,coercion of argument types,

    and invocation of members using reflection. If binder is null,then Binder.DefaultBinding is 

    used.

  

   parameters: An array of type Object used to match the number,order,and type of the parameters for this 

    constructor,under the constraints of binder. If this constructor does not require parameters,

    pass an array with zero elements,as in Object[] parameters=new Object[0]. Any object in this 

    array that is not explicitly initialized with a value will contain the default value for that 

    object type. For reference-type elements,this value is null. For value-type elements,this 

    value is 0,0.0,or false,depending on the specific element type.

  

   culture: A System.Globalization.CultureInfo used to govern the coercion of types. If this is null,the 

    System.Globalization.CultureInfo for the current thread is used.

  

   Returns: An instance of the class associated with the constructor.
  """
  pass
 def Invoke_3(self,obj,parameters):
  """
  Invoke_3(self: _ConstructorInfo,obj: object,parameters: Array[object]) -> object

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MethodBase.Invoke(System.Object,System.Object[]) method.

  

  

   obj: The instance that created this method.

   parameters: An argument list for the invoked method or constructor. This is an array of objects with the 

    same number,order,and type as the parameters of the method or constructor to be invoked. If 

    there are no parameters,parameters should be null.If the method or constructor represented by 

    this instance takes a ref parameter (ByRef in Visual Basic),no special attribute is required 

    for that parameter in order to invoke the method or constructor using this function. Any object 

    in this array that is not explicitly initialized with a value will contain the default value for 

    that object type. For reference-type elements,this value is null. For value-type elements,this 

    value is 0,0.0,or false,depending on the specific element type.

  

   Returns: An instance of the class associated with the constructor.
  """
  pass
 def Invoke_4(self,invokeAttr,binder,parameters,culture):
  """
  Invoke_4(self: _ConstructorInfo,invokeAttr: BindingFlags,binder: Binder,parameters: Array[object],culture: CultureInfo) -> object

  

   Provides COM objects with version-independent access to the 

    System.Reflection.ConstructorInfo.Invoke(System.Reflection.BindingFlags,System.Reflection.Binder,

    System.Object[],System.Globalization.CultureInfo) method.

  

  

   invokeAttr: One of the BindingFlags values that specifies the type of binding.

   binder: A Binder that defines a set of properties and enables the binding,coercion of argument types,

    and invocation of members using reflection. If binder is null,then Binder.DefaultBinding is 

    used.

  

   parameters: An array of type Object used to match the number,order,and type of the parameters for this 

    constructor,under the constraints of binder. If this constructor does not require parameters,

    pass an array with zero elements,as in Object[] parameters=new Object[0]. Any object in this 

    array that is not explicitly initialized with a value will contain the default value for that 

    object type. For reference-type elements,this value is null. For value-type elements,this 

    value is 0,0.0,or false,depending on the specific element type.

  

   culture: A System.Globalization.CultureInfo used to govern the coercion of types. If this is null,the 

    System.Globalization.CultureInfo for the current thread is used.

  

   Returns: An instance of the class associated with the constructor.
  """
  pass
 def Invoke_5(self,parameters):
  """
  Invoke_5(self: _ConstructorInfo,parameters: Array[object]) -> object

  

   Provides COM objects with version-independent access to the 

    System.Reflection.ConstructorInfo.Invoke(System.Object[]) method.

  

  

   parameters: An array of values that matches the number,order,and type (under the constraints of the 

    default binder) of the parameters for this constructor. If this constructor takes no parameters,

    then use either an array with zero elements or null,as in Object[] parameters=new Object[0]. 

    Any object in this array that is not explicitly initialized with a value will contain the 

    default value for that object type. For reference-type elements,this value is null. For 

    value-type elements,this value is 0,0.0,or false,depending on the specific element type.

  

   Returns: An instance of the class associated with the constructor.
  """
  pass
 def IsDefined(self,attributeType,inherit):
  """
  IsDefined(self: _ConstructorInfo,attributeType: Type,inherit: bool) -> bool

  

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
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 Attributes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.Attributes property.



Get: Attributes(self: _ConstructorInfo) -> MethodAttributes



"""

 CallingConvention=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.CallingConvention property.



Get: CallingConvention(self: _ConstructorInfo) -> CallingConventions



"""

 DeclaringType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.DeclaringType property.



Get: DeclaringType(self: _ConstructorInfo) -> Type



"""

 IsAbstract=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsAbstract property.



Get: IsAbstract(self: _ConstructorInfo) -> bool



"""

 IsAssembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsAssembly property.



Get: IsAssembly(self: _ConstructorInfo) -> bool



"""

 IsConstructor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsConstructor property.



Get: IsConstructor(self: _ConstructorInfo) -> bool



"""

 IsFamily=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFamily property.



Get: IsFamily(self: _ConstructorInfo) -> bool



"""

 IsFamilyAndAssembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFamilyAndAssembly property.



Get: IsFamilyAndAssembly(self: _ConstructorInfo) -> bool



"""

 IsFamilyOrAssembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFamilyOrAssembly property.



Get: IsFamilyOrAssembly(self: _ConstructorInfo) -> bool



"""

 IsFinal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsFinal property.



Get: IsFinal(self: _ConstructorInfo) -> bool



"""

 IsHideBySig=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsHideBySig property.



Get: IsHideBySig(self: _ConstructorInfo) -> bool



"""

 IsPrivate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsPrivate property.



Get: IsPrivate(self: _ConstructorInfo) -> bool



"""

 IsPublic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsPublic property.



Get: IsPublic(self: _ConstructorInfo) -> bool



"""

 IsSpecialName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsSpecialName property.



Get: IsSpecialName(self: _ConstructorInfo) -> bool



"""

 IsStatic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsStatic property.



Get: IsStatic(self: _ConstructorInfo) -> bool



"""

 IsVirtual=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.IsVirtual property.



Get: IsVirtual(self: _ConstructorInfo) -> bool



"""

 MemberType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.ConstructorInfo.MemberType property.



Get: MemberType(self: _ConstructorInfo) -> MemberTypes



"""

 MethodHandle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MethodBase.MethodHandle property.



Get: MethodHandle(self: _ConstructorInfo) -> RuntimeMethodHandle



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.Name property.



Get: Name(self: _ConstructorInfo) -> str



"""

 ReflectedType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.ReflectedType property.



Get: ReflectedType(self: _ConstructorInfo) -> Type



"""


