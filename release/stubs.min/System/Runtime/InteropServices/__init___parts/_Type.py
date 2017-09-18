class _Type:
 """ Exposes the public members of the System.Type class to the unmanaged code. """
 def Equals(self,*__args):
  """
  Equals(self: _Type,o: Type) -> bool

  

   Provides COM objects with version-independent access to the System.Type.Equals(System.Type) 

    method.

  

  

   o: The System.Type whose underlying system type is to be compared with the underlying system type 

    of the current System.Type.

  

   Returns: true if the underlying system type of o is the same as the underlying system type of the current 

    System.Type; otherwise,false.

  

  Equals(self: _Type,other: object) -> bool

  

   Provides COM objects with version-independent access to the System.Type.Equals(System.Object) 

    method.

  

  

   other: The System.Object whose underlying system type is to be compared with the underlying system type 

    of the current System.Type.

  

   Returns: true if the underlying system type of o is the same as the underlying system type of the current 

    System.Type; otherwise,false.
  """
  pass
 def FindInterfaces(self,filter,filterCriteria):
  """
  FindInterfaces(self: _Type,filter: TypeFilter,filterCriteria: object) -> Array[Type]

  

   Provides COM objects with version-independent access to the 

    System.Type.FindInterfaces(System.Reflection.TypeFilter,System.Object) method.

  

  

   filter: The System.Reflection.TypeFilter delegate that compares the interfaces against filterCriteria.

   filterCriteria: The search criteria that determines whether an interface should be included in the returned 

    array.

  

   Returns: An array of System.Type objects representing a filtered list of the interfaces implemented or 

    inherited by the current System.Type.-or- An empty array of type System.Type,if no interfaces 

    matching the filter are implemented or inherited by the current System.Type.
  """
  pass
 def FindMembers(self,memberType,bindingAttr,filter,filterCriteria):
  """
  FindMembers(self: _Type,memberType: MemberTypes,bindingAttr: BindingFlags,filter: MemberFilter,filterCriteria: object) -> Array[MemberInfo]

  

   Provides COM objects with version-independent access to the 

    System.Type.FindMembers(System.Reflection.MemberTypes,System.Reflection.BindingFlags,System.Refle

    ction.MemberFilter,System.Object) method.

  

  

   memberType: A MemberTypes object indicating the type of member to search for.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   filter: The delegate that does the comparisons,returning true if the member currently being inspected 

    matches the filterCriteria and false otherwise. You can use the FilterAttribute,FilterName,and 

    FilterNameIgnoreCase delegates supplied by this class. The first uses the fields of 

    FieldAttributes,MethodAttributes,and MethodImplAttributes as search criteria,and the other 

    two delegates use String objects as the search criteria.

  

   filterCriteria: The search criteria that determines whether a member is returned in the array of MemberInfo 

    objects.The fields of FieldAttributes,MethodAttributes,and MethodImplAttributes can be used in 

    conjunction with the FilterAttribute delegate supplied by this class.

  

   Returns: A filtered array of System.Reflection.MemberInfo objects of the specified member type.-or- An 

    empty array of type System.Reflection.MemberInfo,if the current System.Type does not have 

    members of type memberType that match the filter criteria.
  """
  pass
 def GetArrayRank(self):
  """
  GetArrayRank(self: _Type) -> int

  

   Provides COM objects with version-independent access to the System.Type.GetArrayRank method.

   Returns: An System.Int32 containing the number of dimensions in the current System.Type.
  """
  pass
 def GetConstructor(self,*__args):
  """
  GetConstructor(self: _Type,types: Array[Type]) -> ConstructorInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetConstructor(System.Type[]) method.

  

  

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the desired constructor.-or- An empty array of System.Type objects,to get a constructor that 

    takes no parameters. Such an empty array is provided by the static field System.Type.EmptyTypes.

  

   Returns: A System.Reflection.ConstructorInfo object representing the public instance constructor whose 

    parameters match the types in the parameter type array,if found; otherwise,null.

  

  GetConstructor(self: _Type,bindingAttr: BindingFlags,binder: Binder,types: Array[Type],modifiers: Array[ParameterModifier]) -> ConstructorInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetConstructor(System.Reflection.BindingFlags,System.Reflection.Binder,System.Type[],

    System.Reflection.ParameterModifier[]) method.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   binder: A System.Reflection.Binder object that defines a set of properties and enables binding,which 

    can involve selection of an overloaded method,coercion of argument types,and invocation of a 

    member through reflection.-or- null,to use the System.Type.DefaultBinder.

  

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the constructor to get.-or- An empty array of the type System.Type (that is,Type[] types=new 

    Type[0]) to get a constructor that takes no parameters.-or- System.Type.EmptyTypes.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the parameter type array. The default binder does not process 

    this parameter.

  

   Returns: A System.Reflection.ConstructorInfo object representing the constructor that matches the 

    specified requirements,if found; otherwise,null.

  

  GetConstructor(self: _Type,bindingAttr: BindingFlags,binder: Binder,callConvention: CallingConventions,types: Array[Type],modifiers: Array[ParameterModifier]) -> ConstructorInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetConstructor(System.Reflection.BindingFlags,System.Reflection.Binder,System.Reflect

    ion.CallingConventions,System.Type[],System.Reflection.ParameterModifier[]) method.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   binder: A System.Reflection.Binder object that defines a set of properties and enables binding,which 

    can involve selection of an overloaded method,coercion of argument types,and invocation of a 

    member through reflection.-or- null,to use the System.Type.DefaultBinder.

  

   callConvention: The System.Reflection.CallingConventions object that specifies the set of rules to use regarding 

    the order and layout of arguments,how the return value is passed,what registers are used for 

    arguments,and the stack is cleaned up.

  

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the constructor to get.-or- An empty array of the type System.Type (that is,Type[] types=new 

    Type[0]) to get a constructor that takes no parameters.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the types array. The default binder does not process this 

    parameter.

  

   Returns: A System.Reflection.ConstructorInfo object representing the constructor that matches the 

    specified requirements,if found; otherwise,null.
  """
  pass
 def GetConstructors(self,bindingAttr=None):
  """
  GetConstructors(self: _Type) -> Array[ConstructorInfo]

  

   Provides COM objects with version-independent access to the System.Type.GetConstructors method.

   Returns: An array of System.Reflection.ConstructorInfo objects representing all the public instance 

    constructors defined for the current System.Type,but not including the type initializer (static 

    constructor). If no public instance constructors are defined for the current System.Type,or if 

    the current System.Type represents a type parameter of a generic type or method definition,an 

    empty array of type System.Reflection.ConstructorInfo is returned.

  

  GetConstructors(self: _Type,bindingAttr: BindingFlags) -> Array[ConstructorInfo]

  

   Provides COM objects with version-independent access to the 

    System.Type.GetConstructors(System.Reflection.BindingFlags) method.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An array of System.Reflection.ConstructorInfo objects representing all constructors defined for 

    the current System.Type that match the specified binding constraints,including the type 

    initializer if it is defined. Returns an empty array of type System.Reflection.ConstructorInfo 

    if no constructors are defined for the current System.Type,if none of the defined constructors 

    match the binding constraints,or if the current System.Type represents a type parameter of a 

    generic type or method definition.
  """
  pass
 def GetCustomAttributes(self,*__args):
  """
  GetCustomAttributes(self: _Type,inherit: bool) -> Array[object]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.Assembly.GetCustomAttributes(System.Boolean) method.

  

  

   inherit: Specifies whether to search this member's inheritance chain to find the attributes.

   Returns: An array of custom attributes applied to this member,or an array with zero (0) elements if no 

    attributes have been applied.

  

  GetCustomAttributes(self: _Type,attributeType: Type,inherit: bool) -> Array[object]

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MemberInfo.GetCustomAttributes(System.Type,System.Boolean) method.

  

  

   attributeType: The type of attribute to search for. Only attributes that are assignable to this type are 

    returned.

  

   inherit: Specifies whether to search this member's inheritance chain to find the attributes.

   Returns: An array of custom attributes applied to this member,or an array with zero (0) elements if no 

    attributes have been applied.
  """
  pass
 def GetDefaultMembers(self):
  """
  GetDefaultMembers(self: _Type) -> Array[MemberInfo]

  

   Provides COM objects with version-independent access to the System.Type.GetDefaultMembers method.

   Returns: An array of System.Reflection.MemberInfo objects representing all default members of the current 

    System.Type.-or- An empty array of type System.Reflection.MemberInfo,if the current System.Type 

    does not have default members.
  """
  pass
 def GetElementType(self):
  """
  GetElementType(self: _Type) -> Type

  

   Provides COM objects with version-independent access to the System.Type.GetElementType method.

   Returns: The System.Type of the object encompassed or referred to by the current array,pointer or 

    reference type.-or- null if the current System.Type is not an array or a pointer,or is not 

    passed by reference,or represents a generic type or a type parameter of a generic type or 

    method definition.
  """
  pass
 def GetEvent(self,name,bindingAttr=None):
  """
  GetEvent(self: _Type,name: str) -> EventInfo

  

   Provides COM objects with version-independent access to the System.Type.GetEvent(System.String) 

    method.

  

  

   name: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An array of System.Reflection.EventInfo objects representing all events that are declared or 

    inherited by the current System.Type that match the specified binding constraints.-or- An empty 

    array of type System.Reflection.EventInfo,if the current System.Type does not have events,or 

    if none of the events match the binding constraints.

  

  GetEvent(self: _Type,name: str,bindingAttr: BindingFlags) -> EventInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetEvent(System.String,System.Reflection.BindingFlags) method.

  

  

   name: The System.String containing the name of an event that is declared or inherited by the current 

    System.Type.

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: The System.Reflection.EventInfo object representing the specified event that is declared or 

    inherited by the current System.Type,if found; otherwise,null.
  """
  pass
 def GetEvents(self,bindingAttr=None):
  """
  GetEvents(self: _Type,bindingAttr: BindingFlags) -> Array[EventInfo]

  

   Provides COM objects with version-independent access to the 

    System.Type.GetEvents(System.Reflection.BindingFlags) method.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An array of System.Reflection.EventInfo objects representing all events that are declared or 

    inherited by the current System.Type that match the specified binding constraints.-or- An empty 

    array of type System.Reflection.EventInfo,if the current System.Type does not have events,or 

    if none of the events match the binding constraints.

  

  GetEvents(self: _Type) -> Array[EventInfo]

  

   Provides COM objects with version-independent access to the System.Type.GetEvents method.

   Returns: An array of System.Reflection.EventInfo objects representing all the public events that are 

    declared or inherited by the current System.Type.-or- An empty array of type 

    System.Reflection.EventInfo,if the current System.Type does not have public events.
  """
  pass
 def GetField(self,name,bindingAttr=None):
  """
  GetField(self: _Type,name: str) -> FieldInfo

  

   Provides COM objects with version-independent access to the System.Type.GetField(System.String) 

    method.

  

  

   name: The System.String containing the name of the data field to get.

   Returns: A System.Reflection.FieldInfo object representing the public field with the specified name,if 

    found; otherwise,null.

  

  GetField(self: _Type,name: str,bindingAttr: BindingFlags) -> FieldInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetField(System.String,System.Reflection.BindingFlags) method.

  

  

   name: The System.String containing the name of the data field to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: A System.Reflection.FieldInfo object representing the field that matches the specified 

    requirements,if found; otherwise,null.
  """
  pass
 def GetFields(self,bindingAttr=None):
  """
  GetFields(self: _Type) -> Array[FieldInfo]

  

   Provides COM objects with version-independent access to the System.Type.GetFields method.

   Returns: An array of System.Reflection.FieldInfo objects representing all the public fields defined for 

    the current System.Type.-or- An empty array of type System.Reflection.FieldInfo,if no public 

    fields are defined for the current System.Type.

  

  GetFields(self: _Type,bindingAttr: BindingFlags) -> Array[FieldInfo]

  

   Provides COM objects with version-independent access to the 

    System.Type.GetFields(System.Reflection.BindingFlags) method.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An array of System.Reflection.FieldInfo objects representing all fields defined for the current 

    System.Type that match the specified binding constraints.-or- An empty array of type 

    System.Reflection.FieldInfo,if no fields are defined for the current System.Type,or if none of 

    the defined fields match the binding constraints.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: _Type) -> int

  

   Provides COM objects with version-independent access to the System.Type.GetHashCode method.

   Returns: An System.Int32 containing the hash code for this instance.
  """
  pass
 def GetIDsOfNames(self,riid,rgszNames,cNames,lcid,rgDispId):
  """
  GetIDsOfNames(self: _Type,riid: Guid,rgszNames: IntPtr,cNames: UInt32,lcid: UInt32,rgDispId: IntPtr) -> Guid

  

   Maps a set of names to a corresponding set of dispatch identifiers.

  

   riid: Reserved for future use. Must be IID_NULL.

   rgszNames: Passed-in array of names to be mapped.

   cNames: Count of the names to be mapped.

   lcid: The locale context in which to interpret the names.

   rgDispId: Caller-allocated array that receives the IDs corresponding to the names.
  """
  pass
 def GetInterface(self,name,ignoreCase=None):
  """
  GetInterface(self: _Type,name: str) -> Type

  

   Provides COM objects with version-independent access to the 

    System.Type.GetInterface(System.String) method.

  

  

   name: The System.String containing the name of the interface to get. For generic interfaces,this is 

    the mangled name.

  

   Returns: A System.Type object representing the interface with the specified name,implemented or 

    inherited by the current System.Type,if found; otherwise,null.

  

  GetInterface(self: _Type,name: str,ignoreCase: bool) -> Type

  

   Provides COM objects with version-independent access to the 

    System.Type.GetInterface(System.String,System.Boolean) method.

  

  

   name: The System.String containing the name of the interface to get. For generic interfaces,this is 

    the mangled name.

  

   ignoreCase: true to perform a case-insensitive search for name.-or- false to perform a case-sensitive search 

    for name.

  

   Returns: A System.Type object representing the interface with the specified name,implemented or 

    inherited by the current System.Type,if found; otherwise,null.
  """
  pass
 def GetInterfaceMap(self,interfaceType):
  """
  GetInterfaceMap(self: _Type,interfaceType: Type) -> InterfaceMapping

  

   Provides COM objects with version-independent access to the 

    System.Type.GetInterfaceMap(System.Type) method.

  

  

   interfaceType: The System.Type of the interface of which to retrieve a mapping.

   Returns: An System.Reflection.InterfaceMapping object representing the interface mapping for 

    interfaceType.
  """
  pass
 def GetInterfaces(self):
  """
  GetInterfaces(self: _Type) -> Array[Type]

  

   Provides COM objects with version-independent access to the System.Type.GetInterfaces method.

   Returns: An array of System.Type objects representing all the interfaces implemented or inherited by the 

    current System.Type.-or- An empty array of type System.Type,if no interfaces are implemented or 

    inherited by the current System.Type.
  """
  pass
 def GetMember(self,name,*__args):
  """
  GetMember(self: _Type,name: str) -> Array[MemberInfo]

  

   Provides COM objects with version-independent access to the System.Type.GetMember(System.String) 

    method.

  

  

   name: The System.String containing the name of the public members to get.

   Returns: An array of System.Reflection.MemberInfo objects representing the public members with the 

    specified name,if found; otherwise,an empty array.

  

  GetMember(self: _Type,name: str,bindingAttr: BindingFlags) -> Array[MemberInfo]

  

   Provides COM objects with version-independent access to the 

    System.Type.GetMember(System.String,System.Reflection.BindingFlags) method.

  

  

   name: The System.String containing the name of the members to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return an empty array.

  

   Returns: An array of System.Reflection.MemberInfo objects representing the public members with the 

    specified name,if found; otherwise,an empty array.

  

  GetMember(self: _Type,name: str,type: MemberTypes,bindingAttr: BindingFlags) -> Array[MemberInfo]

  

   Provides COM objects with version-independent access to the 

    System.Type.GetMember(System.String,System.Reflection.MemberTypes,System.Reflection.BindingFlags)

     method.

  

  

   name: The System.String containing the name of the members to get.

   type: The System.Reflection.MemberTypes value to search for.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return an empty array.

  

   Returns: An array of System.Reflection.MemberInfo objects representing the public members with the 

    specified name,if found; otherwise,an empty array.
  """
  pass
 def GetMembers(self,bindingAttr=None):
  """
  GetMembers(self: _Type) -> Array[MemberInfo]

  

   Provides COM objects with version-independent access to the System.Type.GetMembers method.

   Returns: An array of System.Reflection.MemberInfo objects representing all the public members of the 

    current System.Type.-or- An empty array of type System.Reflection.MemberInfo,if the current 

    System.Type does not have public members.

  

  GetMembers(self: _Type,bindingAttr: BindingFlags) -> Array[MemberInfo]

  

   Provides COM objects with version-independent access to the 

    System.Type.GetMembers(System.Reflection.BindingFlags) method.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An array of System.Reflection.MemberInfo objects representing all members defined for the 

    current System.Type that match the specified binding constraints.-or- An empty array of type 

    System.Reflection.MemberInfo,if no members are defined for the current System.Type,or if none 

    of the defined members match the binding constraints.
  """
  pass
 def GetMethod(self,name,*__args):
  """
  GetMethod(self: _Type,name: str,types: Array[Type],modifiers: Array[ParameterModifier]) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetMethod(System.String,System.Type[],System.Reflection.ParameterModifier[]) method.

  

  

   name: The System.String containing the name of the public method to get.

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the method to get.-or- An empty array of the type System.Type (that is,Type[] types=new 

    Type[0]) to get a method that takes no parameters.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the types array. The default binder does not process this 

    parameter.

  

   Returns: A System.Reflection.MethodInfo object representing the public method that matches the specified 

    requirements,if found; otherwise,null.

  

  GetMethod(self: _Type,name: str,types: Array[Type]) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetMethod(System.String,System.Type[]) method.

  

  

   name: The System.String containing the name of the public method to get.

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the method to get.-or- An empty array of the type System.Type (that is,Type[] types=new 

    Type[0]) to get a method that takes no parameters.

  

   Returns: A System.Reflection.MethodInfo object representing the public method whose parameters match the 

    specified argument types,if found; otherwise,null.

  

  GetMethod(self: _Type,name: str) -> MethodInfo

  

   Provides COM objects with version-independent access to the System.Type.GetMethod(System.String) 

    method.

  

  

   name: The System.String containing the name of the public method to get.

   Returns: A System.Reflection.MethodInfo object representing the public method with the specified name,if 

    found; otherwise,null.

  

  GetMethod(self: _Type,name: str,bindingAttr: BindingFlags,binder: Binder,types: Array[Type],modifiers: Array[ParameterModifier]) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetMethod(System.String,System.Reflection.BindingFlags,System.Reflection.Binder,Syste

    m.Type[],System.Reflection.ParameterModifier[]) method.

  

  

   name: The System.String containing the name of the method to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   binder: A System.Reflection.Binder object that defines a set of properties and enables binding,which 

    can involve selection of an overloaded method,coercion of argument types,and invocation of a 

    member through reflection.-or- null,to use the System.Type.DefaultBinder.

  

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the method to get.-or- An empty array of the type System.Type (that is,Type[] types=new 

    Type[0]) to get a method that takes no parameters.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the types array. The default binder does not process this 

    parameter.

  

   Returns: A System.Reflection.MethodInfo object representing the method that matches the specified 

    requirements,if found; otherwise,null.

  

  GetMethod(self: _Type,name: str,bindingAttr: BindingFlags) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetMethod(System.String,System.Reflection.BindingFlags) method.

  

  

   name: The System.String containing the name of the method to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: A System.Reflection.MethodInfo object representing the method that matches the specified 

    requirements,if found; otherwise,null.

  

  GetMethod(self: _Type,name: str,bindingAttr: BindingFlags,binder: Binder,callConvention: CallingConventions,types: Array[Type],modifiers: Array[ParameterModifier]) -> MethodInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetMethod(System.String,System.Reflection.BindingFlags,System.Reflection.Binder,Syste

    m.Reflection.CallingConventions,System.Type[],System.Reflection.ParameterModifier[]) method.

  

  

   name: The System.String containing the name of the method to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   binder: A System.Reflection.Binder object that defines a set of properties and enables binding,which 

    can involve selection of an overloaded method,coercion of argument types,and invocation of a 

    member through reflection.-or- null,to use the System.Type.DefaultBinder.

  

   callConvention: The System.Reflection.CallingConventions object that specifies the set of rules to use regarding 

    the order and layout of arguments,how the return value is passed,what registers are used for 

    arguments,and how the stack is cleaned up.

  

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the method to get.-or- An empty array of the type System.Type (that is,Type[] types=new 

    Type[0]) to get a method that takes no parameters.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the types array. The default binder does not process this 

    parameter.

  

   Returns: A System.Reflection.MethodInfo object representing the method that matches the specified 

    requirements,if found; otherwise,null.
  """
  pass
 def GetMethods(self,bindingAttr=None):
  """
  GetMethods(self: _Type) -> Array[MethodInfo]

  

   Provides COM objects with version-independent access to the System.Type.GetMethods method.

   Returns: An array of System.Reflection.MethodInfo objects representing all the public methods defined for 

    the current System.Type.-or- An empty array of type System.Reflection.MethodInfo,if no public 

    methods are defined for the current System.Type.

  

  GetMethods(self: _Type,bindingAttr: BindingFlags) -> Array[MethodInfo]

  

   Provides COM objects with version-independent access to the 

    System.Type.GetMethods(System.Reflection.BindingFlags) method.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An array of System.Reflection.MethodInfo objects representing all methods defined for the 

    current System.Type that match the specified binding constraints.-or- An empty array of type 

    System.Reflection.MethodInfo,if no methods are defined for the current System.Type,or if none 

    of the defined methods match the binding constraints.
  """
  pass
 def GetNestedType(self,name,bindingAttr=None):
  """
  GetNestedType(self: _Type,name: str) -> Type

  

   Provides COM objects with version-independent access to the 

    System.Type.GetNestedType(System.String) method.

  

  

   name: The string containing the name of the nested type to get.

   Returns: A System.Type object representing the public nested type with the specified name,if found; 

    otherwise,null.

  

  GetNestedType(self: _Type,name: str,bindingAttr: BindingFlags) -> Type

  

   Provides COM objects with version-independent access to the 

    System.Type.GetNestedType(System.String,System.Reflection.BindingFlags) method.

  

  

   name: The string containing the name of the nested type to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: A System.Type object representing the nested type that matches the specified requirements,if 

    found; otherwise,null.
  """
  pass
 def GetNestedTypes(self,bindingAttr=None):
  """
  GetNestedTypes(self: _Type) -> Array[Type]

  

   Provides COM objects with version-independent access to the System.Type.GetNestedTypes method.

   Returns: An array of System.Type objects representing all the types nested within the current 

    System.Type.-or- An empty array of type System.Type,if no types are nested within the current 

    System.Type.

  

  GetNestedTypes(self: _Type,bindingAttr: BindingFlags) -> Array[Type]

  

   Provides COM objects with version-independent access to the 

    System.Type.GetNestedTypes(System.Reflection.BindingFlags) method,and searches for the types 

    nested within the current System.Type,using the specified binding constraints.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An array of System.Type objects representing all the types nested within the current System.Type 

    that match the specified binding constraints.-or- An empty array of type System.Type,if no 

    types are nested within the current System.Type,or if none of the nested types match the 

    binding constraints.
  """
  pass
 def GetProperties(self,bindingAttr=None):
  """
  GetProperties(self: _Type) -> Array[PropertyInfo]

  

   Provides COM objects with version-independent access to the System.Type.GetProperties method.

   Returns: An array of System.Reflection.PropertyInfo objects representing all public properties of the 

    current System.Type.-or- An empty array of type System.Reflection.PropertyInfo,if the current 

    System.Type does not have public properties.

  

  GetProperties(self: _Type,bindingAttr: BindingFlags) -> Array[PropertyInfo]

  

   Provides COM objects with version-independent access to the 

    System.Type.GetProperties(System.Reflection.BindingFlags) method.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An array of System.Reflection.PropertyInfo objects representing all properties of the current 

    System.Type that match the specified binding constraints.-or- An empty array of type 

    System.Reflection.PropertyInfo,if the current System.Type does not have properties,or if none 

    of the properties match the binding constraints.
  """
  pass
 def GetProperty(self,name,*__args):
  """
  GetProperty(self: _Type,name: str,types: Array[Type]) -> PropertyInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetProperty(System.String,System.Type[]) method.

  

  

   name: The System.String containing the name of the public property to get.

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the indexed property to get.-or- An empty array of the type System.Type (that is,Type[] types=

    new Type[0]) to get a property that is not indexed.

  

   Returns: A System.Reflection.PropertyInfo object representing the public property whose parameters match 

    the specified argument types,if found; otherwise,null.

  

  GetProperty(self: _Type,name: str,returnType: Type) -> PropertyInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetProperty(System.String,System.Type) method.

  

  

   name: The System.String containing the name of the public property to get.

   returnType: The return type of the property.

   Returns: A System.Reflection.PropertyInfo object representing the public property with the specified 

    name,if found; otherwise,null.

  

  GetProperty(self: _Type,name: str) -> PropertyInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetProperty(System.String) method.

  

  

   name: The System.String containing the name of the public property to get.

   Returns: A System.Reflection.PropertyInfo object representing the public property with the specified 

    name,if found; otherwise,null.

  

  GetProperty(self: _Type,name: str,returnType: Type,types: Array[Type]) -> PropertyInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetProperty(System.String,System.Type,System.Type[]) method.

  

  

   name: The System.String containing the name of the public property to get.

   returnType: The return type of the property.

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the indexed property to get.-or- An empty array of the type System.Type (that is,Type[] types=

    new Type[0]) to get a property that is not indexed.

  

   Returns: A System.Reflection.PropertyInfo object representing the public property whose parameters match 

    the specified argument types,if found; otherwise,null.

  

  GetProperty(self: _Type,name: str,bindingAttr: BindingFlags) -> PropertyInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetProperty(System.String,System.Reflection.BindingFlags) method.

  

  

   name: The System.String containing the name of the property to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: A System.Reflection.PropertyInfo object representing the property that matches the specified 

    requirements,if found; otherwise,null.

  

  GetProperty(self: _Type,name: str,bindingAttr: BindingFlags,binder: Binder,returnType: Type,types: Array[Type],modifiers: Array[ParameterModifier]) -> PropertyInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetProperty(System.String,System.Reflection.BindingFlags,System.Reflection.Binder,Sys

    tem.Type,System.Type[],System.Reflection.ParameterModifier[]) method.

  

  

   name: The System.String containing the name of the property to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   binder: A System.Reflection.Binder object that defines a set of properties and enables binding,which 

    can involve selection of an overloaded method,coercion of argument types,and invocation of a 

    member through reflection.-or- null,to use the System.Type.DefaultBinder.

  

   returnType: The return type of the property.

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the indexed property to get.-or- An empty array of the type System.Type (that is,Type[] types=

    new Type[0]) to get a property that is not indexed.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the types array. The default binder does not process this 

    parameter.

  

   Returns: A System.Reflection.PropertyInfo object representing the property that matches the specified 

    requirements,if found; otherwise,null.

  

  GetProperty(self: _Type,name: str,returnType: Type,types: Array[Type],modifiers: Array[ParameterModifier]) -> PropertyInfo

  

   Provides COM objects with version-independent access to the 

    System.Type.GetProperty(System.String,System.Type,System.Type[],System.Reflection.ParameterModifi

    er[]) method.

  

  

   name: The System.String containing the name of the public property to get.

   returnType: The return type of the property.

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the indexed property to get.-or- An empty array of the type System.Type (that is,Type[] types=

    new Type[0]) to get a property that is not indexed.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the types array. The default binder does not process this 

    parameter.

  

   Returns: A System.Reflection.PropertyInfo object representing the public property that matches the 

    specified requirements,if found; otherwise,null.
  """
  pass
 def GetType(self):
  """
  GetType(self: _Type) -> Type

  

   Provides COM objects with version-independent access to the System.Type.GetType method.

   Returns: The current System.Type.
  """
  pass
 def GetTypeInfo(self,iTInfo,lcid,ppTInfo):
  """
  GetTypeInfo(self: _Type,iTInfo: UInt32,lcid: UInt32,ppTInfo: IntPtr)

   Retrieves the type information for an object,which can then be used to get the type information 

    for an interface.

  

  

   iTInfo: The type information to return.

   lcid: The locale identifier for the type information.

   ppTInfo: Receives a pointer to the requested type information object.
  """
  pass
 def GetTypeInfoCount(self,pcTInfo):
  """
  GetTypeInfoCount(self: _Type) -> UInt32

  

   Retrieves the number of type information interfaces that an object provides (either 0 or 1).
  """
  pass
 def Invoke(self,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr):
  """
  Invoke(self: _Type,dispIdMember: UInt32,riid: Guid,lcid: UInt32,wFlags: Int16,pDispParams: IntPtr,pVarResult: IntPtr,pExcepInfo: IntPtr,puArgErr: IntPtr) -> Guid

  

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
 def InvokeMember(self,name,invokeAttr,binder,target,args,*__args):
  """
  InvokeMember(self: _Type,name: str,invokeAttr: BindingFlags,binder: Binder,target: object,args: Array[object]) -> object

  

   Provides COM objects with version-independent access to the 

    System.Type.InvokeMember(System.String,System.Reflection.BindingFlags,System.Reflection.Binder,Sy

    stem.Object,System.Object[]) method.

  

  

   name: The System.String containing the name of the constructor,method,property,or field member to 

    invoke.-or- An empty string ("") to invoke the default member. -or-For IDispatch members,a 

    string representing the DispID,for example "[DispID=3]".

  

   invokeAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted. The access can be one of the BindingFlags such as Public,NonPublic,Private,

    InvokeMethod,GetField,and so on. The type of lookup need not be specified. If the type of 

    lookup is omitted,BindingFlags.Public | BindingFlags.Instance will apply.

  

   binder: A System.Reflection.Binder object that defines a set of properties and enables binding,which 

    can involve selection of an overloaded method,coercion of argument types,and invocation of a 

    member through reflection.-or- null,to use the System.Type.DefaultBinder.

  

   target: The System.Object on which to invoke the specified member.

   args: An array containing the arguments to pass to the member to invoke.

   Returns: An System.Object representing the return value of the invoked member.

  InvokeMember(self: _Type,name: str,invokeAttr: BindingFlags,binder: Binder,target: object,args: Array[object],culture: CultureInfo) -> object

  

   Provides COM objects with version-independent access to the 

    System.Type.InvokeMember(System.String,System.Reflection.BindingFlags,System.Reflection.Binder,Sy

    stem.Object,System.Object[],System.Globalization.CultureInfo) method.

  

  

   name: The System.String containing the name of the constructor,method,property,or field member to 

    invoke.-or- An empty string ("") to invoke the default member. -or-For IDispatch members,a 

    string representing the DispID,for example "[DispID=3]".

  

   invokeAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted. The access can be one of the BindingFlags such as Public,NonPublic,Private,

    InvokeMethod,GetField,and so on. The type of lookup need not be specified. If the type of 

    lookup is omitted,BindingFlags.Public | BindingFlags.Instance will apply.

  

   binder: A System.Reflection.Binder object that defines a set of properties and enables binding,which 

    can involve selection of an overloaded method,coercion of argument types,and invocation of a 

    member through reflection.-or- null,to use the System.Type.DefaultBinder.

  

   target: The System.Object on which to invoke the specified member.

   args: An array containing the arguments to pass to the member to invoke.

   culture: The System.Globalization.CultureInfo object representing the globalization locale to use,which 

    may be necessary for locale-specific conversions,such as converting a numeric String to a 

    Double.-or- null to use the current thread's System.Globalization.CultureInfo.

  

   Returns: An System.Object representing the return value of the invoked member.

  InvokeMember(self: _Type,name: str,invokeAttr: BindingFlags,binder: Binder,target: object,args: Array[object],modifiers: Array[ParameterModifier],culture: CultureInfo,namedParameters: Array[str]) -> object

  

   Provides COM objects with version-independent access to the 

    System.Type.InvokeMember(System.String,System.Reflection.BindingFlags,System.Reflection.Binder,Sy

    stem.Object,System.Object[],System.Reflection.ParameterModifier[],System.Globalization.CultureInf

    o,System.String[]) method.

  

  

   name: The System.String containing the name of the constructor,method,property,or field member to 

    invoke.-or- An empty string ("") to invoke the default member. -or-For IDispatch members,a 

    string representing the DispID,for example "[DispID=3]".

  

   invokeAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted. The access can be one of the BindingFlags such as Public,NonPublic,Private,

    InvokeMethod,GetField,and so on. The type of lookup need not be specified. If the type of 

    lookup is omitted,BindingFlags.Public | BindingFlags.Instance will apply.

  

   binder: A System.Reflection.Binder object that defines a set of properties and enables binding,which 

    can involve selection of an overloaded method,coercion of argument types,and invocation of a 

    member through reflection.-or- null,to use the System.Type.DefaultBinder.

  

   target: The System.Object on which to invoke the specified member.

   args: An array containing the arguments to pass to the member to invoke.

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the args array. A parameter's associated attributes are stored 

    in the member's signature. The default binder does not process this parameter.

  

   culture: The System.Globalization.CultureInfo object representing the globalization locale to use,which 

    may be necessary for locale-specific conversions,such as converting a numeric String to a 

    Double.-or- null to use the current thread's System.Globalization.CultureInfo.

  

   namedParameters: An array containing the names of the parameters to which the values in the args array are passed.

   Returns: An System.Object representing the return value of the invoked member.
  """
  pass
 def IsAssignableFrom(self,c):
  """
  IsAssignableFrom(self: _Type,c: Type) -> bool

  

   Provides COM objects with version-independent access to the 

    System.Type.IsAssignableFrom(System.Type) method.

  

  

   c: The System.Type to compare with the current System.Type.

   Returns: true if c and the current System.Type represent the same type,or if the current System.Type is 

    in the inheritance hierarchy of c,or if the current System.Type is an interface that c 

    implements,or if c is a generic type parameter and the current System.Type represents one of 

    the constraints of c. false if none of these conditions are the case,or if c is null.
  """
  pass
 def IsDefined(self,attributeType,inherit):
  """
  IsDefined(self: _Type,attributeType: Type,inherit: bool) -> bool

  

   Provides COM objects with version-independent access to the 

    System.Reflection.MemberInfo.IsDefined(System.Type,System.Boolean) method.

  

  

   attributeType: The Type object to which the custom attributes are applied.

   inherit: Specifies whether to search this member's inheritance chain to find the attributes.

   Returns: true if one or more instance of attributeType is applied to this member; otherwise,false.
  """
  pass
 def IsInstanceOfType(self,o):
  """
  IsInstanceOfType(self: _Type,o: object) -> bool

  

   Provides COM objects with version-independent access to the 

    System.Type.IsInstanceOfType(System.Object) method.

  

  

   o: The object to compare with the current System.Type.

   Returns: true if the current System.Type is in the inheritance hierarchy of the object represented by o,

    or if the current System.Type is an interface that o supports. false if neither of these 

    conditions is the case,or if o is null,or if the current System.Type is an open generic type 

    (that is,System.Type.ContainsGenericParameters returns true).
  """
  pass
 def IsSubclassOf(self,c):
  """
  IsSubclassOf(self: _Type,c: Type) -> bool

  

   Provides COM objects with version-independent access to the 

    System.Type.IsSubclassOf(System.Type) method.

  

  

   c: The System.Type to compare with the current System.Type.

   Returns: true if the System.Type represented by the c parameter and the current System.Type represent 

    classes,and the class represented by the current System.Type derives from the class represented 

    by c; otherwise,false. This method also returns false if c and the current System.Type 

    represent the same class.
  """
  pass
 def ToString(self):
  """
  ToString(self: _Type) -> str

  

   Provides COM objects with version-independent access to the System.Type.ToString method.

   Returns: A System.String representing the name of the current System.Type.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 Assembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.Assembly property.



