class BorderGapMaskConverter(object,IMultiValueConverter):
 """
 Represents a converter that converts the dimensions of a System.Windows.Controls.GroupBox control into a System.Windows.Media.VisualBrush.

 

 BorderGapMaskConverter()
 """
 def Convert(self,values,targetType,parameter,culture):
  """
  Convert(self: BorderGapMaskConverter,values: Array[object],targetType: Type,parameter: object,culture: CultureInfo) -> object

  

   Creates a System.Windows.Media.VisualBrush that draws the border for a 

    System.Windows.Controls.GroupBox control.

  

  

   values: An array of three numbers that represent the System.Windows.Controls.GroupBox control 

    parameters.  See Remarks for more information.

  

   targetType: This parameter is not used.

   parameter: The width of the visible line to the left of the 

    System.Windows.Controls.HeaderedContentControl.Header in the System.Windows.Controls.GroupBox.

  

   culture: This parameter is not used.

   Returns: A System.Windows.Media.VisualBrush that draws the border around a 

    System.Windows.Controls.GroupBox control that includes a gap for the 

    System.Windows.Controls.HeaderedContentControl.Header content.
  """
  pass
 def ConvertBack(self,value,targetTypes,parameter,culture):
  """
  ConvertBack(self: BorderGapMaskConverter,value: object,targetTypes: Array[Type],parameter: object,culture: CultureInfo) -> Array[object]

  

   Not implemented.

  

   value: This parameter is not used.

   targetTypes: This parameter is not used.

   parameter: This parameter is not used.

   culture: This parameter is not used.

   Returns: System.Windows.Data.Binding.DoNothing in all cases.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
