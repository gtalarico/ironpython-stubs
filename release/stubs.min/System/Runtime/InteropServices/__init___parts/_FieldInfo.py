class _FieldInfo:
 """ Exposes the public members of the System.Reflection.FieldInfo class to unmanaged code. """
 def Equals(self,other):
  """
  Equals(self: _FieldInfo,other: object) -> bool

  

   Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 

    method.

  

  

   other: The System.Object to compare with the current System.Object.

   Returns: true if the specified System.Object is equal to the current System.Object; otherwise,false.
  """
  pass
 def GetCustomAttributes(self,*__args):
  """
  GetCustomAttributes(self: _FieldInfo,inherit: bool) -> Array[object]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MemberInfo.GetCustomAttributes(System.Boolean) method.

  

  

   inherit: Specifies whether to search this member's inheritance chain to find the attributes.

   Returns: An array that contains all the custom attributes,or an array with zero elements if no 

    attributes are defined.

  

  GetCustomAttributes(self: _FieldInfo,attributeType: Type,inherit: bool) -> Array[object]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MemberInfo.GetCustomAttributes(System.Type,System.Boolean) method.

  

  

   attributeType: The type of attribute to search for. Only attributes that are assignable to this type are 

    returned.

  

   inherit: Specifies whether to search this member's inheritance chain to find the attributes.

   Returns: An array of custom attributes applied to this member,or an array with zero (0) elements if no 

    attributes have been applied.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: _FieldInfo) -> int

  

   Provides COM objects with version-independent access to the System.Object.GetHashCode method.

   Returns: The hash code for the current instance.
  """
  pass
 def GetIDsOfNames(self,riid,rgszNames,cNames,lcid,rgDispId):
  """
  GetIDsOfNames(self: _FieldInfo,riid: Guid,rgszNames: IntPtr,cNames: UInt32,lcid: UInt32,rgDispId: IntPtr) -> Guid

  

   Maps a set of names to a corresponding set of dispatch identifiers.

  

   riid: Reserved for future use. Must be IID_NULL.

   rgszNames: Passed-in array of names to be mapped.

   cNames: Count of the names to be mapped.

   lcid: The locale context in which to interpret the names.

   rgDispId: Caller-allocated array that receives the IDs corresponding to the names.
  """
  pass
 def GetType(self):
  """
  GetType(self: _FieldInfo) -> Type

  

   Provides COM objects with version-independent access to the System.Object.GetType method.

   Returns: A System.Type object.
  """
  pass
 def GetTypeInfo(self,iTInfo,lcid,ppTInfo):
  """
  GetTypeInfo(self: _FieldInfo,iTInfo: UInt32,lcid: UInt32,ppTInfo: IntPtr)

   Retrieves the type information for an object,which can then be used to get the type information 

    for an interface.

  

  

   iTInfo: The type information to return.

   lcid: The locale identifier for the type information.

   ppTInfo: Receives a pointer to the requested type information object.
  """
  pass
 def GetTypeInfoCount(self,pcTInfo):
  """
  GetTypeInfoCount(self: _FieldInfo) -> UInt32

  

   Retrieves the number of type information interfaces that an object provides (either 0 or 1).
  """
  pass
 def GetValue(self,obj):
  """
  GetValue(self: _FieldInfo,obj: object) -> object

  

   Provides COM objects with version-independent access to the 

    System.Reflection.FieldInfo.GetValue(System.Object) method.

  

  

   obj: The object whose field value will be returned.

   Returns: An object containing the value of the field reflected by this instance.
  """
  pass
 def GetValueDirect(self,obj):
  """
  GetValueDirect(self: _FieldInfo,obj: TypedReference) -> object

  

   Provides COM objects with version-independent access to the 

    System.Reflection.FieldInfo.GetValueDirect(System.TypedReference) method.

  

  

   obj: A System.TypedReference structure that encapsulates a managed pointer to a location and a 

    runtime representation of the type that might be stored at that location.

  

   Returns: An System.Object containing a field value.
  """
  pass
 def Invoke(self,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr):
  """
  Invoke(self: _FieldInfo,dispIdMember: UInt32,riid: Guid,lcid: UInt32,wFlags: Int16,pDispParams: IntPtr,pVarResult: IntPtr,pExcepInfo: IntPtr,puArgErr: IntPtr) -> Guid

  

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
 def IsDefined(self,attributeType,inherit):
  """
  IsDefined(self: _FieldInfo,attributeType: Type,inherit: bool) -> bool

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MemberInfo.IsDefined(System.Type,System.Boolean) method.

  

  

   attributeType: The System.Type object to which the custom attributes are applied.

   inherit: Specifies whether to search this member's inheritance chain to find the attributes.

   Returns: true if one or more instance of attributeType is applied to this member; otherwise,false.
  """
  pass
 def SetValue(self,obj,value,invokeAttr=None,binder=None,culture=None):
  """
  SetValue(self: _FieldInfo,obj: object,value: object)

   Provides COM objects with version-independent access to the 

    System.Reflection.FieldInfo.SetValue(System.Object,System.Object) method.

  

  

   obj: The object whose field value will be set.

   value: The value to assign to the field.

  SetValue(self: _FieldInfo,obj: object,value: object,invokeAttr: BindingFlags,binder: Binder,culture: CultureInfo)

   Provides COM objects with version-independent access to the 

    System.Reflection.PropertyInfo.SetValue(System.Object,System.Object,System.Reflection.BindingFlag

    s,System.Reflection.Binder,System.Object[],System.Globalization.CultureInfo) method.

  

  

   obj: The object whose field value will be set.

   value: The value to assign to the field.

   invokeAttr: A field of System.Reflection.Binder that specifies the type of binding that is desired (for 

    example,Binder.CreateInstance or Binder.ExactBinding).

  

   binder: A set of properties that enables the binding,coercion of argument types,and invocation of 

    members through reflection. If binder is null,then Binder.DefaultBinding is used.

  

   culture: The software preferences of a particular culture.
  """
  pass
 def SetValueDirect(self,obj,value):
  """
  SetValueDirect(self: _FieldInfo,obj: TypedReference,value: object)

   Provides COM objects with version-independent access to the 

    System.Reflection.FieldInfo.SetValueDirect(System.TypedReference,System.Object) method.

  

  

   obj: The object whose field value will be set.

   value: The value to assign to the field.
  """
  pass
 def ToString(self):
  """
  ToString(self: _FieldInfo) -> str

  

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
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.Attributes property.



