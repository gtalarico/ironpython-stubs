class ServicePointManager(object):
 """ Manages the collection of System.Net.ServicePoint objects. """
 @staticmethod
 def FindServicePoint(*__args):
  """
  FindServicePoint(address: Uri,proxy: IWebProxy) -> ServicePoint

  

   Finds an existing System.Net.ServicePoint object or creates a new System.Net.ServicePoint object 

    to manage communications with the specified System.Uri object.

  

  

   address: A System.Uri object that contains the address of the Internet resource to contact.

   proxy: The proxy data for this request.

   Returns: The System.Net.ServicePoint object that manages communications for the request.

  FindServicePoint(uriString: str,proxy: IWebProxy) -> ServicePoint

  

   Finds an existing System.Net.ServicePoint object or creates a new System.Net.ServicePoint object 

    to manage communications with the specified Uniform Resource Identifier (URI).

  

  

   uriString: The URI of the Internet resource to be contacted.

   proxy: The proxy data for this request.

   Returns: The System.Net.ServicePoint object that manages communications for the request.

  FindServicePoint(address: Uri) -> ServicePoint

  

   Finds an existing System.Net.ServicePoint object or creates a new System.Net.ServicePoint object 

    to manage communications with the specified System.Uri object.

  

  

   address: The System.Uri object of the Internet resource to contact.

   Returns: The System.Net.ServicePoint object that manages communications for the request.
  """
  pass
 @staticmethod
 def SetTcpKeepAlive(enabled,keepAliveTime,keepAliveInterval):
  """
  SetTcpKeepAlive(enabled: bool,keepAliveTime: int,keepAliveInterval: int)

   Enables or disables the keep-alive option on a TCP connection.

  

   enabled: If set to true,then the TCP keep-alive option on a TCP connection will be enabled using the 

    specified keepAliveTime and keepAliveInterval values. If set to false,then the TCP keep-alive 

    option is disabled and the remaining parameters are ignored.The default value is false.

  

   keepAliveTime: Specifies the timeout,in milliseconds,with no activity until the first keep-alive packet is 

    sent.The value must be greater than 0.  If a value of less than or equal to zero is passed an 

    System.ArgumentOutOfRangeException is thrown.

  

   keepAliveInterval: Specifies the interval,in milliseconds,between when successive keep-alive packets are sent if 

    no acknowledgement is received.The value must be greater than 0.  If a value of less than or 

    equal to zero is passed an System.ArgumentOutOfRangeException is thrown.
  """
  pass
 CertificatePolicy=None
 CheckCertificateRevocationList=False
 DefaultConnectionLimit=2
 DefaultNonPersistentConnectionLimit=4
 DefaultPersistentConnectionLimit=2
 DnsRefreshTimeout=120000
 EnableDnsRoundRobin=False
 EncryptionPolicy=None
 Expect100Continue=True
 MaxServicePointIdleTime=100000
 MaxServicePoints=0
 ReusePort=False
 SecurityProtocol=None
 ServerCertificateValidationCallback=None
 UseNagleAlgorithm=True

