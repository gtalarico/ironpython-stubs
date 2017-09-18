class IPAddress(object):
 """
 Provides an Internet Protocol (IP) address.

 

 IPAddress(newAddress: Int64)

 IPAddress(address: Array[Byte],scopeid: Int64)

 IPAddress(address: Array[Byte])
 """
 def Equals(self,comparand):
  """
  Equals(self: IPAddress,comparand: object) -> bool

  

   Compares two IP addresses.

  

   comparand: An System.Net.IPAddress instance to compare to the current instance.

   Returns: true if the two addresses are equal; otherwise,false.
  """
  pass
 def GetAddressBytes(self):
  """
  GetAddressBytes(self: IPAddress) -> Array[Byte]

  

   Provides a copy of the System.Net.IPAddress as an array of bytes.

   Returns: A System.Byte array.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: IPAddress) -> int

  

   Returns a hash value for an IP address.

   Returns: An integer hash value.
  """
  pass
 @staticmethod
 def HostToNetworkOrder(host):
  """
  HostToNetworkOrder(host: Int16) -> Int16

  

   Converts a short value from host byte order to network byte order.

  

   host: The number to convert,expressed in host byte order.

   Returns: A short value,expressed in network byte order.

  HostToNetworkOrder(host: int) -> int

  

   Converts an integer value from host byte order to network byte order.

  

   host: The number to convert,expressed in host byte order.

   Returns: An integer value,expressed in network byte order.

  HostToNetworkOrder(host: Int64) -> Int64

  

   Converts a long value from host byte order to network byte order.

  

   host: The number to convert,expressed in host byte order.

   Returns: A long value,expressed in network byte order.
  """
  pass
 @staticmethod
 def IsLoopback(address):
  """
  IsLoopback(address: IPAddress) -> bool

  

   Indicates whether the specified IP address is the loopback address.

  

   address: An IP address.

   Returns: true if address is the loopback address; otherwise,false.
  """
  pass
 def MapToIPv4(self):
  """ MapToIPv4(self: IPAddress) -> IPAddress """
  pass
 def MapToIPv6(self):
  """ MapToIPv6(self: IPAddress) -> IPAddress """
  pass
 @staticmethod
 def NetworkToHostOrder(network):
  """
  NetworkToHostOrder(network: Int16) -> Int16

  

   Converts a short value from network byte order to host byte order.

  

   network: The number to convert,expressed in network byte order.

   Returns: A short value,expressed in host byte order.

  NetworkToHostOrder(network: int) -> int

  

   Converts an integer value from network byte order to host byte order.

  

   network: The number to convert,expressed in network byte order.

   Returns: An integer value,expressed in host byte order.

  NetworkToHostOrder(network: Int64) -> Int64

  

   Converts a long value from network byte order to host byte order.

  

   network: The number to convert,expressed in network byte order.

   Returns: A long value,expressed in host byte order.
  """
  pass
 @staticmethod
 def Parse(ipString):
  """
  Parse(ipString: str) -> IPAddress

  

   Converts an IP address string to an System.Net.IPAddress instance.

  

   ipString: A string that contains an IP address in dotted-quad notation for IPv4 and in colon-hexadecimal 

    notation for IPv6.

  

   Returns: An System.Net.IPAddress instance.
  """
  pass
 def ToString(self):
  """
  ToString(self: IPAddress) -> str

  

   Converts an Internet address to its standard notation.

   Returns: A string that contains the IP address in either IPv4 dotted-quad or in IPv6 colon-hexadecimal 

    notation.
  """
  pass
 @staticmethod
 def TryParse(ipString,address):
  """
  TryParse(ipString: str) -> (bool,IPAddress)

  

   Determines whether a string is a valid IP address.

  

   ipString: The string to validate.

   Returns: true if ipString is a valid IP address; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,newAddress: Int64)

  __new__(cls: type,address: Array[Byte],scopeid: Int64)

  __new__(cls: type,address: Array[Byte])
  """
  pass
 def __ne__(self,*args):
  pass
 Address=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """An Internet Protocol (IP) address.



Get: Address(self: IPAddress) -> Int64



Set: Address(self: IPAddress)=value

"""

 AddressFamily=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the address family of the IP address.



Get: AddressFamily(self: IPAddress) -> AddressFamily



"""

 IsIPv4MappedToIPv6=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsIPv4MappedToIPv6(self: IPAddress) -> bool



"""

 IsIPv6LinkLocal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the address is an IPv6 link local address.



Get: IsIPv6LinkLocal(self: IPAddress) -> bool



"""

 IsIPv6Multicast=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the address is an IPv6 multicast global address.



Get: IsIPv6Multicast(self: IPAddress) -> bool



"""

 IsIPv6SiteLocal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the address is an IPv6 site local address.



Get: IsIPv6SiteLocal(self: IPAddress) -> bool



"""

 IsIPv6Teredo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the address is an IPv6 Teredo address.



Get: IsIPv6Teredo(self: IPAddress) -> bool



"""

 ScopeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the IPv6 address scope identifier.



Get: ScopeId(self: IPAddress) -> Int64



Set: ScopeId(self: IPAddress)=value

"""


 Any=None
 Broadcast=None
 IPv6Any=None
 IPv6Loopback=None
 IPv6None=None
 Loopback=None
 None=None