Get: Attributes(self: _FieldInfo) -> FieldAttributes



"""

 DeclaringType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.DeclaringType property.



Get: DeclaringType(self: _FieldInfo) -> Type



"""

 FieldHandle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.FieldHandle property.



Get: FieldHandle(self: _FieldInfo) -> RuntimeFieldHandle



"""

 FieldType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.FieldType property.



Get: FieldType(self: _FieldInfo) -> Type



"""

 IsAssembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsAssembly property.



Get: IsAssembly(self: _FieldInfo) -> bool



"""

 IsFamily=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsFamily property.



Get: IsFamily(self: _FieldInfo) -> bool



"""

 IsFamilyAndAssembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsFamilyAndAssembly property.



Get: IsFamilyAndAssembly(self: _FieldInfo) -> bool



"""

 IsFamilyOrAssembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsFamilyOrAssembly property.



Get: IsFamilyOrAssembly(self: _FieldInfo) -> bool



"""

 IsInitOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsInitOnly property.



Get: IsInitOnly(self: _FieldInfo) -> bool



"""

 IsLiteral=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsLiteral property.



Get: IsLiteral(self: _FieldInfo) -> bool



"""

 IsNotSerialized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsNotSerialized property.



Get: IsNotSerialized(self: _FieldInfo) -> bool



"""

 IsPinvokeImpl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsPinvokeImpl property.



Get: IsPinvokeImpl(self: _FieldInfo) -> bool



"""

 IsPrivate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsPrivate property.



Get: IsPrivate(self: _FieldInfo) -> bool



"""

 IsPublic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsPublic property.



Get: IsPublic(self: _FieldInfo) -> bool



"""

 IsSpecialName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsSpecialName property.



Get: IsSpecialName(self: _FieldInfo) -> bool



"""

 IsStatic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.IsStatic property.



Get: IsStatic(self: _FieldInfo) -> bool



"""

 MemberType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.FieldInfo.MemberType property.



Get: MemberType(self: _FieldInfo) -> MemberTypes



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.Name property.



Get: Name(self: _FieldInfo) -> str



"""

 ReflectedType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.ReflectedType property.



Get: ReflectedType(self: _FieldInfo) -> Type



"""


