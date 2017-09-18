class _MemberInfo:
 """ Exposes the public members of the System.Reflection.MemberInfo class to unmanaged code. """
 def Equals(self,other):
  """
  Equals(self: _MemberInfo,other: object) -> bool

  

   Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 

    method.

  

  

   other: The System.Object to compare with the current System.Object.

   Returns: true if the specified System.Object is equal to the current System.Object; otherwise,false.
  """
  pass
 def GetCustomAttributes(self,*__args):
  """
  GetCustomAttributes(self: _MemberInfo,inherit: bool) -> Array[object]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MemberInfo.GetCustomAttributes(System.Boolean) method.

  

  

   inherit: true to search this member's inheritance chain to find the attributes; otherwise,false.

   Returns: An array that contains all the custom attributes,or an array with zero (0) elements if no 

    attributes are defined.

  

  GetCustomAttributes(self: _MemberInfo,attributeType: Type,inherit: bool) -> Array[object]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetCustomAttributes(System.Type,System.Boolean) method.

  

  

   attributeType: The type of attribute to search for. Only attributes that are assignable to this type are 

    returned.

  

   inherit: true to search this member's inheritance chain to find the attributes; otherwise,false.

   Returns: An array of custom attributes applied to this member,or an array with zero (0) elements if no 

    attributes have been applied.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: _MemberInfo) -> int

  

   Provides COM objects with version-independent access to the System.Object.GetHashCode method.

   Returns: The hash code for the current instance.
  """
  pass
 def GetIDsOfNames(self,riid,rgszNames,cNames,lcid,rgDispId):
  """
  GetIDsOfNames(self: _MemberInfo,riid: Guid,rgszNames: IntPtr,cNames: UInt32,lcid: UInt32,rgDispId: IntPtr) -> Guid

  

   Maps a set of names to a corresponding set of dispatch identifiers.

  

   riid: Reserved for future use. Must be IID_NULL.

   rgszNames: An  array of names to be mapped.

   cNames: The count of the names to be mapped.

   lcid: The locale context in which to interpret the names.

   rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
  """
  pass
 def GetType(self):
  """
  GetType(self: _MemberInfo) -> Type

  

   Provides COM objects with version-independent access to the System.Type.GetType method.

   Returns: A System.Type object.
  """
  pass
 def GetTypeInfo(self,iTInfo,lcid,ppTInfo):
  """
  GetTypeInfo(self: _MemberInfo,iTInfo: UInt32,lcid: UInt32,ppTInfo: IntPtr)

   Retrieves the type information for an object,which can be used to get the type information for 

    an interface.

  

  

   iTInfo: The type information to return.

   lcid: The locale identifier for the type information.

   ppTInfo: A pointer to the requested type information object.
  """
  pass
 def GetTypeInfoCount(self,pcTInfo):
  """
  GetTypeInfoCount(self: _MemberInfo) -> UInt32

  

   Retrieves the number of type information interfaces that an object provides (either 0 or 1).
  """
  pass
 def Invoke(self,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr):
  """
  Invoke(self: _MemberInfo,dispIdMember: UInt32,riid: Guid,lcid: UInt32,wFlags: Int16,pDispParams: IntPtr,pVarResult: IntPtr,pExcepInfo: IntPtr,puArgErr: IntPtr) -> Guid

  

   Provides access to properties and methods exposed by an object.

  

   dispIdMember: An identifier for the member.

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
  IsDefined(self: _MemberInfo,attributeType: Type,inherit: bool) -> bool

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MemberInfo.IsDefined(System.Type,System.Boolean) method.

  

  

   attributeType: The System.Type object to which the custom attributes are applied.

   inherit: true to search this member's inheritance chain to find the attributes; otherwise,false.

   Returns: true if one or more instance of the attributeType parameter is applied to this member; 

    otherwise,false.
  """
  pass
 def ToString(self):
  """
  ToString(self: _MemberInfo) -> str

  

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
 DeclaringType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.DeclaringType property.



Get: DeclaringType(self: _MemberInfo) -> Type



"""

 MemberType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.MemberType property.



Get: MemberType(self: _MemberInfo) -> MemberTypes



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.Name property.



Get: Name(self: _MemberInfo) -> str



"""

 ReflectedType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.ReflectedType property.



Get: ReflectedType(self: _MemberInfo) -> Type



"""


