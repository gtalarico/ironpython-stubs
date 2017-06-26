class FigureLengthConverter(TypeConverter):
 """
 Converts instances of other types to and from a System.Windows.FigureLength.
 
 FigureLengthConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: FigureLengthConverter,typeDescriptorContext: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Indicates whether an object can be converted from a given type to an instance 
    of a System.Windows.FigureLength.
  
  
   typeDescriptorContext: Describes the context information of a type.
   sourceType: The source System.Type that is being queried for conversion support.
   Returns: true if object of the specified type can be converted to a 
    System.Windows.FigureLength; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: FigureLengthConverter,typeDescriptorContext: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines whether instances of System.Windows.FigureLength can be converted to 
    the specified type.
  
  
   typeDescriptorContext: Describes the context information of a type.
   destinationType: The desired type this System.Windows.FigureLength is being evaluated to be 
    converted to.
  
   Returns: true if instances of System.Windows.FigureLength can be converted to 
    destinationType; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: FigureLengthConverter,typeDescriptorContext: ITypeDescriptorContext,cultureInfo: CultureInfo,source: object) -> object
  
   Converts the specified object to a System.Windows.FigureLength.
  
   typeDescriptorContext: Describes the context information of a type.
   cultureInfo: Describes the System.Globalization.CultureInfo of the type being converted.
   source: The object being converted.
   Returns: The System.Windows.FigureLength created from converting source.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: FigureLengthConverter,typeDescriptorContext: ITypeDescriptorContext,cultureInfo: CultureInfo,value: object,destinationType: Type) -> object
  
   Converts the specified System.Windows.FigureLength to the specified type.
  
   typeDescriptorContext: Describes the context information of a type.
   cultureInfo: Describes the System.Globalization.CultureInfo of the type being converted.
   value: The System.Windows.FigureLength to convert.
   destinationType: The type to convert the System.Windows.FigureLength to.
   Returns: The object created from converting this System.Windows.FigureLength.
  """
  pass
