class ListViewItemConverter(ExpandableObjectConverter):
 """
 Provides a type converter to convert System.Windows.Forms.ListViewItem objects to and from various other representations.

 

 ListViewItemConverter()
 """
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: ListViewItemConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object to the given destination 

    type using the context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that represents the type you wish to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: ListViewItemConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the given object to another type.

  

   context: A formatter context. This object can be used to extract additional information about the 

    environment this converter is being invoked from. This may be null,so you should always check. 

    Also,properties on the context object may also return null.

  

   culture: An optional culture info. If not supplied the current culture is assumed.

   value: The object to convert.

   destinationType: The type to convert the object to.

   Returns: The converted object.
  """
  pass
