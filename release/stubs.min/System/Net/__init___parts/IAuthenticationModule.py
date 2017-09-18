class IAuthenticationModule:
 """ Provides the base authentication interface for Web client authentication modules. """
 def Authenticate(self,challenge,request,credentials):
  """
  Authenticate(self: IAuthenticationModule,challenge: str,request: WebRequest,credentials: ICredentials) -> Authorization

  

   Returns an instance of the System.Net.Authorization class in respose to an authentication 

    challenge from a server.

  

  

   challenge: The authentication challenge sent by the server.

   request: The System.Net.WebRequest instance associated with the challenge.

   credentials: The credentials associated with the challenge.

   Returns: An System.Net.Authorization instance containing the authorization message for the request,or 

    null if the challenge cannot be handled.
  """
  pass
 def PreAuthenticate(self,request,credentials):
  """
  PreAuthenticate(self: IAuthenticationModule,request: WebRequest,credentials: ICredentials) -> Authorization

  

   Returns an instance of the System.Net.Authorization class for an authentication request to a 

    server.

  

  

   request: The System.Net.WebRequest instance associated with the authentication request.

   credentials: The credentials associated with the authentication request.

   Returns: An System.Net.Authorization instance containing the authorization message for the request.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 AuthenticationType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the authentication type provided by this authentication module.



Get: AuthenticationType(self: IAuthenticationModule) -> str



"""

 CanPreAuthenticate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the authentication module supports preauthentication.



Get: CanPreAuthenticate(self: IAuthenticationModule) -> bool



"""


