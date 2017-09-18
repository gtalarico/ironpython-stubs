class Uri(object,ISerializable):
 """
 Provides an object representation of a uniform resource identifier (URI) and easy access to the parts of the URI.

 

 Uri(uriString: str)

 Uri(uriString: str,dontEscape: bool)

 Uri(baseUri: Uri,relativeUri: str,dontEscape: bool)

 Uri(uriString: str,uriKind: UriKind)

 Uri(baseUri: Uri,relativeUri: str)

 Uri(baseUri: Uri,relativeUri: Uri)
 """
 def Canonicalize(self,*args):
  """
  Canonicalize(self: Uri)

   Converts the internally stored URI to canonical form.
  """
  pass
 @staticmethod
 def CheckHostName(name):
  """
  CheckHostName(name: str) -> UriHostNameType

  

   Determines whether the specified host name is a valid DNS name.

  

   name: The host name to validate. This can be an IPv4 or IPv6 address or an Internet host name.

   Returns: A System.UriHostNameType that indicates the type of the host name. If the type of the host name 

    cannot be determined or if the host name is null or a zero-length string,this method returns 

    System.UriHostNameType.Unknown.
  """
  pass
 @staticmethod
 def CheckSchemeName(schemeName):
  """
  CheckSchemeName(schemeName: str) -> bool

  

   Determines whether the specified scheme name is valid.

  

   schemeName: The scheme name to validate.

   Returns: A System.Boolean value that is true if the scheme name is valid; otherwise,false.
  """
  pass
 def CheckSecurity(self,*args):
  """
  CheckSecurity(self: Uri)

   Calling this method has no effect.
  """
  pass
 @staticmethod
 def Compare(uri1,uri2,partsToCompare,compareFormat,comparisonType):
  """
  Compare(uri1: Uri,uri2: Uri,partsToCompare: UriComponents,compareFormat: UriFormat,comparisonType: StringComparison) -> int

  

   Compares the specified parts of two URIs using the specified comparison rules.

  

   uri1: The first System.Uri.

   uri2: The second System.Uri.

   partsToCompare: A bitwise combination of the System.UriComponents values that specifies the parts of uri1 and 

    uri2 to compare.

  

   compareFormat: One of the System.UriFormat values that specifies the character escaping used when the URI 

    components are compared.

  

   comparisonType: One of the System.StringComparison values.

   Returns: An System.Int32 value that indicates the lexical relationship between the compared System.Uri 

    components.ValueMeaningLess than zerouri1 is less than uri2.Zerouri1 equals uri2.Greater than 

    zerouri1 is greater than uri2.
  """
  pass
 def Equals(self,comparand):
  """
  Equals(self: Uri,comparand: object) -> bool

  

   Compares two System.Uri instances for equality.

  

   comparand: The System.Uri instance or a URI identifier to compare with the current instance.

   Returns: A System.Boolean value that is true if the two instances represent the same URI; otherwise,

    false.
  """
  pass
 def Escape(self,*args):
  """
  Escape(self: Uri)

   Converts any unsafe or reserved characters in the path component to their hexadecimal character 

    representations.
  """
  pass
 @staticmethod
 def EscapeDataString(stringToEscape):
  """
  EscapeDataString(stringToEscape: str) -> str

  

   Converts a string to its escaped representation.

  

   stringToEscape: The string to escape.

   Returns: A System.String that contains the escaped representation of stringToEscape.
  """
  pass
 def EscapeString(self,*args):
  """
  EscapeString(str: str) -> str

  

   Converts a string to its escaped representation.

  

   str: The string to transform to its escaped representation.

   Returns: The escaped representation of the string.
  """
  pass
 @staticmethod
 def EscapeUriString(stringToEscape):
  """
  EscapeUriString(stringToEscape: str) -> str

  

   Converts a URI string to its escaped representation.

  

   stringToEscape: The string to escape.

   Returns: A System.String that contains the escaped representation of stringToEscape.
  """
  pass
 @staticmethod
 def FromHex(digit):
  """
  FromHex(digit: Char) -> int

  

   Gets the decimal value of a hexadecimal digit.

  

   digit: The hexadecimal digit (0-9,a-f,A-F) to convert.

   Returns: An System.Int32 value that contains a number from 0 to 15 that corresponds to the specified 

    hexadecimal digit.
  """
  pass
 def GetComponents(self,components,format):
  """
  GetComponents(self: Uri,components: UriComponents,format: UriFormat) -> str

  

   Gets the specified components of the current instance using the specified escaping for special 

    characters.

  

  

   components: A bitwise combination of the System.UriComponents values that specifies which parts of the 

    current instance to return to the caller.

  

   format: One of the System.UriFormat values that controls how special characters are escaped.

   Returns: A System.String that contains the components.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Uri) -> int

  

   Gets the hash code for the URI.

   Returns: An System.Int32 containing the hash value generated for this URI.
  """
  pass
 def GetLeftPart(self,part):
  """
  GetLeftPart(self: Uri,part: UriPartial) -> str

  

   Gets the specified portion of a System.Uri instance.

  

   part: One of the System.UriPartial values that specifies the end of the URI portion to return.

   Returns: A System.String that contains the specified portion of the System.Uri instance.
  """
  pass
 def GetObjectData(self,*args):
  """
  GetObjectData(self: Uri,serializationInfo: SerializationInfo,streamingContext: StreamingContext)

   Returns the data needed to serialize the current instance.

  

   serializationInfo: A System.Runtime.Serialization.SerializationInfo object containing the information required to 

    serialize the System.Uri.

  

   streamingContext: A System.Runtime.Serialization.StreamingContext object containing the source and destination of 

    the serialized stream associated with the System.Uri.
  """
  pass
 @staticmethod
 def HexEscape(character):
  """
  HexEscape(character: Char) -> str

  

   Converts a specified character into its hexadecimal equivalent.

  

   character: The character to convert to hexadecimal representation.

   Returns: The hexadecimal representation of the specified character.
  """
  pass
 @staticmethod
 def HexUnescape(pattern,index):
  """
  HexUnescape(pattern: str,index: int) -> (Char,int)

  

   Converts a specified hexadecimal representation of a character to the character.

  

   pattern: The hexadecimal representation of a character.

   index: The location in pattern where the hexadecimal representation of a character begins.

   Returns: The character represented by the hexadecimal encoding at position index. If the character at 

    index is not hexadecimal encoded,the character at index is returned. The value of index is 

    incremented to point to the character following the one returned.
  """
  pass
 def IsBadFileSystemCharacter(self,*args):
  """
  IsBadFileSystemCharacter(self: Uri,character: Char) -> bool

  

   Gets whether a character is invalid in a file system name.

  

   character: The System.Char to test.

   Returns: A System.Boolean value that is true if the specified character is invalid; otherwise false.
  """
  pass
 def IsBaseOf(self,uri):
  """
  IsBaseOf(self: Uri,uri: Uri) -> bool

  

   Determines whether the current System.Uri instance is a base of the specified System.Uri 

    instance.

  

  

   uri: The specified System.Uri instance to test.

   Returns: true if the current System.Uri instance is a base of uri; otherwise,false.
  """
  pass
 def IsExcludedCharacter(self,*args):
  """
  IsExcludedCharacter(character: Char) -> bool

  

   Gets whether the specified character should be escaped.

  

   character: The System.Char to test.

   Returns: A System.Boolean value that is true if the specified character should be escaped; otherwise,

    false.
  """
  pass
 @staticmethod
 def IsHexDigit(character):
  """
  IsHexDigit(character: Char) -> bool

  

   Determines whether a specified character is a valid hexadecimal digit.

  

   character: The character to validate.

   Returns: A System.Boolean value that is true if the character is a valid hexadecimal digit; otherwise 

    false.
  """
  pass
 @staticmethod
 def IsHexEncoding(pattern,index):
  """
  IsHexEncoding(pattern: str,index: int) -> bool

  

   Determines whether a character in a string is hexadecimal encoded.

  

   pattern: The string to check.

   index: The location in pattern to check for hexadecimal encoding.

   Returns: A System.Boolean value that is true if pattern is hexadecimal encoded at the specified location; 

    otherwise,false.
  """
  pass
 def IsReservedCharacter(self,*args):
  """
  IsReservedCharacter(self: Uri,character: Char) -> bool

  

   Gets whether the specified character is a reserved character.

  

   character: The System.Char to test.

   Returns: A System.Boolean value that is true if the specified character is a reserved character 

    otherwise,false.
  """
  pass
 def IsWellFormedOriginalString(self):
  """
  IsWellFormedOriginalString(self: Uri) -> bool

  

   Indicates whether the string used to construct this System.Uri was well-formed and is not 

    required to be further escaped.

  

   Returns: A System.Boolean value that is true if the string was well-formed; else false.
  """
  pass
 @staticmethod
 def IsWellFormedUriString(uriString,uriKind):
  """
  IsWellFormedUriString(uriString: str,uriKind: UriKind) -> bool

  

   Indicates whether the string is well-formed by attempting to construct a URI with the string and 

    ensures that the string does not require further escaping.

  

  

   uriString: The string used to attempt to construct a System.Uri.

   uriKind: The type of the System.Uri in uriString.

   Returns: A System.Boolean value that is true if the string was well-formed; else false.
  """
  pass
 def MakeRelative(self,toUri):
  """
  MakeRelative(self: Uri,toUri: Uri) -> str

  

   Determines the difference between two System.Uri instances.

  

   toUri: The URI to compare to the current URI.

   Returns: If the hostname and scheme of this URI instance and toUri are the same,then this method returns 

    a System.String that represents a relative URI that,when appended to the current URI instance,

    yields the toUri parameter.If the hostname or scheme is different,then this method returns a 

    System.String that represents the toUri parameter.
  """
  pass
 def MakeRelativeUri(self,uri):
  """
  MakeRelativeUri(self: Uri,uri: Uri) -> Uri

  

   Determines the difference between two System.Uri instances.

  

   uri: The URI to compare to the current URI.

   Returns: If the hostname and scheme of this URI instance and uri are the same,then this method returns a 

    relative System.Uri that,when appended to the current URI instance,yields uri.If the hostname 

    or scheme is different,then this method returns a System.Uri  that represents the uri 

    parameter.
  """
  pass
 def Parse(self,*args):
  """
  Parse(self: Uri)

   Parses the URI of the current instance to ensure it contains all the parts required for a valid 

    URI.
  """
  pass
 def ToString(self):
  """
  ToString(self: Uri) -> str

  

   Gets a canonical string representation for the specified System.Uri instance.

   Returns: A System.String instance that contains the unescaped canonical representation of the System.Uri 

    instance. All characters are unescaped except #,?,and %.
  """
  pass
 @staticmethod
 def TryCreate(*__args):
  """
  TryCreate(baseUri: Uri,relativeUri: Uri) -> (bool,Uri)

  

   Creates a new System.Uri using the specified base and relative System.Uri instances.

  

   baseUri: The base System.Uri.

   relativeUri: The relative System.Uri to add to the base System.Uri.

   Returns: A System.Boolean value that is true if the System.Uri was successfully created; otherwise,false.

  TryCreate(baseUri: Uri,relativeUri: str) -> (bool,Uri)

  

   Creates a new System.Uri using the specified base and relative System.String instances.

  

   baseUri: The base System.Uri.

   relativeUri: The relative System.Uri,represented as a System.String,to add to the base System.Uri.

   Returns: A System.Boolean value that is true if the System.Uri was successfully created; otherwise,false.

  TryCreate(uriString: str,uriKind: UriKind) -> (bool,Uri)

  

   Creates a new System.Uri using the specified System.String instance and a System.UriKind.

  

   uriString: The System.String representing the System.Uri.

   uriKind: The type of the Uri.

   Returns: A System.Boolean value that is true if the System.Uri was successfully created; otherwise,false.
  """
  pass
 def Unescape(self,*args):
  """
  Unescape(self: Uri,path: str) -> str

  

   Converts the specified string by replacing any escape sequences with their unescaped 

    representation.

  

  

   path: The System.String to convert.

   Returns: A System.String that contains the unescaped value of the path parameter.
  """
  pass
 @staticmethod
 def UnescapeDataString(stringToUnescape):
  """
  UnescapeDataString(stringToUnescape: str) -> str

  

   Converts a string to its unescaped representation.

  

   stringToUnescape: The string to unescape.

   Returns: A System.String that contains the unescaped representation of stringToUnescape.
  """
  pass
 def __cmp__(self,*args):
  """ x.__cmp__(y) <==> cmp(x,y) """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,uriString: str)

  __new__(cls: type,uriString: str,dontEscape: bool)

  __new__(cls: type,baseUri: Uri,relativeUri: str,dontEscape: bool)

  __new__(cls: type,uriString: str,uriKind: UriKind)

  __new__(cls: type,baseUri: Uri,relativeUri: str)

  __new__(cls: type,baseUri: Uri,relativeUri: Uri)

  __new__(cls: type,serializationInfo: SerializationInfo,streamingContext: StreamingContext)
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 AbsolutePath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the absolute path of the URI.



