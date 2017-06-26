class FontFamilyValueSerializer(ValueSerializer):
 """
 Converts instances of System.String to and from instances of System.Windows.Media.FontFamily.
 
 FontFamilyValueSerializer()
 """
 def CanConvertFromString(self,value,context):
  """
  CanConvertFromString(self: FontFamilyValueSerializer,value: str,context: IValueSerializerContext) -> bool
  
   Determines if conversion from a given System.String to an instance of 
    System.Windows.Media.FontFamily is possible.
  
  
   value: String to evaluate for conversion.
   context: Context information used for conversion.
   Returns: true if value can be converted; otherwise,false.
  """
  pass
 def CanConvertToString(self,value,context):
  """
  CanConvertToString(self: FontFamilyValueSerializer,value: object,context: IValueSerializerContext) -> bool
  
   Determines if an instance of System.Windows.Media.FontFamily can be converted 
    to a System.String.
  
  
   value: Instance of System.Windows.Media.FontFamily to evaluate for conversion.
   context: Context information used for conversion.
   Returns: true if value can be converted into a System.String; otherwise,false.
  """
  pass
 def ConvertFromString(self,value,context):
  """
  ConvertFromString(self: FontFamilyValueSerializer,value: str,context: IValueSerializerContext) -> object
  
   Converts a System.String into a System.Windows.Media.FontFamily.
  
   value: System.String value to convert into a System.Windows.Media.FontFamily.
   context: Context information used for conversion.
   Returns: A new instance of System.Windows.Media.FontFamily based on the supplied value.
  """
  pass
 def ConvertToString(self,value,context):
  """
  ConvertToString(self: FontFamilyValueSerializer,value: object,context: IValueSerializerContext) -> str
  
   Converts an instance of System.Windows.Media.FontFamily to a System.String.
  
   value: Instance of System.Windows.Media.FontFamily to evaluate for conversion.
   context: Context information used for conversion.
   Returns: A System.String representation of the supplied System.Windows.Media.FontFamily 
    object.
  """
  pass
