class Int32CollectionConverter(TypeConverter):
 """
 Converts an System.Windows.Media.Int32Collection to and from other data types.
 
 Int32CollectionConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: Int32CollectionConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Determines if the converter can convert an object of the given type to an 
    instance of System.Windows.Media.Int32Collection.
  
  
   context: Describes the context information of a type.
   sourceType: The type of the source that is being evaluated for conversion.
   Returns: true if the converter can convert the provided type to an instance of 
    System.Windows.Media.Int32Collection; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: Int32CollectionConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines if the converter can convert an System.Windows.Media.Int32Collection 
    to a given data type.
  
  
   context: The context information of a type.
   destinationType: The desired type to evaluate the conversion to.
   Returns: true if an System.Windows.Media.Int32Collection can convert to destinationType; 
    otherwise false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: Int32CollectionConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object
  
   Attempts to convert a specified object to an 
    System.Windows.Media.Int32Collection instance.
  
  
   context: Context information used for conversion.
   culture: Cultural information that is respected during conversion.
   value: The object being converted.
   Returns: A new instance of System.Windows.Media.Int32Collection.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: Int32CollectionConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object
  
   Attempts to convert an instance of System.Windows.Media.Int32Collection to a 
    specified type.
  
  
   context: Context information used for conversion.
   culture: Cultural information that is respected during conversion.
   value: System.Windows.Media.Int32Collection to convert.
   destinationType: Type being evaluated for conversion.
   Returns: A new instance of the destinationType.
  """
  pass
