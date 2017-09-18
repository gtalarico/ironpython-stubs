class FontFamily(MarshalByRefObject,IDisposable):
 """
 Defines a group of type faces having a similar basic design and certain variations in styles. This class cannot be inherited.

 

 FontFamily(name: str)

 FontFamily(name: str,fontCollection: FontCollection)

 FontFamily(genericFamily: GenericFontFamilies)
 """
 def Dispose(self):
  """
  Dispose(self: FontFamily)

   Releases all resources used by this System.Drawing.FontFamily.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: FontFamily,obj: object) -> bool

  

   Indicates whether the specified object is a System.Drawing.FontFamily and is identical to this 

    System.Drawing.FontFamily.

  

  

   obj: The object to test.

   Returns: true if obj is a System.Drawing.FontFamily and is identical to this System.Drawing.FontFamily; 

    otherwise,false.
  """
  pass
 def GetCellAscent(self,style):
  """
  GetCellAscent(self: FontFamily,style: FontStyle) -> int

  

   Returns the cell ascent,in design units,of the System.Drawing.FontFamily of the specified 

    style.

  

  

   style: A System.Drawing.FontStyle that contains style information for the font.

   Returns: The cell ascent for this System.Drawing.FontFamily that uses the specified 

    System.Drawing.FontStyle.
  """
  pass
 def GetCellDescent(self,style):
  """
  GetCellDescent(self: FontFamily,style: FontStyle) -> int

  

   Returns the cell descent,in design units,of the System.Drawing.FontFamily of the specified 

    style.

  

  

   style: A System.Drawing.FontStyle that contains style information for the font.

   Returns: The cell descent metric for this System.Drawing.FontFamily that uses the specified 

    System.Drawing.FontStyle.
  """
  pass
 def GetEmHeight(self,style):
  """
  GetEmHeight(self: FontFamily,style: FontStyle) -> int

  

   Gets the height,in font design units,of the em square for the specified style.

  

   style: The System.Drawing.FontStyle for which to get the em height.

   Returns: The height of the em square.
  """
  pass
 @staticmethod
 def GetFamilies(graphics):
  """
  GetFamilies(graphics: Graphics) -> Array[FontFamily]

  

   Returns an array that contains all the System.Drawing.FontFamily objects available for the 

    specified graphics context.

  

  

   graphics: The System.Drawing.Graphics object from which to return System.Drawing.FontFamily objects.

   Returns: An array of System.Drawing.FontFamily objects available for the specified 

    System.Drawing.Graphics object.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: FontFamily) -> int

  

   Gets a hash code for this System.Drawing.FontFamily.

   Returns: The hash code for this System.Drawing.FontFamily.
  """
  pass
 def GetLineSpacing(self,style):
  """
  GetLineSpacing(self: FontFamily,style: FontStyle) -> int

  

   Returns the line spacing,in design units,of the System.Drawing.FontFamily of the specified 

    style. The line spacing is the vertical distance between the base lines of two consecutive lines 

    of text.

  

  

   style: The System.Drawing.FontStyle to apply.

   Returns: The distance between two consecutive lines of text.
  """
  pass
 def GetName(self,language):
  """
  GetName(self: FontFamily,language: int) -> str

  

   Returns the name,in the specified language,of this System.Drawing.FontFamily.

  

   language: The language in which the name is returned.

   Returns: A System.String that represents the name,in the specified language,of this 

    System.Drawing.FontFamily.
  """
  pass
 def IsStyleAvailable(self,style):
  """
  IsStyleAvailable(self: FontFamily,style: FontStyle) -> bool

  

   Indicates whether the specified System.Drawing.FontStyle enumeration is available.

  

   style: The System.Drawing.FontStyle to test.

   Returns: true if the specified System.Drawing.FontStyle is available; otherwise,false.
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
 def ToString(self):
  """
  ToString(self: FontFamily) -> str

  

   Converts this System.Drawing.FontFamily to a human-readable string representation.

   Returns: The string that represents this System.Drawing.FontFamily.
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
  __new__(cls: type,name: str)

  __new__(cls: type,name: str,fontCollection: FontCollection)

  __new__(cls: type,genericFamily: GenericFontFamilies)
  """
  pass
 def __ne__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of this System.Drawing.FontFamily.



Get: Name(self: FontFamily) -> str



"""


 Families=None
 GenericMonospace=None
 GenericSansSerif=None
 GenericSerif=None