Get: Assembly(self: _Type) -> Assembly



"""

 AssemblyQualifiedName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.AssemblyQualifiedName property.



Get: AssemblyQualifiedName(self: _Type) -> str



"""

 Attributes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.Attributes property.



Get: Attributes(self: _Type) -> TypeAttributes



"""

 BaseType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.BaseType property.



Get: BaseType(self: _Type) -> Type



"""

 DeclaringType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.DeclaringType property.



Get: DeclaringType(self: _Type) -> Type



"""

 FullName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.FullName property.



Get: FullName(self: _Type) -> str



"""

 GUID=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.GUID property.



Get: GUID(self: _Type) -> Guid



"""

 HasElementType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.HasElementType property.



Get: HasElementType(self: _Type) -> bool



"""

 IsAbstract=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsAbstract property.



Get: IsAbstract(self: _Type) -> bool



"""

 IsAnsiClass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsAnsiClass property.



Get: IsAnsiClass(self: _Type) -> bool



"""

 IsArray=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsArray property.



Get: IsArray(self: _Type) -> bool



"""

 IsAutoClass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsAutoClass property.



Get: IsAutoClass(self: _Type) -> bool



"""

 IsAutoLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsAutoLayout property.



Get: IsAutoLayout(self: _Type) -> bool



"""

 IsByRef=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsByRef property.



Get: IsByRef(self: _Type) -> bool



"""

 IsClass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsClass property.



