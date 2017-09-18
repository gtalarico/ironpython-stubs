class Color(object):
 """ Represents an ARGB (alpha,red,green,blue) color. """
 def Equals(self,obj):
  """
  Equals(self: Color,obj: object) -> bool

  

   Tests whether the specified object is a System.Drawing.Color structure and is equivalent to this 

    System.Drawing.Color structure.

  

  

   obj: The object to test.

   Returns: true if obj is a System.Drawing.Color structure equivalent to this System.Drawing.Color 

    structure; otherwise,false.
  """
  pass
 @staticmethod
 def FromArgb(*__args):
  """
  FromArgb(alpha: int,baseColor: Color) -> Color

  

   Creates a System.Drawing.Color structure from the specified System.Drawing.Color structure,but 

    with the new specified alpha value. Although this method allows a 32-bit value to be passed for 

    the alpha value,the value is limited to 8 bits.

  

  

   alpha: The alpha value for the new System.Drawing.Color. Valid values are 0 through 255.

   baseColor: The System.Drawing.Color from which to create the new System.Drawing.Color.

   Returns: The System.Drawing.Color that this method creates.

  FromArgb(red: int,green: int,blue: int) -> Color

  

   Creates a System.Drawing.Color structure from the specified 8-bit color values (red,green,and 

    blue). The alpha value is implicitly 255 (fully opaque). Although this method allows a 32-bit 

    value to be passed for each color component,the value of each component is limited to 8 bits.

  

  

   red: The red component value for the new System.Drawing.Color. Valid values are 0 through 255.

   green: The green component value for the new System.Drawing.Color. Valid values are 0 through 255.

   blue: The blue component value for the new System.Drawing.Color. Valid values are 0 through 255.

   Returns: The System.Drawing.Color that this method creates.

  FromArgb(argb: int) -> Color

  

   Creates a System.Drawing.Color structure from a 32-bit ARGB value.

  

   argb: A value specifying the 32-bit ARGB value.

   Returns: The System.Drawing.Color structure that this method creates.

  FromArgb(alpha: int,red: int,green: int,blue: int) -> Color

  

   Creates a System.Drawing.Color structure from the four ARGB component (alpha,red,green,and 

    blue) values. Although this method allows a 32-bit value to be passed for each component,the 

    value of each component is limited to 8 bits.

  

  

   alpha: The alpha component. Valid values are 0 through 255.

   red: The red component. Valid values are 0 through 255.

   green: The green component. Valid values are 0 through 255.

   blue: The blue component. Valid values are 0 through 255.

   Returns: The System.Drawing.Color that this method creates.
  """
  pass
 @staticmethod
 def FromKnownColor(color):
  """
  FromKnownColor(color: KnownColor) -> Color

  

   Creates a System.Drawing.Color structure from the specified predefined color.

  

   color: An element of the System.Drawing.KnownColor enumeration.

   Returns: The System.Drawing.Color that this method creates.
  """
  pass
 @staticmethod
 def FromName(name):
  """
  FromName(name: str) -> Color

  

   Creates a System.Drawing.Color structure from the specified name of a predefined color.

  

   name: A string that is the name of a predefined color. Valid names are the same as the names of the 

    elements of the System.Drawing.KnownColor enumeration.

  

   Returns: The System.Drawing.Color that this method creates.
  """
  pass
 def GetBrightness(self):
  """
  GetBrightness(self: Color) -> Single

  

   Gets the hue-saturation-brightness (HSB) brightness value for this System.Drawing.Color 

    structure.

  

   Returns: The brightness of this System.Drawing.Color. The brightness ranges from 0.0 through 1.0,where 

    0.0 represents black and 1.0 represents white.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Color) -> int

  

   Returns a hash code for this System.Drawing.Color structure.

   Returns: An integer value that specifies the hash code for this System.Drawing.Color.
  """
  pass
 def GetHue(self):
  """
  GetHue(self: Color) -> Single

  

   Gets the hue-saturation-brightness (HSB) hue value,in degrees,for this System.Drawing.Color 

    structure.

  

   Returns: The hue,in degrees,of this System.Drawing.Color. The hue is measured in degrees,ranging from 

    0.0 through 360.0,in HSB color space.
  """
  pass
 def GetSaturation(self):
  """
  GetSaturation(self: Color) -> Single

  

   Gets the hue-saturation-brightness (HSB) saturation value for this System.Drawing.Color 

    structure.

  

   Returns: The saturation of this System.Drawing.Color. The saturation ranges from 0.0 through 1.0,where 

    0.0 is grayscale and 1.0 is the most saturated.
  """
  pass
 def ToArgb(self):
  """
  ToArgb(self: Color) -> int

  

   Gets the 32-bit ARGB value of this System.Drawing.Color structure.

   Returns: The 32-bit ARGB value of this System.Drawing.Color.
  """
  pass
 def ToKnownColor(self):
  """
  ToKnownColor(self: Color) -> KnownColor

  

   Gets the System.Drawing.KnownColor value of this System.Drawing.Color structure.

   Returns: An element of the System.Drawing.KnownColor enumeration,if the System.Drawing.Color is created 

    from a predefined color by using either the System.Drawing.Color.FromName(System.String) method 

    or the System.Drawing.Color.FromKnownColor(System.Drawing.KnownColor) method; otherwise,0.
  """
  pass
 def ToString(self):
  """
  ToString(self: Color) -> str

  

   Converts this System.Drawing.Color structure to a human-readable string.

   Returns: A string that is the name of this System.Drawing.Color,if the System.Drawing.Color is created 

    from a predefined color by using either the System.Drawing.Color.FromName(System.String) method 

    or the System.Drawing.Color.FromKnownColor(System.Drawing.KnownColor) method; otherwise,a 

    string that consists of the ARGB component names and their values.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 A=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the alpha component value of this System.Drawing.Color structure.



Get: A(self: Color) -> Byte



"""

 B=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the blue component value of this System.Drawing.Color structure.



