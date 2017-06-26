class PointCollectionConverter(TypeConverter):
 """
 Converts instances of other types to and from a System.Windows.Media.PointCollection.
 
 PointCollectionConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: PointCollectionConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Determines whether an object can be converted from a specified type to an 
    instance of a System.Windows.Media.PointCollection.
  
  
   context: The context information of a type.
   sourceType: The type of the source that is being evaluated for conversion.
   Returns: true if the type can be converted to a System.Windows.Media.PointCollection; 
    otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: PointCollectionConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines whether an instance of a System.Windows.Media.PointCollection can be 
    converted to a different type.
  
  
   context: The context information of a type.
   destinationType: The needed type for which you are evaluating this 
    System.Windows.Media.PointCollection for conversion.
  
   Returns: true if this System.Windows.Media.PointCollection can be converted to 
    destinationType; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: PointCollectionConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object
  
   Attempts to convert the specified object to a 
    System.Windows.Media.PointCollection.
  
  
   context: The context information of a type.
   culture: The System.Globalization.CultureInfo of the type you want to convert.
   value: The object being converted.
   Returns: The System.Windows.Media.PointCollection that is created from converting value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: PointCollectionConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object
  
   Attempts to convert a System.Windows.Media.PointCollection to a specified type.
  
   context: The context information of a type.
   culture: The System.Globalization.CultureInfo of the type you want to convert.
   value: The System.Windows.Media.PointCollection to convert.
   destinationType: The type to convert this System.Windows.Media.PointCollection to.
   Returns: The object that is created from converting this 
    System.Windows.Media.PointCollection.
  """
  pass
