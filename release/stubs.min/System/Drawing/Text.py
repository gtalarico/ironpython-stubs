# encoding: utf-8
# module System.Drawing.Text calls itself Text
# from System.Drawing,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class FontCollection:
 """ Provides a base class for installed and private font collections. """
 def Dispose(self):
  """
  Dispose(self: FontCollection)
   Releases all resources used by this System.Drawing.Text.FontCollection.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Families=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the array of System.Drawing.FontFamily objects associated with this System.Drawing.Text.FontCollection.

Get: Families(self: FontCollection) -> Array[FontFamily]

"""



class GenericFontFamilies:
 """
 Specifies a generic System.Drawing.FontFamily object.
 
 enum GenericFontFamilies,values: Monospace (2),SansSerif (1),Serif (0)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Monospace=None
 SansSerif=None
 Serif=None
 value__=None


class HotkeyPrefix:
 """
 Specifies the type of display for hot-key prefixes that relate to text.
 
 enum HotkeyPrefix,values: Hide (2),None (0),Show (1)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Hide=None
 None_ =None
 Show=None
 value__=None


class InstalledFontCollection:
 """
 Represents the fonts installed on the system. This class cannot be inherited.
 
 InstalledFontCollection()
 """
 def Dispose(self):
  """
  Dispose(self: FontCollection,disposing: bool)
   Releases the unmanaged resources used by the System.Drawing.Text.FontCollection and 
    optionally releases the managed resources.
  
  
   disposing: true to release both managed and unmanaged resources; false to release only unmanaged 
    resources.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class PrivateFontCollection:
 """
 Provides a collection of font families built from font files that are provided by the client application.
 
 PrivateFontCollection()
 """
 def AddFontFile(self,filename):
  """
  AddFontFile(self: PrivateFontCollection,filename: str)
   Adds a font from the specified file to this System.Drawing.Text.PrivateFontCollection.
  
   filename: A System.String that contains the file name of the font to add.
  """
  pass
 def AddMemoryFont(self,memory,length):
  """
  AddMemoryFont(self: PrivateFontCollection,memory: IntPtr,length: int)
   Adds a font contained in system memory to this System.Drawing.Text.PrivateFontCollection.
  
   memory: The memory address of the font to add.
   length: The memory length of the font to add.
  """
  pass
 def Dispose(self):
  """ Dispose(self: PrivateFontCollection,disposing: bool) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class TextRenderingHint:
 """
 Specifies the quality of text rendering.
 
 enum TextRenderingHint,values: AntiAlias (4),AntiAliasGridFit (3),ClearTypeGridFit (5),SingleBitPerPixel (2),SingleBitPerPixelGridFit (1),SystemDefault (0)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 AntiAlias=None
 AntiAliasGridFit=None
 ClearTypeGridFit=None
 SingleBitPerPixel=None
 SingleBitPerPixelGridFit=None
 SystemDefault=None
 value__=None


