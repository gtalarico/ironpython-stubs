class UriParser(object):
 """ Parses a new URI scheme. This is an abstract class. """
 def GetComponents(self,*args):
  """
  GetComponents(self: UriParser,uri: Uri,components: UriComponents,format: UriFormat) -> str

  

   Gets the components from a URI.

  

   uri: The URI to parse.

   components: The System.UriComponents to retrieve from uri.

   format: One of the System.UriFormat values that controls how special characters are escaped.

   Returns: A string that contains the components.
  """
  pass
 def InitializeAndValidate(self,*args):
  """
  InitializeAndValidate(self: UriParser,uri: Uri) -> UriFormatException

  

   Initialize the state of the parser and validate the URI.

  

   uri: The T:System.Uri to validate.
  """
  pass
 def IsBaseOf(self,*args):
  """
  IsBaseOf(self: UriParser,baseUri: Uri,relativeUri: Uri) -> bool

  

   Determines whether baseUri is a base URI for relativeUri.

  

   baseUri: The base URI.

   relativeUri: The URI to test.

   Returns: true if baseUri is a base URI for relativeUri; otherwise,false.
  """
  pass
 @staticmethod
 def IsKnownScheme(schemeName):
  """
  IsKnownScheme(schemeName: str) -> bool

  

   Indicates whether the parser for a scheme is registered.

  

   schemeName: The scheme name to check.

   Returns: true if schemeName has been registered; otherwise,false.
  """
  pass
 def IsWellFormedOriginalString(self,*args):
  """
  IsWellFormedOriginalString(self: UriParser,uri: Uri) -> bool

  

   Indicates whether a URI is well-formed.

  

   uri: The URI to check.

   Returns: true if uri is well-formed; otherwise,false.
  """
  pass
 def OnNewUri(self,*args):
  """
  OnNewUri(self: UriParser) -> UriParser

  

   Invoked by a System.Uri constructor to get a System.UriParser instance

   Returns: A System.UriParser for the constructed System.Uri.
  """
  pass
 def OnRegister(self,*args):
  """
  OnRegister(self: UriParser,schemeName: str,defaultPort: int)

   Invoked by the Framework when a System.UriParser method is registered.

  

   schemeName: The scheme that is associated with this System.UriParser.

   defaultPort: The port number of the scheme.
  """
  pass
 @staticmethod
 def Register(uriParser,schemeName,defaultPort):
  """
  Register(uriParser: UriParser,schemeName: str,defaultPort: int)

   Associates a scheme and port number with a System.UriParser.

  

   uriParser: The URI parser to register.

   schemeName: The name of the scheme that is associated with this parser.

   defaultPort: The default port number for the specified scheme.
  """
  pass
 def Resolve(self,*args):
  """
  Resolve(self: UriParser,baseUri: Uri,relativeUri: Uri) -> (str,UriFormatException)

  

   Called by System.Uri constructors and erload:System.Uri.TryCreate to resolve a relative URI.

  

   baseUri: A base URI.

   relativeUri: A relative URI.

   Returns: The string of the resolved relative System.Uri.
  """
  pass
