class TreeViewImageIndexConverter(ImageIndexConverter):
 """
 Provides a type converter to convert data for an image index to and from one data type to another for use by the System.Windows.Forms.TreeView control.

 

 TreeViewImageIndexConverter()
 """
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: TreeViewImageIndexConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The System.Globalization.CultureInfo to use as the current culture.

   value: The System.Object to convert.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: TreeViewImageIndexConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.

   culture: The System.Globalization.CultureInfo to use as the current culture.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the value parameter to.
  """
  pass
 def GetStandardValues(self,context=None):
  """
  GetStandardValues(self: TreeViewImageIndexConverter,context: ITypeDescriptorContext) -> StandardValuesCollection

  

   context: Provides contextual information about the component.
  """
  pass
 IncludeNoneAsStandardValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating null is valid in the System.ComponentModel.TypeConverter.StandardValuesCollection collection.



"""


