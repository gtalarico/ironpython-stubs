class DnsEndPoint(EndPoint):
 """
 Represents a network endpoint as a host name or a string representation of an IP address and a port number.

 

 DnsEndPoint(host: str,port: int)

 DnsEndPoint(host: str,port: int,addressFamily: AddressFamily)
 """
 def Equals(self,comparand):
  """
  Equals(self: DnsEndPoint,comparand: object) -> bool

  

   Compares two System.Net.DnsEndPoint objects.

  

   comparand: A System.Net.DnsEndPoint instance to compare to the current instance.

   Returns: true if the two System.Net.DnsEndPoint instances are equal; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DnsEndPoint) -> int

  

   Returns a hash value for a System.Net.DnsEndPoint.

   Returns: An integer hash value for the System.Net.DnsEndPoint.
  """
  pass
 def ToString(self):
  """
  ToString(self: DnsEndPoint) -> str

  

   Returns the host name or string representation of the IP address and port number of the 

    System.Net.DnsEndPoint.

  

   Returns: A string containing the address family,host name or IP address string,and the port number of 

    the specified System.Net.DnsEndPoint.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,host,port,addressFamily=None):
  """
  __new__(cls: type,host: str,port: int)

  __new__(cls: type,host: str,port: int,addressFamily: AddressFamily)
  """
  pass
 def __ne__(self,*args):
  pass
 AddressFamily=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Internet Protocol (IP) address family.



Get: AddressFamily(self: DnsEndPoint) -> AddressFamily



"""

 Host=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the host name or string representation of the Internet Protocol (IP) address of the host.



Get: Host(self: DnsEndPoint) -> str



"""

 Port=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the port number of the System.Net.DnsEndPoint.



Get: Port(self: DnsEndPoint) -> int



"""


