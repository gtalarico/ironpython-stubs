class IComNativeDescriptorHandler:
 """ Provides a top-level mapping layer between a COM object and a System.ComponentModel.TypeDescriptor. """
 def GetAttributes(self,component):
  """
  GetAttributes(self: IComNativeDescriptorHandler,component: object) -> AttributeCollection

  

   Gets the attributes for the specified component.

  

   component: The component to get attributes for.

   Returns: A collection of attributes for component.
  """
  pass
 def GetClassName(self,component):
  """
  GetClassName(self: IComNativeDescriptorHandler,component: object) -> str

  

   Gets the class name for the specified component.

  

   component: The component to get the class name for.

   Returns: The name of the class that corresponds with component.
  """
  pass
 def GetConverter(self,component):
  """
  GetConverter(self: IComNativeDescriptorHandler,component: object) -> TypeConverter

  

   Gets the type converter for the specified component.

  

   component: The component to get the System.ComponentModel.TypeConverter for.

   Returns: The System.ComponentModel.TypeConverter for component.
  """
  pass
 def GetDefaultEvent(self,component):
  """
  GetDefaultEvent(self: IComNativeDescriptorHandler,component: object) -> EventDescriptor

  

   Gets the default event for the specified component.

  

   component: The component to get the default event for.

   Returns: An System.ComponentModel.EventDescriptor that represents component's default event.
  """
  pass
 def GetDefaultProperty(self,component):
  """
  GetDefaultProperty(self: IComNativeDescriptorHandler,component: object) -> PropertyDescriptor

  

   Gets the default property for the specified component.

  

   component: The component to get the default property for.

   Returns: A System.ComponentModel.PropertyDescriptor that represents component's default property.
  """
  pass
 def GetEditor(self,component,baseEditorType):
  """
  GetEditor(self: IComNativeDescriptorHandler,component: object,baseEditorType: Type) -> object

  

   Gets the editor for the specified component.

  

   component: The component to get the editor for.

   baseEditorType: The base type of the editor for component.

   Returns: The editor for component.
  """
  pass
 def GetEvents(self,component,attributes=None):
  """
  GetEvents(self: IComNativeDescriptorHandler,component: object,attributes: Array[Attribute]) -> EventDescriptorCollection

  

   Gets the events with the specified attributes for the specified component.

  

   component: The component to get events for.

   attributes: The attributes used to filter events.

   Returns: A collection of event descriptors for component.

  GetEvents(self: IComNativeDescriptorHandler,component: object) -> EventDescriptorCollection

  

   Gets the events for the specified component.

  

   component: The component to get events for.

   Returns: A collection of event descriptors for component.
  """
  pass
 def GetName(self,component):
  """
  GetName(self: IComNativeDescriptorHandler,component: object) -> str

  

   Gets the name of the specified component.

  

   component: The component to get the name of.

   Returns: The name of component.
  """
  pass
 def GetProperties(self,component,attributes):
  """
  GetProperties(self: IComNativeDescriptorHandler,component: object,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Gets the properties with the specified attributes for the specified component.

  

   component: The component to get events for.

   attributes: The attributes used to filter properties.

   Returns: A collection of property descriptors for component.
  """
  pass
 def GetPropertyValue(self,component,*__args):
  """
  GetPropertyValue(self: IComNativeDescriptorHandler,component: object,dispid: int,success: bool) -> (object,bool)

  

   Gets the value of the property that has the specified dispatch identifier.

  

   component: The object to which the property belongs.

   dispid: The dispatch identifier.

   success: A System.Boolean,passed by reference,that represents whether the property was retrieved.

   Returns: The value of the property that has the specified dispatch identifier.

  GetPropertyValue(self: IComNativeDescriptorHandler,component: object,propertyName: str,success: bool) -> (object,bool)

  

   Gets the value of the property that has the specified name.

  

   component: The object to which the property belongs.

   propertyName: The name of the property.

   success: A System.Boolean,passed by reference,that represents whether the property was retrieved.

   Returns: The value of the property that has the specified name.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
