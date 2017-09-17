class ZoomPercentageConverter(object,IValueConverter):
 """
 Implements a type converter for converting System.Double (used as the value of System.Windows.Controls.DocumentViewer.Zoom) to and from other types.
 
 ZoomPercentageConverter()
 """
 def Convert(self,value,targetType,parameter,culture):
  """
  Convert(self: ZoomPercentageConverter,value: object,targetType: Type,parameter: object,culture: CultureInfo) -> object
  
   Converts the System.Double (used as the value of 
    System.Windows.Controls.DocumentViewer.Zoom) to an object of the specified 
    type.
  
  
   value: The current value of System.Windows.Controls.DocumentViewer.Zoom.
   targetType: The type to which value is to be converted. This must be System.Double or 
    System.String. See Remarks.
  
   parameter: null. See Remarks.
   culture: The language and culture assumed during the conversion.
   Returns: System.Windows.DependencyProperty.UnsetValue when the converter cannot produce 
    a value; for example,when value is null or when targetType is not 
    System.Double or System.String.- or -The new System.Object of the designated 
    type. As implemented in this class,this must be either a System.Double or a 
    System.String. If it is a string,it will be formatted appropriately for the 
    culture.
  """
  pass
 def ConvertBack(self,value,targetType,parameter,culture):
  """
  ConvertBack(self: ZoomPercentageConverter,value: object,targetType: Type,parameter: object,culture: CultureInfo) -> object
  
   Returns a previously converted value of 
    System.Windows.Controls.DocumentViewer.Zoom back to a System.Double that can be 
    assigned to System.Windows.Controls.DocumentViewer.Zoom.
  
  
   value: The object that is to be converted back to a System.Double.
   targetType: The type of value. This must be System.Double or System.String. See Remarks.
   parameter: null. See Remarks.
   culture: The language and culture assumed during the conversion.
   Returns: System.Windows.DependencyProperty.UnsetValue when the converter cannot produce 
    a value; for example,when value is not a valid percentage when targetType is 
    not System.Double or System.String.- or -A System.Double representing the zoom 
    percentage of a System.Windows.Controls.DocumentViewer.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

# variables with complex values

