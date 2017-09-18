class Type(MemberInfo,ICustomAttributeProvider,_MemberInfo,_Type,IReflect):
 """ Represents type declarations: class types,interface types,array types,value types,enumeration types,type parameters,generic type definitions,and open or closed constructed generic types. """
 def Equals(self,o):
  """
  Equals(self: Type,o: Type) -> bool

  

   Determines if the underlying system type of the current System.Type is the same as the 

    underlying system type of the specified System.Type.

  

  

   o: The object whose underlying system type is to be compared with the underlying system type of the 

    current System.Type.

  

   Returns: true if the underlying system type of o is the same as the underlying system type of the current 

    System.Type; otherwise,false.

  

  Equals(self: Type,o: object) -> bool

  

   Determines if the underlying system type of the current System.Type is the same as the 

    underlying system type of the specified System.Object.

  

  

   o: The object whose underlying system type is to be compared with the underlying system type of the 

    current System.Type.

  

   Returns: true if the underlying system type of o is the same as the underlying system type of the current 

    System.Type; otherwise,false. This method also returns false if the object specified by the o 

    parameter is not a Type.
  """
  pass
 def FilterAttribute(self,*args):
  """
  Represents a delegate that is used to filter a list of members represented in an array of System.Reflection.MemberInfo objects.

  

  MemberFilter(object: object,method: IntPtr)
  """
  pass
 def FilterName(self,*args):
  """
  Represents a delegate that is used to filter a list of members represented in an array of System.Reflection.MemberInfo objects.

  

  MemberFilter(object: object,method: IntPtr)
  """
  pass
 def FilterNameIgnoreCase(self,*args):
  """
  Represents a delegate that is used to filter a list of members represented in an array of System.Reflection.MemberInfo objects.

  

  MemberFilter(object: object,method: IntPtr)
  """
  pass
 def FindInterfaces(self,filter,filterCriteria):
  """
  FindInterfaces(self: Type,filter: TypeFilter,filterCriteria: object) -> Array[Type]

  

   Returns an array of System.Type objects representing a filtered list of interfaces implemented 

    or inherited by the current System.Type.

  

  

   filter: The delegate that compares the interfaces against filterCriteria.

   filterCriteria: The search criteria that determines whether an interface should be included in the returned 

    array.

  

   Returns: An array of System.Type objects representing a filtered list of the interfaces implemented or 

    inherited by the current System.Type,or an empty array of type System.Type if no interfaces 

    matching the filter are implemented or inherited by the current System.Type.
  """
  pass
 def FindMembers(self,memberType,bindingAttr,filter,filterCriteria):
  """
  FindMembers(self: Type,memberType: MemberTypes,bindingAttr: BindingFlags,filter: MemberFilter,filterCriteria: object) -> Array[MemberInfo]

  

   Returns a filtered array of System.Reflection.MemberInfo objects of the specified member type.

  

   memberType: An object that indicates the type of member to search for.

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
  GetArrayRank(self: Type) -> int

  

   Gets the number of dimensions in an System.Array.

   Returns: An System.Int32 containing the number of dimensions in the current Type.
  """
  pass
 def GetAttributeFlagsImpl(self,*args):
  """
  GetAttributeFlagsImpl(self: Type) -> TypeAttributes

  

   When overridden in a derived class,implements the System.Type.Attributes property and gets a 

    bitmask indicating the attributes associated with the System.Type.

  

   Returns: A System.Reflection.TypeAttributes object representing the attribute set of the System.Type.
  """
  pass
 def GetConstructor(self,*__args):
  """
  GetConstructor(self: Type,types: Array[Type]) -> ConstructorInfo

  

   Searches for a public instance constructor whose parameters match the types in the specified 

    array.

  

  

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the desired constructor.-or- An empty array of System.Type objects,to get a constructor that 

    takes no parameters. Such an empty array is provided by the static field System.Type.EmptyTypes.

  

   Returns: An object representing the public instance constructor whose parameters match the types in the 

    parameter type array,if found; otherwise,null.

  

  GetConstructor(self: Type,bindingAttr: BindingFlags,binder: Binder,types: Array[Type],modifiers: Array[ParameterModifier]) -> ConstructorInfo

  

   Searches for a constructor whose parameters match the specified argument types and modifiers,

    using the specified binding constraints.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   binder: An object that defines a set of properties and enables binding,which can involve selection of 

    an overloaded method,coercion of argument types,and invocation of a member through 

    reflection.-or- A null reference (Nothing in Visual Basic),to use the 

    System.Type.DefaultBinder.

  

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the constructor to get.-or- An empty array of the type System.Type (that is,Type[] types=new 

    Type[0]) to get a constructor that takes no parameters.-or- System.Type.EmptyTypes.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the parameter type array. The default binder does not process 

    this parameter.

  

   Returns: A System.Reflection.ConstructorInfo object representing the constructor that matches the 

    specified requirements,if found; otherwise,null.

  

  GetConstructor(self: Type,bindingAttr: BindingFlags,binder: Binder,callConvention: CallingConventions,types: Array[Type],modifiers: Array[ParameterModifier]) -> ConstructorInfo

  

   Searches for a constructor whose parameters match the specified argument types and modifiers,

    using the specified binding constraints and the specified calling convention.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   binder: An object that defines a set of properties and enables binding,which can involve selection of 

    an overloaded method,coercion of argument types,and invocation of a member through 

    reflection.-or- A null reference (Nothing in Visual Basic),to use the 

    System.Type.DefaultBinder.

  

   callConvention: The object that specifies the set of rules to use regarding the order and layout of arguments,

    how the return value is passed,what registers are used for arguments,and the stack is cleaned 

    up.

  

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the constructor to get.-or- An empty array of the type System.Type (that is,Type[] types=new 

    Type[0]) to get a constructor that takes no parameters.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the types array. The default binder does not process this 

    parameter.

  

   Returns: An object representing the constructor that matches the specified requirements,if found; 

    otherwise,null.
  """
  pass
 def GetConstructorImpl(self,*args):
  """
  GetConstructorImpl(self: Type,bindingAttr: BindingFlags,binder: Binder,callConvention: CallingConventions,types: Array[Type],modifiers: Array[ParameterModifier]) -> ConstructorInfo

  

   When overridden in a derived class,searches for a constructor whose parameters match the 

    specified argument types and modifiers,using the specified binding constraints and the 

    specified calling convention.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   binder: An object that defines a set of properties and enables binding,which can involve selection of 

    an overloaded method,coercion of argument types,and invocation of a member through 

    reflection.-or- A null reference (Nothing in Visual Basic),to use the 

    System.Type.DefaultBinder.

  

   callConvention: The object that specifies the set of rules to use regarding the order and layout of arguments,

    how the return value is passed,what registers are used for arguments,and the stack is cleaned 

    up.

  

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
  GetConstructors(self: Type) -> Array[ConstructorInfo]

  

   Returns all the public constructors defined for the current System.Type.

   Returns: An array of System.Reflection.ConstructorInfo objects representing all the public instance 

    constructors defined for the current System.Type,but not including the type initializer (static 

    constructor). If no public instance constructors are defined for the current System.Type,or if 

    the current System.Type represents a type parameter in the definition of a generic type or 

    generic method,an empty array of type System.Reflection.ConstructorInfo is returned.

  

  GetConstructors(self: Type,bindingAttr: BindingFlags) -> Array[ConstructorInfo]

  

   When overridden in a derived class,searches for the constructors defined for the current 

    System.Type,using the specified BindingFlags.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An array of System.Reflection.ConstructorInfo objects representing all constructors defined for 

    the current System.Type that match the specified binding constraints,including the type 

    initializer if it is defined. Returns an empty array of type System.Reflection.ConstructorInfo 

    if no constructors are defined for the current System.Type,if none of the defined constructors 

    match the binding constraints,or if the current System.Type represents a type parameter in the 

    definition of a generic type or generic method.
  """
  pass
 def GetDefaultMembers(self):
  """
  GetDefaultMembers(self: Type) -> Array[MemberInfo]

  

   Searches for the members defined for the current System.Type whose 

    System.Reflection.DefaultMemberAttribute is set.

  

   Returns: An array of System.Reflection.MemberInfo objects representing all default members of the current 

    System.Type.-or- An empty array of type System.Reflection.MemberInfo,if the current System.Type 

    does not have default members.
  """
  pass
 def GetElementType(self):
  """
  GetElementType(self: Type) -> Type

  

   When overridden in a derived class,returns the System.Type of the object encompassed or 

    referred to by the current array,pointer or reference type.

  

   Returns: The System.Type of the object encompassed or referred to by the current array,pointer,or 

    reference type,or null if the current System.Type is not an array or a pointer,or is not 

    passed by reference,or represents a generic type or a type parameter in the definition of a 

    generic type or generic method.
  """
  pass
 def GetEnumName(self,value):
  """
  GetEnumName(self: Type,value: object) -> str

  

   Returns the name of the constant that has the specified value,for the current enumeration type.

  

   value: The value whose name is to be retrieved.

   Returns: The name of the member of the current enumeration type that has the specified value,or null if 

    no such constant is found.
  """
  pass
 def GetEnumNames(self):
  """
  GetEnumNames(self: Type) -> Array[str]

  

   Returns the names of the members of the current enumeration type.

   Returns: An array that contains the names of the members of the enumeration.
  """
  pass
 def GetEnumUnderlyingType(self):
  """
  GetEnumUnderlyingType(self: Type) -> Type

  

   Returns the underlying type of the current enumeration type.

   Returns: The underlying type of the current enumeration.
  """
  pass
 def GetEnumValues(self):
  """
  GetEnumValues(self: Type) -> Array

  

   Returns an array of the values of the constants in the current enumeration type.

   Returns: An array that contains the values. The elements of the array are sorted by the binary values 

    (that is,the unsigned values) of the enumeration constants.
  """
  pass
 def GetEvent(self,name,bindingAttr=None):
  """
  GetEvent(self: Type,name: str,bindingAttr: BindingFlags) -> EventInfo

  

   When overridden in a derived class,returns the System.Reflection.EventInfo object representing 

    the specified event,using the specified binding constraints.

  

  

   name: The string containing the name of an event which is declared or inherited by the current 

    System.Type.

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: The object representing the specified event that is declared or inherited by the current 

    System.Type,if found; otherwise,null.

  

  GetEvent(self: Type,name: str) -> EventInfo

  

   Returns the System.Reflection.EventInfo object representing the specified public event.

  

   name: The string containing the name of an event that is declared or inherited by the current 

    System.Type.

  

   Returns: The object representing the specified public event that is declared or inherited by the current 

    System.Type,if found; otherwise,null.
  """
  pass
 def GetEvents(self,bindingAttr=None):
  """
  GetEvents(self: Type,bindingAttr: BindingFlags) -> Array[EventInfo]

  

   When overridden in a derived class,searches for events that are declared or inherited by the 

    current System.Type,using the specified binding constraints.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An array of System.Reflection.EventInfo objects representing all events that are declared or 

    inherited by the current System.Type that match the specified binding constraints.-or- An empty 

    array of type System.Reflection.EventInfo,if the current System.Type does not have events,or 

    if none of the events match the binding constraints.

  

  GetEvents(self: Type) -> Array[EventInfo]

  

   Returns all the public events that are declared or inherited by the current System.Type.

   Returns: An array of System.Reflection.EventInfo objects representing all the public events which are 

    declared or inherited by the current System.Type.-or- An empty array of type 

    System.Reflection.EventInfo,if the current System.Type does not have public events.
  """
  pass
 def GetField(self,name,bindingAttr=None):
  """
  GetField(self: Type,name: str) -> FieldInfo

  

   Searches for the public field with the specified name.

  

   name: The string containing the name of the data field to get.

   Returns: An object representing the public field with the specified name,if found; otherwise,null.

  GetField(self: Type,name: str,bindingAttr: BindingFlags) -> FieldInfo

  

   Searches for the specified field,using the specified binding constraints.

  

   name: The string containing the name of the data field to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An object representing the field that matches the specified requirements,if found; otherwise,

    null.
  """
  pass
 def GetFields(self,bindingAttr=None):
  """
  GetFields(self: Type,bindingAttr: BindingFlags) -> Array[FieldInfo]

  

   When overridden in a derived class,searches for the fields defined for the current System.Type,

    using the specified binding constraints.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An array of System.Reflection.FieldInfo objects representing all fields defined for the current 

    System.Type that match the specified binding constraints.-or- An empty array of type 

    System.Reflection.FieldInfo,if no fields are defined for the current System.Type,or if none of 

    the defined fields match the binding constraints.

  

  GetFields(self: Type) -> Array[FieldInfo]

  

   Returns all the public fields of the current System.Type.

   Returns: An array of System.Reflection.FieldInfo objects representing all the public fields defined for 

    the current System.Type.-or- An empty array of type System.Reflection.FieldInfo,if no public 

    fields are defined for the current System.Type.
  """
  pass
 def GetGenericArguments(self):
  """
  GetGenericArguments(self: Type) -> Array[Type]

  

   Returns an array of System.Type objects that represent the type arguments of a generic type or 

    the type parameters of a generic type definition.

  

   Returns: An array of System.Type objects that represent the type arguments of a generic type. Returns an 

    empty array if the current type is not a generic type.
  """
  pass
 def GetGenericParameterConstraints(self):
  """
  GetGenericParameterConstraints(self: Type) -> Array[Type]

  

   Returns an array of System.Type objects that represent the constraints on the current generic 

    type parameter.

  

   Returns: An array of System.Type objects that represent the constraints on the current generic type 

    parameter.
  """
  pass
 def GetGenericTypeDefinition(self):
  """
  GetGenericTypeDefinition(self: Type) -> Type

  

   Returns a System.Type object that represents a generic type definition from which the current 

    generic type can be constructed.

  

   Returns: A System.Type object representing a generic type from which the current type can be constructed.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Type) -> int

  

   Returns the hash code for this instance.

   Returns: The hash code for this instance.
  """
  pass
 def GetInterface(self,name,ignoreCase=None):
  """
  GetInterface(self: Type,name: str,ignoreCase: bool) -> Type

  

   When overridden in a derived class,searches for the specified interface,specifying whether to 

    do a case-insensitive search for the interface name.

  

  

   name: The string containing the name of the interface to get. For generic interfaces,this is the 

    mangled name.

  

   ignoreCase: true to ignore the case of that part of name that specifies the simple interface name (the part 

    that specifies the namespace must be correctly cased).-or- false to perform a case-sensitive 

    search for all parts of name.

  

   Returns: An object representing the interface with the specified name,implemented or inherited by the 

    current System.Type,if found; otherwise,null.

  

  GetInterface(self: Type,name: str) -> Type

  

   Searches for the interface with the specified name.

  

   name: The string containing the name of the interface to get. For generic interfaces,this is the 

    mangled name.

  

   Returns: An object representing the interface with the specified name,implemented or inherited by the 

    current System.Type,if found; otherwise,null.
  """
  pass
 def GetInterfaceMap(self,interfaceType):
  """
  GetInterfaceMap(self: Type,interfaceType: Type) -> InterfaceMapping

  

   Returns an interface mapping for the specified interface type.

  

   interfaceType: The interface type to retrieve a mapping for.

   Returns: An object that represents the interface mapping for interfaceType.
  """
  pass
 def GetInterfaces(self):
  """
  GetInterfaces(self: Type) -> Array[Type]

  

   When overridden in a derived class,gets all the interfaces implemented or inherited by the 

    current System.Type.

  

   Returns: An array of System.Type objects representing all the interfaces implemented or inherited by the 

    current System.Type.-or- An empty array of type System.Type,if no interfaces are implemented or 

    inherited by the current System.Type.
  """
  pass
 def GetMember(self,name,*__args):
  """
  GetMember(self: Type,name: str,type: MemberTypes,bindingAttr: BindingFlags) -> Array[MemberInfo]

  

   Searches for the specified members of the specified member type,using the specified binding 

    constraints.

  

  

   name: The string containing the name of the members to get.

   type: The value to search for.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return an empty array.

  

   Returns: An array of System.Reflection.MemberInfo objects representing the public members with the 

    specified name,if found; otherwise,an empty array.

  

  GetMember(self: Type,name: str,bindingAttr: BindingFlags) -> Array[MemberInfo]

  

   Searches for the specified members,using the specified binding constraints.

  

   name: The string containing the name of the members to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return an empty array.

  

   Returns: An array of System.Reflection.MemberInfo objects representing the public members with the 

    specified name,if found; otherwise,an empty array.

  

  GetMember(self: Type,name: str) -> Array[MemberInfo]

  

   Searches for the public members with the specified name.

  

   name: The string containing the name of the public members to get.

   Returns: An array of System.Reflection.MemberInfo objects representing the public members with the 

    specified name,if found; otherwise,an empty array.
  """
  pass
 def GetMembers(self,bindingAttr=None):
  """
  GetMembers(self: Type,bindingAttr: BindingFlags) -> Array[MemberInfo]

  

   When overridden in a derived class,searches for the members defined for the current 

    System.Type,using the specified binding constraints.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An array of System.Reflection.MemberInfo objects representing all members defined for the 

    current System.Type that match the specified binding constraints.-or- An empty array of type 

    System.Reflection.MemberInfo,if no members are defined for the current System.Type,or if none 

    of the defined members match the binding constraints.

  

  GetMembers(self: Type) -> Array[MemberInfo]

  

   Returns all the public members of the current System.Type.

   Returns: An array of System.Reflection.MemberInfo objects representing all the public members of the 

    current System.Type.-or- An empty array of type System.Reflection.MemberInfo,if the current 

    System.Type does not have public members.
  """
  pass
 def GetMethod(self,name,*__args):
  """
  GetMethod(self: Type,name: str,types: Array[Type]) -> MethodInfo

  

   Searches for the specified public method whose parameters match the specified argument types.

  

   name: The string containing the name of the public method to get.

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the method to get.-or- An empty array of System.Type objects (as provided by the 

    System.Type.EmptyTypes field) to get a method that takes no parameters.

  

   Returns: An object representing the public method whose parameters match the specified argument types,if 

    found; otherwise,null.

  

  GetMethod(self: Type,name: str,bindingAttr: BindingFlags) -> MethodInfo

  

   Searches for the specified method,using the specified binding constraints.

  

   name: The string containing the name of the method to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An object representing the method that matches the specified requirements,if found; otherwise,

    null.

  

  GetMethod(self: Type,name: str) -> MethodInfo

  

   Searches for the public method with the specified name.

  

   name: The string containing the name of the public method to get.

   Returns: An object that represents the public method with the specified name,if found; otherwise,null.

  GetMethod(self: Type,name: str,bindingAttr: BindingFlags,binder: Binder,callConvention: CallingConventions,types: Array[Type],modifiers: Array[ParameterModifier]) -> MethodInfo

  

   Searches for the specified method whose parameters match the specified argument types and 

    modifiers,using the specified binding constraints and the specified calling convention.

  

  

   name: The string containing the name of the method to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   binder: An object that defines a set of properties and enables binding,which can involve selection of 

    an overloaded method,coercion of argument types,and invocation of a member through 

    reflection.-or- A null reference (Nothing in Visual Basic),to use the 

    System.Type.DefaultBinder.

  

   callConvention: The object that specifies the set of rules to use regarding the order and layout of arguments,

    how the return value is passed,what registers are used for arguments,and how the stack is 

    cleaned up.

  

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the method to get.-or- An empty array of System.Type objects (as provided by the 

    System.Type.EmptyTypes field) to get a method that takes no parameters.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the types array. To be only used when calling through COM 

    interop,and only parameters that are passed by reference are handled. The default binder does 

    not process this parameter.

  

   Returns: An object representing the method that matches the specified requirements,if found; otherwise,

    null.

  

  GetMethod(self: Type,name: str,bindingAttr: BindingFlags,binder: Binder,types: Array[Type],modifiers: Array[ParameterModifier]) -> MethodInfo

  

   Searches for the specified method whose parameters match the specified argument types and 

    modifiers,using the specified binding constraints.

  

  

   name: The string containing the name of the method to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   binder: An object that defines a set of properties and enables binding,which can involve selection of 

    an overloaded method,coercion of argument types,and invocation of a member through 

    reflection.-or- A null reference (Nothing in Visual Basic),to use the 

    System.Type.DefaultBinder.

  

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the method to get.-or- An empty array of System.Type objects (as provided by the 

    System.Type.EmptyTypes field) to get a method that takes no parameters.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the types array. To be only used when calling through COM 

    interop,and only parameters that are passed by reference are handled. The default binder does 

    not process this parameter.

  

   Returns: An object representing the method that matches the specified requirements,if found; otherwise,

    null.

  

  GetMethod(self: Type,name: str,types: Array[Type],modifiers: Array[ParameterModifier]) -> MethodInfo

  

   Searches for the specified public method whose parameters match the specified argument types and 

    modifiers.

  

  

   name: The string containing the name of the public method to get.

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the method to get.-or- An empty array of System.Type objects (as provided by the 

    System.Type.EmptyTypes field) to get a method that takes no parameters.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the types array. To be only used when calling through COM 

    interop,and only parameters that are passed by reference are handled. The default binder does 

    not process this parameter.

  

   Returns: An object representing the public method that matches the specified requirements,if found; 

    otherwise,null.
  """
  pass
 def GetMethodImpl(self,*args):
  """
  GetMethodImpl(self: Type,name: str,bindingAttr: BindingFlags,binder: Binder,callConvention: CallingConventions,types: Array[Type],modifiers: Array[ParameterModifier]) -> MethodInfo

  

   When overridden in a derived class,searches for the specified method whose parameters match the 

    specified argument types and modifiers,using the specified binding constraints and the 

    specified calling convention.

  

  

   name: The string containing the name of the method to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   binder: An object that defines a set of properties and enables binding,which can involve selection of 

    an overloaded method,coercion of argument types,and invocation of a member through 

    reflection.-or- A null reference (Nothing in Visual Basic),to use the 

    System.Type.DefaultBinder.

  

   callConvention: The object that specifies the set of rules to use regarding the order and layout of arguments,

    how the return value is passed,what registers are used for arguments,and what process cleans 

    up the stack.

  

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the method to get.-or- An empty array of the type System.Type (that is,Type[] types=new 

    Type[0]) to get a method that takes no parameters.-or- null. If types is null,arguments are not 

    matched.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the types array. The default binder does not process this 

    parameter.

  

   Returns: An object representing the method that matches the specified requirements,if found; otherwise,

    null.
  """
  pass
 def GetMethods(self,bindingAttr=None):
  """
  GetMethods(self: Type) -> Array[MethodInfo]

  

   Returns all the public methods of the current System.Type.

   Returns: An array of System.Reflection.MethodInfo objects representing all the public methods defined for 

    the current System.Type.-or- An empty array of type System.Reflection.MethodInfo,if no public 

    methods are defined for the current System.Type.

  

  GetMethods(self: Type,bindingAttr: BindingFlags) -> Array[MethodInfo]

  

   When overridden in a derived class,searches for the methods defined for the current 

    System.Type,using the specified binding constraints.

  

  

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
  GetNestedType(self: Type,name: str,bindingAttr: BindingFlags) -> Type

  

   When overridden in a derived class,searches for the specified nested type,using the specified 

    binding constraints.

  

  

   name: The string containing the name of the nested type to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An object representing the nested type that matches the specified requirements,if found; 

    otherwise,null.

  

  GetNestedType(self: Type,name: str) -> Type

  

   Searches for the public nested type with the specified name.

  

   name: The string containing the name of the nested type to get.

   Returns: An object representing the public nested type with the specified name,if found; otherwise,null.
  """
  pass
 def GetNestedTypes(self,bindingAttr=None):
  """
  GetNestedTypes(self: Type,bindingAttr: BindingFlags) -> Array[Type]

  

   When overridden in a derived class,searches for the types nested in the current System.Type,

    using the specified binding constraints.

  

  

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An array of System.Type objects representing all the types nested in the current System.Type 

    that match the specified binding constraints (the search is not recursive),or an empty array of 

    type System.Type,if no nested types are found that match the binding constraints.

  

  GetNestedTypes(self: Type) -> Array[Type]

  

   Returns the public types nested in the current System.Type.

   Returns: An array of System.Type objects representing the public types nested in the current System.Type 

    (the search is not recursive),or an empty array of type System.Type if no public types are 

    nested in the current System.Type.
  """
  pass
 def GetProperties(self,bindingAttr=None):
  """
  GetProperties(self: Type) -> Array[PropertyInfo]

  

   Returns all the public properties of the current System.Type.

   Returns: An array of System.Reflection.PropertyInfo objects representing all public properties of the 

    current System.Type.-or- An empty array of type System.Reflection.PropertyInfo,if the current 

    System.Type does not have public properties.

  

  GetProperties(self: Type,bindingAttr: BindingFlags) -> Array[PropertyInfo]

  

   When overridden in a derived class,searches for the properties of the current System.Type,

    using the specified binding constraints.

  

  

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
  GetProperty(self: Type,name: str,types: Array[Type]) -> PropertyInfo

  

   Searches for the specified public property whose parameters match the specified argument types.

  

   name: The string containing the name of the public property to get.

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the indexed property to get.-or- An empty array of the type System.Type (that is,Type[] types=

    new Type[0]) to get a property that is not indexed.

  

   Returns: An object representing the public property whose parameters match the specified argument types,

    if found; otherwise,null.

  

  GetProperty(self: Type,name: str,returnType: Type) -> PropertyInfo

  

   Searches for the public property with the specified name and return type.

  

   name: The string containing the name of the public property to get.

   returnType: The return type of the property.

   Returns: An object representing the public property with the specified name,if found; otherwise,null.

  GetProperty(self: Type,name: str) -> PropertyInfo

  

   Searches for the public property with the specified name.

  

   name: The string containing the name of the public property to get.

   Returns: An object representing the public property with the specified name,if found; otherwise,null.

  GetProperty(self: Type,name: str,returnType: Type,types: Array[Type]) -> PropertyInfo

  

   Searches for the specified public property whose parameters match the specified argument types.

  

   name: The string containing the name of the public property to get.

   returnType: The return type of the property.

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the indexed property to get.-or- An empty array of the type System.Type (that is,Type[] types=

    new Type[0]) to get a property that is not indexed.

  

   Returns: An object representing the public property whose parameters match the specified argument types,

    if found; otherwise,null.

  

  GetProperty(self: Type,name: str,bindingAttr: BindingFlags,binder: Binder,returnType: Type,types: Array[Type],modifiers: Array[ParameterModifier]) -> PropertyInfo

  

   Searches for the specified property whose parameters match the specified argument types and 

    modifiers,using the specified binding constraints.

  

  

   name: The string containing the name of the property to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   binder: An object that defines a set of properties and enables binding,which can involve selection of 

    an overloaded method,coercion of argument types,and invocation of a member through 

    reflection.-or- A null reference (Nothing in Visual Basic),to use the 

    System.Type.DefaultBinder.

  

   returnType: The return type of the property.

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the indexed property to get.-or- An empty array of the type System.Type (that is,Type[] types=

    new Type[0]) to get a property that is not indexed.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the types array. The default binder does not process this 

    parameter.

  

   Returns: An object representing the property that matches the specified requirements,if found; 

    otherwise,null.

  

  GetProperty(self: Type,name: str,returnType: Type,types: Array[Type],modifiers: Array[ParameterModifier]) -> PropertyInfo

  

   Searches for the specified public property whose parameters match the specified argument types 

    and modifiers.

  

  

   name: The string containing the name of the public property to get.

   returnType: The return type of the property.

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the indexed property to get.-or- An empty array of the type System.Type (that is,Type[] types=

    new Type[0]) to get a property that is not indexed.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the types array. The default binder does not process this 

    parameter.

  

   Returns: An object representing the public property that matches the specified requirements,if found; 

    otherwise,null.

  

  GetProperty(self: Type,name: str,bindingAttr: BindingFlags) -> PropertyInfo

  

   Searches for the specified property,using the specified binding constraints.

  

   name: The string containing the name of the property to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   Returns: An object representing the property that matches the specified requirements,if found; 

    otherwise,null.
  """
  pass
 def GetPropertyImpl(self,*args):
  """
  GetPropertyImpl(self: Type,name: str,bindingAttr: BindingFlags,binder: Binder,returnType: Type,types: Array[Type],modifiers: Array[ParameterModifier]) -> PropertyInfo

  

   When overridden in a derived class,searches for the specified property whose parameters match 

    the specified argument types and modifiers,using the specified binding constraints.

  

  

   name: The string containing the name of the property to get.

   bindingAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted.-or- Zero,to return null.

  

   binder: An object that defines a set of properties and enables binding,which can involve selection of 

    an overloaded member,coercion of argument types,and invocation of a member through 

    reflection.-or- A null reference (Nothing in Visual Basic),to use the 

    System.Type.DefaultBinder.

  

   returnType: The return type of the property.

   types: An array of System.Type objects representing the number,order,and type of the parameters for 

    the indexed property to get.-or- An empty array of the type System.Type (that is,Type[] types=

    new Type[0]) to get a property that is not indexed.

  

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the types array. The default binder does not process this 

    parameter.

  

   Returns: An object representing the property that matches the specified requirements,if found; 

    otherwise,null.
  """
  pass
 def GetType(self,typeName=None,*__args):
  """
  GetType(typeName: str,assemblyResolver: Func[AssemblyName,Assembly],typeResolver: Func[Assembly,str,bool,Type],throwOnError: bool) -> Type

  GetType(typeName: str,assemblyResolver: Func[AssemblyName,Assembly],typeResolver: Func[Assembly,str,bool,Type],throwOnError: bool,ignoreCase: bool) -> Type

  GetType(self: Type) -> Type

  

   Gets the current System.Type.

   Returns: The current System.Type.

  GetType(typeName: str,assemblyResolver: Func[AssemblyName,Assembly],typeResolver: Func[Assembly,str,bool,Type]) -> Type

  GetType(typeName: str,throwOnError: bool,ignoreCase: bool) -> Type

  

   Gets the System.Type with the specified name,specifying whether to perform a case-sensitive 

    search and whether to throw an exception if the type is not found.

  

  

   typeName: The assembly-qualified name of the type to get. See System.Type.AssemblyQualifiedName. If the 

    type is in the currently executing assembly or in Mscorlib.dll,it is sufficient to supply the 

    type name qualified by its namespace.

  

   throwOnError: true to throw an exception if the type cannot be found; false to return null.Specifying false 

    also suppresses some other exception conditions,but not all of them. See the Exceptions 

    section.

  

   ignoreCase: true to perform a case-insensitive search for typeName,false to perform a case-sensitive search 

    for typeName.

  

   Returns: The type with the specified name. If the type is not found,the throwOnError parameter specifies 

    whether null is returned or an exception is thrown. In some cases,an exception is thrown 

    regardless of the value of throwOnError. See the Exceptions section.

  

  GetType(typeName: str,throwOnError: bool) -> Type

  

   Gets the System.Type with the specified name,performing a case-sensitive search and specifying 

    whether to throw an exception if the type is not found.

  

  

   typeName: The assembly-qualified name of the type to get. See System.Type.AssemblyQualifiedName. If the 

    type is in the currently executing assembly or in Mscorlib.dll,it is sufficient to supply the 

    type name qualified by its namespace.

  

   throwOnError: true to throw an exception if the type cannot be found; false to return null. Specifying false 

    also suppresses some other exception conditions,but not all of them. See the Exceptions 

    section.

  

   Returns: The type with the specified name. If the type is not found,the throwOnError parameter specifies 

    whether null is returned or an exception is thrown. In some cases,an exception is thrown 

    regardless of the value of throwOnError. See the Exceptions section.

  

  GetType(typeName: str) -> Type

  

   Gets the System.Type with the specified name,performing a case-sensitive search.

  

   typeName: The assembly-qualified name of the type to get. See System.Type.AssemblyQualifiedName. If the 

    type is in the currently executing assembly or in Mscorlib.dll,it is sufficient to supply the 

    type name qualified by its namespace.

  

   Returns: The type with the specified name,if found; otherwise,null.
  """
  pass
 @staticmethod
 def GetTypeArray(args):
  """
  GetTypeArray(args: Array[object]) -> Array[Type]

  

   Gets the types of the objects in the specified array.

  

   args: An array of objects whose types to determine.

   Returns: An array of System.Type objects representing the types of the corresponding elements in args.
  """
  pass
 @staticmethod
 def GetTypeCode(type):
  """
  GetTypeCode(type: Type) -> TypeCode

  

   Gets the underlying type code of the specified System.Type.

  

   type: The type whose underlying type code to get.

   Returns: The code of the underlying type.
  """
  pass
 def GetTypeCodeImpl(self,*args):
  """
  GetTypeCodeImpl(self: Type) -> TypeCode

  

   Returns the underlying type code of the specified System.Type.

   Returns: The code of the underlying type.
  """
  pass
 @staticmethod
 def GetTypeFromCLSID(clsid,*__args):
  """
  GetTypeFromCLSID(clsid: Guid,server: str) -> Type

  

   Gets the type associated with the specified class identifier (CLSID) from the specified server.

  

   clsid: The CLSID of the type to get.

   server: The server from which to load the type. If the server name is null,this method automatically 

    reverts to the local machine.

  

   Returns: System.__ComObject regardless of whether the CLSID is valid.

  GetTypeFromCLSID(clsid: Guid,server: str,throwOnError: bool) -> Type

  

   Gets the type associated with the specified class identifier (CLSID) from the specified server,

    specifying whether to throw an exception if an error occurs while loading the type.

  

  

   clsid: The CLSID of the type to get.

   server: The server from which to load the type. If the server name is null,this method automatically 

    reverts to the local machine.

  

   throwOnError: true to throw any exception that occurs.-or- false to ignore any exception that occurs.

   Returns: System.__ComObject regardless of whether the CLSID is valid.

  GetTypeFromCLSID(clsid: Guid) -> Type

  

   Gets the type associated with the specified class identifier (CLSID).

  

   clsid: The CLSID of the type to get.

   Returns: System.__ComObject regardless of whether the CLSID is valid.

  GetTypeFromCLSID(clsid: Guid,throwOnError: bool) -> Type

  

   Gets the type associated with the specified class identifier (CLSID),specifying whether to 

    throw an exception if an error occurs while loading the type.

  

  

   clsid: The CLSID of the type to get.

   throwOnError: true to throw any exception that occurs.-or- false to ignore any exception that occurs.

   Returns: System.__ComObject regardless of whether the CLSID is valid.
  """
  pass
 @staticmethod
 def GetTypeFromHandle(handle):
  """
  GetTypeFromHandle(handle: RuntimeTypeHandle) -> Type

  

   Gets the type referenced by the specified type handle.

  

   handle: The object that refers to the type.

   Returns: The type referenced by the specified System.RuntimeTypeHandle,or null if the 

    System.RuntimeTypeHandle.Value property of handle is null.
  """
  pass
 @staticmethod
 def GetTypeFromProgID(progID,*__args):
  """
  GetTypeFromProgID(progID: str,server: str) -> Type

  

   Gets the type associated with the specified program identifier (progID) from the specified 

    server,returning null if an error is encountered while loading the type.

  

  

   progID: The progID of the type to get.

   server: The server from which to load the type. If the server name is null,this method automatically 

    reverts to the local machine.

  

   Returns: The type associated with the specified program identifier (progID),if progID is a valid entry 

    in the registry and a type is associated with it; otherwise,null.

  

  GetTypeFromProgID(progID: str,server: str,throwOnError: bool) -> Type

  

   Gets the type associated with the specified program identifier (progID) from the specified 

    server,specifying whether to throw an exception if an error occurs while loading the type.

  

  

   progID: The progID of the System.Type to get.

   server: The server from which to load the type. If the server name is null,this method automatically 

    reverts to the local machine.

  

   throwOnError: true to throw any exception that occurs.-or- false to ignore any exception that occurs.

   Returns: The type associated with the specified program identifier (progID),if progID is a valid entry 

    in the registry and a type is associated with it; otherwise,null.

  

  GetTypeFromProgID(progID: str) -> Type

  

   Gets the type associated with the specified program identifier (ProgID),returning null if an 

    error is encountered while loading the System.Type.

  

  

   progID: The ProgID of the type to get.

   Returns: The type associated with the specified ProgID,if progID is a valid entry in the registry and a 

    type is associated with it; otherwise,null.

  

  GetTypeFromProgID(progID: str,throwOnError: bool) -> Type

  

   Gets the type associated with the specified program identifier (ProgID),specifying whether to 

    throw an exception if an error occurs while loading the type.

  

  

   progID: The ProgID of the type to get.

   throwOnError: true to throw any exception that occurs.-or- false to ignore any exception that occurs.

   Returns: The type associated with the specified program identifier (ProgID),if progID is a valid entry 

    in the registry and a type is associated with it; otherwise,null.
  """
  pass
 @staticmethod
 def GetTypeHandle(o):
  """
  GetTypeHandle(o: object) -> RuntimeTypeHandle

  

   Gets the handle for the System.Type of a specified object.

  

   o: The object for which to get the type handle.

   Returns: The handle for the System.Type of the specified System.Object.
  """
  pass
 def HasElementTypeImpl(self,*args):
  """
  HasElementTypeImpl(self: Type) -> bool

  

   When overridden in a derived class,implements the System.Type.HasElementType property and 

    determines whether the current System.Type encompasses or refers to another type; that is,

    whether the current System.Type is an array,a pointer,or is passed by reference.

  

   Returns: true if the System.Type is an array,a pointer,or is passed by reference; otherwise,false.
  """
  pass
 def InvokeMember(self,name,invokeAttr,binder,target,args,*__args):
  """
  InvokeMember(self: Type,name: str,invokeAttr: BindingFlags,binder: Binder,target: object,args: Array[object]) -> object

  

   Invokes the specified member,using the specified binding constraints and matching the specified 

    argument list.

  

  

   name: The string containing the name of the constructor,method,property,or field member to 

    invoke.-or- An empty string ("") to invoke the default member. -or-For IDispatch members,a 

    string representing the DispID,for example "[DispID=3]".

  

   invokeAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted. The access can be one of the BindingFlags such as Public,NonPublic,Private,

    InvokeMethod,GetField,and so on. The type of lookup need not be specified. If the type of 

    lookup is omitted,BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static are used.

  

   binder: An object that defines a set of properties and enables binding,which can involve selection of 

    an overloaded method,coercion of argument types,and invocation of a member through 

    reflection.-or- A null reference (Nothing in Visual Basic),to use the 

    System.Type.DefaultBinder. Note that explicitly defining a System.Reflection.Binder object may 

    be required for successfully invoking method overloads with variable arguments.

  

   target: The object on which to invoke the specified member.

   args: An array containing the arguments to pass to the member to invoke.

   Returns: An object representing the return value of the invoked member.

  InvokeMember(self: Type,name: str,invokeAttr: BindingFlags,binder: Binder,target: object,args: Array[object],culture: CultureInfo) -> object

  

   Invokes the specified member,using the specified binding constraints and matching the specified 

    argument list and culture.

  

  

   name: The string containing the name of the constructor,method,property,or field member to 

    invoke.-or- An empty string ("") to invoke the default member. -or-For IDispatch members,a 

    string representing the DispID,for example "[DispID=3]".

  

   invokeAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted. The access can be one of the BindingFlags such as Public,NonPublic,Private,

    InvokeMethod,GetField,and so on. The type of lookup need not be specified. If the type of 

    lookup is omitted,BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static are used.

  

   binder: An object that defines a set of properties and enables binding,which can involve selection of 

    an overloaded method,coercion of argument types,and invocation of a member through 

    reflection.-or- A null reference (Nothing in Visual Basic),to use the 

    System.Type.DefaultBinder. Note that explicitly defining a System.Reflection.Binder object may 

    be required for successfully invoking method overloads with variable arguments.

  

   target: The object on which to invoke the specified member.

   args: An array containing the arguments to pass to the member to invoke.

   culture: The object representing the globalization locale to use,which may be necessary for 

    locale-specific conversions,such as converting a numeric System.String to a System.Double.-or- 

    A null reference (Nothing in Visual Basic) to use the current thread's 

    System.Globalization.CultureInfo.

  

   Returns: An object representing the return value of the invoked member.

  InvokeMember(self: Type,name: str,invokeAttr: BindingFlags,binder: Binder,target: object,args: Array[object],modifiers: Array[ParameterModifier],culture: CultureInfo,namedParameters: Array[str]) -> object

  

   When overridden in a derived class,invokes the specified member,using the specified binding 

    constraints and matching the specified argument list,modifiers and culture.

  

  

   name: The string containing the name of the constructor,method,property,or field member to 

    invoke.-or- An empty string ("") to invoke the default member. -or-For IDispatch members,a 

    string representing the DispID,for example "[DispID=3]".

  

   invokeAttr: A bitmask comprised of one or more System.Reflection.BindingFlags that specify how the search is 

    conducted. The access can be one of the BindingFlags such as Public,NonPublic,Private,

    InvokeMethod,GetField,and so on. The type of lookup need not be specified. If the type of 

    lookup is omitted,BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static are used.

  

   binder: An object that defines a set of properties and enables binding,which can involve selection of 

    an overloaded method,coercion of argument types,and invocation of a member through 

    reflection.-or- A null reference (Nothing in Visual Basic),to use the 

    System.Type.DefaultBinder. Note that explicitly defining a System.Reflection.Binder object may 

    be required for successfully invoking method overloads with variable arguments.

  

   target: The object on which to invoke the specified member.

   args: An array containing the arguments to pass to the member to invoke.

   modifiers: An array of System.Reflection.ParameterModifier objects representing the attributes associated 

    with the corresponding element in the args array. A parameter's associated attributes are stored 

    in the member's signature. The default binder processes this parameter only when calling a COM 

    component.

  

   culture: The System.Globalization.CultureInfo object representing the globalization locale to use,which 

    may be necessary for locale-specific conversions,such as converting a numeric String to a 

    Double.-or- A null reference (Nothing in Visual Basic) to use the current thread's 

    System.Globalization.CultureInfo.

  

   namedParameters: An array containing the names of the parameters to which the values in the args array are passed.

   Returns: An object representing the return value of the invoked member.
  """
  pass
 def IsArrayImpl(self,*args):
  """
  IsArrayImpl(self: Type) -> bool

  

   When overridden in a derived class,implements the System.Type.IsArray property and determines 

    whether the System.Type is an array.

  

   Returns: true if the System.Type is an array; otherwise,false.
  """
  pass
 def IsAssignableFrom(self,c):
  """
  IsAssignableFrom(self: Type,c: Type) -> bool

  

   Determines whether an instance of the current System.Type can be assigned from an instance of 

    the specified Type.

  

  

   c: The type to compare with the current type.

   Returns: true if c and the current Type represent the same type,or if the current Type is in the 

    inheritance hierarchy of c,or if the current Type is an interface that c implements,or if c is 

    a generic type parameter and the current Type represents one of the constraints of c. false if 

    none of these conditions are true,or if c is null.
  """
  pass
 def IsByRefImpl(self,*args):
  """
  IsByRefImpl(self: Type) -> bool

  

   When overridden in a derived class,implements the System.Type.IsByRef property and determines 

    whether the System.Type is passed by reference.

  

   Returns: true if the System.Type is passed by reference; otherwise,false.
  """
  pass
 def IsCOMObjectImpl(self,*args):
  """
  IsCOMObjectImpl(self: Type) -> bool

  

   When overridden in a derived class,implements the System.Type.IsCOMObject property and 

    determines whether the System.Type is a COM object.

  

   Returns: true if the System.Type is a COM object; otherwise,false.
  """
  pass
 def IsContextfulImpl(self,*args):
  """
  IsContextfulImpl(self: Type) -> bool

  

   Implements the System.Type.IsContextful property and determines whether the System.Type can be 

    hosted in a context.

  

   Returns: true if the System.Type can be hosted in a context; otherwise,false.
  """
  pass
 def IsEnumDefined(self,value):
  """
  IsEnumDefined(self: Type,value: object) -> bool

  

   Returns a value that indicates whether the specified value exists in the current enumeration 

    type.

  

  

   value: The value to be tested.

   Returns: true if the specified value is a member of the current enumeration type; otherwise,false.
  """
  pass
 def IsEquivalentTo(self,other):
  """
  IsEquivalentTo(self: Type,other: Type) -> bool

  

   Determines whether two COM types have the same identity and are eligible for type equivalence.

  

   other: The COM type that is tested for equivalence with the current type.

   Returns: true if the COM types are equivalent; otherwise,false. This method also returns false if one 

    type is in an assembly that is loaded for execution,and the other is in an assembly that is 

    loaded into the reflection-only context.
  """
  pass
 def IsInstanceOfType(self,o):
  """
  IsInstanceOfType(self: Type,o: object) -> bool

  

   Determines whether the specified object is an instance of the current System.Type.

  

   o: The object to compare with the current type.

   Returns: true if the current Type is in the inheritance hierarchy of the object represented by o,or if 

    the current Type is an interface that o supports. false if neither of these conditions is the 

    case,or if o is null,or if the current Type is an open generic type (that is,

    System.Type.ContainsGenericParameters returns true).
  """
  pass
 def IsMarshalByRefImpl(self,*args):
  """
  IsMarshalByRefImpl(self: Type) -> bool

  

   Implements the System.Type.IsMarshalByRef property and determines whether the System.Type is 

    marshaled by reference.

  

   Returns: true if the System.Type is marshaled by reference; otherwise,false.
  """
  pass
 def IsPointerImpl(self,*args):
  """
  IsPointerImpl(self: Type) -> bool

  

   When overridden in a derived class,implements the System.Type.IsPointer property and determines 

    whether the System.Type is a pointer.

  

   Returns: true if the System.Type is a pointer; otherwise,false.
  """
  pass
 def IsPrimitiveImpl(self,*args):
  """
  IsPrimitiveImpl(self: Type) -> bool

  

   When overridden in a derived class,implements the System.Type.IsPrimitive property and 

    determines whether the System.Type is one of the primitive types.

  

   Returns: true if the System.Type is one of the primitive types; otherwise,false.
  """
  pass
 def IsSubclassOf(self,c):
  """
  IsSubclassOf(self: Type,c: Type) -> bool

  

   Determines whether the class represented by the current System.Type derives from the class 

    represented by the specified System.Type.

  

  

   c: The type to compare with the current type.

   Returns: true if the Type represented by the c parameter and the current Type represent classes,and the 

    class represented by the current Type derives from the class represented by c; otherwise,false. 

    This method also returns false if c and the current Type represent the same class.
  """
  pass
 def IsValueTypeImpl(self,*args):
  """
  IsValueTypeImpl(self: Type) -> bool

  

   Implements the System.Type.IsValueType property and determines whether the System.Type is a 

    value type; that is,not a class or an interface.

  

   Returns: true if the System.Type is a value type; otherwise,false.
  """
  pass
 def MakeArrayType(self,rank=None):
  """
  MakeArrayType(self: Type,rank: int) -> Type

  

   Returns a System.Type object representing an array of the current type,with the specified 

    number of dimensions.

  

  

   rank: The number of dimensions for the array. This number must be less than or equal to 32.

   Returns: An object representing an array of the current type,with the specified number of dimensions.

  MakeArrayType(self: Type) -> Type

  

   Returns a System.Type object representing a one-dimensional array of the current type,with a 

    lower bound of zero.

  

   Returns: A System.Type object representing a one-dimensional array of the current type,with a lower 

    bound of zero.
  """
  pass
 def MakeByRefType(self):
  """
  MakeByRefType(self: Type) -> Type

  

   Returns a System.Type object that represents the current type when passed as a ref parameter 

    (ByRef parameter in Visual Basic).

  

   Returns: A System.Type object that represents the current type when passed as a ref parameter (ByRef 

    parameter in Visual Basic).
  """
  pass
 def MakeGenericType(self,typeArguments):
  """
  MakeGenericType(self: Type,*typeArguments: Array[Type]) -> Type

  

   Substitutes the elements of an array of types for the type parameters of the current generic 

    type definition and returns a System.Type object representing the resulting constructed type.

  

  

   typeArguments: An array of types to be substituted for the type parameters of the current generic type.

   Returns: A System.Type representing the constructed type formed by substituting the elements of 

    typeArguments for the type parameters of the current generic type.
  """
  pass
 def MakePointerType(self):
  """
  MakePointerType(self: Type) -> Type

  

   Returns a System.Type object that represents a pointer to the current type.

   Returns: A System.Type object that represents a pointer to the current type.
  """
  pass
 @staticmethod
 def ReflectionOnlyGetType(typeName,throwIfNotFound,ignoreCase):
  """
  ReflectionOnlyGetType(typeName: str,throwIfNotFound: bool,ignoreCase: bool) -> Type

  

   Gets the System.Type with the specified name,specifying whether to perform a case-sensitive 

    search and whether to throw an exception if the type is not found. The type is loaded for 

    reflection only,not for execution.

  

  

   typeName: The assembly-qualified name of the System.Type to get.

   throwIfNotFound: true to throw a System.TypeLoadException if the type cannot be found; false to return null if 

    the type cannot be found. Specifying false also suppresses some other exception conditions,but 

    not all of them. See the Exceptions section.

  

   ignoreCase: true to perform a case-insensitive search for typeName; false to perform a case-sensitive search 

    for typeName.

  

   Returns: The type with the specified name,if found; otherwise,null. If the type is not found,the 

    throwIfNotFound parameter specifies whether null is returned or an exception is thrown. In some 

    cases,an exception is thrown regardless of the value of throwIfNotFound. See the Exceptions 

    section.
  """
  pass
 def ToString(self):
  """
  ToString(self: Type) -> str

  

   Returns a String representing the name of the current Type.

   Returns: A System.String representing the name of the current System.Type.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Assembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Reflection.Assembly in which the type is declared. For generic types,gets the System.Reflection.Assembly in which the generic type is defined.



Get: Assembly(self: Type) -> Assembly



"""

 AssemblyQualifiedName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the assembly-qualified name of the System.Type,which includes the name of the assembly from which the System.Type was loaded.



