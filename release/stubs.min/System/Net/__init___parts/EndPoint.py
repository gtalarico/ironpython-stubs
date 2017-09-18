class EndPoint(object):
 """ Identifies a network address. This is an abstract class. """
 def Create(self,socketAddress):
  """
  Create(self: EndPoint,socketAddress: SocketAddress) -> EndPoint

  

   Creates an System.Net.EndPoint instance from a System.Net.SocketAddress instance.

  

   socketAddress: The socket address that serves as the endpoint for a connection.

   Returns: A new System.Net.EndPoint instance that is initialized from the specified 

    System.Net.SocketAddress instance.
  """
  pass
 def Serialize(self):
  """
  Serialize(self: EndPoint) -> SocketAddress

  

   Serializes endpoint information into a System.Net.SocketAddress instance.

   Returns: A System.Net.SocketAddress instance that contains the endpoint information.
  """
  pass
 AddressFamily=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the address family to which the endpoint belongs.



Get: AddressFamily(self: EndPoint) -> AddressFamily



"""


