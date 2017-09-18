class KeysConverter(TypeConverter,IComparer):
 """
 Provides a System.ComponentModel.TypeConverter to convert System.Windows.Forms.Keys objects to and from other representations.

 

 KeysConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: KeysConverter,context: ITypeDescriptorContext,sourceType: Type) -> bool

  

   Returns a value indicating whether this converter can convert an object in the specified source 

    type to the native type of the converter using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context,which can be 

    used to extract additional information about the environment this converter is being invoked 

    from. This parameter or properties of this parameter can be null.

  

   sourceType: The System.Type to convert from.

   Returns: true if the conversion can be performed; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: KeysConverter,context: ITypeDescriptorContext,destinationType: Type) -> bool

  

   Returns a value indicating whether this converter can convert an object in the specified source 

    type to the native type of the converter using the specified context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context,which can be 

    used to extract additional information about the environment this converter is being invoked 

    from. This parameter or properties of this parameter can be null.

  

   destinationType: The System.Type to convert to.

   Returns: true if the conversion can be performed; otherwise,false.
  """
  pass
 def Compare(self,a,b):
  """
  Compare(self: KeysConverter,a: object,b: object) -> int

  

   Compares two key values for equivalence.

  

   a: An System.Object that represents the first key to compare.

   b: An System.Object that represents the second key to compare.

   Returns: An integer indicating the relationship between the two parameters.Value Type Condition A 

    negative integer. a is less than b. zero a equals b. A positive integer. a is greater than b.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: KeysConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object) -> object

  

   Converts the specified object to the converter's native type.

  

   context: An ITypeDescriptorContext that provides a format context,which can be used to extract 

    additional information about the environment this converter is being invoked from. This 

    parameter or properties of this parameter can be null.

  

   culture: A CultureInfo object to provide locale information.

   value: The object to convert.

   Returns: An object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: KeysConverter,context: ITypeDescriptorContext,culture: CultureInfo,value: object,destinationType: Type) -> object

  

   Converts the specified object to the specified destination type.

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context,which can be 

    used to extract additional information about the environment this converter is being invoked 

    from. This parameter or properties of this parameter can be null.

  

   culture: A System.Globalization.CultureInfo to provide locale information.

   value: The System.Object to convert.

   destinationType: The System.Type to convert the object to.

   Returns: An System.Object that represents the converted value.
  """
  pass
 def GetConvertFromException(self,*args):
  """
  GetConvertFromException(self: TypeConverter,value: object) -> Exception

  

   Returns an exception to throw when a conversion cannot be performed.

  

   value: The System.Object to convert,or null if the object is not available.

   Returns: An System.Exception that represents the exception to throw when a conversion cannot be performed.
  """
  pass
 def GetConvertToException(self,*args):
  """
  GetConvertToException(self: TypeConverter,value: object,destinationType: Type) -> Exception

  

   Returns an exception to throw when a conversion cannot be performed.

  

   value: The System.Object to convert,or null if the object is not available.

   destinationType: A System.Type that represents the type the conversion was trying to convert to.

   Returns: An System.Exception that represents the exception to throw when a conversion cannot be performed.
  """
  pass
 def GetStandardValues(self,context=None):
  """
  GetStandardValues(self: KeysConverter,context: ITypeDescriptorContext) -> StandardValuesCollection

  

   Returns a collection of standard values for the data type that this type converter is designed 

    for when provided with a format context.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context,which can be 

    used to extract additional information about the environment this converter is being invoked 

    from. This parameter or properties of this parameter can be null.

  

   Returns: A System.ComponentModel.TypeConverter.StandardValuesCollection that holds a standard set of 

    valid values,which can be empty if the data type does not support a standard set of values.
  """
  pass
 def GetStandardValuesExclusive(self,context=None):
  """
  GetStandardValuesExclusive(self: KeysConverter,context: ITypeDescriptorContext) -> bool

  

   Determines if the list of standard values returned from GetStandardValues is an exclusive list 

    using the specified System.ComponentModel.ITypeDescriptorContext.

  

  

   context: A formatter context. This object can be used to extract additional information about the 

    environment this converter is being invoked from. This may be null,so you should always check. 

    Also,properties on the context object may also return null.

  

   Returns: true if the collection returned from erload:System.Windows.Forms.KeysConverter.GetStandardValues 

    is an exhaustive list of possible values; otherwise,false if other values are possible. The 

    default implementation for this method always returns false.
  """
  pass
 def GetStandardValuesSupported(self,context=None):
  """
  GetStandardValuesSupported(self: KeysConverter,context: ITypeDescriptorContext) -> bool

  

   Gets a value indicating whether this object supports a standard set of values that can be picked 

    from a list.

  

  

   context: An System.ComponentModel.ITypeDescriptorContext that provides a format context,which can be 

    used to extract additional information about the environment this converter is being invoked 

    from. This parameter or properties of this parameter can be null.

  

   Returns: Always returns true.
  """
  pass
 def SortProperties(self,*args):
  """
  SortProperties(self: TypeConverter,props: PropertyDescriptorCollection,names: Array[str]) -> PropertyDescriptorCollection

  

   Sorts a collection of properties.

  

   props: A System.ComponentModel.PropertyDescriptorCollection that has the properties to sort.

   names: An array of names in the order you want the properties to appear in the collection.

   Returns: A System.ComponentModel.PropertyDescriptorCollection that contains the sorted properties.
  """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