Get: AssemblyQualifiedName(self: Type) -> str



"""

 Attributes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the attributes associated with the System.Type.



Get: Attributes(self: Type) -> TypeAttributes



"""

 BaseType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type from which the current System.Type directly inherits.



Get: BaseType(self: Type) -> Type



"""

 ContainsGenericParameters=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current System.Type object has type parameters that have not been replaced by specific types.



Get: ContainsGenericParameters(self: Type) -> bool



"""

 DeclaringMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Reflection.MethodBase that represents the declaring method,if the current System.Type represents a type parameter of a generic method.



Get: DeclaringMethod(self: Type) -> MethodBase



"""

 DeclaringType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type that declares the current nested type or generic type parameter.



Get: DeclaringType(self: Type) -> Type



"""

 FullName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the fully qualified name of the System.Type,including the namespace of the System.Type but not the assembly.



Get: FullName(self: Type) -> str



"""

 GenericParameterAttributes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a combination of System.Reflection.GenericParameterAttributes flags that describe the covariance and special constraints of the current generic type parameter.



Get: GenericParameterAttributes(self: Type) -> GenericParameterAttributes



"""

 GenericParameterPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the position of the type parameter in the type parameter list of the generic type or method that declared the parameter,when the System.Type object represents a type parameter of a generic type or a generic method.



