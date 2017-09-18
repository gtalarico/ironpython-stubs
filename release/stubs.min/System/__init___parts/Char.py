class Char(object,IComparable,IConvertible,IComparable[Char],IEquatable[Char]):
 """ Represents a character as a UTF-16 code unit. """
 def CompareTo(self,value):
  """
  CompareTo(self: Char,value: Char) -> int

  

   Compares this instance to a specified System.Char object and indicates whether this instance 

    precedes,follows,or appears in the same position in the sort order as the specified 

    System.Char object.

  

  

   value: A System.Char object to compare.

   Returns: A signed number indicating the position of this instance in the sort order in relation to the 

    value parameter.Return Value Description Less than zero This instance precedes value. Zero This 

    instance has the same position in the sort order as value. Greater than zero This instance 

    follows value.

  

  CompareTo(self: Char,value: object) -> int

  

   Compares this instance to a specified object and indicates whether this instance precedes,

    follows,or appears in the same position in the sort order as the specified System.Object.

  

  

   value: An object to compare this instance to,or null.

   Returns: A signed number indicating the position of this instance in the sort order in relation to the 

    value parameter.Return Value Description Less than zero This instance precedes value. Zero This 

    instance has the same position in the sort order as value. Greater than zero This instance 

    follows value.-or- value is null.
  """
  pass
 @staticmethod
 def ConvertFromUtf32(utf32):
  """
  ConvertFromUtf32(utf32: int) -> str

  

   Converts the specified Unicode code point into a UTF-16 encoded string.

  

   utf32: A 21-bit Unicode code point.

   Returns: A string consisting of one System.Char object or a surrogate pair of System.Char objects 

    equivalent to the code point specified by the utf32 parameter.
  """
  pass
 @staticmethod
 def ConvertToUtf32(*__args):
  """
  ConvertToUtf32(s: str,index: int) -> int

  

   Converts the value of a UTF-16 encoded character or surrogate pair at a specified position in a 

    string into a Unicode code point.

  

  

   s: A string that contains a character or surrogate pair.

   index: The index position of the character or surrogate pair in s.

   Returns: The 21-bit Unicode code point represented by the character or surrogate pair at the position in 

    the s parameter specified by the index parameter.

  

  ConvertToUtf32(highSurrogate: Char,lowSurrogate: Char) -> int

  

   Converts the value of a UTF-16 encoded surrogate pair into a Unicode code point.

  

   highSurrogate: A high surrogate code unit (that is,a code unit ranging from U+D800 through U+DBFF).

   lowSurrogate: A low surrogate code unit (that is,a code unit ranging from U+DC00 through U+DFFF).

   Returns: The 21-bit Unicode code point represented by the highSurrogate and lowSurrogate parameters.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: Char,obj: Char) -> bool

  

   Returns a value that indicates whether this instance is equal to the specified System.Char 

    object.

  

  

   obj: An object to compare to this instance.

   Returns: true if the obj parameter equals the value of this instance; otherwise,false.

  Equals(self: Char,obj: object) -> bool

  

   Returns a value that indicates whether this instance is equal to a specified object.

  

   obj: An object to compare with this instance or null.

   Returns: true if obj is an instance of System.Char and equals the value of this instance; otherwise,

    false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Char) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 @staticmethod
 def GetNumericValue(*__args):
  """
  GetNumericValue(s: str,index: int) -> float

  

   Converts the numeric Unicode character at the specified position in a specified string to a 

    double-precision floating point number.

  

  

   s: A System.String.

   index: The character position in s.

   Returns: The numeric value of the character at position index in s if that character represents a number; 

    otherwise,-1.

  

  GetNumericValue(c: Char) -> float

  

   Converts the specified numeric Unicode character to a double-precision floating point number.

  

   c: The Unicode character to convert.

   Returns: The numeric value of c if that character represents a number; otherwise,-1.0.
  """
  pass
 def GetTypeCode(self):
  """
  GetTypeCode(self: Char) -> TypeCode

  

   Returns the System.TypeCode for value type System.Char.

   Returns: The enumerated constant,System.TypeCode.Char.
  """
  pass
 @staticmethod
 def GetUnicodeCategory(*__args):
  """
  GetUnicodeCategory(s: str,index: int) -> UnicodeCategory

  

   Categorizes the character at the specified position in a specified string into a group 

    identified by one of the System.Globalization.UnicodeCategory values.

  

  

   s: A System.String.

   index: The character position in s.

   Returns: A System.Globalization.UnicodeCategory enumerated constant that identifies the group that 

    contains the character at position index in s.

  

  GetUnicodeCategory(c: Char) -> UnicodeCategory

  

   Categorizes a specified Unicode character into a group identified by one of the 

    System.Globalization.UnicodeCategory values.

  

  

   c: The Unicode character to categorize.

   Returns: A System.Globalization.UnicodeCategory value that identifies the group that contains c.
  """
  pass
 @staticmethod
 def IsControl(*__args):
  """
  IsControl(s: str,index: int) -> bool

  

   Indicates whether the character at the specified position in a specified string is categorized 

    as a control character.

  

  

   s: A string.

   index: The position of the character to evaluate in s.

   Returns: true if the character at position index in s is a control character; otherwise,false.

  IsControl(c: Char) -> bool

  

   Indicates whether the specified Unicode character is categorized as a control character.

  

   c: The Unicode character to evaluate.

   Returns: true if c is a control character; otherwise,false.
  """
  pass
 @staticmethod
 def IsDigit(*__args):
  """
  IsDigit(s: str,index: int) -> bool

  

   Indicates whether the character at the specified position in a specified string is categorized 

    as a decimal digit.

  

  

   s: A string.

   index: The position of the character to evaluate in s.

   Returns: true if the character at position index in s is a decimal digit; otherwise,false.

  IsDigit(c: Char) -> bool

  

   Indicates whether the specified Unicode character is categorized as a decimal digit.

  

   c: The Unicode character to evaluate.

   Returns: true if c is a decimal digit; otherwise,false.
  """
  pass
 @staticmethod
 def IsHighSurrogate(*__args):
  """
  IsHighSurrogate(s: str,index: int) -> bool

  

   Indicates whether the System.Char object at the specified position in a string is a high 

    surrogate.

  

  

   s: A string.

   index: The position of the character to evaluate in s.

   Returns: true if the numeric value of the specified character in the s parameter ranges from U+D800 

    through U+DBFF; otherwise,false.

  

  IsHighSurrogate(c: Char) -> bool

  

   Indicates whether the specified System.Char object is a high surrogate.

  

   c: The Unicode character to evaluate.

   Returns: true if the numeric value of the c parameter ranges from U+D800 through U+DBFF; otherwise,false.
  """
  pass
 @staticmethod
 def IsLetter(*__args):
  """
  IsLetter(s: str,index: int) -> bool

  

   Indicates whether the character at the specified position in a specified string is categorized 

    as a Unicode letter.

  

  

   s: A string.

   index: The position of the character to evaluate in s.

   Returns: true if the character at position index in s is a letter; otherwise,false.

  IsLetter(c: Char) -> bool

  

   Indicates whether the specified Unicode character is categorized as a Unicode letter.

  

   c: The Unicode character to evaluate.

   Returns: true if c is a letter; otherwise,false.
  """
  pass
 @staticmethod
 def IsLetterOrDigit(*__args):
  """
  IsLetterOrDigit(s: str,index: int) -> bool

  

   Indicates whether the character at the specified position in a specified string is categorized 

    as a letter or a decimal digit.

  

  

   s: A string.

   index: The position of the character to evaluate in s.

   Returns: true if the character at position index in s is a letter or a decimal digit; otherwise,false.

  IsLetterOrDigit(c: Char) -> bool

  

   Indicates whether the specified Unicode character is categorized as a letter or a decimal digit.

  

   c: The Unicode character to evaluate.

   Returns: true if c is a letter or a decimal digit; otherwise,false.
  """
  pass
 @staticmethod
 def IsLower(*__args):
  """
  IsLower(s: str,index: int) -> bool

  

   Indicates whether the character at the specified position in a specified string is categorized 

    as a lowercase letter.

  

  

   s: A string.

   index: The position of the character to evaluate in s.

   Returns: true if the character at position index in s is a lowercase letter; otherwise,false.

  IsLower(c: Char) -> bool

  

   Indicates whether the specified Unicode character is categorized as a lowercase letter.

  

   c: The Unicode character to evaluate.

   Returns: true if c is a lowercase letter; otherwise,false.
  """
  pass
 @staticmethod
 def IsLowSurrogate(*__args):
  """
  IsLowSurrogate(s: str,index: int) -> bool

  

   Indicates whether the System.Char object at the specified position in a string is a low 

    surrogate.

  

  

   s: A string.

   index: The position of the character to evaluate in s.

   Returns: true if the numeric value of the specified character in the s parameter ranges from U+DC00 

    through U+DFFF; otherwise,false.

  

  IsLowSurrogate(c: Char) -> bool

  

   Indicates whether the specified System.Char object is a low surrogate.

  

   c: The character to evaluate.

   Returns: true if the numeric value of the c parameter ranges from U+DC00 through U+DFFF; otherwise,false.
  """
  pass
 @staticmethod
 def IsNumber(*__args):
  """
  IsNumber(s: str,index: int) -> bool

  

   Indicates whether the character at the specified position in a specified string is categorized 

    as a number.

  

  

   s: A string.

   index: The position of the character to evaluate in s.

   Returns: true if the character at position index in s is a number; otherwise,false.

  IsNumber(c: Char) -> bool

  

   Indicates whether the specified Unicode character is categorized as a number.

  

   c: The Unicode character to evaluate.

   Returns: true if c is a number; otherwise,false.
  """
  pass
 @staticmethod
 def IsPunctuation(*__args):
  """
  IsPunctuation(s: str,index: int) -> bool

  

   Indicates whether the character at the specified position in a specified string is categorized 

    as a punctuation mark.

  

  

   s: A string.

   index: The position of the character to evaluate in s.

   Returns: true if the character at position index in s is a punctuation mark; otherwise,false.

  IsPunctuation(c: Char) -> bool

  

   Indicates whether the specified Unicode character is categorized as a punctuation mark.

  

   c: The Unicode character to evaluate.

   Returns: true if c is a punctuation mark; otherwise,false.
  """
  pass
 @staticmethod
 def IsSeparator(*__args):
  """
  IsSeparator(s: str,index: int) -> bool

  

   Indicates whether the character at the specified position in a specified string is categorized 

    as a separator character.

  

  

   s: A string.

   index: The position of the character to evaluate in s.

   Returns: true if the character at position index in s is a separator character; otherwise,false.

  IsSeparator(c: Char) -> bool

  

   Indicates whether the specified Unicode character is categorized as a separator character.

  

   c: The Unicode character to evaluate.

   Returns: true if c is a separator character; otherwise,false.
  """
  pass
 @staticmethod
 def IsSurrogate(*__args):
  """
  IsSurrogate(s: str,index: int) -> bool

  

   Indicates whether the character at the specified position in a specified string has a surrogate 

    code unit.

  

  

   s: A string.

   index: The position of the character to evaluate in s.

   Returns: true if the character at position index in s is a either a high surrogate or a low surrogate; 

    otherwise,false.

  

  IsSurrogate(c: Char) -> bool

  

   Indicates whether the specified character has a surrogate code unit.

  

   c: The Unicode character to evaluate.

   Returns: true if c is either a high surrogate or a low surrogate; otherwise,false.
  """
  pass
 @staticmethod
 def IsSurrogatePair(*__args):
  """
  IsSurrogatePair(highSurrogate: Char,lowSurrogate: Char) -> bool

  

   Indicates whether the two specified System.Char objects form a surrogate pair.

  

   highSurrogate: The character to evaluate as the high surrogate of a surrogate pair.

   lowSurrogate: The character to evaluate as the low surrogate of a surrogate pair.

   Returns: true if the numeric value of the highSurrogate parameter ranges from U+D800 through U+DBFF,and 

    the numeric value of the lowSurrogate parameter ranges from U+DC00 through U+DFFF; otherwise,

    false.

  

  IsSurrogatePair(s: str,index: int) -> bool

  

   Indicates whether two adjacent System.Char objects at a specified position in a string form a 

    surrogate pair.

  

  

   s: A string.

   index: The starting position of the pair of characters to evaluate within s.

   Returns: true if the s parameter includes adjacent characters at positions index and index + 1,and the 

    numeric value of the character at position index ranges from U+D800 through U+DBFF,and the 

    numeric value of the character at position index+1 ranges from U+DC00 through U+DFFF; otherwise,

    false.
  """
  pass
 @staticmethod
 def IsSymbol(*__args):
  """
  IsSymbol(s: str,index: int) -> bool

  

   Indicates whether the character at the specified position in a specified string is categorized 

    as a symbol character.

  

  

   s: A string.

   index: The position of the character to evaluate in s.

   Returns: true if the character at position index in s is a symbol character; otherwise,false.

  IsSymbol(c: Char) -> bool

  

   Indicates whether the specified Unicode character is categorized as a symbol character.

  

   c: The Unicode character to evaluate.

   Returns: true if c is a symbol character; otherwise,false.
  """
  pass
 @staticmethod
 def IsUpper(*__args):
  """
  IsUpper(s: str,index: int) -> bool

  

   Indicates whether the character at the specified position in a specified string is categorized 

    as an uppercase letter.

  

  

   s: A string.

   index: The position of the character to evaluate in s.

   Returns: true if the character at position index in s is an uppercase letter; otherwise,false.

  IsUpper(c: Char) -> bool

  

   Indicates whether the specified Unicode character is categorized as an uppercase letter.

  

   c: The Unicode character to evaluate.

   Returns: true if c is an uppercase letter; otherwise,false.
  """
  pass
 @staticmethod
 def IsWhiteSpace(*__args):
  """
  IsWhiteSpace(s: str,index: int) -> bool

  

   Indicates whether the character at the specified position in a specified string is categorized 

    as white space.

  

  

   s: A string.

   index: The position of the character to evaluate in s.

   Returns: true if the character at position index in s is white space; otherwise,false.

  IsWhiteSpace(c: Char) -> bool

  

   Indicates whether the specified Unicode character is categorized as white space.

  

   c: The Unicode character to evaluate.

   Returns: true if c is white space; otherwise,false.
  """
  pass
 @staticmethod
 def Parse(s):
  """
  Parse(s: str) -> Char

  

   Converts the value of the specified string to its equivalent Unicode character.

  

   s: A string that contains a single character,or null.

   Returns: A Unicode character equivalent to the sole character in s.
  """
  pass
 @staticmethod
 def ToLower(c,culture=None):
  """
  ToLower(c: Char) -> Char

  

   Converts the value of a Unicode character to its lowercase equivalent.

  

   c: The Unicode character to convert.

   Returns: The lowercase equivalent of c,or the unchanged value of c,if c is already lowercase or not 

    alphabetic.

  

  ToLower(c: Char,culture: CultureInfo) -> Char

  

   Converts the value of a specified Unicode character to its lowercase equivalent using specified 

    culture-specific formatting information.

  

  

   c: The Unicode character to convert.

   culture: An object that supplies culture-specific casing rules.

   Returns: The lowercase equivalent of c,modified according to culture,or the unchanged value of c,if c 

    is already lowercase or not alphabetic.
  """
  pass
 @staticmethod
 def ToLowerInvariant(c):
  """
  ToLowerInvariant(c: Char) -> Char

  

   Converts the value of a Unicode character to its lowercase equivalent using the casing rules of 

    the invariant culture.

  

  

   c: The Unicode character to convert.

   Returns: The lowercase equivalent of the c parameter,or the unchanged value of c,if c is already 

    lowercase or not alphabetic.
  """
  pass
 def ToString(self,*__args):
  """
  ToString(c: Char) -> str

  

   Converts the specified Unicode character to its equivalent string representation.

  

   c: The Unicode character to convert.

   Returns: The string representation of the value of c.

  ToString(self: Char,provider: IFormatProvider) -> str

  

   Converts the value of this instance to its equivalent string representation using the specified 

    culture-specific format information.

  

  

   provider: (Reserved) An object that supplies culture-specific formatting information.

   Returns: The string representation of the value of this instance as specified by provider.

  ToString(self: Char) -> str

  

   Converts the value of this instance to its equivalent string representation.

   Returns: The string representation of the value of this instance.
  """
  pass
 @staticmethod
 def ToUpper(c,culture=None):
  """
  ToUpper(c: Char) -> Char

  

   Converts the value of a Unicode character to its uppercase equivalent.

  

   c: The Unicode character to convert.

   Returns: The uppercase equivalent of c,or the unchanged value of c if c is already uppercase,has no 

    uppercase equivalent,or is not alphabetic.

  

  ToUpper(c: Char,culture: CultureInfo) -> Char

  

   Converts the value of a specified Unicode character to its uppercase equivalent using specified 

    culture-specific formatting information.

  

  

   c: The Unicode character to convert.

   culture: An object that supplies culture-specific casing rules.

   Returns: The uppercase equivalent of c,modified according to culture,or the unchanged value of c if c 

    is already uppercase,has no uppercase equivalent,or is not alphabetic.
  """
  pass
 @staticmethod
 def ToUpperInvariant(c):
  """
  ToUpperInvariant(c: Char) -> Char

  

   Converts the value of a Unicode character to its uppercase equivalent using the casing rules of 

    the invariant culture.

  

  

   c: The Unicode character to convert.

   Returns: The uppercase equivalent of the c parameter,or the unchanged value of c,if c is already 

    uppercase or not alphabetic.
  """
  pass
 @staticmethod
 def TryParse(s,result):
  """
  TryParse(s: str) -> (bool,Char)

  

   Converts the value of the specified string to its equivalent Unicode character. A return code 

    indicates whether the conversion succeeded or failed.

  

  

   s: A string that contains a single character,or null.

   Returns: true if the s parameter was converted successfully; otherwise,false.
  """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y) """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: Char,other: str) -> bool

  __contains__(self: Char,other: Char) -> bool
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __hash__(self,*args):
  """ x.__hash__() <==> hash(x) """
  pass
 def __index__(self,*args):
  """ __index__(self: Char) -> int """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: Char) -> str """
  pass
 def __str__(self,*args):
  pass
 MaxValue=None
 MinValue=None

