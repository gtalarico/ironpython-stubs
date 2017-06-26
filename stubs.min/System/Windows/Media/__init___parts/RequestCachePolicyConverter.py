class RequestCachePolicyConverter(TypeConverter):
 """
 Parses a System.Net.Cache.RequestCachePolicy.
 
 RequestCachePolicyConverter()
 """
 def CanConvertFrom(self,*__args):
  """
  CanConvertFrom(self: RequestCachePolicyConverter,td: ITypeDescriptorContext,t: Type) -> bool
  
   Returns a value that indicates whether this converter can convert an object of 
    the specified type to the type of this converter,using the specified context.
  
  
   td: The format context.
   t: The type to convert from.
   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def CanConvertTo(self,*__args):
  """
  CanConvertTo(self: RequestCachePolicyConverter,typeDescriptorContext: ITypeDescriptorContext,destinationType: Type) -> bool
  
   Returns a value that indicates whether this converter can convert the object to 
    the specified type,using the specified context.
  
  
   typeDescriptorContext: The format context.
   destinationType: The type being queried for support.
   Returns: true if this converter can perform the conversion; otherwise,false.
  """
  pass
 def ConvertFrom(self,*__args):
  """
  ConvertFrom(self: RequestCachePolicyConverter,td: ITypeDescriptorContext,ci: CultureInfo,value: object) -> object
  
   Converts the specified object to a System.Net.Cache.RequestCachePolicy object.
  
   td: The format context.
   ci: The current culture.
   value: The object to convert.
   Returns: An object that represents the converted value.
  """
  pass
 def ConvertTo(self,*__args):
  """
  ConvertTo(self: RequestCachePolicyConverter,typeDescriptorContext: ITypeDescriptorContext,cultureInfo: CultureInfo,value: object,destinationType: Type) -> object
  
   Converts this object to the specified type.
  
   typeDescriptorContext: The format context.
   cultureInfo: The culture to use for the conversion.
   value: The policy to convert.
   destinationType: The type to convert to.
   Returns: The object that is constructed from the conversion.
  """
  pass
