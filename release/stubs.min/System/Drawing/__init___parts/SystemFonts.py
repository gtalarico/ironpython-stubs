class SystemFonts(object):
 """ Specifies the fonts used to display text in Windows display elements. """
 @staticmethod
 def GetFontByName(systemFontName):
  """
  GetFontByName(systemFontName: str) -> Font

  

   Returns a font object that corresponds to the specified system font name.

  

   systemFontName: The name of the system font you need a font object for.

   Returns: A System.Drawing.Font if the specified name matches a value in System.Drawing.SystemFonts; 

    otherwise,null.
  """
  pass
 CaptionFont=None
 DefaultFont=None
 DialogFont=None
 IconTitleFont=None
 MenuFont=None
 MessageBoxFont=None
 SmallCaptionFont=None
 StatusFont=None