Get: IsClass(self: _Type) -> bool



"""

 IsCOMObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsCOMObject property.



Get: IsCOMObject(self: _Type) -> bool



"""

 IsContextful=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsContextful property.



Get: IsContextful(self: _Type) -> bool



"""

 IsEnum=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsEnum property.



Get: IsEnum(self: _Type) -> bool



"""

 IsExplicitLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsExplicitLayout property.



Get: IsExplicitLayout(self: _Type) -> bool



"""

 IsImport=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsImport property.



Get: IsImport(self: _Type) -> bool



"""

 IsInterface=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsInterface property.



Get: IsInterface(self: _Type) -> bool



"""

 IsLayoutSequential=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsLayoutSequential property.



Get: IsLayoutSequential(self: _Type) -> bool



"""

 IsMarshalByRef=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsMarshalByRef property.



Get: IsMarshalByRef(self: _Type) -> bool



"""

 IsNestedAssembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsNestedAssembly property.



Get: IsNestedAssembly(self: _Type) -> bool



"""

 IsNestedFamANDAssem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsNestedFamANDAssem property.



Get: IsNestedFamANDAssem(self: _Type) -> bool



"""

 IsNestedFamily=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsNestedFamily property.



Get: IsNestedFamily(self: _Type) -> bool



"""

 IsNestedFamORAssem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsNestedFamORAssem property.



