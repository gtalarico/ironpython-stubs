class StrokeCollectionConverter(TypeConverter):
 """
 Converts a System.Windows.Ink.StrokeCollection to a string.
 
 StrokeCollectionConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: StrokeCollectionConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Returns a value that indicates whether the 
    System.Windows.StrokeCollectionConverter can convert an object of a specified 
    type to a System.Windows.Ink.StrokeCollection.
  
  
   context: An System.ComponentModel.ITypeDescriptorContext that provides the format 
    context.
  
   sourceType: The System.Type to convert from.
   Returns: true if the System.Windows.StrokeCollectionConverter can convert an object of 
    type sourceType to a System.Windows.Ink.StrokeCollection; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: StrokeCollectionConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Returns a value that indicates whether the 
    System.Windows.StrokeCollectionConverter can convert a 
    System.Windows.Ink.StrokeCollection to the specified type.
  
  
   context: An System.ComponentModel.ITypeDescriptorContext that provides the format 
    context.
  
   destinationType: The System.Type to convert to.
   Returns: true if the System.Windows.StrokeCollectionConverter can convert a 
    System.Windows.Ink.StrokeCollection to the sourceType; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: StrokeCollectionConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object
  
   Converts the specified object to a System.Windows.Ink.StrokeCollection.
  
   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
   culture: The System.Globalization.CultureInfo to use as the current culture.
   value: The System.Object to convert.
   Returns: A System.Windows.Ink.StrokeCollection converted from value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: StrokeCollectionConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object
  
   Converts a System.Windows.Ink.StrokeCollection to a string.
  
   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
   culture: The System.Globalization.CultureInfo to use as the current culture.
   value: The System.Object to convert.
   destinationType: The System.Type to convert to.
   Returns: An object that represents the specified System.Windows.Ink.StrokeCollection.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: StrokeCollectionConverter,context: ITypeDescriptorContext) -> bool
  
   Returns whether this object supports a standard set of values that can be 
    picked from a list,using the specified context.
  
  
   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
   Returns: false in all cases.
  """
  pass