Get: AbsolutePath(self: Uri) -> str



"""

 AbsoluteUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the absolute URI.



Get: AbsoluteUri(self: Uri) -> str



"""

 Authority=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Domain Name System (DNS) host name or IP address and the port number for a server.



Get: Authority(self: Uri) -> str



"""

 DnsSafeHost=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an unescaped host name that is safe to use for DNS resolution.



Get: DnsSafeHost(self: Uri) -> str



"""

 Fragment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the escaped URI fragment.



Get: Fragment(self: Uri) -> str



"""

 Host=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the host component of this instance.



Get: Host(self: Uri) -> str



"""

 HostNameType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of the host name specified in the URI.



Get: HostNameType(self: Uri) -> UriHostNameType



"""

 IdnHost=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IdnHost(self: Uri) -> str



"""

 IsAbsoluteUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the System.Uri instance is absolute.



Get: IsAbsoluteUri(self: Uri) -> bool



"""

 IsDefaultPort=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the port value of the URI is the default for this scheme.



Get: IsDefaultPort(self: Uri) -> bool



"""

 IsFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the specified System.Uri is a file URI.



Get: IsFile(self: Uri) -> bool



"""

 IsLoopback=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the specified System.Uri references the local host.



Get: IsLoopback(self: Uri) -> bool



"""

 IsUnc=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the specified System.Uri is a universal naming convention (UNC) path.



