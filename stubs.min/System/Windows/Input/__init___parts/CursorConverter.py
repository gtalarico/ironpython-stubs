class CursorConverter(TypeConverter):
 """
 Converts a System.Windows.Input.Cursor object to and from other types.
 
 CursorConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: CursorConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool
  
   Determines whether an object of the specified type can be converted to an 
    instance of System.Windows.Input.Cursor,using the specified context.
  
  
   context: A format context that provides information about the environment from which 
    this converter is being invoked.
  
   sourceType: The type being evaluated for conversion.
   Returns: true if sourceType is of type System.String; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: CursorConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Determines whether an instance of System.Windows.Input.Cursor can be converted 
    to the specified type,using the specified context.
  
  
   context: A format context that provides information about the environment from which 
    this converter is being invoked.
  
   destinationType: The type being evaluated for conversion.
   Returns: true if destinationType is of type System.String; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: CursorConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object
  
   Attempts to convert the specified object to a System.Windows.Input.Cursor,
    using the specified context.
  
  
   context: A format context that provides information about the environment from which 
    this converter is being invoked.
  
   culture: Culture specific information.
   value: The object to convert.
   Returns: The converted object,or null if value is an empty string.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: CursorConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object
  
   Attempts to convert a System.Windows.Input.Cursor to the specified type,using 
    the specified context.
  
  
   context: A format context that provides information about the environment from which 
    this converter is being invoked.
  
   culture: Culture specific information.
   value: The object to convert.
   destinationType: The type to convert the object to.
   Returns: The converted object,or an empty string if value is null.
  """
  pass
 def GetStandardValues(self,context=None):
  """
  GetStandardValues(self: CursorConverter,context: ITypeDescriptorContext) -> StandardValuesCollection
  
   Gets a collection of standard cursor values,using the specified context.
  
   context: A format context that provides information about the environment from which 
    this converter is being invoked.
  
   Returns: A collection that holds a standard set of valid values.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: CursorConverter,context: ITypeDescriptorContext) -> bool
  
   Determines whether this object supports a standard set of values that can be 
    picked from a list,using the specified context.
  
  
   context: A format context that provides information about the environment from which 
    this converter is being invoked.
  
   Returns: Always returns true.
  """
  pass
