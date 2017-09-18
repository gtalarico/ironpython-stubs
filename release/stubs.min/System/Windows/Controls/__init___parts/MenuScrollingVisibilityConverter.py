class MenuScrollingVisibilityConverter(object,IMultiValueConverter):
 """
 Represents a data-binding converter to handle the visibility of repeat buttons in scrolling menus.

 

 MenuScrollingVisibilityConverter()
 """
 def Convert(self,values,targetType,parameter,culture):
  """
  Convert(self: MenuScrollingVisibilityConverter,values: Array[object],targetType: Type,parameter: object,culture: CultureInfo) -> object

  

   Called when moving a value from a source to a target.

  

   values: Values produced by the source binding.

   targetType: Type of the target. Type that the source will be converted into.

   parameter: Converter parameter.

   culture: Culture information.

   Returns: Converted value.
  """
  pass
 def ConvertBack(self,value,targetTypes,parameter,culture):
  """
  ConvertBack(self: MenuScrollingVisibilityConverter,value: object,targetTypes: Array[Type],parameter: object,culture: CultureInfo) -> Array[object]

  

   Not supported.

  

   value: This parameter is not used.

   targetTypes: This parameter is not used.

   parameter: This parameter is not used.

   culture: This parameter is not used.

   Returns: System.Windows.Data.Binding.DoNothing
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
