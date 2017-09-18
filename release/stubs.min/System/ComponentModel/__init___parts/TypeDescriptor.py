class TypeDescriptor(object):
 """ Provides information about the characteristics for a component,such as its attributes,properties,and events. This class cannot be inherited. """
 @staticmethod
 def AddAttributes(*__args):
  """
  AddAttributes(instance: object,*attributes: Array[Attribute]) -> TypeDescriptionProvider

  

   Adds class-level attributes to the target component instance.

  

   instance: An instance of the target component.

   attributes: An array of System.Attribute objects to add to the component's class.

   Returns: The newly created System.ComponentModel.TypeDescriptionProvider that was used to add the 

    specified attributes.

  

  AddAttributes(type: Type,*attributes: Array[Attribute]) -> TypeDescriptionProvider

  

   Adds class-level attributes to the target component type.

  

   type: The System.Type of the target component.

   attributes: An array of System.Attribute objects to add to the component's class.

   Returns: The newly created System.ComponentModel.TypeDescriptionProvider that was used to add the 

    specified attributes.
  """
  pass
 @staticmethod
 def AddEditorTable(editorBaseType,table):
  """
  AddEditorTable(editorBaseType: Type,table: Hashtable)

   Adds an editor table for the given editor base type.

  

   editorBaseType: The editor base type to add the editor table for. If a table already exists for this type,this 

    method will do nothing.

  

   table: The System.Collections.Hashtable to add.
  """
  pass
 @staticmethod
 def AddProvider(provider,*__args):
  """
  AddProvider(provider: TypeDescriptionProvider,instance: object)

   Adds a type description provider for a single instance of a component.

  

   provider: The System.ComponentModel.TypeDescriptionProvider to add.

   instance: An instance of the target component.

  AddProvider(provider: TypeDescriptionProvider,type: Type)

   Adds a type description provider for a component class.

  

   provider: The System.ComponentModel.TypeDescriptionProvider to add.

   type: The System.Type of the target component.
  """
  pass
 @staticmethod
 def AddProviderTransparent(provider,*__args):
  """
  AddProviderTransparent(provider: TypeDescriptionProvider,instance: object)

   Adds a type description provider for a single instance of a component.

  

   provider: The System.ComponentModel.TypeDescriptionProvider to add.

   instance: An instance of the target component.

  AddProviderTransparent(provider: TypeDescriptionProvider,type: Type)

   Adds a type description provider for a component class.

  

   provider: The System.ComponentModel.TypeDescriptionProvider to add.

   type: The System.Type of the target component.
  """
  pass
 @staticmethod
 def CreateAssociation(primary,secondary):
  """
  CreateAssociation(primary: object,secondary: object)

   Creates a primary-secondary association between two objects.

  

   primary: The primary System.Object.

   secondary: The secondary System.Object.
  """
  pass
 @staticmethod
 def CreateDesigner(component,designerBaseType):
  """
  CreateDesigner(component: IComponent,designerBaseType: Type) -> IDesigner

  

   Creates an instance of the designer associated with the specified component and of the specified 

    type of designer.

  

  

   component: An System.ComponentModel.IComponent that specifies the component to associate with the designer.

   designerBaseType: A System.Type that represents the type of designer to create.

   Returns: An System.ComponentModel.Design.IDesigner that is an instance of the designer for the component,

    or null if no designer can be found.
  """
  pass
 @staticmethod
 def CreateEvent(componentType,*__args):
  """
  CreateEvent(componentType: Type,oldEventDescriptor: EventDescriptor,*attributes: Array[Attribute]) -> EventDescriptor

  

   Creates a new event descriptor that is identical to an existing event descriptor,when passed 

    the existing System.ComponentModel.EventDescriptor.

  

  

   componentType: The type of the component for which to create the new event.

   oldEventDescriptor: The existing event information.

   attributes: The new attributes.

   Returns: A new System.ComponentModel.EventDescriptor that has merged the specified metadata attributes 

    with the existing metadata attributes.

  

  CreateEvent(componentType: Type,name: str,type: Type,*attributes: Array[Attribute]) -> EventDescriptor

  

   Creates a new event descriptor that is identical to an existing event descriptor by dynamically 

    generating descriptor information from a specified event on a type.

  

  

   componentType: The type of the component the event lives on.

   name: The name of the event.

   type: The type of the delegate that handles the event.

   attributes: The attributes for this event.

   Returns: An System.ComponentModel.EventDescriptor that is bound to a type.
  """
  pass
 @staticmethod
 def CreateInstance(provider,objectType,argTypes,args):
  """
  CreateInstance(provider: IServiceProvider,objectType: Type,argTypes: Array[Type],args: Array[object]) -> object

  

   Creates an object that can substitute for another data type.

  

   provider: The service provider that provides a System.ComponentModel.TypeDescriptionProvider service. This 

    parameter can be null.

  

   objectType: The System.Type of object to create.

   argTypes: An optional array of parameter types to be passed to the object's constructor. This parameter 

    can be null or an array of zero length.

  

   args: An optional array of parameter values to pass to the object's constructor. If not null,the 

    number of elements must be the same as argTypes.

  

   Returns: An instance of the substitute data type if an associated 

    System.ComponentModel.TypeDescriptionProvider is found; otherwise,null.
  """
  pass
 @staticmethod
 def CreateProperty(componentType,*__args):
  """
  CreateProperty(componentType: Type,oldPropertyDescriptor: PropertyDescriptor,*attributes: Array[Attribute]) -> PropertyDescriptor

  

   Creates a new property descriptor from an existing property descriptor,using the specified 

    existing System.ComponentModel.PropertyDescriptor and attribute array.

  

  

   componentType: The System.Type of the component that the property is a member of.

   oldPropertyDescriptor: The existing property descriptor.

   attributes: The new attributes for this property.

   Returns: A new System.ComponentModel.PropertyDescriptor that has the specified metadata attributes merged 

    with the existing metadata attributes.

  

  CreateProperty(componentType: Type,name: str,type: Type,*attributes: Array[Attribute]) -> PropertyDescriptor

  

   Creates and dynamically binds a property descriptor to a type,using the specified property 

    name,type,and attribute array.

  

  

   componentType: The System.Type of the component that the property is a member of.

   name: The name of the property.

   type: The System.Type of the property.

   attributes: The new attributes for this property.

   Returns: A System.ComponentModel.PropertyDescriptor that is bound to the specified type and that has the 

    specified metadata attributes merged with the existing metadata attributes.
  """
  pass
 @staticmethod
 def GetAssociation(type,primary):
  """
  GetAssociation(type: Type,primary: object) -> object

  

   Returns an instance of the type associated with the specified primary object.

  

   type: The System.Type of the target component.

   primary: The primary object of the association.

   Returns: An instance of the secondary type that has been associated with the primary object if an 

    association exists; otherwise,primary if no specified association exists.
  """
  pass
 @staticmethod
 def GetAttributes(*__args):
  """
  GetAttributes(component: object,noCustomTypeDesc: bool) -> AttributeCollection

  

   Returns a collection of attributes for the specified component and a Boolean indicating that a 

    custom type descriptor has been created.

  

  

   component: The component for which you want to get attributes.

   noCustomTypeDesc: true to use a baseline set of attributes from the custom type descriptor if component is of type 

    System.ComponentModel.ICustomTypeDescriptor; otherwise,false.

  

   Returns: An System.ComponentModel.AttributeCollection with the attributes for the component. If the 

    component is null,this method returns an empty collection.

  

  GetAttributes(component: object) -> AttributeCollection

  

   Returns the collection of attributes for the specified component.

  

   component: The component for which you want to get attributes.

   Returns: An System.ComponentModel.AttributeCollection containing the attributes for the component. If 

    component is null,this method returns an empty collection.

  

  GetAttributes(componentType: Type) -> AttributeCollection

  

   Returns a collection of attributes for the specified type of component.

  

   componentType: The System.Type of the target component.

   Returns: An System.ComponentModel.AttributeCollection with the attributes for the type of the component. 

    If the component is null,this method returns an empty collection.
  """
  pass
 @staticmethod
 def GetClassName(*__args):
  """
  GetClassName(componentType: Type) -> str

  

   Returns the name of the class for the specified type.

  

   componentType: The System.Type of the target component.

   Returns: A System.String containing the name of the class for the specified component type.

  GetClassName(component: object,noCustomTypeDesc: bool) -> str

  

   Returns the name of the class for the specified component using a custom type descriptor.

  

   component: The System.Object for which you want the class name.

   noCustomTypeDesc: true to consider custom type description information; otherwise,false.

   Returns: A System.String containing the name of the class for the specified component.

  GetClassName(component: object) -> str

  

   Returns the name of the class for the specified component using the default type descriptor.

  

   component: The System.Object for which you want the class name.

   Returns: A System.String containing the name of the class for the specified component.
  """
  pass
 @staticmethod
 def GetComponentName(component,noCustomTypeDesc=None):
  """
  GetComponentName(component: object,noCustomTypeDesc: bool) -> str

  

   Returns the name of the specified component using a custom type descriptor.

  

   component: The System.Object for which you want the class name.

   noCustomTypeDesc: true to consider custom type description information; otherwise,false.

   Returns: The name of the class for the specified component,or null if there is no component name.

  GetComponentName(component: object) -> str

  

   Returns the name of the specified component using the default type descriptor.

  

   component: The System.Object for which you want the class name.

   Returns: A System.String containing the name of the specified component,or null if there is no component 

    name.
  """
  pass
 @staticmethod
 def GetConverter(*__args):
  """
  GetConverter(type: Type) -> TypeConverter

  

   Returns a type converter for the specified type.

  

   type: The System.Type of the target component.

   Returns: A System.ComponentModel.TypeConverter for the specified type.

  GetConverter(component: object,noCustomTypeDesc: bool) -> TypeConverter

  

   Returns a type converter for the type of the specified component with a custom type descriptor.

  

   component: A component to get the converter for.

   noCustomTypeDesc: true to consider custom type description information; otherwise,false.

   Returns: A System.ComponentModel.TypeConverter for the specified component.

  GetConverter(component: object) -> TypeConverter

  

   Returns a type converter for the type of the specified component.

  

   component: A component to get the converter for.

   Returns: A System.ComponentModel.TypeConverter for the specified component.
  """
  pass
 @staticmethod
 def GetDefaultEvent(*__args):
  """
  GetDefaultEvent(component: object,noCustomTypeDesc: bool) -> EventDescriptor

  

   Returns the default event for a component with a custom type descriptor.

  

   component: The component to get the event for.

   noCustomTypeDesc: true to consider custom type description information; otherwise,false.

   Returns: An System.ComponentModel.EventDescriptor with the default event,or null if there are no events.

  GetDefaultEvent(component: object) -> EventDescriptor

  

   Returns the default event for the specified component.

  

   component: The component to get the event for.

   Returns: An System.ComponentModel.EventDescriptor with the default event,or null if there are no events.

  GetDefaultEvent(componentType: Type) -> EventDescriptor

  

   Returns the default event for the specified type of component.

  

   componentType: The System.Type of the target component.

   Returns: An System.ComponentModel.EventDescriptor with the default event,or null if there are no events.
  """
  pass
 @staticmethod
 def GetDefaultProperty(*__args):
  """
  GetDefaultProperty(component: object,noCustomTypeDesc: bool) -> PropertyDescriptor

  

   Returns the default property for the specified component with a custom type descriptor.

  

   component: The component to get the default property for.

   noCustomTypeDesc: true to consider custom type description information; otherwise,false.

   Returns: A System.ComponentModel.PropertyDescriptor with the default property,or null if there are no 

    properties.

  

  GetDefaultProperty(component: object) -> PropertyDescriptor

  

   Returns the default property for the specified component.

  

   component: The component to get the default property for.

   Returns: A System.ComponentModel.PropertyDescriptor with the default property,or null if there are no 

    properties.

  

  GetDefaultProperty(componentType: Type) -> PropertyDescriptor

  

   Returns the default property for the specified type of component.

  

   componentType: A System.Type that represents the class to get the property for.

   Returns: A System.ComponentModel.PropertyDescriptor with the default property,or null if there are no 

    properties.
  """
  pass
 @staticmethod
 def GetEditor(*__args):
  """
  GetEditor(type: Type,editorBaseType: Type) -> object

  

   Returns an editor with the specified base type for the specified type.

  

   type: The System.Type of the target component.

   editorBaseType: A System.Type that represents the base type of the editor you are trying to find.

   Returns: An instance of the editor object that can be cast to the given base type,or null if no editor 

    of the requested type can be found.

  

  GetEditor(component: object,editorBaseType: Type,noCustomTypeDesc: bool) -> object

  

   Returns an editor with the specified base type and with a custom type descriptor for the 

    specified component.

  

  

   component: The component to get the editor for.

   editorBaseType: A System.Type that represents the base type of the editor you want to find.

   noCustomTypeDesc: A flag indicating whether custom type description information should be considered.

   Returns: An instance of the editor that can be cast to the specified editor type,or null if no editor of 

    the requested type can be found.

  

  GetEditor(component: object,editorBaseType: Type) -> object

  

   Gets an editor with the specified base type for the specified component.

  

   component: The component to get the editor for.

   editorBaseType: A System.Type that represents the base type of the editor you want to find.

   Returns: An instance of the editor that can be cast to the specified editor type,or null if no editor of 

    the requested type can be found.
  """
  pass
 @staticmethod
 def GetEvents(*__args):
  """
  GetEvents(component: object,noCustomTypeDesc: bool) -> EventDescriptorCollection

  

   Returns the collection of events for a specified component with a custom type descriptor.

  

   component: A component to get the events for.

   noCustomTypeDesc: true to consider custom type description information; otherwise,false.

   Returns: An System.ComponentModel.EventDescriptorCollection with the events for this component.

  GetEvents(component: object,attributes: Array[Attribute]) -> EventDescriptorCollection

  

   Returns the collection of events for a specified component using a specified array of attributes 

    as a filter.

  

  

   component: A component to get the events for.

   attributes: An array of type System.Attribute that you can use as a filter.

   Returns: An System.ComponentModel.EventDescriptorCollection with the events that match the specified 

    attributes for this component.

  

  GetEvents(component: object,attributes: Array[Attribute],noCustomTypeDesc: bool) -> EventDescriptorCollection

  

   Returns the collection of events for a specified component using a specified array of attributes 

    as a filter and using a custom type descriptor.

  

  

   component: A component to get the events for.

   attributes: An array of type System.Attribute to use as a filter.

   noCustomTypeDesc: true to consider custom type description information; otherwise,false.

   Returns: An System.ComponentModel.EventDescriptorCollection with the events that match the specified 

    attributes for this component.

  

  GetEvents(componentType: Type) -> EventDescriptorCollection

  

   Returns the collection of events for a specified type of component.

  

   componentType: The System.Type of the target component.

   Returns: An System.ComponentModel.EventDescriptorCollection with the events for this component.

  GetEvents(componentType: Type,attributes: Array[Attribute]) -> EventDescriptorCollection

  

   Returns the collection of events for a specified type of component using a specified array of 

    attributes as a filter.

  

  

   componentType: The System.Type of the target component.

   attributes: An array of type System.Attribute that you can use as a filter.

   Returns: An System.ComponentModel.EventDescriptorCollection with the events that match the specified 

    attributes for this component.

  

  GetEvents(component: object) -> EventDescriptorCollection

  

   Returns the collection of events for the specified component.

  

   component: A component to get the events for.

   Returns: An System.ComponentModel.EventDescriptorCollection with the events for this component.
  """
  pass
 @staticmethod
 def GetFullComponentName(component):
  """
  GetFullComponentName(component: object) -> str

  

   Returns the fully qualified name of the component.

  

   component: The System.ComponentModel.Component to find the name for.

   Returns: The fully qualified name of the specified component,or null if the component has no name.
  """
  pass
 @staticmethod
 def GetProperties(*__args):
  """
  GetProperties(component: object,noCustomTypeDesc: bool) -> PropertyDescriptorCollection

  

   Returns the collection of properties for a specified component using the default type descriptor.

  

   component: A component to get the properties for.

   noCustomTypeDesc: true to not consider custom type description information; otherwise,false.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties for a specified 

    component.

  

  GetProperties(component: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Returns the collection of properties for a specified component using a specified array of 

    attributes as a filter.

  

  

   component: A component to get the properties for.

   attributes: An array of type System.Attribute to use as a filter.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that match the 

    specified attributes for the specified component.

  

  GetProperties(component: object,attributes: Array[Attribute],noCustomTypeDesc: bool) -> PropertyDescriptorCollection

  

   Returns the collection of properties for a specified component using a specified array of 

    attributes as a filter and using a custom type descriptor.

  

  

   component: A component to get the properties for.

   attributes: An array of type System.Attribute to use as a filter.

   noCustomTypeDesc: true to consider custom type description information; otherwise,false.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the events that match the specified 

    attributes for the specified component.

  

  GetProperties(componentType: Type) -> PropertyDescriptorCollection

  

   Returns the collection of properties for a specified type of component.

  

   componentType: A System.Type that represents the component to get properties for.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties for a specified type of 

    component.

  

  GetProperties(componentType: Type,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Returns the collection of properties for a specified type of component using a specified array 

    of attributes as a filter.

  

  

   componentType: The System.Type of the target component.

   attributes: An array of type System.Attribute to use as a filter.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that match the 

    specified attributes for this type of component.

  

  GetProperties(component: object) -> PropertyDescriptorCollection

  

   Returns the collection of properties for a specified component.

  

   component: A component to get the properties for.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties for the specified 

    component.
  """
  pass
 @staticmethod
 def GetProvider(*__args):
  """
  GetProvider(instance: object) -> TypeDescriptionProvider

  

   Returns the type description provider for the specified component.

  

   instance: An instance of the target component.

   Returns: A System.ComponentModel.TypeDescriptionProvider associated with the specified component.

  GetProvider(type: Type) -> TypeDescriptionProvider

  

   Returns the type description provider for the specified type.

  

   type: The System.Type of the target component.

   Returns: A System.ComponentModel.TypeDescriptionProvider associated with the specified type.
  """
  pass
 @staticmethod
 def GetReflectionType(*__args):
  """
  GetReflectionType(instance: object) -> Type

  

   Returns a System.Type that can be used to perform reflection,given an object.

  

   instance: An instance of the target component.

   Returns: A System.Type for the specified object.

  GetReflectionType(type: Type) -> Type

  

   Returns a System.Type that can be used to perform reflection,given a class type.

  

   type: The System.Type of the target component.

   Returns: A System.Type of the specified class.
  """
  pass
 @staticmethod
 def Refresh(*__args):
  """
  Refresh(module: Module)

   Clears the properties and events for the specified module from the cache.

  

   module: The System.Reflection.Module that represents the module to refresh. Each System.Type in this 

    module will be refreshed.

  

  Refresh(assembly: Assembly)

   Clears the properties and events for the specified assembly from the cache.

  

   assembly: The System.Reflection.Assembly that represents the assembly to refresh. Each System.Type in this 

    assembly will be refreshed.

  

  Refresh(component: object)

   Clears the properties and events for the specified component from the cache.

  

   component: A component for which the properties or events have changed.

  Refresh(type: Type)

   Clears the properties and events for the specified type of component from the cache.

  

   type: The System.Type of the target component.
  """
  pass
 @staticmethod
 def RemoveAssociation(primary,secondary):
  """
  RemoveAssociation(primary: object,secondary: object)

   Removes an association between two objects.

  

   primary: The primary System.Object.

   secondary: The secondary System.Object.
  """
  pass
 @staticmethod
 def RemoveAssociations(primary):
  """
  RemoveAssociations(primary: object)

   Removes all associations for a primary object.

  

   primary: The primary System.Object in an association.
  """
  pass
 @staticmethod
 def RemoveProvider(provider,*__args):
  """
  RemoveProvider(provider: TypeDescriptionProvider,instance: object)

   Removes a previously added type description provider that is associated with the specified 

    object.

  

  

   provider: The System.ComponentModel.TypeDescriptionProvider to remove.

   instance: An instance of the target component.

  RemoveProvider(provider: TypeDescriptionProvider,type: Type)

   Removes a previously added type description provider that is associated with the specified type.

  

   provider: The System.ComponentModel.TypeDescriptionProvider to remove.

   type: The System.Type of the target component.
  """
  pass
 @staticmethod
 def RemoveProviderTransparent(provider,*__args):
  """
  RemoveProviderTransparent(provider: TypeDescriptionProvider,instance: object)

   Removes a previously added type description provider that is associated with the specified 

    object.

  

  

   provider: The System.ComponentModel.TypeDescriptionProvider to remove.

   instance: An instance of the target component.

  RemoveProviderTransparent(provider: TypeDescriptionProvider,type: Type)

   Removes a previously added type description provider that is associated with the specified type.

  

   provider: The System.ComponentModel.TypeDescriptionProvider to remove.

   type: The System.Type of the target component.
  """
  pass
 @staticmethod
 def SortDescriptorArray(infos):
  """
  SortDescriptorArray(infos: IList)

   Sorts descriptors using the name of the descriptor.

  

   infos: An System.Collections.IList that contains the descriptors to sort.
  """
  pass
 ComNativeDescriptorHandler=None
 ComObjectType=None
 InterfaceType=None
 Refreshed=None