Get: B(self: Color) -> Byte



"""

 G=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the green component value of this System.Drawing.Color structure.



Get: G(self: Color) -> Byte



"""

 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether this System.Drawing.Color structure is uninitialized.



Get: IsEmpty(self: Color) -> bool



"""

 IsKnownColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this System.Drawing.Color structure is a predefined color. Predefined colors are represented by the elements of the System.Drawing.KnownColor enumeration.



Get: IsKnownColor(self: Color) -> bool



"""

 IsNamedColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this System.Drawing.Color structure is a named color or a member of the System.Drawing.KnownColor enumeration.



Get: IsNamedColor(self: Color) -> bool



"""

 IsSystemColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this System.Drawing.Color structure is a system color. A system color is a color that is used in a Windows display element. System colors are represented by elements of the System.Drawing.KnownColor enumeration.



Get: IsSystemColor(self: Color) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of this System.Drawing.Color.



Get: Name(self: Color) -> str



"""

 R=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the red component value of this System.Drawing.Color structure.



Get: R(self: Color) -> Byte



"""


 AliceBlue=None
 AntiqueWhite=None
 Aqua=None
 Aquamarine=None
 Azure=None
 Beige=None
 Bisque=None
 Black=None
 BlanchedAlmond=None
 Blue=None
 BlueViolet=None
 Brown=None
 BurlyWood=None
 CadetBlue=None
 Chartreuse=None
 Chocolate=None
 Coral=None
 CornflowerBlue=None
 Cornsilk=None
 Crimson=None
 Cyan=None
 DarkBlue=None
 DarkCyan=None
 DarkGoldenrod=None
 DarkGray=None
 DarkGreen=None
 DarkKhaki=None
 DarkMagenta=None
 DarkOliveGreen=None
 DarkOrange=None
 DarkOrchid=None
 DarkRed=None
 DarkSalmon=None
 DarkSeaGreen=None
 DarkSlateBlue=None
 DarkSlateGray=None
 DarkTurquoise=None
 DarkViolet=None
 DeepPink=None
 DeepSkyBlue=None
 DimGray=None
 DodgerBlue=None
 Empty=None
 Firebrick=None
 FloralWhite=None
 ForestGreen=None
 Fuchsia=None
 Gainsboro=None
 GhostWhite=None
 Gold=None
 Goldenrod=None
 Gray=None
 Green=None
 GreenYellow=None
 Honeydew=None
 HotPink=None
 IndianRed=None
 Indigo=None
 Ivory=None
 Khaki=None
 Lavender=None
 LavenderBlush=None
 LawnGreen=None
 LemonChiffon=None
 LightBlue=None
 LightCoral=None
 LightCyan=None
 LightGoldenrodYellow=None
 LightGray=None
 LightGreen=None
 LightPink=None
 LightSalmon=None
 LightSeaGreen=None
 LightSkyBlue=None
 LightSlateGray=None
 LightSteelBlue=None
 LightYellow=None
 Lime=None
 LimeGreen=None
 Linen=None
 Magenta=None
 Maroon=None
 MediumAquamarine=None
 MediumBlue=None
 MediumOrchid=None
 MediumPurple=None
 MediumSeaGreen=None
 MediumSlateBlue=None
 MediumSpringGreen=None
 MediumTurquoise=None
 MediumVioletRed=None
 MidnightBlue=None
 MintCream=None
 MistyRose=None
 Moccasin=None
 NavajoWhite=None
 Navy=None
 OldLace=None
 Olive=None
 OliveDrab=None
 Orange=None
 OrangeRed=None
 Orchid=None
 PaleGoldenrod=None
 PaleGreen=None
 PaleTurquoise=None
 PaleVioletRed=None
 PapayaWhip=None
 PeachPuff=None
 Peru=None
 Pink=None
 Plum=None
 PowderBlue=None
 Purple=None
 Red=None
 RosyBrown=None
 RoyalBlue=None
 SaddleBrown=None
 Salmon=None
 SandyBrown=None
 SeaGreen=None
 SeaShell=None
 Sienna=None
 Silver=None
 SkyBlue=None
 SlateBlue=None
 SlateGray=None
 Snow=None
 SpringGreen=None
 SteelBlue=None
 Tan=None
 Teal=None
 Thistle=None
 Tomato=None
 Transparent=None
 Turquoise=None
 Violet=None
 Wheat=None
 White=None
 WhiteSmoke=None
 Yellow=None
 YellowGreen=None

