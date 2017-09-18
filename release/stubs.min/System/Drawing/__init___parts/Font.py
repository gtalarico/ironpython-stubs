class Font(MarshalByRefObject,ICloneable,ISerializable,IDisposable):
 """
 Defines a particular format for text,including font face,size,and style attributes. This class cannot be inherited.

 

 Font(prototype: Font,newStyle: FontStyle)

 Font(family: FontFamily,emSize: Single,style: FontStyle,unit: GraphicsUnit,gdiCharSet: Byte,gdiVerticalFont: bool)

 Font(family: FontFamily,emSize: Single,style: FontStyle)

 Font(familyName: str,emSize: Single)

 Font(family: FontFamily,emSize: Single,style: FontStyle,unit: GraphicsUnit)

 Font(family: FontFamily,emSize: Single,style: FontStyle,unit: GraphicsUnit,gdiCharSet: Byte)

 Font(familyName: str,emSize: Single,style: FontStyle,unit: GraphicsUnit,gdiCharSet: Byte)

 Font(familyName: str,emSize: Single,style: FontStyle,unit: GraphicsUnit,gdiCharSet: Byte,gdiVerticalFont: bool)

 Font(family: FontFamily,emSize: Single,unit: GraphicsUnit)

 Font(family: FontFamily,emSize: Single)

 Font(familyName: str,emSize: Single,style: FontStyle,unit: GraphicsUnit)

 Font(familyName: str,emSize: Single,style: FontStyle)

 Font(familyName: str,emSize: Single,unit: GraphicsUnit)
 """
 def Clone(self):
  """
  Clone(self: Font) -> object

  

   Creates an exact copy of this System.Drawing.Font.

   Returns: The System.Drawing.Font this method creates,cast as an System.Object.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Font)

   Releases all resources used by this System.Drawing.Font.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: Font,obj: object) -> bool

  

   Indicates whether the specified object is a System.Drawing.Font and has the same 

    System.Drawing.Font.FontFamily,System.Drawing.Font.GdiVerticalFont,

    System.Drawing.Font.GdiCharSet,System.Drawing.Font.Style,System.Drawing.Font.Size,and 

    System.Drawing.Font.Unit property values as this System.Drawing.Font.

  

  

   obj: The object to test.

   Returns: true if the obj parameter is a System.Drawing.Font and has the same 

    System.Drawing.Font.FontFamily,System.Drawing.Font.GdiVerticalFont,

    System.Drawing.Font.GdiCharSet,System.Drawing.Font.Style,System.Drawing.Font.Size,and 

    System.Drawing.Font.Unit property values as this System.Drawing.Font; otherwise,false.
  """
  pass
 @staticmethod
 def FromHdc(hdc):
  """
  FromHdc(hdc: IntPtr) -> Font

  

   Creates a System.Drawing.Font from the specified Windows handle to a device context.

  

   hdc: A handle to a device context.

   Returns: The System.Drawing.Font this method creates.
  """
  pass
 @staticmethod
 def FromHfont(hfont):
  """
  FromHfont(hfont: IntPtr) -> Font

  

   Creates a System.Drawing.Font from the specified Windows handle.

  

   hfont: A Windows handle to a GDI font.

   Returns: The System.Drawing.Font this method creates.
  """
  pass
 @staticmethod
 def FromLogFont(lf,hdc=None):
  """
  FromLogFont(lf: object) -> Font

  

   Creates a System.Drawing.Font from the specified GDI logical font (LOGFONT) structure.

  

   lf: An System.Object that represents the GDI�LOGFONT structure from which to create the 

    System.Drawing.Font.

  

   Returns: The System.Drawing.Font that this method creates.

  FromLogFont(lf: object,hdc: IntPtr) -> Font

  

   Creates a System.Drawing.Font from the specified GDI logical font (LOGFONT) structure.

  

   lf: An System.Object that represents the GDI�LOGFONT structure from which to create the 

    System.Drawing.Font.

  

   hdc: A handle to a device context that contains additional information about the lf structure.

   Returns: The System.Drawing.Font that this method creates.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Font) -> int

  

   Gets the hash code for this System.Drawing.Font.

   Returns: The hash code for this System.Drawing.Font.
  """
  pass
 def GetHeight(self,*__args):
  """
  GetHeight(self: Font,dpi: Single) -> Single

  

   Returns the height,in pixels,of this System.Drawing.Font when drawn to a device with the 

    specified vertical resolution.

  

  

   dpi: The vertical resolution,in dots per inch,used to calculate the height of the font.

   Returns: The height,in pixels,of this System.Drawing.Font.

  GetHeight(self: Font) -> Single

  

   Returns the line spacing,in pixels,of this font.

   Returns: The line spacing,in pixels,of this font.

  GetHeight(self: Font,graphics: Graphics) -> Single

  

   Returns the line spacing,in the current unit of a specified System.Drawing.Graphics,of this 

    font.

  

  

   graphics: A System.Drawing.Graphics that holds the vertical resolution,in dots per inch,of the display 

    device as well as settings for page unit and page scale.

  

   Returns: The line spacing,in pixels,of this font.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def ToHfont(self):
  """
  ToHfont(self: Font) -> IntPtr

  

   Returns a handle to this System.Drawing.Font.

   Returns: A Windows handle to this System.Drawing.Font.
  """
  pass
 def ToLogFont(self,logFont,graphics=None):
  """
  ToLogFont(self: Font,logFont: object,graphics: Graphics)

   Creates a GDI logical font (LOGFONT) structure from this System.Drawing.Font.

  

   logFont: An System.Object that represents the LOGFONT structure that this method creates.

   graphics: A System.Drawing.Graphics that provides additional information for the LOGFONT structure.

  ToLogFont(self: Font,logFont: object)

   Creates a GDI logical font (LOGFONT) structure from this System.Drawing.Font.

  

   logFont: An System.Object that represents the LOGFONT structure that this method creates.
  """
  pass
 def ToString(self):
  """
  ToString(self: Font) -> str

  

   Returns a human-readable string representation of this System.Drawing.Font.

   Returns: A string that represents this System.Drawing.Font.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,prototype: Font,newStyle: FontStyle)

  __new__(cls: type,family: FontFamily,emSize: Single,style: FontStyle,unit: GraphicsUnit)

  __new__(cls: type,family: FontFamily,emSize: Single,style: FontStyle,unit: GraphicsUnit,gdiCharSet: Byte)

  __new__(cls: type,family: FontFamily,emSize: Single,style: FontStyle,unit: GraphicsUnit,gdiCharSet: Byte,gdiVerticalFont: bool)

  __new__(cls: type,familyName: str,emSize: Single,style: FontStyle,unit: GraphicsUnit,gdiCharSet: Byte)

  __new__(cls: type,familyName: str,emSize: Single,style: FontStyle,unit: GraphicsUnit,gdiCharSet: Byte,gdiVerticalFont: bool)

  __new__(cls: type,family: FontFamily,emSize: Single,style: FontStyle)

  __new__(cls: type,family: FontFamily,emSize: Single,unit: GraphicsUnit)

  __new__(cls: type,family: FontFamily,emSize: Single)

  __new__(cls: type,familyName: str,emSize: Single,style: FontStyle,unit: GraphicsUnit)

  __new__(cls: type,familyName: str,emSize: Single,style: FontStyle)

  __new__(cls: type,familyName: str,emSize: Single,unit: GraphicsUnit)

  __new__(cls: type,familyName: str,emSize: Single)
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Bold=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this System.Drawing.Font is bold.



