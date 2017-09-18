class TreeViewImageKeyConverter(ImageKeyConverter):
 """
 Provides a type converter to convert data for an image key to and from another data type.

 

 TreeViewImageKeyConverter()
 """
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: TreeViewImageKeyConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the specified object to an object of the specified type using the specified culture 

    information and context.

  

  

   context: A System.ComponentModel.ITypeDescriptorContext that provides a format context,which can be used 

    to extract additional information about the environment this type converter is being invoked 

    from. This parameter or properties of this parameter can be null.

  

   culture: A System.Globalization.CultureInfo that provides locale information.

   value: The object to convert,typically an image key.

   destinationType: The type to convert the object to.

   Returns: An System.Object that represents the converted value.
  """
  pass
 IncludeNoneAsStandardValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether null is valid in the System.ComponentModel.TypeConverter.StandardValuesCollection collection.



"""


