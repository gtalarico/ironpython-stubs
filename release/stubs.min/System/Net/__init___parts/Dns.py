class Dns(object):
 """ Provides simple domain name resolution functionality. """
 @staticmethod
 def BeginGetHostAddresses(hostNameOrAddress,requestCallback,state):
  """
  BeginGetHostAddresses(hostNameOrAddress: str,requestCallback: AsyncCallback,state: object) -> IAsyncResult

  

   Asynchronously returns the Internet Protocol (IP) addresses for the specified host.

  

   hostNameOrAddress: The host name or IP address to resolve.

   requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is 

    complete.

  

   state: A user-defined object that contains information about the operation. This object is passed to 

    the requestCallback delegate when the operation is complete.

  

   Returns: An System.IAsyncResult instance that references the asynchronous request.
  """
  pass
 @staticmethod
 def BeginGetHostByName(hostName,requestCallback,stateObject):
  """
  BeginGetHostByName(hostName: str,requestCallback: AsyncCallback,stateObject: object) -> IAsyncResult

  

   Begins an asynchronous request for System.Net.IPHostEntry information about the specified DNS 

    host name.

  

  

   hostName: The DNS name of the host.

   requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is 

    complete.

  

   stateObject: A user-defined object that contains information about the operation. This object is passed to 

    the requestCallback delegate when the operation is complete.

  

   Returns: An System.IAsyncResult instance that references the asynchronous request.
  """
  pass
 @staticmethod
 def BeginGetHostEntry(*__args):
  """
  BeginGetHostEntry(address: IPAddress,requestCallback: AsyncCallback,stateObject: object) -> IAsyncResult

  

   Asynchronously resolves an IP address to an System.Net.IPHostEntry instance.

  

   address: The IP address to resolve.

   requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is 

    complete.

  

   stateObject: A user-defined object that contains information about the operation. This object is passed to 

    the requestCallback delegate when the operation is complete.

  

   Returns: An System.IAsyncResult instance that references the asynchronous request.

  BeginGetHostEntry(hostNameOrAddress: str,requestCallback: AsyncCallback,stateObject: object) -> IAsyncResult

  

   Asynchronously resolves a host name or IP address to an System.Net.IPHostEntry instance.

  

   hostNameOrAddress: The host name or IP address to resolve.

   requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is 

    complete.

  

   stateObject: A user-defined object that contains information about the operation. This object is passed to 

    the requestCallback delegate when the operation is complete.

  

   Returns: An System.IAsyncResult instance that references the asynchronous request.
  """
  pass
 @staticmethod
 def BeginResolve(hostName,requestCallback,stateObject):
  """
  BeginResolve(hostName: str,requestCallback: AsyncCallback,stateObject: object) -> IAsyncResult

  

   Begins an asynchronous request to resolve a DNS host name or IP address to an 

    System.Net.IPAddress instance.

  

  

   hostName: The DNS name of the host.

   requestCallback: An System.AsyncCallback delegate that references the method to invoke when the operation is 

    complete.

  

   stateObject: A user-defined object that contains information about the operation. This object is passed to 

    the requestCallback delegate when the operation is complete.

  

   Returns: An System.IAsyncResult instance that references the asynchronous request.
  """
  pass
 @staticmethod
 def EndGetHostAddresses(asyncResult):
  """
  EndGetHostAddresses(asyncResult: IAsyncResult) -> Array[IPAddress]

  

   Ends an asynchronous request for DNS information.

  

   asyncResult: An System.IAsyncResult instance returned by a call to the 

    System.Net.Dns.BeginGetHostAddresses(System.String,System.AsyncCallback,System.Object) method.

  

   Returns: An array of type System.Net.IPAddress that holds the IP addresses for the host specified by the 

    hostNameOrAddress parameter of 

    System.Net.Dns.BeginGetHostAddresses(System.String,System.AsyncCallback,System.Object).
  """
  pass
 @staticmethod
 def EndGetHostByName(asyncResult):
  """
  EndGetHostByName(asyncResult: IAsyncResult) -> IPHostEntry

  

   Ends an asynchronous request for DNS information.

  

   asyncResult: An System.IAsyncResult instance that is returned by a call to the 

    System.Net.Dns.BeginGetHostByName(System.String,System.AsyncCallback,System.Object) method.

  

   Returns: An System.Net.IPHostEntry object that contains DNS information about a host.
  """
  pass
 @staticmethod
 def EndGetHostEntry(asyncResult):
  """
  EndGetHostEntry(asyncResult: IAsyncResult) -> IPHostEntry

  

   Ends an asynchronous request for DNS information.

  

   asyncResult: An System.IAsyncResult instance returned by a call to an erload:System.Net.Dns.BeginGetHostEntry 

    method.

  

   Returns: An System.Net.IPHostEntry instance that contains address information about the host.
  """
  pass
 @staticmethod
 def EndResolve(asyncResult):
  """
  EndResolve(asyncResult: IAsyncResult) -> IPHostEntry

  

   Ends an asynchronous request for DNS information.

  

   asyncResult: An System.IAsyncResult instance that is returned by a call to the 

    System.Net.Dns.BeginResolve(System.String,System.AsyncCallback,System.Object) method.

  

   Returns: An System.Net.IPHostEntry object that contains DNS information about a host.
  """
  pass
 @staticmethod
 def GetHostAddresses(hostNameOrAddress):
  """
  GetHostAddresses(hostNameOrAddress: str) -> Array[IPAddress]

  

   Returns the Internet Protocol (IP) addresses for the specified host.

  

   hostNameOrAddress: The host name or IP address to resolve.

   Returns: An array of type System.Net.IPAddress that holds the IP addresses for the host that is specified 

    by the hostNameOrAddress parameter.
  """
  pass
 @staticmethod
 def GetHostAddressesAsync(hostNameOrAddress):
  """ GetHostAddressesAsync(hostNameOrAddress: str) -> Task[Array[IPAddress]] """
  pass
 @staticmethod
 def GetHostByAddress(address):
  """
  GetHostByAddress(address: IPAddress) -> IPHostEntry

  

   Creates an System.Net.IPHostEntry instance from the specified System.Net.IPAddress.

  

   address: An System.Net.IPAddress.

   Returns: An System.Net.IPHostEntry.

  GetHostByAddress(address: str) -> IPHostEntry

  

   Creates an System.Net.IPHostEntry instance from an IP address.

  

   address: An IP address.

   Returns: An System.Net.IPHostEntry instance.
  """
  pass
 @staticmethod
 def GetHostByName(hostName):
  """
  GetHostByName(hostName: str) -> IPHostEntry

  

   Gets the DNS information for the specified DNS host name.

  

   hostName: The DNS name of the host.

   Returns: An System.Net.IPHostEntry object that contains host information for the address specified in 

    hostName.
  """
  pass
 @staticmethod
 def GetHostEntry(*__args):
  """
  GetHostEntry(address: IPAddress) -> IPHostEntry

  

   Resolves an IP address to an System.Net.IPHostEntry instance.

  

   address: An IP address.

   Returns: An System.Net.IPHostEntry instance that contains address information about the host specified in 

    address.

  

  GetHostEntry(hostNameOrAddress: str) -> IPHostEntry

  

   Resolves a host name or IP address to an System.Net.IPHostEntry instance.

  

   hostNameOrAddress: The host name or IP address to resolve.

   Returns: An System.Net.IPHostEntry instance that contains address information about the host specified in 

    hostNameOrAddress.
  """
  pass
 @staticmethod
 def GetHostEntryAsync(*__args):
  """
  GetHostEntryAsync(hostNameOrAddress: str) -> Task[IPHostEntry]

  GetHostEntryAsync(address: IPAddress) -> Task[IPHostEntry]
  """
  pass
 @staticmethod
 def GetHostName():
  """
  GetHostName() -> str

  

   Gets the host name of the local computer.

   Returns: A string that contains the DNS host name of the local computer.
  """
  pass
 @staticmethod
 def Resolve(hostName):
  """
  Resolve(hostName: str) -> IPHostEntry

  

   Resolves a DNS host name or IP address to an System.Net.IPHostEntry instance.

  

   hostName: A DNS-style host name or IP address.

   Returns: An System.Net.IPHostEntry instance that contains address information about the host specified in 

    hostName.
  """
  pass
 __all__=[
  'BeginGetHostAddresses',
  'BeginGetHostByName',
  'BeginGetHostEntry',
  'BeginResolve',
  'EndGetHostAddresses',
  'EndGetHostByName',
  'EndGetHostEntry',
  'EndResolve',
  'GetHostAddresses',
  'GetHostAddressesAsync',
  'GetHostByAddress',
  'GetHostByName',
  'GetHostEntry',
  'GetHostEntryAsync',
  'GetHostName',
  'Resolve',
 ]

