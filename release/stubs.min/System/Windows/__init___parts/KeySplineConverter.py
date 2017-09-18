class KeySplineConverter(TypeConverter):
 """
 Converts instances of other types to and from a System.Windows.Media.Animation.KeySpline.
 
 KeySplineConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: KeySplineConverter,typeDescriptor: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines whether an object can be converted from a given type to an instance 
    of a System.Windows.Media.Animation.KeySpline.
  
  
   typeDescriptor: Describes the context information of a type.
   destinationType: The type of the source that is being evaluated for conversion.
   Returns: true if the type can be converted to a 
    System.Windows.Media.Animation.KeySpline; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: KeySplineConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines whether an instance of a System.Windows.Media.Animation.KeySpline 
    can be converted to a different type.
  
  
   context: Describes the context information of a type.
   destinationType: The desired type this System.Windows.Media.Animation.KeySpline is being 
    evaluated for conversion.
  
   Returns: true if this System.Windows.Media.Animation.KeySpline can be converted to 
    destinationType; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: KeySplineConverter,context: ITypeDescriptorContext,cultureInfo: CultureInfo,value: object) -> object
  
   Attempts to convert the specified object to a 
    System.Windows.Media.Animation.KeySpline.
  
  
   context: Provides contextual information required for conversion.
   cultureInfo: Cultural information to respect during conversion.
   value: The object being converted.
   Returns: The System.Windows.Media.Animation.KeySpline created from converting value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: KeySplineConverter,context: ITypeDescriptorContext,cultureInfo: CultureInfo,value: object,destinationType: Type) -> object
  
   Attempts to convert a System.Windows.Media.Animation.KeySpline to a specified 
    type.
  
  
   context: Provides contextual information required for conversion.
   cultureInfo: Cultural information to respect during conversion.
   value: The System.Windows.Media.Animation.KeySpline to convert.
   destinationType: The type to convert this System.Windows.Media.Animation.KeySpline to.
   Returns: The object created from converting this 
    System.Windows.Media.Animation.KeySpline.
  """
  pass
