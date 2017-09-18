class TreeNodeConverter(TypeConverter):
 """
 Provides a type converter to convert System.Windows.Forms.TreeNode objects to and from various other representations.

 

 TreeNodeConverter()
 """
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: TreeNodeConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Gets a value indicating whether this converter can convert an object to the given destination 

    type using the context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   destinationType: A System.Type that represents the type you wish to convert to.

   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: TreeNodeConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: A System.Globalization.CultureInfo. If null is passed,the current culture is assumed.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value parameter to.

   Returns: An System.Object that represents the converted value.
  """
  pass
