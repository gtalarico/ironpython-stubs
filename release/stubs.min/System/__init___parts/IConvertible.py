class IConvertible:
 """ Defines methods that convert the value of the implementing reference or value type to a common language runtime type that has an equivalent value. """
 def GetTypeCode(self):
  """
  GetTypeCode(self: IConvertible) -> TypeCode

  

   Returns the System.TypeCode for this instance.

   Returns: The enumerated constant that is the System.TypeCode of the class or value type that implements 

    this interface.
  """
  pass
 def ToBoolean(self,provider):
  """
  ToBoolean(self: IConvertible,provider: IFormatProvider) -> bool

  

   Converts the value of this instance to an equivalent Boolean value using the specified 

    culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: A Boolean value equivalent to the value of this instance.
  """
  pass
 def ToByte(self,provider):
  """
  ToByte(self: IConvertible,provider: IFormatProvider) -> Byte

  

   Converts the value of this instance to an equivalent 8-bit unsigned integer using the specified 

    culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: An 8-bit unsigned integer equivalent to the value of this instance.
  """
  pass
 def ToChar(self,provider):
  """
  ToChar(self: IConvertible,provider: IFormatProvider) -> Char

  

   Converts the value of this instance to an equivalent Unicode character using the specified 

    culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: A Unicode character equivalent to the value of this instance.
  """
  pass
 def ToDateTime(self,provider):
  """
  ToDateTime(self: IConvertible,provider: IFormatProvider) -> DateTime

  

   Converts the value of this instance to an equivalent System.DateTime using the specified 

    culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: A System.DateTime instance equivalent to the value of this instance.
  """
  pass
 def ToDecimal(self,provider):
  """
  ToDecimal(self: IConvertible,provider: IFormatProvider) -> Decimal

  

   Converts the value of this instance to an equivalent System.Decimal number using the specified 

    culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: A System.Decimal number equivalent to the value of this instance.
  """
  pass
 def ToDouble(self,provider):
  """
  ToDouble(self: IConvertible,provider: IFormatProvider) -> float

  

   Converts the value of this instance to an equivalent double-precision floating-point number 

    using the specified culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: A double-precision floating-point number equivalent to the value of this instance.
  """
  pass
 def ToInt16(self,provider):
  """
  ToInt16(self: IConvertible,provider: IFormatProvider) -> Int16

  

   Converts the value of this instance to an equivalent 16-bit signed integer using the specified 

    culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: An 16-bit signed integer equivalent to the value of this instance.
  """
  pass
 def ToInt32(self,provider):
  """
  ToInt32(self: IConvertible,provider: IFormatProvider) -> int

  

   Converts the value of this instance to an equivalent 32-bit signed integer using the specified 

    culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: An 32-bit signed integer equivalent to the value of this instance.
  """
  pass
 def ToInt64(self,provider):
  """
  ToInt64(self: IConvertible,provider: IFormatProvider) -> Int64

  

   Converts the value of this instance to an equivalent 64-bit signed integer using the specified 

    culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: An 64-bit signed integer equivalent to the value of this instance.
  """
  pass
 def ToSByte(self,provider):
  """
  ToSByte(self: IConvertible,provider: IFormatProvider) -> SByte

  

   Converts the value of this instance to an equivalent 8-bit signed integer using the specified 

    culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: An 8-bit signed integer equivalent to the value of this instance.
  """
  pass
 def ToSingle(self,provider):
  """
  ToSingle(self: IConvertible,provider: IFormatProvider) -> Single

  

   Converts the value of this instance to an equivalent single-precision floating-point number 

    using the specified culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: A single-precision floating-point number equivalent to the value of this instance.
  """
  pass
 def ToString(self,provider):
  """
  ToString(self: IConvertible,provider: IFormatProvider) -> str

  

   Converts the value of this instance to an equivalent System.String using the specified 

    culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: A System.String instance equivalent to the value of this instance.
  """
  pass
 def ToType(self,conversionType,provider):
  """
  ToType(self: IConvertible,conversionType: Type,provider: IFormatProvider) -> object

  

   Converts the value of this instance to an System.Object of the specified System.Type that has an 

    equivalent value,using the specified culture-specific formatting information.

  

  

   conversionType: The System.Type to which the value of this instance is converted.

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: An System.Object instance of type conversionType whose value is equivalent to the value of this 

    instance.
  """
  pass
 def ToUInt16(self,provider):
  """
  ToUInt16(self: IConvertible,provider: IFormatProvider) -> UInt16

  

   Converts the value of this instance to an equivalent 16-bit unsigned integer using the specified 

    culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: An 16-bit unsigned integer equivalent to the value of this instance.
  """
  pass
 def ToUInt32(self,provider):
  """
  ToUInt32(self: IConvertible,provider: IFormatProvider) -> UInt32

  

   Converts the value of this instance to an equivalent 32-bit unsigned integer using the specified 

    culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: An 32-bit unsigned integer equivalent to the value of this instance.
  """
  pass
 def ToUInt64(self,provider):
  """
  ToUInt64(self: IConvertible,provider: IFormatProvider) -> UInt64

  

   Converts the value of this instance to an equivalent 64-bit unsigned integer using the specified 

    culture-specific formatting information.

  

  

   provider: An System.IFormatProvider interface implementation that supplies culture-specific formatting 

    information.

  

   Returns: An 64-bit unsigned integer equivalent to the value of this instance.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