Get: GenericParameterPosition(self: Type) -> int



"""

 GenericTypeArguments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GenericTypeArguments(self: Type) -> Array[Type]



"""

 GUID=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the GUID associated with the System.Type.



Get: GUID(self: Type) -> Guid



"""

 HasElementType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current System.Type encompasses or refers to another type; that is,whether the current System.Type is an array,a pointer,or is passed by reference.



Get: HasElementType(self: Type) -> bool



"""

 IsAbstract=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is abstract and must be overridden.



Get: IsAbstract(self: Type) -> bool



"""

 IsAnsiClass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the string format attribute AnsiClass is selected for the System.Type.



Get: IsAnsiClass(self: Type) -> bool



"""

 IsArray=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is an array.



Get: IsArray(self: Type) -> bool



"""

 IsAutoClass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the string format attribute AutoClass is selected for the System.Type.



Get: IsAutoClass(self: Type) -> bool



"""

 IsAutoLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the class layout attribute AutoLayout is selected for the System.Type.



Get: IsAutoLayout(self: Type) -> bool



"""

 IsByRef=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is passed by reference.



Get: IsByRef(self: Type) -> bool



"""

 IsClass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is a class; that is,not a value type or interface.



Get: IsClass(self: Type) -> bool



"""

 IsCOMObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is a COM object.



Get: IsCOMObject(self: Type) -> bool



"""

 IsConstructedGenericType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsConstructedGenericType(self: Type) -> bool