Get: IsUnc(self: Uri) -> bool



"""

 LocalPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a local operating-system representation of a file name.



Get: LocalPath(self: Uri) -> str



"""

 OriginalString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the original URI string that was passed to the System.Uri constructor.



Get: OriginalString(self: Uri) -> str



"""

 PathAndQuery=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Uri.AbsolutePath and System.Uri.Query properties separated by a question mark (?).



Get: PathAndQuery(self: Uri) -> str



"""

 Port=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the port number of this URI.



Get: Port(self: Uri) -> int



"""

 Query=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets any query information included in the specified URI.



Get: Query(self: Uri) -> str



"""

 Scheme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the scheme name for this URI.



Get: Scheme(self: Uri) -> str



"""

 Segments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an array containing the path segments that make up the specified URI.



Get: Segments(self: Uri) -> Array[str]



"""

 UserEscaped=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates that the URI string was completely escaped before the System.Uri instance was created.



Get: UserEscaped(self: Uri) -> bool



"""

 UserInfo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the user name,password,or other user-specific information associated with the specified URI.



Get: UserInfo(self: Uri) -> str



"""


 SchemeDelimiter='://'
 UriSchemeFile='file'
 UriSchemeFtp='ftp'
 UriSchemeGopher='gopher'
 UriSchemeHttp='http'
 UriSchemeHttps='https'
 UriSchemeMailto='mailto'
 UriSchemeNetPipe='net.pipe'
 UriSchemeNetTcp='net.tcp'
 UriSchemeNews='news'
 UriSchemeNntp='nntp'

