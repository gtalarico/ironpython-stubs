class PropertyDescriptor(MemberDescriptor):
 """ Provides an abstraction of a property on a class. """
 def AddValueChanged(self,component,handler):
  """
  AddValueChanged(self: PropertyDescriptor,component: object,handler: EventHandler)

   Enables other objects to be notified when this property changes.

  

   component: The component to add the handler for.

   handler: The delegate to add as a listener.
  """
  pass
 def CanResetValue(self,component):
  """
  CanResetValue(self: PropertyDescriptor,component: object) -> bool

  

   When overridden in a derived class,returns whether resetting an object changes its value.

  

   component: The component to test for reset capability.

   Returns: true if resetting the component changes its value; otherwise,false.
  """
  pass
 def CreateInstance(self,*args):
  """
  CreateInstance(self: PropertyDescriptor,type: Type) -> object

  

   Creates an instance of the specified type.

  

   type: A System.Type that represents the type to create.

   Returns: A new instance of the type.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PropertyDescriptor,obj: object) -> bool

  

   Compares this to another object to see if they are equivalent.

  

   obj: The object to compare to this System.ComponentModel.PropertyDescriptor.

   Returns: true if the values are equivalent; otherwise,false.
  """
  pass
 def GetChildProperties(self,*__args):
  """
  GetChildProperties(self: PropertyDescriptor,instance: object) -> PropertyDescriptorCollection

  

   Returns a System.ComponentModel.PropertyDescriptorCollection for a given object.

  

   instance: A component to get the properties for.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties for the specified 

    component.

  

  GetChildProperties(self: PropertyDescriptor,instance: object,filter: Array[Attribute]) -> PropertyDescriptorCollection

  

   Returns a System.ComponentModel.PropertyDescriptorCollection for a given object using a 

    specified array of attributes as a filter.

  

  

   instance: A component to get the properties for.

   filter: An array of type System.Attribute to use as a filter.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that match the 

    specified attributes for the specified component.

  

  GetChildProperties(self: PropertyDescriptor) -> PropertyDescriptorCollection

  

   Returns the default System.ComponentModel.PropertyDescriptorCollection.

   Returns: A System.ComponentModel.PropertyDescriptorCollection.

  GetChildProperties(self: PropertyDescriptor,filter: Array[Attribute]) -> PropertyDescriptorCollection

  

   Returns a System.ComponentModel.PropertyDescriptorCollection using a specified array of 

    attributes as a filter.

  

  

   filter: An array of type System.Attribute to use as a filter.

   Returns: A System.ComponentModel.PropertyDescriptorCollection with the properties that match the 

    specified attributes.
  """
  pass
 def GetEditor(self,editorBaseType):
  """
  GetEditor(self: PropertyDescriptor,editorBaseType: Type) -> object

  

   Gets an editor of the specified type.

  

   editorBaseType: The base type of editor,which is used to differentiate between multiple editors that a property 

    supports.

  

   Returns: An instance of the requested editor type,or null if an editor cannot be found.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PropertyDescriptor) -> int

  

   Returns the hash code for this object.

   Returns: The hash code for this object.
  """
  pass
 def GetTypeFromName(self,*args):
  """
  GetTypeFromName(self: PropertyDescriptor,typeName: str) -> Type

  

   Returns a type using its name.

  

   typeName: The assembly-qualified name of the type to retrieve.

   Returns: A System.Type that matches the given type name,or null if a match cannot be found.
  """
  pass
 def GetValue(self,component):
  """
  GetValue(self: PropertyDescriptor,component: object) -> object

  

   When overridden in a derived class,gets the current value of the property on a component.

  

   component: The component with the property for which to retrieve the value.

   Returns: The value of a property for a given component.
  """
  pass
 def GetValueChangedHandler(self,*args):
  """
  GetValueChangedHandler(self: PropertyDescriptor,component: object) -> EventHandler

  

   Retrieves the current set of ValueChanged event handlers for a specific component

  

   component: The component for which to retrieve event handlers.

   Returns: A combined multicast event handler,or null if no event handlers are currently assigned to 

    component.
  """
  pass
 def OnValueChanged(self,*args):
  """
  OnValueChanged(self: PropertyDescriptor,component: object,e: EventArgs)

   Raises the ValueChanged event that you implemented.

  

   component: The object that raises the event.

   e: An System.EventArgs that contains the event data.
  """
  pass
 def RemoveValueChanged(self,component,handler):
  """
  RemoveValueChanged(self: PropertyDescriptor,component: object,handler: EventHandler)

   Enables other objects to be notified when this property changes.

  

   component: The component to remove the handler for.

   handler: The delegate to remove as a listener.
  """
  pass
 def ResetValue(self,component):
  """
  ResetValue(self: PropertyDescriptor,component: object)

   When overridden in a derived class,resets the value for this property of the component to the 

    default value.

  

  

   component: The component with the property value that is to be reset to the default value.
  """
  pass
 def SetValue(self,component,value):
  """
  SetValue(self: PropertyDescriptor,component: object,value: object)

   When overridden in a derived class,sets the value of the component to a different value.

  

   component: The component with the property value that is to be set.

   value: The new value.
  """
  pass
 def ShouldSerializeValue(self,component):
  """
  ShouldSerializeValue(self: PropertyDescriptor,component: object) -> bool

  

   When overridden in a derived class,determines a value indicating whether the value of this 

    property needs to be persisted.

  

  

   component: The component with the property to be examined for persistence.

   Returns: true if the property should be persisted; otherwise,false.
  """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type,name: str,attrs: Array[Attribute])

  __new__(cls: type,descr: MemberDescriptor)

  __new__(cls: type,descr: MemberDescriptor,attrs: Array[Attribute])
  """
  pass
 AttributeArray=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an array of attributes.



"""

 ComponentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the type of the component this property is bound to.



Get: ComponentType(self: PropertyDescriptor) -> Type



"""

 Converter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type converter for this property.



Get: Converter(self: PropertyDescriptor) -> TypeConverter



"""

 IsLocalizable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this property should be localized,as specified in the System.ComponentModel.LocalizableAttribute.



Get: IsLocalizable(self: PropertyDescriptor) -> bool



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets a value indicating whether this property is read-only.



Get: IsReadOnly(self: PropertyDescriptor) -> bool



"""

 NameHashCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the hash code for the name of the member,as specified in System.String.GetHashCode.



"""

 PropertyType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the type of the property.



Get: PropertyType(self: PropertyDescriptor) -> Type



"""

 SerializationVisibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this property should be serialized,as specified in the System.ComponentModel.DesignerSerializationVisibilityAttribute.



Get: SerializationVisibility(self: PropertyDescriptor) -> DesignerSerializationVisibility



"""

 SupportsChangeEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether value change notifications for this property may originate from outside the property descriptor.



Get: SupportsChangeEvents(self: PropertyDescriptor) -> bool



"""


