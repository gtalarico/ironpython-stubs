class CredentialCache(object,ICredentials,ICredentialsByHost,IEnumerable):
 """
 Provides storage for multiple credentials.

 

 CredentialCache()
 """
 def Add(self,*__args):
  """
  Add(self: CredentialCache,host: str,port: int,authenticationType: str,credential: NetworkCredential)

   Adds a System.Net.NetworkCredential instance for use with SMTP to the credential cache and 

    associates it with a host computer,port,and authentication protocol. Credentials added using 

    this method are valid for SMTP only. This method does not work for HTTP or FTP requests.

  

  

   host: A System.String that identifies the host computer.

   port: A System.Int32 that specifies the port to connect to on host.

   authenticationType: A System.String that identifies the authentication scheme used when connecting to host using 

    cred. See Remarks.

  

   credential: The System.Net.NetworkCredential to add to the credential cache.

  Add(self: CredentialCache,uriPrefix: Uri,authType: str,cred: NetworkCredential)

   Adds a System.Net.NetworkCredential instance to the credential cache for use with protocols 

    other than SMTP and associates it with a Uniform Resource Identifier (URI) prefix and 

    authentication protocol.

  

  

   uriPrefix: A System.Uri that specifies the URI prefix of the resources that the credential grants access to.

   authType: The authentication scheme used by the resource named in uriPrefix.

   cred: The System.Net.NetworkCredential to add to the credential cache.
  """
  pass
 def GetCredential(self,*__args):
  """
  GetCredential(self: CredentialCache,host: str,port: int,authenticationType: str) -> NetworkCredential

  

   Returns the System.Net.NetworkCredential instance associated with the specified host,port,and 

    authentication protocol.

  

  

   host: A System.String that identifies the host computer.

   port: A System.Int32 that specifies the port to connect to on host.

   authenticationType: A System.String that identifies the authentication scheme used when connecting to host. See 

    Remarks.

  

   Returns: A System.Net.NetworkCredential or,if there is no matching credential in the cache,null.

  GetCredential(self: CredentialCache,uriPrefix: Uri,authType: str) -> NetworkCredential

  

   Returns the System.Net.NetworkCredential instance associated with the specified Uniform Resource 

    Identifier (URI) and authentication type.

  

  

   uriPrefix: A System.Uri that specifies the URI prefix of the resources that the credential grants access to.

   authType: The authentication scheme used by the resource named in uriPrefix.

   Returns: A System.Net.NetworkCredential or,if there is no matching credential in the cache,null.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: CredentialCache) -> IEnumerator

  

   Returns an enumerator that can iterate through the System.Net.CredentialCache instance.

   Returns: An System.Collections.IEnumerator for the System.Net.CredentialCache.
  """
  pass
 def Remove(self,*__args):
  """
  Remove(self: CredentialCache,host: str,port: int,authenticationType: str)

   Deletes a System.Net.NetworkCredential instance from the cache if it is associated with the 

    specified host,port,and authentication protocol.

  

  

   host: A System.String that identifies the host computer.

   port: A System.Int32 that specifies the port to connect to on host.

   authenticationType: A System.String that identifies the authentication scheme used when connecting to host. See 

    Remarks.

  

  Remove(self: CredentialCache,uriPrefix: Uri,authType: str)

   Deletes a System.Net.NetworkCredential instance from the cache if it is associated with the 

    specified Uniform Resource Identifier (URI) prefix and authentication protocol.

  

  

   uriPrefix: A System.Uri that specifies the URI prefix of the resources that the credential is used for.

   authType: The authentication scheme used by the host named in uriPrefix.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 DefaultCredentials=None
 DefaultNetworkCredentials=None

