class NetworkCredential(object,ICredentials,ICredentialsByHost):
 """
 Provides credentials for password-based authentication schemes such as basic,digest,NTLM,and Kerberos authentication.

 

 NetworkCredential(userName: str,password: str)

 NetworkCredential()

 NetworkCredential(userName: str,password: SecureString)

 NetworkCredential(userName: str,password: str,domain: str)

 NetworkCredential(userName: str,password: SecureString,domain: str)
 """
 def GetCredential(self,*__args):
  """
  GetCredential(self: NetworkCredential,host: str,port: int,authenticationType: str) -> NetworkCredential

  

   Returns an instance of the System.Net.NetworkCredential class for the specified host,port,and 

    authentication type.

  

  

   host: The host computer that authenticates the client.

   port: The port on the host that the client communicates with.

   authenticationType: The type of authentication requested,as defined in the 

    System.Net.IAuthenticationModule.AuthenticationType property.

  

   Returns: A System.Net.NetworkCredential for the specified host,port,and authentication protocol,or 

    null if there are no credentials available for the specified host,port,and authentication 

    protocol.

  

  GetCredential(self: NetworkCredential,uri: Uri,authType: str) -> NetworkCredential

  

   Returns an instance of the System.Net.NetworkCredential class for the specified Uniform Resource 

    Identifier (URI) and authentication type.

  

  

   uri: The URI that the client provides authentication for.

   authType: The type of authentication requested,as defined in the 

    System.Net.IAuthenticationModule.AuthenticationType property.

  

   Returns: A System.Net.NetworkCredential object.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,userName=None,password=None,domain=None):
  """
  __new__(cls: type)

  __new__(cls: type,userName: str,password: str)

  __new__(cls: type,userName: str,password: SecureString)

  __new__(cls: type,userName: str,password: str,domain: str)

  __new__(cls: type,userName: str,password: SecureString,domain: str)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Domain=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the domain or computer name that verifies the credentials.



Get: Domain(self: NetworkCredential) -> str



Set: Domain(self: NetworkCredential)=value

"""

 Password=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the password for the user name associated with the credentials.



Get: Password(self: NetworkCredential) -> str



Set: Password(self: NetworkCredential)=value

"""

 SecurePassword=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the password as a System.Security.SecureString instance.



Get: SecurePassword(self: NetworkCredential) -> SecureString



Set: SecurePassword(self: NetworkCredential)=value

"""

 UserName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the user name associated with the credentials.



Get: UserName(self: NetworkCredential) -> str



Set: UserName(self: NetworkCredential)=value

"""


