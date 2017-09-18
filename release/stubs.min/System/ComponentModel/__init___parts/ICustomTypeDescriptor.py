class ICustomTypeDescriptor:
 """ Provides an interface that supplies dynamic custom type information for an object. """
 def GetAttributes(self):
  """
  GetAttributes(self: ICustomTypeDescriptor) -> AttributeCollection

  

   Returns a collection of custom attributes for this instance of a component.

   Returns: An System.ComponentModel.AttributeCollection containing the attributes for this object.
  """
  pass
 def GetClassName(self):
  """
  GetClassName(self: ICustomTypeDescriptor) -> str

  

   Returns the class name of this instance of a component.

   Returns: The class name of the object,or null if the class does not have a name.
  """
  pass
 def GetComponentName(self):
  """
  GetComponentName(self: ICustomTypeDescriptor) -> str

  

   Returns the name of this instance of a component.

   Returns: The name of the object,or null if the object does not have a name.
  """
  pass
 def GetConverter(self):
  """
  GetConverter(self: ICustomTypeDescriptor) -> TypeConverter

  

   Returns a type converter for this instance of a component.

   Returns: A System.ComponentModel.TypeConverter that is the converter for this object,or null if there is 

    no System.ComponentModel.TypeConverter for this object.
  """
  pass
 def GetDefaultEvent(self):
  """
  GetDefaultEvent(self: ICustomTypeDescriptor) -> EventDescriptor

  

   Returns the default event for this instance of a component.

   Returns: An System.ComponentModel.EventDescriptor that represents the default event for this object,or 

    null if this object does not have events.
  """
  pass
 def GetDefaultProperty(self):
  """
  GetDefaultProperty(self: ICustomTypeDescriptor) -> PropertyDescriptor

  

   Returns the default property for this instance of a component.

   Returns: A System.ComponentModel.PropertyDescriptor that represents the default property for this object,

    or null if this object does not have properties.
  """
  pass
 def GetEditor(self,editorBaseType):
  """
  GetEditor(self: ICustomTypeDescriptor,editorBaseType: Type) -> object

  

   Returns an editor of the specified type for this instance of a component.

  

   editorBaseType: A System.Type that represents the editor for this object.

   Returns: An System.Object of the specified type that is the editor for this object,or null if the editor 

    cannot be found.
  """
  pass
 def GetEvents(self,attributes=None):
  """
  GetEvents(self: ICustomTypeDescriptor,attributes: Array[Attribute]) -> EventDescriptorCollection

  

   Returns the events for this instance of a component using the specified attribute array as a 

    filter.

  

  

   attributes: An array of type System.Attribute that is used as a filter.

   Returns: An System.ComponentModel.EventDescriptorCollection that represents the filtered events for this 

    component instance.

  

  GetEvents(self: ICustomTypeDescriptor) -> EventDescriptorCollection

  

   Returns the events for this instance of a component.

   Returns: An System.ComponentModel.EventDescriptorCollection that represents the events for this component 

    instance.
  """
  pass
 def GetProperties(self,attributes=None):
  """
  GetProperties(self: ICustomTypeDescriptor,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Returns the properties for this instance of a component using the attribute array as a filter.

  

   attributes: An array of type System.Attribute that is used as a filter.

   Returns: A System.ComponentModel.PropertyDescriptorCollection that represents the filtered properties for 

    this component instance.

  

  GetProperties(self: ICustomTypeDescriptor) -> PropertyDescriptorCollection

  

   Returns the properties for this instance of a component.

   Returns: A System.ComponentModel.PropertyDescriptorCollection that represents the properties for this 

    component instance.
  """
  pass
 def GetPropertyOwner(self,pd):
  """
  GetPropertyOwner(self: ICustomTypeDescriptor,pd: PropertyDescriptor) -> object

  

   Returns an object that contains the property described by the specified property descriptor.

  

   pd: A System.ComponentModel.PropertyDescriptor that represents the property whose owner is to be 

    found.

  

   Returns: An System.Object that represents the owner of the specified property.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
