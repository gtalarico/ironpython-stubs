class BooleanToVisibilityConverter(object,IValueConverter):
 """
 Represents the converter that converts Boolean values to and from System.Windows.Visibility enumeration values.

 

 BooleanToVisibilityConverter()
 """
 def Convert(self,value,targetType,parameter,culture):
  """
  Convert(self: BooleanToVisibilityConverter,value: object,targetType: Type,parameter: object,culture: CultureInfo) -> object

  

   Converts a Boolean value to a System.Windows.Visibility enumeration value.

  

   value: The Boolean value to convert. This value can be a standard Boolean value or a nullable Boolean 

    value.

  

   targetType: This parameter is not used.

   parameter: This parameter is not used.

   culture: This parameter is not used.

   Returns: System.Windows.Visibility.Visible if value is true; otherwise,

    System.Windows.Visibility.Collapsed.
  """
  pass
 def ConvertBack(self,value,targetType,parameter,culture):
  """
  ConvertBack(self: BooleanToVisibilityConverter,value: object,targetType: Type,parameter: object,culture: CultureInfo) -> object

  

   Converts a System.Windows.Visibility enumeration value to a Boolean value.

  

   value: A System.Windows.Visibility enumeration value.

   targetType: This parameter is not used.

   parameter: This parameter is not used.

   culture: This parameter is not used.

   Returns: true if value is System.Windows.Visibility.Visible; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
