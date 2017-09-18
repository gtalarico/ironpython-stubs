class ICredentials:
 """ Provides the base authentication interface for retrieving credentials for Web client authentication. """
 def GetCredential(self,uri,authType):
  """
  GetCredential(self: ICredentials,uri: Uri,authType: str) -> NetworkCredential

  

   Returns a System.Net.NetworkCredential object that is associated with the specified URI,and 

    authentication type.

  

  

   uri: The System.Uri that the client is providing authentication for.

   authType: The type of authentication,as defined in the 

    System.Net.IAuthenticationModule.AuthenticationType property.

  

   Returns: The System.Net.NetworkCredential that is associated with the specified URI and authentication 

    type,or,if no credentials are available,null.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
