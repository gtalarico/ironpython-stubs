class Fonts(object):
 """ Provides enumeration support for System.Windows.Media.FontFamily and System.Windows.Media.Typeface objects. """
 @staticmethod
 def GetFontFamilies(*__args):
  """
  GetFontFamilies(baseUri: Uri,location: str) -> ICollection[FontFamily]
  
   Returns a collection of System.Windows.Media.FontFamily objects using a base 
    uniform resource identifier (URI) value to resolve the font location.
  
  
   baseUri: The base URI value of the location of the fonts.
   location: The location that contains the fonts.
   Returns: An System.Collections.Generic.ICollection of System.Windows.Media.FontFamily 
    objects that represent the fonts in the resolved font location.
  
  GetFontFamilies(baseUri: Uri) -> ICollection[FontFamily]
  
   Returns a collection of System.Windows.Media.FontFamily objects from a uniform 
    resource identifier (URI) value that represents the location of the fonts.
  
  
   baseUri: The base URI value of the location of the fonts.
   Returns: An System.Collections.Generic.ICollection of System.Windows.Media.FontFamily 
    objects that represent the fonts in baseUri.
  
  GetFontFamilies(location: str) -> ICollection[FontFamily]
  
   Returns the collection of System.Windows.Media.FontFamily objects from a string 
    value that represents the location of the fonts.
  
  
   location: The location that contains the fonts.
   Returns: An System.Collections.Generic.ICollection of System.Windows.Media.FontFamily 
    objects that represent the fonts in location.
  """
  pass
 @staticmethod
 def GetTypefaces(*__args):
  """
  GetTypefaces(baseUri: Uri,location: str) -> ICollection[Typeface]
  
   Returns a collection of System.Windows.Media.Typeface objects using a base 
    uniform resource identifier (URI) value to resolve the font location.
  
  
   baseUri: The base URI value of the location of the fonts.
   location: The location that contains the fonts.
   Returns: An System.Collections.Generic.ICollection of System.Windows.Media.Typeface 
    objects that represent the fonts in the resolved font location.
  
  GetTypefaces(baseUri: Uri) -> ICollection[Typeface]
  
   Returns a collection of System.Windows.Media.Typeface objects from a uniform 
    resource identifier (URI) value that represents the font location.
  
  
   baseUri: The base URI value of the location of the fonts.
   Returns: An System.Collections.Generic.ICollection of System.Windows.Media.Typeface 
    objects that represent the fonts in baseUri.
  
  GetTypefaces(location: str) -> ICollection[Typeface]
  
   Returns the collection of System.Windows.Media.Typeface objects from a string 
    value that represents the font directory location.
  
  
   location: The location that contains the fonts.
   Returns: An System.Collections.Generic.ICollection of System.Windows.Media.Typeface 
    objects that represent the fonts in location.
  """
  pass
 SystemFontFamilies=None
 SystemTypefaces=None
 __all__=[
  'GetFontFamilies',
  'GetTypefaces',
 ]

