class DependencyProperty(object):
 """ Represents a property that can be set through methods such as,styling,data binding,animation,and inheritance. """
 def AddOwner(self,ownerType,typeMetadata=None):
  """
  AddOwner(self: DependencyProperty,ownerType: Type,typeMetadata: PropertyMetadata) -> DependencyProperty
  
   Adds another type as an owner of a dependency property that has already been 
    registered,providing dependency property metadata for the dependency property 
    as it will exist on the provided owner type.
  
  
   ownerType: The type to add as owner of this dependency property.
   typeMetadata: The metadata that qualifies the dependency property as it exists on the 
    provided type.
  
   Returns: A reference to the original System.Windows.DependencyProperty identifier that 
    identifies the dependency property. This identifier should be exposed by the 
    adding class as a public�static�readonly field.
  
  AddOwner(self: DependencyProperty,ownerType: Type) -> DependencyProperty
  
   Adds another type as an owner of a dependency property that has already been 
    registered.
  
  
   ownerType: The type to add as an owner of this dependency property.
   Returns: A reference to the original System.Windows.DependencyProperty identifier that 
    identifies the dependency property. This identifier should be exposed by the 
    adding class as a public static readonly field.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DependencyProperty) -> int
  
   Returns a hash code for this System.Windows.DependencyProperty.
   Returns: The hash code for this System.Windows.DependencyProperty.
  """
  pass
 def GetMetadata(self,*__args):
  """
  GetMetadata(self: DependencyProperty,dependencyObjectType: DependencyObjectType) -> PropertyMetadata
  
   Returns the metadata for this dependency property as it exists on a specified 
    type.
  
  
   dependencyObjectType: A specific object that records the dependency object type from which the 
    dependency property metadata is desired.
  
   Returns: A property metadata object.
  GetMetadata(self: DependencyProperty,dependencyObject: DependencyObject) -> PropertyMetadata
  
   Returns the metadata for this dependency property as it exists on the specified 
    object instance.
  
  
   dependencyObject: A dependency object that is checked for type,to determine which type-specific 
    version of the dependency property the metadata should come from.
  
   Returns: A property metadata object.
  GetMetadata(self: DependencyProperty,forType: Type) -> PropertyMetadata
  
   Returns the metadata for this dependency property as it exists on a specified 
    existing type.
  
  
   forType: The specific type from which to retrieve the dependency property metadata.
   Returns: A property metadata object.
  """
  pass
 def IsValidType(self,value):
  """
  IsValidType(self: DependencyProperty,value: object) -> bool
  
   Determines whether a specified value is acceptable for this dependency 
    property's type,as checked against the property type provided in the original 
    dependency property registration.
  
  
   value: The value to check.
   Returns: true if the specified value is the registered property type or an acceptable 
    derived type; otherwise,false.
  """
  pass
 def IsValidValue(self,value):
  """
  IsValidValue(self: DependencyProperty,value: object) -> bool
  
   Determines whether the provided value is accepted for the type of property 
    through basic type checking,and also potentially if it is within the allowed 
    range of values for that type.
  
  
   value: The value to check.
   Returns: true if the value is acceptable and is of the correct type or a derived type; 
    otherwise,false.
  """
  pass
 def OverrideMetadata(self,forType,typeMetadata,key=None):
  """
  OverrideMetadata(self: DependencyProperty,forType: Type,typeMetadata: PropertyMetadata,key: DependencyPropertyKey)
   Supplies alternate metadata for a read-only dependency property when it is 
    present on instances of a specified type,overriding the metadata that was 
    provided in the initial dependency property registration. You must pass the 
    System.Windows.DependencyPropertyKey for the read-only dependency property to 
    avoid raising an exception.
  
  
   forType: The type where this dependency property is inherited and where the provided 
    alternate metadata will be applied.
  
   typeMetadata: The metadata to apply to the dependency property on the overriding type.
   key: The access key for a read-only dependency property.
  OverrideMetadata(self: DependencyProperty,forType: Type,typeMetadata: PropertyMetadata)
   Specifies alternate metadata for this dependency property when it is present on 
    instances of a specified type,overriding the metadata that existed for the 
    dependency property as it was inherited from base types.
  
  
   forType: The type where this dependency property is inherited and where the provided 
    alternate metadata will be applied.
  
   typeMetadata: The metadata to apply to the dependency property on the overriding type.
  """
  pass
 @staticmethod
 def Register(name,propertyType,ownerType,typeMetadata=None,validateValueCallback=None):
  """
  Register(name: str,propertyType: Type,ownerType: Type,typeMetadata: PropertyMetadata,validateValueCallback: ValidateValueCallback) -> DependencyProperty
  
   Registers a dependency property with the specified property name,property 
    type,owner type,property metadata,and a value validation callback for the 
    property.
  
  
   name: The name of the dependency property to register.
   propertyType: The type of the property.
   ownerType: The owner type that is registering the dependency property.
   typeMetadata: Property metadata for the dependency property.
   validateValueCallback: A reference to a callback that should perform any custom validation of the 
    dependency property value beyond typical type validation.
  
   Returns: A dependency property identifier that should be used to set the value of a 
    public�static�readonly field in your class. That identifier is then used to 
    reference the dependency property later,for operations such as setting its 
    value programmatically or obtaining metadata.
  
  Register(name: str,propertyType: Type,ownerType: Type,typeMetadata: PropertyMetadata) -> DependencyProperty
  
   Registers a dependency property with the specified property name,property 
    type,owner type,and property metadata.
  
  
   name: The name of the dependency property to register.
   propertyType: The type of the property.
   ownerType: The owner type that is registering the dependency property.
   typeMetadata: Property metadata for the dependency property.
   Returns: A dependency property identifier that should be used to set the value of a 
    public�static�readonly field in your class. That identifier is then used to 
    reference the dependency property later,for operations such as setting its 
    value programmatically or obtaining metadata.
  
  Register(name: str,propertyType: Type,ownerType: Type) -> DependencyProperty
  
   Registers a dependency property with the specified property name,property 
    type,and owner type.
  
  
   name: The name of the dependency property to register. The name must be unique within 
    the registration namespace of the owner type.
  
   propertyType: The type of the property.
   ownerType: The owner type that is registering the dependency property.
   Returns: A dependency property identifier that should be used to set the value of a 
    public static readonly field in your class. That identifier is then used to 
    reference the dependency property later,for operations such as setting its 
    value programmatically or obtaining metadata.
  """
  pass
 @staticmethod
 def RegisterAttached(name,propertyType,ownerType,defaultMetadata=None,validateValueCallback=None):
  """
  RegisterAttached(name: str,propertyType: Type,ownerType: Type,defaultMetadata: PropertyMetadata,validateValueCallback: ValidateValueCallback) -> DependencyProperty
  
   Registers an attached property with the specified property type,owner type,
    property metadata,and value validation callback for the property.
  
  
   name: The name of the dependency property to register.
   propertyType: The type of the property.
   ownerType: The owner type that is registering the dependency property.
   defaultMetadata: Property metadata for the dependency property. This can include the default 
    value as well as other characteristics.
  
   validateValueCallback: A reference to a callback that should perform any custom validation of the 
    dependency property value beyond typical type validation.
  
   Returns: A dependency property identifier that should be used to set the value of a 
    public static readonly field in your class. That identifier is then used to 
    reference the dependency property later,for operations such as setting its 
    value programmatically or obtaining metadata.
  
  RegisterAttached(name: str,propertyType: Type,ownerType: Type,defaultMetadata: PropertyMetadata) -> DependencyProperty
  
   Registers an attached property with the specified property name,property type,
    owner type,and property metadata.
  
  
   name: The name of the dependency property to register.
   propertyType: The type of the property.
   ownerType: The owner type that is registering the dependency property.
   defaultMetadata: Property metadata for the dependency property. This can include the default 
    value as well as other characteristics.
  
   Returns: A dependency property identifier that should be used to set the value of a 
    public�static�readonly field in your class. That identifier is then used to 
    reference the dependency property later,for operations such as setting its 
    value programmatically or obtaining metadata.
  
  RegisterAttached(name: str,propertyType: Type,ownerType: Type) -> DependencyProperty
  
   Registers an attached property with the specified property name,property type,
    and owner type.
  
  
   name: The name of the dependency property to register.
   propertyType: The type of the property.
   ownerType: The owner type that is registering the dependency property.
   Returns: A dependency property identifier that should be used to set the value of a 
    public�static�readonly field in your class. That identifier is then used to 
    reference the dependency property later,for operations such as setting its 
    value programmatically or obtaining metadata.
  """
  pass
 @staticmethod
 def RegisterAttachedReadOnly(name,propertyType,ownerType,defaultMetadata,validateValueCallback=None):
  """
  RegisterAttachedReadOnly(name: str,propertyType: Type,ownerType: Type,defaultMetadata: PropertyMetadata,validateValueCallback: ValidateValueCallback) -> DependencyPropertyKey
  
   Registers a read-only attached property,with the specified property type,
    owner type,property metadata,and a validation callback.
  
  
   name: The name of the dependency property to register.
   propertyType: The type of the property.
   ownerType: The owner type that is registering the dependency property.
   defaultMetadata: Property metadata for the dependency property.
   validateValueCallback: A reference to a user-created callback that should perform any custom 
    validation of the dependency property value beyond typical type validation.
  
   Returns: A dependency property key that should be used to set the value of a static 
    read-only field in your class,which is then used to reference the dependency 
    property.
  
  RegisterAttachedReadOnly(name: str,propertyType: Type,ownerType: Type,defaultMetadata: PropertyMetadata) -> DependencyPropertyKey
  
   Registers a read-only attached property,with the specified property type,
    owner type,and property metadata.
  
  
   name: The name of the dependency property to register.
   propertyType: The type of the property.
   ownerType: The owner type that is registering the dependency property.
   defaultMetadata: Property metadata for the dependency property.
   Returns: A dependency property key that should be used to set the value of a static 
    read-only field in your class,which is then used to reference the dependency 
    property later.
  """
  pass
 @staticmethod
 def RegisterReadOnly(name,propertyType,ownerType,typeMetadata,validateValueCallback=None):
  """
  RegisterReadOnly(name: str,propertyType: Type,ownerType: Type,typeMetadata: PropertyMetadata,validateValueCallback: ValidateValueCallback) -> DependencyPropertyKey
  
   Registers a read-only dependency property,with the specified property type,
    owner type,property metadata,and a validation callback.
  
  
   name: The name of the dependency property to register.
   propertyType: The type of the property.
   ownerType: The owner type that is registering the dependency property.
   typeMetadata: Property metadata for the dependency property.
   validateValueCallback: A reference to a user-created callback that should perform any custom 
    validation of the dependency property value beyond typical type validation.
  
   Returns: A dependency property key that should be used to set the value of a static 
    read-only field in your class,which is then used to reference the dependency 
    property later.
  
  RegisterReadOnly(name: str,propertyType: Type,ownerType: Type,typeMetadata: PropertyMetadata) -> DependencyPropertyKey
  
   Registers a read-only dependency property,with the specified property type,
    owner type,and property metadata.
  
  
   name: The name of the dependency property to register.
   propertyType: The type of the property.
   ownerType: The owner type that is registering the dependency property.
   typeMetadata: Property metadata for the dependency property.
   Returns: A dependency property key that should be used to set the value of a static 
    read-only field in your class,which is then used to reference the dependency 
    property.
  """
  pass
 def ToString(self):
  """
  ToString(self: DependencyProperty) -> str
  
   Returns the string representation of the dependency property.
   Returns: The string representation of the dependency property.
  """
  pass
 DefaultMetadata=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the default metadata of the dependency property.

Get: DefaultMetadata(self: DependencyProperty) -> PropertyMetadata

"""

 GlobalIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an internally generated value that uniquely identifies the dependency property.

Get: GlobalIndex(self: DependencyProperty) -> int

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the dependency property.

Get: Name(self: DependencyProperty) -> str

"""

 OwnerType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of the object that registered the dependency property with the property system,or added itself as owner of the property.

Get: OwnerType(self: DependencyProperty) -> Type

"""

 PropertyType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type that the dependency property uses for its value.

Get: PropertyType(self: DependencyProperty) -> Type

"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the dependency property identified by this System.Windows.DependencyProperty instance is a read-only dependency property.

Get: ReadOnly(self: DependencyProperty) -> bool

"""

 ValidateValueCallback=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value validation callback for the dependency property.

Get: ValidateValueCallback(self: DependencyProperty) -> ValidateValueCallback

"""


 UnsetValue=None

