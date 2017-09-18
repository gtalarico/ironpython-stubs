class UriBuilder(object):
 """
 Provides a custom constructor for uniform resource identifiers (URIs) and modifies URIs for the System.Uri class.

 

 UriBuilder()

 UriBuilder(uri: str)

 UriBuilder(uri: Uri)

 UriBuilder(schemeName: str,hostName: str)

 UriBuilder(scheme: str,host: str,portNumber: int)

 UriBuilder(scheme: str,host: str,port: int,pathValue: str)

 UriBuilder(scheme: str,host: str,port: int,path: str,extraValue: str)
 """
 def Equals(self,rparam):
  """
  Equals(self: UriBuilder,rparam: object) -> bool

  

   Compares an existing System.Uri instance with the contents of the System.UriBuilder for equality.

  

   rparam: The object to compare with the current instance.

   Returns: true if rparam represents the same System.Uri as the System.Uri constructed by this 

    System.UriBuilder instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: UriBuilder) -> int

  

   Returns the hash code for the URI.

   Returns: The hash code generated for the URI.
  """
  pass
 def ToString(self):
  """
  ToString(self: UriBuilder) -> str

  

   Returns the display string for the specified System.UriBuilder instance.

   Returns: The string that contains the unescaped display string of the System.UriBuilder.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,uri: str)

  __new__(cls: type,uri: Uri)

  __new__(cls: type,schemeName: str,hostName: str)

  __new__(cls: type,scheme: str,host: str,portNumber: int)

  __new__(cls: type,scheme: str,host: str,port: int,pathValue: str)

  __new__(cls: type,scheme: str,host: str,port: int,path: str,extraValue: str)
  """
  pass
 def __ne__(self,*args):
  pass
 Fragment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the fragment portion of the URI.



Get: Fragment(self: UriBuilder) -> str



Set: Fragment(self: UriBuilder)=value

"""

 Host=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Domain Name System (DNS) host name or IP address of a server.



Get: Host(self: UriBuilder) -> str



Set: Host(self: UriBuilder)=value

"""

 Password=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the password associated with the user that accesses the URI.



Get: Password(self: UriBuilder) -> str



Set: Password(self: UriBuilder)=value

"""

 Path=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the path to the resource referenced by the URI.



Get: Path(self: UriBuilder) -> str



Set: Path(self: UriBuilder)=value

"""

 Port=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the port number of the URI.



Get: Port(self: UriBuilder) -> int



Set: Port(self: UriBuilder)=value

"""

 Query=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets any query information included in the URI.



Get: Query(self: UriBuilder) -> str



Set: Query(self: UriBuilder)=value

"""

 Scheme=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the scheme name of the URI.



Get: Scheme(self: UriBuilder) -> str



Set: Scheme(self: UriBuilder)=value

"""

 Uri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Uri instance constructed by the specified System.UriBuilder instance.



Get: Uri(self: UriBuilder) -> Uri



"""

 UserName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The user name associated with the user that accesses the URI.



Get: UserName(self: UriBuilder) -> str



Set: UserName(self: UriBuilder)=value

"""


