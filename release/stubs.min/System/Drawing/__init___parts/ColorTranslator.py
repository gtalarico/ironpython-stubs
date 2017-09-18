class ColorTranslator(object):
 """ Translates colors to and from GDI+ System.Drawing.Color structures. This class cannot be inherited. """
 @staticmethod
 def FromHtml(htmlColor):
  """
  FromHtml(htmlColor: str) -> Color

  

   Translates an HTML color representation to a GDI+ System.Drawing.Color structure.

  

   htmlColor: The string representation of the Html color to translate.

   Returns: The System.Drawing.Color structure that represents the translated HTML color or 

    System.Drawing.Color.Empty if htmlColor is null.
  """
  pass
 @staticmethod
 def FromOle(oleColor):
  """
  FromOle(oleColor: int) -> Color

  

   Translates an OLE color value to a GDI+ System.Drawing.Color structure.

  

   oleColor: The OLE color to translate.

   Returns: The System.Drawing.Color structure that represents the translated OLE color.
  """
  pass
 @staticmethod
 def FromWin32(win32Color):
  """
  FromWin32(win32Color: int) -> Color

  

   Translates a Windows color value to a GDI+ System.Drawing.Color structure.

  

   win32Color: The Windows color to translate.

   Returns: The System.Drawing.Color structure that represents the translated Windows color.
  """
  pass
 @staticmethod
 def ToHtml(c):
  """
  ToHtml(c: Color) -> str

  

   Translates the specified System.Drawing.Color structure to an HTML string color representation.

  

   c: The System.Drawing.Color structure to translate.

   Returns: The string that represents the HTML color.
  """
  pass
 @staticmethod
 def ToOle(c):
  """
  ToOle(c: Color) -> int

  

   Translates the specified System.Drawing.Color structure to an OLE color.

  

   c: The System.Drawing.Color structure to translate.

   Returns: The OLE color value.
  """
  pass
 @staticmethod
 def ToWin32(c):
  """
  ToWin32(c: Color) -> int

  

   Translates the specified System.Drawing.Color structure to a Windows color.

  

   c: The System.Drawing.Color structure to translate.

   Returns: The Windows color value.
  """
  pass
