class Attribute(object,_Attribute):
 """ Represents the base class for custom attributes. """
 def Equals(self,obj):
  """
  Equals(self: Attribute,obj: object) -> bool

  

   Returns a value that indicates whether this instance is equal to a specified object.

  

   obj: An System.Object to compare with this instance or null.

   Returns: true if obj equals the type and value of this instance; otherwise,false.
  """
  pass
 @staticmethod
 def GetCustomAttribute(element,attributeType,inherit=None):
  """
  GetCustomAttribute(element: Module,attributeType: Type,inherit: bool) -> Attribute

  

   Retrieves a custom attribute applied to a module. Parameters specify the module,the type of the 

    custom attribute to search for,and an ignored search option.

  

  

   element: An object derived from the System.Reflection.Module class that describes a portable executable 

    file.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   inherit: This parameter is ignored,and does not affect the operation of this method.

   Returns: A reference to the single custom attribute of type attributeType that is applied to element,or 

    null if there is no such attribute.

  

  GetCustomAttribute(element: Module,attributeType: Type) -> Attribute

  

   Retrieves a custom attribute applied to a module. Parameters specify the module,and the type of 

    the custom attribute to search for.

  

  

   element: An object derived from the System.Reflection.Module class that describes a portable executable 

    file.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   Returns: A reference to the single custom attribute of type attributeType that is applied to element,or 

    null if there is no such attribute.

  

  GetCustomAttribute(element: Assembly,attributeType: Type,inherit: bool) -> Attribute

  

   Retrieves a custom attribute applied to an assembly. Parameters specify the assembly,the type 

    of the custom attribute to search for,and an ignored search option.

  

  

   element: An object derived from the System.Reflection.Assembly class that describes a reusable collection 

    of modules.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   inherit: This parameter is ignored,and does not affect the operation of this method.

   Returns: A reference to the single custom attribute of type attributeType that is applied to element,or 

    null if there is no such attribute.

  

  GetCustomAttribute(element: Assembly,attributeType: Type) -> Attribute

  

   Retrieves a custom attribute applied to a specified assembly. Parameters specify the assembly 

    and the type of the custom attribute to search for.

  

  

   element: An object derived from the System.Reflection.Assembly class that describes a reusable collection 

    of modules.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   Returns: A reference to the single custom attribute of type attributeType that is applied to element,or 

    null if there is no such attribute.

  

  GetCustomAttribute(element: MemberInfo,attributeType: Type,inherit: bool) -> Attribute

  

   Retrieves a custom attribute applied to a member of a type. Parameters specify the member,the 

    type of the custom attribute to search for,and whether to search ancestors of the member.

  

  

   element: An object derived from the System.Reflection.MemberInfo class that describes a constructor,

    event,field,method,or property member of a class.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   inherit: If true,specifies to also search the ancestors of element for custom attributes.

   Returns: A reference to the single custom attribute of type attributeType that is applied to element,or 

    null if there is no such attribute.

  

  GetCustomAttribute(element: MemberInfo,attributeType: Type) -> Attribute

  

   Retrieves a custom attribute applied to a member of a type. Parameters specify the member,and 

    the type of the custom attribute to search for.

  

  

   element: An object derived from the System.Reflection.MemberInfo class that describes a constructor,

    event,field,method,or property member of a class.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   Returns: A reference to the single custom attribute of type attributeType that is applied to element,or 

    null if there is no such attribute.

  

  GetCustomAttribute(element: ParameterInfo,attributeType: Type,inherit: bool) -> Attribute

  

   Retrieves a custom attribute applied to a method parameter. Parameters specify the method 

    parameter,the type of the custom attribute to search for,and whether to search ancestors of 

    the method parameter.

  

  

   element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a 

    member of a class.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   inherit: If true,specifies to also search the ancestors of element for custom attributes.

   Returns: A reference to the single custom attribute of type attributeType that is applied to element,or 

    null if there is no such attribute.

  

  GetCustomAttribute(element: ParameterInfo,attributeType: Type) -> Attribute

  

   Retrieves a custom attribute applied to a method parameter. Parameters specify the method 

    parameter,and the type of the custom attribute to search for.

  

  

   element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a 

    member of a class.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   Returns: A reference to the single custom attribute of type attributeType that is applied to element,or 

    null if there is no such attribute.
  """
  pass
 @staticmethod
 def GetCustomAttributes(element,*__args):
  """
  GetCustomAttributes(element: Module,inherit: bool) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to a module. Parameters specify the module,

    and an ignored search option.

  

  

   element: An object derived from the System.Reflection.Module class that describes a portable executable 

    file.

  

   inherit: This parameter is ignored,and does not affect the operation of this method.

   Returns: An System.Attribute array that contains the custom attributes applied to element,or an empty 

    array if no such custom attributes exist.

  

  GetCustomAttributes(element: Module,attributeType: Type,inherit: bool) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to a module. Parameters specify the module,

    the type of the custom attribute to search for,and an ignored search option.

  

  

   element: An object derived from the System.Reflection.Module class that describes a portable executable 

    file.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   inherit: This parameter is ignored,and does not affect the operation of this method.

   Returns: An System.Attribute array that contains the custom attributes of type attributeType applied to 

    element,or an empty array if no such custom attributes exist.

  

  GetCustomAttributes(element: Module,attributeType: Type) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to a module. Parameters specify the module,

    and the type of the custom attribute to search for.

  

  

   element: An object derived from the System.Reflection.Module class that describes a portable executable 

    file.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   Returns: An System.Attribute array that contains the custom attributes of type attributeType applied to 

    element,or an empty array if no such custom attributes exist.

  

  GetCustomAttributes(element: Module) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to a module. A parameter specifies the 

    module.

  

  

   element: An object derived from the System.Reflection.Module class that describes a portable executable 

    file.

  

   Returns: An System.Attribute array that contains the custom attributes applied to element,or an empty 

    array if no such custom attributes exist.

  

  GetCustomAttributes(element: Assembly) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to an assembly. A parameter specifies the 

    assembly.

  

  

   element: An object derived from the System.Reflection.Assembly class that describes a reusable collection 

    of modules.

  

   Returns: An System.Attribute array that contains the custom attributes applied to element,or an empty 

    array if no such custom attributes exist.

  

  GetCustomAttributes(element: Assembly,inherit: bool) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to an assembly. Parameters specify the 

    assembly,and an ignored search option.

  

  

   element: An object derived from the System.Reflection.Assembly class that describes a reusable collection 

    of modules.

  

   inherit: This parameter is ignored,and does not affect the operation of this method.

   Returns: An System.Attribute array that contains the custom attributes applied to element,or an empty 

    array if no such custom attributes exist.

  

  GetCustomAttributes(element: Assembly,attributeType: Type) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to an assembly. Parameters specify the 

    assembly,and the type of the custom attribute to search for.

  

  

   element: An object derived from the System.Reflection.Assembly class that describes a reusable collection 

    of modules.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   Returns: An System.Attribute array that contains the custom attributes of type attributeType applied to 

    element,or an empty array if no such custom attributes exist.

  

  GetCustomAttributes(element: Assembly,attributeType: Type,inherit: bool) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to an assembly. Parameters specify the 

    assembly,the type of the custom attribute to search for,and an ignored search option.

  

  

   element: An object derived from the System.Reflection.Assembly class that describes a reusable collection 

    of modules.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   inherit: This parameter is ignored,and does not affect the operation of this method.

   Returns: An System.Attribute array that contains the custom attributes of type attributeType applied to 

    element,or an empty array if no such custom attributes exist.

  

  GetCustomAttributes(element: MemberInfo) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to a member of a type. A parameter specifies 

    the member.

  

  

   element: An object derived from the System.Reflection.MemberInfo class that describes a constructor,

    event,field,method,or property member of a class.

  

   Returns: An System.Attribute array that contains the custom attributes applied to element,or an empty 

    array if no such custom attributes exist.

  

  GetCustomAttributes(element: MemberInfo,inherit: bool) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to a member of a type. Parameters specify 

    the member,the type of the custom attribute to search for,and whether to search ancestors of 

    the member.

  

  

   element: An object derived from the System.Reflection.MemberInfo class that describes a constructor,

    event,field,method,or property member of a class.

  

   inherit: If true,specifies to also search the ancestors of element for custom attributes.

   Returns: An System.Attribute array that contains the custom attributes applied to element,or an empty 

    array if no such custom attributes exist.

  

  GetCustomAttributes(element: MemberInfo,type: Type) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to a member of a type. Parameters specify 

    the member,and the type of the custom attribute to search for.

  

  

   element: An object derived from the System.Reflection.MemberInfo class that describes a constructor,

    event,field,method,or property member of a class.

  

   type: The type,or a base type,of the custom attribute to search for.

   Returns: An System.Attribute array that contains the custom attributes of type type applied to element,

    or an empty array if no such custom attributes exist.

  

  GetCustomAttributes(element: MemberInfo,type: Type,inherit: bool) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to a member of a type. Parameters specify 

    the member,the type of the custom attribute to search for,and whether to search ancestors of 

    the member.

  

  

   element: An object derived from the System.Reflection.MemberInfo class that describes a constructor,

    event,field,method,or property member of a class.

  

   type: The type,or a base type,of the custom attribute to search for.

   inherit: If true,specifies to also search the ancestors of element for custom attributes.

   Returns: An System.Attribute array that contains the custom attributes of type type applied to element,

    or an empty array if no such custom attributes exist.

  

  GetCustomAttributes(element: ParameterInfo,attributeType: Type,inherit: bool) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to a method parameter. Parameters specify 

    the method parameter,the type of the custom attribute to search for,and whether to search 

    ancestors of the method parameter.

  

  

   element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a 

    member of a class.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   inherit: If true,specifies to also search the ancestors of element for custom attributes.

   Returns: An System.Attribute array that contains the custom attributes of type attributeType applied to 

    element,or an empty array if no such custom attributes exist.

  

  GetCustomAttributes(element: ParameterInfo,inherit: bool) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to a method parameter. Parameters specify 

    the method parameter,and whether to search ancestors of the method parameter.

  

  

   element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a 

    member of a class.

  

   inherit: If true,specifies to also search the ancestors of element for custom attributes.

   Returns: An System.Attribute array that contains the custom attributes applied to element,or an empty 

    array if no such custom attributes exist.

  

  GetCustomAttributes(element: ParameterInfo) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to a method parameter. A parameter specifies 

    the method parameter.

  

  

   element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a 

    member of a class.

  

   Returns: An System.Attribute array that contains the custom attributes applied to element,or an empty 

    array if no such custom attributes exist.

  

  GetCustomAttributes(element: ParameterInfo,attributeType: Type) -> Array[Attribute]

  

   Retrieves an array of the custom attributes applied to a method parameter. Parameters specify 

    the method parameter,and the type of the custom attribute to search for.

  

  

   element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a 

    member of a class.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   Returns: An System.Attribute array that contains the custom attributes of type attributeType applied to 

    element,or an empty array if no such custom attributes exist.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Attribute) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: Attribute) -> bool

  

   When overridden in a derived class,indicates whether the value of this instance is the default 

    value for the derived class.

  

   Returns: true if this instance is the default attribute for the class; otherwise,false.
  """
  pass
 @staticmethod
 def IsDefined(element,attributeType,inherit=None):
  """
  IsDefined(element: Module,attributeType: Type,inherit: bool) -> bool

  

   Determines whether any custom attributes are applied to a module. Parameters specify the module,

    the type of the custom attribute to search for,and an ignored search option.

  

  

   element: An object derived from the System.Reflection.Module class that describes a portable executable 

    file.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   inherit: This parameter is ignored,and does not affect the operation of this method.

   Returns: true if a custom attribute of type attributeType is applied to element; otherwise,false.

  IsDefined(element: Module,attributeType: Type) -> bool

  

   Determines whether any custom attributes of a specified type are applied to a module. Parameters 

    specify the module,and the type of the custom attribute to search for.

  

  

   element: An object derived from the System.Reflection.Module class that describes a portable executable 

    file.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   Returns: true if a custom attribute of type attributeType is applied to element; otherwise,false.

  IsDefined(element: Assembly,attributeType: Type,inherit: bool) -> bool

  

   Determines whether any custom attributes are applied to an assembly. Parameters specify the 

    assembly,the type of the custom attribute to search for,and an ignored search option.

  

  

   element: An object derived from the System.Reflection.Assembly class that describes a reusable collection 

    of modules.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   inherit: This parameter is ignored,and does not affect the operation of this method.

   Returns: true if a custom attribute of type attributeType is applied to element; otherwise,false.

  IsDefined(element: Assembly,attributeType: Type) -> bool

  

   Determines whether any custom attributes are applied to an assembly. Parameters specify the 

    assembly,and the type of the custom attribute to search for.

  

  

   element: An object derived from the System.Reflection.Assembly class that describes a reusable collection 

    of modules.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   Returns: true if a custom attribute of type attributeType is applied to element; otherwise,false.

  IsDefined(element: MemberInfo,attributeType: Type,inherit: bool) -> bool

  

   Determines whether any custom attributes are applied to a member of a type. Parameters specify 

    the member,the type of the custom attribute to search for,and whether to search ancestors of 

    the member.

  

  

   element: An object derived from the System.Reflection.MemberInfo class that describes a constructor,

    event,field,method,type,or property member of a class.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   inherit: If true,specifies to also search the ancestors of element for custom attributes.

   Returns: true if a custom attribute of type attributeType is applied to element; otherwise,false.

  IsDefined(element: MemberInfo,attributeType: Type) -> bool

  

   Determines whether any custom attributes are applied to a member of a type. Parameters specify 

    the member,and the type of the custom attribute to search for.

  

  

   element: An object derived from the System.Reflection.MemberInfo class that describes a constructor,

    event,field,method,type,or property member of a class.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   Returns: true if a custom attribute of type attributeType is applied to element; otherwise,false.

  IsDefined(element: ParameterInfo,attributeType: Type,inherit: bool) -> bool

  

   Determines whether any custom attributes are applied to a method parameter. Parameters specify 

    the method parameter,the type of the custom attribute to search for,and whether to search 

    ancestors of the method parameter.

  

  

   element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a 

    member of a class.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   inherit: If true,specifies to also search the ancestors of element for custom attributes.

   Returns: true if a custom attribute of type attributeType is applied to element; otherwise,false.

  IsDefined(element: ParameterInfo,attributeType: Type) -> bool

  

   Determines whether any custom attributes are applied to a method parameter. Parameters specify 

    the method parameter,and the type of the custom attribute to search for.

  

  

   element: An object derived from the System.Reflection.ParameterInfo class that describes a parameter of a 

    member of a class.

  

   attributeType: The type,or a base type,of the custom attribute to search for.

   Returns: true if a custom attribute of type attributeType is applied to element; otherwise,false.
  """
  pass
 def Match(self,obj):
  """
  Match(self: Attribute,obj: object) -> bool

  

   When overridden in a derived class,returns a value that indicates whether this instance equals 

    a specified object.

  

  

   obj: An System.Object to compare with this instance of System.Attribute.

   Returns: true if this instance equals obj; otherwise,false.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 TypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When implemented in a derived class,gets a unique identifier for this System.Attribute.



Get: TypeId(self: Attribute) -> object



"""