Get: Bold(self: Font) -> bool



"""

 FontFamily=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Drawing.FontFamily associated with this System.Drawing.Font.



Get: FontFamily(self: Font) -> FontFamily



"""

 GdiCharSet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a byte value that specifies the GDI character set that this System.Drawing.Font uses.



Get: GdiCharSet(self: Font) -> Byte



"""

 GdiVerticalFont=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a Boolean value that indicates whether this System.Drawing.Font is derived from a GDI vertical font.



Get: GdiVerticalFont(self: Font) -> bool



"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the line spacing of this font.



Get: Height(self: Font) -> int



"""

 IsSystemFont=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the font is a member of System.Drawing.SystemFonts.



Get: IsSystemFont(self: Font) -> bool



"""

 Italic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this font has the italic style applied.



Get: Italic(self: Font) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the face name of this System.Drawing.Font.



Get: Name(self: Font) -> str



"""

 OriginalFontName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the font originally specified.



Get: OriginalFontName(self: Font) -> str



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the em-size of this System.Drawing.Font measured in the units specified by the System.Drawing.Font.Unit property.



Get: Size(self: Font) -> Single



"""

 SizeInPoints=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the em-size,in points,of this System.Drawing.Font.



Get: SizeInPoints(self: Font) -> Single



"""

 Strikeout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this System.Drawing.Font specifies a horizontal line through the font.



Get: Strikeout(self: Font) -> bool



"""

 Style=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets style information for this System.Drawing.Font.



Get: Style(self: Font) -> FontStyle



"""

 SystemFontName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the system font if the System.Drawing.Font.IsSystemFont property returns true.



Get: SystemFontName(self: Font) -> str



"""

 Underline=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this System.Drawing.Font is underlined.



Get: Underline(self: Font) -> bool



"""

 Unit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unit of measure for this System.Drawing.Font.



Get: Unit(self: Font) -> GraphicsUnit



"""


