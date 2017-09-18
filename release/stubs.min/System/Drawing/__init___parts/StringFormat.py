class StringFormat(MarshalByRefObject,ICloneable,IDisposable):
 """
 Encapsulates text layout information (such as alignment,orientation and tab stops) display manipulations (such as ellipsis insertion and national digit substitution) and OpenType features. This class cannot be inherited.

 

 StringFormat()

 StringFormat(options: StringFormatFlags)

 StringFormat(options: StringFormatFlags,language: int)

 StringFormat(format: StringFormat)
 """
 def Clone(self):
  """
  Clone(self: StringFormat) -> object

  

   Creates an exact copy of this System.Drawing.StringFormat object.

   Returns: The System.Drawing.StringFormat object this method creates.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: StringFormat)

   Releases all resources used by this System.Drawing.StringFormat object.
  """
  pass
 def GetTabStops(self,firstTabOffset):
  """
  GetTabStops(self: StringFormat) -> (Array[Single],Single)

  

   Gets the tab stops for this System.Drawing.StringFormat object.

   Returns: An array of distances (in number of spaces) between tab stops.
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
 def SetDigitSubstitution(self,language,substitute):
  """
  SetDigitSubstitution(self: StringFormat,language: int,substitute: StringDigitSubstitute)

   Specifies the language and method to be used when local digits are substituted for western 

    digits.

  

  

   language: A National Language Support (NLS) language identifier that identifies the language that will be 

    used when local digits are substituted for western digits. You can pass the 

    System.Globalization.CultureInfo.LCID property of a System.Globalization.CultureInfo object as 

    the NLS language identifier. For example,suppose you create a System.Globalization.CultureInfo 

    object by passing the string "ar-EG" to a System.Globalization.CultureInfo constructor. If you 

    pass the System.Globalization.CultureInfo.LCID property of that System.Globalization.CultureInfo 

    object along with System.Drawing.StringDigitSubstitute.Traditional to the 

    System.Drawing.StringFormat.SetDigitSubstitution(System.Int32,System.Drawing.StringDigitSubstitut

    e) method,then Arabic-Indic digits will be substituted for western digits at display time.

  

   substitute: An element of the System.Drawing.StringDigitSubstitute enumeration that specifies how digits are 

    displayed.
  """
  pass
 def SetMeasurableCharacterRanges(self,ranges):
  """
  SetMeasurableCharacterRanges(self: StringFormat,ranges: Array[CharacterRange])

   Specifies an array of System.Drawing.CharacterRange structures that represent the ranges of 

    characters measured by a call to the 

    System.Drawing.Graphics.MeasureCharacterRanges(System.String,System.Drawing.Font,System.Drawing.R

    ectangleF,System.Drawing.StringFormat) method.

  

  

   ranges: An array of System.Drawing.CharacterRange structures that specifies the ranges of characters 

    measured by a call to the 

    System.Drawing.Graphics.MeasureCharacterRanges(System.String,System.Drawing.Font,System.Drawing.R

    ectangleF,System.Drawing.StringFormat) method.
  """
  pass
 def SetTabStops(self,firstTabOffset,tabStops):
  """
  SetTabStops(self: StringFormat,firstTabOffset: Single,tabStops: Array[Single])

   Sets tab stops for this System.Drawing.StringFormat object.

  

   firstTabOffset: The number of spaces between the beginning of a line of text and the first tab stop.

   tabStops: An array of distances between tab stops in the units specified by the 

    System.Drawing.Graphics.PageUnit property.
  """
  pass
 def ToString(self):
  """
  ToString(self: StringFormat) -> str

  

   Converts this System.Drawing.StringFormat object to a human-readable string.

   Returns: A string representation of this System.Drawing.StringFormat object.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
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
  __new__(cls: type)

  __new__(cls: type,options: StringFormatFlags)

  __new__(cls: type,options: StringFormatFlags,language: int)

  __new__(cls: type,format: StringFormat)
  """
  pass
 def __str__(self,*args):
  pass
 Alignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets horizontal alignment of the string..



Get: Alignment(self: StringFormat) -> StringAlignment



Set: Alignment(self: StringFormat)=value

"""

 DigitSubstitutionLanguage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the language that is used when local digits are substituted for western digits.



Get: DigitSubstitutionLanguage(self: StringFormat) -> int



"""

 DigitSubstitutionMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the method to be used for digit substitution.



Get: DigitSubstitutionMethod(self: StringFormat) -> StringDigitSubstitute



"""

 FormatFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Drawing.StringFormatFlags enumeration that contains formatting information.



Get: FormatFlags(self: StringFormat) -> StringFormatFlags



Set: FormatFlags(self: StringFormat)=value

"""

 HotkeyPrefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Drawing.Text.HotkeyPrefix object for this System.Drawing.StringFormat object.



Get: HotkeyPrefix(self: StringFormat) -> HotkeyPrefix



Set: HotkeyPrefix(self: StringFormat)=value

"""

 LineAlignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the vertical alignment of the string.



Get: LineAlignment(self: StringFormat) -> StringAlignment



Set: LineAlignment(self: StringFormat)=value

"""

 Trimming=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Drawing.StringTrimming enumeration for this System.Drawing.StringFormat object.



Get: Trimming(self: StringFormat) -> StringTrimming



Set: Trimming(self: StringFormat)=value

"""


 GenericDefault=None
 GenericTypographic=None

