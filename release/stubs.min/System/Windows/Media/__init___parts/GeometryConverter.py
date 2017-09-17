class GeometryConverter(TypeConverter):
 """
 Converts instances of other types to and from instances of System.Windows.Media.Geometry.
 
 GeometryConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: GeometryConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Indicates whether an object can be converted from a given type to an instance 
    of a System.Windows.Media.Geometry.
  
  
   context: Context information required for conversion.
   sourceType: The source System.Type that is being queried for conversion support.
   Returns: true if object of the specified type can be converted to a 
    System.Windows.Media.Geometry; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: GeometryConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines whether instances of System.Windows.Media.Geometry can be converted 
    to the specified type.
  
  
   context: Context information required for conversion.
   destinationType: The desired type this System.Windows.Media.Geometry is being evaluated to be 
    converted to.
  
   Returns: true if instances of System.Windows.Media.Geometry can be converted to 
    destinationType; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: GeometryConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object
  
   Converts the specified object to a System.Windows.Media.Geometry.
  
   context: Context information required for conversion.
   culture: Cultural information respected during conversion.
   value: The object being converted.
   Returns: The System.Windows.Media.Geometry created from converting value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: GeometryConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object
  
   Converts the specified System.Windows.Media.Geometry to the specified type.
  
   context: Context information required for conversion.
   culture: Cultural information respected during conversion.
   value: The System.Windows.Media.Geometry to convert.
   destinationType: The type to convert the System.Windows.Media.Geometry to.
   Returns: The object created from converting this System.Windows.Media.Geometry.
  """
  pass
