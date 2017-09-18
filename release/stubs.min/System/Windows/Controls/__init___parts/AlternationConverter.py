class AlternationConverter(object,IValueConverter):
 """
 Converts an integer to and from an object by applying the integer as an index to a list of objects.

 

 AlternationConverter()
 """
 def Convert(self,o,targetType,parameter,culture):
  """
  Convert(self: AlternationConverter,o: object,targetType: Type,parameter: object,culture: CultureInfo) -> object

  

   Converts an integer to an object in the System.Windows.Controls.AlternationConverter.Values list.

  

   o: The integer to use to find an object in the System.Windows.Controls.AlternationConverter.Values 

    property.

  

   targetType: The type of the binding target property.

   parameter: The converter parameter to use.

   culture: The culture to use in the converter.

   Returns: The object that is in the position of o modulo the number of items in 

    System.Windows.Controls.AlternationConverter.Values.
  """
  pass
 def ConvertBack(self,o,targetType,parameter,culture):
  """
  ConvertBack(self: AlternationConverter,o: object,targetType: Type,parameter: object,culture: CultureInfo) -> object

  

   Converts an object in the System.Windows.Controls.AlternationConverter.Values list to an integer.

  

   o: The object to find in the System.Windows.Controls.AlternationConverter.Values property.

   targetType: The type of the binding target property.

   parameter: The converter parameter to use.

   culture: The culture to use in the converter.

      not exist in System.Windows.Controls.AlternationConverter.Values.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Values=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a list of objects that the System.Windows.Controls.AlternationConverter returns when an integer is passed to the System.Windows.Controls.AlternationConverter.Convert(System.Object,System.Type,System.Object,System.Globalization.CultureInfo) method.



Get: Values(self: AlternationConverter) -> IList



"""