Get: IsNestedFamORAssem(self: _Type) -> bool



"""

 IsNestedPrivate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsNestedPrivate property.



Get: IsNestedPrivate(self: _Type) -> bool



"""

 IsNestedPublic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsNestedPublic property.



Get: IsNestedPublic(self: _Type) -> bool



"""

 IsNotPublic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsNotPublic property.



Get: IsNotPublic(self: _Type) -> bool



"""

 IsPointer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsPointer property.



Get: IsPointer(self: _Type) -> bool



"""

 IsPrimitive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsPrimitive property.



Get: IsPrimitive(self: _Type) -> bool



"""

 IsPublic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsPublic property.



Get: IsPublic(self: _Type) -> bool



"""

 IsSealed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsSealed property.



Get: IsSealed(self: _Type) -> bool



"""

 IsSerializable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsSerializable property.



Get: IsSerializable(self: _Type) -> bool



"""

 IsSpecialName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsSpecialName property.



Get: IsSpecialName(self: _Type) -> bool



"""

 IsUnicodeClass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsUnicodeClass property.



Get: IsUnicodeClass(self: _Type) -> bool



"""

 IsValueType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.IsValueType property.



Get: IsValueType(self: _Type) -> bool



"""

 MemberType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.MemberType property.



Get: MemberType(self: _Type) -> MemberTypes



"""

 Module=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.Module property.



Get: Module(self: _Type) -> Module



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Reflection.MemberInfo.Name property.



Get: Name(self: _Type) -> str



"""

 Namespace=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.Namespace property.



Get: Namespace(self: _Type) -> str



"""

 ReflectedType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.ReflectedType property.



Get: ReflectedType(self: _Type) -> Type



"""

 TypeHandle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.TypeHandle property.



Get: TypeHandle(self: _Type) -> RuntimeTypeHandle



"""

 TypeInitializer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.TypeInitializer property.



Get: TypeInitializer(self: _Type) -> ConstructorInfo



"""

 UnderlyingSystemType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Provides COM objects with version-independent access to the System.Type.UnderlyingSystemType property.



Get: UnderlyingSystemType(self: _Type) -> Type



"""


