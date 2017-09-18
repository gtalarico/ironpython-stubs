class IPEndPoint(EndPoint):
 """
 Represents a network endpoint as an IP address and a port number.

 

 IPEndPoint(address: Int64,port: int)

 IPEndPoint(address: IPAddress,port: int)
 """
 def Create(self,socketAddress):
  """
  Create(self: IPEndPoint,socketAddress: SocketAddress) -> EndPoint

  

   Creates an endpoint from a socket address.

  

   socketAddress: The System.Net.SocketAddress to use for the endpoint.

   Returns: An System.Net.EndPoint instance using the specified socket address.
  """
  pass
 def Equals(self,comparand):
  """
  Equals(self: IPEndPoint,comparand: object) -> bool

  

   Determines whether the specified System.Object is equal to the current System.Net.IPEndPoint 

    instance.

  

  

   comparand: The specified System.Object to compare with the current System.Net.IPEndPoint instance.

   Returns: true if the specified System.Object is equal to the current System.Object; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: IPEndPoint) -> int

  

   Returns a hash value for a System.Net.IPEndPoint instance.

   Returns: An integer hash value.
  """
  pass
 def Serialize(self):
  """
  Serialize(self: IPEndPoint) -> SocketAddress

  

   Serializes endpoint information into a System.Net.SocketAddress instance.

   Returns: A System.Net.SocketAddress instance containing the socket address for the endpoint.
  """
  pass
 def ToString(self):
  """
  ToString(self: IPEndPoint) -> str

  

   Returns the IP address and port number of the specified endpoint.

   Returns: A string containing the IP address and the port number of the specified endpoint (for example,

    192.168.1.2:80).
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,address,port):
  """
  __new__(cls: type,address: Int64,port: int)

  __new__(cls: type,address: IPAddress,port: int)
  """
  pass
 def __ne__(self,*args):
  pass
 Address=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the IP address of the endpoint.



Get: Address(self: IPEndPoint) -> IPAddress



Set: Address(self: IPEndPoint)=value

"""

 AddressFamily=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Internet Protocol (IP) address family.



Get: AddressFamily(self: IPEndPoint) -> AddressFamily



"""

 Port=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the port number of the endpoint.



Get: Port(self: IPEndPoint) -> int



Set: Port(self: IPEndPoint)=value

"""


 MaxPort=65535
 MinPort=0

