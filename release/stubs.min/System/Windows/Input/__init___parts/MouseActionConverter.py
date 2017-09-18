class MouseActionConverter(TypeConverter):
 """
 Converts a System.Windows.Input.MouseAction object to and from other types.
 
 MouseActionConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: MouseActionConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Determines whether an object of the specified type can be converted to an 
    instance of System.Windows.Input.MouseAction,using the specified context.
  
  
   context: A format context that provides information about the environment from which 
    this converter is being invoked.
  
   sourceType: The type being evaluated for conversion.
   Returns: true if this converter can perform the operation; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: MouseActionConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines whether an instance of System.Windows.Input.MouseAction can be 
    converted to the specified type,using the specified context.
  
  
   context: A format context that provides information about the environment from which 
    this converter is being invoked.
  
   destinationType: The type being evaluated for conversion.
   Returns: true if this converter can perform the operation; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: MouseActionConverter,context: ITypeDescriptorContext,culture: CultureInfo,source: object) -> object
  
   Attempts to convert the specified object to a System.Windows.Input.MouseAction,
    using the specified context.
  
  
   context: A format context that provides information about the environment from which 
    this converter is being invoked.
  
   culture: Culture specific information.
   source: The object to convert.
   Returns: The converted object.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: MouseActionConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object
  
   Attempts to convert a System.Windows.Input.MouseAction to the specified type,
    using the specified context.
  
  
   context: A format context that provides information about the environment from which 
    this converter is being invoked.
  
   culture: Culture specific information.
   value: The object to convert.
   destinationType: The type to convert the object to.
   Returns: The converted object.
  """
  pass
