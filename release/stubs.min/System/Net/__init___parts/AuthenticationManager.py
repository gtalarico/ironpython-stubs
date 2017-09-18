class AuthenticationManager(object):
 """ Manages the authentication modules called during the client authentication process. """
 @staticmethod
 def Authenticate(challenge,request,credentials):
  """
  Authenticate(challenge: str,request: WebRequest,credentials: ICredentials) -> Authorization

  

   Calls each registered authentication module to find the first module that can respond to the 

    authentication request.

  

  

   challenge: The challenge returned by the Internet resource.

   request: The System.Net.WebRequest that initiated the authentication challenge.

   credentials: The System.Net.ICredentials associated with this request.

   Returns: An instance of the System.Net.Authorization class containing the result of the authorization 

    attempt. If there is no authentication module to respond to the challenge,this method returns 

    null.
  """
  pass
 @staticmethod
 def PreAuthenticate(request,credentials):
  """
  PreAuthenticate(request: WebRequest,credentials: ICredentials) -> Authorization

  

   Preauthenticates a request.

  

   request: A System.Net.WebRequest to an Internet resource.

   credentials: The System.Net.ICredentials associated with the request.

   Returns: An instance of the System.Net.Authorization class if the request can be preauthenticated; 

    otherwise,null. If credentials is null,this method returns null.
  """
  pass
 @staticmethod
 def Register(authenticationModule):
  """
  Register(authenticationModule: IAuthenticationModule)

   Registers an authentication module with the authentication manager.

  

   authenticationModule: The System.Net.IAuthenticationModule to register with the authentication manager.
  """
  pass
 @staticmethod
 def Unregister(*__args):
  """
  Unregister(authenticationScheme: str)

   Removes authentication modules with the specified authentication scheme from the list of 

    registered modules.

  

  

   authenticationScheme: The authentication scheme of the module to remove.

  Unregister(authenticationModule: IAuthenticationModule)

   Removes the specified authentication module from the list of registered modules.

  

   authenticationModule: The System.Net.IAuthenticationModule to remove from the list of registered modules.
  """
  pass
 CredentialPolicy=None
 CustomTargetNameDictionary=None
 RegisteredModules=None