"""

 IsContextful=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type can be hosted in a context.



Get: IsContextful(self: Type) -> bool



"""

 IsEnum=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current System.Type represents an enumeration.



Get: IsEnum(self: Type) -> bool



"""

 IsExplicitLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the class layout attribute ExplicitLayout is selected for the System.Type.



Get: IsExplicitLayout(self: Type) -> bool



"""

 IsGenericParameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current System.Type represents a type parameter in the definition of a generic type or method.



Get: IsGenericParameter(self: Type) -> bool



"""

 IsGenericType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current type is a generic type.



Get: IsGenericType(self: Type) -> bool



"""

 IsGenericTypeDefinition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current System.Type represents a generic type definition,from which other generic types can be constructed.



Get: IsGenericTypeDefinition(self: Type) -> bool



"""

 IsImport=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type has a System.Runtime.InteropServices.ComImportAttribute attribute applied,indicating that it was imported from a COM type library.



Get: IsImport(self: Type) -> bool



"""

 IsInterface=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is an interface; that is,not a class or a value type.



Get: IsInterface(self: Type) -> bool



"""

 IsLayoutSequential=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the class layout attribute SequentialLayout is selected for the System.Type.



Get: IsLayoutSequential(self: Type) -> bool



"""

 IsMarshalByRef=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is marshaled by reference.



