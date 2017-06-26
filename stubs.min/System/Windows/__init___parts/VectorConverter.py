class VectorConverter(TypeConverter):
 """
 Converts instances of other types to and from a System.Windows.Vector.
 
 VectorConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: VectorConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Indicates whether an object can be converted from a given type to an instance 
    of a System.Windows.Vector.
  
  
   context: Describes the context information of a type.
   sourceType: The source System.Type that is being queried for conversion support.
   Returns: true if objects of the specified type can be converted to a 
    System.Windows.Vector; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: VectorConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines whether instances of System.Windows.Vector can be converted to the 
    specified type.
  
  
   context: Describes the context information of a type.
   destinationType: The desired type this System.Windows.Vector is being evaluated for conversion.
   Returns: true if instances of System.Windows.Vector can be converted to destinationType; 
    otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: VectorConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object
  
   Converts the specified object to a System.Windows.Vector.
  
   context: Describes the context information of a type.
   culture: Describes the System.Globalization.CultureInfo of the type being converted.
   value: The object being converted.
   Returns: The System.Windows.Vector created from converting value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: VectorConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object
  
   Converts the specified System.Windows.Vector to the specified type.
  
   context: Describes the context information of a type.
   culture: Describes the System.Globalization.CultureInfo of the type being converted.
   value: The System.Windows.Vector to convert.
   destinationType: The type to convert this System.Windows.Vector to.
   Returns: The object created from converting this System.Windows.Vector.
  """
  pass
