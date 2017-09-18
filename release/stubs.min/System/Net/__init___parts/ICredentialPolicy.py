class ICredentialPolicy:
 """ Defines the credential policy to be used for resource requests that are made using System.Net.WebRequest and its derived classes. """
 def ShouldSendCredential(self,challengeUri,request,credential,authenticationModule):
  """
  ShouldSendCredential(self: ICredentialPolicy,challengeUri: Uri,request: WebRequest,credential: NetworkCredential,authenticationModule: IAuthenticationModule) -> bool

  

   Returns a System.Boolean that indicates whether the client's credentials are sent with a 

    resource request made using an instance of the System.Net.WebRequest class.

  

  

   challengeUri: The System.Uri that will receive the request. For more information,see the Remarks section.

   request: The System.Net.WebRequest that represents the resource being requested.

   credential: The System.Net.NetworkCredential that will be sent with the request if this method returns true.

   authenticationModule: The System.Net.IAuthenticationModule that will conduct the authentication,if authentication is 

    required.

  

   Returns: true if the credentials are sent with the request; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