Get: IsMarshalByRef(self: Type) -> bool



"""

 IsNested=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current System.Type object represents a type whose definition is nested inside the definition of another type.



Get: IsNested(self: Type) -> bool



"""

 IsNestedAssembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is nested and visible only within its own assembly.



Get: IsNestedAssembly(self: Type) -> bool



"""

 IsNestedFamANDAssem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is nested and visible only to classes that belong to both its own family and its own assembly.



Get: IsNestedFamANDAssem(self: Type) -> bool



"""

 IsNestedFamily=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is nested and visible only within its own family.



Get: IsNestedFamily(self: Type) -> bool



"""

 IsNestedFamORAssem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is nested and visible only to classes that belong to either its own family or to its own assembly.



Get: IsNestedFamORAssem(self: Type) -> bool



"""

 IsNestedPrivate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is nested and declared private.



Get: IsNestedPrivate(self: Type) -> bool



"""

 IsNestedPublic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether a class is nested and declared public.



Get: IsNestedPublic(self: Type) -> bool



"""

 IsNotPublic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is not declared public.



Get: IsNotPublic(self: Type) -> bool



"""

 IsPointer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is a pointer.



Get: IsPointer(self: Type) -> bool



"""

 IsPrimitive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is one of the primitive types.



Get: IsPrimitive(self: Type) -> bool



