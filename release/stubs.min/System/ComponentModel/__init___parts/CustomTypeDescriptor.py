class CustomTypeDescriptor(object,ICustomTypeDescriptor):
 """ Provides a simple default implementation of the System.ComponentModel.ICustomTypeDescriptor interface. """
 def GetAttributes(self):
  """
  GetAttributes(self: CustomTypeDescriptor) -> AttributeCollection

  

   Returns a collection of custom attributes for the type represented by this type descriptor.

   Returns: An System.ComponentModel.AttributeCollection containing the attributes for the type. The default 

    is System.ComponentModel.AttributeCollection.Empty.
  """
  pass
 def GetClassName(self):
  """
  GetClassName(self: CustomTypeDescriptor) -> str

  

   Returns the fully qualified name of the class represented by this type descriptor.

   Returns: A System.String containing the fully qualified class name of the type this type descriptor is 

    describing. The default is null.
  """
  pass
 def GetComponentName(self):
  """
  GetComponentName(self: CustomTypeDescriptor) -> str

  

   Returns the name of the class represented by this type descriptor.

   Returns: A System.String containing the name of the component instance this type descriptor is 

    describing. The default is null.
  """
  pass
 def GetConverter(self):
  """
  GetConverter(self: CustomTypeDescriptor) -> TypeConverter

  

   Returns a type converter for the type represented by this type descriptor.

   Returns: A System.ComponentModel.TypeConverter for the type represented by this type descriptor. The 

    default is a newly created System.ComponentModel.TypeConverter.
  """
  pass
 def GetDefaultEvent(self):
  """
  GetDefaultEvent(self: CustomTypeDescriptor) -> EventDescriptor

  

   Returns the event descriptor for the default event of the object represented by this type 

    descriptor.

  

   Returns: The System.ComponentModel.EventDescriptor for the default event on the object represented by 

    this type descriptor. The default is null.
  """
  pass
 def GetDefaultProperty(self):
  """
  GetDefaultProperty(self: CustomTypeDescriptor) -> PropertyDescriptor

  

   Returns the property descriptor for the default property of the object represented by this type 

    descriptor.

  

   Returns: A System.ComponentModel.PropertyDescriptor for the default property on the object represented by 

    this type descriptor. The default is null.
  """
  pass
 def GetEditor(self,editorBaseType):
  """
  GetEditor(self: CustomTypeDescriptor,editorBaseType: Type) -> object

  

   Returns an editor of the specified type that is to be associated with the class represented by 

    this type descriptor.

  

  

   editorBaseType: The base type of the editor to retrieve.

   Returns: An editor of the given type that is to be associated with the class represented by this type 

    descriptor. The default is null.
  """
  pass
 def GetEvents(self,attributes=None):
  """
  GetEvents(self: CustomTypeDescriptor,attributes: Array[Attribute]) -> EventDescriptorCollection

  

   Returns a filtered collection of event descriptors for the object represented by this type 

    descriptor.

  

  

   attributes: An array of attributes to use as a filter. This can be null.

   Returns: An System.ComponentModel.EventDescriptorCollection containing the event descriptions for the 

    object represented by this type descriptor. The default is 

    System.ComponentModel.EventDescriptorCollection.Empty.

  

  GetEvents(self: CustomTypeDescriptor) -> EventDescriptorCollection

  

   Returns a collection of event descriptors for the object represented by this type descriptor.

   Returns: An System.ComponentModel.EventDescriptorCollection containing the event descriptors for the 

    object represented by this type descriptor. The default is 

    System.ComponentModel.EventDescriptorCollection.Empty.
  """
  pass
 def GetProperties(self,attributes=None):
  """
  GetProperties(self: CustomTypeDescriptor) -> PropertyDescriptorCollection

  

   Returns a collection of property descriptors for the object represented by this type descriptor.

   Returns: A System.ComponentModel.PropertyDescriptorCollection containing the property descriptions for 

    the object represented by this type descriptor. The default is 

    System.ComponentModel.PropertyDescriptorCollection.Empty.

  

  GetProperties(self: CustomTypeDescriptor,attributes: Array[Attribute]) -> PropertyDescriptorCollection

  

   Returns a filtered collection of property descriptors for the object represented by this type 

    descriptor.

  

  

   attributes: An array of attributes to use as a filter. This can be null.

   Returns: A System.ComponentModel.PropertyDescriptorCollection containing the property descriptions for 

    the object represented by this type descriptor. The default is 

    System.ComponentModel.PropertyDescriptorCollection.Empty.
  """
  pass
 def GetPropertyOwner(self,pd):
  """
  GetPropertyOwner(self: CustomTypeDescriptor,pd: PropertyDescriptor) -> object

  

   Returns an object that contains the property described by the specified property descriptor.

  

   pd: The property descriptor for which to retrieve the owning object.

   Returns: An System.Object that owns the given property specified by the type descriptor. The default is 

    null.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type)

  __new__(cls: type,parent: ICustomTypeDescriptor)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
