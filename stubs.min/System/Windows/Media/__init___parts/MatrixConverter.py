class MatrixConverter(TypeConverter):
 """
 Converts instances of other types to and from a System.Windows.Media.Matrix.
 
 MatrixConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: MatrixConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Determines whether an object can be converted from a specific type to an 
    instance of a System.Windows.Media.Matrix.
  
  
   context: The context information of a type.
   sourceType: The type of the source that is being evaluated for conversion.
   Returns: true if the type can be converted to a System.Windows.Media.Matrix; otherwise,
    false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: MatrixConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines whether an instance of a System.Windows.Media.Matrix can be 
    converted to a different type.
  
  
   context: The context information of a type.
   destinationType: The desired type this System.Windows.Media.Matrix is being evaluated for 
    conversion.
  
   Returns: true if this System.Windows.Media.Matrix can be converted to destinationType; 
    otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: MatrixConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object
  
   Attempts to convert the specified object to a System.Windows.Media.Matrix.
  
   context: The context information of a type.
   culture: The System.Globalization.CultureInfo of the type being converted.
   value: The object being converted.
   Returns: The System.Windows.Media.Matrix created from converting value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: MatrixConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object
  
   Attempts to convert a System.Windows.Media.Matrix to a specified type.
  
   context: The context information of a type.
   culture: The System.Globalization.CultureInfo of the type being converted.
   value: The System.Windows.Media.Matrix to convert.
   destinationType: The type to convert this System.Windows.Media.Matrix to.
   Returns: The object created from converting this System.Windows.Media.Matrix.
  """
  pass
