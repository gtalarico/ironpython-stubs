class KeyGestureValueSerializer(ValueSerializer):
 """
 Converts instances of System.String to and from instances of System.Windows.Input.KeyGesture.
 
 KeyGestureValueSerializer()
 """
 def CanConvertFromString(self,value,context):
  """
  CanConvertFromString(self: KeyGestureValueSerializer,value: str,context: IValueSerializerContext) -> bool
  
   Determines if the specified System.String can be convert to an instance of 
    System.Windows.Input.KeyGesture.
  
  
   value: String to evaluate for conversion.
   context: Context information that is used for conversion.
   Returns: Always returns true.
  """
  pass
 def CanConvertToString(self,value,context):
  """
  CanConvertToString(self: KeyGestureValueSerializer,value: object,context: IValueSerializerContext) -> bool
  
   Determines if the specified System.Windows.Input.KeyGesture can be converted to 
    a System.String.
  
  
   value: The gesture to evaluate for conversion.
   context: Context information that is used for conversion.
   Returns: true if value can be converted into a System.String; otherwise,false.
  """
  pass
 def ConvertFromString(self,value,context):
  """
  ConvertFromString(self: KeyGestureValueSerializer,value: str,context: IValueSerializerContext) -> object
  
   Converts a System.String into a System.Windows.Input.KeyGesture.
  
   value: The string to convert into a System.Windows.Input.KeyGesture.
   context: Context information that is used for conversion.
   Returns: A new instance of System.Windows.Input.KeyGesture based on the supplied value.
  """
  pass
 def ConvertToString(self,value,context):
  """
  ConvertToString(self: KeyGestureValueSerializer,value: object,context: IValueSerializerContext) -> str
  
   Converts an instance of System.Windows.Input.KeyGesture to a System.String.
  
   value: The gesture to convert into a string.
   context: Context information that is used for conversion.
   Returns: An invariant string representation of the specified 
    System.Windows.Input.KeyGesture.
  """
  pass
