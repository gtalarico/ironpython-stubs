class EndpointPermission(object):
 """ Defines an endpoint that is authorized by a System.Net.SocketPermission instance. """
 def Equals(self,obj):
  """
  Equals(self: EndpointPermission,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to the current 

    System.Net.SocketPermission instance.

  

  

   obj: The specified System.Object

   Returns: true if the specified System.Object is equal to the current System.Object; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: EndpointPermission) -> int

  

   Serves as a hash function for a particular System.Net.SocketPermission instance.

   Returns: A hash code for the current System.Object.
  """
  pass
 def ToString(self):
  """
  ToString(self: EndpointPermission) -> str

  

   Returns a string that represents the current System.Net.EndpointPermission instance.

   Returns: A string that represents the current System.Net.EndpointPermission instance.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 Hostname=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the DNS host name or IP address of the server that is associated with this endpoint.



Get: Hostname(self: EndpointPermission) -> str



"""

 Port=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the network port number that is associated with this endpoint.



Get: Port(self: EndpointPermission) -> int



"""

 Transport=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the transport type that is associated with this endpoint.



Get: Transport(self: EndpointPermission) -> TransportType



"""


