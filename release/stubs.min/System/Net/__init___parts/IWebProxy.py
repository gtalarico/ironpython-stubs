class IWebProxy:
 """ Provides the base interface for implementation of proxy access for the System.Net.WebRequest class. """
 def GetProxy(self,destination):
  """
  GetProxy(self: IWebProxy,destination: Uri) -> Uri

  

   Returns the URI of a proxy.

  

   destination: A System.Uri that specifies the requested Internet resource.

   Returns: A System.Uri instance that contains the URI of the proxy used to contact destination.
  """
  pass
 def IsBypassed(self,host):
  """
  IsBypassed(self: IWebProxy,host: Uri) -> bool

  

   Indicates that the proxy should not be used for the specified host.

  

   host: The System.Uri of the host to check for proxy use.

   Returns: true if the proxy server should not be used for host; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Credentials=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The credentials to submit to the proxy server for authentication.



Get: Credentials(self: IWebProxy) -> ICredentials



Set: Credentials(self: IWebProxy)=value

"""


