class ThicknessConverter(TypeConverter):
 """
 Converts instances of other types to and from instances of System.Windows.Thickness.
 
 ThicknessConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: ThicknessConverter,typeDescriptorContext: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Determines whether the type converter can create an instance of 
    System.Windows.Thickness from a specified type.
  
  
   typeDescriptorContext: The context information of a type.
   sourceType: The source type that the type converter is evaluating for conversion.
   Returns: true if the type converter can create an instance of System.Windows.Thickness 
    from the specified type; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: ThicknessConverter,typeDescriptorContext: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines whether the type converter can convert an instance of 
    System.Windows.Thickness to a different type.
  
  
   typeDescriptorContext: The context information of a type.
   destinationType: The type for which the type converter is evaluating this instance of 
    System.Windows.Thickness for conversion.
  
   Returns: true if the type converter can convert this instance of 
    System.Windows.Thickness to the destinationType; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: ThicknessConverter,typeDescriptorContext: ITypeDescriptorContext,cultureInfo: CultureInfo,source: object) -> object
  
   Attempts to create an instance of System.Windows.Thickness from a specified 
    object.
  
  
   typeDescriptorContext: The context information for a type.
   cultureInfo: The System.Globalization.CultureInfo of the type being converted.
   source: The sourceSystem.Object being converted.
   Returns: An instance of System.Windows.Thickness created from the converted source.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: ThicknessConverter,typeDescriptorContext: ITypeDescriptorContext,cultureInfo: CultureInfo,value: object,destinationType: Type) -> object
  
   Attempts to convert an instance of System.Windows.Thickness to a specified type.
  
   typeDescriptorContext: The context information of a type.
   cultureInfo: The System.Globalization.CultureInfo of the type being converted.
   value: The instance of System.Windows.Thickness to convert.
   destinationType: The type that this instance of System.Windows.Thickness is converted to.
   Returns: The type that is created when the type converter converts an instance of 
    System.Windows.Thickness.
  """
  pass
