class ICredentialsByHost:
 """ Provides the interface for retrieving credentials for a host,port,and authentication type. """
 def GetCredential(self,host,port,authenticationType):
  """
  GetCredential(self: ICredentialsByHost,host: str,port: int,authenticationType: str) -> NetworkCredential

  

   Returns the credential for the specified host,port,and authentication protocol.

  

   host: The host computer that is authenticating the client.

   port: The port on host that the client will communicate with.

   authenticationType: The authentication protocol.

   Returns: A System.Net.NetworkCredential for the specified host,port,and authentication protocol,or 

    null if there are no credentials available for the specified host,port,and authentication 

    protocol.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
