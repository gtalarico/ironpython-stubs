class TextRange(object,ITextRange):
 """
 Represents a selection of content between two System.Windows.Documents.TextPointer positions.
 
 TextRange(position1: TextPointer,position2: TextPointer)
 """
 def ApplyPropertyValue(self,formattingProperty,value):
  """
  ApplyPropertyValue(self: TextRange,formattingProperty: DependencyProperty,value: object)
   Applies a specified formatting property and value to the current selection.
  
   formattingProperty: A formatting property to apply.
   value: The value for the formatting property.
  """
  pass
 def CanLoad(self,dataFormat):
  """
  CanLoad(self: TextRange,dataFormat: str) -> bool
  
   Checks whether the current selection can be loaded with content in a specified 
    data format.
  
  
   dataFormat: A data format to check for load-compatibility into the current selection.  See 
    System.Windows.DataFormats for a list of predefined data formats.
  
   Returns: true if the current selection can be loaded with content in the specified data 
    format; otherwise,false.
  """
  pass
 def CanSave(self,dataFormat):
  """
  CanSave(self: TextRange,dataFormat: str) -> bool
  
   Checks whether the current selection can be saved as a specified data format.
  
   dataFormat: A data format to check for save compatibility with the current selection.  See 
    System.Windows.DataFormats for a list of predefined data formats.
  
   Returns: true if the current selection can be saved as the specified data format; 
    otherwise,false.
  """
  pass
 def ClearAllProperties(self):
  """
  ClearAllProperties(self: TextRange)
   Removes all formatting properties (represented by 
    System.Windows.Documents.Inline elements) from the current selection.
  """
  pass
 def Contains(self,textPointer):
  """
  Contains(self: TextRange,textPointer: TextPointer) -> bool
  
   Checks whether a position (specified by a System.Windows.Documents.TextPointer) 
    is located within the current selection.
  
  
   textPointer: A position to test for inclusion in the current selection.
   Returns: true if the specified position is located within the current selection; 
    otherwise,false.
  """
  pass
 def GetPropertyValue(self,formattingProperty):
  """
  GetPropertyValue(self: TextRange,formattingProperty: DependencyProperty) -> object
  
   Returns the effective value of a specified formatting property on the current 
    selection.
  
  
   formattingProperty: A formatting property to get the value of with respect to the current selection.
   Returns: An object specifying the value of the specified formatting property.
  """
  pass
 def Load(self,stream,dataFormat):
  """
  Load(self: TextRange,stream: Stream,dataFormat: str)
   Loads the current selection in a specified data format from a specified stream.
  
   stream: A readable stream that contains data to load into the current selection.
   dataFormat: A data format to load the data as.  Currently supported data formats are 
    System.Windows.DataFormats.Rtf,System.Windows.DataFormats.Text,
    System.Windows.DataFormats.Xaml,and System.Windows.DataFormats.XamlPackage.
  """
  pass
 def Save(self,stream,dataFormat,preserveTextElements=None):
  """
  Save(self: TextRange,stream: Stream,dataFormat: str,preserveTextElements: bool)
   Saves the current selection to a specified stream in a specified data format,
    with the option of preserving custom System.Windows.Documents.TextElement 
    objects.
  
  
   stream: An empty,writable stream to save the current selection to.
   dataFormat: A data format to save the current selection as.  Currently supported data 
    formats are System.Windows.DataFormats.Rtf,System.Windows.DataFormats.Text,
    System.Windows.DataFormats.Xaml,and System.Windows.DataFormats.XamlPackage.
  
   preserveTextElements: true to preserve custom System.Windows.Documents.TextElement objects; 
    otherwise,false.
  
  Save(self: TextRange,stream: Stream,dataFormat: str)
   Saves the current selection to a specified stream in a specified data format.
  
   stream: An empty,writable stream to save the current selection to.
   dataFormat: A data format to save the current selection as.  Currently supported data 
    formats are System.Windows.DataFormats.Rtf,System.Windows.DataFormats.Text,
    System.Windows.DataFormats.Xaml,and System.Windows.DataFormats.XamlPackage.
  """
  pass
 def Select(self,position1,position2):
  """
  Select(self: TextRange,position1: TextPointer,position2: TextPointer)
   Updates the current selection,taking two System.Windows.Documents.TextPointer 
    positions to indicate the updated selection.
  
  
   position1: A fixed anchor position that marks one end of the updated selection.
   position2: A movable position that marks the other end of the updated selection.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,position1,position2):
  """ __new__(cls: type,position1: TextPointer,position2: TextPointer) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the position that marks the end of the current selection.

Get: End(self: TextRange) -> TextPointer

"""

 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not the current selection is empty.

Get: IsEmpty(self: TextRange) -> bool

"""

 Start=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the position that marks the beginning of the current selection.

Get: Start(self: TextRange) -> TextPointer

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the plain text contents of the current selection.

Get: Text(self: TextRange) -> str

Set: Text(self: TextRange)=value
"""


 Changed=None

