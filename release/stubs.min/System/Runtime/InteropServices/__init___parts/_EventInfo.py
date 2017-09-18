class _EventInfo:
 """ Exposes the public members of the System.Reflection.EventInfo class to unmanaged code. """
 def AddEventHandler(self,target,handler):
  """
  AddEventHandler(self: _EventInfo,target: object,handler: Delegate)

   Provides COM objects with version-independent access to the 

    System.Reflection.EventInfo.AddEventHandler(System.Object,System.Delegate) method.

  

  

   target: The event source.

   handler: A method or methods to be invoked when the event is raised by the target.
  """
  pass
 def Equals(self,other):
  """
  Equals(self: _EventInfo,other: object) -> bool

  

   Provides COM objects with version-independent access to the System.Object.Equals(System.Object) 

    method.

  

  

   other: The System.Object to compare with the current System.Object.

   Returns: true if the specified System.Object is equal to the current System.Object; otherwise,false.
  """
  pass
 def GetAddMethod(self,nonPublic=None):
  """
  GetAddMethod(self: _EventInfo) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Reflection.EventInfo.GetAddMethod method.

  

   Returns: A System.Reflection.MethodInfo object representing the method used to add an event-handler 

    delegate to the event source.

  

  GetAddMethod(self: _EventInfo,nonPublic: bool) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Reflection.EventInfo.GetAddMethod(System.Boolean) method.

  

  

   nonPublic: true to return non-public methods; otherwise,false.

   Returns: A System.Reflection.MethodInfo object representing the method used to add an event-handler 

    delegate to the event source.
  """
  pass
 def GetCustomAttributes(self,*__args):
  """
  GetCustomAttributes(self: _EventInfo,inherit: bool) -> Array[object]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MemberInfo.GetCustomAttributes(System.Boolean) method.

  

  

   inherit: true to search a member's inheritance chain to find the attributes; otherwise,false.

   Returns: An array that contains all the custom attributes,or an array with zero (0) elements if no 

    attributes are defined.

  

  GetCustomAttributes(self: _EventInfo,attributeType: Type,inherit: bool) -> Array[object]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MemberInfo.GetCustomAttributes(System.Type,System.Boolean) method.

  

  

   attributeType: The type of attribute to search for. Only attributes that are assignable to this type are 

    returned.

  

   inherit: true to search this member's inheritance chain to find the attributes; otherwise,false.

   Returns: An array of custom attributes applied to this member,or an array with zero (0) elements if no 

    attributes have been applied.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: _EventInfo) -> int

  

   Provides COM objects with version-independent access to the System.Object.GetHashCode method.

   Returns: The hash code for the current instance.
  """
  pass
 def GetIDsOfNames(self,riid,rgszNames,cNames,lcid,rgDispId):
  """
  GetIDsOfNames(self: _EventInfo,riid: Guid,rgszNames: IntPtr,cNames: UInt32,lcid: UInt32,rgDispId: IntPtr) -> Guid

  

   Maps a set of names to a corresponding set of dispatch identifiers.

  

   riid: Reserved for future use. Must be IID_NULL.

   rgszNames: An array of names to be mapped.

   cNames: The count of the names to be mapped.

   lcid: The locale context in which to interpret the names.

   rgDispId: An array allocated by the caller that receives the identifiers corresponding to the names.
  """
  pass
 def GetRaiseMethod(self,nonPublic=None):
  """
  GetRaiseMethod(self: _EventInfo) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Reflection.EventInfo.GetRaiseMethod method.

  

   Returns: The method that is called when the event is raised.

  GetRaiseMethod(self: _EventInfo,nonPublic: bool) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Reflection.EventInfo.GetRaiseMethod(System.Boolean) method.

  

  

   nonPublic: true to return non-public methods; otherwise,false.

   Returns: The System.Reflection.MethodInfo object that was called when the event was raised.
  """
  pass
 def GetRemoveMethod(self,nonPublic=None):
  """
  GetRemoveMethod(self: _EventInfo) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Reflection.EventInfo.GetRemoveMethod method.

  

   Returns: A System.Reflection.MethodInfo object representing the method used to remove an event-handler 

    delegate from the event source.

  

  GetRemoveMethod(self: _EventInfo,nonPublic: bool) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Reflection.EventInfo.GetRemoveMethod(System.Boolean) method.

  

  

   nonPublic: true to return non-public methods; otherwise,false.

   Returns: A System.Reflection.MethodInfo object representing the method used to remove an event-handler 

    delegate from the event source.
  """
  pass
 def GetType(self):
  """
  GetType(self: _EventInfo) -> Type

  

   Provides COM objects with version-independent access to the System.Object.GetType method.

   Returns: A System.Type object.
  """
  pass
 def GetTypeInfo(self,iTInfo,lcid,ppTInfo):
  """
  GetTypeInfo(self: _EventInfo,iTInfo: UInt32,lcid: UInt32,ppTInfo: IntPtr)

   Retrieves the type information for an object,which can be used to get the type information for 

    an interface.

  

  

   iTInfo: The type information to return.

   lcid: The locale identifier for the type information.

   ppTInfo: A pointer to the requested type information object.
  """
  pass
 def GetTypeInfoCount(self,pcTInfo):
  """
  GetTypeInfoCount(self: _EventInfo) -> UInt32

  

   Retrieves the number of type information interfaces that an object provides (either 0 or 1).
  """
  pass
 def Invoke(self,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr):
  """
  Invoke(self: _EventInfo,dispIdMember: UInt32,riid: Guid,lcid: UInt32,wFlags: Int16,pDispParams: IntPtr,pVarResult: IntPtr,pExcepInfo: IntPtr,puArgErr: IntPtr) -> Guid

  

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
  IsDefined(self: _EventInfo,attributeType: Type,inherit: bool) -> bool

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MemberInfo.IsDefined(System.Type,System.Boolean) method.

  

  

   attributeType: The Type object to which the custom attributes are applied.

   inherit: true to search this member's inheritance chain to find the attributes; otherwise,false.

   Returns: true if one or more instance of the attributeType parameter is applied to this member; 

    otherwise,false.
  """
  pass
 def RemoveEventHandler(self,target,handler):
  """
  RemoveEventHandler(self: _EventInfo,target: object,handler: Delegate)

   Provides COM objects with version-independent access to the 

    System.Reflection.EventInfo.RemoveEventHandler(System.Object,System.Delegate) method.

  

  

   target: The event source.

   handler: The delegate to be disassociated from the events raised by target.
  """
  pass
 def ToString(self):
  """
  ToString(self: _EventInfo) -> str

  

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
 """Provides COM objects with version-independent access to the System.Reflection.EventInfo.Attributes property.



Get: Attributes(self: _EventInfo) -> EventAttributes



"""

 DeclaringType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.DeclaringType property.



Get: DeclaringType(self: _EventInfo) -> Type



"""

 EventHandlerType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.EventInfo.EventHandlerType property.



Get: EventHandlerType(self: _EventInfo) -> Type



"""

 IsMulticast=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.EventInfo.IsMulticast property.



Get: IsMulticast(self: _EventInfo) -> bool



"""

 IsSpecialName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.EventInfo.IsSpecialName property.



Get: IsSpecialName(self: _EventInfo) -> bool



"""

 MemberType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.EventInfo.MemberType property.



Get: MemberType(self: _EventInfo) -> MemberTypes



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.Name property.



Get: Name(self: _EventInfo) -> str



"""

 ReflectedType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.ReflectedType property.



Get: ReflectedType(self: _EventInfo) -> Type



"""