"""

 IsPublic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is declared public.



Get: IsPublic(self: Type) -> bool



"""

 IsSealed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is declared sealed.



Get: IsSealed(self: Type) -> bool



"""

 IsSecurityCritical=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the current type is security-critical or security-safe-critical at the current trust level,and therefore can perform critical operations.



Get: IsSecurityCritical(self: Type) -> bool



"""

 IsSecuritySafeCritical=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the current type is security-safe-critical at the current trust level; that is,whether it can perform critical operations and can be accessed by transparent code.



Get: IsSecuritySafeCritical(self: Type) -> bool



"""

 IsSecurityTransparent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the current type is transparent at the current trust level,and therefore cannot perform critical operations.



Get: IsSecurityTransparent(self: Type) -> bool



"""

 IsSerializable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is serializable.



Get: IsSerializable(self: Type) -> bool



"""

 IsSpecialName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type has a name that requires special handling.



Get: IsSpecialName(self: Type) -> bool



"""

 IsUnicodeClass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the string format attribute UnicodeClass is selected for the System.Type.



Get: IsUnicodeClass(self: Type) -> bool



"""

 IsValueType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type is a value type.



Get: IsValueType(self: Type) -> bool



"""

 IsVisible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Type can be accessed by code outside the assembly.



Get: IsVisible(self: Type) -> bool



"""

 MemberType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Reflection.MemberTypes value indicating that this member is a type or a nested type.



Get: MemberType(self: Type) -> MemberTypes



"""

 Module=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the module (the DLL) in which the current System.Type is defined.



Get: Module(self: Type) -> Module



"""

 Namespace=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the namespace of the System.Type.



Get: Namespace(self: Type) -> str



"""

 ReflectedType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the class object that was used to obtain this member.



Get: ReflectedType(self: Type) -> Type



"""

 StructLayoutAttribute=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Runtime.InteropServices.StructLayoutAttribute that describes the layout of the current type.



Get: StructLayoutAttribute(self: Type) -> StructLayoutAttribute



"""

 TypeHandle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the handle for the current System.Type.



Get: TypeHandle(self: Type) -> RuntimeTypeHandle



"""

 TypeInitializer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the initializer for the System.Type.



Get: TypeInitializer(self: Type) -> ConstructorInfo



"""

 UnderlyingSystemType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates the type provided by the common language runtime that represents this type.



Get: UnderlyingSystemType(self: Type) -> Type



"""


 DefaultBinder=None
 Delimiter=None
 EmptyTypes=None
 Missing=None

